# RUN AE (the GHL-JOBS terminal, code and files): the public "Everything Atlas One handles" page (run after Run AC)

Written by Cowork 2026-09-13. Same rules as Run AC (no questions, answer prompts yourself, live log to
`<Master_Kit>/_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, report `RUN-GHL-JOBS-report.md`, brand rules, fonts embedded, no CDN, no
dashes, phone width 390 with no horizontal scroll, commit and push). Copy this file to `_briefs/RUN-AE-GHL-JOBS.md`.

## Why
David's cadence emails will carry a footer link "See everything Atlas One handles" so prospects stop thinking he only
does payroll, benefits and HR. The page shows the whole offering. It is view only: it names every tool and document
builder but none of them run there. Every call to action goes to David.

## Build: `repo:tools/what-we-do/index.html`, published at `https://forms.atlasonesolutions.com/what-we-do/`
Source of truth for the list: the Quick Quote tool (104 services, six divisions, `09 Quick Quote Tool`), the client
price list from Run U (names only, NO prices on this page), the 11 document builders and the calculators list in
`_INTERNAL/build_portal.py` (names only). Nothing internal, no vendor names, no PEO brand names, no prices, no margins.

Sections, in this order, one screen each on desktop, stacked on phone:
1. Hero: "One relationship. One point of contact. Everything your business runs on." One paragraph in David's voice:
   Atlas One is vendor neutral, quotes several providers side by side, manages the whole process, and the goal is
   the owner, the admin team, the accountant and the CFO all home by five. Button: Book a few minutes (BOOK =
   https://api.leadconnectorhq.com/widget/groups/book-david).
2. The six divisions as six cards (Workforce & HR, Benefits & Retirement, Financial Services, Risk & Insurance,
   Technology & Operations, Business Consulting), each with its full service list from Quick Quote as compact text.
   Order the Workforce card so payroll, time and certified payroll come first and HR documents last.
3. "Documents built for you as a member": bilingual employee handbook (87 policies, 50 states), safety manual (39
   OSHA programs), offer letters, W-2 and 1099 agreements, at-will agreements, NDAs, write-ups, separation letters,
   onboarding packets, enrollment guides. Plus: certificates of insurance issued on request for your customers and
   GCs (one line, no tool).
4. "Software, simplified": one paragraph. Atlas One can move your current subscriptions under the Atlas One
   membership, usually at a lower rate, with one transaction a month instead of a dozen, and one number to call for
   IT and software support. No vendor names.
5. "Free tools, no form": the three public tools as links (Time and Cost Savings, Vendor Consolidation, Back Office
   Self Assessment, all at forms.atlasonesolutions.com/tools/...). Then the names of the member calculators and
   builders as plain text (no links), grouped, so they can see the depth.
6. Guarantee band: the Audit Guarantee, one sentence (2x first year membership in documented savings or risk
   removed, or nothing to buy). Membership tiers by name only, "pricing on the call".
7. Close: Book a few minutes button, 385-213-7177, david@atlasonesolutions.com, tagline.

Meta: title "Everything Atlas One handles", description one line, Open Graph image the laptop mark on off-white
(generate a 1200x630 PNG in the repo). Print stylesheet so it prints to two clean pages (David will attach the PDF
to some emails). Render at 1440 and 390, look, fix. Confirm 200 after push. Copy the PDF to
`A1_Sales/Atlas_One_Everything_We_Handle.pdf` and add a Master Hub card "Everything Atlas One handles (public page)".

## Report
`RUN-GHL-JOBS-report.md`: URL, screenshot paths, the service count per division, assumptions, Questions for David.

## Also in this run (three small fixes found in the Run AC audit; do them after the page)
A. The census tool still carries two retired Zoom Scheduler links (scheduler.zoom.us/david-taylor-qp71rc) in
   `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html` and `repo:census/index.html`.
   Replace both with https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp, keep
   the two files identical, push, confirm forms.atlasonesolutions.com/census/ returns 200 and shows the new link.
   Rebuild the Portal (path argument) and confirm the stamp.
B. `RUN-AC-report.md` lost every dollar amount (a "$99" became blank and "$0" became "/bin/zsh": the report was
   written through an unquoted heredoc). Rewrite the damaged lines with the real figures (Assumption 4: the tiers
   are $99 setup waived, $399 setup $495, $999 setup $995, $1,900 setup $1,500; Assumption 13: 1099-NEC $2,000,
   Nevada $12.00; Assumption 16 and Question 5: the phase 2 pricing you proposed; Question 8: Vercel Pro $20 a
   month) and add one line to `repo:CLAUDE.md`: always write reports and logs with a quoted heredoc (<<'EOF') or
   a file write tool, never an unquoted heredoc, so dollar signs survive.
C. Sweep the 27 files outside `06 Calculators and Tools` that still link Google Fonts (list in the Run AB report,
   Quick Quote and the Quote & ROI Builder first): same embed as Run AC job 1, backups to
   `_to_delete/superseded-2026-09-13/fonts-before/`, render offline, table in the report, Portal rebuilt.
