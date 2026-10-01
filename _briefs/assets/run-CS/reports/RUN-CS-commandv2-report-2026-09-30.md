# RUN CS Job 3: COMMAND v2 report (helper commandv2, 2026-09-30)

## What was built (all in MK/_INTERNAL (do not share))
- `hubs.py` (new): data model. Decorates CATALOGUE at import with hub, sub, service, industry, language, family, fmt, purpose, card_title, collection. Hub rules plus `HUB_BY_ID` override table, `PURPOSE` (one calm line per card, no dashes, replaces the raw notes that used to show), `COLLECTIONS`, `HOME_START`, `VENDOR_ROWS`.
- `command_shell.py` (new): the page template (CSS and JS). All sizes in rem; four colours; Horas and DM Sans embedded; no CDN.
- `build_command.py`: v2 builder. Zones replaced by hubs. Lead's rep rows, rep_path_map, deck_pdf_map, Present, rep_scrub hook, text swap and safe restore kept untouched. Legacy zone scope still decides which rows a rep or the shared kit may receive (so those sets did not change); `hub_exclude=NEVER_REP_HUBS` (Internal, Partner programs, Systems) drops whole hubs from rep and shared builds.
- `catalogue.py`: removed `build-audit-report` (a .py, lives at `08 ROI Quote Master Template/Total_Impact_Model/build_audit_report.py`, run it from a terminal); marked three .md rows `render='md'` (rendered at build with lead's `render_md_pages.render_markdown`, no second renderer); renamed the duplicate id of the "Build request inbox" row to `build-request-inbox`; 10 vendor rows appended through hubs.py.
- `catalogue_check.py`: 6 checks added (20 total, none removed): hub, purpose, language and sub hub valid, no duplicate ids; format cards unambiguous; nothing opens as code (.py .js .json, unrendered .md); rep hub rules and vendor rows internal only; Talk Track row pinned and rep visible; collections have members.
- Backups: `MK/_to_delete/superseded-2026-09-30/command-v1/` (old COMMAND.html, build_command.py, catalogue.py, catalogue_check.py).

## Behaviour
- Left sidebar of hubs with counts (Home, Prospect and pitch, Industry overlays, Discover and audit, Quote and price, Forms and intake, Deliver to clients, Agreements, Email templates, Partner programs, Systems, Internal, Espanol, Present). At 390 px it is a menu drawer.
- Search box (Cmd or Ctrl K, or /) searches every hub and Present playlists at once, grouped by hub, arrows and Enter work, empty state. Filter chips: audience, service, language. Quick links row always visible: Client portal, GoHighLevel, AI Email Assistant queue (the last two Internal only), Book a call (people.json for the viewer, hidden for Charity until she has a link).
- Cards: title, one line purpose, audience by shape plus words (ring "Share with prospects", diamond "Clients", solid square "Internal only"), one button per format, star pin (localStorage, try/catch), Attach these box on email cards (email_attach_map.json). Collections: "Division sheets" (six buttons) and "Industry overlays" (six). Partner programs and Systems have sub hub pills; Vendor ordering is a Systems group.
- Open is a real `<a target="_blank" rel="noopener">`. Inlined tools and rendered .md pages: Blob URL set on pointerover, focus, touchstart, mousedown and again on click, revoked on pagehide and on Sending as change. PDFs, decks, docs: relative URL (rep kit uses rep_path_map). No in page preview, no Close button. Present keeps its full screen runner.
- Presenting switch (scales html to 130 percent, remembered), Dark switch (remembered), both with 2px track, knob, text label, 44px targets, visible focus ring. Body 17px, labels 15px.

## Proof (Playwright, shots in `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/command-v2/`)
- Chromium desktop 1440, 1024, 390: home, hub, search, Present, dark; scrollWidth equals viewport at all three (also in dark); zero console errors; zero non file requests. Shots `cmd-*`.
- WebKit iPhone 15 and iPad (gen 7): home, hub, search, Present, dark (`wk-iphone-*`, `wk-ipad-*`): zero errors, scrollWidth equals viewport, new tab opened (blob page "Atlas One Quick Quote").
- Scene shots: `cmd-home-full`, `cmd-hub-overlays` (collection), `cmd-hub-email` (Attach these), `cmd-hub-systems` (sub hub pills), `cmd-hub-present`, `cmd-390-menu`, `cmd-1280-presenting` / `chromium-1280-presenting`. Rep kit: `rep-1440-home`, `rep-1440-prospect`.
- New tab test (Chromium and WebKit): inlined tool (href blob:null/...), rendered .md page (blob), PDF and PPTX (relative href, new page opens; headless Chromium downloads them so its URL is blank, WebKit lands on file://), external link: context.pages grew 1 to 2 each time, original tab and its search box untouched, zero console errors.
- Search test from Home: "commission" (exists only in Internal side: Commission and Revenue Tracker) returns 1; "handbook" returns 3 prospect tools; "dental" returns the Industry overlays card; nonsense returns the empty state.
- Presenting at 1280x720: root font 20.8px (130 percent), scrollWidth 1280, no horizontal overflow.
- Rep build (Charity): nav is Home, Prospect and pitch, Industry overlays, Discover and audit, Quote and price, Forms and intake, Deliver to clients, Email templates, Espanol, Present. No Internal only, no Sending as select, no Vendor ordering, no Partner programs or Systems hub, no Cornerstone, no David Taylor; quick links are Client portal only (Book a call hidden, no booking link); Talk Track is the Home feature card and first in Start here of Prospect and pitch; 8 playlists in Present. Job 2 leak guard printed "clean".

## Load time (iPad profile, file://)
Before (v1, 57.7 MB): Chromium iPad viewport with 4x CPU throttle 0.65 s median. After (v2, 64.6 MB): 0.69 s; WebKit iPad (gen 7) 0.37 s. Under 3 s, so no blob restructuring was needed (blobs already decode only on open; tool bytes are never decoded at load). File grew 7 MB from the rendered .md pages and the extra card markup.

## Counts and stamps
COMMAND: 207 items (was 199 rows: minus 1 script row, plus 10 vendor rows, other lane rows moved in), title stamp `Atlas One COMMAND: build Sep 30, 2026 7:0x PM`. Shared Sales Kit 59 items. Charity kit 97 items.

## Guard status
- catalogue_check earlier full run: my 6 new checks ok (after fixing a bug in my own vendor check). Failing, not mine: embedded PRICES in Atlas_One_Audit_Workbench.html (another lane), retired price hits in the Presentation Services Deck PDF and in Agreements_How_They_Fit.md (late fee sentence, another lane's text). A final rerun was still running when this report was written (OneDrive was slow); see Questions.
- Rep build guards (scan_default_person_leak, forbidden terms, footer swap): clean on the first v2 Charity build. A later rebuild failed in `rep_scrub.scrub` for `overlay-01-audiology` ("forbidden text left after scrub"); the lead's safe restore put the previous Charity kit back. That is in rep_scrub.py or the overlay HTML source (another helper's files), not v2. Charity's kit currently on disk is the first good v2 build (its JS carries the full hub name list; the later source fix limits it to present hubs, applies on next successful build).

## What still fails or is open
1. Charity rebuild after my last edit blocked by the rep_scrub overlay-01 error above (repscrub helper lane).
2. Vendor URLs: confirmed from notes: Pax8 (app.pax8.com), TD SYNNEX (partnerfirst.us.tdsynnex.com), Connecteam (app.connecteam.com), Software Store (pax8 storefront). Not on file, site only or standard address used: Cornerstone CRM (cornerstonepeo.com), G&A Partners (gnapartners.com), Vero (verohcm.com), Microsoft Partner Center (partner.microsoft.com/dashboard), QuickBooks Online Accountant (qboa.intuit.com), GoHighLevel (app.gohighlevel.com, agency sub domain unconfirmed).
3. COMMAND file is now 64.6 MB; no problem at load, but OneDrive sync is slower.

## Assumptions
1. Rows keep their legacy zone only for deciding what a rep or the shared kit may receive, so those sets are unchanged (the Price List html and pdf stay out of the shared kit as before).
2. A piece with rep=True and audience internal shows "Share with prospects" everywhere (it is what a rep shares).
3. A family sits in the hub of its primary format (html, link, pptx, docx, xlsx, then pdf).
4. The public Software Store link sits in Prospect and pitch (reps need it); an Internal admin copy sits in Systems, Vendor ordering.
5. The AI Email Assistant and AI Task Agent one pagers moved to Prospect and pitch (they are prospect audience; Systems never reaches reps).
6. The INTERNAL passphrase curtain is gone in v2 (it was already None since Run CE); build prints a note if it is set.
7. Card text uses the new `purpose` lines, not the old blurbs (old blurbs carried notes, a firm ID and a retired $299 price).
8. Hub counts count items (a collection counts its members).
9. Home "Start here" is the HOME_START list; user stars give Your pins; recents store card keys.
10. A hub shows a Start here group only in Prospect and pitch, Quote and price, Discover and audit, Deliver to clients.

## Questions for David
1. Confirm the six vendor addresses listed under item 2 above, or send the real login URLs.
2. Should the Price List (client facing, HTML and PDF) also appear in the shared Sales Kit and rep kit Quote hub? It was left out before and still is.
3. Should "Cornerstone PEO" have its own login row once you have the CRM address?

## Placement table (every row: old zone and division, new hub)
| Row id | Title | Old zone | Old division | New hub | Sub or group | Format |
|---|---|---|---|---|---|---|
| agreements-index-2026-09-12 | Agreements Index (2026-09-12) | Internal | Agreements | Agreements |  | html |
| agreements-how-they-fit | Agreements, How They Fit | Internal | Agreements | Agreements |  | html |
| book-of-business-non-circumvention | Book-of-Business & Non-Circumvention | Internal | Agreements | Agreements |  | docx |
| mutual-nda | Mutual NDA | Internal | Agreements | Agreements |  | docx |
| mutual-nda-pdf | Mutual NDA (PDF) | Internal | Agreements | Agreements |  | pdf |
| mutual-nda-template-draft-2026-09-12 | Mutual NDA TEMPLATE (DRAFT, 2026-09-12) | Internal | Agreements | Agreements |  | docx |
| peo-services-schedule | PEO Services Schedule | Internal | Agreements | Agreements |  | docx |
| referral-partner-agreement-template-draft-2026-09-12 | Referral Partner Agreement TEMPLATE (DRAFT, 2026-09-12) | Internal | Agreements | Agreements |  | docx |
| msa-2026-09-15 | Master Client Services Agreement (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| msa-2026-09-15-pdf | Master Client Services Agreement (2026-09-15, PDF) | Internal | Agreements | Agreements |  | pdf |
| hold-harmless-2026-09-15 | Hold Harmless and Acknowledgement (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| hold-harmless-2026-09-15-pdf | Hold Harmless and Acknowledgement (2026-09-15, PDF) | Internal | Agreements | Agreements |  | pdf |
| schedule-software-licenses-2026-09-15 | Schedule, Software and Licenses (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-software-licenses-2026-09-15-pdf | Schedule, Software and Licenses (2026-09-15, PDF) | Internal | Agreements | Agreements |  | pdf |
| schedule-bookkeeping-2026-09-15 | Schedule, Bookkeeping (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-gl-converter-2026-09-15 | Schedule, Payroll to GL Converter (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-cert-payroll-2026-09-15 | Schedule, Certified Payroll (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-wc-audit-2026-09-15 | Schedule, WC Audit Recovery (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-coi-2026-09-15 | Schedule, COI Tracking (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-ai-services-2026-09-15 | Schedule, AI Services (2026-09-15, regenerated) | Internal | Agreements | Agreements |  | docx |
| schedule-document-services-2026-09-15 | Schedule, Document Services (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| schedule-membership-2026-09-15 | Schedule, Membership (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| proposal-shell-2026-09-15 | Proposal Shell (2026-09-15) | Internal | Agreements | Agreements |  | docx |
| sample-proposals-2026-09-15 | Sample Proposals, Tell Me More LLC (2026-09-15, 8 docs) | Internal | Agreements | Agreements |  | folder |
| employee-benefits-menu | Employee Benefits Menu | Tools | Benefits & Retirement | Prospect and pitch |  | html |
| employee-benefits-menu-pdf | Employee Benefits Menu (PDF) | Internal | Benefits & Retirement | Prospect and pitch |  | pdf |
| 27-business-generators | 27 Business Generators | Tools | Business Consulting | Deliver to clients |  | html |
| 53-business-calculators | 53 Business Calculators | Tools | Business Consulting | Deliver to clients |  | html |
| auditoria-de-proveedores-y-software-espanol | Auditoria de Proveedores y Software (Espanol) | Tools | Business Consulting | Espanol |  | html |
| back-office-self-assessment | Back Office Self-Assessment | Tools | Business Consulting | Discover and audit |  | html |
| business-infrastructure-audit-espanol | Business Infrastructure Audit (Espanol) | Tools | Business Consulting | Espanol |  | html |
| business-value-diagnostic | Business Value Diagnostic | Tools | Business Consulting | Discover and audit |  | html |
| business-value-diagnostic-espanol | Business Value Diagnostic (Espanol) | Tools | Business Consulting | Espanol |  | html |
| compliance-calendar-by-state | Compliance Calendar by state | Tools | Business Consulting | Deliver to clients |  | html |
| compliance-risk-scorecard | Compliance Risk Scorecard | Tools | Business Consulting | Discover and audit |  | html |
| cost-of-a-compliance-mistake | Cost of a Compliance Mistake | Tools | Business Consulting | Discover and audit |  | html |
| have-atlas-one-build-this-for-me | Have Atlas One build this for me | Sales Kit | Business Consulting | Forms and intake |  | link |
| infrastructure-audit | Infrastructure Audit | Tools | Business Consulting | Discover and audit |  | html |
| retention-cost-calculator | Retention Cost Calculator | Tools | Business Consulting | Discover and audit |  | html |
| retention-scorecard | Retention Scorecard | Tools | Business Consulting | Discover and audit |  | html |
| time-and-cost-savings-discovery | Time and Cost Savings Discovery | Tools | Business Consulting | Discover and audit |  | html |
| vendor-software-audit | Vendor & Software Audit | Tools | Business Consulting | Discover and audit |  | html |
| audit-workbench | Audit Workbench | Tools | Sell & Pitch | Discover and audit |  | html |
| service-content-library | Service Content Library | Tools | Sell & Pitch | Prospect and pitch |  | html |
| client-launch-companion | Client Launch Companion | Sales Kit | Decks | Deliver to clients |  | docx |
| client-launch-companion-pdf | Client Launch Companion (PDF) | Sales Kit | Decks | Deliver to clients |  | pdf |
| client-launch-deck-2026-09 | Client Launch Deck 2026-09 | Sales Kit | Decks | Deliver to clients |  | pptx |
| client-launch-deck-2026-09-pdf | Client Launch Deck 2026-09 (PDF) | Sales Kit | Decks | Deliver to clients |  | pdf |
| partner-pitch-deck-v9 | Partner Pitch Deck v9 | Sales Kit | Decks | Partner programs | Referral partners | pptx |
| partner-pitch-deck-v9-pdf | Partner Pitch Deck v9 (PDF) | Sales Kit | Decks | Partner programs | Referral partners | pdf |
| partner-speaking-sheet | Partner Speaking Sheet | Sales Kit | Decks | Partner programs | Referral partners | pdf |
| partner-deck-v9-light-43-slides | Partner deck v9 LIGHT (43 slides) | Sales Kit | Decks | Partner programs | Referral partners | pptx |
| partner-deck-20-slide-room-cut-2026-09-12 | Partner deck, 20 slide room cut (2026-09-12) | Sales Kit | Decks | Partner programs | Referral partners | pptx |
| prospect-pitch-deck | Prospect Pitch Deck | Sales Kit | Decks | Prospect and pitch |  | pptx |
| prospect-pitch-deck-first-meeting-9-slides | Prospect Pitch Deck, First Meeting (9 slides) | Sales Kit | Decks | Prospect and pitch |  | pdf |
| prospect-pitch-deck-first-meeting-pptx | Prospect Pitch Deck, First Meeting (PPTX) | Sales Kit | Decks | Prospect and pitch |  | pptx |
| prospect-web-pitch | Prospect Web Pitch (live page) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| services-overview-client-sheet | Services Overview (one page, every service) | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| service-deck-ai-task-agent | Service deck: AI Task Agent | Sales Kit | Decks | Prospect and pitch |  | pptx |
| service-deck-bookkeeping-accounting | Service deck: Bookkeeping & Accounting | Sales Kit | Decks | Prospect and pitch |  | pptx |
| service-deck-handbook-safety | Service deck: Handbook & Safety | Sales Kit | Decks | Prospect and pitch |  | pptx |
| service-deck-wc-premium-audit-review | Service deck: WC Premium Audit Review | Sales Kit | Decks | Prospect and pitch |  | pptx |
| services-one-pager-pptx | Services One-Pager (PPTX) | Sales Kit | Decks | Prospect and pitch |  | pptx |
| atlas-one-email-templates-pdf | Atlas One Email Templates (PDF) | Internal | Email templates | Email templates |  | pdf |
| client-launch-email-drafts-2026-09-06 | Client Launch Email Drafts (2026-09-06) | Tools | Email templates | Email templates |  | html |
| email-blast-library | Email Blast Library | Tools | Email templates | Email templates |  | html |
| prospect-email-templates | Prospect Email Templates | Tools | Email templates | Email templates |  | html |
| referral-request-emails | Referral Request Emails | Tools | Email templates | Email templates |  | html |
| bonus-import-builder | Bonus Import Builder | Tools | Financial Services | Deliver to clients |  | html |
| quickbooks-accountant-access-guide | QuickBooks accountant access guide | Sales Kit | Financial Services | Deliver to clients |  | pdf |
| bookkeeping-onboarding-emails | Bookkeeping onboarding emails | Tools | Email templates | Email templates |  | html |
| bookkeeping-client-agreement-packet | Bookkeeping Client Agreement Packet | Internal | Financial Services | Agreements |  | pdf |
| bookkeeping-invoice-master | Bookkeeping Invoice (blank master) | Internal | Financial Services | Deliver to clients |  | pdf |
| bookkeeping-client-intake-guide | Bookkeeping Client Intake Guide | Internal | Financial Services | Forms and intake |  | docx |
| bookkeeping-marketing-sheet | Bookkeeping Marketing Sheet | Internal | Financial Services | Prospect and pitch |  | pdf |
| certified-payroll-converter | Certified Payroll Converter | Tools | Financial Services | Deliver to clients |  | html |
| certified-payroll-manager | Certified Payroll Manager | Tools | Financial Services | Deliver to clients |  | html |
| payroll-gl-import | Payroll → GL Import | Tools | Financial Services | Deliver to clients |  | html |
| overlay-01-audiology | Overlay 01: Audiology | Tools | Industry overlays | Industry overlays |  | html |
| overlay-02-dental-ortho-optometry-ent | Overlay 02: Dental, Ortho, Optometry, ENT | Tools | Industry overlays | Industry overlays |  | html |
| overlay-03-construction-and-trades | Overlay 03: Construction and Trades | Tools | Industry overlays | Industry overlays |  | html |
| overlay-04-technology-and-startups | Overlay 04: Technology and Startups | Tools | Industry overlays | Industry overlays |  | html |
| overlay-05-hospitality-and-restaurants | Overlay 05: Hospitality and Restaurants | Tools | Industry overlays | Industry overlays |  | html |
| overlay-06-professional-services | Overlay 06: Professional Services | Tools | Industry overlays | Industry overlays |  | html |
| vip-partnership-plus-calculator | VIP Partnership Plus Calculator | Tools | Industry overlays | Partner programs | WSA and VIP Partnership Plus | html |
| wsa-audiology-partnership-plus-overview-v3 | WSA Audiology Partnership Plus Overview v3 | Tools | Industry overlays | Partner programs | WSA and VIP Partnership Plus | html |
| wsa-audiology-partnership-plus-overview-v3-pdf | WSA Audiology Partnership Plus Overview v3 (PDF) | Sales Kit | Industry overlays | Partner programs | WSA and VIP Partnership Plus | pdf |
| ai-email-assistant-setup-intake | AI Email Assistant Setup Intake | Tools | Intake & Client | Forms and intake |  | html |
| booking-confirmation-page | Booking Confirmation Page | Tools | Intake & Client | Forms and intake |  | html |
| bookkeeping-intake-form | Bookkeeping Intake Form | Tools | Intake & Client | Forms and intake |  | html |
| client-portal-admin-sign-in | Client portal (admin sign-in) | Internal | Intake & Client | Systems | Client portal | link |
| peo-intake-form | PEO Intake Form | Tools | Intake & Client | Forms and intake |  | html |
| benefits-aggregation-strategy-memo | Benefits Aggregation Strategy (memo) | Internal | Internal (do not share) | Internal |  | docx |
| bookkeeping-profit-calculator-v7 | Bookkeeping Profit Calculator V7 | Internal | Internal (do not share) | Internal |  | xlsx |
| carrier-master-plan-discovery-brief | Carrier Master Plan Discovery Brief | Internal | Internal (do not share) | Internal |  | docx |
| commission-revenue-tracker | Commission & Revenue Tracker | Tools | Internal (do not share) | Partner programs | Referral partners | html |
| cornerstone-strategy | Cornerstone Strategy | Tools | Internal (do not share) | Partner programs | Cornerstone PEO | html |
| document-inventory | Document Inventory | Internal | Internal (do not share) | Internal |  | pdf |
| internal-master-pricing-v8-xlsx | INTERNAL Master Pricing V8 (xlsx) | Internal | Internal (do not share) | Quote and price |  | xlsx |
| jotform-decision | Jotform Decision | Tools | Internal (do not share) | Internal |  | html |
| member-program-spec | Member Program Spec | Internal | Internal (do not share) | Internal |  | docx |
| peo-private-label-ask | PEO Private Label Ask | Internal | Internal (do not share) | Partner programs | Cornerstone PEO | docx |
| screening-pricing-calculator | Screening Pricing Calculator | Tools | Internal (do not share) | Quote and price |  | html |
| vendor-partner-directory | Vendor Partner Directory | Internal | Internal (do not share) | Partner programs | Referral partners | xlsx |
| health-quote-tool | Health Quote Tool | Tools | Pricing & Quotes | Quote and price |  | html |
| membership-brochure-4-pages | Membership Brochure (4 pages) | Tools | Pricing & Quotes | Quote and price |  | html |
| membership-comparison-one-page | Membership Comparison (one page) | Tools | Pricing & Quotes | Quote and price |  | html |
| price-list-pdf | Price List (PDF) | Internal | Pricing & Quotes | Quote and price |  | pdf |
| price-list-client-facing-2-pages | Price List (client facing, 2 pages) | Tools | Pricing & Quotes | Quote and price |  | html |
| quote-roi-builder | Quote & ROI Builder | Tools | Pricing & Quotes | Quote and price |  | html |
| quote-cockpit-start-here | Quote Cockpit (START HERE) | Tools | Pricing & Quotes | Quote and price |  | html |
| background-screening-one-pager | Background Screening, one-pager | Tools | Sell & Pitch | Prospect and pitch |  | html |
| benefits-options-presenter | Benefits Options Presenter | Tools | Sell & Pitch | Prospect and pitch |  | html |
| benefits-routing-tool | Benefits Routing Tool | Tools | Sell & Pitch | Deliver to clients |  | html |
| coi-tracker | COI Tracker | Tools | Sell & Pitch | Deliver to clients |  | html |
| coi-wc-premium-estimator | COI → WC Premium Estimator | Tools | Sell & Pitch | Deliver to clients |  | html |
| client-portal-leave-behind | Client Portal leave-behind | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-benefits-retirement | Division sheet: Benefits & Retirement | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| division-sheet-business-consulting | Division sheet: Business Consulting | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| division-sheet-financial-services | Division sheet: Financial Services | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| division-sheet-risk-insurance | Division sheet: Risk & Insurance | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| division-sheet-technology-operations | Division sheet: Technology & Operations | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| division-sheet-workforce-hr | Division sheet: Workforce & HR | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| everything-atlas-one-handles-public-page | Everything Atlas One handles (public page) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| health-comparison-builder | Health Comparison Builder | Tools | Sell & Pitch | Quote and price |  | html |
| health-quote-census | Health Quote Census | Tools | Sell & Pitch | Quote and price |  | html |
| peo-vs-aso-vs-software | PEO vs ASO vs Software | Tools | Sell & Pitch | Prospect and pitch |  | html |
| proof-sheet | Proof Sheet | Tools | Sell & Pitch | Prospect and pitch |  | html |
| prospect-onboarding-tracker | Prospect Onboarding Tracker | Tools | Sell & Pitch | Deliver to clients |  | html |
| quick-quote | Quick Quote | Tools | Sell & Pitch | Prospect and pitch |  | html |
| savings-summary | Savings Summary | Tools | Sell & Pitch | Quote and price |  | html |
| start-to-success | Start to Success | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| software-licenses-one-pager | Software and Licenses, one-pager | Tools | Sell & Pitch | Prospect and pitch |  | html |
| software-licenses-one-pager-pdf | Software and Licenses, one-pager (PDF) | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| microsoft-365-one-pager | Microsoft 365 through Atlas One, one-pager | Tools | Sell & Pitch | Prospect and pitch |  | html |
| microsoft-365-one-pager-pdf | Microsoft 365 through Atlas One, one-pager (PDF) | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| software-card-portal-add-services | Software and licenses card (portal Add services) | Tools | Technology & Operations | Systems | Software store | html |
| software-card-spec-for-portal | Software card: spec for PORTAL | Internal | Technology & Operations | Systems | Software store | html |
| total-impact-model | Total Impact Model | Tools | Sell & Pitch | Discover and audit |  | html |
| true-cost-of-doing-it-yourself | True Cost of Doing It Yourself | Tools | Sell & Pitch | Discover and audit |  | html |
| brand-guide-official-2026 | Brand Guide (official 2026) | Sales Kit | Start here | Internal |  | pdf |
| how-to-build-a-quote | How to Build a Quote | Tools | Start here | Quote and price |  | html |
| prospecting-playbook-v1 | Prospecting Playbook v1 | Tools | Start here | Prospect and pitch |  | html |
| sales-conversation-playbook | Sales Conversation Playbook | Tools | Start here | Prospect and pitch |  | html |
| tools-cheat-sheet | Tools Cheat Sheet | Sales Kit | Start here | Internal |  | pdf |
| what-we-do-business-overview | What We Do, Business Overview | Tools | Start here | Prospect and pitch |  | html |
| ai-email-assistant-activity-log-live | AI Email Assistant, Activity log (LIVE) | Internal | Technology & Operations | Systems | AI Email Assistant | link |
| ai-email-assistant-approval-queue-live | AI Email Assistant, Approval Queue (LIVE) | Internal | Technology & Operations | Systems | AI Email Assistant | link |
| ai-email-assistant-install-support | AI Email Assistant, Install & Support | Tools | Technology & Operations | Systems | AI Email Assistant | html |
| ai-email-assistant-tasks-follow-ups-live | AI Email Assistant, Tasks & Follow-ups (LIVE) | Internal | Technology & Operations | Systems | AI Email Assistant | link |
| ai-email-assistant-one-pager | AI Email Assistant, one-pager | Tools | Technology & Operations | Prospect and pitch |  | html |
| ai-email-assistant-client-help-page | AI Email Assistant: client help page | Tools | Technology & Operations | Systems | AI Email Assistant | html |
| ai-task-agent-one-pager | AI Task Agent, one-pager | Tools | Technology & Operations | Prospect and pitch |  | html |
| collections-letter | Collections Letter | Tools | Technology & Operations | Deliver to clients |  | html |
| feedback-review-request | Feedback / Review Request | Tools | Technology & Operations | Deliver to clients |  | html |
| software-marketplace-sheet | Software Marketplace Sheet (tiles) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| atlas-one-software-store | Atlas One Software Store (public link) | Sales Kit | Technology & Operations | Prospect and pitch |  | link |
| scan-id | Scan ID | Tools | Technology & Operations | Deliver to clients |  | html |
| 1099-onboarding-packet | 1099 Onboarding Packet | Tools | Workforce & HR | Deliver to clients |  | html |
| company-safety-manual-template | Company Safety Manual Template | Internal | Workforce & HR | Deliver to clients |  | pdf |
| contractor-agreement | Contractor Agreement | Tools | Workforce & HR | Deliver to clients |  | html |
| disciplinary-write-up | Disciplinary Write-Up | Tools | Workforce & HR | Deliver to clients |  | html |
| safety-training-program | Safety Training Program | Tools | Workforce & HR | Deliver to clients |  | html |
| employee-handbook-builder | Employee Handbook Builder | Tools | Workforce & HR | Deliver to clients |  | html |
| enrollment-guide | Enrollment Guide | Tools | Workforce & HR | Deliver to clients |  | html |
| hr-template-library | HR Template Library | Tools | Workforce & HR | Deliver to clients |  | html |
| build-request-inbox | Build request inbox (internal) | Tools | Workforce & HR | Forms and intake |  | html |
| labor-law-poster-center | Labor Law Poster Center | Tools | Workforce & HR | Deliver to clients |  | html |
| nda-builder | NDA Builder | Tools | Workforce & HR | Deliver to clients |  | html |
| new-client-onboarding-intake-pdf | New Client Onboarding Intake (PDF) | Internal | Workforce & HR | Forms and intake |  | pdf |
| peo-comparison-tool | PEO Comparison Tool | Tools | Workforce & HR | Prospect and pitch |  | html |
| retention-cost-calculator-espanol | Retention Cost Calculator (Espanol) | Tools | Workforce & HR | Espanol |  | html |
| retention-scorecard-espanol | Retention Scorecard (Espanol) | Tools | Workforce & HR | Espanol |  | html |
| safety-manual-builder | Safety Manual Builder | Tools | Workforce & HR | Deliver to clients |  | html |
| separation-letter | Separation Letter | Tools | Workforce & HR | Deliver to clients |  | html |
| w-2-at-will-agreement | W-2 At-Will Agreement | Tools | Workforce & HR | Deliver to clients |  | html |
| w-2-onboarding-packet | W-2 Onboarding Packet | Tools | Workforce & HR | Deliver to clients |  | html |
| wc-no-loss-letter-loss-history-affidavit | WC No-Loss Letter / Loss History Affidavit | Tools | Workforce & HR | Deliver to clients |  | html |
| workforce-software-comparison | Workforce Software Comparison | Tools | Workforce & HR | Prospect and pitch |  | html |
| atlas-one-sales-kit-html | Atlas One Sales Kit (share with partners) | Sales Kit | Start here | Prospect and pitch |  | html |
| start-front-door-page | Start (front door page) | Sales Kit | Start here | Prospect and pitch |  | link |
| ppg-partner-client-program-one-pager | Atlas One for PeoplePay Global clients (one pager) | Sales Kit | Sell & Pitch | Prospect and pitch |  | pdf |
| audit-intake-page-public | Audit intake page (public) | Sales Kit | Start here | Forms and intake |  | link |
| division-sheet-workforce-hr-html | Division sheet: Workforce & HR (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-benefits-retirement-html | Division sheet: Benefits & Retirement (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-financial-services-html | Division sheet: Financial Services (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-risk-insurance-html | Division sheet: Risk & Insurance (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-technology-operations-html | Division sheet: Technology & Operations (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| division-sheet-business-consulting-html | Division sheet: Business Consulting (HTML) | Tools | Sell & Pitch | Prospect and pitch |  | html |
| digital-business-card-david | Digital business card: David (Atlas One) | Sales Kit | Sell & Pitch | Prospect and pitch |  | link |
| digital-business-card-david-wsa | Digital business card: David (WSA, with Cornerstone PEO) | Sales Kit | Sell & Pitch | Partner programs | WSA and VIP Partnership Plus | link |
| digital-business-card-charity | Digital business card: Charity (Atlas One) | Sales Kit | Sell & Pitch | Prospect and pitch |  | link |
| business-cards-folder | Business Cards (folder: all files, QR plan, share instructions) | Sales Kit | Sell & Pitch | Prospect and pitch |  | folder |
| bookkeeping-email-cadence | Bookkeeping email cadence | Tools | Email templates | Email templates |  | html |
| client-announcement-series | Client Announcement Series (6 emails) | Tools | Email templates | Email templates |  | html |
| atlas-one-talk-track | Talk Track (read aloud) | Tools | Start here | Prospect and pitch |  | html |
| presentation-services-deck-pdf | Presentation Services Deck (PDF) | Sales Kit | Decks | Prospect and pitch |  | pdf |
| vendor-cornerstone-crm | Cornerstone PEO | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-ga-partners | G&A Partners | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-vero | Vero HCM | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-pax8 | Pax8 partner portal | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-td-synnex | TD SYNNEX PartnerFirst | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-microsoft-partner-center | Microsoft Partner Center | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-qbo-accountant | QuickBooks Online Accountant | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-connecteam | Connecteam | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-gohighlevel | GoHighLevel | Internal | Internal (do not share) | Systems | Vendor ordering | link |
| vendor-software-store | Software Store (admin) | Internal | Internal (do not share) | Systems | Vendor ordering | link |
