# Claude Code brief: Form A design v3 + the add-field test (2026-09-04). Supersedes design-v2.

Rules: use my Chrome browser. Navigate in-app (Sites > Forms > click the form); builder takes ~30s to paint. Form A = "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc, Draft. Never Publish. Never delete or re-add a field on Form A. Never touch HIPAA. Rendered checks use https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc (hard-reload, clear "Submission in progress" with Start over). Assets for this brief are in /Users/david/Projects/atlas-one-intake-forms/_briefs/assets/.

## TASK 0: the add-field test, on a SCRATCH form, not Form A
Goal: settle whether you can ADD a field to a form WITHOUT dragging. Sites > Forms > "+ Add Form" (or New Form) > blank. Name it "ZZ scratch add-field test". In the left panel (Quick Add / Custom Fields / Standard Fields), try, in this order, and report which one adds a field to the canvas:
 a) single-click a field tile (e.g. "Phone" or any custom field)
 b) double-click it
 c) hover the tile and look for a "+" / "Add" icon, click it
 d) press Enter with the tile focused (Tab to it)
 e) the computer tool's left_click_drag from the tile to the canvas, then also a manual sequence: mouse down on the tile, move in 4 small steps into the canvas, mouse up
Try each on a DIFFERENT tile so results are unambiguous. Then, if any method added fields, test ORDER: add three fields (A, B, C) and report whether each new one lands at the bottom, and whether clicking a field on the canvas first changes where the next one lands (some builders insert below the selected field). Also check the field's own settings panel for any "move up / move down" control. Screenshot the panel. Leave the scratch form unsaved-or-saved as a Draft, do not publish; tell me its name so David can delete it. THIS RESULT MATTERS MORE THAN EVERYTHING BELOW: it decides whether you can build Form B yourself.

## TASK 1: layout and header image (Styles panel, no drag)
In Form A's builder open Styles & Options. Report the exact options under any "Layout" / "Image layout" / "Form layout" / "Theme" / "Template" control (one column, two column, single line, image top/left/right/background, etc.). Then:
 1a) Replace the header/logo image with assets/a1-primary-fullcolor-transparent.png (transparent PNG; the current one has a white box baked in). If the current logo is the stacked "A1 / Solutions" lockup use a1-namemark-fullcolor-transparent.png instead so the shape matches. Set its width to about 240px.
 1b) If an "image left" / "two column with image" layout exists, screenshot Form A with it applied using assets/a1-brand-photo-laptop.png as the side image, then REVERT to the previous layout before saving. That screenshot is for David to choose from; do not leave it applied.
Save.

## TASK 2: append the block below to Custom CSS, ADDITIVELY
Styles & Options > Advanced > Custom CSS. Do NOT touch any existing line. Cmd+End, Enter twice, enter the block. Auto-formatting is fine. Save.

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

## TASK 3: rename the Submit button
Click the Submit button element, change its text to "Get My Quote". If a loading label exists, "Sending...". Save.

## TASK 4: verify on the rendered widget (hard-reload)
Confirm: light blue-grey page with a white rounded card; eyebrow "ONE CALL SOLVES EVERYTHING." + "Tell us about your business." + subtitle above the first field; logo has NO white box; NO blank gaps between "Which core services" and "Workers Compensation"; headings left-aligned with periwinkle left rule and thin top divider; Privacy/Terms footer has NO left rule; checkboxes clearly visible, clicked one turns periwinkle with a white check (uncheck after); button reads "Get My Quote"; selecting PEO Payroll still reveals the payroll block. Screenshot top of form, the checklist, the button. Then hard-reload the builder and confirm brand CSS intact from line 1.

## TASK 5: negative test (read only)
Hard-reload the widget. In "Which core services" select ONLY "Benefits Administration". Payroll block should stay hidden. Report.

## REPORT, in this order
Task 0 (which method adds a field, where it lands, any move controls, scratch form name). Task 1 (layout options found, logo swapped, side-image screenshot path). Task 2 line range. Task 3. Task 4 pass/fail per item with screenshots. Task 5. Form A left as a Draft.
