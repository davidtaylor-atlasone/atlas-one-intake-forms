# BRIEF-GHL-JOBS (current run: Run AH, files only): the bookkeeping cadence, written and ready for the GHL terminal

Rules as always: no questions, answer prompts yourself, live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, report
`_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted heredoc), commit and push, never delete (mv to _to_delete).

## Why
David: "nobody will know I do bookkeeping, full AP/AR, or basic and self-service payroll." The prospecting cadences
(Post-Presentation Email, Call: not now, Seasonal touches) are payroll/benefits led. Form B (bookkeeping intake) is
live but has only a confirmation. Build the copy and the GHL build brief; the GHL terminal builds it in GHL later.

## Job 1: read first
`claude` docs are not on disk; read these on OneDrive instead: `_BUILD-LOG/RUN-P-cadence.md` and `RUN-P-report.md`
(how the cadences are built: gates, waits, Last Touch Date, recent-touch cooldown, tags), `RUN-AD-GHL.md` Part 4
(the global email rules now in force: from name "David Taylor, Atlas One Solutions", real paragraphs, the E0
signature block with logo, the two footer lines, dark blue links, button CTA, booking link first, no dashes, HR
never leads), `A1_Sales/Atals 1 Bookkeeping/` (the client-facing bookkeeping sheet, retail prices only; NEVER the
Xperienced approval sheet or anything from _INTERNAL), and `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`.

## Job 2: write `A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md`
Two short sequences, David's voice (plain, warm, short sentences, no dashes anywhere, value not just cost):
A. "Books: after the call" (trigger: tag books-interest added by David after any call where books came up, or
   Form B submitted without a booked call): B-1 same day (what Atlas One bookkeeping actually is: monthly close,
   AP/AR, payroll through the books at $30 monthly / $15 bi-weekly / $7.50 weekly per employee, QuickBooks cleanup,
   one point of contact, the owner sees one number a month; button: book a few minutes), B-2 at +3 days (the
   cost of books that are behind: late invoices, missed deductions, the tax bill surprise; Time and Cost Savings
   calculator link), B-3 at +7 days (one proof point without an industry name, and the "we can also run basic or
   self-service payroll inside the books" line), B-4 at +14 days (the close-the-file email, reply later or yes).
   Then add tag not-now (hand off to the 45 day rhythm) and end.
B. "Books: quarter and year end" three seasonal one-offs to fold into "Seasonal touches 2026-27": BQ-1 (30 days
   before quarter end: a clean quarter close is the easiest place to switch bookkeepers), BYE-1 (Nov 1: January
   books start clean, 1099s and W-2s come out of one system), BYE-2 (Jan 5: "start the year with a clean set of
   books; the first month is the setup month").
Every email: subject line, full body with merge fields, the button text and link, and the footer lines. Retail
prices only from the client-facing bookkeeping sheet. Never name Brittney, Xperienced, or any vendor. Mention the
guarantee once (B-1). Render each email through the How-To skeleton to a screenshot and look (no dashes, links
dark blue, button present); save shots to `repo:_briefs/assets/run-AH/`.

## Job 3: write `_BUILD-LOG/BRIEF-GHL-bookkeeping-cadence.md` (the GHL terminal's build brief, ready to run)
Exact node list for workflow "Books: after the call" (trigger, suppression gate identical to Call: not now's
current gate, sends, waits, exit-on-reply-or-booked after each wait, Last Touch Date + recent-touch after each
send, the not-now hand off), the three seasonal inserts with their dates and the 10 day cooldown check, the tags
to create (books-interest), the test plan (one test contact, plus-addressed email, unique phone, waits shortened
for the test then restored, delete after), and the hand-off mode Part 0 from the current BRIEF-GHL.md.

## Job 4: Quick Quote DM Mono
The two Quick Quote files still ask for DM Mono for numbers. Embed DM Mono 400 and 500 as base64 (subset, digits
and punctuation are enough) the same way DM Sans was embedded, backups to _to_delete/superseded-2026-09-13/,
render offline, Portal rebuilt with build_portal_single.py, stamp confirmed.

## Report: paths, screenshots looked at, assumptions, Questions for David (pricing lines you were unsure of go here).
