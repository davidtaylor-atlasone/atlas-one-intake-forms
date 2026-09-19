# BRIEF-GHL-JOBS (current run: Run BT, 2026-09-18 14:45). Kill the wrong expiry date in the two offer emails, and make the Audit report write the real one.

Terminal name: GHL-JOBS. Files, code and the GHL REST API only, never the GoHighLevel browser UI. Safe to run
alongside the GHL browser terminal. Build end to end, no questions, log assumptions, questions at the END.
Never fork or background (rule 44). Commit and push after each job. Assets `_briefs/assets/run-BT-jobs/`.
No dashes in any email copy. Log to `TERMINAL-GHL-JOBS-live.md`; report to
`Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md` plus a copy in the assets folder. Prior report already backed
up. Send nothing, spend nothing, delete nothing.

## The problem this run fixes
`audit-offer-day20.html` and `audit-offer-day28.html` both print `{{contact.audit_offer_expires}}`. Run BQ
found this GHL account has no date math (its Date/Time Formatter only formats and compares), so the workflow
now sets that field to the date the workflow runs. A prospect on day 20 would read "your offer expires" next
to the date the offer STARTED. That is worse than a blank, so the merge tag comes out of the emails and the
real date comes from the one place that already computes it correctly, the Audit report.

Decision (Cowork, do not re-ask David): the offer deadline is stated in words in the emails, and as a real
date only in the written Audit report, which already renders "offer good through <report date + 30>".

## Job 1: take the date out of the two offer emails
In `_BUILD-LOG/cadence-emails-2026-09-13/audit-offer-day20.html` and `audit-offer-day28.html`, remove every
`{{contact.audit_offer_expires}}` and rewrite the sentence around it in plain words, keeping David's voice and
the existing structure, CSS, button and signature untouched:
- day 20: the offer from the Audit report holds for ten more days. The number, the three fixes and the price
  in that report stay good until then.
- day 28: two days left on the offer in your Audit report. After that the numbers get rebuilt from current
  rates.
Keep `{{contact.first_name}}`. No dashes. Run the dash check on both files. Render both headless at 390 and
700 wide, look at them, screenshots to the assets folder. Confirm by grep that no
`{{contact.audit_offer_expires}}` remains in either file.

## Job 2: re-push both templates in place
Push the two edited files through the Email Builder API so the LIVE templates change, keeping the same ids
(`A1 | Audit | offer-day20` = 6aad411bb0cd6d0085e3ac07, `A1 | Audit | offer-day28` = 6aad411d173deedb774b43e6):
use the `fill` call (`POST /emails/builder/data`) with the existing templateId, not create. Fetch each
previewUrl back and confirm the date merge tag is gone and the new sentence is there. Do not create a new
template and do not delete the old ones. Update the Subject and any note column in
`_BUILD-LOG/email-templates-map.md` if the row text no longer matches.

## Job 3: the Audit report writes the real expiry to GHL
In `build_audit_report.py` (`08 ROI Quote Master Template/Total_Impact_Model/`), after the report renders, write
the offer expiry to the prospect's GHL contact: `PUT /contacts/{contactId}` with the custom field
`audit_offer_expires` (field id `TGGXt9MICuxqMDk8LNpz`) set to the same date the report prints (report date
plus 30 days), formatted the way the field accepts. Reuse the token loader in `tools/ghl_custom_fields.py`
(`.env`, `GHL_PIT`, never printed). Rules:
- The contact id comes from the prospect JSON (`audit.ghl_contact_id`, add the key to `AUDIT_SCHEMA.md`). If
  it is missing, or the token or the call fails, the report still renders and the script prints one plain line
  for David: "Could not set the offer expiry in GoHighLevel. Open the contact and type <date> into Audit Offer
  Expires." Never fail the report over this.
- Add `--no-ghl` to skip the write, and skip it automatically for the Tell Me More LLC sample so the sample
  never touches a real contact.
Test both paths with a fake contact id (expect the API to refuse) and with `--no-ghl`, and show the printed
fallback line in the report.

## Job 4: keep the sample honest
Re-render the Tell Me More LLC sample audit report and confirm the offer page still reads the right date and
that nothing about the email change broke it. Rebuild COMMAND only if a catalogued file changed; if nothing
catalogued changed, say so rather than rebuilding.

## Report
First line: whether both templates are clean of the date merge tag, and whether the report can write the
expiry. Then per job: what changed, the preview check, screenshots, assumptions, "Questions for David" at
the end.
