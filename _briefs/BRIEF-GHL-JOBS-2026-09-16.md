# BRIEF for the GHL-JOBS terminal: Run BC (membership headcount labels everywhere, commission agreement clean-up)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no questions,
answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the prior report
to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunBB.md` (Cowork already copied the
Run BB report there; overwrite is fine). Back up every file before editing. Commit and push. Repo assets go in
`_briefs/assets/run-BC-jobs/` (the GHL browser terminal owns `run-BC/`; never share a folder with it again).
No dashes in copy. Clients are in all 50 states.

Answers to Run BB's questions (Cowork, 2026-09-16 14:05):
1. California minimum wage 2026 is $16.90 an hour, confirmed against the DIR announcement
   (dir.ca.gov/DIRNews/2025/2025-118.html). Floor $70,304 is right. Add that URL to the STATE_MIN_WAGE comment.
2. Keep the three state tables. Mark them in the code comment "internal summary, confirm with counsel, refresh
   every January". Do not drop the other-state notes.
3. Yes, generate the Sales Commission Agreement in every state when Commissions Paid is on.
4. Confirmed: nothing outside the Master Kit links to the two retired pricing PDFs (Cowork grepped A1_Sales,
   the repo and every cadence email file; only build logs mention them).

## Job 1: membership headcount labels (David's decision 2026-09-16)
New labels. Essential: "1 to 20 employees, one state, you do most of it yourself." Professional: "15 to 50
employees, the owner is still the back office." Enterprise and Concierge unchanged.
Where a file carries the longer form with an hours clause, change only the headcount clause and keep the rest,
for example "1 to 20 employees, one state, under five hours a month. You do most of it yourself. No benefits
renewal to manage yet." and "15 to 50 employees, or five to fifteen hours a month. The owner is still the back
office."
Files known to carry the old text (grep each for "Under 20 employees", "About 20 to 50", "Twenty to fifty",
"20 to 50" and fix every hit):
- `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Pricing.html` and `.pdf` (re-render with headless
  Chromium; the sheet must still fit one Letter landscape page).
- `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Brochure.html` and `.pdf` (page 4 tier picker).
- `A1_Sales/Website/BRJ Pricing Page Package 2026-09-13/Atlas_One_Pricing_Page_SPEC.html` and
  `Atlas_One_Pricing_Page_SPEC_preview.pdf`, plus the two PDF copies in that same folder
  (`Atlas_One_Membership_Pricing.pdf`, `Atlas_One_Membership_Brochure.pdf`): replace them with the new renders.
- `Master_Kit/08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html` (tier descriptions).
- The Quick Quote in the repo and the portal Add services card, if their membership tier descriptions carry
  headcounts (grep "employees" near Essential/Professional).
- The Membership Schedule in `_INTERNAL (do not share)/tools/agreements/generate.py` if it carries headcounts;
  if so regenerate with generate.py (all 21 pairs, same as Run BB) and note it.
Then rebuild COMMAND (catalogue_check first), confirm the stamp, and write a two line note for Thomas at BRJ
saying the Essential and Professional headcount labels changed and what they now read, saved as
`A1_Sales/Website/BRJ Pricing Page Package 2026-09-13/Note_to_Thomas_headcount_labels_2026-09-16.txt`.
Plain words, no dashes, written the way David talks.

## Job 2: commission agreement clean-up (found in the Run BB audit)
In the W-2 builder the Sales Commission Agreement body prints two editorial sentences inside the document the
employee signs: "Default earning terms prepared by Atlas One for the Company's review; the Company's counsel
should confirm or adjust before signing." (section 4) and "Default terms prepared by Atlas One; the Company's
counsel should confirm before signing." (section 6). Remove both from the printed document. Put that guidance
where the builder's other field hints live (under the Commissions Paid fields, on screen only, never printed).
Confirm the Sales Commission Agreement still starts on its own printed page (page-break-before is at line 218;
check it applies to the commission block, not only the Hold Harmless page) by printing the $125,000 California
test to PDF and reading the page count and first line of each page with pdftotext.

## Job 3: verify
Headless Chromium 1440 and 390 on every edited HTML: zero console errors, no external requests, no dashes,
fonts embedded, the pricing sheet still one page. pdftotext each regenerated PDF and grep for the new labels
and for any leftover "Under 20" or "20 to 50". Screenshots in `_briefs/assets/run-BC-jobs/shots/`.

## Report
Built, Verification (list every file changed with old and new label text), Assumptions, Skipped, Questions for
David.
