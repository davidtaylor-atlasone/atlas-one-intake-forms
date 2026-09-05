# Claude Code brief: STUDIO RUN (2026-09-05). Runs unattended. Phase 1 then Phase 2. Stop at any FAIL and report.

Rules: use my Chrome browser. Navigate in-app (Sites > Forms > click the form); builders take ~30s to paint. Never Publish. Never touch HIPAA. Never delete a field that a rule references (drag it instead). Never rename a dropdown OPTION. Save often (Save is not Publish). BEFORE ANY EDIT resize the Chrome window to at least 1512px wide and confirm the Save button is visible; below ~1400px it is clipped and NOTHING autosaves. Never edit in a builder tab opened before the latest save. If a page renders blank, check for ?logout=true and stop. Permission prompts: proceed.
 FORM A = "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc. Widget https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc
 FORM B = "Atlas One — Accounting, Bookkeeping & Payroll — Service Request.", ID V2EzO3FlRnsthXfHUT7g. Widget https://api.leadconnectorhq.com/widget/form/V2EzO3FlRnsthXfHUT7g
Widget checks: hard-reload; clear "Submission in progress" with Start over; use element refs, not coordinates, when the page shifts.

## PHASE 1: v3 CSS fix on BOTH forms
For EACH form: Styles & Options > Advanced > Custom CSS. Cmd+End, Enter twice, append the block below (touch nothing above). Save.

/* === A1 v3 fix (2026-09-04) === */
#_builder-form .standard-checkbox-container input[type=checkbox], #_builder-form .in-r-c input[type=checkbox], #_builder-form input[type=checkbox] { width: 20px !important; height: 20px !important; min-width: 20px !important; border-radius: 5px !important; }
#_builder-form .standard-radio-container input[type=radio], #_builder-form input[type=radio] { width: 20px !important; height: 20px !important; min-width: 20px !important; border-radius: 50% !important; }
#_builder-form .form-builder--item input.form-control, #_builder-form .form-builder--item textarea.form-control, #_builder-form .multiselect__tags { background: #f3f6fb !important; border-color: #d5deea !important; }
#_builder-form .form-builder--item input.form-control:focus, #_builder-form .form-builder--item textarea.form-control:focus, #_builder-form .multiselect--active .multiselect__tags { background: #ffffff !important; }
.fields-container::before, .fields-container::after { content: none !important; }
#_builder-form .form-side > .fields-container::before { content: "Tell us about your business." !important; }
#_builder-form .form-side > .fields-container::after { content: "Takes about 5 minutes. Only the sections you pick will open up." !important; }

Verify each widget: title/subtitle exactly once (nothing below the footer); checkboxes 20x20; inputs #f3f6fb, white on focus; logo is the transparent Full Mark (no white box); Form A: PEO Payroll reveals the payroll block; Form B: Monthly bookkeeping reveals the 4 bookkeeping fields. If the title appears ZERO times, report the .fields-container parent chain and STOP.

## PHASE 2: Form A structure polish (drag work; you can drag with left_click_drag; drop position = placement; the blue "+" under a selected canvas field anchors an insert slot)
2a) Custom fields. Settings > Custom Fields (main app, not the builder). Check whether these exist; create any that are missing, object Contact, type Number: "# Full-time W-2 Employees" and "Estimated Annual Gross Revenue ($)". Do not rename anything else.
2b) Contact block to the top. In Form A's builder, drag existing canvas fields by their grip handle so the top of the form reads, in order: First Name, Last Name, Email, Phone (each 50%), then Legal Business Name (100%), DBA / Trade Name (50%), FEIN / EIN (50%), Entity Type (50%), then "Which core services..." and everything else unchanged. Tip: Cmd+minus twice so the whole form fits, then zoom back. Save after every 4 to 6 drags.
2c) Section headings. Drag in three Heading elements and set their text: "Your contact information" directly above First Name; "Your business" directly above Legal Business Name; "What would you like quoted?" directly above "Which core services...". Match the existing heading style (they inherit the CSS automatically).
2d) Two new fields inside the payroll block. Drag "# Full-time W-2 Employees" (custom) to sit directly ABOVE "# Part-time W-2 Employees"; set width 33%, and set # Part-time W-2 and # 1099 to 33% so the three sit on one row. Drag "Estimated Annual Gross Revenue ($)" directly BELOW "Estimated Annual Gross Payroll ($)"; both 50%. Then open Conditional Logic and ADD both new fields as targets of the existing payroll Show Fields rule (trigger "Which core services..." Is Equal To PEO Payroll OR ASO Payroll OR HCM Self-Service (Basic) OR HR Support). Then tick Hidden on both new fields (they are text/number fields, so the box exists). Save.
2e) Verify on the Form A widget, hard-reloaded: order at the top is heading, First, Last, Email, Phone, heading, Legal Business Name, DBA, FEIN, Entity Type, heading, core services; on load the two new fields are hidden; selecting PEO Payroll reveals the block INCLUDING the two new fields; WC section reveals on "Do you currently have Workers' Comp coverage? = Yes"; benefits census section reveals on "Review or quote employee benefits? = Yes"; other-insurance policies reveal on its Yes. All 9 original rules plus the payroll rule must still fire. Screenshot the top of the form and the revealed payroll block.

## REPORT
Phase 1: per form, line range added, pass/fail per item. Phase 2: custom fields created or found; final top-of-form order; rule targets added; each 2e check pass/fail with screenshots. Both forms stay Draft. If anything failed, say exactly which step and leave the form saved in its last good state.
