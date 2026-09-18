# BRIEF for the GHL-JOBS terminal: Run BP (wire the audit intake form into the landing page). RUN ONLY AFTER GHL Run BP reports (it writes `_BUILD-LOG/audit-form-id.md`).

Terminal name: GHL-JOBS. Files and code only. Build end to end, no questions, log assumptions, questions at
the END. Never fork or background (rule 44). Commit and push. Repo assets in `_briefs/assets/run-BP-jobs/`.
No dashes. Log to `TERMINAL-GHL-JOBS-live.md`; report to `Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md`
plus a copy in the assets folder. Prior report already backed up.

Before starting: read `_BUILD-LOG/audit-form-id.md`. If it is missing or `AUDIT_FORM_ID=` is empty, stop and
write "waiting on GHL Run BP" as the report.

## Job 1: fill the constant
In `~/Projects/atlas-one-intake-forms/audit/index.html` set `const AUDIT_FORM_ID = "<id from the file>"`.
Verify headless at 390 and 1440 that the fallback line is hidden, the iframe to
`https://api.leadconnectorhq.com/widget/form/<id>` renders (the form's own fields visible in the
screenshot), `?audit_code=TEST-JOBS` on the page URL is passed through to the iframe URL, zero console
errors, no horizontal scroll at 390. Screenshots to the assets folder. Commit and push. Confirm the live URL
returns 200 and contains the id (curl, allow a few minutes for Pages).

## Job 2: the audit link in the catalogue
Add a catalogue row in `_INTERNAL (do not share)/catalogue.py` (Sales Kit, Start here, audience prospect,
kind link): "Audit intake page (public)", blurb "Send a prospect here before the Audit call: four documents,
five minutes. The prep email sends it automatically after they book the Audit calendar.", path the live
URL. Rebuild COMMAND and the Sales Kit (`python3 build_command.py "$MK"`), `catalogue_check.py` OK, stamps
today.

## Report
The id used, the screenshots, live URL check, COMMAND stamp, assumptions, "Questions for David" at the end.
