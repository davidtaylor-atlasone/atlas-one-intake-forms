# RUN-GHL-JOBS-report, Run DB, 2026-10-10

Run DA's report is archived at `_BUILD-LOG/RUN-GHL-JOBS-report-runDA-done-2026-10-10.md` (copied, original not deleted). Brief copy: repo `_briefs/BRIEF-GHL-JOBS-2026-10-10.md`. Evidence: repo `_briefs/assets/run-DB/` (shots, this report).

## Built
1. **people.json booking.** `people.charity.booking` is now `https://api.leadconnectorhq.com/widget/groups/book-charity`; the card live_note updated. READ ME FIRST.txt text lives in `build_command.py` (build_rep_kit) and now says the booking link is live.
2. **Contact blocks.**
   - Everything We Handle: master source gets a `data-a1-person-contact` row (David's phone, david@, contact@). New `_swap_person_contact_block` in `build_command.py` replaces it with the rep's phone, email and contact@ in every rep copy. Rep copy now uses the full (email) person line (public=False).
   - Price List: rep copy built with public=False, so charity@ prints.
   - Email Blast Library (`Atlas_One_Email_Blast_Library.md`): the three signature lines that carried a phone now end with `{{rep_email}}`.
3. **David's launch pieces out of rep kits.** `rep_assets.py` DAVID_ONLY_OFFICE_FILES (Client Launch Deck pptx and Companion docx) are skipped for any non default person. `present.py` gains REP_EXCLUDED_IDS and playlist_pages(); rep Present playlists, cards and deck rendering drop the launch deck. `catalogue.py` _REP_IDS no longer lists the four client launch rows. Client Announcement Series: the only line naming David is the licensed agent line, so it stays in.
4. **Rebuild and proof.** `build_command.py --person charity` ran clean. COMMAND rebuilt: stamp moved from "Oct 10, 2026 11:27 AM" to "3:14 PM", 216 items.

## What was looked at
- Text scan (PyMuPDF for pdf with link URIs, xml for docx and pptx, raw html) of every file in her folder (68 files) and of the unzipped new zip (64 files). Zip: **0 hits** for david@, "David Taylor" outside the licensed agent line, 385-213-7177, book-david, quick-call-with-david, back-office-audit-30, atlas-one-15-minute-intro-call-hoswp. Folder: the same 0 hits except the 4 stale launch files below.
- Every client facing piece has charity@ or 801-787-8154 except Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.html (and Prospect_Email_Templates carries no person line either): both are templates with first name tokens and booking buttons only, no signature block. See Questions.
- Sales Kit rendered in headless Chromium at 1440 and 390: `#bookcall` visible, href book-charity, scrollWidth 1440 and 390, 0 console errors, 0 non file requests, no Client Launch text. Shots: `_briefs/assets/run-DB/shots/charity-saleskit-desktop.png` and `-mobile.png`.
- catalogue_check: 26 of 27 ok. The one FAIL is retired price "$23" inside `_INTERNAL/test_assistant_guard.py:15` (a test fixture from Run AS1), not from this run.

## Assumptions
1. The brief says old zip and pieces go to `_to_delete`; the terminal rules forbid that. Nothing was parked or deleted. Replaced files are under Retire.
2. "No git push to main": commits go on the current branch `ghl-jobs-run-cw` and push there only.
3. Price List and Everything We Handle rep copies switched to the email bearing person line (brief overrides Run CF's no email on public pages rule, for rep copies only).
4. pdftotext is not installed on this Mac; PDFs scanned with PyMuPDF (text plus link URIs).
5. Hero line of the rep kit already says "Call 801-787-8154"; left as is.
6. "Atlas One Tools (share with prospects).html" does not exist in the Master Kit root (only COMMAND and the Sales Kit built); not created.
7. Email_Blast_Library signatures: only the lines that already had a phone got email.

## Skipped
- Removing the 4 stale launch files from her folder (delete is a hard stop).

## Retire (the auditing chat deletes)
- `A1_Sales/_Rep Kits/Charity Taylor/Client Presentations/Atlas_One_Client_Launch_Companion_2026-09.docx`
- `.../Client Presentations/Atlas_One_Client_Launch_Companion_2026-09.pdf`
- `.../Client Presentations/Atlas_One_Client_Launch_Deck_2026-09.pptx`
- `.../Client Presentations/Atlas_One_Client_Launch_Deck_2026-09.pdf`
- `A1_Sales/_Rep Kits/Charity Taylor.zip` as of 2026-10-08: replaced in place by the new zip (old copy kept only at /tmp/Charity-old-2026-10-08.zip, not in the kit).
- Everything else in her folder was overwritten in place by the rebuild (same file names, new content).

## Questions for David
1. Please have the audit chat delete the 4 launch files above from her folder; until then the folder (not the zip) still holds them. The zip is clean.
2. Bookkeeping Cadence and Prospect Email Templates carry no rep contact line at all. Add a signature block with her email and phone?
3. Fix or exempt the `$23` string in test_assistant_guard.py so catalogue_check passes 27 of 27?
4. Should "Atlas One Tools (share with prospects).html" be built again? It is missing from the kit root.
