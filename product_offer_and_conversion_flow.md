# Franchise Decision Radar — Product & Conversion Strategy Memo

**Date:** 2026-03-14
**Status:** Internal strategy document — not for publication
**Scope:** Mosquito pest control wedge only

---

## The core insight this product sits on

Someone considering a mosquito franchise is about to spend $100K–$170K and lock themselves into a 10-year contract. The FDD contains the information they need to make that decision, but it's a 250-page legal document designed for compliance, not for comparison. Most buyers either don't read it, read it without context, or pay a franchise attorney $3K–$5K to summarize one brand without cross-brand comparison.

Franchise Decision Radar sits in that gap: structured, regulator-sourced comparison data that a prospective buyer can't easily build themselves.

---

## 1. What the actual product is

**Free layer:** Cross-brand comparison pages that establish trust, demonstrate data quality, and make the visitor realize they're missing information they need.

**Paid layer:** A single-brand decision report that gives a prospective buyer everything they need to walk into a discovery day (or walk away) with confidence.

The free layer answers: "How do these franchises compare?"
The paid layer answers: "Should I buy this specific franchise, and what should I watch out for?"

These are different questions. The first is browsable. The second is personal and worth paying for.

---

## 2. What the paid offer should be (first)

**A one-time, single-brand Franchise Decision Report.**

Not a subscription. Not a comparison unlock. Not a category report. One brand, one report, one purchase.

Why this and not the alternatives:

| Option | Problem |
|--------|---------|
| Premium comparison page unlock | The comparison pages are your top-of-funnel trust builder. Gating them kills distribution. |
| Category-level report (all 5 brands) | Overbuilt for the buyer who's already narrowed to 1–2 brands. Underbuilt for the tire-kicker who isn't ready to pay. |
| Subscription | Nobody needs ongoing franchise comparison data. This is a one-time life decision. |
| Per-brand comparison unlock | Too thin. The comparison data alone isn't worth paying for — the synthesis and risk analysis is. |

The single-brand report works because:

- It matches the buyer's actual decision unit ("Should I buy Mosquito Joe?")
- It can be priced meaningfully ($49–$149 range) without needing to justify recurring value
- It's buildable now from existing extracted data plus a templated analysis layer
- It converts naturally from the free comparison pages ("You've seen how they compare — here's the deep dive on the one you're considering")

### What goes in the report

This is the critical product design question. The report must contain things the buyer cannot get from the free comparison pages or from reading the FDD themselves:

- **Fee burden modeling:** Total ongoing cost as a percentage of revenue at different revenue levels (not just the rate — the actual dollar math including minimums, technology fees, marketing fund components)
- **System health narrative:** Unit growth trend, turnover rate in context ("Is 15% turnover normal for this category or a red flag?"), what the closures and transfers suggest
- **Investment structure breakdown:** Where the initial investment actually goes, what's negotiable vs. fixed, what the FDD buries in footnotes
- **Item 19 translation:** What the financial performance data actually tells you about likely revenue (and what it conspicuously omits)
- **Risk flags:** Litigation summary, entity changes, ownership changes, anything that a franchise attorney would flag
- **Questions to ask on discovery day:** Specific, data-informed questions derived from the FDD analysis (e.g., "The FDD shows 11 terminations in 2023 — ask what drove that")
- **How this brand compares:** A brief positioning summary against the category (pulled from the free comparison data, but contextualized for this brand)

The report should feel like getting a smart franchise attorney's memo for $99 instead of $4,000 — except it's faster, data-driven, and includes cross-brand context the attorney wouldn't have.

---

## 3. User journeys

### Journey A: Category-first searcher
**Query:** "best mosquito franchise" / "mosquito franchise comparison"
**Lands on:** Comparison hub or one of the three comparison pages (Fee Burden, System Health, Cost to Enter)
**Understands quickly:** These five brands are the real options, and they differ meaningfully on cost, fees, and system health
**Key moment:** Sees a brand that interests them, or sees a red flag on one they were considering
**Next action:** Clicks through to that brand's page (currently doesn't exist — this is the gap)
**Conversion path:** Brand page → report CTA

### Journey B: Brand-first buyer
**Query:** "Mosquito Joe franchise cost" / "Mosquito Hunters FDD"
**Lands on:** Brand page (needs to exist) or gets pulled in via a comparison page that ranks for the query
**Understands quickly:** Here's the real cost structure, here's how it compares to alternatives
**Key moment:** Realizes the comparison context changes their understanding of the brand
**Next action:** Either explores comparisons (enters Journey A) or goes straight to report purchase
**Conversion path:** Brand page → report CTA

### Journey C: Comparison shopper (2–3 brands in mind)
**Query:** "Mosquito Joe vs Mosquito Squad" / "mosquito franchise fees comparison"
**Lands on:** Comparison page (Fee Burden or Cost to Enter most likely)
**Understands quickly:** Side-by-side differences on the dimension they care about
**Key moment:** Narrows from 3 to 1–2 serious contenders
**Next action:** Wants the deeper analysis on their top pick
**Conversion path:** Comparison page → brand page → report CTA

### Journey D: Serious buyer ready to pay
**Query:** "Mosquito Joe franchise review" / "should I buy a Mosquito Hunters franchise"
**Lands on:** Brand page (ideally) or comparison page
**Understands quickly:** This site has real data, not affiliate fluff
**Key moment:** Sees the report offer and recognizes it answers their actual question
**Next action:** Purchases report
**Conversion path:** Brand page → report CTA → purchase

**The common thread:** Every journey converges on the brand page. That's the missing piece in the current site.

---

## 4. Site structure needed next

### Current state (what exists)
- Comparison: Fee Burden page
- Comparison: System Health page
- Comparison: Cost to Enter page

### What's needed (in priority order)

**Priority 1 — Brand pages (5 pages)**
One page per brand. This is the conversion surface. Structure:

- Brand header (name, parent company, system age, size)
- Key metrics summary (initial investment range, royalty rate, total fee burden, net unit growth)
- "How [brand] compares" — brief positioning vs. category with links to comparison pages
- Risk and complexity flags (from FDD extraction warnings and ambiguity flags)
- CTA: "Get the full [brand] Decision Report"
- Report preview (table of contents or sample section — enough to show depth without giving it away)

**Priority 2 — Report purchase flow (1 page/modal)**
Simple purchase page or modal. Brand-specific. Shows:

- What's in the report (section list)
- Sample excerpt or preview
- Price
- Payment (Stripe checkout or equivalent)
- Delivery (instant PDF download or email)

**Priority 3 — Methodology page (1 page)**
Short, trust-building page explaining:

- Data comes from regulator-filed FDDs (not franchise sales materials)
- Which state filings are used and why
- What "regulator-source" means vs. third-party
- How extraction works (structured extraction with provenance, not summarization)
- What's not included and why

This page exists for the skeptical buyer who needs to trust the data before paying. It also helps with SEO for "franchise disclosure document" queries.

**Priority 4 — Comparison hub (1 page)**
A landing page that links to all three comparison dimensions and provides a category overview. Useful for the Journey A searcher who doesn't land on a specific comparison page.

**Not needed yet:**
- Blog / content marketing pages (premature before the conversion flow works)
- Multi-category pages (out of scope for this wedge)
- User accounts / dashboard (the product is a report, not a platform)

---

## 5. What should be free vs. paid

### Free (public, indexable, shareable)

- All three comparison pages (Fee Burden, System Health, Cost to Enter) — these are top-of-funnel
- Brand pages with key metrics summary — enough to be useful, not enough to replace the report
- Methodology page
- Comparison hub

**Why these stay free:** They're your distribution engine. Every comparison page is a potential search result. Every brand page captures brand-name search traffic. Gating any of this kills the funnel before it starts.

### Paid (behind purchase)

- The single-brand Franchise Decision Report
- Specifically, the report contains:
  - Fee burden modeling at multiple revenue levels (the free page shows the rate; the report shows the dollar math)
  - System health narrative with context (the free page shows the trend; the report explains what it means)
  - Full Item 19 translation (the free page says whether Item 19 is disclosed; the report breaks down what it reveals)
  - Investment breakdown with footnote analysis
  - Risk flags and litigation summary
  - Discovery day questions
  - Cross-brand positioning narrative

**The line:** Free pages show *what*. The paid report explains *so what* and *what to do about it*.

---

## 6. Main CTA

**"Get the [Brand Name] Decision Report"**

One CTA. Appears on:
- Every brand page (primary placement)
- Bottom of every comparison page (secondary, contextualized: "Ready to go deeper on one brand?")
- Not on the methodology page (wrong intent)

Why this CTA and not others:
- "Decision Report" signals that this is a tool for making a decision, not just more information
- Brand-specific naming makes it feel tailored, not generic
- It's concrete enough to click on and understand what you're buying

Avoid: "Unlock premium data" (sounds like a paywall, not a product), "Subscribe" (wrong model), "Get full access" (access to what?).

---

## 7. Pricing structure

**Flat fee per report. Single tier.**

No bundles, no tiers, no category package — yet. Reasons:

- The decision unit is one brand. Price for that unit.
- Tiering requires enough volume to test. You don't have it yet.
- Bundles ("all 5 brands for $X") sound logical but don't match buyer behavior. Nobody is equally serious about all five.
- A single clear price eliminates decision friction.

**Price range to test:** $79–$149. This is anchored against the alternatives:
- Free comparison pages: $0 (but incomplete)
- Franchise attorney FDD review: $3,000–$5,000 (thorough but single-brand, no comparison context)
- Franchise broker "consultation": free but conflicted (they earn commissions from the franchisor)

The report sits in the "serious but accessible" range. Under $100 is an impulse buy for someone about to invest $150K. Over $150 starts to need more social proof than a new product has.

Start at $99. Adjust based on conversion data, not theory.

**Future optionality (not now):**
- Two-brand comparison bundle at a discount (after you see if people buy one and come back for a second)
- Category report with all five brands (after enough single-brand sales validate demand)

---

## 8. Biggest product mistakes from here

**Mistake 1: Building more free comparison pages before the paid report exists.**
Every additional free page without a conversion path is content marketing with no business model. The three comparison pages are enough free content. Build the report next.

**Mistake 2: Treating this as a dashboard instead of a decision product.**
The temptation is to build interactive filters, custom comparisons, saved searches — platform features. The buyer doesn't want a platform. They want an answer. The report is the answer.

**Mistake 3: Gating comparison data behind payment.**
The comparison pages are how people find you. If you gate them, you're invisible. The free layer is distribution. The paid layer is the product. Don't confuse them.

**Mistake 4: Launching with multiple pricing tiers.**
"Basic report $49 / Full report $99 / Premium report $149" creates decision paralysis and signals that the cheaper versions are incomplete. One product, one price. You can tier later with data.

**Mistake 5: Expanding to other franchise categories before the mosquito wedge converts.**
The wedge is narrow on purpose. If 5 brands and one category can't convert, 50 brands and 10 categories won't either. Prove the model here first.

**Mistake 6: Over-investing in report design before validating demand.**
The first version of the report can be a well-structured PDF generated from your extraction data plus a templated analysis layer. It doesn't need to be beautiful. It needs to be accurate, useful, and worth $99. Design polish comes after you know people will buy it.

**Mistake 7: Adding user accounts.**
No login, no dashboard, no saved reports. Stripe checkout → instant PDF delivery. Accounts add friction and imply ongoing engagement that doesn't match the product (a one-time decision tool).

---

## Summary

**Recommended product model in one sentence:**
Franchise Decision Radar is a free cross-brand comparison site that converts to paid single-brand decision reports ($99) for prospective franchise buyers.

**Recommended free-to-paid funnel in one sentence:**
Search-discovered comparison pages → brand-specific pages with key metrics → single-brand Decision Report purchase via one-click checkout.

**Next 3 concrete steps:**

1. **Build the 5 brand pages.** These are the missing conversion surface. Each brand page pulls from the extracted FDD data and links to the report purchase. Without brand pages, there's no natural place for the CTA.

2. **Define the report template and generate the first report.** Pick Mosquito Hunters (you have the deepest extraction). Write the templated analysis sections. Produce a PDF. This is your v1 product. It doesn't need to be automated yet — it needs to exist.

3. **Wire up the purchase flow.** Stripe checkout on the brand page. Instant PDF delivery via email or download link. No accounts. Test with the Mosquito Hunters report first, then generate the other four.

Everything else — methodology page, comparison hub, SEO optimization, design polish, pricing experiments — comes after these three steps are done and real buyers can pay real money.
