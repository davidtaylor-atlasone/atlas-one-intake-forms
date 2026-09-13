# RUN AC report (terminal B, code and files only, no GHL UI)

Built 2026-09-13 by Claude Code, unattended, twelve jobs in order, no questions asked, every permission prompt answered here. Nothing sent, nothing deployed, nothing spent, nothing deleted: every file that changed was copied first to `OneDrive:_to_delete/superseded-2026-09-13/<job folder>/`. One commit per job on `repo` main (`atlas-one-intake-forms`), plus two on `atlas-one-portal`; every commit pushed. Live log: `_BUILD-LOG/TERMINAL-B-live.md`. Scripts, tests, logs and renders: `repo:_briefs/assets/run-AC/` (29 MB, `shots/job<N>/` per job).

Paths are relative to `HR_Docs/Atlas_One_Master_Kit/` unless marked `repo:` (atlas-one-intake-forms), `portal:` (atlas-one-portal), `OneDrive:` (the OneDrive-AtlasOneSolutions root) or `A1_Sales/`. `CAL/` is `06 Calculators and Tools (NEW Aug 2026)/`.

## What was built, job by job

| Job | Result | Where |
|---|---|---|
| 0 | Live log rule | `_BUILD-LOG/TERMINAL-B-live.md` (created, one line per step, 30 lines this run); `repo:CLAUDE.md` (new: brief from disk, live log, report with Assumptions and Questions, never ask mid run, hard stops, commit per job, render to verify, brand rules, Portal rebuild) |
| 1 | Fonts offline | Zero Google Fonts links remained in `CAL/` or the root (Run AB had done the twelve). Fifteen more tools asked for DM Sans in CSS but never loaded it, so they drew in the system font offline; DM Sans embedded in all fifteen (`embedfonts2.py`). All 45 `CAL/` tools and the Tools Hub re rendered offline at 1440 and 390: table below |
| 2 | Portal deploy readiness kit | `portal:DEPLOY.md` (copied to `_BUILD-LOG/portal-DEPLOY-for-David.md`), `portal:vercel.json` (install, build, output, function timeout, cache headers), `portal:package.json` (packageManager pnpm@12.4.1, engines node 22.x, `pnpm preflight`), `portal:scripts/preflight.mjs`. Lint, prettier, server typecheck, build green; Playwright 12 of 12 passed locally in test mode (no email sent). CI on GitHub is green after two fixes (see Assumptions 6). No Vercel project created, no DNS touched |
| 3 | Quote Cockpit: Export deck (.pptx) | `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html` (the Hub calls it current; the Quote & ROI Builder is marked older). New button builds exactly ten slides from page state with the PptxGenJS 3.12 already embedded in the file (no CDN): cover, situation, itemized quote, PEO separate, savings and ROI, time value, guarantee, membership tier, next steps, contact. Membership option list updated to the four current tiers with setup fees. Sample prospect exported, deck rendered to images and looked at (`shots/job3/deck_contact_sheet.png`) |
| 4 | Benefits Routing Tool | `CAL/Atlas_One_Benefits_Routing_Tool.html` (315 KB, offline). Entity, headcount, who needs coverage, current coverage, budget, goal, states, carrier program filed, health history in; route, two sentence why, one question, flags, the never say / say instead table out. Nine scenarios run. Cards: Portal (Quoting & Proposals, Internal), Master Hub (Internal and Benefits). Not on the Tools Hub (Assumption 8) |
| 5 | Compliance Calendar by state | `CAL/Atlas_One_Compliance_Calendar.html` (334 KB, offline). Federal plus UT AZ FL NV CA CO ID TX OR WA: 44 dated rules (annual, quarterly, ranges), 55 standing rules (new hire reporting, pay frequency, sick leave, harassment training, wage notices) with a source URL and "Confirm before relying" on every line, Settled vs Verify by form, weekend shift to the next business day, headcount and plan filters, .ics export with 7 day alarms (RFC 5545 folded), print. Cards: Tools Hub (Compliance, New), Master Hub (Risk, HR), Portal |
| 6 | COI Tracker phase 1 + phase 2 spec | `CAL/Atlas_One_COI_Tracker.html` (316 KB, offline): subs, GL and WC with expiry, waiver, 30 day flag, hold payment by form (auto, force, release), request email in three tones, CSV in and out, JSON save and reload, print report. `_BUILD-LOG/coi-collection-phase-2-spec.md`: research table (myCOI, Jones, TrustLayer, Billy, CertFocus, SubDoc, GHL native), GHL objects and five workflows, portal Subcontractors page, pricing proposal. Cards: Tools Hub, Master Hub (Risk, Industry, Internal), Portal |
| 7 | Marketplace catalog for BRJ | `A1_Sales/Website/Atlas_One_Marketplace_Catalog_for_BRJ.xlsx` and `.md`: 30 rows (7 Signed, 22 Pending, 1 Do not sign), name, category, one line, retail or quote, official logo page (URLs probed live), status by form, note for BRJ. No costs, margins or revenue share. Master Hub cards (Technology) |
| 8 | Email safe HTML how to | `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`: the Run E wrapper with the corrected bgcolor table button (no style on anchors), raw PNG logo URL, text signature, body pieces, source dialog rules (BUILD-INDEX 23) and the rule 31 scan, breakage table. Skeleton assembled and rendered (`shots/job8/wrapper_sample.png`). Master Hub card (Email) |
| 9 | Census v2 | `CAL/Health Quote Census Intake (Atlas One).html` and `repo:census/index.html` (identical, pushed, `forms.atlasonesolutions.com/census/` returns 200 with matching content). Relationship column; + spouse and + child rows under each employee; full home address columns appear at 10 or more eligible employees, ZIP only below; tobacco removed from the UI; optional SSN masked on screen, written only into the downloaded CSV, never in the payload; "more than one plan option" question; header based CSV import that still reads the old eight column file; dash pass. Payload keys unchanged, new keys added (`relationship, street, city, state, employeeIndex, plan.multiPlan, censusVersion`) |
| 10 | What is this for? panel | `_INTERNAL/build_portal.py` gained `header_copy()` (meta description, hero paragraph, first explanatory paragraph, catalogue blurb as last resort); `build_portal_single.py` emits the panel on the Overview (43 rows, each opens the tool) and a "?" strip above every open tool. Tools Hub got the same panel from its TOOLS array (31 rows). Copies of both builders in `repo:_briefs/assets/run-AC/portal-builder/` |
| 11 | Final rebuild and audit | Portal rebuilt: `<title>Atlas One Portal: build Sep 13, 2026  10:16 AM</title>`, 43 tools, 17.48 MB. Every produced file reopened (14 files, all present); zero dashes in new copy; every new tool scrollWidth 390 at 390 px; all 13 Master Hub rows added this run resolve; the four new or changed tools open inside the Portal offline with DM Sans loaded and zero non file requests |

## Job 1 table (all 45 `CAL/` tools plus the Tools Hub, offline, 1440 px; `repo:_briefs/assets/run-AC/shots/job1/`)

Columns: what happened to the file; the face Chrome drew for the first DM Sans text element (`CSS.getPlatformFontsForNode`; the woff2 subset reports its family as "DM Sans 9pt", it is DM Sans); DM Sans asked / drawn in DM Sans among sampled elements; JS errors; non file requests; scrollWidth at 390 px.

| File | Action | Body face offline | DM asked / drawn | Errors | Requests | sw 390 |
|---|---|---|---|---|---|---|
| `Atlas One Business Tools (17 generators).html` | Run AB | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `Atlas One Calculators (53 tools).html` | never asks for DM Sans (system stack), untouched | system | 0 / 0 | 0 | 0 | 390 |
| `Atlas One Savings Summary (Atlas One).html` | Run AB | DM Sans | 12 / 12 | 0 | 0 | 390 |
| `Atlas_One_Back_Office_Self_Assessment.html` | already embedded | DM Sans | 3 / 3 | 0 | 0 | 390 |
| `Atlas_One_Build_This_For_Me.html` | already embedded | DM Sans | 3 / 3 | 0 | 0 | 390 |
| `Atlas_One_Collections_Letter.html` | Run AB | DM Sans | 4 / 4 | 0 | 0 | 390 |
| `Atlas_One_Feedback_Request.html` | Run AB | DM Sans | 5 / 5 | 0 | 0 | 390 |
| `Atlas_One_Onboarding_Tracker.html` | already embedded | DM Sans | 5 / 4 | 0 | 0 | 390 |
| `Atlas_One_PEO_vs_ASO_vs_Software.html` | already embedded | DM Sans | 4 / 4 | 0 | 0 | 390 |
| `Atlas_One_Scan_ID.html` | Run AB | DM Sans | 3 / 3 | 1 | 1 | 390 |
| `Atlas_One_Time_Savings_Discovery.html` | Run AB | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `Atlas_One_True_Cost_Calculator.html` | already embedded | DM Sans | 5 / 5 | 0 | 0 | 390 |
| `Atlas_One_WC_No_Loss_Letter.html` | already embedded | DM Sans | 5 / 3 | 0 | 0 | 390 |
| `atlas-command-center.html` | Run AB | DM Sans | 3 / 3 | 0 | 0 | 390 |
| `Business Infrastructure Audit (Atlas One).html` | already embedded | DM Sans | 5 / 5 | 0 | 0 | 390 |
| `Business Infrastructure Audit (Espanol).html` | already embedded | DM Sans | 5 / 5 | 0 | 0 | 390 |
| `Business Value Diagnostic (Atlas One).html` | already embedded | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `Business Value Diagnostic (Espanol).html` | already embedded | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `Certified Payroll Converter (WH-347) (Atlas One).html` | embedded this run | DM Sans | 9 / 9 | 0 | 0 | 390 |
| `Certified Payroll Manager (Atlas One).html` | Run AB | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `COI to Workers Comp Premium Estimator (Atlas One).html` | embedded this run | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `Compliance Risk Scorecard (Atlas One).html` | embedded this run | DM Sans | 7 / 7 | 0 | 0 | 390 |
| `Cost of a Compliance Mistake (Atlas One).html` | embedded this run | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `Disciplinary Write-Up Notice Generator (Atlas One).html` | embedded this run | DM Sans | 10 / 10 | 0 | 0 | 390 |
| `Employee Benefits Options (Atlas One).html` | embedded this run | DM Sans | 12 / 10 | 0 | 0 | 390 |
| `Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html` | embedded this run | DM Sans | 7 / 7 | 0 | 0 | 390 |
| `Employee Handbook Builder (Bilingual 50-State).html` | already embedded | DM Sans | 13 / 12 | 0 | 0 | 390 |
| `Health Comparison Builder (Atlas One).html` | Run AB | DM Sans | 7 / 7 | 0 | 0 | 390 |
| `Health Quote Census Intake (Atlas One).html` | embedded this run | DM Sans | 9 / 8 | 0 | 0 | 390 |
| `Independent Contractor Agreement Builder (Atlas One).html` | embedded this run | DM Sans | 14 / 13 | 0 | 0 | 390 |
| `Independent Contractor Onboarding Packet (Bilingual).html` | embedded this run | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `Meeting Bonus Import Builder (Atlas One).html` | Run AB | DM Sans | 5 / 5 | 0 | 0 | 390 |
| `NDA Builder (Atlas One).html` | embedded this run | DM Sans | 19 / 17 | 0 | 0 | 390 |
| `Payroll to GL Import Converter (Atlas One).html` | already embedded | DM Sans | 9 / 9 | 0 | 0 | 390 |
| `Retention Cost Calculator (Atlas One).html` | already embedded | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `Retention Cost Calculator (Espanol).html` | already embedded | DM Sans | 6 / 6 | 0 | 0 | 390 |
| `Retention Scorecard (Atlas One).html` | Run AB | DM Sans | 3 / 3 | 0 | 0 | 390 |
| `Retention Scorecard (Espanol).html` | Run AB | DM Sans | 3 / 3 | 0 | 0 | 390 |
| `Safety Manual Builder (Bilingual OSHA).html` | already embedded | DM Sans | 13 / 12 | 0 | 0 | 390 |
| `Separation Letter Generator (Atlas One).html` | embedded this run | DM Sans | 10 / 10 | 0 | 0 | 390 |
| `Vendor Consolidation Savings (Atlas One).html` | already embedded | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `Vendor Consolidation Savings (Espanol).html` | already embedded | DM Sans | 8 / 8 | 0 | 0 | 390 |
| `W-2 At-Will Employment Agreement Builder (Atlas One).html` | embedded this run | DM Sans | 16 / 14 | 0 | 0 | 390 |
| `W-2 Employee Onboarding Packet (Bilingual).html` | embedded this run | DM Sans | 9 / 9 | 0 | 0 | 390 |
| `Atlas One — Tools Hub.html` | embedded this run | DM Sans | 6 / 6 | 0 | 0 | 390 |

Where asked and drawn differ by one or two, the misses are symbol glyphs DM Sans does not contain (checkmarks, stars, envelopes, dingbats) drawn from a system symbol font, plus the embedded 600 weight the checker names "SemiBold". `Atlas_One_Scan_ID.html` still requests its barcode library from cdnjs (known since Run AB, not a font). Backups of the fifteen: `OneDrive:_to_delete/superseded-2026-09-13/fonts-before/` (now 27 files with Run AB's twelve).

## What was looked at

- Job 1: `shots/job1/*_1440.png` and `*_390.png` for 46 files; `Portal_nda_builder_1440.png`, `Portal_compliance_scorecard_1440.png` (two fixed tools open inside the Portal offline, fonts.check true).
- Job 2: `shots/job2-portal-e2e/` (Playwright screenshots, mobile and desktop, every portal page).
- Job 3: `shots/job3/cockpit_1440.png`, `cockpit_390.png`, `deck/slide-01..10.png`, `deck_contact_sheet.png`, the exported `Atlas_One_Deck_Ridgeline_Concrete_LLC.pptx`.
- Job 4: nine scenario screenshots `routing_*.png`, `Atlas_One_Benefits_Routing_Tool_1440.png`, `_390.png`, `hub_search_routing.png`.
- Job 5: `calendar_1440_filled.png`, `_390.png`, the exported `.ics`, `hub_search.png`, `toolshub_search.png`.
- Job 6: `coi_1440.png`, `coi_print.png`, `coi_390.png`, the exported CSV and JSON, `hub_search.png`, `toolshub_search.png`.
- Job 7: `catalog_xlsx_render.png` (the workbook rendered as a table), `hub_search.png`.
- Job 8: `wrapper_sample.png` (logo loads from the storage.googleapis.com URL, button and signature render), `hub_search.png`.
- Job 9: `census_step4_1440.png` (employee with spouse and child rows, address columns on at 12 employees), `census_review_1440.png`, `census_390.png`, the downloaded CSV.
- Job 10: `portal_help_open.png`, `portal_tool_help.png`, `portal_help_390.png`, `toolshub_whatfor.png`.
- Job 11: `shots/job11/` renders of the six new or changed HTML files and the four opened inside the Portal.

## Repo

`repo` (atlas-one-intake-forms, main, pushed): commits `b413d26` (job 0), `01abed8` (1), `a05d7c6` (2 shots), `0e44989` (3), `8b3c2a6` (4), `0a1eefe` (5), `2fc9d93` (6), `aeaaefb` (7), `b929cd9` (8), `ce73ad0` (9), `06d80bf` (10), then the job 11 commit carrying this report. `portal` (atlas-one-portal, main, pushed): `f15de1b` (job 2 kit), then the CI fix and the lockfile commit; CI run 34768232726 green.

Files in `repo:_briefs/assets/run-AC/`: `log.sh`, `verify.mjs`, `embedfonts2.py`, `job1-embed-log.jsonl`, `portal-fontcheck.mjs`, `cockpit_deck10.js`, `cockpit_export_test.mjs`, `pptx2html.py` + `deckshots.mjs` + `fontfaces.css`, `a1shell.py` + `fonts/`, `build_routing_tool.py`, `routing_scenarios.mjs`, `build_compliance_calendar.py`, `calendar_test.mjs`, `build_coi_tracker.py`, `coi_test.mjs`, `build_marketplace_catalog.py`, `census_v2_patch.py`, `census_test.mjs`, `hub_add.py` + `hub_rows_job*.json`, `toolshub_add.py` + `toolshub_rows_job*.json`, `hubcheck.mjs`, `toolshub_check.mjs`, `portal_help_test.mjs`, `portal-builder/`, copies of the three markdown deliverables, `shots/`.

## Assumptions (every judgment call)

1. **Job 1 scope widened to tools that never loaded DM Sans.** The brief scoped Job 1 to files still linking Google Fonts; none were left. Fifteen tools asked for DM Sans in their CSS and never loaded it anywhere (they drew in .SF NS or Helvetica offline and online). The brand rule and "every tool works offline" made embedding the same TTF faces the obvious call; each was backed up first and the change is additive (one `<style id="a1fonts-2026-09-13">` block before the first `<style>`). `Atlas One Calculators (53 tools).html` does not ask for DM Sans at all (system stack) and was left alone: changing its font stack is a redesign, not a font embed.
2. **TTF, not woff2, for the fifteen** (same reasoning as Run AB: identical bytes to the hosted self assessment). The three new tools and the shell helper use the smaller woff2 subsets the PEO vs ASO tool already carries (14 KB per face) plus the Horas TTF, so each new tool is about 315 KB instead of 450 KB.
3. **Job 3: the Cockpit's existing One-pager and Full ROI deck buttons were left in place** and the new "Export deck (.pptx)" added beside them. The brief asked for the button; removing the older exports was not asked. The one brand fix made to the old code: the green savings colour in the Full ROI deck became navy (status by form). The green "Full ROI deck" button, the red Discount row and the amber margin panel in the Cockpit UI are pre existing off palette colours and were not touched.
4. **Job 3: membership tier options updated.** The Cockpit's membership row listed the retired tiers (/bin/zsh /  /  / /bin/zsh). It now lists Essential  (setup waived), Professional  (), Enterprise  (), Concierge ,900 (,500), the set on the live payment links and the 09-12 brochure; picking a tier also fills the setup fee. Saved prospect files keep whatever they had.
5. **Job 3: the old Excel in, deck out generator (`PEO_Proposal_Generator_V4.5_MASTER/`) was left in place.** The Master Hub has no card for it at all, so it is not marked "older"; nothing was retired.
6. **Job 2: two CI fixes after the kit landed.** Adding `packageManager` to package.json made pnpm/action-setup fail ("Multiple versions of pnpm specified", the workflow also said `version: 12`), so the workflow now takes the version from package.json only; pnpm 12 then wanted the packageManager dependency recorded in the lockfile, so `pnpm-lock.yaml` gained that block (no dependency versions changed; frozen install passes locally and in CI). The CI secret `GHL_PRIVATE_INTEGRATION_TOKEN` is empty on GitHub, so CI runs lint, format, typecheck and build only; the Playwright suite ran here (12 passed) against the real seed contacts in test mode.
7. **Job 2: the preflight script reads `.env` by default** and treats `http://localhost` in `PORTAL_APP_URL` as a warning, not a failure, so David can run it on the Mac Studio as is. Against the real `.env` it passed everything except the customFields scope (401), which is exactly the scope DEPLOY.md tells David to add.
8. **Job 4: no Tools Hub card for the Benefits Routing Tool.** The Tools Hub is the prospect safe launcher that gets sent out with the kit; the routing tool is internal and prints the never say table and referral partner discipline. The brief said Portal + Tools Hub + Master Hub; I put it on the Portal (Internal badge) and the Master Hub (Internal and Benefits) and kept it off the Hub. One line in `toolshub_add.py` if you want it there anyway.
9. **Job 4: the solo owner route deviates from the spec's row 3.** The spec says a one person S corp routes to ICHRA. An ICHRA can only reimburse employees; owners of S corps (over 2 percent), partners and sole proprietors cannot participate themselves. So a working owner with no employees routes to individual coverage placed by Atlas One as broker, with ICHRA offered as the alternative only for a C corp paying the owner W-2 wages, and the PEO or EOR route named where they want W-2 payroll. The tool also carries a sixth outcome the spec requires (row 5): "leave the health plan where it is, carve it out" when they are happy with what they have. Both are marked for counsel in the tool's footer.
10. **Job 4: the state list of carrier program filings is unknown**, so the tool asks "carrier program filed in every one of those states?" and flags "confirm the state list before you promise it" rather than pretending to know.
11. **Job 5: dates and amounts.** Statutory dates are marked Settled; anything an agency sets each year (minimum wage amounts, EEO-1 window, CA pay data report day, FAMLI and Paid Leave rates, MBT rate) is marked Verify and the amount is not stated. Weekend dates move to the next business day; federal holidays are not adjusted (stated on the page). The EEO-1 line uses a placeholder date from the 2025 cycle and says so.
12. **Job 5: sources.** 85 distinct URLs. 67 answer 200 to curl. 17 return 403 to every automated agent tried (Cloudflare or CloudFront bot walls on colorado.gov, azica.gov, des.az.gov, detr.nv.gov, ui.nv.gov, floridajobs.org, osha.gov, acf.hhs.gov); they are the agencies' own pages and open in a normal browser, but they could not be machine verified here. Ten URLs that returned 404 or did not resolve were replaced with the agency's confirmed landing page (Utah Labor Commission, Idaho Department of Labor, Texas OAG new hire, Nevada DWSS, Oregon BOLI employers page, IRS PCORI Q&A, DOL Form 5500 page).
13. **Job 5: specific legal reads to confirm** (all marked on the page): ACA furnishing relief under the 2024 Paperwork Burden Reduction Act; the Form 5500 small plan exemption wording; the 1099-NEC threshold rising to ,000 for 2026 payments; Florida's post 2026 indexing start; Nevada's flat .00 rate; Oregon and Washington employer share thresholds (25 and 50 employees) for paid leave.
14. **Job 6: research sources are vendor pages and vendor authored comparisons** (Billy's, Vertikal's, SubDoc's). Prices are reported ranges, not quotes; the spec says so. GHL native is listed as costing nothing extra because the subscription already exists.
15. **Job 6: "waiver" is left to the client's contract** (the subcontractor agreement with its waiver of subrogation, or the lien waiver); the tool says so and the request email names it generically.
16. **Job 6: the phase 2 pricing ( /  a month,  setup) is a proposal**, marked as such in the spec, not a decision.
17. **Job 7: status mapping.** Ramp, Intuit (QuickBooks Online and QuickBooks Time), Big Red Jelly, Microsoft CSP and G&A ("Active, legacy") are Signed; SimpliVerified is Do not sign (the directory says so); everything else with TBD or "pending" is Pending. Atlas One's own AI products are listed as Signed (own products); the website card is Pending because the Jason Petty pricing is an open question. Retail figures come from the V8 Technology sheet and Quick Quote; Jotform's are its public list prices. `experiencedpayrollpros.com` did not resolve on 2026-09-13 and the row says so.
18. **Job 7: logo source URLs point at the vendor's press or about page** where a brand kit page could not be found (probed live: the deel.com, ramp.com, connecteam.com press pages and the Intuit press room exist; Jotform, Pax8, PartnerStack, AppDirect, PrismHR have no public press kit URL that answered, so BRJ requests assets by email). No logo files were downloaded.
19. **Job 8: the wrapper's signature links carry no inline style** (the brief's rule), so most clients underline them. Accepted and stated in the how to. The Run E paste notes had a styled anchor button; the how to documents the as built table button from rule 23 instead.
20. **Job 9: the kit copy was the source**, not the repo copy (the repo copy still had the em dashes Run W removed from the kit). Both are now identical and both carry the embedded fonts, so the hosted census draws DM Sans for the first time (it was system font before). Dependant rows inherit the employee's ZIP, address and tier in the payload; their tier and ZIP cells are blank in the CSV. Untouched seed rows are no longer exported. The Zoom Scheduler booking links in the census were left as they are (Run X owns the repointing).
21. **Job 9: SSN handling.** Digits live only in a data attribute on the row, shown as `***-**-6789`, revealed on focus, written into the downloaded CSV, and excluded from `collectData()` (the object the commented webhook example posts). The page never posts anywhere today, so "webhook payload" means that object; its v1 keys are unchanged.
22. **Job 10: four tools have no usable header paragraph** (Employee Handbook Builder, Safety Manual Builder, Disciplinary Write-Up, Separation Letter: their intros are titles or "the document updates as you type"), so their panel text is the Portal catalogue blurb. The Portal shell itself still draws in the system font (it embeds no DM Sans); pre existing, not changed.
23. **Portal rebuilt after every job that touched a tool** (rule 12), six builds today; the previous Portal is backed up once at `OneDrive:_to_delete/superseded-2026-09-13/portal-before-AC-job1/`.
24. **Another session (Run AD, terminal A) committed to the repo during this run** (`90052e4`). No conflict; pulls and pushes were clean.

## Skipped or partial

- Job 3: no retirement of the old generator (not marked older on the Hub).
- Job 4: Tools Hub card deliberately not added (Assumption 8).
- Job 5: 17 source URLs could not be machine verified (bot walls); they need one human click each.
- Job 8: not pasted into GHL (terminal A owns the GHL UI); the how to is the document only.
- Nothing else in the brief was skipped.

## Observations, not changed

- `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, `08 ROI Quote Master Template/Atlas_One_Quote_and_ROI_Builder.html` and the other 25 files outside `CAL/` listed in the Run AB report still link Google Fonts (one non file request appears when Quick Quote is opened inside the Portal). Same one line change if wanted.
- Cockpit UI carries a red Discount row, a green button and an amber margin panel (off palette, pre existing).
- The Portal shell does not embed DM Sans; tools inside it do.
- The census tool has no live webhook; the review page holds a commented example only.

## Questions for David

1. **Benefits Routing Tool, solo owners:** the spec sends a one person S corp to ICHRA; the tool sends them to an individual plan because S corp owners cannot be ICHRA participants. Do you want the spec's wording kept (with a counsel flag), or the tool's?
2. **Benefits Routing Tool on the Tools Hub:** it is internal, so it is off the prospect safe Hub. Put it there anyway?
3. **Compliance Calendar:** which states next, and is the Verify list (minimum wage amounts each January, EEO-1 window, FAMLI and Paid Leave rates) something you want me to refresh each October, or leave to the member?
4. **Compliance Calendar as a product:** subscription price and whether it ships inside Essential or only Professional and above.
5. **COI Tracker phase 2:** approve the GHL build brief (five workflows, one pipeline, one upload form) for terminal A, and the  /  pricing idea, or change the numbers.
6. **Marketplace catalog:** confirm the seven Signed rows are the only ones BRJ may publish today, and whether G&A ("Active, legacy") should show on a public page at all given the never print who quoted rule.
7. **Marketplace catalog:** Experienced Payroll Pros' domain did not resolve; still a partner?
8. **Portal deploy:** Hobby (free, non commercial terms) or Pro ( a month) on Vercel. Step 1 of DEPLOY.md leaves this to you.
9. **Portal deploy:** add `locations/customFields.readonly` to the Private Integration and create the `services` (Multiple Options) and `savings_to_date` (Monetary) fields as written in DEPLOY.md step 6, or tell me different types.
10. **Quote Cockpit deck:** the ten slide deck says "setup fees are often waived on an annual plan; annual plans get two months free" (from the brochure). Still true?
11. **Quote Cockpit:** keep the older One-pager and Full ROI deck buttons now that Export deck exists, or retire them?
12. **Census v2:** should dependant rows carry their own tier and ZIP (some carriers want them), or inherit the employee's as built?
13. **Census v2:** the Zoom Scheduler booking links in the census still point at scheduler.zoom.us; Run X repoints them to the GHL 15 minute link when it runs. Confirm that is still the plan.
14. **Fonts:** `Atlas One Calculators (53 tools).html` never asks for DM Sans (system font stack). Restyle it to the brand fonts, or leave the 53 calculators as they are?
15. **Fonts outside `CAL/`:** 27 files still link Google Fonts (list in the Run AB report). Run the same embed over them?
