# Run AH report (terminal GHL-JOBS, files only)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` ("the bookkeeping cadence, written and ready for the GHL terminal"), copied to
`repo:_briefs/BRIEF-GHL-JOBS-2026-09-13.md`. All four jobs done. Prior report backed up to
`_to_delete/superseded-2026-09-13/prior-reports/RUN-GHL-JOBS-report-preAH.md`.

## Job 1: read first (done)

Read `RUN-P-cadence.md` and `RUN-P-report.md` (the Long Tail loop / Call: not now / Seasonal touches build, the
exact suppression gate tags, the tag based `recent-touch` cooldown pattern, why GHL If/Else branches cannot merge
back together), `RUN-AD-GHL.md` Part 4 (the global email rules now in force: from name, paragraph style, signature
block plus two footer lines, link colours, button pattern, booking link first, no dashes), the client facing
`A1_Sales/Atlas 1 Bookkeeping/Atlas_One_Bookkeeping_Marketing_Sheet_V7.pdf` (retail prices only, never the
"Internal Master Bookkeeping" subfolder), and `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md` (the wrapper,
the button markup, the rule 31 dash scan). Also read `RUN-W-report.md` to confirm the only permitted guarantee
wording is the Audit Guarantee.

## Job 2: bookkeeping cadence copy (done)

Wrote `A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md`: sequence A "Books: after the call"
(B-1 same day, B-2 at +3 days, B-3 at +7 days, B-4 at +14 days, then hand off to not-now) and sequence B "Books:
quarter and year end" (BQ-1, BYE-1 2026-11-01, BYE-2 2027-01-05), each with subject, full HTML body, button
markup, and the standing wrapper/signature rules from Part 4.1. Retail prices used: bookkeeping plans $300 to
$1,000 / $1,000 to $2,000 / $2,000 to $3,000 a month, payroll $30 monthly / $15 bi-weekly / $7.50 weekly per
employee, all from the V7 client sheet.

Rendered B-1 and BQ-1 offline through the How To wrapper in headless Chromium: 0 console errors, logo shows,
button is periwinkle with white text, signature block shows the two new footer lines, no dashes (grep scan clean).
Screenshots: `repo:_briefs/assets/run-AH/shots/B1-render.png`, `BQ1-render.png`.

## Job 3: GHL build brief (done)

Wrote `_BUILD-LOG/BRIEF-GHL-bookkeeping-cadence.md`: exact node list for a new workflow "Books: after the call"
(trigger tag `books-interest`, a seven segment suppression gate combining Call: not now's five standing tags with
the Long Tail loop's reply/booked exits, four sends, three waits at 3/4/7 days, tail wait 3 days, hand off via tag
`not-now`), the three seasonal inserts into "Seasonal touches 2026-27" with their placement in the existing date
order, the tag to create (`books-interest`), the hand off mode Part 0 procedure copied from the current
`BRIEF-GHL.md`, and a full test plan (two test contacts, waits shortened then restored, delete after). This is
ready for the GHL terminal to build; it was not built in GHL this run (that requires the browser UI terminal).

## Job 4: Quick Quote DM Mono (done)

Both Quick Quote files (`Atlas_One_Quick_Quote.html` and `Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html`)
declared `--mono:'DM Mono',...` but never embedded the font, so numbers silently fell back to a system font.
Embedded DM Mono 400 (Regular, already on disk from a local font asset cache) and 500 (Medium, fetched once from
`raw.githubusercontent.com/google/fonts` since no CDN reference is shipped in the final files) as base64
`@font-face` rules inside the existing `<style id="a1fonts-2026-09-13">` block, subset with `fonttools` (installed
into a throwaway venv, cleaned up after) to digits and punctuation only. Original TTFs 48.9KB / 49.2KB, subsets
10.8KB / 10.8KB each.

Backed up both original files to `_to_delete/superseded-2026-09-13/quick-quote-pre-dmmono/` before editing.
Rendered both live files offline in headless Chromium at 390px, 768px and 1440px: 0 console errors, 0 non-file
network requests, `scrollWidth` equals the viewport at 390px on both files. The dollar figures in the bottom quote
bar visibly render in DM Mono's tabular numeral style at all three widths. Screenshots:
`repo:_briefs/assets/run-AH/shots/quickquote-dmmono-390.png`, `-768.png`, `-1440.png`.

Rebuilt the Portal: `python3 "_INTERNAL (do not share)/build_portal_single.py" "<Master_Kit>"`. New title stamp
`Atlas One Portal: build Sep 13, 2026 12:00 PM`, 44 tools (same count as the last confirmed build), 19.45MB.

## Assumptions (numbered)

1. The Audit Guarantee wording ("the only permitted guarantee wording is the Audit Guarantee," `RUN-W-report.md`)
   is reused in B-1 with "your first year membership" changed to "your first year cost," since bookkeeping is sold
   per plan, not a membership tier. The core promise (two times the cost in documented savings or risk removed,
   or nothing to buy) is preserved.
2. The Email HTML How To's general rule "no Atlas One prices in marketing email" is overridden in B-1 on this
   brief's explicit instruction to use the retail bookkeeping and payroll prices. This is a direct instruction
   conflict; flagged below for a decision on which rule wins going forward.
3. B-3's proof point is written generically (unreconciled QuickBooks, overlapping subscriptions, a payroll error)
   rather than pulled from `Atlas_One_Proof_Sheet.html`, because that sheet's stories are HR and payroll wins, not
   bookkeeping wins, and the brief says never invent a number. No dollar figure is claimed in B-3.
4. Job 3's seasonal insert placement (BYE-1 immediately before YE-1, BQ-1 immediately before each Q-1, both on the
   same calendar date) means only the first send of each same date pair will actually go out, because every send
   in that chain shares one `recent-touch` cooldown gate. This mirrors how YE-3 already covers two purposes on one
   date. Documented as a build note and a question below rather than decided.
5. DM Mono 500 (Medium) was fetched once from Google's official font source repository during this run to obtain
   the bytes to embed; the two shipped HTML files make no network calls at runtime (confirmed: 0 non-file requests
   in the offline render).
6. `fonttools` was not installed on this machine; installed into a throwaway Python venv for this job only and the
   venv was deleted afterward. No system Python packages were modified.

## Skipped

- Job 3's workflow was written as a build brief only; it was not created in GHL, since this terminal never touches
  the GHL browser UI. The GHL terminal builds it from `BRIEF-GHL-bookkeeping-cadence.md`.

## Questions for David

1. Job 2 puts retail prices ($30/$15/$7.50 per employee, and the $300 to $3,000 monthly plan ranges) directly in
   the first bookkeeping email (B-1), on this brief's explicit instruction. That conflicts with the standing rule
   in `Atlas_One_Email_HTML_How_To.md` ("no Atlas One prices in marketing email"). Please confirm prices belong in
   this cadence specifically, or if B-1 should be rewritten to point to a booking call for pricing instead.
2. Is the Audit Guarantee ("two times your first year cost in documented savings or risk removed, or there is
   nothing to buy") an acceptable wording applied to bookkeeping specifically, where the guarantee was originally
   written for the membership tiers? If not, B-1's guarantee paragraph should be cut rather than reworded, since
   no other guarantee wording is permitted.
3. Job 3's build brief: when BYE-1/YE-1 and each BQ-1/Q-1 pair land on the same date, only the first of the pair
   will actually send (the second is suppressed by the shared `recent-touch` cooldown). Is that acceptable, or
   should one member of each pair move a day earlier or later so both fire?
4. Same as Run P's still open question 1: the wait node between Email 1 and Email 2 in "Post-Presentation Email"
   is still configured for 3 minutes instead of 3 days (not touched this run, just carried forward since it
   affects live prospects). Please confirm whether to fix it.

## Paths touched

- `A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md` (new)
- `_BUILD-LOG/BRIEF-GHL-bookkeeping-cadence.md` (new)
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html` (edited: DM Mono embedded)
- `09 Quick Quote Tool/Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html` (edited: DM Mono embedded)
- `_to_delete/superseded-2026-09-13/quick-quote-pre-dmmono/` (backups of both Quick Quote files, pre edit)
- `_to_delete/superseded-2026-09-13/prior-reports/RUN-GHL-JOBS-report-preAH.md` (backup of the prior report)
- `Atlas One PORTAL.html` (rebuilt)
- repo: `_briefs/BRIEF-GHL-JOBS-2026-09-13.md`, `_briefs/BRIEF-GHL-bookkeeping-cadence.md`,
  `_briefs/assets/run-AH/shots/` (B1-render.png, BQ1-render.png, quickquote-dmmono-390/768/1440.png)
