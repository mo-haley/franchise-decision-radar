# Decision Report Specification — v2

**Updated:** 2026-03-31

---

## What the report is

A single-brand decision-preparation document for a prospective franchise buyer
who has narrowed to one brand and needs to understand what the FDD actually says
before committing. Delivered as a PDF immediately after purchase. Typically
18–25 pages depending on disclosure depth.

## Format

Self-contained HTML file rendered to PDF via Playwright (headless Chromium).
No external dependencies, no navigation, no interactive elements, no links to
the public site. Styled for reading and printing.

## Tone

Calm, direct, analytical. Reads like a memo from a sharp advisor who has
read the FDD and the four competing FDDs. Not legal advice. Not a
recommendation. Decision-useful information presented honestly.

---

## Sections (13 total)

Each section is a numbered entry in the Table of Contents. The HTML template
is `templates/report-artifact.html`. Editorial content lives in:
- `scripts/generate_report.py` (mosquito cohort)
- `scripts/lawn_narratives.py` (lawn cohort)
- `scripts/cleaning_narratives.py` (cleaning cohort)

### 1. Cover Page
Brand name, "Franchise Decision Report" subtitle, source FDD year, filing
state, legal entity, report generation date, "Franchise Decision Radar" origin.
Full-page layout with `page-break-after: always`.

### 2. Table of Contents
Numbered list linking to all sections. Auto-numbered via CSS counters.
Full-page layout with `page-break-after: always`.

### 3. Executive Summary
4–8 paragraphs. Category position, primary advantage, primary limitation,
key economic question, bottom-line posture. This is the synthesis — not
a recap of section headers.

### 4. Decision Scorecard
Rated table across 7–8 dimensions (entry cost, ongoing fees, system stability,
revenue disclosure, disclosure quality, downside risk, buyer fit, overall).
Each row has: dimension name, rating (Strong/Mixed/Weak), color class, and
one-line summary. Followed by an "Overall posture" callout.

**Template keys:** `scorecard` (list of dicts with `dimension`, `rating`,
`color`, `summary`), `scorecard_posture` (HTML string).

### 5. Buyer-Fit Profile
Structured narrative with three subsections: "Best fit for", "Weaker fit for",
"Proceed only if". Uses `.fit-section` wrapper.

**Template key:** `buyer_fit_narrative` (HTML string with `<h3>` subsections).

### 6. Fee Burden Analysis
Narrative intro + fee table (4 revenue levels: $200K, $300K, $400K, $500K)
showing royalty, marketing, tech/other, total, % of revenue, cohort rank.
Followed by cohort fee bar comparison at $300K. Then detailed fee narrative.

**Template keys:** `fee_burden_narrative`, `fee_burden_detail` (both HTML),
plus auto-generated `fee_table` and `fee_comparison`.

### 7. Item 19 Interpretation
What is disclosed, what it implies, what it omits, what a new operator should
and should not infer. Optional triangulation subsection.

**Template keys:** `item19_narrative`, `item19_triangulation` (optional).

### 8. Buyer-Side Economics Reality Check
Illustrative operating scenarios (typically 3: conservative, moderate, strong)
showing revenue, franchisor fees, estimated COGS, and remaining margin.
Followed by assumption note and detailed economics narrative.

**Template keys:** `economics_preamble`, `economics_assumptions`,
`economics_detail`, plus auto-generated `economics_scenarios`.

**Config keys in narratives:** `economics_scenarios_config` (list of
(label, revenue) tuples), `economics_cogs_ratio` (float).

### 9. Illustrative Payback Sensitivity (optional)
Only included if `payback_narrative` is provided. Shows payback timeline
under multiple assumptions.

### 10. Investment Breakdown
Narrative intro + Item 7 line-item table (category, low, high) with total row.
Then detailed investment narrative covering what's negotiable vs. fixed.

**Template keys:** `investment_narrative`, `investment_detail`, plus
auto-generated `investment_table`, `investment_total_low`, `investment_total_high`.

### 11. System Health
Narrative intro + yearly health table (year, opened, closed, net, end count).
Then detailed system health narrative.

**Template keys:** `system_health_narrative`, `system_health_detail`, plus
auto-generated `health_table`.

### 12. Risk Signals
Free-form narrative covering: entity structure, litigation, regulatory history,
confidentiality clauses, company-owned outlets, document quality concerns.

**Template key:** `risk_narrative`.

### 13. Peer Context
Comparative narrative + peer comparison table (all brands in cohort across 7
metrics: system size, investment range, fee burden at $300K, % of revenue,
3-year net growth, recent attrition, royalty rate).

**Followed by Decision Overlay** — a table of 6–7 decision-relevant
comparisons (e.g., "Lowest-cost entry", "Richest disclosure depth",
"Strongest growth trajectory") with the winning brand and rationale for each.

**Template keys:** `peer_narrative`, plus auto-generated `peer_brands`,
`peer_table`, `this_brand_index`. Editorial: `peer_decision_overlay`.

### 14. Discovery Day Diligence Script
8–12 FDD-specific questions. Each question includes:
- `question`: The question text
- `context`: Why it matters (FDD page reference)
- `strong_answer` or `strong`: What a good answer sounds like
- `weak_answer` or `evasion`: What evasion sounds like
- `follow_up` or `follow_ups`: Follow-up questions

**Template key:** `discovery_questions` (list of dicts).

### 15. Source & Methodology
Auto-generated from brand data. Covers: source document (with SHA-256),
extraction method, fee modeling assumptions, economics scenario methodology,
peer comparison scope, and disclaimer.

---

## Decision Overlay — Required for All Brands

The `peer_decision_overlay` key is **required** for every brand in every cohort.
It is a list of dicts with exactly three keys:

```python
"peer_decision_overlay": [
    {"label": "...", "brand": "...", "rationale": "..."},
]
```

**Key names must be exactly:** `label`, `brand`, `rationale`
Do NOT use: `priority`, `best_brand`, `note`, or any other key names.

Typical overlay dimensions (6–7 entries per cohort):
- Lowest-cost entry
- Lowest ongoing fee burden
- Richest disclosure / revenue data
- Strongest growth trajectory
- Lowest franchise turnover
- Best for first-time buyers
- Highest risk (if applicable)

The overlay content is the same across all brands within a cohort (it's a
cohort-level comparison, not brand-specific).

---

## PDF Formatting Rules

### Page breaks
- **Cover page** and **Table of Contents**: `page-break-after: always`
- **Major sections with tables** (Fee Burden, Item 19, Economics, Investment,
  System Health, Peer Context, Discovery Day, Methodology): start on new page
  via `class="section-break"`
- **Flowing sections** (Decision Scorecard, Buyer-Fit, Payback, Risk Signals):
  do NOT force new page — let content flow naturally to avoid orphaned tails
- `h2` and `h3`: `break-after: avoid` to stay with following content

### Page break avoidance
- Small tables: `page-break-inside: avoid`
- Callouts, fee-bars, decision-overlay: `page-break-inside: avoid`
- Individual discovery questions: `page-break-inside: avoid`
- **Large tables** (`.peer-table`, `.scorecard`): `page-break-inside: auto` —
  these are too large to force onto a single page without creating blank gaps
- **Variable-length content** (`.fit-section`, `.methodology`): let flow
  naturally — do NOT use `page-break-inside: avoid`

### Page numbering
- Rendered via Playwright `footer_template` with `<span class="pageNumber">`
- Bottom margin: 0.9in to accommodate footer
- Font: 8px, -apple-system, color #999, centered

### Common formatting errors to avoid
1. **Orphaned tails**: A section-break forces the next section to a new page,
   but the previous section's last paragraph barely overflows, creating a
   page with only 1–2 lines. Fix: remove section-break from short sections.
2. **Heading-only pages**: A section heading + intro appear on a page but
   the table gets pushed to the next page by `page-break-inside: avoid`.
   Fix: let large tables flow naturally.
3. **Blank gaps**: `page-break-inside: avoid` on a large element pushes it
   to the next page, leaving a visible gap. Fix: override with
   `page-break-inside: auto` for elements that may exceed half a page.

---

## PDF Build Pipeline

1. `python scripts/generate_report.py --all` — renders HTML from template + narratives
2. `python scripts/build_report_pdfs.py` — converts HTML to PDF via Playwright
3. PDFs are written to `site/reports/` with security tokens in filenames
4. Push to `main` triggers GitHub Pages deployment

---

## Provenance posture

The report does not use notation tags (Extracted/Modeled/Editorial) inline like
the site. Instead, the methodology section explains the data layers once.
Specific claims reference FDD page numbers where useful (e.g., "Item 6, p. 15").

## Disclaimers

- Not legal advice, not investment advice
- Based on publicly filed 2025 FDD (Wisconsin DFI)
- Modeled values use stated assumptions
- Buyer should read the actual FDD and consult professionals
