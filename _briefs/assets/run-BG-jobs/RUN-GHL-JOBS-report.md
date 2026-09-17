# RUN GHL-JOBS report: Run BG (stale phone in P prospecting templates, apar default)

Terminal: GHL-JOBS (files and code only, no GHL browser UI). 2026-09-17.

## Built

### Job 1: stale 385-213-7177 phone number (partially done, see Skipped)
- Grepped `_BUILD-LOG/cadence-emails-2026-09-13/` in the Master Kit for `385-213-7177`, `385.213.7177`,
  `(385) 213-7177`, `+13852137177`: zero hits.
- Grepped the repo's `_briefs/assets/` for the same strings. Hits exist only in
  `_briefs/assets/_stale/run-AI-cadence-emails/` (marked stale historical run assets, excluded per the brief's
  "not the historical run assets" instruction) and in old run report/JSON files that quote the number as history
  (`run-W`, `run-AC`, `run-AM`, `run-AS`, `run-AY`, `run-AZ`, `run-BE`, `run-BG` report files). No live cadence
  file in the repo carries the stale number, so nothing needed fixing here.
- The Email Builder API portion of Job 1 (pulling the 21 P prospecting templates, grepping and fixing them) was
  not attempted. See Skipped and Questions below.

### Job 2: apar default and rebuild
- Backed up `Atlas_One_Quote_Cockpit.html` to
  `_to_delete/superseded-2026-09-17/before-runBG/Atlas_One_Quote_Cockpit.html`.
- Set the `apar` row ("A/P + A/R management", Financial Services) monthly price from $0 to $500 (A/P $250 plus
  A/R $250, matching the two separate Quick Quote rows `ap` and `ar`, each `rate:250`) in the service catalog
  array, line 268 of `Atlas_One_Quote_Cockpit.html`.
- Reran `build_cockpit.py`. It only rewrites the ATLAS_ONE_PRICES/ATLAS_ONE_TIERSET marker blocks from
  `prices.json` (unrelated to `apar`, which lives in the catalog array outside those markers), so the price
  edit survived untouched. Console output unchanged from the last run (QBO, M365, AI Email, membership tiers,
  cert payroll, handbook/safety custom setups, GL import all as before).
- Backed up `Atlas One COMMAND.html` to `_to_delete/superseded-2026-09-17/command-before-runBG/`.
- Ran `catalogue_check.py`: OK, 192 entries, all paths resolve.
- Ran `build_command.py`: wrote `Atlas One COMMAND.html`, 192 items, 48,648,912 bytes (same item count and size
  as the pre-run file; `apar` lives in the Cockpit, not the catalogue, so the COMMAND rebuild is unaffected in
  content but was rerun and reconfirmed per the brief). Stamp confirmed:
  `Atlas One COMMAND: build Sep 17, 2026  8:00 AM`.

## Verification
Headless Chromium (Playwright), against the pre-edit backup and the rebuilt Cockpit:
- **Before total** (backup file, `apar` row checked in the UI): **$0** added to "Total monthly, all-in".
- **After total** (rebuilt file, same row checked): **$500** added to "Total monthly, all-in".
- Zero console errors and zero non-`file://` network requests on both the before and after Cockpit, at 1440px
  and at 390px (scrollWidth equals the viewport at both widths on both versions).
- One-pager PPTX export: clicked the button, download completed to
  `_briefs/assets/run-BG-jobs/onepager_test.pptx`, zero console errors.
- `Atlas One COMMAND.html` at 1440px: zero console errors, zero non-`file://` requests, scrollWidth equals
  viewport.
- Screenshots at `_briefs/assets/run-BG-jobs/shots/`: `cockpit_before_1440.png`, `cockpit_before_390.png`,
  `cockpit_after_1440.png`, `cockpit_after_390.png`, `command_1440.png`.

## Assumptions
1. `apar` is a single combined catalog row in the Cockpit ("A/P + A/R management") with no separate A/P and A/R
   line items, unlike Quick Quote which has two rows (`ap` $250/mo, `ar` $250/mo). Cowork's answer said "apar:
   default $500 a month (A/P $250 plus A/R $250, both Quick Quote rows)" — read as: price the one Cockpit row at
   the sum of the two Quick Quote rows ($500), not split it into two rows. Did not split the Cockpit row into
   two, since that would change the catalog array shape and nothing in the brief asked for that.
2. "Before and after total" in the brief is read as the effect of the `apar` row alone on the Cockpit's running
   total when it is the only item checked (a clean, isolated before/after of the one value that changed), rather
   than a full sample-entity quote total like Run BF used for its three-fix comparison — the brief's answer only
   changed this one row, so isolating it avoids conflating it with unrelated catalog values.
3. Treated the lack of any Private Integration token or Email Builder API helper script anywhere on this
   machine's filesystem (no `.env`, no prior push script, no surviving Run AW report) the same way the brief
   treats an API scope refusal: stop Job 1's API portion cleanly, log the exact blocker, and continue with the
   rest of the run rather than halting entirely.
4. `build_command.py` in this run only regenerates `Atlas One COMMAND.html` (not the prospect-facing "Atlas One
   Tools (share with prospects).html"), matching what Run BF's rebuild produced; did not investigate further
   since that file was not part of this brief's scope.

## Skipped
- **Job 1, the Email Builder API work** (pulling the 21 P prospecting templates to
  `_briefs/assets/run-BG-jobs/templates-before/`, grepping them for the stale number, pushing fixes, re-pulling
  to diff): not attempted. No Private Integration token, no `.env`, and no working copy of the push script the
  brief describes Run AW using (`GET /emails/builder`, `POST /emails/builder/data`) exist anywhere in this repo
  or the Master Kit filesystem that this terminal can reach. Also could not locate the Run AW report itself
  (referenced as being in `_to_delete/superseded-2026-09-16/prior-reports/`) to confirm the exact auth setup.
  This is functionally the same stop condition the brief names for a scope error, so Job 1's template work is
  left for the GHL browser terminal to do by hand, same as the brief's own fallback path.
- Did not split the Cockpit `apar` row into two separate A/P and A/R rows (see Assumption 1).
- Did not rebuild the prospect-facing COMMAND output (see Assumption 4) since it was not asked for in this brief.

## Questions for David
1. Job 1's API path needs a working Private Integration token for the GHL Email Builder API (scopes for
   `emails/builder` list and update) accessible to this terminal, or the GHL browser terminal needs to do the
   21-template phone-number fix by hand. Which do you want, and if the former, where should the token live so
   this terminal can find it (an env var, a local file outside the synced Master Kit, etc.)?
2. Should the Run AW report (the one this brief pointed to for the exact API call sequence) be restored from
   wherever it currently lives, so a future GHL-JOBS run can follow it without re-deriving the approach?
