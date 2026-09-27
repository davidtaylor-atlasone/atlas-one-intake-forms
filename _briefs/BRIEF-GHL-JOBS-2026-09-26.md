# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CN, 2026-09-26). Finish Run CM, fix its audit findings, the last two GL prices, contact@ as the company line, digital business cards, the TD SYNNEX catalog fix (Job 7, run before Job 6) and the build this for me flash plus two broken links (Job 8, run right after Job 0).

Installed by chat A1 GHL Jobs 3 after its on disk audit of Run CM (`_BUILD-LOG/COWORK-AUDIT-run-CM-2026-09-26.md`, read it
first). Run CM's brief is archived at `_BUILD-LOG/BRIEF-GHL-JOBS-runCM-done-2026-09-26.md`.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the
portal repo. No questions mid run. No sends, no spending, no new vendors. The only push allowed is the intake forms
repo main branch for Jobs 0 to 4; Job 5 (cards) is built on a local branch and NOT pushed or merged. Deleting is a
move into `Master_Kit/_to_delete/superseded-2026-09-26/`. No dashes in anything a client or prospect reads. Log to
`_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md` (Run CN, and put the Run CM
Job 6 results in it as its own section). No time limit; commit after each job, and write a log line when each job
STARTS as well as when it ends, so a stop mid job is visible. Screenshots to `_briefs/assets/run-CN-jobs/` (cards to
`_briefs/assets/run-CN-cards/`). Name this run "GHL-JOBS Run CN" everywhere. Keep every Run CL and Run CM guard on.

## Job 0: finish Run CM Job 6 (it stopped at the start)
Run CM rebuilt COMMAND and the shared Sales Kit at 12:58 MT and then stopped. Charity's folder is half built: only her
Sales Kit html, READ ME FIRST and an empty Division Sheets folder (it held 43 files). Her last full kit is in
`A1_Sales/_to_delete/superseded-2026-09-22/charity-kit-before-CH-9/` for comparison; do not copy it back, rebuild.
Find why the `--person charity` build stopped (look for an exception or a hung PDF render) and fix the cause, then
rebuild and confirm she has the same set of files as CH-9 (plus anything new since). Do Job 0 before anything else
and log the cause in the report. The Job 6 proof steps run once, at the end of this run, in Job 6 below.

## Job 1: fix the Run CM audit findings (details and paths in the audit file)
1. Audit Workbench (`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`) embeds an old copy of
   prices.json that still says the COI price is pending. Re-embed from prices.json at build time (or read it the
   same way the other tools do). Extend the catalogue_check.py guard: fail the build on the words "price pending" or
   "[__]" in any client or prospect piece, and on any embedded prices object that differs from prices.json.
2. catalogue.py line 153: the COI Tracking Schedule blurb still says "Price pending David." Rewrite it from the real
   tiers.
3. Price List (A1_Sales/Pricing and the rep kit copy): match prices.json's wording, not just its dollars. Handbook
   update and safety manual update are per update and included Professional and up (not "/yr"). Safety training
   done for you shows waived Enterprise and up, larger quoted, included in Concierge. COI done for you shows a month
   on each tier, over 100 quoted, included in Concierge up to 25 subs. Do NOT touch the workers comp audit line
   (Price List says 25%, prices.json says [__]%); that is a question for David, list it in the report.
4. Retire `09 Quick Quote Tool/Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html` (check catalogue.py first).
5. Safety Training Program (`04 Safety Library/Safety Training Program/`):
   - Company line only on the calendar and every month page: remove David's person line and the "Book 15 minutes
     with David" link. These are client service handouts, so the company line keeps support@.
   - Split the quiz: an employee quiz page with no answers (name, date, score lines) and a supervisor answer key on a
     separate printed page. The sign in sheet stays its own page.
   - Spanish: the calendar page in both languages, and the quiz questions and the sign in sheet headings in Spanish
     under the English. Add `q_es` and `a_es` to each quiz item in safety-calendar.json.
   - Do not duplicate talks: point to the Safety Library originals by relative path from the pages and from
     safety-calendar.json, then move `Construction/Toolbox Talks (reused from Safety Library)/` to
     `_to_delete/superseded-2026-09-26/`. Update the Connecteam import kit paths to match.
   - Print checklist names without the spaced hyphen.
   Rerender the calendar and two month pages at 1440 and 390, zero console errors, and print one month to PDF to show
   the quiz and the answer key land on separate pages.
6. Connecteam named on client pieces is allowed (it is a resold product like Microsoft 365 and QuickBooks). Leave it.

## Job 2: the last two GL converter prices (David approved 2026-09-26, after Run CM started)
Add to prices.json and to every price list Run CM put in lockstep (Quick Quote, Quote Cockpit, Price List and the rep
kit copy, Bookkeeping Marketing Sheet V8 section 05, the service content library via build.py, COMMAND and the Sales
Kit on rebuild):
- GL converter, Atlas One runs it and sends the files: $35 per payroll run.
- GL converter plus certified payroll bought together: one $300 setup, not $250 plus $300.
Update the two queued notes Run CM wrote (`BRIEF-PORTAL-queued-tool-pricing.md`, `BRIEF-GHL-queued-products.md`) with
both lines; they are unapproved there today. List every place with before and after in the report.

## Job 3: contact@ as the company line (Run CL Job 4, APPROVED 2026-09-26)
The rep must stay the prospect's contact. Rule, unchanged from the 2026-09-22 footer standard
(`_BUILD-LOG/contact-footer-and-rep-standard-2026-09-22.md`):
- Line one of every footer is the PERSON: the rep (or David) with their own name, email, phone and booking link. On
  anything a rep presents, the rep's line is there and it is the first contact.
- Line two is the COMPANY line. On public and prospect pieces it now reads contact@atlasonesolutions.com instead of
  support@. On client service pieces (portal, invoices, onboarding packets, agreements, client confirmations, the
  Safety Training Program handouts) it stays support@.
- Pieces with no person (website pages, public tools, calculators) carry only the company line with contact@.
- Guard in catalogue_check.py: AR@, AP@, Info@, Sales@, Bookkeeping@ never on public or prospect material
  (Bookkeeping@ only on the QuickBooks Accountant Access Guide); support@ never on a public or prospect piece;
  contact@ never replaces a person line.
Make the switch at the source (people.json gets a `contact_email` in the company block, build scripts choose it by
audience from catalogue.py), not by find and replace in built files. Rebuild COMMAND, the shared Sales Kit and
`--person charity`, and prove Charity's line one still reads charity@ on every piece.

## Job 4: queued notes for two other lanes (write the notes only)
- `_BUILD-LOG/BRIEF-GHL-queued-contact-routing.md` and `_BUILD-LOG/BRIEF-EMAIL-queued-contact-routing.md`: contact@ is
  an alias on David's mailbox. When a message to contact@ is about a prospect a rep owns, it must reach the rep: GHL
  assigns the contact to its owner and notifies them, the email assistant files it under that prospect and flags the
  owner. The routing is those lanes' job, not this terminal's. Never edit BRIEF-GHL.md or BRIEF-EMAIL.md.
- Add to `BRIEF-GHL-queued-products.md`: the five COI notices use `{{custom_values.client_company_name}}` and
  `{{custom_values.coi_upload_link}}`. GHL custom values are account wide, so with two or more contractor clients
  every notice would print the same company. The GHL lane must map both to a per contractor field when it loads the
  templates.
- Add to the same GHL note (Job 5 i below): the GHL external tracking script on the card pages.

## Job 5: digital business cards (from A1 DECKS WSA demo, decisions updated by David the evening of 2026-09-26)
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
   `_briefs/assets/run-CN-cards/`. The real phone check is David's after publish: list the three taps to do.
i) Tracking: GitHub Pages counts nothing. No third party analytics (spending, new vendor). Note for the GHL lane (Job
   4): add the GHL external tracking script to the card pages so scans count by utm_campaign. Until then the booking
   utm is the count.
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

## Job 6: rebuild and prove (this is also Run CM's missing Job 6)
Rebuild COMMAND, the shared Sales Kit and `--person charity` once more after Jobs 0 to 5. Rerun the Run CL scanner over
Charity's whole folder, every decoded blob and every PDF's text: zero david@, zero David Taylor outside the licensed
sentence, zero bare David, zero cornerstone, zero scheduler.zoom.us, zero 385 number, zero dashes; her line one reads
charity@ on every piece; contact@ (not support@) as the company line on her prospect pieces. Run the price guard (now
including the $35 and $300 lines, "price pending" and embedded copies) and the new email address guard. Headless at
1440 and 390 on the Price List, Quick Quote, the safety calendar and one month page, and the david card page: zero
console errors, screenshots. Report with a file count for Charity's folder against CH-9.

## Job 7: fix the TD SYNNEX catalog undercount (from A1 PARTNER TD SYNNEX, added 2026-09-26 evening)
Full reasoning: project doc `claude/td-synnex-catalog-gap-2026-09-26.md`. Do Job 7 BEFORE the Job 6 rebuild so Job 6 proves it.
The TD SYNNEX rows added in Run CL Job 6 undercount what is sellable. Fix the Software Marketplace Catalog v2 (xlsx and
md), the Software Marketplace Sheet, both software one pagers, the website copy
(`A1_Sales/Website/BRJ Software Marketplace Package 2026-09-26/`), catalogue.py and Charity's rep kit copies, the same
files Run CL Job 6 touched:
1. Reclassify the TD SYNNEX Hold list (Google Workspace, Adobe, Dropbox, Cisco Duo, Fortinet, Palo Alto, Trend Micro,
   Symantec, CyFlare, CyberArk, DigiCert, Entrust, StorageCraft, Autodesk) to Available, quote on request, the same bar
   the Pax8 rows already use. Do not leave them on Hold.
2. Nerdio Manager for MSP: do NOT put it on any client or website piece. The catalog already lists Nerdio under
   "Internal only, MSP tooling" (software an IT provider runs to manage its clients' Azure desktops, not something a
   small business buys). Add it as an internal row only (TD SYNNEX, live Buy Now, usage driven, internal tool) and list
   it in the report as a question for David: does he want to offer managed Azure Virtual Desktop as an Atlas One
   service? That is a new service, not a catalog line.
3. Do NOT add AnyCloud, Equinix, HPE, IBM, Meta, NexGen Technologies or Mirantis. Their status needs the TD SYNNEX
   portal login (A1 PARTNER TD SYNNEX lane); they follow later.
4. Never name TD SYNNEX or Pax8 on anything a client or prospect reads (standing rule); the product names are fine.
5. Rebuild COMMAND (Job 6 does it). If `A1_Sales/Website/Email_to_Thomas_BRJ_website_update_followup_2026-09-26.txt`
   has not been sent (David has not said it was), regenerate it from the corrected list, no dashes, and retire the old
   copy to `_to_delete/superseded-2026-09-26/`. Also refresh the zip beside the package folder if one exists.

## Job 8: "Have Atlas One build this for me" flashes a page, then jumps into the form (David's screen recording, 2026-09-26 21:03 MT). Do this right after Job 0, it is live.
What happens today: the Sales Kit row "Have Atlas One build this for me" opens `https://forms.atlasonesolutions.com/build/?doc=blank`.
That page (`build/index.html` in atlas-one-intake-forms, about 400 KB because both fonts are inlined) paints its old
"Done for you" holding page first, and only the script at the very bottom of the body then calls
`location.replace(GHL_BUILD_FORM + '?doc=...')`. So the prospect sees one page for a second and is then yanked into the
GoHighLevel form. `doc=blank` is also not a known slug, so it becomes `doc=other`.
Fix, so nothing flashes and no page ever changes under the reader:
1. Every "Have Atlas One build this for me" link (the Sales Kit and COMMAND row in catalogue.py, the five builders in
   `06 Calculators and Tools (NEW Aug 2026)/` that link `build/?doc=<slug>`, the WSA booth demo copy of the handbook
   builder, and build_portal.py if it links there) points STRAIGHT at the GoHighLevel build form
   `https://api.leadconnectorhq.com/widget/form/hxPZ7HEhqG57aoS61MqM` with `?doc=<slug>` and opens in a new tab. Read the
   form URL from one place (people.json company block or a constant in catalogue.py), not pasted per file. The general
   row (no document picked) passes no doc at all, so the form's "Which document?" starts blank instead of "Other".
2. Keep `/build/` working for anything already printed or emailed, but make it a tiny redirect page like `/peo/` and
   `/bookkeeping/`: meta refresh 0 and `location.replace` in the HEAD, a one line "Opening the form" body with a
   Continue link, no fonts, no old holding content (that old content still says David@ and "Email David", retire it).
   Map known slugs through; anything unknown or `blank` passes no doc.
3. Sweep for the same pattern everywhere else: no page on forms.atlasonesolutions.com and no tool in the Master Kit or
   A1_Sales may render visible content and then redirect. Cowork checked the live site on 2026-09-26: `/peo/` and
   `/bookkeeping/` are instant head redirects (fine), `/tools/vendor-consolidation/` is an instant alias to
   `/tools/vendor-audit/` (fine, but repoint the 8 links that still use the old address), `/census/` only opens email
   on a button click (fine). Only `/build/` had the flash. Re-check with a headless browser: record every navigation
   after load for each page and fail any page whose first paint has content and then navigates away.
4. Two live links are BROKEN (404) and are fixed in the same pass: `forms.atlasonesolutions.com/what-we-do/` (7 links;
   the live page is `/tools/what-we-do/`) and `forms.atlasonesolutions.com/tools/handbook-basic/` (2 links; point them at
   the handbook generator's real live address, or at the Sales Kit row if it has no public page). Files that carry them:
   the Sales Kit and Charity's copy (rebuilt from catalogue.py), COMMAND, `W-2 Employee Onboarding Packet
   (Bilingual).html`, `Atlas_One_Everything_We_Handle.html`, build_portal.py, catalogue.py. Add a link check to
   catalogue_check.py that requests every forms.atlasonesolutions.com address in the catalogue and fails on a 404.
5. Push the intake forms repo (main, like every other GHL-JOBS run), rebuild COMMAND, the Sales Kit and --person charity
   (Job 6 does it), then open the Sales Kit in Chromium, click the build row and prove the new tab lands on the form with
   no in between page (screenshot and the navigation list in the report).

## Waiting on David, do not do
Publishing the cards (merge and push `cards-draft`). The workers comp audit recovery percentage (25% on the Price List,
blank in prices.json). Handing Charity her kit (her mailbox does not exist yet).
