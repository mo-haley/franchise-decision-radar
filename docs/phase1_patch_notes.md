# Phase 1 Patch Notes

**Date:** 2026-03-14
**Status:** Phase 1 schema/inventory/sample extraction revised for bulk extraction readiness.

## What Changed

### A. Extraction Schema (`docs/extraction_schema.json`)

1. **Split fee sections.** Replaced `raw.item_5_fees` (which mixed Item 5 and Item 6
   content) with `raw.item_5_initial_fees` (Item 5 only) and `raw.item_6_other_fees`
   (all Item 6 fees: royalty, advertising, technology, transfer, other).

2. **Added `source_document` block.** Top-level audit trail for the physical PDF:
   `download_origin`, `download_url`, `downloaded_at`, `local_filename`, `sha256`,
   `page_count`, `ocr_used`, `document_identity_notes`. Fields may be null if
   regulator-source PDF has not yet been downloaded.

3. **Added `field_status` enum.** Values: `extracted`, `not_found`, `ambiguous`,
   `not_applicable`, `deferred`. Applied to all fields that may be null or complex
   (ad/marketing funds, transfer fees, states registered, deferred items).

4. **Tightened `required` arrays.** Core structural fields are now required:
   `source_document`, all raw item sections, key provenance fields, field_status on
   nullable fields. Item 19 tables are intentionally not overconstrained.

5. **Consistent provenance policy.** Provenance required at each important extracted
   field. Parent-level provenance allowed for grouped sections (e.g., Item 7 line
   items sharing a page range) where all values share the same source.

6. **Item 19 restructured.** Replaced normalized `metrics` array with `tables` array
   that preserves the FDD's own table structure faithfully. Added `normalized_metrics`
   as an explicit null placeholder for future cross-brand normalization (deferred).

7. **Added deferred item placeholders.** `raw.item_12_territory`,
   `raw.item_17_contract_terms`, `raw.item_21_financial_statements_summary` reserved
   with `_status: "deferred"`. Not populated from inference.

8. **Advertising/marketing structure.** `item_6_other_fees.advertising_and_marketing`
   now has a `components` array for multi-part marketing obligations, plus
   `structure_description` for free-text explanation when a single rate is impossible.

9. **Added `spot_check` to metadata.** Extraction confidence of `high` now requires
   at least 3 values spot-checked against source PDF page references.

10. **Added `non_renewals` and `reacquired_by_franchisor` to Item 20.** These are
    separate columns in the FDD's Table 3 and were previously collapsed into `closed`.

11. **Schema version added.** `version: "2.0.0"` at top level.

### B. Source Inventory (`data/extracted/source_inventory.json`)

1. **Added cohort note.** Explains why these 5 brands were selected and that the
   cohort is intentionally limited to this market segment.

2. **Normalized source statuses.** Replaced inconsistent status values with a defined
   vocabulary: `confirmed_registered`, `manual_access_required`, `not_yet_searched`,
   `searched_not_found`, `access_blocked`, `third_party_only`. Vocabulary is
   documented in the inventory file itself.

3. **Added source trust tiers.** `regulator`, `public_filing_system`, `third_party`.
   Each known FDD URL now has `source_trust_tier` and `approved_for_extraction`.

4. **Removed speculative statements.** Removed or reframed:
   - "likely Delaware" → set `state_of_formation: null` with explanatory note
   - "SPV structure is a Neighborly corporate reorganization" → reframed as
     unverified observation
   - "net worth exemption may apply" → reframed as possibility, not assertion
   - CA DFPI statuses changed from "unverified" to "not_yet_searched" (more accurate)

5. **Structured entity aliases.** Each brand now has `entity_aliases` object with:
   `current_legal_entity`, `historical_entities`, `trade_names`,
   `known_filing_aliases`, `parent_company`.

6. **Added `approved_for_extraction` flag.** Third-party sources default to `false`.
   Regulator and public filing system sources default to `true`.

### C. Manual Download Steps (`docs/manual-download-steps.md`)

1. **Added provenance capture rules.** Mandatory recording of: source system, entity
   searched, filing year (from source page, not filename), state, download URL,
   local filename, SHA-256 hash.

2. **Added regulator-source preference rule.** Regulator-source first; third-party
   only as fallback, explicitly marked as lower-trust.

3. **Added filename-does-not-determine-truth rule.** Filing year/state/entity must
   come from filing detail page or FDD cover page.

4. **Fixed Mosquito Joe search guidance.** Added instruction to try both "Mosquito Joe
   SPV" and "Mosquito Joe Franchising" as search terms, plus historical variant.

5. **Added download log template.** CSV format for `data/raw/download_log.csv`.

6. **Corrected third-party URL labeling.** The FranchiseIndx/GCS URL for Mosquito
   Hunters is now labeled as `third_party`, not implied NASAA.

### D. Sample Extraction (`data/extracted/mosquito-hunters.json`)

1. **Added `source_document` block.** Documents download origin as `third_party`,
   includes SHA-256 hash, identity notes explaining provenance limitations.

2. **Restructured fees.** Split into `item_5_initial_fees` and `item_6_other_fees`
   per new schema. Added previously missing fees: Out-of-Territory Royalty (15%),
   Centrally Managed Media Boost Program ($5,000 optional), Broker Fee ($25,000).

3. **Applied `field_status` markers.** `ambiguous` on advertising/marketing (complex
   3-component structure), transfer fee (formula-based). `deferred` on states
   registered and future items.

4. **Restructured Item 19.** Replaced flat `metrics` array with `tables` array
   preserving FDD's own table labels (A.1 through A.7). Data is now structured
   per-table rather than flattened into generic metric objects.

5. **Added `non_renewals` and `reacquired_by_franchisor`** to Item 20 year records
   (both are 0 for all years in this FDD).

6. **Downgraded confidence to `medium`.** Was `high`. Downgraded because source PDF
   is third-party, not regulator-sourced. Added spot-check record.

7. **Corrected provenance page numbers.** Item 20 provenance now references all three
   relevant tables (pages 60, 62, 65) not just 60 and 65.

8. **Removed `source_state` and `source_year` from metadata.** These are redundant
   with the `source_document` and `filing_year` top-level fields. Source state is
   now in provenance objects only.

### E. Validation Rule

Added to schema and metadata: extraction confidence of `high` requires spot-check
of at least 3 values against source PDF page references. Spot-check record is
included in the `metadata.spot_check` object.

## What Did Not Change

- Extracted data values are unchanged (all numbers, text, provenance from the
  original extraction are preserved).
- Derived calculations are unchanged and still valid.
- Research documentation (`docs/wisconsin-dfi-research.md`,
  `docs/california-dfpi-research.md`) left as-is for reference.

## Unresolved Issues (Deferred to Phase 2+)

1. **Regulator-source PDFs not yet downloaded.** The sample extraction uses a
   third-party PDF. All 5 brands need regulator-source (WI DFI) downloads before
   Phase 2 extraction can be considered authoritative.

2. **CA DFPI not searched.** None of the 5 brands have been verified in the
   California DFPI system.

3. **Mosquito Authority entity mapping.** Which of the 3 "Main Line Brands LLC"
   registrations in WI DFI corresponds to the Mosquito Authority FDD must be
   confirmed from detail pages.

4. **Item 19 normalization.** No cross-brand normalization schema designed yet.
   Each brand's Item 19 structure is unique. Normalization should be designed
   after seeing at least 3 brands' Item 19 content.

5. **Items 12, 17, 21.** Reserved in schema but not extracted. Extraction
   priority TBD.

6. **Filing year history.** We have current registration status for all 5 brands
   in WI but do not know which historical filing years are downloadable.

## Phase 2 Extraction Requirements

Every Phase 2 brand extraction must satisfy all four before being labeled complete:

1. One saved source PDF in `data/raw/`
2. One recorded SHA-256 hash (in `source_document.sha256` and `download_log.csv`)
3. One row in `data/raw/download_log.csv`
4. One spot-check of at least 3 extracted values against source PDF page references
   (recorded in `metadata.spot_check`)
