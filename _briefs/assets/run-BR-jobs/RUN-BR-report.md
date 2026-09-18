# RUN-GHL-JOBS report: Run BR (2026-09-18)

**CLIENT_TEMPLATE_ID=6aad97b6cbcc9427cbd4f68b** · **CALL_PURPOSE_FIELD_ID=8htKmj1jyx7kJWFwIC4n** ·
**CALL_PURPOSE_KEY=contact.call_purpose** · **PULSE_ADMIN_URL is NOT set** (pulse-admin-url.md does not
exist yet, PORTAL staff pulse run has not shipped it).

Scope: the API half of the audit/client booking follow up decision (decision 1 in
`audit-decisions-2026-09-18.md`). GHL Run BS (browser) wires the new template and field into the booking
workflow and form after this report lands. All four jobs done, zero hard stops, nothing sent, nothing spent,
nothing deleted.

## Job 1: the client email file

Wrote `_BUILD-LOG/cadence-emails-2026-09-13/client-more-we-handle.html`, copying the exact table structure,
inline CSS, header image, button style, footer and signature block from `audit-prep.html` in the same folder
so the two read as one family. Body, in order: "Hi {{contact.first_name}},", "Thanks for booking.", one
paragraph on Atlas One now handling payroll, benefits, insurance, bookkeeping, software and the paperwork in
between under the one relationship, "Nothing you have today moves unless you ask for it.", the button "See
everything Atlas One handles" linking to `https://forms.atlasonesolutions.com/tools/what-we-do/`, then
"Talk soon,\nDavid" and the standard signature block exactly as `audit-prep.html` carries it. Subject
(carried in the map, not the file): "Everything Atlas One handles for you now, {{contact.first_name}}".

Dash check: clean, no em dash, en dash, or hyphen used between spaces anywhere in the file.

Rendered headless at 390 and 700 wide (Playwright/Chromium): `scrollWidth` equals the viewport at both
widths, zero console errors. Screenshots at `_briefs/assets/run-BR-jobs/shots/client-more-we-handle-390.png`
and `-700.png`. Looked at both: the header mark, body copy, periwinkle button and footer signature all render
as expected, no overflow, no clipping.

## Job 2: push it as a template

Ran the create then fill two call sequence against the Email Builder API
(`services.leadconnectorhq.com/emails/builder` then `/emails/builder/data`) with `tools/ghl_email_builder.py`.
Create returned 201 with template id `6aad97b6cbcc9427cbd4f68b`; fill returned 201. Re-listed templates to get
the live `previewUrl`, fetched the rendered HTML back and diffed it against the source file (the same check
Run BO did for the audit prep and offer templates): only GHL's own Outlook/mso-fixes markup was added (a
`<!-- outlook-fixes-applied -->` head comment, `mso-style-textfill-fill-color` inline styles and
`<!--[if mso]>` font-color fallback comments on every link), no content or link differences.

Appended a row to `_BUILD-LOG/email-templates-map.md` under a new heading "## Client booking template (1, Run
BR, pushed through the Email Builder API)" with the same columns the Audit rows use (Send, Workflow, Template
name, Template id, Subject, File). Wrote `_BUILD-LOG/audit-client-template-id.md` with
`CLIENT_TEMPLATE_ID=6aad97b6cbcc9427cbd4f68b` on the first line. Sent nothing.

## Job 3: the call purpose field

Ran `python3 tools/ghl_custom_fields.py list` first: no contact field named "Call purpose" or keyed
`contact.call_purpose` existed. Extended `create_field` in `tools/ghl_custom_fields.py` with an optional
`options` argument (API body key `options`, a list of strings). Created the field: name "Call purpose",
dataType `SINGLE_OPTIONS`, model `contact`, parent folder `AmY51esJO2QF0v3wvODu` (the Audit Code folder, the
brief's preferred parent). The API accepted the parent on the first try (201), no fallback needed. Options,
written exactly as specified: "My Back Office Audit", "I am already a client", "Something else". Result: id
`8htKmj1jyx7kJWFwIC4n`, key `contact.call_purpose`.

Listed fields again and read the field back by its key: name, dataType, parentId and all three picklist
options matched what was created. Appended `CALL_PURPOSE_FIELD_ID=8htKmj1jyx7kJWFwIC4n` and
`CALL_PURPOSE_KEY=contact.call_purpose` to `audit-client-template-id.md`. Created no other field; confirmed
`audit_code`, `audit_offer_expires`, `wc_policy_expiration` and `benefits_renewal_date` all already existed
from prior runs and were left untouched.

## Job 4: the 90 day pulse task text

Checked for `_BUILD-LOG/pulse-admin-url.md`: it does not exist. Appended `PULSE_ADMIN_URL=` (empty) to
`audit-client-template-id.md` per the brief's fallback instruction. No build performed, per the brief (this
job is a check, not a build, when the file is missing).

## Assumptions

1. **"Thanks for booking. Talk soon." bullet split across the opening and closing lines.** The brief lists
   "Thanks for booking. Talk soon." as one bullet, but `audit-prep.html`'s pattern (which the brief says to
   copy the structure of) opens with "Thanks for booking. [content]" and closes "Talk soon,\nDavid". Read
   "Thanks for booking." as the second line of the body and "Talk soon," as the closing salutation before the
   signature, matching `audit-prep.html` exactly rather than placing both sentences together as one paragraph.
2. **PULSE_ADMIN_URL not set.** The PORTAL staff pulse run has not shipped `pulse-admin-url.md` yet (decision
   2 in `audit-decisions-2026-09-18.md` names it as a separate chat/run). Left the line empty as instructed
   rather than guessing a URL.
3. **Call purpose field parent folder.** Used `AmY51esJO2QF0v3wvODu` as instructed; the API accepted it on the
   first call, so no fallback to a parentless field was needed.

## Questions for David

1. None blocking. If the "Thanks for booking. Talk soon." wording (Assumption 1) is not what you meant, say
   so and Job 1 gets a one line edit before the next push.
