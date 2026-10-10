# BRIEF-GHL-JOBS (current run: GHL-JOBS Run DA, 2026-10-09): business cards path, then idle

Installed by A1 GHL Jobs 4 after the Run CZ audit (PASS, claude/ghl-jobs-run-CZ-audit-2026-10-09.md). Archive Run CZ's
report first. Files and code only. No questions mid run, no sends, no deploys, no git push to main. Log real clock
times. Finish with RUN-GHL-JOBS-report.md.

## Job 1: business cards row
The Business Cards folder now lives at `A1_Sales/Blog and Content/Business Cards/` (moved by another lane). Point the
catalogue row `business-cards-folder` at that path in catalogue.py (and hubs.py if it carries the path). Rebuild
COMMAND and the Sales Kit. catalogue_check must be 27 of 27 green.

## Answers to Run CZ questions (no work)
- The Service Content Library has no standalone builder; its source lives in
  `14 Service Content Library/service-content-library-src-2026-09-30.tgz`. Unpack to a temp folder and confirm its
  build script writes nothing under `1. A1 Solutions prospect_Client`. Report the result.
- The BRJ package has no script; terminals assemble it by hand each run. Nothing to check.
- Access To Hearing documents: do NOT regenerate them. The operator lane does client documents.

## Job 2: prove
COMMAND and Sales Kit render clean in Chromium at 1440 and 390, the Business Cards card opens the folder.
