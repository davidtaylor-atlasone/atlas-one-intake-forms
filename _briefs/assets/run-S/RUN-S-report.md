# RUN S report (terminal B, code and files only)

Built 2026-09-12 by Claude Code, unattended. Brief: `_BUILD-LOG/RUN-S-terminal-B.md`, copied to the repo at `_briefs/RUN-S-terminal-B.md` with a progress log at the bottom. The GHL browser UI was not touched. No email sent, nothing deployed beyond the normal GitHub Pages push of the intake-forms repo, nothing deleted (retired files moved to `_to_delete/superseded-2026-09-12/`). Every page was rendered in headless Chromium (Playwright 1.63, Node) and the screenshots were looked at before being called done.

Paths below are relative to `OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/` unless they start with `repo:` (the `atlas-one-intake-forms` repo, pushed to `main`) or `OneDrive:`.

## Job 1: retention sample image for 45-C

- `repo:tools/assets/retention-sample-25ee.png`, 1200 x 507 px, 104 KB (under 250 KB).
- Live and confirmed 200: **https://forms.atlasonesolutions.com/tools/assets/retention-sample-25ee.png**
- Numbers came from the calculator itself, driven in headless Chromium: salary 52000, team 25, turnover 8% (2 of 25). Outputs read from the DOM: $52,000 per departure, $104,000 a year, 2 people lost, "~5.2 mo to a fully productive replacement". Nothing typed by hand.
- Frame: off white, result panel, caption "Sample: 25 employees, two people leave in a year" in DM Sans, dark blue logo mark bottom right.

## Job 2: Back Office Self-Assessment (new free tool)

- `repo:tools/self-assessment/index.html` (412 KB, Horas and DM Sans embedded, works offline). Live, 200: **https://forms.atlasonesolutions.com/tools/self-assessment/**
- Copy in the kit: `HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Back_Office_Self_Assessment.html`
- Registered: `_INTERNAL (do not share)/build_portal.py` (Calculators & Diagnostics), `Atlas One — Tools Hub.html` (Diagnostics & Savings, tag New), Master Hub (Sell & Pitch), and `repo:tools/index.html` now lists four tools.
- Ten questions exactly as specified, one screen each, tap to answer, Back link, progress bar (form, not colour). Three scores 0 to 10 (10 = holding, 0 = leaking) with "Points came off for ..." under each; tiles are solid (Time), tinted (Money), outlined (Risk). Three biggest leaks, one sentence each. Button "Book the 30 minute Back Office Audit" to `https://api.leadconnectorhq.com/widget/groups/book-david`. Optional name, company, email, phone; requires at least an email or a phone before posting.
- Webhook: same endpoint and payload shape as the branded intake forms (`first_name, last_name, phone, email, company, atlas_tool, atlas_headline, atlas_results_text, atlas_source_url, atlas_generated_at`) plus `score_time, score_money, score_risk, leak_1..3` and `sa_payroll, sa_coi, sa_benefits, sa_classcodes, sa_vendors, sa_hours, sa_audit, sa_handbook, sa_hr, sa_overlap`. **Test submission through the page returned HTTP 200** (email `muddybudmods+runs5363335@gmail.com`, phone `8015553335`, company "Run S Test Co"). That contact is now in GHL; delete it when convenient.
- Screenshots checked at 390 px and 1440 px: intro, question 1, result, capture.

## Job 3: "Have Atlas One build this for me"

- Button added next to the main Print / Save button in all five builders in `06 Calculators and Tools (NEW Aug 2026)/`: Employee Handbook Builder (handbook), Safety Manual Builder (safety-manual), W-2 At-Will Employment Agreement Builder (offer-letter), Independent Contractor Agreement Builder (ic-agreement), NDA Builder (nda). Outlined style, label "Have Atlas One build this for me", hidden in print.
- Forward page: `repo:build/index.html`, live at **https://forms.atlasonesolutions.com/build/?doc=<slug>** (200 confirmed for `?doc=nda`). One constant at the top: `const GHL_BUILD_FORM = "";`. Empty now, so the page shows the holding message with a prefilled mailto to David@AtlasOneSolutions.com (subject and body carry the document name) and the booking link. When terminal A creates the form, paste its URL into the constant; the page forwards with `?doc=<slug>` appended (uses `&` if the URL already has a query).
- Tools Hub card (Premium Builders, links to `build/?doc=blank`). Portal card via a local copy `06 .../Atlas_One_Build_This_For_Me.html` registered under Document Builders.
- Click test: NDA button href resolves to `build/?doc=nda`; forward page shows "Non-Disclosure Agreement" and the prefilled mailto.

## Job 4: master pricing V8 and the client price list

- `HR_Docs/Atlas_One_Master_Kit/_INTERNAL (do not share)/Atlas_One_INTERNAL_Master_Pricing_V8.xlsx`. 15 sheets: README, Membership, Payroll Models, Workforce & HR, Benefits & Retirement, Financial Services, Risk & Insurance, Technology & Operations, Business Consulting, AI Services, Documents, Screening, Web, Partner Income, Retail only. Columns exactly as specified; Margin $ and Margin % are formulas; Xperienced vendor costs are formulas like `=20*0.85` (vendor fee less the 15% commission) so Margin $ equals V7 "Atlas One keeps".
- **Row check PASS**: V7 49 of 49, Cost & Margin 41 of 41, Quick Quote 99 of 99. Nothing unplaced. The check reads the written file back. Script kept at `_INTERNAL (do not share)/tools/master-pricing-v8/build_master_pricing_v8.py` with a README and the Quick Quote JSON snapshot.
- Retired (row check passed): `A1_Sales/Atlas 1 Bookkeeping/Internal Master Bookkeeping/Atlas_One_INTERNAL_Master_Pricing_V7.docx` and `.pdf`, and `_INTERNAL (do not share)/Atlas_One_Cost_and_Margin_INTERNAL.xlsx` moved to `OneDrive:_to_delete/superseded-2026-09-12/pricing-V7-and-cost-margin/`. The Xperienced Approval sheet was not touched.
- Client facing: `A1_Sales/Pricing/Atlas_One_Price_List.html` and `.pdf` (two Letter pages, retail only, no vendor, margin or partner names, brand kit, print checked page by page).
- Master Hub: the Cost & Margin card now points at V8; the V7 card was dropped; two Price List cards added (Pricing & Quotes).

## Job 5: agreements inventory and the referral partner agreement draft

- `OneDrive:2. A1 Official Docs/4. Brokers_Vendors A1 Solutions/AGREEMENTS-INDEX-2026-09-12.md`: 41 agreement files (path, size, modified, sha256, detected title, counterparty, signed or unsigned, version words), current copy per group, duplicates moved, same title different content pairs.
- Moved (byte identical): `A1_Doc_Library Client_Vendor/.../Broker Contract Templates/Atlas_One_White_Label_Services_Agreement_Xperienced.pdf` to `_to_delete/superseded-2026-09-12/agreements/` (same path). Kept: the copy under `10_Broker_and_Partner_Docs/Experienced Payroll Pros/.../Signed docs/Old Docs Templates/`.
- Not moved, David to decide (same title, different bytes): White River Client Agreement Packet (docx and pdf, two copies each), Brittney Vendor Services Agreement (docx x2, pdf x3), Mutual NDA & Non-Circumvention (two pdfs), Excel Health Mutual NDA (signed vs unsigned docx), Ramp Partnership Agreement (Signed Agreement folder vs the loose copy). Full list in the index.
- Draft: `A1_Sales/A1 Agreements/Atlas_One_Referral_Partner_Agreement_TEMPLATE_2026-09-12.docx` (python-docx, DM Sans body, Horas headings, header on every page "DRAFT for attorney review. Not for signature."). Parties, purpose, definitions (Net Revenue), referral and attribution (first form submission or booked call wins, CRM timestamp decides), revenue share on collected money, payment the month after Atlas One is paid, clawback, W-9, term, termination, confidentiality, non circumvention (24 months), no exclusivity, liability, indemnity, licensing clause, Utah law, signatures, Schedule A by service line, referred client log, and a "notes for counsel" page. Nothing sent.
- Master Hub: Agreements section gained the draft and the index. The four existing Agreements cards pointed at `A1_Sales/Agreements/`, which does not exist on disk; the files live in `A1_Sales/A1 Agreements/`, so the cards were repointed.

## Job 6: website pricing page draft

- `A1_Sales/Website/Atlas_One_Website_Pricing_Page_DRAFT.html` (title starts with DRAFT, a draft bar on top) and `A1_Sales/Website/Pricing_Page_Notes_for_BRJ.md`.
- Essential $99 (setup waived) and Professional $399 (setup $495, often waived) priced; Enterprise and Concierge read "Built around your business. Starts with a 30 minute Back Office Audit." Value stats, do the math box (live), guarantee, three question picker (live, recommends a tier), seven member items, one CTA to the booking link. Every sentence is from the 2026-09-12 brochure.
- Rendered at 390 px and 1440 px; picker and math box exercised. Two Hub cards (Pricing & Quotes).

## Job 7: Portal and clean up

- Portal rebuilt with the path argument: `Atlas One PORTAL.html`, **BUILD Sep 12, 2026 12:11 PM**, 38 tools, 10.32 MB. Opened headless: stamp reads today, the Self-Assessment and the build forward page appear and open inside the Portal.
- Master Hub: 152 cards, every file card resolves on disk (five stale cards from earlier moves, What We Do x2, Sales Conversation Playbook, Prospecting Playbook, Document Inventory, were repointed to the subfolders where the files now live). Tools Hub: 28 tools, every file resolves.

## Self audit

- Reopened every file produced: the PNG, the two repo pages, the kit copy of the tool, the five patched builders, V8, the price list HTML and PDF, the agreements index, the docx, the pricing page draft, the notes, the Portal, both Hubs. All open without JS errors in headless Chromium.
- Links: Master Hub 152 cards, 0 missing; Tools Hub 28, 0 missing; every builder button href is the one stable address; forward page and live tool URLs return 200; webhook returned 200.
- Portal stamp: Sep 12, 2026 12:11 PM.
- Dashes: no em dashes, en dashes or spaced hyphens in any copy written this run. Hyphens remain inside compound words that already appear across the kit (W-2, bi-weekly, co-employment, E-Verify, Self-Assessment, Non-Disclosure Agreement). The agreements index contains dashes only inside file names and detected titles quoted from the documents.
- Fonts: the same subset Horas and DM Sans blobs the existing tools carry were reused (pyftsubset is not installed on this machine, so no new subsetting was done).

## Assumptions made

1. Tooling: Playwright was not installed for Python; the Node copy in the npx cache (1.63.0, Chromium 153) was used. python-docx and pypdf were installed into the user site to read docx and pdf files.
2. Scoring model for the self-assessment: each answer carries time, money and risk points lost; score = 10 x (1 minus points lost over the maximum possible). Leaks ranked by total points, ties by question order. 10 means holding, 0 means leaking.
3. The self-assessment posts only when an email or phone is given (GHL cannot attach a contact without one).
4. The Quick Quote array holds 99 service rows, not 104 as the Hub and BUILD-INDEX say; all 99 are in V8.
5. Vendor cost on Xperienced rows is shown net of the 15% commission so the margin column reproduces V7's "Atlas One keeps". Bookkeeping tier costs already net the 15/20/25% commission.
6. The Web sheet in V8 carries the Jason Petty card from the 2026-09-10 meeting kit (List and Member columns) with Jason's quote as cost, marked proposed. It is left OFF the Retail only sheet and OFF the client price list because nothing is agreed with Jason in writing.
7. The client price list uses the Marketing Sheet V7 figures where the internal V7 disagrees (1099 processing: $75 setup and $17 per form automated, $100 and $25 manual). V8 carries the internal numbers with the conflict noted.
8. Screening on the client price list uses the per product catalog retail from the Cost & Margin sheet, not the Quick Quote's flat $30 and $20.
9. Documents on the client price list are the current Quick Quote lines ($950 handbook and so on), not the 2026-09-06 options, because those are not decided. V8 carries both, labelled.
10. The referral partner draft went into `A1_Sales/A1 Agreements/` (the folder that exists) rather than creating a second `A1_Sales/Agreements/` folder.
11. The Vendor Partner Directory holds vendor to Atlas One rates only, so every percentage cell in Schedule A is blank.
12. The agreements inventory excluded brochures, quotes, benefit summaries, pricing sheets, SOPs, forms and marketing copy even when their text contains agreement wording; the exclusion list is in `_INTERNAL (do not share)/tools/agreements_inventory_2026-09-12.py`. "Signed" was inferred from the file name, a parent folder named Signed, or DocuSign / Ironclad text; PDFs without a text layer are flagged "confirm by eye".
13. The Master Hub self-assessment card sits under Sell & Pitch (it is a lead magnet, not a price document).
14. BUILD-INDEX.md was not edited (it is Cowork's document); its "Pricing sources of truth" table still names V7 and the Cost & Margin sheet.

## Retired (moved, not deleted)

- `_to_delete/superseded-2026-09-12/pricing-V7-and-cost-margin/`: `Atlas_One_INTERNAL_Master_Pricing_V7.docx`, `Atlas_One_INTERNAL_Master_Pricing_V7.pdf`, `Atlas_One_Cost_and_Margin_INTERNAL.xlsx`
- `_to_delete/superseded-2026-09-12/agreements/A1_Doc_Library Client_Vendor/Atlas One Document Library v1.0/0. Service Agmts and Letters/Broker Contract Templates/Atlas_One_White_Label_Services_Agreement_Xperienced.pdf`

## Not done

- Nothing in the brief was skipped. Run O part 2 was not started, as instructed.
- BUILD-INDEX.md pricing table not updated (see assumption 14).

## Commits (repo `atlas-one-intake-forms`, branch main)

Brief copy; job 1; job 2; job 3; job 4 log; job 5 log; job 6 log; job 7 log and report. Each pushed. GitHub Pages rebuilt after each push (last build status "built").

## Questions for David

1. Pricing conflicts to settle in one pass (all flagged in V8 Notes): 1099 processing ($100 and $15 internal V7 vs $75 and $17 marketing sheet); screening (Quick Quote $30 background and $20 drug vs the per product catalog $55 and $65); document services (Quick Quote lines vs the 2026-09-06 DIY / Assisted / Done-for-you options); Quick Quote website lines vs the Jason Petty card.
2. Jason Petty web packages: confirm the card (List $595 / $895 / $1,795 / $3,295 / $4,295, build $9,950; member column) before they go on any client material. They are in V8 only.
3. Referral partner agreement: which percentages go in Schedule A per service line, and does this draft replace the July 2026 Master Referral & Revenue Share Agreement (36 month non circumvention, liquidated damages) or sit beside it?
4. Agreements: the eight same title / different content groups in the index. Which copy is current for the White River packet, the Brittney vendor agreement, the Mutual NDA, Excel Health NDA, and Ramp? The loose Ramp copy outside the Signed Agreement folder can probably go.
5. The four Hub Agreements cards and five other cards pointed at files that had been moved into subfolders; I repointed them. Was the move deliberate (a new folder layout) so the Hub sweep should follow it, or should the files go back?
6. Self-assessment: should the public tools index and the seasonal Q-1 / LT-4 emails link it now, and do you want the GHL side (custom fields for `score_time` etc.) mapped by terminal A?
7. Pricing page draft: keep Enterprise and Concierge fully unpriced, or show "from $999" style anchors? The draft follows the recommendation (no price).
8. The client price list shows every division on two pages. Do you want a one page short version for leave behinds as well?
9. Test contact "Run S Test Co" (phone 8015553335) is in GHL from the webhook test; delete or keep as a fixture?
