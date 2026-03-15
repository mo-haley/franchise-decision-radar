# Wisconsin DFI Franchise Filing Database Research

Date: 2026-03-14

## Database Access

**Search Portal URL:** https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx

**Active Registrations List:** https://apps.dfi.wi.gov/apps/franchiseefiling/activeFilings.aspx
(Lists all 1,813+ currently registered franchises with legal names and expiration dates)

**Search Method:**
- Single search field: "Name (Legal or Trade)"
- No CAPTCHA
- ASP.NET WebForms application (server-side rendered, not a REST API)
- Search results link to detail pages; FDD PDFs are downloadable from the bottom of each detail page

**Access Issues:**
- No CAPTCHA or login required for search
- The search form is ASP.NET WebForms with `__VIEWSTATE` / `__EVENTVALIDATION` tokens, making programmatic POST requests fragile (tokens change per session)
- Detail page URLs follow this pattern: `https://apps.dfi.wi.gov/apps/FranchiseSearch/details.aspx?id=<ID>&hash=<HASH>&search=external&type=GENERAL`
- Detail page IDs/hashes are not predictable; they must be obtained from search results
- **Recommended approach: manual browser search, then download FDD PDFs from detail pages**
- The detail pages are NOT indexed by Google

**FDD PDF Availability:**
- Wisconsin is a franchise registration state; filed FDDs are public record
- FDD PDFs can be downloaded from the "Filing Details" page for each franchise
- Each filing detail page includes a summary of the franchisor's filings and a download link for the FDD at the bottom of the page

---

## Brand Research Results

### 1. Mosquito Joe

| Field | Value |
|---|---|
| **WI Registered Legal Entity** | Mosquito Joe SPV LLC |
| **WI Registration Status** | Active (expires 4/4/2026) |
| **Entity Type** | Special Purpose Vehicle LLC |
| **Parent/Affiliate** | Dwyer Franchising LLC d/b/a Neighborly |
| **Historical Entity** | Mosquito Joe Franchising, LLC (Virginia LLC, formed 2012-08-06) |
| **Principal Address** | 2829 Guardian Lane, Suite 100, Virginia Beach, VA 23452 |
| **State of Formation** | Virginia (original); SPV entity likely Delaware |
| **Notes** | The WI filing is under the SPV entity, NOT the original "Mosquito Joe Franchising, LLC". The SPV structure is a Neighborly corporate reorganization. When searching WI DFI, search for "Mosquito Joe" (the trade name search should match). |

**AMBIGUITY FLAG:** The legal entity name in Wisconsin ("Mosquito Joe SPV LLC") differs from the historical franchisor entity ("Mosquito Joe Franchising, LLC") referenced in older FDDs and third-party sources. The SPV appears to be the current franchising entity as of the 2025 FDD cycle.

---

### 2. Mosquito Authority

| Field | Value |
|---|---|
| **WI Registered Legal Entity** | Main Line Brands LLC |
| **WI Registration Status** | Active (expires 5/8/2026) — appears 3 times (likely covers multiple brands under the same parent) |
| **Entity Type** | Delaware LLC |
| **Parent/Affiliate** | Main Line Brands LLC is the parent entity |
| **Historical Entities** | TMAFS, LLC (NC LLC, formed 2016); TMA Franchise Systems, Inc. (NC corp, incorporated 2011-12-02); Authority Franchising, LLC (original name before rename to Main Line Brands, formed 2020-09-10) |
| **Principal Address** | 2359 Perimeter Pointe Parkway, Suite 250, Charlotte, NC 28208 |
| **State of Formation** | Delaware |
| **Notes** | Main Line Brands LLC files for multiple brands (Mosquito Authority, Pest Authority, Fitness Machine Technicians). When searching WI DFI, search for "Main Line Brands" to find the filing. Searching for "Mosquito Authority" as a trade name may also work. |

**AMBIGUITY FLAG:** The WI registration is under "Main Line Brands LLC" — the parent/franchisor entity — not under the consumer brand name "Mosquito Authority". The three separate listings on the active registrations page likely correspond to different brands under the same entity. It is unclear which specific registration maps to the Mosquito Authority FDD vs. other Main Line Brands franchises. The detail pages should clarify this.

---

### 3. Mosquito Hunters

| Field | Value |
|---|---|
| **WI Registered Legal Entity** | Mosquito Hunters, LLC |
| **WI Registration Status** | Active (expires 5/8/2026) |
| **Entity Type** | Delaware LLC |
| **Parent/Affiliate** | LD Parent, Inc. (direct parent); CNL Strategic Capital, LLC (indirect parent); Happinest Brands (operating brand) |
| **Historical Entity** | MH Franchising, LLC (predecessor, acquired May 2018) |
| **Principal Address** | 142 State Route 34, Holmdel, NJ 07733 |
| **State of Formation** | Delaware |
| **Affiliated Franchise** | Lawn Doctor, Inc. (same address, same parent) |
| **Notes** | Entity name matches consumer brand name. Straightforward search on WI DFI. |

**No ambiguity.** Legal entity name aligns with the brand name.

---

### 4. Mosquito Squad

| Field | Value |
|---|---|
| **WI Registered Legal Entity** | Mosquito Squad Franchising SPE LLC |
| **WI Registration Status** | Active (expires 4/17/2026) |
| **Entity Type** | Delaware LLC (SPE = Special Purpose Entity) |
| **Parent/Affiliate** | AB Assetco LLC (direct parent); Authority Brands, Inc. (indirect parent) |
| **Historical Entity** | Mosquito Squad Franchising Corporation (Delaware corp, formed 2009-01-19); converted to Mosquito Squad Franchising, LLC on 2018-12-07 |
| **Principal Address** | Richmond, Virginia |
| **State of Formation** | Delaware |
| **Notes** | The WI filing uses the SPE entity name, not the plain "Mosquito Squad Franchising, LLC." When searching WI DFI, search for "Mosquito Squad" as a trade name. |

**AMBIGUITY FLAG:** Similar to Mosquito Joe, the WI filing is under an SPE (Special Purpose Entity) name, which differs from the historical "Mosquito Squad Franchising, LLC" referenced in older FDD sources. The SPE entity is the current franchising entity.

---

### 5. Mosquito Shield

| Field | Value |
|---|---|
| **WI Registered Legal Entity** | Mosquito Shield Franchise Corporation |
| **WI Registration Status** | Active (expires 5/13/2026) |
| **Entity Type** | Delaware Corporation |
| **Parent/Affiliate** | Five Star Franchising (acquired March 2022) |
| **Principal Address** | 500 E. Washington Street #24, North Attleboro, MA 02760 |
| **State of Formation** | Delaware (incorporated November 2012) |
| **Business Since** | 2001 (franchising since 2013) |
| **Notes** | Entity name closely matches brand name. Straightforward search on WI DFI. |

**No ambiguity.** Legal entity name clearly maps to the brand.

---

## Summary Table

| Brand | WI Legal Entity | WI Status | Expires | Entity Matches Brand? |
|---|---|---|---|---|
| Mosquito Joe | Mosquito Joe SPV LLC | Active | 4/4/2026 | No (SPV entity) |
| Mosquito Authority | Main Line Brands LLC | Active | 5/8/2026 | No (parent entity) |
| Mosquito Hunters | Mosquito Hunters, LLC | Active | 5/8/2026 | Yes |
| Mosquito Squad | Mosquito Squad Franchising SPE LLC | Active | 4/17/2026 | No (SPE entity) |
| Mosquito Shield | Mosquito Shield Franchise Corporation | Active | 5/13/2026 | Yes |

**All 5 brands are actively registered in Wisconsin as of 2026-03-14.**

---

## Manual Download Procedure

Since programmatic access to the WI DFI franchise search is impractical (ASP.NET WebForms with session tokens), use this manual procedure:

1. Open browser to: https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx
2. In the "Name (Legal or Trade)" field, enter the search term (see table below)
3. Click Search
4. Click on the matching result to open the Filing Details page
5. Scroll to the bottom of the Filing Details page
6. Click the FDD document download link

**Recommended search terms:**

| Brand | Search Term |
|---|---|
| Mosquito Joe | `Mosquito Joe` |
| Mosquito Authority | `Main Line Brands` |
| Mosquito Hunters | `Mosquito Hunters` |
| Mosquito Squad | `Mosquito Squad` |
| Mosquito Shield | `Mosquito Shield` |

**Downloaded files should be saved to:** `data/raw/` (per project convention)

**Naming convention (suggested):** `{brand_slug}_{filing_year}_wi.pdf`
- `mosquito-joe_2025_wi.pdf`
- `mosquito-authority_2025_wi.pdf`
- `mosquito-hunters_2025_wi.pdf`
- `mosquito-squad_2025_wi.pdf`
- `mosquito-shield_2025_wi.pdf`

---

## Alternative FDD Sources

- **NASAA Electronic Filing Depository:** https://www.nasaaefd.org/Franchise/Search
  - Some FDDs may be publicly downloadable here
  - Mosquito Hunters 2022 FDD confirmed available: https://www.nasaaefd.org/Franchise/Actions/DownloadFile.ashx?DocId=30056&isRegistered=true
  - Mosquito Hunters 2024 FDD found at: https://storage.googleapis.com/franchiseindx_fdds/Home-Services/Mosquito%20Hunters_2024_rb12ox58

- **FDD Exchange:** https://fddexchange.com/ (may require registration/payment for full documents)

- **Wisconsin DFI remains the primary free source** for current FDDs filed with the state.

---

## Open Questions

1. Which of the 3 "Main Line Brands LLC" registrations on the WI active list corresponds specifically to the Mosquito Authority FDD? (Resolve by checking detail pages in the search portal.)
2. What filing years are available for each brand? (The active registrations page only shows current expiration dates, not historical filings. The search portal detail pages may show multiple filing years.)
3. Has the Mosquito Joe entity transitioned fully from "Mosquito Joe Franchising, LLC" to "Mosquito Joe SPV LLC" across all states, or is this Wisconsin-specific?
