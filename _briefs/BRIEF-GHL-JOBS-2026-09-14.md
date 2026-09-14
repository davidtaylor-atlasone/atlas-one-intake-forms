# BRIEF-GHL-JOBS (current run: Run AM, files only, short): two Portal fixes David found on 2026-09-14

Rules as always (no questions, live log TERMINAL-GHL-JOBS-live.md, report RUN-GHL-JOBS-report.md via quoted
heredoc, commit and push, never delete: mv to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-14/`).

## Job 1: the Portal card "Everything Atlas One handles (public page)" shows PDF gibberish
`_INTERNAL (do not share)/build_portal.py` line 31 points that catalogue entry at
`A1_Sales/Atlas_One_Everything_We_Handle.pdf`, and the single-file Portal inlines it as text. Fix: copy the
page's HTML (`repo:tools/what-we-do/index.html`, the live one) into the Master Kit as
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Everything_We_Handle.html` (self-contained already; confirm
zero external requests offline) and point the catalogue entry at that file. Keep the blurb. The PDF stays in
A1_Sales for attaching. Rebuild the Portal with build_portal_single.py (path argument), open that card inside
the Portal in headless Chromium, screenshot, confirm the page renders (hero, six cards) and the stamp is today.
Also confirm the Tools Hub and Master Hub cards for this page point at the live URL or the HTML, never the PDF
as an inline page.

## Job 2: "Have Atlas One build this for me" reads vague
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Build_This_For_Me.html` (and the hosted copy in
`repo:build/index.html`; keep both identical). The white box today says: "Tell David which document you need.
Email him with the document name already filled in, or book the 30 minute call and walk through it together."
Rewrite the box so the reader knows exactly what happens, in David's plain voice, no dashes:

Title chip: "Which document?" stays, but make it a real picker: a dropdown of the eleven builders (Employee
Handbook, Safety Manual, W-2 At-Will Agreement, Contractor Agreement, NDA, Disciplinary Write-Up, Separation
Letter, W-2 Onboarding Packet, 1099 Onboarding Packet, Enrollment Guide, Other) that pre-selects the one the
visitor arrived from (the page already receives the document name; keep that) and can be changed.
Under it, four short fields: Company name, Number of employees, States you operate in, When you need it.
Copy above the buttons: "Pick the document, answer the four questions, and click Email David. Your email opens
already written with those answers so nothing is left to explain. David builds it around your business, reviews
it with you, and sends it back ready to sign, usually within five business days. If it is easier to talk it
through, book the 30 minute call instead and bring the same four answers."
Buttons stay: "Email David" (mailto with subject "Build this for me: <document>" and a body that lists the four
answers plus "Anything else I should know:" on its own line) and "Book a 30 minute call" (group booking link).
Keep "Or call 385-213-7177." Fields are optional; the email still opens if they are blank. Render at 390 and
1440, screenshot, click Email David in the headless browser and read the generated mailto to confirm the body.
Push the repo copy, confirm forms.atlasonesolutions.com/build/ returns 200 with the new copy. Rebuild the Portal.

## Report: paths, screenshots looked at, the mailto body as generated, assumptions, Questions for David.
