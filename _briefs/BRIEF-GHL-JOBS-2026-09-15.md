# BRIEF for the GHL-JOBS terminal: Run AV (push every cadence email into GHL as a template, through the API)

Terminal name: GHL-JOBS. Files, code, API and headless Chromium only. Never the GoHighLevel browser. Build end
to end, no questions, permission prompts answered by you, assumptions logged, questions at the END of the
report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; report `_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted
heredoc). Back up the prior report to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAU.md`.
Commit and push. Clients are in all 50 states.

## Why
GHL's workflow Quick Compose editor rewrites pasted HTML: Cowork read a delivered test of Email-1 on
2026-09-15 and it arrived with every paragraph forced to Verdana 16px, the logo images stripped and the link
colour gone. Marketing > Emails > Templates keeps HTML intact, and workflows can send a template instead of
Quick Compose. So every cadence file becomes a template, created through the Email Builder API, and the GHL
terminal only switches each Send Email action to the template (its brief already says how).

## Job 0: scopes check (do this first, stop cleanly if it fails)
The Private Integration "Atlas One apps" (token in `~/Projects/atlas-one-portal/.env`,
`GHL_PRIVATE_INTEGRATION_TOKEN`, location `AzTPxnK2vSUj19jYoDmR`) needs `emails/builder.readonly` and
`emails/builder.write`. Call `GET https://services.leadconnectorhq.com/emails/builder?locationId=...` with
`Version: 2021-07-28`. If it returns 401 or a scope error, write the report with "David: add the two email
builder scopes" at the top (click path: Settings > Integrations > Private Integrations > Atlas One apps > Edit
> Scopes > search "builder" > tick both > Update; the token does not rotate on a scope change, proven in Run
AV) and end the run. Never print the token.

## Job 1: push the templates
Source: every `.html` in `_BUILD-LOG/cadence-emails-2026-09-13/` that is a FULL file (skip the PLACEHOLDER
files listed in INDEX.md: 45-b, 45-c, construction-audit, email-3, email-4, ye-2, ye-4; and skip the three
internal-* files, which the GHL terminal pastes by hand). Before pushing, confirm each file contains
"380-225-5217", no "385-213", no `{{contact.company_name}}`, and no dashes in copy.
For each file: create one template named `A1 | <Send> | <file stem>` (Send from INDEX.md, for example
`A1 | Email-1 | email-1`), type HTML, body = the file verbatim, subject = the INDEX.md subject where one is
given. Use the Email Builder API (`POST /emails/builder`, then `GET` to confirm). If the API rejects raw
HTML templates, say exactly what it returned and stop after the first failure; do not paste in a browser.
Write `_BUILD-LOG/email-templates-map.md`: one row per template: Send, workflow (from INDEX.md), template
name, template id, subject, file. Also write it as `email-templates-map.json` for the portal build.

## Job 2: proof
Fetch two of the created templates back through the API and diff their HTML against the source files (must
be byte-identical apart from whitespace). Render one fetched template at 600px in headless Chromium and look
at it (logo present, DM Sans, periwinkle button, 380 phone). Screenshots in `_briefs/assets/run-AV/shots/`.

## Report
Built (template count, map path), Verification (diffs, screenshot), Assumptions, Skipped (the placeholders
and internal files, by name), Questions for David.
