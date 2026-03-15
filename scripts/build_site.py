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

# TODO: Replace with production domain when deployed (e.g. "https://franchisedecisionradar.com/")
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
}

BRAND_META_DESCRIPTIONS: dict[str, str] = {
    "mosquito-authority": "Review Mosquito Authority franchise cost, ongoing fees, system health, and key risks using regulator-source data before deciding whether to buy.",
    "mosquito-hunters": "Review Mosquito Hunters franchise cost, fee structure, system health, and major buyer watchouts using public franchise disclosure data.",
    "mosquito-joe": "Review Mosquito Joe franchise fees, startup cost, system health, and key risks using public disclosure data for serious franchise buyers.",
    "mosquito-shield": "Review Mosquito Shield franchise cost, ongoing fees, system health signals, and key buyer risks before committing capital.",
    "mosquito-squad": "Review Mosquito Squad franchise cost, royalty structure, system health, and major decision factors using regulator-source data.",
}

BRAND_DIFFERENTIATORS: dict[str, str] = {
    "mosquito-authority": "Lowest fee burden",
    "mosquito-hunters": "3-brand license",
    "mosquito-joe": "Highest marketing spend",
    "mosquito-shield": "Fastest growth",
    "mosquito-squad": "Highest avg revenue",
}

# Stripe Payment Links — add real URLs as reports go live.
STRIPE_PAYMENT_LINKS: dict[str, str | None] = {
    "mosquito-authority": None,
    "mosquito-hunters": None,
    "mosquito-joe": None,
    "mosquito-shield": None,
    "mosquito-squad": None,
}

# Mosquito-specific cost page editorial
MOSQUITO_FEE_NOTES: dict[str, str] = {
    "Mosquito Authority": "Hometown ($25K) vs Full-Size ($45K) tiers",
    "Mosquito Hunters": "$50K license + $57K training/supply. Highest fee in cohort.",
    "Mosquito Joe": "Standard single territory. Discounts available.",
    "Mosquito Shield": "First territory. Multi-territory discounts available.",
    "Mosquito Squad": "Standard territory (350K\u2013500K pop). Micro territory $35K.",
}

MOSQUITO_RESERVES: dict[str, str] = {
    "Mosquito Squad": "12 months",
}

MOSQUITO_ROYALTY: dict[str, tuple[str, str]] = {
    "Mosquito Authority": ("10%", "Flat rate. Min $500/mo at Year 5."),
    "Mosquito Hunters": ("10%", "Flat rate. Plus 15% on out-of-territory revenue."),
    "Mosquito Joe": ("10% / 7%", "10% on first $500K, 7% above. Rewards growth."),
    "Mosquito Shield": ("8%", "Flat rate \u2014 lowest in cohort. Min Gross Sales shortfall penalty."),
    "Mosquito Squad": ("10% / 9% / 8%", "Triple-tiered by revenue bracket. Min $3K/mo at Year 9+."),
}

MOSQUITO_ROYALTY_ORDER = [
    "Mosquito Shield", "Mosquito Squad", "Mosquito Joe",
    "Mosquito Authority", "Mosquito Hunters",
]

MOSQUITO_INVESTMENT_DETAILS: list[dict] = [
    {"brand_name": "Mosquito Authority", "detail": "$15K&ndash;$25K pre-opening marketing. Vehicle $0&ndash;$30K (zero if owned). 3-mo reserves."},
    {"brand_name": "Mosquito Hunters", "detail": "<strong>$57K mandatory training/supply fee</strong> (on top of $50K license). $6K&ndash;$14K holiday lighting inventory. 3-mo reserves."},
    {"brand_name": "Mosquito Joe", "detail": "<strong>$72K in mandatory marketing</strong> ($37K DMP + $35K local). These two items alone are nearly half the total. 3-mo reserves."},
    {"brand_name": "Mosquito Shield", "detail": "$23.6K mandatory Starter Package. $35K&ndash;$50K first-year local advertising. 3-mo reserves."},
    {"brand_name": "Mosquito Squad", "detail": "$9.5K business outfitting + $4K&ndash;$9.5K truck outfitting. <strong>12-month reserves ($84K&ndash;$117K)</strong>."},
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
        data["brand"]["brand_name"]: data["derived"]["initial_investment_midpoint"]
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
        item7 = data["raw"]["item_7_initial_investment"]
        item6 = data["raw"]["item_6_other_fees"]
        derived = data["derived"]

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
            "total_low": item7["total_low"],
            "total_high": item7["total_high"],
            "midpoint": derived["initial_investment_midpoint"],
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
        item7 = data["raw"]["item_7_initial_investment"]
        item6 = data["raw"]["item_6_other_fees"]
        sorted_years = sorted(years, key=lambda y: y["year"])
        y_last = sorted_years[-1]

        franchised_end = y_last["total_outlets_end"] - (y_last.get("company_owned_end") or 0)

        inv_low = item7["total_low"]
        inv_high = item7["total_high"]
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
            "brand_short": brand_name.split(" ", 1)[-1] if " " in brand_name else brand_name,
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
    """Build combined navigation data for all cohorts."""
    result = []
    for cohort in cohorts:
        cohort_nav = {
            "id": cohort["id"],
            "short_name": cohort["short_name"],
            "pages": build_nav_pages(cohort),
        }
        result.append(cohort_nav)
    return result


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
    all_nav = build_all_nav(cohorts)
    total_pages = 0

    # Pre-collect brand info for all cohorts (needed by footer on every page)
    all_brands_by_cohort: list[dict] = []
    for cohort in cohorts:
        pre_brands = load_brand_data(cohort["brands"])
        all_brands_by_cohort.append({
            "id": cohort["id"],
            "display_name": cohort["display_name"],
            "short_name": cohort["short_name"],
            "brands": [
                {"name": pre_brands[s]["brand"]["brand_name"], "slug": s}
                for s in cohort["brands"]
            ],
        })

    for cohort in cohorts:
        brand_slugs = cohort["brands"]
        brands = load_brand_data(brand_slugs)
        slug_map = build_slug_map(brands)
        prefix = cohort["url_prefix"]

        fee_model = None
        if cohort.get("has_fee_model") and cohort.get("fee_model_file"):
            fee_model = load_fee_model(cohort["fee_model_file"])

        nav_pages = build_nav_pages(cohort)

        shared = {
            "site_base_url": SITE_BASE_URL,
            "nav_pages": nav_pages,
            "all_nav": all_nav,
            "all_brands_by_cohort": all_brands_by_cohort,
            "cohort_id": cohort["id"],
            "cohort_display_name": cohort["display_name"],
            "cohort_short_name": cohort["short_name"],
            "cohort_brand_count": len(brand_slugs),
            "brand_slug_map": slug_map,
        }

        # Fee burden (only if model exists)
        if fee_model and "fee-burden" in cohort["comparison_pages"]:
            fee_ctx = build_fee_context(fee_model, brands)
            active = f"{prefix}fee-burden" if prefix else "fee-burden"
            render_page(env, "fee-burden.html", f"{prefix}fee-burden.html", {
                **shared, "active_page": active, **fee_ctx,
            })
            total_pages += 1

        # System health
        if "system-health" in cohort["comparison_pages"]:
            health_ctx = build_health_context(brands, slug_map)
            active = f"{prefix}system-health" if prefix else "system-health"
            render_page(env, "system-health.html", f"{prefix}system-health.html", {
                **shared, "active_page": active, **health_ctx,
            })
            total_pages += 1

        # Cost to enter
        if "cost-to-enter" in cohort["comparison_pages"]:
            cost_ctx = build_cost_context(brands, slug_map)
            active = f"{prefix}cost-to-enter" if prefix else "cost-to-enter"
            render_page(env, "cost-to-enter.html", f"{prefix}cost-to-enter.html", {
                **shared, "active_page": active, **cost_ctx,
            })
            total_pages += 1

        # Report listing
        report_ctx = build_report_context(brands, brand_slugs)
        active = f"{prefix}report" if prefix else "report"
        render_page(env, "report.html", f"{prefix}report.html", {
            **shared, "active_page": active, **report_ctx,
        })
        total_pages += 1

        # Brand pages
        brand_ctxs = build_brand_contexts(
            brands, brand_slugs, fee_model, slug_map, cohort,
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

    # --- Homepage (multi-cohort) ---
    homepage_cohorts = []
    for cohort in cohorts:
        brand_slugs = cohort["brands"]
        brands = load_brand_data(brand_slugs)
        slug_map = build_slug_map(brands)
        fee_model = None
        if cohort.get("has_fee_model") and cohort.get("fee_model_file"):
            fee_model = load_fee_model(cohort["fee_model_file"])

        homepage_cohorts.append({
            "id": cohort["id"],
            "display_name": cohort["display_name"],
            "short_name": cohort["short_name"],
            "description": cohort["description"],
            "brand_count": len(brand_slugs),
            "brand_slugs": brand_slugs,
            "brands_data": brands,
            "brand_slug_map": slug_map,
            "has_fee_model": fee_model is not None,
            "fee_model": fee_model,
            "comparison_pages": [
                {"url": f"{cohort['url_prefix']}{pid}.html", "label": PAGE_LABELS[pid]}
                for pid in cohort["comparison_pages"]
            ],
            "report_url": f"{cohort['url_prefix']}report.html",
        })

    render_page(env, "index.html", "index.html", {
        "site_base_url": SITE_BASE_URL,
        "active_page": "home",
        "all_nav": all_nav,
        "all_brands_by_cohort": all_brands_by_cohort,
        "nav_pages": [],
        "cohorts": homepage_cohorts,
        "cohort_id": None,
    })
    total_pages += 1

    print(f"\nSite built successfully. {total_pages} pages rendered to site/.")


if __name__ == "__main__":
    build_site()
