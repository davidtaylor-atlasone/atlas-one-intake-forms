# RUN-GHL-JOBS report, Run CU (2026-10-04)

Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` (installed 2026-09-30, "Run CU"). Terminal: GHL-JOBS, files and code only, no GoHighLevel UI.
Nothing was pushed (no push of atlas-one-intake-forms, per the brief). Local commits only, on branch `ghl-jobs-run-cu`.
Run CT's report was archived first as `_BUILD-LOG/RUN-GHL-JOBS-report-runCT-done-2026-10-04.md`.

## Result at a glance

| Job | Status |
|---|---|
| 1 Charity's playbooks, vendor pay | Done. Zero vendor pay or commission lines in her kit (grep proof below). |
| 2 Charity's booking link | Skipped: no link exists yet (see Skipped). |
| 3 Vendor ordering links (COMMAND Systems hub) | Done. 13 rows, 3 shown as "Link needed". |
| 4 Run CT follow ups | Done, all four items. Item 5 (annual plan lines) left alone as told. |
| 5 Rebuild and prove | Done. COMMAND, Sales Kit and `--person charity` rebuilt, 25 of 25 catalogue checks green. |

## Job 1: vendors pay David only

Rule added once, in one place each: `people.json` gets `"vendor_pay": true` for David and `false` for Charity. Every guard keys off that flag, so a future rep gets the same treatment.

What a rep copy now does instead: the "how I get paid" hook is replaced by "the review costs you nothing, you pay for the one relationship", and insurance and PEO questions go to "David Taylor, our licensed agent" (David's name stays in a rep copy only in that exact phrase, plus the older "Insurance products are offered through David Taylor, licensed agent" line that was already allowed).

Changed, by file:
- `_INTERNAL (do not share)/rep_scrub.py`: asserted literal rewrites for the two playbooks and overlays 03 and 06, a generic rewrite for the repeated "most of it costs you nothing extra because the vendors pay me" sentence, "near free line" renamed "price line", the licensed agent phrase, a `REP_LITERALS` table for rows outside the scrubbed set, and a pay guard (`PAY_PATTERNS`, `pay_problems`, `assert_no_pay_language`) that fails the build and names the id. Overlay 06's referral fee mentions come out of the rep copy only.
- `_INTERNAL.../build_command.py`: rep builds run `REP_LITERALS`, assert no pay language on every inlined row, and the rep kit leak guard (`scan_default_person_leak`, also used by `--check-zip`) now scans HTML, every decoded tool blob, PDFs, pptx, docx and xlsx for pay language. The licensed agent phrase is allowed in the David name leak check.
- `_INTERNAL.../rep_assets.py`: the rep's office files are rewritten too (see "Found on the way").
- `_INTERNAL.../render_md_pages.py` plus three email masters: new `{{#if rep_vendor_pay}}...{{else}}...{{/if}}` conditional. Masters edited: `Atlas_One_Prospect_Email_Templates.md` ("I'm paid by the vendors" line), `Atlas_One_Referral_Request_Emails.md` (commission or revenue share offer; a rep says she will send business back and offers a call instead), `Atlas_One_Client_Announcement_Series.md` (Email 4, "paid for by the providers"). David's reader copy shows both branches, labelled "David only" and "Reps".
- `_INTERNAL.../build_talk_track.py` and the rebuilt `Atlas_One_Talk_Track.html`: three pay lines reworded (this page is rep neutral and shared, so David's copy changed too, see Assumptions).
- `_INTERNAL.../catalogue_check.py`: new check "rep copies carry no vendor pay, commission or referral fee language". It builds the rep text of every rep or prospect inline row (scrub, literals, md merge) for each non-default person and fails on any hit, and it fails if `vendor_pay` is true for anyone but the default person.
- `_INTERNAL.../test_rep_scrub.py`: pay guard self test (the guard must catch 9 kinds of bad line and not raise false alarms on 4 good ones, vendor_pay flags must be right, both playbooks must name David as licensed agent), screen share snippet strip fixed (the old test failed on the Run CS snippet), shots now go to `run-CU`.

Found on the way (not in the brief's list, but in her kit):
1. Her office decks carried pay lines: Prospect Pitch Deck (both versions: speaker note, slide 4 or 6, slide 16), Client Launch Deck slide 6 ("HOW I GET PAID, Vendors pay me ... each pays a referral commission"), Client Launch Companion docx ("vendors pay me a commission when you use them"). Fixed in `rep_assets.py` for any person with `vendor_pay` false: slide 6 now reads "THE REVIEW COSTS NOTHING" with the licensed agent line. Looked at the rendered slide (`shots/charity-client-launch-deck-slide6.jpg`).
2. The PEO Comparison Tool said "we're paid the same no matter which direction you choose", and the Client Portal leave behind said "we're paid by the vendors, not you". Reworded in the rep build only (`REP_LITERALS`).
3. David's 15 minute intro calendar link was on three "Book a call" buttons of the BRJ Resource Library page inside her Sales Kit. The rep swap now treats that slug (read from `people.json`, never typed in code) as David's link: her buttons become a call to her own number.

## Job 2: skipped

No booking link for Charity exists. `people.json` still has `"booking": null`; the GHL lane report and live log show Run CV stopped (GHL screens dead) before creating her calendars, so there is nothing to put in. Her card, kit and announcement series keep the phone call fallback. When the GHL lane creates `quick-call-with-charity`, put it in `people.json` (`booking`) and rerun this job.

## Job 3: vendor ordering links (COMMAND, Systems, Vendor ordering, internal only)

`hubs.py` `VENDOR_ROWS` rewritten, 13 rows. The existing guard that keeps vendor rows out of rep and shared builds still passes.

| Row | Link | Source |
|---|---|---|
| GoHighLevel | https://app.ridethehightide.com (sign in as David@AtlasOneSolutions.com) | brief, David 2026-10-01 (was app.gohighlevel.com) |
| Microsoft Partner Center | https://partner.microsoft.com/dashboard | brief, David 2026-10-01 |
| QuickBooks Online Accountant | https://qbo.intuit.com | brief, David 2026-10-01 (was qboa.intuit.com) |
| Pax8 partner portal | https://app.pax8.com | Pax8 notes |
| TD SYNNEX PartnerFirst | https://partnerfirst.us.tdsynnex.com | account notes |
| Software Store (admin) | the Pax8 storefront | Pax8 notes |
| Connecteam | https://app.connecteam.com | notes |
| Ramp (tracked partner link) | https://ramp.com/partners/atlasone | Vendor Partner Directory |
| QuickBooks referral link (tracked) | the cid link | Vendor Partner Directory and Audit |
| SimpliVerified (tracked link) | https://simpliverified.com/atlas-one-solutions | Partner Directory Audit |
| Cornerstone PEO login | link needed | partner CRM login address is not on disk |
| G&A Partners login | link needed | not on disk |
| Vero HCM login | link needed | not on disk |

The three "link needed" cards say so in plain words and their button opens the vendor's public site only. Looked at it: `shots/command-vendor-ordering-1440.png`.
Left out on purpose: a Deel row (the directory says the old discount link is not used under the rev share, the audit says the partner link is live, so they disagree) and Jotform (partner link pending). Nothing named AppDirect was added (the catalogue check forbids it).

## Job 4: Run CT follow ups

1. Storefront URL never printed as visible text. Fixed at the source (`software-catalog-src-2026-10-04.tgz`, `catalog/build_catalog.py`): md rows show `[Browse the store](url)`, xlsx cells show "Browse the store" as a hyperlink, the Sheet keeps its "Browse the Atlas One Software Store" button. New output guard fails the build if the URL or "pax8" appears in md text, any xlsx cell or the Sheet's visible text. Regenerated in `A1_Sales/Atlas 1 Software and Licenses/`: Sheet html and pdf (11 pages), catalog v2 md and xlsx. BRJ: new `A1_Sales/Website/Atlas One for BRJ 2026-10-04/` and `.zip` (47 members, three files refreshed), the 2026-09-30 folder and zip retired. Checked the zip: zero AppDirect, SYNNEX or myappdirect in names, text, xlsx or pdf text, zero visible storefront URL.
2. Quote Cockpit W-2 label is now "Year-end W-2s (one extra payroll run at your rate, monthly minimum applies)".
3. DM Sans embedded (base64, Google Fonts links removed) in `05 Build Specs (for BRJ)/Atlas One Website Package/06 Calculators and Tools/Atlas One Business Tools (17 generators).html`, and in `Atlas One Complete Kit for BRJ/2. Interactive Tools (embed these)/` copy of the same file, which had the same gap. Loaded in Chromium and WebKit at 1440 and 390: DM Sans loads, scrollWidth equals viewport, zero console errors, zero non file requests. The `06 Calculators and Tools (NEW Aug 2026)` copy already had it.
4. "Lehi, Utah" kept only as address lines. Examples changed to placeholders: Prospecting Playbook ("Congrats on the second [City] location"), Overlay 03 ("Your trucks are all over [City]"), and the sample rows in `PrismHR_Employee_Census_Template.csv` and `Atlas_One_GHL_Client_Import_Template.csv` (now Springfield, IL 62704, 217 area code).
5. Annual plan lines untouched.

## Job 5: rebuild and proof

- COMMAND: `Atlas One COMMAND.html`, stamp "build Oct 4, 2026 10:38 AM", 216 items (stamp changed from Sep 30 11:10 PM). Sales Kit: 62 items. Her kit: 99 items in the Sales Kit file, six division sheets, five one pagers, eight sales pieces, price list, six email template pages, decks, office files with PDFs. Rebuilt four times because each proof pass found one more thing (see Found on the way); the last build is final. The previous kit folders went to `_to_delete/superseded-2026-10-04/charity-kit-before-CS`, `-2`, `-3` (the builder's own location, one level above the Master Kit).
- Her zip: `A1_Sales/_Rep Kits/Charity Taylor.zip`, 76 members (same count as before), `build_command.py --check-zip` clean. Earlier zips: `Master_Kit/_to_delete/superseded-2026-10-04/charity-zip/`.
- Guards: catalogue_check 25 of 25 pass; rep_scrub test ALL PASS (self test plus 8 pages at 1440 and 390); rep kit leak guard clean at build and on the zip.
- Renders (Chromium and WebKit, 1440 and 390): COMMAND, Sales Kit, her Sales Kit file, both generators files. Every one: scrollWidth equals the viewport, zero console errors, zero non file requests. Shots in `_briefs/assets/run-CU/shots/` (copied to the repo, committed locally).
- Grep proof, her final zip (`_briefs/assets/run-CU/charity-kit-grep-proof.txt`), 67 files including every decoded tool blob, pdf, pptx, docx and xlsx: 0 "vendors pay me or us", 0 "carrier or provider pays me", 0 "paid by the vendors, carriers, providers or PEO", 0 "how I get paid", 0 "I am paid or we are paid", 0 "revenue share", 0 "referral fee back or to partners", 0 "my or your commission", 0 "near free", 0 David booking links (book-david, quick-call-with-david, the intro calendar), 9 uses of "David Taylor, our licensed agent". The bare word "commission" still appears 25 times, all in client facing business tools: Commission and Total Comp Calculator and the Sales Commission Agreement builder (for a client's own sales staff), a benefits quote form field "Broker commission (optional)", and the service name "Comp and commission plan design" on the Business Consulting sheet. None is about a rep.

## Files changed (Marketing root = `2. A1 Official Docs/2. Atlas 1 Solutions Marketing`)

Code and data (`HR_Docs/Atlas_One_Master_Kit/_INTERNAL (do not share)/`): `rep_scrub.py`, `build_command.py`, `rep_assets.py`, `render_md_pages.py`, `build_talk_track.py`, `catalogue_check.py`, `hubs.py`, `people.json`, `test_rep_scrub.py`; regenerated `rendered_md_manifest.json`, `screenshare_manifest.json`, `present_assets/charity/*` page images.
Sales material (`A1_Sales/`): `A1 Playbook Sales/Atlas_One_Prospecting_Playbook_v1.html`, `A1 Playbook Sales/Atlas_One_Talk_Track.html`, `Industry Playbooks/Atlas_One_Industry_Overlay_03_Construction.html`, `Email Templates/` (three md masters edited, six html pages re-rendered), `Atlas 1 Software and Licenses/` (Sheet html and pdf, catalog md and xlsx), `Website/Atlas One for BRJ 2026-10-04/` and zip, `Atlas One Sales Kit.html`, `_Rep Kits/Charity Taylor/` and `Charity Taylor.zip`.
Master Kit: `Atlas One COMMAND.html`, `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`, `05 Build Specs (for BRJ)/.../Atlas One Business Tools (17 generators).html`, `Atlas One Complete Kit for BRJ/2. Interactive Tools (embed these)/Atlas One Business Tools (17 generators).html`, `07 New HR and Safety Docs (NEW Aug 2026)/PrismHR_Employee_Census_Template.csv`, `12 GHL Setup doccs/Atlas_One_GHL_Client_Import_Template.csv`, `_BUILD-LOG/software-catalog-src-2026-10-04.tgz`.
Retired (moved, never deleted) to `HR_Docs/Atlas_One_Master_Kit/_to_delete/superseded-2026-10-04/`: `catalog-link/`, `catalog-src/` (the 09-30 source tgz is there twice, once as a copy and once as `.moved`), `quote-cockpit/`, `generators-17/`, `lehi-examples/`, `brj/` (2026-09-30 folder and zip), `command-before-CU/`, `charity-zip/`.
Backups of every file I edited in place sit in those folders. Pre edit copies of the code files I changed are in `/tmp` only (not kept), the git history of the repo does not cover the Master Kit.

## Assumptions

1. `vendor_pay` is the one switch. David true, Charity false, and the catalogue check fails if that ever changes without a decision.
2. The Talk Track is one rep neutral page used by David and reps, so rewording it removed "providers pay us" for David's copy too. David can say what is true himself; if he wants his own wording back, it needs a David only variant of the page.
3. For a rep, "how I get paid" content becomes "the review is free, you pay for the one relationship". I did not invent any new claim (for example about pricing parity with going direct).
4. Referral partner emails: a rep offers to send business back and to talk it through, with no commission or revenue share and no partner overview (that document is David's).
5. The 15 minute intro calendar is David's calendar (the GHL brief lists it among his five) so it counts as a "David booking link" in a rep kit even though it is allowed on website pages.
6. The storefront URL stays as a hyperlink target (David's Run CT decision: keep the button, never print the URL). If even the target must go, the storefront needs a custom domain.
7. Retired files went to `Master_Kit/_to_delete/superseded-2026-10-04/` as the brief says. The rep kit builder uses its own `_to_delete` one level up; I left that behaviour alone.
8. Job 3 added tracked referral links (Ramp, QuickBooks, SimpliVerified) because they are on disk and confirmed; they are referral links, not ordering portals.
9. A rep copy of the BRJ Resource Library page now has "Call 801-787-8154" style buttons instead of David's intro call.

## Skipped

- Job 2 (no link yet).
- A Deel row, a Jotform row, any AppDirect row (see Job 3).
- No other kit (David's COMMAND copy of the playbooks, the BRJ website copy) was changed for vendor pay: David's own copies keep his wording.

## Questions for David

1. Charity's booking link: when the GHL lane has created `quick-call-with-charity`, drop it in `people.json` and run this brief again. Do you want her intro buttons to use it too, or only the 15 minute call?
2. The Quick Quote tool still says "one additional payroll run at your rate" on the year end W-2 line (only the Cockpit was in the brief). Should it get the same new wording?
3. David's masters still use Draper and Utah in examples (Prospecting Playbook scripts: "owners in Utah", "the new Draper office", "Utah names" time zone block; Overlay 04 "Utah software teams"). Charity's copies already show [City] and [state]. Do you want David's masters changed too? I only changed Lehi, as the brief said. The census template also still has a Provo, UT sample row.
4. The service name "Comp and commission plan design" is on the Business Consulting sheet in her kit. It is something we sell to clients, not a rep commission. Keep it, or rename it so a grep for "commission" is zero?
5. The Sales Partner Welcome Email (how sales partners are paid) is not in any kit. When Charity's own rates are set, where should her pay terms live?
6. Do you want the Cornerstone, G&A and Vero login addresses added once you have them (the cards are ready, they only need the URLs)?
