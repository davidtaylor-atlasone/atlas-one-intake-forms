# BRIEF for the GHL-JOBS terminal: Run BN (two more portal fields, Azure Blob container, two portal email templates)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Never
fork, background or delegate to a sub agent (rule 44). Do only the jobs written here. Commit and push. Repo
assets in `_briefs/assets/run-BN-jobs/`. No dashes in copy. Log to `TERMINAL-GHL-JOBS-live.md`; report to
`Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted heredoc) AND a copy in the repo assets folder.
Prior report already backed up (`_to_delete/superseded-2026-09-18/prior-reports/RUN-GHL-JOBS-report-RunBM.md`).

Token: `GHL_PIT` in `~/Projects/atlas-one-intake-forms/.env`. Never print or log it, never look in
`~/.claude.json`. Location `AzTPxnK2vSUj19jYoDmR`, `Version: 2021-07-28`, browser User-Agent. Reuse
`tools/ghl_custom_fields.py` and `tools/ghl_email_builder.py`. Master Kit by name; A1_Sales is `$MK/../../A1_Sales`.

## Job 1: two more contact fields (PORTAL Run P3 asked for them)
Same as Run BM Job 1: read first, then create Contact fields type LARGE_TEXT named "Portal Documents"
(key `portal_documents`) and "Portal Messages" (key `portal_messages`) in folder `AmY51esJO2QF0v3wvODu`.
Append `GHL_FIELD_PORTAL_DOCUMENTS=<id>` and `GHL_FIELD_PORTAL_MESSAGES=<id>` to
`~/Projects/atlas-one-portal/.env` (confirm the names in `server/fields.ts` or `server/env.ts` first). Append
the two lines to `_BUILD-LOG/portal-env-additions-2026-09-18.md` under a "Run BN" heading (David adds them in
Azure by hand, same steps as before).

## Job 2: Azure Blob container for portal uploads (no new spend)
Run `az account show` (if not logged in, stop this job, write "needs az login" and continue with Job 3).
`az storage account list --resource-group atlas-one-ai-email-assistant-v2` (and, if empty, across the
subscription). If a storage account already exists in that resource group, create container `portal-docs`
in it (`az storage container create`, private access), fetch its connection string with
`az storage account show-connection-string` and append `AZURE_STORAGE_CONNECTION=<string>` to the portal
`.env` ONLY (never into the report, log, git or OneDrive). Add the line name (not the value) to
`portal-env-additions-2026-09-18.md` with "value: copy from the portal .env on the Mac Studio, or Azure
Portal, storage account, Access keys". If NO storage account exists, create nothing (a new account is new
spend) and write in the report exactly which resource groups and accounts you saw.

## Job 3: two portal email templates pushed to GHL (Email Builder API, as Run AW and BK)
Build two HTML emails in `_BUILD-LOG/cadence-emails-2026-09-13/` using the same wrapper, logo, DM Sans,
button and signature as `internal-new-intake.html` and the client welcome template (read
`email-templates-map.md` for the welcome template's file and the push sequence). No dashes.
a. `portal-doc-ready.html`, template name `A1 | Portal | doc-ready`, to the client. Subject "A new document is
   waiting in your portal". Body: "Hi {{contact.first_name}}, David added a document to your Atlas One
   portal. Sign in and open Documents to view or download it." Button "Open my portal" to
   https://portal.atlasonesolutions.com/ . One line under: "Questions? Reply to this email or call
   380-CALL-A1S (380-225-5217)." Standard signature.
b. `internal-doc-uploaded.html`, template name `A1 | Internal | doc-uploaded`, to David. Subject
   "Portal upload: {{contact.name}}". Body table: Client {{contact.name}} ({{contact.company_name}} if it
   resolves in this account; Run BD found which keys resolve, read RUN-GHL-report history in BRIEF-GHL.md
   if unsure and use only keys proven to resolve), Email {{contact.email}}, then "Open the contact" link to
   https://app.ridethehightide.com/v2/location/AzTPxnK2vSUj19jYoDmR/contacts/detail/{{contact.id}} and
   "Open the portal admin" link to https://portal.atlasonesolutions.com/admin . Line: "The file and folder
   are in the contact's notes."
Push both with `POST /emails/builder/data` (create first with `POST /emails/builder`), fetch back, diff, save
before and after copies in the repo assets folder, add both rows to `email-templates-map.md`. Send nothing.
Report the two template ids; the GHL terminal wires them into workflows.

## Report
Field ids, container result, template ids, env names written, assumptions, "Questions for David" at the end.
