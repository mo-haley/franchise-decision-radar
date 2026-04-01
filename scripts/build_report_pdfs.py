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

# Must stay in sync with PDF_TOKENS in build_site.py
PDF_TOKENS: dict[str, str] = {
    "mosquito-authority": "67951af91d92",
    "mosquito-hunters": "0282031c5464",
    "mosquito-joe": "305b54c8d68e",
    "mosquito-shield": "cab728a38e88",
    "mosquito-squad": "650687ba7092",
    "lawn-doctor": "26b857676f46",
    "spring-green": "18f0b7ec9fd1",
    "naturalawn": "35baa1a22a8f",
    "cleaning-authority": "ec7fe8faeb02",
    "two-maids": "3075f3ec1829",
    "molly-maid": "732768ef2571",
    "the-maids": "868de7c0f67e",
    "merry-maids": "04c86de4ccd0",
    "maidpro": "7e1cc4a53938",
    "maid-right": "0056b5989dca",
}

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

            # Remove old un-tokenized PDF if it exists
            old_pdf = REPORTS_PDF / f"{slug}-decision-report.pdf"
            if old_pdf.exists():
                old_pdf.unlink()
                print(f"    Removed old: {old_pdf.name}")

            token = PDF_TOKENS.get(slug, "")
            pdf_name = (
                f"{slug}-decision-report-{token}.pdf"
                if token
                else f"{slug}-decision-report.pdf"
            )
            pdf_path = REPORTS_PDF / pdf_name
            file_url = html_path.resolve().as_uri()

            print(f"  Converting: {html_path.name}")
            page.goto(file_url, wait_until="networkidle")
            page.pdf(
                path=str(pdf_path),
                format="Letter",
                margin={"top": "0.75in", "bottom": "0.9in", "left": "0.75in", "right": "0.75in"},
                print_background=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=(
                    '<div style="width:100%; text-align:center; font-size:8px;'
                    ' font-family:-apple-system,Helvetica,sans-serif; color:#999;">'
                    '<span class="pageNumber"></span></div>'
                ),
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
