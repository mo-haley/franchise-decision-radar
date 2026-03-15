# Manual FDD Download Steps

All state franchise databases require manual browser access (ASP.NET session tokens
or JS-rendered SPAs prevent programmatic download).

## Rules

1. **Regulator-source first.** Always use a regulator-source PDF (WI DFI, CA DFPI)
   when available. Third-party copies may be used only if no regulator source is
   accessible, and must be explicitly marked as lower-trust in the extraction.

2. **Provenance capture is mandatory.** For every manual download, record:
   - Source system (WI_DFI, CA_DFPI, NASAA_EFD, or third_party)
   - Entity name searched
   - Filing year (as stated on the filing/source page, NOT inferred from filename)
   - State of filing
   - Download URL (if visible/stable)
   - Local filename saved as
   - SHA-256 hash after save: `shasum -a 256 <filename>`

3. **Filename does not determine truth.** Filing year, state, and entity must come
   from the filing detail page or FDD cover page. Do not infer these from the
   filename or URL path.

4. **Validation rule.** After saving, open the PDF and confirm the cover page
   matches the expected brand, legal entity, and filing year before using it
   for extraction.

## Wisconsin DFI (Primary Source — All 5 Brands Confirmed Registered)

1. Open: https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx
2. Enter search term in "Name (Legal or Trade)" field (see table below)
3. Click Search
4. Click the matching result to open the Filing Details page
5. On the Filing Details page, confirm the legal entity name and filing year
6. Scroll to bottom and click the FDD document download link
7. Save to `data/raw/` using naming convention below
8. Run `shasum -a 256` on the saved file and record the hash

### Search Terms and Legal Entity Names

| Brand              | Search Term        | Expected Legal Entity                    | Notes                                    |
|--------------------|--------------------|------------------------------------------|------------------------------------------|
| Mosquito Joe       | `Mosquito Joe`     | Mosquito Joe SPV LLC                     | Also try `Mosquito Joe SPV`              |
| Mosquito Authority | `Main Line Brands` | Main Line Brands LLC                     | 3 registrations under this entity; check Filing Details to confirm Mosquito Authority FDD specifically |
| Mosquito Hunters   | `Mosquito Hunters` | Mosquito Hunters, LLC                    |                                          |
| Mosquito Squad     | `Mosquito Squad`   | Mosquito Squad Franchising SPE LLC       |                                          |
| Mosquito Shield    | `Mosquito Shield`  | Mosquito Shield Franchise Corporation    |                                          |

**Mosquito Joe note:** The WI filing is under the SPV entity ("Mosquito Joe SPV LLC"),
not the historical "Mosquito Joe Franchising, LLC". If searching by trade name does
not return results, try the legal entity name directly. Also try historical variant
"Mosquito Joe Franchising" in case the search indexes older filings.

**Mosquito Authority note:** This entity files under "Main Line Brands LLC" which
bears no resemblance to the brand name. The entity also covers Pest Authority and
Fitness Machine Technicians. You must check the Filing Details page to confirm you
are downloading the Mosquito Authority FDD.

## California DFPI (Secondary Source — Registration Not Yet Verified)

1. Open: https://dfpi.ca.gov/regulated-industries/franchises/
2. Click "Search Franchises"
3. Search using the legal entity name (NOT the brand name)
4. For each result, record registration status and filing years
5. Click portfolio number to access filed documents
6. Download the most recent FDD PDF
7. Record provenance per rules above

### Search Terms (Try All Variants)

| Brand              | Primary Search                         | Also Try                                           |
|--------------------|----------------------------------------|----------------------------------------------------|
| Mosquito Joe       | `Mosquito Joe SPV`                     | `Mosquito Joe Franchising`                         |
| Mosquito Authority | `Main Line Brands`                     | `TMAFS`, `TMA Franchise Systems`, `Authority Franchising` |
| Mosquito Hunters   | `Mosquito Hunters`                     | `MH Franchising`                                   |
| Mosquito Squad     | `Mosquito Squad Franchising SPE`       | `Mosquito Squad Franchising`                       |
| Mosquito Shield    | `Mosquito Shield Franchise Corporation`|                                                    |

**Note:** CA DFPI registration has not been verified for any of these brands.

## NASAA EFD (Alternative Public Filing Source)

1. Open: https://www.nasaaefd.org/Franchise/Search
2. Search by franchisor name
3. Download available FDD documents
4. Record provenance per rules above
5. Note: NASAA EFD is a public filing system, not a regulator portal. Trust
   tier is `public_filing_system`, not `regulator`.

### Known Download URLs (Access Not Re-verified)

These URLs were identified during Phase 1 research. Re-verify before relying on them:

- **Mosquito Hunters 2022 FDD (NASAA EFD):**
  https://www.nasaaefd.org/Franchise/Actions/DownloadFile.ashx?DocId=30056&isRegistered=true
- **Mosquito Hunters 2024 FDD (third-party — Google Cloud Storage / FranchiseIndx):**
  https://storage.googleapis.com/franchiseindx_fdds/Home-Services/Mosquito%20Hunters_2024_rb12ox58

## File Naming Convention

Save all downloaded FDDs to `data/raw/` using:

```
{brand-slug}_{filing_year}_{source}.pdf
```

Where `{source}` is: `wi` (WI DFI), `ca` (CA DFPI), `nasaa` (NASAA EFD), or
`3p` (third party).

Examples:
- `mosquito-joe_2025_wi.pdf`
- `mosquito-hunters_2024_3p.pdf`
- `mosquito-shield_2025_ca.pdf`

**Important:** The `{filing_year}` in the filename must match the filing year
confirmed from the source page or cover page, not assumed from context.

## Provenance Log Template

After each download, append a row to `data/raw/download_log.csv`:

```csv
brand_slug,filing_year,source,legal_entity_searched,download_url,local_filename,sha256,downloaded_at,notes
```

## Phase 2 Extraction Completion Checklist

No Phase 2 extraction should be labeled complete without all four:

1. One saved source PDF in `data/raw/`
2. One recorded SHA-256 hash (in `source_document.sha256` and `download_log.csv`)
3. One row in `data/raw/download_log.csv`
4. One spot-check of at least 3 extracted values against source PDF page references
   (recorded in `metadata.spot_check`)
