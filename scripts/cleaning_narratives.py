"""
Editorial narratives for the Residential Cleaning cohort.

These are the interpretive layer that makes the report worth paying for.
They cannot be auto-generated from data alone — they are authored analysis.
"""

CLEANING_NARRATIVES: dict[str, dict] = {

"cleaning-authority": {

"executive_summary": """
<p>The Cleaning Authority is a mature, PE-backed residential cleaning franchise (Authority Brands / Apax Partners)
with 236 total outlets (233 franchised, 3 company-owned) as of year-end 2024 and one of the richest Item 19 disclosures in the cleaning cohort.
The average Enterprise territory generated $1.46M in gross revenue in fiscal year 2024, with COGS running
61–63% and average price per clean of $165–$173. The system has grown steadily — 212 to 236 units over
three years (+24 net), with 2024 the strongest year (+12). Turnover dropped to 4.1% in 2024, the lowest
in the reporting period.</p>

<p>The biggest active risk is the TCAF litigation: an independent franchisee association is suing the franchisor
over marketing fund transparency, above-market pricing for franchisor-supplied services, and alleged inhibition
of franchisee free association (Item 3, p. 15). The appeal is pending as of April 2025. Separately, confidentiality
clauses restrict current and former franchisees from speaking openly about their experience — a structural
obstacle to your due diligence. The $100,000 liquidated damages floor on termination (Item 6, p. 26) and
DHH-based Local Marketing Fee that cannot be modeled without territory-specific data add complexity to
the economic picture.</p>

<p>On balance, this is a franchise with strong disclosed revenue, a favorable royalty structure (tiered 6%/5%/4%),
and modest Brand Fund contributions (1%, capped at $200/week). But the true total fee burden is higher than
the modelable fees suggest, because the primary marketing cost — the Local Marketing Fee — is territory-size-dependent
and excluded from standard revenue-percentage comparisons. A buyer must get territory-specific Local Marketing
Fee estimates before signing.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Strong", "color": "strong",
     "summary": "Enterprise: $93K–$147K. Hometown: $77K–$120K. Mid-to-low for cleaning cohort, with Hometown offering a lower on-ramp."},
    {"dimension": "Ongoing fee burden", "rating": "Mixed", "color": "mixed",
     "summary": "Modelable fees are lowest in cohort (7.4–8.0% at $200K–$500K). But Local Marketing Fee (DHH-based, ~$10K–$20K+/yr) is excluded — true burden is materially higher."},
    {"dimension": "System stability", "rating": "Strong", "color": "strong",
     "summary": "Steady growth: +9, +3, +12 net units over 3 years. Only 1 termination in 2024. Turnover dropped from 10.6% to 4.1%."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Richest Item 19 in cleaning cohort. Per-territory gross revenue, COGS%, price per clean, customer loss rates, lead conversion, and employee counts across performance thirds."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Rich data offset by confidentiality clauses restricting franchisee speech and TCAF litigation alleging marketing fund opacity."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "TCAF lawsuit is a live red flag. $100K liquidated damages floor on termination. Local Marketing Fee is opaque and franchisor-controlled. Confidentiality restrictions hinder diligence."},
    {"dimension": "Buyer fit breadth", "rating": "Strong", "color": "strong",
     "summary": "Two market types (Enterprise/Hometown), non-seasonal recurring revenue, tiered royalty that rewards growth. Works for owner-operators and semi-absentee at scale."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "Disclosed unit economics and disclosure depth are among the strongest in the cohort, but the TCAF litigation and fee opacity demand careful diligence. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """The Cleaning Authority is the strongest disclosure story in the residential cleaning cohort
and produces genuinely large revenue per territory. The tiered royalty and low Brand Fund rate reward scale.
But the TCAF litigation, confidentiality clauses, and opaque Local Marketing Fee structure mean the franchise
agreement has more friction than the topline economics suggest. This is a franchise where the numbers look
good on paper — your job in diligence is to verify that the costs you cannot model from the FDD alone
do not erode the margin the disclosed numbers imply.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Experienced operator comfortable managing labor:</strong> With COGS at 61–63% (mostly direct labor,
payroll taxes, and workers' comp), this is a labor-intensive business. The top third of Enterprise territories
employ an estimated 45 cleaning staff per territory. You are running a workforce, not performing the service yourself.</li>
<li><strong>Buyer seeking recurring, non-seasonal revenue:</strong> Unlike mosquito control, residential cleaning
generates year-round income. Average weekly customer loss of 0.76–1.12% means retention is a treadmill, but
the revenue base does not disappear in winter.</li>
<li><strong>Growth-oriented buyer who will benefit from tiered royalty:</strong> The 6%/5%/4% marginal structure
means your effective royalty rate drops as revenue climbs. An Enterprise territory at $1.46M average revenue
pays a blended ~4.8% royalty — well below the 6–7% flat rates common in the cohort.</li>
<li><strong>Buyer with $120K–$150K liquid capital (Enterprise):</strong> The midpoint Enterprise investment
is ~$120K. Hometown offers a lower entry at ~$98K midpoint, but Item 19 data covers Enterprise only —
Hometown economics are unverified in the FDD.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Solo owner-operator expecting to clean houses yourself:</strong> This is designed as a
manager-led operation with cleaning teams. The Item 7 includes a Full Time Manager line item ($0–$13,750).
If you want to be the one cleaning, this model is not built for that.</li>
<li><strong>Buyer uncomfortable with opaque fee structures:</strong> The Local Marketing Fee is DHH-based,
paid to the franchisor (who is the sole approved supplier), and cannot be calculated without territory-specific
data. If you need full cost transparency before signing, this structure will frustrate you.</li>
<li><strong>Buyer in a small market (sub-15,000 DHH):</strong> Hometown Market is the minimum at 15,000 DHH.
Below that, you do not qualify. And the 12 Hometown territories are excluded from Item 19 entirely —
you have no disclosed revenue benchmarks for Hometown operations.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have obtained a territory-specific Local Marketing Fee estimate for your proposed territory and
incorporated it into your financial model. The FDD does not give you a dollar amount — you must ask.</li>
<li>You have read the TCAF lawsuit filing and understand the allegations. Regardless of outcome,
the claims about marketing fund opacity and above-market pricing are specific enough to investigate.</li>
<li>You have talked to current franchisees about their actual total fee burden — not just the
modelable components. The confidentiality clauses may limit what they share, which is itself a signal.</li>
</ul>
""",

"fee_burden_narrative": """
<p>The Cleaning Authority's modelable fees (royalty + Brand Fund + technology) are the lowest in the cleaning
cohort at every revenue level — 7.4% to 8.0% of revenue from $200K to $500K. But this figure is misleadingly
low because it excludes the Local Marketing Fee, which is the primary ongoing marketing cost and is paid
directly to the franchisor. The fee is calculated per Designated Household in your territory, not as a
percentage of revenue, making it impossible to model without territory-specific data.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (6%/5%/4% tiered):</strong> Marginal brackets like income tax. Enterprise: 6% on first
$600K, 5% on $600K–$1.3M, 4% above $1.3M. At the system average of $1.46M, blended effective rate is ~4.8%.
This is the most franchisee-friendly royalty structure in the cleaning cohort. Hometown thresholds are lower
($300K/$550K). Rate reverts to 6% each January 1. Reduced rates void if not in compliance. (p. 19)</li>
<li><strong>Brand Fund (1%, capped at $200/week):</strong> Modest. At $500K revenue, 1% = $5,000/yr, well
below the $10,400 annual cap. Can only be increased above 1% with consent of 50%+ of franchisees. This is
one of the lowest national marketing contributions in the cohort. (p. 19)</li>
<li><strong>Technology ($36.58/week, rising to $40.24):</strong> $1,902/yr currently, increasing to $2,092/yr
in July 2025. Covers TCA IQ software. Lower than most competitors ($5,500–$10,900/yr in this cohort).
Franchisor reserves right to increase annually. (p. 21)</li>
<li><strong>Local Marketing Fee (DHH-based — NOT modeled):</strong> Currently $0.374 per DHH times a percentage
(9–13%) of territory DHH, depending on customer count. For a 40,000 DHH Enterprise territory at the 11%
tier: $0.374 × 4,400 = $1,646/week = $85,580/year. This is a rough illustration — your actual number depends
on territory size and customer count. The fee is paid to the franchisor, who is the sole approved supplier
of the Local Marketing Program. Anticipated increase to $0.389 in 2025, with up to 4% cumulative annual
increases allowed. (pp. 19–20, 26–27)</li>
</ul>

<div class="callout">
<div class="callout-title">The fee structure you cannot see from the FDD alone</div>
At $500K revenue, the modelable fees total $36,902 (7.4%). But if the Local Marketing Fee runs $40K–$85K
(plausible range depending on territory size), the true total fee burden is $77K–$122K — or 15–24% of
revenue. This would place The Cleaning Authority anywhere from competitive to expensive relative to peers,
depending entirely on your territory's DHH count. The TCAF lawsuit specifically alleges above-market pricing
for these franchisor-supplied marketing services. Until you have your territory-specific number, you cannot
make an informed fee comparison.
</div>

<div class="implication">
<strong>What this means:</strong> The royalty and Brand Fund are genuinely favorable. The technology fee is low.
But the Local Marketing Fee is the elephant in the room — it could easily be 2–5× larger than all other
fees combined, and it is controlled by the franchisor with limited franchisee visibility into how the money
is spent (per TCAF's allegations). Your diligence must focus on this single fee above all others.
</div>
""",

"item19_narrative": """
<p>The Cleaning Authority provides the richest Item 19 in the residential cleaning cohort. Table 1 reports
per-territory gross revenue, COGS percentages, average price per clean, customer loss rates, lead conversion
metrics, and employee counts — broken into performance thirds for 206 Enterprise Market territories that
operated the full fiscal year 2024. (pp. 71–73)</p>

<h3>Revenue by performance third (Enterprise Market, FY 2024)</h3>
<ul>
<li><strong>Top Third (69 territories):</strong> Average $2.45M, median $2.26M. Range: $1.65M–$5.10M.</li>
<li><strong>Middle Third (68 territories):</strong> Average $1.29M, median $1.26M. Range: $976K–$1.64M.</li>
<li><strong>Lower Third (69 territories):</strong> Average $638K, median $692K. Range: $121K–$973K.</li>
<li><strong>System average (206 territories):</strong> $1,457,906.</li>
</ul>

<p>These are large numbers by franchise standards. The system generated $300.3M in total gross revenue across
206 reporting Enterprise territories. Even the lower third averages $638K — though the range extends down
to $121K, suggesting at least some territories are struggling or early-stage.</p>

<h3>Operational metrics worth noting</h3>
<ul>
<li><strong>Average price per clean:</strong> Remarkably consistent across thirds ($165–$173). Pricing power
does not appear to drive the revenue spread — volume (number of cleans) does.</li>
<li><strong>COGS:</strong> 61% for top and middle thirds, 63% for lower third. The 2-point spread suggests
lower-revenue territories have slightly less labor efficiency or cost discipline.</li>
<li><strong>Weekly customer loss rate:</strong> 0.76% (top), 0.86% (middle), 1.12% (lower). Annualized,
the lower third loses roughly 44% of its customer base per year — a brutal retention treadmill that demands
constant lead generation to maintain revenue.</li>
<li><strong>Lead-to-appointment conversion:</strong> 41% across top and middle thirds, 44% for lower third.
Conversion rates are consistent; the difference is lead volume, not conversion efficiency.</li>
</ul>

<h3>What's missing</h3>
<ul>
<li><strong>Hometown Market data:</strong> The 12 Hometown territories are excluded entirely from Item 19.
If you are considering a Hometown territory, you have zero disclosed revenue benchmarks.</li>
<li><strong>Net income or profit:</strong> COGS is disclosed but overhead costs (rent, manager salary, admin,
Local Marketing Fee) are not included in COGS. The FDD footnotes that COGS excludes advertising, Local
Marketing Fees, rent ($1,200–$2,000/mo), phone/internet ($250–$350/mo), manager salaries, owner draws, and
employee recruitment advertising ($300–$500/mo). (p. 73)</li>
<li><strong>Survivorship bias:</strong> 3 territories that closed during 2024 and 15 that opened during
2024 are excluded. The closed territories' revenue is not reflected in the averages.</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross revenue to owner economics</h3>
<p>The Item 19 gives you revenue and COGS — but not profitability. Here is what we can reconstruct
from the disclosed data and footnotes:</p>

<p><strong>For a middle-third Enterprise territory ($1.29M revenue):</strong></p>
<ul>
<li>COGS at 61%: ~$787K (includes direct labor, payroll taxes, workers' comp, GL insurance, cleaning supplies, mileage, and Royalty Fees — note royalty is embedded in COGS)</li>
<li>Gross margin after COGS: ~$503K (39%)</li>
<li>Estimated overhead from footnotes: rent ($14K–$24K), phone/internet ($3K–$4K), manager salary ($40K–$60K+), employee recruitment ($3,600–$6,000), Local Marketing Fee (unknown, likely $40K–$85K+)</li>
<li>Estimated overhead range: $101K–$179K</li>
<li>Implied pre-tax owner income: $324K–$402K before Local Marketing Fee, or $239K–$362K after estimated Local Marketing Fee range</li>
</ul>

<p>For a <strong>lower-third Enterprise territory ($638K revenue)</strong>, the math tightens considerably:</p>
<ul>
<li>COGS at 63%: ~$402K</li>
<li>Gross margin: ~$236K</li>
<li>After estimated overhead ($90K–$160K): $76K–$146K implied pre-tax owner income</li>
</ul>

<div class="implication">
<strong>What this means:</strong> The top two-thirds of Enterprise territories appear to generate meaningful
owner income even after estimated overhead — potentially $150K–$350K+ for a mature, well-run operation.
The lower third is tighter but still appears viable. The critical unknown is the Local Marketing Fee,
which could represent $40K–$85K+ of the overhead estimate. Until you pin down that number for your
specific territory, these triangulations have a wide confidence interval.
</div>

<div class="callout">
<div class="callout-title">Royalty is inside COGS</div>
An important detail: the FDD states that COGS includes Royalty Fees (p. 73). This means the 61–63% COGS
figure already accounts for the 6%/5%/4% royalty. When building your own financial model, do not
double-count the royalty as both a COGS component and a separate fee line item.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using The Cleaning Authority's
disclosed Item 19 revenue and COGS data for Enterprise Market territories. The FDD does not disclose
net franchisee profitability. COGS (61–63%) includes royalty fees but excludes rent, manager salary,
Local Marketing Fee, and other overhead. Your actual results depend on your territory, labor market,
customer acquisition costs, and execution. Hometown Market territories have no disclosed benchmarks.</p>
""",

"economics_scenarios_config": [
    ("Lower Third average", 638000),
    ("Middle Third average", 1288000),
    ("Top Third average", 2446000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue from Item 19 Table 1 Enterprise Market performance thirds (FY 2024, 206 territories). COGS at 55% (adjusted from disclosed 61% to remove the royalty component, which the FDD includes in COGS per footnotes p. 73 but which is separately modeled in the franchisor fee column). The disclosed 61% includes direct labor, payroll taxes, workers' comp, insurance, supplies, mileage, and Royalty Fees. Using 61% in the COGS column while also subtracting royalty in the fee column would double-count royalty. The 55% figure approximates COGS-excluding-royalty at modeled revenue levels (effective blended royalty of ~5–6%). COGS still excludes: rent, manager salary, Local Marketing Fee, phone/internet, employee recruitment advertising, and owner draw. 'Remaining' must cover all of those excluded overhead items plus personal taxes.",

"investment_narrative": """
<p>Two investment tiers: Enterprise Market ($92,850–$147,100) and Hometown Market ($76,600–$119,599).
The spread is driven primarily by Territory Fee (based on DHH count), whether you hire a full-time
manager at launch ($0–$13,750), and office rent. The franchise fee itself is fixed: $20,000 Enterprise,
$15,000 Hometown. Multiple discount programs exist: 30% for existing franchisees, 30% for military/VetFran,
$5,000 off for diversity or first responders. (pp. 16–18, 28–29)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Territory Fee ($22,500–$45,000 Enterprise / $11,250–$22,499 Hometown):</strong> Calculated at $0.75
per Designated Household in your territory. This is a variable cost driven by territory size — a 30,000 DHH
Enterprise territory costs $22,500; a 60,000 DHH territory costs $45,000. Unlike most franchise fees, you are
paying for territory size, not just the brand license. (pp. 16–17)</li>
<li><strong>Franchise Fee ($20,000 Enterprise / $15,000 Hometown):</strong> Fixed, nonrefundable, due at signing.
Combined with Territory Fee, total initial fees ranged from $7,500 to $64,107 in fiscal year 2024. (p. 16)</li>
<li><strong>Additional Funds — 3 months ($27,000–$30,000):</strong> Covers incorporation, internet, recruitment,
employee wages (excluding owner and manager salary), and advertising for first 3 months. Does not include
royalty fees. This is the single largest line item and is estimated, not fixed. (p. 28)</li>
<li><strong>Full Time Manager ($0–$13,750):</strong> Three months' salary if you hire a manager at launch.
Zero if the owner operates. This is a meaningful swing factor — and a key decision about your operating
model from day one. (p. 28)</li>
<li><strong>Office space ($6,000–$12,000):</strong> Three months' rent plus security deposit. Enterprise assumes
800–1,200 sq ft; Hometown 700–1,100 sq ft. You need a physical location for equipment storage, laundry,
and crew staging. (pp. 28–29)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> An owner-operator taking the smallest Enterprise territory (30,000 DHH)
with existing equipment can enter near the low end (~$93K). A buyer taking a large Enterprise territory
with a hired manager is closer to $147K. The Hometown tier offers a genuine lower on-ramp ($77K–$120K) —
but with no Item 19 data to validate the economics. Discount programs can reduce the Territory + Franchise
Fee by 30%, saving $12K–$20K at the Enterprise level.
</div>
""",

"system_health_narrative": """
<p>Steady, accelerating growth. The system added 24 net total units over three years (212 to 236 total; 233 franchised), with 2024 the
strongest year at +12. Terminations are minimal: 3 in 2022, 4 in 2023, and just 1 in 2024. Ceased operations
followed a similar pattern: 0, 6, 3. The 2024 numbers — 16 openings against just 4 departures (1 termination,
3 ceased) — represent the healthiest year in the reporting period. Eleven franchise agreements were signed
but not yet opened as of year-end 2024, suggesting the pipeline remains active. (pp. 75–82)</p>
""",

"system_health_detail": """
<h3>Turnover trend</h3>
<p>Turnover rate (terminations + non-renewals + reacquisitions + ceased operations + transfers, divided by
start-of-year franchised count): 6.7% (2022), 10.6% (2023), 4.1% (2024). The 2023 spike was driven by 6
ceased operations and 13 transfers; 2024 saw both metrics improve sharply. Zero non-renewals across all
three years. (pp. 75, 78, 81)</p>

<h3>Transfer activity</h3>
<p>11 transfers (2022), 13 (2023), 5 (2024). The decline in 2024 transfers is ambiguous — it could mean
fewer owners wanting to sell (positive) or fewer buyers interested (negative). At 5 transfers out of 221
start-of-year units, the 2024 rate is just 2.3% — low by industry standards.</p>

<h3>Geography of closures</h3>
<p>Ceased operations cluster in coastal/high-cost states: California (2 across 2023–2024), Florida (1),
New Jersey (2), Oregon (1), Washington (1). This could reflect labor cost pressure in those markets or
unrelated individual circumstances. The Midwest and South, where most growth occurred (Florida +3, Texas +3,
Alabama +1, Georgia +1 in 2024), appear healthier.</p>

<div class="implication">
<strong>What this means:</strong> This is a system that is growing modestly and losing very few units.
The 2024 acceleration (+12 net) with minimal departures is a positive signal. But the system is also
not growing fast — 236 total units after nearly 30 years of franchising (since 1996) suggests organic,
steady-state growth rather than aggressive expansion. For a buyer, this means less risk of oversaturation
but also less network effect momentum than a rapidly expanding system.
</div>

<h3>Company-owned outlets</h3>
<p>Three company-owned outlets, all in Maryland, unchanged across the entire reporting period. The franchisor
is not competing with its franchisees and is not acquiring or flipping territories.</p>
""",

"risk_narrative": """
<h3>TCAF litigation — the headline risk</h3>
<p>The Independent Association of Cleaning Authority Franchisees (TCAF) filed suit in October 2023 in
Howard County, Maryland, alleging: (1) inadequate disclosure of TCAF contact info in the FDD; (2) inhibition
of franchisee association; (3) denial of marketing revenue and expenditure information; (4) above-market rates
for franchisor-supplied marketing and services; and (5) failure to use marketing funds for franchisee benefit.
The court dismissed TCAF's representative claims, holding they must proceed as individual arbitrations.
TCAF appealed; oral arguments were held April 3, 2025. The case is pending. (p. 15)</p>

<p>Regardless of the legal outcome, the allegations are specific and substantive. An independent franchisee
association does not form and file suit lightly — it signals organized dissatisfaction among a meaningful
subset of the franchise base. The marketing fund transparency claims are directly relevant to the Local
Marketing Fee that dominates franchisee cost structure. A prospective buyer should independently investigate
these claims during diligence.</p>

<h3>Confidentiality clauses</h3>
<p>The FDD discloses that "during the last three fiscal years, current and former franchisees have signed
confidentiality clauses and provisions restricting their ability to speak openly about their experience."
This is not unique to TCA — but combined with the TCAF litigation over free association rights, it creates
a chilling effect on your ability to gather candid franchisee feedback during diligence. If franchisees
you contact seem guarded or unwilling to discuss economics, this is likely why.</p>

<h3>$100,000 liquidated damages floor</h3>
<p>If the franchisor terminates your agreement for default, you owe the greater of (i) two years of Royalty
Fees (average per period × number of periods in 2 years) or (ii) $100,000. For a territory generating
$1.3M in revenue at ~5% blended royalty, two years of royalty is ~$130K — so the $100K floor is a binding
constraint mainly for smaller or newer territories. This is a significant termination penalty that limits
your downside options. (p. 26)</p>

<h3>SPV entity structure</h3>
<p>The franchisor is The Cleaning Authority Franchising SPE LLC — a special purpose entity within the
Authority Brands / Apax Partners securitization chain. All franchise agreements were transferred to the SPE
in May 2021. This is a PE-standard structure that may affect your legal recourse in a dispute — you are
contracting with a ring-fenced entity, not with Authority Brands directly. The Cleaning Authority is a
sister brand to Mosquito Squad under the Authority Brands umbrella. (p. 6)</p>

<h3>Cavallaro litigation</h3>
<p>The Cleaning Authority sued a former franchisee (Mike Cavallaro) for breach of agreement and post-term
non-compete violation. The franchisee counterclaimed alleging misrepresentations that induced him to sign
the franchise agreement. Summary judgment motions were under submission as of December 2024. While a single
case, the misrepresentation counterclaim is worth noting — it suggests at least one franchisee felt the
pre-sale representations did not match reality. (p. 15)</p>
""",

"peer_narrative": """
<p>The Cleaning Authority stands out in the residential cleaning cohort for revenue scale: the $1.46M average
Enterprise territory dwarfs what most cleaning franchise brands disclose (or can claim). The tiered royalty
that drops to 4% above $1.3M rewards that scale. Among the seven brands in this cohort, TCA has the lowest
modelable ongoing fee burden — but the asterisk on that claim is enormous, because the Local Marketing Fee
that dominates real-world costs is not revenue-based and cannot be compared apples-to-apples.</p>

<p><strong>Closest comparison: Molly Maid.</strong> Similar PE-backed structure (Neighborly / KKR), similar
system size. Molly Maid charges a flat 6.5% royalty plus 2% MAP — simpler and more predictable. But Molly
Maid's Item 19 reports average cleans per territory rather than dollar revenue, making direct revenue
comparison difficult. TCA's disclosure is significantly richer.</p>

<p><strong>Sharpest contrast: Two Maids & A Mop.</strong> Highest total fee burden in the cohort (27.9% at
$200K) due to $2,500/month mandatory local advertising plus 7% base royalty. TCA's modelable burden at the
same revenue is 8.0%. Even after adding an estimated Local Marketing Fee, TCA is almost certainly cheaper
to operate. But Two Maids has no confidentiality clauses and no franchisee lawsuit — sometimes simpler
structures come with less friction.</p>

<p><strong>Worth noting: MaidPro</strong> offers the simplest fee structure (6% royalty + 2% Brand Fund +
$500/mo tech = 9.2% at $500K) with no DHH-based complications. If fee transparency is a priority and
you are willing to accept a simpler system with less disclosed performance data, MaidPro is the cleaner
alternative — literally and figuratively.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "What is the actual Local Marketing Fee for the specific territory I am considering, expressed as a weekly and annual dollar amount?",
        "context": "Item 6, pp. 19–20, 26–27. Fee is $0.374/DHH × a percentage (9–13%) of territory DHH based on customer count. Cannot be calculated from the FDD without territory-specific data.",
        "follow_ups": ["Ask what customer count threshold triggers each percentage tier (9%, 10%, 11%, 12%, 13%).", "Ask what the fee was for the previous franchisee in this territory.", "Ask for a 3-year history of rate increases on this fee."],
    },
    {
        "question": "The TCAF lawsuit alleges above-market rates for franchisor-supplied marketing services and failure to use marketing funds for franchisee benefit. How do you respond to those specific allegations?",
        "context": "Item 3, p. 15. TCAF v. The Cleaning Authority, filed October 2023. Appeal pending after court dismissed representative claims.",
        "follow_ups": ["Ask whether the franchisor provides franchisees with an annual accounting of Local Marketing Fee expenditures.", "Ask if you can review a sample marketing report showing how funds were spent.", "Ask how many franchisees are TCAF members."],
    },
    {
        "question": "The FDD notes that current and former franchisees have signed confidentiality clauses restricting their ability to speak openly. What specifically can and cannot a current franchisee share with me during my diligence?",
        "context": "FDD metadata warnings. Confidentiality provisions disclosed as applying during last three fiscal years.",
        "follow_ups": ["Ask for a copy of the confidentiality provision so your attorney can review its scope.", "Ask if the franchisor will provide a list of franchisees willing to speak with prospective buyers without restriction."],
    },
    {
        "question": "Item 19 covers only Enterprise Market territories. What does revenue look like for the 12 Hometown Market territories?",
        "context": "Item 19 Table 1 explicitly excludes 12 Hometown territories. pp. 71–73.",
        "follow_ups": ["Ask for the average and median gross revenue for Hometown territories.", "Ask how many of the 12 Hometown franchisees have been operating for 2+ years.", "Ask if any Hometown territories have converted to Enterprise."],
    },
    {
        "question": "The lower third of Enterprise territories has a 1.12% weekly customer loss rate — annualized, that is roughly 44% customer churn. What support do you provide to territories with high attrition?",
        "context": "Item 19 Table 1, lower third metrics. 69 territories averaging $638K revenue. p. 72.",
        "follow_ups": ["Ask what percentage of lower-third territories were in the lower third the prior year.", "Ask what the most common driver of customer loss is — price, service quality, or competition."],
    },
    {
        "question": "The liquidated damages clause sets a floor of $100,000 upon franchisor-initiated termination. Under what circumstances has this been enforced in the last 5 years, and what was the average amount collected?",
        "context": "Item 6, p. 26. Greater of 2 years' royalty or $100K.",
        "follow_ups": ["Ask how many of the terminations in the 2022–2024 period resulted in liquidated damages collection.", "Ask if the $100K has ever been negotiated down in a settlement."],
    },
    {
        "question": "COGS in Item 19 includes Royalty Fees. Can you provide a breakout of COGS components — specifically, what percentage is direct labor vs. royalty vs. supplies vs. insurance?",
        "context": "Item 19 footnotes, p. 73. COGS includes direct labor, payroll taxes, workers' comp, GL insurance, cleaning supplies, mileage, and Royalty Fees.",
        "follow_ups": ["If they provide a breakout, calculate labor as a percentage of revenue independently.", "Ask what the average hourly wage for cleaning staff is across the system."],
    },
    {
        "question": "Authority Brands also owns Mosquito Squad. Are there any shared services, cross-selling arrangements, or combined territory requirements between the two brands?",
        "context": "Parent company is Authority Brands, Inc. / Apax Partners. Mosquito Squad is a sister brand.",
        "follow_ups": ["Ask whether existing TCA franchisees have been offered or required to take on Mosquito Squad territories.", "Ask if there are shared technology platforms or marketing programs across the Authority Brands portfolio."],
    },
],

},

"two-maids": {

"executive_summary": """
<p>Two Maids & A Mop is the fastest-growing residential cleaning franchise in this cohort,
expanding from 92 to 144 outlets over three years (+56.5%). It is backed by JM Family
Enterprises — a family-office holding company, not private equity — making it an outlier
in a cohort where PE ownership is the norm. The brand discloses an unusually rich Item 19:
12 charts covering gross revenue, cost of sales, gross margins, web leads, conversion rates,
recurring customer percentages, and pricing — broken out by quintile, territory age, household
count, and multi-unit ownership.</p>

<p>The core tension is between strong top-line data and a heavy fee structure. At $300K gross
revenue, annual franchisor fees total $64,800 (21.6% of revenue) — the highest in the cleaning
cohort except for The Maids. The primary driver is the $2,500/month Local Advertising Services
Program Fee, which is franchisor-directed and non-negotiable. Combined with a $650/month
technology fee and a tiered royalty starting at 7%, the fixed-cost floor is substantial.
A franchise doing $300K/year sends roughly $5,400/month to the franchisor before paying
a single employee.</p>

<p>The upside case is real: median-quintile territories (Q3) generate ~$495K in gross revenue
with 54% gross margins (p.&nbsp;52), and the recurring customer rate runs 79–83% across all
mature quintiles. The system's growth trajectory is accelerating (12 &rarr; 24 &rarr; 32 openings per year)
with minimal closures (4–6/year). Litigation is effectively clean. But the fee burden means
the gap between gross margin and owner take-home is wider here than at most peers.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$93K–$150K total investment. Mid-cohort. In-house financing available for franchise and territory fees, which lowers cash-at-signing."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "Highest in cohort at every modeled revenue level. 21.6% of revenue at $300K, driven by $2,500/mo franchisor-directed local ad spend + $650/mo tech fee."},
    {"dimension": "System stability", "rating": "Strong", "color": "strong",
     "summary": "Fastest growth in cohort (+56.5% over 3 years). Only 4–6 exits/year against 100+ outlets. Turnover under 5.1%."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "12-chart Item 19 with gross margin data by quintile. Includes cost of sales, lead metrics, pricing, and recurring rates. Best disclosure depth in cleaning cohort."},
    {"dimension": "Disclosure quality", "rating": "Strong", "color": "strong",
     "summary": "Clean filing. Minor OCR artifacts in Table 3 footnotes but all values cross-verified. No formula errors or population mismatches."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Fee burden is the primary risk. Local ad fee is franchisor-directed and subject to change. Transfer fees ($25K–$50K) create exit friction. No material litigation risk."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Strong for operators targeting $400K+ revenue who value franchisor-managed marketing. Weaker for budget-sensitive buyers or those wanting marketing control."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "Richest disclosure and fastest growth in cohort, but the highest fee burden at lower revenue levels. The fee structure rewards scale — economics improve materially above $500K where royalty tiers and fixed costs dilute. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """Two Maids has the deepest operational disclosure in the residential cleaning
cohort and the fastest-growing system by a wide margin. The 12-chart Item 19 gives a buyer
more data to work with than any competitor. The trade-off is a heavy fee structure that takes
a larger share of revenue than most peers — particularly at lower revenue levels where the
$2,500/month local advertising fee and $650/month technology fee are most punitive as a
percentage of gross. The economics work best for operators who can push past $500K in gross
revenue, where the tiered royalty starts to reward scale and the fixed fees dilute. Buyers
who are cost-sensitive or want to control their own marketing spend will find the fee
structure less favorable than lower-burden alternatives in this cohort.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Operator targeting $400K+ revenue:</strong> The fee structure is regressive at
low revenue — the $30K+/year in fixed local advertising and technology fees hit hardest
below $300K. Above $400K, these fixed costs dilute to a manageable percentage and the
tiered royalty (dropping from 7% to 6% and 5%) starts to reward growth.</li>
<li><strong>Buyer who wants franchisor-managed marketing:</strong> Two Maids runs your
local digital advertising for you. If you view $2,500/month as buying a managed marketing
service rather than a tax, the model works. Web leads average 157–238/month for mature
territories (pp.&nbsp;50–54), suggesting the spend generates activity.</li>
<li><strong>Multi-unit operator:</strong> Chart 12 shows 20 multi-unit owners averaging
$1.69M gross revenue across ~2.85 territories each. At that scale, the fee structure's
regressiveness disappears. The simultaneous-territory discount ($30K vs $40K for additional
territories) and in-house financing support multi-unit expansion.</li>
<li><strong>Conversion franchise buyer:</strong> Existing cleaning business owners can convert
with up to $10K off the territory fee and bring their customer base. The recurring customer
rate (79–83%) suggests the model supports customer retention through branding transition.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive first-time buyer:</strong> Between the $60K franchise/territory
fee, $9K in startup advertising, and $3K/month in local ad spend from day one, cash burn
in the first year is significant. Year 1–2 territories average only $275K revenue with 46%
gross margin (p.&nbsp;60) — the math is tight.</li>
<li><strong>Buyer who wants marketing control:</strong> The Local Advertising Services Program
Fee is franchisor-directed. You pay $2,500–$3,000/month and they decide where it goes. The
franchisor retains up to 10% as a management fee. If you have strong local marketing skills
and want to allocate your own spend, this structure will frustrate you.</li>
<li><strong>Buyer planning to exit in 3–5 years:</strong> Transfer fees of $24,950–$50,000
(plus a potential $15,000 referral fee if the buyer was already in the franchisor's database)
create meaningful exit friction. At a $200K sale price, you could pay $50K+ in transfer-related
fees — 25% of the transaction.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have modeled your personal cash flow through the first 18 months, including the
$3,000/month local ad fee, $650/month tech fee, and 7% royalty — all of which start
before revenue ramps.</li>
<li>You have spoken to at least 3 franchisees in different quintiles (not just top performers)
about whether the franchisor-directed local advertising generates leads proportional to cost.</li>
<li>You understand the transfer fee structure and have a realistic exit scenario that accounts
for $25K–$65K in transfer-related costs.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Two Maids has the highest ongoing fee burden in the residential cleaning cohort at every
modeled revenue level. The primary driver is the franchisor-directed Local Advertising
Services Program Fee: $2,500/month ($30,000/year) on top of a 2% national advertising
fund, a 7%-to-4% tiered royalty, and a $650/month technology fee. At $300K revenue,
total franchisor fees reach $64,800 — 21.6% of gross. At $200K, the burden spikes to
27.9% because the fixed-dollar components ($37,800/year in local ad + tech fees) do not
scale down with revenue.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (7%&rarr;4% marginal monthly tiers):</strong> 7% on first $30K/month, 6%
on $30K–$60K, 5% on $60K–$90K, 4% above $90K. Minimums: $500/month Year 1, $1,500/month
thereafter. Most single-territory operators will pay effectively 7% — you need
$30K+/month ($360K+/year) before the first tier break even begins to apply. (pp.&nbsp;15, 19–20)</li>
<li><strong>National Advertising Fund (2% of Gross Revenue):</strong> Floor of $250/month Year 1,
$500/month thereafter. Straightforward. (p.&nbsp;15)</li>
<li><strong>Local Advertising Services Program Fee ($2,500–$3,000/month):</strong> $3,000/month
during first 6 months, then $2,500/month ongoing. Franchisor-directed digital advertising —
you do not control the spend. Franchisor retains up to 10% as a management fee (currently
greater of $300 or 10% of monthly spend). This is $30,000–$36,000/year in mandatory,
non-discretionary marketing cost. (pp.&nbsp;15–16)</li>
<li><strong>Technology fee ($650/month):</strong> Per territory. Among the highest fixed
technology fees in the cleaning cohort. Covers franchisor technology platforms. May increase
based on actual costs. (p.&nbsp;16)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, you retain ~$235K after franchisor fees.
At MaidPro (the lowest-burden brand at that level), you'd keep ~$270K — a $35,000/year
difference. Over a 10-year franchise term, that's $350,000 in additional fees paid. The
question is whether Two Maids' managed marketing infrastructure and brand momentum justify
the premium. The lead generation data in Item 19 (157–238 web leads/month for mature
territories) provides partial evidence — but you need to validate conversion quality
with current franchisees.
</div>

<div class="callout">
<div class="callout-title">Fee structure rewards scale</div>
The royalty tiers are genuinely progressive — at $90K+/month ($1.08M+/year), marginal
royalty drops to 4%. But the math is more interesting at modest scale: a territory doing
$500K/year pays an effective blended royalty of ~6.7%, while a $200K territory pays the
full 7%. The local ad and tech fees ($37,800/year combined) represent 18.9% of revenue
at $200K but only 7.6% at $500K. Two Maids is designed for operators who grow past $400K.
Below that, the fee structure is punitive relative to peers.
</div>
""",

"item19_narrative": """
<p>Two Maids discloses the most detailed Item 19 in the residential cleaning cohort: 12 charts
covering 147 franchised locations as of December 31, 2024. The disclosure includes gross
revenue, direct labor, cleaning materials, cost of sales, gross margin, web leads per month,
lead conversion rates, recurring customer percentages, and average pricing — broken out by
revenue quintile, territory age, household count, and multi-unit ownership. No other cleaning
brand in this cohort provides this level of operational transparency.</p>

<h3>Mature territories (2+ years) by revenue quintile</h3>
<p>86 territories open 2 or more years, ranked by Gross Revenue and split into quintiles
(pp.&nbsp;50–54):</p>
<ul class="compact">
<li><strong>Q1 (top 17):</strong> Average $1.17M, median $1.12M, 52% gross margin.
238 web leads/month, 13% conversion, 82% recurring. (p.&nbsp;50)</li>
<li><strong>Q2 (next 17):</strong> Average $653K, median $625K, 53% gross margin.
192 leads/month, 16% conversion, 80% recurring. (p.&nbsp;51)</li>
<li><strong>Q3 (middle 17):</strong> Average $495K, median $486K, 54% gross margin.
157 leads/month, 13% conversion, 83% recurring. (p.&nbsp;52)</li>
<li><strong>Q4 (next 17):</strong> Average $377K, median $374K, 54% gross margin.
165 leads/month, 12% conversion, 79% recurring. (p.&nbsp;53)</li>
<li><strong>Q5 (bottom 18):</strong> Average $230K, median $235K, 57% gross margin.
105 leads/month, 13% conversion, 79% recurring. Low of $20K suggests at least one
near-inactive territory. (p.&nbsp;54)</li>
</ul>

<p>The weighted average across all five quintiles is approximately $584K in gross revenue
with ~53% gross margin. The inverse relationship between revenue and gross margin percentage
is notable — bottom-quintile territories show 57% margin vs 52% at the top. This is because
direct labor does not scale linearly: higher-revenue territories run more crews with slightly
lower utilization per dollar of revenue.</p>

<h3>New territories (1–2 years open)</h3>
<p>17 territories open 12–24 months: average $275K, median $262K, 46% gross margin.
Recurring rate 76%, lower than mature territories. (p.&nbsp;60)</p>
<p>The 46% gross margin for new territories vs 53% for mature territories reflects ramp-up
inefficiency — new operations carry relatively higher labor costs per dollar of revenue
as they build route density. This 7-percentage-point gap narrows as the business matures.</p>

<h3>What's disclosed vs what's missing</h3>
<p>Two Maids provides <em>gross</em> margin — revenue minus direct labor and cleaning
materials. It does <strong>not</strong> include owner salary, rent, utilities, insurance,
vehicle costs, royalties, advertising fees, technology fees, or any other SG&amp;A.
The disclosed 53% gross margin does not mean 53% profit. After franchisor fees alone
(~16–22% of revenue depending on scale), the remaining margin for all other operating
costs and owner income is roughly 31–37% of gross revenue.</p>
""",

"item19_triangulation": """
<h3>Gross-to-net margin triangulation</h3>
<p>The Item 19 gives gross margin only. To estimate what a franchisee actually keeps, we need
to layer in franchisor fees and operating costs:</p>

<p><strong>At Q3 median revenue ($486K):</strong></p>
<ul class="compact">
<li>Gross margin: 54% = ~$262K</li>
<li>Less franchisor fees (royalty + national ad + local ad + tech): ~$76K (from fee burden model at $500K)</li>
<li>Remaining for rent, insurance, vehicle, office, supplies, owner draw: ~$186K</li>
</ul>

<p><strong>At Q5 average revenue ($230K):</strong></p>
<ul class="compact">
<li>Gross margin: 57% = ~$131K</li>
<li>Less franchisor fees: ~$56K (from fee burden model at $200K)</li>
<li>Remaining for all other costs and owner draw: ~$75K</li>
</ul>

<p>The gap is dramatic. A median Q3 territory has $186K to cover overhead and pay the owner.
A Q5 territory has $75K — and must still cover rent (~$18K–$24K), insurance (~$3K–$5K),
vehicle/fuel (~$6K–$10K), and miscellaneous office/supply costs (~$5K–$8K) before
the owner takes any draw. At Q5 revenue, an owner-operator might net $30K–$40K before
taxes. At Q3 revenue, the owner draw plausibly reaches $100K–$130K.</p>

<div class="implication">
<strong>What this means:</strong> The Item 19 is rich enough to build a credible model, but
the gross-margin-only disclosure flatters the picture. A buyer should focus on the Q3–Q4
range ($375K–$495K) as the realistic target for a single mature territory — not the Q1
headline of $1.17M, which represents the top 20% of a self-selected survivor population.
The new-territory data (Chart 11) tells you where you'll start: $275K average, 46% gross margin,
approximately $55K–$70K remaining after fees and overhead. That is your Year 1–2 reality.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Two Maids'
disclosed Item 19 revenue and gross margin data, combined with the fee burden model for this
cohort. Two Maids is unusual in disclosing cost-of-sales data (direct labor + cleaning
materials), which gives us a more grounded COGS estimate than most franchise FDDs provide.
Your actual results depend on your market, your hiring costs, your route density, and your execution.</p>
""",

"economics_scenarios_config": [
    ("Year 1-2 territory (Chart 11 avg)", 275000),
    ("Q4 mature territory (Chart 4 avg)", 377000),
    ("Q3 mature territory (Chart 3 avg)", 495000),
],

"economics_cogs_ratio": 0.47,

"economics_assumptions": "Revenue from Item 19 quintile and tenure data. COGS at 47% (derived from disclosed ~53% gross margin for mature quintiles; COGS = 100% − 53% gross margin = 47%, covering direct labor + cleaning materials). Franchisor fees from cleaning cohort fee burden model. 'Remaining' must still cover: rent/lease ($1,500–$2,500/mo), vehicle/fuel, insurance, office supplies, administrative costs, personal taxes, and owner draw. Gross margin for Year 1-2 territories is lower (46%) — the 47% COGS assumption is slightly optimistic for new operations.",

"investment_narrative": """
<p>Mid-cohort entry cost: $93,440–$149,890 (p.&nbsp;21). The two-part franchise fee structure
($19,950 Initial Franchise Fee + $40,000 Initial Territory Fee = $59,950) is higher than
MaidPro ($29,950) but lower than Molly Maid ($75K territory fee + training). The franchisor
offers in-house financing for both fees — unusual in this cohort and a meaningful advantage
for cash-constrained buyers.</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee + territory fee ($59,950):</strong> Two-part structure. $19,950
franchise fee + $40,000 territory fee for first territory. No franchise fee on subsequent
agreements; additional territories are $40,000 ($30,000 if purchased simultaneously).
15% veteran/spouse discount available. In-house financing available — terms not
fully disclosed in Item 7 but referenced in Item 10. (pp.&nbsp;14–15, 20)</li>
<li><strong>Local Advertising Start-Up Program Fee ($9,000):</strong> $3,000/month for
first 3 months, included in Item 7. This is on top of the ongoing $3,000/month local
ad fee for months 4–6, then $2,500/month thereafter. Total first-year local advertising
cost: approximately $33,000. (p.&nbsp;21)</li>
<li><strong>Working capital ($10K–$40K):</strong> 3 months. Does not include owner salary
or draw. The $30K spread is wide — actual needs depend on how quickly revenue ramps.
Given that Year 1–2 territories average $275K gross ($23K/month) with 46% gross margin,
the low end of this range is likely insufficient. (p.&nbsp;21)</li>
<li><strong>Lease and improvements ($6,500–$17,500):</strong> Light industrial/commercial
space, 1,200–1,800 sq ft. Minor improvements. This is a real cost — Two Maids requires
a physical office location, not a home-based operation. (pp.&nbsp;20–21)</li>
<li><strong>Conversion franchise discount:</strong> Territory fee reduced by 10% of prior
year Gross Revenue, up to $10,000. Total investment range for conversions: $83,440–$139,890.
(p.&nbsp;21)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> A new buyer should plan for ~$120K total cash outlay
(the midpoint) plus personal living expenses for 12–18 months. The in-house financing
option could reduce cash-at-signing meaningfully — clarify exact terms before committing.
The first-year advertising spend ($33K in mandatory local ad fees alone) is a significant
component that does not appear in the headline Item 7 range because only $9K of it falls
within the "initial investment" period.
</div>
""",

"system_health_narrative": """
<p>Fastest-growing residential cleaning franchise in this cohort. Net unit growth accelerated
each year: +7 (2022), +19 (2023), +26 (2024). The system expanded from 92 to 144 outlets
in three years — a 56.5% increase. This is not incremental growth; it is an active expansion
campaign. With 21 signed-but-not-yet-opened agreements and 35 projected new outlets for 2025
(p.&nbsp;67), the franchisor is targeting continued acceleration.</p>
""",

"system_health_detail": """
<h3>Low attrition against high growth</h3>
<p>Total exits over the 3-year window: 4 (2022), 5 (2023), 6 (2024) — combining terminations
and ceased operations. Zero non-renewals in any year. Turnover rate (excluding transfers):
4.4%, 5.1%, 5.1%. For a system growing this fast, the attrition is remarkably low. New
franchise systems often see high early-cohort failure rates; Two Maids' 2022–2024 openings
appear to be sticking. (pp.&nbsp;63–67)</p>

<h3>Active transfer market</h3>
<p>8 (2022), 6 (2023), 10 (2024) transfers. The 10 transfers in 2024 represent 8.5% of
start-of-year outlets. A functioning resale market is a positive signal — it means
territories have value to buyers. However, the transfer fee structure ($24,950–$50,000
for sales to new franchisees, plus a potential $15,000 referral fee) is among the most
complex and expensive in this cohort. Ask the franchisor what recent resale multiples
look like. (pp.&nbsp;16–17, 63–67)</p>

<div class="implication">
<strong>What this means:</strong> Two Maids is in an aggressive growth phase backed by
family-office capital (JM Family Enterprises). The system is adding outlets faster than
any peer while maintaining low attrition — a combination that suggests the franchisor's
lead generation and training infrastructure is working. The risk is that rapid growth
dilutes territory quality or support resources. Ask franchisees who opened in 2023–2024
whether they felt adequately supported during onboarding.
</div>

<h3>No company-owned outlets</h3>
<p>Zero company-owned locations as of December 2024. The last company-owned territory
(Birmingham, AL) was sold to a franchisee in 2022 (p.&nbsp;66). The franchisor is not
competing with its franchisees in any market.</p>
""",

"risk_narrative": """
<h3>Fee burden is the primary financial risk</h3>
<p>At $200K revenue, total franchisor fees consume 27.9% of gross — the highest in the
cleaning cohort at that revenue level. The $2,500/month local advertising fee
is the largest single ongoing cost component, and it is franchisor-directed: you cannot
redirect that spend to channels you believe perform better in your market. The franchisor
also retains a management fee of up to 10% of monthly ad spend. If the managed advertising
underperforms in your territory, you bear the cost without the ability to pivot. (pp.&nbsp;15–16)</p>

<h3>Transfer fee friction</h3>
<p>The transfer fee structure is the most complex in this cohort. Sales to new franchisees:
greater of $24,950 or 6% of sale price, capped at $50,000. If the buyer was already in
the franchisor's sales pipeline, an additional Transfer Lead Referral Fee of $15,000 (or
broker fee amount) applies. A franchisee selling a $250K territory to a franchisor-sourced
buyer could pay $30,000 in combined transfer fees — 12% of the transaction. This is a
meaningful drag on exit economics and should be factored into any long-term financial model.
(pp.&nbsp;16–17)</p>

<h3>Litigation: effectively clean</h3>
<p>One disclosed action — an affiliate entity (Aussie Pet Mobile, under prior ownership)
entered a consent order with the Maryland Securities Commissioner in 2006 for selling
franchises without proper registration. This involved a different brand under different
ownership and predates Two Maids' founding by seven years. No actions involving Two Maids
Franchising, LLC directly. This is the cleanest litigation profile in the cohort. (p.&nbsp;14)</p>

<h3>Ownership structure</h3>
<p>Two Maids is a subsidiary of Home Franchise Concepts, LLC, which is owned by JM Family
Enterprises, Inc. — a diversified family-office holding company controlled by the James M.
Moran Intervivos Trust. This is <strong>not</strong> private equity. Family-office
ownership typically implies a longer investment horizon and less pressure for rapid exit
or dividend extraction compared to PE sponsors. It also means less likelihood of the
brand being flipped to a new owner within your franchise term. This is a structural
positive, but it does not eliminate the possibility of strategic changes. (p.&nbsp;9)</p>
""",

"peer_narrative": """
<p>Two Maids occupies a distinctive position in the residential cleaning cohort: best
disclosure, fastest growth, but the highest fee burden in the cohort. It is the only brand that
provides gross margin data by quintile alongside lead generation metrics — giving buyers
a more complete picture of unit economics than any competitor.</p>

<p><strong>Closest comparison: The Maids.</strong> Similar fee burden profiles (both have
$30K/year in mandatory local advertising). The Maids has a larger, more mature system
(~338 territories) but is shrinking, not growing. Two Maids is adding 25–30 units/year.
If you are choosing between high-fee-burden brands, Two Maids' growth momentum and Item 19
transparency give it a clear edge.</p>

<p><strong>Sharpest contrast: MaidPro.</strong> Lowest fully-modelable fee burden among brands
without excluded fee components (9–11% of revenue; TCA models lower but excludes its DHH-based Local
Marketing Fee). MaidPro gives you more of every dollar you earn, but its
Item 19 is thinner and its system is smaller. If you want to keep costs low and run your
own marketing, MaidPro is the opposite bet. If you want franchisor-managed marketing and are
willing to pay for it, Two Maids is the argument that the spend generates results — web
leads of 157–238/month for mature territories provide partial evidence.</p>

<p><strong>Scale consideration: Molly Maid.</strong> Largest system in the cohort (over 400
territories), backed by Neighborly's multi-brand infrastructure. Lower fee burden than
Two Maids (10–11% of revenue), but its Item 19 is less detailed. Molly Maid is the safer,
lower-cost choice for buyers who prioritize brand recognition over growth momentum.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "The Local Advertising Services Program Fee is $2,500/month and franchisor-directed. What specific channels does the spend go to, and what lead attribution data can you show me for a territory similar to mine?",
        "context": "Item 6, pp. 15–16. $30,000/year in non-discretionary, franchisor-managed ad spend. Franchisor retains up to 10% management fee.",
        "follow_ups": [
            "Ask for actual monthly lead reports from 2–3 territories at different revenue levels.",
            "Ask what happens if you believe the advertising is underperforming — can you request a channel reallocation?",
            "Ask whether the 10% management fee is applied to the full $2,500 or only the media spend portion."
        ],
    },
    {
        "question": "Chart 11 shows Year 1–2 territories averaging $275K with 46% gross margin. What does the typical cash flow timeline look like — when do most new operators reach monthly breakeven after all fees?",
        "context": "Item 19, Chart 11, p. 60. 17 territories open 12–24 months. Gross margin 7 points below mature average.",
        "follow_ups": [
            "Ask how many of the 17 Chart 11 territories were cash-flow positive (after all franchisor fees) by month 12.",
            "Ask what the 44 excluded locations (open less than 1 year) look like — are any already generating meaningful revenue?"
        ],
    },
    {
        "question": "The transfer fee can reach $50,000 plus a $15,000 referral fee. Of the 10 transfers in 2024, what was the typical total transfer cost as a percentage of the sale price?",
        "context": "Item 6, pp. 16–17. Transfer fee: greater of $24,950 or 6% of sale price (max $50K). Separate $15K referral fee if buyer was in franchisor pipeline.",
        "follow_ups": [
            "Ask how many of the 10 transfers involved the Transfer Lead Referral Fee.",
            "Ask what the average resale multiple was (sale price relative to trailing 12-month gross revenue).",
            "Ask whether the franchisor actively facilitates resales or whether franchisees find their own buyers."
        ],
    },
    {
        "question": "The technology fee is $650/month per territory. What specifically does this cover, and is there a cap on future increases?",
        "context": "Item 6, p. 16. $7,800/year — among the highest fixed tech fees in the cleaning cohort.",
        "follow_ups": [
            "Ask for a list of the specific software platforms included.",
            "Ask whether you can use your own CRM, scheduling, or accounting tools, or whether the franchisor's platforms are mandatory.",
            "Ask how much the fee has increased over the past 3 years."
        ],
    },
    {
        "question": "The system grew from 92 to 144 outlets in 3 years. At what point does the franchisor expect to slow new openings, and how does rapid growth affect support quality for existing franchisees?",
        "context": "Item 20, pp. 63–67. 32 openings in 2024, 35 projected for 2025. 21 signed-but-not-opened.",
        "follow_ups": [
            "Ask what the ratio of field support staff to franchisees is, and how it has changed as the system grew.",
            "Ask franchisees who opened in 2023–2024 whether onboarding support met expectations.",
            "Ask whether any existing territories have been encroached by new openings."
        ],
    },
    {
        "question": "Q1 territories average $1.17M and Q5 territories average $230K — a 5:1 spread. What distinguishes top-quintile operators from bottom-quintile, and how many years does it typically take to reach Q2–Q3 performance?",
        "context": "Item 19, Charts 1–5, pp. 50–54. All 86 territories are 2+ years old, so the spread is not simply tenure-driven.",
        "follow_ups": [
            "Ask whether market size, operator experience, or tenure is the strongest predictor of quintile placement.",
            "Ask whether any Q5 territories are on performance improvement plans or at risk of termination.",
            "Ask what specifically the $20K-revenue territory in Q5 represents — is it winding down or a part-time operation?"
        ],
    },
    {
        "question": "JM Family Enterprises is a family-office holding company, not PE. What is the parent company's strategic plan for Two Maids over the next 5–10 years — is a sale, IPO, or roll-up on the horizon?",
        "context": "Item 1, p. 9. Two Maids is a subsidiary of Home Franchise Concepts, LLC, owned by JM Family Enterprises (Moran Trust).",
        "follow_ups": [
            "Ask whether Home Franchise Concepts has acquired or divested any other franchise brands in the past 3 years.",
            "Ask whether JM Family Enterprises has a stated holding period for portfolio companies."
        ],
    },
    {
        "question": "The in-house financing for franchise and territory fees is referenced but not fully detailed in Item 7. What are the specific terms — interest rate, repayment period, and what happens if you default?",
        "context": "Item 7, p. 20. Financing referenced for Initial Franchise Fee and Initial Territory Fee. Full terms in Item 10.",
        "follow_ups": [
            "Ask what percentage of new franchisees use in-house financing vs paying cash.",
            "Ask whether the financing terms are negotiable or standardized."
        ],
    },
],

},

"molly-maid": {

"executive_summary": """
<p>Molly Maid is the largest residential cleaning franchise in this cohort by unit count (448 outlets as of
year-end 2024) and the oldest by system age (franchising since 1984). It is backed by Neighborly / KKR through
a securitization structure (Molly Maid SPV LLC). The system has contracted every year for three consecutive
years — 501 to 448 units, a net loss of 53 (-10.6%). This is not a growing system; it is a mature brand
in managed decline.</p>

<p>The fee structure is mid-cohort: a marginal tiered royalty starting at 6.5% (declining to 3% above $2.8M),
2% MAP contribution, and ~$463/month in technology fees. At $300K revenue, total modelable fees are $31,056
(10.4%) — below Merry Maids, The Maids, Two Maids, and Maid Right, but above The Cleaning Authority and
MaidPro. However, the Local Marketing Requirement (per-Target-Household, territory-size-dependent) is excluded
from the model and adds an unknown additional cost.</p>

<p>The Item 19 is unusual: it discloses per-cleaning revenue ($173 average), per-Target-Household penetration,
recurring customer rates (91%), and same-store sales growth distributions — but does <strong>not</strong>
disclose total gross revenue per franchisee or per territory. You cannot directly determine what a Molly Maid
territory generates in annual revenue from this FDD alone. The operational metrics are strong (79% of franchisees
grew YoY), but the missing revenue denominator is a meaningful gap for financial modeling.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$140K–$197K total investment. Mid-to-high for cleaning cohort. Two-part fee (franchise + territory) averages ~$56K–$64K in initial fees."},
    {"dimension": "Ongoing fee burden", "rating": "Mixed", "color": "mixed",
     "summary": "10.4% of revenue at $300K (modelable). Marginal royalty tiers reward scale. But Local Marketing Requirement (per-TH) is excluded and adds unknown cost."},
    {"dimension": "System stability", "rating": "Weak", "color": "weak",
     "summary": "Three consecutive years of contraction: -20, -17, -16 net units. System lost 53 units (-10.6%) over 2022–2024. Ceased operations (16–22/year) drive exits."},
    {"dimension": "Revenue disclosure", "rating": "Mixed", "color": "mixed",
     "summary": "Rich operational metrics (per-cleaning revenue, recurring rates, YoY growth). But no total revenue per franchisee or territory disclosed — the most important number for financial modeling is missing."},
    {"dimension": "Disclosure quality", "rating": "Strong", "color": "strong",
     "summary": "Clean filing. Light litigation (2 concluded affiliate actions). Extraction confidence high across all items."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "System contraction is the primary risk. 25 businesses closed during 2024 (excluded from Item 19 — survivorship bias). SPV/securitization structure adds entity complexity."},
    {"dimension": "Buyer fit breadth", "rating": "Strong", "color": "strong",
     "summary": "Strongest brand recognition in cleaning. Neighborly multi-brand infrastructure. Tiered royalty rewards growth. VetFran and multi-unit discounts available."},
    {"dimension": "Overall", "rating": "Mixed", "color": "mixed",
     "summary": "The safest brand name in the cohort paired with a shrinking system. Operational metrics are healthy, but the system is losing more units than it adds. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """Molly Maid offers the strongest brand recognition and longest track record in the
residential cleaning cohort, backed by Neighborly's multi-brand franchise infrastructure. The tiered royalty
structure genuinely rewards scale. But the system is contracting — losing 15–20 units per year net — and the
Item 19 omits the single most important metric for a prospective buyer: total revenue per territory. You are
buying into a mature, recognized brand with a shrinking footprint. Your diligence must focus on whether the
contraction is pruning weak territories (healthy) or signaling systemic problems (concerning).""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Brand-recognition buyer:</strong> Molly Maid is one of the most recognized names in residential
cleaning. If local marketing leverage and consumer trust matter to you, this brand has decades of awareness
that newer competitors cannot match.</li>
<li><strong>Multi-brand Neighborly investor:</strong> If you already own or plan to own other Neighborly
brands (Mr. Rooter, Mr. Electric, Mosquito Joe, etc.), the shared infrastructure, cross-selling, and
multi-unit discount structure create genuine portfolio synergies.</li>
<li><strong>Buyer seeking recurring revenue stability:</strong> 91% recurring customer rate is the highest
in the cohort. Weekly customer retention is a core operational strength of this system.</li>
<li><strong>Scale-oriented operator who will benefit from royalty tiers:</strong> The marginal royalty drops
from 6.5% to 3% as revenue climbs through brackets. At $1M+ revenue, the blended effective rate is well
below 6% — more favorable than most competitors' flat rates.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who needs disclosed revenue benchmarks:</strong> The Item 19 does not disclose total
revenue per franchisee or per territory. If you need disclosed revenue data to build your financial model,
MaidPro, The Cleaning Authority, Merry Maids, or Two Maids all disclose absolute revenue figures.</li>
<li><strong>Growth-oriented buyer seeking system momentum:</strong> The system has contracted every year
for three years. If you want to join a franchise that is expanding, Two Maids or The Cleaning Authority
are growing; Molly Maid is not.</li>
<li><strong>Budget-sensitive buyer:</strong> The two-part fee structure (franchise fee + per-TH territory fee)
means initial fees typically run $56K–$64K — higher than MaidPro ($45K) or The Cleaning Authority ($20K–$35K
franchise fee). Total investment midpoint of $169K is above most peers.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have talked to current franchisees about their actual annual gross revenue — the FDD will not
tell you this number.</li>
<li>You understand why the system is contracting and whether your proposed territory is in a growth or
decline market. Ask the franchisor for territory-specific unit history.</li>
<li>You have calculated your Local Marketing Requirement based on your territory's Target Household count
and incorporated it into your cost model.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Molly Maid's modelable fee burden is mid-cohort: 10.4% of revenue at $300K, dropping to 9.6% at $500K
as the tiered royalty begins to bite. This is below Merry Maids (11.0%), significantly below The Maids (19.7%)
and Two Maids (21.6%), but above MaidPro (10.0%) and The Cleaning Authority (7.6%, though TCA excludes its
DHH-based Local Marketing Fee). The key caveat: Molly Maid's model also excludes the Local Marketing
Requirement, which is per-Target-Household and territory-size-dependent.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (6.5%&rarr;3% marginal tiers):</strong> Progressive brackets like income tax. 6.5% on
first $500K, 6% on $500K–$800K, 5.5% on $800K–$1.2M, continuing down to 3% above $2.8M. At $500K revenue,
effective rate is 6.5% flat (all within first tier). At $1M, blended effective rate drops to ~6.15%. The
tiers are genuinely franchisee-friendly at scale — but most single-territory operators will never leave the
6.5% bracket. Roll-In franchisees get reduced Year 1 rates (3% small/medium, 2.5% large). (pp. 26, 36–37)</li>
<li><strong>MAP Contribution (2% of Gross Sales):</strong> National brand fund. Straightforward. Subject to
ramp-up for legacy franchisees through 2025; full 2% applies to all from 2026. (pp. 26–27)</li>
<li><strong>Technology ($463/month):</strong> Split across two payees: $58/month to ZorWare (Qvinci, Broadly
NPS, FranConnect, Office 365) + $405/month to ServiceTitan (CLEO business management software). Total
$5,556/year. May increase up to 30% annually. (pp. 27–28, 35)</li>
<li><strong>Local Marketing Requirement (per-TH — NOT modeled):</strong> $1.00 per Target Household per year
at $0–$15K weekly Gross Sales, declining to $0.15/TH at $25K+ weekly. For a 55,000 TH territory at the
$1.00 rate: $55,000/year in mandatory local marketing. At the $0.50 rate ($15K–$20K weekly): $27,500/year.
If you do not spend this amount, the franchisor may collect and spend on your behalf. This is a significant
cost excluded from the fee burden model. (pp. 34–35)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, you retain ~$269K after modelable franchisor fees.
At MaidPro (lowest-burden at that level), you'd keep ~$270K — nearly identical. But Molly Maid's
Local Marketing Requirement could add $15K–$55K depending on territory size, making the true gap
between Molly Maid and cheaper competitors substantially wider than the modelable fees suggest.
</div>

<div class="callout">
<div class="callout-title">Key Accounts fee — a hidden cost layer</div>
Molly Maid charges up to 3% of Gross Sales on Key Account, Business Development, and call-center-dispatched
work (p. 32). If a meaningful share of your revenue comes through franchisor-generated channels, this fee
effectively adds to the royalty. Ask what percentage of a typical territory's revenue flows through
Key Accounts.
</div>
""",

"item19_narrative": """
<p>Molly Maid's Item 19 is operationally rich but financially incomplete. It provides four parts covering
197 operators (417 franchised businesses out of 448 total) for calendar year 2024. What it discloses is
genuinely useful — per-cleaning revenue, territory penetration, recurring customer rates, and year-over-year
growth. What it omits — total gross revenue per territory — is the single most important number for a
prospective buyer's financial model.</p>

<h3>Part I — Average gross sales per cleaning</h3>
<ul class="compact">
<li><strong>System average:</strong> $173.43 per cleaning. Median: $169.75.</li>
<li><strong>Top quartile:</strong> $213.76 average ($191–$263 range).</li>
<li><strong>Bottom quartile:</strong> $132.70 average ($90–$152 range).</li>
<li>The $80 spread between top and bottom quartile per-cleaning revenue suggests meaningful pricing variation
across markets — but this is a tighter distribution than revenue per territory would likely show.</li>
</ul>

<h3>Part II — Gross sales per Target Household</h3>
<ul class="compact">
<li><strong>System average:</strong> $16.23 per TH. Wide range: $2.59 to $88.13.</li>
<li>Top 10% generates ~5× more revenue per TH than the system average, suggesting massive territory
utilization variance.</li>
<li>For a 55,000 TH territory at the system average: implied revenue of ~$893K. At the median ($15.17/TH):
~$834K. These are rough estimates — the FDD does not validate this arithmetic.</li>
</ul>

<h3>Part III — Recurring vs. occasional customers</h3>
<ul class="compact">
<li><strong>91% recurring, 9% occasional</strong> (average). The highest recurring rate in the cohort.</li>
<li>56% of operators exceed the system average recurring rate — a positive signal for business predictability.</li>
</ul>

<h3>Part IV — Same-store sales growth (2023 vs 2024)</h3>
<ul class="compact">
<li><strong>79% of franchisees grew year-over-year.</strong> Only 4% declined more than 10%.</li>
<li>22% grew more than 10%. The growth distribution is healthy — but this is same-store, not same-system.
The 25 businesses that closed during 2024 are excluded.</li>
</ul>

<h3>What's missing</h3>
<ul class="compact">
<li><strong>Total gross revenue per franchisee or per territory:</strong> Not disclosed. You can attempt to
triangulate from per-cleaning revenue × estimated cleans/year, or from per-TH revenue × TH count, but
neither calculation is validated by the FDD.</li>
<li><strong>Any cost data:</strong> No COGS, no gross margin, no expense breakdowns. The Cleaning Authority
and Two Maids both disclose more cost information.</li>
<li><strong>Survivorship bias:</strong> 25 businesses that closed in 2024 are excluded. 9 that opened,
13 mid-transfer, 2 with unreliable data, and 6 with territory changes are also excluded.</li>
</ul>
""",

"item19_triangulation": """
<h3>Estimating territory revenue from disclosed metrics</h3>
<p>The FDD does not disclose total revenue, but we can attempt a rough triangulation:</p>

<p><strong>Method 1 — Per-TH revenue × territory size:</strong></p>
<ul class="compact">
<li>System average: $16.23/TH. For a 55,000 TH territory: ~$893K implied revenue.</li>
<li>Median: $15.17/TH. Same territory: ~$834K.</li>
<li>Bottom quartile average: $8.10/TH. Same territory: ~$446K.</li>
</ul>

<p><strong>Method 2 — Per-cleaning revenue × estimated cleanings:</strong></p>
<ul class="compact">
<li>System average per cleaning: $173. If a territory performs 15 cleanings/day × 250 working days = 3,750
cleanings/year: implied revenue ~$649K. At 10 cleanings/day: ~$433K.</li>
<li>These estimates are not validated by the FDD. Actual cleans/day/territory is not disclosed.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Rough triangulation suggests a mid-range Molly Maid territory might
generate $450K–$900K in gross revenue depending on territory size and utilization. But these are estimates
built on estimates. Unlike MaidPro ($462K disclosed average), The Cleaning Authority ($1.46M disclosed
Enterprise average), or Merry Maids ($487K Qualified Franchise average), Molly Maid gives you no confirmed
revenue number. You must talk to current franchisees or get territory-specific data from the franchisor
to build a credible financial model.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. Molly Maid's FDD does not disclose total gross revenue per territory
or any cost/expense data. The scenarios below use estimated revenue ranges triangulated from per-TH and
per-cleaning metrics — these are illustrative, not FDD-sourced revenue figures. Your actual results depend
on territory size, local pricing, route density, labor costs, and execution. No COGS data is available
from this FDD.</p>
""",

"economics_scenarios_config": [
    ("Bottom-quartile TH estimate", 300000),
    ("Median TH estimate", 500000),
    ("Top-quartile TH estimate", 800000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue estimated from per-TH metrics (Part II) applied to a hypothetical 55,000 TH territory. Bottom quartile: $8.10/TH × 55K = ~$446K, rounded to $300K as conservative. Median: $15.17/TH × 55K = ~$834K, rounded to $500K as midpoint. Top quartile: $32.60/TH × 55K = ~$1.79M, capped at $800K for single-territory realism. COGS estimated at 55% based on cleaning industry norms (no FDD cost data available). 'Remaining' must cover all operating expenses, Local Marketing Requirement, and owner draw. These are illustrative scenarios, not disclosed figures.",

"investment_narrative": """
<p>Mid-to-high cohort entry cost: $139,900–$197,200. The two-part initial fee structure ($14,900 franchise
fee + ~$45,000–$70,000 territory fee based on $1.00 per Target Household) means your upfront fees scale
with territory size. A standard 55,000–70,000 TH territory will cost $70K–$85K in combined initial fees.
Multiple discount programs exist: VetFran (20% off territory fee), Roll-In (5–50% based on existing
business sales), Multi-Unit (5–20% based on tenure). (pp. 23–26)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Territory Fee ($45,000–$70,000 standard / $30,000–$45,000 mid-size):</strong> $1.00 per Target
Household. This is the primary variable — your territory size drives your initial cost. Average paid in 2024:
~$56K. Franchise fee ($14,900) is waived for expansion of existing compliant franchisees. (pp. 23–25)</li>
<li><strong>Additional Funds — 3 months ($50,000–$60,000):</strong> The largest line item. Covers payroll,
marketing, gas, auto maintenance, internet, general business. Does not include owner salary or draw. At the
low end, this may be tight for a territory still ramping revenue. (p. 39)</li>
<li><strong>Auto lease + computer hardware ($6,100–$10,000):</strong> Minimum 2 vehicles required (one for
estimates, one for team). New vehicle purchase runs $23,500–$26,500 — substantially above the lease deposit
shown in Item 7. (p. 39)</li>
<li><strong>Software enrollment ($1,500 one-time):</strong> Paid to ZorWare. In addition to the ongoing
$463/month technology fees. (p. 39)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Plan for $169K at the midpoint. The territory fee structure means
larger territories cost proportionally more to enter — and the Local Marketing Requirement also scales
with territory size. A buyer targeting a large 70,000 TH territory should expect $85K+ in initial fees
alone, plus ongoing local marketing costs of $35K–$70K/year depending on revenue level. The economics
favor territories large enough to generate scale but small enough that per-TH costs remain manageable.
</div>
""",

"system_health_narrative": """
<p>Molly Maid is the largest residential cleaning franchise in this cohort — and it is contracting. The
system has shrunk every year for three consecutive years: 501 to 481 to 464 to 448 outlets. That is
53 net lost units (-10.6%). New openings averaged only 7 per year (5, 7, 9) against 25–38 annual exits.
This is a mature system that is losing more units than it replaces.</p>
""",

"system_health_detail": """
<h3>Exit composition</h3>
<p>The exit pattern shifted over the three-year window:</p>
<ul class="compact">
<li><strong>2022:</strong> 8 terminations, 1 non-renewal, 16 ceased operations, 20 transfers. Total exits: 45.</li>
<li><strong>2023:</strong> 2 terminations, 0 non-renewals, 22 ceased operations, 15 transfers. Total exits: 39.</li>
<li><strong>2024:</strong> 6 terminations, 2 non-renewals, 17 ceased operations, 13 transfers. Total exits: 38.</li>
</ul>
<p>Terminations declined, but "ceased operations — other reasons" has been the dominant exit category every year
(16, 22, 17). The FDD notes that this column includes transfers to existing franchisees, territory consolidations,
and abandonments — making it difficult to distinguish healthy portfolio management from business failures.
(pp. 78–85)</p>

<h3>Turnover rate in context</h3>
<p>Overall turnover (all exits ÷ start-of-year count): 9.0% (2022), 8.1% (2023), 8.2% (2024). This is
mid-range for the cleaning cohort — well below Merry Maids (14.1%) and Maid Right (38.6%), but above
The Maids (3.9%) and Two Maids (5.1%). The concerning pattern is not the rate itself but the inability
to offset exits with new openings. Only 21 new franchises opened across the entire three-year window.</p>

<div class="implication">
<strong>What this means:</strong> This is not a system in crisis — the turnover rate is moderate and
same-store sales growth is healthy (79% grew YoY). But it is a system that has stopped growing. For
a buyer, the question is whether you are buying into a mature brand with stable territories or a declining
system that will have fewer peers, less brand momentum, and potentially less franchisor investment in
innovation over time. The Neighborly/KKR infrastructure provides a floor — this brand is unlikely to
be abandoned — but growth is not coming from new franchise sales.
</div>

<h3>No company-owned outlets</h3>
<p>Zero company-owned locations. All 448 outlets are franchised. The franchisor is not competing with
its franchisees in any market.</p>
""",

"risk_narrative": """
<h3>System contraction is the primary structural risk</h3>
<p>Three consecutive years of net unit loss with only 21 new openings across the period. The system shrank
10.6% while same-store sales grew for 79% of franchisees. This divergence — healthy existing operators
but no new ones joining — suggests either the franchise offering is not competitive for new buyers, or the
franchisor is prioritizing territory consolidation over expansion. Either way, the trajectory matters for
long-term brand investment and support resources. (pp. 78–85)</p>

<h3>SPV securitization structure</h3>
<p>Molly Maid SPV LLC is a special-purpose vehicle within the Neighborly/KKR securitization chain. All
franchise agreements were transferred from the predecessor entity to the SPV in March 2021. This adds
entity complexity — your franchise agreement is with a special-purpose entity, not the operating company
directly. In practice, Neighborly manages operations, but the legal structure matters if the securitization
is restructured or sold. (pp. 1–2)</p>

<h3>Litigation: effectively clean</h3>
<p>Two disclosed actions — both concluded, both involving predecessor or affiliate entities (Kansas consumer
protection action against Molly Maid, Inc. in 2010, settled for $50K; California regulatory action against
Window Genie affiliate in 2017, $5K penalty). No actions involving the current Molly Maid SPV LLC franchisor.
Clean litigation profile. (pp. 21–22)</p>

<h3>Item 19 disclosure gap</h3>
<p>The omission of total revenue per territory is itself a risk factor — not because it suggests bad
economics, but because it forces you to build your financial model on triangulated estimates rather than
disclosed data. Competitors who disclose revenue (MaidPro, The Cleaning Authority, Merry Maids, Two Maids)
give their prospective buyers a material advantage in pre-purchase analysis.</p>
""",

"peer_narrative": """
<p>Molly Maid is the largest system in the cohort and the most recognized brand. It offers a competitive
fee structure (10.4% modelable at $300K), a tiered royalty that rewards growth, and Neighborly's multi-brand
infrastructure. But it is the only cohort member combining system contraction with a missing revenue disclosure —
two features that make pre-purchase analysis harder than at most peers.</p>

<p><strong>Closest comparison: Merry Maids.</strong> Similar scale (802 units), similar age (46 years),
similar system contraction (worse — Merry Maids lost 187 units over 3 years). Merry Maids discloses
total revenue ($487K average for Qualified Franchises) while Molly Maid does not. Merry Maids' fee burden
is slightly higher (11.0% vs 10.4% at $300K). If revenue disclosure matters to you, Merry Maids provides
more to work with — but its contraction is more severe.</p>

<p><strong>Sharpest contrast: Two Maids & A Mop.</strong> Fastest-growing system (+56.5% over 3 years) vs
Molly Maid's contraction (-10.6%). Two Maids charges significantly higher fees (21.6% at $300K) but provides
the richest disclosure in the cohort. If you are choosing between brand recognition and growth momentum,
Molly Maid and Two Maids are opposite bets.</p>

<p><strong>Lower-cost alternative: MaidPro.</strong> Simpler fee structure (10.0% at $300K), lower entry
cost ($110K–$159K), disclosed revenue ($462K average), and a stabilizing system. If Molly Maid's brand
premium and Neighborly ecosystem do not justify the higher entry cost and missing revenue disclosure,
MaidPro is the cleaner comparison.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "The Item 19 discloses per-cleaning revenue and per-TH metrics but not total revenue per territory. What is the average and median annual gross revenue for a single-territory Molly Maid franchisee?",
        "context": "Item 19, Parts I–IV, pp. 74–78. 197 operators, 417 businesses. No total revenue figure provided.",
        "follow_ups": [
            "Ask for the revenue distribution (quartiles or deciles) for single-territory operators specifically.",
            "Ask what the average number of cleanings per week per territory is — this allows you to calculate total revenue from the disclosed per-cleaning average.",
            "Ask whether franchisees who closed during 2024 (25 businesses excluded from Item 19) were generating below-average revenue."
        ],
    },
    {
        "question": "The system has contracted from 501 to 448 outlets over three years. What is driving the net decline — is the franchisor pruning underperforming territories, or are franchisees choosing to exit?",
        "context": "Item 20, pp. 78–85. 'Ceased operations — other reasons' is the largest exit category (16, 22, 17 per year) but includes transfers to existing franchisees and territory consolidations.",
        "follow_ups": [
            "Ask how many of the 'ceased operations' were territory consolidations by multi-unit operators vs business failures.",
            "Ask what the franchisor's target system size is — does the strategic plan call for growth or managed contraction?",
            "Ask how many new franchise agreements were signed (not just opened) in 2024."
        ],
    },
    {
        "question": "The Local Marketing Requirement scales from $1.00/TH to $0.15/TH based on weekly Gross Sales. For the territory I am considering, what is the estimated annual Local Marketing Requirement?",
        "context": "Item 6, pp. 34–35. Territory-size-dependent marketing cost excluded from fee burden model.",
        "follow_ups": [
            "Ask what weekly Gross Sales threshold a typical territory reaches by end of Year 2 — this determines your applicable rate.",
            "Ask whether the franchisor collects and spends unmet Local Marketing Requirement funds on your behalf, and if so, what that spend looks like."
        ],
    },
    {
        "question": "The Key Accounts/Management Fee is up to 3% of Gross Sales on franchisor-generated business. What percentage of a typical territory's revenue comes through Key Accounts or call-center-dispatched leads?",
        "context": "Item 6, pp. 32–33. This fee is layered on top of the royalty for franchisor-sourced revenue.",
        "follow_ups": [
            "Ask whether Key Account revenue is growing as a share of total system revenue.",
            "Ask whether franchisees can decline Key Account assignments."
        ],
    },
    {
        "question": "79% of franchisees grew same-store sales in 2024, but the system lost 16 net units. How do you reconcile healthy same-store performance with system contraction?",
        "context": "Item 19 Part IV (pp. 77–78) vs Item 20 (pp. 78–85).",
        "follow_ups": [
            "Ask whether the franchisees who closed were concentrated in specific markets or demographics.",
            "Ask whether any of the 25 closures in 2024 involved territories that were later consolidated into adjacent franchisees."
        ],
    },
    {
        "question": "The technology fee ($463/month) may increase up to 30% annually. What has the actual year-over-year increase been for the past 3 years?",
        "context": "Item 6, pp. 27–28, 35. $5,556/year currently, split between ZorWare and ServiceTitan.",
        "follow_ups": [
            "Ask whether franchisees have any input into technology platform selection.",
            "Ask what the CLEO (ServiceTitan) platform specifically provides vs the ZorWare stack."
        ],
    },
],

},

"the-maids": {

"executive_summary": """
<p>The Maids is a 47-year-old residential cleaning franchise (The Maids International, LLC / Gladstone
Management Corp.) with 369 total outlets — 338 franchised and 31 company-owned — as of fiscal year-end
September 30, 2025. The system has contracted modestly (382 to 369 over 3 years, -3.4%), but franchised
unit count stabilized at 338 in the most recent year. Turnover is declining: 5.2% to 4.1% to 3.9% —
the lowest trajectory in the cohort.</p>

<p>The Item 19 is the most analytically valuable in the cohort for one reason: it includes a full
company-owned P&L showing 15.5% average net income margin across 6 offices. No other cleaning franchise
in this cohort discloses net profitability data. Average per-territory revenue is $386K (median $306K),
and the company-owned offices averaged $1.42M revenue with $220K net income ($209K median). These are
real profitability numbers — rare in franchise disclosure.</p>

<p>The trade-off is fees. The Maids has the second-highest total fee burden in the cleaning cohort (behind Two Maids)
at every revenue level: 25.0% at $200K, 19.7% at $300K, 15.1% at $500K. The primary driver is the $2,500/month
mandatory Local Marketing Requirement ($30,000/year), layered on top of a 2.25% marketing fund percentage
and a weekly non-marginal royalty starting at 6.9%. The entry cost is the lowest in the cohort ($118K–$141K),
but the ongoing fees are the highest.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Strong", "color": "strong",
     "summary": "$118K–$141K total investment. Lowest in cleaning cohort. Includes $19,900 SMART Start Package (training + equipment)."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "Second-highest in cohort. 19.7% at $300K, driven by $30K/year mandatory local marketing + 6.9% royalty at that revenue level. Two Maids is higher at every level."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Modest contraction (-3.4% over 3 years) but franchised count stabilized in FY2025 (338→338). Turnover declining to 3.9% — lowest trend in cohort."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Per-territory revenue, per-clean metrics, AND company-owned P&L with 15.5% net margin. Only brand in cohort disclosing actual profitability."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Table 3 arithmetic discrepancy (FY2025). Financial condition flagged by states. Confidentiality clauses present. But overall extraction confidence is high."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Fee burden is the primary risk. Franchisor financial condition flagged. Liquidated damages at 9.15% of average weekly revenue × remaining weeks. Company-owned offices being sold to franchisees."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Low entry cost and team-based cleaning model work for owner-operators. But high ongoing fees compress margins at all revenue levels. Multi-territory operators benefit from royalty tier and local marketing discounts."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "The only cleaning franchise disclosing actual net profitability — and the most expensive to operate on a percentage basis. The data says the model works at scale; the question is whether the fee burden leaves enough for the franchisee. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """The Maids is the most analytically transparent franchise in this cohort: a full
company-owned P&L showing 15.5% net margin is data no competitor provides. The low entry cost ($118K–$141K)
makes it the most accessible brand to enter. But the ongoing fee burden — highest in the cohort at every
revenue level — means you are paying the most for what you get. The tension is real: the data says the model
is profitable at scale (company-owned offices net $220K/year), but the fees compress what reaches the
franchisee. Your diligence must focus on whether franchised operators achieve the same margins as
company-owned — and whether the mandatory $30K/year local marketing spend generates proportional returns.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Buyer seeking lowest entry cost in the cohort:</strong> At $118K–$141K total investment, The Maids
has the lowest initial capital requirement. The $19,900 SMART Start Package bundles training, equipment,
supplies, and uniforms into a single predictable cost.</li>
<li><strong>Analytical buyer who values profitability disclosure:</strong> If you want to see actual net
income data before you invest, The Maids is the only brand in this cohort that provides it. The company-owned
P&L gives you a cost structure to benchmark against.</li>
<li><strong>Multi-territory operator:</strong> The royalty structure rewards scale — multi-unit owners in
compliance can combine weekly revenues to reach lower tier rates (6.9% down to 3.9%). Local Marketing
Requirement also discounts for 2nd+ territories ($500/mo and $250/mo vs $2,500/mo for the first).</li>
<li><strong>Owner-operator comfortable with team-based model:</strong> The Maids' 4-person cleaning team
model is designed for supervised crew operations, not solo cleaning.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Fee-sensitive buyer:</strong> If ongoing cost control is a priority, The Maids' fee burden is
the highest in the cohort. At $300K revenue, $59,130 goes to the franchisor (19.7%). MaidPro at the same
revenue retains nearly $30K more per year.</li>
<li><strong>Single-territory buyer expecting to stay small:</strong> The 6.9% royalty applies to territories
under ~$350K/year in weekly revenue. Multi-territory pooling is required to reach lower tiers. A single
territory will pay the maximum royalty rate unless it grows past ~$700K in weekly billing.</li>
<li><strong>Buyer uncomfortable with franchisor financial condition warnings:</strong> Multiple states'
risk disclosures flag the franchisor's financial ability to provide services and support. Consolidated
financials show net losses and related-party debt.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have compared the company-owned P&L margins (15.5% net) to what current franchisees report as their
actual take-home. Company-owned may pay lower royalty rates — verify this directly.</li>
<li>You have modeled the full local marketing commitment ($2,500/month for your first territory) alongside
the 2.25% marketing fund and royalty. Total fees are not obvious from any single line item.</li>
<li>You understand the liquidated damages clause: 9.15% of your average weekly revenue × remaining weeks
in your agreement if terminated. On a $400K/year territory with 5 years remaining, that is ~$94K.</li>
</ul>
""",

"fee_burden_narrative": """
<p>The Maids has the second-highest ongoing fee burden in the residential cleaning cohort (behind
Two Maids) at every modeled revenue level. At $200K, total fees reach $49,980 (25.0% of revenue) — nearly
matching the revenue itself after COGS. At $300K, fees total $59,130 (19.7%). At $500K, fees decline to 15.1% as the fixed-dollar components
become less punitive as a share of revenue. The primary driver is the $30,000/year mandatory Local Marketing
Requirement, which does not scale with revenue.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (6.9%&rarr;3.9% non-marginal weekly tiers):</strong> Unlike Molly Maid's marginal
structure, The Maids uses a single-rate approach: your entire week's revenue is charged at one rate based
on which bracket it falls in. At $300K/year ($5,769/week), you are in the $0–$6,730 bracket at 6.9%.
You need $6,731+/week (~$350K/year) to reach the 6.5% tier. Multi-unit owners in compliance can combine
weekly revenues to reach lower tiers. Minimum weekly fees apply: $150 (months 7–24), $200 (months 25–48),
$250 (months 49+). (pp. 13, 18–19)</li>
<li><strong>Marketing Fund Fee (2% of Gross Revenues):</strong> National brand fund. Franchisor may increase
by up to 0.5% every 2 years with Advisory Council review. (p. 13)</li>
<li><strong>Technology Innovation Fund Fee (0.25% of Gross Revenues):</strong> Separate from Marketing Fund.
May be increased to max 1% with 90 days notice, capped at $15,000/franchisee/year. (p. 13)</li>
<li><strong>Local Marketing Requirement ($2,500/month first territory):</strong> $30,000/year minimum.
Second contiguous territory: $500/month additional. Third+: $250/month each. If not spent, franchisor may
collect and spend on your behalf. This is the largest single fee component for most single-territory operators.
(pp. 19–20)</li>
<li><strong>Technology ($140/month):</strong> Lowest in the cohort. Software and Support Fee. Additional
$85/month per additional office. May increase up to 25% annually. (p. 14)</li>
<li><strong>National Sales Center (variable, mandatory Year 1):</strong> $60/week base + $7.50/unsold quote
+ $36/sold quote. Required for first year, optional thereafter. At 20 quotes/week with 30% close rate:
~$60 + $105 + $216 = $381/week = $19,812/year. This is a material Year 1 cost. (pp. 14, 20)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, The Maids takes $59,130 in fees — nearly double what
MaidPro ($30,000) or Molly Maid ($31,056) charge at the same level. The gap narrows at higher revenue
because the $30K local marketing cost is fixed while royalty tiers drop, but it never fully closes. At
$500K, The Maids charges $75,430 vs MaidPro's $46,000 — a $29,430/year difference. Over a 10-year term,
that is $294,000 more in franchisor fees.
</div>

<div class="callout">
<div class="callout-title">The fee structure has a cliff, not a slope</div>
Because the royalty is non-marginal (your entire week is charged at one rate), crossing a tier boundary
creates a sudden fee reduction. Going from $6,730/week to $6,731/week drops your royalty from 6.9% to 6.5%
on the ENTIRE amount — saving $27/week ($1,400/year) for $1/week more revenue. This rewards operators
who can consistently push weekly billing past tier thresholds, but creates odd incentives near boundaries.
</div>
""",

"item19_narrative": """
<p>The Maids provides three Item 19 tables for the fiscal year ended September 30, 2025. The disclosure is
analytically unusual: it includes per-clean revenue metrics, per-territory revenue, AND a full company-owned
P&L — the only brand in this cohort to disclose actual profitability data.</p>

<h3>Table I — Revenue per clean and per customer</h3>
<ul class="compact">
<li><strong>Average revenue per clean (Regular Maid Service):</strong> $221.39 (median $204.61). Range:
$123–$357. The highest per-clean average in the cohort (vs Molly Maid's $173).</li>
<li><strong>Average annual revenue per recurring customer:</strong> $4,203 (median $3,998). This implies
~19 cleanings per customer per year (~biweekly).</li>
<li><strong>95.1% of cleans are Regular Maid Service;</strong> 4.9% are Special Projects (one-time jobs
averaging $862 per clean).</li>
</ul>

<h3>Table II — Total revenue per outlet and per territory</h3>
<ul class="compact">
<li><strong>Per outlet (97 outlets):</strong> Average $1,184,667, median $764,051. Range: $53K–$7.2M.
Very wide range reflects varying territory counts per outlet.</li>
<li><strong>Per territory (338 territories):</strong> Average $386,244, median $305,938. Range: $42K–$1.28M.
This is the more comparable metric for a prospective single-territory buyer.</li>
<li>Only 32% of outlets exceeded the average — top-heavy distribution skewed by multi-territory operators.</li>
</ul>

<h3>Table III — Company-owned P&L (the rare data)</h3>
<p>6 company-owned offices operating in 31 territories across 6 states:</p>
<ul class="compact">
<li><strong>Average revenue per office: $1,424,377</strong> (median $1,195,040).</li>
<li><strong>Cost of sales: 57.8%</strong> (direct labor 38.6%, vehicle/gas 4.0%, payment processing 2.3%,
CLF royalty 5.4%, marketing fees 2.3%, supplies 1.1%, other 4.1%).</li>
<li><strong>Cost of support: 12.9%</strong> (benefits 3.5%, payroll taxes 3.8%, rent/utilities 4.9%, other 0.7%).</li>
<li><strong>Total cost of revenue: 71.0%.</strong></li>
<li><strong>Operating expenses: 13.6%</strong> (marketing 4.0%, payroll 6.3%, depreciation 0.9%, other 2.4%).</li>
<li><strong>Net income: $220,356 average (15.5% margin), $208,952 median.</strong></li>
</ul>

<h3>What's disclosed vs what's missing</h3>
<ul class="compact">
<li><strong>Disclosed:</strong> Full cost breakdown for company-owned. Direct labor at 38.6% of revenue is
a key benchmark. The 15.5% net margin includes royalty, marketing fees, rent, and all operating expenses.</li>
<li><strong>Company vs franchisee gap:</strong> Company-owned may pay lower CLF rates than franchisees and
have different cost structures (higher manager salaries, different vendor pricing). The 15.5% margin is a
ceiling, not a guarantee for franchisees.</li>
<li><strong>Franchised cost data:</strong> Not disclosed. Only revenue metrics for franchisees.</li>
<li><strong>11 outlets that closed during the Measurement Period ARE included</strong> — unlike Molly Maid
and MaidPro, which exclude closures. This is a more honest representation but may depress averages.</li>
</ul>
""",

"item19_triangulation": """
<h3>From company-owned P&L to franchisee economics</h3>
<p>The Maids' company-owned P&L provides a real cost structure — but company-owned outlets operate at different
scale (average 5.2 territories per office) and may have different fee arrangements. Here is what we can
estimate for a single-territory franchisee:</p>

<p><strong>At per-territory median revenue ($306K):</strong></p>
<ul class="compact">
<li>Applying company-owned cost ratios: COGS at 57.8% = ~$177K, support costs at 12.9% = ~$39K,
operating expenses at 13.6% = ~$42K.</li>
<li>Total costs: ~$258K. Implied net income: ~$48K (15.7% margin).</li>
<li>But this assumes company-owned cost ratios apply — single-territory operators likely have higher
per-unit overhead (especially rent and G&A) and may pay higher royalty rates.</li>
</ul>

<p><strong>At per-territory average revenue ($386K):</strong></p>
<ul class="compact">
<li>Same ratios: total costs ~$325K. Implied net income: ~$61K.</li>
<li>Adding the National Sales Center Fee (mandatory Year 1, ~$15K–$20K): net drops to ~$41K–$46K.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Even applying the most favorable cost ratios (company-owned at scale),
a single-territory operator at the system median ($306K) would net roughly $40K–$50K before personal taxes.
At the average ($386K), closer to $50K–$60K. These are modest owner incomes given the capital and labor
commitment. The math improves dramatically at scale — the company-owned offices average $1.4M across
5+ territories and net $220K. The Maids is designed as a multi-territory build, not a single-territory
lifestyle business.
</div>

<div class="callout">
<div class="callout-title">The labor cost benchmark</div>
Direct labor at 38.6% of revenue (company-owned data) is the single most important cost to validate.
If your local market has higher labor costs (minimum wage, competition for cleaning staff), this ratio
will be worse. Ask current franchisees what percentage of gross revenue goes to direct labor — even a
3-point difference ($386K × 3% = $11,580) materially changes the profitability picture.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It uses The Maids' disclosed per-territory revenue from Table II
and company-owned cost ratios from Table III. Company-owned offices may have different cost structures
than franchised outlets. The scenarios below apply company-owned COGS ratios (57.8%) to franchised
revenue levels — an approximation, not a direct disclosure. Your actual costs depend on your local labor
market, territory size, and operational efficiency.</p>
""",

"economics_scenarios_config": [
    ("Per-territory median", 306000),
    ("Per-territory average", 386000),
    ("Multi-territory (2-pack median)", 612000),
],

"economics_cogs_ratio": 0.578,

"economics_assumptions": "Revenue from Item 19 Table II per-territory metrics (FY ending Sept 30, 2025, 338 territories). COGS at 57.8% from company-owned Table III (includes direct labor 38.6%, vehicle/gas 4.0%, royalty 5.4%, marketing fees 2.3%, payment processing 2.3%, supplies 1.1%, other 4.1%). 'Remaining' must cover operating expenses (13.6% at company-owned scale), personal taxes, and owner draw. Company-owned ratios are for offices averaging 5.2 territories — single-territory operators will have higher per-unit overhead. National Sales Center Fee (~$15K–$20K in Year 1) not included in COGS.",

"investment_narrative": """
<p>Lowest entry cost in the cleaning cohort: $117,720–$141,200. The franchise fee ($60,000) is mid-range,
but the SMART Start Package ($19,900) bundles training, equipment, supplies, and uniforms — eliminating
the need to source these separately. Multi-territory pricing reduces the per-territory franchise fee
significantly: a 3-Pack costs $145,000 ($48,333/territory) vs $60,000 for a single territory.
VetFran discount: $1,000 off total. (pp. 12–13, 20–21)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise Fee ($60,000 single / $55K–$38K effective per territory in packs):</strong> Multi-territory
pricing creates strong incentives for scale: 2-Pack $110K ($55K/territory), 3-Pack $145K ($48.3K), 4-Pack
$170K ($42.5K), 5-Pack $190K ($38K). Each additional territory beyond 5 is $20K. The discount is substantial.
(p. 12)</li>
<li><strong>SMART Start Package ($19,900):</strong> Bundled one-time cost covering training (2 weeks at
franchisor facility), cleaning solvents, supplies, consumables, uniforms, branded apparel, vacuums, and
equipment. Not required for additional contiguous territories. This replaces what other franchises charge
separately across multiple line items. (p. 20)</li>
<li><strong>Grand Opening Marketing ($5,000):</strong> Minimum pre-opening marketing spend. In addition to
the ongoing $2,500/month Local Marketing Requirement. Not required for additional contiguous territories.
(p. 20)</li>
<li><strong>Additional Funds — 3 months ($24,880–$34,500):</strong> Does not include royalty fees, marketing
fund fees, Technology Innovation Fund fees, or franchisee compensation/personal living expenses. The low end
is the most conservative working capital estimate in the cohort — plan for the high end. (p. 21)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> The Maids has the lowest barrier to entry in the cohort. A buyer with
$130K in capital can get in. But the ongoing fee burden (highest in cohort) means the savings on entry are
offset by higher operating costs over time. At $300K revenue, The Maids charges $28K more per year in fees
than MaidPro. Over a 10-year term, that $28K/year gap more than erases the ~$15K lower entry cost. The
Maids' entry cost is a draw, not a destination — the economics are a multi-territory build story.
</div>
""",

"system_health_narrative": """
<p>The Maids' system is modestly contracting but stabilizing. Total outlets declined from 382 to 369 over
three fiscal years (-3.4%), with franchised outlets holding flat at 338 in the most recent year. Company-owned
outlets shrunk more noticeably (36 to 31), with the franchisor selling some locations to franchisees and
closing others. Turnover has improved each year: 5.2% to 4.1% to 3.9% — the best declining-turnover
trajectory in the cohort.</p>
""",

"system_health_detail": """
<h3>Exit composition</h3>
<ul class="compact">
<li><strong>FY2023:</strong> 17 terminations, 0 non-renewals, 1 reacquired, 5 transfers. Terminations
dominated. Georgia lost 4 outlets to terminations.</li>
<li><strong>FY2024:</strong> 8 terminations, 0 non-renewals, 6 reacquired, 6 transfers. Terminations halved.
6 franchised outlets reacquired by franchisor (TX: 2, TN: 4). System held flat at 374 total.</li>
<li><strong>FY2025:</strong> 11 terminations, 0 non-renewals, 2 reacquired, 4 transfers. System contracted
slightly to 369 total. Franchised count held at 338. North Carolina grew by 6 (12→18). Colorado grew by
4 (9→13). (pp. 49–55)</li>
</ul>

<h3>Company-owned portfolio is shrinking</h3>
<p>Company-owned outlets declined from 36 to 31 — primarily due to Tennessee closures (4 outlets) and sales
to franchisees. The franchisor is not expanding its company-owned operations; it is divesting them. This
could indicate a strategic shift toward asset-light operations, or it could reflect financial pressure
(the franchisor's financial condition is flagged by states).</p>

<div class="implication">
<strong>What this means:</strong> The turnover trajectory is genuinely positive — 3.9% is the lowest
in the cohort and improving. But the system is not growing. Only 9 new franchised outlets opened in FY2025
against 13 exits. The franchisor is selling company-owned locations and the financial condition is flagged.
For a buyer, the question is whether the stabilizing franchised count represents a floor or a pause before
further contraction. The declining turnover rate favors the floor interpretation.
</div>

<h3>Fiscal year note</h3>
<p>The Maids uses a September 30 fiscal year-end — not calendar year like most competitors. All Item 20
years refer to FY ending September 30. This means The Maids' "2025" data covers October 2024–September 2025,
while competitors' "2024" data covers calendar year 2024. Direct year-over-year comparisons across brands
require accounting for this offset.</p>
""",

"risk_narrative": """
<h3>Fee burden is the primary financial risk</h3>
<p>At every revenue level, The Maids charges the second-most in total franchisor fees in the
cleaning cohort (behind Two Maids). The $30,000/year Local Marketing Requirement is the largest single driver — it is a fixed
cost that does not scale with revenue, making it particularly punitive for territories under $300K. Combined
with the 6.9% royalty rate (for most single-territory operators), the fee structure requires strong revenue
to generate meaningful owner income. (pp. 13–20)</p>

<h3>Franchisor financial condition</h3>
<p>Multiple states' special risk disclosures flag that the franchisor's financial condition "calls into question
the Franchisor's financial ability to provide services and support." Consolidated financials show a net loss
of $(3,857,961) for FY2025, member's deficit of $(3,548,483), and $28.56M in related-party long-term debt.
A correction of prior-year errors added $7.25M to equity, which suggests the pre-correction financial
position was materially worse. This does not mean the franchisor will fail, but it is a genuine risk factor
for ongoing support quality and system investment. (p. 5)</p>

<h3>Liquidated damages clause</h3>
<p>Termination triggers liquidated damages calculated at 9.15% of average weekly revenue × remaining weeks
in the agreement. On a $400K/year territory with 5 years remaining: ~$94,000. On a $300K territory with
8 years remaining: ~$114,000. This creates significant exit friction and financial exposure. Due within
15 days of termination. (pp. 17, 20)</p>

<h3>Litigation: franchisor-aggressive posture</h3>
<p>4 active lawsuits — all filed by The Maids against former franchisees for breach of contract, unpaid fees,
trademark infringement, and non-compete violations. Damages sought range from $69K to $467K. No lawsuits
filed against The Maids by franchisees. This pattern suggests the franchisor actively enforces its rights
post-termination. (p. 11)</p>

<h3>Confidentiality clauses</h3>
<p>Franchisees have signed confidentiality clauses that may restrict their ability to speak openly about
their experience — a structural obstacle to your due diligence, consistent across several brands in
this cohort.</p>
""",

"peer_narrative": """
<p>The Maids occupies a distinctive position in the cleaning cohort: lowest entry cost, highest ongoing fees,
and the only brand disclosing actual net profitability. It is the analytical buyer's paradox — the most
data to work with, paired with the most expensive operating structure.</p>

<p><strong>Closest comparison: Two Maids & A Mop.</strong> Similar fee burden profiles (both charge ~$30K/year
in mandatory local marketing). Two Maids is growing rapidly (+56.5% over 3 years) while The Maids is flat.
Two Maids' Item 19 provides gross margin data by quintile; The Maids provides a full company-owned P&L.
If you want profitability data, The Maids is better. If you want growth momentum, Two Maids wins.</p>

<p><strong>Sharpest contrast: MaidPro.</strong> MaidPro charges $30,000 at $300K revenue vs The Maids' $59,130
— a $29,130/year difference. Over a 10-year term, that gap represents $291,000 in additional fees paid to
The Maids' franchisor. MaidPro also discloses total revenue ($462K average). The question is whether The Maids'
company-owned P&L data and SMART Start bundling justify nearly double the ongoing cost.</p>

<p><strong>Scale consideration: The Maids' multi-territory math.</strong> The franchise fee discounts
(5-Pack at $38K/territory) and royalty pooling across territories create a multi-unit build strategy where
the economics improve dramatically. Company-owned offices averaging $1.4M across 5+ territories and netting
$220K/year show what the model looks like at scale. A single territory at $306K median revenue is a different
proposition entirely.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "The company-owned P&L shows 15.5% net margin, but company-owned offices may pay lower Continuing License Fee rates. What CLF rate do company-owned offices actually pay, and how does it compare to what franchisees at the same revenue level pay?",
        "context": "Item 19 Table III, pp. 47–48. CLF is shown as 5.4% of revenue for company-owned. Standard franchisee CLF at the same revenue level ($1.4M/office ÷ 5.2 territories = $274K/territory/week = ~$5,269/week) would be in the 6.9% bracket.",
        "follow_ups": [
            "Ask for the specific CLF rate in company-owned franchise agreements.",
            "Ask what the net margin would be if company-owned offices paid the standard 6.9% CLF rate.",
            "Ask whether franchisees can negotiate CLF rates at signing or renewal."
        ],
    },
    {
        "question": "The Local Marketing Requirement is $2,500/month ($30,000/year) for the first territory. What does a typical franchisee spend this on, and does the franchisor track the ROI of this mandatory spend?",
        "context": "Item 6, pp. 19–20. If not spent, franchisor may collect and spend on your behalf.",
        "follow_ups": [
            "Ask for examples of approved local marketing activities and their cost ranges.",
            "Ask what percentage of franchisees meet the Local Marketing Requirement through their own efforts vs having the franchisor spend on their behalf.",
            "Ask whether the $2,500/month minimum has been increased in the past 5 years."
        ],
    },
    {
        "question": "The franchisor's financial condition is flagged by multiple states as calling into question the ability to provide services and support. What specific steps has the franchisor taken to address this concern, and what is the current cash position?",
        "context": "FDD Special Risks, p. 5. Net loss of $(3.86M) in FY2025, member's deficit, $28.56M related-party debt.",
        "follow_ups": [
            "Ask whether the related-party debt is from Gladstone Management Corp or another entity, and what the repayment terms are.",
            "Ask whether any specific services or support programs have been reduced or discontinued due to financial constraints.",
            "Ask for the franchisor's projections for when it expects to return to profitability."
        ],
    },
    {
        "question": "The National Sales Center is mandatory for Year 1 and charges $60/week + $7.50/unsold quote + $36/sold quote. What does a typical new territory's Year 1 National Sales Center cost total?",
        "context": "Item 6, pp. 14, 20. Variable cost structure makes total unpredictable without quote volume data.",
        "follow_ups": [
            "Ask how many quotes per week a typical new territory receives through the Sales Center.",
            "Ask what the close rate is for Sales Center quotes vs franchisee-generated leads.",
            "Ask whether franchisees who opt out after Year 1 see a decline in lead volume."
        ],
    },
    {
        "question": "The per-territory median revenue is $306K (Table II) but company-owned offices average $274K per territory. Does the company-owned portfolio include territories of similar demographic and household profiles to available franchised territories?",
        "context": "Item 19, Tables II and III. 338 franchised territories, 31 company-owned territories in 6 states.",
        "follow_ups": [
            "Ask which states the company-owned territories are in.",
            "Ask whether company-owned territories were selected for their profitability or acquired through reacquisition of struggling franchisees."
        ],
    },
    {
        "question": "Table 3 arithmetic for FY2025 does not reconcile (338+9-11-0-2-0=334, but stated end count is 338). What accounts for the 4-unit gap?",
        "context": "Item 20, pp. 49–50. Likely includes company-to-franchisee territory sales not captured in standard columns.",
        "follow_ups": [
            "Confirm whether territories sold from company-owned to franchised are reflected in Table 3 or only in Table 4.",
            "Ask for a clean reconciliation of franchised unit changes for FY2025."
        ],
    },
],

},

"merry-maids": {

"executive_summary": """
<p>Merry Maids is the second-largest residential cleaning franchise in this cohort (802 units as of year-end
2024) and among the oldest (franchising since 1980). It is owned by Roark Capital through the ServiceMaster
securitization structure — not Neighborly/KKR (a common misconception). The system is in severe contraction:
989 to 802 units over three years, a net loss of 187 (-18.9%), with the decline accelerating each year
(-43, -62, -82). This is the most aggressive contraction trajectory in the cohort.</p>

<p>The Item 19 discloses total gross revenue for "Qualified Franchises" (306 of 802 units with 40,000+
Qualified Households): average $487,441, median $427,425. But 419 "Legacy Franchises" and 90 that ceased
operations during 2024 are excluded — survivorship bias is significant. The broader picture from Table 3
shows all 725 Active Franchises averaging $347,990 per franchise (median $262,519). The gap between
Qualified and all-franchise averages suggests Legacy territories substantially underperform.</p>

<p>The fee structure is mid-cohort: 11.0% at $300K with a 7% base royalty (discretionary incentive tiers at
$400K and $500K), 2% total marketing, and $499/month technology fee. The royalty incentive tiers are
explicitly discretionary — the franchisor may change or discontinue them at any time. This means the true
guaranteed ongoing rate is 9% (7% royalty + 2% marketing) plus technology, not the 6% or 5% that the
incentive tiers suggest at higher revenue.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$127K–$170K total investment. Mid-cohort. $55K flat franchise fee with multiple discount programs (military 20%, affiliate 15%, conversion 15%)."},
    {"dimension": "Ongoing fee burden", "rating": "Mixed", "color": "mixed",
     "summary": "11.0% at $300K. Mid-cohort. But royalty incentive tiers (6% and 5% at higher revenue) are discretionary and can be withdrawn at any time."},
    {"dimension": "System stability", "rating": "Weak", "color": "weak",
     "summary": "Severe contraction: -187 units over 3 years (-18.9%). 73 ceased operations in 2024 alone. Decline is accelerating, not stabilizing."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Total gross revenue by quartile for Qualified Franchises AND by Franchise Ownership Group size. Three tables with genuine analytical depth."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Severe survivorship bias: only 306 of 802 units in Table 1 (38.2%). 90 ceased businesses excluded. Confidentiality clauses restrict franchisee speech."},
    {"dimension": "Downside risk profile", "rating": "Weak", "color": "weak",
     "summary": "Accelerating contraction. 90 businesses ceased in 2024. Liquidated damages clause. Wisconsin risk disclosure explicitly warns of high turnover rate."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Strong brand recognition and established infrastructure. Multi-unit economics disclosed (FOG data). But system trajectory is concerning for long-term brand investment."},
    {"dimension": "Overall", "rating": "Caution", "color": "weak",
     "summary": "Meaningful revenue data offset by the most severe system contraction in the cohort. Qualified Franchise economics look viable ($487K average), but the system is losing units faster than any peer. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """Merry Maids has genuine strengths: a recognized brand, disclosed revenue data,
a clean direct litigation profile, and an established multi-unit operator ecosystem. But the system
contraction is severe and accelerating — 82 net unit losses in 2024 alone, with 73 businesses ceasing
operations. The Wisconsin risk disclosure explicitly warns that this franchise "could be a higher risk
investment than a franchise in a system with a lower turnover rate." When the state regulator adds a
warning label, read it carefully. Your diligence must focus on why units are exiting at this rate and
whether the available territories represent opportunity (former operators who failed for controllable
reasons) or signal (structural decline in the brand's competitiveness).""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Multi-unit operator seeking scale:</strong> The FOG (Franchise Ownership Group) data shows
top-quartile multi-unit operators averaging $2.24M in combined gross sales. The system is designed for
multi-territory ownership — 67% of operators hold 2+ territories.</li>
<li><strong>Resale buyer acquiring an existing operation:</strong> With 35 transfers in 2024 and the
independent MMFOA franchisee association, there is an active resale market. Buying an existing, cash-flowing
territory may be lower-risk than starting new in a contracting system.</li>
<li><strong>Conversion franchise buyer:</strong> 15% discount on franchise fee for conversion, plus
$250/customer acquisition fee for existing territory customers. If you already run a cleaning business,
the conversion path reduces entry cost and preserves revenue continuity.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>New-to-franchise buyer seeking system momentum:</strong> The system is contracting at an
accelerating rate. New unit openings (4, 13, 8 per year) are minimal compared to exits. If you want to
join a growing brand, Two Maids or The Cleaning Authority are expanding.</li>
<li><strong>Buyer relying on discretionary royalty tiers:</strong> The 6% and 5% incentive rates above
$400K and $500K are not guaranteed. If the franchisor discontinues them, your effective royalty jumps from
~6.3% blended to 7% flat at $500K — a $3,500/year increase. Do not build your financial model around
rates the franchisor can revoke.</li>
<li><strong>Single-territory buyer in a small market:</strong> If your territory has fewer than 40,000
Qualified Households, you are a "Legacy Franchise" — excluded from Table 1 of Item 19 entirely. You have
no disclosed revenue benchmarks for your territory type.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You understand why 73 businesses ceased operations in 2024 and whether the territories available to
you were among them. Ask the franchisor for the specific exit history of your proposed territory.</li>
<li>You have modeled your financials using the 7% base royalty, not the incentive tiers. If the incentive
rates hold, treat it as upside.</li>
<li>You have talked to current franchisees — acknowledging that confidentiality clauses may limit what
they share — about whether franchisor support quality has declined as the system contracts.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Merry Maids' fee burden is mid-cohort: 11.0% at $300K, declining to 10.0% at $500K if the discretionary
royalty incentive tiers hold. This places it slightly above Molly Maid (10.4%) and MaidPro (10.0%), but
well below The Maids (19.7%) and Two Maids (21.6%). The important caveat: the royalty incentive tiers that
reduce the rate from 7% to 6% ($400K–$500K) and 5% (above $500K) are explicitly discretionary. The
guaranteed fee floor is 9% of revenue (7% royalty + 2% marketing) plus $499/month technology.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (7% base, discretionary tiers):</strong> 7% of Gross Sales is the contractual base.
"Royalty Incentive" reduces to 6% on $400K–$500K and 5% above $500K — but the FDD states this incentive
"may be changed or discontinued at any time." National Account revenue excluded from tier calculation.
Resets each calendar year. Failure to timely renew franchise agreement triggers 2.5% royalty increase
(to 9.5%). (pp. 24, 30)</li>
<li><strong>Marketing (2% total):</strong> Clean split: 1.3% Ad Fund (national) + 0.7% Local Marketing
Obligation (must be spent on approved "Eligible Marketing"). If Local Marketing Obligation not met,
shortfall must be contributed to the Ad Fund. Plus $6,000 Initial Marketing Obligation in 120-day window
around opening. (pp. 24–25)</li>
<li><strong>Technology ($499/month):</strong> Per Franchised Business. Covers MM360 CRM, Service Mobility
software, Office 365, LMS, BI platform. Begins at signing (pre-opening). Additional QuickBooks license
~$475/year separate. (pp. 23, 25)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Merry Maids retains ~$267K after modelable franchisor
fees — comparable to Molly Maid (~$269K) and slightly less than MaidPro (~$270K). The gap is narrow at
this level. But if the royalty incentive is revoked, the $400K+ economics change: at $500K, you'd retain
~$450K with incentive tiers vs ~$443K without — a $7,000/year difference that compounds over a 10-year term.
</div>

<div class="callout">
<div class="callout-title">Late fees are unusually punitive</div>
Interest on unpaid balances: 2% per month compounded daily (24% APR) or max legal rate. Late fees: $200/week
for first 4 weeks, then $500/week, plus all costs including attorneys' fees. These are among the most
aggressive late-payment provisions in the cohort. If cash flow timing is tight (seasonal business, slow
ramp-up), these penalties can compound quickly. (p. 28)
</div>
""",

"item19_narrative": """
<p>Merry Maids' Item 19 provides three tables with meaningful analytical depth — but severe survivorship
bias limits how much you can trust the headline numbers. Understanding what is included and excluded is
as important as the numbers themselves.</p>

<h3>Table 1 — Qualified Franchises (306 of 802 units)</h3>
<ul class="compact">
<li><strong>Population:</strong> 306 "Qualified Franchises" — territories with 40,000+ Qualified Households
and office physically within the territory. This is 38.2% of total units.</li>
<li><strong>Average:</strong> $487,441. Median: $427,425.</li>
<li><strong>Top quartile (77 units):</strong> Average $919,797, median $854,086.</li>
<li><strong>Bottom quartile (77 units):</strong> Average $169,957, median $173,413. Low of $42,868.</li>
<li><strong>41.5% at or above the average</strong> — top-heavy distribution.</li>
</ul>

<h3>Table 2 — Franchise Ownership Groups (249 FOGs)</h3>
<ul class="compact">
<li><strong>Average FOG revenue:</strong> $1,047,237. Median: $767,299.</li>
<li>Multi-unit operators dominate: top 10% of FOGs average $3.23M.</li>
<li>67% of FOGs operate 2+ franchises — this is a multi-unit system.</li>
</ul>

<h3>Table 3 — Revenue by FOG size (the most revealing table)</h3>
<ul class="compact">
<li><strong>Single-unit FOGs (82):</strong> Average $547,630 per franchise. Median: $515,865.</li>
<li><strong>2-unit FOGs (70):</strong> Average $379,135 per franchise. Median: $339,229.</li>
<li><strong>5-7 unit FOGs (31):</strong> Average $299,005 per franchise. Median: $237,477.</li>
<li><strong>All 725 Active Franchises:</strong> Average $347,990. Median: $262,519.</li>
<li>Key insight: per-franchise revenue <strong>decreases</strong> as FOG size increases. Single-unit
operators have the highest per-franchise average ($548K) and median ($516K). Multi-unit operators spread
revenue across more territories, many of which are likely smaller Legacy territories.</li>
</ul>

<h3>What's excluded</h3>
<ul class="compact">
<li><strong>419 Legacy Franchises:</strong> Active but not "Qualified" (smaller territories, or office
outside territory). Excluded from Table 1 entirely. Their all-franchise average of $348K (Table 3) vs
Qualified average of $487K suggests they substantially underperform.</li>
<li><strong>90 businesses that ceased operations in 2024:</strong> Excluded from all tables. None opened
within 12 months prior to closing. This is severe survivorship bias — 90 closures from 802 units (11.2%)
are removed before calculating averages.</li>
<li><strong>No cost data:</strong> Revenue only. No COGS, margins, or profitability of any kind.</li>
</ul>
""",

"item19_triangulation": """
<h3>What the excluded units tell you</h3>
<p>The gap between Table 1 (Qualified, $487K average) and Table 3 all-franchise data ($348K average)
is $139K — a 28.5% difference. This means the 419 Legacy Franchises that are excluded from the headline
number significantly underperform the Qualified population. If you are offered a Legacy territory (under
40,000 QH), your closest revenue benchmark is the all-franchise Table 3 data, not the Table 1 headline.</p>

<p><strong>For a single-territory Qualified Franchise at the median ($427K):</strong></p>
<ul class="compact">
<li>Franchisor fees at 11.0%: ~$47K</li>
<li>Revenue after fees: ~$380K</li>
<li>Estimated COGS at 55% (industry norm, not disclosed): ~$235K</li>
<li>Remaining for overhead and owner draw: ~$145K</li>
<li>After overhead (rent $12K–$18K, insurance $5K–$10K, vehicle $6K–$10K, misc $5K–$8K):
~$99K–$112K for owner income before taxes</li>
</ul>

<p><strong>For a single-territory at the all-franchise median ($263K):</strong></p>
<ul class="compact">
<li>Franchisor fees at ~11%: ~$29K</li>
<li>Revenue after fees: ~$234K</li>
<li>Estimated COGS at 55%: ~$145K</li>
<li>Remaining: ~$89K</li>
<li>After overhead: ~$48K–$61K for owner income</li>
</ul>

<div class="implication">
<strong>What this means:</strong> The economics look viable at the Qualified Franchise median ($427K) but
tight at the all-franchise median ($263K). Given that 90 businesses closed in 2024 — and their revenue
is excluded from all tables — the actual distribution includes a significant tail of territories where
the economics did not work. If you are evaluating Merry Maids, focus on whether your proposed territory
resembles the Qualified population or the broader all-franchise population. The $140K gap between those
benchmarks is the difference between a viable and a marginal business.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It uses Merry Maids' disclosed Table 1 revenue for Qualified
Franchises (306 of 802 total units) and Table 3 all-franchise data. No cost data is disclosed — COGS
is estimated from industry norms. The royalty incentive tiers are discretionary and may be changed or
discontinued. Your actual results depend on territory size, local market conditions, labor costs, and
whether your territory qualifies as a "Qualified Franchise" or a Legacy territory.</p>
""",

"economics_scenarios_config": [
    ("All-franchise median (Table 3)", 263000),
    ("Qualified Franchise median (Table 1)", 427000),
    ("Single-unit FOG average (Table 3)", 548000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue from Item 19: all-franchise median from Table 3 ($262,519, rounded to $263K), Qualified Franchise median from Table 1 ($427,425, rounded to $427K), single-unit FOG average from Table 3 ($547,630, rounded to $548K). COGS estimated at 55% (cleaning industry norm — not disclosed by Merry Maids). Royalty modeled at 7% base rate (discretionary incentive tiers not included as they may be revoked). 'Remaining' must cover all overhead, taxes, and owner draw. 90 businesses that ceased operations in 2024 are excluded from all revenue benchmarks — survivorship bias applies.",

"investment_narrative": """
<p>Mid-cohort entry cost: $126,880–$170,110. The flat $55,000 franchise fee is straightforward, with
multiple discount programs: Military (20% off), Affiliate (15% — existing ServiceMaster/related brand
franchisee or employee), Conversion (15%), Industry Experience (5%). Actual fees collected in 2024
ranged from $18,750 to $49,500. An additional $250 per existing customer acquisition fee may apply if
the territory has active customers from a prior operator. (pp. 22–24)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise Fee ($55,000 flat):</strong> Fixed, nonrefundable, includes Initial Training for
two people. Multiple discounts available but only one may be used. Conversion franchisees (existing cleaning
businesses) get 15% off. At the military discount: $44,000. (pp. 22–23)</li>
<li><strong>Additional Funds — 3 months ($38,000–$43,000):</strong> Covers employee wages, payroll taxes,
uniforms, licenses, phone/internet/utilities, vehicle payments, bank charges, advertising, supplies, Technology
Fees, credit card processing. Does not include owner salary or draw. This is the largest single line item.
(pp. 31, 33)</li>
<li><strong>Professional Fees ($5,000–$15,000):</strong> Legal and accounting. The wide range suggests you
should budget for the high end if you want thorough FDD review and entity formation. (pp. 31, 33)</li>
<li><strong>Insurance ($3,400–$9,400):</strong> First-year prepayment including GL, auto, fidelity bond,
workers' comp, employment practices liability. Varies by state and payroll size. (pp. 31–32)</li>
<li><strong>Opening Marketing ($6,000–$8,000):</strong> Includes the mandatory $6,000 Initial Marketing
Obligation in the 120-day window around opening. (p. 31)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Plan for ~$149K at the midpoint. The franchise fee discounts (up to 20%)
can reduce total investment by $8K–$11K if you qualify. The Technology Fee ($499/month) begins at signing,
not at opening — so you'll pay $1,000–$1,500 in tech fees before the business generates any revenue.
Factor this into your pre-opening cash burn estimate.
</div>
""",

"system_health_narrative": """
<p>Merry Maids is experiencing the most severe system contraction in the residential cleaning cohort.
The system has shrunk from 989 to 802 units over three years — a net loss of 187 units (-18.9%). The
decline is accelerating: -43 (2022), -62 (2023), -82 (2024). In 2024 alone, 73 businesses ceased
operations (8.3% of start-of-year count), 10 were terminated, and 7 were not renewed. Only 8 new
franchises opened. Wisconsin's mandatory risk disclosure states this franchise "could be a higher risk
investment than a franchise in a system with a lower turnover rate." (pp. 4, 63–70)</p>
""",

"system_health_detail": """
<h3>Exit composition — an evolving pattern</h3>
<ul class="compact">
<li><strong>2022:</strong> 47 terminations, 0 non-renewals, 0 ceased operations, 18 transfers. Terminations
dominated — the franchisor was actively cutting underperformers.</li>
<li><strong>2023:</strong> 16 terminations, 24 non-renewals, 35 ceased operations, 66 transfers. A shift:
terminations dropped but non-renewals surged and "ceased operations" appeared for the first time. 66
transfers indicate massive ownership churn.</li>
<li><strong>2024:</strong> 10 terminations, 7 non-renewals, 73 ceased operations, 35 transfers. Ceased
operations exploded. The 73 businesses ceasing operations represent the largest single-year exit event
in this cohort by a wide margin.</li>
</ul>

<p>The shift from terminations (2022) to ceased operations (2024) suggests the exits are increasingly
voluntary — franchisees choosing to leave rather than being forced out. This is a more concerning pattern
than franchisor-initiated pruning, because it suggests operators are concluding the business is not viable.</p>

<h3>Geographic concentration of losses</h3>
<p>The contraction is nationwide but concentrated:</p>
<ul class="compact">
<li><strong>California:</strong> 137→89 over 3 years (-48 units, -35%).</li>
<li><strong>Pennsylvania:</strong> Accelerating losses: 2 (2022), 1 (2023), 9 (2024).</li>
<li><strong>New Jersey:</strong> 31→21 over 3 years (-10 units, -32%).</li>
<li><strong>Connecticut, Ohio, New York, Florida, Illinois:</strong> All lost 5–7 units in 2024 alone.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> This is not a regional problem — the contraction is systemic. A buyer
must understand whether the exits reflect (a) the franchise model no longer competing effectively in
those markets, (b) the Roark/ServiceMaster ownership structure extracting value rather than investing,
or (c) a natural portfolio reset after decades of growth. The answer determines whether the remaining
802 units represent a stabilized base or a system still mid-decline. With only 8 openings in 2024 and
1 signed-but-not-opened agreement, there is no visible growth pipeline.
</div>
""",

"risk_narrative": """
<h3>System contraction is the dominant risk</h3>
<p>187 net unit losses over 3 years (-18.9%), accelerating. 90 businesses ceased operations in 2024 and
are excluded from all Item 19 revenue data. The Wisconsin risk disclosure explicitly flags the high turnover
rate. For a prospective buyer, this is not background noise — it is the central fact that must be explained
before investing. (pp. 4, 63–70)</p>

<h3>Survivorship bias in Item 19</h3>
<p>Only 306 of 802 units (38.2%) are in Table 1. 419 Legacy Franchises and 90 ceased businesses are excluded.
The $487K average for Qualified Franchises may overstate what a typical operator experiences. The all-franchise
average of $348K (Table 3) is more representative but still excludes the 90 closures. The actual median
across all 802 units — including those that closed — is unknowable from the FDD. (pp. 58–62)</p>

<h3>Discretionary royalty tiers</h3>
<p>The 6% ($400K–$500K) and 5% (above $500K) incentive rates are discretionary and "may be changed or
discontinued at any time." Do not model your economics around these rates. If revoked at $500K revenue,
your annual royalty increases by $3,500. (pp. 24, 30)</p>

<h3>Ownership structure</h3>
<p>Merry Maids is owned by RW Purchaser LLC / Roark Capital Management through the ServiceMaster securitization
structure. This is <strong>not</strong> the same ownership as Molly Maid (Neighborly/KKR). Roark Capital is
a PE firm — typical implications include financial engineering, cost discipline, and potential for brand
flipping or portfolio restructuring. The system contraction pattern is consistent with PE-style portfolio
optimization. (p. 9)</p>

<h3>Confidentiality clauses</h3>
<p>Current and former franchisees have signed confidentiality provisions restricting their ability to speak
openly about their experience. MMFOA (Merry Maids Franchise Owners Association) exists through AAFD as an
independent organization — its existence may indicate franchisee-franchisor tensions worth investigating.</p>

<h3>Liquidated damages</h3>
<p>If terminated for default: average monthly Royalties and Ad Fund Contributions over the past 12 months ×
the lesser of remaining term or 24 months. At $400K revenue with 24 months: ~$14,400 ($600/month × 24).
Less punitive than The Maids' formula but still a meaningful exit cost. (p. 29)</p>
""",

"peer_narrative": """
<p>Merry Maids is the second-largest system in the cohort by unit count but the fastest-shrinking by
percentage (-18.9% over 3 years). It offers disclosed revenue data, a mid-cohort fee structure, and
deep multi-unit operator economics — but the contraction trajectory dominates the competitive picture.</p>

<p><strong>Closest comparison: Molly Maid.</strong> Similar scale, similar age, similar system contraction
(though Molly Maid's is less severe at -10.6%). Molly Maid does not disclose total revenue; Merry Maids
does ($487K Qualified, $348K all-franchise). Molly Maid has slightly lower modelable fees (10.4% vs 11.0%
at $300K). Both are PE-backed legacy brands losing units. If revenue disclosure matters, Merry Maids provides
more. If stability matters, Molly Maid is contracting more slowly.</p>

<p><strong>Sharpest contrast: Two Maids & A Mop.</strong> Growing 56.5% while Merry Maids shrinks 18.9%.
Two Maids charges significantly higher fees (21.6% vs 11.0% at $300K) but provides richer disclosure and
growth momentum. If you believe the cleaning franchise market is growing, Two Maids is the growth bet.
If you believe established territories are the value play, Merry Maids' resale market (35 transfers in
2024) offers entry points.</p>

<p><strong>Lower-risk alternative: MaidPro.</strong> Simpler fees (10.0% at $300K), disclosed revenue ($462K
average), stabilizing system (237 units, net zero change in 2024), and declining turnover (8.4%). If Merry
Maids' brand recognition is not worth the contraction risk, MaidPro is the less dramatic option.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "73 businesses ceased operations in 2024 — the largest single-year exit in the cohort. What were the primary reasons these operators exited, and how many were Legacy vs Qualified Franchises?",
        "context": "Item 20, pp. 63–70. 'Ceased operations — other reasons' surged from 0 (2022) to 35 (2023) to 73 (2024).",
        "follow_ups": [
            "Ask for a state-by-state breakdown of the 73 ceased operations.",
            "Ask what the average tenure of the 73 operators was — were they long-standing franchisees exiting or newer operators failing?",
            "Ask what the average revenue of the ceased operations was before they exited."
        ],
    },
    {
        "question": "The Royalty Incentive tiers (6% at $400K–$500K, 5% above $500K) are discretionary and may be changed or discontinued at any time. Has the franchisor ever changed or discontinued these tiers?",
        "context": "Item 6, pp. 24, 30. Incentive applied per individual Franchised Business per calendar year.",
        "follow_ups": [
            "Ask whether the franchisor has committed to maintaining these tiers for any specific period.",
            "Ask what percentage of Qualified Franchises currently benefit from the 6% or 5% tiers.",
            "Ask whether the royalty rate increase for failure to timely renew (to 9.5%) has been enforced."
        ],
    },
    {
        "question": "Table 1 covers only 306 'Qualified Franchises' of 802 total. What is the average and median gross revenue for the 419 Legacy Franchises?",
        "context": "Item 19, pp. 58–62. Legacy Franchises = Active but not meeting current 40K+ Qualified Household standard or office-within-territory requirement.",
        "follow_ups": [
            "Ask what the plan is for Legacy territories — are they being phased out, consolidated, or converted to Qualified standards?",
            "Ask whether a buyer can purchase a Legacy territory or whether all new sales are Qualified-standard territories."
        ],
    },
    {
        "question": "The MMFOA (Merry Maids Franchise Owners Association) is an independent franchisee organization through AAFD. What is the franchisor's relationship with the MMFOA, and what are the primary concerns franchisees have raised?",
        "context": "FDD reference to independent franchisee organizations.",
        "follow_ups": [
            "Ask whether the franchisor engages in regular dialogue with the MMFOA.",
            "Ask whether any MMFOA grievances have resulted in system-wide policy changes."
        ],
    },
    {
        "question": "90 businesses ceased operations during 2024 and are excluded from all Item 19 tables. If their revenue were included, how would the system-wide average and median change?",
        "context": "Item 19, pp. 58–59. Survivorship bias from excluding 11.2% of units.",
        "follow_ups": [
            "Ask whether the 90 ceased businesses were generating revenue in 2024 before they ceased — and if so, how much.",
            "Ask whether the franchisor has analyzed what revenue level is the 'break-even floor' below which operators typically exit."
        ],
    },
    {
        "question": "Only 8 new franchises opened in 2024, and only 1 agreement is signed but not yet open. What is the franchisor's growth strategy — is the focus on new sales, resales to existing operators, or territory consolidation?",
        "context": "Item 20, pp. 63–70. Projected 7 new openings in 2025.",
        "follow_ups": [
            "Ask what the franchisor's target system size is for the next 3–5 years.",
            "Ask whether Roark Capital has a stated investment thesis for Merry Maids — growth, optimization, or divestiture."
        ],
    },
],

},

"maidpro": {

"executive_summary": """
<p>MaidPro is a 29-year-old residential cleaning franchise (MaidPro Franchise, LLC / Threshold Brands /
The Riverside Company) with 237 outlets as of year-end 2024. The system has stabilized after modest
contraction: 246 to 241 to 237 to 237 over three years, with net zero change in 2024. Turnover has
improved significantly — 15.0% to 12.4% to 8.4% — the strongest improving-turnover trend in the cohort
alongside The Maids.</p>

<p>MaidPro has the simplest fee structure in the residential cleaning cohort: 6% flat royalty, 2% Brand
Fund, $500/month technology fee. No mandatory local marketing percentage, no DHH-based fees, no contact
center surcharges, no escalating weekly minimums. At $300K revenue, total fees are $30,000 (10.0%) —
the lowest fully-transparent burden in the cohort (The Cleaning Authority models lower at 7.6%, but its
DHH-based Local Marketing Fee is excluded — see that report for details). At $500K, fees are $46,000 (9.2%).
The simplicity is itself a competitive advantage: you can model your economics without hidden fee layers
or territory-size-dependent variables.</p>

<p>The Item 19 discloses total gross revenue by quartile for 231 outlets: system average $461,941, median
$397,548. The dispersion is wide (Q1 average $958K vs Q4 average $134K), and only 42% of outlets exceed
the average — a top-heavy distribution. No cost data is disclosed. The franchise offers a Franchise Option
Program ($0 franchise fee in exchange for 10% royalty for 10 years) and a Conversion Program (2% royalty
for first 2 years), creating distinct fee tiers within the system.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$110K–$159K total investment. Mid-cohort. $45K franchise fee with military (20%), multi-unit (25%), and conversion (full waiver) discounts available."},
    {"dimension": "Ongoing fee burden", "rating": "Strong", "color": "strong",
     "summary": "Lowest fully-transparent fee burden in cohort (TCA models lower but excludes its DHH-based Local Marketing Fee). 10.0% at $300K, 9.2% at $500K. Simplest structure — no hidden layers."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Stabilized at 237 units after modest contraction (-9 over 3 years, -3.7%). Turnover improving: 15.0%→12.4%→8.4%. Net zero change in 2024 is a positive inflection."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Total gross revenue by quartile for 231 outlets. System average $462K, median $398K. Clear, comparable data."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Table 1 has a typographical error (mislabeled year). Territory definition changed in 2023 (~45K QH at $100K+ income). Confidentiality clauses present. 7 closures excluded."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Wide revenue dispersion (Q1 7.1× Q4). Bottom quartile average of $134K may not support fee obligations. Franchise Option Program creates 10% royalty cohort within system."},
    {"dimension": "Buyer fit breadth", "rating": "Strong", "color": "strong",
     "summary": "Lowest fully-modelable fee burden and simplest structure in cohort. Multiple entry paths (standard, conversion, franchise option). Works for budget-sensitive and control-oriented buyers."},
    {"dimension": "Overall", "rating": "Favorable", "color": "strong",
     "summary": "The cleanest fee structure and lowest fully-modelable ongoing cost in the cohort, paired with disclosed revenue and a stabilizing system. The trade-off is less franchisor-managed marketing infrastructure and a smaller system than legacy competitors. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """MaidPro is the simplest franchise in this cohort to model: flat 6% royalty, 2% brand
fund, $500/month tech fee, and that's it. No DHH-based marketing fees, no contact center surcharges, no
escalating weekly minimums. You can calculate your total franchisor obligation in 30 seconds. The fee
advantage is real — $29K/year less than The Maids and $35K/year less than Two Maids at $300K revenue. The
trade-off: MaidPro's marketing infrastructure is thinner than brands that charge for managed local advertising,
and the system is smaller. You are paying less but getting less franchisor-directed marketing support. If
you want to control your own marketing spend and keep more of what you earn, MaidPro is the cohort's
strongest argument for that approach.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Cost-conscious buyer who wants to keep more revenue:</strong> MaidPro retains the most revenue
for the franchisee at every modeled level. At $500K, you keep $454K after franchisor fees. At Two Maids,
you'd keep $419K. That $35K/year gap compounds.</li>
<li><strong>Marketing-independent operator:</strong> No mandatory franchisor-managed local advertising program.
The $3,000/month local ad minimum for the first 24 months is a spend requirement, not a payment to the
franchisor. You choose where and how to advertise.</li>
<li><strong>Conversion franchise buyer:</strong> The Conversion Program waives the franchise fee entirely
and reduces royalty to 2% for the first 2 years. If you already run a cleaning business, this is the
lowest-friction entry in the cohort.</li>
<li><strong>Buyer who values fee transparency:</strong> Every fee is predictable and calculable. No territory-
size-dependent marketing costs, no contact center escalators, no discretionary royalty adjustments.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Buyer who wants franchisor-managed marketing:</strong> MaidPro does not run your local advertising
for you. The optional TMS Connect Internet Presence service is $90/month, SEO is $305/month — but these
are opt-in, not managed programs. If you want the franchisor to handle lead generation, Two Maids or
The Cleaning Authority offer more managed infrastructure (at higher cost).</li>
<li><strong>Buyer seeking large-system brand recognition:</strong> 237 outlets is smaller than Molly Maid
(448), Merry Maids (802), or The Maids (369). If national brand awareness is a priority, larger systems
offer more. MaidPro's recognition is regional, not national.</li>
<li><strong>Risk-averse buyer focused on bottom-quartile outcomes:</strong> Q4 average revenue is $134K
with a low of $14,440. At that level, franchisor fees ($22K/year) consume 16% of gross revenue before
any operating costs. The bottom quartile of MaidPro is not viable as a standalone business.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You are comfortable managing your own local marketing. The fee savings versus managed-marketing brands
assume you can generate leads efficiently on your own or through the optional MaidPro tools.</li>
<li>You have evaluated whether the Franchise Option Program (10% royalty for 10 years) or the standard
program (6% royalty, $45K fee) is better for your cash flow profile. At $400K revenue, the crossover
is ~7.5 years — after that, the standard program saves money.</li>
<li>You understand that territory definitions changed in January 2023 (~45K QH at $100K+ income), which
means historical performance data from pre-2023 territories may not be comparable to current offerings.</li>
</ul>
""",

"fee_burden_narrative": """
<p>MaidPro has the lowest fully-transparent ongoing fee burden in the residential cleaning cohort at every modeled revenue
level: 11.0% at $200K, 10.0% at $300K, 9.5% at $400K, 9.2% at $500K. The gap versus competitors is
significant — $29,130/year less than The Maids and $34,800/year less than Two Maids at $300K. The primary
reason: no mandatory local marketing program payable to the franchisor. MaidPro charges a flat 2% Brand
Fund and leaves local marketing to the franchisee.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (6% flat):</strong> Simplest royalty in the cohort. No tiers, no brackets, no discretionary
incentives, no resets. 6% of monthly Gross Consumer Sales. Minimum Royalty of $800/month applies after
12 months if sales fall below $15,000/month. Premium Royalty of 2.5% on out-of-territory customers
(with franchisor permission). (pp. 10, 13–14)</li>
<li><strong>Brand Fund (2% flat):</strong> Monthly. Straightforward. No additional local marketing percentage
to the franchisor. The mandatory $3,000/month local advertising spend for the first 24 months is a franchisee-
directed requirement, not a payment to the franchisor. (pp. 10, 14)</li>
<li><strong>Technology ($500/month):</strong> Covers proprietary cloud-based software (4 licenses), branded
email (4 licenses), MACS marketing tool, and 1-800 customer service number. Waived for second and subsequent
MaidPro franchises. May increase up to 10% per year compounding. (pp. 12–14, 16)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, you retain ~$270K after franchisor fees. At Merry Maids
(next comparable): ~$267K. At The Maids: ~$241K. At Two Maids: ~$235K. The MaidPro advantage is modest vs
Merry Maids and Molly Maid but dramatic vs The Maids and Two Maids. Over a 10-year term at $300K revenue,
the cumulative fee difference vs The Maids is $291,300. That is real money.
</div>

<div class="callout">
<div class="callout-title">Two hidden fee structures within the system</div>
MaidPro has two alternative fee programs that create different cost profiles for different operators:
(1) Franchise Option Program: $0 franchise fee but 10% royalty for 10 years (vs standard 6%). At $400K
revenue, the annual cost difference is $16,000/year — the $45K franchise fee is recovered in under 3 years.
After Year 3, the standard program saves money every year. (2) Conversion Program: franchise fee waived,
2% royalty for first 2 years. These operators are included in the Item 19 data — their economics differ
from standard franchisees. (pp. 8–9)
</div>
""",

"item19_narrative": """
<p>MaidPro's Item 19 discloses total Gross Consumer Sales and number of jobs for 231 franchised outlets
open the full calendar year 2024. It is straightforward and comparable — a single table with system-wide
and quartile breakdowns, plus a separate section for operators reporting from two combined territories.</p>

<h3>System-wide performance</h3>
<ul class="compact">
<li><strong>Average Gross Consumer Sales:</strong> $461,941. Median: $397,548.</li>
<li><strong>Range:</strong> $14,440 to $2,815,974. Extremely wide.</li>
<li><strong>42% at or above average</strong> — top-heavy distribution driven by high performers.</li>
<li><strong>Average jobs:</strong> 2,644. Implied average revenue per job: ~$175.</li>
</ul>

<h3>By quartile</h3>
<ul class="compact">
<li><strong>Q1 (53 outlets):</strong> Average $958,412, median $891,162. Range: $659K–$2.82M.</li>
<li><strong>Q2 (53 outlets):</strong> Average $520,615, median $515,502. Range: $415K–$653K.</li>
<li><strong>Q3 (53 outlets):</strong> Average $312,844, median $318,560. Range: $225K–$406K.</li>
<li><strong>Q4 (52 outlets):</strong> Average $134,476, median $139,439. Range: $14K–$222K.</li>
</ul>

<h3>What this tells you</h3>
<ul class="compact">
<li>The Q1-to-Q4 ratio is 7.1:1 ($958K vs $134K). This is among the widest dispersions in the cohort.</li>
<li>Q2 and Q3 are relatively tight ($313K–$521K) — suggesting a "middle band" of $300K–$500K as the
realistic range for an established single-territory operator.</li>
<li>Q4 includes outlets generating as little as $14K — some may be part-time, winding down, or in the
Conversion/Franchise Option Program with different operating profiles.</li>
</ul>

<h3>What's missing</h3>
<ul class="compact">
<li><strong>Any cost data:</strong> No COGS, no gross margin, no expense breakdown. Cannot assess
profitability from the FDD alone.</li>
<li><strong>Revenue by territory age/tenure:</strong> Unlike The Cleaning Authority or Two Maids, MaidPro
does not break out revenue by how long the territory has been operating. You cannot see the ramp curve.</li>
<li><strong>Survivorship bias:</strong> 7 outlets that permanently closed in 2024 are excluded. 6 that
opened during 2024 (not full year) are also excluded. Smaller exclusion count than Merry Maids (90) or
Molly Maid (25).</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross revenue to owner economics</h3>
<p>MaidPro does not disclose costs. Using industry-norm estimates:</p>

<p><strong>At the system median ($398K):</strong></p>
<ul class="compact">
<li>Franchisor fees at 10%: ~$40K</li>
<li>Revenue after fees: ~$358K</li>
<li>Estimated COGS at 55% (cleaning industry norm): ~$219K</li>
<li>Remaining for overhead and owner draw: ~$139K</li>
<li>After overhead (rent $12K–$18K, insurance $4K–$8K, vehicle $5K–$8K, local marketing $18K–$36K,
misc $4K–$6K): ~$63K–$96K for owner income before taxes</li>
</ul>

<p><strong>At Q3 average ($313K):</strong></p>
<ul class="compact">
<li>Franchisor fees: ~$31K. Revenue after fees: ~$282K.</li>
<li>COGS at 55%: ~$172K. Remaining: ~$110K.</li>
<li>After overhead ($43K–$76K): ~$34K–$67K for owner income.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> MaidPro's fee advantage translates to approximately $5K–$15K more in
annual owner income compared to mid-range competitors at the same revenue level. The advantage grows
at lower revenue levels where MaidPro's lack of fixed-dollar marketing fees (no $30K/year local marketing
program) matters most. At $300K, the fee difference vs The Maids is $29K — potentially the difference
between a viable and an unviable business.
</div>

<div class="callout">
<div class="callout-title">The $3,000/month local marketing question</div>
MaidPro requires $3,000/month in local advertising for the first 24 months — $72,000 over two years. This
is a spend requirement, not a fee to the franchisor. After 24 months, the Manuals govern the spend amount
(not disclosed). The critical question for your model: what is the required local marketing spend after
Month 24? If it drops to $1,000/month, your Year 3+ costs improve materially. If it remains at $3,000/month,
MaidPro's true ongoing cost is closer to competitors than the modelable fees suggest.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It uses MaidPro's disclosed Item 19 revenue data (231 outlets,
calendar year 2024). No cost data is disclosed — COGS and overhead are estimated from industry norms.
Conversion franchisees (2% royalty) and Franchise Option Program participants (10% royalty) are included
in the revenue data — their economics differ from standard 6% franchisees. Your actual results depend on
your territory, labor market, marketing effectiveness, and operating model.</p>
""",

"economics_scenarios_config": [
    ("Q4 average", 134000),
    ("Q3 average", 313000),
    ("System median", 398000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue from Item 19 quartile data (CY2024, 231 outlets). COGS estimated at 55% (cleaning industry norm — not disclosed by MaidPro). Franchisor fees at standard 6% royalty + 2% Brand Fund + $500/mo tech = varies by revenue level. 'Remaining' must cover local marketing (minimum $3,000/month for first 24 months), overhead, taxes, and owner draw. Q4 scenario may include part-time, winding-down, or alternative-fee-program operators.",

"investment_narrative": """
<p>Mid-cohort entry cost: $109,860–$158,650. The $45,000 franchise fee is competitive (below Merry Maids'
$55K, The Maids' $60K, and Molly Maid's $60K–$85K combined fees). Multiple programs reduce or eliminate
the fee: Military/First Responder (20% off first franchise), Multi-Unit (25% off 2nd+ if 3+ purchased
simultaneously), Conversion (full waiver), Franchise Option ($0 fee, 10% royalty for 10 years). (pp. 8–9)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($45,000):</strong> Due at signing, nonrefundable. Training for 2 included. The
Franchise Option Program refunds this fee at opening in exchange for 10% royalty (vs 6%) for 10 years —
a meaningful cash-flow alternative for capital-constrained buyers. (pp. 8–9)</li>
<li><strong>Advertising — Initial 3 months ($15,000):</strong> Mandatory $3,000/month local advertising
for first 24 months. Item 7 captures only the first 3 months ($15,000). Total first-year local ad cost:
$36,000. Total 24-month commitment: $72,000. This is the largest ongoing cost commitment and is separate
from franchisor fees. (p. 17)</li>
<li><strong>Cost for initial vehicle with wrap ($5,300–$28,000):</strong> Widest range of any line item.
Low is lease/financed used vehicle; high is new vehicle purchase. Must display MaidPro car wrap. (p. 17)</li>
<li><strong>Additional Funds — 3 months ($18,800–$23,000):</strong> Includes payroll, insurance, professional
fees, monthly Technology Fee. Does not include owner salary. (p. 17)</li>
<li><strong>Insurance ($2,000–$12,000):</strong> Varies widely by state, payroll, and employee count.
Workers' comp and third-party bonding ($25K per loss) required. (pp. 17–19)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Plan for ~$134K at the midpoint. The Franchise Option Program ($0 fee)
reduces cash-at-signing by $45K but increases ongoing costs by $16K/year at $400K revenue ($40K vs $24K
royalty). The crossover point where the standard program becomes cheaper is approximately Year 2.8 at $400K
revenue. Most buyers who can afford the $45K fee upfront should pay it — the 10-year commitment to 10%
royalty is a steep long-term cost.
</div>
""",

"system_health_narrative": """
<p>MaidPro's system is stabilizing after modest contraction. Unit count declined from 246 to 237 over
three years (-3.7%), but 2024 showed net zero change — the first year without net losses. Turnover has
improved significantly: 15.0% (2022) to 12.4% (2023) to 8.4% (2024). The trajectory is positive.
Terminations dropped from 13 to 9 to 4 over the period. Only 7 outlets permanently closed in 2024 —
the lowest exit count in the cohort relative to system size.</p>
""",

"system_health_detail": """
<h3>Modest, stabilizing system</h3>
<ul class="compact">
<li><strong>2022:</strong> 19 opened, 13 terminated, 11 ceased, 13 transferred. Net: -5.</li>
<li><strong>2023:</strong> 12 opened, 9 terminated, 6 ceased, 1 non-renewal, 14 transferred. Net: -4.</li>
<li><strong>2024:</strong> 7 opened, 4 terminated, 3 ceased, 13 transferred. Net: 0.</li>
</ul>
<p>The key trend: exits are declining (37 → 30 → 20) while new openings have slowed (19 → 12 → 7).
The system reached equilibrium in 2024 — not through growth, but through reduced churn. (pp. 40–46)</p>

<h3>Active transfer market</h3>
<p>13 transfers per year across the period — consistent and substantial relative to the 237-unit system
(5.5% transfer rate). This suggests territories have resale value and an established ownership turnover
mechanism. The $5,000 flat transfer fee is the lowest in the cohort — significantly below Molly Maid
($15,000), The Maids ($15,000), and Two Maids ($25K–$50K). Low transfer friction is a positive signal
for exit optionality.</p>

<h3>Projected growth</h3>
<p>4 new outlets projected (CO, CT, FL ×2), plus 2 signed-but-not-opened (IL, OH). Modest pipeline but
consistent with a system that is not aggressively expanding. (pp. 45–46)</p>

<div class="implication">
<strong>What this means:</strong> MaidPro is not a growth story. It is a stability story. The system
found its floor in 2024 at 237 units. Turnover is dropping. The $5,000 transfer fee means exits are
low-friction. For a buyer, the relevant question is whether 237 units is a stable base or a pause before
further decline. The turnover trajectory (15% → 8.4%) strongly favors the stable-base interpretation.
</div>

<h3>No company-owned outlets</h3>
<p>Zero company-owned locations. All 237 outlets are franchised. The franchisor is not competing with
its franchisees. (pp. 40–46)</p>
""",

"risk_narrative": """
<h3>Revenue dispersion is the primary economic risk</h3>
<p>The 7.1:1 ratio between Q1 ($958K) and Q4 ($134K) average revenue means outcomes vary enormously.
Q4's average of $134K — with a low of $14K — represents a cohort of operators for whom the franchise
is not working as a full-time business. At $134K revenue, franchisor fees ($22K), estimated COGS ($74K),
and basic overhead ($30K+) leave effectively nothing for owner income. The question is whether Q4
territories are failing due to market conditions, operator execution, or structural issues with certain
territory types. (pp. 38–40)</p>

<h3>Territory definition change</h3>
<p>In January 2023, MaidPro changed its territory definition to ~45,000 Qualified Households with
$100K+ household income (previously 20K–80K QH with $75K+ income). This means territories sold before
2023 may be structurally different from current offerings. Older territories could be significantly
smaller or in lower-income markets. The Item 19 data includes all 231 outlets regardless of territory
definition — historical territories may drag averages. (pp. 38, 40)</p>

<h3>Franchise Option Program creates a split system</h3>
<p>Operators who chose the Franchise Option Program ($0 fee, 10% royalty for 10 years) pay 67% more
in royalties than standard operators at the same revenue level. They are included in the Item 19 revenue
data but their cost structure is materially different. A buyer comparing themselves to the system average
must account for the fact that some peers are paying 6% royalty and others are paying 10%. (pp. 8–9)</p>

<h3>Litigation: effectively clean</h3>
<p>Single disclosed arbitration — MaidPro vs former franchisee for unpaid fees and non-compete violation.
Settled within 3 months (June 2024). No pending matters. No regulatory actions. This is the lightest
litigation profile in the cohort. (p. 8)</p>

<h3>Independent franchisee association</h3>
<p>Maid Together Franchisee Association Inc. exists as an independent organization. Independent franchisee
associations sometimes form in response to franchisor-franchisee tensions. The FDD does not provide details
on the association's membership or concerns. Ask about its role during your diligence.</p>

<h3>Confidentiality clauses</h3>
<p>Current and former franchisees have signed provisions restricting their ability to speak openly — a
due diligence obstacle consistent across several brands in this cohort.</p>
""",

"peer_narrative": """
<p>MaidPro has the simplest and lowest fully-modelable fee structure in the residential cleaning cohort. It offers fee
transparency that no competitor matches, disclosed revenue data, a stabilizing system, and the lowest
transfer fee ($5K). It is the anti-complexity choice.</p>

<p><strong>Closest comparison: Molly Maid.</strong> Similar fee burden (10.0% vs 10.4% at $300K), similar
system trajectory (both stabilizing after contraction). Molly Maid has more brand recognition and
Neighborly infrastructure but does not disclose total revenue. MaidPro discloses revenue and has simpler
fees. Molly Maid offers the bigger brand name; MaidPro offers more transparency and simplicity.</p>

<p><strong>Sharpest contrast: The Maids.</strong> The Maids charges $59,130 at $300K vs MaidPro's $30,000 —
nearly double. The Maids provides a company-owned P&L (15.5% net margin) that MaidPro cannot match.
The question: is The Maids' profitability data worth $29K/year more in fees? For an analytical buyer
who values data, possibly. For a cost-conscious buyer, MaidPro's fee advantage is transformative.</p>

<p><strong>Growth alternative: Two Maids & A Mop.</strong> If you want a franchise that is growing rapidly
and provides franchisor-managed marketing, Two Maids is the opposite end of the spectrum. You pay 21.6%
of revenue at $300K (vs MaidPro's 10.0%) but get managed advertising, richer disclosure, and system
momentum. MaidPro is the DIY bet; Two Maids is the managed bet.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "The mandatory local advertising spend is $3,000/month for the first 24 months. What is the required spend after Month 24, and who determines it?",
        "context": "Item 6, pp. 14, 17. After 24 months, 'Manuals govern local spend amount' — not specified in FDD.",
        "follow_ups": [
            "Ask what the current Manual specifies as the post-24-month local advertising minimum.",
            "Ask whether the franchisor can increase this requirement without franchisee consent.",
            "Ask what a typical mature MaidPro territory spends on local marketing annually."
        ],
    },
    {
        "question": "Q4 outlets average $134K in revenue with a low of $14K. How many of the 52 Q4 outlets are Franchise Option Program participants (10% royalty), Conversion Program operators (2% royalty), or standard franchisees (6% royalty)?",
        "context": "Item 19, pp. 38–40. Three distinct fee structures coexist in the system. Program participation likely correlates with performance.",
        "follow_ups": [
            "Ask what the average revenue is for standard-program franchisees specifically (excluding Conversion and Franchise Option).",
            "Ask how many outlets are currently on each fee program.",
            "Ask whether any Q4 outlets are being supported or placed on performance improvement plans."
        ],
    },
    {
        "question": "Territory definitions changed in January 2023 to ~45K Qualified Households at $100K+ income. How many of the 231 reporting outlets are on the old territory definition vs the new one?",
        "context": "Item 19 footnotes, pp. 38, 40. Historical territories ranged from 20K–80K QH at $75K+ income.",
        "follow_ups": [
            "Ask whether franchisees on old territory definitions can be redefined to the new standard.",
            "Ask whether the revenue dispersion (Q1 vs Q4) correlates with territory definition vintage."
        ],
    },
    {
        "question": "The $5,000 transfer fee is the lowest in the cohort. What has been the typical resale price for MaidPro territories that transferred in 2024, expressed as a multiple of trailing 12-month revenue?",
        "context": "Item 20, pp. 40–46. 13 transfers in 2024.",
        "follow_ups": [
            "Ask whether the franchisor maintains a resale listing service or facilitates introductions between sellers and buyers.",
            "Ask how long a typical transfer process takes from listing to closing."
        ],
    },
    {
        "question": "The Franchise Option Program charges 10% royalty for 10 years in exchange for $0 franchise fee. How many current operators are on this program, and what is their average revenue compared to standard franchisees?",
        "context": "Item 5, pp. 8–9. $45K franchise fee refunded at opening, replaced by 10% royalty.",
        "follow_ups": [
            "Ask whether Franchise Option participants can convert to the standard 6% royalty by paying the $45K fee later.",
            "Ask what percentage of new franchisees in 2023–2024 chose the Franchise Option vs standard program."
        ],
    },
    {
        "question": "The Maid Together Franchisee Association exists as an independent organization. What is the association's current focus, and does the franchisor engage with it on policy decisions?",
        "context": "FDD reference to independent franchisee organization.",
        "follow_ups": [
            "Ask whether any MTFA concerns have resulted in system-wide changes.",
            "Ask what the membership rate is among the 237 franchisees."
        ],
    },
],

},

"maid-right": {

"executive_summary": """
<p>Maid Right is a small, founder-led residential cleaning franchise (Maid Right, LLC / Premium Service
Brands / PSB Group) with 35 outlets as of year-end 2024 — down from 44 the prior year. It is the smallest
system in this cohort by a wide margin (the next smallest is MaidPro at 237) and the only non-PE-backed
brand. The system grew from 24 to 44 units over 2022–2023, then contracted to 35 in 2024 — a net loss
of 9 units in a single year, the first year of terminations (6). Turnover rates are extraordinary:
37.8% (2023) and 38.6% (2024).</p>

<p>The Item 19 discloses total gross sales for 20 franchised businesses operated by 18 franchisees:
average $520,441, median $356,020. But only 18 of 39 total franchisees (46%) are included — 21 franchisees
operating 30 businesses are excluded for not operating the full year or not using CRM software properly.
The exclusion rate is itself a significant signal about system maturity and data infrastructure.</p>

<p>The fee structure is deceptively complex. The headline royalty (6%) and marketing (2%) rates are
competitive, but mandatory weekly service fees — Technology ($210/week), Contact Center ($220/week
minimum at Year 5), and Accounting/Business Advisory ($85/week) — add $295/week ($15,340/year) in
fixed costs paid to the franchisor regardless of revenue. At $300K revenue, total franchisor fees reach
$50,780 (16.9%). At $200K, they spike to 21.4%. This places Maid Right's fee burden third-highest in
the cohort — above Merry Maids, Molly Maid, and MaidPro — despite a nominally "low" royalty rate.</p>

<p>The most significant risk factors are not economic but organizational: CEO Paul Flick was barred from
offering or selling franchises in California for 36 months. Affiliate entities under the same parent
(360 Painting, Rooterman, Window Gang) have been the subject of regulatory actions in 6 states for FDD
disclosure failures. The franchisor's financial condition is flagged by state regulators. Confidentiality
clauses restrict current and former franchisees from speaking openly. These are not hypothetical risks —
they are documented regulatory findings about the parent organization's compliance culture.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$147K–$219K total investment. Highest in cohort. $65K standard franchise fee plus $5K technology fee at signing."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "Third-highest in cohort (16.9% at $300K). Nominal 6% royalty is masked by $295/week in mandatory fixed service fees (tech + contact center + accounting)."},
    {"dimension": "System stability", "rating": "Weak", "color": "weak",
     "summary": "35 units, contracting. 38.6% turnover in 2024. First-ever terminations (6) in 2024. System grew then shrank — classic early-franchise volatility."},
    {"dimension": "Revenue disclosure", "rating": "Mixed", "color": "mixed",
     "summary": "Item 19 has 4 tables with quartile, tenure, and service-type data. But only 46% of franchisees included. 86% recurring revenue is a positive signal."},
    {"dimension": "Disclosure quality", "rating": "Weak", "color": "weak",
     "summary": "17 affiliate litigation actions. CEO barred in California. 6 state regulatory actions. Financial condition flagged. Confidentiality clauses. High Item 19 exclusion rate."},
    {"dimension": "Downside risk profile", "rating": "Weak", "color": "weak",
     "summary": "Affiliate regulatory pattern, franchisor financial condition warning, 38.6% turnover, system contraction, and confidentiality clauses create a multi-layered risk profile."},
    {"dimension": "Buyer fit breadth", "rating": "Weak", "color": "weak",
     "summary": "Very narrow. Suitable only for buyers with high risk tolerance who have independently validated the local market, the specific territory, and the franchisor's financial stability."},
    {"dimension": "Overall", "rating": "Elevated Risk", "color": "weak",
     "summary": "The data is sufficient to analyze but the risk profile is the most elevated in the cohort. The regulatory pattern, turnover rate, system contraction, and financial condition warnings demand exceptional diligence. Inclusion in this library reflects analytical value for cohort comparison, not endorsement. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """Maid Right is included in this cohort library because it represents a distinct
archetype — small, founder-led, high-risk — that buyers encounter in the market and deserve disciplined
analysis of, not silence about. The data is sufficient for a structured report. But the risk profile is
the most elevated in the cohort by every measure: turnover, regulatory history, financial condition, and
system trajectory. This is a franchise where the disclosed risks are not theoretical — they are documented
regulatory findings across multiple states about the parent organization. Your diligence must be
exceptionally thorough, and you should assume that the disclosed risks understate the actual situation
given the confidentiality clauses restricting franchisee speech.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Experienced operator with high risk tolerance who has independently validated the opportunity:</strong>
If you have cleaning industry experience, a strong local market, and have personally verified the franchisor's
financial stability and support quality through direct investigation — not just the FDD — Maid Right's
relatively low royalty rate (6%) and recurring revenue model could work. But you are assuming risks that
most buyers should not.</li>
<li><strong>Existing PSB Group franchisee expanding into cleaning:</strong> If you already operate a
360 Painting, Window Gang, or other PSB brand and are familiar with the parent organization's strengths
and weaknesses, you have informational advantages other buyers lack. 10% discount for existing PSB
affiliates. (p. 17)</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>First-time franchise buyer:</strong> A system with 38.6% turnover, 35 units, a CEO barred from
selling franchises in one state, and franchisor financial condition warnings is not an appropriate first
franchise for most buyers.</li>
<li><strong>Buyer seeking peer support and system scale:</strong> 28 franchisees operating 35 territories
— 8 of whom are master franchisees. The peer network is very thin. In comparison, Molly Maid has 197
operators, Merry Maids has 249 FOGs.</li>
<li><strong>Buyer in California:</strong> CEO Paul Flick was barred from offering or selling franchises
in California for 36 months by the California Department of Financial Protection and Innovation. While
this applied to the 360 Painting affiliate, not Maid Right directly, the regulatory action is on the
same individual who leads Maid Right. (pp. 15–16)</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have independently verified the franchisor's current financial condition beyond what the FDD
discloses. The state-mandated risk disclosure flags the franchisor's financial ability to provide services
and support. (p. 5)</li>
<li>You have read and understood all 17 litigation actions — particularly the regulatory pattern across
6 states (MD, IL, VA, CA, WA). The individual actions are against affiliate entities, but the pattern
reflects the parent organization's compliance culture.</li>
<li>You have talked to multiple current and former franchisees, with full awareness that confidentiality
clauses may limit what they share. Try to reach franchisees who have exited — the 38.6% turnover rate
means many recent exits exist.</li>
<li>You have modeled the full fee burden including the $295/week fixed service fees — not just the
6% royalty and 2% marketing headline rates.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Maid Right's fee burden is third-highest in the cohort: 21.4% at $200K, 16.9% at $300K, 13.4% at $500K.
The headline royalty (6%) and marketing (2%) rates are competitive — matching MaidPro. But the mandatory
weekly service fees ($295/week = $15,340/year) create a fixed-cost floor that is highly regressive.
At $200K revenue, these service fees alone consume 7.7% of gross — more than most competitors' entire
technology fees. The Contact Center Fee ($220/week minimum at Year 5) is the most punitive component,
escalating from $50/week in the first 12 weeks to $220/week by Year 5.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (6% flat):</strong> Competitive rate matching MaidPro. $150/week minimum. At $200K+
revenue, the percentage exceeds the minimum. (pp. 18, 20)</li>
<li><strong>Marketing (2% of Gross Sales):</strong> $50/week minimum. Straightforward. Advertising Cooperative
Fee may also apply (up to $10K or 2% per year) but is not in addition to other required marketing spend.
(pp. 18–19)</li>
<li><strong>Technology Fee ($210/week = $10,920/year):</strong> The second-highest technology cost in the
cohort (behind only Two Maids' $7,800 on a per-year basis, but Maid Right's is actually higher). Covers
website, email, software. Also requires $5,000 one-time Initial Technology Fee at signing. (p. 19)</li>
<li><strong>Contact Center Fee (escalating minimums):</strong> Greater of 2% of Gross Sales or escalating
weekly minimum: $50/week (weeks 1–12), $100/week (weeks 13–24), $150/week (remainder of Year 1),
$220/week (Year 2+). Maximum cap of $770/week. At $200K revenue, the $220/week minimum ($11,440/year)
far exceeds the 2% rate ($4,000/year). At $500K, the 2% rate ($10,000) still falls below the minimum
($11,440). The floor does not become non-binding until revenue exceeds ~$572K. (p. 18)</li>
<li><strong>Accounting and Business Advisory Fee ($85/week = $4,420/year):</strong> Monthly accounting
and business advisory support. Can opt out after 12 months in favor of approved third-party vendor.
(p. 19)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Maid Right charges $50,780 — nearly $21K more than
MaidPro ($30,000) despite having the same nominal royalty and marketing rates. The entire difference is
the $295/week in mandatory service fees. Over a 10-year term, that is $207,000 more than MaidPro's fees.
The service fees are what make Maid Right's effective fee burden closer to The Maids and Two Maids than
to MaidPro, despite the similar headline rates.
</div>

<div class="callout">
<div class="callout-title">The contact center escalation trap</div>
The Contact Center Fee starts at $50/week but reaches $220/week by Year 2. A franchisee who joins
at $200K revenue pays $11,440/year for the contact center alone — 5.7% of gross revenue on a single
service. At MaidPro, the optional National Sales Center is a per-inquiry charge ($30–$35/inquiry) that
scales with actual usage. The difference in philosophy — mandatory flat floor vs optional variable rate —
is fundamental to comparing these systems.
</div>
""",

"item19_narrative": """
<p>Maid Right's Item 19 provides four tables covering fiscal year 2024 for 18 franchisees operating
20 Franchised Businesses. The data is detailed — consolidated revenue, quartile breakdowns, tenure
segmentation, and service mix. But the 46% inclusion rate (18 of 39 franchisees) creates significant
questions about what the excluded 54% look like.</p>

<h3>Table A — Consolidated system revenue</h3>
<ul class="compact">
<li><strong>Total system Gross Sales: $10,408,825</strong> across 20 businesses.</li>
<li><strong>Average per business:</strong> $520,441. Median: $356,020.</li>
<li>Large gap between average and median ($164K) indicates top performers skew the average significantly.</li>
</ul>

<h3>Table B — Revenue by quartile</h3>
<ul class="compact">
<li><strong>Top quartile (6 businesses):</strong> Average $1,258,050, median $1,182,243. Range: $884K–$1.73M.</li>
<li><strong>Middle 50% (9 businesses):</strong> Average $435,696, median $356,020. Range: $288K–$856K.</li>
<li><strong>Bottom quartile (5 businesses):</strong> Average $126,601, median $95,578. Range: $30K–$278K.</li>
</ul>

<h3>Table C — Revenue by tenure (most revealing)</h3>
<ul class="compact">
<li><strong>12–23 months (3 businesses):</strong> Average $66,206. Range: $30K–$96K.</li>
<li><strong>24–35 months (3 businesses):</strong> Average $274,598. Range: $156K–$341K.</li>
<li><strong>36+ months (14 businesses):</strong> Average $782,201, median $709,533. Range: $278K–$1.73M.</li>
</ul>
<p>Strong maturity curve: 36+ month operators average nearly 12× what 12–23 month operators generate.
But two-thirds of reporting franchisees (12/18) have been operating 36+ months — the sample is heavily
weighted toward survivors.</p>

<h3>Table D — Service mix</h3>
<ul class="compact">
<li><strong>86.4% recurring service</strong> ($190 avg job size). Strong recurring base.</li>
<li>Move in/out cleaning: 1.9% of sales but $317 avg job size (highest per-job).</li>
<li>Commercial: only 1.98%. This is a residential-focused operation.</li>
</ul>

<h3>What's excluded — and why it matters</h3>
<ul class="compact">
<li><strong>21 franchisees operating 30 businesses excluded</strong> for not operating the full year
or not using CRM software properly. That is 54% of franchisees and 60% of businesses.</li>
<li>The "not using CRM software properly" exclusion criterion is unusual and concerning — it suggests
either poor technology adoption across the system or a franchisor-selected filter that removes
inconvenient data points.</li>
<li>With 38.6% annual turnover, many of the excluded operators may have exited during 2024. Their
revenue is not reflected in the averages.</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross sales to owner economics</h3>
<p>Using disclosed revenue and industry cost estimates:</p>

<p><strong>At the median ($356K):</strong></p>
<ul class="compact">
<li>Franchisor fees at ~15%: ~$53K (including $15.3K fixed weekly fees)</li>
<li>Revenue after fees: ~$303K</li>
<li>Estimated COGS at 55%: ~$196K</li>
<li>Remaining for overhead and owner draw: ~$107K</li>
<li>After overhead (rent, insurance, vehicle, marketing beyond 2%): ~$50K–$75K for owner income</li>
</ul>

<p><strong>At 12–23 month average ($66K):</strong></p>
<ul class="compact">
<li>Franchisor fees: ~$25K (fixed fees dominate: $15.3K weekly fees + ~$4K royalty + ~$1.3K marketing + ~$5K technology setup). The fixed fees exceed the royalty at this revenue level.</li>
<li>Revenue after fees: ~$41K</li>
<li>Estimated COGS: ~$36K</li>
<li>Remaining: ~$5K for all overhead and owner income. This is not viable.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> The ramp period is brutal. A new Maid Right territory generating $66K
in Year 1 sends ~$25K to the franchisor in fees — 38% of gross revenue. After COGS and basic overhead,
the operator is deeply negative. The 36+ month cohort at $782K average looks much better (~$100K+ implied
owner income), but you have to survive 2–3 years of negative or marginal cash flow to get there — in a
system where 38.6% of operators exited in a single year. The tenure data simultaneously proves the model
works at maturity and demonstrates why the turnover rate is so high.
</div>

<div class="callout">
<div class="callout-title">The 54% exclusion problem</div>
When more than half the system is excluded from performance data, the reported averages describe survivors,
not the system. MaidPro excludes 2.5% (6 of 237 for not operating full year). Molly Maid excludes 7%
(31 of 448). Maid Right excludes 54% (21 of 39). This is not a minor statistical caveat — it fundamentally
changes what the averages mean. The system average for the INCLUDED population is $520K. The system average
for the entire system — including excluded operators generating unknown revenue — could be substantially lower.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It uses Maid Right's disclosed Item 19 revenue for 20 franchised
businesses (of 50 total) that were open the full year and using CRM properly. 54% of the system is
excluded from these figures. No cost data is disclosed. COGS is estimated from industry norms. The fixed
weekly service fees ($295/week = $15,340/year) dominate the fee burden at lower revenue levels and create
a structural disadvantage vs competitors with variable-only fee structures. Your actual results depend on
territory, market conditions, ramp speed, and whether the franchisor delivers the services these fees
are meant to cover.</p>
""",

"economics_scenarios_config": [
    ("Year 1-2 operator (Table C avg)", 66000),
    ("System median (Table A)", 356000),
    ("36+ month operator average (Table C)", 782000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue from Item 19 Tables A and C (FY2024, 18 franchisees / 20 businesses — 46% of system). COGS estimated at 55% (cleaning industry norm — not disclosed). Fixed weekly fees ($295/week = $15,340/year) apply regardless of revenue level. 'Remaining' must cover all overhead, taxes, and owner draw. 54% of franchisees excluded from data. Turnover rate of 38.6% means many operators do not reach the 36+ month maturity stage.",

"investment_narrative": """
<p>Highest entry cost in the cleaning cohort: $147,100–$218,500. The $65,000 standard franchise fee is
the highest single fee in the cohort, with a $5,000 one-time technology fee on top. Military/first
responder and existing PSB affiliate discounts (10% each) are available. During 2024, actual franchise
fees ranged from $25,000 to $65,000 — suggesting substantial negotiation or promotional discounting.
The Designated Manager Salary line ($0–$30,000) creates a wide range in total investment. (pp. 17–21)</p>
""",

"investment_detail": """
<h3>What to know about the major line items</h3>
<ul class="compact">
<li><strong>Franchise Fee ($65,000 standard):</strong> Highest in cohort. Payable by wire at signing.
If SBA-financed: $15,000 at signing, remainder after funding. Non-refundable. Discounts: 10% military/
first responder, 10% existing PSB affiliate (not combinable). (pp. 17–18)</li>
<li><strong>Additional Funds — 6 months ($50,000–$60,000):</strong> Note: 6-month runway, not the 3-month
standard most competitors use. This is appropriate given the revenue ramp data (Year 1–2 average: $66K).
But at the low end ($50K), that is $8,333/month for 6 months — tight given that franchisor fees alone
are $2,100+/month before any COGS or overhead. (p. 21)</li>
<li><strong>Marketing ($10,000–$20,000):</strong> In addition to the mandatory 2% ongoing marketing fund.
This is pre-opening and launch marketing spend. (p. 21)</li>
<li><strong>Designated Manager Salary ($0–$30,000):</strong> Applies only if the owner is not devoting
full-time efforts and hires a manager. Creates the wide range in total investment. If you plan to be
hands-on, this is $0. (p. 21)</li>
<li><strong>Initial Technology Fee ($5,000 one-time):</strong> In addition to the ongoing $210/week
technology fee. Paid at signing. (p. 18)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Plan for $183K at the midpoint — the most capital-intensive entry in the
cohort. Combined with the highest ongoing fee burden among percentage-based-plus-fixed-fee brands,
Maid Right requires the most capital AND charges among the most in ongoing fees. The math only works
at $350K+ revenue, which the tenure data suggests takes 2–3 years to reach. You need enough capital
to survive negative cash flow for an extended ramp period in a system where 38.6% of operators
exited in a single year.
</div>
""",

"system_health_narrative": """
<p>Maid Right is the smallest and most volatile system in the residential cleaning cohort. The unit count
tells a boom-and-bust story: 24 outlets at start of 2022, rapid growth to 44 by end of 2023 (17 and 21
openings), then contraction to 35 in 2024 (only 6 openings against 15 exits). The system expanded
aggressively, lost a significant portion of the new entrants, and is now smaller than it was 18 months
after the growth surge began.</p>
""",

"system_health_detail": """
<h3>Turnover that demands explanation</h3>
<ul class="compact">
<li><strong>2022:</strong> 17 opened, 4 ceased operations, 1 transfer. Turnover: 20.8%. Fast growth phase.</li>
<li><strong>2023:</strong> 21 opened, 14 ceased operations. Turnover: 37.8%. The 14 ceased exits wiped out
two-thirds of the 21 new openings. Texas alone lost 8 units to ceased operations.</li>
<li><strong>2024:</strong> 6 opened, 6 terminated, 9 ceased, 2 transferred. Turnover: 38.6%. First-ever
terminations. System contracted by 9 net units.</li>
</ul>
<p>The pattern is classic early-franchise volatility: aggressive unit sales, rapid openings, then
equally rapid exits as operators discover the economics do not work at early-stage revenue levels.
The tenure data (Year 1–2 average revenue of $66K) explains why — operators generating $66K against
$25K+ in franchisor fees cannot sustain the business. (pp. 48–51)</p>

<h3>Geographic concentration of losses</h3>
<ul class="compact">
<li><strong>Texas:</strong> 8 ceased (2023), then 4 ceased + 2 terminated (2024). Texas accounts for
14 of the 27 exits in 2023–2024 — over half the total losses.</li>
<li><strong>Florida:</strong> 2 ceased (2022), 4 ceased (2023), 4 terminated (2024). 10 total exits.</li>
<li>The geographic concentration suggests market-specific problems (oversaturation, inadequate support,
or poor territory selection) rather than purely systemic issues.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> A 38.6% turnover rate means roughly 1 in 3 operators exits per year.
This is nearly 5× higher than The Maids (3.9%), 4.6× higher than MaidPro (8.4%), and 4.7× higher than
Molly Maid (8.2%). Even for a small, young system, this rate is exceptional. The growth-then-contraction
pattern suggests the franchisor sold territories faster than it could support them — a concern reinforced
by the financial condition warnings. If you are evaluating Maid Right, the single most important question
is whether the factors that caused 38.6% annual turnover have been addressed.
</div>

<h3>Master franchisees</h3>
<p>8 of 28 franchisees are master franchisees offering subfranchises. This is an unusual structure
for a 35-unit system and introduces an additional layer between the franchisor and the operator.
Ask how many of the operational territories are master-franchised vs direct.</p>
""",

"risk_narrative": """
<h3>Affiliate regulatory pattern — the most significant risk</h3>
<p>17 disclosed litigation actions. While none directly name Maid Right, LLC as defendant, the pattern
involves the same CEO (Paul Flick), the same parent organization (PSB Group / Premium Service Brands),
and the same types of violations:</p>
<ul class="compact">
<li><strong>Maryland (2016):</strong> Consent order against Maid Right predecessor (MRF) for failure to register.</li>
<li><strong>Maryland (2023):</strong> $50,000 penalty against 360 Painting for disclosure failures.</li>
<li><strong>Illinois (2020):</strong> Assurance of Voluntary Compliance against 360 Painting.</li>
<li><strong>Virginia (2021):</strong> Settlement with $25,000 penalty against 360 Painting.</li>
<li><strong>California (2022):</strong> Desist and refrain order + bar order on Paul Flick for 36 months
from offering/selling franchises in California.</li>
<li><strong>Washington (2022):</strong> Consent order against 360 Painting, $2,000 costs.</li>
</ul>
<p>Six state regulatory actions across 6 states — all for FDD disclosure failures — involving the same
leadership and parent organization. When multiple independent state regulators reach similar conclusions
about the same people, the pattern is the signal. (pp. 12–17)</p>

<h3>Franchisor financial condition</h3>
<p>Wisconsin special risk disclosure: the franchisor's financial condition "calls into question the
franchisor's financial ability to provide services and support." Financial statements are consolidated
at the Premium Service Brands, LLC level, not standalone for Maid Right. This means you cannot assess
Maid Right's individual financial health from the FDD. (p. 5)</p>

<h3>38.6% annual turnover</h3>
<p>This is the headline statistic that summarizes system health. In 2024, 17 of 44 starting outlets
exited (6 terminated, 9 ceased, 2 transferred). For comparison: The Maids' turnover is 3.9%, MaidPro's
is 8.4%, Molly Maid's is 8.2%. Maid Right's rate is in a different category entirely.</p>

<h3>Confidentiality clauses</h3>
<p>"In the last 3 years, some franchisees have signed confidentiality clauses" restricting speech. In a
system with 38.6% turnover and 17 litigation actions, the inability to speak freely with former operators
about their experience is a substantial obstacle to informed due diligence.</p>

<h3>Additional fee risks</h3>
<ul class="compact">
<li><strong>Lost Profits clause:</strong> Upon termination, you owe an amount equal to the royalties,
marketing fund payments, and other fees that would have been paid for the full remaining term. On a
$300K/year territory with 5 years remaining at ~17% fee burden: ~$255,000. (p. 20)</li>
<li><strong>Annual Convention:</strong> $1,000 attendance fee — or $2,000 if you do NOT attend. You
are penalized more for absence than presence. (p. 19)</li>
</ul>
""",

"peer_narrative": """
<p>Maid Right occupies a unique — and isolated — position in the residential cleaning cohort. It is the
smallest system (35 units vs 237–802 for peers), the only founder-led brand, the only one with a
multi-state regulatory pattern against its parent organization, and the only one with turnover above
15%. It is not directly comparable to any peer on system maturity or stability.</p>

<p><strong>Fee comparison with MaidPro:</strong> Both charge 6% royalty and 2% marketing. But MaidPro's total
fees at $300K are $30,000 (10.0%) vs Maid Right's $50,780 (16.9%). The entire $20,780 gap is mandatory
weekly service fees that MaidPro does not charge. MaidPro also has 237 units, improving turnover (8.4%),
one settled litigation action, and no regulatory pattern. For a buyer comparing 6%-royalty brands,
MaidPro is the straightforward alternative.</p>

<p><strong>Risk comparison with Merry Maids:</strong> Both are contracting systems. Merry Maids is larger (802
units) and contracting at -18.9% over 3 years. Maid Right is smaller (35 units) and contracted -20.5%
in a single year. Merry Maids has disclosed revenue data for a larger population. Both have confidentiality
clauses. But Maid Right carries a regulatory pattern and financial condition warning that Merry Maids
does not. The risk profiles are qualitatively different — Merry Maids is a declining legacy; Maid Right
is a young system with organizational red flags.</p>

<p><strong>Why this report exists:</strong> Maid Right is included in the cohort library because excluding it
would create a distorted peer set. Buyers who encounter Maid Right in the market deserve the same disciplined
analysis available for every other cleaning franchise. The elevated risk profile is not a reason to omit the
brand — it is a reason to analyze it transparently.</p>
""",

"peer_decision_overlay": [
    {"label": "Lowest modelable fee burden", "brand": "MaidPro", "rationale": "10.0% at $300K with the simplest structure in the cohort: flat 6% royalty + 2% Brand Fund + $500/mo tech. No territory-size-dependent fees."},
    {"label": "Richest revenue disclosure", "brand": "The Cleaning Authority", "rationale": "Per-territory gross revenue ($1.46M average Enterprise), COGS breakdown, price per clean, and customer metrics. Most data for financial modeling."},
    {"label": "Best profitability disclosure", "brand": "The Maids", "rationale": "Only brand disclosing company-owned net margin (15.5%). 97 company-owned offices with $1.18M system-wide average."},
    {"label": "Strongest growth trajectory", "brand": "Two Maids", "rationale": "56.5% system growth over 3 years (+7, +19, +26 net units). Only brand with sustained, accelerating expansion."},
    {"label": "Lowest franchise turnover", "brand": "The Cleaning Authority", "rationale": "4.1% in 2024, down from 10.6%. Zero terminations in 2024 across 236-outlet system."},
    {"label": "Strongest brand recognition", "brand": "Molly Maid", "rationale": "448 outlets, franchising since 1980. Longest track record and Neighborly multi-brand ecosystem."},
    {"label": "Highest regulatory risk", "brand": "Maid Right", "rationale": "CEO barred in California, 6 state regulatory actions, 38.6% turnover, financial condition warnings. Smallest system (35 units)."},
],

"discovery_questions": [
    {
        "question": "Paul Flick was barred from offering or selling franchises in California for 36 months (through the 360 Painting affiliate). Has that bar expired, and have any other states taken similar action since 2022?",
        "context": "Item 3, pp. 15–16. California Department of Financial Protection and Innovation issued desist & refrain order plus bar order.",
        "follow_ups": [
            "Ask whether any of the 6 state regulatory actions resulted in changes to Maid Right's compliance processes.",
            "Ask whether Maid Right has hired a dedicated compliance officer since these actions.",
            "Ask for a copy of the most recent state examination or audit of Maid Right's FDD compliance."
        ],
    },
    {
        "question": "The franchisor's financial condition is flagged by state regulators as calling into question the ability to provide services and support. What is Maid Right's standalone financial position — separate from the consolidated Premium Service Brands financials?",
        "context": "FDD Special Risk #5, p. 5. Financials are consolidated at PSB level.",
        "follow_ups": [
            "Ask whether Maid Right has positive operating cash flow on a standalone basis.",
            "Ask what happens to Maid Right franchisees if Premium Service Brands restructures or divests the brand.",
            "Ask what the franchisor's cash runway is if no new franchise fees are collected."
        ],
    },
    {
        "question": "21 of 39 franchisees (54%) are excluded from Item 19 for 'not operating the full year or not using CRM software properly.' How many were excluded for each reason, and what was their revenue?",
        "context": "Item 19 notes, pp. 45–47. Only 18 of 39 franchisees included.",
        "follow_ups": [
            "Ask what 'not using CRM software properly' specifically means — is it failure to report, or failure to use the system at all?",
            "Ask how many of the excluded franchisees are still operating vs how many exited during 2024.",
            "Ask what the franchisor is doing to improve CRM adoption across the system."
        ],
    },
    {
        "question": "Turnover was 38.6% in 2024. Of the 17 exits (6 terminated, 9 ceased, 2 transferred), what were the primary reasons operators left?",
        "context": "Item 20, pp. 48–51. Texas accounted for 6 exits (4 ceased + 2 terminated), Florida for 4 terminated.",
        "follow_ups": [
            "Ask whether any of the 6 terminated franchisees are contesting the termination.",
            "Ask what the average tenure of the 9 'ceased operations' franchisees was.",
            "Ask whether the franchisor offered any support or transition assistance to franchisees who ceased operations."
        ],
    },
    {
        "question": "The Contact Center Fee escalates to $220/week minimum by Year 2 ($11,440/year). What is the actual value delivered by the Contact Center — specifically, how many leads/calls does it handle per week for a typical franchisee, and what is the conversion rate?",
        "context": "Item 6, p. 18. Contact Center Fee: greater of 2% or escalating weekly minimum up to $770/week cap.",
        "follow_ups": [
            "Ask whether you can see actual Contact Center performance data (calls handled, leads generated, bookings made) for the territory you are considering.",
            "Ask what happens if you are dissatisfied with Contact Center performance — can you opt out?",
            "Ask how many current franchisees are at the $220/week minimum vs paying the 2% rate."
        ],
    },
    {
        "question": "8 of 28 franchisees are master franchisees offering subfranchises. How does the master franchise structure affect support, quality control, and the franchisee experience for sub-franchisees?",
        "context": "Item 19 notes. System includes master franchisees alongside direct franchisees.",
        "follow_ups": [
            "Ask whether master franchisees receive different fee structures or support levels.",
            "Ask how many of the 35 total territories are operated by sub-franchisees vs direct franchisees.",
            "Ask whether the territory you are considering is under a master franchise or directly with Maid Right, LLC."
        ],
    },
    {
        "question": "Texas accounted for 6 of 17 exits in 2024, and Florida for 4. What is driving the geographic concentration of closures, and how many active territories remain in each state?",
        "context": "Item 20, pp. 48–51. Exit concentration suggests market-specific or regional management issues.",
        "follow_ups": [
            "Ask whether the Texas and Florida exits share a common cause (e.g., master franchisee issues, market conditions, or support gaps).",
            "Ask what the franchisor has changed in those markets since the closures.",
            "Ask how many territories remain in Texas and Florida and whether they are stable."
        ],
    },
    {
        "question": "The FDD contains confidentiality clauses that may restrict what current and former franchisees can share with prospective buyers. What specific restrictions apply, and will you provide a written waiver allowing franchisees I contact to speak freely during my diligence?",
        "context": "Risk signals section. Confidentiality restrictions can hinder a buyer's ability to verify disclosed data through franchisee conversations.",
        "follow_ups": [
            "Ask whether any franchisees have been penalized for speaking with prospective buyers.",
            "Ask for a list of current franchisees you can contact without restriction.",
            "Ask whether former franchisees are subject to the same confidentiality provisions."
        ],
    },
],

},

}  # end CLEANING_NARRATIVES
