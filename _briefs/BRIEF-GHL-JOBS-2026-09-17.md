# BRIEF for the GHL-JOBS terminal: Run BG (stale phone in the P prospecting templates, apar default)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the
prior report to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBF.md` (already copied;
overwrite is fine). Back up every file before editing. Commit and push. Repo assets in `_briefs/assets/run-BG-jobs/`.
No dashes in copy.

Answers to Run BF's questions (Cowork, 2026-09-17 08:15):
1. `apar`: default $500 a month (A/P $250 plus A/R $250, both Quick Quote rows), editable. Fix it, rerun
   build_cockpit.py, note the before and after total.
2. Bookkeeping anchors stay as they are; the AI Task Agent standalone figure stays out of the Cockpit; Quick
   Quote stays hand maintained. All three closed.

## Job 1: the 385 number is still in the P prospecting email templates
GHL Run BG (read only) found the P-C-2 and P-C-3 templates ("Inbound Email 2" and "Inbound Email 3", used by
"W1 Inbound speed to lead") still carry 385-213-7177 in the footer. Rule: Atlas One material carries
380-225-5217 only. Using the Email Builder API the way Run AW pushed templates (`GET /emails/builder` to list,
`POST /emails/builder/data` to update; the Private Integration token and scopes are already in place, see
`_BUILD-LOG/email-templates-map.md` and the Run AW report in `_to_delete/superseded-2026-09-16/prior-reports/`):
1. Pull every template whose name starts with `A1 | P-` (the 21 P prospecting templates in the map's second
   table) plus any other template in the account; save each template's HTML to
   `_briefs/assets/run-BG-jobs/templates-before/<name>.html`.
2. Grep them all for `385-213-7177`, `385.213.7177`, `(385) 213-7177`, `+13852137177`, `385` near "call". List
   every hit by template name.
3. For each hit, replace with 380-225-5217 (and `tel:+13802255217` in any tel link), keep everything else byte
   for byte, push the update, re-pull and diff to confirm only the phone changed. Never touch a template with
   no hit. Do not send anything.
4. Also grep `_BUILD-LOG/cadence-emails-2026-09-13/` and the repo's `_briefs/assets/` email HTML files for the
   same strings; fix any live cadence file (not the historical run assets) and say which.
5. Report the table: template name, id, hits before, hits after, updated yes or no.
If the API refuses (scope error), stop Job 1 cleanly, write the exact error and the exact scope name to add,
and continue with Job 2; the GHL browser terminal will do the edits by hand in that case.

## Job 2: apar default and rebuild
Set `apar` to $500 a month as above. Rerun build_cockpit.py, verify as in Run BF (before and after totals, zero
console errors, no external requests, 1440 and 390, PPTX export). catalogue_check.py, rebuild COMMAND, stamp.

## Report
Built, Verification, Assumptions, Skipped, Questions.
