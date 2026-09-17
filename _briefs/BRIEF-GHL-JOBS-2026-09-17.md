# BRIEF for the GHL-JOBS terminal: Run BI (COMMAND blank previews, coinsurance wording and health tool audit, onboarding packets: W-9 and handbook)

Terminal name: GHL-JOBS. Files and code only, headless Chromium for verification. Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END of the report. Back up the
prior report to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBH.md` (already copied;
overwrite is fine). Back up every file before editing. Commit and push. Repo assets in
`_briefs/assets/run-BI-jobs/`. No dashes in copy. Clients in all 50 states. Tools stay self contained and offline.
(The phone fix brief is parked as `BRIEF-GHL-JOBS-queued-phone-fix-runBJ.md` until David creates the new token.)

## Job 1: blank Preview and Open in COMMAND (David's report 2026-09-17)
David clicks Preview or Open on many items in `Atlas One COMMAND.html` (the Safety portal among them) and gets a
blank screen; on one the "Have Atlas One build this for me" bar shows over an empty page. Reproduce in headless
Chromium loading COMMAND from `file://`: for EVERY catalogue item, click Preview, wait, and record whether the
preview frame has a document with a non empty body (check `contentDocument` when same origin allows it, else the
frame's load event plus a screenshot); then click Open and record whether the new page loaded (title, body
length). Write `_BUILD-LOG/command-preview-audit-2026-09-17.md`: one row per item with Preview ok/blank, Open
ok/blank, and the console error. Then fix the causes you find. Likely causes to check first: the file:// iframe
restriction (rule 21: a file hub cannot always Preview a file doc in an iframe; the fallback is New tab), paths
with `#`, `?` or unusual characters not URL encoded, items whose path is a folder or a PDF/pptx/docx (those
must open in a new tab, never a frame), and the `#atlas-cta-banner` modal script from Run BD interfering with
the frame. The rule for the rebuilt COMMAND: Preview only for HTML tools that render in a frame; everything
else gets Open (new tab) only, and when a Preview fails the panel shows a one line message with an Open button
instead of a blank. Rebuild COMMAND with build_command.py, re-run the audit, and the report must show zero blanks.

## Job 2: coinsurance wording, and a full check of the health tools
1. Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`) Health step: the dropdown labelled
   "COINSURANCE IN YOUR PASTE MEANS" with "What the MEMBER pays (e.g. 30%)" and "What the CARRIER pays (e.g.
   70%)" is the paste normaliser, not a plan picker, and David read it as a two option plan list. Relabel:
   heading "How the carrier sheet shows coinsurance", options "As the member's share (10%, 20%, 30%)" and "As the
   carrier's share (90%, 80%, 70%)", helper line "Either way the comparison shows both, for example 80/20."
   Every plan card and every comparison table then shows coinsurance as "carrier / member", for example 80% / 20%
   and 100% / 0%, never a lone number.
2. In the same tool's "Add one by hand" plan form (and the current plan form) the coinsurance field becomes a
   picker: 100% / 0%, 90% / 10%, 80% / 20%, 70% / 30%, 60% / 40%, 50% / 50%, plus "Other" with a number box.
   The parser must accept 100, 100%, 100/0, 0, and treat them as a 100% plan.
3. Audit the rest for the same thing and for stale content: `10 Health Comparison Tool/Atlas_One_Health_Quote_Tool.html`,
   `health_compare.py`, `06 Calculators and Tools (NEW Aug 2026)/Health Comparison Builder (Atlas One).html`,
   `Health Quote Census Intake (Atlas One).html`, `A1_Sales/Atlas 1 Benefits/` (the Employee Benefits Menu and the
   Benefits & Retirement sheet), and the Benefits Routing Tool. For each: coinsurance shown as carrier / member;
   HSA and HDHP handled (2026 IRS HDHP minimum deductible and out of pocket limits: read them from the IRS page
   for 2026, cite the URL in the report); deductible embedded versus non embedded flagged where the tool cares;
   the one carrier under 500 lives rule (rule 14) still enforced; no vendor or broker names client facing; no
   dashes; fonts embedded; phone 380-225-5217. Write `_BUILD-LOG/health-tools-audit-2026-09-17.md` with a table
   (tool, finding, fixed yes/no) and fix everything that is a bug or a stale fact; list anything that is a
   judgement call under Questions.

## Job 3: onboarding packets, submit and the real W-9
Files: `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Onboarding Packet (Bilingual).html` and
`W-2 Employee Onboarding Packet (Bilingual).html`. Today both only Save and Print, the 1099 packet's W-9 is the
tool's own form not the IRS form, and the W-2 handbook acknowledgement links to nothing.
1. 1099 packet: add "Download the completed W-9" which fills the official IRS Form W-9 (current revision; fetch
   the PDF from irs.gov/pub/irs-pdf/fw9.pdf once, embed it as base64, fill its AcroForm fields with pdf-lib
   embedded, never a CDN). Map every packet field to the W-9 field names; box 3 tax classification, TIN, address,
   signature date. Keep the packet's own summary page too.
2. Both packets: add "Send to Atlas One" which opens, in a new tab, the GHL "Onboarding documents" form
   (Form D, the GHL terminal is building it as Run BI Part 33; until its id exists, point the button at
   `https://forms.atlasonesolutions.com/onboarding/send/` and create that page in the repo as a placeholder
   that says "David is finishing this page; email your documents to david@atlasonesolutions.com for now") with
   the worker's name, email, company and worker type prefilled through URL query parameters (GHL forms prefill
   standard fields from `?first_name=&last_name=&email=&phone=` and custom fields from their keys). The button
   also triggers the PDF download first so the person has the file to attach. Plain instruction text under the
   button: "Download the PDF, then attach it on the next page."
3. W-2 packet handbook acknowledgement: the acknowledgement text links to the handbook. Source order: a
   `?handbook=<url>` query parameter (David's link to that client's own handbook), otherwise the generic
   state handbook at `https://forms.atlasonesolutions.com/tools/handbook-basic/<STATE>.pdf`. Build those:
   drive `Employee Handbook Builder (Bilingual 50-State).html` headless for every state and DC with a neutral
   company name "Your Employer" and the builder's default policy set, print to PDF, and add a first page notice:
   "This is a general employee handbook for <State>, provided by Atlas One Solutions as a starting point. It is
   not legal advice and your employer's own handbook, where one exists, replaces it. Policies change; have counsel
   review before relying on it." Publish under `tools/handbook-basic/` in the repo (commit; David pushes if the
   classifier refuses). The packet's acknowledgement line reads "I have received and read the employee handbook
   (link)" with the link resolved as above, and the state comes from the packet's own state field.
4. Verify: fill the 1099 packet in headless Chromium, download the W-9, open the PDF with pymupdf and read the
   filled fields back; the W-2 packet with `?handbook=https://example.com/h.pdf` shows that link, without it
   shows the state link; the Send button opens the placeholder page with the query prefilled; zero console
   errors; no external requests except the two atlasonesolutions.com links when clicked; fonts embedded; 390 and
   1440; no dashes. Rebuild COMMAND (both packets are inlined), confirm the stamp.

## Report
Built, Verification (the two audit files summarized, the W-9 field readback, the handbook set count),
Assumptions, Skipped, Questions.
