# Claude Code brief: Form A design pass v2 (2026-09-04). Supersedes the "headers-followup" brief.

Same rules as before. Use my Chrome browser. Navigate in-app (Sites > Forms > click the form); the builder takes ~30s to paint. Form A only: "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc, Draft. Never Publish. Never drag. Never delete or re-add a field. Never touch HIPAA. Widget for rendered checks: https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc (hard-reload, clear "Submission in progress" with Start over).

This CSS was prototyped live on the rendered widget by Cowork and verified: hidden-field gaps collapse, the payroll reveal still fires with it in place, checkboxes render dark with a periwinkle checked state. Apply it as written.

## TASK A: append the block below to Custom CSS, ADDITIVELY
Styles & Options > Advanced > Custom CSS. Do NOT touch any existing line (brand CSS at the top, or the "A1 section headers" block you added). Cmd+End, Enter twice, then enter this block. The editor auto-formats; that is fine. Save (not Publish).

/* === A1 design v2 (added 2026-09-04) === */
body, .hl_form-builder--main-full, .hl-app { background: #eef2f7 !important; }
.form-builder--wrap { background: #ffffff !important; border: 1px solid #e3eaf2 !important; border-radius: 20px !important; padding: 28px 48px 40px !important; box-shadow: 0 24px 60px rgba(35,48,77,0.10), 0 2px 6px rgba(35,48,77,0.05) !important; margin: 32px auto !important; }
.fields-container { background: transparent !important; border: 0 !important; border-radius: 0 !important; box-shadow: none !important; }
.image-layout-container img, .image-layout-top-fixed img { background: #ffffff !important; padding: 12px 28px !important; border-radius: 16px !important; box-shadow: 0 6px 18px rgba(35,48,77,0.08) !important; }
.form-side::before { content: "ONE CALL SOLVES EVERYTHING."; display: block; width: 100%; text-align: center; font-family: 'DM Sans', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.16em; color: #788de3; margin: 6px 0 8px; }
.fields-container::before { content: "Tell us about your business."; display: block; width: 100%; flex: 0 0 100%; order: -2; text-align: center; font-family: 'DM Sans', sans-serif; font-size: 28px; font-weight: 700; letter-spacing: -0.01em; color: #23304d; margin: 0 0 6px; }
.fields-container::after { content: "Takes about 5 minutes. Only the sections you pick will open up."; display: block; width: 100%; flex: 0 0 100%; order: -1; text-align: center; font-family: 'DM Sans', sans-serif; font-size: 15px; color: #5b6784; margin: 0 0 28px; }
.form-field-wrapper:has(.d-none) { display: none !important; }
.form-field-wrapper { margin-bottom: 22px !important; }
label, .field-label { font-family: 'DM Sans', sans-serif !important; font-size: 14px !important; font-weight: 600 !important; color: #23304d !important; margin-bottom: 8px !important; }
.form-control, .multiselect__tags { min-height: 48px !important; border: 1.5px solid #cfd9e6 !important; border-radius: 10px !important; background: #fafaf8 !important; box-shadow: none !important; font-size: 16px !important; color: #23304d !important; }
.form-control { height: 48px !important; }
textarea.form-control { height: auto !important; min-height: 120px !important; }
.multiselect { border: 0 !important; background: transparent !important; }
.form-control:focus, .multiselect--active .multiselect__tags { border-color: #788de3 !important; background: #ffffff !important; box-shadow: 0 0 0 4px rgba(120,141,227,0.18) !important; outline: none !important; }
.form-control::placeholder { color: #8a94a8 !important; }
.multiselect__tag { background: #eef1fc !important; color: #23304d !important; border: 1px solid #788de3 !important; }
input[type=checkbox], input[type=radio] { width: 20px !important; height: 20px !important; border: 1.5px solid #23304d !important; background-color: #ffffff !important; border-radius: 5px !important; flex: 0 0 20px !important; margin-right: 10px !important; cursor: pointer !important; }
input[type=radio] { border-radius: 50% !important; }
input[type=checkbox]:checked, input[type=radio]:checked { background-color: #788de3 !important; border-color: #788de3 !important; }
.standard-checkbox-container label, .standard-radio-container label { font-weight: 400 !important; font-size: 15px !important; color: #23304d !important; margin-bottom: 0 !important; }
.form-builder--item.heading-element:has(h1, h2, h3) { margin-top: 34px !important; padding-top: 22px !important; border-top: 1px solid #e3eaf2 !important; }
.form-builder--item.heading-element:not(:has(h1, h2, h3)) { border-left: 0 !important; padding-left: 0 !important; margin-top: 8px !important; }
.form-builder--item.heading-element h1, .form-builder--item.heading-element h1 *, .form-builder--item.heading-element h2, .form-builder--item.heading-element h2 *, .form-builder--item.heading-element h3, .form-builder--item.heading-element h3 * { font-size: 20px !important; text-align: left !important; }
button.btn, .btn.button-element, button[type=submit] { width: 100% !important; height: 54px !important; background: #788de3 !important; color: #ffffff !important; border: none !important; border-radius: 12px !important; font-family: 'DM Sans', sans-serif !important; font-size: 16px !important; font-weight: 600 !important; box-shadow: 0 8px 20px rgba(120,141,227,0.35) !important; }
button.btn:hover, .btn.button-element:hover { background: #23304d !important; }
a { color: #788de3 !important; }

## TASK B: rename the Submit button
In the builder, click the Submit button element and change its text from "Submit" to "Get My Quote". If there is a "submitting" / loading label, set it to "Sending...". Save.

## TASK C: verify on the rendered widget (hard-reload)
Confirm: page background light blue-grey with a white rounded card; eyebrow "ONE CALL SOLVES EVERYTHING." + title "Tell us about your business." + subtitle above the first field; NO blank gaps between "Which core services" and the "Workers Compensation" heading; headings left-aligned with periwinkle left rule and a thin top divider; Privacy/Terms footer has NO left rule; checkboxes in "Quote or explore" are clearly visible (dark outline), and one clicked turns periwinkle with a white check (uncheck it after); button reads "Get My Quote"; selecting PEO Payroll still reveals the payroll block. Screenshot the top of the form, the checklist, and the button. Then hard-reload the builder and confirm the brand CSS is intact from line 1.

## TASK D: one negative test on the payroll reveal (read only)
Hard-reload the widget. In "Which core services", select ONLY "Benefits Administration". Report whether the payroll block stays hidden. (Intended: hidden. The rule should fire only on PEO Payroll, ASO Payroll, HCM Self-Service (Basic), HR Support.)

## REPORT
Task A line range added. Task B done or not. Task C each item pass/fail with screenshots. Task D result. Form left as a Draft.
