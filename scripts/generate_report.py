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


@dataclass
class EconomicsScenario:
    name: str
    revenue: int
    franchisor_fees: int
    fee_pct: float
    est_cogs: int
    remaining: int


# ---------------------------------------------------------------------------
# Brand-specific editorial content
#
# This is the interpretive layer that makes the report worth paying for.
# It cannot be auto-generated from data alone — it is authored analysis.
# ---------------------------------------------------------------------------

BRAND_NARRATIVES: dict[str, dict] = {

"mosquito-authority": {

"executive_summary": """
<p>Within the mosquito pest control cohort (7 brands), Mosquito Authority ranks second-lowest
in ongoing franchisor fees and lowest in entry cost among the five established systems
(100+ outlets). At $300K gross revenue, annual fees total $52,800 (17.6% of revenue).
Only Mosquito Sheriff is lower at 13.2% — but Sheriff operates 5 total outlets, making
fee-burden comparison structurally asymmetric. Among the five established brands,
Authority's fees run $25,000–$33,000/year below the next peer. The system is the largest
in the cohort (546 franchised outlets) with zero terminations across the 2022–2024
reporting window.</p>

<p>A favorable relative position within this peer set does not, by itself, validate the
underlying business. Single-territory revenue — which the FDD does not directly disclose —
appears to fall in the $60K–$120K range for early-year operators (inferred, not stated;
see Item 19 section). At those revenue levels, even the cohort's lowest fee burden leaves
limited room for owner income after operating costs. The economics case depends heavily on
revenue growth and, for many operators, expansion to multiple territories.</p>

<p>The biggest risk is latent, not current: the franchisor reserves the right to implement
a national marketing fee of up to 3% of Gross Revenues at any time, which would add
$6,000–$15,000/year. The predecessor entity's regulatory history (5 state actions for
selling without registration) is real but pre-dates current ownership. Disclosure quality
is above average for this cohort, with a rich Item 19 — though a <code>#REF!</code>
spreadsheet error and minor population mismatches are quality blemishes worth noting.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Authority ranks 2nd of 7 in ongoing fee burden across the full cohort, and 1st
among the five established brands (100+ outlets). Only Mosquito Sheriff (5 outlets) models
lower. The primary driver of Authority's advantage over larger peers is marketing:
Authority's local ad minimum ($5,500 or 5%) is 4–7× lower than competitors' mandatory
marketing floors ($37,500–$75,000+).</p>
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
<strong>What this means:</strong> At $300K revenue, $247K remains after franchisor fees.
Among the five established brands (100+ outlets), the next closest is Mosquito Squad at
~$222K remaining — a $25,000/year gap. (Mosquito Sheriff, with 5 outlets, models even
lower fees but is not a comparable system.) That gap is real, but it is a difference in
fees paid, not in owner income. COGS, operating costs, vehicle, insurance, and seasonal
cash flow gaps still come out of the $247K. The fee advantage matters most for operators
who can push revenue high enough that the remaining margin covers a meaningful draw.
</div>

<div class="callout">
<div class="callout-title">Latent risk — unimplemented national marketing fee</div>
The FDD reserves the right to implement a national marketing fee of up to 3% at any time,
adding $6K–$15K/year. No timeline or conditions are specified. If activated, Authority's
burden rises to 20–21% of revenue — still below most peers, but the gap narrows significantly.
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
<p>Lowest entry floor in the cohort at $54,000, though the range extends to $127,700
(Mosquito Sheriff's range is narrower at $79K–$81K but with a higher floor). The wide
spread is driven by two variables: franchise type (Hometown $25K vs Full-Size $45K) and
vehicle ($0 if you own a qualifying truck, $30K if not).</p>
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
<p>Among the lowest attrition rates in the cohort, and the lowest among brands with 100+
outlets (FDD-disclosed, Item 20). Modest growth every year (+5, +10, +7) with no
rapid-open/rapid-close churn. For context: Mosquito Shield grew +140 in the same
period but lost 128 outlets to terminations and closures. Authority grew +22 and
lost 17. The growth is slower, but what growth occurs appears durable.</p>
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
competitors — notably simpler than Mosquito Joe's 6-layer SPV chain. All brands in
this cohort are PE-backed; this is industry-standard for mosquito pest control franchises.</p>
""",

"peer_narrative": """
<p>Among the five established brands in this cohort (100+ outlets), Authority is the only one
where you can enter for under $60K, operate with fees under 18% of revenue at $300K, and
point to a system with zero terminations. Mosquito Sheriff (5 outlets) and MosquitoNix
(8 outlets) also appear in the cohort data tables for completeness but are micro-systems;
Sheriff models lower fees but has no comparable system-health track record at scale.
Authority is not the most transparent (Squad's Item 19 is richer) or the fastest-growing
(Shield added +140 units). Its distinguishing feature is cost structure, not revenue
potential — the FDD gives less per-territory revenue visibility than Squad or Joe.</p>

<p><strong>Closest comparison: Mosquito Squad.</strong> Similar age, both PE-backed, both with
solid disclosure. Squad has better unit economics data ($484K/territory) and the richest
company-owned P&L in the cohort ($20.8M, 25.9% margin) — but costs 2× more to enter and
$25K/year more to operate at $300K revenue. A buyer choosing between these two is trading
fee savings (Authority) for disclosure depth and revenue visibility (Squad).</p>

<p><strong>Sharpest contrast: Mosquito Shield.</strong> Opposite profiles. Shield has the
fastest growth (+140) but highest churn (65 terminations in 2023). Lowest royalty (8%) but
highest local ad floor ($50K). Authority has higher royalty (10%) but the lowest total
burden. Both carry latent risks — Authority's unimplemented national fee, Shield's
churn-masked growth — that buyers should price into their models differently.</p>
""",

"discovery_questions": [
    {
        "question": "The FDD reserves a national marketing fee of up to 3%. Under what conditions would you implement it, and what timeline are you considering?",
        "context": "FDD p. 15, Note 4. Not yet active but could add $6K–$15K/year.",
        "why_it_matters": "This is the single largest latent cost risk. If activated, it adds $6K–$15K/year and narrows Authority's fee advantage over competitors. A buyer needs to price this risk into their decision.",
        "strong_answer": "'We have no plans to implement in the next 2–3 years. If we did, it would be tied to a specific national campaign with measurable ROI targets.' Specific conditions and transparency.",
        "weak_answer": "'It's in the FDD as a standard provision. We'll implement it when the time is right.' No specifics, no timeline, no criteria.",
        "follow_up": "Ask whether existing franchisee advisory councils have input on this decision. Ask if it would replace or stack on top of local ad minimums."
    },
    {
        "question": "The company-owned location in Hickory showed declining EBITDA ($72K to $53K) and negative net income both years. What's driving that trend?",
        "context": "Item 19 Part 1, pp. 51–52. Net income −$6.8K (2023), −$30.4K (2024).",
        "why_it_matters": "This is the only full P&L in the FDD. If the company-owned location's economics are deteriorating, it signals margin pressure that could affect all operators — especially a new one with less pricing power.",
        "strong_answer": "'The EBITDA decline was driven by [specific factor: new technician, call center beta costs, one-time expenses]. Here is what normalized profitability looks like.' Willing to walk through the expense categories.",
        "weak_answer": "'Amortization makes the net income look bad — it's really profitable on a cash basis.' Deflects from the EBITDA decline trend, which is the real signal.",
        "follow_up": "Ask for a breakout of the $244K total expenses. Specifically: what are the call center beta costs ($14K in 2024) and will franchisees bear a similar cost?"
    },
    {
        "question": "The Item 19 average gross revenue ($464,600) is per franchisee, not per territory. What is the average revenue for a single-territory operator?",
        "context": "Item 19 Part 2, p. 53. Average franchisee owns ~4 territories.",
        "why_it_matters": "A buyer looking at one territory cannot use the $465K headline number. The per-territory figure is likely $100K–$120K based on implied math. Confirming this directly affects your financial planning.",
        "strong_answer": "'Single-territory operators average around $[X]K in their first 2–3 years.' Specific number, willingness to share segmented data.",
        "weak_answer": "'Most of our successful franchisees expand to multiple territories quickly.' Redirects away from the question — implies single-territory economics may not work well.",
        "follow_up": "Ask how many of the 154 franchisees operate exactly one territory, and what their average revenue is."
    },
    {
        "question": "There are 3 non-renewals in 2024 — the first in the 3-year reporting period. What happened?",
        "context": "Item 20, Table 3, p. 56. Zero non-renewals in 2022–2023.",
        "why_it_matters": "Non-renewals are a signal that some franchisees chose not to continue after their term ended. In a system with zero terminations, this is the only indicator of voluntary exit dissatisfaction.",
        "strong_answer": "'Two were retirements, one was a market that didn't develop as expected.' Specific, honest, willing to provide context.",
        "weak_answer": "'Three out of 540+ is insignificant.' Dismissive. Even if statistically small, the trend change matters.",
        "follow_up": "Ask if the non-renewals were in any particular geography or franchise type (Hometown vs Full-Size)."
    },
    {
        "question": "The predecessor entity (TMA) had regulatory actions in 5 states for selling without registration. What specifically changed in the compliance process under Main Line Brands?",
        "context": "Item 3, pp. 11–13. Actions in MD, RI, VA, WI, WA (2013–2020).",
        "why_it_matters": "Five state actions for the same violation over 7 years is a pattern, not an accident. You need to understand whether the root cause was fixed or just papered over by a corporate restructuring.",
        "strong_answer": "'We hired a franchise compliance officer, built a state-by-state registration calendar, and engaged outside franchise counsel. Here's our current registration status.' Structural changes, not just new management.",
        "weak_answer": "'That was the old management team. We're a completely different company now.' Corporate veil language without describing actual process changes.",
        "follow_up": "Ask to see proof of current registration status in the states where you plan to operate."
    },
    {
        "question": "The technology fee tiers go up to $1,200/month at $1.05M+ revenue. Is there a cap, or will additional tiers be added?",
        "context": "Item 6, Note 10, p. 21. 12-tier schedule from $100–$1,200/month.",
        "why_it_matters": "If you scale to multiple territories, this fee scales aggressively. At $1M+ revenue, $14,400/year in tech fees is significant. And if there's no cap, future tiers could be added.",
        "strong_answer": "'$1,200/month is the current cap. We have no plans to add tiers. The fee covers [specific tools and services].' Clear ceiling and value justification.",
        "weak_answer": "'The tiers are reviewed periodically.' Leaves open the possibility of unlimited escalation.",
        "follow_up": "Ask what the tech fee specifically pays for — is it Dispatch Plus/FieldRoutes software licensing, or does it include any other services?"
    },
    {
        "question": "There's a #REF! error in the Item 19 table for 10+ Full Seasons franchisees. Can you provide the corrected average?",
        "context": "Item 19 Part 2, p. 55. Spreadsheet formula error in filed FDD.",
        "why_it_matters": "The 10+ season cohort (60 franchisees, 275 territories) represents the most experienced operators in the system. Their average is the most relevant benchmark for long-term economics, and it's missing from the filed document.",
        "strong_answer": "Provides the corrected number on the spot, or commits to providing it before you leave Discovery Day.",
        "weak_answer": "'We'll have to look into that. It's in the next filing.' No urgency to correct an error in the document they're selling from.",
        "follow_up": "If they provide the number, compare it to the median ($450,722). A large gap between average and median would indicate skew from a few very large operators."
    },
    {
        "question": "What does the Hometown Franchise ($25K fee, smaller territory) look like in practice? How does revenue compare to Full-Size territories?",
        "context": "Item 5, p. 13. 62 Hometown franchises as of end 2024.",
        "why_it_matters": "Hometown is the cheapest entry point ($25K fee vs $45K). But if revenue potential is proportionally lower, the economics may not be better. You need this comparison to make an informed tier choice.",
        "strong_answer": "'Hometown territories average about $[X]K. They work well for [specific buyer profile]. Here's the territory size difference.' Concrete data and honest framing.",
        "weak_answer": "'Hometown is a great option for getting started — you can always upgrade later.' Sales language without economics.",
        "follow_up": "Ask how many of the 62 Hometown operators have upgraded to Full-Size, and what the upgrade process/cost looks like."
    },
    {
        "question": "The West Chester, PA company-owned location was acquired in 2023 and sold back in 2024. What happened?",
        "context": "Item 20, Table 4, pp. 63–64. Short-lived company ownership.",
        "why_it_matters": "A franchisor briefly acquiring and then reselling a territory can mean several things: rescuing a struggling operator, testing a market, or flipping inventory. The motive matters.",
        "strong_answer": "'The previous franchisee wanted to exit. We acquired the territory to maintain service continuity and resold it to a qualified buyer within the year.' Operational rationale.",
        "weak_answer": "'That's a routine territory transition.' Vague, avoids explaining why the franchisor itself had to step in.",
        "follow_up": "Ask whether the resale price was higher or lower than the original franchise fee. Ask if this is something they do regularly."
    },
    {
        "question": "Transfer volume is ~37/year (7% of system). Are these primarily retirements, upgrades to multi-territory, or something else?",
        "context": "Item 20, Table 2. 37 transfers in 2022, 29 in 2023, 37 in 2024.",
        "why_it_matters": "Transfer motive tells you whether the resale market is healthy (owners cashing out at a gain) or distressed (owners exiting at a loss). 7% annual transfer rate is high enough to matter.",
        "strong_answer": "Specific breakdown: 'About half are retirements or lifestyle changes, the rest are multi-territory consolidation.' Willingness to connect you with recent sellers.",
        "weak_answer": "'People sell for all kinds of reasons.' No data, no specifics, won't facilitate introductions to recent sellers.",
        "follow_up": "Ask for the average sale price relative to original franchise fee. If they won't share, ask recent transferees directly."
    },
],

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Strong", "color": "strong",
     "summary": "Lowest entry floor in cohort ($54K). Among established brands (100+ outlets), the gap is wide: $54K–$128K vs $120K–$220K for peers. Mosquito Sheriff ($79K–$81K) is the only brand with a lower ceiling."},
    {"dimension": "Ongoing fee burden", "rating": "Strong", "color": "strong",
     "summary": "Ranks 2/7 in full cohort (17–18% of revenue). Only Mosquito Sheriff (5 outlets, 13%) is lower. Among the 5 established brands (100+ outlets), Authority is lowest."},
    {"dimension": "System stability", "rating": "Strong", "color": "strong",
     "summary": "Zero terminations across 3 years. Largest system in cohort (546 outlets) with 1.8% recent attrition — among the lowest, and notably low for a system this size."},
    {"dimension": "Revenue disclosure", "rating": "Mixed", "color": "mixed",
     "summary": "Rich Item 19 (company-owned P&L + franchised revenue). But data is per-franchisee, not per-territory. #REF! error in key cell."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "#REF! spreadsheet error and minor population mismatches. Not fatal, but blemishes in a six-figure decision document."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Latent 3% national marketing fee could add $6K–$15K/yr. Predecessor had 5 regulatory actions. Both manageable but real."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Strong for budget-sensitive owner-operators. Weaker for passive investors or buyers needing high revenue visibility per territory."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "Among the lowest cost and lowest attrition in the cohort, with the strongest combination of these two factors at scale. But relative advantage within the peer set does not establish that single-territory economics are strong on an absolute basis. Revenue visibility is limited."},
],

"scorecard_posture": """Within this cohort, Mosquito Authority shows the lowest entry cost among
established brands, a fee burden that ranks 2nd of 7 overall (1st among the five brands with 100+
outlets), and among the lowest franchisee attrition rates — notably low for a system of its
size (546 outlets). The fee gap is measurable and compounds over
time. However, these are relative comparisons within a seasonal, route-based pest control category
where single-territory revenue appears modest. The main limitations are disclosure clarity
(per-franchisee not per-territory revenue), latent fee risk (unimplemented 3% national marketing
fee), and the open question of whether single-territory economics support a full-time owner draw
without multi-territory expansion. A buyer should treat the comparative fee advantage as a
structural input — not as a conclusion about profitability.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive first-time buyer:</strong> Among the lowest entry costs and ongoing fees
in the cohort, which means you preserve more capital for the ramp period and retain more of
each revenue dollar after franchisor fees than at most peers.</li>
<li><strong>Owner-operator:</strong> The economics work best when you are the primary service
provider in the early years. The company-owned P&L includes a $48K manager salary — if you
operate yourself, that becomes your draw, not an expense.</li>
<li><strong>Buyer who prioritizes low measured attrition:</strong> Zero terminations and steady
growth over the 3-year reporting window. This is a system with low disclosed churn —
not a guarantee of future stability, but a stronger track record than most peers in this cohort.</li>
<li><strong>Buyer comfortable with seasonality:</strong> Mosquito control is seasonal (spring–fall
in most markets). You need personal reserves or off-season income plans for winter months.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Passive or semi-absentee investor:</strong> At single-territory revenue levels
($100K–$190K in early years), there is not enough margin to pay a manager and still generate
meaningful returns. This is an owner-operator business until you scale to multiple territories.</li>
<li><strong>Buyer who needs precise revenue projections:</strong> The Item 19 gives averages
per franchisee (not per territory), making single-territory projections an exercise in
inference rather than direct lookup.</li>
<li><strong>Buyer seeking rapid scale:</strong> Authority's growth is slow and steady (+7/year),
not explosive. If you want to grow fast, the franchisor's pace may feel conservative.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You can sustain 6–12 months of personal living expenses without relying on franchise income
(seasonal ramp risk is real).</li>
<li>You have validated the latent 3% national marketing fee risk and are comfortable with
the possibility of a $6K–$15K/year cost increase at any time.</li>
<li>You have talked to at least 3 current single-territory franchisees about actual
per-territory revenue — the FDD does not give you this number directly.</li>
</ul>
""",

"item19_triangulation": """
<h3>Per-territory triangulation</h3>
<p>The FDD reports average revenue per <strong>franchisee</strong> ($464,600), not per
territory. The qualifying population is 128 franchisees operating 506 territories —
an average of 3.95 territories per franchisee. This ratio is critical.</p>

<p><strong>Implied per-territory revenue:</strong> $464,600 ÷ 3.95 = ~$117,600. This is
a rough average, not a disclosed figure — the FDD does not break revenue down by territory.
But it aligns with the years-active data: franchisees with 2 full seasons show a median
of $97,460 and an average of $149,470. The implied per-territory figure ($118K) falls
squarely between these.</p>

<p>The revenue-by-territories-owned table (p. 54) adds another signal: franchisees in the
$100K–$250K revenue bracket own a median of 4 territories. That implies
$25K–$63K revenue per territory at the lower end. Franchisees earning $500K+ own a median
of 5 territories, implying $100K+ per territory — but these are the most established
operators in the system.</p>

<div class="implication">
<strong>What this means [inference, not disclosed]:</strong> Based on these calculations,
a single-territory revenue range of $60K–$120K in early years, growing toward $120K–$190K
with 4+ seasons, appears plausible — but this is derived math, not a figure the FDD states.
The headline $465K average is not achievable with one territory. Whether single-territory
economics support a full-time owner draw after operating costs remains an open question
that depends on your market, your cost structure, and your revenue ramp. For many operators,
the path to meaningful income may require expanding to multiple territories — but the FDD
does not disclose the economics or timeline for that expansion.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise designed to help
you stress-test buyer-side economics. The FDD does not disclose franchisee profitability.</p>

<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;">
<strong>Key limitations:</strong> Revenue estimates are inferred from per-franchisee
averages and years-active data — the FDD does not disclose per-territory revenue directly.
The COGS ratio (23%) is derived from a single company-owned location that has operated for
15+ years and is not representative of a new operation's cost structure. The "Remaining"
column is <strong>not</strong> owner income — it must still cover vehicle costs, insurance,
storage, office/admin, seasonal cash gaps, personal taxes, and your living expenses.
Revenue is seasonal (near-zero in winter months in most markets), which these annualized
figures do not reflect.</p>
""",

"economics_assumptions": "Revenue from Item 19 years-active data. COGS at 23% (derived from company-owned P&L, Hickory NC). Franchisor fees from fee burden model. 'Remaining' must still cover: vehicle costs, insurance, storage, office/admin, personal taxes, and your living expenses.",

"economics_detail": """
<h3>What the scenarios tell you</h3>

<p><strong>Conservative (early years):</strong> At median Year 2–3 revenue ($97K — FDD-disclosed
median for franchisees with "at least 2 full seasons," p.&nbsp;53), approximately $57K remains
after franchisor fees and estimated COGS. This is not owner income. Vehicle costs, insurance,
storage, supplies, and other operating expenses still come out of this amount. If those run
$25K–$35K (this report's estimate, not FDD-disclosed), the implied pre-tax owner draw is
$19K–$29K. For a seasonal business with near-zero winter revenue, this level may not support
a full-time owner without outside income or reserves.</p>

<p><strong>Moderate (Year 4+):</strong> At the 4+ season average ($193K — FDD-disclosed average,
p.&nbsp;53), approximately $113K remains after fees and estimated COGS. After operating costs,
an owner-operator draw of $50K–$70K may be plausible — but this figure is inferred, not
disclosed. The $193K is an average, not a floor; the median at this tenure level would be
lower. Variance across markets, territories, and operator skill is not visible from the FDD.</p>

<p><strong>Mature proxy:</strong> The company-owned location at $384K (FDD-disclosed, p.&nbsp;51)
has operated for 15+ years in a single territory. It employs a paid manager ($48K/year).
Even at this revenue level, the location reported negative net income in both years (driven by
amortization). This illustrates an important point: <strong>revenue that looks adequate at the
gross level can still produce modest or negative returns depending on cost structure.</strong>
An owner-operator replacing the manager salary with their own draw changes the math
significantly — but that is a choice about lifestyle, not a proof of profitability.</p>

<div class="callout">
<div class="callout-title">Structural framing</div>
Low franchisor fees do not automatically equal attractive owner economics. At $100K revenue,
Mosquito Authority's fee advantage over competitors (~$15K–$25K/year) is measurable — but the
total revenue base is small, and the remaining margin is thin after operating costs. The fee
advantage compounds as revenue grows, but revenue growth itself is uncertain and market-dependent.
The FDD does not disclose how many single-territory operators reach $200K+ revenue, or how long
it takes. This is the most important unknown in any Mosquito Authority buyer's model.
</div>

<h3>What the buyer still needs to validate</h3>
<ul class="compact">
<li><strong>Actual operating costs [not disclosed]:</strong> Vehicle fuel/maintenance, insurance
premiums in your state, chemical costs in your market, storage rental, seasonal labor. None of
these are estimated in the FDD. Your expense model must be built independently.</li>
<li><strong>Revenue ramp reality [partially disclosed]:</strong> The FDD gives averages and medians
by years-active, but not distributions or failure rates. Talk to 3+ current single-territory
operators about their Year 1–3 revenue trajectory. Ask specifically about revenue in winter months.</li>
<li><strong>Seasonality cash flow [not addressed in FDD]:</strong> Revenue is near-zero in winter
months in most markets. The FDD's 3-month working capital estimate ($3K–$10K) does not account
for this. You need a separate personal cash reserve for 3–5 months of limited activity.</li>
<li><strong>Multi-territory economics [not disclosed]:</strong> If single-territory economics are
modest, the path to meaningful income may require expanding to multiple territories. The FDD does
not disclose incremental costs, timeline, or economics of second-territory expansion. This is a
critical question for franchisee calls.</li>
</ul>
""",

"payback_narrative": """
<p>The table below shows how long it would take to recover your initial investment under
different assumptions about annual owner draw (net income after all costs, fees, and
operating expenses — but before personal taxes). These calculations assume full cash
investment at signing. If you use the available 50% franchise fee deferral (at 8% over
36 months, FDD p.&nbsp;13), your initial cash outlay is lower but you carry debt service
during the ramp period, which is not reflected in this table.</p>

<table>
<thead>
<tr>
<th>Assumed annual owner draw</th>
<th class="num">Low investment ($54K)</th>
<th class="num">Mid investment ($91K)</th>
<th class="num">High investment ($128K)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">$20K (conservative early years)</td>
<td class="num">2.7 years</td>
<td class="num">4.6 years</td>
<td class="num">6.4 years</td>
</tr>
<tr>
<td class="label">$50K (moderate, Year 4+ target)</td>
<td class="num">1.1 years</td>
<td class="num">1.8 years</td>
<td class="num">2.6 years</td>
</tr>
<tr>
<td class="label">$80K (optimistic mature operation)</td>
<td class="num">0.7 years</td>
<td class="num">1.1 years</td>
<td class="num">1.6 years</td>
</tr>
</tbody>
</table>

<div class="callout">
<div class="callout-title">Assumption sensitivity</div>
These payback periods assume a constant annual draw, which is unrealistic — real income
ramps from near-zero in Year 1 to a steady state over several years. A more honest way
to think about it: if you enter at the low end ($54K) and can sustain yourself through
2–3 years of modest income, the investment likely pays back within the first 4 years.
At the high end ($128K), you need either a longer horizon or faster revenue ramp.
The single biggest variable is how quickly you build a recurring customer base.
</div>
""",

"peer_decision_overlay": [
    {"label": "Lowest-cost entry", "brand": "Mosquito Authority",
     "rationale": "$54K–$128K. Next closest is Mosquito Shield at $120K–$157K."},
    {"label": "Lowest ongoing fee burden (established brands)", "brand": "Mosquito Authority",
     "rationale": "17–18% of revenue at all levels. Ranks 2/7 in full cohort (Mosquito Sheriff at 13% is lower but operates only 5 outlets). Among the 5 brands with 100+ outlets, Authority is 1st."},
    {"label": "Lowest attrition at scale", "brand": "Mosquito Authority",
     "rationale": "Zero terminations across 3 years in a 546-outlet system. Hunters and Sheriff show 0.0% attrition but from much smaller bases (135 and 5 outlets). Authority's track record is more statistically meaningful."},
    {"label": "Richest disclosure depth", "brand": "Mosquito Squad",
     "rationale": "Per-territory revenue ($484K average), company-owned P&L with $20.8M revenue and 25.9% margin."},
    {"label": "Lowest-friction entry profile", "brand": "Mosquito Authority",
     "rationale": "Lowest entry floor ($54K), simplest entity structure, fee deferral option. Note: low friction to enter does not predict profitability."},
    {"label": "Highest growth trajectory", "brand": "Mosquito Shield",
     "rationale": "+140 net units in 3 years. But also 65 terminations in 2023 — growth masks churn."},
    {"label": "Highest headline-vs-reality gap risk", "brand": "Mosquito Shield",
     "rationale": "Lowest royalty (8%) but highest local ad floor ($50K). Net burden is among the highest at low revenue."},
],

},

"mosquito-joe": {

"executive_summary": """
<p>Mosquito Joe is the third-largest mosquito franchise brand by outlet count (415 franchised)
and the most data-rich in the cohort — its Item 19 discloses customer retention rates (77%),
per-treatment pricing ($90.54 average), and gross sales broken out by operator tenure. For
a buyer doing due diligence, this is the most transparent brand in the category.</p>

<p>The trade-off is cost. Mosquito Joe has the most complex and expensive fee structure in
the cohort. At $300K gross revenue, annual franchisor fees total $84,752 (28.3% of revenue) —
$32,000 more than Mosquito Authority and roughly $7,000 more than Mosquito Squad. The marketing
structure alone includes five mandatory components (MAP fee, Direct Marketing Program, Local
Performance Marketing, SEO, and potentially LMG), with first-year marketing obligations
exceeding $75,000. Initial investment runs $150K–$192K, highest in the cohort.</p>

<p>The sharpest concern is the 2024 termination spike: 24 closures (up from 5–6 in prior years),
concentrated in Alabama (8 of 24). The system contracted by 1 unit for the first time in the
reporting period. This may be a one-time correction, but it requires explanation.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Joe has the second-highest ongoing fee burden in the cohort at most revenue levels,
and the most complex marketing structure of any brand reviewed. The primary cost driver is
marketing: five mandatory components that total $44,900–$48,900/year before any conditional
programs.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (10%/7% tiered):</strong> 10% on the first $500K of Gross Sales per
territory, dropping to 7% above $500K. The tier benefits larger operators but is irrelevant
at the revenue levels most single-territory operators reach. Minimum License Fees begin
Year 3: $325/week (Jun–Sep only), Year 4: $400/week, Year 5+: $500/week. (pp. 28–29)</li>
<li><strong>MAP Fee (2% of Gross Sales):</strong> Brand fund contribution. Includes
WebPunch license. This is the straightforward component. (p. 28)</li>
<li><strong>Direct Marketing Program ($37,000/year):</strong> The largest single mandatory
fee. Covers direct mail and digital marketing programs. Reduced to $26,000 if prior-year
Gross Sales exceed $450K. Setup fee $1,000 + mailing list fee $0.05/household ($1,250–$1,750
additional). (pp. 30, 35)</li>
<li><strong>Local Performance Marketing ($35,000/year):</strong> Required for the first
12 months only. This is a first-year marketing investment on top of the DMP — a $35K
obligation that does not repeat but significantly increases Year 1 cash requirements.
(p. 35, Item 7)</li>
<li><strong>SEO Program ($325/month):</strong> $3,900/year. Per website. May increase
up to 30% annually. (p. 30)</li>
<li><strong>Technology ($371/month):</strong> $4,452/year. Covers ServSuite, Office365,
FranConnect, Nextiva, Qvinci. +$25/month per additional territory. May increase up
to 30% annually. (p. 30)</li>
<li><strong>Call Center ($200/month + $25/closed sale):</strong> Mandatory for rollover
and after-hours. The per-sale fee is variable and excluded from the model — at 200
closed sales/year, it adds $5,000. (p. 29)</li>
<li><strong>Convention ($1,000/year):</strong> Plus travel. $2,000 penalty for
non-attendance. (p. 31)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, you retain ~$215K after franchisor fees.
At Mosquito Authority, you'd keep ~$247K — a $32,000/year difference. Over a 10-year term,
that's $320,000 in additional fees paid to the franchisor. The question is whether Neighborly's
brand infrastructure, marketing programs, and operational support justify that premium.
</div>

<div class="callout">
<div class="callout-title">Hidden variable — conditional fees</div>
The fee model excludes Local Marketing Groups (LMG, 2% of Gross Sales — may be required)
and the per-closed-sale call center fee ($25/sale). If both are active, add $11,000–$15,000/year
at $300K revenue. The FDD also permits up to 30% annual increases on technology and SEO fees.
The disclosed fee structure is a floor, not a ceiling.
</div>
""",

"item19_narrative": """
<p>Mosquito Joe's Item 19 is the most useful in the cohort for a prospective buyer. It provides
three things no other brand in this category discloses together: customer retention metrics,
per-treatment pricing, and gross sales segmented by operator tenure.</p>

<h3>Part I — Customer metrics (2024)</h3>
<p>Based on 410 of 415 franchised businesses:</p>
<ul class="compact">
<li><strong>Customer retention: 77%</strong> — three-quarters of customers return year over year</li>
<li><strong>Recurring customer rate: 89%</strong> — among returning customers, nearly all are on
recurring service plans</li>
<li><strong>Average gross sales per treatment: $90.54</strong> (median: $88.62)</li>
<li>167 of 410 (41%) achieved or exceeded the average per-treatment price</li>
</ul>

<p>The 77% retention rate is a strong signal for a recurring-revenue business. It means roughly
one in four customers needs to be replaced each year. Combined with the 89% recurring rate,
the business model is demonstrably sticky once you acquire customers.</p>

<h3>Part II — Gross sales by tenure (2024)</h3>
<p>387 businesses open 12+ months, segmented by operating tenure:</p>

<table>
<thead>
<tr>
<th>Tenure</th>
<th class="num">Count</th>
<th class="num">Average</th>
<th class="num">Median</th>
<th class="num">High</th>
<th class="num">Low</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">First 5 Years</td>
<td class="num">91</td>
<td class="num">$214,794</td>
<td class="num">$287,832</td>
<td class="num">$850,881</td>
<td class="num">$15,980</td>
</tr>
<tr>
<td class="label">Six Plus Years</td>
<td class="num">296</td>
<td class="num">$432,954</td>
<td class="num">$339,460</td>
<td class="num">$1,901,756</td>
<td class="num">$13,884</td>
</tr>
</tbody>
</table>

<h3>What to be careful about</h3>
<p><strong>The First 5 Years data is left-skewed:</strong> The median ($287,832) exceeds the
average ($214,794), meaning a cluster of very low performers pulls the average down. If you're
evaluating likely revenue, the median is more representative than the average for this cohort —
but the $16K low shows some operators barely function.</p>

<p><strong>These are per-franchisee figures, not per-territory.</strong> The FDD doesn't disclose
how many territories each reporting business operates. If the average is 1.5–2 territories,
per-territory revenue is significantly lower. The FDD does not clarify this.</p>

<p><strong>Document quality flag:</strong> Column headers in the Part II tables contain copy-paste
errors — customer and job count headers read "Average Annual Gross Sales" and "Median Annual
Gross Sales" instead of the correct labels. The data values appear correct; it's a formatting
error in the filed FDD, not a data integrity issue.</p>

<div class="implication">
<strong>What this means:</strong> A reasonable revenue expectation for a single-territory
operator in the first 5 years is likely in the $200K–$290K range (between the average and
median). Mature operators reach $340K–$430K. The high performers ($850K–$1.9M) almost certainly
operate multiple territories. Plan around the median, not the average or the high — and validate
the per-territory assumption with current franchisees.
</div>
""",

"item19_triangulation": """
<h3>Revenue triangulation</h3>
<p>Cross-checking the gross sales data against treatment pricing provides a useful sanity check.
At the average price of $90.54 per treatment:</p>
<ul class="compact">
<li>$215K (First 5 Years average) implies ~2,375 treatments/year</li>
<li>$288K (First 5 Years median) implies ~3,180 treatments/year</li>
<li>$340K (Six Plus Years median) implies ~3,750 treatments/year</li>
</ul>
<p>The reported average jobs per business for First 5 Years is 2,305 (median 3,328), which aligns
closely with the treatment-count math. This internal consistency gives reasonable confidence
in the revenue figures.</p>

<p>Customer counts add another check: First 5 Years average of 298 customers, with ~8 treatments
per customer per season (2,305 jobs ÷ 298 customers). The math is consistent. This is a business
where you serve ~300 customers, each receiving ~8 treatments at ~$90, for ~$215K–$290K in
gross revenue during the first few years.</p>
""",

"investment_narrative": """
<p>Highest in the cohort: $150,155–$192,075. The major cost drivers are the marketing programs:
the Direct Marketing Program ($37K), Local Performance Marketing ($35K), and setup fees account
for roughly half the total investment before you buy a single piece of equipment.</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($42,500):</strong> Standard for 25,000–35,000 Targeted Households.
Extensive discount programs available (Community Heroes $8,500 off, VetFran $8,500 off,
Licensed Pesticide Applicator $2,500 off). Multi-territory pricing: 2 for $85K, 3 for
$118.5K. Only one discount may be used. (pp. 24–28)</li>
<li><strong>Direct Marketing Program ($37K–$38.75K):</strong> $37K annual fee + $1K setup +
$1,250–$1,750 mailing list. This is a mandatory pre-opening expense, not optional marketing
you choose to do. It's the single most distinctive cost in Mosquito Joe's model. (pp. 30, 35)</li>
<li><strong>Local Performance Marketing ($35,000):</strong> Required first 12 months.
This is on top of the DMP — essentially a $35K marketing investment required before you
know if your territory works. (p. 35)</li>
<li><strong>Vehicle ($3K–$10K):</strong> Vehicle, shelving, and decals. Notably lower
than competitors because MJ's Item 7 assumes you're adding equipment to an existing
vehicle, not buying one. (p. 39)</li>
<li><strong>Additional funds ($16.8K–$28K):</strong> 3-month working capital estimate.
Given the high fixed marketing costs, this is conservative. A buyer should plan for
additional personal reserves beyond this. (p. 39)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Mosquito Joe's investment is front-loaded with mandatory
marketing spend ($72K+ in Year 1 marketing programs alone). The theory is that this aggressive
launch marketing builds a customer base faster. The risk is that you're paying $72K for
marketing programs before you've validated your territory. If the programs underperform,
that money is gone — unlike equipment, marketing spend has no residual value.
</div>
""",

"system_health_narrative": """
<p>The second-largest system in the cohort (415 franchised units), with steady growth through
2023 (+22/year) that reversed in 2024 (−1). The 2024 contraction is driven entirely by a
termination spike: 24 closures, up from 5–6 in prior years. This is the most significant
system health signal in the current filing.</p>
""",

"system_health_detail": """
<h3>The 2024 termination spike</h3>
<p>24 terminations in 2024, compared to 5 in 2023 and 6 in 2022. Nearly 5× the prior-year
rate. Eight of the 24 were in Alabama, which went from 9 outlets to 1 — suggesting a
state-level issue (regulatory, market, or operator-cluster problem) rather than a
system-wide trend.</p>

<p>The remaining 16 terminations were distributed across other states. Without more detail,
this could represent:</p>
<ul class="compact">
<li>A one-time enforcement action against underperforming operators</li>
<li>A change in franchisor tolerance for non-compliance (possibly related to the Bailey
litigation, which involved failure to pay DMP fees)</li>
<li>Genuine market stress in certain territories</li>
</ul>

<div class="implication">
<strong>What this means:</strong> This is the most important item to investigate at Discovery
Day. A one-time correction of non-compliant operators is actually a positive signal (the
franchisor is enforcing quality). But if it reflects market deterioration or fee-burden
stress, it's a warning. The Alabama concentration is notable — ask specifically about
what happened there.
</div>

<h3>Transfer activity</h3>
<p>30 transfers in 2022, 11 in 2023, 8 in 2024. The steep decline (30 → 8) coincides with
the termination spike. Fewer transfers could mean fewer voluntary exits (good), or fewer
willing buyers for resales (bad). Context matters.</p>

<h3>Company-owned footprint</h3>
<p>Two company-owned locations, stable across the reporting period. Minimal franchisor
competition with franchisees.</p>
""",

"risk_narrative": """
<h3>Fee complexity and escalation risk</h3>
<p>Five mandatory marketing components, plus technology and call center fees, each with
separate escalation provisions (up to 30% annual increases on tech and SEO). The
Key Accounts/Management Fee (up to 5% of related Gross Sales) and per-closed-sale
call center fee ($25/sale) are variable and hard to forecast. The FDD's fee structure
is the most complex in the cohort — and complexity itself is a risk, because it makes
total cost of ownership harder to predict.</p>

<h3>Entity structure</h3>
<p>Mosquito Joe SPV LLC is a securitization vehicle within Neighborly's multi-brand
platform (Neighborly Assetco LLC / Dwyer Franchising LLC / KKR). The SPV structure
is standard for PE-backed franchise portfolios but means the entity could be sold,
restructured, or have royalty streams redirected without changing the operating
relationship. All brands in this cohort are PE-backed; the SPV layering is
distinctive to Mosquito Joe in its depth.</p>

<h3>Litigation</h3>
<p>One direct action: <em>SPV LLC v. Bailey et al.</em> — breach of contract for
failure to pay Direct Marketing Program fees. The franchisor prevailed at trial
(Sep 2023) and on appeal (Apr 2025). The franchisee's countersuit alleging
fraudulent inducement was dismissed. Three additional concluded actions involving
Neighborly affiliate entities, not MJ directly.</p>

<div class="implication">
<strong>What this means:</strong> The Bailey case is instructive — it shows the
franchisor will enforce DMP payment obligations through litigation. If you sign,
you are committing to the full marketing program. The fee complexity means your
total cost of ownership may be higher than the base model suggests once conditional
fees and escalation provisions are factored in.
</div>

<h3>Document quality</h3>
<p>Copy-paste errors in Item 19 Part II column headers (customer/job tables labeled
with gross sales headers). Data values appear correct. This is a formatting blemish,
not a data integrity issue — but notable in a Neighborly-backed brand with corporate
resources to produce clean filings.</p>
""",

"peer_narrative": """
<p>Mosquito Joe sits at the premium end of this cohort: highest investment, second-highest
ongoing fees, most complex fee structure. The compensating factor is disclosure quality —
Joe's Item 19 is the most useful in the category, giving buyers actual retention rates,
per-treatment pricing, and tenure-segmented revenue data that no competitor matches.</p>

<p><strong>Direct contrast: Mosquito Authority.</strong> Opposite ends of the cost spectrum.
Authority costs $32K/year less in ongoing fees at $300K revenue, enters for $54K–$128K
(vs Joe's $150K–$192K), and has zero terminations. Joe offers more data transparency and
the Neighborly brand infrastructure. The question is whether the Neighborly ecosystem
justifies a $320K premium over a 10-year term.</p>

<p><strong>Closest comparison: Mosquito Squad.</strong> Similar system size, similar PE
backing (Authority Brands). Squad's fees are slightly lower ($78K vs $85K at $300K),
but Squad's Item 19 is richer in some dimensions (per-territory revenue, company-owned
P&L). Squad's graduated royalty (10/9/8%) rewards scale better than Joe's 10/7% tier.</p>

<p><strong>The Neighborly factor:</strong> Joe is the only brand in this cohort backed by
a multi-brand franchise platform (25+ service brands). This means shared call centers,
cross-selling potential, and operational infrastructure that standalone brands can't match.
Whether this translates to better unit economics for an individual franchisee is the
question the buyer must answer — the FDD provides the data, the buyer provides the judgment.</p>
""",

"discovery_questions": [
    {
        "question": "24 franchisees were terminated in 2024 — nearly 5× the prior year. What happened?",
        "context": "Item 20, 2024 data. 8 of 24 terminations in Alabama (9 outlets to 1).",
        "why_it_matters": "This is the single biggest system health anomaly in the filing. Whether it's a one-time correction or a systemic issue changes the risk profile of buying in.",
        "strong_answer": "'The Alabama cluster was [specific issue: regulatory, non-compliance, operator group]. The remaining 16 were enforcement of fee obligations we'd been patient on. We don't expect this level to repeat.' Specific causes, willingness to detail.",
        "weak_answer": "'We're focused on quality over quantity. Sometimes you need to clean house.' Vague, positions mass termination as routine housekeeping.",
        "follow_up": "Ask for the termination causes by state. Ask whether any of the terminated franchisees dispute the franchisor's characterization."
    },
    {
        "question": "The Direct Marketing Program costs $37,000/year. What is the measured ROI for a typical territory?",
        "context": "Item 6/Item 7. DMP is the single largest mandatory fee beyond royalty.",
        "why_it_matters": "You're committing to $37K/year in a program you can't opt out of. If the ROI is strong, it's an investment. If it's unclear, it's a $37K tax.",
        "strong_answer": "'Average DMP-sourced leads convert at [X]% and generate $[Y] in first-year revenue per territory. Here's the attribution data.' Specific, measurable, willing to share tracking.",
        "weak_answer": "'Our franchisees tell us it works. Marketing is a long-term investment.' No data, no attribution, anecdotal evidence only.",
        "follow_up": "Ask to see actual DMP campaign reports from a territory similar to yours. Ask what happens if you believe the program is underperforming — can you redirect spend?"
    },
    {
        "question": "The fee model excludes LMG (2% of Gross Sales) and the per-sale call center fee ($25/sale). Under what circumstances are these activated, and what is the typical total cost?",
        "context": "Item 6. LMG 'may be required.' Call center fee is per closed sale on rollover/after-hours calls.",
        "why_it_matters": "These conditional fees could add $11K–$15K/year at $300K revenue. If they're routinely active, your actual fee burden is significantly higher than the base model.",
        "strong_answer": "'LMG is active in [X]% of territories. Average annual LMG cost is $[Y]. Call center averages [Z] closed sales per territory per year.' Transparent about actual frequency and cost.",
        "weak_answer": "'LMG depends on your local market. The call center fee is only for leads we generate for you.' Deflects from total cost impact.",
        "follow_up": "Ask for the average total franchisor fee payment (all components) from a territory doing $300K in Gross Sales. Compare to the base model."
    },
    {
        "question": "The Bailey litigation was over DMP fee non-payment. How common is DMP non-compliance, and are the 2024 terminations related?",
        "context": "Item 3, Bailey v. SPV LLC. Franchisor prevailed on breach of contract for DMP fees.",
        "why_it_matters": "If the franchisor is litigating and terminating over DMP fee compliance, it signals either that the DMP creates genuine financial stress for operators or that the franchisor is tightening enforcement. Either way, it affects your risk.",
        "strong_answer": "'Bailey was an isolated case. DMP compliance is [X]%. The 2024 terminations were for [separate specific reasons].' Distinguishes the cases clearly.",
        "weak_answer": "'We enforce our agreements consistently. Franchisees who don't follow the program put the whole system at risk.' Policy language, avoids the specific question.",
        "follow_up": "Ask how many franchisees are currently in default or on payment plans for DMP fees."
    },
    {
        "question": "The Item 19 shows First 5 Years average ($215K) well below the median ($288K). What's happening with the low performers?",
        "context": "Item 19 Part II. Left-skewed distribution with a $16K low.",
        "why_it_matters": "Left skew means a cluster of operators at very low revenue is pulling the average down. Understanding why some operators are at $16K–$50K tells you what failure looks like in this system.",
        "strong_answer": "'Low performers are typically [part-time operators / seasonal markets / territories that hadn't ramped yet]. Here's what we do to support underperformers.' Honest about causes, active about support.",
        "weak_answer": "'Every business has a range of outcomes. We provide the tools, franchisees provide the effort.' Implies low performance is the franchisee's fault without evidence.",
        "follow_up": "Ask how many of the 91 First 5 Years businesses are below $100K, and whether any are on performance improvement plans."
    },
    {
        "question": "Transfer activity dropped from 30 (2022) to 8 (2024). Is the resale market contracting?",
        "context": "Item 20, Table 2. 73% decline in transfers over 2 years.",
        "why_it_matters": "If fewer territories are changing hands, it could mean franchisees are happy (positive) or that buyers aren't willing to pay asking prices (negative). In a system that just had 24 terminations, the latter interpretation needs to be ruled out.",
        "strong_answer": "'Transfer volume declined because franchisee retention improved — fewer people wanting to sell. Average resale prices have [increased/held steady].' Data on resale economics.",
        "weak_answer": "'Transfers fluctuate year to year.' No data, no explanation for a 73% decline.",
        "follow_up": "Ask for the average resale price as a multiple of annual Gross Sales. Ask if any of the 2024 terminated territories were previously listed for sale."
    },
    {
        "question": "Technology and SEO fees may increase up to 30% annually. What has the actual increase history been?",
        "context": "Item 6, technology fee ($371/month) and SEO ($325/month) escalation clauses.",
        "why_it_matters": "A 30% annual increase on $8,352/year (combined tech + SEO) would reach $14,000+ within 3 years. The permission to escalate is disclosed; the track record matters.",
        "strong_answer": "'Tech fees have increased [X]% over the past 3 years. We added [specific capabilities] with each increase.' Transparent history, value justification.",
        "weak_answer": "'We always try to keep fees reasonable. The 30% is a contractual maximum, not a plan.' No history, no commitment.",
        "follow_up": "Ask for a 3-year fee history for all recurring non-royalty charges."
    },
    {
        "question": "What does the Neighborly multi-brand platform actually deliver to a Mosquito Joe franchisee that a standalone brand can't?",
        "context": "Parent: Neighborly Assetco LLC / KKR. 25+ service brands.",
        "why_it_matters": "Mosquito Joe's fees are the highest in the cohort. The implicit justification is Neighborly's infrastructure. The buyer needs to know what that infrastructure concretely provides vs. what standalone competitors deliver for less.",
        "strong_answer": "'Cross-brand lead sharing generated [X] leads per MJ territory last year. Neighborly's shared call center handles [Y]% of inbound calls. Here's the NPS data for our support services.' Measurable, specific.",
        "weak_answer": "'Being part of the Neighborly family gives you access to our proven systems and brand recognition.' Marketing language without measurable claims.",
        "follow_up": "Ask for actual cross-brand lead volume data for a territory similar to yours. Ask what Neighborly services would disappear if MJ were spun off."
    },
    {
        "question": "The Key Accounts/Management Fee can reach 5% of related Gross Sales. How much revenue typically comes through this channel?",
        "context": "Item 6. Key Account work, Business Development leads, call center dispatched work.",
        "why_it_matters": "If 20% of your revenue comes through Key Accounts, this adds 1% to your effective total fee burden. At higher percentages, it materially changes the economics.",
        "strong_answer": "'Key Account revenue averages [X]% of total Gross Sales per territory. The management fee on that is [Y].' Transparent about volume and cost.",
        "weak_answer": "'Key Accounts are a great revenue source. The fee covers our business development costs.' Avoids quantifying the cost impact.",
        "follow_up": "Ask whether Key Account leads are opt-in or automatic. Ask if you can decline Key Account work."
    },
    {
        "question": "What does a realistic first-year cash flow timeline look like for a single-territory operator starting in spring?",
        "context": "Seasonal business. Item 7 shows $16.8K–$28K in 3-month working capital. First-year marketing obligations exceed $72K.",
        "why_it_matters": "With $150K+ invested and $72K+ in Year 1 marketing obligations, the cash draw in Year 1 is severe. The buyer needs to understand when revenue starts offsetting costs and how long personal reserves need to last.",
        "strong_answer": "'Typical spring start: first revenue in Month 2, breakeven on monthly cash flow by Month 5–6. Here's a sample first-year P&L from a recent launch.' Specific timeline with supporting data.",
        "weak_answer": "'Results vary by market. We recommend having 6 months of personal expenses saved.' Generic advice without franchise-specific cash flow data.",
        "follow_up": "Ask when the DMP and LPM payments are due relative to revenue ramp. Ask how many 2024 launches hit monthly breakeven within the first season."
    },
],

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Weak", "color": "weak",
     "summary": "Highest in cohort. $150K–$192K driven by $72K+ in mandatory first-year marketing programs."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "#4 at most revenue levels. 28% at $300K. Most complex fee structure with 5+ mandatory marketing components."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Steady growth reversed in 2024 (−1 unit). 24 terminations (5× prior years). Alabama cluster (8 of 24) is concentrated."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Best Item 19 in cohort. Retention rates, per-treatment pricing, and tenure-segmented gross sales. Actionable data."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Copy-paste errors in Item 19 headers. Data appears correct but formatting sloppiness in a Neighborly-backed filing is notable."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Termination spike needs explanation. Fee escalation provisions (30%/year on tech/SEO) and conditional fees create cost uncertainty."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Requires $150K+ capital and tolerance for complex fee structure. Best for buyers who value brand infrastructure over cost efficiency."},
    {"dimension": "Overall", "rating": "Cautious", "color": "mixed",
     "summary": "Most data-rich brand but highest cost. The premium buys transparency and Neighborly infrastructure — not lower risk or better unit economics."},
],

"scorecard_posture": """Mosquito Joe is the most transparent brand in this cohort and the most
expensive. The disclosure quality is genuinely useful — a buyer can build a more informed
financial model from Joe's Item 19 than from any competitor's. But the fee complexity, the
2024 termination spike, and the highest investment in the category mean this is not a low-risk
entry. It suits a buyer with capital, comfort with complex fee structures, and belief in the
Neighborly platform's value. It does not suit a budget-sensitive first-time buyer.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who values data transparency:</strong> Joe's Item 19 gives you the most
complete picture of system economics in the cohort. If you want to build a detailed financial
model before committing, this brand gives you the most inputs to work with.</li>
<li><strong>Buyer who values brand infrastructure:</strong> Neighborly's platform provides
shared call centers, cross-brand marketing, operational systems, and a recognized home-services
brand. If you believe platform effects matter, Joe delivers them.</li>
<li><strong>Well-capitalized buyer:</strong> $150K–$192K entry cost plus $72K+ in Year 1
marketing means you need $200K+ in accessible capital. This is not a shoestring operation.</li>
<li><strong>Buyer comfortable with complex fee structures:</strong> If you can model and
manage 5+ fee components, conditional charges, and escalation provisions, the complexity
is navigable. If you want a simple cost structure, look elsewhere.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive first-time buyer:</strong> At $150K+ to enter and $85K/year in
franchisor fees at $300K revenue, this is the most expensive option in the category. Mosquito
Authority enters for $54K and costs $32K/year less to operate.</li>
<li><strong>Buyer who prioritizes cost efficiency:</strong> If your strategy is to minimize
franchisor fees and maximize retained earnings, Joe is the wrong brand. The fee structure
is designed to fund franchisor programs, not minimize franchisee cost.</li>
<li><strong>Buyer in a smaller or unproven market:</strong> The mandatory $72K+ in first-year
marketing obligations don't scale down for smaller territories. If your market's potential
is modest, the fixed marketing costs consume a disproportionate share of revenue.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have at least $200K in accessible capital (investment + personal reserves for 6+ months).</li>
<li>You've gotten a satisfactory explanation for the 2024 termination spike — particularly the
Alabama cluster.</li>
<li>You've validated the DMP's ROI with 3+ current franchisees who can show actual lead attribution data.</li>
<li>You understand and accept every conditional fee (LMG, per-sale call center, Key Accounts)
and have modeled worst-case total fee burden.</li>
</ul>
""",

"economics_scenarios_config": [
    ("Conservative (First 5 Yrs avg)", 215000),
    ("Moderate (First 5 Yrs median)", 288000),
    ("Mature (Six Plus Yrs median)", 340000),
],

"economics_cogs_ratio": 0.23,

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Mosquito
Joe's disclosed Item 19 revenue data combined with a 23% cost-of-goods estimate borrowed from
Mosquito Authority's company-owned P&L (the only company-owned cost data available in this cohort).
Mosquito Joe does not disclose franchisee cost data. Your actual results depend on your market,
operating costs, and execution.</p>
""",

"economics_assumptions": "Revenue from Item 19 tenure-segmented data. COGS at 23% (borrowed from Mosquito Authority company-owned P&L — no MJ cost data available). Franchisor fees from fee burden model. 'Remaining' must cover: vehicle costs, insurance, chemical supplies, seasonal labor, marketing beyond mandatory programs, and your living expenses.",

"economics_detail": """
<h3>What the scenarios tell you</h3>

<p><strong>Conservative (First 5 Yrs average, $215K):</strong> After fees ($75K) and COGS ($49K),
$91K remains. This must cover all operating costs and your living expenses. If non-fee operating
costs run $30K–$40K, your effective owner draw is $50K–$60K before taxes. This is tighter than
it looks — the $72K+ in first-year marketing obligations are already spent.</p>

<p><strong>Moderate (First 5 Yrs median, $288K):</strong> The median revenue produces $133K
remaining after fees and COGS. After typical operating costs, an owner draw of $80K–$95K is
plausible. This is the scenario where Joe's economics start working. But remember: half of
first-5-year operators are below this number.</p>

<p><strong>Mature (Six Plus Yrs median, $340K):</strong> At mature revenue levels, $163K
remains after fees and COGS. A well-run single-territory operation could generate $100K+
owner draw at this level. This is where the Neighborly premium becomes defensible — if the
brand infrastructure helped you get to $340K.</p>

<div class="callout">
<div class="callout-title">The cost premium in context</div>
At $300K revenue, Mosquito Joe's franchisor fees are $85K — about $32K more than Mosquito
Authority ($53K). That means the buyer is paying an additional $32K/year for the Neighborly
platform. Is the brand infrastructure, marketing program, and operational support worth
$32K/year to you? If the DMP and Neighborly's systems help you reach $340K+ faster than
you'd reach $300K with a low-cost brand, the premium pays for itself. If not, you've funded
corporate programs at the expense of your own economics.
</div>

<h3>What the buyer still needs to validate</h3>
<ul class="compact">
<li><strong>Actual total fees:</strong> Model worst-case by including LMG (2% of GS), per-sale
call center fees ($25 × estimated sales), Key Account fees (up to 5% of related GS), and
30% annual escalation on tech/SEO.</li>
<li><strong>Per-territory revenue:</strong> Confirm whether the Item 19 figures are per
franchisee or per territory. If multi-territory operators are included in the averages,
single-territory revenue is lower.</li>
<li><strong>DMP attribution:</strong> Get actual lead data from 3+ franchisees. The $37K/year
program should have measurable ROI — if the franchisor can't demonstrate it, that's a signal.</li>
<li><strong>First-year cash flow:</strong> With $72K+ in mandatory Year 1 marketing, map the
month-by-month cash draw against expected revenue ramp. The 3-month working capital estimate
in Item 7 ($17K–$28K) is almost certainly insufficient.</li>
</ul>
""",

"payback_narrative": """
<p>The table below shows how long it would take to recover your initial investment under
different assumptions about annual owner draw (net income after all costs, fees, and
operating expenses — but before personal taxes).</p>

<table>
<thead>
<tr>
<th>Assumed annual owner draw</th>
<th class="num">Low investment ($150K)</th>
<th class="num">Mid investment ($171K)</th>
<th class="num">High investment ($192K)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">$40K (conservative early years)</td>
<td class="num">3.8 years</td>
<td class="num">4.3 years</td>
<td class="num">4.8 years</td>
</tr>
<tr>
<td class="label">$70K (moderate, Year 4+ target)</td>
<td class="num">2.1 years</td>
<td class="num">2.4 years</td>
<td class="num">2.7 years</td>
</tr>
<tr>
<td class="label">$100K (mature operation)</td>
<td class="num">1.5 years</td>
<td class="num">1.7 years</td>
<td class="num">1.9 years</td>
</tr>
</tbody>
</table>

<div class="callout">
<div class="callout-title">Assumption sensitivity</div>
These payback periods assume a constant annual draw, which is unrealistic. Year 1 income will
be low while you build a customer base, and $72K+ in mandatory marketing is front-loaded.
A more honest frame: if you reach $288K revenue (First 5 Years median) by Year 3 and sustain
$80K–$95K owner draw from Year 3 onward, payback occurs around Year 5–6 at mid investment.
The higher investment threshold compared to competitors means you need either higher revenue
or a longer time horizon to recover your capital.
</div>
""",

"peer_decision_overlay": [
    {"label": "Lowest-cost entry", "brand": "Mosquito Authority",
     "rationale": "$54K–$128K. MJ is $150K–$192K — $96K more at the low end."},
    {"label": "Lowest ongoing fee burden (established brands)", "brand": "Mosquito Authority",
     "rationale": "17–18% of revenue (2/7 in full cohort; 1st among brands with 100+ outlets). MJ is 28% at $300K — $32K/year more in franchisor fees."},
    {"label": "Richest revenue disclosure", "brand": "Mosquito Joe",
     "rationale": "Retention rates, per-treatment pricing, tenure-segmented sales. Among the most actionable Item 19 disclosures in the cohort."},
    {"label": "Lowest attrition at scale", "brand": "Mosquito Authority",
     "rationale": "Zero terminations in a 546-outlet system. MJ had 24 terminations in 2024 — a 5× spike requiring explanation."},
    {"label": "Richest operational data for modeling", "brand": "Mosquito Joe",
     "rationale": "Most operational data points in a single FDD. If you want to model before you commit, MJ gives you the most inputs."},
    {"label": "Highest 'costs more than it looks' risk", "brand": "Mosquito Joe",
     "rationale": "Conditional fees (LMG, per-sale, Key Accounts) and 30%/year escalation provisions mean disclosed fees are a floor."},
    {"label": "Lowest-friction entry profile", "brand": "Mosquito Authority",
     "rationale": "Lowest entry floor ($54K), fee deferral option. MJ requires $200K+ capital and comfort with fee complexity. Note: low friction to enter does not predict profitability."},
],

},

"mosquito-squad": {

"executive_summary": """
<p>Mosquito Squad has the most detailed disclosure in the mosquito pest control cohort.
Its Item 19 provides per-territory revenue broken out by quartile, close and renewal
rates, per-appointment and per-customer revenue, five years of systemwide growth data, and a
14-territory company-owned P&amp;L showing $20.8M revenue with a 25.9% net margin. No other
brand in this category gives a prospective buyer this much to work with.</p>

<p>The trade-off is that Squad is a mid-cost, mid-complexity brand that is still recovering from a
rough 2022 (−10 net franchised units). The system has grown since (+4 in 2023, +9 in 2024), and
2024 saw zero terminations. But at 226 franchised outlets, it is smaller than Mosquito Authority
(546) and Mosquito Joe (415), and the investment range ($162K–$220K) is inflated by a 12-month
working capital estimate that most competitors quote at 3 months.</p>

<p>The graduated royalty (10%/9%/8%) rewards scale, and the local marketing cap ($50K/year) puts
a ceiling on a cost that is uncapped at most competitors. The Massachusetts Attorney General
marketing-claims action (2024) is a regulatory signal worth understanding — it affects how
franchisees can advertise, not the franchise relationship itself.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Squad sits in the middle of the cohort on fee burden — second-lowest at $200K–$300K
revenue, but third at higher levels where the graduated royalty tiers provide less relief than
competitors' stepped structures. The marketing cap ($50K/year) is a distinctive feature: it's
a cost ceiling that no other brand offers.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (10%/9%/8% graduated):</strong> 10% on first $250K, 9% on $250K–$500K, 8%
above $500K per territory per calendar year. Minimum royalty begins Month 13: $650/mo (Y2),
escalating to $3,000/mo (Y9+). The graduation rewards scale — at $500K revenue, effective
rate is 9.5%. (pp. 19–20, 29)</li>
<li><strong>Brand Fund ($150–$450/month, escalating):</strong> Flat fee, not percentage-based.
$350/mo at Year 5 ($4,200/year). Unusual structure — doesn't scale with revenue, which
benefits high-revenue operators and costs low-revenue operators proportionally more. (p. 20)</li>
<li><strong>Local Marketing ($35K floor / $50K cap):</strong> Greater of $35,000 or 10% of
prior-year Gross Revenue, up to $50,000. The cap is a rare feature — at $500K+ revenue, you
hit the ceiling while competitors' obligations keep climbing. (pp. 20–21)</li>
<li><strong>Website ($350/month):</strong> $4,200/year. Can be increased 10% on 30 days'
notice. (p. 22)</li>
<li><strong>Technology ($60/month):</strong> $720/year — covers branded email and required
portals. Separately: ServiceMinder operational software at $280/month + $25/user, paid to
vendor. Combined tech cost is ~$4,380/year. (p. 22)</li>
<li><strong>Conference ($600/year):</strong> Non-attendance penalties: $500 first miss, $2,000
each consecutive miss. (p. 25)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Squad's $77,880 in total fees (26%) puts it
between Authority ($52,800 / 17.6%) and Joe ($84,752 / 28.3%). The graduated royalty and
marketing cap mean Squad's cost curve flattens at higher revenue — at $500K, Squad's 22.2%
is competitive. The fee structure rewards growth more than any other brand in the cohort.
</div>

<div class="callout">
<div class="callout-title">Marketing cap advantage</div>
Squad caps local marketing at $50,000/year. At $500K revenue, Mosquito Joe's marketing
obligations are uncapped, and Mosquito Shield's local ad floor is $50K with no ceiling on
other marketing components. The cap creates a predictable cost ceiling that matters
increasingly as revenue grows.
</div>
""",

"item19_narrative": """
<p>Mosquito Squad's Item 19 is the most comprehensive in the cohort — seven tables covering
every dimension a buyer needs: per-territory revenue by quartile, operational conversion
metrics, systemwide trends, and a full company-owned P&amp;L. This section is long because
there is genuinely a lot to interpret.</p>

<h3>Per-territory revenue by quartile (Table 1)</h3>
<p>Based on 207 franchised territories operating for the full 2024 fiscal year:</p>

<table>
<thead>
<tr>
<th>Quartile</th>
<th class="num">Territories</th>
<th class="num">Average</th>
<th class="num">Median</th>
<th class="num">High</th>
<th class="num">Low</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">Q1 (top 25%)</td>
<td class="num">52</td>
<td class="num">$1,123,247</td>
<td class="num">$955,075</td>
<td class="num">$2,787,688</td>
<td class="num">$656,078</td>
</tr>
<tr>
<td class="label">Q2</td>
<td class="num">52</td>
<td class="num">$467,598</td>
<td class="num">$443,197</td>
<td class="num">$653,830</td>
<td class="num">$317,881</td>
</tr>
<tr>
<td class="label">Q3</td>
<td class="num">51</td>
<td class="num">$233,445</td>
<td class="num">$226,114</td>
<td class="num">$316,113</td>
<td class="num">$165,032</td>
</tr>
<tr>
<td class="label">Q4 (bottom 25%)</td>
<td class="num">52</td>
<td class="num">$108,907</td>
<td class="num">$111,552</td>
<td class="num">$164,719</td>
<td class="num">$11,242</td>
</tr>
<tr style="border-top:2px solid #333">
<td class="label">All territories</td>
<td class="num">207</td>
<td class="num">$484,506</td>
<td class="num">$317,881</td>
<td class="num">$2,787,688</td>
<td class="num">$11,242</td>
</tr>
</tbody>
</table>

<p>This is the only brand in the cohort that discloses <strong>per-territory</strong> revenue.
The average ($484,506) and median ($317,881) tell different stories — the gap between them
($167K) signals significant right skew from top performers. The median is the more representative
number for a prospective single-territory buyer.</p>

<h3>Operational metrics</h3>
<p>From 75 franchisees (183 territories) who reported via CRM and submitted year-end P&amp;L:</p>
<ul class="compact">
<li><strong>Close rate: 48% average</strong> (Q1 operators: 65%, Q4: 30%)</li>
<li><strong>Renewal rate: 70% average</strong> (median 69%, range 33%–90%)</li>
<li><strong>Revenue per appointment: $98 average</strong> (median $95)</li>
<li><strong>Revenue per customer: $705 average</strong> (median $715)</li>
</ul>

<p>The 70% renewal rate is below Mosquito Joe's 77%. Combined with the 48% close rate, the
business model requires replacing roughly 30% of customers each year — and converting fewer
than half of leads. A buyer should expect significant ongoing marketing spend to maintain
revenue, which aligns with the $35K+ local marketing obligation.</p>

<h3>Company-owned P&amp;L (14 territories, MA/NH/RI)</h3>
<p>The best unit economics data in the entire cohort:</p>
<ul class="compact">
<li>Revenue: $20,843,565 (~$1.49M per territory)</li>
<li>COGS: 47.7% — technician labor (23.4%), program costs (12.7%), marketing (7.3%), products (4.3%)</li>
<li>Gross profit: 52.3%</li>
<li>Operating expenses: 26.4% — admin personnel (16.2%), facilities (4.1%), professional fees (3.0%)</li>
<li><strong>Net income: 25.9% ($5.4M)</strong></li>
</ul>

<div class="callout">
<div class="callout-title">Important context for the P&amp;L</div>
This is a 14-territory corporate operation, not a single-territory franchisee. The per-territory
economics ($1.49M revenue, ~$386K net) are dramatically better than a typical single-territory
franchisee will achieve — Q1 operators average $1.1M, most are below $500K. The P&amp;L is most
useful for cost ratios (what percentage goes to labor, chemicals, overhead), not absolute dollars.
Company-owned territories do not pay royalty or brand fund fees, so a franchisee's cost structure
will differ.
</div>

<h3>What to be careful about</h3>
<p><strong>Excluded territories:</strong> 29 of 236 territories were excluded from Table 1
(9 opened during year, 10 ceased, 10 added by existing franchisees). The 10 ceased territories
are notable — these are units that stopped operating during 2024 and are not reflected in the
revenue data.</p>

<p><strong>Table numbering error:</strong> The company-owned P&amp;L is labeled "Table 9" in the
FDD but is the 7th table in Item 19. Minor formatting issue.</p>

<div class="implication">
<strong>What this means:</strong> A prospective single-territory buyer should plan around Q3
economics as a reasonable base case: $226K median revenue per territory. Q2 ($443K) is
achievable with strong execution and a good market. The company-owned P&amp;L provides cost
ratios to build a realistic expense model — specifically the 23.4% technician labor ratio,
which is the largest single cost line and directly applicable to a franchisee operation.
</div>
""",

"item19_triangulation": """
<h3>Revenue triangulation</h3>
<p>Cross-checking revenue against operational metrics:</p>
<ul class="compact">
<li>At $705/customer (average) and Q3 median revenue of $226K: ~320 customers per territory</li>
<li>At $98/appointment and Q3 median revenue: ~2,300 appointments per territory per year</li>
<li>With 70% renewal rate: ~225 returning customers + ~95 new customers needed per year</li>
<li>At 48% close rate: ~200 leads needed per year to acquire 95 new customers</li>
</ul>
<p>This math is internally consistent and gives a concrete picture of the business at Q3 level:
serve ~320 customers, deliver ~2,300 treatments, close ~200 leads, retain ~225 renewals.
The marketing machine needs to generate roughly 4 qualified leads per week during the
season to sustain this level.</p>

<p><strong>Same-store growth:</strong> 195 territories that operated in both 2023 and 2024 showed
5% aggregate growth ($93.7M → $98.2M). This is a positive signal for existing operators — the
business grows modestly with tenure, not just with new territory openings.</p>
""",

"investment_narrative": """
<p>The headline range ($162K–$220K) is the highest in the cohort, but it is misleading. Squad
includes 12 months of working capital in Item 7 ($84K–$117K), while most competitors include
only 3 months. Adjusting for equivalent working capital assumptions, the comparable investment
is roughly $100K–$130K — closer to the middle of the cohort.</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($50,000 standard):</strong> $35K for Micro territories (&lt;350K pop).
Extensive discount programs (Veterans 30%, Existing Franchisee 30%, Conversion 25–75%). Range
collected in 2024: $24K–$53.5K, suggesting significant discounting in practice. (pp. 15, 18)</li>
<li><strong>Pre-opening outfitting fees ($15.5K–$21K):</strong> Business Outfitting $9,500 +
Operations Outfitting $2,000 + Truck Outfitting $4K–$9.5K. These are paid to the franchisor
and cover initial setup, equipment, and vehicle branding. (p. 30)</li>
<li><strong>Additional Funds — 12 months ($84K–$117K):</strong> This is the line that inflates
the range. It includes local marketing obligations ($35K+), software fees, insurance, and
operating expenses for a full year. Most competitors show 3 months here. The 12-month estimate
is arguably more honest — it forces the buyer to plan for a full year of negative cash flow.
(p. 31)</li>
<li><strong>Vehicle ($0–$11K):</strong> Assumes an existing vehicle; the range covers
modifications and signage. (p. 30)</li>
<li><strong>Insurance ($7K–$7.5K):</strong> Higher than most competitors, reflecting the
outdoor service nature of the business. (p. 30)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Strip out the 12-month working capital and Squad's core
investment (franchise fee + outfitting + vehicle + equipment) is roughly $70K–$95K. The
franchisor is being transparent about how much cash you actually need for the first year — other
brands quote lower investment ranges by hiding 9 months of operating costs in "Additional Funds"
footnotes. The honest Item 7 is a feature, not a bug.
</div>
""",

"system_health_narrative": """
<p>Squad's system health tells a recovery story. The franchise contracted by 10 units in 2022
(12 terminations, 3 non-renewals, only 5 openings) — the worst single year in the cohort.
Since then: +4 in 2023, +9 in 2024, with zero terminations in 2024. The three-year net is
+3 franchised units, essentially flat — but the trajectory is positive.</p>
""",

"system_health_detail": """
<h3>The 2022 contraction</h3>
<p>2022 was a rough year: 12 terminations, 3 non-renewals, 5 openings, net −10 franchised
units. This followed a major 2021 event where the franchisor reacquired 14 territories
(reflected in the 12,646% spike in company-owned revenue that year). The picture is one
of a system that went through a significant restructuring — culling underperformers and
absorbing territories — before stabilizing.</p>

<div class="implication">
<strong>What this means:</strong> The 2022 contraction is not a current-year risk signal.
It's a historical restructuring. The relevant question is whether the post-2022 trajectory
(+4, +9, zero terminations in 2024) represents genuine recovery or just a pause before
the next correction. The 2024 data is encouraging — 19 openings, zero terminations, 13
signed agreements not yet open.
</div>

<h3>Transfer and exit activity</h3>
<p>18 transfers in 2022, 14 in 2023, 12 in 2024 — declining but still active. Turnover rate
improved from 13.9% (2022) to 9.5% (2024). In 2024, the exits were 3 non-renewals and 7
ceased operations, with zero terminations — suggesting voluntary departures, not franchisor
enforcement.</p>

<h3>Company-owned footprint</h3>
<p>15 company-owned territories (MA, NH, RI), stable across the reporting period. This is the
largest company-owned operation in the cohort and the basis for the P&amp;L data in Item 19. The
franchisor is a significant operator in its own system, which creates both alignment (they know
the business firsthand) and potential tension (they compete with franchisees in the Northeast).</p>
""",

"risk_narrative": """
<h3>Massachusetts Attorney General action (2024)</h3>
<p>Assurance of Discontinuance with the MA AG (September 2024) over marketing claims: alleging
that advertisements claiming barrier protection provides health benefits, is "natural" or
"all-natural," eliminates a high percentage of dangers, may be used "worry-free," and uses
"EPA-approved" pesticides violated the Massachusetts Consumer Protection Act. Not an admission
of liability. Squad agreed to cease such advertisements, alert franchisees, and inform new
MA franchisees. Collective cost: $13,000 for investigation.</p>

<div class="implication">
<strong>What this means:</strong> This is a marketing-language issue, not a franchise-relationship
issue. But it affects how franchisees can advertise — certain claims that may have been part of
standard marketing materials are now prohibited in Massachusetts and potentially challengeable
in other states. Ask the franchisor what marketing materials were revised and whether similar
actions are pending elsewhere.
</div>

<h3>Liquidated damages</h3>
<p>On termination: the greater of 2 years' average Royalty Fees or $50,000. This is the most
aggressive exit penalty in the cohort. At $300K revenue with ~$30K annual royalty, the penalty
would be $60K. This creates a significant financial barrier to exit — you cannot walk away cheaply.</p>

<h3>Entity structure</h3>
<p>Mosquito Squad Franchising SPE LLC, within Authority Brands / Apax Partners. SPE
(Special Purpose Entity) structure is standard for PE-backed franchise systems. Authority Brands
operates multiple home-service brands (Benjamin Franklin Plumbing, Mister Sparky, One Hour
Heating &amp; Air, DRYmedic, etc.). The multi-brand parent provides operational infrastructure
but also means franchise royalty streams can be securitized and redirected.</p>

<h3>Company-owned territory tension</h3>
<p>15 company-owned territories generating $20.8M in revenue is a meaningful footprint. While
this provides excellent P&amp;L disclosure, it also means the franchisor directly competes with
franchisees in the MA/NH/RI market. A buyer in the Northeast should understand whether company-owned
expansion is planned and whether territory protections are sufficient.</p>
""",

"peer_narrative": """
<p>Mosquito Squad occupies a distinctive position: mid-cost fees, the richest disclosure in the
category, and a system that is recovering from a rough 2022. It's not the cheapest (Authority),
not the largest (Joe), and not the fastest-growing (Shield). But it gives a buyer more data
to make a decision than any competitor.</p>

<p><strong>Direct contrast: Mosquito Authority.</strong> Authority is cheaper at every dimension
($25K/year less in fees at $300K, $108K less at the low investment end) and has zero terminations.
But Authority's Item 19 doesn't provide per-territory revenue, and the company-owned P&amp;L is
a single location generating $384K. Squad's 14-territory, $20.8M operation gives a fundamentally
richer picture of unit economics — even if the absolute numbers aren't directly applicable.</p>

<p><strong>Closest comparison: Mosquito Joe.</strong> Similar system size, both PE-backed platforms.
Joe's fees are higher ($85K vs $78K at $300K), Joe's Item 19 provides tenure-segmented data but
not per-territory quartiles. Squad's per-territory quartile data is arguably more actionable for
a prospective buyer than Joe's per-franchisee averages. Joe has better customer retention (77%
vs 70%). The choice between Joe and Squad comes down to: do you want Neighborly's infrastructure
at a premium, or Authority Brands' data transparency at a moderate price?</p>

<p><strong>The data-transparency edge:</strong> Squad is the only brand where you can look at
per-territory revenue distributions, company-owned cost structures, close rates, renewal rates,
and per-customer economics in one filing. For a buyer who wants to build a financial model
before committing, this is the most useful raw material in the category.</p>
""",

"discovery_questions": [
    {
        "question": "The system contracted by 10 units in 2022 and 14 territories were reacquired in 2021. What triggered the restructuring?",
        "context": "Item 20, 2022 data. Item 19 Table 6 shows 12,646% company-owned revenue spike in 2021.",
        "why_it_matters": "A 14-territory reacquisition followed by 12 terminations is a major system event. Whether it was a strategic cleanup or a crisis response changes how you interpret the post-2022 recovery.",
        "strong_answer": "'We identified underperforming territories in [specific regions], reacquired some to stabilize service quality, and terminated franchisees who weren't meeting standards. Here's the timeline and outcome.' Specific, structured, demonstrates control.",
        "weak_answer": "'We went through a transition period. The system is stronger now.' Vague, avoids explaining the scale of the restructuring.",
        "follow_up": "Ask what happened to the 14 reacquired territories — were they resold, converted to company-owned, or closed? How many of the 2022 terminations were in the same regions?"
    },
    {
        "question": "The company-owned P&L shows 25.9% net margin on $20.8M. What would that look like adjusted for franchisee-level fees?",
        "context": "Item 19 Table 7 (labeled Table 9). Company-owned pays no royalty or brand fund.",
        "why_it_matters": "The P&L is the most useful in the cohort, but company-owned territories don't pay franchisor fees. A franchisee at equivalent per-territory revenue ($1.49M) would owe roughly $130K–$145K in additional fees. Understanding the adjusted margin tells you what your economics actually look like.",
        "strong_answer": "'At the average per-territory level, a franchisee would net approximately $[X] after fees. Here's how we walk prospective buyers through the adjustment.' Willing to do the math with you.",
        "weak_answer": "'The P&L shows the business is very profitable. Franchisees do great.' Avoids the fee adjustment, implies company-owned margins are representative.",
        "follow_up": "Ask for the COGS breakdown by line item. Specifically: is the 23.4% technician labor ratio achievable for a single-territory operator, or does it reflect multi-territory staffing efficiencies?"
    },
    {
        "question": "The Massachusetts AG action required you to stop certain marketing claims. Which specific materials were revised, and have similar challenges been raised in other states?",
        "context": "Item 3, Assurance of Discontinuance (Sep 2024). Claims about 'natural,' 'health benefits,' 'EPA-approved.'",
        "why_it_matters": "If key marketing claims are now prohibited, franchisees need to know what language they can and can't use. Similar challenges in other states could further restrict marketing options.",
        "strong_answer": "'We revised [specific materials]. Here are the updated marketing guidelines. No similar actions pending in other states. Here's our compliance review process.' Transparent, proactive.",
        "weak_answer": "'It was a Massachusetts-specific issue. We settled for $13K and moved on.' Dismissive, doesn't address the impact on franchisee marketing.",
        "follow_up": "Ask to see the current approved marketing materials. Ask whether franchisees were consulted before the AOD was agreed to."
    },
    {
        "question": "The liquidated damages clause requires the greater of 2 years' royalty or $50,000 on termination. Has this been enforced, and is it negotiable?",
        "context": "Item 6, Liquidated Damages row. Most aggressive exit penalty in cohort.",
        "why_it_matters": "At $300K revenue, this penalty is ~$60K — a significant barrier to exit. If it's strictly enforced, it materially affects the downside risk of buying in.",
        "strong_answer": "'We've enforced it [X] times in the last 3 years. The clause is standard and not negotiable, but here's how it works in practice.' Transparent about enforcement history.",
        "weak_answer": "'That's a standard franchise provision. We rarely have terminations.' Avoids the enforcement question.",
        "follow_up": "Ask how many of the 2022–2024 terminations/non-renewals resulted in liquidated damages collection. Ask whether the clause survives a transfer (i.e., does a buyer inherit the obligation?)."
    },
    {
        "question": "Q4 territories average $109K revenue. What support exists for operators in the bottom quartile?",
        "context": "Item 19 Table 1. 52 territories in Q4, low of $11,242.",
        "why_it_matters": "25% of territories are at or below $165K — a revenue level where franchisor fees ($68K at $200K) consume a disproportionate share. Understanding what happens to struggling operators tells you about the safety net.",
        "strong_answer": "'We have a performance improvement program. Q4 operators get [specific support: territory analysis, marketing assistance, operational coaching]. Here's the Q4-to-Q3 graduation rate.' Structured support with measurable outcomes.",
        "weak_answer": "'Those are usually newer territories that haven't ramped yet.' Assumes all Q4 operators are early-stage without evidence.",
        "follow_up": "Ask how many of the 10 territories that ceased operations in 2024 were in Q4. Ask what the average tenure of Q4 operators is."
    },
    {
        "question": "The 70% renewal rate is below Mosquito Joe's 77%. What is driving the 30% annual customer loss, and what programs exist to improve retention?",
        "context": "Item 19 Table 3. 70% average, range 33%–90%.",
        "why_it_matters": "Losing 30% of customers annually means you need to replace roughly 100 customers per year at Q3 revenue levels. The cost of acquiring 100 new customers at 48% close rate requires ~200 leads — this is why marketing obligations are $35K+.",
        "strong_answer": "'Retention varies by service type and market. Our top quartile retains 85%+. Here's what they do differently and how we're implementing that system-wide.' Acknowledges the issue, shows improvement plan.",
        "weak_answer": "'70% is strong for a seasonal service business.' Accepts the rate without addressing the cost of churn.",
        "follow_up": "Ask whether retention rates have improved or declined over the past 3 years. Ask for retention broken out by single-territory vs multi-territory operators."
    },
    {
        "question": "The Brand Fund is a flat fee ($150–$450/month) rather than a percentage. What does it fund, and how are spending decisions made?",
        "context": "Item 6, Brand Fund. Escalates from $150 (Y1) to $450/mo (Y7+).",
        "why_it_matters": "Flat-fee brand funds are unusual — they don't scale with system revenue, which means the fund grows only as franchisee count grows. Understanding what it funds and how it's governed tells you whether you're paying for value or just a line item.",
        "strong_answer": "'The Brand Fund supports [specific programs: national digital campaigns, brand development, conference]. Spending is reviewed by the franchisee advisory council. Here's last year's fund report.' Governance and transparency.",
        "weak_answer": "'It supports the brand.' No specifics, no governance detail, no spending report.",
        "follow_up": "Ask for a breakdown of Brand Fund spending. Ask if franchisees have voting input on fund priorities."
    },
    {
        "question": "15 company-owned territories generate $20.8M in the Northeast. Is company-owned expansion planned, and how do territory protections work for franchisees in adjacent markets?",
        "context": "Item 20 Tables 3-4. 15 company-owned stable across 3 years. MA (9), NH (3), RI (2).",
        "why_it_matters": "A franchisor that operates 15 territories is a significant competitor to its own franchisees in the region. Territory encroachment risk is higher when the franchisor has operational infrastructure and incentive to expand company-owned.",
        "strong_answer": "'No company-owned expansion planned. Franchisee territories have [specific protections: minimum population, geographic boundaries, non-compete radius]. We haven't converted any franchised territory to company-owned since [date].' Concrete protections.",
        "weak_answer": "'Our company-owned territories are in a different market. There's no conflict.' Ignores the structural incentive.",
        "follow_up": "Ask whether the 14 territories reacquired in 2021 were converted to the current 15 company-owned. Ask if Item 12 territory protections include a right of first refusal on adjacent territories."
    },
    {
        "question": "Franchised revenue declined -6% in 2022 but recovered to +7% in 2024. What drove the decline, and is the recovery sustainable?",
        "context": "Item 19 Table 6. Same-store growth 5% in 2024 (195 territories).",
        "why_it_matters": "A system-level revenue decline followed by recovery could reflect either a one-time disruption or structural volatility. The 5% same-store growth is positive, but one year doesn't prove a trend.",
        "strong_answer": "'The 2022 decline was driven by [specific factors: reacquisitions removing revenue, territory closures, market conditions]. 2024 same-store growth of 5% reflects [specific improvements: better marketing programs, service expansion, pricing]. We expect [realistic outlook].' Honest about causes, specific about recovery drivers.",
        "weak_answer": "'2022 was an off year. We're back on track.' No specifics, assumes recovery is self-evident.",
        "follow_up": "Ask for 2025 year-to-date same-store growth data if available. Ask whether the recovery is concentrated in specific regions or broad-based."
    },
    {
        "question": "The minimum royalty escalates to $3,000/month by Year 9. How many current franchisees are paying the minimum versus the percentage?",
        "context": "Item 6, Royalty Fee. Minimums begin Month 13, escalate through Year 9+.",
        "why_it_matters": "If you're paying the minimum royalty ($36K/year at Year 9+), it means your revenue is below $360K — a level where $36K in royalty alone is already 10%+. Understanding how many operators are at the minimum tells you about the bottom of the system's economics.",
        "strong_answer": "'[X]% of franchisees currently pay the minimum. Most hit the percentage threshold by Year [Y].' Specific data, willingness to share system distribution.",
        "weak_answer": "'The minimum is there to ensure commitment. Most franchisees exceed it quickly.' No data, implied dismissal.",
        "follow_up": "Ask whether the minimum royalty has ever been waived or deferred for struggling operators."
    },
],

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "Headline $162K–$220K is inflated by 12-month working capital. Core investment ~$78K–$103K. Franchise fee ($50K) is highest in cohort."},
    {"dimension": "Ongoing fee burden", "rating": "Mixed", "color": "mixed",
     "summary": "#2 at lower revenue, #3 at higher. 26% at $300K. Graduated royalty and marketing cap reward scale."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Recovering from 2022 contraction (−10 net). Zero terminations in 2024. Trajectory positive but 3-year net is only +3."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Best in cohort. Per-territory quartile data, company-owned P&L ($20.8M, 25.9% margin), close/renewal rates. Most actionable Item 19."},
    {"dimension": "Disclosure quality", "rating": "Strong", "color": "strong",
     "summary": "Comprehensive, well-structured. Table numbering error is minor. Honest 12-month working capital estimate. Best overall FDD quality."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Aggressive liquidated damages ($50K+ on termination). MA AG marketing-claims action. 15 company-owned territories create franchisor competition."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Best for data-driven buyers who want to model before committing. Higher franchise fee ($50K) and complex royalty tiers narrow the entry profile."},
    {"dimension": "Overall", "rating": "Mixed", "color": "mixed",
     "summary": "The data-transparency leader in the cohort. Mid-cost, recovering system, most useful Item 19 for buyer financial modeling."},
],

"scorecard_posture": """Mosquito Squad is the best-disclosed brand in this cohort and a reasonable
mid-range option for a buyer who values data over cost minimization. The per-territory quartile
data and company-owned P&amp;L provide the strongest foundation for financial modeling of any brand
reviewed. The system's 2022 contraction is a historical concern, not a current one — 2024 showed
genuine recovery. The main risks are the aggressive liquidated damages clause, the 15 company-owned
territories, and the regulatory signal from the MA AG action. None are disqualifying; all warrant
Discovery Day investigation.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Data-driven buyer who wants to model before committing:</strong> Squad's Item 19
provides more inputs for a financial model than any competitor. If you want to build a
territory P&amp;L from real data before signing, this is the brand that enables it.</li>
<li><strong>Buyer planning to scale:</strong> The graduated royalty (10/9/8%) and marketing cap
($50K) reward revenue growth. At $500K+, Squad's fee structure becomes competitive with brands
that cost less at lower revenue levels.</li>
<li><strong>Buyer comfortable with a recovering system:</strong> The 2022 contraction and
subsequent recovery are fully disclosed. If you believe the turnaround is real, you're buying
into a system with positive momentum and room to grow.</li>
<li><strong>Buyer in a non-Northeast market:</strong> The 15 company-owned territories are
concentrated in MA/NH/RI. Outside this region, there's no direct franchisor competition.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive first-time buyer:</strong> $50K franchise fee (highest in cohort)
plus $15.5K–$21K in outfitting fees means $65K–$71K to the franchisor before any operating
costs. Mosquito Authority enters for $25K–$45K.</li>
<li><strong>Buyer who prioritizes system stability:</strong> The 3-year net growth of +3 units is
essentially flat. Authority (+22) and Joe (+43) have stronger growth records. The 2022 contraction
is a historical fact that some buyers won't look past.</li>
<li><strong>Buyer in the Northeast:</strong> 15 company-owned territories in MA/NH/RI mean
the franchisor is your neighbor and competitor. Territory protections need careful review.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You've gotten a satisfactory explanation for the 2021–2022 restructuring (14 reacquisitions,
12 terminations) and believe the recovery is durable.</li>
<li>You've understood the liquidated damages clause ($50K+ on termination) and accepted
the exit cost.</li>
<li>You've validated Q3 economics ($226K median per territory) with 3+ current single-territory
franchisees — not just Q1/Q2 operators.</li>
<li>If in the Northeast, you've confirmed territory protections against company-owned expansion.</li>
</ul>
""",

"economics_scenarios_config": [
    ("Conservative (Q4 average)", 109000),
    ("Moderate (Q3 median)", 226000),
    ("Strong (Q2 median)", 443000),
],

"economics_cogs_ratio": 0.28,

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Mosquito
Squad's per-territory revenue quartiles (Item 19 Table 1) combined with a 28% cost-of-goods
estimate derived from the company-owned P&amp;L (technician labor 23.4% + products 4.3%). The
company-owned P&amp;L shows 47.7% total COGS, but that includes marketing (7.3%) and program costs
(12.7%) that partially overlap with franchisor fees. The 28% figure represents direct service
delivery costs only. Your actual COGS will depend on your market, staffing model, and
chemical costs.</p>
""",

"economics_assumptions": "Revenue from Item 19 per-territory quartile data. COGS at 28% (technician labor + products from company-owned P&L). Franchisor fees from fee burden model. 'Remaining' must cover: vehicle costs, insurance, storage/facilities, admin, marketing beyond mandatory programs, and your living expenses.",

"economics_detail": """
<h3>What the scenarios tell you</h3>

<p><strong>Conservative (Q4 average, $109K):</strong> After fees ($67K) and COGS ($31K),
only $11K remains. This does not work as a standalone business. Q4 operators are either in
ramp-up phase, operating part-time, or in distressed territories. At this revenue level,
the minimum royalty ($650/mo in Year 2) is not yet binding, but the $35K local marketing
obligation consumes 32% of revenue before any other cost.</p>

<p><strong>Moderate (Q3 median, $226K):</strong> After fees ($71K) and COGS ($63K), $92K
remains. After typical operating costs ($25K–$35K for vehicle, insurance, facilities, admin),
an owner draw of $55K–$65K is plausible. This is a functional business — not luxury income,
but a real livelihood. 51 of 207 territories (25%) are at or above this level within Q3.</p>

<p><strong>Strong (Q2 median, $443K):</strong> After fees ($92K) and COGS ($124K), $227K
remains. After operating costs, an owner draw of $150K+ is achievable. This is where Squad's
graduated royalty starts paying off — the effective rate drops below 10%, and the marketing cap
kicks in. 104 of 207 territories (50%) are at or above Q3 level.</p>

<div class="callout">
<div class="callout-title">The company-owned benchmark</div>
The company-owned operation achieves 25.9% net margin at $1.49M/territory — but without paying
franchisor fees. A franchisee at Q2 median ($443K) paying $92K in franchisor fees would see
margins closer to 15–18% after all costs. This is still attractive, but roughly 8–10 percentage
points lower than the company-owned P&amp;L suggests. The P&amp;L is useful for cost ratios, not
for margin expectations.
</div>

<h3>What the buyer still needs to validate</h3>
<ul class="compact">
<li><strong>Technician labor costs in your market:</strong> The company-owned P&amp;L shows 23.4%
of revenue in tech labor. Verify whether this ratio holds in your geography — labor costs vary
significantly by market.</li>
<li><strong>Q3 achievability timeline:</strong> Talk to 3+ current single-territory operators
about how long it took to reach $226K+ revenue. The quartile data is a snapshot, not a trajectory.</li>
<li><strong>Marketing spend effectiveness:</strong> At Q4 revenue ($109K), the mandatory $35K
marketing obligation is 32% of revenue. Ask whether the franchisor provides marketing support
or optimization for territories at this level.</li>
<li><strong>Seasonality reserves:</strong> Revenue is concentrated in spring–fall. Plan for
3–5 months of minimal income. The 12-month working capital estimate in Item 7 reflects
this reality.</li>
</ul>
""",

"payback_narrative": """
<p>The table below shows how long it would take to recover your initial investment under
different assumptions about annual owner draw (net income after all costs, fees, and
operating expenses — but before personal taxes).</p>

<table>
<thead>
<tr>
<th>Assumed annual owner draw</th>
<th class="num">Core investment (~$90K)</th>
<th class="num">Mid investment ($162K)</th>
<th class="num">High investment ($220K)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">$30K (ramp years)</td>
<td class="num">3.0 years</td>
<td class="num">5.4 years</td>
<td class="num">7.3 years</td>
</tr>
<tr>
<td class="label">$60K (Q3 steady state)</td>
<td class="num">1.5 years</td>
<td class="num">2.7 years</td>
<td class="num">3.7 years</td>
</tr>
<tr>
<td class="label">$100K (Q2 target)</td>
<td class="num">0.9 years</td>
<td class="num">1.6 years</td>
<td class="num">2.2 years</td>
</tr>
</tbody>
</table>

<p class="assumption-note">
"Core investment" strips out the 12-month working capital to show payback on capital you
wouldn't recover even if the business immediately generates cash. The "Mid" and "High"
columns include the full Item 7 range — if you view the working capital as sunk investment
rather than bridge funding, payback takes longer.
</p>

<div class="callout">
<div class="callout-title">The honest frame</div>
If you reach Q3 economics ($226K revenue, ~$60K draw) by Year 3 and sustain it, payback on
core investment occurs around Year 4.5. At the full mid-range investment ($162K), payback
extends to Year 5.7. The key variable is how quickly you exit Q4 — the first 1–2 years of
minimal income are the period where your personal reserves matter most.
</div>
""",

"peer_decision_overlay": [
    {"label": "Lowest-cost entry", "brand": "Mosquito Authority",
     "rationale": "$54K–$128K. Squad's core investment is ~$78K–$103K (stripping 12-month working capital)."},
    {"label": "Lowest ongoing fee burden (established brands)", "brand": "Mosquito Authority",
     "rationale": "17–18% of revenue (2/7 in full cohort; 1st among brands with 100+ outlets). Squad is 26% at $300K — $25K/year more."},
    {"label": "Richest disclosure depth", "brand": "Mosquito Squad",
     "rationale": "Per-territory quartile revenue, company-owned P&L, close/renewal rates. Among the most actionable data sets for financial modeling in this cohort."},
    {"label": "Strongest structure for scaling", "brand": "Mosquito Squad",
     "rationale": "Graduated royalty (10/9/8%) and marketing cap ($50K) reward revenue growth. Fee burden decreases with scale."},
    {"label": "Lowest attrition at scale", "brand": "Mosquito Authority",
     "rationale": "Zero terminations in a 546-outlet system, +22 net 3-year. Squad: +3 net 3-year, recovering from 2022 contraction."},
    {"label": "Richest company-owned benchmark", "brand": "Mosquito Squad",
     "rationale": "$20.8M, 14 territories, 25.9% margin. No other brand provides comparable unit economics data at this scale."},
    {"label": "Lowest-friction entry profile", "brand": "Mosquito Authority",
     "rationale": "Lowest entry floor ($54K), fee deferral option. Squad's $50K franchise fee and complex royalty tiers are less forgiving for new entrants. Note: low friction to enter does not predict profitability."},
],

},

"mosquito-shield": {

"executive_summary": """
<p>Mosquito Shield is the fastest-growing brand in the mosquito pest control cohort — and the
one that most requires careful reading. Net growth of +140 franchised outlets over 2022–2024
leads the category by a wide margin. But that headline masks a churn rate unlike anything else
in the cohort: 122 terminations over the same period, including 65 in a single year (2023).
For every 2.2 outlets opened, one was terminated. This is a system that grows fast and loses
fast.</p>

<p>The fee structure compounds the complexity. Shield's royalty (8%) is the lowest in the cohort,
but its local advertising minimum ($50,000/year) is the highest. At $300K revenue, total
franchisor fees are $86,000 (28.7%) — the highest in the category. The low royalty headline
is misleading; total cost of operation is among the most expensive. And the $50K local ad
floor hits hardest at low revenue levels, precisely where new franchisees operate.</p>

<p>The Item 19 provides quartile-level revenue data with retention metrics. But 21% of outlets
are excluded as "non-conforming" — the highest exclusion rate in the cohort. The revenue data
that is disclosed shows per-outlet figures, not per-territory, and the average reporting outlet
operates 4.5 territories. A single-territory buyer cannot use these numbers directly.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Shield has the most deceptive fee structure in the cohort. The 8% royalty is the
lowest — but the $50,000 local advertising floor pushes total fees to the highest level at
most revenue points. The gap between the royalty headline and the total fee reality is wider
for Shield than for any other brand.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (8% flat):</strong> Lowest in cohort. But paired with Minimum Gross Sales
requirements escalating to $283,500 by Year 5. If you don't hit the minimum, the franchisor
may collect 7% of the shortfall — effectively adding a performance penalty on top of the
royalty. (p. 14)</li>
<li><strong>Brand Fund (2% of Gross Sales):</strong> Weekly. Standard brand contribution.
(p. 14)</li>
<li><strong>Local Advertising ($50K or 10%):</strong> Greater of $50,000 or 10% of gross
revenues per year (after Year 1). This is the highest local ad floor in the cohort. At $200K
revenue, this single line item costs 25% of your gross — before royalty, before any other fee.
At $300K, it's still 17%. The floor creates severe regressive pressure on smaller
operators. (pp. 14–15)</li>
<li><strong>Sales Center ($300–$750/month):</strong> $3,600–$9,000/year. Required for call
handling. Modeled at low end. (p. 16)</li>
<li><strong>Bookkeeping ($200–$500/month):</strong> $2,400–$6,000/year. Mandatory approved
vendor. Modeled at low end. (p. 16)</li>
<li><strong>Advertising Cooperative:</strong> Currently $0. Maximum $25,000/year unless 2/3 of
members approve more. Credits toward local ad obligation. Dormant but contractually
available. (p. 15)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Shield's total franchisor fees ($86,000)
exceed Mosquito Joe ($84,752) — despite Joe having a 10% royalty and Shield having 8%. The
difference is the local ad floor. At $200K, Shield's fees ($76,000) are the highest in the
cohort at 38% of revenue. The 8% royalty is real, but it buys you the most expensive marketing
obligation in the category.
</div>

<div class="callout">
<div class="callout-title">Minimum Gross Sales — a hidden performance requirement</div>
The FDD specifies escalating Minimum Gross Sales thresholds: $45K (Year 1), $100K (Year 2),
$189K (Year 3), $236K (Year 4), $283,500 (Year 5+). If you miss the target, the franchisor
may collect 7% of the shortfall. At Year 5, missing the $283K target by $83K (achieving $200K)
would mean an additional $5,845 in effective fees — on top of the standard royalty. This is a
performance penalty that no other brand in the cohort imposes. (p. 14)
</div>
""",

"item19_narrative": """
<p>Shield's Item 19 provides quartile-level revenue data plus customer retention metrics. It is
substantive — but it requires more careful reading than any other brand's disclosure, because of
a high exclusion rate and multi-territory reporting that complicates per-territory inference.</p>

<h3>Company-owned P&amp;L (1 location, SE Pennsylvania)</h3>
<p>Cost percentages only — absolute revenue is not disclosed:</p>
<ul class="compact">
<li>COGS: 19.1%</li>
<li>Payroll &amp; personnel: 33.2%</li>
<li>Marketing &amp; advertising: 3.6%</li>
<li>Insurance: 4.3%</li>
<li>Auto &amp; travel: 5.7%</li>
<li>Other: 4.6%</li>
<li><strong>Total costs: 70.5% — Adjusted EBITDA: 29.5%</strong></li>
</ul>

<p>This is a single acquired location, 5+ years operational, with a larger geography than a
standard new territory. Owner compensation was adjusted to reflect a general manager salary,
not actual pre-acquisition owner draw. Without absolute revenue, you cannot compute dollar
amounts from these percentages. The 29.5% EBITDA margin is directionally useful but not
directly comparable to your economics.</p>

<h3>Franchisee gross sales by quartile (2024)</h3>
<p>81 of 125 outlets reporting, with 26 excluded as "non-conforming":</p>

<table>
<thead>
<tr>
<th>Quartile</th>
<th class="num">Outlets</th>
<th class="num">Average</th>
<th class="num">Median</th>
<th class="num">Avg Territories</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">Q1 (top 25%)</td>
<td class="num">~20</td>
<td class="num">$819,520</td>
<td class="num">$721,144</td>
<td class="num">8.1</td>
</tr>
<tr>
<td class="label">Q2</td>
<td class="num">~20</td>
<td class="num">$210,494</td>
<td class="num">$175,371</td>
<td class="num">4.4</td>
</tr>
<tr>
<td class="label">Q3</td>
<td class="num">~20</td>
<td class="num">$94,275</td>
<td class="num">$91,470</td>
<td class="num">3.4</td>
</tr>
<tr>
<td class="label">Q4 (bottom 25%)</td>
<td class="num">~20</td>
<td class="num">$31,771</td>
<td class="num">$37,004</td>
<td class="num">2.3</td>
</tr>
<tr style="border-top:2px solid #333">
<td class="label">All outlets</td>
<td class="num">81</td>
<td class="num">$285,839</td>
<td class="num">$134,918</td>
<td class="num">4.51</td>
</tr>
</tbody>
</table>

<h3>What to be careful about</h3>
<p><strong>The exclusion rate is the highest in the cohort.</strong> 26 outlets (21%) are excluded
as "non-conforming." The FDD does not define what non-conforming means. If these are
underperforming outlets, their exclusion materially inflates the reported averages. No other
brand excludes more than a handful of outlets from their Item 19 reporting.</p>

<p><strong>Revenue is per-outlet, not per-territory.</strong> The average reporting outlet operates
4.51 territories. At the system-wide median ($134,918) with 4.51 territories, implied
per-territory revenue is approximately $30,000. Even at the Q2 median ($175,371 across 4.4
territories), per-territory revenue is roughly $40,000. For a buyer evaluating a single
territory, the published revenue data suggests very modest economics.</p>

<p><strong>Customer retention is strong:</strong> 85% returning year-over-year, with $715 average
revenue per customer. 28% prepay rate. These are healthy recurring-business signals — but they
come from the full system, not just the 81 qualifying outlets.</p>

<div class="implication">
<strong>What this means:</strong> The Item 19 data is structurally harder to use than Squad's
(which gives per-territory quartiles) or Joe's (which gives per-franchisee tenure-segmented
data). Shield's data requires you to adjust for multi-territory ownership and accept a 21%
exclusion rate you cannot independently verify. The customer retention metrics are the most
reliable signal — 85% retention with $715/customer revenue is a real recurring business. The
revenue-level data requires more caution.
</div>
""",

"item19_triangulation": """
<h3>Revenue triangulation</h3>
<p>Cross-checking against system-level data provides a useful sanity check.</p>
<ul class="compact">
<li>Total system-wide sales: $25.7M (2024), up from $23.8M (2023)</li>
<li>435 franchised outlets at year-end → approximately $59,000 per outlet across the full system</li>
<li>But many outlets were not operational for the full year (73 opened during 2024)</li>
<li>For 81 qualifying outlets with full-year data: average $285,839 per outlet</li>
<li>Implied contribution from the other 354 outlets: ($25.7M − ($285,839 × 81)) / 354 ≈ $7,200 per outlet</li>
</ul>
<p>That math doesn't quite work — the non-qualifying outlets include recent openings, the 26
"non-conforming," and 44 that were terminated during the year. Many had partial-year revenue.
But the gap between qualifying-outlet revenue ($286K average) and system-level per-outlet
revenue (~$59K) illustrates how much the reported Item 19 data departs from typical unit
economics in the system.</p>

<p>At the customer level: 35,902 total customers across 435 outlets ≈ 83 customers per outlet.
At $715/customer ≈ $59,300 per outlet — this aligns with the system-level per-outlet figure
and is far below the Item 19 qualifying-outlet average. The customer-level math is the more
honest benchmark for what a typical outlet looks like.</p>
""",

"investment_narrative": """
<p>The headline investment range ($120,525–$157,950) is mid-cohort, but two structural features
make it distinctive: the $54,500 franchise fee is the highest in the category, and the
$1,500–$5,000 working capital estimate is the lowest and least conservative.</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($54,500):</strong> Highest in cohort. Multi-territory discounts
available (2nd territory $45K, decreasing to $23.5K for the 10th). A 10% deposit option
exists (Exhibit F). (pp. 12–13)</li>
<li><strong>Franchise Starter Package ($23,600):</strong> Mandatory. Covers laptop, platform
setup, 3-month pest control product supply, marketing materials, 3 months ProNexis/Pocomos/SEO,
training hotel. This is a bundled pre-opening package paid to the franchisor — you cannot
source these independently. (p. 19)</li>
<li><strong>Local advertising ($35K–$50K):</strong> First-year local ad expenditure. This becomes
the $50K floor in Year 2+. A significant portion of the initial investment is pre-committed
to marketing. (p. 19)</li>
<li><strong>Vehicle ($2.1K–$16K):</strong> Low end assumes 3 months of financing; high end
covers customization on your own vehicle ($13,890). Full vehicle + customization can run
~$54.5K MSRP — not reflected in the Item 7 range. (p. 19)</li>
<li><strong>Additional Funds — 3 months ($1,500–$5,000):</strong> This is the lowest working
capital estimate in the cohort. It explicitly excludes salary, employees, rent, and utilities.
Compare to Squad's 12-month/$84K–$117K estimate. Plan for significantly more personal reserves
than this line suggests. (p. 20)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> The $121K–$158K range understates true first-year cash needs.
The $5K working capital cap excludes most actual operating costs. A more realistic first-year
budget adds $30K–$50K beyond the Item 7 range for operating costs, living expenses, and the
gap between the $35K–$50K first-year ad spend and the $50K Year 2+ minimum. Budget $170K–$210K
total for a realistic picture.
</div>
""",

"system_health_narrative": """
<p>Shield's system health is the most conflicted story in the cohort. Net growth of +140
franchised outlets over 3 years is the highest — but it required 267 openings to achieve,
because 122 outlets were terminated in the same period. No other brand comes close to this
churn volume. The question is whether this represents aggressive quality enforcement or
underlying system instability.</p>
""",

"system_health_detail": """
<h3>The termination pattern</h3>
<p>The three-year pattern is stark:</p>
<ul class="compact">
<li><strong>2022:</strong> 91 opened, 13 terminated. Growth-dominant. Net +74.</li>
<li><strong>2023:</strong> 103 opened, 65 terminated, 5 ceased. Massive churn year. Net +38.</li>
<li><strong>2024:</strong> 73 opened, 44 terminated, 1 ceased. Churn moderating but still high. Net +28.</li>
</ul>

<p>In 2023, the system terminated 65 outlets — more than any other brand in the cohort has
terminated in three years combined. Mosquito Authority had zero terminations across the entire
period. Mosquito Joe had 24 in its worst year (2024). Shield's 65 is in a different category.</p>

<div class="implication">
<strong>What this means:</strong> There are two ways to read this data. The charitable
interpretation: the franchisor is aggressively enforcing quality standards, removing
underperformers to strengthen the system. The concerning interpretation: the business model
or territory assignments are producing a high failure rate, and growth is being sustained by
selling faster than operators leave. Both interpretations are consistent with the data. A buyer
must determine which applies.
</div>

<h3>Geographic concentration</h3>
<p>Massachusetts went from 14 outlets to 39 in 2023 (+25 opened in one year). This level of
single-state concentration is unusual. It could reflect genuine market demand, or it could
reflect territory over-saturation. If you're evaluating a territory in a state with rapid
Shield expansion, ask how many outlets have been terminated in that same state.</p>

<h3>Transfer activity</h3>
<p>12 transfers in 2022, 21 in 2023, 28 in 2024 — steadily increasing. Combined with the
high termination rate, rising transfers suggest increasing franchisee turnover through both
voluntary (transfer) and involuntary (termination) channels. Total churn (terminations +
ceased operations + transfers) was 25 in 2022, 91 in 2023, and 73 in 2024.</p>

<h3>No company-owned outlets</h3>
<p>Zero company-owned locations as of 2024 (2 were sold to franchisees in 2022). The
company-owned P&amp;L in Item 19 is for a location acquired "early 2025" — after the
reporting period. The franchisor is not currently operating in its own system.</p>
""",

"risk_narrative": """
<h3>Churn rate as structural risk</h3>
<p>122 terminations across 3 years against an average system size of ~350 outlets is a
termination rate that no other brand in this cohort approaches. Whether this is quality
enforcement or system failure, the probability of involuntary exit is materially higher for a
Shield franchisee than for any competitor. This is the single most important risk factor in
this report.</p>

<h3>Minimum Gross Sales performance requirements</h3>
<p>Escalating minimum revenue targets ($45K in Year 1, $283,500 by Year 5+) with a 7%
shortfall penalty. This is unique in the cohort — no other brand imposes financial penalties
for underperformance. Combined with the high termination rate, this creates pressure: miss your
revenue targets and you face both a financial penalty and the implicit threat of termination.
Ask the franchisor how many of the terminations were related to minimum gross sales
shortfalls.</p>

<h3>Item 19 exclusion rate</h3>
<p>21% of outlets excluded as "non-conforming" — undefined. If these are struggling operators,
the reported revenue data is systematically biased upward. Combined with the high termination
rate, this raises the question: are underperformers being excluded from the data and then
terminated from the system? The buyer cannot independently verify either the exclusion criteria
or the outcomes for excluded outlets.</p>

<h3>Entity structure</h3>
<p>Mosquito Shield Franchise, LLC (reorganized from Corporation to LLC in Feb 2022) within
Mosquito Holdco / FS PEP Holdco / Princeton Equity Group. Standard PE-backed structure. The
entity reorganization coincided with the start of the rapid expansion period — worth
understanding what operational changes accompanied the restructuring.</p>

<h3>Litigation</h3>
<p>No litigation required to be disclosed. This is clean — but notable in the context of 122
terminations. Either all terminations were consensual / uncontested, or disputes are resolved
outside the disclosure threshold. A buyer should ask whether any terminated franchisees have
disputed their exits.</p>

<h3>Document quality</h3>
<p>PDF text rendering issue (garbled "Pennsylvania" in Table 2). Minor Table 1 vs Table 3
discrepancy (1-unit difference in 2022 start count). These are quality blemishes, not integrity
concerns — but in a filing with a 21% Item 19 exclusion rate, document quality signals matter
more than usual.</p>
""",

"peer_narrative": """
<p>Mosquito Shield sits at the intersection of the strongest growth story and the weakest system
stability in the cohort. It added more outlets than any competitor but also lost more. It has the
lowest royalty but the highest total fee burden at most revenue levels. It grew fastest but has
the highest exclusion rate in its revenue data. Every strength has a corresponding tension.</p>

<p><strong>Sharpest contrast: Mosquito Authority.</strong> Opposite profiles. Authority: zero
terminations, slowest growth (+22), lowest fees, largest system. Shield: 122 terminations,
fastest growth (+140), lowest royalty but highest total fees, second-largest system. Authority
is the conservative play; Shield is the aggressive bet.</p>

<p><strong>Fee comparison: Mosquito Joe.</strong> Similar total fee burden ($86K vs $85K at $300K),
but structured differently. Joe's costs are spread across 5 marketing components; Shield's are
dominated by the $50K local ad floor. Joe offers richer Item 19 data with lower exclusion. The
brands cost about the same but have very different risk profiles — Joe's risk is fee complexity;
Shield's risk is system churn.</p>

<p><strong>Data comparison: Mosquito Squad.</strong> Both provide quartile revenue data, but
Squad's is per-territory (much more useful for a single-territory buyer) while Shield's is
per-outlet (average 4.5 territories). Squad's company-owned P&amp;L provides absolute revenue
($20.8M); Shield's provides only percentages. For financial modeling, Squad gives you
substantially more to work with.</p>
""",

"discovery_questions": [
    {
        "question": "65 outlets were terminated in 2023 and 44 in 2024. What were the primary causes, and how many were related to minimum gross sales shortfalls?",
        "context": "Item 20. 122 terminations over 3 years — highest in cohort by a wide margin.",
        "why_it_matters": "This is the single most important data point in the FDD. Whether terminations are quality enforcement (positive) or system failure (negative) fundamentally changes the risk profile. The minimum gross sales shortfall mechanism provides a financial and contractual basis for termination.",
        "strong_answer": "'[X]% were for non-payment, [Y]% for performance shortfalls, [Z]% for compliance violations. Here are the geographic concentrations. Here's what we've changed since 2023.' Specific causes, willingness to break down the numbers.",
        "weak_answer": "'We maintain high standards. When franchisees don't follow the system, we part ways.' Generic quality language without specific cause data.",
        "follow_up": "Ask for termination causes by state. Ask whether any terminated franchisees were in their first 2 years of operation."
    },
    {
        "question": "26 outlets (21%) are excluded from Item 19 as 'non-conforming.' What does that mean, and what were their revenue levels?",
        "context": "Item 19 Table 1. Highest exclusion rate in cohort. Only 81 of 125 outlets included.",
        "why_it_matters": "If non-conforming outlets are underperformers, the reported revenue data is systematically biased upward. A buyer relying on the quartile data to plan their financial model could be working from inflated numbers.",
        "strong_answer": "'Non-conforming means [specific criteria: incomplete reporting, mid-year status changes, data quality issues]. Their average revenue was $[X]. Here's the comparison with qualifying outlets.' Transparent, quantified.",
        "weak_answer": "'They didn't meet the reporting requirements. The data we show is for compliant operators.' Deflects from the performance question.",
        "follow_up": "Ask whether any of the 26 non-conforming outlets were subsequently terminated. Ask for the revenue distribution with non-conforming outlets included."
    },
    {
        "question": "The local advertising minimum is $50,000/year — the highest in the cohort. What measurable ROI does this deliver for a single-territory operator?",
        "context": "Item 6. At $200K revenue, this is 25% of gross — before royalty or any other fee.",
        "why_it_matters": "The $50K floor is the primary driver of Shield's high total fee burden. If it generates proportionally more leads or higher customer acquisition than competitors' lower ad spend, it justifies the cost. If not, it's a regressive tax on smaller operators.",
        "strong_answer": "'Territories spending $50K on local advertising generate an average of [X] leads, converting to [Y] new customers worth $[Z] in first-year revenue. Here's the attribution data.' Specific, measurable.",
        "weak_answer": "'Marketing is essential to building your business. Our franchisees know it's an investment.' No data, no attribution.",
        "follow_up": "Ask for the average customer acquisition cost across the system. Ask whether any franchisees have successfully negotiated a lower ad floor."
    },
    {
        "question": "Massachusetts went from 14 to 39 outlets in one year (2023). Was this market-driven or recruitment-driven, and how have those outlets performed?",
        "context": "Item 20, state-level data. +25 in a single state in one year is unusual.",
        "why_it_matters": "Rapid expansion in a single market can lead to territory saturation and cannibalization. If many of the 2023 MA openings are now in the bottom quartile or have been terminated, it's a signal about territory quality.",
        "strong_answer": "'Market expansion in MA was driven by [demand signal: customer waitlists, market studies]. Of the 25 opened, [X] are still operating and average $[Y] in revenue.' Performance data for the cohort.",
        "weak_answer": "'Massachusetts is a great market for mosquito control. We saw strong interest from qualified candidates.' Recruitment language without performance data.",
        "follow_up": "Ask how many of the 2023 MA openings appear in the 2024 termination data. Ask whether existing MA franchisees were consulted before the expansion."
    },
    {
        "question": "The Item 19 reports revenue per outlet, but the average outlet operates 4.5 territories. What is the revenue for a single-territory operator?",
        "context": "Item 19 Table 1. System-wide average: $285,839 per outlet across 4.51 territories.",
        "why_it_matters": "A buyer evaluating one territory cannot use per-outlet data. The implied per-territory revenue (~$30K at the median) is dramatically lower than the per-outlet figures suggest.",
        "strong_answer": "'Single-territory operators average $[X] in revenue. We have [Y] single-territory operators in the system.' Specific segmented data.",
        "weak_answer": "'Most successful franchisees expand to multiple territories. We recommend starting with at least 2–3.' Redirects toward multi-territory without answering the question.",
        "follow_up": "Ask how many of the 81 qualifying outlets operate exactly 1 territory, and what their average and median revenue is."
    },
    {
        "question": "The Minimum Gross Sales threshold is $283,500 by Year 5. What percentage of current franchisees are above this threshold, and how many have been charged the shortfall penalty?",
        "context": "Item 6. Franchisor may collect 7% of the difference between actual royalty and 7% of the minimum.",
        "why_it_matters": "If a significant percentage of franchisees are below the minimum, the penalty is a recurring cost, not an edge case. Combined with the high termination rate, it suggests a system where many operators struggle to meet revenue targets.",
        "strong_answer": "'[X]% of Year 5+ franchisees exceed the minimum. We've collected the shortfall penalty from [Y] operators in the past year. Here's what support we provide to help operators reach the threshold.' Transparent about incidence.",
        "weak_answer": "'The minimums are designed to motivate growth. Most franchisees meet them.' No specific numbers.",
        "follow_up": "Ask whether any terminations were directly triggered by minimum gross sales shortfalls. Ask if the shortfall penalty and minimum threshold are negotiable."
    },
    {
        "question": "The entity was reorganized from a Corporation to an LLC in February 2022 — the same period the rapid expansion began. What changed operationally?",
        "context": "Brand notes. Mosquito Shield Franchise Corporation → LLC (Feb 2022).",
        "why_it_matters": "Entity restructuring often coincides with changes in strategy, ownership terms, or franchise agreement structure. The timing with the acceleration from +74 (2022) openings suggests a strategic shift.",
        "strong_answer": "'The restructuring was for [specific reason: PE investment, tax optimization, operational flexibility]. Operationally, we [changed recruitment approach, territory standards, marketing programs].' Connects structure to strategy.",
        "weak_answer": "'It was a routine corporate reorganization. No impact on franchisees.' Dismisses without explaining timing.",
        "follow_up": "Ask whether the franchise agreement terms changed after the reorganization. Ask if territory sizes or franchise fees were modified."
    },
    {
        "question": "No litigation is disclosed despite 122 terminations. Have any terminated franchisees disputed their exits through arbitration or informal channels?",
        "context": "Item 3 — no litigation. Item 20 — 122 terminations.",
        "why_it_matters": "Zero disclosed litigation with 122 terminations is unusual. It could mean all exits were clean and consensual, or it could mean disputes are resolved below the disclosure threshold (arbitration, pre-litigation settlements, or disputes not yet reaching the required stage).",
        "strong_answer": "'We've had [X] arbitration proceedings. Most terminations are mutual — the franchisee agrees to exit. Here's our exit process.' Acknowledges the question honestly.",
        "weak_answer": "'Our legal record speaks for itself. No litigation required to be disclosed.' Technically correct but avoids the substance of the question.",
        "follow_up": "Ask if the franchise agreement requires binding arbitration (which would not appear in Item 3). Ask if any terminated franchisees received settlements or releases."
    },
    {
        "question": "The working capital estimate is $1,500–$5,000 (3 months), excluding salary, employees, rent, and utilities. What should a realistic first-year budget look like?",
        "context": "Item 7. Lowest working capital estimate in cohort. Squad includes $84K–$117K for 12 months.",
        "why_it_matters": "The $5K working capital cap almost certainly understates real cash needs. A buyer who plans around the Item 7 total ($158K) without additional reserves will likely run out of cash.",
        "strong_answer": "'We recommend $[X] in additional personal reserves. Here's a realistic first-year cash flow timeline for a new single-territory operator.' Specific, honest supplemental guidance.",
        "weak_answer": "'The Item 7 estimates are conservative. Most franchisees find them adequate.' Contradicted by the explicit exclusions in the FDD.",
        "follow_up": "Ask what the average first-year total cash outlay is for recent franchise launches. Ask how many of the 2024 terminations were first- or second-year operators."
    },
    {
        "question": "Transfers increased from 12 to 28 over the 3-year period. Are resale prices holding, and what is the average time on market?",
        "context": "Item 20. 12 transfers (2022), 21 (2023), 28 (2024). Rising steadily.",
        "why_it_matters": "Rising transfers combined with high terminations could signal distressed selling. If resale prices are declining or time on market is increasing, the exit economics are deteriorating.",
        "strong_answer": "'Average resale price is [X]× the original franchise fee. Average time on market is [Y] months. We facilitate introductions between sellers and buyers.' Specific data, active support.",
        "weak_answer": "'Transfers fluctuate. We support franchisees who want to transition.' No data on pricing or market dynamics.",
        "follow_up": "Ask whether any transfers were at a loss (below original franchise fee). Ask how many transfers were franchisor-facilitated vs franchisee-initiated."
    },
],

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$121K–$158K headline, but working capital ($5K max) is unrealistically low. True first-year cost is likely $170K–$210K. $54.5K franchise fee is highest in cohort."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "Highest total fees in cohort at most revenue levels despite lowest royalty (8%). $50K local ad floor is the primary driver."},
    {"dimension": "System stability", "rating": "Weak", "color": "weak",
     "summary": "122 terminations over 3 years — no other brand is close. 65 in 2023 alone. Fastest growth (+140) but highest churn. Net growth masks a volatile system."},
    {"dimension": "Revenue disclosure", "rating": "Mixed", "color": "mixed",
     "summary": "Quartile data exists but per-outlet (avg 4.5 territories), not per-territory. 21% exclusion rate is highest in cohort. Company-owned P&L gives percentages only."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "21% 'non-conforming' exclusion rate is a significant transparency concern. PDF rendering issues. Minor table discrepancies. Below peer standard."},
    {"dimension": "Downside risk profile", "rating": "Weak", "color": "weak",
     "summary": "Highest termination rate in cohort. Minimum Gross Sales penalty is unique. Involuntary exit probability is materially higher than any competitor."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Requires high risk tolerance and capital ($170K+ realistic). Best for buyers who believe the growth story and can execute at scale."},
    {"dimension": "Overall", "rating": "Cautious", "color": "weak",
     "summary": "Strongest growth, weakest stability. Every headline number requires a second read. The gap between what Shield looks like on paper and what the underlying data shows is the widest in the cohort."},
],

"scorecard_posture": """Mosquito Shield is the brand in this cohort where the surface story and the
underlying data diverge the most. The growth is real — +140 net units is unmatched. But so is the
churn — 122 terminations in 3 years. The low royalty is real — 8% is the lowest. But total fees are
the highest. The Item 19 data exists — but 21% of outlets are excluded, and per-outlet figures
obscure per-territory economics. A buyer considering Shield needs the highest tolerance for
uncertainty and the sharpest diligence of any brand in this cohort.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who believes in the growth thesis:</strong> If you believe Shield is building
a dominant brand and the churn is a temporary cost of rapid expansion, the growth trajectory
and low royalty could reward early entry.</li>
<li><strong>Multi-territory buyer from day one:</strong> The economics appear to work better at
scale. Q1 operators average 8.1 territories and $820K revenue. The graduated multi-territory
franchise fee discounts support this path.</li>
<li><strong>Buyer with high risk tolerance:</strong> The probability of involuntary exit
(termination) is materially higher than any competitor. You need to be comfortable with that
possibility and capitalized enough to absorb a loss if it happens.</li>
<li><strong>Buyer in an underserved market:</strong> If your target market has genuine unmet
demand for mosquito control and limited competition, Shield's aggressive marketing model
($50K+ local ad spend) could build market share quickly.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Risk-averse first-time buyer:</strong> The termination rate, fee complexity,
Minimum Gross Sales penalties, and 21% exclusion rate create more uncertainty than any other
brand in the cohort. Authority is a categorically safer entry.</li>
<li><strong>Single-territory buyer on a budget:</strong> Per-territory economics appear modest
(implied ~$30K median per territory). The $50K local ad floor is devastating at low revenue
levels. The math works for multi-territory; it's unclear at single-territory scale.</li>
<li><strong>Buyer who needs transparent data:</strong> The 21% exclusion rate, per-outlet
(not per-territory) reporting, and percentage-only P&amp;L make Shield's Item 19 the hardest
to build a financial model from. Squad or Joe offer substantially more usable data.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You've gotten a detailed, cause-level explanation for the 122 terminations and believe the
rate will continue declining.</li>
<li>You've validated per-territory (not per-outlet) revenue with 3+ current single-territory
operators.</li>
<li>You understand and accept the Minimum Gross Sales shortfall penalty and have modeled the
Year 5 threshold ($283,500) against realistic revenue projections.</li>
<li>You've budgeted $170K–$210K total first-year cash (not the $121K–$158K Item 7 range).</li>
<li>You've asked what "non-conforming" means and what those excluded outlets' revenue looked like.</li>
</ul>
""",

"economics_scenarios_config": [
    ("Conservative (Q3 median per outlet)", 91000),
    ("Moderate (Q2 median per outlet)", 175000),
    ("Strong (system-wide average)", 286000),
],

"economics_cogs_ratio": 0.19,

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Mosquito
Shield's per-outlet revenue quartiles (Item 19 Table 1) combined with a 19% COGS estimate
from the company-owned P&amp;L. Shield's Item 19 reports revenue per outlet, not per territory —
the average outlet operates 4.5 territories. A single-territory buyer's economics will differ
significantly. The 21% exclusion rate means the revenue data may overstate typical performance.
Use these scenarios as a framework for questions, not as projections.</p>
""",

"economics_assumptions": "Revenue from Item 19 per-outlet quartile data (not per-territory). COGS at 19% (company-owned P&L, single acquired location, SE PA). Franchisor fees from fee burden model. 'Remaining' must cover: payroll/personnel (33.2% of revenue in company-owned P&L), insurance, vehicle costs, facilities, and your living expenses. The company-owned P&L shows total costs of 70.5% — the scenarios below show only COGS + franchisor fees, not the full cost stack.",

"economics_detail": """
<h3>What the scenarios tell you</h3>

<p><strong>Conservative (Q3 median per outlet, $91K):</strong> After fees ($75K) and COGS ($17K),
essentially nothing remains. At Q3 economics with a single territory (implied ~$27K revenue),
the business is not viable — the $50K local ad floor alone exceeds revenue. Q3 outlets average
3.4 territories, and even at the per-outlet level, fees consume 82% of revenue. This scenario
does not produce a livelihood.</p>

<p><strong>Moderate (Q2 median per outlet, $175K):</strong> After fees ($79K) and COGS ($33K),
$63K remains. But the company-owned P&amp;L shows that payroll/personnel consume 33.2% of
revenue — that's $58K at this revenue level. After payroll, there is virtually no margin. Q2
outlets average 4.4 territories, so per-territory revenue is ~$40K. The math requires
multi-territory scale to work.</p>

<p><strong>Strong (system-wide average, $286K):</strong> After fees ($85K) and COGS ($54K),
$147K remains. After payroll (33.2% = $95K), $52K for all other costs and owner draw. This
is where Shield starts functioning as a business — but $286K is the average of qualifying
outlets (which excludes 21% as non-conforming), not the system average (~$59K per outlet).
Reaching this level likely requires 3–5 territories.</p>

<div class="callout">
<div class="callout-title">The multi-territory math</div>
Shield's economics appear fundamentally oriented toward multi-territory operation. Q1
operators (8.1 territories, $820K average) are likely generating viable margins. Q3–Q4
operators (2–3 territories, $31K–$94K) are likely losing money after fees and operating costs.
The question for a buyer is not "can I make one territory work?" — it may be "can I commit to
and fund 3–5 territories from day one?" The franchise fee discounts ($45K for 2nd, $35K for
3rd) suggest the franchisor agrees.
</div>

<h3>What the buyer still needs to validate</h3>
<ul class="compact">
<li><strong>Single-territory viability:</strong> Ask for revenue data on operators with exactly
1 territory. If no one can sustain a single territory, this is a multi-territory investment
from day one — which changes the capital requirement dramatically.</li>
<li><strong>The payroll ratio:</strong> The company-owned P&amp;L shows 33.2% in payroll/personnel.
Verify whether this is achievable for a smaller operation or reflects economies of scale in a
large geography.</li>
<li><strong>True first-year costs:</strong> The $5K working capital estimate is almost certainly
insufficient. Build your own 12-month cash flow projection with realistic assumptions for
payroll, vehicle, insurance, and the $50K advertising obligation.</li>
<li><strong>Exclusion bias:</strong> If the 26 non-conforming outlets had $0–$50K revenue, the
true system median could be significantly below the reported $135K. Ask for system-wide
revenue data including all outlets.</li>
</ul>
""",

"payback_narrative": """
<p>The table below shows how long it would take to recover your initial investment under
different assumptions about annual owner draw (net income after all costs, fees, and
operating expenses — but before personal taxes).</p>

<table>
<thead>
<tr>
<th>Assumed annual owner draw</th>
<th class="num">Item 7 low ($121K)</th>
<th class="num">Item 7 high ($158K)</th>
<th class="num">Realistic ($190K)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">$20K (Q3 scenario — marginal)</td>
<td class="num">6.0 years</td>
<td class="num">7.9 years</td>
<td class="num">9.5 years</td>
</tr>
<tr>
<td class="label">$50K (Q2 scenario — functional)</td>
<td class="num">2.4 years</td>
<td class="num">3.2 years</td>
<td class="num">3.8 years</td>
</tr>
<tr>
<td class="label">$80K (average qualifying outlet)</td>
<td class="num">1.5 years</td>
<td class="num">2.0 years</td>
<td class="num">2.4 years</td>
</tr>
</tbody>
</table>

<div class="callout">
<div class="callout-title">The honest frame</div>
At Q3 economics ($91K per outlet, ~$20K draw), payback takes 6–10 years. At Q2 ($175K, ~$50K
draw), payback is 2.4–3.8 years. But these are per-outlet figures at 3–4+ territories. A
single-territory buyer at $27K–$40K revenue has no realistic path to payback. The investment
math only works if you reach Q2+ economics — which historically requires multiple territories.
The "Realistic" column adds $32K to the Item 7 high to reflect actual first-year cash needs.
</div>
""",

"peer_decision_overlay": [
    {"label": "Lowest-cost entry", "brand": "Mosquito Authority",
     "rationale": "$54K–$128K. Shield's realistic first-year cost is $170K–$210K."},
    {"label": "Lowest ongoing fee burden (established brands)", "brand": "Mosquito Authority",
     "rationale": "17–18% of revenue (2/7 in full cohort; 1st among brands with 100+ outlets). Shield is 29–38% — among the highest."},
    {"label": "Lowest attrition at scale", "brand": "Mosquito Authority",
     "rationale": "Zero terminations in a 546-outlet system. Shield had 122 terminations over the same 3-year window."},
    {"label": "Fastest growth", "brand": "Mosquito Shield",
     "rationale": "+140 net franchised outlets (2022–2024). But required 267 openings and 122 terminations to achieve."},
    {"label": "Richest disclosure depth", "brand": "Mosquito Squad",
     "rationale": "Per-territory quartiles, $20.8M company-owned P&L. Shield's data is per-outlet with 21% exclusion rate."},
    {"label": "Lowest royalty rate", "brand": "Mosquito Shield",
     "rationale": "8% flat. But total fee burden is among the highest in the cohort due to $50K local ad floor."},
    {"label": "Lowest-friction entry profile", "brand": "Mosquito Authority",
     "rationale": "Lowest entry floor ($54K), fee deferral option. Shield's termination rate and fee complexity make it a higher-risk entry point. Note: low friction to enter does not predict profitability."},
],

},

"mosquito-hunters": {

"executive_summary": """
<p>Mosquito Hunters is the smallest system in the mosquito pest control cohort (135 franchised
outlets) and the only brand structured as a combination franchise — bundling mosquito control,
general pest control (Pest Hunters), and holiday lighting (Humbug). This diversification is the
single most distinctive feature of the brand: it directly addresses the seasonality problem that
every mosquito franchise faces.</p>

<p>The Item 19 provides 7 tables of operational data — customer counts, treatment pricing,
customer values by region, and holiday lighting revenue — but <strong>does not disclose gross
revenue or profitability per franchise unit</strong>. This means the most fundamental number a
buyer needs (how much money does this business make?) must be triangulated from indirect data.
The triangulation is possible and produces plausible estimates, but it is inference, not
disclosure.</p>

<p>The system health story is one of genuine turnaround. Hunters contracted in 2022 (−4 net)
and 2023 (−1), then reversed sharply in 2024 (+13, zero terminations). The 3-year net of +8
is modest, but the trajectory — from 17 terminations in 2022 to zero in 2024 — is the most
dramatic stability improvement in the cohort. The initial franchise fee ($107,000) is the
highest in the category by a wide margin, driven by a $57,000 bundled training/supply/support
component that is unlike any competitor's fee structure.</p>
""",

"fee_burden_narrative": """
<p>Mosquito Hunters sits in the middle of the cohort on ongoing fee burden — third at most
revenue levels. The 10% royalty matches Authority, the $37,500 marketing floor is competitive
with Joe's $37K DMP, and the $9,000/year call center fee is a meaningful fixed cost at lower
revenue levels. The structure is simpler than Joe's or Shield's.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (10% of Net Revenues):</strong> Standard rate. Basis is Net Revenues
(excludes taxes/refunds), not Gross Sales — modeled as equivalent at these revenue levels.
Additional 15% royalty on revenue earned outside territory (total 25% for out-of-territory
work). (p. 15)</li>
<li><strong>Marketing ($37,500 floor or 10%):</strong> Three mandatory components: Local
Advertising ($8K or 2%), Centrally Managed Media Fund ($26.5K or 7%), and Tools &amp;
Programs Fund ($3K or 1%). The combined floor ($37,500) is regressive at lower revenue —
at $200K, it's 18.75% of revenue on marketing alone. (pp. 15–16, 19–20)</li>
<li><strong>Call Center ($750/month):</strong> $9,000/year. First year included in the initial
franchise fee. May increase, not expected to exceed $1,000/month. This is a significant
fixed cost — higher than any competitor's call center charge. (p. 15)</li>
<li><strong>Technology ($150/month):</strong> $1,800/year. Increases to $250/month when
cumulative Net Revenues reach $1M. May increase up to $500/month. (p. 15)</li>
<li><strong>Convention (up to $2,000/year):</strong> Must pay even if not attending. Excludes
travel/lodging. (p. 17)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Hunters' $80,300 total fees (26.8%) are
mid-cohort — less than Joe ($84,752) and Shield ($86,000), more than Authority ($52,800) and
Squad ($77,880). The fee structure is relatively straightforward compared to Joe's 5-component
marketing or Shield's minimum gross sales penalty. The main cost risk is the $37,500 marketing
floor hitting hard at low revenue: at $200K, total fees are $70,300 (35.1%).
</div>

<div class="callout">
<div class="callout-title">The out-of-territory penalty</div>
Revenue earned outside your assigned territory incurs an additional 15% royalty (total 25%).
This is the most punitive out-of-territory provision in the cohort. If your service area
bleeds across territory lines — common in pest control where customers don't know franchise
boundaries — this can create unexpected cost. Ask the franchisor how territory boundaries
are enforced in practice. (p. 15)
</div>
""",

"item19_narrative": """
<p>Mosquito Hunters' Item 19 is the most unusual in the cohort. It provides 7 tables of
operational data — customer counts, treatment pricing, customer values, and holiday lighting
revenue — but <strong>never discloses gross revenue or profitability per franchise unit</strong>.
This means the single most important number a buyer needs must be inferred, not read.</p>

<h3>What IS disclosed</h3>

<p><strong>Customer counts by quartile (Table A.1):</strong> 63 Strategic Partners operating 100
territories, segmented by quartile:</p>

<table>
<thead>
<tr>
<th>Quartile</th>
<th class="num">SPs</th>
<th class="num">Avg Customers</th>
<th class="num">Median</th>
<th class="num">High</th>
<th class="num">Low</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">Q1 (top 25%)</td>
<td class="num">15</td>
<td class="num">444</td>
<td class="num">439</td>
<td class="num">611</td>
<td class="num">357</td>
</tr>
<tr>
<td class="label">Q2</td>
<td class="num">16</td>
<td class="num">283</td>
<td class="num">287</td>
<td class="num">354</td>
<td class="num">213</td>
</tr>
<tr>
<td class="label">Q3</td>
<td class="num">16</td>
<td class="num">167</td>
<td class="num">163</td>
<td class="num">203</td>
<td class="num">147</td>
</tr>
<tr>
<td class="label">Q4 (bottom 25%)</td>
<td class="num">16</td>
<td class="num">101</td>
<td class="num">100</td>
<td class="num">146</td>
<td class="num">30</td>
</tr>
</tbody>
</table>

<p><strong>Treatment pricing (Tables A.2–A.3):</strong> Mosquito treatment prices range from
$72–$88 average by region. Non-mosquito pest control averages $61–$88. Pricing is competitive
with the cohort.</p>

<p><strong>Customer value (Table A.4):</strong> Average annual customer value for mosquito-only
service ranges from $726 (Region 2: Midwest/Mid-Atlantic) to $1,232 (Region 4: FL/LA/TX).
Median values are similar. This is per-customer annual spend, not per-territory revenue.</p>

<p><strong>Holiday lighting (Table A.7):</strong> 26 Strategic Partners fully participated in
Humbug Holiday Lighting in 2024 (up from 3 in 2023 pilot). Average revenue: $64,727. Median:
$53,701. High: $305,528. This is the most distinctive data point in the filing — no other
brand offers a counter-seasonal revenue stream.</p>

<h3>What is NOT disclosed</h3>
<ul class="compact">
<li><strong>Total gross revenue per franchise unit</strong> — not disclosed anywhere</li>
<li><strong>Profitability or cost structure</strong> — no P&amp;L, no COGS, no margin data</li>
<li><strong>Revenue per territory</strong> — customer counts are per Strategic Partner (who may
operate multiple territories), not per territory</li>
<li><strong>Customer retention rate</strong> — not disclosed (unlike Joe at 77% and Shield at 85%)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Hunters gives you the building blocks to estimate revenue
(customer count × customer value), but requires you to assemble them yourself. The absence of
a direct revenue disclosure is itself a signal — the franchisor chose to disclose operational
metrics while withholding the bottom line. A buyer should ask why. The holiday lighting data is
a genuine differentiator and deserves separate analysis.
</div>
""",

"item19_triangulation": """
<h3>Revenue triangulation (inferred — not disclosed)</h3>
<p><strong>This section presents revenue estimates derived from indirect Item 19 data.
These are not disclosed figures. They are analytical inferences with meaningful uncertainty.</strong></p>

<p>Using Region 2 (Midwest/Mid-Atlantic, 21 businesses — the largest regional group) as
the baseline for customer value ($726 average):</p>
<ul class="compact">
<li>Q3 median (163 customers) × $726 = <strong>~$118K mosquito revenue</strong></li>
<li>Q2 median (287 customers) × $726 = <strong>~$208K mosquito revenue</strong></li>
<li>Q1 median (439 customers) × $726 = <strong>~$319K mosquito revenue</strong></li>
</ul>

<p>Adding holiday lighting for the 26 participating SPs (median $53,701):</p>
<ul class="compact">
<li>Q3 + holiday lighting: ~$118K + $54K = <strong>~$172K combination revenue</strong></li>
<li>Q2 + holiday lighting: ~$208K + $54K = <strong>~$262K combination revenue</strong></li>
</ul>

<p>Adding non-mosquito pest control revenue is harder — the FDD provides treatment counts
and pricing but not customer-level revenue for pest control in an easily combinable format.
Directionally, pest control adds $10K–$30K per SP depending on the market.</p>

<div class="callout">
<div class="callout-title">Triangulation uncertainty</div>
These estimates carry at least ±20% uncertainty. The customer value varies significantly
by region ($726–$1,232), the customer count data excludes 26% of SPs, and pest control
revenue is not cleanly estimable. The combination franchise (mosquito + pest + holiday)
adds genuine revenue diversification, but the total is uncertain. A buyer must validate
these estimates directly with current franchisees — the FDD does not give you the answer.
</div>
""",

"investment_narrative": """
<p>The headline investment range ($141,295–$170,743) is mid-to-high in the cohort, but the
fee structure is unique: $107,000 goes directly to the franchisor ($50K license fee + $57K
training/supply/support package). This is the highest initial franchise fee in the category
by a wide margin — nearly double Authority's $45K and more than double Squad's $50K standalone
fee.</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Initial License Fee ($50,000):</strong> The franchise fee itself. VetFran/MinorityFran
/First Responder discount: 10% off this portion. Additional territory: $25,000. (pp. 14–15)</li>
<li><strong>Training, Supply &amp; Support Fee ($57,000):</strong> Mandatory bundled package
covering initial training, pest control supplies, marketing materials, and first-year call
center service. This is the most distinctive and expensive line item in the cohort — no other
brand bundles a $57K pre-opening package. The buyer cannot unbundle or source components
independently. (p. 15)</li>
<li><strong>Service Vehicle ($8.35K–$16.7K deposit):</strong> 60- or 72-month lease with 10–20%
down. The ongoing lease payment ($1,200–$1,525/month) is listed separately. Total vehicle cost
over the lease term is $72K–$110K — a significant long-term commitment not fully reflected in
the Item 7 range. (p. 21)</li>
<li><strong>Holiday Lighting Inventory ($6K–$14K):</strong> New line item for the Humbug
program. This is the investment that enables the counter-seasonal revenue stream. (p. 21)</li>
<li><strong>Additional Funds — 3 months ($11.9K–$15.4K):</strong> Modest working capital
estimate. Like most competitors (except Squad's 12-month approach), this underestimates true
first-year cash needs. (p. 21)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> $107K of the $141K–$171K investment goes to the franchisor.
This is 75% of the low-end investment — the highest franchisor share in the cohort. The $57K
bundled package means you are paying for training, supplies, and call center service upfront
whether or not you would have chosen to spend that amount independently. The value proposition
of this bundle is the central question of the investment decision.
</div>
""",

"system_health_narrative": """
<p>Mosquito Hunters tells a clear turnaround story. The system contracted for two consecutive
years (2022: −4 net, 2023: −1) before reversing sharply in 2024 (+13, zero terminations).
The 3-year net of +8 franchised units is modest, but the trajectory from 17 terminations in
2022 to zero in 2024 is the most dramatic stability improvement in the cohort.</p>
""",

"system_health_detail": """
<h3>The contraction years (2022–2023)</h3>
<p>17 terminations in 2022, 11 in 2023. All closures across all three years are coded
exclusively as "Terminations" — zero non-renewals, zero ceased operations. This classification
is the franchisor's choice and is unusually uniform. In other brands, exits are distributed
across multiple categories. Whether this reflects genuine termination or a reporting convention
is worth understanding.</p>

<div class="implication">
<strong>What this means:</strong> The contraction was real — the system shrank from 127 to 122
franchised outlets over two years. But the coding pattern matters. If all exits are classified
as terminations (franchisor-initiated), it suggests the franchisor was actively removing
operators. If some were actually voluntary departures coded as terminations, the picture is
different. Ask the franchisor what triggered each termination category.
</div>

<h3>The 2024 reversal</h3>
<p>Zero terminations, 13 openings, net +13. The turnover rate dropped from 20.3% (2022) to
3.9% (2024) — the sharpest improvement in the cohort. 21 projected new outlets for next year.
This is either a genuine operational turnaround or a one-year anomaly. One year of data doesn't
prove a trend, but zero terminations is zero terminations.</p>

<h3>Transfer activity</h3>
<p>10 transfers in 2022, 8 in 2023, 5 in 2024 — steadily declining. This is consistent with
a stabilizing system: fewer people wanting to sell, or the system is small enough that transfer
volume is naturally low.</p>

<h3>Affiliate-owned footprint</h3>
<p>6 affiliate-owned territories, stable across the reporting period. These are excluded from
the Item 19 data. The franchisor operates a small portion of the system alongside
franchisees.</p>
""",

"risk_narrative": """
<h3>Revenue disclosure gap</h3>
<p>The absence of gross revenue disclosure is the most significant risk signal in this FDD —
not because it implies bad economics, but because it prevents the buyer from independently
validating the business model. Every other brand in the cohort provides some form of revenue
data (per-territory, per-outlet, or per-franchisee). Hunters provides customer counts,
treatment pricing, and customer values — the building blocks — but withholds the assembled
number. A buyer must ask why, and must validate revenue directly with current franchisees.</p>

<h3>The $107K initial franchise fee</h3>
<p>The highest in the cohort by far. The $57K training/supply/support bundle is mandatory and
non-negotiable. If the bundled services (training, supplies, call center first year) are
genuinely worth $57K, this is fair pricing. If comparable services could be sourced for $20K–
$30K, the buyer is overpaying. There is no way to verify this from the FDD alone — the buyer
needs to compare the training program, supply quality, and call center service against what
competitors offer at lower price points.</p>

<h3>Item 19 exclusion rate</h3>
<p>22 of 85 Strategic Partners (26%) are excluded from the Item 19 tables. Eight are excluded
specifically for "failing to invest in MH marketing programs." Excluding operators who don't
follow the system is defensible — but it also means the reported customer counts and values
represent compliant operators only. If non-compliant operators have materially lower customer
counts, the disclosed data overstates what a typical operator achieves.</p>

<h3>Out-of-territory royalty</h3>
<p>25% total royalty on revenue earned outside territory (10% standard + 15% surcharge). This
is the most aggressive out-of-territory provision in the cohort. In practice, pest control
customers don't know or respect franchise boundaries. If 10% of your revenue is classified as
out-of-territory, you pay an extra $2,100–$5,250/year at typical revenue levels.</p>

<h3>Combination franchise complexity</h3>
<p>Hunters is now a three-brand combination (Mosquito Hunters + Pest Hunters + Humbug Holiday
Lighting). This diversification is genuinely valuable for offsetting seasonality, but it also
means you're operating three distinct service lines with different skill requirements, inventory
needs, and customer acquisition strategies. The operational complexity is higher than a
single-service franchise.</p>

<h3>Litigation</h3>
<p>No litigation required to be disclosed. Clean record across the reporting period.</p>
""",

"peer_narrative": """
<p>Mosquito Hunters occupies a unique position in this cohort: the smallest system, the only
combination franchise, the highest initial fee, and the only brand that gives you customer
data without giving you revenue. It is not easily comparable to the other four on a single
dimension.</p>

<p><strong>Cost comparison: Mosquito Authority.</strong> Authority enters for $54K–$128K vs.
Hunters' $141K–$171K. At $300K revenue, Authority's ongoing fees are $52,800 vs. Hunters'
$80,300 — a $27,500/year gap. Authority has zero terminations vs. Hunters' recent 28. The
cost-and-stability comparison heavily favors Authority. Hunters' advantage is the combination
franchise: Authority offers mosquito control only.</p>

<p><strong>Disclosure comparison: Mosquito Joe &amp; Squad.</strong> Joe and Squad both
disclose gross revenue per franchise unit (Joe by tenure, Squad by quartile per territory).
Hunters discloses customer counts and values but not the total. For financial modeling, Joe
and Squad give you the assembled picture; Hunters gives you the parts and asks you to build
it yourself.</p>

<p><strong>The differentiation case: combination franchise.</strong> If you are specifically
attracted to the multi-service model (mosquito + pest + holiday lighting), Hunters is the only
option in this cohort. The holiday lighting data ($54K median per participating SP) represents
a genuine counter-seasonal revenue stream that no competitor offers. The question is whether
this diversification justifies the $107K initial fee and the disclosure limitations.</p>
""",

"discovery_questions": [
    {
        "question": "The Item 19 provides customer counts and values but never discloses gross revenue per franchise unit. Why?",
        "context": "Item 19 — 7 tables of operational data, no revenue total. Every other brand in the cohort discloses some form of revenue.",
        "why_it_matters": "Revenue disclosure is the single most useful data point for a prospective buyer. Its absence forces reliance on triangulation and franchisee conversations. Understanding the franchisor's reasoning tells you whether this is a strategic choice (revenue data is unfavorable) or a structural one (the combination franchise makes revenue reporting complex).",
        "strong_answer": "'Revenue varies significantly by service mix and market. We provide building blocks so buyers can model their specific situation. Here is supplemental revenue data we can share informally.' Acknowledges the gap, offers to fill it.",
        "weak_answer": "'Our Item 19 is comprehensive — 7 tables of data. We give you more operational detail than most brands.' Deflects from what's missing.",
        "follow_up": "Ask for total revenue (all services combined) for the median Strategic Partner. Ask whether revenue data was disclosed in prior-year FDDs."
    },
    {
        "question": "The initial franchise fee is $107,000 — the highest in the cohort by far. What specifically does the $57,000 training/supply/support component include, and how does it compare to competitors' training programs?",
        "context": "Item 5. $50K license + $57K bundled package. Next highest is Shield at $54.5K total franchise fee.",
        "why_it_matters": "75% of the low-end investment goes directly to the franchisor. The $57K bundle is the most expensive pre-opening package in the cohort. If the services are genuinely worth $57K, it's fair. If not, the buyer is overpaying for a bundle they can't unbundle.",
        "strong_answer": "'The $57K covers [specific itemized list: X days training, Y months product supply, Z call center minutes]. Here's how each component is valued. Competitors charge less but provide [specific differences].' Transparent breakdown.",
        "weak_answer": "'It's a comprehensive launch program. Our franchisees tell us it's worth every penny.' No breakdown, no comparison.",
        "follow_up": "Ask for a line-item breakdown of the $57K. Ask what a franchisee receives differently than competitors' $0–$25K training programs."
    },
    {
        "question": "17 terminations in 2022, 11 in 2023, then zero in 2024. What changed?",
        "context": "Item 20. All exits across all years coded as 'Terminations' — zero in any other category.",
        "why_it_matters": "The turnaround is the most dramatic in the cohort. Understanding what drove it tells you whether the improvement is structural (operational changes, better territory selection, improved support) or cyclical (one good year).",
        "strong_answer": "'We [changed territory selection criteria / improved training / added support programs / restructured underperforming markets]. Here are the specific operational changes and their timing.' Cause-and-effect, not coincidence.",
        "weak_answer": "'We're focused on supporting our franchisees. The results speak for themselves.' No explanation for why 2024 was different from 2022.",
        "follow_up": "Ask whether the same franchisor management team was in place throughout 2022–2024. Ask whether franchise agreement terms changed."
    },
    {
        "question": "26 of 63 qualifying SPs participated in Humbug Holiday Lighting. What's the adoption trajectory, and what does a non-participating SP look like during winter?",
        "context": "Item 19 Table A.7. 26 SPs in 2024, up from 3 in 2023 pilot. Median revenue: $53,701.",
        "why_it_matters": "The combination franchise is the core differentiator. If only 41% of SPs participate in holiday lighting, 59% have a pure mosquito/pest business with winter dead season. Understanding adoption rates and barriers tells you how real the diversification is.",
        "strong_answer": "'Adoption grew from 3 to 26 and we expect [X] next year. Non-participants typically [describe winter operations: reduced hours, off-season marketing, etc]. Here's the revenue impact of adding holiday lighting.' Adoption trajectory with economics.",
        "weak_answer": "'Holiday lighting is optional but strongly recommended. Participants love it.' No adoption data, no economics for non-participants.",
        "follow_up": "Ask what prevents the other 37 SPs from participating (inventory cost? skill gap? market?). Ask whether the $6K–$14K lighting inventory investment is a one-time or recurring cost."
    },
    {
        "question": "22 Strategic Partners (26%) are excluded from Item 19, including 8 for not investing in MH marketing. What were their customer counts?",
        "context": "Item 19 population notes. Exclusion rate is comparable to Shield's 21%.",
        "why_it_matters": "If excluded SPs have significantly lower customer counts, the reported quartile data is biased upward. The 8 excluded for marketing non-compliance are particularly interesting — their underperformance may reflect what happens when the marketing programs don't work or feel unaffordable.",
        "strong_answer": "'Excluded SPs averaged [X] customers. The 8 marketing non-compliant operators averaged [Y] customers. Here's the data with all SPs included.' Transparent, quantified.",
        "weak_answer": "'We exclude operators who don't follow the system. The data represents what compliant franchisees achieve.' Defensible but avoids the performance question.",
        "follow_up": "Ask whether any of the 8 marketing-excluded SPs were subsequently terminated. Ask for the customer count distribution with all 85 SPs included."
    },
    {
        "question": "The 25% royalty on out-of-territory revenue — how is 'outside territory' determined in practice, and what percentage of a typical SP's revenue falls outside?",
        "context": "Item 6. 10% standard + 15% surcharge for out-of-territory revenue.",
        "why_it_matters": "If boundary enforcement is strict and 10–15% of revenue is classified as out-of-territory, this adds $2,100–$7,900/year in extra royalty at typical revenue levels. In pest control, customers near territory edges frequently straddle boundaries.",
        "strong_answer": "'We define territory by [zip code / geography / household count]. Typical out-of-territory revenue is [X]% of total. Here's how disputes are resolved.' Specific mechanism and typical impact.",
        "weak_answer": "'Territories are clearly defined. Out-of-territory revenue is rare.' No data on typical incidence.",
        "follow_up": "Ask for the average out-of-territory royalty paid per SP last year. Ask whether territory boundaries can be adjusted."
    },
    {
        "question": "The vehicle lease runs 60–72 months at $1,200–$1,525/month. What is the total cost of ownership, and can franchisees source vehicles independently?",
        "context": "Item 7. Deposit $8.4K–$16.7K + monthly lease. Total over term: $72K–$110K.",
        "why_it_matters": "The vehicle cost over the lease term exceeds the franchise fee. If franchisees must use a designated supplier and lease structure, the total cost may be above market. If they can source independently, the Item 7 range is more controllable.",
        "strong_answer": "'Franchisees can source vehicles independently as long as they meet [specific specs]. Here are the specs. The designated supplier offers [competitive advantage].' Flexibility and transparency.",
        "weak_answer": "'Our vehicle program ensures brand consistency. It's competitively priced.' No flexibility, no market comparison.",
        "follow_up": "Ask whether any current franchisees sourced vehicles independently and at what cost."
    },
    {
        "question": "The combination franchise adds pest control and holiday lighting. What percentage of total revenue does each service line contribute for a typical SP?",
        "context": "Brand is now Mosquito Hunters + Pest Hunters + Humbug Holiday Lighting.",
        "why_it_matters": "Understanding the revenue mix tells you whether this is truly a diversified business or a mosquito franchise with add-ons. If 90% of revenue is mosquito, the combination is marketing, not economics.",
        "strong_answer": "'Typical mix is [X]% mosquito, [Y]% pest, [Z]% holiday. SPs with all three services average $[total]. Here's how the mix changes by market and tenure.' Specific, segmented.",
        "weak_answer": "'It depends on the market. We encourage SPs to maximize all three service lines.' No data on typical mix.",
        "follow_up": "Ask for revenue-mix data segmented by SPs who participate in all three services vs mosquito-only. Ask which service line is growing fastest."
    },
],

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Weak", "color": "weak",
     "summary": "Highest initial franchise fee in cohort ($107K, of which $57K is mandatory bundled package). Total $141K–$171K."},
    {"dimension": "Ongoing fee burden", "rating": "Mixed", "color": "mixed",
     "summary": "#3 at most revenue levels. 26.8% at $300K. $37.5K marketing floor is regressive. 25% out-of-territory royalty is most aggressive in cohort."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Dramatic turnaround: 17 terminations (2022) to zero (2024). But smallest system (135 outlets) and only +8 net over 3 years."},
    {"dimension": "Revenue disclosure", "rating": "Weak", "color": "weak",
     "summary": "No gross revenue disclosed. Customer counts and values enable triangulation (~$120K–$210K mosquito-only) but this is inference, not disclosure."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "7 Item 19 tables with useful operational data, but the deliberate omission of revenue is a transparency concern. 26% SP exclusion rate."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "System stabilizing. No litigation. But small system, high initial fee, and revenue uncertainty create meaningful risk."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Only combination franchise in cohort (mosquito + pest + holiday). Appeals to buyers who want diversification. Requires comfort with revenue uncertainty."},
    {"dimension": "Overall", "rating": "Cautious", "color": "mixed",
     "summary": "The differentiation story (combination franchise, holiday lighting) is real. The disclosure gap (no revenue) is real. Both must be weighed."},
],

"scorecard_posture": """Mosquito Hunters is the hardest brand in this cohort to evaluate — not
because the data is bad, but because the most important number (revenue) isn't disclosed. The
operational data is genuinely useful: customer counts, treatment pricing, customer values, and
holiday lighting economics give you the building blocks. But the buyer must do the assembly. The
combination franchise is a legitimate differentiator that no competitor matches. The system health
turnaround (zero terminations in 2024) is encouraging. The $107K initial fee is the hardest pill
to swallow without revenue validation. This brand requires more franchisee due diligence than any
other in the cohort — not because it's necessarily worse, but because the FDD asks you to take
more on trust.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who wants year-round revenue:</strong> The combination franchise (mosquito
spring–fall + holiday lighting fall–winter + pest control year-round) directly addresses the
seasonality problem that limits every other brand in the cohort. If off-season income matters
to you, Hunters is the only option.</li>
<li><strong>Buyer comfortable with operational complexity:</strong> Running three service lines
requires more diverse skills (pest identification, lighting design, seasonal inventory
management) than a single-service franchise. If you welcome variety, this fits.</li>
<li><strong>Buyer willing to do more pre-purchase diligence:</strong> The revenue gap in the
FDD means you must validate economics through 3–5 franchisee conversations. If you're
disciplined about diligence, the data is obtainable — it's just not in the document.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who needs transparent unit economics before committing:</strong> If you want
to model P&amp;L from disclosed data (like Joe or Squad provide), Hunters won't give you that.
Revenue must be inferred or obtained informally.</li>
<li><strong>Budget-sensitive buyer:</strong> $107K initial franchise fee is more than double
most competitors. The $57K bundled package cannot be negotiated or unbundled.</li>
<li><strong>Buyer who wants a simple, focused business:</strong> Three service lines, seasonal
transitions, and different inventory/skill requirements create more operational complexity than
a pure mosquito franchise.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You've validated actual total revenue with 3+ current Strategic Partners across different
regions and service mixes.</li>
<li>You've gotten a satisfactory explanation for why gross revenue is not disclosed while
competitors provide it.</li>
<li>You understand what the $57K training/supply/support package includes and have compared
it against competitors' offerings at lower price points.</li>
<li>You've confirmed that the 2024 turnaround (zero terminations) reflects structural changes,
not just a one-year pause in enforcement.</li>
<li>You've evaluated whether you actually want to operate three service lines or just want
a mosquito franchise — because you're buying all three.</li>
</ul>
""",

"economics_scenarios_config": [
    ("Mosquito-only (Q3 triangulation)", 118000),
    ("Mosquito-only (Q2 triangulation)", 208000),
    ("Combination (Q2 + holiday lighting)", 262000),
],

"economics_cogs_ratio": 0.23,

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This section uses revenue estimates <strong>inferred from indirect Item 19 data</strong>, not
disclosed figures. Mosquito Hunters does not disclose gross revenue per franchise unit. Revenue
is triangulated from customer counts (Table A.1) × customer values (Table A.4, Region 2
baseline). COGS at 23% is borrowed from Mosquito Authority's company-owned P&amp;L — the only
single-territory cost data available in the cohort. Mosquito Hunters provides no cost data.
These scenarios carry more uncertainty than those in the other reports in this series.</p>
""",

"economics_assumptions": "Revenue triangulated from Item 19 customer counts × customer values (Region 2 baseline, $726/customer). Holiday lighting from Table A.7 median ($53,701). COGS at 23% (borrowed from Mosquito Authority — no Hunters cost data available). Franchisor fees from fee burden model. 'Remaining' must cover: vehicle lease ($14.4K–$18.3K/year), insurance, storage, bookkeeping, seasonal labor, and your living expenses.",

"economics_detail": """
<h3>What the scenarios tell you</h3>

<p><strong>Mosquito-only conservative (Q3 triangulation, $118K):</strong> After fees ($69K)
and COGS ($27K), $22K remains. This must cover vehicle lease ($14K–$18K/year), insurance,
storage, and living expenses. At Q3 mosquito-only revenue, the business is likely cash-flow
negative after operating costs. This is why the combination franchise matters — holiday
lighting income could bridge the gap.</p>

<p><strong>Mosquito-only moderate (Q2 triangulation, $208K):</strong> After fees ($77K) and
COGS ($48K), $83K remains. After vehicle lease and operating costs ($25K–$35K), an owner draw
of $48K–$58K is plausible. This is a functional but modest livelihood — and it requires reaching
Q2 customer counts (287 median), which fewer than half of qualifying SPs achieve.</p>

<p><strong>Combination franchise (Q2 + holiday, $262K):</strong> After fees ($82K) and COGS
($60K), $120K remains. After operating costs, an owner draw of $70K–$85K becomes plausible.
This is the scenario where Hunters' combination model starts to differentiate — the holiday
lighting revenue fills the winter gap and pushes total economics past the pure-mosquito
competitors at comparable fee levels.</p>

<div class="callout">
<div class="callout-title">The inference chain</div>
These scenarios are two steps removed from disclosed data: (1) revenue is triangulated, not
reported, and (2) COGS is borrowed from another brand. The combination scenario adds a third
inference layer: assuming holiday lighting participation and median performance. Each step adds
uncertainty. The scenarios are useful for framing questions, not for financial planning. A buyer
must validate actual revenue — from franchisee conversations, not from this report.
</div>

<h3>What the buyer still needs to validate</h3>
<ul class="compact">
<li><strong>Actual total revenue:</strong> The single most important number. Ask 3+ current SPs
for their total gross revenue across all three service lines.</li>
<li><strong>Holiday lighting economics:</strong> The $54K median revenue sounds attractive, but
what are the costs? Inventory ($6K–$14K initial), labor (installation and removal), insurance,
and equipment — the FDD doesn't provide holiday-lighting-specific margins.</li>
<li><strong>The $57K bundle value:</strong> Compare what Hunters provides for $57K against
what competitors include in their $0–$25K franchise fees. Is the training longer? Are the
supplies better? Is the first-year call center service a genuine advantage?</li>
<li><strong>Service mix viability:</strong> Ask SPs who run all three lines about the
operational complexity. Is it three businesses or one business with three revenue streams?</li>
</ul>
""",

"payback_narrative": """
<p>The table below shows how long it would take to recover your initial investment under
different assumptions about annual owner draw. <strong>Revenue estimates are inferred from
indirect Item 19 data, not disclosed figures. These payback periods carry more uncertainty
than those in the other reports in this series.</strong></p>

<table>
<thead>
<tr>
<th>Assumed annual owner draw</th>
<th class="num">Low investment ($141K)</th>
<th class="num">Mid investment ($156K)</th>
<th class="num">High investment ($171K)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="label">$30K (mosquito-only conservative)</td>
<td class="num">4.7 years</td>
<td class="num">5.2 years</td>
<td class="num">5.7 years</td>
</tr>
<tr>
<td class="label">$55K (mosquito-only moderate)</td>
<td class="num">2.6 years</td>
<td class="num">2.8 years</td>
<td class="num">3.1 years</td>
</tr>
<tr>
<td class="label">$80K (combination franchise)</td>
<td class="num">1.8 years</td>
<td class="num">2.0 years</td>
<td class="num">2.1 years</td>
</tr>
</tbody>
</table>

<div class="callout">
<div class="callout-title">The honest frame</div>
At mosquito-only Q3 economics, payback takes 5+ years on a $141K+ investment with inferred
revenue. At the combination-franchise level ($262K revenue, $80K draw), payback is ~2 years —
but this assumes Q2 mosquito performance plus median holiday lighting participation, both of
which are estimates, not disclosed outcomes. The combination model is the bull case: if it works,
the economics are competitive. If it doesn't (you don't participate in holiday lighting, or
your market doesn't support it), you have a $141K+ mosquito franchise with the highest initial
fee and mid-tier ongoing fees. Validate the combination thesis before committing.
</div>
""",

"peer_decision_overlay": [
    {"label": "Lowest-cost entry", "brand": "Mosquito Authority",
     "rationale": "$54K–$128K. Hunters' $107K franchise fee alone exceeds most competitors' total investment low end."},
    {"label": "Lowest ongoing fee burden (established brands)", "brand": "Mosquito Authority",
     "rationale": "17–18% of revenue (2/7 in full cohort; 1st among brands with 100+ outlets). Hunters is 26.8% at $300K."},
    {"label": "Richest revenue disclosure", "brand": "Mosquito Joe",
     "rationale": "Retention rates, per-treatment pricing, tenure-segmented sales. Hunters provides building blocks but withholds total revenue."},
    {"label": "Lowest attrition at scale", "brand": "Mosquito Authority",
     "rationale": "Zero terminations in a 546-outlet system across 3 years. Hunters improved to zero in 2024 but started from 17 in 2022."},
    {"label": "Only combination franchise", "brand": "Mosquito Hunters",
     "rationale": "Mosquito + pest + holiday lighting. Only brand addressing seasonality directly. Holiday median: $54K per participating SP."},
    {"label": "Richest unit economics data", "brand": "Mosquito Squad",
     "rationale": "Per-territory quartiles + $20.8M company-owned P&L. Hunters has no revenue or cost disclosure."},
    {"label": "Lowest-friction entry profile", "brand": "Mosquito Authority",
     "rationale": "Lowest entry floor ($54K), simplest model, fee deferral option. Hunters requires the most pre-purchase diligence and the highest initial fee in the cohort. Note: low friction to enter does not predict profitability."},
],

},

}  # end BRAND_NARRATIVES

# Import cleaning cohort narratives
try:
    from cleaning_narratives import CLEANING_NARRATIVES
    BRAND_NARRATIVES.update(CLEANING_NARRATIVES)
except ImportError:
    pass

# Import lawn cohort narratives
try:
    from lawn_narratives import LAWN_NARRATIVES
    BRAND_NARRATIVES.update(LAWN_NARRATIVES)
except ImportError:
    pass


def load_brand(slug: str) -> dict:
    """Load extracted brand JSON."""
    path = DATA_EXTRACTED / f"{slug}.json"
    with open(path) as f:
        return json.load(f)


def _get_cohort_for_brand(slug: str) -> dict | None:
    """Return the cohort dict for a given brand slug."""
    registry_path = ROOT / "data" / "cohort_registry.json"
    if registry_path.exists():
        with open(registry_path) as f:
            cohorts = json.load(f)["cohorts"]
        for cohort in cohorts:
            if slug in cohort["brands"]:
                return cohort
    return None


def load_fee_model(slug: str | None = None) -> dict:
    """Load fee model output for the brand's cohort."""
    cohort = _get_cohort_for_brand(slug) if slug else None
    if cohort and cohort.get("fee_model_file"):
        path = DATA_DERIVED / cohort["fee_model_file"]
    else:
        path = DATA_DERIVED / "fee_burden_model_output.json"
    with open(path) as f:
        return json.load(f)


def build_fee_table(brand_name: str, fee_model: dict, cohort_brands: list[str] | None = None) -> list[FeeLevel]:
    """Build fee level rows for this brand with cohort ranking."""
    levels = []
    for revenue in fee_model["revenue_levels"]:
        all_at_level = [r for r in fee_model["results"] if r["gross_revenue"] == revenue]
        if cohort_brands:
            all_at_level = [r for r in all_at_level if r["brand"] in cohort_brands]
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
    item7 = data["raw"]["item_7_initial_investment"]
    items = []
    # Handle brands with market-type-specific tables (e.g., The Cleaning Authority)
    if "enterprise_market" in item7:
        market = item7["enterprise_market"]
        for li in market["line_items"]:
            items.append({
                "category": li["category"],
                "low": li["low"],
                "high": li["high"],
            })
        total_low = market["total_low"]
        total_high = market["total_high"]
    else:
        for li in item7["line_items"]:
            items.append({
                "category": li["category"],
                "low": li["low"],
                "high": li["high"],
            })
        total_low = item7["total_low"]
        total_high = item7["total_high"]
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


def build_peer_table(fee_model: dict, brands_data: dict, brand_name: str = "Mosquito Authority") -> tuple[list[str], list[dict], int]:
    """Build peer comparison table at $300K with system metrics."""
    # Build brand order and slug map dynamically from loaded brands
    slug_map = {}
    for slug, d in brands_data.items():
        slug_map[d["brand"]["brand_name"]] = slug
    brands_order = list(slug_map.keys())
    # Sort alphabetically for consistency
    brands_order.sort()

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
        years = d["raw"]["item_20_outlet_summary"]["years_reported"]
        y = years[-1]  # Use most recent year
        total = y["closed"] + (y.get("non_renewals") or 0) + (y.get("ceased_operations_other") or 0)
        start = y["total_outlets_start"]
        pct = round((total / start) * 100, 1) if start else 0
        return f"{pct}%"

    def get_investment(b: str) -> str:
        d = brands_data[slug_map[b]]
        item7 = d["raw"]["item_7_initial_investment"]
        if "enterprise_market" in item7:
            low = item7["enterprise_market"]["total_low"]
            high = item7["enterprise_market"]["total_high"]
        else:
            low = item7["total_low"]
            high = item7["total_high"]
        return f"${low // 1000}K–${high // 1000}K"

    def get_royalty(b: str) -> str:
        d = brands_data[slug_map[b]]
        r = d["raw"]["item_6_other_fees"]["royalty_rate"]
        if r.get("value") is not None:
            return f"{r['value']}%"
        elif r.get("tiers"):
            rates = [t["rate"] for t in r["tiers"] if "rate" in t]
            if rates:
                return f"{max(rates)}–{min(rates)}%"
        return "varies"

    def get_fee_at_300k(b: str) -> str:
        if b in at_300k:
            return f"${at_300k[b]['total']:,.0f}"
        return "n/a"

    def get_fee_pct(b: str) -> str:
        if b in at_300k:
            return f"{at_300k[b]['pct_of_revenue']}%"
        return "n/a"

    metrics = [
        ("System size", get_system_size),
        ("Investment range", get_investment),
        ("Fee burden at $300K", get_fee_at_300k),
        ("% of revenue", get_fee_pct),
        ("3-year net growth", get_growth),
        ("Recent attrition", get_attrition),
        ("Royalty rate", get_royalty),
    ]

    table = []
    for metric_name, fn in metrics:
        table.append({
            "metric": metric_name,
            "cells": [fn(b) for b in brands_order],
        })

    this_idx = brands_order.index(brand_name) + 1  # 1-indexed for template
    return brands_order, table, this_idx


def build_economics_scenarios(
    data: dict, fee_model: dict, brand_name: str,
    scenarios_config: list[tuple[str, int]] | None = None,
    cogs_override: float | None = None,
) -> list[EconomicsScenario]:
    """Build illustrative economics scenarios from Item 19 + fee model.

    Args:
        scenarios_config: Optional list of (label, revenue) tuples. Defaults to
            Mosquito Authority's Item 19 benchmarks if not provided.
        cogs_override: Optional COGS ratio. Defaults to 0.23 (MA company-owned P&L).
    """
    cogs_ratio = cogs_override if cogs_override is not None else 0.23

    scenarios_raw = scenarios_config or [
        ("Conservative (Year 2–3)", 97000),
        ("Moderate (Year 4+)", 193000),
        ("Mature proxy (company-owned)", 384000),
    ]

    # Get fee model results for this brand
    brand_fees = {r["gross_revenue"]: r for r in fee_model["results"] if r["brand"] == brand_name}

    scenarios = []
    for name, revenue in scenarios_raw:
        # Interpolate fees from the fee model (use closest modeled level or linear interpolation)
        if revenue <= 200000:
            fee_data = brand_fees.get(200000)
            fee_pct = fee_data["pct_of_revenue"] if fee_data else 18.3
            fees = int(revenue * fee_pct / 100)
        elif revenue <= 300000:
            low_fee = brand_fees[200000]["total"]
            high_fee = brand_fees[300000]["total"]
            ratio = (revenue - 200000) / 100000
            fees = int(low_fee + (high_fee - low_fee) * ratio)
            fee_pct = round(fees / revenue * 100, 1)
        elif revenue <= 400000:
            low_fee = brand_fees[300000]["total"]
            high_fee = brand_fees[400000]["total"]
            ratio = (revenue - 300000) / 100000
            fees = int(low_fee + (high_fee - low_fee) * ratio)
            fee_pct = round(fees / revenue * 100, 1)
        else:
            low_fee = brand_fees[400000]["total"]
            high_fee = brand_fees[500000]["total"]
            ratio = min((revenue - 400000) / 100000, 1.0)
            fees = int(low_fee + (high_fee - low_fee) * ratio)
            fee_pct = round(fees / revenue * 100, 1)

        est_cogs = int(revenue * cogs_ratio)
        remaining = revenue - fees - est_cogs

        scenarios.append(EconomicsScenario(
            name=name,
            revenue=revenue,
            franchisor_fees=fees,
            fee_pct=fee_pct,
            est_cogs=est_cogs,
            remaining=remaining,
        ))

    return scenarios


def build_fee_comparison(fee_model: dict, brand_name: str, peer_brands: list[str]) -> list[dict]:
    """Build fee burden comparison bars for cohort brands at $300K."""
    at_300k = [r for r in fee_model["results"]
               if r["gross_revenue"] == 300000 and r["brand"] in peer_brands]
    if not at_300k:
        return []

    # Sort by pct ascending (lowest burden first)
    at_300k.sort(key=lambda r: r["pct_of_revenue"])

    max_pct = max(r["pct_of_revenue"] for r in at_300k)
    bars = []
    for r in at_300k:
        bars.append({
            "brand": r["brand"],
            "pct": r["pct_of_revenue"],
            "bar_width": round(r["pct_of_revenue"] / max_pct * 100, 1),
            "is_subject": r["brand"] == brand_name,
        })
    return bars


def generate_report(slug: str) -> None:
    """Generate a Decision Report for a single brand."""
    if slug not in BRAND_NARRATIVES:
        print(f"Error: No editorial content for '{slug}'. Available: {list(BRAND_NARRATIVES.keys())}")
        sys.exit(1)

    data = load_brand(slug)
    fee_model = load_fee_model(slug)
    narratives = BRAND_NARRATIVES[slug]
    brand_name = data["brand"]["brand_name"]

    # Scope peer brands to same cohort
    cohort = _get_cohort_for_brand(slug)
    cohort_slugs = cohort["brands"] if cohort else BRAND_SLUGS
    all_brands = {s: load_brand(s) for s in cohort_slugs}
    peer_brands, peer_table, this_brand_idx = build_peer_table(fee_model, all_brands, brand_name)
    fee_table = build_fee_table(brand_name, fee_model, cohort_brands=peer_brands)
    inv_table, inv_low, inv_high = build_investment_table(data)
    health_table = build_health_table(data)
    economics_scenarios = build_economics_scenarios(
        data, fee_model, brand_name,
        scenarios_config=narratives.get("economics_scenarios_config"),
        cogs_override=narratives.get("economics_cogs_ratio"),
    )
    fee_comparison = build_fee_comparison(fee_model, brand_name, peer_brands)

    # Render
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=False)
    template = env.get_template("report-artifact.html")

    cohort_display = cohort.get("display_name", "this") if cohort else "this"

    context = {
        "brand_name": brand_name,
        "filing_year": data["filing_year"],
        "legal_entity": data["brand"]["legal_entity"],
        "cohort_display_name": cohort_display,
        "report_date": date.today().isoformat(),
        "page_count": data["source_document"]["page_count"] or "~230",
        "sha256": data["source_document"]["sha256"] or "not recorded",

        "executive_summary": narratives["executive_summary"],

        # Scorecard
        "scorecard": narratives.get("scorecard", []),
        "scorecard_posture": narratives.get("scorecard_posture", ""),

        # Buyer fit
        "buyer_fit_narrative": narratives.get("buyer_fit_narrative", ""),

        "fee_burden_narrative": narratives["fee_burden_narrative"],
        "fee_table": fee_table,
        "cohort_size": len(peer_brands),
        "fee_comparison": fee_comparison,
        "fee_burden_detail": narratives["fee_burden_detail"],
        "item19_narrative": narratives["item19_narrative"],
        "item19_triangulation": narratives.get("item19_triangulation", ""),

        # Economics
        "economics_preamble": narratives.get("economics_preamble", ""),
        "economics_scenarios": economics_scenarios,
        "economics_assumptions": narratives.get("economics_assumptions", ""),
        "economics_detail": narratives.get("economics_detail", ""),
        "payback_narrative": narratives.get("payback_narrative", ""),

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
        "peer_decision_overlay": narratives.get("peer_decision_overlay", []),
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
