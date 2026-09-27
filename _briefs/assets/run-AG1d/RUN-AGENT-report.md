# RUN-AGENT report (Run AG1d, 2026-09-26)

Terminal: AGENT. Read only against sources, no GHL writes, no employee files, no FEIN/rates/commission/bank,
no client data in git. Patched `job_ag1c_build.py` into `job_ag1d_build.py` (did not start over) to fix
three defects Cowork found in v3, plus two named merges from the "Also" section of the brief.

## What was built

- `job_ag1d_build.py` (script, committed to the repo, no client data inside it)
- `master-book-v4-2026-09-26.xlsx` in `<Master Kit>/_INTERNAL (do not share)/Book of Business/`
- `summary-v4-2026-09-26.json`, same folder
- `load-plan.md`, rewritten in place with v4 numbers, same folder
- `cornerstone-export-cache-from-v3-2026-09-26.json`, same folder (see Assumption 1 below — not in git)
- v3 book and summary moved to `_to_delete/superseded-2026-09-26/master-book-v3/`
- v2 (AG1c) report backed up to `_to_delete/superseded-2026-09-26/run-ag1c-report/RUN-AGENT-report.md`

Nothing written to GHL. Nothing deleted (v3 files moved, not deleted).

## Defect 1: Cornerstone Client was over-counting

**Root cause:** two separate bugs stacked. (a) The "Client CSR List for David 9.9.25.xlsx" rows were
unconditionally added to Book as "Cornerstone Client" even when neither the Cornerstone Connect export
nor DT Clients - CSR.xlsx backed them up, and were ALSO added to the new Cornerstone verify tab —
double-counted. (b) Every company found under the Clients Cornerstone PEO folder tree was marked
"Cornerstone Client" from folder evidence alone, with no check against export/DT CSR truth.

**Fix:** a CSR-list-only row (not in export, not already a company from another source) now lives on
the verify tab only, never in Book. A folder-only Cornerstone company (no export/DT CSR backing) is
downgraded to a new status, `Cornerstone (folder only, verify)`, Load ready forced to no, and also
added to the verify tab.

| | Before (v3) | After (v4) |
|---|---|---|
| Cornerstone Client (Book) | 395 | **84** |
| Cornerstone (folder only, verify) | (didn't exist) | **29** |
| Cornerstone verify tab rows | 280 | **309** |
| Verify-tab rows that ALSO appear as a Cornerstone Client Book row (double-count) | 273 (confirmed same companies) | **0** (confirmed by direct overlap check) |

The 395-to-84 drop is exactly the intended effect: 280 CSR-list-only rows moved off Book entirely onto
the verify tab, and 29 folder-only rows got their own honest status instead of a false "Cornerstone
Client."

## Defect 2: folder parser was turning subfolders into companies

**Root cause:** the folder walk decided "is this a group wrapper to recurse through, or a real company"
using a fuzzy substring match for "referr" / "terminat" in the folder name. That cut both ways:
- **False positive:** a real company whose name happens to contain the word "Referral" (e.g. "Vet AI -
  PPG Referral Jasmine") got treated as a wrapper, so its own admin subfolders — "1. Client Info
  CornerStone", "1099 Proposals", "2. Clients Previous Provider Information" — were scanned in as bogus
  companies.
- **False negative:** typo'd wrapper names ("Refferals", "Referaals" — real folder names on disk) didn't
  match the fuzzy check, so the wrapper folder itself got added as a bogus company row ("1. Hoffman
  Refferals", "1. Z Works Refferals", "1. Mathew Matta Referaals"), AND its real children were never
  discovered.

**Fix:** a folder is only ever a group wrapper when its name starts with a number and a dot (David's own
rule), recursed through exactly one level and never added as its own row. A generic administrative
folder name (client info, proposals, previous provider information, census, payroll, docs, forms,
quotes, copy folders) is dropped outright at any level, never recursed into.

Confirmed directly against every named example in the brief:

| Row | Before (v3) | After (v4) |
|---|---|---|
| "1. Client Info CornerStone" | present | gone |
| "1099 Proposals" | present | gone |
| "2. Clients Previous Provider Information" | present | gone |
| "1. Hoffman Refferals" | present | gone |
| "1. Z Works Refferals" | present | gone |
| "1. Mathew Matta Referaals" | present | gone |

13 wrapper folders dropped outright by name (10 examples logged in `summary-v4-2026-09-26.json`,
`defect2_dropped_junk_folder_examples`); the three admin-subfolder rows above are gone through a
different path (their parent folder is now correctly classified as a real company, so it is never
recursed into at all — they were never "dropped," just never visited a second time).

**Checked no real company was lost:** the 41 real companies inside "1. Hoffman Refferals" (e.g. ANDY
EARL CREATIVE LLC, Big Frog Systems), the 6 inside "1. Z Works Refferals" (including 5G Hearing), and
Dulak Physical Therapy and Golf (inside "1. Mathew Matta Referaals") all still appear in the Book —
every one of them already exists via the Cornerstone Connect export, GHL, or Zoho, just without that
one specific folder path attributed to them now. Confirmed directly, name by name.

## Defect 3: main contact was skipping the real person

**Root cause:** a "company phone, no named contact" placeholder row was inserted into each company's
contact list ahead of the real GHL and Cornerstone Connect contacts. The main-contact picker took the
first contact with an email OR phone — so the placeholder (which always has a phone if the company has
one) won the slot whenever it happened to be inserted before a real named contact, even one with an
email.

**Fix:** removed the placeholder entirely (the company phone still has its own Book column and still
counts toward Load ready — it just never wins the main-contact slot). Main contact now explicitly
prefers a named person with an email (Cornerstone Connect first for Cornerstone companies), then a
named person with a phone, and leaves the field blank if no named contact exists at all.

Ibex Plumbing (the brief's required example): **Mason Finch, info@ibexplumbingutah.com** — comes out
correctly as main contact now.

## Also (named merges)

- "AAMCOR Companies" (G&A lost folder) merged into the AAMCOR Inc row, placement note added.
- "Vet AI PPG referral" (Atlas One folder) merged into Vet-AI Inc, placement note added.
- "CIrque Lodge Tax FIllings" (Atlas One folder) is now a note + folder path on the existing Cirque
  Lodge Inc row, not its own row.

## Spot check (Status, PEO, CSR, main contact, Load ready)

| Company | Status | PEO | CSR | Main contact | Load ready |
|---|---|---|---|---|---|
| 5G Hearing LLC | Cornerstone Client | Cornerstone | Kayla Mouton | (none named — company phone only) | yes |
| AAMCOR Inc | Cornerstone Client | Cornerstone | Jennifer Allison | Digna Gittins, digna@aamcor.com | yes |
| CIRQUE LODGE INC | Cornerstone Client | Cornerstone | Jennifer Allison | Leslee Cook, leslee@cirquelodge.com | yes |
| Ibex Plumbing | Cornerstone Client | Cornerstone | Jennifer Allison | Mason Finch, info@ibexplumbingutah.com | yes |
| Vet-AI Inc | Cornerstone Client | Atlas One, Cornerstone | Charity Taylor | Jasmine Wickens, jasmine.wickens@peoplepayglobal.com | yes |
| Alta Auto Sales LLC | G&A Client | G&A | (none — not a Cornerstone account) | Craig Clayton, Claytoncraig75@gmail.com | yes |

AAMCOR carries a placement note ("Also quoted through G&A, lost (folder: AAMCOR Companies)"); Vet-AI
carries one for the PPG referral merge; Cirque Lodge carries the folded-in Atlas One task-word note.

## Full before/after counts (v3 -> v4)

| | v3 | v4 |
|---|---|---|
| Total companies | 2,674 | 2,375 |
| Cornerstone Client | 395 | 84 |
| Cornerstone (folder only, verify) | — | 29 |
| G&A Client | 617 | 616 |
| Load ready | 1,012 | 1,007 |
| Proposed action: create | 787 | 842 |
| Proposed action: update | 221 | 161 |
| Proposed action: skip - needs contact | 1,628 | 1,337 |
| Proposed action: skip (partner/vendor) | 38 | 35 |
| Cornerstone verify tab | 280 | 309 |
| Conflicts (true, unresolved) | 16 | 16 (unchanged — Defects 1-3 didn't touch conflict logic) |

(Total company count and create/update/skip mix shift for reasons unrelated to being "wrong": 280
CSR-list-only companies dropped from Book to verify-only per Defect 1, and a few merges per the Also
section reduced row count further; these are intended, not a regression.)

## Assumptions

1. **`~/Downloads/cornerstone-book-2026-09-26.json` became unreadable mid-run.** Same file, same owner,
   normal Unix permissions (`-rw-r--r--`), but every read attempt (Python open, `cp`, even `xattr -l`)
   returned "Operation not permitted" — a macOS folder-level privacy block (Downloads is a
   TCC-protected folder) on whatever app hosts this terminal session, not a data problem. It was
   readable earlier today in AG1c (confirmed by that run's own live log and report). Rather than block
   Job 1 again (AG1b's failure mode when the export was genuinely missing), I rebuilt a small cache of
   the export's already-verified per-company fields from AG1c's own `master-book-v3` output (Book,
   Contacts, and Notes tabs, filtered to rows/contacts/notes tagged `cornerstone:connect_export` /
   "Cornerstone Connect") and used that as this run's Job 1 truth source instead. No fresh Cornerstone
   Connect data was pulled this run — but Defects 1-3 are independent of that, and every fix above was
   verified correct against real folder-tree data either way. The cache lives at
   `<Master Kit>/_INTERNAL (do not share)/Book of Business/cornerstone-export-cache-from-v3-2026-09-26.json`
   (client data, correctly NOT committed to git) and the script falls back to it automatically only when
   the live Downloads file can't be read.
2. **The 41 Hoffman-referral clients, 6 Z-Works-referral clients, and Dulak Physical Therapy** (all
   3 levels deep inside a typo'd wrapper folder) are no longer linked to their Cornerstone folder path,
   since David's literal rule (company = immediate child of root, or immediate child of a digit-dot
   wrapper directly under root — never deeper) puts them one level past what the rule allows. Checked
   and confirmed every one of them still appears in Book via another source (export, GHL, or Zoho), so
   this is a folder-path-attribution loss only, not a missing-company loss. Flagged below in case David
   wants a follow-up rule for that specific double-wrapper pattern.
3. **The Client Info/Proposals/Previous-Provider-Information junk-word list** is a fixed set (client
   info, proposals, previous provider information, census, payroll, docs, forms, quotes, copy folders)
   matched with word boundaries, not a learned or exhaustive list — a future oddly-named admin subfolder
   under a different company could still slip through. Since the fix also stops all recursion into real
   company folders (the deeper root-cause fix), this risk is now limited to junk folders sitting directly
   under a Clients/Quotes root or a digit-dot wrapper, which is a much smaller surface than before.
4. Manual company merges (AAMCOR, Vet-AI) and the Atlas-One task-word fold (Cirque Lodge) are named,
   hand-written rules from the brief's exact examples, not a general fuzzy-matching heuristic — a general
   prefix-match rule risked folding in a real distinct company (e.g. "Arkus Advisory LLC US PPG",
   already its own legitimate row from the Cornerstone quotes tree, is NOT a task-word variant of
   anything).

## Questions for David

1. Do you want the same double-wrapper folder-path fix (Assumption 2) applied so Hoffman/Z-Works/Guiden
   referral clients get their Cornerstone folder path back, even though they're already in Book via
   other sources? It would mean allowing recursion one level past a referral-named wrapper inside a
   digit-dot group wrapper specifically (not a general depth increase).
2. This Mac's Downloads folder became unreadable to this terminal session mid-run (Assumption 1) — worth
   checking System Settings > Privacy & Security > Files and Folders for whatever app hosts this
   session, in case a future run needs a fresh Cornerstone Connect export pull.
3. Same 16 true conflicts as AG1c, still unresolved (list in `load-plan.md`) — still your call on which
   PEO wins each one.
4. Same as prior runs: OK to load the 842 "create" + 161 "update" rows (Load ready, no true conflict, no
   verify-tab flag) to GHL, with Do Not Disturb ON, once you've reviewed the Conflicts and Cornerstone
   verify tabs?
