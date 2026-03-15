# Fee Burden Comparison — Mosquito Pest Control Franchise Cohort

**Source:** 2025 FDDs filed with Wisconsin DFI
**Methodology:** [fee_modeling_framework.md](fee_modeling_framework.md)
**Script:** [scripts/fee_burden_model.py](../scripts/fee_burden_model.py)
**Date:** 2026-03-14

---

## What This Shows

Estimated annual ongoing fees paid to the franchisor (or mandatory designated
vendors) at four common gross revenue levels. All figures assume Year 5 of
operation, single territory, one owner-operator plus one technician.

This is the comparison most prospective franchise buyers cannot easily make from
reading FDDs side-by-side, because fee structures differ so radically across brands.

---

## Summary Table — Annual Fee Burden by Revenue Level

### At $200,000 Gross Revenue

| Rank | Brand | Royalty | Marketing | Tech + Other | **TOTAL** | **% of Revenue** |
|---|---|---|---|---|---|---|
| 1 | **Mosquito Authority** | $20,000 | $10,000 | $6,600 | **$36,600** | **18.3%** |
| 2 | Mosquito Squad | $20,000 | $39,200 | $9,180 | **$68,380** | **34.2%** |
| 3 | Mosquito Hunters | $20,000 | $37,500 | $12,800 | **$70,300** | **35.1%** |
| 4 | Mosquito Joe | $20,000 | $44,900 | $7,852 | **$72,752** | **36.4%** |
| 5 | Mosquito Shield | $16,000 | $54,000 | $6,000 | **$76,000** | **38.0%** |

**Spread:** $39,400 (Authority pays roughly half what Shield pays)

### At $300,000 Gross Revenue

| Rank | Brand | Royalty | Marketing | Tech + Other | **TOTAL** | **% of Revenue** |
|---|---|---|---|---|---|---|
| 1 | **Mosquito Authority** | $30,000 | $15,000 | $7,800 | **$52,800** | **17.6%** |
| 2 | Mosquito Squad | $29,500 | $39,200 | $9,180 | **$77,880** | **26.0%** |
| 3 | Mosquito Hunters | $30,000 | $37,500 | $12,800 | **$80,300** | **26.8%** |
| 4 | Mosquito Joe | $30,000 | $46,900 | $7,852 | **$84,752** | **28.3%** |
| 5 | Mosquito Shield | $24,000 | $56,000 | $6,000 | **$86,000** | **28.7%** |

**Spread:** $33,200

### At $400,000 Gross Revenue

| Rank | Brand | Royalty | Marketing | Tech + Other | **TOTAL** | **% of Revenue** |
|---|---|---|---|---|---|---|
| 1 | **Mosquito Authority** | $40,000 | $20,000 | $9,000 | **$69,000** | **17.2%** |
| 2 | Mosquito Squad | $38,500 | $44,200 | $9,180 | **$91,880** | **23.0%** |
| 3 | Mosquito Hunters | $40,000 | $40,000 | $12,800 | **$92,800** | **23.2%** |
| 4 | Mosquito Shield | $32,000 | $58,000 | $6,000 | **$96,000** | **24.0%** |
| 5 | Mosquito Joe | $40,000 | $48,900 | $7,852 | **$96,752** | **24.2%** |

**Spread:** $27,752

### At $500,000 Gross Revenue

| Rank | Brand | Royalty | Marketing | Tech + Other | **TOTAL** | **% of Revenue** |
|---|---|---|---|---|---|---|
| 1 | **Mosquito Authority** | $50,000 | $25,000 | $10,200 | **$85,200** | **17.0%** |
| 2 | Mosquito Joe | $50,000 | $39,900 | $7,852 | **$97,752** | **19.6%** |
| 3 | Mosquito Shield | $40,000 | $60,000 | $6,000 | **$106,000** | **21.2%** |
| 4 | Mosquito Squad | $47,500 | $54,200 | $9,180 | **$110,880** | **22.2%** |
| 5 | Mosquito Hunters | $50,000 | $50,000 | $12,800 | **$112,800** | **22.6%** |

**Spread:** $27,600

---

## Key Findings

### 1. Mosquito Authority is the lowest-cost franchise at every revenue level

Authority's fee burden ranges from 17.0% to 18.3% of gross revenue — roughly half
the burden of the most expensive brand at $200K. This is driven by:
- No national marketing fund (reserved but not implemented)
- Local ad minimum of just $5,500 or 5% (vs $37,500–$50,000 for competitors)
- No mandatory call center fee

**Latent risk:** If Authority implements its reserved 3% national marketing fee,
annual burden would increase by $6,000–$15,000 across modeled levels, bringing it
to 20–21% of revenue. Still lowest, but the gap narrows significantly.

### 2. Marketing — not royalty — drives the fee spread

Royalty rates are similar across the cohort (8–10%). At $300K revenue, the royalty
spread is only $6,000 ($24K for Shield vs $30K for Authority/Hunters/Joe). But the
marketing spread is $41,000 ($15K for Authority vs $56K for Shield).

**Marketing is 2x–4x more variable than royalty across brands.** A buyer fixating
on royalty rate differences is looking at the wrong number.

### 3. Rank order changes at higher revenue levels

At $200K–$400K: Shield is most expensive, Joe is 4th–5th.
At $500K: Joe drops to 2nd cheapest thanks to the DMP discount ($37K→$26K at
$450K+ prior year revenue). Hunters becomes most expensive because its 10%
marketing obligation scales without a cap.

**Implication for buyers:** A brand that feels expensive at low revenue may become
relatively cheaper at scale, and vice versa. The fee structure's behavior at the
buyer's expected mature revenue level matters more than the headline rate.

### 4. Fixed-dollar marketing floors are regressive

Brands with high dollar-floor marketing obligations (Hunters $37,500, Joe $37,000
DMP, Shield $50,000 local ad) impose a disproportionate burden on lower-revenue
franchisees:

| Brand | Marketing at $200K | Marketing as % of $200K | Marketing at $500K | Marketing as % of $500K |
|---|---|---|---|---|
| Authority | $10,000 | 5.0% | $25,000 | 5.0% |
| Shield | $54,000 | 27.0% | $60,000 | 12.0% |
| Hunters | $37,500 | 18.8% | $50,000 | 10.0% |
| Joe | $44,900 | 22.5% | $39,900 | 8.0% |
| Squad | $39,200 | 19.6% | $54,200 | 10.8% |

Authority's marketing scales proportionally (5% flat). Everyone else has dollar
floors that hit harder at lower revenue.

### 5. Mosquito Squad has the only capped local marketing obligation

Squad's local marketing is capped at $50,000/year. This means a $1M franchisee
pays the same local marketing as a $500K franchisee. No other brand offers this
ceiling. This makes Squad increasingly favorable at very high revenue levels
(above $500K, where the model doesn't reach but the pattern is clear).

### 6. The fee spread narrows as revenue grows

| Revenue | Cheapest | Most Expensive | Spread | Spread as % of Revenue |
|---|---|---|---|---|
| $200K | $36,600 | $76,000 | $39,400 | 19.7% |
| $300K | $52,800 | $86,000 | $33,200 | 11.1% |
| $400K | $69,000 | $96,752 | $27,752 | 6.9% |
| $500K | $85,200 | $112,800 | $27,600 | 5.5% |

The dollar spread narrows because Authority's percentage-based fees scale while
competitors' dollar-floor fees plateau. But even at $500K, Authority costs $27,600
less per year than the most expensive brand — real money.

---

## Why Fee Burden Can Diverge Sharply from Franchise Fee / Startup Cost

A prospective buyer typically compares initial franchise fees ($25K–$107K range)
and total initial investment ($54K–$220K range). These are one-time costs.

But a franchise operates for 10+ years. Over a 10-year term at $300K/year revenue:

| Brand | 10-Year Cumulative Fee Burden | Initial Investment (midpoint) | Ongoing-to-Entry Ratio |
|---|---|---|---|
| Mosquito Authority | $528,000 | $90,850 | 5.8x |
| Mosquito Squad | $778,800 | $191,378 | 4.1x |
| Mosquito Hunters | $803,000 | $156,019 | 5.1x |
| Mosquito Joe | $847,520 | $171,115 | 5.0x |
| Mosquito Shield | $860,000 | $139,238 | 6.2x |

**Over a 10-year term, ongoing fees are 4x–6x the initial investment.** The
ongoing fee structure is a far more consequential financial decision than the
franchise fee. A buyer who shops on franchise fee alone is optimizing for ~15%
of total franchisor cost.

Mosquito Shield is a striking example: it has a mid-range initial investment
($139K midpoint) but the highest ongoing burden, giving it the worst
ongoing-to-entry ratio (6.2x). Its low royalty rate (8%) is offset by the $50K+
annual marketing floor.

---

## Important Caveats

### What this model includes and excludes
This model captures mandatory, recurring franchisor fees only. It does NOT include:
- Business operating costs (labor, chemicals, vehicle, insurance, rent)
- One-time fees (transfer, renewal, penalties)
- Variable fees (per-sale call center charges, per-complaint fees)
- Revenue to the franchisee (this is a cost model, not a profitability model)

### Mosquito Shield's range uncertainty
Shield's bookkeeping ($200–$500/mo) and sales center ($300–$750/mo) are modeled
at the low end ($6,000/year). High-end estimate adds $9,000/year, which would
push Shield's totals to $85,000 at $200K and $115,000 at $500K — widening its
lead as the most expensive brand at lower revenue levels.

### Mosquito Shield's Minimum Gross Sales penalty
At $200K gross revenue (Year 5), Shield may collect an additional $3,845 shortfall
penalty. This is discretionary and not included in the base model. If enforced,
Shield's effective burden at $200K rises to $79,845 (39.9% of revenue).

### Mosquito Authority's unimplemented national marketing fee
Authority reserves the right to implement a 3% national marketing fee at any time.
If implemented, Authority's burden at $300K would rise from $52,800 to $61,800
(20.6%) — still lowest in the cohort but materially higher.

### Mosquito Joe's potential ongoing local marketing obligation
Joe's $35K first-year Local Performance Marketing Investment is excluded as a
startup cost. If there is an ongoing local marketing minimum beyond Year 1 (the
FDD references a "Minimum Local Marketing Spending" but the amount is not clearly
extracted), Joe's burden would be higher than modeled. This is the biggest open
question in the model.

### Mosquito Squad's Year 9+ minimum royalty
At Year 9+, Squad's minimum royalty reaches $3,000/month ($36,000/year). At $200K
gross revenue, this exceeds the 10% percentage ($20,000), adding $16,000 to the
annual burden. At $300K+, the percentage exceeds the minimum. This is a long-term
risk for lower-revenue operators who stay in the system.

### Revenue basis differences
Hunters uses "Net Revenues" (excludes taxes and refunds), which is ~3–5% lower than
"Gross Sales." This means Hunters' actual fees are slightly lower than modeled. The
difference is immaterial for comparison purposes but noted for precision.

---

## Product-Facing Readiness Assessment

### Is this model ready for Phase 3 comparison pages?
**Yes, with mandatory caveats.** The model produces defensible, auditable outputs
at four revenue levels. The methodology is explicit, the assumptions are documented,
and the script is reproducible.

### Which outputs are safe for direct public comparison?

| Output | Safe for Public? | Notes |
|---|---|---|
| Total fee burden by revenue level | ✅ Yes, with caveats | Label as "estimated" and note Year 5 assumptions |
| Rank order by revenue level | ✅ Yes, with caveats | Note that rank changes at $500K |
| Component breakdown (royalty / marketing / tech) | ✅ Yes | Most useful for buyer understanding |
| Fee burden as % of revenue | ✅ Yes | Clearest comparative metric |
| 10-year cumulative burden | ⚠️ With heavy caveat | Assumes constant revenue; real trajectory varies |
| "Authority is cheapest" | ✅ Yes | True at every modeled level |
| "Shield is most expensive at low revenue" | ✅ Yes, with caveat | Note the bookkeeping/sales center range |
| Shield shortfall penalty | ⚠️ Signal only | Discretionary; present as risk, not certainty |
| Authority national fee risk | ⚠️ Signal only | Not implemented; present as latent risk |

### Which require caveat labels?
All public-facing outputs should include:
1. "Estimated annual fee burden based on 2025 FDD data"
2. "Year 5 of operation, single territory"
3. "Includes mandatory recurring fees to franchisor; excludes business operating costs"
4. "Fee structures differ significantly — see component detail for each brand"
5. A note that actual fees may vary based on operator year, territory, and franchisor
   discretion

### Recommended presentation format for Phase 3 pages
1. **Lead with the comparison table** at a revenue level most relevant to the buyer
   (suggest $300K as the default view — it's close to cohort median revenue and avoids
   both the very-low and very-high distortions)
2. **Allow revenue-level toggle** ($200K / $300K / $400K / $500K) so buyers can model
   at their expected level
3. **Show component breakdown** for each brand — this is where the real insight lives
4. **Highlight the marketing finding** — "Marketing burden, not royalty rate, is the
   primary driver of fee differences across these brands"
5. **Show the rank-order shift** at $500K to illustrate that the cheapest-at-low-revenue
   brand may not be cheapest at scale
