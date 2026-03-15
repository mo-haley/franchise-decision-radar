#!/usr/bin/env python3
"""
build_pdf_inventory.py

Scans a folder of downloaded FDD PDFs and produces a structured inventory
with file metadata, page counts, and heuristic section-boundary detection.

Does NOT extract franchise data (Item 5/7/19/20). This is a pre-extraction
inventory and normalization layer.

Usage:
    python scripts/build_pdf_inventory.py [--input-dir data/raw] [--output-dir data/derived]
"""

import argparse
import csv
import hashlib
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import pdfplumber

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants: heuristic patterns for section detection
# ---------------------------------------------------------------------------

# Each pattern maps to a section label.  Order matters — first match wins
# when classifying a page's *primary* role.
SECTION_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("state_addendum", re.compile(
        r"(?i)(state[\s\-]*specific\s+addend|addendum\s+to\s+the\s+franchise\s+"
        r"disclosure\s+document|state\s+of\s+california|state\s+of\s+wisconsin|"
        r"state\s+of\s+minnesota|state\s+of\s+maryland|state\s+of\s+new\s+york|"
        r"state\s+effective\s+dates)"
    )),
    ("receipt", re.compile(
        r"(?i)(receipt\s*$|receipt\s+page|acknowledge\s+receipt\s+of|"
        r"keep\s+this\s+copy|return\s+this\s+copy|detach\s+and\s+retain)"
    )),
    ("exhibit", re.compile(
        r"(?i)^[\s]*exhibit\s+[a-z0-9]"
    )),
    ("table_of_contents", re.compile(
        r"(?i)(table\s+of\s+contents|^\s*contents\s*$)"
    )),
    ("cover_page", re.compile(
        r"(?i)(franchise\s+disclosure\s+document\s*$|"
        r"franchise\s+disclosure\s+document\s*\n)"
    )),
    ("item_page", re.compile(
        r"(?i)^\s*item\s+\d{1,2}[\.\s]"
    )),
]

# Items we care about for downstream extraction — just detect presence
ITEM_HEADER_RE = re.compile(
    r"(?i)(?:^|\n)\s*item\s+(\d{1,2})\b"
)

PDF_MAGIC = b"%PDF"


def sha256_file(path: Path) -> str:
    """Return hex SHA-256 digest of file contents."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def is_valid_pdf(path: Path) -> bool:
    """Check if file starts with the PDF magic bytes."""
    try:
        with open(path, "rb") as f:
            header = f.read(8)
        return header[:4] == PDF_MAGIC
    except OSError:
        return False


def classify_page(text: str) -> list[str]:
    """Return list of section labels that match the page text."""
    labels: list[str] = []
    for label, pattern in SECTION_PATTERNS:
        if pattern.search(text):
            labels.append(label)
    return labels


def detect_items_on_page(text: str) -> list[int]:
    """Return sorted list of Item numbers found on the page."""
    return sorted(set(int(m.group(1)) for m in ITEM_HEADER_RE.finditer(text)))


def extract_page_text_safe(page: Any) -> str:
    """Extract text from a pdfplumber page, returning '' on failure."""
    try:
        text = page.extract_text() or ""
        return text
    except Exception as exc:
        log.warning("  Failed to extract text from page %s: %s", page.page_number, exc)
        return ""


def build_page_map(pdf_path: Path) -> dict:
    """
    Open a PDF with pdfplumber, scan every page, and return a dict with:
      - page_count
      - pdf_metadata (from the PDF info dict)
      - pages: list of per-page dicts with classification info
      - section_ranges: estimated page ranges per detected section type
      - items_detected: list of Item numbers found anywhere in the document
    """
    result: dict[str, Any] = {
        "page_count": 0,
        "pdf_metadata": {},
        "pages": [],
        "section_ranges": {},
        "items_detected": [],
    }

    try:
        pdf = pdfplumber.open(pdf_path)
    except Exception as exc:
        log.error("  pdfplumber could not open %s: %s", pdf_path.name, exc)
        result["error"] = str(exc)
        return result

    with pdf:
        result["page_count"] = len(pdf.pages)
        result["pdf_metadata"] = {
            k: str(v) for k, v in (pdf.metadata or {}).items()
        }

        all_items: set[int] = set()
        section_pages: dict[str, list[int]] = {}

        for page in pdf.pages:
            page_num = page.page_number  # 1-indexed
            text = extract_page_text_safe(page)
            labels = classify_page(text)
            items = detect_items_on_page(text)
            all_items.update(items)

            page_info: dict[str, Any] = {
                "page": page_num,
                "labels": labels,
                "items": items,
                "text_length": len(text),
            }
            result["pages"].append(page_info)

            for label in labels:
                section_pages.setdefault(label, []).append(page_num)

        # Build contiguous ranges from page lists
        for label, pages in section_pages.items():
            pages_sorted = sorted(pages)
            ranges = _collapse_to_ranges(pages_sorted)
            result["section_ranges"][label] = ranges

        result["items_detected"] = sorted(all_items)

    return result


def _collapse_to_ranges(pages: list[int]) -> list[dict[str, int]]:
    """Collapse a sorted list of page numbers into contiguous range dicts."""
    if not pages:
        return []
    ranges: list[dict[str, int]] = []
    start = pages[0]
    end = pages[0]
    for p in pages[1:]:
        if p == end + 1:
            end = p
        else:
            ranges.append({"start": start, "end": end})
            start = p
            end = p
    ranges.append({"start": start, "end": end})
    return ranges


def estimate_core_fdd_range(page_map: dict) -> Optional[dict[str, int]]:
    """
    Heuristic: the core FDD runs from the first page with an Item header
    through the last page with an Item header (before addenda start).
    Returns {"start": N, "end": M} or None.
    """
    item_pages = [
        p["page"] for p in page_map["pages"]
        if p["items"] and "state_addendum" not in p["labels"]
    ]
    if not item_pages:
        return None
    return {"start": min(item_pages), "end": max(item_pages)}


def process_one_pdf(pdf_path: Path) -> dict[str, Any]:
    """Build complete inventory record for a single PDF."""
    log.info("Processing: %s", pdf_path.name)

    record: dict[str, Any] = {
        "filename": pdf_path.name,
        "filepath": str(pdf_path.resolve()),
        "file_size_bytes": pdf_path.stat().st_size,
        "is_valid_pdf": False,
        "sha256": None,
        "scan_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    if not is_valid_pdf(pdf_path):
        log.error("  NOT a valid PDF: %s", pdf_path.name)
        record["error"] = "File does not begin with PDF magic bytes"
        return record

    record["is_valid_pdf"] = True
    record["sha256"] = sha256_file(pdf_path)

    page_map = build_page_map(pdf_path)
    record["page_count"] = page_map["page_count"]
    record["pdf_metadata"] = page_map["pdf_metadata"]
    record["section_ranges"] = page_map["section_ranges"]
    record["items_detected"] = page_map["items_detected"]
    record["core_fdd_range_estimate"] = estimate_core_fdd_range(page_map)

    if "error" in page_map:
        record["error"] = page_map["error"]

    # Per-page detail kept in full JSON but excluded from CSV summary
    record["pages"] = page_map["pages"]

    # Confidence / uncertainty flags
    flags: list[str] = []
    if not page_map["items_detected"]:
        flags.append("NO_ITEM_HEADERS_FOUND")
    if "state_addendum" not in page_map["section_ranges"]:
        flags.append("NO_STATE_ADDENDUM_DETECTED")
    if "receipt" not in page_map["section_ranges"]:
        flags.append("NO_RECEIPT_DETECTED")
    if page_map["page_count"] < 50:
        flags.append("UNUSUALLY_SHORT_DOCUMENT")
    record["flags"] = flags

    if flags:
        log.warning("  Flags for %s: %s", pdf_path.name, ", ".join(flags))

    log.info(
        "  Done: %d pages, %d items detected, %d section types found",
        record["page_count"],
        len(record["items_detected"]),
        len(record["section_ranges"]),
    )
    return record


def write_csv_summary(records: list[dict], output_path: Path) -> None:
    """Write a flat CSV with one row per PDF (no per-page detail)."""
    fieldnames = [
        "filename", "file_size_bytes", "is_valid_pdf", "sha256",
        "page_count", "items_detected", "section_types",
        "core_fdd_start", "core_fdd_end", "flags", "scan_timestamp",
    ]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rec in records:
            core = rec.get("core_fdd_range_estimate") or {}
            row = {
                "filename": rec["filename"],
                "file_size_bytes": rec["file_size_bytes"],
                "is_valid_pdf": rec["is_valid_pdf"],
                "sha256": rec.get("sha256", ""),
                "page_count": rec.get("page_count", ""),
                "items_detected": ";".join(str(i) for i in rec.get("items_detected", [])),
                "section_types": ";".join(rec.get("section_ranges", {}).keys()),
                "core_fdd_start": core.get("start", ""),
                "core_fdd_end": core.get("end", ""),
                "flags": ";".join(rec.get("flags", [])),
                "scan_timestamp": rec.get("scan_timestamp", ""),
            }
            writer.writerow(row)
    log.info("CSV summary written to %s", output_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build PDF inventory from downloaded FDD files."
    )
    parser.add_argument(
        "--input-dir", type=Path, default=Path("data/raw"),
        help="Directory containing downloaded FDD PDFs (default: data/raw)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("data/derived"),
        help="Directory for output files (default: data/derived)",
    )
    args = parser.parse_args()

    input_dir: Path = args.input_dir
    output_dir: Path = args.output_dir

    if not input_dir.is_dir():
        log.error("Input directory does not exist: %s", input_dir)
        sys.exit(1)

    pdf_files = sorted(input_dir.glob("*.pdf"))
    if not pdf_files:
        log.error("No .pdf files found in %s", input_dir)
        sys.exit(1)

    log.info("Found %d PDF files in %s", len(pdf_files), input_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    for pdf_path in pdf_files:
        record = process_one_pdf(pdf_path)
        records.append(record)

    # Write JSON inventory (full detail including per-page data)
    json_path = output_dir / "pdf_inventory.json"
    with open(json_path, "w") as f:
        json.dump(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "input_directory": str(input_dir.resolve()),
                "file_count": len(records),
                "files": records,
            },
            f,
            indent=2,
        )
    log.info("JSON inventory written to %s", json_path)

    # Write CSV summary
    csv_path = output_dir / "pdf_inventory.csv"
    write_csv_summary(records, csv_path)

    # Print quick summary
    valid = sum(1 for r in records if r["is_valid_pdf"])
    flagged = sum(1 for r in records if r.get("flags"))
    print(f"\n{'='*60}")
    print(f"PDF Inventory Complete")
    print(f"  Total files:  {len(records)}")
    print(f"  Valid PDFs:   {valid}")
    print(f"  Flagged:      {flagged}")
    print(f"  JSON output:  {json_path}")
    print(f"  CSV output:   {csv_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
