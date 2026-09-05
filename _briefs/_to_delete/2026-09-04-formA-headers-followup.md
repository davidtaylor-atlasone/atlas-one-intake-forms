# Claude Code brief: Form A header polish + one negative reveal test (2026-09-04, follow-up)

Same rules as the last brief. Use my Chrome browser. Navigate in-app (Sites > Forms > click the form); the builder takes ~30s to paint. Form A only: "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc, Draft. Never Publish. Never drag. Never delete or re-add a field. Never touch HIPAA. Widget host for rendered checks: https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc (hard-reload, clear any "Submission in progress" prompt with Start over).

## TASK A: two CSS edits, confined to the block YOU added last run (lines ~65 to 87)
Open Styles & Options > Advanced > Custom CSS. Do NOT touch anything above the "/* === A1 section headers" comment. Inside the new block only:
1. Add `text-align: left !important;` to the heading type selector (the one carrying font-family / color / text-decoration for h1, h2, h3 and their descendants), so the heading text sits against the periwinkle rule instead of centered.
2. Scope the wrapper selector that carries margin / padding / border-left so it excludes the footer text element: change `.form-builder--item.heading-element` to `.form-builder--item.heading-element:has(h1, h2, h3)` on that wrapper rule only.
Save (not Publish). Hard-reload the builder and confirm the original brand CSS is still intact from line 1.

## TASK B: verify on the rendered widget
Hard-reload the widget. Confirm all five section headings are left-aligned, DM Sans, #23304d, no underline, with the periwinkle left rule, and that the "Privacy Policy | Terms of Service" footer has NO left rule. Screenshot one heading and the footer.

## TASK C: one negative test on the payroll reveal rule (read only)
The rule is intended to fire on exactly four options: PEO Payroll, ASO Payroll, HCM Self-Service (Basic), HR Support. HR Support is intentional. To rule out "fires on any selection": hard-reload the widget, then in "Which core services would you like included in your quote?" select ONE option that is NOT one of those four (list the full option set first and tell me which one you picked). Report whether the payroll block stays hidden. If every option in the dropdown is one of the four, say so and skip.

## REPORT
Task A: what changed, line numbers. Task B: pass/fail with the two screenshots. Task C: the option list, the one you picked, hidden or revealed. Leave the form as a Draft.
