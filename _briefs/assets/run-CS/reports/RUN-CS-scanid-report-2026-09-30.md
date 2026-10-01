# Run CS helper "scanid" report (Job 5 items 5 and 7, 2026-09-30)

Item A (Scan ID wired into person block tools) and Item B (booking links, website only) are done. No GoHighLevel UI or API touched, nothing sent, nothing deleted, nothing deployed.

## Item A: Scan ID

### Design choice and why
The decoder that reads PDF417 on every browser (ZXing, 336 KB) is far over the 150 KB line, and nine tools times 336 KB is too much. So the hand off design:
- Each tool carries one small shared module (about 12 KB, between `<!-- a1-scanid:start v1 -->` and `<!-- a1-scanid:end -->`, source `_INTERNAL (do not share)/scanid_module.html`). It puts a "Scan ID" button (icon plus text label, 48 px high) next to each person's name field and opens a full screen panel only when pressed.
- The panel decodes with the browser's own `BarcodeDetector` (Chrome, Edge, Android) from the live camera or a photo of the back barcode, and always has a paste box that takes a handheld scanner's typed text, raw AAMVA text, or the one line copied from the Scan ID page ("Copy for Atlas One tools"). Where the browser has no PDF417 detector (Safari on iPhone and iPad) the panel says so and points to the paste route.
- `Atlas_One_Scan_ID.html` itself now works offline everywhere: ZXing sits inside the file as a `text/plain` script and is only run when there is no native detector (the CDN script tag is gone, it used to need the internet). Nothing needs a relative path, so every tool works from file:// and from a COMMAND blob: tab.
- Nothing stored: no localStorage, sessionStorage, cookies or network; the pasted text is cleared when the panel closes. The module only reads `data-a1scan` marks on inputs, hidden in print (`@media print`).
- `apply_scanid.py "<MK>" [--check]` (in `_INTERNAL (do not share)`) is idempotent: puts the module just before the screen share block (so `apply_screenshare.py --check` still passes) and adds `data-a1scan` marks by id, label or generator. Added to `catalogue_check.py` as the check "Scan ID module and field marks on every person block tool".

### Tools wired (8 files, 12 views, button next to the name field of each person block)
In `MK/06 Calculators and Tools (NEW Aug 2026)/`:
1. W-2 Employee Onboarding Packet (Bilingual): four blocks: employee info (name, home address, date of birth), W-4 (first and middle initial, last, address, city state ZIP), I-9 (last, first, middle initial, address, city, state, ZIP, date of birth), direct deposit (name).
2. Independent Contractor Onboarding Packet (Bilingual): Contractor Information Sheet (name, address), W-9 (name, address, city, state, ZIP), direct deposit (name).
3. Independent Contractor Agreement Builder: contractor name and address.
4. NDA Builder: Party B name and address (Party A is Atlas One's own company, left alone).
5. W-2 At-Will Employment Agreement Builder: employee name and address.
6. Separation Letter Generator: employee name.
7. Disciplinary Write-Up Notice Generator: employee name.
8. Atlas One Business Tools (17 generators): Employee ID Card Maker (name), Offer Letter (candidate name and address), Direct Deposit, Payroll / Status Change, Offboarding Checklist (employee name).
The button label and panel switch to Spanish when the bilingual packets are set to Spanish.

Surveyed and left alone (no person typed in, or not a person block): Employee Handbook Builder, Safety Manual Builder (acknowledgement lines only), Certified Payroll Manager and Converter (company and signer), Health Quote Census Intake (company address, bulk employee census rows with dates of birth: skipped on purpose, it is a bulk table and a PII risk), Back Office Self Assessment, Onboarding Tracker, WC No Loss Letter, 07 New HR and Safety Docs (PDFs and CSV only, no HTML tools). Copies of the 17 generators inside the BRJ kit and the Website Package are website embeds, not touched.

### Scan ID page additions
- "Scan and open form" buttons (one constant `GHL_FORMS` at the top of the page script maps form id to URL and query keys). With a name already scanned the button says "Open form" and opens the form in a new tab with `?first_name=...&last_name=...`; otherwise the first tap scans and the second tap opens (a new tab opened after an async scan would be blocked by popup rules).
- Enabled (keys confirmed by the GHL lane's live prefill tests): Form A (PEO and quote request, `Cxqawj85qg4ULUl64nMc`, tested 2026-09-29) and Onboarding documents (`p0UoqkUnGEwvlc31q636`, tested 2026-09-17). Keys: `first_name`, `last_name`.
- One line note on the page: "The scanned values travel in the web address of the form, so use this on your own device."
- "Copy for Atlas One tools" copies an `A1SCAN:{...}` line the tool panels accept (the route for iPhone and iPad).
- Button contrast fixed (navy instead of periwinkle with white text), 48 px high.

### Forms whose field keys I could NOT confirm (the GHL lane must supply them; I did not guess)
- No key at all for address, city, state, ZIP or date of birth on any form: the lane's own Job 3 note (TERMINAL-GHL-live.md 2026-09-29) says no live form uses GHL's native Address, City, State, Postal Code or Date of birth elements; every address looking field is a custom text field with its own custom query key. So only name travels today.
- `first_name` and `last_name` are unconfirmed (no live test) on: Audit booking (`SHhITMEwWONx08AE4VJT`), Audit intake (`pUCVA3wZgAOMMVnZsb4c`), Intro call booking (`jnesTr2nZpXOsGddGLka`), Form B bookkeeping (`V2EzO3FlRnsthXfHUT7g`), Form C2 build this for me (`hxPZ7HEhqG57aoS61MqM`), Service sign up (`nmXxvIegefND7h0ULeXW`), Form D business insurance quote (`LguXr1X9YMjD4WHrJt9D`; its Business Mailing Address key `vOM54...` is also not in the notes). They are listed in `GHL_FORMS` with `keys:null`, so they get no button until the lane sets keys. Form 0 and the Free Assessment survey are deliberately left out.

### Proof (Playwright, Chromium and WebKit, venv from the preamble)
Script: `/private/tmp/claude-501/scratch/test_scanid.py` (and `test_scanpage.py`). A synthetic AAMVA payload (header glued to the first element, 9 digit ZIP, middle name) and a fake `BarcodeDetector`:
- 12 tool views, every person block, photo path and paste path, both browsers: 68 runs, 0 failures. Fields landed in the right inputs (name, first, first plus initial, last, street, city, state, ZIP, combined address, city state ZIP, date of birth in the format of the input, date inputs ISO), live previews and generator state updated (ID card name, offer address, letters show the name).
- localStorage, sessionStorage and cookies identical before and after; zero console errors; zero requests other than file:; scrollWidth equals 390 at a 390 viewport; every button 44 px or taller with the text "Scan ID".
- Scan ID page: paste parse fills all fields; "Open form" URL is exactly `https://api.leadconnectorhq.com/widget/form/p0UoqkUnGEwvlc31q636?first_name=Jordan&last_name=Smith`; native detector path fills; with no native detector the inline ZXing loads (`typeof ZXing` is object) and a headless camera denial shows a message instead of an unhandled error; "Copy for Atlas One tools" round trip into the Contractor Agreement Builder fills name and address; no storage, no console errors, no network, no sideways scroll.
- Screenshots (looked at): `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/scanid/` (`w2-chromium-390-button.png`, `w2-webkit-390-overlay.png`, `idcard-chromium-1440-button.png`, `scanid-chromium-390.png` and the rest, 1440 and 390, both engines).
- `apply_screenshare.py --check` passes (183 files). `a1-footer-person` and `a1-contact-person` counts unchanged in every file touched (0 and 0 in all Item A files).

### Not proven
A real PDF417 license barcode on a real camera was not available. The decode of real barcodes relies on `BarcodeDetector` and ZXing as built; the AAMVA parsing was tested only on a synthetic payload. David should scan his own license once (Chrome on the Mac or Android, and Safari on iPhone via the Scan ID page).

## Item B: booking links, website only

- `people.json`: added `company.website_booking` = `https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`; `people.david.booking` now `https://api.leadconnectorhq.com/widget/bookings/quick-call-with-david` (was the group link `book-david`); Charity's stays null. Nothing else in people.json touched. The lead must rebuild the generated outputs (COMMAND, Sales Kit, `_Rep Kits`) so they pick it up; the build regex for `book15` and `book30` already replaces whatever value the overlay and playbook CONFIGs hold.
- `catalogue_check.py` (only appended): `check_intro_calendar` fails if the intro calendar string is in any text file under the Marketing root (and the repo's `tools/`) that is not on `INTRO_CALENDAR_WEBSITE_ALLOW` (data, one comment per entry); it also asserts people.json holds the website link and david.booking no longer does. `check_scanid` added too. Both are in `CHECKS`. Full run: all other checks ok; the new guard flagged only the guard file itself, fixed by an allow entry, re-run of the guard alone: clean.
- Counts: 53 files used the intro calendar (52 under the Marketing root plus repo `tools/index.html`). 27 changed (34 replacements), 26 kept.
- Special cases: the KB sentence "The 15 minute intro is ..." became "The 15 minute call with David is <quick call link>". The Micah `README.txt` slug (split across two lines) and `00_EMAIL_TO_MICAH.txt` were edited in place. The WSA credit page keeps its utm parameters on the new link.
- IMPORTANT: the Micah packet zip another helper rebuilt may predate this edit and could still carry the old link. Rebuild it from the unpacked folder after this.
## Item B file lists

### Changed (27 files, 34 replacements)

- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_03_Construction.html (1)
- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_02_Dental.html (1)
- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_01_Audiology.html (1)
- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_04_Technology.html (1)
- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_05_Hospitality.html (1)
- A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_06_Professional_Services.html (1)
- A1_Sales/WSA Booth Demo 2026-10-15/Atlas_One_WSA_Credit_Page_2026.html (2)
- A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html (1)
- A1_Sales/A1 Playbook Sales/Atlas_One_Prospecting_Playbook_v1.html (1)
- A1_Sales/A1_Prospects_MKTG/00_EMAIL_TO_MICAH.txt (1)
- A1_Sales/A1_Prospects_MKTG/Atlas_One_for_Micah_ExcelHealth/README.txt (1)
- A1_Sales/A1 Playbook Sales/Atlas_One_Sales_Conversation_Playbook.html (1)
- A1_Sales/Atlas 1 Software and Licenses/Atlas_One_Software_Card_Portal_Add_Services.html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Certified Payroll Converter (WH-347) (Atlas One).html (2)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/NDA Builder (Atlas One).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Options (Atlas One).html (4)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html (2)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Employee Handbook Builder (Bilingual 50-State).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/COI to Workers Comp Premium Estimator (Atlas One).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Atlas One Savings Summary (Atlas One).html (2)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/W-2 At-Will Employment Agreement Builder (Atlas One).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Safety Manual Builder (Bilingual OSHA).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Atlas One Calculators (53 tools).html (1)
- HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Agreement Builder (Atlas One).html (1)
- HR_Docs/Atlas_One_Master_Kit/14 Service Content Library/Atlas_One_Service_Content_Library_KB.md (1)
- /Users/davidtaylor/Projects/atlas-one-intake-forms/tools/index.html (1)

### Kept on the website allow list (26 files)

- A1_Sales/Blog and Content/Atlas_One_Blog_Content_Brief_2026-09-11.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-10-ai-email-assistant-small-office.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-04-payroll-is-a-time-problem.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-14-what-atlas-one-actually-does.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-10-ai-email-assistant-small-office.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-07-group-health-under-50-employees.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/worth-watching-page.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-01-business-cannot-run-without-the-owner.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-01-business-cannot-run-without-the-owner.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-09-disorganized-business-six-fixes.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-15-home-by-five.md
- A1_Sales/Website/Atlas One for BRJ 2026-09-27/2 Software Marketplace/Atlas_One_Software_and_Licenses_WEBSITE_COPY.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-08-bookkeeping-cleanup.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-08-bookkeeping-cleanup.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-11-peo-vs-aso-vs-in-house.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-15-home-by-five.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/4_Interactive/DEMO-open-me-Home-by-Five.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-09-disorganized-business-six-fixes.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-07-group-health-under-50-employees.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/3_Markdown/blog-11-peo-vs-aso-vs-in-house.md
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-04-payroll-is-a-time-problem.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/blog-14-what-atlas-one-actually-does.html
- A1_Sales/Blog and Content/Blog Set V1 (2026-09-11)/2_Web_paste/worth-watching-page.html
- A1_Sales/Website/BRJ Software Marketplace Package 2026-09-26/Atlas_One_Software_and_Licenses_WEBSITE_COPY.md
- A1_Sales/Atlas 1 Software and Licenses/Atlas_One_Software_and_Licenses_WEBSITE_COPY.md
- HR_Docs/Atlas_One_Master_Kit/Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html
## Files created or changed outside the lists above
- Created: `_INTERNAL (do not share)/scanid_module.html`, `_INTERNAL (do not share)/apply_scanid.py`.
- Edited: `_INTERNAL (do not share)/people.json` (booking keys only), `_INTERNAL (do not share)/catalogue_check.py` (appended two functions, an allow list and three lines in CHECKS; backup in the scratch dir).
- Item A tool files: the 8 files listed under "Tools wired", plus `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Scan_ID.html`.

## price_scan
No prices touched. Full `catalogue_check.py` ran: price checks all ok. Waived hits listed by it are all Dr Gould files (another lane).

## Assumptions
1. Spanish strings in the panel and button were written by me, not reviewed by a translator.
2. "Website pages" for the allow list = everything under `A1_Sales/Blog and Content/`, `A1_Sales/Website/`, the Software and Licenses WEBSITE_COPY.md, and the BRJ kit `templates.html`, per the brief.
3. Name only goes to GHL forms because no address keys are confirmed; middle name is not sent.
4. Party A in the NDA Builder and the company fields in every builder are not scan targets (they are the business, not a person).
5. Census Intake and the Employee Handbook were not wired (bulk rows and acknowledgement lines).
6. David's booking changed from the group page to the single Quick call calendar in people.json, as instructed, so every footer that uses `booking` now links the one calendar.

## Skipped
- Real barcode test (no license or physical camera in the headless run).
- Rebuilding COMMAND, Sales Kit and rep kits (lead owns them; the Scan ID file inlined into COMMAND will be bigger, about 840 KB).

## Questions for David
1. Which other GHL forms should get a "Scan and open form" button? The GHL lane needs to confirm `first_name` and `last_name` (and any custom address keys) on the forms listed under "could NOT confirm".
2. Should the Health Quote Census Intake get a Scan ID per employee row? I left it out.
