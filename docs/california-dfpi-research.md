# California DFPI Franchise Filing Database Research

**Date:** 2026-03-14
**Researcher:** Automated web research
**Status:** Partial — manual verification required (see Access Issues below)

---

## Database Access

### Primary Search Interface

**URL:** https://dfpi.ca.gov/search/ (then filter by Franchises industry)

The DFPI's franchise filing search is available through a "Unified Search" on the
main DFPI website. The search is JavaScript-rendered, meaning it cannot be accessed
programmatically via simple HTTP requests.

**Full search URL pattern:**
```
https://dfpi.ca.gov/search-results/?searchStudioQuery=<LEGAL_NAME>&isGrid=false&facets=fq%3Dss_industry_s%3A%22Franchises%22%26fq%3Dss_content_type_s%3A%22Regulated%2520Entity%22&orderBy=&start=0
```

### Legacy Search (RETIRED)

**URL:** https://docqnet.dfpi.ca.gov/search/

This was the old DocQNet search interface. It has been **retired and is no longer
being updated**. Users are redirected to the Unified Search above.

### FRANSES (Filing Portal — NOT Public Search)

**URL:** https://franses.dfpi.ca.gov

This is the Franchise and Securities Electronic Submissions portal. It is a
ServiceNow-based filing system for franchisors to submit applications — it is
**not a public search tool**.

### NASAA Electronic Filing Depository (Alternative Source)

**URL:** https://www.nasaaefd.org/Franchise/Search

The NASAA EFD provides free public access to franchise filings across multiple
states. This is a viable alternative source for FDD documents. The interface is
also JavaScript-rendered.

---

## Access Issues (ALL DATABASES)

1. **JavaScript-rendered search:** Both the DFPI Unified Search and the NASAA EFD
   search interfaces are JavaScript-rendered single-page applications. They cannot
   be queried via simple HTTP GET requests or basic web scraping. A headless browser
   (e.g., Playwright, Selenium) would be required for programmatic access.

2. **No CAPTCHA observed** on any of the search interfaces.

3. **Legal name required:** The DFPI search requires the franchisor's exact legal
   entity name, not the consumer brand name. This is critical — searching for
   "Mosquito Joe" will not work; you must search for "Mosquito Joe Franchising, LLC."

4. **California net worth exemption:** Franchisors with a net worth exceeding $5 million
   may be exempt from full registration, and their FDD may not appear in the database.
   Several of these brands are subsidiaries of large parent companies (Neighborly,
   Authority Brands, Five Star Franchising) which may qualify for this exemption.

5. **Slow updates:** Multiple sources note that California's search engine is "slow to
   update" but that all documents (FDDs, blacklines, applications, comment letters,
   approvals) are eventually available.

---

## Brand Research Results

### 1. Mosquito Joe

| Field | Value |
|---|---|
| **Legal Entity Name** | Mosquito Joe Franchising, LLC |
| **Entity Type** | Virginia Limited Liability Company |
| **Organized** | August 6, 2012 |
| **Parent Company** | Neighborly (formerly Dwyer Group) |
| **Ownership History** | Founded by Buzz Franchise Brands → Sold to Dwyer Group/Neighborly in 2018 |
| **Principal Address** | (Per Neighborly corporate structure) |
| **Franchising Since** | 2012 |
| **System Size** | 415 franchised locations, 2 corporate (as of Dec 31, 2024) |
| **FDD Years Found Online** | 2013 (FDD Exchange), 2020 (FranChimp), 2024 (FranChimp), 2025 (various references) |
| **California Registration** | LIKELY — Mosquito Joe accepts franchise inquiries from California and has CA locations |
| **CA DFPI Verified** | NOT YET — requires manual search on DFPI Unified Search |
| **Search Name for DFPI** | "Mosquito Joe Franchising" |

**Ambiguity:** None. Legal entity name is well-documented.

### 2. Mosquito Squad

| Field | Value |
|---|---|
| **Legal Entity Name** | Mosquito Squad Franchising SPE LLC |
| **Prior Entity Name** | Mosquito Squad Franchising, LLC (before May 2021); Mosquito Squad Franchising Corporation (before Dec 2018) |
| **Entity Type** | Delaware Limited Liability Company |
| **Organized** | March 24, 2021 (SPE LLC); predecessor incorporated Jan 19, 2009 |
| **Parent Company** | Authority Brands, Inc. (indirect); AB Assetco LLC (direct) |
| **Principal Address** | 7120 Samuel Morse Drive, Suite 300, Columbia, MD 21046 |
| **Franchising Since** | February 2009 |
| **FDD Years Found Online** | 2012 (FDD Exchange), 2013 (FDD Exchange), 2019 (FDD Exchange), 2020 (FranChimp), 2025 (FDD Exchange) |
| **California Registration** | LIKELY — CA is listed as a franchise registration state in their FDD |
| **CA DFPI Verified** | NOT YET — requires manual search on DFPI Unified Search |
| **Search Name for DFPI** | "Mosquito Squad Franchising SPE" (current) or "Mosquito Squad Franchising" (historical) |

**Ambiguity:** The legal entity changed names multiple times. The DFPI filing may
be under any of the three entity names depending on the year. Search for all three.

### 3. Mosquito Authority

| Field | Value |
|---|---|
| **Legal Entity Name** | Main Line Brands LLC |
| **Prior Entity Names** | Authority Franchising, LLC (Sept 2020 – Mar 2021); TMAFS, LLC (2018–2020); TMA Franchise Systems, Inc. (2011–2018) |
| **Entity Type** | Delaware Limited Liability Company |
| **Organized** | September 10, 2020 (as Authority Franchising, LLC); renamed March 18, 2021 |
| **Parent Company** | Main Line Brands (is the parent entity itself) |
| **Principal Address** | Hickory, North Carolina |
| **Franchising Since** | ~2012 (under TMA Franchise Systems) |
| **FDD Years Found Online** | 2018 (FDD Exchange), 2025 (FDD Exchange) |
| **California Registration** | UNCERTAIN — not confirmed from available sources |
| **CA DFPI Verified** | NOT YET — requires manual search on DFPI Unified Search |
| **Search Name for DFPI** | "Main Line Brands" (current) or "TMAFS" or "TMA Franchise Systems" (historical) |

**Ambiguity:** HIGH. The franchisor entity has changed names four times. The DFPI
filing could be under any of these names. The brand name "Mosquito Authority" does
not appear in any of the legal entity names. Must search all four entity names.

### 4. Mosquito Hunters

| Field | Value |
|---|---|
| **Legal Entity Name** | Mosquito Hunters, LLC (also referred to as "MH" in FDD documents) |
| **Prior Entity Name** | MH Franchising, LLC (predecessor, before May 2018 acquisition) |
| **Entity Type** | Delaware Limited Liability Company |
| **Parent Company** | LD Parent, Inc. (direct); CNL Strategic Capital, LLC (indirect) |
| **Principal Address** | 142 State Route 34, Holmdel, New Jersey 07733 |
| **Franchising Since** | May 2018 (under MH); brand founded ~2013 |
| **Current Brand Names** | Pest Hunters / Mosquito Hunters / Humbug Holiday Lighting |
| **FDD Years Found Online** | 2021 (FranChimp), 2022 (NASAA EFD — downloadable PDF), 2024 (Google Cloud Storage) |
| **California Registration** | LIKELY — CA is listed as a franchise registration state in their FDD |
| **CA DFPI Verified** | NOT YET — requires manual search on DFPI Unified Search |
| **Search Name for DFPI** | "Mosquito Hunters" |

**Ambiguity:** MODERATE. The FDD uses "MH" as a shorthand for the franchisor.
The brand has expanded to include Pest Hunters and Humbug Holiday Lighting. The
DFPI filing could be under "Mosquito Hunters" or "MH."

### 5. Mosquito Shield

| Field | Value |
|---|---|
| **Legal Entity Name** | Mosquito Shield Franchise Corporation |
| **Entity Type** | Delaware Corporation |
| **Organized** | November 2012 |
| **Parent Company** | Five Star Franchising (acquired March 2022) |
| **Principal Address** | Springville, Utah (Five Star HQ); formerly North Attleboro, MA |
| **Franchising Since** | February 2013 |
| **System Size** | 125 franchised outlets in 441 territories (as of Dec 31, 2024) |
| **FDD Years Found Online** | 2023 (FranChimp), 2025 (various references) |
| **California Registration** | REPORTED — one source states registered in CA, NY, WI, WA, RI |
| **CA DFPI Verified** | NOT YET — requires manual search on DFPI Unified Search |
| **Search Name for DFPI** | "Mosquito Shield Franchise Corporation" |

**Ambiguity:** LOW. Legal entity name is straightforward and well-documented.

---

## Manual Verification Steps Required

The JavaScript-rendered DFPI search interface prevents automated verification.
A human must perform the following steps:

### Step 1: Access the DFPI Unified Search
1. Go to https://dfpi.ca.gov/regulated-industries/franchises/
2. Click "Search Franchises"
3. This opens the Unified Search filtered to franchise entities

### Step 2: Search for Each Brand (by Legal Entity Name)
Search for each of these legal entity names (one at a time):

1. `Mosquito Joe Franchising`
2. `Mosquito Squad Franchising SPE` (also try `Mosquito Squad Franchising`)
3. `Main Line Brands` (also try `TMAFS`, `TMA Franchise Systems`, `Authority Franchising`)
4. `Mosquito Hunters` (also try `MH`)
5. `Mosquito Shield Franchise Corporation`

### Step 3: For Each Result Found
Record:
- Registration status (Effective, Expired, Revoked, Terminated)
- Portfolio number (has a downloadable link to documents)
- Expiration date
- Filing years available

### Step 4: Download FDD Documents
- Click the portfolio number link to access filed documents
- FDDs, blacklines, applications, comment letters, and approvals should be available
- Download the most recent FDD PDF for each brand
- Place downloaded files in `data/raw/` following naming convention:
  `{brand-slug}_CA_{year}_FDD.pdf`

---

## Alternative FDD Sources (Free)

| Source | URL | Notes |
|---|---|---|
| NASAA EFD | https://www.nasaaefd.org/Franchise/Search | Free public search; has Mosquito Hunters 2022 FDD confirmed |
| FDD Exchange | https://fddexchange.com | Membership community; has historical FDDs for most brands |
| FranChimp | https://www.franchimp.com | Has FDD PDFs but returns 403 on programmatic access |
| Wisconsin DFI | (separate research needed) | Wisconsin is another major FDD source state |

### Confirmed Downloadable FDD URLs

1. **Mosquito Hunters 2022 FDD (NASAA EFD):**
   https://www.nasaaefd.org/Franchise/Actions/DownloadFile.ashx?DocId=30056&isRegistered=true

2. **Mosquito Hunters 2024 FDD (Google Cloud Storage):**
   https://storage.googleapis.com/franchiseindx_fdds/Home-Services/Mosquito%20Hunters_2024_rb12ox58

3. **Mosquito Squad 2012 FDD (FDD Exchange):**
   https://fddexchange.com/wp-content/uploads/2014/03/Mosquito-Squad-Franchise-Disclosure-Document-FDD-April-10-2012.pdf

4. **Mosquito Joe 2013 FDD (FDD Exchange):**
   https://fddexchange.com/wp-content/uploads/2014/09/Mosquito-Joe-FDD-2013.pdf

5. **Mosquito Squad 2013 FDD (FDD Exchange):**
   https://fddexchange.com/wp-content/uploads/2014/11/Mosquito-Squad-FDD-2013.pdf

---

## Summary of Confidence Levels

| Brand | Legal Entity Confidence | CA Registration Likelihood | Manual Verification Needed |
|---|---|---|---|
| Mosquito Joe | HIGH | HIGH (has CA locations) | Yes — DFPI search |
| Mosquito Squad | HIGH (but entity changed 3x) | HIGH (CA in FDD reg states) | Yes — DFPI search, try all entity names |
| Mosquito Authority | MEDIUM (entity changed 4x) | UNCERTAIN | Yes — DFPI search, try all entity names |
| Mosquito Hunters | MEDIUM-HIGH | HIGH (CA in FDD reg states) | Yes — DFPI search |
| Mosquito Shield | HIGH | HIGH (reported registered in CA) | Yes — DFPI search |
