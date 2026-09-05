# Claude Code brief: Form A headers + inventory + reveal check (2026-09-04)

Use my Chrome browser. GHL is at app.ridethehightide.com (location AzTPxnK2vSUj19jYoDmR). Navigate IN-APP (dashboard > Sites > Forms > click the form); cold deep links render blank. If any page renders blank or spins, check the URL for ?logout=true, STOP, and tell me to re-sign-in. Do not keep clicking.

Work ONLY on Form A: "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc. It is a Draft. Never click Publish. Never drag anything. Never delete or re-add a field. Never touch the HIPAA feature. Task 1 (payroll hidden-on-load + reveal on PEO Payroll) is already verified; do not redo it.

## TASK A: finish the reveal check (rendered widget, read only)
Open the public widget URL you used last time (https://link.ridethehightide.com/widget/form/Cxqawj85qg4ULUl64nMc). Hard-reload between trials. In "Which core services would you like included in your quote?" select, one at a time, ASO Payroll, then HCM Self-Service (Basic), then HR Support. For each, report whether the payroll block (Current Payroll Provider, # Part-time W-2, # 1099, Pay Period Frequency, Est Annual Gross Payroll, Description of operations, the payroll upload, and the "Payroll uploads ROI Comparison." heading) reveals. Also confirm "Are you using a PEO?" reveals with the block. Report a simple pass/fail per option.

## TASK B: element inventory (read only)
From the rendered widget DOM (fallback: the builder canvas visually), list every element on Form A in order, top to bottom, with its type (field, heading, text, upload) and whether it is hidden on load. Then answer yes/no: (1) does a "# Full-time W-2 Employees" field (or any full-time headcount field) exist? (2) does "Estimated Annual Gross Revenue" exist? Do not add anything.

## TASK C: section headers, fixed via Custom CSS, ADDITIVELY
Step 1, inspect first. On the rendered widget, inspect a section heading such as "Workers Compensation". Report the exact tag, classes, and where the underline and serif come from (inline style, a <u> tag, or a stylesheet rule). Read its computed font-family, font-size, text-decoration.

Step 2, write CSS that targets what you actually found. Use the block below as the base and adjust the selectors to the real tag/class from Step 1. Keep the values.

/* === A1 section headers (added 2026-09-04) === */
.form-builder--item h1, .form-builder--item h2, .form-builder--item h3,
.form-builder--item h1 *, .form-builder--item h2 *, .form-builder--item h3 *,
.hl-text h1, .hl-text h2, .hl-text h3 {
  font-family: 'DM Sans', Arial, sans-serif !important;
  font-size: 18px !important;
  font-weight: 600 !important;
  line-height: 1.3 !important;
  color: #23304d !important;
  text-decoration: none !important;
  border-bottom: none !important;
  margin: 18px 0 6px 0 !important;
  padding: 0 0 6px 10px !important;
  border-left: 4px solid #788de3 !important;
}
.form-builder--item u, .hl-text u { text-decoration: none !important; }

Step 3, apply it. In the builder go to Styles > Custom CSS. That editor is narrow and clips horizontally. Do NOT select-all and do NOT edit or delete any existing line. Click into the editor, press Cmd+End so the cursor is after the last character, press Enter twice, paste the block. Click Save (not Publish).

Step 4, verify. Hard-reload the builder and confirm the original brand CSS lines are still present above the new block. Then hard-reload the public widget and confirm the headings now render in DM Sans, #23304d, no underline, with the periwinkle left rule. Screenshot one heading before and after. If they did NOT change, report the exact selector you observed and stop; do not keep guessing with more CSS.

## REPORT
Short report in this order: Task A pass/fail per option; Task B inventory plus the two yes/no answers; Task C the selector that worked and before/after. Leave the form as a Draft.
