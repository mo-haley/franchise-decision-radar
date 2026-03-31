"""
Editorial narratives for the Lawn Care cohort.

These are the interpretive layer that makes the report worth paying for.
They cannot be auto-generated from data alone — they are authored analysis.
"""

LAWN_NARRATIVES: dict[str, dict] = {

"lawn-doctor": {

"executive_summary": """
<p>Lawn Doctor is the oldest and largest franchise in the lawn care cohort — 58 years of
continuous franchising and 653 outlets as of year-end 2024. It is PE-backed (CNL Strategic
Capital) and discloses the richest Item 19 in the lawn wedge: four tables covering revenue
by territory count, customer metrics, gross profit margins, and a 16-year historical revenue
trend. The 2024 system average of $1.13M per Strategic-Partner (all territories combined)
and median of $659K sit well above most peer systems, and the 16-year trend shows consistent
upward growth from $367K average in 2009.</p>

<p>The core tension is cost. At $300K gross revenue, annual franchisor fees total $78,800
(26.3% of revenue) — the highest among the four established brands in the cohort. The
primary driver is a mandatory local advertising minimum of the greater of $30,000 or 10%
of Net Revenues, paid on top of a 10% flat royalty. At $500K, the fee burden moderates to
24.6%, but a Lawn Doctor franchisee always sends more to the franchisor than a Spring-Green
or Weed Man operator at equivalent revenue. The franchise fee itself is also the highest:
$124K–$127K (a bundled package including equipment leases, training, and initial supplies).</p>

<p>System health is genuinely strong. The 2024 reporting year showed +23 net growth with only
1 closure and 0 non-renewals — the cleanest year in recent history. Turnover dropped from
6.7% (2022) to 1.6% (2024). The 85.4% average gross profit margin (Table C, 2023 data) is
the highest in the cohort — though this figure deducts only materials, not labor, making it
not directly comparable to Spring-Green's or NaturaLawn's margin figures which include
direct labor in COGS. A buyer choosing Lawn Doctor is paying a premium for scale, disclosure
depth, and system stability — the question is whether the fee structure leaves enough room
for the economics to work in your specific territory.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Weak", "color": "weak",
     "summary": "Highest in cohort: $150K–$177K total investment including $124K–$127K franchise fee (bundled with equipment/training/supplies). Fee is 2–5× higher than peers."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "4th of 6 in full cohort (26.3% at $300K). Among the 4 established brands: 3rd of 4. 10% flat royalty + $30K+ mandatory local ad spend drive the burden."},
    {"dimension": "System stability", "rating": "Strong", "color": "strong",
     "summary": "Largest system (653 outlets). Only 1 closure in 2024. Turnover dropped from 6.7% to 1.6% over 3 years. 23 net new units in 2024."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "Richest Item 19 in lawn cohort: 4 tables with revenue by territory count, customer metrics, gross margin, and 16-year trend. System average $1.13M."},
    {"dimension": "Disclosure quality", "rating": "Strong", "color": "strong",
     "summary": "No litigation. Clean filing. Comprehensive Item 19 population disclosure (205 of 229 Strategic-Partners). 16-year historical trend is rare."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "High fee burden is the primary risk. Gross margin (85.4%) deducts only materials — not labor — creating potential for margin misperception. PE ownership standard for lawn."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Strong for buyers with $150K+ capital who prioritize system scale and disclosure. Weak for budget-sensitive or first-time buyers due to high entry and ongoing costs."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "The strongest combination of disclosure depth and system stability in the lawn cohort, offset by the highest entry cost and one of the highest ongoing fee burdens. Scale and transparency come at a price."},
],

"scorecard_posture": """Lawn Doctor is the scale-and-transparency play in this cohort. It offers
the largest system (653 outlets), the deepest disclosure (4-table Item 19 with 16-year trend),
and the lowest recent attrition (1.6%). But it is also the most expensive to enter and among
the most expensive to operate. The fee structure — 10% royalty, $30K+ mandatory local advertising,
$9K+ call center — takes a substantial share of revenue at every level. A buyer should treat
Lawn Doctor's disclosure depth as an analytical advantage for due diligence, not as a guarantee
of returns. The fee burden is the price of that transparency and system scale.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Well-capitalized buyer seeking maximum system support and transparency:</strong>
If you have $150K+ in capital and prioritize being part of the largest lawn care franchise
system with the best disclosure, Lawn Doctor delivers. The 16-year revenue trend, customer
metrics, and gross margin data give you more due diligence material than any peer.</li>
<li><strong>Multi-territory operator:</strong> The Item 19 shows operators with 4+ territories
averaging $2.57M in net revenues. At that scale, the fee burden dilutes and the gross margin
(85.4%) on a materials-only COGS basis leaves room for owner income after labor costs.</li>
<li><strong>Buyer in established markets who will acquire existing territories:</strong>
With 653 units and consistent transfer activity (28, 22, 9 transfers across 3 years),
resale territories are available. Buying an existing book avoids the ramp period where
the high fee burden is most punitive.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive first-time buyer:</strong> The $124K–$127K franchise fee alone
exceeds the total investment at NaturaLawn ($78K–$153K range) and Spring-Green ($118K–$134K).
You will have the highest cash-at-signing requirement in the cohort.</li>
<li><strong>Single-territory operator at sub-$400K revenue:</strong> At $300K revenue, $78,800
goes to the franchisor (26.3%). After materials (estimated 14–15% based on 85.4% gross margin),
roughly $175K remains for labor, overhead, and owner draw. In a seasonal business with
significant labor costs, this may be tight.</li>
<li><strong>Buyer who wants marketing autonomy:</strong> The $30K+ mandatory local advertising
minimum is non-negotiable and is managed through the franchisor's approved channels. If you
want to allocate your own marketing spend based on local conditions, this structure constrains you.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have modeled your territory's likely revenue against the fee structure — not just the
system average ($1.13M) but the median for your territory count. Single-territory operators
(1–3 territories) have a median of $380K, where the fee burden is highest.</li>
<li>You understand that the 85.4% gross margin deducts only materials, not labor. Your actual
margin after paying employees will be substantially lower. Ask for labor cost benchmarks
during discovery day.</li>
<li>You have compared the total cost of Lawn Doctor (entry + 10-year fees) against Spring-Green
and NaturaLawn, which offer similar services at lower ongoing cost — with the trade-off of
less system scale and disclosure depth.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Lawn Doctor has the highest ongoing fee burden among the four established brands in the cohort
at every revenue level below $500K. At $300K revenue, total franchisor fees are $78,800 (26.3%).
The primary drivers are the 10% flat royalty ($30,000) and the mandatory local advertising
minimum of the greater of $30,000 or 10% of Net Revenues ($30,000 at this level). At $500K,
the fee burden remains 24.6% — nearly double Spring-Green's 13.5%.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (10% flat):</strong> The highest flat royalty rate in the cohort (tied with
Spring-Green's first tier). Unlike Spring-Green, there are no volume discounts — 10% applies
regardless of revenue. Payable weekly. 'Net Revenues' = gross collected from customers excluding
taxes and refunds. (p. 15)</li>
<li><strong>Local advertising (greater of $30,000 or 10% of Net Revenues):</strong> This is the
most aggressive local marketing requirement in the lawn cohort. At $300K revenue, the floor
matches the percentage; at $400K+, the percentage exceeds the floor. Spent on radio, digital,
direct mail, and other local media through approved channels. (pp. 15, 25)</li>
<li><strong>National/regional advertising fund (currently 0%):</strong> Franchisor reserves the
right to establish a fund of up to 2% of Net Revenues, but it is not currently active. If
activated, this would add $6,000–$10,000/year at $300K–$500K revenue. (p. 15)</li>
<li><strong>Technology ($150–$250/month):</strong> $150/month until cumulative Net Revenues reach
$1M, then $250/month. Can increase to $500/month at franchisor's discretion. Relatively
modest compared to peers. (p. 20)</li>
<li><strong>Call center ($750/month = $9,000/year):</strong> Mandatory Lawn Doctor Answer Center.
$750/month currently. Handles customer inquiries and scheduling. (p. 20)</li>
<li><strong>Convention ($2,000/year):</strong> $2,000 registration fee for mandatory annual
convention, plus travel and lodging. (p. 16)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, $78,800 goes to the franchisor — $33,500
more than Spring-Green ($45,318) and $53,250 more than Weed Man ($25,550). Over a 10-year
term, that gap compounds to $335,000–$532,500 of additional fees paid to Lawn Doctor vs.
peers. The question is whether Lawn Doctor's system scale, brand recognition, call center
infrastructure, and disclosure depth justify that premium.
</div>

<div class="callout">
<div class="callout-title">The local ad minimum is the key differentiator</div>
Strip out the local advertising minimum, and Lawn Doctor's fee burden falls to $48,800 at $300K
(16.3%) — competitive with most peers. The $30,000 floor is what pushes the total to 26.3%.
A buyer should evaluate whether the franchisor's mandatory local advertising program generates
proportional lead volume. Ask current franchisees: does the $30K minimum translate to enough
customers to justify the spend?
</div>
""",

"item19_narrative": """
<p>Lawn Doctor discloses the richest Item 19 in the lawn care cohort — four tables covering
revenue segmented by territory count, customer-level metrics, gross profit margins, and a
16-year historical revenue trend for the system. (pp. 53–55)</p>

<h3>Revenue by territory count (Table A, 2024)</h3>
<p>205 Strategic-Partners operating 2+ full years, representing 490 of 653 total Lawn Doctor
Businesses. Revenue is per Strategic-Partner (all their territories combined), not per territory.</p>
<ul>
<li><strong>1–3 territories (146 SPs):</strong> Average $682K, median $380K. Range: $35K–$3.65M.
Only 32% met or exceeded the average — strong right-skew.</li>
<li><strong>4–6 territories (39 SPs):</strong> Average $1.47M, median $1.38M.</li>
<li><strong>7–9 territories (11 SPs):</strong> Average $2.57M, median $2.39M.</li>
<li><strong>10+ territories (9 SPs):</strong> Average $5.39M, median $4.63M.</li>
<li><strong>All SPs combined (205):</strong> Average $1.13M, median $659K. Only 29% met or
exceeded the average.</li>
</ul>

<h3>Customer metrics (Table B, 2024)</h3>
<ul>
<li><strong>Average customer program value:</strong> $860 (median $648). This represents total
revenue per customer-program, not per service visit.</li>
<li><strong>Average customer tenure:</strong> 6.15 years (median 4.21). The high tenure suggests
strong recurring revenue — customers stay more than 4 years at the median.</li>
<li><strong>Annual revenue per customer:</strong> $765 (median $576).</li>
</ul>

<h3>Gross profit margin (Table C, 2023 data)</h3>
<ul>
<li><strong>Average: 85.4%, median: 84.5%.</strong> 130 of 205 Strategic-Partners included
(75 excluded for insufficient data). 41.5% met or exceeded the average.</li>
</ul>

<h3>Critical comparability warning</h3>
<p>Lawn Doctor's COGS deducts only materials (chemicals, fertilizer, supplies). It does <strong>not</strong>
include direct labor. Spring-Green (68.1% margin) and NaturaLawn (60.7–65.2% margin) both include
direct labor in their COGS calculations. These margins are <strong>not directly comparable</strong>.
Lawn Doctor's 85% margin overstates the operating profit available to the franchisee relative to
peers who show 60–68% margins with labor included.</p>

<h3>16-year trend (Table D, 2009–2024)</h3>
<p>Average net revenues grew from $367K (2009) to $1.13M (2024) — a 208% increase over 16 years.
Median grew from $207K to $659K (218%). The trend is consistently upward with the exception of
2020 (COVID year). This is the most comprehensive historical disclosure in the lawn cohort and
shows a system that has compounded revenue steadily.</p>

<h3>What's missing</h3>
<ul>
<li><strong>Per-territory revenue:</strong> Revenue is per Strategic-Partner, not per territory.
A Strategic-Partner with 4 territories averaging $1.47M total is not making $1.47M per territory —
likely $350K–$400K per territory. The median for 1–3 territory SPs ($380K) is the closest proxy
for single-territory economics.</li>
<li><strong>Labor costs:</strong> The 85.4% gross margin excludes labor entirely. Lawn care is
labor-intensive (seasonal crews, training, equipment operation). Actual operating margin after
labor is likely 30–50 percentage points lower. The FDD provides no labor cost benchmarks.</li>
<li><strong>Net income or profit:</strong> No profitability data is disclosed. After fees ($78,800
at $300K), materials (~$45K at 85% margin), labor (unknown), and overhead, the owner's income
is uncertain.</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross revenue to owner economics</h3>
<p>The Item 19 gives revenue and materials-only COGS. Here is what we can estimate:</p>

<p><strong>For a median single-territory SP ($380K revenue):</strong></p>
<ul>
<li>Materials at ~15% (from 85% gross margin): ~$57K</li>
<li>After materials: ~$323K</li>
<li>Franchisor fees at $300K (conservative proxy): ~$73K (scaled from the $78,800 at $300K model)</li>
<li>After fees: ~$250K</li>
<li>Estimated labor (40–50% of remaining, based on industry benchmarks for seasonal lawn care): $100K–$125K</li>
<li>Overhead (vehicle, insurance, office, misc): $30K–$50K</li>
<li>Implied pre-tax owner income: $75K–$120K</li>
</ul>

<p><strong>For an average single-territory SP ($682K revenue):</strong></p>
<ul>
<li>Materials at ~15%: ~$102K</li>
<li>After materials: ~$580K</li>
<li>Franchisor fees (interpolated): ~$122K</li>
<li>After fees: ~$458K</li>
<li>Estimated labor: $160K–$200K</li>
<li>Overhead: $40K–$60K</li>
<li>Implied pre-tax owner income: $198K–$258K</li>
</ul>

<div class="callout">
<div class="callout-title">The labor gap is the critical unknown</div>
The 85.4% gross margin looks exceptional — until you account for the fact that labor is excluded.
In seasonal lawn care, direct labor (technicians, crew leaders, seasonal workers) typically
represents 30–45% of revenue. At $380K revenue, that could be $114K–$171K. The "high margin"
story depends entirely on labor efficiency, which the FDD does not disclose. Your discovery day
should focus heavily on labor cost benchmarks from current franchisees.
</div>

<div class="implication">
<strong>What this means:</strong> A single-territory operator at the median ($380K) likely takes
home $75K–$120K before taxes — viable as a full-time business but not exceptional. At the average
($682K), the math improves materially to a potential $200K+ owner draw. The fee burden matters
more at lower revenue levels, where every dollar sent to the franchisor comes directly out of
the owner's income. Multi-territory operators ($1.4M+) are where the Lawn Doctor economics
become genuinely attractive.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Lawn Doctor's
disclosed Item 19 revenue data. The FDD does not disclose net franchisee profitability or labor
costs. The 85.4% gross profit margin deducts only materials — not labor, vehicle costs, insurance,
or overhead. Your actual results depend on territory size, local labor market, customer density,
seasonal length, and execution. These scenarios use estimated COGS of 55% (materials + estimated
labor) based on lawn care industry benchmarks. This is an assumption, not a disclosed figure.</p>
""",

"economics_scenarios_config": [
    ("Median single-territory SP", 380000),
    ("Average single-territory SP", 682000),
    ("Average 4–6 territory SP", 1470000),
],

"economics_cogs_ratio": 0.55,

"economics_assumptions": "Revenue from Item 19 Table A (2024, 205 Strategic-Partners operating 2+ years). COGS estimated at 55% of revenue: ~15% materials (from disclosed 85.4% gross margin) + ~40% estimated direct labor (industry benchmark for seasonal lawn care; NOT disclosed in FDD). This COGS estimate is illustrative, not extracted. 'Remaining' must cover vehicle costs, insurance, office overhead, owner draw, and taxes.",

"economics_detail": "",

"payback_narrative": "",

"investment_narrative": """
<p>Highest entry cost in the cohort: $150,070–$177,052 total. The franchise fee alone ($124K–$127K)
exceeds the total investment at NaturaLawn. The fee is a bundled package including: $50,000 initial
license fee, $70,600 initial training/supply/support fee, and $6,400 in equipment lease deposits
(Turf Tamer applicator and power seeder). The $3K variation depends on local agronomic
conditions affecting equipment needs.</p>
""",

"investment_detail": """
<h3>What the franchise fee buys</h3>
<ul class="compact">
<li><strong>Initial license fee ($50,000):</strong> The territory rights and brand license.
Nonrefundable. (p. 13)</li>
<li><strong>Training/supply/support fee ($70,600):</strong> Covers initial training program,
initial supply of materials, equipment setup, and launch support. (p. 13)</li>
<li><strong>Equipment lease deposits ($6,400):</strong> Turf Tamer Stand-On Applicator ($3,350)
and Power Seeder ($3,050). These are lease deposits, not purchases. The equipment remains
franchisor property. (p. 13)</li>
</ul>

<h3>Beyond the franchise fee</h3>
<ul class="compact">
<li><strong>Vehicle:</strong> $7,000–$10,000 (used truck or van). Many operators start with
a personal vehicle.</li>
<li><strong>Insurance:</strong> $2,000–$5,000 (general liability, workers' comp, vehicle).</li>
<li><strong>Additional working capital:</strong> $14,000–$28,000 for first 3 months of operations.</li>
<li><strong>Local advertising (first year):</strong> The $30,000+ minimum begins immediately.
This is operating cost, not a one-time charge, but the initial cash impact is significant.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> A Lawn Doctor franchise requires roughly $150K–$177K before you
earn your first dollar. The high franchise fee reflects the bundled equipment and training package —
you are not buying just a territory, you are buying a turnkey launch kit. But the capital
requirement means this is not an entry-level franchise. Buyers with less than $175K in liquid
capital should consider Spring-Green ($118K–$134K) or NaturaLawn ($78K–$153K) as alternatives
with lower entry barriers.
</div>
""",

"system_health_narrative": """
<p>Largest and most stable system in the cohort. 653 outlets at year-end 2024, with net growth
of +11, +6, and +23 over the three reported years. Turnover declined sharply: 6.7% (2022) to
5.0% (2023) to 1.6% (2024). The 2024 result — only 1 closure against 24 openings — is the
cleanest system health year any lawn cohort brand has reported.</p>
""",

"system_health_detail": """
<h3>Outlet trajectory</h3>
<ul class="compact">
<li><strong>2022:</strong> 613→624 (+11 net). 24 opened, 13 closed. 28 transfers — healthy
resale market. Turnover 6.7%.</li>
<li><strong>2023:</strong> 624→630 (+6 net). 15 opened, 9 closed. 22 transfers. Turnover 5.0%.</li>
<li><strong>2024:</strong> 630→653 (+23 net). 24 opened, 1 closed, 0 non-renewals. 9 transfers.
Turnover 1.6%.</li>
</ul>

<h3>Transfer activity</h3>
<p>28, 22, and 9 transfers across the three reported years. The declining transfer count could
signal fewer franchisees wanting to exit (positive) or fewer buyers in the resale market
(ambiguous). At this system size, transfer activity is a normal part of franchise lifecycle.</p>

<h3>PE ownership context</h3>
<p>Owned by CNL Strategic Capital. PE ownership is standard across the lawn cohort — Lawn Doctor,
Spring-Green's corporate parent, and NaturaLawn all have institutional backing of some form.
The PE ownership does not appear to have driven aggressive expansion or extraction behavior:
growth has been steady, not hockey-stick, and attrition has declined.</p>

<div class="implication">
<strong>What this means:</strong> For a 58-year-old system with 653 units, 1.6% turnover is
exceptional. Most franchise systems at this scale experience structural attrition of 3–8% annually
just from retirements, market exits, and non-renewals. The 2024 result suggests franchisees are
staying, which is the strongest available proxy for franchisee satisfaction. But it is one year —
the 3-year trend is more informative, and even the 6.7% from 2022 was respectable.
</div>
""",

"risk_narrative": """
<h3>Litigation</h3>
<p>No litigation required to be disclosed (Item 3). No bankruptcy (Item 4). This is a clean
legal history — uncommon for a system this size and age.</p>

<h3>Entity and ownership</h3>
<p>LD Parent, Inc., backed by CNL Strategic Capital, LLC. Straightforward entity structure.
The franchise is operated under a "Strategic-Partner" model rather than the traditional
"franchisee" terminology. This is a branding choice, not a legal distinction — the FDD
is a standard franchise disclosure document.</p>

<h3>Fee escalation risk</h3>
<p>The national/regional advertising fund (up to 2% of Net Revenues) is currently at 0% but
could be activated at any time. If implemented, this would add $6,000–$10,000/year at
$300K–$500K revenue on top of an already-high fee burden. Technology fees can also increase
to up to $500/month at franchisor's discretion. (pp. 15, 20)</p>

<h3>Seasonal concentration</h3>
<p>Lawn care is inherently seasonal in most markets. Revenue concentrates in the April–October
window (varies by geography). Cash flow management during the off-season is a real operational
challenge that the annual revenue averages in Item 19 do not surface. The FDD does not disclose
monthly revenue patterns.</p>
""",

"peer_narrative": """
<p>Among the four established brands in this cohort, Lawn Doctor occupies a distinctive position:
highest cost, highest transparency, most stable system. It is the premium choice — you pay more
and you see more.</p>

<p><strong>Closest comparison: Spring-Green.</strong> Similar services, similar maturity (48 vs. 58
years), both with tiered/flat royalties near 10%. But Spring-Green's total fees at $300K are
$45,318 (15.1%) vs. Lawn Doctor's $78,800 (26.3%). The $33,500 annual gap is almost entirely
driven by Lawn Doctor's $30K local advertising minimum — Spring-Green has no equivalent floor.
Spring-Green's Item 19 is solid (3 tables, $744K average for single-territory operators) but
less deep than Lawn Doctor's 4-table, 16-year dataset.</p>

<p><strong>Value alternative: NaturaLawn.</strong> Lowest entry cost ($78K–$153K) and highest
revenue per customer ($810 vs. Lawn Doctor's $765). But NaturaLawn's fee burden at $300K
is actually the highest in the cohort ($101,584, 33.9%) due to $60K–$80K mandatory marketing
spend. NaturaLawn's Item 19 is limited to 6 company-owned and 40 franchised locations — far
smaller samples than Lawn Doctor's 205 SPs.</p>

<p><strong>Budget play: Weed Man.</strong> Lowest fees in the cohort by a wide margin (8.5% at
$300K). But Weed Man declines Item 19 entirely — no revenue, no margin, no customer data.
A buyer choosing Weed Man over Lawn Doctor is trading disclosure and system support for
the lowest possible fee structure. This trade-off is only appropriate for operators with
independent market knowledge who do not need FDD-based revenue benchmarks.</p>
""",

"peer_decision_overlay": [
    {"priority": "Lowest ongoing fee burden", "best_brand": "Weed Man", "note": "8.5% at $300K, but no Item 19 disclosure — you are flying blind on revenue benchmarks."},
    {"priority": "Best revenue disclosure", "best_brand": "Lawn Doctor", "note": "4-table Item 19 with 16-year trend. Most data to work with in diligence."},
    {"priority": "Lowest entry cost", "best_brand": "NaturaLawn", "note": "$78K–$153K total. But ongoing fee burden is the highest in the cohort."},
    {"priority": "Best balance of cost vs. data", "best_brand": "Spring-Green", "note": "15.1% fee burden at $300K with solid 3-table Item 19. The middle ground."},
    {"priority": "Lowest turnover", "best_brand": "Lawn Doctor / NaturaLawn", "note": "Both under 2% in 2024. NaturaLawn at 0% for 2 of 3 years (but 88-unit system)."},
    {"priority": "First-time buyer", "best_brand": "Spring-Green", "note": "Moderate cost, clean disclosure, manageable fee burden, stable 126-unit system."},
],

"discovery_questions": [
    {"question": "What are typical annual direct labor costs for a single-territory operator in my region?",
     "context": "The 85.4% gross margin deducts only materials, not labor. You need labor cost benchmarks to build a realistic P&L.",
     "strong_answer": "They provide a range with regional context (e.g., '$60K–$100K for 2 seasonal technicians in the Midwest'). Even better if they reference Item 19 data to show how labor fits into the margin picture.",
     "evasion": "They say 'it varies' without providing any benchmarks, or they point you to the 85.4% margin as if it represents operating profit.",
     "follow_up": "What percentage of net revenue should I expect to spend on direct labor in my first 3 years?"},
    {"question": "The mandatory local advertising minimum is $30,000 or 10% of Net Revenues. What is the typical lead volume and cost per lead generated by this spend?",
     "context": "At $300K revenue, local advertising is 10% of gross — you need evidence it works.",
     "strong_answer": "They provide average leads per $1K spent, cost per acquired customer, or conversion rates from the local advertising program. Data from comparable markets to yours.",
     "evasion": "Vague claims about 'strong brand presence' without quantifying lead generation. Inability to provide cost-per-lead or conversion metrics.",
     "follow_up": "Can I see anonymized lead generation data for 3 Strategic-Partners in similar-sized markets?"},
    {"question": "Table A shows the median for 1–3 territory SPs is $380K. What does a typical first-year trajectory look like in my market?",
     "context": "The median is for operators with 2+ years. First-year revenue is likely lower. You need ramp expectations.",
     "strong_answer": "They provide first-year revenue benchmarks or ramp curves showing expected quarters to reach median performance. Honest about seasonal startup timing.",
     "evasion": "They redirect to the $1.13M average (which includes multi-territory operators) or avoid discussing early-year economics.",
     "follow_up": "What percentage of first-year Strategic-Partners reach $200K in their initial year?"},
    {"question": "The national/regional advertising fund is currently at 0%. Under what circumstances would you activate it, and what would the funds be used for?",
     "context": "The FDD reserves the right to charge up to 2% for a national fund. If activated on top of the current fee structure, total fees would exceed 28% at $300K.",
     "strong_answer": "Clear criteria for activation and specific planned uses. Honest about likelihood and timeline. Acknowledgment that this would increase total fees.",
     "evasion": "Dismissive ('we have no plans to activate it') without explaining why the provision exists or what would trigger it.",
     "follow_up": "Is there a franchisee vote or consent mechanism before the fund is activated?"},
    {"question": "The franchise fee is $124K–$127K including equipment leases and training. If I decide to exit after 3 years, what is the residual value of these assets?",
     "context": "The equipment (Turf Tamer applicator, power seeder) remains franchisor property via lease. The training/support fee is sunk. Understanding residual value is critical for exit planning.",
     "strong_answer": "They explain what assets you retain vs. what reverts to the franchisor. Honest about transfer fee structure and resale market conditions.",
     "evasion": "They focus on why you wouldn't want to leave rather than answering the question directly.",
     "follow_up": "What was the average resale price for territories that transferred in 2024? What percentage of the original investment did sellers typically recover?"},
    {"question": "Technology fees can increase from $150/month to $500/month at LDI's discretion. What has the historical fee increase pattern been?",
     "context": "A $350/month potential increase ($4,200/year) adds to an already-high fee burden.",
     "strong_answer": "They provide historical fee increase data and explain the rationale. Demonstrate that increases have been gradual and tied to service improvements.",
     "evasion": "They downplay the possibility or refuse to provide historical increase data.",
     "follow_up": "Has LDI ever decreased a recurring fee, or do increases only go one direction?"},
    {"question": "75 of 205 Strategic-Partners were excluded from the gross margin data (Table C) for 'insufficient information.' What does that mean?",
     "context": "37% exclusion rate for margin data. If the excluded SPs have systematically lower margins, the 85.4% average overstates the system.",
     "strong_answer": "They explain the data collection process and whether the exclusions are random or correlated with performance. Ideally: 'These SPs didn't submit complete cost data, and we believe their margins are similar.'",
     "evasion": "They don't know why SPs were excluded, or they deflect to the 85.4% average as representative without addressing the missing 37%.",
     "follow_up": "Could you survey the excluded SPs to get a fuller picture of system margins?"},
    {"question": "Customer tenure averages 6.15 years. What is the annual customer attrition rate, and how does it vary by territory age and geography?",
     "context": "High tenure is positive, but you need to understand the churn rate to model customer acquisition costs against the $30K+ local ad spend.",
     "strong_answer": "They provide annual retention rates and acknowledge geographic variation (shorter tenure in competitive markets, longer in established territories).",
     "evasion": "They cite only the average tenure without discussing the distribution or attrition rate.",
     "follow_up": "What is the typical cost to acquire a new customer through the local advertising program?"},
],

},  # end lawn-doctor


"spring-green": {

"executive_summary": """
<p>Spring-Green is a 48-year-old, privately held lawn care and tree/shrub treatment franchise
with 126 outlets as of year-end 2024 — a mid-sized system that has been remarkably stable
(+2, –2, +4 net units over three years). It occupies the middle ground of the lawn care cohort:
lower fees than Lawn Doctor and NaturaLawn, better disclosure than Weed Man, and a balanced
fee structure that does not punish low-revenue operators as severely as its higher-cost peers.</p>

<p>At $300K gross revenue, annual franchisor fees total $45,318 (15.1%) — second-lowest in the
full cohort (only Weed Man is lower at 8.5%). The tiered royalty (10%/9%/8%) rewards revenue
growth, and the 2% national advertising fund with no mandatory local advertising minimum gives
franchisees more marketing autonomy than any peer. The Item 19 discloses 3 tables covering cost
structure, revenue, and marketing effectiveness for 71 franchised businesses — with the unique
addition of revenue-per-production-vehicle metrics and customer acquisition data.</p>

<p>The main limitations are scale and growth trajectory. At 126 units, Spring-Green is the
second-smallest active cohort brand (behind NaturaLawn's 88). Net growth has been flat — the
system is not expanding or contracting. For a buyer who values stability over growth momentum,
this is neutral. For a buyer who wants to join a system with accelerating expansion, it is a
constraint. Turnover is moderate (2.0%, 5.2%, 4.6%) with the 2023 and 2024 years reflecting
a handful of exits from a small base.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Mixed", "color": "mixed",
     "summary": "$118K–$134K total investment. Mid-cohort. Franchise fee ($27K–$45K) is substantially lower than Lawn Doctor ($124K) but higher than NaturaLawn ($20K–$40K)."},
    {"dimension": "Ongoing fee burden", "rating": "Strong", "color": "strong",
     "summary": "2nd lowest in full cohort: 15.1% at $300K. Only Weed Man (8.5%) is lower. No mandatory local advertising minimum — significant advantage over Lawn Doctor and NaturaLawn."},
    {"dimension": "System stability", "rating": "Mixed", "color": "mixed",
     "summary": "Stable but flat: +2, –4, +2 net over 3 years. 126 units. Turnover moderate at 2–5%. No rapid growth, no contraction. Not exciting, but not concerning."},
    {"dimension": "Revenue disclosure", "rating": "Strong", "color": "strong",
     "summary": "3-table Item 19 with cost structure, revenue by territory type, and marketing metrics. Average $744K single-territory, $1.55M multi-territory. Revenue per vehicle and customer acquisition data are unique."},
    {"dimension": "Disclosure quality", "rating": "Strong", "color": "strong",
     "summary": "Clean filing, no litigation. Honest COGS definition (includes direct labor). Gross margin (68.1%) is more conservative and more useful than Lawn Doctor's materials-only 85.4%."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Flat growth trajectory is the primary concern. System is not declining, but it is not demonstrating the kind of momentum that attracts new franchisees. Fee escalation risk is modest."},
    {"dimension": "Buyer fit breadth", "rating": "Strong", "color": "strong",
     "summary": "Best balance of cost and data in the cohort. Works for first-time buyers, single-territory operators, and multi-unit operators. No mandatory local ad spend gives marketing flexibility."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "The most balanced option in the lawn cohort: moderate cost, solid disclosure, stable system, honest COGS. Not the cheapest (Weed Man), not the most transparent (Lawn Doctor), not the most stable (NaturaLawn) — but the best combination of all three. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """Spring-Green is the balanced choice in the lawn care cohort. It offers the
second-lowest ongoing fee burden, the most useful gross margin disclosure (including labor in COGS),
no mandatory local advertising minimum, and a clean litigation history. The trade-off is a flat growth
trajectory and a mid-sized system (126 units) that lacks the scale of Lawn Doctor or the hyper-local
niche identity of NaturaLawn. For a buyer who wants good data, manageable costs, and marketing
autonomy — without paying Lawn Doctor's premium or accepting Weed Man's disclosure blackout —
Spring-Green is the most natural fit.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>First-time franchise buyer seeking a balanced entry:</strong> Moderate investment
($118K–$134K), no mandatory local ad minimums, tiered royalty that rewards growth, clean
disclosure. The lowest-friction entry in the cohort for a buyer who wants both data and
manageable costs.</li>
<li><strong>Operator who values marketing autonomy:</strong> Spring-Green does not mandate a
local advertising floor. The 2% national fund and optional regional fund (currently 0%)
are the only marketing obligations. You control your own local marketing spend and strategy.</li>
<li><strong>Single-territory operator targeting $500K+ revenue:</strong> At $500K, the tiered
royalty drops to an 8% marginal rate on revenue above $500K, and total fees are $67,318
(13.5%) — nearly half of NaturaLawn's $121,584 (24.3%) at the same revenue. The economics
reward scale more than any other brand in the cohort.</li>
<li><strong>Tree and shrub treatment interest:</strong> Spring-Green franchises include a
tree/shrub care line alongside core lawn services. This adds a revenue stream and seasonal
diversification not available at all competitors.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Buyer seeking rapid system growth and momentum:</strong> Net growth has been flat
(+4 net over 3 years). If you value being part of an expanding system with accelerating
franchisee additions, Spring-Green's trajectory may disappoint.</li>
<li><strong>Buyer who wants franchisor-managed marketing:</strong> The absence of a mandatory
local ad program means you are responsible for your own marketing. If you prefer a turnkey
marketing solution (like Lawn Doctor's mandatory program), Spring-Green's model requires
more initiative.</li>
<li><strong>Buyer in a market with no existing Spring-Green presence:</strong> With 126 units,
geographic coverage is thinner than Lawn Doctor's 653. You may be the only franchisee in
your region, with limited peer support and less local brand recognition.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have modeled your territory using the single-territory median ($615K) rather than the
all-business average ($1.09M), which includes multi-territory operators and inflates expectations.</li>
<li>You have a local marketing plan and budget. Without mandatory franchisor marketing, customer
acquisition is your responsibility. Table 3 shows the average franchisee spends 7.4% of
revenue on marketing — build that into your financial model.</li>
<li>You understand that the 68.1% gross margin includes direct labor (unlike Lawn Doctor's 85.4%
which excludes it). Spring-Green's margin is more conservative but more realistic as a proxy
for what you keep after direct costs.</li>
</ul>
""",

"fee_burden_narrative": """
<p>Spring-Green has the second-lowest ongoing fee burden in the lawn cohort — $45,318 (15.1%) at
$300K revenue. Only Weed Man (8.5%) is lower. The primary advantage is the absence of a mandatory
local advertising minimum: Lawn Doctor requires $30,000+ and NaturaLawn requires $60,000–$80,000,
while Spring-Green's only marketing obligation is the 2% national fund ($6,000 at $300K). At $500K,
Spring-Green's fees ($67,318, 13.5%) are less than half of NaturaLawn's ($121,584, 24.3%).</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (tiered: 10%/9%/8%):</strong> 10% on first $250K of annual Gross Sales, 9%
on $250K–$500K, 8% above $500K. First-season Industry Associate Program rates are lower
(5%/4%/3%). Multi-territory discount: after 5,000 total customers, 8% on first $250K, 7%
on $250K–$500K, 6% above $500K. Payable weekly. (pp. 16–17)</li>
<li><strong>National advertising (2% of Gross Sales):</strong> $6,000 at $300K. Simple and low.
Regional advertising fund (up to 2% additional) is authorized but not currently imposed.
If imposed, would apply only with approval of franchisees in the region. (pp. 17–18)</li>
<li><strong>Technology ($235/month + per-user licenses):</strong> $2,820/year base plus $192–$348/year
per user (Office Online or Full Office License, minimum 1 Full Office License required).
Total ~$3,168/year for a single-user setup. Subject to fee adjustment of up to 100% increase
over any 5-year period — effectively a maximum doubling over 5 years. (pp. 17–18)</li>
<li><strong>Call center ($500/month = $6,000/year):</strong> National Call Center charges
$500/month base during season (April–November), plus per-lead fees ($5/internet lead,
$7.50/phone lead). Off-season rate is lower. This is a meaningful cost — at $300K revenue,
the call center alone is 2% of gross. (p. 17)</li>
<li><strong>Convention ($650/attendee):</strong> Annual convention registration fee. Travel and
lodging additional. (p. 17)</li>
</ul>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, Spring-Green's $45,318 in fees leaves $254,682
after franchisor costs — $33,482 more than Lawn Doctor ($221,200) and $76,266 more than NaturaLawn
($198,416). Over a 10-year term, that's $335K–$763K more retained earnings vs. peers. The fee
advantage widens at higher revenue levels because the tiered royalty reduces the marginal rate.
</div>

<div class="callout">
<div class="callout-title">No mandatory local advertising floor</div>
Spring-Green is the only established brand in this cohort without a mandatory local advertising
minimum. This is a structural advantage for operators who want to control their own marketing
spend, but it is also a responsibility: Table 3 data shows the average franchisee spends 7.4%
of revenue on marketing voluntarily. If you spend $0 on local marketing, you will likely
underperform the disclosed averages.
</div>
""",

"item19_narrative": """
<p>Spring-Green discloses a solid 3-table Item 19 covering cost structure, revenue, and marketing
effectiveness. The disclosure is notable for including direct labor in the COGS calculation —
making the 68.1% gross margin more conservative and more useful than Lawn Doctor's materials-only
85.4%. (pp. 47–50)</p>

<h3>Cost structure (Table 1, 2024)</h3>
<p>62 franchised businesses with $300K+ in Gross Sales:</p>
<ul>
<li><strong>Material costs:</strong> Average 12.8%, median 12.6%.</li>
<li><strong>Direct labor costs:</strong> Average 19.1%, median 18.2%.</li>
<li><strong>Total cost of sales:</strong> Average 31.9%, median 30.8%.</li>
<li><strong>Gross profit margin:</strong> Average 68.1%, median 69.2%.</li>
</ul>
<p>This is the most useful cost disclosure in the lawn cohort because it separates materials from
labor and includes both in COGS. At 68.1% margin after materials AND labor, the franchisee retains
substantially more than the raw percentage might suggest when compared to Lawn Doctor's 85.4%
(which excludes labor entirely).</p>

<h3>Revenue (Table 2, 2024)</h3>
<p>71 franchised businesses operating 2+ years:</p>
<ul>
<li><strong>All businesses (71):</strong> Average $1,093,544, median $886,680. Range: $168K–$3.87M.</li>
<li><strong>Single territory (36):</strong> Average $743,598, median $614,679. Range: $168K–$1.75M.</li>
<li><strong>Multiple territories (32):</strong> Average $1,554,728, median $1,321,291.</li>
<li><strong>Revenue per customer:</strong> Average $556, median $549. Range: $393–$957.</li>
<li><strong>Revenue per production vehicle:</strong> Average $201,144, median $203,395.</li>
</ul>

<h3>Marketing effectiveness (Table 3, 2024)</h3>
<ul>
<li><strong>Marketing investment:</strong> Average 7.4% of revenue (median 7.9%). Range: 2.0%–20.6%.</li>
<li><strong>New service agreements per $1 of marketing:</strong> Average 0.0042, median 0.0029.
(At $50K marketing spend, this implies ~210 new agreements for the average operator.)</li>
<li><strong>Revenue per new agreement:</strong> Average $424, median $399.</li>
</ul>

<h3>What's missing</h3>
<ul>
<li><strong>Owner income or net profit:</strong> The 68.1% gross margin is after materials and
labor, but before overhead (vehicle, insurance, office, franchisor fees). No net income
data is disclosed.</li>
<li><strong>Geographic or seasonal variation:</strong> Revenue and cost data are system-wide
averages — no breakdown by region or season length.</li>
<li><strong>Customer retention rate:</strong> Revenue per customer ($556) is disclosed but
annual retention/churn rates are not.</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross revenue to owner economics</h3>
<p>Spring-Green's Item 19 provides both revenue and COGS (including labor), making triangulation
more straightforward than Lawn Doctor:</p>

<p><strong>For a median single-territory operator ($615K revenue):</strong></p>
<ul>
<li>COGS at 31.9% (materials + labor): ~$196K</li>
<li>Gross margin (68.1%): ~$419K</li>
<li>Franchisor fees (interpolated from model): ~$57K</li>
<li>Voluntary marketing at 7.4% (system average): ~$46K</li>
<li>Overhead (vehicle, insurance, office): $25K–$40K</li>
<li>Implied pre-tax owner income: $276K–$291K</li>
</ul>

<p><strong>For a conservative single-territory ($400K revenue):</strong></p>
<ul>
<li>COGS at 31.9%: ~$128K</li>
<li>Gross margin: ~$272K</li>
<li>Franchisor fees: ~$47K</li>
<li>Marketing at 7.4%: ~$30K</li>
<li>Overhead: $25K–$35K</li>
<li>Implied pre-tax owner income: $160K–$170K</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Spring-Green's economics triangulate more favorably than Lawn
Doctor's at equivalent single-territory revenue, primarily because of lower franchisor fees. At
the median ($615K), a Spring-Green operator potentially retains $276K–$291K vs. an estimated
$198K–$258K at Lawn Doctor — a $20K–$90K annual advantage. The difference is almost entirely
fee structure, not operating economics. But note: Spring-Green's voluntary marketing spend
(7.4%) should be treated as quasi-mandatory — operators who spend less likely underperform the
disclosed averages.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using Spring-Green's
disclosed Item 19 revenue and cost-of-sales data. COGS (31.9% average) includes materials AND
direct labor — a more complete cost picture than some peers. 'Remaining' must still cover
vehicle costs, insurance, office overhead, voluntary marketing spend (average 7.4% of revenue),
owner draw, and taxes. Your actual results depend on territory, labor market, season length,
customer density, and execution.</p>
""",

"economics_scenarios_config": [
    ("Conservative single-territory", 400000),
    ("Median single-territory", 615000),
    ("Average multi-territory", 1555000),
],

"economics_cogs_ratio": 0.319,

"economics_assumptions": "Revenue from Item 19 Table 2 (2024, businesses operating 2+ years). COGS at 31.9% (Table 1 average for businesses with $300K+ Gross Sales, includes materials and direct labor). 'Remaining' covers overhead, voluntary marketing, owner draw, and taxes. Industry Associate first-season royalty rates (5%/4%/3%) not modeled — these apply only to first-season operators.",

"economics_detail": "",

"payback_narrative": "",

"investment_narrative": """
<p>Mid-cohort entry cost: $117,543–$134,342 total. The franchise fee ($27,000–$45,000) varies
by territory population and is substantially lower than Lawn Doctor's $124K bundled package.
A typical new single-territory franchise pays $35,000 ($27,000 license + $8,000 territory fee).
Additional territories can be acquired at incremental territory fees.</p>
""",

"investment_detail": """
<h3>Key line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($27,000–$45,000):</strong> Base license ($27,000) plus territory fee
based on population. Multi-unit discounts available. (p. 14)</li>
<li><strong>Vehicle ($15,000–$25,000):</strong> Truck or van for equipment transport. Can start
with existing vehicle if suitable.</li>
<li><strong>Equipment ($20,000–$28,000):</strong> Spray equipment, spreaders, and supplies.
Purchased from approved vendors.</li>
<li><strong>Working capital ($15,000–$20,000):</strong> First 3–6 months of operations.</li>
<li><strong>Technology setup ($3,000–$5,000):</strong> Computer, software licenses, phone system.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> Spring-Green's $118K–$134K total is $30K–$40K less than Lawn
Doctor and comparable to NaturaLawn's mid-range. The franchise fee is the key differentiator:
Spring-Green's $27K–$45K vs. Lawn Doctor's $124K means substantially more of your investment
goes into working capital and equipment rather than upfront fees.
</div>
""",

"system_health_narrative": """
<p>Stable and unremarkable — which is not a criticism. Spring-Green's 126-unit system has been
essentially flat for three years: +2, –4, +2 net. Turnover is moderate (2.0%, 5.2%, 4.6%).
For a 48-year-old system, this suggests maturity rather than decline — the brand is holding
its position without aggressive expansion or concerning contraction.</p>
""",

"system_health_detail": """
<h3>Outlet trajectory</h3>
<ul class="compact">
<li><strong>2022:</strong> 126→128 (+2 net). 2 opened, 0 closed. 3 transfers. Turnover 2.0%.</li>
<li><strong>2023:</strong> 128→124 (–4 net). 2 opened, 4 closed, 2 non-renewals. 2 transfers.
Turnover 5.2%.</li>
<li><strong>2024:</strong> 124→126 (+2 net). 4 opened, 0 closed. 5 transfers. Turnover 4.6%.</li>
</ul>

<h3>Context on size</h3>
<p>At 126 units, small absolute numbers can create large percentage swings. The 5.2% turnover
in 2023 represents just 8 exits from a 128-unit base — hardly a systemic problem. The 5 transfers
in 2024 suggest a healthy resale market proportional to system size.</p>

<div class="implication">
<strong>What this means:</strong> Spring-Green is a mature, stable system. It is not growing
rapidly, which may concern buyers seeking expansion momentum. But it is also not contracting,
which is the more important signal for franchise durability. A buyer joining Spring-Green is
joining a system that has proven it can sustain itself at this size for decades.
</div>
""",

"risk_narrative": """
<h3>Litigation</h3>
<p>No litigation required to be disclosed (Item 3). No bankruptcy (Item 4). Clean legal
history across the system's 48-year franchise history.</p>

<h3>Entity and ownership</h3>
<p>Spring-Green Enterprises, Inc. — privately held. The company also operates Spring-Green's
tree and shrub care services as part of the franchise offering. The private ownership provides
operational stability without the leveraged acquisition dynamics that can accompany PE buyouts.</p>

<h3>Fee escalation risk</h3>
<p>The regional advertising fund (up to 2%) is not currently active and requires franchisee
approval in the region to implement. Technology fees can increase up to 100% over any 5-year
period — the most explicitly defined escalation cap in the cohort. The call center fee
($500/month + per-lead fees) is season-dependent, which creates cost variability but also
means you pay less in the off-season. (pp. 17–18)</p>

<h3>System growth concern</h3>
<p>Flat growth is not a crisis, but it is worth investigating. A system that adds 2–4 net units
per year in a growing market may be failing to attract new franchisees — or it may be
deliberately maintaining quality over growth. Ask the franchisor which it is, and why.</p>
""",

"peer_narrative": """
<p>Spring-Green occupies the center of the lawn care cohort on most dimensions: moderate cost,
solid disclosure, stable system, honest COGS definition. It is the best-balanced option for
a buyer who does not want to pay Lawn Doctor's premium, does not want Weed Man's disclosure
blackout, and does not want NaturaLawn's paradoxically high fee burden despite a low headline
royalty.</p>

<p><strong>Key comparison: Lawn Doctor.</strong> Lawn Doctor offers more data (4 tables vs. 3),
a larger system (653 vs. 126 units), and lower turnover. But it costs $33,500/year more in
fees at $300K revenue and $55,000/year more at $500K. Over 10 years, that gap is $335K–$550K.
Spring-Green's 68.1% gross margin (including labor) is also more useful for financial modeling
than Lawn Doctor's 85.4% (materials only).</p>

<p><strong>Key comparison: NaturaLawn.</strong> NaturaLawn has the lowest entry cost and highest
revenue per customer ($810 vs. $556), but its ongoing fee burden is the highest in the cohort —
$101,584 at $300K vs. Spring-Green's $45,318. NaturaLawn's $60K–$80K mandatory marketing spend
dominates the fee structure. A buyer choosing NaturaLawn over Spring-Green is paying 2.25× the
ongoing fees for a niche organic positioning — which may or may not justify the premium.</p>

<p><strong>Key comparison: Weed Man.</strong> Weed Man's 8.5% total fee burden is the lowest by far,
but Weed Man discloses zero Item 19 data. A buyer choosing Weed Man over Spring-Green saves
$20K/year in fees but loses all revenue benchmarks, margin data, and customer metrics. For
a buyer with independent market knowledge, this trade-off might work. For a first-time buyer,
it is risky.</p>
""",

"peer_decision_overlay": [
    {"priority": "Lowest ongoing fee burden (with Item 19)", "best_brand": "Spring-Green", "note": "15.1% at $300K. Weed Man is cheaper but has no Item 19."},
    {"priority": "Marketing autonomy", "best_brand": "Spring-Green", "note": "No mandatory local advertising minimum. You control your own marketing budget."},
    {"priority": "Most useful gross margin data", "best_brand": "Spring-Green", "note": "68.1% margin includes direct labor — more realistic than Lawn Doctor's materials-only 85.4%."},
    {"priority": "Largest system", "best_brand": "Lawn Doctor", "note": "653 units vs. Spring-Green's 156. Scale has operational advantages."},
    {"priority": "Highest revenue per customer", "best_brand": "NaturaLawn", "note": "$810/customer vs. Spring-Green's $556. Organic positioning commands premium pricing."},
    {"priority": "Budget-conscious buyer", "best_brand": "Weed Man or Spring-Green", "note": "Weed Man: lowest fees, no data. Spring-Green: moderate fees, solid data. Depends on your risk tolerance."},
],

"discovery_questions": [
    {"question": "The system has been essentially flat for 3 years (+2, –2, +4 net). Is this intentional, and what is the growth strategy going forward?",
     "context": "A 48-year-old system that adds 2–4 net units per year may be in maintenance mode. You want to know if the franchisor is investing in growth or managing a mature portfolio.",
     "strong_answer": "They articulate a specific growth plan — target markets, recruitment strategy, conversion franchise program. Honest about historical growth pace and reasons.",
     "evasion": "They claim aggressive growth plans without evidence, or they cannot explain why growth has been flat despite a 48-year brand.",
     "follow_up": "How many franchise inquiries do you receive per year, and what is the close rate?"},
    {"question": "Table 1 shows 68.1% average gross margin including labor. What is the typical labor cost breakdown — seasonal vs. year-round employees, and how many technicians for a single-territory operation?",
     "context": "Labor at 19.1% of revenue is the largest single cost. Understanding labor structure is critical for your financial model.",
     "strong_answer": "They provide benchmarks: typical crew size, seasonal vs. year-round ratio, labor cost per production vehicle. Even better if they share data on labor markets by region.",
     "evasion": "They redirect to the 68.1% margin without drilling into the labor component, or they say 'it varies' without any benchmarks.",
     "follow_up": "What is the average revenue per employee for a single-territory operation?"},
    {"question": "Revenue per customer averages $556 with a median of $549. How many customers does a median single-territory operator serve, and what is annual customer retention?",
     "context": "At $615K median revenue and $549 median revenue per customer, a single-territory operator serves roughly 1,120 customers. You need to know the churn rate to model acquisition costs.",
     "strong_answer": "They provide customer counts by territory size and annual retention rates. The data should be consistent with the revenue and revenue-per-customer figures.",
     "evasion": "They cannot provide customer retention data, or they cite only new customer acquisition without discussing churn.",
     "follow_up": "What is the typical cost to acquire a new customer, and how does it compare to the Table 3 marketing effectiveness data?"},
    {"question": "The franchise fee ranges from $27K to $45K based on territory population. How is territory size determined, and can I see examples of territory maps?",
     "context": "Territory design directly affects revenue potential. Understanding the methodology helps you evaluate whether your specific territory can support the revenue benchmarks in Item 19.",
     "strong_answer": "They explain the population-based methodology, show example territories, and discuss how territory size correlates with revenue in the Item 19 data.",
     "evasion": "They are vague about territory design or unwilling to show examples before you commit.",
     "follow_up": "What is the average population per territory for the 36 single-territory operators in Table 2?"},
    {"question": "The regional advertising fund (up to 2% additional) requires franchisee approval. Has this ever been proposed or implemented in any region?",
     "context": "If activated, this would increase the marketing cost by $6,000–$10,000/year at $300K–$500K revenue.",
     "strong_answer": "Clear history of whether the fund has been proposed, voted on, or implemented in any region. Honest about the approval process.",
     "evasion": "Dismissive ('we've never used it') without explaining the governance process.",
     "follow_up": "What voting threshold is required, and how are regions defined?"},
    {"question": "The technology fee has a cap of 100% increase over any 5-year period. What has been the historical pattern of technology fee increases?",
     "context": "A $235/month fee that can double to $470/month over 5 years is a meaningful escalation. You want to know the actual historical trajectory.",
     "strong_answer": "They provide the history of technology fee changes and explain what service improvements accompanied each increase.",
     "evasion": "They dismiss the concern without providing historical data.",
     "follow_up": "Are there additional technology costs beyond the base fee and user licenses that I should budget for?"},
    {"question": "Table 3 shows marketing effectiveness data — 0.0042 new agreements per $1 of marketing spend. How does this compare to your internal benchmarks, and what marketing channels drive the most agreements?",
     "context": "Unique disclosure. You want to understand whether the average marketing ROI is achievable in your market.",
     "strong_answer": "They discuss which channels (direct mail, digital, door-to-door) are most effective and provide regional variation data.",
     "evasion": "They cannot explain the marketing effectiveness data or redirect to 'it depends on your market.'",
     "follow_up": "What is the recommended marketing mix for a new single-territory operator in a suburban market?"},
    {"question": "Revenue per production vehicle averages $201K. How many vehicles does a typical single-territory operator run, and is there a minimum?",
     "context": "At $615K median single-territory revenue, this implies roughly 3 vehicles per territory. Vehicle count directly affects labor costs and capital requirements.",
     "strong_answer": "They explain the relationship between territory size, vehicle count, and revenue. Provide benchmarks for new vs. mature territories.",
     "evasion": "They cannot connect vehicle count to the revenue data, or they provide only system-wide averages without territory-level context.",
     "follow_up": "What is the average cost per production vehicle including equipment and insurance?"},
],

},  # end spring-green


"naturalawn": {

"executive_summary": """
<p>NaturaLawn of America is a 36-year-old, privately held lawn care franchise specializing in
organic-based lawn care — a distinct niche positioning that commands the highest revenue per
customer in the cohort ($810, vs. $765 for Lawn Doctor and $556 for Spring-Green). The 88-unit
system is the smallest in the active cohort, growing from 81 to 90 over 2022–2023
before slipping to 88 (–2 net in 2024). Turnover is exceptional: 0% in 2022 and 2023, 2% in
2024 — the lowest attrition of any brand in the lawn cohort.</p>

<p>The paradox of NaturaLawn is that its headline fees appear low (9% royalty, 1% ad fund)
while its actual fee burden is the highest in the cohort. At $300K revenue, total franchisor
fees are $101,584 (33.9%). The driver: a mandatory $60,000–$80,000 annual marketing spend
disclosed in Item 7, which dwarfs the 1% national advertising contribution and represents
the single largest franchisee cost outside of labor and royalty. This marketing requirement is
not captured in the royalty or ad fund line items — it is an Item 7 investment requirement that
persists as an ongoing operating cost.</p>

<p>The Item 19 is split between company-owned (6 locations, with gross margin data) and
franchised (40 locations operating 5+ years, revenue and customer data only). Franchised
average revenue is $2.19M (median $1.10M) — high numbers, but the right-skew is extreme
(range $252K–$9.73M) and only 50% meet or exceed the average. The company-owned gross margin
(60.7–65.2%, including labor) provides a useful benchmark but is from a sample of only 6
locations, all in the Mid-Atlantic. Whether these margins transfer to franchised operations
in other markets is uncertain.</p>
""",

"scorecard": [
    {"dimension": "Entry cost burden", "rating": "Strong", "color": "strong",
     "summary": "Lowest entry floor in cohort: $77,500–$152,650. Franchise fee ($19,500–$39,500) is well below Lawn Doctor's $124K. But $60K–$80K mandatory marketing spend is an ongoing cost disclosed in Item 7."},
    {"dimension": "Ongoing fee burden", "rating": "Weak", "color": "weak",
     "summary": "Highest in cohort: 33.9% at $300K (6th of 6). Driven by $60K–$80K mandatory marketing spend. Headline 9% royalty + 1% ad fund is misleading without the marketing obligation."},
    {"dimension": "System stability", "rating": "Strong", "color": "strong",
     "summary": "Exceptional turnover: 0%, 0%, 2% over 3 years. 88 units — small but extraordinarily stable. Not a single exit in 2 of 3 years."},
    {"dimension": "Revenue disclosure", "rating": "Mixed", "color": "mixed",
     "summary": "2-table Item 19 split between 6 company-owned (with margin) and 40 franchised (revenue only). Franchised avg $2.19M, median $1.10M. Small samples limit statistical confidence."},
    {"dimension": "Disclosure quality", "rating": "Mixed", "color": "mixed",
     "summary": "Item 3 contradiction: states 'no litigation required to be disclosed' then discloses the Ford TCPA case. Gross margin data only from 6 company-owned locations. Population discrepancy in franchised data (40+7≠44)."},
    {"dimension": "Downside risk profile", "rating": "Mixed", "color": "mixed",
     "summary": "Fee burden is primary risk. Organic niche may limit addressable market. Small system (88 units) means less peer support. Royalty drops to 7% on renewal only if $500K+ revenue maintained."},
    {"dimension": "Buyer fit breadth", "rating": "Mixed", "color": "mixed",
     "summary": "Strong for buyers committed to organic positioning with $100K+ capital. Weaker for budget-sensitive buyers or those in markets where organic lawn care has limited demand."},
    {"dimension": "Overall", "rating": "Notable", "color": "mixed",
     "summary": "The strongest niche positioning and lowest turnover in the cohort, offset by the highest fee burden and smallest sample sizes in the Item 19. The organic premium commands higher revenue per customer but costs more to maintain through mandatory marketing. Relative cohort position does not establish absolute profitability."},
],

"scorecard_posture": """NaturaLawn is the niche specialist in this cohort — organic-based lawn care
with the highest revenue per customer and lowest franchise turnover. The zero-attrition record
(0% in 2 of 3 years) is extraordinary and suggests strong franchisee satisfaction. But the
fee structure is misleading at first glance: the 9% royalty and 1% ad fund look competitive, but the $60K–$80K
mandatory marketing spend (disclosed in Item 7, not Item 6) pushes total fees to the highest
in the cohort. A buyer must evaluate whether the organic niche commands enough premium pricing
in their specific market to absorb these costs — and whether 88 units with limited Item 19
samples provide enough evidence to build confidence.""",

"buyer_fit_narrative": """
<h3>Best fit for</h3>
<ul class="fit-list">
<li><strong>Buyer committed to organic/environmental positioning:</strong> If you believe organic
lawn care is a growing market and are willing to invest in that niche, NaturaLawn offers the
only pure-play organic franchise in the cohort. The $810 average revenue per customer is 46%
higher than Spring-Green's $556 — organic commands premium pricing.</li>
<li><strong>Buyer in affluent suburban markets with environmental awareness:</strong> The organic
premium works best in markets where customers will pay more for natural alternatives. Median
franchised revenue of $1.10M suggests strong economics in the right markets.</li>
<li><strong>Buyer who values franchisee community:</strong> Zero turnover in 2 of 3 years means
the franchise community is exceptionally stable. Peer support from long-tenured franchisees
is a real advantage for new operators.</li>
<li><strong>Buyer planning to grow past $500K:</strong> The royalty drops from 9% to 7% upon
renewal if Gross Sales exceed $500K — a meaningful 2-point reduction that rewards scale.
Combined with the 1% ad fund, the core franchise fees become competitive above $500K.</li>
</ul>

<h3>Weaker fit for</h3>
<ul class="fit-list">
<li><strong>Budget-sensitive buyer focused on fee burden:</strong> Despite the low entry cost,
the $60K–$80K annual marketing spend makes NaturaLawn the most expensive brand to operate
in the cohort. At $300K revenue, a third of gross goes to the franchisor.</li>
<li><strong>Buyer in price-sensitive markets:</strong> If your local market does not support
organic premium pricing ($810/customer average), the economics tighten rapidly. The high
fee burden only works at premium revenue per customer.</li>
<li><strong>Buyer who needs robust Item 19 data:</strong> The franchised sample (40 locations)
is reasonable, but gross margin data comes from only 6 company-owned locations. If you
need statistical confidence in the margin benchmarks, NaturaLawn's disclosure is thin.</li>
<li><strong>Buyer seeking system scale:</strong> 88 units is small. You will have fewer peers,
less brand recognition in many markets, and less negotiating leverage with vendors.</li>
</ul>

<h3>Proceed only if</h3>
<ul class="fit-list">
<li>You have verified that organic lawn care commands premium pricing in your specific market.
The $810 average revenue per customer is a system-wide figure — your local market may differ.</li>
<li>You have modeled the $60K–$80K annual marketing spend as a fixed cost, not a variable one.
This obligation exists regardless of your revenue level.</li>
<li>You understand that the 60.7–65.2% gross margin is from 6 company-owned locations in the
Mid-Atlantic. If you are operating in a different region, this benchmark may not transfer.</li>
</ul>
""",

"fee_burden_narrative": """
<p>NaturaLawn has the highest ongoing fee burden in the lawn cohort at every revenue level: 45.8%
at $200K, 33.9% at $300K, 24.3% at $500K. The headline rates (9% royalty, 1% ad fund) are
mid-range, but the $60,000–$80,000 mandatory annual marketing spend — disclosed in Item 7
rather than Item 6 — dominates the cost structure. At $300K revenue, marketing alone represents
$73,000 (24.3% of revenue), dwarfing the royalty ($27,000) and everything else combined.</p>
""",

"fee_burden_detail": """
<h3>Component breakdown</h3>
<ul class="compact">
<li><strong>Royalty (9% flat, 7% on renewal if $500K+):</strong> 9% of Gross Sales during
initial term. Reduces to 7% upon renewal if Gross Sales exceeded $500K in the last full
calendar year before renewal AND are maintained at $500K+. If revenue drops below $500K
after renewal, rate reverts to 9%. (pp. 16–17)</li>
<li><strong>Advertising fee (1% of Gross Sales):</strong> The lowest national ad fund in the
cohort. Simple and transparent. (p. 16)</li>
<li><strong>Mandatory marketing spend ($60,000–$80,000/year):</strong> This is the critical
cost. Disclosed in Item 7 as an initial investment line item, but it is an ongoing annual
obligation. The FDD notes this as the expected annual marketing investment. This spend is
franchisee-directed (unlike Lawn Doctor's franchisor-managed program), which gives you more
control but also more responsibility. (Item 7)</li>
<li><strong>Technology ($132/month first user + $58–$74 additional):</strong> Real Green Service
Assistant 5, cloud-based. First user $132/month ($1,584/year). Additional users at reduced
rates. Modest relative to peers. (p. 17)</li>
<li><strong>No call center fee:</strong> NaturaLawn does not charge a mandatory call center fee —
one of only two brands in the cohort (with Weed Man) without this cost.</li>
</ul>

<div class="callout">
<div class="callout-title">The Item 7 marketing spend is the fee in disguise</div>
NaturaLawn's 1% ad fund is the lowest in the cohort. But the $60K–$80K annual marketing spend
— listed as an Item 7 investment line rather than an Item 6 ongoing fee — is the highest mandatory
marketing cost of any lawn brand. By comparison, Lawn Doctor's $30K local ad minimum is disclosed
in Item 6 as an ongoing fee. The economic effect is the same; only the disclosure location differs.
A buyer comparing NaturaLawn's "1% ad fund" to Lawn Doctor's "10% marketing" without reading
Item 7 will dramatically underestimate NaturaLawn's true cost.
</div>

<div class="implication">
<strong>What this means:</strong> At $300K revenue, NaturaLawn's $101,584 in total fees exceeds
Lawn Doctor ($78,800) by $22,784 and Spring-Green ($45,318) by $56,266. The entire difference
is the marketing spend. Over a 10-year term, a NaturaLawn operator sends $228K–$563K more to
the franchisor than Spring-Green or Lawn Doctor operators at equivalent revenue. The organic
premium ($810/customer vs. $556–$765) must justify this gap.
</div>
""",

"item19_narrative": """
<p>NaturaLawn's Item 19 provides two tables: one for company-owned locations (gross margin + revenue)
and one for franchised locations (revenue and customers only). The split means you get margin
data from a very small company-owned sample and revenue data from a moderate franchised
sample — but not both from the same population.</p>

<h3>Company-owned locations (Table 1, 2024)</h3>
<p>6 locations operating 5+ years in Damascus MD, Virginia Beach VA, Newport News VA,
Richmond VA, Manassas VA, and Greenville SC:</p>
<ul>
<li><strong>Gross profit margin:</strong> 60.7%–65.2% range (includes direct labor in COGS).
Comparable to Spring-Green's 68.1% on the same COGS basis.</li>
<li><strong>Average revenue:</strong> $1.73M (median $1.52M). Range: $528K–$3.32M.</li>
<li><strong>Average customers:</strong> 2,304 (median 1,971).</li>
<li><strong>Revenue per customer:</strong> $740 (median $740). Consistent across the 6 locations.</li>
</ul>

<h3>Franchised locations (Table 2, 2024)</h3>
<p>40 franchised locations operating 5+ years:</p>
<ul>
<li><strong>Average revenue:</strong> $2,192,129 (median $1,097,125). Range: $252K–$9.73M.
Extreme right-skew — the top franchise is nearly 40× the bottom. Only 50% met or exceeded
the average.</li>
<li><strong>Average customers:</strong> 2,707 (median 1,716). Same right-skew pattern.</li>
<li><strong>Revenue per customer:</strong> $810 (median $696). Range: $361–$1,386.
The highest in the lawn cohort.</li>
</ul>

<h3>Critical limitations</h3>
<ul>
<li><strong>Small sample bias:</strong> 6 company-owned locations is too small for statistical
confidence. All 6 are in the Mid-Atlantic — margins may differ in other climates and
labor markets.</li>
<li><strong>No franchised margin data:</strong> The 60.7–65.2% margin is from company-owned
only. The FDD explicitly states franchised data was excluded from margin analysis "due
to differences in accounting methodology." You cannot assume franchised margins match.</li>
<li><strong>Population discrepancy:</strong> The FDD states 44 franchised locations total, 40
operating 5+ years, 7 operating less than 5 years — but 40 + 7 = 47, not 44. This
arithmetic inconsistency should be clarified with the franchisor.</li>
<li><strong>Revenue skew:</strong> The $9.73M top franchise pulls the average to $2.19M while
the median is only $1.10M. The median is the better benchmark for a new single-territory
operator.</li>
</ul>
""",

"item19_triangulation": """
<h3>From gross revenue to owner economics</h3>
<p>Using company-owned gross margin (60.7–65.2%) as a proxy for franchised operations:</p>

<p><strong>For a median franchised location ($1.10M revenue):</strong></p>
<ul>
<li>COGS at ~37% (midpoint of 34.8–39.3%): ~$407K</li>
<li>Gross margin (~63%): ~$693K</li>
<li>Franchisor fees (interpolated): ~$171K (royalty $99K + ad $11K + marketing $60K + tech $1.6K)</li>
<li>Overhead (vehicle, insurance, office): $40K–$60K</li>
<li>Implied pre-tax owner income: $462K–$482K</li>
</ul>

<p><strong>For a conservative franchised location ($500K revenue):</strong></p>
<ul>
<li>COGS at ~37%: ~$185K</li>
<li>Gross margin: ~$315K</li>
<li>Franchisor fees: ~$117K (royalty $45K + ad $5K + marketing $65K + tech $1.6K)</li>
<li>Overhead: $35K–$50K</li>
<li>Implied pre-tax owner income: $148K–$163K</li>
</ul>

<div class="callout">
<div class="callout-title">The marketing spend is fixed, not variable</div>
The $60K–$80K marketing obligation does not scale with revenue. At $1.1M revenue, it represents
5.5–7.3% of gross — manageable. At $500K, it jumps to 12–16% — punitive. At $300K, it is
20–27% of revenue before royalty and ad fund. NaturaLawn's economics work at the median
($1.1M) but deteriorate rapidly below $600K because the marketing spend does not flex downward.
</div>

<div class="implication">
<strong>What this means:</strong> At median revenue ($1.1M), NaturaLawn appears to generate strong
owner income ($460K+) — comparable to or exceeding peers. But the fixed marketing spend creates
a higher breakeven threshold. A NaturaLawn operator needs to reach roughly $600K+ in revenue before
the economics become comfortable. Below that, the fixed marketing cost consumes a disproportionate
share of gross margin.
</div>
""",

"economics_preamble": """
<p style="font-size:0.88rem; color:#555; margin-bottom:0.25rem;"><strong>Important framing:</strong>
This is not a profitability forecast. It is an illustrative scenario exercise using NaturaLawn's
disclosed Item 19 data. COGS is estimated using the company-owned gross margin (60.7–65.2%),
which includes direct labor. The FDD does not disclose franchised gross margins. The $60K–$80K
annual marketing spend is modeled as a fixed cost. Your actual results depend on your territory,
local demand for organic lawn care, labor market, customer acquisition costs, and execution.</p>
""",

"economics_scenarios_config": [
    ("Conservative ($500K)", 500000),
    ("Median franchised", 1097000),
    ("Average franchised", 2192000),
],

"economics_cogs_ratio": 0.37,

"economics_assumptions": "Revenue from Item 19 Table 2 (2024, 40 franchised locations operating 5+ years). COGS estimated at 37% based on midpoint of company-owned gross margin range (60.7–65.2%), which includes direct labor — not from franchised data. 'Remaining' must cover the $60K–$80K mandatory marketing spend, overhead, owner draw, and taxes. Marketing spend is modeled separately at $65K (midpoint) because it is a fixed cost, not a variable one.",

"economics_detail": "",

"payback_narrative": "",

"investment_narrative": """
<p>Lowest entry floor in the cohort: $77,500–$152,650. The franchise fee ($19,500–$39,500) varies
by territory size and is 3–6× lower than Lawn Doctor's $124K. But the Item 7 also includes
the first year of the $60,000–$80,000 mandatory marketing spend — which is an ongoing annual
cost, not a one-time investment. The low entry cost is real, but the first-year cash burn
is higher than the headline investment range suggests.</p>
""",

"investment_detail": """
<h3>Key line items</h3>
<ul class="compact">
<li><strong>Franchise fee ($19,500–$39,500):</strong> Varies by territory population. Includes
initial training and setup support. Substantially below peers. (p. 14)</li>
<li><strong>Marketing first year ($60,000–$80,000):</strong> This is the dominant cost. It
is disclosed as an initial investment but persists annually. Budget it as an ongoing
$65K/year cost from year one forward. (Item 7)</li>
<li><strong>Equipment and vehicle ($10,000–$18,000):</strong> Spray equipment, spreader, and
delivery vehicle. Can start with existing vehicle if suitable.</li>
<li><strong>Working capital ($5,000–$15,000):</strong> First 3 months of operations.</li>
</ul>

<div class="implication">
<strong>What this means:</strong> NaturaLawn's low franchise fee makes it the cheapest to enter,
but the mandatory marketing spend makes it the most expensive to operate. A buyer should model
total first-year costs (investment + $65K marketing + operating costs) rather than just the
Item 7 range. The effective first-year cash requirement is closer to $140K–$230K when marketing
is included.
</div>
""",

"system_health_narrative": """
<p>Smallest system in the active cohort (88 units) but the most stable by turnover metrics:
0% attrition in 2022 and 2023, 2% in 2024. Not a single franchisee exited the system for
two consecutive years — a result that no other lawn brand (or any brand in this product's
library) matches. Growth has been modest: +3, +6, –2 net over three years.</p>
""",

"system_health_detail": """
<h3>Outlet trajectory</h3>
<ul class="compact">
<li><strong>2022:</strong> 81→84 (+3 net). 3 opened, 0 closed, 0 non-renewals, 0 transfers.
Turnover 0%.</li>
<li><strong>2023:</strong> 84→90 (+6 net). 6 opened, 0 closed, 0 non-renewals, 0 transfers.
Turnover 0%.</li>
<li><strong>2024:</strong> 90→88 (–2 net). 0 opened, 2 closed, 0 non-renewals, 0 transfers.
Turnover 2% (based on derived turnover rate calculation).</li>
</ul>

<h3>Interpreting the zero-turnover years</h3>
<p>Zero exits from an 84–90 unit system for two consecutive years is extraordinary. In most
franchise systems, structural attrition (retirements, market exits, relocations) produces
at least 2–5% turnover annually. Zero suggests either very high franchisee satisfaction,
limited exit options, or both. The absence of any transfers is also notable — no franchisee
sold their territory, which could mean the resale market is illiquid or franchisees simply
don't want to sell.</p>

<p>The 2024 result (–2 net, 0 openings) is the first year without growth. No new franchisees
joined. Whether this reflects the franchisor's choice to pause recruitment, market saturation,
or declining attractiveness is worth investigating during diligence.</p>

<div class="implication">
<strong>What this means:</strong> NaturaLawn's attrition data is the strongest positive signal
in the entire lawn cohort. Existing franchisees are staying. But the 2024 stall (0 openings,
–2 net) is a yellow flag that warrants investigation. A system that stops adding new franchisees
may be signaling capacity constraints, market limitations, or franchisor strategic choices —
any of which affect your outlook as a new entrant.
</div>
""",

"risk_narrative": """
<h3>Litigation</h3>
<p>The Item 3 disclosure contains a contradiction: it states "no litigation is required to be
disclosed" and then immediately discloses the Ford v. NaturaLawn TCPA case — a putative class
action alleging unsolicited marketing calls/texts in violation of the Telephone Consumer
Protection Act. The case status and outcome should be verified during diligence. The
contradictory disclosure framing is a minor quality flag. (pp. 12–14)</p>

<h3>Entity and ownership</h3>
<p>NaturaLawn of America, Inc. — privately held, founder-led. No parent company or PE ownership
disclosed. The private, founder-led structure provides operational stability and alignment
between franchisor leadership and brand mission (organic lawn care). No institutional exit
pressure. This is the only founder-led brand in the lawn cohort.</p>

<h3>Fee structure deception risk</h3>
<p>The gap between headline fee rates (9% royalty, 1% ad fund = 10% of revenue) and actual
total burden (33.9% at $300K) is the widest in the cohort. A buyer who evaluates NaturaLawn
based on Item 6 alone will dramatically underestimate the true cost. The $60K–$80K marketing
spend in Item 7 is the single largest fee and is easy to overlook if you are not reading
Item 7 as an ongoing cost. (Item 7)</p>

<h3>Niche market risk</h3>
<p>Organic-based lawn care is a niche within a niche. If consumer preferences shift away from
organic premium services, or if conventional competitors adopt "green" messaging without
the cost, NaturaLawn's pricing power could erode. The $810/customer premium depends on
customers continuing to pay more for organic positioning.</p>

<h3>Renewal royalty reduction</h3>
<p>The 7% renewal royalty (vs. 9% initial) requires maintaining $500K+ in Gross Sales. If
revenue drops below $500K after renewal, the rate reverts to 9%. This creates a cliff
effect at $500K that should be modeled explicitly. (pp. 16–17)</p>
""",

"peer_narrative": """
<p>NaturaLawn occupies a unique position in the lawn cohort: niche organic specialist with the
highest revenue per customer and lowest turnover, but also the highest fee burden and smallest
system. It is the premium play — you pay more and you bet on organic demand.</p>

<p><strong>Closest comparison: Spring-Green.</strong> Both are mid-sized systems with moderate entry
costs. But Spring-Green's total fees at $300K are $45,318 (15.1%) vs. NaturaLawn's $101,584
(33.9%). The $56,266 annual gap is almost entirely the marketing spend obligation. NaturaLawn's
revenue per customer is 46% higher ($810 vs. $556), which partially offsets the fee gap — but
only if your market supports organic premium pricing.</p>

<p><strong>The fee paradox: NaturaLawn vs. Lawn Doctor.</strong> Lawn Doctor (26.3% at $300K) is
perceived as the expensive brand, but NaturaLawn (33.9%) is actually more expensive at every
modeled revenue level. The difference is disclosure framing: Lawn Doctor's costs are in Item 6
(easy to find), while NaturaLawn's marketing obligation is in Item 7 (easy to miss). A buyer
comparing these two should look at total dollar outflow, not headline rates.</p>

<p><strong>Versus Weed Man:</strong> The polar opposite. Weed Man's 8.5% total fees are 4× lower
than NaturaLawn's 33.9%. Weed Man has no Item 19 and no organic positioning, but its fee structure
leaves dramatically more revenue in the franchisee's pocket. A buyer choosing NaturaLawn over
Weed Man is betting that organic positioning and the NaturaLawn brand generate enough additional
revenue per customer to overcome a $76,000/year fee gap.</p>
""",

"peer_decision_overlay": [
    {"priority": "Organic/environmental niche", "best_brand": "NaturaLawn", "note": "Only organic-first brand in the cohort. $810/customer vs. $556–$765 for peers."},
    {"priority": "Lowest franchise turnover", "best_brand": "NaturaLawn", "note": "0% turnover in 2 of 3 years. Extraordinary franchisee retention."},
    {"priority": "Lowest entry cost", "best_brand": "NaturaLawn", "note": "$78K–$153K total — but ongoing costs are the highest due to mandatory marketing spend."},
    {"priority": "Lowest ongoing fees", "best_brand": "Weed Man (no Item 19) / Spring-Green (with Item 19)", "note": "NaturaLawn is the most expensive to operate at every revenue level."},
    {"priority": "Best revenue disclosure", "best_brand": "Lawn Doctor", "note": "NaturaLawn's Item 19 is limited to 6 company-owned + 40 franchised vs. Lawn Doctor's 205 SPs with 16-year trend."},
    {"priority": "Founder-led stability", "best_brand": "NaturaLawn", "note": "Only founder-led brand. No PE exit pressure. Aligned incentives between franchisor and mission."},
],

"discovery_questions": [
    {"question": "The $60,000–$80,000 annual marketing spend is disclosed in Item 7. What specifically does this fund, who manages it, and can it be reduced in a down year?",
     "context": "This is the single largest cost component and dominates the fee burden. Understanding its flexibility is critical.",
     "strong_answer": "They explain exactly where the money goes (digital, direct mail, local events), whether it is franchisor-directed or franchisee-managed, and whether there is any flexibility for new or struggling operators.",
     "evasion": "They minimize the cost, redirect to the 1% ad fund, or claim 'it varies' without providing the actual spend range for comparable territories.",
     "follow_up": "What is the average marketing cost per acquired customer, and how does it compare to the revenue per customer ($810 average)?"},
    {"question": "The gross margin data (60.7–65.2%) comes from 6 company-owned locations, all in the Mid-Atlantic. Do you have any franchised gross margin data, even informal?",
     "context": "The FDD explicitly excludes franchised margins due to 'differences in accounting methodology.' You need to understand if company-owned margins transfer to franchised operations.",
     "strong_answer": "They acknowledge the limitation and provide informal benchmarks from franchisees, or they explain what accounting differences exist and how they affect margin comparisons.",
     "evasion": "They cite the company-owned margins as representative without addressing the accounting methodology differences the FDD itself flags.",
     "follow_up": "What is the primary accounting difference between company-owned and franchised operations that prevents you from disclosing franchised margins?"},
    {"question": "Average franchised revenue is $2.19M but median is $1.10M — a 2:1 ratio. What drives this extreme right-skew?",
     "context": "One franchise at $9.73M pulls the average well above the median. You want to know if the distribution reflects territory size variation, operator quality, or multi-location consolidation.",
     "strong_answer": "They explain the distribution — whether high-revenue franchises are multi-territory, have been operating longer, or are in premium markets. Honest about what a realistic first-5-year trajectory looks like.",
     "evasion": "They cite the average ($2.19M) as representative and do not address the skew or the $252K bottom end.",
     "follow_up": "What is the typical first-year and third-year revenue trajectory for a new single-territory franchisee?"},
    {"question": "Zero openings in 2024 and 2 net losses. Why did the system stop growing?",
     "context": "After adding 3 and 6 new franchisees in 2022–2023, adding 0 in 2024 is a sharp break in pattern.",
     "strong_answer": "Honest explanation — whether it was a strategic pause, recruitment difficulty, territory saturation, or operational choice. Ideally with plans for 2025–2026.",
     "evasion": "They dismiss the concern or blame external factors without acknowledging the trend break.",
     "follow_up": "How many franchise inquiries did you receive in 2024, and how many were qualified?"},
    {"question": "The royalty drops from 9% to 7% on renewal if revenue exceeds $500K. How many franchisees have achieved this reduction?",
     "context": "If the median franchised revenue is $1.10M, most mature franchisees should qualify. But you want to verify this and understand what happens if revenue drops temporarily.",
     "strong_answer": "They provide the percentage of franchisees on the 7% renewal rate and explain the revenue maintenance requirement clearly.",
     "evasion": "They cannot say how many franchisees qualify or avoid discussing the reversion to 9% if revenue drops below $500K.",
     "follow_up": "Is there a grace period if revenue dips below $500K temporarily (e.g., due to weather or COVID-type events)?"},
    {"question": "The population note says 44 franchised locations total, 40 operating 5+ years, 7 operating less than 5 years. 40 + 7 = 47, not 44. Can you explain this discrepancy?",
     "context": "Arithmetic errors in disclosure documents are worth flagging. It may be harmless, but it could indicate sloppy internal data management.",
     "strong_answer": "They can explain it — perhaps 3 locations closed or changed status between the reference dates. Honest about the inconsistency.",
     "evasion": "They don't acknowledge the discrepancy or claim it doesn't matter.",
     "follow_up": "Can you provide the current unit count as of today?"},
    {"question": "Revenue per customer is $810 on average but $696 at the median, with a range of $361–$1,386. What drives the variation? Is it geographic, service-mix, or pricing-strategy differences?",
     "context": "The revenue per customer premium is NaturaLawn's core competitive advantage. Understanding what drives it — and whether it is replicable in your market — is essential.",
     "strong_answer": "They explain service tiers, upsell strategies, and geographic pricing variation. They provide regional benchmarks if available.",
     "evasion": "They cite the average without explaining the distribution or acknowledging the $361 bottom end.",
     "follow_up": "What is the revenue per customer for franchisees in my target region?"},
    {"question": "The Ford v. NaturaLawn TCPA class action is disclosed in Item 3 despite the heading stating no litigation needs disclosure. What is the current status and potential exposure?",
     "context": "TCPA class actions can result in significant damages ($500–$1,500 per violation). The contradictory disclosure framing is itself a quality concern.",
     "strong_answer": "They provide a clear update on the case status, the potential financial exposure, and whether the marketing practices that led to the suit have been changed.",
     "evasion": "They minimize the case or don't know the current status.",
     "follow_up": "Have any marketing practices changed as a result of this litigation?"},
],

},  # end naturalawn

}  # end LAWN_NARRATIVES
