# Claude Code brief: BUILD FORM B (Bookkeeping) end to end (2026-09-04)
You CAN add fields: the computer tool's `left_click_drag` from a left-panel tile to a canvas spot adds the field AT THE DROP POINT (proven on the scratch form). Nothing can reorder afterwards, so drop each field in its final position. Tip: select the canvas field you want to insert BELOW, click the blue "+" that appears under it, then drag the tile into that anchored slot.

Rules: use my Chrome browser. Navigate in-app (Sites > Forms). Builders take ~30s to paint. Never Publish anything. Never touch HIPAA. Never rename a dropdown OPTION. Do not touch Form A (Cxqawj85qg4ULUl64nMc) except to duplicate it. Save often (Save is not Publish). If a page renders blank, check for ?logout=true and stop.

## STEP 1: create Form B by duplicating Form A (carries styling, Custom CSS, logo, consent, submit)
Sites > Forms > Form A's three-dot menu > Duplicate (or Clone). Open the copy. Rename it EXACTLY:
Atlas One — Accounting, Bookkeeping & Payroll — Service Request.
Record the new form ID from the URL; call it FORM_B in your report.

## STEP 2: strip Form A's logic and non-shared fields from the copy
2a) Open Conditional Logic and DELETE every rule (they reference fields you are about to remove).
2b) KEEP these elements: First Name, Last Name, Phone, Email, Legal Business Name, the two consent checkboxes, the Privacy/Terms text, the Submit button. DELETE every other element (fields, headings, uploads). Save. Confirm the canvas shows only the kept elements, in this order: First Name, Last Name, Phone, Email, Legal Business Name, consent x2, Privacy text, Submit.

## STEP 3: drag in the fields, in this exact final order (Custom Fields group unless marked standard)
Final canvas order top to bottom. Items marked KEEP already exist; drop the new ones between them.
 1 First Name (KEEP, 50%, required)
 2 Last Name (KEEP, 50%, required)
 3 Phone (KEEP, 50%, required)
 4 Email (KEEP, 50%, required)
 5 Best Way To Reach You (custom, 100%)
 6 Legal Business Name (KEEP, 100%, required)
 7 Website (STANDARD field from Personal Info; do NOT create a custom one; 50%)
 8 Entity Type (Bookkeeping) (custom, 50%). TRAP: there is also "Entity Type" (Form A's, 7 options). Pick the one WITH "(Bookkeeping)" in its name, 9 options including "Not yet formed".
 9 Approximate Annual Revenue (custom, 50%)
10 Number of W-2 Employees (custom, 50%)
11 State(s) You Operate In (custom, 50%)
12 Services Requested (custom multi-checkbox, 100%, required)
13 Monthly Transaction Volume (custom, 100%, HIDDEN)
14 Current Accounting Software (custom, 50%, HIDDEN)
15 Are Your Books Current? (custom, 50%, HIDDEN)
16 Quote Access Method (custom, 100%, HIDDEN)
17 Pay Period Frequency (custom, 50%, HIDDEN). Its options must include "Not currently running payroll"; if missing, STOP and report (adding it is a Settings > Custom Fields job).
18 Payroll States (custom, 50%, HIDDEN)
19 Entity Formed Yet? (custom, 50%, HIDDEN)
20 States Needing Tax Accounts (custom, 50%, HIDDEN)
21 Tax Intro Timing (custom, 100%, HIDDEN)
22 Desired Start Timing (custom, 100%, required)
23 Anything Else We Should Know (custom, 100%)
24 consent checkboxes (KEEP)
25 Privacy/Terms text (KEEP)
26 Submit (KEEP); change its text to: Submit My Request
Save after every 4 or 5 drops. After all drops, hard-reload and confirm the order above.

## STEP 4: labels, widths, required, hidden (click work)
Relabel the DISPLAY label only (never the Custom Field Name):
 5 Best way to reach you · 6 Company Legal Name · 8 Entity Type · 9 Approximate annual revenue · 10 Number of W-2 employees · 11 State(s) you operate in · 12 What do you need help with? · 13 Monthly transaction volume · 14 Current accounting software · 15 Are your books current? · 16 How would you like to give us access for a quote? · 17 Pay frequency · 18 States your employees physically work in · 19 Have you formed your entity yet? · 20 Which states need tax accounts set up? · 21 When would you like the introduction? · 22 When would you like to begin? · 23 Anything else we should know?
Description on 13: A transaction is any single deposit, payment, charge, or transfer. Best estimate is fine.
Set widths, Required and Hidden per the list in STEP 3. Mark Hidden on 13 to 21 ONLY AFTER their rules exist (STEP 5), so nothing is stranded invisible. Save.

## STEP 5: conditional logic (4 rule groups). Operator is "Is Equal To" (GHL has no "contains"; on a multi-checkbox it includes-matches). Use "Show Fields" (plural). Never "Is Not Equal To".
Option strings, byte-exact (copy, do not retype): Monthly bookkeeping | Catch-up / clean-up of prior periods | Accounts Payable & Receivable | Payroll (W-2 / 1099) | Sales tax filings | Business formation & tax registrations | Tax prep / advisory | QuickBooks / software setup | Not sure — help me figure it out
 A) IF Services Requested Is Equal To "Monthly bookkeeping" OR "Catch-up / clean-up of prior periods" OR "Accounts Payable & Receivable" THEN Show Fields: Monthly Transaction Volume, Current Accounting Software, Are Your Books Current?, Quote Access Method
 B) IF Services Requested Is Equal To "Payroll (W-2 / 1099)" THEN Show Fields: Pay Period Frequency, Payroll States
 C) IF Services Requested Is Equal To "Business formation & tax registrations" OR Entity Type (Bookkeeping) Is Equal To "Not yet formed" THEN Show Fields: Entity Formed Yet?, States Needing Tax Accounts   (two different source fields in one OR group; both required)
 D) IF Services Requested Is Equal To "Tax prep / advisory" THEN Show Fields: Tax Intro Timing
Then set Hidden on 13 to 21. Save. Hard-reload and confirm all 4 rules and 9 hidden flags persisted.

## STEP 6: verify on the rendered widget https://api.leadconnectorhq.com/widget/form/FORM_B (hard-reload each trial, Start over on the resume prompt)
 - On load: 13 to 21 invisible; no blank gaps (the Form A CSS collapses hidden wrappers).
 - Each of the three bookkeeping options ALONE reveals 13, 14, 15, 16.
 - Payroll (W-2 / 1099) reveals 17 and 18.
 - Business formation reveals 19 and 20; separately, Entity Type = Not yet formed alone reveals 19 and 20.
 - Tax prep / advisory reveals 21.
 - Negative: only Sales tax filings, only QuickBooks / software setup, only Not sure: nothing appears.
 - Design matches Form A (card, eyebrow, title, headers, checkboxes, button). Button reads "Submit My Request".
Screenshot top, the services checklist, and one revealed group.

## REPORT
FORM_B id and name; the final element order as rendered; which of the 9 hidden flags and 4 rules persisted; each STEP 6 check pass/fail with screenshots; anything you could not do and why. Leave FORM_B as a Draft. Do not delete the scratch form (David will).
