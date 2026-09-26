# RUN-AGENT-report.md (Run AG1, 2026-09-26)

Terminal: AGENT. Goal: build David's master book of business, read only, nothing loaded to GHL and
no files moved. All five jobs in BRIEF-AGENT.md are complete.

## Outputs (all in `<Master_Kit>/_INTERNAL (do not share)/Book of Business/`, none in git)

- `inventory.md` — Job 1
- `master-book-2026-09-26.xlsx` — Job 3 (tabs: Book, Conflicts, Contacts, Notes, Sources)
- `summary-2026-09-26.json` — counts backing the numbers below
- `load-plan.md` — Job 4
- `folder-plan.md` — Job 5

`_briefs/BRIEF-AGENT-2026-09-25.md` in this repo is the copy of the brief this run worked from.

## Job 1: inventory

12 sources scanned end to end (file counts, sizes, spreadsheet inventory). Full table in
`inventory.md`. Highlights:
- Confirmed duplicates (safe to retire, proven byte-for-byte): the older `Clients Cornerstone` folder
  (3.2 GB), the older `Quotes Cornerstone` folder (0.65 GB), and one of the three Zoho client info
  copies (1 MB). Combined recoverable space: ~3.85 GB.
- Disproved one suspected duplicate: the two "Teamworks Group One Drive Transfer" folders (one nested
  inside `Teamworks Client info`, one at the iCloud top level) are NOT copies of each other — they
  diverged, each has files the other lacks. Do not touch either without David's input.
- The Cornerstone CRM JSON export Cowork mentioned (`~/Downloads/cornerstone-book-2026-09-26.json`)
  does not exist. Used the CS CSR spreadsheets and folder names instead, as the brief allowed.
- Two source trees are far larger than their file counts explain (A1 Brokers/Vendors: 65 GB / 410
  files; Cornerstone CS Sales: 50 GB / 2,049 files). Not investigated file-by-file this run (out of
  scope for a read-only pass); flagged for AG3 to run a top-largest-files check before doing anything
  with those trees.

## Job 2: structured sources

Read all 20 spreadsheets named in the brief (plus a fresh GHL contact snapshot re-pulled today via the
existing read-only export script: 2,150 contacts, up from the 2026-09-24 file's presumed count).
Notable finding: 9 of the Zoho CRM report exports in `ZOHO Reports` (Accounts by Services, Accounts by
Industry, Open Deals, Notes Report, Notes Deal, Contact Report, Contact Mailing List, Lead, Sales
Account report) contain only a header row — the export ran empty at some point. The real data lives in
a differently-named sibling file in most cases (e.g. `Sales+Deals+Report+Customized copy.xlsx` has 487
rows of real deal/contact data where `Sales+Deals+Report+Customized.xlsx` does not) or in the separate
`Zoho client info` folder (`Notes_Accounts`, `Notes_Contacts`, `Notes_Deals`: 508 / 21 / 1,966 rows).

## Job 3: the master book

`master-book-2026-09-26.xlsx`, tab **Book**: **2,620 companies**, deduplicated by normalized name
(LLC/Inc/Corp/DBA/punctuation stripped).

| Status | Count |
|---|---|
| Cornerstone Client | 584 |
| G&A Client | 582 |
| Prospect open | 1,184 |
| Lost | 213 |
| Former Client | 12 |
| Broker or Partner | 28 |
| Vendor | 10 |
| Atlas One Client | 7 |

By PEO: Cornerstone 940, G&A 1,517, both (flagged in Conflicts) 107, Atlas One 16, none (brokers/
vendors) 38, Atlas One+G&A 2.

The Zywave cold-call list (`Prospects Zywave.xlsx`, 8,030 rows) was **not** expanded into individual
Book rows — see Assumption 1 below. Its row count is recorded in the Sources tab so it is not lost from
the audit trail.

**Conflicts tab: 355 companies show signals for both PEOs.** Split into 39 HARD (the company has an
actual folder under both a Cornerstone tree and a G&A tree — highest confidence, e.g. Ibex Plumbing,
Good Bones LLC, Access To Hearing LLC) and 316 soft (one side is folder-confirmed, the other is only a
name match against a Cornerstone Closed Deals export row, and could be a genuine dual-referral
placement or a coincidental name collision between unrelated small businesses). Per the brief's rule
("a company that shows as a client with G&A must never be marked Cornerstone, and the reverse"), none
of these 355 rows had their PEO silently guessed — the Book tab shows one PEO for display but the
Conflicts tab is the source of truth, and the load plan tells AG2 not to touch any of them until
reviewed.

Fresh GHL snapshot matched by company name: 59 of 2,620 companies. Low, but expected — only 368 of the
2,150 GHL contacts have a Company field populated at all (see load-plan.md).

## Job 4: GHL load plan

`load-plan.md`. 2,561 proposed creates, 59 updates, 38 skips (brokers/vendors). Exact field mapping,
8 new tags (verified against today's GHL tag list — none collide with an existing tag), and the DND
safety rule the brief requires for every new contact until AG2 confirms Contact Created workflow
behavior.

## Job 5: folder tidy plan

`folder-plan.md`. Target structure plus a table of the 3 proven-duplicate moves (~3.85 GB recoverable,
all via `_to_delete/superseded-2026-09-26/`, nothing deleted) and a separate table of 4 "looks like a
duplicate but isn't, don't touch yet" items so AG3 doesn't repeat the same mistake this run almost made
with the Teamworks folders.

## What could not be read

Nothing failed outright. The Cornerstone CRM JSON was simply absent (see Job 1). No iCloud or
OneDrive-G&APartners folder was slow enough to skip.

## Assumptions

1. **Zywave cold list excluded from the per-company Book.** `Prospects Zywave.xlsx` has 8,030 rows of
   vendor-sourced cold-call data with no relationship history (no folder, no CRM record, no note). Per
   the brief's "every company David has ever touched," a cold list he has not personally engaged with
   is a different thing from the rest of the book, and expanding it would have tripled the row count
   with almost no usable data per row. Its count is preserved in the Sources tab; if David wants it
   merged in as `book-lead` rows for AG2, that is a small follow-up script, not a rebuild.
2. **CCG / CIP / CU / CESV treated as Cornerstone entity codes, not separate PEOs.** These four codes
   appear in the "PEO" column of `Client CSR List for David 9.9.25.xlsx` and were mapped to
   "Cornerstone" rather than kept as distinct PEO values, since the brief's PEO vocabulary is
   Cornerstone/G&A/Teamworks/none. The original code is preserved per-company in a hidden extra field
   if David wants it back.
3. **Closed Deals "Closed Won" mapped to Cornerstone Client, not Former Client.** An early build of this
   script wrongly treated every row in the Cornerstone Closed Deals export as a terminated client; the
   Stage column shows most closed rows are "Closed Won" (526 of 1,361), which means the deal closed and
   the company became a client, not that it left. Fixed before the final build; "Closed Lost" /
   "Closed-Lost to Competition" / "Closed - Fraud" / "Closed Never Ran Payroll" map to Lost.
4. **Folder placement outranks a CRM/spreadsheet name match for the displayed Status/PEO.** Where a
   company's own client/quote folder says one thing and a CRM row says another, the folder wins for the
   single Status/PEO shown in the Book tab (folder placement is closer to ground truth than a fuzzy name
   match). The losing signal is never discarded — it lands in the Conflicts tab.
5. **G&A CRM Accounts Update.xlsx status taken from the Rating column, not Account Type.** Account Type
   is empty for 1,067 of 1,171 rows; Rating (Active/Prospect/Acquired/Business Closed/Lost/Not
   Interested) is populated for all but 12 and is the real status signal in that sheet.
6. **Contract type, Referral partner, and Effective date columns are blank for every row.** No source
   read this run reliably carries these three fields at the company level (Referral partner is
   sometimes inferable from a folder name like "5. The Guiden Group" but that is a group container, not
   a clean data column, and Contract type / Effective date were not found in any of the 20 spreadsheets
   read). Populating these would need either a targeted new export or per-company folder inspection,
   which is out of scope for a read-only pass at this volume.

## Questions for David

1. The 39 HARD conflicts (real folders on both PEO sides for the same company) need your call on which
   PEO is actually current for each — see the Conflicts tab. Want these resolved before AG2, or should
   AG2 create both and let you merge in GHL?
2. Zywave cold list (8,030 rows, Assumption 1): merge into the Book as `book-lead` rows for AG2, or
   leave it as a separate cold-outreach list entirely outside this system?
3. `Notes_Deals_2025_10_15.xlsx` differs between the Cornerstone and G&A copies of "Zoho client info"
   (inventory.md) — do you know which export is more current, or should both be kept until you check?
4. The two "Teamworks Group One Drive Transfer" folders that turned out not to be duplicates — do you
   know which one is the one you actually use, so AG3 can propose where the smaller one's few unique
   files (including a "Client list closed for G and A in TWG prism.xlsx") should live?
5. A1 Brokers/Vendors (65 GB/410 files) and Cornerstone CS Sales (50 GB/2,049 files) are unusually
   large for their file counts — OK for AG3 to run a top-largest-files report there as a first step?
