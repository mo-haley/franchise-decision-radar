#!/usr/bin/env python3
"""
Fee Burden Model — Mosquito Pest Control Franchise Cohort

Computes estimated annual ongoing fee burden for each brand at standard
gross revenue levels ($200K, $300K, $400K, $500K).

Source: 2025 FDDs filed with Wisconsin DFI
Methodology: docs/fee_modeling_framework.md

Usage:
    python scripts/fee_burden_model.py
    python scripts/fee_burden_model.py --validate  # compare against baseline
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

EXTRACTED_DIR = Path("data/extracted")


# ---------------------------------------------------------------------------
# Canonical data loader — reads fee parameters from extracted JSON
# ---------------------------------------------------------------------------


def load_brand_fees(brand_slug: str) -> dict:
    """Load fee data from canonical extracted JSON for a brand.

    Returns the raw.item_6_other_fees subtree.
    Raises FileNotFoundError if the brand JSON does not exist.
    """
    path = EXTRACTED_DIR / f"{brand_slug}.json"
    with open(path) as f:
        data = json.load(f)
    return data["raw"]["item_6_other_fees"]


def get_royalty_rate(fees: dict) -> Optional[float]:
    """Extract base royalty rate (percentage) from loaded fee data.

    Returns None if the rate is ambiguous (e.g., tiered) and value is null.
    """
    rr = fees.get("royalty_rate", {})
    val = rr.get("value")
    if val is not None:
        return val / 100.0  # convert 10.0 -> 0.10
    return None


def get_royalty_tiers(fees: dict) -> Optional[list[dict]]:
    """Extract royalty tier structure from loaded fee data.

    Returns a list of tier dicts with 'threshold_up_to' and 'rate' keys,
    or None if tiers are not present.
    """
    rr = fees.get("royalty_rate", {})
    tiers = rr.get("tiers")
    if tiers and isinstance(tiers, list) and len(tiers) > 0:
        return tiers
    return None


def compute_tiered_royalty(gross_revenue: int, tiers: list[dict]) -> float:
    """Compute royalty from marginal rate tiers.

    Each tier applies its rate to the revenue band between the previous
    tier's threshold and this tier's threshold_up_to. The final tier
    (threshold_up_to=null) applies to all remaining revenue.
    """
    total = 0.0
    prev_threshold = 0
    for tier in tiers:
        rate = tier["rate"] / 100.0
        threshold = tier.get("threshold_up_to")
        if threshold is None:
            # Final uncapped tier
            total += (gross_revenue - prev_threshold) * rate
            break
        elif gross_revenue <= threshold:
            total += (gross_revenue - prev_threshold) * rate
            break
        else:
            total += (threshold - prev_threshold) * rate
            prev_threshold = threshold
    return total


def get_technology_fee_monthly(fees: dict) -> Optional[float]:
    """Extract flat monthly technology fee from loaded fee data.

    Returns None if the fee is ambiguous (e.g., tiered or range).
    """
    tf = fees.get("technology_fee", {})
    if tf.get("field_status") == "extracted" and tf.get("value") is not None:
        return tf["value"]
    return None


def get_marketing_component_rate(fees: dict, component_name: str) -> Optional[float]:
    """Extract a marketing component's percentage rate by name.

    Returns the rate as a decimal (e.g., 2.0 -> 0.02), or None if not found
    or value is null.
    """
    mktg = fees.get("advertising_and_marketing", {})
    for comp in mktg.get("components", []):
        if comp.get("name") == component_name and comp.get("value") is not None:
            return comp["value"] / 100.0
    return None


def get_marketing_component_floor(fees: dict, component_name: str) -> Optional[float]:
    """Extract a marketing component's minimum_dollar floor by name.

    Returns the annual dollar floor, or None if not found or value is null.
    """
    mktg = fees.get("advertising_and_marketing", {})
    for comp in mktg.get("components", []):
        if comp.get("name") == component_name and comp.get("minimum_dollar") is not None:
            return comp["minimum_dollar"]
    return None


def get_marketing_component_flat_annual(fees: dict, component_name: str) -> Optional[float]:
    """Extract a marketing component's minimum_dollar as a flat annual fee.

    For components with no percentage rate (value is null), minimum_dollar
    represents the annual flat-fee amount. Returns None if not found.
    """
    mktg = fees.get("advertising_and_marketing", {})
    for comp in mktg.get("components", []):
        if comp.get("name") == component_name:
            if comp.get("value") is None and comp.get("minimum_dollar") is not None:
                return comp["minimum_dollar"]
    return None


def get_other_fee(fees: dict, fee_name: str) -> Optional[float]:
    """Extract a named fee from other_fees array.

    Returns the numeric value, or None if not found or value is null.
    """
    for fee in fees.get("other_fees", []):
        if fee.get("fee_name") == fee_name and fee.get("value") is not None:
            return fee["value"]
    return None


@dataclass
class FeeBreakdown:
    """Itemized annual fee burden for a single brand at a given revenue level."""
    brand: str
    gross_revenue: int
    royalty: float = 0.0
    marketing: float = 0.0
    technology: float = 0.0
    call_center: float = 0.0
    convention: float = 0.0
    website_digital: float = 0.0
    software_vendor: float = 0.0
    bookkeeping: float = 0.0
    sales_center: float = 0.0
    notes: list[str] = field(default_factory=list)

    @property
    def total(self) -> float:
        return (
            self.royalty
            + self.marketing
            + self.technology
            + self.call_center
            + self.convention
            + self.website_digital
            + self.software_vendor
            + self.bookkeeping
            + self.sales_center
        )

    @property
    def pct_of_revenue(self) -> float:
        if self.gross_revenue == 0:
            return 0.0
        return (self.total / self.gross_revenue) * 100

    def to_dict(self) -> dict:
        return {
            "brand": self.brand,
            "gross_revenue": self.gross_revenue,
            "royalty": self.royalty,
            "marketing": self.marketing,
            "technology": self.technology,
            "call_center": self.call_center,
            "convention": self.convention,
            "website_digital": self.website_digital,
            "software_vendor": self.software_vendor,
            "bookkeeping": self.bookkeeping,
            "sales_center": self.sales_center,
            "total": round(self.total, 2),
            "pct_of_revenue": round(self.pct_of_revenue, 1),
            "notes": self.notes,
        }


# ---------------------------------------------------------------------------
# Brand fee models — Year 5 assumptions, single territory
#
# Each function loads canonical fee parameters from extracted JSON via
# load_brand_fees(), then applies modeled assumptions (tiers, floors, caps,
# year-of-operation logic) that are not structured in the extraction layer.
#
# Parameters marked HARDCODED: are values that exist only in free-text notes
# in the extracted JSON and cannot yet be loaded programmatically. These are
# candidates for future schema enrichment.
# ---------------------------------------------------------------------------


def model_mosquito_authority(gross_revenue: int) -> FeeBreakdown:
    """
    Mosquito Authority (Main Line Brands LLC) — 2025 FDD

    Source: data/extracted/mosquito-authority.json
    Royalty: 10% of Gross Revenues, min $500/mo at Y5 (pp. 15, 18)
    Marketing: max($5,500, 5% of Gross Sales) annually (pp. 15, 19-20)
    Technology: tiered $100–$1,200/mo by trailing revenue (pp. 16, 21)
    Website/Digital: $250/mo (p. 15)
    National Marketing Fund: reserved up to 3% but NOT implemented — excluded
    """
    fees = load_brand_fees("mosquito-authority")
    fb = FeeBreakdown(brand="Mosquito Authority", gross_revenue=gross_revenue)

    # Royalty: loaded rate, or minimum $500/mo at Y5, whichever greater
    royalty_rate = get_royalty_rate(fees)  # 0.10 from JSON
    royalty_pct = gross_revenue * royalty_rate
    # HARDCODED: minimum royalty schedule (Y5: $500/mo) — only in notes
    royalty_min = 500 * 12
    fb.royalty = max(royalty_pct, royalty_min)
    if royalty_min > royalty_pct:
        fb.notes.append(
            f"Minimum royalty ({royalty_min:,.0f}) exceeds percentage ({royalty_pct:,.0f})"
        )

    # Marketing: loaded rate and floor from component
    local_ad_rate = get_marketing_component_rate(
        fees, "Minimum Individual Local Advertising Expense"
    )  # 0.05 from JSON
    local_ad_floor = get_marketing_component_floor(
        fees, "Minimum Individual Local Advertising Expense"
    )  # 5500 from JSON minimum_dollar
    fb.marketing = max(local_ad_floor, gross_revenue * local_ad_rate)

    # Technology: tiered by trailing 12-month gross revenue
    # HARDCODED: entire tier table — only in technology_fee.notes free text
    tech_tiers = [
        (50_000, 100), (150_000, 200), (250_000, 300), (350_000, 400),
        (450_000, 500), (550_000, 600), (650_000, 700), (750_000, 800),
        (850_000, 900), (950_000, 1000), (1_050_000, 1100),
    ]
    monthly_tech = 1200  # default to max tier
    for threshold, rate in tech_tiers:
        if gross_revenue <= threshold:
            monthly_tech = rate
            break
    fb.technology = monthly_tech * 12

    # Website/Digital Footprint: loaded from other_fees
    website_monthly = get_other_fee(fees, "Local Website/Digital Footprint")  # 250
    fb.website_digital = website_monthly * 12

    fb.notes.append(
        "National Marketing Fee (up to 3%) reserved but NOT implemented — excluded"
    )

    return fb


def model_mosquito_hunters(gross_revenue: int) -> FeeBreakdown:
    """
    Mosquito Hunters (Mosquito Hunters, LLC) — 2025 FDD

    Source: data/extracted/mosquito-hunters.json
    Royalty: 10% of Net Revenues (p. 15)
    Marketing: greater of $37,500 or 10% of Net Revenues total, via 3 components (pp. 15-16, 19-20)
      - Local: max($8,000, 2%)
      - Centrally Managed Media: max($26,500, 7%)
      - Tools & Programs: max($3,000, 1%)
    Technology: $150/mo (increases to $250 at $1M cumulative) (p. 15)
    Call Center: $750/mo (p. 17)
    Convention: up to $2,000/yr (p. 17)
    """
    fees = load_brand_fees("mosquito-hunters")
    fb = FeeBreakdown(brand="Mosquito Hunters", gross_revenue=gross_revenue)

    # Royalty: loaded rate
    royalty_rate = get_royalty_rate(fees)  # 0.10 from JSON
    fb.royalty = gross_revenue * royalty_rate
    fb.notes.append(
        "'Net Revenues' excludes taxes/refunds; modeled as Gross Revenue (slight overestimate)"
    )

    # Marketing: 3 components with loaded rates and floors from JSON
    local_rate = get_marketing_component_rate(
        fees, "Local Advertising Obligation"
    )  # 0.02
    media_rate = get_marketing_component_rate(
        fees, "Centrally Managed Media Fund"
    )  # 0.07
    tools_rate = get_marketing_component_rate(
        fees, "Centrally Managed Tools and Programs Fund"
    )  # 0.01
    local_floor = get_marketing_component_floor(
        fees, "Local Advertising Obligation"
    )  # 8000 from JSON minimum_dollar
    media_floor = get_marketing_component_floor(
        fees, "Centrally Managed Media Fund"
    )  # 26500 from JSON minimum_dollar
    tools_floor = get_marketing_component_floor(
        fees, "Centrally Managed Tools and Programs Fund"
    )  # 3000 from JSON minimum_dollar
    local = max(local_floor, gross_revenue * local_rate)
    media = max(media_floor, gross_revenue * media_rate)
    tools = max(tools_floor, gross_revenue * tools_rate)
    fb.marketing = local + media + tools

    # Technology: loaded flat fee
    tech_monthly = get_technology_fee_monthly(fees)  # 150
    fb.technology = tech_monthly * 12

    # Call Center: loaded from other_fees
    call_center_monthly = get_other_fee(fees, "Call Center Fees")  # 750
    fb.call_center = call_center_monthly * 12

    # Convention: loaded from other_fees
    convention_annual = get_other_fee(fees, "Convention/Conference Fee")  # 2000
    fb.convention = convention_annual

    if gross_revenue < 375_000:
        fb.notes.append(
            f"At ${gross_revenue:,}, marketing floor ($37,500) exceeds "
            f"10% (${gross_revenue * 0.10:,.0f}). "
            "Dollar floor is regressive — costs more as % of revenue for smaller operators."
        )

    return fb


def model_mosquito_joe(gross_revenue: int) -> FeeBreakdown:
    """
    Mosquito Joe (Mosquito Joe SPV LLC) — 2025 FDD

    Source: data/extracted/mosquito-joe.json
    Royalty: 10% on first $500K per territory per calendar year, 7% above (pp. 28-29)
    MAP Fee: 2% of Gross Sales (p. 28)
    DMP: $37,000/yr standard, $26,000 if prior year GS >= $450K (pp. 30-31)
    SEO: $325/mo (p. 31)
    Technology: $371/mo (p. 30)
    Call Center: $199.99/mo base (p. 31) — per-sale variable excluded
    Convention: up to $1,000/yr (p. 32)
    LMG: 2% of GS, "may be required" — excluded (conditional)
    Local Performance Marketing: $35K first 12 months — excluded (startup cost)
    """
    fees = load_brand_fees("mosquito-joe")
    fb = FeeBreakdown(brand="Mosquito Joe", gross_revenue=gross_revenue)

    # Royalty: tiered — loaded from structured tiers in JSON
    tiers = get_royalty_tiers(fees)
    if tiers:
        fb.royalty = compute_tiered_royalty(gross_revenue, tiers)
    else:
        # Fallback: hardcoded tiers if structured data missing
        if gross_revenue <= 500_000:
            fb.royalty = gross_revenue * 0.10
        else:
            fb.royalty = (500_000 * 0.10) + ((gross_revenue - 500_000) * 0.07)

    # MAP Fee (Brand Fund): loaded rate
    map_rate = get_marketing_component_rate(
        fees, "MAP Fee (Brand Fund)"
    )  # 0.02
    map_fee = gross_revenue * map_rate

    # HARDCODED: DMP amounts ($37K/$26K) and threshold ($450K) — only in component notes
    if gross_revenue >= 450_000:
        dmp = 26_000
        fb.notes.append("DMP reduced to $26,000 (prior year GS >= $450K discount)")
    else:
        dmp = 37_000

    # SEO: flat annual fee loaded from component minimum_dollar
    seo = get_marketing_component_flat_annual(fees, "SEO Program Fee")  # 3900 from JSON

    fb.marketing = map_fee + dmp + seo

    # Technology: loaded flat fee
    tech_monthly = get_technology_fee_monthly(fees)  # 371
    fb.technology = tech_monthly * 12

    # Call Center: loaded from other_fees
    call_center_monthly = get_other_fee(fees, "Call Center Program")  # 199.99
    fb.call_center = call_center_monthly * 12

    # Convention: loaded from other_fees
    convention_annual = get_other_fee(fees, "Convention Fee")  # 1000
    fb.convention = convention_annual

    fb.notes.append(
        "Excludes LMG (2%, conditional) and Local Performance Marketing ($35K, first year only)"
    )
    fb.notes.append("Excludes per-closed-sale call center fee ($25/sale)")

    return fb


def model_mosquito_shield(gross_revenue: int) -> FeeBreakdown:
    """
    Mosquito Shield (Mosquito Shield Franchise, LLC) — 2025 FDD

    Source: data/extracted/mosquito-shield.json
    Royalty: 8% of Gross Sales (p. 14)
    Brand Fund: 2% of Gross Sales (p. 14)
    Local Ad: greater of $50,000 or 10% of gross revenues annually, after Y1 (pp. 14-15)
    Bookkeeping: $200–$500/mo mandatory vendor (p. 16) — modeled at low ($200/mo)
    Sales Center: $300–$750/mo (p. 16) — modeled at low ($300/mo)
    Minimum Gross Sales shortfall: Y5 threshold $283,500 — modeled separately
    """
    fees = load_brand_fees("mosquito-shield")
    fb = FeeBreakdown(brand="Mosquito Shield", gross_revenue=gross_revenue)

    # Royalty: loaded rate
    royalty_rate = get_royalty_rate(fees)  # 0.08 from JSON
    fb.royalty = gross_revenue * royalty_rate

    # Brand Fund: loaded rate from component
    brand_fund_rate = get_marketing_component_rate(
        fees, "Brand Fund Fee"
    )  # 0.02
    brand_fund = gross_revenue * brand_fund_rate

    # Local Ad: loaded rate and floor from component
    local_ad_rate = get_marketing_component_rate(
        fees, "Local Advertising"
    )  # 0.10
    local_ad_floor = get_marketing_component_floor(
        fees, "Local Advertising"
    )  # 50000 from JSON minimum_dollar
    local_ad = max(local_ad_floor, gross_revenue * local_ad_rate)

    fb.marketing = brand_fund + local_ad

    # HARDCODED: bookkeeping and sales center low-end estimates — values are null
    # in JSON (ranges only in notes: $200-$500/mo and $300-$750/mo)
    # Modeled assumption: use low end
    fb.bookkeeping = 200 * 12
    fb.sales_center = 300 * 12

    fb.notes.append(
        "Bookkeeping/Sales Center modeled at low end ($200/$300 per mo). "
        "High end ($500/$750) would add $9,000/yr."
    )

    # HARDCODED: Minimum Gross Sales shortfall (Y5: $283,500) — only in royalty notes
    min_gross_sales_y5 = 283_500
    if gross_revenue < min_gross_sales_y5:
        shortfall_penalty = (0.07 * min_gross_sales_y5) - (royalty_rate * gross_revenue)
        if shortfall_penalty > 0:
            fb.notes.append(
                f"⚠ MINIMUM GROSS SALES SHORTFALL: At ${gross_revenue:,}, franchisor may collect "
                f"${shortfall_penalty:,.0f} additional (7% of ${min_gross_sales_y5:,} threshold minus "
                f"actual royalty). This is NOT included in the total — it is discretionary."
            )

    return fb


def model_mosquito_squad(gross_revenue: int) -> FeeBreakdown:
    """
    Mosquito Squad (Mosquito Squad Franchising SPE LLC) — 2025 FDD

    Source: data/extracted/mosquito-squad.json
    Royalty: 10% on first $250K, 9% on $250K–$500K, 8% above $500K (pp. 19-20)
      Min $1,250/mo at Y5 ($15K/yr). At $200K+, percentage exceeds min.
    Brand Fund: $350/mo at Y5, escalating (pp. 20-21) — flat fee, not percentage
    Local Marketing: max($35,000, 10% of prior year GR), capped at $50,000 (p. 21)
    Website: $350/mo (p. 22)
    Technology: $60/mo (p. 22)
    ServiceMinder: $280/mo + $25/mo per user (p. 22) — vendor-paid, mandatory
    Convention: $600/yr max on-site registration (p. 25)
    Call Center: $2–$3/min, NOT required — excluded
    """
    fees = load_brand_fees("mosquito-squad")
    fb = FeeBreakdown(brand="Mosquito Squad", gross_revenue=gross_revenue)

    # Royalty: triple-tiered marginal rate — loaded from structured tiers in JSON
    tiers = get_royalty_tiers(fees)
    if tiers:
        fb.royalty = compute_tiered_royalty(gross_revenue, tiers)
    else:
        # Fallback: hardcoded tiers if structured data missing
        if gross_revenue <= 250_000:
            fb.royalty = gross_revenue * 0.10
        elif gross_revenue <= 500_000:
            fb.royalty = (250_000 * 0.10) + ((gross_revenue - 250_000) * 0.09)
        else:
            fb.royalty = (250_000 * 0.10) + (250_000 * 0.09) + ((gross_revenue - 500_000) * 0.08)

    # HARDCODED: minimum royalty (Y5: $1,250/mo) — only in royalty_rate.notes
    royalty_min = 1_250 * 12
    if royalty_min > fb.royalty:
        fb.notes.append(
            f"Minimum royalty (${royalty_min:,}) exceeds percentage (${fb.royalty:,.0f})"
        )
        fb.royalty = royalty_min

    # HARDCODED: Brand Fund flat $350/mo at Y5 — escalating schedule only in
    # component notes, component value is null
    brand_fund = 350 * 12

    # Local Marketing: loaded rate and floor from component, cap still hardcoded
    local_mktg_rate = get_marketing_component_rate(
        fees, "Local Marketing"
    )  # 0.10
    local_mktg_floor = get_marketing_component_floor(
        fees, "Local Marketing"
    )  # 35000 from JSON minimum_dollar
    # HARDCODED: cap ($50,000) — no maximum_dollar field in schema yet
    local_mktg = min(max(local_mktg_floor, gross_revenue * local_mktg_rate), 50_000)

    fb.marketing = brand_fund + local_mktg

    # Website: loaded from marketing components (stored there, not other_fees)
    # HARDCODED: $350/mo — component value is null in JSON, amount only in notes
    fb.website_digital = 350 * 12

    # Technology: loaded flat fee
    tech_monthly = get_technology_fee_monthly(fees)  # 60
    fb.technology = tech_monthly * 12

    # ServiceMinder: loaded base from other_fees, plus per-user assumption
    serviceminder_monthly = get_other_fee(
        fees, "ServiceMinder (operational software)"
    )  # 280
    # HARDCODED: +$25/user, modeled at 1 additional user — assumption
    fb.software_vendor = (serviceminder_monthly + 25) * 12

    # Convention: loaded from other_fees
    convention_annual = get_other_fee(fees, "Annual Conference")  # 600
    fb.convention = convention_annual

    fb.notes.append(
        "Brand Fund is flat fee ($350/mo at Y5), not percentage-based "
        "— does not scale with revenue"
    )
    fb.notes.append(
        "Local marketing capped at $50,000/yr — cost ceiling that other brands lack"
    )

    return fb


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

REVENUE_LEVELS = [200_000, 300_000, 400_000, 500_000]
BRAND_MODELS = {
    "Mosquito Authority": model_mosquito_authority,
    "Mosquito Hunters": model_mosquito_hunters,
    "Mosquito Joe": model_mosquito_joe,
    "Mosquito Shield": model_mosquito_shield,
    "Mosquito Squad": model_mosquito_squad,
}


def run_model() -> list[dict]:
    """Run the fee model for all brands at all revenue levels."""
    results = []
    for revenue in REVENUE_LEVELS:
        for brand_name, model_fn in BRAND_MODELS.items():
            fb = model_fn(revenue)
            results.append(fb.to_dict())
    return results


def validate_against_baseline(results: list[dict]) -> bool:
    """Compare current results against saved baseline output.

    Returns True if outputs match, False otherwise.
    Prints detailed diff on mismatch.
    """
    baseline_path = Path("data/derived/fee_burden_model_output_baseline.json")
    if not baseline_path.exists():
        print(f"ERROR: Baseline file not found at {baseline_path}")
        print("Run the pre-refactor version first to generate the baseline.")
        return False

    with open(baseline_path) as f:
        baseline = json.load(f)

    baseline_results = baseline["results"]

    if len(results) != len(baseline_results):
        print(f"FAIL: Result count mismatch: {len(results)} vs {len(baseline_results)}")
        return False

    mismatches = []
    for i, (new, old) in enumerate(zip(results, baseline_results)):
        for key in ["brand", "gross_revenue", "royalty", "marketing", "technology",
                     "call_center", "convention", "website_digital", "software_vendor",
                     "bookkeeping", "sales_center", "total", "pct_of_revenue"]:
            if new.get(key) != old.get(key):
                mismatches.append(
                    f"  [{new['brand']} @ ${new['gross_revenue']:,}] "
                    f"{key}: {old.get(key)} -> {new.get(key)}"
                )

    if mismatches:
        print(f"FAIL: {len(mismatches)} value mismatch(es):")
        for m in mismatches:
            print(m)
        return False

    print("PASS: All numeric outputs match baseline exactly.")
    return True


def print_summary_table(results: list[dict]) -> None:
    """Print a formatted summary table."""
    print("\n" + "=" * 100)
    print("ANNUAL ONGOING FEE BURDEN — MOSQUITO PEST CONTROL FRANCHISE COHORT")
    print("Year 5 assumptions, single territory, 2025 FDD data")
    print("=" * 100)

    for revenue in REVENUE_LEVELS:
        print(f"\n--- At ${revenue:,} Gross Revenue ---\n")
        print(f"{'Brand':<25} {'Royalty':>10} {'Marketing':>12} {'Tech+Other':>12} {'TOTAL':>12} {'% of Rev':>10}")
        print("-" * 85)

        level_results = [r for r in results if r["gross_revenue"] == revenue]
        level_results.sort(key=lambda x: x["total"])

        for r in level_results:
            tech_other = (
                r["technology"] + r["call_center"] + r["convention"]
                + r["website_digital"] + r["software_vendor"]
                + r["bookkeeping"] + r["sales_center"]
            )
            print(
                f"{r['brand']:<25} "
                f"${r['royalty']:>9,.0f} "
                f"${r['marketing']:>11,.0f} "
                f"${tech_other:>11,.0f} "
                f"${r['total']:>11,.0f} "
                f"{r['pct_of_revenue']:>8.1f}%"
            )

        cheapest = level_results[0]
        most_expensive = level_results[-1]
        spread = most_expensive["total"] - cheapest["total"]
        print(f"\n  Spread: ${spread:,.0f} ({cheapest['brand']} to {most_expensive['brand']})")

    print("\n" + "=" * 100)
    print("NOTES:")
    for revenue in REVENUE_LEVELS:
        level_results = [r for r in results if r["gross_revenue"] == revenue]
        for r in level_results:
            if r["notes"]:
                for note in r["notes"]:
                    print(f"  [{r['brand']} @ ${revenue:,}] {note}")
    print()


def print_component_detail(results: list[dict]) -> None:
    """Print detailed component breakdown for each brand at each level."""
    print("\n" + "=" * 100)
    print("COMPONENT DETAIL")
    print("=" * 100)

    for revenue in REVENUE_LEVELS:
        print(f"\n{'=' * 50}")
        print(f"  AT ${revenue:,} GROSS REVENUE")
        print(f"{'=' * 50}")

        level_results = [r for r in results if r["gross_revenue"] == revenue]
        level_results.sort(key=lambda x: x["total"])

        for r in level_results:
            print(f"\n  {r['brand']}:")
            if r["royalty"]:
                print(f"    Royalty:          ${r['royalty']:>10,.0f}")
            if r["marketing"]:
                print(f"    Marketing:        ${r['marketing']:>10,.0f}")
            if r["technology"]:
                print(f"    Technology:        ${r['technology']:>10,.0f}")
            if r["website_digital"]:
                print(f"    Website/Digital:   ${r['website_digital']:>10,.0f}")
            if r["software_vendor"]:
                print(f"    Software (vendor): ${r['software_vendor']:>10,.0f}")
            if r["call_center"]:
                print(f"    Call Center:       ${r['call_center']:>10,.0f}")
            if r["bookkeeping"]:
                print(f"    Bookkeeping:       ${r['bookkeeping']:>10,.0f}")
            if r["sales_center"]:
                print(f"    Sales Center:      ${r['sales_center']:>10,.0f}")
            if r["convention"]:
                print(f"    Convention:        ${r['convention']:>10,.0f}")
            print(f"    {'─' * 30}")
            print(f"    TOTAL:            ${r['total']:>10,.0f}  ({r['pct_of_revenue']:.1f}% of revenue)")


def main() -> None:
    """Run the model and output results."""
    results = run_model()

    if "--validate" in sys.argv:
        success = validate_against_baseline(results)
        sys.exit(0 if success else 1)

    print_summary_table(results)
    print_component_detail(results)

    # Save structured output
    output_dir = Path("data/derived")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "fee_burden_model_output.json"

    output = {
        "model_version": "1.1",
        "methodology": "docs/fee_modeling_framework.md",
        "assumptions": {
            "year_of_operation": 5,
            "territories": 1,
            "employees": "1 owner + 1 technician",
            "revenue_basis": "Gross Sales/Revenue (treated as equivalent)",
        },
        "revenue_levels": REVENUE_LEVELS,
        "results": results,
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nStructured output saved to: {output_path}")


if __name__ == "__main__":
    main()
