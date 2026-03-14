# Franchise Decision Radar

## About This Project

A tool that downloads Franchise Disclosure Documents (FDDs) from public state
government databases, extracts structured data from the PDFs, and generates
a static website presenting franchise comparison data for prospective investors.

## Tech Stack

- Python 3.x with virtual environment in `.venv/`
- pdfplumber (primary PDF extraction — especially for tables)
- PyPDF2 (secondary — page counts, text search, basic operations)
- pandas for data manipulation
- Jinja2 for HTML templating
- JSON for intermediate data storage

## Key Directories

- `data/raw/` — Downloaded FDD PDFs (git-ignored, can be large)
- `data/extracted/` — Structured JSON output from extraction
- `scripts/` — All Python scripts for downloading, extracting, processing
- `site/` — Generated static HTML pages (the final output)
- `templates/` — Jinja2 HTML templates for site generation
- `docs/` — Project documentation, build specs, schema proposals

## Conventions

- Use pdfplumber as the primary PDF extraction library
- Store all extracted data as JSON (one file per franchise brand per year)
- Scripts should be runnable individually: `python scripts/scriptname.py`
- Use type hints on all functions
- Follow PEP 8, 100 character line limit
- Include docstrings on all public functions

## Common Commands

```bash
source .venv/bin/activate        # Activate virtual environment
pip install -r requirements.txt  # Install dependencies
python scripts/<name>.py         # Run individual scripts
```

## Critical Rules

1. **Never infer or fabricate data.** If a value cannot be clearly extracted from
   the source PDF, record it as `null` with a note explaining why.

2. **Provenance on every field.** Every extracted data point must include:
   filing year, state source, page number, and item/table reference.

3. **Fail loud.** If a filing is ambiguous, incomplete, inaccessible, or the
   franchisor entity is unclear, stop and report the issue rather than guessing.

4. **Separate raw facts from derived metrics.** Raw extracted values (e.g., Item 20
   outlet counts) go in one layer. Calculated values (e.g., turnover percentages)
   go in a clearly distinct derived layer. Narrative conclusions are a third layer.

5. **No premature site generation.** Do not generate website pages, scores, verdicts,
   or SEO copy until the extraction pipeline is validated and the schema is stable.

6. **Manual download fallback.** If direct programmatic download is not possible for
   a given state database (CAPTCHAs, browser-only access, etc.), document the manual
   retrieval steps and expected URL patterns so a human can download the files and
   place them in `data/raw/`.

## Architecture Notes

- FDDs are public documents filed with state regulators (primarily Wisconsin, California)
- Each franchise brand files one FDD per year
- Key sections to extract:
  - Item 5 — Initial and ongoing fees
  - Item 7 — Estimated initial investment
  - Item 19 — Financial performance representations
  - Item 20 — Outlet counts and transfers (system size, openings, closings, turnover)
- Additional signals: system age, ownership structure, notable litigation
- Extraction is per-brand, per-year; data is normalized to a common schema

## Target Brands (Initial Set)

1. Mosquito Joe
2. Mosquito Authority
3. Mosquito Hunters
4. Mosquito Squad
5. Mosquito Shield

## Project Phases (For Reference)

- **Phase 1** — Source acquisition, schema design, proof-of-extraction on 1 brand
- **Phase 2** — Extract remaining 4 brands, validate and normalize
- **Phase 3** — Static site generation with comparison pages
- **Phase 4** — Deployment and SEO optimization

Current active phase: **Phase 1**
