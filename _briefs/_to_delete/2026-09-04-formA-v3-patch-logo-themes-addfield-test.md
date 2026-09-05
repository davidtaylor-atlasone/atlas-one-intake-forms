# Claude Code brief: Form A v3 patch + logo + Themes survey + the add-field test (2026-09-04)
Supersedes every earlier brief in this folder. Design v2 CSS and the "Get My Quote" button are already applied and verified; do not redo them.

Rules: use my Chrome browser. Navigate in-app (Sites > Forms > click the form); builder takes ~30s to paint. Form A = "Atlas One — PEO / Prospect Quote Request", ID Cxqawj85qg4ULUl64nMc, Draft. Never Publish. Never delete or re-add a field on Form A. Never touch HIPAA. Rendered checks: https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc (hard-reload, clear "Submission in progress" with Start over). Assets: /Users/david/Projects/atlas-one-intake-forms/_briefs/assets/

## TASK 0: the add-field test, on a SCRATCH form (never Form A)
Goal: settle whether a field can be ADDED to a form WITHOUT the drag gesture. Sites > Forms > Add Form > blank. Name it "ZZ scratch add-field test". In the left panel (Quick Add / Custom Fields / Standard Fields) try, each on a DIFFERENT tile, and report which adds a field to the canvas:
 a) single-click the tile
 b) double-click it
 c) hover it and look for a "+" / "Add" icon, click that
 d) Tab focus onto the tile, press Enter, then try Space
 e) the computer tool's left_click_drag from tile to canvas; then a manual sequence: mouse down on tile, move in 4 small steps into the canvas, mouse up
If any method adds fields: add three (A, B, C) and report where each lands (bottom? below the selected canvas field?). Open a canvas field's settings and look for any move up / move down / reorder control; screenshot the panel. Leave the scratch form as a Draft (or unsaved), never publish, and tell me its exact name so David can delete it. This result decides whether you can build Form B yourself, so be thorough and literal.

## TASK 1: logo swap + Themes survey (Styles panel, no drag)
1a) In Form A: Styles & Options > find the header/logo image setting. Replace the current logo (it has a white background baked in) with assets/a1-namemark-fullcolor-transparent.png if the current one is the stacked "A1 / Solutions" lockup, otherwise assets/a1-primary-fullcolor-transparent.png. Width about 240px. Save.
1b) Styles & Options > Themes tab. Do NOT apply any theme. Screenshot the gallery (scroll through all of it, multiple screenshots if needed) and list every theme name. Also open the Layout section and list its options verbatim (columns, image position, etc.). Also note where "Background image" lives under Colors & Background. Report only; change nothing except 1a.

## TASK 2: small CSS patch, appended ADDITIVELY after the v2 block (currently ends ~line 270)
Styles & Options > Advanced > Custom CSS. Cmd+End, Enter twice, enter this block. Touch nothing above. Save.

/* === A1 v3 patch (2026-09-04) === */
.fields-container:not(:first-of-type)::before, .fields-container:not(:first-of-type)::after { content: none !important; display: none !important; }
.standard-checkbox-container input[type=checkbox], .standard-radio-container input[type=radio], .in-r-c input[type=checkbox] { width: 20px !important; height: 20px !important; min-width: 20px !important; border-radius: 5px !important; }
.standard-radio-container input[type=radio] { border-radius: 50% !important; }
.form-control, .multiselect__tags { background: #f3f6fb !important; border-color: #d5deea !important; }
.form-control:focus, .multiselect--active .multiselect__tags { background: #ffffff !important; }
.image-layout-container img, .image-layout-top-fixed img { background: transparent !important; box-shadow: none !important; padding: 0 !important; }
.form-builder--wrap { box-shadow: 0 24px 60px rgba(35,48,77,0.12), 0 2px 6px rgba(35,48,77,0.06) !important; }

## TASK 3: verify on the rendered widget (hard-reload)
Confirm: title/subtitle appear ONCE (nothing repeated below the footer); logo has no white box; checkboxes measure 20px; inputs are a faint blue-grey tint that turns white on focus; payroll reveal on PEO Payroll still works. Screenshot top of form and the checklist. Hard-reload the builder and confirm brand CSS intact from line 1.

## REPORT, in this order
Task 0 (method that works, where fields land, reorder controls, scratch form name). Task 1 (logo swapped yes/no; theme names; layout options verbatim; background-image location). Task 2 line range. Task 3 pass/fail with screenshots. Form A left as a Draft.
