# OneDrive duplicate and old-version audit — 2026-09-14 (Run AR, Job 2)

Scope: `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/` (A1_Sales, HR_Docs, the Master Kit). Excluded
`_to_delete/`, `_gold_backup_2026-08-24/`, `3. Cornerstone PEO/`, `_reference-archive/`. **2,482 files** scanned
(hashed by SHA-256; no OneDrive Files-On-Demand placeholders were hit, every file materialized and hashed cleanly).

Protected from any move regardless of what the scan found: `A1_Final Brand/`, `_INTERNAL (do not share)` pricing
sheets, `12 DEMO Proposal Set`, any `_BUILD-LOG/` content (active build journal/working files, some intentionally
identical placeholders), `3. Cornerstone PEO/`. Nothing in this run's move step touched any of those paths.

## 1. Exact duplicates (same SHA-256, different paths)

**55 duplicate sets found, 79 duplicate files total.** Kept rule: the copy in the deepest/most-specific folder
inside the Master Kit or A1_Sales; the other copy is the move candidate.

- **45 moved** to `_to_delete/superseded-2026-09-14/duplicates/<original relative path>` (see section "Moves made" below for the list).
- **34 skipped (protected path)** — either the kept copy or the duplicate sits under `A1_Final Brand/`, `_BUILD-LOG/`,
  or is a `.DS_Store` collision inside a protected tree. Listed, not moved:
  - Brand asset duplicates (internal `_briefs/assets/` PNGs that duplicate the real `A1_Final Brand/1. Logos/...`
    files, and one `.ai` file duplicated into two proposal-generator `brand_logos/` folders) — 13 sets. Recommend:
    leave as is, these are working copies used by Python build scripts (`build_command.py`/proposal generators)
    that need a local `brand_logos/` folder to exist; deleting them would break those scripts even though the
    bytes are redundant with the master brand file.
  - `.DS_Store` collisions where at least one side is under `A1_Final Brand/` — 10 sets, cosmetic, not worth
    the risk of touching that tree.
  - `_BUILD-LOG` content duplicates — 9 sets: `email-3.html`/`email-4.html` (Run AQ's cadence-email set —
    these are two of the seven *intentionally identical* keep-as-is placeholders, confirmed against
    `RUN-GHL-JOBS-report.md`, do NOT deduplicate), `RUN-EMAIL-report.md` vs its `-phone-docs-stamp-2026-09-14`
    copy, four `phone-stamp-samples/*.png` before/after screenshot pairs that happen to hash identical (same
    footer crop, different source doc), and two `Excavation Toolbox Talks` `.ai`/`.png` false matches already
    covered by the zip section below.

## 2. Version families (name differs only by version tag, date, "(1)", "copy", "old", "FINAL", "draft")

**7 families found**, all list-only (none moved):
- 6 are inside `_BUILD-LOG/` (`resume-here-*`, `CHECKPOINT-2026-09-1[2-4]-*`, `prospecting-kit-src-*`) — this is
  the terminal's own dated checkpoint/resume system, working as designed, not stale duplicates.
- 1 real candidate: `Claude AI Workflow Setup and trainnings/Claud Master Blue Print Workflow/` has
  `Atlas_One_Master_Blueprint.docx`, `_v2.docx`, `_v3.docx`. Newest by name is v3 but oldest by mtime is the
  unversioned file — recommend David confirm which is actually current before anyone archives v1/v2 (docx,
  not touched here).

## 3. Zip files (25 found)

**14 are the brand kit deliverable under `A1_Final Brand/`** (both the working folders' own zips and the
`Final Brand Kit Zip files/` set) — kept, not touched, per instruction.

Of the remaining 11:
- **5 moved** (contents confirmed fully present unzipped beside the zip, via `zipfile` listing diff):
  - `A1_Sales/A1_Pitch Decks Inv/.../Atlas_One_General_Deck_LIGHT.pptx.zip`
  - `A1_Sales/Atlas 1 Bookkeeping/Archive.zip`
  - `A1_Sales/Atlas 1 Bookkeeping/Book Keeping Docs.zip`
  - `A1_Sales/Industry Playbooks/Audiology WSA Partnership Plus/WSA_VIP_Partnership_Plus_Package.zip`
  - `A1_Sales/Blog and Content/Atlas_One_Blog_Set_V1_2026-09-11.zip`
- **1 already handled as an exact duplicate** in section 1: the two `Excavation Toolbox Talks (28 EN and ES).zip`
  copies (`07 New HR and Safety Docs` and `Atlas One — Complete Kit for BRJ/7. Safety Library`) are byte-identical
  to each other; the `07 New HR...` copy was moved there, not here, to avoid double-counting.
- **5 list-only, not moved** — contents only partially or not at all present unzipped beside the zip:
  - `Book Keeping zip V 7.0/Book Keeping V 7.0.zip` — nothing unzipped beside it.
  - `Atlas 1 Payroll PEO/Atlas One Payroll and PEO.zip` — 3 of 4 internal PDFs exist beside it, but
    `Atlas_One_Division_Financial_Services.pdf` inside the zip is missing beside it.
  - `Atlas 1 Risk Docs/Risk Docs.zip` — only 1 of 4 internal PDFs exists beside it.
  - `05 Build Specs (for BRJ)/Atlas One Website Package/Atlas One - Website Package.zip` — 400-entry zip, only
    187 of 400 entries have a same-named file anywhere under the sibling folder; recommend a closer manual look
    rather than an automatic move.
  - Both `Excavation Toolbox Talks (28 EN and ES).zip` files (see above) — their own 28-file contents are NOT
    unzipped anywhere beside either copy, only duplicated as a zip-to-zip pair.

## 4. Junk (`~$` Office lock files, `.DS_Store`, empty folders)

**71 junk files found** (70 `.DS_Store`, 1 `~$Atlas_One_General_Deck_LIGHT.pptx` Word/PowerPoint lock file).
**48 moved** to `_to_delete/superseded-2026-09-14/duplicates/junk/`. **23 skipped** because they sit under a
protected path (`A1_Final Brand/1. Logos/...` — 20 files, `12 DEMO Proposal Set/...` — 3 files); left in place.

**9 empty directories** found (all under `_BUILD-LOG` or scratch/working folders) — listed, not touched, since
removing directories wasn't in scope and none were outside protected/working areas.

## 5. Stale content (old phone number, retired prices, old logo filename)

- **Old phone number `385-213-7177`**: 26 hits in html/md/txt, same finding as Run AQ (2026-09-14 earlier today) —
  every hit is inside `_BUILD-LOG/` build-journal files, a `_briefs/` internal note, or one draft email
  (`A1_Sales/Website/Email_to_Thomas_BRJ_phone_change_2026-09-14.txt`) that is *about* the phone number change.
  **Zero live/shipped files** contain the old number. Confirmed again, not re-fixed (rewriting the historical
  build journal would corrupt its own record, same reasoning Run AQ used). docx/pptx/xlsx not scanned this pass
  (Run AQ already covered that ground on 2026-09-14 and found 20 files — see `RUN-GHL-JOBS-report.md` from that
  run; not repeated here since this run made no doc edits).
- **Retired prices** (`$0/$299/$899` membership tiers, `$199/$349/$649` AI-assistant tiers): **zero live
  occurrences of the retired combination**. Every `$199` hit found in html/md is the *current* AI Task Agent
  standalone price (a different product from the AI Email Assistant, confirmed by
  `_BUILD-LOG/pricing-reconciliation-2026-09-07.md` and `build_portal.py`'s own catalogue blurb: "$199 per month
  standalone, $99 bundled with the Email Assistant"). The only place the old `$299`/`$899` membership numbers
  still appear is `_BUILD-LOG/RUN-V-report.md`, which is itself a still-open question to David about a pitch-deck
  slide (Slide 25 revenue boxes) from a prior run — already flagged there, not duplicated here.
- **Old logo filename**: could not confidently identify which A1_Final Brand filename is "the old globe logo"
  from the Master Kit's own naming (current names are Primary/Full Mark/Logo Mark/Name Mark, no filename
  containing "globe" was found anywhere in the brand folder or build logs). **Assumption**: skipped this specific
  check rather than guess at a wrong candidate filename; flagging as a question for David.

## 6. Unreferenced files (html/pdf/docx with no catalogue/Master Hub/other-html reference)

**1,306 candidate files** flagged by the heuristic (basename does not otherwise appear inside any other .html
or .md file in scope, or inside itself + zero other times for html files). The overwhelming majority are not
actually orphaned content needing action — they are **delivered library bundles meant to exist as a folder of
individual files**, not individually hyperlinked:
- 389 — `05 Build Specs (for BRJ)/Atlas One Website Package/` (a full packaged copy of the site content for BRJ)
- 269 — `Atlas One — Complete Kit for BRJ/6. Template Library (PDF lead magnets)/`
- 229 — `03 Template Library/Vol 2 (115)/`
- 118 — `Atlas One — Complete Kit for BRJ/7. Safety Library (programs & checklists)/`
- 116 — `04 Safety Library/Programs & Checklists/`
- 58 — `A1_Final Brand/1. Logos/` (individual logo file variants, not meant to be linked)
- 40 — `03 Template Library/Vol 1 (40)/`
- 34 — `A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/` (word/web-paste export folders)
- ~53 singleton hits scattered across division one-pagers, BRJ handoff docs, HR training PDFs, `Updated laws/`
  state notices, and old (`_v2`, `_v3`) Master Blueprint docx drafts.

Not moved (per brief, list-only). Catalogue.py did not exist yet when this scan ran (Job 1 was still building
it in parallel), so the reference check fell back to grepping filenames across every .html/.md file rather than
checking Job 1's new catalogue directly — worth a second, catalogue-based pass once `catalogue.py` lands, since
that will resolve most of these "unreferenced" hits as intentionally-bundled library content rather than actual
orphans.

## Moves made (summary)

- **93 files moved** total: 45 exact-duplicate files, 5 redundant zip files, 43 junk files (`.DS_Store`/lock
  files outside protected paths — note: 48 junk moves were attempted per the plan, but 5 of the DS_Store paths
  had already been relocated by the duplicate-move pass since some DS_Store files hash-collide across folders
  and were caught by both checks; net unique files moved is 93, not 98).
- All moved to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-14/duplicates/` (files) and
  `.../duplicates/zips/` and `.../duplicates/junk/` (zips and junk respectively), preserving each file's
  original relative path so it is traceable and reversible. Nothing was deleted.

## Assumptions

1. Kept-copy rule for exact duplicates: deepest/most-specific folder wins, per brief. Where the "kept" and
   "duplicate" folders were equally deep, the alphabetically/structurally more specific one (e.g. inside
   `Atlas One — Complete Kit for BRJ/` over a loose `05 Build Specs (for BRJ)/` file) was treated as more
   specific.
2. Any duplicate pair touching `_BUILD-LOG/`, `A1_Final Brand/`, `_INTERNAL (do not share)` pricing sheets,
   `12 DEMO Proposal Set`, or `3. Cornerstone PEO/` was treated as protected and left in place even though it
   technically matched the duplicate/junk criteria, since the brief's "Do not do" list bars touching those
   trees regardless of what else is true about the file.
3. Zip redundancy was judged by comparing the zip's internal file list against files present anywhere under the
   sibling folder (not just exact relative paths), to avoid false "not redundant" results from minor path
   nesting differences.
4. Old logo filename check skipped (no confident candidate found) rather than risk a wrong flag — see section 5.
5. Unreferenced-file check used a filename-substring heuristic across all html/md content in scope rather than
   Job 1's `catalogue.py` (which didn't exist yet when this scan ran); expect it to over-flag delivered library
   bundles as "unreferenced" when they're actually meant to ship as a folder, not a linked catalogue entry.

## Questions for David

1. `Claud Master Blue Print Workflow/`: which of `Atlas_One_Master_Blueprint.docx` / `_v2.docx` / `_v3.docx` is
   current? (docx, not edited/moved here.)
2. What filename is the retired "old globe A1 logo"? Couldn't find a confident match in `A1_Final Brand/` or the
   build logs to check against.
3. `Atlas One - Website Package.zip` (05 Build Specs for BRJ) is only 47% redundant with its sibling folder
   (187/400 entries match) — want it fully unzipped-and-reconciled, or left as is?
4. The 34 protected-path duplicate sets (brand asset working copies, `.DS_Store` inside `A1_Final Brand`,
   `_BUILD-LOG` near-duplicates) were left untouched on purpose — confirm that's right, or say which of those
   should actually be cleaned up despite sitting in a protected tree.
