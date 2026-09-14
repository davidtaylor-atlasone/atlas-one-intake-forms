# BRIEF-GHL-JOBS (current run: Run AQ): finish Run AO. Cowork 2026-09-14 14:45.

Rules as always (no questions, live log TERMINAL-GHL-JOBS-live.md, report RUN-GHL-JOBS-report.md via quoted
heredoc, commit and push, never delete OneDrive files: mv to `_to_delete/superseded-2026-09-14/`).
Run AO did: link audit, five new email files, phone number in the cadence files and the repo pages, the Azure web
app with its settings, deploy-azure.sh and finish-domain.sh. It could NOT ship code (classifier). David runs
`scripts/deploy-azure.sh` himself in a plain Terminal; this run never calls `az webapp deploy` or `zip`.
Answers to Run AO's questions: (1) David deploys by hand, see above. (2) Use david+portal@atlasonesolutions.com
for the sign-in test. (3) Distinct subjects per event are right.

## Job 1: the 16 booking and intake email files (Run AO skipped this)
Bodies live in the project doc `claude/email-template-pass-run-E-2026-09-07.md`; a copy may be in `_BUILD-LOG/`
(look for `email-template-pass-run-E*`), otherwise in the repo under `_briefs/` (RUN-E). Wrap each body in the
standard wrapper (logo, signature with 380-225-5217, both footer lines, coloured spans on every link, no dashes)
and save in `_BUILD-LOG/cadence-emails-2026-09-13/` as: `booking-c1.html`, `booking-reminder-24h.html`,
`booking-reminder-1h.html`, `booking-c2.html`, `booking-c3.html`, `booking-cancelled.html`, `booking-no-show.html`,
`intake-instant-reply.html`, `send-peo-form.html`, `send-bookkeeping-form.html`, `tool-lead-nurture-1.html` (and
-2, -3 if the doc has them), `won-email-6.html`, `won-email-7-checklist.html`. Subject on the <title>. Add every
one to INDEX.md with workflow and node name. Render two at 390 px, zero console errors. Commit, push, log
"Job 1 files ready".

## Job 2: verify the portal on its test address (only if David has deployed)
`curl -s -o /dev/null -w "%{http_code}" https://atlas-one-portal.azurewebsites.net/api/health`. If not 200, log
"portal not deployed yet, David runs scripts/deploy-azure.sh" and skip to Job 3. If 200: in headless Chromium open
the sign-in page (brand, fonts, zero console errors), request a sign-in link for david+portal@atlasonesolutions.com
(temporarily set PORTAL_APP_URL to the azurewebsites address for the test, then set it back), read the link from
the GHL conversation on that contact if possible (otherwise log "David: check the david+portal inbox and paste the
link into the live log" and wait), follow it, screenshot Home, Documents, Requests, Book, Pay, Partners, Admin at
1440 and 390 to `~/Projects/atlas-one-intake-forms/_briefs/assets/run-AQ/shots/`. Then check DNS:
`dig +short portal.atlasonesolutions.com CNAME` and `dig +short TXT asuid.portal.atlasonesolutions.com`. If both
answer, run `scripts/finish-domain.sh` and confirm https://portal.atlasonesolutions.com returns 200 with the
sign-in page. If DNS is not there, say so; do not touch GoDaddy.

## Job 3: phone number sweep across OneDrive (Run AO skipped this)
Find every 385-213-7177 (also 385.213.7177, (385) 213-7177, tel:13852137177) under
`2. Atlas 1 Solutions Marketing/` (Master Kit tools, Tools Hub, MASTER HUB, Portal catalogue, A1_Sales playbooks,
overlays, decks, agreements, one-pagers, pricing sheets, email drafts) EXCEPT `_to_delete/`, `_gold_backup*`, and
anything under `3. Cornerstone PEO/`. Replace with 380-225-5217 (where a signature block prints the number, use
"380-225-5217 (380-CALL-A1S)"). .html/.md/.txt/.json/.py/.js by sed; .docx and .pptx with python-docx and
python-pptx (replace inside every run and table cell, save in place, back up each original first to
`_to_delete/superseded-2026-09-14/phone-sweep/`); .xlsx with openpyxl the same way; .pdf: regenerate from its
source when the source sits in the same folder, otherwise list it under "PDFs to regenerate". Rebuild the Portal
(path argument) and confirm the stamp. Report: count per file type, files changed, PDFs to regenerate, and any
file that still contains the old number.

## Report
Paths, the portal test result and screenshots looked at, DNS state, the sweep counts, assumptions, Questions for David.
