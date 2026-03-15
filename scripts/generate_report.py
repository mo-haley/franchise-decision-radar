#!/usr/bin/env python3
"""
Generate a Franchise Decision Report for a single brand.

Reads extracted brand JSON, fee model output, and brand-specific editorial
content, then renders a self-contained HTML report artifact.

Usage:
    python scripts/generate_report.py mosquito-authority
    python scripts/generate_report.py --all
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parent.parent
DATA_EXTRACTED = ROOT / "data" / "extracted"
DATA_DERIVED = ROOT / "data" / "derived"
TEMPLATES = ROOT / "templates"
REPORTS_OUT = ROOT / "reports"

def _load_all_brand_slugs() -> list[str]:
    """Load brand slugs from cohort registry."""
    registry_path = ROOT / "data" / "cohort_registry.json"
    if registry_path.exists():
        with open(registry_path) as f:
            cohorts = json.load(f)["cohorts"]
        slugs = []
        for cohort in cohorts:
            slugs.extend(cohort["brands"])
        return slugs
    # Fallback to mosquito-only if registry missing
    return [
        "mosquito-authority",
        "mosquito-hunters",
        "mosquito-joe",
        "mosquito-shield",
        "mosquito-squad",
    ]


BRAND_SLUGS = _load_all_brand_slugs()


@dataclass
class FeeLevel:
    revenue: int
    royalty: float
    marketing: float
    tech_other: float
    total: float
    pct: float
    rank: int


# ---------------------------------------------------------------------------
# Brand-specific editorial content
#
# This is the interpretive layer that makes the report worth paying for.
# It cannot be auto-generated from data alone — it is authored analysis.
# ---------------------------------------------------------------------------

BRAND_NARRATIVES: dict[str, dict] = {

"mosquito-authority": {

"executive_summary": """
<p>Mosquito Authority is the lowest-cost franchise in the mosquito pest control cohort
by a significant margin — both to enter and to operate. At $300K gross revenue, annual
franchisor fees total $52,800 (17.6% of revenue), roughly $25,000–$33,000 less than any
competitor. The system is the largest in the cohort (546 franchised outlets) with zero
terminations across the 2022–2024 reporting window — the cleanest system health profile
of any brand reviewed.</p>

<p>The biggest risk is latent, not current: the franchisor reserves the right to implement
a national marketing fee of up to 3% of Gross Revenues at any time, which would add
$6,000–$15,000/year. The predecessor entity's regulatory history (5 state actions for
selling without registration) is real but pre-dates current ownership. Disclosure quality
is strong, with a rich Item 19 — though a <code>#REF!</code> spreadsheet error and minor
population mismatches are quality blemishes worth noting.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Authority has the lightest ongoing fee burden at every modeled revenue level.
The primary driver is marketing: Authority's local ad minimum ($5,500 or 5%) is 4–7× lower
than competitors' mandatory marketing floors ($37,500–$75,000+).</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (10% flat):</strong> Mid-cohort rate. Minimum monthly fee ($700/mo by Year 7+)
never exceeds the percentage at modeled revenue levels. (p. 15)</li>
<li><strong>Marketing ($5,500 or 5%):</strong> Proportional to revenue with a low floor.
No active national fund. This is why Authority's total burden is so much lower — competitors
pay $37K–$75K in fixed marketing obligations that hit hardest at low revenue. (pp. 15, 19–20)</li>
<li><strong>Technology ($100–$1,200/mo, tiered):</strong> Jumps in $100/mo steps per $50K revenue
bracket. At $300K: $400/mo ($4,800/yr). At $500K: $600/mo ($7,200/yr). The escalation is
predictable but not obvious from the headline rate. (pp. 16, 21)</li>
<li><strong>Website/digital ($250/mo):</strong> Fixed. Covers local site, SEO, review tools. (p. 15)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, you keep ~$247K after franchisor fees.
The next cheapest brand (Mosquito Squad) leaves you ~$222K. That $25,000/year gap compounds
over a 10-year franchise term into a quarter-million dollars of difference in retained earnings.
</div>

<div class="callout">
<div class="callout-title">Latent risk — unimplemented national marketing fee</div>
The FDD reserves the right to implement a national marketing fee of up to 3% at any time,
adding $6K–$15K/year. No timeline or conditions are specified. If activated, Authority's
burden rises to 20–21% of revenue — still lowest in cohort, but the gap narrows significantly.
(p. 15, Note 4)
</div>
""",

"item19_narrative": """
<p>Authority's Item 19 is the second-richest in the cohort, providing both a company-owned
P&L and detailed franchised revenue distributions. This is more than most competitors
offer — but it requires careful interpretation.</p>

<h3>Company-owned P&L (Part 1)</h3>
<p>One company-owned territory in Hickory, NC, operating since 2009. Full P&L for 2023 and
2024:</p>
<ul>
<li>Revenue: $374,420 (2023), $384,192 (2024)</li>
<li>EBITDA: $71,691 (2023), $52,578 (2024)</li>
<li><strong>Net income: −$6,852 (2023), −$30,411 (2024)</strong></li>
</ul>
<p>The negative net income is driven by $60,000/year in amortization. Before amortization
and depreciation, the location is profitable. But the EBITDA decline from $72K to $53K is
a real signal — expenses grew faster than revenue.</p>

<p><strong>What to be careful about:</strong> This is a single location that has operated for
15+ years. It pays 10% royalty and ~10% in advertising (matching franchisee obligations). It
is not representative of a new operator's first years. The manager salary ($48K/year) is
included in expenses — if you operate the business yourself, that cost becomes your draw,
changing the economics significantly.</p>

<h3>Franchised revenue (Part 2)</h3>
<p>Average gross revenue of $464,600 across 128 qualifying franchisees (506 territories).
But this is <strong>per franchisee, not per territory</strong>. The average qualifying
franchisee owns approximately 4 territories. A single-territory operator should not assume
$465K revenue.</p>

<p>The revenue-by-years-active breakdown is more useful: franchisees with "at least 2 full
seasons" average $149,470 (median $97,460). Those with 4+ seasons average $192,574. Revenue
grows meaningfully with tenure, but the early years are significantly lower than the
headline average suggests.</p>

<h3>What's missing</h3>
<p>No franchised cost data or profitability. No per-territory revenue. The <code>#REF!</code>
error in the 10+ Full Seasons cell (p. 55) means the most experienced cohort's average
is missing from the filed document.</p>

<div class="implication">
<strong>What this means:</strong> You can estimate likely gross revenue from the years-active
data ($100K–$190K in early years, growing with tenure), but you cannot estimate profitability
from this FDD alone. The company-owned P&L gives cost ratios but from a 15-year mature location
that is not representative of a new operation. You will need to build your own expense model
or talk to current franchisees.
</div>
""",

"investment_narrative": """
<p>Lowest in the cohort: $54,000–$127,700. The range is wide because two variables swing it:
franchise type (Hometown $25K vs Full-Size $45K) and vehicle ($0 if you own a qualifying
truck, $30K if not).</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($25K–$45K):</strong> Franchisor will defer up to 50% at 8% over
36 months — unusual flexibility. Some 2024 sales at $31.5K–$35K suggest room to negotiate. (p. 13)</li>
<li><strong>Pre-opening marketing ($15K–$25K):</strong> Mandatory branded package. May be
reduced if existing franchisees operate nearby. At the low end, this is nearly 28% of total
investment. (p. 22)</li>
<li><strong>Vehicle ($0–$30K):</strong> Late model white full-size pickup. Own one already and
this entire line disappears — it's the single biggest swing factor in the range. (p. 22)</li>
<li><strong>Working capital ($3K–$10K):</strong> Only 3 months, which is conservative for a
seasonal business with near-zero winter revenue. Plan for personal reserves beyond this. (p. 23)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> A buyer with a qualifying vehicle and the Hometown tier can
realistically enter for ~$54K cash (or ~$41K with the fee deferral). A Full-Size buyer
needing a vehicle is closer to $100K+. The investment range is real — your actual number
depends on decisions you control.
</div>
""",

"system_health_narrative": """
<p>Most stable system in the cohort. Modest growth every year (+5, +10, +7) with no
rapid-open/rapid-close churn. For context: Mosquito Shield grew +140 in the same
period but lost 128 outlets to terminations and closures. Authority grew +22 and
lost 17. Different kind of growth.</p>
""",

"system_health_detail": """
<h3>Zero terminations</h3>
<p>No franchisee was terminated across the entire 3-year window — unique in this cohort.
Closures are limited to ceased operations (2, 7, 7) and 3 non-renewals in 2024 (the first
in the reporting period). Small numbers against 530+ outlets.</p>

<div class="implication">
<strong>What this means:</strong> The franchisor is not aggressively culling underperformers,
and franchisees are not walking away. In a cohort where one competitor terminated 65
outlets in a single year, this stability is a meaningful differentiator.
</div>

<h3>Active resale market</h3>
<p>37, 29, 37 transfers per year (~7% of system). In a system with zero terminations,
transfers mean ownership changes with the outlet staying open. People are buying these
franchises from existing owners — a signal that the business has resale value.</p>

<h3>Minimal company-owned footprint</h3>
<p>One location (Hickory, NC). A second (West Chester, PA) was briefly company-owned in
2023–2024, then sold back. The franchisor is not competing with its franchisees.</p>
""",

"risk_narrative": """
<h3>Predecessor regulatory history</h3>
<p>Five concluded actions — all against predecessor TMA Franchise Systems, Inc., not the
current entity (Main Line Brands LLC, formed 2020):</p>
<ul class="compact">
<li>Maryland (2013): selling without registration</li>
<li>Rhode Island (2013): selling without registration, $5K penalty</li>
<li>Virginia (2015): selling without registration, $20K penalty</li>
<li>Wisconsin (2016): selling without registration, $10K penalty</li>
<li>Washington (2020): Assurance of Discontinuance (inherited)</li>
</ul>
<p>Same violation, five states, seven years. This was systemic, not accidental. Under current
ownership (since 2020): zero regulatory actions.</p>

<div class="implication">
<strong>What this means:</strong> The predecessor had a genuine compliance problem. The current
entity appears clean, but the brand's regulatory history is disclosed in every FDD and will
surface in any attorney review. Ask the franchisor directly what changed operationally —
not just whether new management was installed.
</div>

<h3>Document quality</h3>
<p>A <code>#REF!</code> spreadsheet error in Item 19 (p. 55) and minor population mismatches
(129/508 vs stated 128/506). Quality blemishes in the filing, not fabrication signals — but
worth noting in a document underlying a six-figure decision.</p>

<h3>Entity and ownership</h3>
<p>PE-backed (Susquehanna Private Capital). Straightforward entity structure relative to
competitors — notably simpler than Mosquito Joe's 6-layer SPV chain. All five brands in
this cohort are PE-backed; this is industry-standard.</p>
""",

"peer_narrative": """
<p>Authority is the only brand in this cohort where you can enter for under $60K, operate
with fees under 18% of revenue, and look at a system with zero terminations. It is not
the most transparent (Squad's Item 19 is richer) or the fastest-growing (Shield added +140
units). But it is the lowest-risk, lowest-cost option by a clear margin.</p>

<p><strong>Closest comparison: Mosquito Squad.</strong> Similar age, both PE-backed, both with
solid disclosure. Squad has better unit economics data ($484K/territory) and the best
company-owned P&L ($20.8M, 25.9% margin) — but costs 2× more to enter and $25K/year more
to operate at $300K revenue.</p>

<p><strong>Sharpest contrast: Mosquito Shield.</strong> Opposite profiles. Shield has the
fastest growth (+140) but highest churn (65 terminations in 2023). Lowest royalty (8%) but
highest local ad floor ($50K). Authority has higher royalty (10%) but the lowest total
burden by far.</p>
""",

"discovery_questions": [
    {
        "question": "The FDD reserves a national marketing fee of up to 3%. Under what conditions would you implement it, and what timeline are you considering?",
        "context": "FDD p. 15, Note 4. Not yet active but could add $6K–$15K/year."
    },
    {
        "question": "The company-owned location in Hickory showed declining EBITDA ($72K to $53K) and negative net income both years. What's driving that trend?",
        "context": "Item 19 Part 1, pp. 51–52. Net income −$6.8K (2023), −$30.4K (2024)."
    },
    {
        "question": "The Item 19 average gross revenue ($464,600) is per franchisee, not per territory. What is the average revenue for a single-territory operator?",
        "context": "Item 19 Part 2, p. 53. Average franchisee owns ~4 territories."
    },
    {
        "question": "There are 3 non-renewals in 2024 — the first in the 3-year reporting period. What happened?",
        "context": "Item 20, Table 3, p. 56. Zero non-renewals in 2022–2023."
    },
    {
        "question": "The predecessor entity (TMA) had regulatory actions in 5 states for selling without registration. What specifically changed in the compliance process under Main Line Brands?",
        "context": "Item 3, pp. 11–13. Actions in MD, RI, VA, WI, WA (2013–2020)."
    },
    {
        "question": "The technology fee tiers go up to $1,200/month at $1.05M+ revenue. Is there a cap, or will additional tiers be added?",
        "context": "Item 6, Note 10, p. 21. 12-tier schedule from $100–$1,200/month."
    },
    {
        "question": "There's a #REF! error in the Item 19 table for 10+ Full Seasons franchisees. Can you provide the corrected average?",
        "context": "Item 19 Part 2, p. 55. Spreadsheet formula error in filed FDD."
    },
    {
        "question": "What does the Hometown Franchise ($25K fee, smaller territory) look like in practice? How does revenue compare to Full-Size territories?",
        "context": "Item 5, p. 13. 62 Hometown franchises as of end 2024."
    },
    {
        "question": "The West Chester, PA company-owned location was acquired in 2023 and sold back in 2024. What happened?",
        "context": "Item 20, Table 4, pp. 63–64. Short-lived company ownership."
    },
    {
        "question": "Transfer volume is ~37/year (7% of system). Are these primarily retirements, upgrades to multi-territory, or something else?",
        "context": "Item 20, Table 2. 37 transfers in 2022, 29 in 2023, 37 in 2024."
    },
],

},
}  # end BRAND_NARRATIVES


def load_brand(slug: str) -> dict:
    """Load extracted brand JSON."""
    path = DATA_EXTRACTED / f"{slug}.json"
    with open(path) as f:
        return json.load(f)


def load_fee_model() -> dict:
    """Load fee model output."""
    path = DATA_DERIVED / "fee_burden_model_output.json"
    with open(path) as f:
        return json.load(f)


def build_fee_table(brand_name: str, fee_model: dict) -> list[FeeLevel]:
    """Build fee level rows for this brand with cohort ranking."""
    levels = []
    for revenue in fee_model["revenue_levels"]:
        all_at_level = [r for r in fee_model["results"] if r["gross_revenue"] == revenue]
        all_at_level.sort(key=lambda x: x["total"])
        brand_row = next(r for r in all_at_level if r["brand"] == brand_name)
        rank = next(i + 1 for i, r in enumerate(all_at_level) if r["brand"] == brand_name)
        tech_other = (
            brand_row["technology"] + brand_row["call_center"] + brand_row["convention"]
            + brand_row["website_digital"] + brand_row["software_vendor"]
            + brand_row["bookkeeping"] + brand_row["sales_center"]
        )
        levels.append(FeeLevel(
            revenue=revenue, royalty=brand_row["royalty"],
            marketing=brand_row["marketing"], tech_other=tech_other,
            total=brand_row["total"], pct=brand_row["pct_of_revenue"], rank=rank,
        ))
    return levels


def build_investment_table(data: dict) -> tuple[list[dict], int, int]:
    """Build investment line items from Item 7."""
    items = []
    for li in data["raw"]["item_7_initial_investment"]["line_items"]:
        items.append({
            "category": li["category"],
            "low": li["low"],
            "high": li["high"],
        })
    total_low = data["raw"]["item_7_initial_investment"]["total_low"]
    total_high = data["raw"]["item_7_initial_investment"]["total_high"]
    return items, total_low, total_high


def build_health_table(data: dict) -> list[dict]:
    """Build yearly health rows."""
    rows = []
    for yr in data["raw"]["item_20_outlet_summary"]["years_reported"]:
        closed = yr["closed"] + (yr.get("non_renewals") or 0) + (yr.get("ceased_operations_other") or 0)
        f_start = yr["total_outlets_start"] - (yr.get("company_owned_start") or 0)
        f_end = yr["total_outlets_end"] - (yr.get("company_owned_end") or 0)
        rows.append({
            "year": yr["year"],
            "opened": yr["opened"],
            "closed": closed,
            "net": f_end - f_start,
            "end_count": f_end,
        })
    return rows


def build_peer_table(fee_model: dict, brands_data: dict) -> tuple[list[str], list[dict], int]:
    """Build peer comparison table at $300K with system metrics."""
    brands_order = [
        "Mosquito Authority", "Mosquito Hunters", "Mosquito Joe",
        "Mosquito Shield", "Mosquito Squad",
    ]
    slug_map = {
        "Mosquito Authority": "mosquito-authority",
        "Mosquito Hunters": "mosquito-hunters",
        "Mosquito Joe": "mosquito-joe",
        "Mosquito Shield": "mosquito-shield",
        "Mosquito Squad": "mosquito-squad",
    }
    at_300k = {r["brand"]: r for r in fee_model["results"] if r["gross_revenue"] == 300000}

    def get_system_size(b: str) -> str:
        d = brands_data[slug_map[b]]
        y = d["raw"]["item_20_outlet_summary"]["years_reported"][-1]
        return str(y["total_outlets_end"] - (y.get("company_owned_end") or 0))

    def get_growth(b: str) -> str:
        d = brands_data[slug_map[b]]
        total = sum(g["value"] for g in d["derived"]["net_unit_growth"])
        return f"{total:+d}"

    def get_attrition(b: str) -> str:
        d = brands_data[slug_map[b]]
        y = next(y for y in d["raw"]["item_20_outlet_summary"]["years_reported"] if y["year"] == 2024)
        total = y["closed"] + (y.get("non_renewals") or 0) + (y.get("ceased_operations_other") or 0)
        start = y["total_outlets_start"]
        pct = round((total / start) * 100, 1) if start else 0
        return f"{pct}%"

    def get_investment(b: str) -> str:
        d = brands_data[slug_map[b]]
        low = d["raw"]["item_7_initial_investment"]["total_low"]
        high = d["raw"]["item_7_initial_investment"]["total_high"]
        return f"${low // 1000}K–${high // 1000}K"

    metrics = [
        ("System size", get_system_size),
        ("Investment range", get_investment),
        ("Fee burden at $300K", lambda b: f"${at_300k[b]['total']:,.0f}"),
        ("% of revenue", lambda b: f"{at_300k[b]['pct_of_revenue']}%"),
        ("3-year net growth", get_growth),
        ("2024 attrition", get_attrition),
        ("Royalty rate", lambda b: {"Mosquito Authority": "10%", "Mosquito Hunters": "10%",
            "Mosquito Joe": "10/7%", "Mosquito Shield": "8%", "Mosquito Squad": "10/9/8%"}[b]),
    ]

    table = []
    for metric_name, fn in metrics:
        table.append({
            "metric": metric_name,
            "cells": [fn(b) for b in brands_order],
        })

    this_idx = 1  # 1-indexed for template
    return brands_order, table, this_idx


def generate_report(slug: str) -> None:
    """Generate a Decision Report for a single brand."""
    if slug not in BRAND_NARRATIVES:
        print(f"Error: No editorial content for '{slug}'. Available: {list(BRAND_NARRATIVES.keys())}")
        sys.exit(1)

    data = load_brand(slug)
    fee_model = load_fee_model()
    narratives = BRAND_NARRATIVES[slug]
    brand_name = data["brand"]["brand_name"]

    # Build data contexts
    fee_table = build_fee_table(brand_name, fee_model)
    inv_table, inv_low, inv_high = build_investment_table(data)
    health_table = build_health_table(data)
    all_brands = {s: load_brand(s) for s in BRAND_SLUGS}
    peer_brands, peer_table, this_brand_idx = build_peer_table(fee_model, all_brands)

    # Render
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=False)
    template = env.get_template("report-artifact.html")

    context = {
        "brand_name": brand_name,
        "filing_year": data["filing_year"],
        "legal_entity": data["brand"]["legal_entity"],
        "report_date": date.today().isoformat(),
        "page_count": data["source_document"]["page_count"] or "~230",
        "sha256": data["source_document"]["sha256"] or "not recorded",

        "executive_summary": narratives["executive_summary"],
        "fee_burden_narrative": narratives["fee_burden_narrative"],
        "fee_table": fee_table,
        "fee_burden_detail": narratives["fee_burden_detail"],
        "item19_narrative": narratives["item19_narrative"],
        "investment_narrative": narratives["investment_narrative"],
        "investment_table": inv_table,
        "investment_total_low": inv_low,
        "investment_total_high": inv_high,
        "investment_detail": narratives["investment_detail"],
        "system_health_narrative": narratives["system_health_narrative"],
        "health_table": health_table,
        "system_health_detail": narratives["system_health_detail"],
        "risk_narrative": narratives["risk_narrative"],
        "peer_narrative": narratives["peer_narrative"],
        "peer_brands": peer_brands,
        "peer_table": peer_table,
        "this_brand_index": this_brand_idx,
        "discovery_questions": narratives["discovery_questions"],
    }

    html = template.render(**context)

    REPORTS_OUT.mkdir(exist_ok=True)
    output_path = REPORTS_OUT / f"{slug}-decision-report.html"
    output_path.write_text(html)
    print(f"Report generated: {output_path.relative_to(ROOT)}")
    print(f"  Brand: {brand_name}")
    print(f"  Size: {len(html):,} bytes")
    print(f"  Open in browser: file://{output_path}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_report.py <brand-slug>")
        print(f"Available: {', '.join(BRAND_NARRATIVES.keys())}")
        sys.exit(1)

    slug = sys.argv[1]
    if slug == "--all":
        for s in BRAND_NARRATIVES:
            generate_report(s)
    else:
        generate_report(slug)


if __name__ == "__main__":
    main()
