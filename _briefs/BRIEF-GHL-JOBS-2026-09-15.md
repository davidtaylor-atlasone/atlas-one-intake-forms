# BRIEF for the GHL-JOBS terminal: Run AW (push every cadence email into GHL as a template, the way Run G did it)

Terminal name: GHL-JOBS. Files, code, API and headless Chromium only. Never the GoHighLevel browser. Build end
to end, no questions, permission prompts answered by you, assumptions logged, questions at the END of the
report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; report `_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted
heredoc). Back up the prior report to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAV.md`.
Commit and push. Clients are in all 50 states. Never print the token.

## What Run AV missed (read this before anything else)
Run AV concluded the Email Builder API cannot write a template body. It can. On 2026-09-08 this same token
created 21 named templates (P-A-3, P-B-1 ... P-W7-3, ids in `_briefs/prospecting-workflows-W1-W7-REPORT.md`,
"Checkpoint 2") with a two-call sequence Run AV never tried:

1. Create: `POST https://services.leadconnectorhq.com/emails/builder`
   headers `Authorization: Bearer <token>`, `Version: 2021-07-28`, `Content-Type: application/json`
   body `{"locationId":"AzTPxnK2vSUj19jYoDmR","type":"html","title":"A1 | Email-1 | email-1","updatedBy":"atlas-one-apps"}`
   The name field is `title`, not `name`. Response carries the new template id.
2. Fill: `POST https://services.leadconnectorhq.com/emails/builder/data`
   body `{"locationId":"AzTPxnK2vSUj19jYoDmR","templateId":"<id from step 1>","updatedBy":"atlas-one-apps","editorType":"html","html":"<the file, verbatim>","dnd":{},"previewText":""}`
   Then `GET /emails/builder?locationId=...` and fetch the template's `previewUrl` to confirm the body landed.

Job 0: prove the sequence on ONE file (email-1.html) before touching the rest: create, fill, fetch back,
diff against the source. If step 2 returns 401 or 4xx, record the exact status and body, try the field
name `html` and then `editorContent` once each, and if both fail stop cleanly with the two responses at the
top of the report. Do not probe anything else and do not create more empty shells.

Templates carry no subject; the subject is set on each workflow's Send Email action (the GHL terminal does
that from the map). So the map's Subject column is for the GHL terminal, taken from INDEX.md.

## Job 1: push the templates
Source: every `.html` in `_BUILD-LOG/cadence-emails-2026-09-13/` that is a FULL file (skip the PLACEHOLDER
files listed in INDEX.md: 45-b, 45-c, construction-audit, email-3, email-4, ye-2, ye-4; and skip the three
internal-* files, which the GHL terminal pastes by hand). Run AV already verified the 35 candidates: each
contains "380-225-5217", no "385-213", no `{{contact.company_name}}` in the body, no dashes. Re-run that
check anyway (files may have changed) and push all 35 with the two-call sequence above, named
`A1 | <Send> | <file stem>` (Send from INDEX.md). Write `_BUILD-LOG/email-templates-map.md`: one row per
template: Send, workflow (from INDEX.md), template name, template id, subject (from INDEX.md), file. Also
write `email-templates-map.json` (same rows) for the portal build. Include the 21 P- templates from the
2026-09-08 report in a second table so the GHL terminal has every template id in one place.

## Job 2: proof
Fetch three of the created templates back through their previewUrl and diff against the source files (must
be identical apart from whitespace). Render one at 600px in headless Chromium and look at it (logo present,
DM Sans, periwinkle button, 380 phone). Screenshots in `_briefs/assets/run-AW/shots/`.

## Cleanup note
Run AV left four empty templates named "New Template" (ids 6aa9c57694dd617868466523, 6aa9c5b9e686ab50486928b1,
6aa9c5ef3029d837f98f9666, 6aa9c6179ed784b5df8c1a95). Try `DELETE /emails/builder/AzTPxnK2vSUj19jYoDmR/<id>`
once each; if the sandbox blocks it, list them under Questions and move on. David can delete them in
Marketing > Emails > Templates.

## Report
Built (template count, map path), Verification (diffs, screenshot), Assumptions, Skipped (the placeholders
and internal files, by name), Questions for David.
