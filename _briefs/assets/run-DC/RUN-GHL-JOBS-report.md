# RUN-GHL-JOBS report: Run DC (2026-10-10), follow ups from the Run DB audit

## Built
1. **Signature blocks.** Prospect Email Templates: the four line sender block (name, title, phone, email) now ends all 7 emails (A1 to A3, B1 to B3, C), replacing the first name only sign off. Bookkeeping Cadence: same block at the end of all 7 sends (B-1 to B-4, BQ-1, BYE-1, BYE-2). Master sources in `A1_Sales/Email Templates/*.md`, HTML re-rendered with render_md_pages.py. David's copy keeps merge fields filled from his people.json entry; Charity's carries charity@atlasonesolutions.com and 801-787-8154.
2. **Retired price scan.** `_INTERNAL (do not share)/price_scan.py` iter_files now skips `test_*.py` (fixtures hold retired figures on purpose). The fixture was not edited. catalogue_check: **216 entries, all 27 of 27 checks passed**.
3. **CLAUDE.md** (this repo): the "Atlas One Tools (share with prospects).html" mention removed; COMMAND now described as one output.
4. **Rebuild.** `build_command.py --person charity` clean, COMMAND rebuilt (stamp Oct 10, 2026 5:02 PM, was 3:14 PM; 216 items), Sales Kit rebuilt (62 items). `Charity Taylor.zip` rebuilt from her folder (73 entries).

## Looked at
- Her folder (29 text files) and the new zip: 0 hits for david@, davidtaylor@, 385-213-7177, book-david, quick-call-with-david, back-office-audit-30, atlas-one-15-minute-intro-call-hoswp. Zero launch files in zip. `--check-zip` guard: clean.
- All 7 email template pages in the zip carry charity@ or 801-787-8154.
- Renders at 390 px (Playwright headless shell): Prospect Email Templates and Bookkeeping Cadence, scrollWidth 390, 0 console errors, 0 non file requests. Shots in `_briefs/assets/run-DC/shots/`.

## Assumptions
1. Prospect section D (LinkedIn DM / text short versions) gets no signature block: it is not an email.
2. The Cadence wrapper already adds a saved GHL signature block; per the brief each send now also ends with the block in its own copy. If GHL then shows the details twice, drop the in-email block when the workflow is built.
3. Cadence block is HTML (`<br>` lines) to match that file's paragraph markup; Prospect uses markdown line breaks.
4. The first zip attempt was stale (still 15:13 content, Cadence lacked her details); I rebuilt it with `zip -X`, excluding .DS_Store, same `Charity Taylor/` root as before.
5. Run DB's report archived as `RUN-GHL-JOBS-report-runDB-done-2026-10-10.md`.

## Retire
- `A1_Sales/_Rep Kits/Charity Taylor.zip` overwritten in place; previous copy kept only in the session scratchpad, not the kit.
- Charity's folder files overwritten in place by `--person charity` (same names): Email Templates pages and Sales Pieces/Service Decks PDFs and PPTX listed by the builder's RETIRE lines.

## Skipped
- Deleting a scratch zip in the session scratchpad was blocked by the hard stop hook; not retried. It sits harmlessly outside the kit.

## Questions for David
1. Should the in-email signature on the Cadence sends stay once the GHL saved signature snippet is applied, or is the snippet enough?
