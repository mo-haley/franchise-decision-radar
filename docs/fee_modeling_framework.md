# Fee Modeling Framework — Mosquito Pest Control Cohort

**Cohort:** Mosquito Authority, Mosquito Hunters, Mosquito Joe, Mosquito Shield, Mosquito Squad
**Source:** 2025 FDDs filed with Wisconsin DFI
**Date:** 2026-03-14

---

## Purpose

This document defines the methodology for computing annual ongoing fee burden at
standard gross revenue levels across all five brands. The goal is to answer a
buyer's core question: **"At $X in annual revenue, how much do I pay in mandatory
recurring fees to this franchisor?"**

---

## 1. Included Fee Components

Each brand's model includes only fees that are:
- **Mandatory** (not optional or recommended)
- **Recurring** (paid monthly, weekly, or annually as part of ongoing operations)
- **Clearly extracted** from the 2025 FDD with sufficient precision to model

### Components modeled per brand:

| Component | Authority | Hunters | Joe | Shield | Squad |
|---|---|---|---|---|---|
| Royalty | ✓ | ✓ | ✓ | ✓ | ✓ |
| Marketing / Ad Fund | ✓ | ✓ | ✓ | ✓ | ✓ |
| Technology Fee | ✓ | ✓ | ✓ | ✓ ¹ | ✓ |
| Website / Digital | ✓ | — | — | — | ✓ |
| Call Center | — | ✓ | ✓ ² | — | — |
| Software (vendor-paid) | — | — | — | — | ✓ |
| Bookkeeping (mandatory vendor) | — | — | — | ✓ ¹ | — |
| Sales Center | — | — | — | ✓ ¹ | — |
| Convention / Conference | — | ✓ | ✓ | — | ✓ |

¹ Shield's technology, bookkeeping, and sales center fees are ranges. Modeled at
low-end estimate (see Section 4).

² Joe's call center base fee only ($199.99/month). Per-closed-sale variable ($25)
excluded.

---

## 2. Excluded Fee Components

| Category | Reason for Exclusion |
|---|---|
| Initial franchise fee | One-time startup, not ongoing |
| Transfer fee | One-time, situational |
| Renewal / Successor fee | One-time, end-of-term |
| Convention travel / lodging | Variable, not a fee to franchisor |
| Late fees / penalty fees | Situational, avoidable |
| Liquidated damages | Termination event, not ongoing |
| Audit noncompliance fees | Situational, avoidable |
| Broker / referral fees | Situational |
| Additional training | Optional / as-needed |
| Insurance | Paid to third party, not a franchisor fee |
| Out-of-territory royalty surcharge (Hunters) | Modeled only for in-territory revenue |
| Key Accounts fee (Joe) | Variable, cannot model precisely |
| Local Marketing Group (Joe, 2% of GS) | "May be required" — conditional, excluded |

---

## 3. How Minimums, Thresholds, and Step-Ups Are Handled

### Royalty minimums
Several brands have minimum royalty schedules that override the percentage when
revenue is low:
- **Mosquito Authority:** Min $500/month at Year 5 ($6,000/year). At $200K+ gross
  revenue, 10% percentage ($20K+) always exceeds the minimum. Not material.
- **Mosquito Joe:** Min $500/week during Jun–Sep only (Year 5+). ~$8,500/year.
  For a seasonal pest control business doing $200K+, peak-season weekly revenue
  should exceed the weekly minimum. Not material at modeled levels.
- **Mosquito Squad:** Min $1,250/month at Year 5 ($15,000/year). At $200K+,
  percentage ($20K+) exceeds minimum. Not material at modeled levels.
  **Warning:** At Year 9+, Squad minimum is $3,000/month ($36,000/year). At
  $200K gross revenue, this EXCEEDS 10% ($20K) and would cost $36K. Noted
  in outputs but not used in the base model.
- **Mosquito Shield:** Minimum Gross Sales requirement is different — it's not a
  royalty minimum but a performance shortfall penalty. Modeled separately.

**Base model assumption:** Year 5 of operation. At all modeled revenue levels
($200K–$500K), percentage-based royalties exceed minimums for all brands except
Squad at $200K in Year 9+ (flagged but not used in base model).

### Tiered royalties
- **Mosquito Joe:** 10% on first $500,000 per territory per calendar year; 7% above.
  At modeled levels ($200K–$500K), all revenue falls in the 10% tier. The 7% tier
  does not activate until revenue exceeds $500K.
- **Mosquito Squad:** 10% on first $250K, 9% on $250K–$500K, 8% above $500K.
  Tiers are applied incrementally (marginal rate structure).

### Marketing floors and caps
- Where marketing obligation is "greater of $X or Y%," the model computes both
  and uses the higher value.
- **Mosquito Squad** local marketing is capped at $50,000/year. This cap is applied.
- **Mosquito Shield** local ad (10%) has no stated cap.
- Dollar-floor marketing obligations are the single largest source of fee burden
  divergence at low revenue levels.

### Technology fee tiers (Mosquito Authority)
Authority's technology fee is tiered by trailing 12-month gross revenue:
- $0–$50K → $100/month
- $50K–$150K → $200/month
- $150K–$250K → $300/month
- $250K–$350K → $400/month
- $350K–$450K → $500/month
- $450K–$550K → $600/month

The model applies the tier matching the modeled revenue level.

---

## 4. How Ambiguous/Conditional Fees Are Treated

### Mosquito Shield — Technology/Bookkeeping/Sales Center
Shield's technology-related fees are disclosed as ranges with mandatory vendor
requirements:
- Bookkeeping: $200–$500/month (mandatory approved vendor)
- Sales Center: $300–$750/month
- Software/Applications: vendor rates, variable

**Model approach:** Low-end estimate used ($200 bookkeeping + $300 sales center =
$500/month = $6,000/year). High-end ($500 + $750 + $250 = $1,500/month =
$18,000/year) noted in outputs. This range creates a $12,000/year uncertainty band
in Shield's model.

### Mosquito Shield — Minimum Gross Sales Shortfall
Shield imposes Minimum Gross Sales thresholds: $45K (Y1) escalating to $283,500
(Y5+). If actual Gross Sales fall below the minimum, franchisor **may** collect
the difference between actual royalty paid and 7% of the Minimum Gross Sales figure.

At $200K (Year 5): Shortfall = $283,500 − $200,000 = $83,500.
Penalty = (7% × $283,500) − (8% × $200,000) = $19,845 − $16,000 = $3,845.

**Model approach:** Shown as a separate line item, not included in the base total.
The penalty is discretionary ("may collect") and may not be enforced consistently.
But a conservative buyer should assume it will be enforced.

### Mosquito Joe — Ongoing Local Marketing Beyond Year 1
Joe's Item 7 lists a $35,000 "Local Performance Marketing Investment" for the first
12 months. There appears to be an ongoing "Minimum Local Marketing Spending"
obligation referenced in the LMG description, but the specific ongoing amount is
not clearly extracted from the FDD.

**Model approach:** The $35,000 first-year amount is excluded from the ongoing model.
The 2% LMG (conditional, "may be required") is also excluded. This means Joe's
ongoing model may understate true marketing burden if there is an ongoing local
marketing minimum beyond Year 1. Flagged as an open question.

### Mosquito Authority — National Marketing Fee
Authority reserves the right to implement a national marketing fee of up to 3% of
Gross Revenues. As of the 2025 FDD, this fee is **not implemented**.

**Model approach:** Excluded from the base model. Noted as a latent risk. If
implemented at 3%, it would add $6,000–$15,000/year at the modeled revenue levels,
materially changing Authority's position as the lowest-cost brand.

---

## 5. Standard Assumptions

| Assumption | Value | Rationale |
|---|---|---|
| Year of operation | Year 5 | Mid-life franchise; most minimums active, not maximum |
| Number of territories | 1 | Standard single-territory model |
| Number of employees | 1 owner + 1 technician | For per-user software fees |
| Revenue distribution | Even across year | Simplification; actual is highly seasonal |
| Revenue basis | Gross Sales / Gross Revenue | Treated as equivalent across brands ¹ |
| All mandatory fees enforced | Yes | Conservative assumption |
| Optional fees excluded | Yes | Unless clearly mandatory |

¹ Brands use slightly different terms: "Gross Sales" (Joe, Shield), "Gross Revenue"
(Squad), "Gross Revenues" (Authority), "Net Revenues" (Hunters). The differences
(primarily around tax and refund exclusions) are immaterial at the modeling level
but noted for completeness. Hunters' "Net Revenues" excludes taxes and refunds,
which could be 3–5% lower than Gross Sales, making Hunters' effective fee burden
slightly lower than modeled. Not adjusted.

---

## 6. What This Model Does NOT Capture

1. **Seasonality effects on minimum royalties** — Mosquito control revenue is
   heavily seasonal (70–80% in Apr–Sep). Weekly/monthly minimums may bite during
   off-season even if annual revenue exceeds thresholds.

2. **Multi-territory economics** — Many operators own 2–10+ territories. Volume
   discounts, shared marketing, and tier thresholds work differently at scale.

3. **Year 1 vs steady-state costs** — The model uses Year 5 assumptions. Year 1
   costs differ (lower minimums but higher startup marketing obligations).

4. **Variable call center costs** — Joe's $25/closed-sale and Squad's $2–3/minute
   (optional) are excluded because they scale unpredictably with business volume.

5. **Inflation/escalation clauses** — Most brands reserve the right to increase
   fees (Joe: 30%/year on tech and SEO, Squad: 10% on website fee). Not modeled.

6. **Insurance, rent, vehicle, labor** — These are business operating costs, not
   franchisor fees. Excluded by design. A full unit economics model would include
   these; this model intentionally isolates the franchisor fee layer.

---

## 7. Source Field References

All fee data sourced from `data/extracted/<brand>.json`, field paths:

| Component | JSON Path |
|---|---|
| Royalty | `raw.item_6_other_fees.royalty_rate` |
| Marketing | `raw.item_6_other_fees.advertising_and_marketing` (+ `.components[]`) |
| Technology | `raw.item_6_other_fees.technology_fee` |
| Transfer | `raw.item_6_other_fees.transfer_fee` |
| Other fees | `raw.item_6_other_fees.other_fees[]` |

The Python script (`scripts/fee_burden_model.py`) encodes the exact logic for each
brand with inline comments referencing these fields and FDD page numbers.
