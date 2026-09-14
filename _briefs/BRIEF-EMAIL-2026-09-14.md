# BRIEF-EMAIL — chunk `build-help-live` (now includes Part D, the phone number), written by Cowork 2026-09-14 (after the build-client-kit-2 audit, which PASSED)

Terminal EMAIL. Repo `~/Projects/atlas-one-ai-email-assistant`. Sister repo `~/Projects/atlas-one-intake-forms`
(GitHub Pages behind forms.atlasonesolutions.com, already serving /peo/, /bookkeeping/, /census/).

Cowork's answers to the three questions in RUN-EMAIL-report-build-client-kit-2-2026-09-14.md:
1. Yes, link the help page from the Help tab in the queue. Do it the way question 2 suggests: a URL, so the
   page is always findable and never has to be emailed.
2. Publish it at https://forms.atlasonesolutions.com/help/ (the intake forms site). Attachments stay as the
   offline fallback; the URL is the front door.
3. Yes. Say the verify-link step in 01-for-your-it-person as well, early, in plain words.

## Build, end to end, no questions mid-run

### Part A: publish the help page and the intake form on the forms site
1. In `atlas-one-intake-forms`, add `help/index.html` = the generated `docs/client/Atlas_One_AI_Email_Assistant_Help.html`
   byte for byte, and `email-assistant/index.html` = the Master Kit intake form
   (`12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Email_Assistant_Setup_Intake.html`, webhook already set).
   Follow whatever convention /peo/ and /bookkeeping/ use for filenames, CNAME and index pages.
2. Make `tools/faq_html.py` also write the `help/index.html` copy when that sister repo exists on disk (skip
   silently if not), so the three copies plus this one can never drift. Extend the byte-for-byte test to cover it.
3. Commit in the sister repo with a clear message. Pushing that repo publishes to GitHub Pages: that is a
   production deploy, so it will stop for David. Present it as one prompt and say plainly what it publishes.
4. After the push, wait for Pages, then GET both URLs and confirm 200, correct title, and that the help page
   makes zero offsite requests (it must still work with the network off).

### Part B: link the page from the app
5. Edit `_help_body_html()` in `app.py`: a short line at the top of the Help tab, "The client help page
   (every question, searchable) is at forms.atlasonesolutions.com/help/", as a link that opens in a new tab.
   No other app changes. Tests as needed. Build marker `build-help-live`.
6. Also put the URL in `docs/install/00`, `03`, `docs/client/FAQ-and-troubleshooting.md` ("Where is this page
   online?") and `faq.json`, then regenerate the HTML (which is why Part A step 2 comes first).
7. Deploy the app the normal way. Deploy is the second and last stop for David. Verify by deployment log,
   ARM status and the live marker on /queue/login, never by the CLI alone (a 504 is not a verdict). Then open
   /queue/help with the dashboard token and confirm the link is there and resolves.

### Part C: the verify-link warning for the IT person
8. In `docs/install/01-for-your-it-person.md`, near the top, in plain words: "Azure will email a verify link to
   every alert address we put in. Whoever owns that address has to click it within about thirty minutes or that
   address gets nothing, with no visible error. Tell them it is coming." Keep the existing line in 02.

### Part D: the new Atlas One phone number (added by Cowork 2026-09-14, do this BEFORE Part A so the published pages carry it)
Atlas One's main number is now 380-225-5217 (a GoHighLevel line). The old 385-213-7177 is retired everywhere.
Rules: plain form "380-225-5217"; where there is room, the vanity form "380-CALL-A1S (380-225-5217)", for example
"Call 380-CALL-A1S (380-225-5217)" on click-to-call buttons and contact lines; tel: links become tel:+13802255217.
Cowork has already swept every HTML, MD, JSON, PY and TXT file on OneDrive (A1_Sales and the Master Kit, 179 files)
and rebuilt the Portal. Your part is the two repos:
D1. `atlas-one-ai-email-assistant`: every occurrence (docs/client/FAQ-and-troubleshooting.md, faq.json, tools/faq_html.py,
    config/clients/atlas-one.yaml, docs/signature-transport-rule.md, the tests that assert the number, README if present).
    Use the vanity form in the FAQ "Need a human?" line. Regenerate the help page. Do not touch CHECKPOINT-*.md history files.
    The recipient-facing signature lives in the M365 transport rule, not the app: add "David edits the transport rule to
    380-225-5217" to Questions for David rather than changing anything in M365.
D2. `atlas-one-intake-forms`: every page under tools/ (index, what-we-do, self-assessment, time-savings, vendor-consolidation,
    retention-cost, wc-premium-check, text), plus peo/, bookkeeping/, census/ if they carry it. Footer and contact lines get the
    vanity form where the line has room; tel: links to tel:+13802255217. Leave _briefs/ alone (records). This goes out with the
    same push as Part A, so the site publishes the new number in one deploy.
D3. After the push, GET the what-we-do page and confirm 380-225-5217 is on it and 385-213-7177 is not.
Grep both repos for 385-213-7177, 3852137177, 385.213.7177, (385) 213-7177 and 385 213 7177 before calling it done.

### Close out
9. Full offline suite, commit, push, confirm main equals origin/main. Rules as always: SEND_ENABLED stays false,
   no App Settings writes beyond the deploy itself, no secrets printed or committed, no Azure create or delete,
   never sed -i, no rm or mv. Live log after every step in `_BUILD-LOG/TERMINAL-EMAIL-live.md`; final report to
   `_BUILD-LOG/RUN-EMAIL-report.md` (Questions for David at the END); `CHECKPOINT-2026-09-14-3.md` in the repo.
   Log every judgment call under Assumptions.
