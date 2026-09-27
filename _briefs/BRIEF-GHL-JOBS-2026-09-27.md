# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CQ, 2026-09-27). Job 0: fix the software catalog at its source (Run CP audit failed). Job 1: digital business cards.

Installed by A1 GHL Jobs 3 after its audit of Run CP. Job 0 is small and comes first; Job 1 (cards) was carried unstarted through Runs CN and CO and must be finished in this run. Archive Run CP's report first.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the
portal repo. No questions mid run. No sends, no spending, no new vendors. Deleting is a move into
`Master_Kit/_to_delete/superseded-<date>/`. No dashes in anything a client or prospect reads. Log a line when each job
STARTS and ends with the real clock time (`date`), never an estimated time. There is NO time limit: this run has
one job, so do all of it; do not stop early to "carry it forward". Finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`
(archive the previous report first). Keep every Run CL to CO guard on.

## Job 0 (do FIRST): put the catalog right, at the SOURCE (Cowork audit of Run CP failed, see COWORK-AUDIT-run-CP-2026-09-27.md)
1. Edit the generator source, not the built files: unpack `_BUILD-LOG/software-catalog-src-2026-09-26.tgz`, change
   `catalog/data.py`, rebuild with `catalog/build_catalog.py`, repack the tgz. Any edit to a built md, xlsx or html
   without the source is lost on the next rebuild; that is exactly how Run CN's Job 7 was wiped by Run CP.
2. Set the 13 TD SYNNEX Cloud Marketplace Hold rows to Available, quote on request (Google Workspace, Adobe Acrobat and
   Adobe Express for teams, Dropbox Business, Cisco Duo and Cisco security, Fortinet, Palo Alto Networks, Trend Micro,
   Symantec (Broadcom), CyFlare, CyberArk, DigiCert / Entrust, StorageCraft (Arcserve), Autodesk).
3. Rule for every row: if any source (Pax8, TD SYNNEX Cloud Marketplace or TD SYNNEX Distribution) lists it as
   orderable, the row is Available, quote on request. Apply it to the Pax8 Hold rows that now carry a TD SYNNEX
   Distribution note (Barracuda, ThreatLocker, Cove Data Protection (N-able), Dropbox / Box / DocuSign, Cloudflare /
   Fortinet / Cisco Meraki, and any other). For a combined row, split out the orderable names or mark the row
   Available with a note naming which part is quote only. Report the final Hold list with the reason each stays.
4. Add a guard to the catalog build: a row whose note says "available through" any source cannot be Hold, and a test
   that the 13 rows above are Available, so this cannot regress again.
5. Regenerate the md, xlsx (all tabs and header counts), both Software Marketplace Sheets and PDFs, catalogue.py blurbs.
6. Rewrite `A1_Sales/Website/Email_to_Thomas_BRJ_website_update_followup_2026-09-27.txt` so the Hold line matches the
   real count (say "short", and give the number only if it is under 12). No dashes, no distributor names, no prices.
7. Rebuild `Atlas One for BRJ 2026-09-27.zip` with the corrected files and WITHOUT the Thomas email txt inside it.
8. Stop after Job 0 is logged and write a Job 0 line in the report, then continue to Job 1.
Cowork re-audits the catalog before David sends anything.

## Job 1: digital business cards
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
   `_briefs/assets/run-CQ-cards/`. The real phone check is David's after publish: list the three taps to do.
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

## Job 2: rebuild COMMAND, the shared Sales Kit and --person charity, rerun every guard, report.
