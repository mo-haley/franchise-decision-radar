#!/usr/bin/env python3
"""
Convert HTML decision reports to PDF for deployment.

Reads rendered HTML reports from reports/ and generates PDFs
in site/reports/ using Playwright (headless Chromium).

Usage:
    python scripts/build_report_pdfs.py          # all brands
    python scripts/build_report_pdfs.py mosquito-joe  # single brand

Requires: playwright with chromium browser installed
    pip install playwright && playwright install chromium
"""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent.parent
REPORTS_HTML = ROOT / "reports"
REPORTS_PDF = ROOT / "site" / "reports"

BRAND_SLUGS = [
    # Mosquito
    "mosquito-authority",
    "mosquito-hunters",
    "mosquito-joe",
    "mosquito-shield",
    "mosquito-squad",
    # Lawn
    "lawn-doctor",
    "spring-green",
    "naturalawn",
    # Cleaning
    "cleaning-authority",
    "two-maids",
    "molly-maid",
    "the-maids",
    "merry-maids",
    "maidpro",
    "maid-right",
]


def build_pdfs(slugs: list[str]) -> None:
    """Convert HTML reports to PDF using headless Chromium."""
    REPORTS_PDF.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for slug in slugs:
            html_path = REPORTS_HTML / f"{slug}-decision-report.html"
            if not html_path.exists():
                print(f"  SKIP: {html_path.name} (not found — run generate_report.py first)")
                continue

            pdf_path = REPORTS_PDF / f"{slug}-decision-report.pdf"
            file_url = html_path.resolve().as_uri()

            print(f"  Converting: {html_path.name}")
            page.goto(file_url, wait_until="networkidle")
            page.pdf(
                path=str(pdf_path),
                format="Letter",
                margin={"top": "0.75in", "bottom": "0.75in", "left": "0.75in", "right": "0.75in"},
                print_background=True,
            )
            size_kb = pdf_path.stat().st_size / 1024
            print(f"    → {pdf_path.relative_to(ROOT)} ({size_kb:.0f} KB)")

        browser.close()


def main() -> None:
    """Build PDFs for all brands or a single specified brand."""
    if len(sys.argv) > 1:
        slug = sys.argv[1]
        if slug not in BRAND_SLUGS:
            print(f"Unknown brand: {slug}")
            print(f"Available: {', '.join(BRAND_SLUGS)}")
            sys.exit(1)
        build_pdfs([slug])
    else:
        print("Building report PDFs...")
        build_pdfs(BRAND_SLUGS)
        print(f"\nDone. PDFs written to site/reports/.")


if __name__ == "__main__":
    main()
