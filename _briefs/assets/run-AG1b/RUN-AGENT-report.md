**needs the Cornerstone export** — Fix 1 (Cornerstone truth from David's Cornerstone Connect export)
could not run. `~/Downloads/cornerstone-book-2026-09-26.json` does not exist (checked Downloads in
full, and searched the whole disk for the filename; not found anywhere). Everything below is Fix 2, 3
and 4 only. No "Cornerstone verify" tab was produced. See Assumptions #1 and Questions #1.

# RUN-AGENT-report (Run AG1b, 2026-09-26): fix the master book

Terminal: AGENT. Read only against every source, no GHL writes, no files moved except the two
supersede moves the brief asked for, no employee-level data anywhere, no client data in git.

## Setup

- Read `_BUILD-LOG/BRIEF-AGENT.md` (Run AG1b) and `_BUILD-LOG/COWORK-AUDIT-run-AG1-2026-09-26.md` first,
  as instructed.
- Backed up `_BUILD-LOG/RUN-AGENT-report.md` (the AG1 report) to
  `_to_delete/superseded-2026-09-26/run-ag1-report/RUN-AGENT-report-v1.md` before overwriting it.
- Moved `master-book-2026-09-26.xlsx` (v1) to `_to_delete/superseded-2026-09-26/master-book-v1/`.
- Reused AG1's build script rather than starting over: it was not in this repo or the Master Kit (only
  the brief copy and report copy were ever committed), but the actual AG1 scripts and their raw output
  files were still sitting in that prior session's scratchpad directory on this Mac
  (`/private/tmp/claude-501/.../8655c99f.../scratchpad/job3_build_book.py` and siblings). Copied them in,
  read `job2_read_sheets.py` and `job3_build_book.py` in full, then patched `job3_build_book.py` into
  `job_ag1b_build.py` with the four fixes below rather than rewriting the pipeline.

## Fix 1: Cornerstone truth — BLOCKED, not applied

`~/Downloads/cornerstone-book-2026-09-26.json` is missing. Per the brief, stopped Fix 1 and left
Cornerstone-side logic exactly as AG1 had it: folder placement under
`3. Cornerstone PEO/4. Clients Cornerstone PEO` still wins as the strongest signal (unchanged), and
`Client CSR List for David 9.9.25.xlsx` / `DT Clients - CSR.xlsx` enrichment is untouched — there is
nothing to check either against without the export. No "Cornerstone verify" tab exists this run.

## Fix 2: Zoho is Teamworks, never Cornerstone — DONE

Before (AG1, wrong): the Zoho Closed Deals report added PEO = Cornerstone to every company it touched,
whether the deal was Closed Won or Closed Lost, and the Zoho Sales Deals (open) report did the same for
every open deal. Combined with folder data this produced 940 companies tagged PEO = Cornerstone and 355
Cornerstone/G&A "conflicts" (Cowork's audit: 229 of the "Cornerstone Client" 584 came from this file
alone).

Change: neither Zoho file sets a PEO anymore (both are Teamworks Group's old CRM). Zoho Closed Won deals
now map to "G&A Client" (301 — company also has a real G&A folder, or an Active rating in G&A CRM
Accounts Update) or "Former Teamworks client" (225 — no other PEO evidence; new status, not seen in
AG1). Zoho Closed Lost stays "Lost" (244) but no longer force-tags PEO = Cornerstone. Zoho open deals
(previously PEO = Cornerstone) now carry no PEO.

| Metric | Before (AG1) | After (AG1b) |
|---|---|---|
| PEO = Cornerstone (any) | 940 | 372 |
| PEO = Cornerstone,G&A (dual) | 107 | 39 |
| Status: Cornerstone Client | 584 | 355 |
| Status: G&A Client | 582 | 617 |
| Status: Former Teamworks client | (did not exist) | 193 |
| Conflicts total | 355 | 39 |
| Conflicts — HARD (real folder both sides) | 39 | 39 |
| Conflicts — soft (name match only) | 316 | 0 |

All 316 soft conflicts disappeared, confirming Cowork's read that they were a side effect of the Zoho
mislabel rather than real dual-PEO relationships. The 39 HARD conflicts are unchanged (folder evidence,
not touched by this fix) — full list under Questions #2 below.

## Fix 3: contacts and notes — DONE, with one source blocked

**Contacts.** Gathered from: the Zoho Sales Deals report copy (`crm:cs_sales_deals_report`, same source
AG1 used), G&A CRM Accounts Update (company phone only — this file has no contact name/email columns),
and the fresh GHL snapshot (`GHL-contacts-for-Cornerstone-CRM-2026-09-24.csv`, 2,150 rows — AG1 only
used this to set an in/out flag; this run pulls the actual name/email/phone/title off every row). The
Cornerstone Connect export would have been a fourth contact source (Fix 1) but is missing. **The iCloud
"ZOHO information" Contacts and Leads files could not be read this run** — every attempt (`find`, `ls`)
against that folder was blocked by the local permission classifier as "Credential Exploration"; this is
not a client-data or hard-stop issue, it is this session's own tool permissions. See Questions #3.

Result: 1,122 contact rows across 916 distinct companies (AG1 had 486 contact rows, all from the one
Zoho deals file, and only 121 companies with any email).

**Notes.** AG1's report said notes could not be linked because "no Zoho Accounts master export exists
to map [note] record IDs back to company names." That was incorrect — checked the actual columns:
`Notes_Accounts_2025_10_15.csv`'s "Parent ID" column and `Notes_Deals_2025_10_15.xlsx`'s "Parent ID"
column already hold the company/deal **name** directly (not just a raw `zcrm_...` ID — that's the
separate "Parent ID.id" column); `Notes_Contacts_2025_10_15.csv` has a separate "Client" column with the
company name. Linked all three files by matching that name against the Book's normalized company names.

| Metric | Before (AG1) | After (AG1b) |
|---|---|---|
| Notes tab rows | 0 (placeholder text only) | 1,003 linked |
| Raw note rows available | 508 + 21 + 1,966 = 2,495 | same 2,495 |
| Notes linked to a Book company | 0 | 1,003 |
| Notes NOT linked (no matching company/deal name in the Book) | — | 1,492 |

The 1,492 unlinked notes are mostly Cornerstone service-line deal names that don't match a folder or CRM
company row exactly (e.g. "AGL Boxing Crew LLC - Payroll and HR", "A&T Services LLC- PEO
(onboarding/HR)") — full sample list in `summary-v2-2026-09-26.json`. Note text is capped at 4,000
characters and HTML-unescaped/stripped per the brief.

## Fix 4: load readiness — DONE

Added a real "Load ready" column to the Book tab: yes only if the company has a real status (every row
has one) AND at least one contact (from the new Contacts tab, any source) with an email or a phone.
Name-only companies move to a new "Needs contact" tab and are marked `skip - needs contact` in Proposed
GHL action rather than `create`.

GHL matching is now a cascade — contact email, then contact phone, then contact email domain, then
company name (AG1 only tried company name).

| Metric | Before (AG1) | After (AG1b) |
|---|---|---|
| Load ready (has an email or phone contact) | 121 companies had *any* email (no formal column) | 916 (yes), 1,704 (no → Needs contact) |
| Matched to an existing GHL contact | 59 (name only) | 145 (67 email, 46 phone, 32 email domain) — the 59 AG1 found by name are all inside this 145; a better method already caught every one of them |
| Proposed action: create | 2,561 | 771 |
| Proposed action: update | 59 | 141 |
| Proposed action: skip (Broker/Vendor) | 38 | 38 |
| Proposed action: skip - needs contact | (did not exist) | 1,670 |

## Outputs

- `master-book-v2-2026-09-26.xlsx` — tabs: Book, Conflicts (HARD listed first), Contacts, Notes,
  Needs contact, Sources. (No "Cornerstone verify" tab — see Fix 1.)
- `load-plan.md` — rewritten with all four fixes' numbers and what changed from AG1.
- `summary-v2-2026-09-26.json` — machine-readable counts, including the notes-unlinked sample.
- v1 outputs (`master-book-2026-09-26.xlsx`, the AG1 `RUN-AGENT-report.md`) moved/backed up to
  `_to_delete/superseded-2026-09-26/` as instructed. `folder-plan.md`, `inventory.md` and the v1
  `summary-2026-09-26.json` are untouched — this run's brief did not ask for changes there.

Nothing was written to GoHighLevel and no client folders were touched (only the two supersede moves
above, both inside `_to_delete/` in the same OneDrive tree).

## Assumptions

1. **Fix 1 stop condition read literally.** The brief says "if it is missing, stop" under the Fix 1
   heading specifically; read that as stopping Fix 1 only (not the whole run), since Fixes 2-4 do not
   depend on the Cornerstone Connect export and the brief's own "how David wants runs done" rule says
   build the whole run end to end. If David meant the whole run should halt, Fixes 2-4 below are still
   correct and reusable once the export shows up — nothing here needs to be redone.
2. **"Real status" in Fix 4** taken as: every company already has some status from the folder/CRM pass,
   so "Load ready" reduces to the contact-presence test alone. No company was excluded from Load ready
   for having a "fake" status.
3. **Zoho Closed Won → G&A Client threshold.** Used "has a real G&A folder" OR "Active rating in G&A CRM
   Accounts Update" as the bar for G&A Client vs. Former Teamworks client, per the brief's Fix 2 wording
   ("unless the company has a G&A client folder or an Active rating in G&A CRM Accounts Update"). A
   company with neither signal defaults to Former Teamworks client even if it's plausibly still a G&A
   client under a slightly different name — this is a conservative read, not a confirmed fact.
4. **Which Notes_Deals copy.** Used the same copy AG1 used (`3. Cornerstone PEO/.../Zoho client info`),
   not the G&A OneDrive copy — they differ by ~100 bytes (inventory.md, AG1). Still unresolved which is
   current; see Questions #4.
5. **iCloud ZOHO information folder** (Contacts/Leads files) named in Fix 3 could not be read — blocked
   by this session's own permission classifier, not a brief hard-stop. Did not retry with a different
   tool or a workaround per the tool's own instructions; flagging it for David instead. See Questions #3.
6. Zywave cold list (8,030 rows) stayed out of the Book, unchanged from AG1/Cowork's answer.

## Questions for David

1. **Cornerstone Connect export.** `~/Downloads/cornerstone-book-2026-09-26.json` was never found. Can
   you re-export it from Cornerstone Connect (accounts, contacts, notes, tasks) so Fix 1 can run — CSR,
   contract type, referral partner, effective date, employee count, entity code (CIP/CU/CCG/CESIV), and
   the "Cornerstone verify" tab for the 303 CSR-list rows all depend on it.
2. **The 39 HARD conflicts** (real folder on both a Cornerstone and a G&A tree) — your call on which PEO
   each one actually is: Access To Hearing LLC Michael Guiden Referal, Do Unto Others Construction, Good
   Bones LLC Megan S Corp, Gratidao LLC, Hope Hearing and tinnitus center, Ibex Plumbing, Incisor health
   and fitness, John V Loia MD PC, Kim Day Construction, KW Powder and Fab LLC DBA Advanced Powder
   Coating and Fabrication, LA Hearing Diagnostic Center Warner, LERANA Talents LLC, Lotus Health, Make
   Wellness, Many Hands For Haiti, Mery Floor Coverings Inc - S-Corp, Modern Optical International,
   Nlitn, Nlitn Energy Solutions Ops, North Shore Lodge, Pacific Coast Polished Concrete, Pioneer
   plastics Inc. DBA pioneer molding, Pro Elements, Progressive Eye Care, Ravenswood, Rhino Insurance
   Inc, Siding Solutions and Construction, Silver State Surgery Center, Sistar Mortgage Company, SoCal
   Elite TC - Tara Hellickson referral, SoCal Hearing Jonathan Leitterman, Solid Rock Paving Co LLC,
   Stellar Excavtion, StretchLab, Tommy Gun Tools & Autobody LLC, Tuxedo Yard Care LLC James Wingett,
   Velvet Ink Hadlee S corp, Wernli Inc, Windsor Healthcare Recruitment Group Inc.
3. **iCloud "ZOHO information" folder** (under Personal/Davids Entities/Family businesses and docs/PEO
   Business) is blocked for this Claude Code session by its own auto-mode classifier ("Credential
   Exploration"), so its Contacts and Leads files were never read for Fix 3. Do you want to add a
   permission rule for that path, or should future AGENT runs skip that folder entirely?
4. **Which `Notes_Deals_2025_10_15.xlsx` copy is current** — the one under
   `3. Cornerstone PEO/1. CS Sales/5. Leads/Old PEO Info Leads/Zoho client info` (used this run, same as
   AG1) or the one under `OneDrive-G&APartners/My Drive/Zoho client info` — they differ by about 100
   bytes.
5. **Which "Teamworks Group One Drive Transfer" folder is the real one** — the 264 KB top-level one
   (which has one file the other lacks, "Client list closed for G and A in TWG prism.xlsx") or the 549
   MB one nested inside "Teamworks Client info" — carried over unanswered from AG1, this run did not
   touch either.
