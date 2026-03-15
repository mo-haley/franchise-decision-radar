# Item 19 Normalization Plan — Mosquito Pest Control Cohort

**Cohort:** Mosquito Authority, Mosquito Hunters, Mosquito Joe, Mosquito Shield, Mosquito Squad
**Source:** 2025 FDDs filed with Wisconsin DFI
**Date:** 2026-03-14

---

## 1. What Each Brand Actually Discloses in Item 19

### Mosquito Authority
- **Company-owned P&L:** Full dollar amounts for 1 territory (Hickory, NC). Revenue,
  COGS, expenses, EBITDA, depreciation, amortization, net income. 2023 and 2024.
- **Franchised gross revenue distributions:** Average gross revenue ($464,600) for 128
  qualifying franchisees (506 territories). Revenue brackets by franchisee count,
  territory count, ownership length, and years active.
- **What it does NOT provide:** Per-territory revenue (reports per franchisee, who may
  own multiple territories). Franchised cost data or profitability.
- **Data quality issue:** `#REF!` error in 10+ Full Seasons average cell. Minor
  population count mismatch (129/508 vs stated 128/506).

### Mosquito Hunters
- **Per-treatment pricing:** Average and median mosquito treatment price by 4 regions
  ($72–$88 avg). Non-mosquito treatment pricing.
- **Per-customer value:** Average annual customer value by region ($726–$1,232 for
  mosquito-only).
- **Customer counts:** By quartile for qualifying Strategic-Partners.
- **Holiday lighting pilot:** Revenue per franchisee ($64,727 avg, 26 SPs).
- **What it does NOT provide:** Total gross revenue per franchise unit. Any P&L data.
  Any cost data.
- **Exclusion rate:** 26% of Strategic-Partners excluded, including 8 who "failed to
  invest in MH marketing programs." This exclusion criterion biases data upward.

### Mosquito Joe
- **Retention metrics:** 77% customer retention, 89% recurring customer rate.
- **Per-treatment revenue:** $90.54 average gross sales per treatment (410 businesses).
- **Gross sales by tenure:** First 5 Years avg $214,794 / median $287,832. 6+ Years
  avg $432,954 / median $339,460. Plus customer counts and job counts by same tenure split.
- **What it does NOT provide:** Company-owned P&L. Cost data. Per-territory breakdown.
- **Data quality issue:** Column header copy errors (3 tables). Statistical anomaly:
  median exceeds average (left-skewed distribution).
- **Exclusion:** 24 closed businesses excluded, plus 5 not reporting full year. ~7% rate.

### Mosquito Shield
- **Company-owned cost structure:** Adjusted EBITDA 29.5% of revenue. Full cost
  percentage breakdown. But NO absolute revenue figure — only percentages.
- **Franchisee gross sales by quartile:** Average $285,839 / median $134,918 for 81
  qualifying outlets. System-wide sales totals ($25.7M in 2024).
- **Retention data:** 85% returning YoY. $715 avg revenue per customer. $7.1M prepay.
- **What it does NOT provide:** Dollar-amount company-owned revenue. Franchised cost
  data or profitability.
- **Exclusion rate:** 21% — 26 "non-conforming" outlets excluded. Highest exclusion
  rate in cohort. "Non-conforming" is undefined.

### Mosquito Squad
- **Per-territory gross revenue by quartile:** Average $484,506 across 207 territories.
  Full quartile breakdown with aggregate, average, median, high, low.
- **Close rate:** 48% average (75 franchisees, 183 territories).
- **Renewal rate:** 70% average.
- **Per-appointment revenue:** $98 average.
- **Per-customer revenue:** $705 average.
- **Systemwide sales growth:** 5-year trend ($81M–$124M). Same-store growth 5%.
- **Company-owned full P&L:** $20.8M revenue, 14 territories, 25.9% net margin.
  Full dollar breakdown of COGS and OpEx.
- **What it does NOT provide:** Franchised cost data or profitability.
- **Exclusion rate:** ~8% (19 of 226 territories excluded for valid reasons).

---

## 2. Cross-Brand Comparisons That Are Realistically Possible

### A. Per-Treatment / Per-Appointment Revenue
**Brands with data:** Mosquito Hunters, Mosquito Joe, Mosquito Squad

| Brand | Metric | Value |
|---|---|---|
| Mosquito Squad | Avg gross revenue per appointment | $98 |
| Mosquito Joe | Avg gross sales per treatment | $90.54 |
| Mosquito Hunters | Avg mosquito treatment price (Region 2, largest) | $78.14 |

**Assessment:** Roughly comparable, but "appointment" vs "treatment" vs "price" may
differ (an appointment may include multiple services). Directionally useful. The
spread ($78–$98) is real and meaningful.

**Recommendation:** Present as "indicative pricing range" with methodology notes.
Do not rank-order as though these are identical metrics.

### B. Customer Value Per Year
**Brands with data:** Mosquito Hunters, Mosquito Shield, Mosquito Squad

| Brand | Metric | Value |
|---|---|---|
| Mosquito Hunters | Avg customer value (mosquito-only, Region 2) | $726 |
| Mosquito Shield | Avg revenue per customer | $715 |
| Mosquito Squad | Avg gross revenue per customer | $705 |

**Assessment:** Remarkably similar ($705–$726). This suggests genuine market
convergence on per-customer economics in this service category. However, Hunters
reports by region (4 regions, $726–$1,232 range), while Shield and Squad report
system-wide averages. The comparison is valid for the overlapping range but should
not be forced to precision.

**Recommendation:** Note the convergence as a market insight. Present as evidence
that per-customer economics are relatively stable across brands, which makes
operator execution and customer acquisition costs the real differentiators.

### C. Customer Retention / Renewal
**Brands with data:** Mosquito Joe (77% retention), Mosquito Shield (85% returning),
Mosquito Squad (70% renewal)

**Assessment:** Definitions differ enough to prevent clean ranking. "Retention"
(Joe) vs "returning YoY" (Shield) vs "renewal rate" (Squad) likely measure slightly
different things. Shield's 85% is software-dependent (only 57% of customers had
data for the calculation).

**Recommendation:** Present as brand-specific signals, not a ranked comparison.
Note that all three report retention in the 70–85% range, suggesting the category
has naturally high recurring revenue characteristics.

---

## 3. Cross-Brand Comparisons That Are Misleading

### A. Average Revenue Per Franchise Unit
This is the comparison buyers most want, and the one most likely to mislead.

**Why it is misleading to compare directly:**
1. **Unit of analysis differs:** Authority reports per franchisee (avg 4 territories),
   Squad reports per territory, Joe splits by tenure, Shield reports per outlet,
   Hunters doesn't report it at all.
2. **Exclusion rates bias results:** Shield excludes 21%, Hunters 26%, Joe 7%, Squad 8%.
   Higher exclusion removes weaker performers, inflating averages.
3. **Tenure composition is uncontrolled:** A system with mostly 10+ year franchisees
   (Authority) will naturally show higher averages than one with many recent entrants
   (Shield, with +140 net units in 3 years).
4. **Multi-territory operators skew averages:** Authority's $464,600 is per franchisee
   who may own 2–35 territories. Squad's $484,506 is per territory.

**If forced to compare, this is the honest version:**
- Mosquito Squad: $484,506 per territory (207 territories, 8% excluded)
- Mosquito Joe: $432,954 per outlet, 6+ years tenure (296 outlets, 7% excluded)
- Mosquito Authority: $464,600 per franchisee, multi-territory (128 franchisees, 17% excluded)
- Mosquito Shield: $285,839 per outlet (81 outlets, **21% excluded**)
- Mosquito Hunters: **Not reported** (per-customer value only)

### B. Company-Owned Profitability as Franchisee Benchmark
Squad's company-owned operation ($20.8M, 14 territories, 25.9% margin) is an
excellent unit economics signal — but it does not pay royalties, and it operates at
a scale (14 territories, mature NE market) that is not representative of a new
single-territory franchisee. Authority's company-owned location shows negative net
income after amortization. Presenting either as "what you can expect" would be wrong.

### C. Mosquito Hunters' Item 19 as Revenue Evidence
Hunters provides per-treatment pricing and per-customer value but does NOT disclose
total revenue per franchise unit. Multiplying average customer count × average customer
value to estimate revenue would be a fabrication, not an extraction. Do not do this.

---

## 4. Proposed Minimal Normalized Layer for Phase 3

**Principle:** Only normalize where the underlying data genuinely measures the same
thing. Do not create false symmetry.

### Tier 1: Normalize (Defensible)

| Normalized Field | Source Brands | Method |
|---|---|---|
| `per_treatment_revenue` | Hunters, Joe, Squad | Direct extraction. Note terminology differences. |
| `per_customer_annual_value` | Hunters (by region), Shield, Squad | Direct extraction. Note scope differences. |
| `customer_retention_signal` | Joe, Shield, Squad | Qualitative band (70–85%). Do not rank-order. |
| `system_wide_gross_revenue` | Shield ($25.7M), Squad ($124.3M) | Direct extraction. Others don't report. |

### Tier 2: Normalize with Heavy Caveat (Proceed with Caution)

| Normalized Field | Source Brands | Method | Caveat |
|---|---|---|---|
| `avg_revenue_per_unit` | Authority, Joe, Shield, Squad | See "honest version" above | Must disclose unit definition, exclusion rate, tenure mix |
| `company_owned_ebitda_margin` | Authority, Shield, Squad | Extract margin % | Scale, comp adjustments, and royalty-free status differ |

### Tier 3: Do Not Normalize (Preserve as Brand-Specific)

| Data Element | Why |
|---|---|
| Mosquito Authority revenue bracket distributions | Unique format; no other brand provides this |
| Mosquito Authority length-of-ownership revenue correlation | Unique to Authority |
| Mosquito Hunters regional pricing tables | No other brand segments by region this way |
| Mosquito Hunters holiday lighting revenue | Unique revenue stream, no parallel |
| Mosquito Joe tenure-split gross sales | Unique split; others don't bifurcate by tenure |
| Mosquito Joe column-header copy errors | Document quality signal, not a data point |
| Mosquito Shield quartile breakdown | Others provide quartiles too, but exclusion rate makes Shield's non-comparable |
| Mosquito Squad close rate / per-appointment revenue | Only Squad provides these; no cross-brand comparison possible |
| Mosquito Squad 5-year systemwide sales trend | Only Squad provides multi-year system revenue |
| Mosquito Squad same-store growth | Only Squad provides this metric |

---

## 5. Implementation Notes for Phase 3

1. **Do not add a `normalized_metrics` object to the extraction JSON until the
   normalization layer is independently validated.** The schema already has a
   `normalized_metrics: null` placeholder — do not populate it prematurely.

2. **The normalized layer should be a separate file** (e.g.,
   `data/derived/cohort_normalized_metrics.json`), not embedded in brand-level
   extraction JSONs. This maintains the raw/derived/narrative separation.

3. **Every normalized metric must include:**
   - Which brands contribute data
   - What was excluded and why
   - What the original metric was called in each brand's FDD
   - A confidence flag (high/medium/low comparability)

4. **The site should present brand-specific Item 19 data on individual brand pages**
   and only present normalized cross-brand metrics on comparison pages. This avoids
   forcing every brand into the same template.

5. **Mosquito Hunters requires special handling.** It is the only brand without any
   form of total revenue per unit. On comparison pages, its Item 19 cell should
   read "Not disclosed — per-treatment pricing only" rather than being blank or
   showing a derived estimate.

---

## 6. Honest Assessment

The five brands in this cohort disclose Item 19 data in fundamentally different ways.
This is normal for franchise disclosure — the FTC does not mandate a standard format
for Item 19, only that representations be substantiated.

**The right answer for most Item 19 metrics is: "These are not directly comparable."**

What IS comparable:
- Per-treatment/appointment revenue (3 brands, directionally useful)
- Per-customer annual value (3 brands, surprisingly convergent around $700–$730)
- Customer retention (3 brands, all in 70–85% range)

What is NOT comparable and should not be forced:
- Total revenue per unit (different denominators, exclusion rates, tenure mixes)
- Profitability (only 2 full P&Ls, at wildly different scales)

The product's value is not in pretending these are comparable. The product's value is
in clearly explaining WHY they're not comparable and what that tells a buyer about
each franchisor's disclosure posture.
