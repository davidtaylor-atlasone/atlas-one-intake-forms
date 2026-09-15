# RUN-GHL-JOBS report: Run AW (push cadence emails into GHL as templates, corrected sequence)

Full brief completed end to end: Job 0 (prove the sequence), Job 1 (push all 35 templates),
Job 2 (proof: diff and render), plus the cleanup note. Prior report backed up to
`_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAV.md` before this one
was written.

## Built

- **35 new email templates** created in GHL's Email Builder via the two-call sequence
  (`POST /emails/builder` then `POST /emails/builder/data`), named `A1 | <Send> | <file stem>`.
  Full map: `_BUILD-LOG/email-templates-map.md` and `email-templates-map.json` (also copied to
  `_briefs/assets/run-AW/` in the forms repo). The map's second table lists all 21 P- templates
  from the 2026-09-08 run (`prospecting-workflows-W1-W7-REPORT.md`, Checkpoint 2) so every
  template id lives in one document.
- Cleaned up the 4 empty "New Template" shells Run AV left behind, plus 1 test shell this run
  created while proving Job 0 (`A1 | TEST-JOB0 | email-1`) -- all 5 deleted via
  `DELETE /emails/builder/{locationId}/{id}`, which this session's sandbox allowed (unlike Run
  AV's, which was blocked). Run AV's report listed these as needing manual deletion; that is
  now done.

## What Run AV got wrong

Run AV concluded the write scope only creates an empty shell and that no endpoint sets a
template's name, subject, or body. That conclusion was based on omitting the `title` field
(it tried `name`) on the create call and never calling the separate `/emails/builder/data`
fill endpoint documented in this brief. The two-call sequence this brief specifies works
exactly as described: create with `title`, then a second call to `/emails/builder/data` with
the HTML, both returning 201.

## Job 0 (prove the sequence on email-1.html)

`POST /emails/builder` with `{locationId, type:"html", title:"A1 | TEST-JOB0 | email-1",
updatedBy:"atlas-one-apps"}` -> **201**, returned template id. `POST /emails/builder/data`
with `{locationId, templateId, updatedBy, editorType:"html", html:<file>, dnd:{},
previewText:""}` -> **201**, returned a real `previewUrl`. Fetched the `previewUrl` and
diffed against `email-1.html` (whitespace-insensitive): identical except GHL added
`<!--outlook-fixes-applied-->` and `<!--[if mso]>...<![endif]-->` Outlook-safety comment
wrappers around every link (benign, server-added, does not change rendered output). Deleted
this test template after Job 1 confirmed the pattern (see Cleanup above).

## Job 1 (push all 35)

Source file check re-run per the brief (files may have changed since Run AV's pass):
`_BUILD-LOG/cadence-emails-2026-09-13/` has 44 `.html` files. Excluding the 7 placeholders
(`45-b.html`, `45-c.html`, `construction-audit.html`, `email-3.html` [does not exist],
`email-4.html`, `ye-2.html`, `ye-4.html`) and the 3 `internal-*.html` files leaves the same
**35 full-body files**. All 35 re-checked and all pass:
- Contain `380-225-5217`: 35/35
- Contain the wrong `385-213...` number: 0/35
- Contain `{{contact.company_name}}` in the body: 0/35
- Contain an em dash or en dash: 0/35

All 35 pushed with the two-call sequence, both calls 201 for every file. Template ids in
`_BUILD-LOG/email-templates-map.md`.

## Job 2 (proof)

Fetched 3 created templates back through their `previewUrl` and diffed against source
(`bq-1.html`, `booking-c1.html`, `won-email-7-checklist.html`): all 3 identical apart from
the same benign Outlook-safety comment wrappers Job 0 found. Rendered `booking-c1`'s pushed
preview in headless Chromium at 600px and 390px: `scrollWidth` equals the viewport at both
sizes, zero console errors, only `file://` network activity (the fetched preview HTML has no
external requests beyond the embedded Google Cloud Storage image, which is present in every
source file already, not introduced by the push). Logo present, DM Sans font, periwinkle
button, 380 phone number all visible in the screenshot. Screenshots:
`_briefs/assets/run-AW/shots/booking-c1-600px.png`, `booking-c1-390px.png`.

## Assumptions

1. Named every template `A1 | <Send> | <file stem>` (the brief's exact format), using the
   file stem to disambiguate cases where two Sends share a similar label across different
   workflows (for example "Email-1" in Post-Presentation Email vs. "Email 1" in Intake:
   Instant reply) rather than the Send text alone, since Send text alone would collide.
2. Treated the fill call's `html` field as correct on the first try since Job 0 returned 201
   with a real `previewUrl` and the diff came back clean; did not need to try
   `editorContent` as a fallback (the brief only asked for that if the first field failed).
3. Deleted the 4 stale shells from Run AV and the 1 test shell from this run's Job 0 since
   the brief explicitly names this as a job ("Try DELETE ... once each") and this session's
   sandbox permitted the DELETE calls, unlike Run AV's. Not a hard-stop deletion (that rule
   covers repo/local files, not authorized GHL API cleanup the brief itself requested).
4. Subjects in the map come straight from `INDEX.md` text, matched by file stem; the map
   states plainly that subjects are not stored on the template and must be set on each
   workflow's Send Email action by the GHL terminal.
5. Left the 21 P- templates from 2026-09-08 untouched; only copied their ids into the map's
   second table for reference, per the brief.

## Skipped (per brief, correctly excluded)

- 7 placeholder files: `45-b.html`, `45-c.html`, `construction-audit.html`, `email-3.html`
  (does not exist), `email-4.html`, `ye-2.html`, `ye-4.html` -- these keep their current live
  GHL body; the GHL terminal edits the wrapper by hand around the existing body.
- 3 internal notification files: `internal-new-booking.html`, `internal-cancelled.html`,
  `internal-rescheduled.html` -- the GHL terminal pastes these by hand.

## Questions for David

1. **Subjects are not set yet.** The 35 templates carry no subject (confirmed: the Email
   Builder API's create/fill calls have no subject field). Terminal A needs to set each
   workflow's Send Email action subject from the map's Subject column when it wires these
   templates into workflows.
2. Should the 21 P- templates from 2026-09-08 also get a consolidated map entry updated in
   this same file going forward, or should their map stay in the original prospecting report?
   Kept them as a reference-only second table this run; easy to change.
