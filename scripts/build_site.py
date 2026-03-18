#!/usr/bin/env python3
"""
Build script for Franchise Decision Radar static site.

Reads cohort registry, extracted brand JSONs, and derived data,
then renders Jinja2 templates to site/ for all cohorts.

Usage:
    python scripts/build_site.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parent.parent
DATA_EXTRACTED = ROOT / "data" / "extracted"
DATA_DERIVED = ROOT / "data" / "derived"
TEMPLATES = ROOT / "templates"
SITE = ROOT / "site"

SITE_BASE_URL = "https://franchisedecisionradar.com/"


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

def load_registry() -> list[dict]:
    """Load cohort definitions from the registry file."""
    path = ROOT / "data" / "cohort_registry.json"
    with open(path) as f:
        return json.load(f)["cohorts"]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def all_cohort_slugs(cohort: dict) -> list[str]:
    """Return all brand slugs for a cohort, including watchlist brands."""
    slugs = list(cohort["brands"])
    for s in cohort.get("watchlist", []):
        if s not in slugs:
            slugs.append(s)
    return slugs


def load_brand_data(brand_slugs: list[str]) -> dict[str, dict]:
    """Load extracted brand JSONs for a list of slugs."""
    brands: dict[str, dict] = {}
    for slug in brand_slugs:
        path = DATA_EXTRACTED / f"{slug}.json"
        with open(path) as f:
            brands[slug] = json.load(f)
    return brands


def load_fee_model(filename: str) -> Optional[dict]:
    """Load fee model output if available."""
    path = DATA_DERIVED / filename
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


# Minimum franchised outlet count for inclusion in peer comparison pages.
# Brands below this threshold get individual brand pages but are excluded
# from fee-burden, system-health, and cost-to-enter comparison tables.
COMPARISON_MIN_OUTLETS = 25


def normalize_item7(data: dict) -> tuple[int, int, int]:
    """Extract (total_low, total_high, midpoint) from Item 7, handling split-market brands.

    Some brands (e.g., The Cleaning Authority) have separate enterprise/hometown
    market tables instead of a single total_low/total_high. For those, we use the
    enterprise market as the primary comparison figure.
    """
    item7 = data["raw"]["item_7_initial_investment"]
    derived_mid = data["derived"]["initial_investment_midpoint"]

    if "total_low" in item7:
        low = item7["total_low"]
        high = item7["total_high"]
        mid = derived_mid if isinstance(derived_mid, (int, float)) else int(derived_mid)
    elif "enterprise_market" in item7:
        ent = item7["enterprise_market"]
        low = ent["total_low"]
        high = ent["total_high"]
        mid = derived_mid.get("enterprise_market", (low + high) // 2) if isinstance(derived_mid, dict) else derived_mid
    else:
        raise ValueError(f"Unrecognized Item 7 structure: {list(item7.keys())}")

    return int(low), int(high), int(mid)


def franchised_outlet_count(data: dict) -> int:
    """Return the most recent year-end franchised outlet count for a brand."""
    years = data["raw"]["item_20_outlet_summary"]["years_reported"]
    y_last = sorted(years, key=lambda y: y["year"])[-1]
    return y_last["total_outlets_end"] - (y_last.get("company_owned_end") or 0)


def filter_comparison_brands(
    brands: dict[str, dict],
) -> tuple[dict[str, dict], list[str]]:
    """Split brands into comparison-eligible and excluded based on outlet count.

    Returns (eligible_brands, excluded_slugs).
    """
    eligible = {}
    excluded = []
    for slug, data in brands.items():
        if franchised_outlet_count(data) >= COMPARISON_MIN_OUTLETS:
            eligible[slug] = data
        else:
            excluded.append(slug)
    return eligible, excluded


def build_slug_map(brands: dict[str, dict]) -> dict[str, str]:
    """Build brand display-name to slug mapping from loaded data."""
    return {data["brand"]["brand_name"]: slug for slug, data in brands.items()}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def derive_trajectory(growth_vals: dict[int, int]) -> tuple[str, str]:
    """Auto-derive system trajectory label and CSS class from 3 years of growth."""
    years = sorted(growth_vals.keys())
    if len(years) < 3:
        return "Insufficient data", "caution"

    g1, g2, g3 = growth_vals[years[0]], growth_vals[years[1]], growth_vals[years[2]]
    total = g1 + g2 + g3

    if total > 0 and g3 >= g2 and g2 >= g1:
        return "Accelerating", "positive"
    elif total > 0 and g3 > 0:
        if g3 < g2:
            return "Decelerating", "caution"
        return "Stable positive", "positive"
    elif total > 0 and g3 <= 0:
        return "Mixed — recent contraction", "negative"
    elif total == 0:
        return "Flat", "caution"
    elif total < 0 and g3 > g2:
        return "Recovering", "positive"
    else:
        return "Contracting", "negative"


def derive_royalty_display(item6: dict) -> tuple[str, str]:
    """Auto-derive royalty rate display string and structure note from fee data."""
    rr = item6.get("royalty_rate", {})
    tiers = rr.get("tiers")
    if tiers and isinstance(tiers, list) and len(tiers) > 0:
        rates = [f"{t['rate']}%" for t in tiers]
        return " / ".join(rates), "Tiered by revenue bracket"
    if rr.get("value") is not None:
        basis = rr.get("basis", "Gross Revenue")
        return f"{rr['value']}%", f"Flat rate on {basis}"
    return "\u2014", "See FDD for details"


# ---------------------------------------------------------------------------
# Hardcoded editorial — mosquito brands only
# ---------------------------------------------------------------------------

# Trajectory overrides for brands with manually assessed trajectories
TRAJECTORY_OVERRIDES: dict[str, tuple[str, str]] = {
    "Mosquito Authority": ("Stable positive", "positive"),
    "Mosquito Hunters": ("Turnaround", "caution"),
    "Mosquito Joe": ("Deteriorating", "negative"),
    "Mosquito Shield": ("Decelerating + high churn", "negative"),
    "Mosquito Squad": ("Recovering", "positive"),
    "Mosquito Sheriff": ("Early-stage launch", "caution"),
    "MosquitoNix": ("Launch year", "caution"),
    "Lawn Doctor": ("Accelerating", "positive"),
    "Weed Man": ("Stable (contract restructure)", "caution"),
    "Spring-Green": ("Flat", "caution"),
    "NaturaLawn": ("Stable niche", "positive"),
    "Lawn Pride": ("Explosive launch", "positive"),
    "Lawn Squad": ("Launch year", "caution"),
    "Merry Maids": ("Accelerating contraction", "negative"),
    "Molly Maid": ("Steady contraction", "negative"),
    "The Cleaning Authority": ("Stable positive", "positive"),
    "The Maids": ("Mild contraction", "caution"),
    "MaidPro": ("Stabilizing", "caution"),
    "Two Maids & A Mop": ("Accelerating", "positive"),
    "Maid Right": ("Growing but high churn", "caution"),
}

# Editorial content per brand — only for brands with manually authored analysis.
# Brands not in this dict get data-only pages (no watchouts, positives, etc.)
BRAND_EDITORIAL: dict[str, dict] = {
    "mosquito-authority": {
        "parent_short": "Susquehanna Private Capital",
        "ownership": "PE-backed",
        "royalty_display": "10% flat",
        "royalty_context": "mid-cohort rate",
        "marketing_floor": "$5,500/yr",
        "marketing_context": "lowest in cohort",
        "disclosure_quality": "Strong",
        "disclosure_rank": "2nd of 5",
        "disclosure_narrative": (
            "Rich Item 19 with full company-owned P&L (1 territory, Hickory NC) and detailed "
            "franchised gross revenue distributions by bracket, territory count, and ownership "
            "length. A <code>#REF!</code> spreadsheet error in one cell and minor population "
            "count mismatches are quality blemishes but not disqualifying. The predecessor "
            "entity (TMA) had 5 state regulatory actions for selling without registration "
            "(2013&ndash;2020) &mdash; all pre-current-ownership."
        ),
        "watchouts": [
            "National marketing fee (up to 3%) is reserved but not yet implemented. "
            "Franchisor can activate it at any time, adding $6K&ndash;$15K/year.",
            "Company-owned location runs at negative net income after $60K annual amortization "
            "&mdash; weakens the P&L as an economic benchmark.",
            "Predecessor entity (TMA) had 5 state regulatory actions for selling franchises "
            "without registration. All pre-2020 under prior ownership, but pattern is real.",
            "Technology fee is tiered by revenue ($100&ndash;$1,200/mo) &mdash; unpredictable "
            "ongoing cost that scales with success.",
        ],
        "positives": [
            "Lowest ongoing fee burden at every modeled revenue level &mdash; 17&ndash;18% of "
            "revenue vs 26&ndash;38% for competitors.",
            "Zero terminations across the entire 3-year reporting period (2022&ndash;2024). "
            "Cleanest system health in the cohort.",
            "Largest system in the cohort (546 franchised outlets) with 16 years of history.",
            "Fee deferral option: franchisor will defer up to 50% of initial fee at 8% interest.",
            "Lightest marketing burden: local ad minimum of $5,500 or 5%. No mandatory "
            "franchisor-managed marketing program.",
        ],
        "fee_caveats": [{
            "title": "Latent risk &mdash; unimplemented national fee",
            "text": "Authority reserves the right to implement a national marketing fee of up "
                    "to 3%. If activated, burden at $300K rises from $52,800 to ~$61,800. "
                    "Still lowest, but the gap narrows.",
        }],
        "health_flag": None,
    },
    "mosquito-hunters": {
        "parent_short": "LLCP / CNL Strategic Capital",
        "ownership": "PE-backed",
        "royalty_display": "10% flat",
        "royalty_context": "+15% on out-of-territory revenue",
        "marketing_floor": "$37,500/yr",
        "marketing_context": "high, regressive at low revenue",
        "disclosure_quality": "Weakest in cohort",
        "disclosure_rank": "5th of 5",
        "disclosure_narrative": (
            "Item 19 has 7 tables but reports only per-treatment pricing and per-customer "
            "value by region. Does not disclose total gross revenue per franchise unit &mdash; "
            "making it impossible to assess unit economics from the FDD alone. 26% of "
            "Strategic-Partners excluded from Item 19, including 8 for &ldquo;failing to invest "
            "in MH marketing programs.&rdquo; This exclusion criterion likely biases reported "
            "performance upward. Flagged as &ldquo;Special Risk&rdquo; on page 4 of the FDD."
        ),
        "watchouts": [
            "Highest franchise fee in the cohort: $107,000 ($50K license + $57K mandatory "
            "training/supply) for the smallest system.",
            "No total revenue per franchise unit disclosed in Item 19. A buyer cannot assess "
            "unit economics from the FDD.",
            "26% of Strategic-Partners excluded from Item 19 data, including 8 for not "
            "investing in marketing &mdash; circular exclusion that biases data upward.",
            "$37,500 marketing floor on a system where many units may gross under $375K "
            "&mdash; regressive burden on smaller operators.",
            "All closures coded exclusively as &ldquo;Terminations&rdquo; (zero non-renewals, "
            "zero ceased operations) &mdash; classification methodology is the franchisor&rsquo;s.",
        ],
        "positives": [
            "Strong 2024 turnaround: zero terminations (down from 17 in 2022, 11 in 2023), "
            "+13 net unit growth.",
            "Now a combination franchise: Pest Hunters + Mosquito Hunters + Humbug Holiday "
            "Lighting &mdash; multiple revenue streams.",
            "Holiday lighting pilot data (26 SPs): avg $64,727 per franchisee. Meaningful "
            "off-season revenue potential.",
            "Clean litigation history &mdash; no actions required to be disclosed.",
        ],
        "fee_caveats": [],
        "health_flag": {
            "title": "Classification note",
            "text": "All closures across 3 years are coded exclusively as "
                    "&ldquo;Terminations&rdquo; with zero in any other category. This is "
                    "statistically unusual and may reflect classification methodology "
                    "rather than operational reality.",
        },
    },
    "mosquito-joe": {
        "parent_short": "KKR / Neighborly",
        "ownership": "PE-backed (6-layer SPV)",
        "royalty_display": "10% / 7%",
        "royalty_context": "tiered at $500K &mdash; rewards growth",
        "marketing_floor": "~$75,000+/yr",
        "marketing_context": "highest in cohort",
        "disclosure_quality": "Mixed",
        "disclosure_rank": "3rd of 5",
        "disclosure_narrative": (
            "Useful tenure-split gross sales data (First 5 Years avg $214,794 / 6+ Years "
            "avg $432,954) and strong retention metrics (77% customer retention, 89% "
            "recurring). However, three Item 19 tables have wrong column headers (copy "
            "errors in a filed regulatory document). No company-owned P&L despite owning "
            "2 locations. 24 closed businesses excluded but only ~7% exclusion rate overall."
        ),
        "watchouts": [
            "Highest mandatory marketing spend in the cohort: $37K/yr DMP + $35K local "
            "+ 2% MAP + $325/mo SEO = ~$75,000+ per year before a single customer is acquired.",
            "24 terminations in 2024, up from 5 in 2023 &mdash; nearly 5&times; increase. "
            "Alabama went from 9 outlets to 1. Unexplained in the FDD.",
            "System contracted for the first time in 2024 (&minus;1 net units).",
            "Franchisor litigated a franchisee over $37K/yr DMP fee non-payment and prevailed "
            "&mdash; signals willingness to enforce mandatory marketing program.",
            "6-layer SPV/securitization entity structure adds counterparty complexity.",
        ],
        "positives": [
            "Strongest brand recognition in the cohort (KKR/Neighborly portfolio).",
            "77% customer retention rate, 89% recurring customer rate.",
            "Tiered royalty (10% &rarr; 7% above $500K) genuinely rewards growth.",
            "Second-largest system (415 units) with 13 years of franchising history.",
        ],
        "fee_caveats": [{
            "title": "Possible undercount",
            "text": "May have an ongoing local marketing minimum beyond Year 1 (FDD references "
                    "&ldquo;Minimum Local Marketing Spending&rdquo; but amount unclear). If so, "
                    "the modeled burden is lower than actual.",
        }],
        "health_flag": {
            "title": "2024 termination spike",
            "text": "24 terminations in 2024, up from 5 in 2023. Alabama went from 9 outlets "
                    "to 1 (8 terminations). System contracted for the first time. This spike "
                    "is not explained in the FDD.",
        },
    },
    "mosquito-shield": {
        "parent_short": "Princeton Equity Group",
        "ownership": "PE-backed",
        "royalty_display": "8% flat",
        "royalty_context": "lowest rate in cohort",
        "marketing_floor": "$50,000+/yr",
        "marketing_context": "highest local ad floor",
        "disclosure_quality": "Below average",
        "disclosure_rank": "4th of 5",
        "disclosure_narrative": (
            "Item 19 exclusion rate is highest in cohort: 26 &ldquo;non-conforming&rdquo; "
            "outlets excluded (21% of 125 total). &ldquo;Non-conforming&rdquo; is not defined. "
            "Only 81 outlets in gross sales data. Average of $285,839 vs median of $134,918 "
            "shows heavy right skew. Company-owned P&L provides cost percentages only "
            "&mdash; no absolute revenue figure."
        ),
        "watchouts": [
            "Highest absolute termination counts in the cohort: 65 in 2023, 44 in 2024. "
            "Growth masks significant churn (11&ndash;25% annual turnover).",
            "21% of outlets excluded from Item 19 as &ldquo;non-conforming&rdquo; (undefined). "
            "Reported averages are likely biased upward.",
            "$50,000/year local ad minimum &mdash; highest mandatory marketing floor in "
            "the cohort. Plus 2% brand fund.",
            "Minimum Gross Sales thresholds: franchisor may collect 7% of shortfall between "
            "actual revenue and required minimum ($283,500 at Year 5). Punitive.",
            "Mandatory bookkeeping vendor ($200&ndash;$500/mo) adds non-discretionary cost "
            "not captured in headline fee rates.",
        ],
        "positives": [
            "Fastest net growth in cohort: +140 units over 3 years.",
            "Lowest royalty rate (8% flat) &mdash; though offset by high marketing floor.",
            "85% customer retention, $715 avg revenue per customer.",
            "29.5% adjusted EBITDA on company-owned location (strong margin signal, "
            "though percentages only &mdash; no absolute revenue).",
            "System-wide sales growing: $19.4M (2021) to $25.7M (2024).",
        ],
        "fee_caveats": [{
            "title": "Range uncertainty",
            "text": "Bookkeeping ($200&ndash;$500/mo) and sales center ($300&ndash;$750/mo) "
                    "modeled at low end. High-end adds $9,000/year to all totals.",
        }],
        "health_flag": {
            "title": "Growth masking high churn",
            "text": "65 terminations in 2023, 44 in 2024 &mdash; highest in cohort. Net growth "
                    "looks positive only because openings outpace losses. The system churned "
                    "at 11&ndash;25% per year.",
        },
    },
    "mosquito-squad": {
        "parent_short": "Apax Partners / Authority Brands",
        "ownership": "PE-backed",
        "royalty_display": "10% / 9% / 8%",
        "royalty_context": "triple-tiered, rewards scale",
        "marketing_floor": "$35K&ndash;$50K/yr",
        "marketing_context": "moderate, capped at $50K",
        "disclosure_quality": "Best in cohort",
        "disclosure_rank": "1st of 5",
        "disclosure_narrative": (
            "Most comprehensive Item 19 in the cohort by a significant margin. 7 tables "
            "covering per-territory revenue by quartile, close rates (48%), renewal rates "
            "(70%), per-appointment revenue ($98), per-customer revenue ($705), 5-year "
            "systemwide growth, same-store growth (5%), and a full dollar-amount company-owned "
            "P&L ($20.8M revenue, 14 territories, 25.9% net margin). The only document quality "
            "issue is a table numbering error."
        ),
        "watchouts": [
            "Highest headline initial investment ($162K&ndash;$220K) &mdash; though $84K&ndash;$117K "
            "is 12-month working capital reserves (vs 3 months for all others).",
            "Minimum royalty escalates to $3,000/month at Year 9+ ($36,000/year). At $200K revenue, "
            "this exceeds the percentage-based royalty.",
            "Aggressive termination penalty: greater of 2 years&rsquo; royalty or $50,000 "
            "in liquidated damages.",
            "MA Attorney General AOD (2024) regarding &ldquo;natural&rdquo; and &ldquo;EPA-approved&rdquo; "
            "marketing claims. May constrain lead generation language.",
            "System contracted in 2022 (&minus;10 net units) before recovering.",
        ],
        "positives": [
            "Highest average revenue per territory in cohort: $484,506 (207 territories).",
            "Best disclosure quality: the only brand providing close rates, renewal rates, "
            "per-appointment revenue, and a full company-owned P&L.",
            "Company-owned operation proves 25.9% net margin at scale (14 territories, $20.8M).",
            "Brand fund is flat fee ($150&ndash;$450/mo) not percentage &mdash; does not scale "
            "with revenue. Local marketing capped at $50K.",
            "Same-store growth of 5% (195 territories, 2023 vs 2024).",
            "$124.3M total systemwide sales &mdash; 5&times; the next closest brand.",
        ],
        "fee_caveats": [{
            "title": "Year 9+ escalation",
            "text": "Minimum royalty reaches $3,000/month at Year 9+. At $200K revenue, this "
                    "exceeds the percentage and would add $16,000 to annual burden.",
        }],
        "health_flag": None,
    },
    "mosquito-sheriff": {
        "parent_short": "Founder-operated",
        "ownership": "founder-operated",
        "royalty_display": "10%",
        "royalty_context": "Flat rate on Gross Revenues",
        "marketing_floor": "$1,800/yr",
        "marketing_context": "lowest in cohort (flat $150/mo)",
        "disclosure_quality": "Minimal",
        "disclosure_rank": "7th of 7",
        "disclosure_narrative": (
            "No Item 19 financial performance representation. No revenue, profit, or "
            "customer data disclosed. With only 5 franchised units and no public "
            "performance benchmarks, a buyer cannot assess unit economics from the FDD."
        ),
        "watchouts": [
            "94% of initial investment ($75,000 of $79,450&ndash;$81,500) goes directly to "
            "the franchisor at signing &mdash; highest franchisor capture ratio in either cohort.",
            "No Item 19 disclosure &mdash; zero financial performance data available.",
            "5 franchised units total. Smallest system in the mosquito cohort by a wide margin.",
            "Technology fees are tiered by revenue (Dispatch Routing $100&ndash;$700/mo) and "
            "include per-sale commissions ($15&ndash;$35/sale) &mdash; unpredictable ongoing cost.",
            "Minimum royalty escalates to $2,000/month at Year 6+ ($24,000/year).",
        ],
        "positives": [
            "Lowest initial investment in the cohort ($79,450&ndash;$81,500).",
            "Simplest marketing structure: flat $150/month. No percentage-based fund, no "
            "mandatory local spend.",
            "Zero terminations, non-renewals, or transfers across all 3 years.",
            "Projected to double system size in 2025 (5 new units).",
        ],
        "fee_caveats": [],
        "health_flag": {
            "title": "Micro-system",
            "text": "5 franchised units is extremely small. Zero closures is positive but "
                    "the sample size is too small to draw conclusions about system stability.",
        },
    },
    "mosquitonix": {
        "parent_short": "Franworth / O'Neal Family Trust",
        "ownership": "PE-backed",
        "royalty_display": "10% / 9% / 8% / 7%",
        "royalty_context": "four-tier, rewards scale",
        "marketing_floor": "$42,000+/yr",
        "marketing_context": "highest local spend in cohort",
        "disclosure_quality": "Mixed",
        "disclosure_rank": "6th of 7",
        "disclosure_narrative": (
            "Item 19 provides detailed P&amp;L for 7 company-operated markets &mdash; but "
            "no franchisees had operated a full year at reporting time. Conforming markets "
            "show 25&ndash;35% net margins; non-conforming markets show 2 of 3 unprofitable. "
            "8% Customer Acquisition Commission on new sales is substantial and unusual."
        ),
        "watchouts": [
            "8% Customer Acquisition Commission on new sales is effectively a second royalty "
            "&mdash; combined with 10% royalty and 2% brand fund = 20% on new sales revenue.",
            "2 of 10 franchised units ceased operations in their first year (20% first-year attrition).",
            "$42,000 mandatory local marketing spend in Year 1 is the highest in the mosquito cohort.",
            "Item 19 data is exclusively from company-operated locations. Zero franchisee data.",
            "Predecessor FEMO Group franchisees subject to confidentiality clauses.",
            "19 franchise agreements signed but not yet opened &mdash; aggressive pipeline, execution risk.",
        ],
        "positives": [
            "Four-tier royalty (10% &rarr; 7%) rewards scale more aggressively than any competitor.",
            "Detailed Item 19 P&amp;L with actual COGS and expense breakdowns (company-operated).",
            "Conforming markets show 25&ndash;35% net operating margins after franchise fees.",
            "Holiday lighting revenue stream ($418K across 4 conforming markets).",
            "7 company-owned locations provide operational playbook (operating since 2006).",
        ],
        "fee_caveats": [{
            "title": "Customer Acquisition Commission",
            "text": "8% CAC on single new sales (misting, pest control, holiday lighting) is "
                    "charged on top of the 10% royalty + 2% brand fund. On a new misting system "
                    "sale of $3,586, total franchisor take is $717 (20%).",
        }],
        "health_flag": {
            "title": "First-year attrition",
            "text": "2 of 10 franchised units opened in 2024 ceased operations within the same "
                    "year (South Carolina). 20% first-year attrition in the launch year.",
        },
    },
    "lawn-doctor": {
        "parent_short": "CNL Strategic Capital",
        "ownership": "PE-backed",
        "royalty_display": "10%",
        "royalty_context": "Flat rate on Net Revenues",
        "marketing_floor": "$30,000+/yr",
        "marketing_context": "high, 10% or $30K floor + national fund",
        "disclosure_quality": "Best in cohort",
        "disclosure_rank": "1st of 6",
        "disclosure_narrative": (
            "Richest Item 19 in the lawn cohort: 4 tables covering revenue by territory count, "
            "customer metrics (avg tenure 6.15 years), gross profit margin (85.4%), and a 16-year "
            "historical revenue trend ($367K avg in 2009 &rarr; $1.13M in 2024). Median franchisee "
            "revenue of $659K. Only blemish: 37% exclusion rate on Table C."
        ),
        "watchouts": [
            "Highest initial franchise fee in the lawn cohort: $127,000 (includes $70,600 "
            "mandatory training/supply fee).",
            "25% total royalty on out-of-territory revenue (10% base + 15% surcharge) &mdash; "
            "structurally discourages geographic expansion.",
            "Marketing obligation requires the greater of $30,000 or 10% of Net Revenues for "
            "local advertising, plus national fund (2% or $5,500/yr) &mdash; expensive at low revenue.",
            "Mandatory equipment leases: Turf Tamer Applicator $335/mo + Power Seeder $306/mo "
            "= $641/month ongoing.",
            "Transfer fee is 75% of the initial license fee ($37,500) &mdash; highest in cohort.",
        ],
        "positives": [
            "Largest system in the lawn cohort (653 outlets) with 58 years of franchising history.",
            "Terminations dropped to 1 in 2024 (from 13 in 2022) &mdash; dramatically improving churn.",
            "16-year revenue trend shows 3x growth ($367K &rarr; $1.13M average).",
            "Average customer tenure of 6.15 years &mdash; strong retention signal.",
            "85.4% gross profit margin (materials only) &mdash; high-margin service business.",
            "Clean litigation history: zero actions required to be disclosed.",
        ],
        "fee_caveats": [{
            "title": "Regional fund exposure",
            "text": "If in a regional fund area (15 regions), up to 5% additional marketing "
                    "contribution. Total national + regional capped at 5% of Net Revenues, but "
                    "this is on top of the $30K+ local requirement.",
        }],
        "health_flag": None,
    },
    "weed-man": {
        "parent_short": "TH Canada (private, Canadian)",
        "ownership": "private",
        "royalty_display": "6.5% / 5.5%",
        "royalty_context": "tiered at $1M &mdash; rewards scale",
        "marketing_floor": "$2,400/yr",
        "marketing_context": "lowest in cohort (1.2%)",
        "disclosure_quality": "Weakest in cohort",
        "disclosure_rank": "6th of 6",
        "disclosure_narrative": (
            "No Item 19 financial performance representation &mdash; the only lawn brand that "
            "declines to disclose. A buyer cannot assess unit economics from the FDD. Combined "
            "with the 2024 contract restructure making Item 20 data hard to interpret, Weed Man "
            "offers the least transparency in the cohort."
        ),
        "watchouts": [
            "No Item 19 disclosure &mdash; zero financial performance data.",
            "Item 20 data is heavily distorted by 2024 contract merging: Table 1 shows apparent "
            "-134 net change that is entirely an accounting artifact.",
            "Technology fee is revenue-based (0.65% of prior year gross, min $1,200/yr) &mdash; "
            "scales with success, unpredictable.",
            "Canadian-origin system with complex multi-layer ownership: US franchisor, Canadian "
            "master licensor, sub-franchisor consolidation in 2025.",
        ],
        "positives": [
            "Lowest ongoing fee burden in the cohort at every revenue level (8.5% of revenue).",
            "Lowest royalty rate (6.5%/5.5%) and lowest marketing contribution (1.2%).",
            "Franchisor matches 50% of franchisee advertising contributions until 2033.",
            "55-year brand history (founded 1970) with 154 physical locations.",
            "Also offers mosquito control and perimeter pest services &mdash; multiple revenue streams.",
        ],
        "fee_caveats": [{
            "title": "Minimum royalty",
            "text": "Minimum annual royalty of $7,192 per Unit Territory (CPI-adjusted). "
                    "At very low revenue this floor exceeds the 6.5% rate.",
        }],
        "health_flag": {
            "title": "Contract restructure obscures data",
            "text": "~95% of franchisees converted to new agreements effective Jan 1, 2024. "
                    "Multi-area contracts were merged, reducing reported outlet count from 255 "
                    "to 117 (an accounting change, not system contraction).",
        },
    },
    "spring-green": {
        "parent_short": "Spring-Green Enterprises (private)",
        "ownership": "private",
        "royalty_display": "10% / 9% / 8%",
        "royalty_context": "triple-tiered by revenue bracket",
        "marketing_floor": "$4,000/yr",
        "marketing_context": "low (2% national), regional not active",
        "disclosure_quality": "Strong",
        "disclosure_rank": "2nd of 6",
        "disclosure_narrative": (
            "Item 19 provides gross profit margin (68.1% including labor), gross sales by business "
            "type, revenue per customer ($556), and marketing ROI ($2.62 per $1). Customer retention "
            "of 81.3%. Note: gross margin includes direct labor unlike Lawn Doctor (which only "
            "deducts materials) &mdash; not directly comparable."
        ),
        "watchouts": [
            "Affiliate Superior Lawns has reacquired 4 franchised territories over 2 years "
            "(2023&ndash;2024) &mdash; company buying back territories is a mixed signal.",
            "$35,000 Initial Marketing Campaign Fee + $16,500 Property Data Fee = $51,500 in "
            "upfront costs beyond the franchise fee.",
            "Fee Adjustment clause allows up to 100% annual increase on technology, education, "
            "meeting, and reporting fees.",
            "Some franchisees signed confidentiality clauses restricting them from speaking "
            "about their experience.",
            "System growth is flat: +2/&minus;2/+4 net units over 3 years.",
        ],
        "positives": [
            "Privately held (no PE) &mdash; founder-family controlled, no securitization layers.",
            "81.3% customer retention and $2.62 marketing ROI.",
            "Revenue per production vehicle ($201K) provides useful unit economics benchmark.",
            "48-year franchising track record.",
            "Pest control add-on service expands revenue streams.",
        ],
        "fee_caveats": [{
            "title": "Property Data Fee",
            "text": "$16,500 initial + ongoing $0.55/SFDU for territory data. This is an unusual "
                    "fee not seen in other brands &mdash; adds to total cost of operation.",
        }],
        "health_flag": None,
    },
    "naturalawn": {
        "parent_short": "Founder-operated (Philip Catron)",
        "ownership": "private (founder)",
        "royalty_display": "9% / 7%",
        "royalty_context": "reduces to 7% at $500K+ on renewal",
        "marketing_floor": "$60,000&ndash;$80,000/yr",
        "marketing_context": "highest in cohort (annual spend requirement)",
        "disclosure_quality": "Good",
        "disclosure_rank": "3rd of 6",
        "disclosure_narrative": (
            "Item 19 provides both company-owned and franchise data. Company-owned gross margin "
            "60.7%&ndash;65.2% (includes labor). Franchisee avg revenue $2.19M (median $1.1M). "
            "Revenue per customer $810 (highest in cohort) reflects organic-based premium positioning. "
            "Population count discrepancy: stated 44 but detail tables sum to 47."
        ),
        "watchouts": [
            "Requires $150,000&ndash;$250,000 line of credit IN ADDITION to the $77,500&ndash;$152,650 "
            "cash investment &mdash; the only brand requiring a credit line.",
            "$60,000&ndash;$80,000 annual marketing spend is ongoing, not one-time &mdash; creates the "
            "highest ongoing fee burden in the cohort at low revenue levels (45.8% at $200K).",
            "System contracted in 2024 (&minus;2 net units) after growing +4 each in 2022&ndash;2023.",
            "Active TCPA lawsuit (Ford v. NaturaLawn) &mdash; potential liability for telemarketing practices.",
            "Item 3 contains contradictory disclosure: heading says &ldquo;no litigation required&rdquo; "
            "but then discloses the TCPA case.",
        ],
        "positives": [
            "Highest revenue per customer in the cohort ($810 avg franchised) &mdash; organic-based "
            "premium positioning commands higher prices.",
            "Founder-operated (Philip Catron) with 36-year track record &mdash; no PE layers.",
            "Zero transfers across all 3 reported years &mdash; unique in the lawn cohort.",
            "Royalty reduces to 7% upon renewal at $500K+ Gross Sales.",
            "Franchisee avg revenue ($2.19M) exceeds company-owned ($1.73M) &mdash; franchisees "
            "outperform corporate locations.",
        ],
        "fee_caveats": [{
            "title": "Marketing is not a fee &mdash; it is a spend requirement",
            "text": "The $60K&ndash;$80K annual marketing spend goes to third-party vendors, not "
                    "the franchisor. But it is a mandatory expense that materially affects unit economics "
                    "and is modeled as part of the fee burden.",
        }],
        "health_flag": None,
    },
    "lawn-pride": {
        "parent_short": "KKR / Neighborly",
        "ownership": "PE-backed (Neighborly SPV)",
        "royalty_display": "8%",
        "royalty_context": "standard rate, Roll-In discounts available",
        "marketing_floor": "$20,000+/yr",
        "marketing_context": "2% MAP + $20K local (year 3+)",
        "disclosure_quality": "Below average",
        "disclosure_rank": "5th of 6",
        "disclosure_narrative": (
            "Item 19 discloses only per-customer revenue (not total revenue or gross sales per unit). "
            "All 35 franchised units are extremely new (30 opened during 2024). Affiliate location "
            "shows declining per-customer revenue ($1,341 &rarr; $838 over 4 years). Most limited "
            "Item 19 in the lawn cohort."
        ),
        "watchouts": [
            "Brand new franchise system: started January 2023. All 35 units are less than 2 years old.",
            "$80,000 mandatory local marketing spend in Year 1 &mdash; combined with 2% MAP and "
            "8% royalty, this front-loads costs heavily.",
            "Same Neighborly/KKR/SPV structure as Mosquito Joe &mdash; 6-layer securitization.",
            "Affiliate per-customer revenue declining year over year ($1,341 &rarr; $838 residential).",
            "Item 19 provides no total revenue or gross sales data &mdash; only per-customer averages.",
            "Mandatory HelpDesk ($200&ndash;$400/mo) and Call Center ($350&ndash;$450/mo + $25/booking) "
            "fees in addition to technology fee.",
        ],
        "positives": [
            "Explosive growth: 30 new units in 2024, 6x system size in one year.",
            "Zero terminations or transfers across all years.",
            "Lowest headline royalty in the lawn cohort (8% flat).",
            "Extensive discount programs for initial franchise fee.",
            "Part of Neighborly portfolio &mdash; established support infrastructure.",
        ],
        "fee_caveats": [{
            "title": "Year 1 marketing burden",
            "text": "$80,000 local marketing spend requirement in Year 1 is mandatory. Combined "
                    "with 2% MAP fee, a new franchisee at $200K revenue spends $84,000+ on marketing "
                    "alone (42% of revenue).",
        }],
        "health_flag": {
            "title": "All units are brand new",
            "text": "30 of 35 franchised units opened during 2024. No unit has a full year of "
                    "operating history. Zero closures is expected for a system this new.",
        },
    },
    "lawn-squad": {
        "parent_short": "Apax Partners / Authority Brands",
        "ownership": "PE-backed",
        "royalty_display": "7%",
        "royalty_context": "flat rate &mdash; lowest headline rate",
        "marketing_floor": "$42,000+/yr",
        "marketing_context": "2% brand fund + $42K local",
        "disclosure_quality": "Best P&amp;L in cohort",
        "disclosure_rank": "4th of 6",
        "disclosure_narrative": (
            "Most detailed P&amp;L disclosure in the lawn cohort: company-owned outlets show EBITDA "
            "with imputed franchisor fees. Cleveland: $399K/territory revenue, 16% EBITDA. Columbus: "
            "$192K/territory, 19% EBITDA. However, data is company-owned only (0 franchisees have "
            "operated a full year)."
        ),
        "watchouts": [
            "Highest ongoing fee burden in the lawn cohort at every revenue level: 7% royalty + "
            "2% brand fund + 5% call center = 14% of Gross Revenue before marketing.",
            "5% call center fee (percentage of Gross Revenue) is effectively a second royalty &mdash; "
            "most other brands charge flat monthly call center fees.",
            "$42,000/year mandatory local marketing on top of 14% franchisor take.",
            "Monthly technology costs total $1,170 ($450 tech + $370 ServiceMinder + $350 website).",
            "Liquidated damages clause: greater of 2 years&rsquo; royalty or $50,000 on default.",
            "Only 7 franchised territories open (4 franchisees).",
        ],
        "positives": [
            "Most detailed P&amp;L in the lawn cohort: EBITDA with imputed fees.",
            "Company-owned locations prove 16&ndash;19% EBITDA at scale.",
            "Sister brand to Mosquito Squad &mdash; established parent (Authority Brands).",
            "Lowest headline royalty in the lawn cohort (7% flat).",
            "80% customer retention, 71% sales conversion, $810 avg customer value.",
            "AB Inc. guarantees franchisor&rsquo;s obligations under franchise agreements.",
        ],
        "fee_caveats": [{
            "title": "Effective royalty is 14%, not 7%",
            "text": "The 5% call center fee (charged as % of Gross Revenue, not flat monthly) "
                    "plus 2% brand fund bring total franchisor percentage take to 14% before any "
                    "marketing or technology costs.",
        }],
        "health_flag": {
            "title": "Micro-system",
            "text": "Only 7 franchised territories operated by 4 franchisees. Company-owned "
                    "data is strong but franchise track record is non-existent.",
        },
    },
    # --- Residential Cleaning cohort ---
    "merry-maids": {
        "parent_short": "Roark Capital / ServiceMaster",
        "ownership": "PE-backed",
        "royalty_display": "7% / 6% / 5%",
        "royalty_context": "incentive tiers (discretionary, may be discontinued)",
        "marketing_floor": "$0 + 2% of Gross Sales",
        "marketing_context": "2% total (1.3% ad fund + 0.7% local) &mdash; lowest in cohort",
        "disclosure_quality": "Mixed",
        "disclosure_rank": "4th of 7",
        "disclosure_narrative": (
            "Item 19 provides average and median gross sales for &ldquo;Qualified Franchises&rdquo; "
            "($487K avg, $427K median) but only 306 of 802 units qualify. 419 &ldquo;Legacy "
            "Franchises&rdquo; are reported separately at lower averages ($256K). Wisconsin risk "
            "disclosure flags the turnover rate as a specific risk factor."
        ),
        "watchouts": [
            "System contracted by 187 units over 3 years (989 &rarr; 802, &minus;18.9%). "
            "Contraction is accelerating: &minus;43, &minus;62, &minus;82.",
            "73 units ceased operations in 2024 alone &mdash; highest single-year loss in the cohort.",
            "Only 306 of 802 units qualify for the Item 19 &ldquo;Qualified&rdquo; tier. "
            "419 Legacy Franchises have lower averages and were on different fee structures.",
            "Wisconsin risk disclosure explicitly flags turnover rate as a buyer risk.",
            "Incentive royalty tiers (6% at $400K+, 5% at $500K+) are discretionary and "
            "may be discontinued at any time.",
        ],
        "positives": [
            "Largest system in the cleaning cohort (802 units) with 46 years of history.",
            "Lowest marketing burden in the cohort: 2% total (1.3% ad fund + 0.7% local).",
            "Qualified Franchise average gross sales of $487,441 (median $427,425).",
            "Simple fee structure with low technology cost ($499/month).",
            "Lowest initial investment in the cohort ($127K&ndash;$170K).",
        ],
        "fee_caveats": [{
            "title": "Incentive tiers are not guaranteed",
            "text": "The reduced royalty rates (6% at $400K+, 5% at $500K+) are discretionary "
                    "incentive programs that the franchisor can discontinue at any time. "
                    "Base rate is 7%.",
        }],
        "health_flag": {
            "title": "Accelerating contraction",
            "text": "System lost 187 units in 3 years (&minus;18.9%), with losses accelerating "
                    "each year. 73 units ceased operations in 2024 alone. Wisconsin risk "
                    "disclosure flags the turnover rate.",
        },
    },
    "molly-maid": {
        "parent_short": "KKR / Neighborly",
        "ownership": "PE-backed (Neighborly SPV)",
        "royalty_display": "6.5% / 6% / 5.5% / 5% / 4.5% / 4% / 3.5% / 3%",
        "royalty_context": "8-tier marginal &mdash; declines to 3% above $2.8M",
        "marketing_floor": "2% + $1/TH/yr local",
        "marketing_context": "moderate (MAP 2% + declining per-TH local)",
        "disclosure_quality": "Strong",
        "disclosure_rank": "2nd of 7",
        "disclosure_narrative": (
            "Item 19 provides 4 parts: per-cleaning revenue ($173 avg), per-TH penetration, "
            "91% recurring customer rate, and YoY growth distribution. 79% of franchisees grew "
            "in 2024. Does not disclose absolute total gross sales per franchisee. 25 businesses "
            "that closed during 2024 excluded."
        ),
        "watchouts": [
            "System has contracted every year for 3 consecutive years "
            "(501 &rarr; 481 &rarr; 464 &rarr; 448, &minus;10.6%).",
            "Item 19 does not disclose absolute total gross sales per franchisee &mdash; only "
            "per-cleaning and per-TH metrics. Revenue comparisons require inference.",
            "Technology costs total ~$463/month ($58 ZorWare + $405 CLEO/ServiceTitan).",
            "Same Neighborly/KKR SPV structure as Mosquito Joe &mdash; securitization layers.",
            "Minimum License Fees apply from Year 2 based on TH in territory.",
        ],
        "positives": [
            "Tiered marginal royalty genuinely rewards growth: 6.5% on first $500K declining "
            "to 3% above $2.8M. Most favorable royalty structure in the cleaning cohort at scale.",
            "91% recurring customer rate &mdash; one of the highest in any franchise vertical.",
            "79% of franchisees grew YoY in 2024. Only 4% declined more than 10%.",
            "Per-cleaning revenue of $173 average ($170 median) is a useful unit metric.",
            "45-year system history (founded 1979, US franchising since 1984).",
        ],
        "fee_caveats": [{
            "title": "Minimum License Fees",
            "text": "Minimum fees based on TH in territory apply from Year 2. At low revenue, "
                    "these minimums may exceed the percentage-based royalty.",
        }],
        "health_flag": {
            "title": "Steady contraction",
            "text": "System has lost 53 units over 3 years (&minus;10.6%). Contraction is "
                    "consistent but slowing slightly (&minus;20, &minus;17, &minus;16).",
        },
    },
    "cleaning-authority": {
        "parent_short": "Apax Partners / Authority Brands",
        "ownership": "PE-backed",
        "royalty_display": "6% / 5% / 4%",
        "royalty_context": "tiered &mdash; different thresholds for Enterprise vs Hometown",
        "marketing_floor": "1% brand fund + DHH-based local",
        "marketing_context": "low &mdash; brand fund capped at $200/wk",
        "disclosure_quality": "Best in cohort",
        "disclosure_rank": "1st of 7",
        "disclosure_narrative": (
            "Richest Item 19 in the cleaning cohort: 206 Enterprise Market territories with "
            "average gross revenue by thirds (Top $2.45M, Middle $1.29M, Lower $638K), "
            "average price per clean ($165&ndash;$173), and average COGS (61&ndash;63%). "
            "The only cleaning brand providing revenue-tier breakdowns with COGS."
        ),
        "watchouts": [
            "TCAF lawsuit (The Cleaning Authority Franchisee Association) alleges marketing "
            "fund opacity, above-market vendor pricing, and inhibition of association rights. "
            "Pending as of filing.",
            "Two separate investment tables (Enterprise vs Hometown Market) make direct comparison "
            "with single-table brands less straightforward.",
            "Brand fund capped at $200/week &mdash; but local marketing fee is DHH-based, "
            "not revenue-based, creating unpredictable cost.",
            "Royalty thresholds differ between Enterprise and Hometown markets.",
        ],
        "positives": [
            "Only growing system among the large cleaning franchises: +24 units over 3 years (+11.3%).",
            "Turnover rate dropped from 10.6% (2023) to 4.1% (2024) &mdash; best improvement in cohort.",
            "Richest Item 19 disclosure: revenue by thirds, COGS percentages, price per clean.",
            "Top-third Enterprise territories average $2.45M gross revenue.",
            "Sister brand to Mosquito Squad &mdash; established Authority Brands platform.",
            "Lowest initial investment in the cohort ($93K&ndash;$147K Enterprise).",
        ],
        "fee_caveats": [{
            "title": "Dual market structure",
            "text": "Enterprise and Hometown markets have different fee thresholds, investment "
                    "ranges, and territory definitions. Comparison data uses Enterprise Market.",
        }],
        "health_flag": None,
    },
    "the-maids": {
        "parent_short": "Gladstone Management Corp",
        "ownership": "private",
        "royalty_display": "6.9% / 5.9% / 4.9% / 3.9%",
        "royalty_context": "non-marginal tiers &mdash; entire week at one rate",
        "marketing_floor": "2% + 0.25% + $2,500+/mo local",
        "marketing_context": "moderate-to-high (2.25% + mandatory local spend)",
        "disclosure_quality": "Good",
        "disclosure_rank": "3rd of 7",
        "disclosure_narrative": (
            "Item 19 provides 3 tables: per-territory revenue ($386K avg, $306K median), "
            "company-owned P&amp;L showing 15.5% net margin ($220K/office average), and "
            "detailed expense categories. One of only two cleaning brands disclosing "
            "company-owned profitability."
        ),
        "watchouts": [
            "Franchisor financial condition is flagged as a special risk in state disclosures. "
            "Net loss of $(3.86M) in FY2025, member&rsquo;s deficit of $(3.55M), "
            "$28.56M in related-party debt.",
            "$19,900 mandatory SMART Start Package on top of $60,000 franchise fee.",
            "Royalty is non-marginal (entire week at one rate based on threshold). "
            "Crossing a threshold changes the rate on ALL revenue, not just the increment.",
            "Minimum royalty ($150&ndash;$250/week) applies if percentage doesn&rsquo;t meet floor.",
            "Fiscal year ends September 30, making calendar-year comparisons non-standard.",
        ],
        "positives": [
            "Company-owned P&amp;L shows 15.5% average net margin ($220K/office) &mdash; "
            "one of only two cleaning brands proving profitability at the franchisor level.",
            "47-year system history (founded 1979). Longest track record in the cohort.",
            "System contraction slowing: franchised outlets stabilized at 338 in FY2025.",
            "Per-territory average revenue of $386K with $306K median.",
            "Privately held (Gladstone) &mdash; no PE securitization layers.",
        ],
        "fee_caveats": [{
            "title": "Non-marginal royalty structure",
            "text": "Unlike marginal/progressive tiers, the entire week&rsquo;s revenue is "
                    "charged at whatever rate the threshold dictates. Crossing from 6.9% to "
                    "5.9% saves on ALL sales, not just the increment.",
        }],
        "health_flag": {
            "title": "Franchisor financial condition",
            "text": "State-required risk disclosure flags financial condition. Net loss of "
                    "$(3.86M), member&rsquo;s deficit of $(3.55M), significant related-party debt.",
        },
    },
    "maidpro": {
        "parent_short": "The Riverside Company / Threshold Brands",
        "ownership": "PE-backed",
        "royalty_display": "6%",
        "royalty_context": "flat rate &mdash; simplest structure in cohort",
        "marketing_floor": "2% brand fund",
        "marketing_context": "low (8% total ongoing = royalty + brand fund only)",
        "disclosure_quality": "Good",
        "disclosure_rank": "5th of 7",
        "disclosure_narrative": (
            "Item 19 provides system-wide average gross consumer sales of $461,941 "
            "(median $397,548) across 231 outlets with quintile breakdowns. Wide dispersion: "
            "Q1 avg $958K vs Q4 avg $134K. Jobs data also provided."
        ),
        "watchouts": [
            "Franchise Option Program creates a bifurcated royalty structure: standard 6% vs "
            "10% for franchisees who entered through the option program.",
            "Technology fee of $500/month ($6,000/year) is above average for the cohort.",
            "Table 1 in the FDD contains a year-label typo (third row labeled &ldquo;2023&rdquo; "
            "should be &ldquo;2024&rdquo;) &mdash; document quality blemish.",
            "Confidentiality clauses restrict some former franchisees from speaking openly.",
            "Wide performance dispersion: Q1 avg $958K vs Q4 avg $134K "
            "(7:1 ratio between top and bottom quintile).",
        ],
        "positives": [
            "Simplest fee structure in the cohort: 6% flat royalty + 2% brand fund = 8% total. "
            "No tiered schedules, no mandatory local marketing minimums.",
            "System stabilized in 2024 (0 net change) after 3 years of mild contraction.",
            "Turnover rate improving: 15.0% &rarr; 12.4% &rarr; 8.4% over 3 years.",
            "Average gross sales of $461,941 with useful quintile breakdowns.",
            "Transfer fee of only $5,000 &mdash; lowest in the cohort.",
        ],
        "fee_caveats": [{
            "title": "Franchise Option Program",
            "text": "Franchisees who entered through the $0-down Franchise Option Program pay "
                    "10% royalty instead of 6%. This affects per-brand fee comparisons.",
        }],
        "health_flag": None,
    },
    "two-maids": {
        "parent_short": "JM Family Enterprises / Home Franchise Concepts",
        "ownership": "PE-backed",
        "royalty_display": "7% / 6% / 5% / 4%",
        "royalty_context": "marginal tiered by monthly revenue",
        "marketing_floor": "2% national + $2,500&ndash;$3,000/mo local",
        "marketing_context": "moderate-to-high (2% + $30K&ndash;$36K/yr local)",
        "disclosure_quality": "Strong",
        "disclosure_rank": "2nd of 7",
        "disclosure_narrative": (
            "Richest Item 19 in terms of breadth: 12 charts covering 5 quintiles of territories "
            "open 2+ years (86 territories), new territories (1&ndash;2 years, 17), multi-unit "
            "owners (20), gross margins (52% top quintile), and labor efficiency."
        ),
        "watchouts": [
            "Technology fee of $650/month per territory ($7,800/year) &mdash; "
            "highest tech fee in the cleaning cohort.",
            "Transfer fee is complex and expensive: $24,950&ndash;$50,000 for new buyers, "
            "plus potential $15,000 referral fee.",
            "Mandatory franchisor-directed local advertising of $2,500&ndash;$3,000/month "
            "($30K&ndash;$36K/year) on top of 2% national fund.",
            "Minimum royalty of $1,500/month applies from Year 2.",
        ],
        "positives": [
            "Fastest growing system in the cleaning cohort: +52 units over 3 years (+56.5%). "
            "2024 saw 32 openings vs only 6 exits.",
            "Top quintile territories average $1.17M gross revenue with 52% gross margin.",
            "Most detailed Item 19 in the cohort: 12 charts, quintile breakdowns, multi-unit data.",
            "Tiered royalty rewards growth: drops from 7% to 4% above $90K/month.",
            "21 signed-but-not-opened agreements + 35 projected for 2025 &mdash; strong pipeline.",
        ],
        "fee_caveats": [{
            "title": "Local advertising is franchisor-directed",
            "text": "The $2,500&ndash;$3,000/month local advertising is managed by the franchisor, "
                    "not discretionary. Combined with 2% national fund, total marketing "
                    "costs are $32K&ndash;$42K/year at any revenue level.",
        }],
        "health_flag": None,
    },
    "maid-right": {
        "parent_short": "Premium Service Brands / AE Capital",
        "ownership": "founder-led",
        "royalty_display": "6%",
        "royalty_context": "flat rate, $150/week minimum",
        "marketing_floor": "2% + $50/wk + contact center 2%",
        "marketing_context": "moderate headline but high fixed weekly minimums",
        "disclosure_quality": "Below average",
        "disclosure_rank": "6th of 7",
        "disclosure_narrative": (
            "Item 19 includes only 18 of 39 franchisees (46%). Average $520K, median $356K. "
            "Strong maturity curve (36+ months avg $782K, 86% recurring). But 21 franchisees "
            "excluded &mdash; highest exclusion rate in the cohort."
        ),
        "watchouts": [
            "CEO Paul Flick barred from California franchise sales for 36 months due to "
            "regulatory actions at affiliate 360 Painting.",
            "17 disclosed litigation actions against affiliates (360 Painting, ProLift Garage Doors) "
            "across multiple states for FDD disclosure failures.",
            "System contracted sharply in 2024: &minus;9 units (&minus;20.5%). "
            "First 6 terminations appeared after 2 years of none.",
            "Turnover rates are the highest in the cohort: 20.8%, 37.8%, 38.6% over 3 years.",
            "Highest initial investment in the cohort ($147K&ndash;$219K). "
            "Effective ongoing fixed fees (~$15,340/year in weekly minimums) are substantial.",
            "State risk disclosures flag franchisor financial condition, short operating history, "
            "and significant number of unopened franchises.",
        ],
        "positives": [
            "86.4% of revenue from recurring service &mdash; strong business predictability.",
            "Mature franchisees (36+ months) average $782K gross revenue.",
            "Simple flat 6% royalty with no tiered complexity.",
            "10 franchise agreements signed but not yet opened as of year-end 2024 "
            "&mdash; pipeline suggests continued interest.",
        ],
        "fee_caveats": [{
            "title": "Fixed weekly minimums add up",
            "text": "Technology ($210/wk), accounting ($85/wk), contact center ($50&ndash;$220/wk "
                    "escalating) add ~$295&ndash;$515/week in fixed costs regardless of revenue.",
        }],
        "health_flag": {
            "title": "CEO regulatory history",
            "text": "Paul Flick (CEO/founder) was barred from California franchise sales for "
                    "36 months. 17 affiliate litigation actions for FDD disclosure failures "
                    "across multiple states.",
        },
    },
}

BRAND_META_DESCRIPTIONS: dict[str, str] = {
    "mosquito-authority": "Review Mosquito Authority franchise cost, ongoing fees, system health, and key risks using regulator-source data before deciding whether to buy.",
    "mosquito-hunters": "Review Mosquito Hunters franchise cost, fee structure, system health, and major buyer watchouts using public franchise disclosure data.",
    "mosquito-joe": "Review Mosquito Joe franchise fees, startup cost, system health, and key risks using public disclosure data for serious franchise buyers.",
    "mosquito-shield": "Review Mosquito Shield franchise cost, ongoing fees, system health signals, and key buyer risks before committing capital.",
    "mosquito-squad": "Review Mosquito Squad franchise cost, royalty structure, system health, and major decision factors using regulator-source data.",
    "mosquito-sheriff": "Review Mosquito Sheriff franchise cost, fees, system size, and key risks using regulator-source FDD data for prospective franchise buyers.",
    "mosquitonix": "Review MosquitoNix franchise cost, fee structure, system health, and buyer watchouts using 2025 FDD data from Wisconsin DFI.",
    "lawn-doctor": "Review Lawn Doctor franchise cost, ongoing fees, system health, and key risks using regulator-source FDD data before investing.",
    "weed-man": "Review Weed Man franchise cost, royalty structure, system health, and key decision factors using 2025 FDD data.",
    "spring-green": "Review Spring-Green franchise cost, fees, system health, and buyer watchouts using regulator-source FDD data.",
    "naturalawn": "Review NaturaLawn franchise cost, fee burden, system health, and key risks for organic lawn care franchise buyers.",
    "lawn-pride": "Review Lawn Pride franchise cost, fees, system growth, and key watchouts using 2025 FDD data from Wisconsin DFI.",
    "lawn-squad": "Review Lawn Squad franchise cost, fee structure, system health, and major buyer risks using regulator-source FDD data.",
    "merry-maids": "Review Merry Maids franchise cost, fees, system health, and contraction risk using regulator-source FDD data.",
    "molly-maid": "Review Molly Maid franchise cost, tiered royalty structure, system health, and key risks using 2025 FDD data.",
    "cleaning-authority": "Review The Cleaning Authority franchise cost, system growth, COGS data, and key buyer factors using regulator-source FDD data.",
    "the-maids": "Review The Maids franchise cost, company-owned P&L, system health, and franchisor financial condition using 2026 FDD data.",
    "maidpro": "Review MaidPro franchise cost, simple fee structure, system health, and key risks using 2025 FDD data.",
    "two-maids": "Review Two Maids franchise cost, growth trajectory, fee structure, and key decision factors using 2025 FDD data.",
    "maid-right": "Review Maid Right franchise cost, system health, regulatory history, and key buyer risks using 2025 FDD data.",
}

BRAND_SHORT_NAMES: dict[str, str] = {
    "maid-right": "Maid Right",
    "molly-maid": "Molly Maid",
    "merry-maids": "Merry Maids",
    "the-maids": "The Maids",
    "two-maids": "Two Maids",
    "weed-man": "Weed Man",
    "lawn-doctor": "Lawn Doctor",
    "lawn-pride": "Lawn Pride",
    "lawn-squad": "Lawn Squad",
}

BRAND_DIFFERENTIATORS: dict[str, str] = {
    "mosquito-authority": "Lowest fee burden",
    "mosquito-hunters": "3-brand license",
    "mosquito-joe": "Highest marketing spend",
    "mosquito-shield": "Fastest growth",
    "mosquito-squad": "Highest avg revenue",
    "mosquito-sheriff": "Lowest investment",
    "mosquitonix": "Holiday lighting add-on",
    "lawn-doctor": "Largest system, 58yr track record",
    "weed-man": "Lowest fee burden",
    "spring-green": "Privately held, 48yr history",
    "naturalawn": "Organic-based premium",
    "lawn-pride": "Explosive growth (Neighborly)",
    "lawn-squad": "Detailed P&L disclosure",
    "merry-maids": "Largest system, lowest fees",
    "molly-maid": "Best tiered royalty at scale",
    "cleaning-authority": "Only growing large brand",
    "the-maids": "Company-owned P&L disclosed",
    "maidpro": "Simplest fee structure",
    "two-maids": "Fastest growth (+57%)",
    "maid-right": "Highest recurring revenue %",
}

# Stripe Payment Links — add real URLs as reports go live.
STRIPE_PAYMENT_LINKS: dict[str, str | None] = {
    "mosquito-authority": "https://buy.stripe.com/dRmbJ3ewz1PY6E0ejCawo01",
    "mosquito-hunters": "https://buy.stripe.com/fZuaEZagj66e5zWa3mawo02",
    "mosquito-joe": "https://buy.stripe.com/dRm4gBfADbqy9Qc0sMawo03",
    "mosquito-shield": "https://buy.stripe.com/5kQ14p4VZ8emfaw7Veawo04",
    "mosquito-squad": "https://buy.stripe.com/7sYbJ39cfcuC3rOejCawo05",
    "mosquito-sheriff": None,
    "mosquitonix": None,
    "lawn-doctor": "https://buy.stripe.com/7sY28tewzcuCbYkejCawo06",
    "weed-man": None,
    "spring-green": "https://buy.stripe.com/eVq28t9cf9iq7I4fnGawo07",
    "naturalawn": "https://buy.stripe.com/4gM6oJ88bfGO3rO0sMawo08",
    "lawn-pride": None,
    "lawn-squad": None,
    "merry-maids": "https://buy.stripe.com/bJecN7gEHdyG0fC4J2awo09",
    "molly-maid": "https://buy.stripe.com/eVqfZjcor1PY2nK7Veawo0a",
    "cleaning-authority": "https://buy.stripe.com/9B628tcor9iq6E02AUawo0b",
    "the-maids": "https://buy.stripe.com/4gMdRb4VZgKS7I4dfyawo0c",
    "maidpro": "https://buy.stripe.com/7sYcN7bknamuaUg8Ziawo0d",
    "two-maids": "https://buy.stripe.com/dRm5kFfADcuC7I40sMawo0e",
    "maid-right": "https://buy.stripe.com/7sY14pgEH66e6E0b7qawo0f",
}

# Mosquito-specific cost page editorial
MOSQUITO_FEE_NOTES: dict[str, str] = {
    "Mosquito Authority": "Hometown ($25K) vs Full-Size ($45K) tiers",
    "Mosquito Hunters": "$50K license + $57K training/supply. Highest fee in cohort.",
    "Mosquito Joe": "Standard single territory. Discounts available.",
    "Mosquito Shield": "First territory. Multi-territory discounts available.",
    "Mosquito Squad": "Standard territory (350K\u2013500K pop). Micro territory $35K.",
    "Mosquito Sheriff": "$40K franchise fee + $27.5K Starter Kit. $75K to franchisor at signing.",
    "MosquitoNix": "$49K franchise fee + $7K training + $13.5K Opening Package. VetFran $2.5K off.",
    "Lawn Doctor": "$50K license + $70.6K training/supply + $6.4K equipment deposits. Highest in lawn cohort.",
    "Weed Man": "$30K\u2013$50K based on territory population. Seasonal early-payment discounts (5\u201310%).",
    "Spring-Green": "$45K franchise fee + $35K marketing campaign + $16.5K property data.",
    "NaturaLawn": "$39.5K standard. Discounts for existing lawn care operators.",
    "Lawn Pride": "$0.89/Targeted Household. Typical $40K\u2013$62K. Neighborly discounts available.",
    "Lawn Squad": "$45K standard. Authority Brands franchisees: $15K. Heavy discounting in 2024.",
}

MOSQUITO_RESERVES: dict[str, str] = {
    "Mosquito Squad": "12 months",
    "NaturaLawn": "6 months",
}

MOSQUITO_ROYALTY: dict[str, tuple[str, str]] = {
    "Mosquito Authority": ("10%", "Flat rate. Min $500/mo at Year 5."),
    "Mosquito Hunters": ("10%", "Flat rate. Plus 15% on out-of-territory revenue."),
    "Mosquito Joe": ("10% / 7%", "10% on first $500K, 7% above. Rewards growth."),
    "Mosquito Shield": ("8%", "Flat rate \u2014 lowest in cohort. Min Gross Sales shortfall penalty."),
    "Mosquito Squad": ("10% / 9% / 8%", "Triple-tiered by revenue bracket. Min $3K/mo at Year 9+."),
    "Mosquito Sheriff": ("10%", "Flat rate. Min $2K/mo at Year 6+."),
    "MosquitoNix": ("10% / 9% / 8% / 7%", "Four-tiered by revenue. Most aggressive scale discount."),
    "Lawn Doctor": ("10%", "Flat rate on Net Revenues. Plus 15% on out-of-territory."),
    "Weed Man": ("6.5% / 5.5%", "Tiered at $1M. Lowest rate in lawn cohort."),
    "Spring-Green": ("10% / 9% / 8%", "Triple-tiered by revenue bracket."),
    "NaturaLawn": ("9% / 7%", "Reduces to 7% at renewal if $500K+ sustained."),
    "Lawn Pride": ("8%", "Flat rate. Roll-In franchisees get reduced 4\u20136%."),
    "Lawn Squad": ("7%", "Flat rate \u2014 lowest headline. But +5% call center = 12% effective."),
}

MOSQUITO_ROYALTY_ORDER = [
    "Mosquito Shield", "Mosquito Squad", "Mosquito Joe",
    "Mosquito Authority", "Mosquito Hunters", "Mosquito Sheriff", "MosquitoNix",
    "Lawn Squad", "Lawn Pride", "Weed Man", "NaturaLawn",
    "Spring-Green", "Lawn Doctor",
]

MOSQUITO_INVESTMENT_DETAILS: list[dict] = [
    {"brand_name": "Mosquito Authority", "detail": "$15K&ndash;$25K pre-opening marketing. Vehicle $0&ndash;$30K (zero if owned). 3-mo reserves."},
    {"brand_name": "Mosquito Hunters", "detail": "<strong>$57K mandatory training/supply fee</strong> (on top of $50K license). $6K&ndash;$14K holiday lighting inventory. 3-mo reserves."},
    {"brand_name": "Mosquito Joe", "detail": "<strong>$72K in mandatory marketing</strong> ($37K DMP + $35K local). These two items alone are nearly half the total. 3-mo reserves."},
    {"brand_name": "Mosquito Shield", "detail": "$23.6K mandatory Starter Package. $35K&ndash;$50K first-year local advertising. 3-mo reserves."},
    {"brand_name": "Mosquito Squad", "detail": "$9.5K business outfitting + $4K&ndash;$9.5K truck outfitting. <strong>12-month reserves ($84K&ndash;$117K)</strong>."},
    {"brand_name": "Mosquito Sheriff", "detail": "<strong>$75K to franchisor at signing</strong> ($40K fee + $27.5K Starter Kit + $5K vehicle + $2.5K tools). 3-mo reserves only $1K&ndash;$1.6K."},
    {"brand_name": "MosquitoNix", "detail": "$24K Market Entry Campaign + $13.5K Opening Package. Vehicle 10% down on $62K&ndash;$64K lease. 3-mo reserves."},
    {"brand_name": "Lawn Doctor", "detail": "<strong>$70.6K mandatory training/supply</strong> (on top of $50K license). $6K&ndash;$14K holiday lighting inventory. 3-mo reserves."},
    {"brand_name": "Weed Man", "detail": "$4.6K training + $6.25K software/hardware. $25K&ndash;$30K reserves (3 months). Lowest total in lawn cohort."},
    {"brand_name": "Spring-Green", "detail": "<strong>$35K Initial Marketing Campaign + $16.5K Property Data Fee</strong>. $5.5K equipment (20% down on lease). 3-mo reserves."},
    {"brand_name": "NaturaLawn", "detail": "<strong>$60K&ndash;$80K annual marketing</strong> is the largest line item. Plus $150K&ndash;$250K credit line required. <strong>6-mo reserves</strong>."},
    {"brand_name": "Lawn Pride", "detail": "<strong>$81.7K&ndash;$146K reserves (3 months)</strong> includes $80K Year 1 Local Marketing Spend. Highest reserves in cohort."},
    {"brand_name": "Lawn Squad", "detail": "$6K call center setup fee. $5.8K&ndash;$18K vehicle. $1.17K/mo total technology costs. 3-mo reserves."},
]


# ---------------------------------------------------------------------------
# Fee burden page context (requires fee model)
# ---------------------------------------------------------------------------

@dataclass
class FeeRow:
    brand: str
    royalty: float
    marketing: float
    tech_other: float
    total: float
    pct_of_revenue: float


def build_fee_context(fee_model: dict, brands: dict[str, dict]) -> dict:
    """Build context for the fee burden comparison page."""
    revenue_levels = fee_model["revenue_levels"]

    fee_data: dict[int, list[FeeRow]] = {}
    for level in revenue_levels:
        rows = []
        for r in fee_model["results"]:
            if r["gross_revenue"] == level:
                tech_other = (
                    r["technology"] + r["call_center"] + r["convention"]
                    + r["website_digital"] + r["software_vendor"]
                    + r["bookkeeping"] + r["sales_center"]
                )
                rows.append(FeeRow(
                    brand=r["brand"],
                    royalty=r["royalty"],
                    marketing=r["marketing"],
                    tech_other=tech_other,
                    total=r["total"],
                    pct_of_revenue=r["pct_of_revenue"],
                ))
        rows.sort(key=lambda x: x.total)
        fee_data[level] = rows

    # 10-year burden at $300K — derive midpoints from brand data
    investment_midpoints = {
        data["brand"]["brand_name"]: normalize_item7(data)[2]
        for data in brands.values()
    }

    ten_year_data = []
    for r in fee_model["results"]:
        if r["gross_revenue"] == 300000:
            midpoint = investment_midpoints.get(r["brand"])
            if midpoint is None:
                continue
            ten_year = r["total"] * 10
            ratio = round(ten_year / midpoint, 1)
            ten_year_data.append({
                "brand": r["brand"],
                "investment_midpoint": midpoint,
                "ten_year_burden": ten_year,
                "ratio": ratio,
            })
    ten_year_data.sort(key=lambda x: x["ratio"])

    return {
        "revenue_levels": revenue_levels,
        "fee_data": fee_data,
        "ten_year_data": ten_year_data,
    }


# ---------------------------------------------------------------------------
# System health page context
# ---------------------------------------------------------------------------

def build_health_context(brands: dict[str, dict], brand_slug_map: dict[str, str]) -> dict:
    """Build context for the system health trajectory page. Works for any cohort."""

    brand_health = []
    for slug, data in brands.items():
        name = data["brand"]["brand_name"]
        years = data["raw"]["item_20_outlet_summary"]["years_reported"]
        derived = data["derived"]

        sorted_years = sorted(years, key=lambda y: y["year"])
        y_last = sorted_years[-1]

        # Net growth
        growth_vals = {g["year"]: g["value"] for g in derived["net_unit_growth"]}

        # 3-year aggregates
        opened_3yr = sum(y["opened"] for y in years)
        terminated_3yr = sum(y["closed"] for y in years)
        ceased_nr_3yr = sum(
            (y.get("ceased_operations_other") or 0) + (y.get("non_renewals") or 0)
            for y in years
        )
        transferred_3yr = sum(y.get("transferred") or 0 for y in years)

        # Trajectory — use override if available, otherwise auto-derive
        if name in TRAJECTORY_OVERRIDES:
            trajectory, tclass = TRAJECTORY_OVERRIDES[name]
        else:
            trajectory, tclass = derive_trajectory(growth_vals)

        franchised_end = y_last["total_outlets_end"] - (y_last.get("company_owned_end") or 0)
        company_owned_end = y_last.get("company_owned_end") or 0

        # Growth values by year
        growth_by_year = []
        for yr in sorted_years:
            growth_by_year.append({
                "year": yr["year"],
                "value": growth_vals.get(yr["year"], 0),
            })

        brand_health.append({
            "brand_name": name,
            "slug": slug,
            "franchised_end": franchised_end,
            "company_owned_end": company_owned_end,
            "total_end": y_last["total_outlets_end"],
            "system_age": derived["system_age_years"],
            "growth_by_year": growth_by_year,
            "growth_total": sum(g["value"] for g in growth_by_year),
            "trajectory": trajectory,
            "trajectory_class": tclass,
            "opened_3yr": opened_3yr,
            "terminated_3yr": terminated_3yr,
            "ceased_nonrenewed_3yr": ceased_nr_3yr,
            "transferred_3yr": transferred_3yr,
        })

    brands_by_size = sorted(brand_health, key=lambda x: x["total_end"], reverse=True)
    brands_by_growth = sorted(brand_health, key=lambda x: x["growth_total"], reverse=True)

    # Last-year attrition
    attrition = []
    for slug, data in brands.items():
        name = data["brand"]["brand_name"]
        years = data["raw"]["item_20_outlet_summary"]["years_reported"]
        y_last = sorted(years, key=lambda y: y["year"])[-1]

        terminated = y_last["closed"]
        non_renewals = y_last.get("non_renewals") or 0
        ceased = y_last.get("ceased_operations_other") or 0
        total = terminated + non_renewals + ceased
        start = y_last["total_outlets_start"]
        pct = round((total / start) * 100, 1) if start > 0 else 0

        attrition.append({
            "brand_name": name,
            "slug": slug,
            "terminated": terminated,
            "non_renewals": non_renewals,
            "ceased": ceased,
            "total": total,
            "start": start,
            "pct": pct,
        })

    attrition.sort(key=lambda x: x["pct"])

    # Reporting years from first brand
    sample_years = sorted(
        brands[next(iter(brands))]["raw"]["item_20_outlet_summary"]["years_reported"],
        key=lambda y: y["year"],
    )
    reporting_years = [y["year"] for y in sample_years]

    return {
        "brands_by_size": brands_by_size,
        "brands_by_growth": brands_by_growth,
        "attrition_last_year": attrition,
        "reporting_years": reporting_years,
        "last_year": reporting_years[-1],
    }


# ---------------------------------------------------------------------------
# Cost to enter page context
# ---------------------------------------------------------------------------

def build_cost_context(brands: dict[str, dict], brand_slug_map: dict[str, str]) -> dict:
    """Build context for the cost to enter page. Works for any cohort."""

    fee_data = []
    investment_data = []
    royalty_data = []

    for slug, data in brands.items():
        name = data["brand"]["brand_name"]
        item5 = data["raw"]["item_5_initial_fees"]["initial_franchise_fee"]
        item6 = data["raw"]["item_6_other_fees"]
        inv_low, inv_high, inv_mid = normalize_item7(data)

        # Franchise fee display
        if item5["value"] is not None:
            fee_display = f"${item5['value']:,.0f}"
        elif item5.get("range_low") is not None:
            fee_display = f"${item5['range_low']:,.0f}\u2013${item5['range_high']:,.0f}"
        else:
            fee_display = "N/A"

        fee_sort_val = item5["value"] or item5.get("range_high") or 0

        fee_data.append({
            "brand_name": name,
            "fee_display": fee_display,
            "fee_notes": MOSQUITO_FEE_NOTES.get(name, ""),
            "fee_sort": fee_sort_val,
        })

        # Investment range
        reserves = MOSQUITO_RESERVES.get(name, "3 months")

        investment_data.append({
            "brand_name": name,
            "total_low": inv_low,
            "total_high": inv_high,
            "midpoint": inv_mid,
            "reserves_period": reserves,
            "caveat": name in MOSQUITO_RESERVES,
        })

        # Royalty — editorial or auto-derived
        if name in MOSQUITO_ROYALTY:
            rate_display, structure = MOSQUITO_ROYALTY[name]
        else:
            rate_display, structure = derive_royalty_display(item6)

        royalty_data.append({
            "brand_name": name,
            "rate_display": rate_display,
            "structure": structure,
        })

    brands_by_fee = sorted(fee_data, key=lambda x: x["fee_sort"])
    brands_by_investment = sorted(investment_data, key=lambda x: x["midpoint"])

    def royalty_sort_key(x: dict) -> int:
        if x["brand_name"] in MOSQUITO_ROYALTY_ORDER:
            return MOSQUITO_ROYALTY_ORDER.index(x["brand_name"])
        try:
            first_num = float(x["rate_display"].split("%")[0].split("/")[0].strip())
            return 100 + int(first_num * 10)
        except (ValueError, IndexError):
            return 999

    royalty_data.sort(key=royalty_sort_key)

    return {
        "brands_by_fee": brands_by_fee,
        "brands_by_investment": brands_by_investment,
        "royalty_data": royalty_data,
        "investment_details": [
            d for d in MOSQUITO_INVESTMENT_DETAILS
            if d["brand_name"] in brand_slug_map
        ],
    }


# ---------------------------------------------------------------------------
# Brand page context
# ---------------------------------------------------------------------------

@dataclass
class BrandFeeLevel:
    """Fee data for a single brand at a single revenue level."""
    revenue: int
    total: float
    pct: float
    rank: int


def build_brand_contexts(
    brands: dict[str, dict],
    brand_slugs: list[str],
    fee_model: Optional[dict],
    brand_slug_map: dict[str, str],
    cohort: dict,
) -> list[dict]:
    """Build context for each brand page. Handles missing editorial and fee data."""
    fee_rankings: dict[int, list[dict]] = {}
    if fee_model:
        for level in fee_model["revenue_levels"]:
            level_data = [r for r in fee_model["results"] if r["gross_revenue"] == level]
            level_data.sort(key=lambda x: x["total"])
            fee_rankings[level] = level_data

    cohort_size = len(brand_slugs)
    brand_contexts = []

    for slug in brand_slugs:
        data = brands[slug]
        editorial = BRAND_EDITORIAL.get(slug)
        has_editorial = editorial is not None
        has_fee_model = fee_model is not None
        brand_name = data["brand"]["brand_name"]
        derived = data["derived"]
        years = data["raw"]["item_20_outlet_summary"]["years_reported"]
        item6 = data["raw"]["item_6_other_fees"]
        sorted_years = sorted(years, key=lambda y: y["year"])
        y_last = sorted_years[-1]

        franchised_end = y_last["total_outlets_end"] - (y_last.get("company_owned_end") or 0)

        inv_low, inv_high, _ = normalize_item7(data)
        investment_range = f"${inv_low // 1000}K\u2013${inv_high // 1000}K"
        investment_note = "Item 7 range"
        if brand_name in MOSQUITO_RESERVES:
            investment_note = "includes 12-mo reserves"

        # Fee burden & ranking
        fee_burden_300k = None
        fee_rank_300k = None
        fee_by_level: list[BrandFeeLevel] = []

        if has_fee_model:
            fee_at_300k = next(
                (r for r in fee_model["results"]
                 if r["gross_revenue"] == 300000 and r["brand"] == brand_name),
                None,
            )
            if fee_at_300k:
                fee_burden_300k = f"${fee_at_300k['total']:,.0f}"
                fee_rank_300k = next(
                    (i + 1 for i, r in enumerate(fee_rankings[300000])
                     if r["brand"] == brand_name),
                    None,
                )

            for level in fee_model["revenue_levels"]:
                row = next(
                    (r for r in fee_model["results"]
                     if r["gross_revenue"] == level and r["brand"] == brand_name),
                    None,
                )
                if row:
                    rank = next(
                        (i + 1 for i, r in enumerate(fee_rankings[level])
                         if r["brand"] == brand_name),
                        None,
                    )
                    fee_by_level.append(BrandFeeLevel(
                        revenue=level,
                        total=row["total"],
                        pct=row["pct_of_revenue"],
                        rank=rank or 0,
                    ))

        # Growth
        growth_vals = {g["year"]: g["value"] for g in derived["net_unit_growth"]}
        growth_total = sum(growth_vals.values())

        if brand_name in TRAJECTORY_OVERRIDES:
            trajectory = TRAJECTORY_OVERRIDES[brand_name][0]
        else:
            trajectory = derive_trajectory(growth_vals)[0]

        # Attrition
        terminated = y_last["closed"]
        non_renewals = y_last.get("non_renewals") or 0
        ceased = y_last.get("ceased_operations_other") or 0
        attrition_total = terminated + non_renewals + ceased
        attrition_start = y_last["total_outlets_start"]
        attrition_pct = round(
            (attrition_total / attrition_start) * 100, 1
        ) if attrition_start else 0

        if attrition_pct > 10:
            attrition_context = "highest in cohort"
        elif attrition_pct > 5:
            attrition_context = "above cohort average"
        elif attrition_pct > 0:
            attrition_context = "moderate"
        else:
            attrition_context = "lowest in cohort"

        yearly_health = []
        for yr in sorted_years:
            net = (yr["total_outlets_end"] - (yr.get("company_owned_end") or 0)) - \
                  (yr["total_outlets_start"] - (yr.get("company_owned_start") or 0))
            closed_total = yr["closed"] + (yr.get("non_renewals") or 0) + \
                          (yr.get("ceased_operations_other") or 0)
            franchised_end_yr = yr["total_outlets_end"] - (yr.get("company_owned_end") or 0)
            flag = False
            if brand_name == "Mosquito Joe" and yr["year"] == 2024:
                flag = True
            if brand_name == "Mosquito Shield" and yr["year"] == 2023:
                flag = True
            yearly_health.append({
                "year": yr["year"],
                "opened": yr["opened"],
                "closed": closed_total,
                "net": net,
                "end_count": franchised_end_yr,
                "flag": flag,
            })

        peer_brands = [
            {"name": brands[s]["brand"]["brand_name"], "slug": s}
            for s in brand_slugs if s != slug
        ]

        if has_editorial:
            royalty_display = editorial["royalty_display"]
            royalty_context = editorial["royalty_context"]
        else:
            royalty_display, royalty_context = derive_royalty_display(item6)

        parent_short = editorial["parent_short"] if has_editorial else (
            data["brand"].get("parent_company") or "\u2014"
        )
        ownership = editorial["ownership"] if has_editorial else (
            (data["brand"].get("ownership_structure") or "").replace("_", " ") or "\u2014"
        )

        ctx = {
            "active_page": "brand",
            "brand_name": brand_name,
            "brand_short": BRAND_SHORT_NAMES.get(slug, brand_name.split(" ", 1)[-1] if " " in brand_name else brand_name),
            "slug": slug,
            "site_base_url": SITE_BASE_URL,
            "meta_description": BRAND_META_DESCRIPTIONS.get(
                slug,
                f"Review {brand_name} franchise cost, fees, and system health using "
                f"regulator-source data from the 2025 FDD.",
            ),
            "peer_brands": peer_brands,
            "stripe_payment_link": STRIPE_PAYMENT_LINKS.get(slug),
            "legal_entity": data["brand"]["legal_entity"],
            "parent_short": parent_short,
            "ownership": ownership,
            "year_first_franchised": data["brand"]["year_first_franchised"],
            "system_size": franchised_end,
            "investment_range": investment_range,
            "investment_note": investment_note,
            "net_growth_3yr": f"{growth_total:+d} units",
            "trajectory": trajectory,
            "royalty_display": royalty_display,
            "royalty_context": royalty_context,
            "attrition_last_year_pct": f"{attrition_pct}%",
            "attrition_context": attrition_context,
            "yearly_health": yearly_health,
            "has_fee_model": has_fee_model,
            "fee_burden_300k": fee_burden_300k,
            "fee_rank_300k": f"#{fee_rank_300k}" if fee_rank_300k else None,
            "fee_by_level": fee_by_level,
            "has_editorial": has_editorial,
            "marketing_floor": editorial["marketing_floor"] if has_editorial else None,
            "marketing_context": editorial["marketing_context"] if has_editorial else None,
            "disclosure_quality": editorial["disclosure_quality"] if has_editorial else None,
            "disclosure_rank": editorial["disclosure_rank"] if has_editorial else None,
            "disclosure_narrative": editorial["disclosure_narrative"] if has_editorial else None,
            "watchouts": editorial["watchouts"] if has_editorial else [],
            "positives": editorial["positives"] if has_editorial else [],
            "fee_caveats": editorial["fee_caveats"] if has_editorial else [],
            "health_flag": editorial["health_flag"] if has_editorial else None,
            "og_title": f"{brand_name} Franchise Review | Fees, Cost, Risks & FDD Takeaways",
            "og_description": BRAND_META_DESCRIPTIONS.get(
                slug,
                f"Review {brand_name} franchise cost, fees, and system health using "
                f"regulator-source data from the 2025 FDD.",
            ),
            "og_url": f"{SITE_BASE_URL}{slug}.html",
        }
        brand_contexts.append(ctx)

    return brand_contexts


# ---------------------------------------------------------------------------
# Report page context
# ---------------------------------------------------------------------------

def build_report_context(
    brands: dict[str, dict],
    brand_slugs: list[str],
) -> dict:
    """Build context for the report purchase-intent page."""
    brand_list = []
    for slug in brand_slugs:
        data = brands[slug]
        years = data["raw"]["item_20_outlet_summary"]["years_reported"]
        y_last = sorted(years, key=lambda y: y["year"])[-1]
        franchised = y_last["total_outlets_end"] - (y_last.get("company_owned_end") or 0)
        brand_list.append({
            "brand_name": data["brand"]["brand_name"],
            "slug": slug,
            "system_size": franchised,
            "year_first_franchised": data["brand"]["year_first_franchised"],
            "differentiator": BRAND_DIFFERENTIATORS.get(slug, ""),
            "stripe_payment_link": STRIPE_PAYMENT_LINKS.get(slug),
        })
    return {"brands": brand_list}


def build_master_report_context(
    ready_cohorts: list[dict],
) -> dict:
    """Build context for the unified master report page across all cohorts."""
    cohort_groups: list[dict] = []
    for cohort in ready_cohorts:
        brand_slugs = all_cohort_slugs(cohort)
        brand_slugs = [
            s for s in brand_slugs
            if (DATA_EXTRACTED / f"{s}.json").exists()
        ]
        brands = load_brand_data(brand_slugs)
        brand_list = []
        for slug in brand_slugs:
            data = brands[slug]
            years = data["raw"]["item_20_outlet_summary"]["years_reported"]
            y_last = sorted(years, key=lambda y: y["year"])[-1]
            franchised = (
                y_last["total_outlets_end"]
                - (y_last.get("company_owned_end") or 0)
            )
            stripe_link = STRIPE_PAYMENT_LINKS.get(slug)
            brand_list.append({
                "brand_name": data["brand"]["brand_name"],
                "slug": slug,
                "system_size": franchised,
                "year_first_franchised": data["brand"]["year_first_franchised"],
                "differentiator": BRAND_DIFFERENTIATORS.get(slug, ""),
                "stripe_payment_link": stripe_link,
                "is_paid": stripe_link is not None,
            })
        paid_count = sum(1 for b in brand_list if b["is_paid"])
        cohort_groups.append({
            "id": cohort["id"],
            "display_name": cohort["display_name"],
            "short_name": cohort["short_name"],
            "brands": brand_list,
            "paid_count": paid_count,
            "total_count": len(brand_list),
        })
    return {"cohort_groups": cohort_groups}


# ---------------------------------------------------------------------------
# Category landing page editorial
# ---------------------------------------------------------------------------

CATEGORY_PAGE_DATA: dict[str, dict] = {
    "mosquito": {
        "title": "Mosquito Control Franchise Fees, Cost &amp; FDD Comparison | 7 Brands Analyzed",
        "h1": "Mosquito control franchises: 7 brands compared from regulator-filed FDDs",
        "canonical_slug": "mosquito-franchise.html",
        "output_file": "mosquito-franchise.html",
        "meta_description": (
            "Compare 7 mosquito control franchise brands on fees, startup cost, "
            "and system health using data extracted from regulator-filed FDDs. "
            "Fee burden spread, investment ranges, and growth trajectories side by side."
        ),
        "subhead": (
            "Side-by-side fee burden, startup cost, and system health for every major "
            "mosquito control franchise\u200a\u2014\u200abuilt from 2025 FDDs filed with "
            "the Wisconsin Department of Financial Institutions."
        ),
        "editorial_section": (
            "<p>"
            "The headline difference in this category is fee architecture. "
            "Mosquito Authority charges a flat 10% royalty with no mandatory marketing fund, "
            "producing the lowest total fee burden in the cohort. "
            "Mosquito Joe pairs a tiered royalty (10%/7%) with $72K in mandatory first-year marketing, "
            "making it the most expensive to operate at every revenue level. "
            "At $300K gross revenue, the annual fee gap between the cheapest and most expensive brand "
            "exceeds <strong>$50,000/year</strong>."
            "</p>"
            "<p>"
            "System trajectories have diverged sharply. Mosquito Shield was the fastest-growing brand "
            "but is now decelerating with high churn. Mosquito Joe, the second-largest system, "
            "has turned net-negative on unit growth. Meanwhile, Mosquito Squad is showing recovery "
            "after several flat years. "
            "For a buyer, this means the brand with the most name recognition and the brand with "
            "the healthiest growth numbers are not the same brand."
            "</p>"
            "<p>"
            "Investment ranges are tighter here than in lawn care or cleaning "
            "\u2014\u200a$54K to $220K across all seven brands "
            "\u2014\u200abut the composition varies significantly. "
            "Some brands front-load marketing spend in the initial investment (Joe, Shield), "
            "while others keep startup costs low and collect more through ongoing fees (Authority, Sheriff)."
            "</p>"
        ),
        "comparison_descriptions": {
            "Fee Burden": (
                "Marketing fees\u200a\u2014\u200anot royalties\u200a\u2014\u200adrive the biggest "
                "cost differences in mosquito control. The fee burden comparison shows exactly where "
                "each brand\u2019s ongoing costs come from at four revenue levels."
            ),
            "System Health": (
                "Two brands are growing, two are contracting, and three are early-stage or transitional. "
                "The system health comparison shows outlet-level openings, closings, and transfers "
                "for each brand over three years."
            ),
            "Cost to Enter": (
                "The tightest investment range of any category on the site, but reserve requirements "
                "and mandatory marketing packages vary widely. The cost comparison breaks down where "
                "startup capital actually goes."
            ),
        },
    },
    "lawn": {
        "title": "Lawn Care Franchise Fees, Cost &amp; FDD Comparison | 6 Brands Analyzed",
        "h1": "Lawn care franchises: 6 brands compared from regulator-filed FDDs",
        "canonical_slug": "lawn-franchise.html",
        "output_file": "lawn-franchise.html",
        "meta_description": (
            "Compare 6 lawn care franchise brands on fees, startup cost, "
            "and system health using data extracted from regulator-filed FDDs. "
            "Four established brands plus two watchlisted newcomers."
        ),
        "subhead": (
            "Side-by-side fee burden, startup cost, and system health for major "
            "lawn care franchises\u200a\u2014\u200abuilt from 2025 FDDs filed with "
            "the Wisconsin Department of Financial Institutions."
        ),
        "editorial_section": (
            "<p>"
            "Lawn care is the most established category on the site. "
            "All four core brands have been franchising for 30 to 58 years, "
            "which means the FDD data reflects mature, stable systems "
            "rather than early-stage volatility. "
            "The fee spread is narrower than in mosquito control or cleaning "
            "\u2014\u200aat $300K revenue, the gap between highest and lowest annual fee burden "
            "is roughly half what it is in the mosquito cohort."
            "</p>"
            "<p>"
            "Where these brands diverge most is disclosure quality and royalty structure. "
            "Weed Man offers the lowest effective royalty in the cohort (6.5%/5.5% tiered) "
            "but provides no Item 19 financial performance data. "
            "Lawn Doctor charges 10% flat but sits atop the largest system (600+ outlets) "
            "with an accelerating growth trajectory. "
            "NaturaLawn occupies a premium organic niche with a loyalty-rewarding royalty "
            "that drops from 9% to 7% at renewal."
            "</p>"
        ),
        "comparison_descriptions": {
            "Fee Burden": (
                "The narrowest fee spread of any category, but royalty structures range "
                "from flat 10% to tiered schedules that reward growth. "
                "The fee burden comparison models total ongoing costs at four revenue levels."
            ),
            "System Health": (
                "Four systems with decades of operating history. "
                "Growth trajectories range from accelerating (Lawn Doctor) to flat (Spring-Green). "
                "The system health comparison shows year-by-year outlet changes."
            ),
            "Cost to Enter": (
                "Investment ranges vary by more than 2x, driven largely by mandatory marketing "
                "packages and reserve requirements. "
                "The cost comparison shows where each brand\u2019s startup capital goes."
            ),
        },
        "watchlist_note": (
            "<strong>Lawn Pride</strong> and <strong>Lawn Squad</strong> appear on brand pages "
            "but are excluded from comparison tables. Both are backed by major franchise holding "
            "companies (Neighborly and Authority Brands, respectively) but have fewer than three years "
            "of franchised operating data. They are included in the brand count but not in the "
            "fee, health, or cost analyses."
        ),
    },
    "cleaning": {
        "title": "Residential Cleaning Franchise Fees, Cost &amp; FDD Comparison | 7 Brands Analyzed",
        "h1": "Residential cleaning franchises: 7 brands compared from regulator-filed FDDs",
        "canonical_slug": "cleaning-franchise.html",
        "output_file": "cleaning-franchise.html",
        "meta_description": (
            "Compare 7 residential cleaning franchise brands on fees, startup cost, "
            "and system health using data extracted from regulator-filed FDDs. "
            "Legacy giants contracting while newer brands grow."
        ),
        "subhead": (
            "Side-by-side fee burden, startup cost, and system health for major "
            "residential cleaning franchises\u200a\u2014\u200abuilt from 2025 FDDs filed with "
            "the Wisconsin Department of Financial Institutions."
        ),
        "editorial_section": (
            "<p>"
            "Residential cleaning has the widest performance spread of any category on the site. "
            "The two largest systems\u200a\u2014\u200aMerry Maids (1,400+ outlets) and "
            "Molly Maid (500+ outlets)\u200a\u2014\u200aare both contracting, "
            "losing franchised units in each of the last three reporting years. "
            "Meanwhile, The Cleaning Authority and Two Maids are the only brands posting "
            "consistent net growth, with Two Maids growing 57% over three years."
            "</p>"
            "<p>"
            "This is also the strongest category for Item 19 disclosure. "
            "All seven brands provide some form of financial performance representation, "
            "though the depth varies considerably. "
            "The Cleaning Authority reports average unit revenue and COGS ratios. "
            "The Maids discloses company-owned P&amp;L data. "
            "Others provide revenue distributions or medians. "
            "No other category on the site offers this level of financial disclosure across the board."
            "</p>"
            "<p>"
            "Fee structures are more varied here than in mosquito control or lawn care. "
            "Merry Maids pairs the largest system with the lowest total fees. "
            "Molly Maid offers a tiered royalty that rewards scale. "
            "MaidPro has the simplest structure\u200a\u2014\u200aflat royalty, "
            "no technology surcharges, no call center fees. "
            "A buyer\u2019s fee exposure depends heavily on which combination of "
            "royalty, marketing, and technology fees a given brand mandates."
            "</p>"
        ),
        "comparison_descriptions": {
            "Fee Burden": (
                "The most varied fee structures of any category. "
                "Royalty rates, marketing minimums, and technology surcharges combine differently "
                "across seven brands. The fee burden comparison models total ongoing costs "
                "at four revenue levels."
            ),
            "System Health": (
                "A category split between legacy contraction and newcomer growth. "
                "The system health comparison shows which brands are gaining outlets, "
                "which are losing them, and how fast."
            ),
            "Cost to Enter": (
                "Investment ranges span from under $100K to over $200K, "
                "with significant variation in what\u2019s included. "
                "The cost comparison breaks down initial fees, equipment, marketing, and reserves."
            ),
        },
    },
}


def build_category_context(
    cohort: dict,
    brands: dict[str, dict],
    brand_slugs: list[str],
    fee_model: dict | None,
) -> dict | None:
    """Build context for a category landing page."""
    cohort_id = cohort["id"]
    cat_data = CATEGORY_PAGE_DATA.get(cohort_id)
    if not cat_data:
        return None

    # Build brands table
    brands_table = []
    for slug in brand_slugs:
        data = brands[slug]
        name = data["brand"]["brand_name"]
        outlets = franchised_outlet_count(data)
        low, high, _ = normalize_item7(data)
        inv_display = f"${low // 1000:,}K\u2013${high // 1000:,}K"

        fee_300k_display = "\u2014"
        if fee_model:
            for r in fee_model["results"]:
                if r["gross_revenue"] == 300000 and r["brand"] == name:
                    fee_300k_display = (
                        f"${r['total']:,.0f}"
                        f'<span class="muted small"> ({r["pct_of_revenue"]}%)</span>'
                    )
                    break

        diff = BRAND_DIFFERENTIATORS.get(slug, "")
        brands_table.append({
            "slug": slug,
            "name": name,
            "outlets": f"{outlets:,}",
            "investment": inv_display,
            "fee_300k": fee_300k_display,
            "differentiator": diff,
        })

    # Compute stat-strip values
    all_lows = []
    all_highs = []
    all_outlets = []
    for slug in brand_slugs:
        low, high, _ = normalize_item7(brands[slug])
        all_lows.append(low)
        all_highs.append(high)
        all_outlets.append(franchised_outlet_count(brands[slug]))

    inv_range = f"${min(all_lows) // 1000:,}K\u2013${max(all_highs) // 1000:,}K"
    size_range = f"{min(all_outlets):,}\u2013{max(all_outlets):,}"

    fee_spread = ""
    if fee_model:
        fees_300 = [
            r["total"] for r in fee_model["results"]
            if r["gross_revenue"] == 300000
        ]
        if fees_300:
            spread = max(fees_300) - min(fees_300)
            spread_rounded = round(spread / 1000) * 1000
            fee_spread = f"${spread_rounded:,.0f}"

    # Comparison links with per-category descriptions
    prefix = cohort["url_prefix"]
    comp_links = []
    for page_id in cohort["comparison_pages"]:
        label = PAGE_LABELS[page_id]
        comp_links.append({
            "url": f"{prefix}{page_id}.html",
            "label": label,
            "description": cat_data["comparison_descriptions"].get(label, ""),
        })

    # Paid report count
    paid_count = sum(
        1 for slug in brand_slugs
        if STRIPE_PAYMENT_LINKS.get(slug)
    )

    # Watchlist
    watchlist_slugs = cohort.get("watchlist", [])
    watchlist_note = cat_data.get("watchlist_note", "")

    return {
        "title_text": cat_data["title"],
        "h1_text": cat_data["h1"],
        "canonical_slug": cat_data["canonical_slug"],
        "meta_description": cat_data["meta_description"],
        "subhead": cat_data["subhead"],
        "brand_count": len(brand_slugs),
        "investment_range_display": inv_range,
        "fee_spread_display": fee_spread,
        "system_size_range": size_range,
        "has_fee_model": fee_model is not None,
        "brands_table": brands_table,
        "editorial_section": cat_data["editorial_section"],
        "comparison_links": comp_links,
        "paid_report_count": paid_count,
        "watchlist_brands": watchlist_slugs,
        "watchlist_note": watchlist_note,
        "filing_year": "2025",
        "og_title": cat_data["title"].replace("&amp;", "&"),
        "og_description": cat_data["meta_description"],
        "og_url": f"{SITE_BASE_URL}{cat_data['canonical_slug']}",
    }


# ---------------------------------------------------------------------------
# Navigation helpers
# ---------------------------------------------------------------------------

PAGE_LABELS: dict[str, str] = {
    "fee-burden": "Fee Burden",
    "system-health": "System Health",
    "cost-to-enter": "Cost to Enter",
}


def build_nav_pages(cohort: dict) -> list[dict]:
    """Build navigation links for a single cohort's pages."""
    prefix = cohort["url_prefix"]
    pages = []
    for page_id in cohort["comparison_pages"]:
        full_id = f"{prefix}{page_id}" if prefix else page_id
        pages.append({
            "url": f"{prefix}{page_id}.html",
            "label": PAGE_LABELS[page_id],
            "id": full_id,
        })
    return pages


def build_all_nav(cohorts: list[dict]) -> list[dict]:
    """Build combined navigation data for all cohorts with comparison pages."""
    result = []
    for cohort in cohorts:
        pages = build_nav_pages(cohort)
        if not pages:
            continue
        cohort_nav = {
            "id": cohort["id"],
            "short_name": cohort["short_name"],
            "pages": pages,
        }
        result.append(cohort_nav)
    return result


# ---------------------------------------------------------------------------
# VS comparison page data + builder
# ---------------------------------------------------------------------------

VS_PAGES: list[dict] = [
    {
        "slug_a": "mosquito-joe",
        "slug_b": "mosquito-authority",
        "cohort_id": "mosquito",
        "output_file": "mosquito-joe-vs-mosquito-authority.html",
        "canonical_slug": "mosquito-joe-vs-mosquito-authority.html",
        "title": "Mosquito Joe vs. Mosquito Authority | Franchise Fee, Cost &amp; FDD Comparison",
        "h1": "Mosquito Joe vs. Mosquito Authority: what the FDD data shows",
        "meta_description": (
            "Side-by-side comparison of Mosquito Joe and Mosquito Authority franchise "
            "fees, startup cost, system health, and FDD data. Fee burden, growth "
            "trajectories, and investment breakdown from regulator-filed disclosures."
        ),
        "subhead": (
            "The two largest mosquito control franchises by system size, "
            "with opposite fee structures and diverging growth trajectories. "
            "All data from 2025 FDDs filed with the Wisconsin DFI."
        ),
        "fee_burden_editorial": (
            "<p>"
            "The fee gap between these two brands is the largest in the mosquito cohort "
            "and it widens at higher revenue. "
            "Mosquito Authority charges a flat 10% royalty with no mandatory marketing fund "
            "and no technology surcharges beyond fixed weekly fees. "
            "Mosquito Joe pairs a tiered royalty (10% on the first $500K, 7% above) "
            "with $72K in mandatory first-year marketing and ongoing national ad fund contributions."
            "</p>"
            "<p>"
            "At $300K gross revenue, Authority\u2019s annual fee burden is "
            "$52,800 (17.6% of revenue). Joe\u2019s is $84,752 (28.3%). "
            "That\u2019s a <strong>$31,952/year difference</strong>\u200a\u2014\u200aenough to "
            "change the unit economics of the business. "
            "The gap narrows at higher revenue because Joe\u2019s tiered royalty "
            "drops to 7% above $500K, but the marketing burden keeps Joe structurally more expensive."
            "</p>"
        ),
        "fee_caveats_editorial": (
            '<div class="callout callout-caveat">'
            '<div class="callout-title">Authority fixed fees add up</div>'
            "Mosquito Authority\u2019s fee model looks simple (flat 10% royalty), "
            "but weekly technology ($210), accounting ($85), and contact center "
            "($50\u2013$220, escalating) fees add $295\u2013$515/week in fixed costs "
            "regardless of revenue. At low revenue, these fixed charges represent a "
            "higher percentage of income than Joe\u2019s percentage-based fees."
            "</div>"
            '<div class="callout callout-caveat">'
            '<div class="callout-title">Joe front-loads marketing</div>'
            "Mosquito Joe\u2019s Item 7 includes $72K in mandatory marketing "
            "($37K DMP + $35K local). This is not optional and is due during the first year. "
            "It\u2019s nearly half the initial investment and inflates the cost-to-enter comparison "
            "relative to Authority."
            "</div>"
        ),
        "system_health_editorial": (
            "<p>"
            "The growth trajectories are moving in opposite directions. "
            "Mosquito Authority has maintained stable positive growth, adding outlets "
            "consistently across the last three reporting years. "
            "Mosquito Joe peaked in system size and has turned net-negative, "
            "losing more franchised outlets than it opened in the most recent year."
            "</p>"
            "<p>"
            "For a buyer, this means the brand with the most consumer recognition "
            "(Joe has higher marketing spend) and the brand with the healthiest "
            "franchisee growth signal (Authority) are not the same brand."
            "</p>"
        ),
        "cost_editorial": (
            "<p>"
            "Mosquito Authority\u2019s initial investment ranges from $54K\u2013$127K, "
            "depending on territory tier (Hometown vs. Full-Size). "
            "Mosquito Joe\u2019s ranges from $150K\u2013$192K."
            "</p>"
            "<p>"
            "The gap is driven primarily by Joe\u2019s mandatory marketing: "
            "$37K DMP + $35K local marketing are due in Year 1 and represent the "
            "single largest cost differentiator between the two brands. "
            "Authority keeps startup costs lower and relies more on ongoing fees "
            "to generate franchisor revenue."
            "</p>"
        ),
        "tradeoffs_editorial": (
            "<p>"
            "Authority costs less to enter, costs less to operate, and has a healthier "
            "growth trajectory. Joe has higher consumer brand recognition (driven by "
            "Neighborly\u2019s marketing machine), a larger existing franchisee network to "
            "learn from, and a tiered royalty that rewards scale."
            "</p>"
            "<p>"
            "A buyer prioritizing low fee exposure and capital efficiency has a clearer path "
            "with Authority. A buyer prioritizing brand recognition and national marketing "
            "infrastructure has a rationale for Joe\u200a\u2014\u200abut should model whether "
            "the $32,000/year fee premium generates enough incremental revenue to justify itself."
            "</p>"
            "<p>"
            "Neither brand is categorically better. The right choice depends on "
            "your revenue expectations, marketing tolerance, and how much you weight "
            "system growth trajectory in your diligence."
            "</p>"
        ),
    },
]


def _build_vs_pages(
    env: Environment,
    all_nav: list[dict],
    all_brands_by_cohort: list[dict],
    ready_cohorts: list[dict],
) -> None:
    """Build VS comparison pages from VS_PAGES config."""
    for vs in VS_PAGES:
        cohort = next((c for c in ready_cohorts if c["id"] == vs["cohort_id"]), None)
        if not cohort:
            continue

        slug_a, slug_b = vs["slug_a"], vs["slug_b"]
        brands = load_brand_data([slug_a, slug_b])
        data_a, data_b = brands[slug_a], brands[slug_b]
        name_a = data_a["brand"]["brand_name"]
        name_b = data_b["brand"]["brand_name"]

        # Fee model
        fee_model = None
        if cohort.get("has_fee_model") and cohort.get("fee_model_file"):
            fee_model = load_fee_model(cohort["fee_model_file"])

        # Fee table
        fee_table = []
        if fee_model:
            for level in fee_model["revenue_levels"]:
                row_a = next(
                    (r for r in fee_model["results"]
                     if r["gross_revenue"] == level and r["brand"] == name_a),
                    None,
                )
                row_b = next(
                    (r for r in fee_model["results"]
                     if r["gross_revenue"] == level and r["brand"] == name_b),
                    None,
                )
                if row_a and row_b:
                    fee_table.append({
                        "revenue": level,
                        "a_total": row_a["total"],
                        "a_pct": row_a["pct_of_revenue"],
                        "b_total": row_b["total"],
                        "b_pct": row_b["pct_of_revenue"],
                        "diff": abs(row_a["total"] - row_b["total"]),
                    })

        # System health table
        def _health_rows(data: dict) -> dict[int, dict]:
            years = data["raw"]["item_20_outlet_summary"]["years_reported"]
            result = {}
            for yr in sorted(years, key=lambda y: y["year"]):
                fran_end = yr["total_outlets_end"] - (yr.get("company_owned_end") or 0)
                fran_start = yr["total_outlets_start"] - (yr.get("company_owned_start") or 0)
                result[yr["year"]] = {
                    "net": fran_end - fran_start,
                    "end": fran_end,
                }
            return result

        rows_a = _health_rows(data_a)
        rows_b = _health_rows(data_b)
        all_years = sorted(set(rows_a.keys()) | set(rows_b.keys()))
        health_table = []
        for yr in all_years:
            health_table.append({
                "year": yr,
                "a_net": rows_a.get(yr, {}).get("net", 0),
                "a_end": rows_a.get(yr, {}).get("end", 0),
                "b_net": rows_b.get(yr, {}).get("net", 0),
                "b_end": rows_b.get(yr, {}).get("end", 0),
            })

        # Brand summary data
        def _brand_summary(slug: str, data: dict) -> dict:
            name = data["brand"]["brand_name"]
            outlets = franchised_outlet_count(data)
            low, high, _ = normalize_item7(data)
            growth_vals = {g["year"]: g["value"] for g in data["derived"]["net_unit_growth"]}
            growth_total = sum(growth_vals.values())
            traj = TRAJECTORY_OVERRIDES.get(name, derive_trajectory(growth_vals))[0]
            editorial = BRAND_EDITORIAL.get(slug) or {}
            royalty_display = editorial.get("royalty_display") or derive_royalty_display(
                data["raw"]["item_6_other_fees"]
            )[0]

            fee_300k = ""
            if fee_model:
                row = next(
                    (r for r in fee_model["results"]
                     if r["gross_revenue"] == 300000 and r["brand"] == name),
                    None,
                )
                if row:
                    fee_300k = f"${row['total']:,.0f} ({row['pct_of_revenue']}%)"

            short = BRAND_SHORT_NAMES.get(slug, name.split(" ", 1)[-1] if " " in name else name)

            return {
                "slug": slug,
                "name": name,
                "short_name": short,
                "outlets": f"{outlets:,}",
                "investment": f"${low // 1000}K\u2013${high // 1000}K",
                "fee_300k": fee_300k,
                "net_growth": f"{growth_total:+d} units",
                "trajectory": traj,
                "royalty": royalty_display,
                "year_started": data["brand"]["year_first_franchised"],
                "watchouts": editorial.get("watchouts", []),
                "stripe_link": STRIPE_PAYMENT_LINKS.get(slug),
            }

        brand_a = _brand_summary(slug_a, data_a)
        brand_b = _brand_summary(slug_b, data_b)

        prefix = cohort["url_prefix"]
        nav_pages = build_nav_pages(cohort)

        ctx = {
            "site_base_url": SITE_BASE_URL,
            "active_page": "",
            "all_nav": all_nav,
            "all_brands_by_cohort": all_brands_by_cohort,
            "nav_pages": nav_pages,
            "cohort_id": cohort["id"],
            "cohort_short_name": cohort["short_name"],
            "cohort_brand_count": len(cohort["brands"]),
            "cohort_fee_burden_url": f"{prefix}fee-burden.html",
            "cohort_system_health_url": f"{prefix}system-health.html",
            "cohort_cost_to_enter_url": f"{prefix}cost-to-enter.html",
            "title_text": vs["title"],
            "h1_text": vs["h1"],
            "canonical_slug": vs["canonical_slug"],
            "meta_description": vs["meta_description"],
            "subhead": vs["subhead"],
            "brand_a": brand_a,
            "brand_b": brand_b,
            "fee_table": fee_table,
            "health_table": health_table,
            "fee_burden_editorial": vs["fee_burden_editorial"],
            "fee_caveats_editorial": vs["fee_caveats_editorial"],
            "system_health_editorial": vs["system_health_editorial"],
            "cost_editorial": vs["cost_editorial"],
            "tradeoffs_editorial": vs["tradeoffs_editorial"],
            "og_title": vs["title"].replace("&amp;", "&"),
            "og_description": vs["meta_description"],
            "og_url": f"{SITE_BASE_URL}{vs['canonical_slug']}",
        }

        render_page(env, "vs.html", vs["output_file"], ctx)


# ---------------------------------------------------------------------------
# Render helper
# ---------------------------------------------------------------------------

def render_page(env: Environment, template_name: str, output_name: str, context: dict) -> None:
    """Render a Jinja2 template and write to site/."""
    template = env.get_template(template_name)
    html = template.render(**context)
    output_path = SITE / output_name
    output_path.write_text(html)
    print(f"  Built: {output_path.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build_site() -> None:
    """Render all templates to site/."""
    SITE.mkdir(exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=False,
    )

    cohorts = load_registry()
    total_pages = 0

    # Filter to cohorts where ALL brand JSONs exist AND contain valid extraction data
    def _cohort_ready(cohort: dict) -> bool:
        for slug in cohort["brands"]:
            path = DATA_EXTRACTED / f"{slug}.json"
            if not path.exists():
                return False
            try:
                data = json.loads(path.read_text())
                # Check for a required field that only exists in completed extractions
                normalize_item7(data)
            except (KeyError, TypeError, ValueError, json.JSONDecodeError):
                return False
        return True

    ready_cohorts = [c for c in cohorts if _cohort_ready(c)]
    pending_cohorts = [c for c in cohorts if c not in ready_cohorts]
    if pending_cohorts:
        for c in pending_cohorts:
            print(f"  Skipped: {c['display_name']} (no extracted data yet)")

    # Only include ready cohorts in nav
    all_nav = build_all_nav(ready_cohorts)

    # Pre-collect brand info for all ready cohorts (needed by footer on every page)
    all_brands_by_cohort: list[dict] = []
    for cohort in ready_cohorts:
        all_slugs = all_cohort_slugs(cohort)
        available = [s for s in all_slugs if (DATA_EXTRACTED / f"{s}.json").exists()]
        pre_brands = load_brand_data(available)
        all_brands_by_cohort.append({
            "id": cohort["id"],
            "display_name": cohort["display_name"],
            "short_name": cohort["short_name"],
            "brands": [
                {"name": pre_brands[s]["brand"]["brand_name"], "slug": s}
                for s in available
            ],
        })

    for cohort in ready_cohorts:
        # Include watchlist brands that have extracted data
        brand_slugs = all_cohort_slugs(cohort)
        brand_slugs = [s for s in brand_slugs if (DATA_EXTRACTED / f"{s}.json").exists()]
        brands = load_brand_data(brand_slugs)
        slug_map = build_slug_map(brands)
        prefix = cohort["url_prefix"]

        # Split brands into comparison-eligible and excluded
        comp_brands, excluded_slugs = filter_comparison_brands(brands)
        comp_slugs = [s for s in brand_slugs if s in comp_brands]
        comp_slug_map = build_slug_map(comp_brands)

        if excluded_slugs:
            excluded_names = [brands[s]["brand"]["brand_name"] for s in excluded_slugs]
            print(f"  Comparison exclusion (<{COMPARISON_MIN_OUTLETS} outlets): "
                  f"{', '.join(excluded_names)}")

        fee_model = None
        if cohort.get("has_fee_model") and cohort.get("fee_model_file"):
            fee_model = load_fee_model(cohort["fee_model_file"])

        # Filter fee model results to only comparison-eligible brands
        comp_fee_model = None
        if fee_model:
            comp_brand_names = {
                comp_brands[s]["brand"]["brand_name"] for s in comp_slugs
            }
            comp_fee_model = {
                **fee_model,
                "results": [
                    r for r in fee_model["results"]
                    if r["brand"] in comp_brand_names
                ],
            }

        nav_pages = build_nav_pages(cohort)

        shared = {
            "site_base_url": SITE_BASE_URL,
            "nav_pages": nav_pages,
            "all_nav": all_nav,
            "all_brands_by_cohort": all_brands_by_cohort,
            "cohort_id": cohort["id"],
            "cohort_display_name": cohort["display_name"],
            "cohort_short_name": cohort["short_name"],
            "cohort_brand_count": len(comp_slugs),
            "brand_slug_map": comp_slug_map,
            "og_title": "",
            "og_description": "",
            "og_url": "",
        }

        # Fee burden — comparison-eligible brands only
        if comp_fee_model and "fee-burden" in cohort["comparison_pages"]:
            fee_ctx = build_fee_context(comp_fee_model, comp_brands)
            active = f"{prefix}fee-burden" if prefix else "fee-burden"
            fb_file = f"{prefix}fee-burden.html"
            render_page(env, "fee-burden.html", fb_file, {
                **shared, "active_page": active, **fee_ctx,
                "og_title": f"{cohort['display_name']} Franchise Fees Comparison",
                "og_description": f"Compare {cohort['display_name'].lower()} franchise fee burden across major brands, including royalty structure, marketing fees, and estimated annual franchisor take at real revenue levels.",
                "og_url": f"{SITE_BASE_URL}{fb_file}",
            })
            total_pages += 1

        # System health — comparison-eligible brands only
        if "system-health" in cohort["comparison_pages"]:
            health_ctx = build_health_context(comp_brands, comp_slug_map)
            active = f"{prefix}system-health" if prefix else "system-health"
            sh_file = f"{prefix}system-health.html"
            render_page(env, "system-health.html", sh_file, {
                **shared, "active_page": active, **health_ctx,
                "og_title": f"{cohort['short_name']} Franchise System Health Comparison",
                "og_description": f"Compare {cohort['short_name'].lower()} franchise system health using outlet growth, closures, transfers, and other signals that may indicate brand stability or buyer risk.",
                "og_url": f"{SITE_BASE_URL}{sh_file}",
            })
            total_pages += 1

        # Cost to enter — comparison-eligible brands only
        if "cost-to-enter" in cohort["comparison_pages"]:
            cost_ctx = build_cost_context(comp_brands, comp_slug_map)
            active = f"{prefix}cost-to-enter" if prefix else "cost-to-enter"
            cte_file = f"{prefix}cost-to-enter.html"
            render_page(env, "cost-to-enter.html", cte_file, {
                **shared, "active_page": active, **cost_ctx,
                "og_title": f"{cohort['display_name']} Franchise Startup Cost Comparison",
                "og_description": f"Compare {cohort['display_name'].lower()} franchise startup cost and initial investment ranges across brands, using disclosure-document data.",
                "og_url": f"{SITE_BASE_URL}{cte_file}",
            })
            total_pages += 1

        # Brand pages — ALL brands get individual pages
        brand_ctxs = build_brand_contexts(
            brands, brand_slugs, comp_fee_model, slug_map, cohort,
        )
        brand_template = env.get_template("brand.html")
        for ctx in brand_ctxs:
            html = brand_template.render(**{**shared, **ctx})
            output_path = SITE / f"{ctx['slug']}.html"
            output_path.write_text(html)
            print(f"  Built: {output_path.relative_to(ROOT)}")
            total_pages += 1

        # Thank-you pages — generate for all brands with paid reports
        # (ready for Stripe fulfillment even before links are live)
        thank_you_template = env.get_template("thank-you.html")
        for s_slug in brand_slugs:
            if s_slug not in brands:
                continue
            bname = brands[s_slug]["brand"]["brand_name"]
            ty_ctx = {
                **shared,
                "active_page": "",
                "brand_name": bname,
                "slug": s_slug,
            }
            html = thank_you_template.render(**ty_ctx)
            output_path = SITE / f"thank-you-{s_slug}.html"
            output_path.write_text(html)
            print(f"  Built: {output_path.relative_to(ROOT)}")
            total_pages += 1

        # Category landing page — one per cohort
        cat_ctx = build_category_context(cohort, brands, brand_slugs, fee_model)
        if cat_ctx:
            cat_output = CATEGORY_PAGE_DATA[cohort["id"]]["output_file"]
            render_page(env, "category.html", cat_output, {
                **shared,
                "active_page": cohort["id"],
                **cat_ctx,
            })
            total_pages += 1

    # --- Master report page (all cohorts) ---
    master_report_ctx = build_master_report_context(ready_cohorts)
    render_page(env, "report.html", "report.html", {
        "site_base_url": SITE_BASE_URL,
        "active_page": "report",
        "all_nav": all_nav,
        "all_brands_by_cohort": all_brands_by_cohort,
        "nav_pages": [],
        "cohort_id": None,
        "og_title": "Franchise Decision Reports | Brand-by-Brand FDD Analysis",
        "og_description": "Buy brand-specific franchise decision reports with Item 19 translation, fee modeling, key risks, and discovery-day questions. Mosquito, lawn care, and residential cleaning franchises.",
        "og_url": f"{SITE_BASE_URL}report.html",
        **master_report_ctx,
    })
    total_pages += 1

    # --- Homepage (multi-cohort) ---
    live_cohorts = []
    for cohort in ready_cohorts:
        brand_slugs = all_cohort_slugs(cohort)
        brand_slugs = [s for s in brand_slugs if (DATA_EXTRACTED / f"{s}.json").exists()]
        brands = load_brand_data(brand_slugs)
        slug_map = build_slug_map(brands)
        comp_brands_hp, _ = filter_comparison_brands(brands)
        fee_model = None
        if cohort.get("has_fee_model") and cohort.get("fee_model_file"):
            fee_model = load_fee_model(cohort["fee_model_file"])

        # Pre-compute investment ranges (handles split-market brands)
        brand_investment = {}
        for s in brand_slugs:
            low, high, _ = normalize_item7(brands[s])
            brand_investment[s] = {"low": low, "high": high}

        cat_data = CATEGORY_PAGE_DATA.get(cohort["id"])
        cat_url = cat_data["output_file"] if cat_data else f"{cohort['id']}-franchise.html"

        live_cohorts.append({
            "id": cohort["id"],
            "display_name": cohort["display_name"],
            "short_name": cohort["short_name"],
            "description": cohort["description"],
            "brand_count": len(brand_slugs),
            "brand_slugs": brand_slugs,
            "brands_data": brands,
            "brand_slug_map": slug_map,
            "brand_investment": brand_investment,
            "has_fee_model": fee_model is not None,
            "fee_model": fee_model,
            "category_url": cat_url,
            "comparison_pages": [
                {"url": f"{cohort['url_prefix']}{pid}.html", "label": PAGE_LABELS[pid]}
                for pid in cohort["comparison_pages"]
            ],
        })

    # Pending cohorts shown as "coming soon" on homepage
    hp_pending_cohorts = [
        {
            "id": c["id"],
            "display_name": c["display_name"],
            "short_name": c["short_name"],
            "description": c["description"],
            "brands": c["brands"],
        }
        for c in pending_cohorts
    ]

    total_brands = sum(c["brand_count"] for c in live_cohorts)
    total_categories = len(live_cohorts) + len(hp_pending_cohorts)

    render_page(env, "index.html", "index.html", {
        "site_base_url": SITE_BASE_URL,
        "active_page": "home",
        "all_nav": all_nav,
        "all_brands_by_cohort": all_brands_by_cohort,
        "nav_pages": [],
        "cohort_id": None,
        "live_cohorts": live_cohorts,
        "pending_cohorts": hp_pending_cohorts,
        "total_brands": total_brands,
        "total_categories": total_categories,
        "og_title": "Franchise Decision Radar | Recurring Residential Service Franchise Comparison",
        "og_description": f"Compare recurring residential service franchises using regulator-source disclosure data. Fee burden, system health, startup cost, and brand-specific risk across {total_brands} brands in {total_categories} categories.",
        "og_url": SITE_BASE_URL,
    })
    total_pages += 1

    # --- Methodology page ---
    render_page(env, "methodology.html", "methodology.html", {
        "site_base_url": SITE_BASE_URL,
        "active_page": "methodology",
        "all_nav": all_nav,
        "all_brands_by_cohort": all_brands_by_cohort,
        "nav_pages": [],
        "cohort_id": None,
        "og_title": "Methodology | Franchise Decision Radar",
        "og_description": "How Franchise Decision Radar extracts, models, and presents franchise comparison data from regulator-filed Franchise Disclosure Documents.",
        "og_url": f"{SITE_BASE_URL}methodology.html",
    })
    total_pages += 1

    # --- How to Read an FDD guide ---
    render_page(env, "how-to-read-fdd.html", "how-to-read-fdd.html", {
        "site_base_url": SITE_BASE_URL,
        "active_page": "",
        "all_nav": all_nav,
        "all_brands_by_cohort": all_brands_by_cohort,
        "nav_pages": [],
        "cohort_id": None,
        "brand_count": total_brands,
        "category_count": len(ready_cohorts),
        "og_title": "How to Read a Franchise Disclosure Document | FDD Buyer's Guide",
        "og_description": f"A buyer's guide to the five FDD items that matter most for franchise diligence, with real examples from {total_brands} franchise brands we've analyzed.",
        "og_url": f"{SITE_BASE_URL}how-to-read-fdd.html",
    })
    total_pages += 1

    # --- VS comparison pages ---
    _build_vs_pages(env, all_nav, all_brands_by_cohort, ready_cohorts)

    # --- Auto-generate sitemap.xml ---
    from datetime import date
    today = date.today().isoformat()
    public_pages = sorted(
        p.name for p in SITE.glob("*.html")
        if not p.name.startswith("thank-you-")
    )
    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for page in public_pages:
        sitemap_lines.append(
            f"  <url>"
            f"<loc>{SITE_BASE_URL}{page}</loc>"
            f"<lastmod>{today}</lastmod>"
            f"</url>"
        )
    sitemap_lines.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(sitemap_lines) + "\n")
    print("  Built: site/sitemap.xml")

    # --- Auto-generate robots.txt ---
    thank_you_pages = sorted(
        p.name for p in SITE.glob("thank-you-*.html")
    )
    robots_lines = ["User-agent: *", "Disallow: /reports/"]
    for ty_page in thank_you_pages:
        robots_lines.append(f"Disallow: /{ty_page}")
    robots_lines.append("")
    robots_lines.append(f"Sitemap: {SITE_BASE_URL}sitemap.xml")
    (SITE / "robots.txt").write_text("\n".join(robots_lines) + "\n")
    print("  Built: site/robots.txt")

    print(f"\nSite built successfully. {total_pages} pages rendered to site/.")


if __name__ == "__main__":
    build_site()
