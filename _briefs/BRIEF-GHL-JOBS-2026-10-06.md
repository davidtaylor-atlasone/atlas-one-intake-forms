# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CW, 2026-10-06): no annual plans, Run CU follow ups

Installed by A1 GHL Jobs 4 after the Run CU audit (PASS, claude/ghl-jobs-run-CU-audit-2026-10-04.md). Archive Run CU's
report first. Files and code only, never the GHL UI. No questions mid run, no sends, no spending, no deploys, no git push
to main of atlas-one-intake-forms. No dashes in anything a client, prospect or BRJ reads. Log real clock times. Finish
with RUN-GHL-JOBS-report.md.
RETIRE RULE (new, 2026-10-03): never move old files into a `_to_delete` folder. Overwrite in place, and list every file
you replaced or that should go under a heading "Retire" in the report. Cowork deletes them after the audit.

## Job 1: annual plans are OFF (David, 2026-10-06: "Annual plans, two months free: no")
Remove every annual plan offer from every client, rep and BRJ piece: "two months free", "annual plans get two months
free", "15% off" annual, "setup waived on annual", "waived on an annual plan", "pay annually". Enterprise setup now
reads "$995, often waived" (same as Professional's wording). Sources first: prices.json (set Enterprise setup text,
add a changelog line "2026-10-06 annual plans removed, David"), the membership brochure and comparison sheet
generators, Price List template, Membership Schedule and generate.py, Quick Quote, Quote Cockpit, Micah menu, the AI
Email demo deck, the Service Content Library, the BRJ pricing page copy, the agreement masters. Add retired phrases to
the catalogue_check price guard so they can never come back. Regenerate everything from the sources and rebuild the
BRJ package with today's date.

## Job 2: stop the builder making _to_delete folders
build_command.py (rep kits) and any other script that backs up into `_to_delete` or `superseded-*`: remove that
behaviour. A rebuild overwrites in place; the report lists replaced files under "Retire". Add a guard that fails if a
build creates a folder named `_to_delete` or `superseded-*` anywhere under the Marketing root.

## Job 3: small follow ups from the Run CU audit
1. Quick Quote year end W-2 line: "Year-end W-2s (one extra payroll run at your rate, monthly minimum applies)".
2. David's own masters: replace Utah and Draper examples with [City] and [state] (Prospecting Playbook scripts, the
   "Utah names" time zone block, Overlay 04 "Utah software teams", the census template Provo row). Clients are
   national. Lehi stays only as the company address line.
3. Keep "Comp and commission plan design" as a client service name; add it to the rep pay guard allow list.

## Job 4: rebuild and prove
Rebuild COMMAND, the shared Sales Kit and `--person charity` (re zip her kit); all guards green; Chromium and WebKit at
1440 and 390, zero console errors; grep proof of zero annual plan phrases across A1_Sales, the Master Kit outputs and
her zip. Report every file changed and the Retire list.
