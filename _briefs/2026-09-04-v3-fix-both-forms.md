# Claude Code brief: v3 specificity fix on BOTH forms (2026-09-04)
Apply the same CSS block to two forms. Never Publish. Navigate in-app (Sites > Forms). Builders take ~30s to paint.
 FORM A = "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc
 FORM B = "Atlas One — Accounting, Bookkeeping & Payroll — Service Request." ID V2EzO3FlRnsthXfHUT7g

For EACH form: Styles & Options > Advanced > Custom CSS. Cmd+End, Enter twice, append the block below (touch nothing above). Save. On Form A it lands after the existing v3-patch block (~line 307). On Form B the CSS is a copy of Form A's, so it lands in the same place.

/* === A1 v3 fix (2026-09-04) === */
#_builder-form .standard-checkbox-container input[type=checkbox], #_builder-form .in-r-c input[type=checkbox], #_builder-form input[type=checkbox] { width: 20px !important; height: 20px !important; min-width: 20px !important; border-radius: 5px !important; }
#_builder-form .standard-radio-container input[type=radio], #_builder-form input[type=radio] { width: 20px !important; height: 20px !important; min-width: 20px !important; border-radius: 50% !important; }
#_builder-form .form-builder--item input.form-control, #_builder-form .form-builder--item textarea.form-control, #_builder-form .multiselect__tags { background: #f3f6fb !important; border-color: #d5deea !important; }
#_builder-form .form-builder--item input.form-control:focus, #_builder-form .form-builder--item textarea.form-control:focus, #_builder-form .multiselect--active .multiselect__tags { background: #ffffff !important; }
.fields-container::before, .fields-container::after { content: none !important; }
#_builder-form .form-side > .fields-container::before { content: "Tell us about your business." !important; }
#_builder-form .form-side > .fields-container::after { content: "Takes about 5 minutes. Only the sections you pick will open up." !important; }

Verify each form on its hard-reloaded widget (https://api.leadconnectorhq.com/widget/form/<ID>): title/subtitle appear exactly once (nothing below the footer); checkboxes 20x20; inputs #f3f6fb and white on focus; the logo is the transparent Full Mark (laptop mark + "A1 Solutions", no white box); on Form A the PEO Payroll reveal still works; on Form B "Monthly bookkeeping" reveals the four bookkeeping fields. If the title appears ZERO times on either form, report that form's .fields-container parent chain and stop.

REPORT: per form, line range added and pass/fail per item. Both forms stay Draft.

IMPORTANT: the builder Save button is clipped and invisible below ~1400px window width, and nothing autosaves. Resize the Chrome window to at least 1512px wide BEFORE editing, and confirm the Save button is visible. Never edit in a builder tab that was opened before the latest save; open the form fresh from Sites > Forms.
