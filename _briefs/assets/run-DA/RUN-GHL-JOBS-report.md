# RUN-GHL-JOBS-report, Run DA, 2026-10-09

Run CZ's report is archived at `_BUILD-LOG/RUN-GHL-JOBS-report-runCZ-done-2026-10-09.md` (copied, original not deleted). Brief copy: repo `_briefs/BRIEF-GHL-JOBS-2026-10-09.md`. Evidence: repo `_briefs/assets/run-DA/` (shots, this report).

## Built
1. Job 1: catalogue row `business-cards-folder` now points at `A1_Sales/Blog and Content/Business Cards/` (`_INTERNAL (do not share)/catalogue.py`). hubs.py carries only the row id and blurb, no path, so no change there.
2. Also repointed the QR plan entry in `render_md_pages.py` (it named the old `A1_Sales/Business Cards/QR-plan-2026-09-26.md`).
3. `catalogue_check.py`: OK, 216 entries, all 27 checks passed.
4. Rebuilt COMMAND: `<title>` stamp "Atlas One COMMAND: build Oct 9, 2026 6:28 PM" (new). Sales Kit rebuilt, 62 items (`A1_Sales/Atlas One Sales Kit.html`, rewritten 18:28).

## Looked at
- Chromium headless, COMMAND and Sales Kit at 1440 and 390: scrollWidth equals viewport at both widths, 0 console errors, 0 network requests beyond file/data. Shots in `_briefs/assets/run-DA/shots/`.
- Business Cards card in COMMAND: href is `../../A1_Sales/Blog%20and%20Content/Business%20Cards`, which resolves to the existing folder (contains charity, david, david-wsa, HOW TO SHARE MY CARD.txt, QR-plan, Text-my-card.txt). I checked the href resolves, I did not click through in a file browser.
- Sales Kit has no Business Cards card (internal only), so nothing to open there.

## Service Content Library check (Run CZ answer)
Unpacked `service-content-library-src-2026-09-30.tgz` to a temp folder. `build.py` reads `catalogue.json` and `qq.json` and writes only to `out/` relative to its working directory (json, ts, md, csv, html). No reference to `1. A1 Solutions prospect_Client` anywhere. Result: writes nothing under the client folder.

## Assumptions
1. "Archive Run CZ's report" done as a copy; the old file is overwritten by this report.
2. Copying the brief to `_briefs/BRIEF-GHL-JOBS-2026-10-09.md` overwrote the Run CZ brief copy of the same date name (untracked, identical purpose).
3. `screenshare_manifest.json` and `rendered_md_manifest.json` still list old `A1_Sales/Business Cards/...` source paths; they are generated, left untouched. Not part of this brief.
4. Committed on the current branch `ghl-jobs-run-cw`, not main, per "no push to main".

## Skipped
- Access To Hearing documents (told not to regenerate). BRJ package (no script, nothing to check).
- `Atlas One Tools (share with prospects).html` is not written by the current build_command (not present in the Master Kit); noted, not investigated.

## Retire
None.

## Questions for David
1. Should the generated manifests (screenshare_manifest.json, rendered_md_manifest.json) get the new Business Cards path via a regeneration run?
2. CLAUDE.md names `Atlas One Tools (share with prospects).html` as a COMMAND output, but the build no longer produces it. Retired, or a regression?
