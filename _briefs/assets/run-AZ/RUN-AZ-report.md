# Run AZ report (GHL JOBS terminal): software lines in Quick Quote, prices.json, Total Impact model

Written 2026-09-16. All five jobs in `_BUILD-LOG/BRIEF-GHL-JOBS.md` are done. No hard stops hit. Committed and
pushed to the atlas-one-intake-forms repo.

## Built

### Job 1: Quick Quote gets per product software lines
File: `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`. Backed up first to
`_to_delete/superseded-2026-09-16/Atlas_One_Quick_Quote_before_runAZ.html`.

- Added five new items to the `tech` division, right after `sw_marketplace`: `m365_basic` ($7), `m365_standard`
  ($14), `m365_premium` ($22) and `m365_copilot` ($21), all model `per_unit_mo` with a Users quantity box
  (qtyLabel "Users", qtyDefault 1), and `m365_other` (quoted). See Assumptions for why the model is `per_unit_mo`
  and not `flat_mo`.
- Added `qb_time` (QuickBooks Time), model quoted, in `tech`.
- `sw_marketplace`'s description rewritten to drop the dash and the word "negotiated."
- `qbo` item (in `financial`) fixed: choices are now Simple Start $38, Essentials $85, Plus $140, Advanced $340,
  default Essentials $85, new description, the "50% off the first three months" line removed, Ledger and
  Solopreneur dropped.
- Verified in headless Chromium: enabled Business Basic and Business Standard, set 12 users on each, total shows
  $84/mo + $168/mo = $252/mo, $3,024 year one, zero console errors. Screenshot:
  `_briefs/assets/run-AZ/shots/runAZ-quickquote.png`.

### Job 2: prices.json software block gets real prices
Files: `tools/agreements/prices.json` (repo) and its mirror at
`_INTERNAL (do not share)/tools/agreements/prices.json` (Master Kit). Backed up the mirror's old version to
`_to_delete/superseded-2026-09-16/prices_before_runAZ.json`.

- Replaced the `software` block with the six real client prices from the brief, removed the placeholder `_note`.
- Fixed `bookkeeping.quickbooks_sub` to the four plan prices.
- Found `generate.py` had no function to build a "Software and Licenses Schedule" at all, despite the brief
  assuming one exists. There WAS a stray, hand built `Atlas_One_Software_and_Licenses_Schedule.docx` sitting in
  the masters output folder (marked "ATTORNEY REVIEW PENDING," missing the Copilot and QuickBooks Online rows,
  no matching PDF, never wired into `generate.py`). Moved it to
  `_to_delete/superseded-2026-09-16/Atlas_One_Software_and_Licenses_Schedule_stray_attorney_review_pending.docx`
  and wrote a proper `schedule_software()` function plus a `Sample_Proposal_Software_and_Licenses` into
  `generate.py` (repo and mirror; backed up the mirror's prior `generate.py` to
  `_to_delete/superseded-2026-09-16/generate_before_runAZ.py`), reusing the stray document's clause language
  since it read well and matched the house style.
- Ran `generate.py`: 21 documents built (was 19) into
  `_INTERNAL (do not share)/tools/A1_Sales/A1 Agreements/2026-09-15 masters/`.
- Verified: BaseFont in both new PDFs is Horas-Medium / DM Sans-Regular / DM Sans-Bold only. Read the docx tables
  back for the Schedule, its sample proposal, and the Bookkeeping Schedule; all six software prices and the new
  QuickBooks Online line print correctly.

### Job 3: Total Impact Model shows software
File: `08 ROI Quote Master Template/Total_Impact_Model/total_impact_model.py`. Backed up to
`_to_delete/superseded-2026-09-16/total_impact_model_before_runAZ.py`.

- Added `software_resold` to `LINE_SPEC` (Technology & Operations division).
- Added `software_resold_line(p)`, which reads `m365_users`, `m365_plan` (basic/standard/premium),
  `m365_copilot_users`, `qbo_plan` (simple_start/essentials/plus/advanced) and `current_software_spend` from the
  prospect JSON, and reads unit prices from `prices.json` (Job 2) by a path resolved relative to the script, so
  no username and no hardcoded $7/$14/$22 anywhere in the model.
- With none of those fields present, `build()` falls through to the standard "not quoted" zero row, so an
  existing prospect file is completely unaffected. Verified: ran `total_impact_model.py` against
  `prospects/big_red_jelly.json` before any edit and after, output is byte for byte identical
  (`_briefs/assets/run-AZ/runAZ-tim-before.txt`).
- Added the new fields to a scratch copy of the same prospect (10 users on Standard, 2 Copilot seats, QuickBooks
  Essentials, no `current_software_spend`): Technology & Operations now shows a cost of ($3,204)/yr
  (10x$14 + 2x$21 + $85, x12), correctly printed as a negative, and the net first year impact drops from $1,667
  to ($1,537) (`_briefs/assets/run-AZ/runAZ-tim-after.txt`). Smoke tested the `current_software_spend` branch
  separately (not saved): a spend of $5,000 against a $2,700 resale total prints a $2,300 saving, as designed.
- Updated `build_tim.py`'s `LINES` list to add the same row so the interactive HTML builder stays in step, but
  could **not** re-run `build_tim.py` itself: it reads `/home/claude/pb` (base64 font data) and
  `/home/claude/tim/tim.html`, both paths from whatever cloud sandbox last built
  `Atlas_One_Total_Impact_Model.html`, and neither exists in this environment. Question for David below.
- Checked the PEO/HCM deck generator (`PEO_Proposal_Generator_V4.5_MASTER/service_deck.py`, `peo_deck.py`,
  `comparison_deck.py`, `light_deck.py`) for anything that renders a quote table from a prospect JSON. None of
  them do; they are static sales decks with fixed content, no dynamic pricing table. No deck edit made, no
  render done.

### Job 4: Quote Cockpit
File: `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`. Backed up to
`_to_delete/superseded-2026-09-16/Atlas_One_Quote_Cockpit_before_runAZ.html`.

- Confirmed the Cockpit carries its own, separate service catalogue; it does not read Quick Quote at all (no
  reference to the Quick Quote file or its item ids anywhere in the Cockpit, and its own QBO picker had already
  drifted to 10/20/35/65/99/235, different numbers from Quick Quote's own pre-fix 10/20/38/75/115/275).
- Fixed the Cockpit's QBO picker to 38/85/140/340 and dropped Ledger/Solopreneur, matching Job 1.
- Added `m365basic`, `m365std`, `m365prem`, `m365copilot` (7/14/22/21, Technology & AI division) and `qbtime`
  (quoted) to the Cockpit's own service array.
- The Cockpit has no per-user quantity mechanism anywhere; every line is a flat monthly price the user types
  into a "price /mo" box while on a call (confirmed by reading its `renderSvc()`/`calc()` functions). No similar
  per-user flag exists to reuse, so the four Microsoft labels say "(per user, type users x $7)" etc., so David
  multiplies by seat count himself when filling in the price box.
- Left the Cockpit's internal margin-cost field at 0 for all five new lines; I do not have Atlas One's real Pax8
  cost for these products, and typing a guess would quietly corrupt the Cockpit's own margin calculator. Question
  for David below.
- Verified in headless Chromium: zero console errors, "Business Basic" and "QBO Simple Start" both present in the
  rendered service list, scrollWidth = 390 at a 390px viewport. Screenshot:
  `_briefs/assets/run-AZ/shots/runAZ-cockpit-390.png`.
- The Cockpit and Quick Quote now hold two independent copies of the software catalogue and will need to be kept
  in step by hand going forward.

### Job 5: COMMAND rebuild and check
- `catalogue_check.py` OK: 192 entries, all paths resolve.
- Rebuilt `Atlas One COMMAND.html`: 192 items, 47,894,803 bytes. Title stamp confirmed current
  ("Atlas One COMMAND: build Sep 15, 2026 8:04 PM").
- Verified in headless Chromium at 1440px: zero console errors, scrollWidth = viewport.
- `build_command.py` now produces one output only; the separate "Atlas One Tools (share with prospects).html"
  was retired 2026-09-15 (per the script's own comment) in favor of a prospect/client audience guard that checks
  COMMAND's own rows. CLAUDE.md's description of "two outputs from one builder" predates that change. Not fixed
  without being asked; flagged below.

## Assumptions

1. Microsoft 365 lines use model `per_unit_mo` (Quick Quote's per-unit-with-its-own-qty-box mechanism), not
   `flat_mo`. `flat_mo` has no per-user quantity control anywhere in the catalogue; `per_unit_mo` without a
   shared `qtyKey` is the catalogue's existing per-seat mechanism (used by `pay_1099`, `filing_1099`, etc.), so I
   used that instead of inventing a new field.
2. `qb_time` (both Quick Quote and Cockpit) ships as Quoted rather than a fixed rate, per the brief's own
   instruction ("Intuit prices it per user plus a base fee and the numbers move").
3. Wrote `schedule_software()` and its sample proposal into `generate.py` from scratch, since no such function
   existed despite the brief assuming one did. Reused the language from the stray, unfinished
   `Atlas_One_Software_and_Licenses_Schedule.docx` I found sitting in the masters folder, since it read well and
   matched the rest of the agreement set's tone.
4. `current_software_spend` in the Total Impact Model is treated as an annual figure, matching every other
   dollar amount in the prospect JSON schema (all existing `lines` entries are annual, e.g. BRJ's health premium
   line is $2,198/yr, not/mo).
5. `software_resold`'s `escalates` flag defaults to `True`, matching its sibling `software_stack` line, even
   though a software cost arguably would not grow with payroll. Kept consistent with the existing row rather than
   introducing a special case.
6. Left the Cockpit's per-line internal cost field at $0 for the five new lines rather than guess at Atlas One's
   Pax8 cost. The field only feeds the Cockpit's own margin calculator, so a wrong guess would be worse than a
   visible zero.
7. Did not touch CLAUDE.md's "two outputs from one builder" description of Atlas One COMMAND, even though the
   actual `build_command.py` now produces one output; that section describes Run AR (2026-09-14) history, and
   fixing repo documentation wasn't part of this brief.

## Skipped

- `build_tim.py` could not be re-executed; it depends on `/home/claude/pb` and `/home/claude/tim/tim.html`, paths
  from a different (cloud sandbox) session that built `Atlas_One_Total_Impact_Model.html` previously. Its source
  code was updated to match (the `LINES` list now includes `software_resold`) but the HTML output on disk is
  stale relative to that source until someone with those assets rebuilds it.
- No PEO/HCM deck was rendered to PNG, because none of the deck generator files in
  `PEO_Proposal_Generator_V4.5_MASTER` render a dynamic quote table from a prospect JSON or the Total Impact
  Model; they are static sales decks. There is nothing to add a software row to.
- Noticed `_BUILD-LOG/software-licenses-src-2026-09-16.tgz` (a build script for three marketing HTML one-pagers
  about software and licenses, unrelated to the agreements/proposal system this brief covers) sitting in the
  build log directory, apparently left by a different chat. Did not touch it; out of scope for this brief.

## Questions for David

1. **Ledger and Solopreneur**: dropped from both the Quick Quote and Cockpit QuickBooks pickers per the brief.
   Confirm you never quote those two plans, or say if they should come back.
2. **QuickBooks Time price**: currently Quoted everywhere (Quick Quote's `qb_time`, the Cockpit's `qbtime`) since
   Intuit prices it per user plus a base fee that moves. If you have a standard number you quote, tell me and
   I'll make it a fixed rate.
3. **Pax8 cost for the five new Cockpit software lines**: left at $0 in the internal margin field. If you want the
   Cockpit's margin calculator to mean anything for these lines, send me your current Pax8 cost per seat for
   each Microsoft 365 tier, Copilot, and your QuickBooks Online cost, and I'll fill it in.
4. **`Atlas_One_Total_Impact_Model.html` rebuild**: the interactive page is now one edit behind its own source
   (`build_tim.py`). Whoever last built it (with `/home/claude/pb` and `/home/claude/tim/tim.html` available)
   needs to rerun it to pick up the new software line.
5. **Cockpit vs Quick Quote drift**: they now hold two separately maintained software catalogues. Worth asking
   whether the Cockpit should eventually read Quick Quote's catalogue directly instead of keeping its own copy,
   to stop this from happening again on the next price change.
6. **`software-licenses-src-2026-09-16.tgz`**: a set of marketing one-pagers about software and licenses is
   sitting unbuilt in `_BUILD-LOG/`. Not part of this brief; let me know if you want it built or if it is stale.
