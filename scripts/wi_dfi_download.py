"""
Wisconsin DFI FDD Batch Downloader

Downloads FDD PDFs from the Wisconsin DFI Franchise Search portal
using Playwright (headless Chromium). Computes SHA-256 and logs to CSV.

Usage:
    python scripts/wi_dfi_download.py                          # all 5 brands
    python scripts/wi_dfi_download.py mosquito-hunters         # single brand
    python scripts/wi_dfi_download.py mosquito-joe mosquito-squad  # specific brands
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Configuration ---

PORTAL_URL = "https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx"
BRANDS_FILE = Path("scripts/wi_brands.json")
RAW_DIR = Path("data/raw")
DOWNLOAD_LOG = RAW_DIR / "download_log.csv"
TIMEOUT_MS = 30_000


def sha256_file(path: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def append_log_row(
    brand_slug: str,
    filing_year: str,
    source: str,
    entity_searched: str,
    download_url: str,
    local_filename: str,
    sha256: str,
    notes: str,
) -> None:
    """Append a row to the download log CSV."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    row = [
        brand_slug,
        filing_year,
        source,
        entity_searched,
        download_url,
        local_filename,
        sha256,
        timestamp,
        notes,
    ]
    with open(DOWNLOAD_LOG, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def load_brands(filter_slugs: list[str] | None = None) -> list[dict]:
    """Load brand definitions from wi_brands.json, optionally filtered."""
    with open(BRANDS_FILE) as f:
        brands = json.load(f)
    if filter_slugs:
        known = {b["brand_slug"] for b in brands}
        for slug in filter_slugs:
            if slug not in known:
                print(f"ERROR: Unknown brand slug '{slug}'. Known: {sorted(known)}")
                sys.exit(1)
        brands = [b for b in brands if b["brand_slug"] in filter_slugs]
    return brands


def download_one(page, brand: dict) -> dict:
    """Download one FDD PDF for a single brand. Returns result dict.

    Uses an existing Playwright page (caller manages browser lifecycle).
    Navigates to search portal fresh for each brand.
    """
    slug = brand["brand_slug"]
    search_term = brand["search_term"]
    expected = brand["expected_entity"]

    print(f"\n{'='*60}")
    print(f"  BRAND: {slug}")
    print(f"  Search: '{search_term}'  Match: '{expected}'")
    print(f"{'='*60}")

    # Step 1: Navigate to search portal
    print(f"[1/7] Navigating to portal")
    page.goto(PORTAL_URL, timeout=TIMEOUT_MS)
    page.wait_for_load_state("networkidle")

    # Step 2: Search
    print(f"[2/7] Searching for '{search_term}'")
    page.locator("#txtName").fill(search_term)
    page.locator("#btnSearch").click()
    page.wait_for_load_state("networkidle")

    # Step 3: Find the correct result row
    # The results table has rows with: filing ID, legal name, trade name(s)
    # We match on expected_entity appearing anywhere in the row text.
    # For multi-result searches (e.g. Main Line Brands), this disambiguates.
    print(f"[3/7] Looking for result matching '{expected}'")

    target_link = None

    # First pass: scan <a> tags for a direct match with detail link
    result_links = page.locator("a")
    for i in range(result_links.count()):
        link = result_links.nth(i)
        text = link.text_content() or ""
        href = link.get_attribute("href") or ""
        if expected.lower() in text.lower() and "details" in href.lower():
            print(f"  Direct link match: '{text.strip()}'")
            target_link = link
            break

    # Second pass: scan table rows
    if target_link is None:
        rows = page.locator("tr")
        for i in range(rows.count()):
            row_text = rows.nth(i).text_content() or ""
            if expected.lower() in row_text.lower():
                row_link = rows.nth(i).locator("a").first
                if row_link.count() > 0:
                    print(f"  Row match: {row_text.strip()[:80]}")
                    target_link = row_link
                    break

    if target_link is None:
        raise RuntimeError(
            f"No result matching '{expected}' found for search '{search_term}'. "
            f"Page may have changed or brand is no longer registered."
        )

    # Step 4: Click through to detail page
    print("[4/7] Opening detail page")
    target_link.click()
    page.wait_for_load_state("networkidle")
    detail_url = page.url
    print(f"  URL: {detail_url}")

    # Confirm the detail page has the expected entity in its text
    detail_text = page.locator("body").text_content() or ""
    if expected.lower() not in detail_text.lower():
        raise RuntimeError(
            f"Detail page does not contain '{expected}'. "
            f"May have clicked wrong result. URL: {detail_url}"
        )

    # Step 5: Find download button
    print("[5/7] Looking for FDD download button")
    download_btn = page.locator("#upload_downloadFile")
    if download_btn.count() == 0:
        raise RuntimeError(
            f"No download button found on detail page. URL: {detail_url}"
        )

    upload_info = page.locator("#upload_fileUploadInformation")
    upload_text = ""
    if upload_info.count() > 0:
        upload_text = upload_info.text_content().strip()
        print(f"  {upload_text}")

    # Step 6: Download
    print("[6/7] Downloading PDF")
    with page.expect_download(timeout=60_000) as download_info:
        download_btn.click()
    download = download_info.value

    # Detect filing year from detail page
    year_matches = re.findall(r"20[12]\d", detail_text)
    filing_year = max(year_matches) if year_matches else "unknown"
    print(f"  Filing year: {filing_year}")

    # Save
    local_filename = f"{slug}_{filing_year}_wi_auto.pdf"
    local_path = RAW_DIR / local_filename
    download.save_as(str(local_path))
    file_size = local_path.stat().st_size
    print(f"  Saved: {local_path} ({file_size:,} bytes)")

    if file_size < 10_000:
        raise RuntimeError(
            f"File suspiciously small ({file_size} bytes). May not be a real PDF."
        )

    # Step 7: SHA-256 and log
    print("[7/7] SHA-256 and logging")
    sha = sha256_file(local_path)
    print(f"  SHA-256: {sha}")

    append_log_row(
        brand_slug=slug,
        filing_year=filing_year,
        source="WI_DFI",
        entity_searched=search_term,
        download_url=detail_url,
        local_filename=local_filename,
        sha256=sha,
        notes=f"Automated batch download. {upload_text}",
    )

    # Compare with manual download if available
    manual_path = RAW_DIR / f"{slug}_{filing_year}_wi.pdf"
    hash_match = None
    if manual_path.exists():
        manual_sha = sha256_file(manual_path)
        hash_match = manual_sha == sha
        if hash_match:
            print(f"  HASH MATCH with manual download")
        else:
            print(f"  HASH MISMATCH: auto={sha[:16]}... manual={manual_sha[:16]}...")

    return {
        "brand_slug": slug,
        "filing_year": filing_year,
        "filename": local_filename,
        "sha256": sha,
        "size_bytes": file_size,
        "detail_url": detail_url,
        "hash_match": hash_match,
    }


def main() -> None:
    """Batch download FDDs for Wisconsin brands."""
    filter_slugs = sys.argv[1:] if len(sys.argv) > 1 else None
    brands = load_brands(filter_slugs)

    print(f"Wisconsin DFI batch download: {len(brands)} brand(s)")
    for b in brands:
        print(f"  - {b['brand_slug']}")

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        for brand in brands:
            try:
                result = download_one(page, brand)
                results.append(result)
            except Exception as e:
                slug = brand["brand_slug"]
                print(f"\n  FAILED: {slug} — {e}")
                errors.append({"brand_slug": slug, "error": str(e)})

        browser.close()

    # Summary
    print(f"\n{'='*60}")
    print(f"  BATCH COMPLETE")
    print(f"{'='*60}")
    print(f"  Succeeded: {len(results)}/{len(brands)}")
    for r in results:
        match_str = ""
        if r["hash_match"] is True:
            match_str = " [hash match]"
        elif r["hash_match"] is False:
            match_str = " [hash mismatch]"
        print(f"    OK  {r['brand_slug']} — {r['filename']} ({r['size_bytes']:,} bytes){match_str}")

    if errors:
        print(f"  Failed: {len(errors)}/{len(brands)}")
        for e in errors:
            print(f"    FAIL  {e['brand_slug']} — {e['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
