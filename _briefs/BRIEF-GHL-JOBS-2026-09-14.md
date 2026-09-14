# BRIEF-GHL-JOBS (current run: Run AO): stage the client portal on Azure (test address only, no public domain yet). Cowork 2026-09-14.

Rules as always (no questions, live log TERMINAL-GHL-JOBS-live.md, report RUN-GHL-JOBS-report.md via quoted
heredoc, commit and push, never delete OneDrive files: mv to `_to_delete/superseded-2026-09-14/`). Repo for this
run: `~/Projects/atlas-one-portal` (log and report still go to the Master Kit _BUILD-LOG as usual).

Decision (David, 2026-09-14): no Vercel account. Atlas One already pays for Azure (the email assistant runs there
on App Service plan `ASP-atlasoneaiemailassistantv2-8088`, B1, resource group `atlas-one-ai-email-assistant-v2`,
West US 2, subscription "Azure subscription 1", az CLI already logged in as david@AtlasOneSolutions.com). The
portal goes on that SAME plan as a second web app: one vendor, no new monthly cost. This run stops at the private
*.azurewebsites.net test address; portal.atlasonesolutions.com (the real go-live) is a later run after David adds
DNS, so nothing in this run is public. The sign-in test email goes to david@atlasonesolutions.com only (David).

## Job 0 (FIRST, 20 minutes, repo ~/Projects/atlas-one-intake-forms): email files the GHL terminal will paste
Do this before the Azure jobs and commit it on its own, because the GHL terminal reads these files mid-run.
a) Link colour fix. In Outlook for Mac (dark mode) every link without its own colour renders magenta. GHL strips
   inline styles from <a>, so the colour must sit on a <span> inside the anchor. In every file in
   `_BUILD-LOG/cadence-emails-2026-09-13/*.html` (all 26) and in the two wrapper sources in
   `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`: for every <a ...>text</a> whose inner content is plain
   text (no span, no table button), rewrite to <a href="..."><span style="color:#23304D;text-decoration:underline;">text</span></a>.
   Leave table buttons alone. Write the list of files changed and the count of anchors fixed per file to
   `cadence-emails-2026-09-13/LINK-FIX-2026-09-14.md`. Re-render two of them (email-1.html, b-1.html) in headless
   Chromium and confirm no anchor is left without a coloured span (querySelectorAll('a:not(:has(span))') = 0
   outside table buttons).
b) Two branded confirmation emails on the standard wrapper (logo header, signature block, both footer lines,
   no dashes), saved as `cadence-emails-2026-09-13/confirm-service-signup.html` and `confirm-document-build.html`
   and added to INDEX.md. Use the merge tag placeholders {{contact.which_service}} and {{contact.which_document}}
   (the GHL terminal swaps in the real picker tags). Copy, plain and specific:
   Service sign-up, subject "Your {{contact.which_service}} request is in, {{contact.first_name}}": Hi first name.
   Got your request for {{contact.which_service}} for {{contact.company_name}}. Here is what happens next: I look it
   over today, then call or email you within one business day to confirm the details and the start date. If
   documents are needed I will send one short list, not a drip. Questions before then: reply here or call
   385-213-7177. Signature.
   Document build, subject "Your {{contact.which_document}} is in the queue, {{contact.first_name}}": Hi first name.
   Got your request: a {{contact.which_document}} for {{contact.company_name}}. I build it around your business,
   review it with you, and send it back ready to sign, usually within five business days. If I need anything I
   will ask once. Questions: reply here or call 385-213-7177. Signature.
c) Three internal notification emails to David (same wrapper, compact): `internal-new-booking.html` (subject
   "New booking: {{contact.name}}, {{appointment.start_time}}", body: calendar name, date and time, company,
   phone, email, how they came in (lead source), one link to the contact in GHL), `internal-cancelled.html`,
   `internal-rescheduled.html`. Add to INDEX.md.
Commit and push, then log "Job 0 files ready" in the live log before starting Job 1.

## Job 1: make the app run as a plain Node server (it already nearly does)
`server/app.ts` is Hono; `pnpm start` = `SERVE_STATIC=1 tsx server/dev.ts`. Add a production start that does not
need tsx at runtime: compile the server (`tsc -p tsconfig.server.json` or an esbuild bundle to `dist-server/`),
keep `pnpm build` for the Vite client, add `"start:prod"` that serves `dist/` and `/api/*` on `process.env.PORT`.
`/api/health` must return 200. Test locally with PORTAL_TEST_MODE=1 first. Remove the Vercel pieces so nothing is
duplicated: `git rm vercel.json api/index.ts`, drop `hono/vercel` if unused. Rewrite `DEPLOY.md` for Azure: David's
only part is the two DNS records in Job 3, written in plain words (which account, which menu, what to type). Copy
it to `<Master_Kit>/_BUILD-LOG/portal-DEPLOY-for-David.md` (overwrite; the old one is Vercel).

## Job 2: create the Azure web app and stage the build on its test address
- `az webapp create -g atlas-one-ai-email-assistant-v2 -p ASP-atlasoneaiemailassistantv2-8088 -n atlas-one-portal
  --runtime "NODE:22-lts"` (if the name is taken use atlas-one-client-portal). Startup command = the production
  start. Always On: on. HTTPS only: on.
- App settings from `~/Projects/atlas-one-portal/.env` (GHL_PRIVATE_INTEGRATION_TOKEN, GHL_LOCATION_ID,
  PORTAL_SESSION_SECRET) plus PORTAL_APP_URL=https://portal.atlasonesolutions.com,
  PORTAL_ADMIN_EMAILS=david@atlasonesolutions.com, PORTAL_EMAIL_FROM=David@AtlasOneSolutions.com,
  GHL_DAVID_USER_ID=vTV2wRivyR9f9XWNook3, NODE_ENV=production. Never print the token or secret in the log or the
  report. Never set PORTAL_TEST_MODE on Azure.
- Ship a prebuilt zip (`az webapp deploy --type zip`: client `dist/`, compiled server, production node_modules)
  or SCM build with a pnpm-aware script, whichever is more reliable. Make it `scripts/deploy-azure.sh` so the
  next update is one command; describe it in DEPLOY.md.
- Verify on the azurewebsites.net address in headless Chromium: sign-in page renders (brand, fonts),
  `/api/health` 200, zero console errors. Request a sign-in link for david@atlasonesolutions.com (PORTAL_APP_URL
  will make the link point at portal.atlasonesolutions.com, which does not resolve yet: for this test set
  PORTAL_APP_URL to the azurewebsites.net address, test, then set it back to the portal URL). Follow the link,
  screenshot Home, Documents, Requests, Book, Pay, Partners, Admin at 1440 and 390 to
  `~/Projects/atlas-one-intake-forms/_briefs/assets/run-AO/shots/`. If the email cannot be read by the terminal,
  say "David: check your inbox" in the log and wait for him.
- Run `node scripts/preflight.mjs` against the Azure settings; put the output in the report (customFields scope
  may still be 401 until the GHL terminal's Part 5 adds it; say so, do not fix it here).

## Job 3: prepare the custom domain, do not bind it
`az webapp show -n <app> -g atlas-one-ai-email-assistant-v2 --query customDomainVerificationId`. Put at the TOP
of the report a box titled "David: two records to add at GoDaddy" with exactly:
  Record 1: Type CNAME, Name portal, Value <app>.azurewebsites.net, TTL 1 hour.
  Record 2: Type TXT, Name asuid.portal, Value <the verification id>, TTL 1 hour.
Write `scripts/finish-domain.sh` (hostname add, free managed certificate create, SNI bind, poll until
https://portal.atlasonesolutions.com answers 200) but DO NOT run it this run; Cowork queues that as its own run
after David adds the records. Do not touch GoDaddy.

## Report
Paths, the azurewebsites.net URL, the two DNS records at the top, screenshots looked at, preflight output, monthly
cost (should be $0 extra on the existing B1 plan; say so or say what it costs), assumptions, Questions for David.
