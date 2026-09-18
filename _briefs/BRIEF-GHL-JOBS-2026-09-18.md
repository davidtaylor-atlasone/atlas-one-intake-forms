# BRIEF-GHL-JOBS (current run: Run BR, 2026-09-18 13:55). Audit booking follow up, the API half: one client email template, one custom field. GHL Run BS (browser) wires them after this reports.

Terminal name: GHL-JOBS. Files, code and the GHL REST API only, never the GoHighLevel browser UI. Safe to run
while the GHL terminal is on Run BQ (different terminal, no browser). Build end to end, no questions, log
assumptions, questions at the END. Never fork or background (rule 44). Commit and push after each job. Repo
assets in `_briefs/assets/run-BR-jobs/`. No dashes anywhere in email copy. Log to `TERMINAL-GHL-JOBS-live.md`;
report to `Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md` plus a copy in the assets folder. Prior report already
backed up. Send nothing, spend nothing, delete nothing.

Why: current clients book the same 30 minute calendar as Audit prospects. David decided (2026-09-18, see
`_BUILD-LOG/audit-decisions-2026-09-18.md` decision 1): a booking question routes the email. The audit answer
gets `A1 | Audit | prep` (exists, 6aad411ab397941922a158c5). The client answer, or the tag `client-current`,
gets a short "here is everything else Atlas One handles now" email. That email and the field the booking
question writes to are built here by API so the browser run only has to click them into place.

## Job 1: the client email file
Write `_BUILD-LOG/cadence-emails-2026-09-13/client-more-we-handle.html`. Copy the exact table structure,
inline CSS, header, button style, footer and signature block from `audit-prep.html` in the same folder so the
two read as one family. Copy, plain and short, no dashes, no vendor names, David's voice:
- "Hi {{contact.first_name}},"
- "Thanks for booking. Talk soon."
- One short paragraph: Atlas One now handles payroll, benefits, insurance, bookkeeping, software and the
  paperwork in between, all under the one relationship you already have with us. One call, one bill, one
  person who knows your business.
- One line: "Nothing you have today moves unless you ask for it."
- Button "See everything Atlas One handles" to https://forms.atlasonesolutions.com/tools/what-we-do/
- The standard signature exactly as audit-prep.html carries it.
Subject (goes in the map, not the file): "Everything Atlas One handles for you now, {{contact.first_name}}"
Render it headless at 390 and 700 wide, look at it, no horizontal scroll, screenshots to the assets folder.
Run the dash check over the file (em dash, en dash, or a hyphen used between spaces all fail).

## Job 2: push it as a template
`python3 tools/ghl_email_builder.py` create then fill (the two call sequence in that file's docstring):
title `A1 | Client | more we handle`, editorType html, the file's full HTML. Fetch the previewUrl back and
diff its body against the file (the same check Run BO did). Append one row to
`_BUILD-LOG/email-templates-map.md` under a new heading
"## Client booking template (1, Run BR, pushed through the Email Builder API)" with the same columns as the
Audit rows (Send, Workflow, Template name, Template id, Subject, File). Write
`_BUILD-LOG/audit-client-template-id.md` containing exactly `CLIENT_TEMPLATE_ID=<id>` on the first line.

## Job 3: the call purpose field
`python3 tools/ghl_custom_fields.py list` first. If a contact field named "Call purpose" (key
`contact.call_purpose`) already exists, use it and skip creation. Otherwise extend `create_field` in
`tools/ghl_custom_fields.py` with an optional `options` argument (the API body key is `options`, a list of
strings) and create: name "Call purpose", dataType SINGLE_OPTIONS, model contact, parent folder
`AmY51esJO2QF0v3wvODu` (the folder Audit Code lives in; if the API rejects that parent, create without it and
say so), options exactly: `My Back Office Audit`, `I am already a client`, `Something else`. List again and
read the field back. Append `CALL_PURPOSE_FIELD_ID=<id>` and `CALL_PURPOSE_KEY=<key>` as two more lines to
`_BUILD-LOG/audit-client-template-id.md`. Create no other field: `audit_code`, `audit_offer_expires`,
`wc_policy_expiration` and `benefits_renewal_date` all already exist.

## Job 4: the 90 day pulse task text
Check whether `_BUILD-LOG/pulse-admin-url.md` exists (the PORTAL staff pulse run writes it). If it does,
append `PULSE_ADMIN_URL=<url>` to `audit-client-template-id.md`; if not, append `PULSE_ADMIN_URL=` (empty)
and note "PORTAL pulse not shipped yet" under Assumptions. No build either way.

## Report
First line: the three ids (template id, field id, field key) and whether PULSE_ADMIN_URL is set. Then per job:
what was done, the preview diff result, screenshots, assumptions, "Questions for David" at the end.

---- Last run (BP), kept for reference ----
Run BP (done 2026-09-18 09:59, audited): Job 1 filled AUDIT_FORM_ID (pUCVA3wZgAOMMVnZsb4c) into
`audit/index.html`, verified headless, live URL 200. Job 2 added the "Audit intake page (public)" catalogue
row and rebuilt COMMAND (199 items) and the Sales Kit (57 items).
