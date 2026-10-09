# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CZ, 2026-10-08): master builds never write into client folders

Installed by A1 GHL Jobs 4 after the Run CY audit (PASS, claude/ghl-jobs-run-CY-audit-2026-10-07.md). Archive Run CY's
report first. Files and code only, never the GHL UI. No questions mid run, no sends, no spending, no deploys, no git push
to main of atlas-one-intake-forms. Log real clock times. Finish with RUN-GHL-JOBS-report.md. RETIRE RULE: overwrite in
place, list replaced files under "Retire".

## Job 1: remove client folders from build manifests
`bookkeeping-docs/build.py` has a standing manifest that writes two Access To Hearing PDFs into
`1. A1 Solutions prospect_Client/3. Quotes_A1/Access To Hearing LLC (Guiden Group)/`. Prospect and client data never
come from a master build. Remove those entries from the manifest so the build writes only master and A1_Sales outputs.
If the Access To Hearing documents need a generator, give the script a separate opt in flag (`--client <folder>`),
off by default.
Then check every other build script under the Master Kit and the intake forms repo (build_command.py, generate.py,
division_sheets_build, render_html_pdfs.py, the SCL builder, BRJ package builder) for any output path under
`1. A1 Solutions prospect_Client`. Remove each one the same way and list them.

## Job 2: guard
Add a catalogue_check guard: fail if any build manifest or output list contains a path under
`1. A1 Solutions prospect_Client`. Run catalogue_check and report the result (the GHL How-To booking link fail is the
GHL lane's and is expected until they fix it; name it, do not edit those files).

## Job 3: prove
Run the bookkeeping build once and show (file list plus mtimes) that nothing under `1. A1 Solutions prospect_Client`
changed. Report every file changed.
