# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CO, 2026-09-27). Digital business cards, the safety quiz split and Spanish, and the contact@ sweep. All three are carry overs from Run CN.

Installed by chat A1 GHL Jobs 3 after its on disk audit of Run CN (`_BUILD-LOG/COWORK-AUDIT-run-CN-2026-09-27.md`, read
it first). Run CN's brief is archived at `_BUILD-LOG/BRIEF-GHL-JOBS-runCN-done-2026-09-26.md`.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the
portal repo. No questions mid run. No sends, no spending, no new vendors. Job 1 (cards) is built on a local branch
`cards-draft` and NOT pushed or merged; everything else may push the intake forms repo main as usual. Deleting is a
move into `Master_Kit/_to_delete/superseded-2026-09-27/`. No dashes in anything a client or prospect reads. Log to
`_BUILD-LOG/TERMINAL-GHL-JOBS-live.md` with a line when each job STARTS and when it ends; finish with
`_BUILD-LOG/RUN-GHL-JOBS-report.md` (archive Run CN's report to `_to_delete/superseded-2026-09-27/` first). Name this
run "GHL-JOBS Run CO" everywhere. Keep every Run CL, CM and CN guard on. Order: Job 1, Job 2, Job 3, Job 4. If the
run gets long, finish the job you are on, write the report and stop cleanly; never leave a build half written.

## Job 1: digital business cards (carried whole from Run CN Job 5, not started there)
The goal is not a paper card. It is the fastest way for a prospect to save David's contact in their phone: scan it off
his phone screen, scan it off a printed piece, or tap a link he texts them. Build and test need no approval.
Publishing waits for David's yes: build on a local branch `cards-draft` of atlas-one-intake-forms, commit, DO NOT push
or merge to main. Everything also saved to `A1_Sales/Business Cards/` (create), one folder per card.
The BUILD-INDEX line from earlier today that names a `david-cornerstone` card with the Cornerstone email and the 801
number is the superseded first draft. Do not build it.

Two cards for David, both on forms.atlasonesolutions.com, both Atlas One contact details:
- `david`: Atlas One only. The everyday card.
- `david-wsa`: dual brand for anything WSA. Atlas One Solutions logo and the Cornerstone PEO logo side by side, with
  the line "Atlas One Solutions, Cornerstone PEO's number one preferred back office partner" (the approved WSA
  wording from the booth demo work, do not invent a new one). Cornerstone logo:
  `1. A1 Solutions prospect_Client/1. Prospect - Client Folder Skeleton/0_Templates/PEO_Proposal_Generator_V4.5/brand_logos/cornerstone_peo.png`
  (copy it, do not move it). utm_campaign=wsa on its QRs.
Contact details on BOTH cards: David Taylor, Founder and President, Atlas One Solutions, david@atlasonesolutions.com,
380-225-5217 (380-CALL-A1S), booking link from people.json. Do NOT print the 385 cell (standing rule: it never appears
client facing; the 380 number forwards to it). Do NOT use the Cornerstone email or the 801 number on either card. A
`charity` card is built the same way (Atlas One only), held and not in the publish list until her mailbox exists; her
people.json booking is null, so her card hides the booking button until one exists. Read people.json for every
field; add a `cards` block there for the per card overrides (brand pair, campaign, title "Founder and President").

NO PHOTO. The logo is the hero. The bar is premium and distinctive, not a generic link in bio or template card look:
Atlas One brand per atlas-brand (four colors only, Horas display, DM Sans body, fonts embedded, no CDN), generous
spacing, the Full Mark lockup, a subtle soft blue and periwinkle treatment, crisp at 390 wide and on a Retina iPad.
Render screenshots and look at them before calling it done; if it looks like a stock template, redo it.

a) Phone page at `card/<slug>/index.html`: logo(s), name, title, tap to call, tap to email, "Book 15 minutes", and a
   large "Save my contact" button that downloads `<slug>.vcf`. Also a "Share" button using the Web Share API (falls
   back to copy link) so a prospect can forward it. noindex. The page reads utm_source, utm_medium, utm_campaign from
   its own URL and appends them to the booking link so a booked call carries the source into GHL.
b) vCard 3.0 `<slug>.vcf`: N, FN, ORG (Atlas One Solutions), TITLE, TEL work, EMAIL, URL (card page), second URL
   (booking), NOTE with the one line of what Atlas One does (and the Cornerstone line on the WSA card), PHOTO = the
   Atlas One logo mark as a square base64 JPEG under 40 KB so the contact shows the logo in the prospect's phone.
   Parse test with python vobject; confirm GitHub Pages serves .vcf as text/vcard (check the mime table GitHub Pages
   uses; the live check is David's after publish).
c) Two QRs per card, PNG and SVG, error correction H, quiet zone 4, logo mark in the center only if it still decodes:
   (1) page, `https://forms.atlasonesolutions.com/card/<slug>/?utm_source=business-card&utm_medium=qr&utm_campaign=<slug>`
   (the WSA card uses utm_campaign=wsa); (2) offline, the vCard inside the code (no photo). segno (pip install).
   Decode every PNG back with zbarimg or pyzbar and compare to the payload.
d) Show from my phone: a lock screen image 1179x2556 PNG per card (QR clear of the clock and the bottom buttons) AND
   a full screen "scan me" page `card/<slug>/show/` (big QR, logos, name, screen stays bright; add to home screen as
   an icon). David opens it and turns the phone around.
e) Text it: `A1_Sales/Business Cards/Text-my-card.txt` with a ready to paste text for each card (two short sentences,
   no dashes, the link with utm_source=text), plus steps in plain words to save it as an iPhone Text Replacement
   (Settings, General, Keyboard, Text Replacement, shortcut "a1card") so David types a1card and the message appears.
f) iPhone built in sharing, zero software: steps in plain words for David to fill his own My Card in iPhone Contacts
   with the same details and the logo as the photo, so NameDrop (phones held together) and Share Contact also work.
   Put it in `A1_Sales/Business Cards/HOW TO SHARE MY CARD.txt` with the lock screen, show page, text and NameDrop
   options on one page.
g) Print: `card-3.5x2.pdf` (front logos, name and contact; back the page QR; 0.125 in bleed, crop marks) and
   `card-full-page.pdf` (letter, for a booth table or front desk, both QRs labelled "Open my card" and "Save without
   internet"), per card.
h) Tests: Playwright WebKit with the iPhone 15 profile and Chromium with the Pixel 7 profile at 390 wide, zero console
   errors, Save returns the .vcf with the right content type, the booking link carries the utm values, screenshots to
   `_briefs/assets/run-CO-cards/`. The real phone check is David's after publish: list the three taps to do.
i) Tracking: GitHub Pages counts nothing. No third party analytics (spending, new vendor). Note for the GHL lane (already written in Run CN Job 4): add the GHL external tracking script to the card pages so scans count by
   utm_campaign. Until then the booking utm is the count.
j) QR plan (plan only, no piece changes this run except COMMAND): a table of every one pager, division sheet,
   handout, the Sales Kit and the WSA booth pieces, each with its QR destination and its own tracking label
   (utm_source=print, utm_medium=qr, utm_campaign=<short piece code>; WSA pieces point to david-wsa; rep builds swap to
   the rep's own card), where the QR sits, and how build_command.py stamps it. Save
   `A1_Sales/Business Cards/QR-plan-2026-09-26.md`, copy to `_BUILD-LOG/`. Build now: a "My card QR" button in COMMAND
   and in each `--person` build that opens that person's show page full screen (Charity's button is built but points
   at her held card).
k) Rules: no dashes in anything a prospect reads; the Run CL scanner still passes on Charity's kit; COMMAND catalogue
   row for the cards (Internal and rep). Report lists every file path and the exact publish step (merge `cards-draft`,
   push) for David's yes.

## Job 2: Safety Training Program quiz split and Spanish (carried from Run CN Job 1)
Folder `04 Safety Library/Safety Training Program/`.
- Add `q_es` and `a_es` to every quiz item in safety-calendar.json (24 months x 5). Plain, crew level Spanish, the same
  register as the existing Espanol talk text on the General Industry pages.
- Regenerate the 24 month pages so each prints three separate pages: (1) the talk (as today), (2) an employee quiz
  with NO answers, English question then Spanish under it, with name, date and score lines, (3) a supervisor answer key
  page. The sign in sheet headings get Spanish under the English (Nombre, Firma, Fecha, Calificacion).
- The 12 month calendar page gets Spanish under each month's topic.
- Update the two Connecteam import kits to carry the Spanish questions.
- Leave `Construction/Toolbox Talks (reused from Safety Library)/` where it is. Cowork found the source: the 28 talks
  exist only as `Atlas One — Complete Kit for BRJ/7. Safety Library (programs & checklists)/Excavation Toolbox Talks
  (28 EN and ES).zip`, so this folder is the only unzipped copy and the month pages may keep linking to it. Rename the
  folder to `Toolbox Talks (from the Safety Library zip)` and fix every link and the json.
- Print one month to PDF and prove the quiz and the answer key land on separate pages; headless 1440 and 390, zero
  console errors, screenshots.

## Job 3: finish the contact@ sweep (carried from Run CN Job 3)
Run CN built the guard (`check_role_and_support_emails` in catalogue_check.py) and it reports 40 hits. Clear them:
- support@ on a prospect or public piece becomes contact@ as the COMPANY line only, through people.json or the piece's
  source file, never by find and replace in a built file. First confirm each hit really is the company line; a hit that
  is an operational instruction for an existing client ("email support@ for payroll changes") stays and goes on a
  documented allow list in catalogue_check.py with the reason.
- The two role mailbox hits: info@ and sales@ in the Email Assistant Setup Intake form, bookkeeping@ in the Bookkeeping
  Intake Form. If they are a company contact line, make it contact@. If they are an address the client is asked to
  forward or connect as part of setup, they stay, on the allow list with the reason.
- Person line stays first everywhere; contact@ never replaces a person.
- Also fix the em dash in the Quick Quote catalogue item "Contract bundle — all three" (prospects see Quick Quote).
- The guard must end clean (zero hits outside the allow list). List every file changed.

## Job 4: rebuild and prove
Rebuild COMMAND, the shared Sales Kit and `--person charity`. Rerun the Run CL scanner over Charity's whole folder,
decoded blobs and PDF text (zero david@, zero David Taylor outside the licensed sentence, zero bare David, zero
cornerstone, zero scheduler.zoom.us, zero 385 phone number, zero dashes; line one charity@; company line contact@ on
her prospect pieces, support@ count zero). catalogue_check.py clean except the documented Price List retail note.
Headless 1440 and 390 on the david card page and show page, the safety calendar and one month page, and the Price
List; zero console errors; screenshots. Report with Charity's file count against Run CN (42).

## Waiting on David, do not do
Publishing the cards (merge and push `cards-draft`). The workers comp audit recovery percentage (25% on the Price List,
blank in prices.json). Nerdio or managed Azure virtual desktops as a service. Handing Charity her kit (her mailbox does
not exist yet). AnyCloud, Equinix, HPE, IBM, Meta, NexGen Technologies and Mirantis (TD SYNNEX lane).
