# BRIEF-GHL-JOBS (current run: GHL-JOBS Run DB, 2026-10-10): Charity's kit carries only her contact details

Installed by Cowork (chat A1 GHL status) after a live audit of A1_Sales/_Rep Kits/Charity Taylor/ (68 files scanned).
Archive Run DA's report first. Files and code only. No sends, no deploys, no git push to main, no GHL changes.
Log real clock times. Finish with RUN-GHL-JOBS-report.md. No questions mid run; batch them at the end.

Her details (must match her GoHighLevel user, read live 2026-10-10): Charity Taylor, Business Advisor,
charity@atlasonesolutions.com, mobile 801-787-8154, office 380-225-5217 (company line, fine to show as office).
Booking: https://api.leadconnectorhq.com/widget/groups/book-charity (group "book-charity", live since 2026-10-06).

Keep on purpose (decided, do not change): "Insurance and PEO questions go to David Taylor, our licensed agent" and
"Insurance products are offered through David Taylor, licensed agent" lines. Charity holds no insurance license.

## Job 1: people.json booking
`_INTERNAL (do not share)/people.json`, people.charity.booking is null. Set it to the book-charity URL above.
Then her booking button shows everywhere the build reads it. Update READ ME FIRST.txt (it still says booking is pending).

## Job 2: pieces that do not carry her contact block
- Sales Pieces/Atlas_One_Everything_We_Handle (html and pdf): only contact@ and 380. Add the rep contact block from
  people.json like the other Sales Pieces. Fix in the master generator so David's copy and every rep copy get it.
- Price List (html and pdf): has her name and phone, not her email. Add charity@ via people.json.
- Email Templates/Atlas_One_Email_Blast_Library.html: signatures have her name and phone, no email. Add it.

## Job 3: David's own client launch pieces do not belong in a rep kit
Client Presentations/Atlas_One_Client_Launch_Companion_2026-09 (docx, pdf) and Atlas_One_Client_Launch_Deck_2026-09
(pptx, pdf) are David's announcement to his existing clients: "A quick heads up from David", "Talk soon, David", his
back-office-audit-30 calendar, "text me 380.225.5217". Exclude both from every rep kit build (not from David's own).
Same check for Email Templates/Atlas_One_Client_Announcement_Series.html: if any line other than the licensed agent
line names David as the sender, exclude it from rep kits too and list it.

## Job 4: rebuild and prove
Rebuild with build_command.py --person charity. Rebuild `A1_Sales/_Rep Kits/Charity Taylor.zip` (current zip is
2026-10-08, older than the folder). Old zip and old pieces go to _to_delete (do not delete).
Prove with a text scan of every file in her folder (pdftotext for pdf, xml for pptx and docx, stripped html):
0 hits for david@, "David Taylor" outside the licensed agent line, 385-213-7177, book-david, quick-call-with-david,
back-office-audit-30, atlas-one-15-minute-intro-call-hoswp. Every client facing piece has charity@ or 801-787-8154.
Render her Sales Kit at 1440 and 390 in Chromium: booking button present and opens book-charity.
