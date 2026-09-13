# BRIEF-GHL-JOBS (current run: Run AI, files and API only): make the GHL email pass cheap

Rules as always (no questions, live log TERMINAL-GHL-JOBS-live.md, report RUN-GHL-JOBS-report.md via quoted
heredoc, commit and push, never delete, never send an email, never enable anything).

## Why
The GHL terminal spent about 30 tool calls per email send (reading the old source through a tiny textarea, then
typing 2,000 characters) and finished 2 of about 20 sends. From now on the GHL terminal never reads old copy and
never composes; it pastes finished HTML that this run produces, or picks a template this run created.

## Job 1: the standard signature block
Read the current Email 1 source the GHL terminal built (it describes it in RUN-GHL-report.md, Part 4: logo mark at
36px on the left, name / Founder, Atlas One Solutions / phone / email, two footer lines in #9AA3B2, then tagline
and address footer). Rebuild that exact block in `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md` as THE
standard signature (replace the old text-only one) with the two footer lines: "Vendor neutral. I quote several
providers, show them side by side, and you choose. You never pay for anything you do not need." and "Payroll,
benefits, insurance, bookkeeping, software, IT and the paperwork in between. See everything Atlas One handles:
<a>one page, no form</a>" linking https://forms.atlasonesolutions.com/tools/what-we-do/. Decision: E0 will be
updated to match this block, not the other way round.

## Job 2: one finished HTML file per send, `_BUILD-LOG/cadence-emails-2026-09-13/<send>.html`
Wrapper, button, signature and links exactly per RUN-AD-GHL.md Part 4.1 (from name is set in GHL, not in the file;
note it in the index). Bodies:
- From RUN-AD-GHL.md 4.2 verbatim: Email 1 (with the five bullets as recorded in RUN-GHL-report.md), Email 2, E0,
  LT-1, LT-2, LT-4 (retention link https://forms.atlasonesolutions.com/tools/retention-cost/), LT-5, 45-A.
- Global-only sends (body copy unchanged, wrapper and rules applied): Email 3, Email 4, LT-3, 45-B, 45-C, the
  construction audit email, Q-1, YE-1, YE-2, YE-3, YE-4. Find their CURRENT body copy in the OneDrive reports
  (`RUN-P-cadence.md`, `RUN-P-report.md`, `RUN-Q-report.md`, `RUN-M.md`, `run-G-workflows-audit-2026-09-10.md`,
  `ghl-prospecting-workflows-REPORT-2026-09-08.md`, `COWORK-*.md`, the Run E template pass notes) and the
  follow-up cadence spec drafts. Where a body is not in any file, write the file with the wrapper and a clearly
  marked `<!-- BODY: READ FROM GHL, keep as is -->` placeholder so the GHL terminal knows to keep the existing
  body and only replace the surrounding wrapper. Apply the global rules to those bodies too (booking link instead
  of "send me times", no dashes, no "here" links).
- Also the seven bookkeeping sends from Run AH, with these decisions applied first: cut the guarantee paragraph
  from B-1 (the guarantee is a membership promise, not a bookkeeping one); keep the per employee payroll price,
  remove the $300 to $3,000 plan ranges from the email and say "plans start under a few hundred a month; the call
  sets the number"; move BQ-1 one day after each Q-1 date and BYE-1 to Nov 2 so both fire.
Render every file offline through the wrapper, screenshot each, look, check: DM Sans loads, button present, links
#23304D, both footer lines, zero dashes, merge fields intact. Write `INDEX.md` in that folder: send name, workflow,
subject line, from name to set, file name, "replace whole body" or "wrapper only", screenshot path.

## Job 3: try the GHL Email Builder API (this is the real win if it works)
Token: the Private Integration token the portal uses (`~/Projects/atlas-one-portal/.env`, or `~/Projects/.env.ghl`),
location AzTPxnK2vSUj19jYoDmR. Read the docs (https://marketplace.gohighlevel.com/docs/ Email Builder: create
template, update template, fetch templates; scopes emails/builder.readonly and emails/builder.write). Test with
ONE template named "A1 TEST delete me" containing Email 2's HTML. If create works and the fetched template carries
the HTML intact, create every send from Job 2 as a template named "A1 cadence: <send name>" and list the template
ids in INDEX.md. Then delete only the test template via the API (a template is not a file; deleting your own test
template is allowed). If the API refuses (scope missing, type unsupported), stop there and write exactly what the
token needs (scope names, where David clicks in Settings > Integrations > Private Integrations) under Questions.
Never send anything. Never touch workflows via API.

## Job 4: write `_BUILD-LOG/BRIEF-GHL-part4-resume.md` for the GHL terminal
Per send, the fastest verified path: if templates exist, open the send, switch it to the template, save, preview,
screenshot; else triple-click the source textarea, select all, paste the file's HTML (use the clipboard write tool
or type it), save, preview, screenshot. No reading of old source except the placeholder sends. Set from name and
from email on every send. Then Part 1 item 3 (construction dead ends, every one) and Run R, hand-off mode Part 0,
/compact between workflows.

## Report: paths, the API result (exact responses), screenshots looked at, assumptions, Questions for David.
