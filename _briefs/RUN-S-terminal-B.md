# RUN S (terminal B, code and files only, no GHL browser UI): the unattended build batch

Written by Cowork 2026-09-12 evening. David is away. Build everything below end to end, in order, without asking a
single question. Make the reasonable call, record every assumption in the report, and batch questions at the END of the
report. Never touch the GHL browser UI in this run (terminal A owns it). Never send an email, never enable anything in
production, never delete: removals are `mv` into `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-12/`.
Copy this file to `_briefs/RUN-S-terminal-B.md` in the atlas-one-intake-forms repo first and log progress in it.

Paths. Master Kit: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv`.
Marketing root is two levels up from the Master Kit (`2. Atlas 1 Solutions Marketing/`); `A1_Sales/` and
`Atlas_One_MASTER_HUB.html` live there. Brand kit: `Master_Kit/A1_Final Brand/` (Horas-Medium.ttf, DM Sans static TTFs,
logo SVGs under `1. Logos/`). Brand rules: four colours only (#23304D, #788DE3, #FAFAF8, #DBE4ED), Horas headlines,
DM Sans body, fonts embedded as base64 (subset with pyftsubset, woff2), no CDN, no dashes in copy (use commas, periods,
colons, parentheses), status shown by form not colour. Every HTML tool must work offline on iPhone, iPad and desktop.
Verify visually: render with headless Chromium (Playwright is installed) and look at the screenshots before claiming
anything works. Every new or changed sales asset gets a card on the Master Hub (it is a JS array of
`["section", "Title", "Description", "relative/path", "type"]` entries; the Pricing section id is `price`, look at the
existing entries and match the pattern). Every tool edit means rebuilding the Portal at the end:
`python3 "<Master_Kit>/_INTERNAL (do not share)/build_portal_single.py" "<Master_Kit>"` and confirm the build stamp.

Commit and push after every numbered job so nothing is lost. Final report to
`<Master_Kit>/_BUILD-LOG/RUN-S-report.md`: what was built, exact file paths, what was retired, assumptions, anything
skipped and why, then the batched questions. Also write a short self-audit section: reopen every file you produced,
check links resolve, check the Portal stamp, check the Hub cards open, check no dashes in copy.

---

## Job 1: retention calculator sample image for the 45-C email (small, do first)
The Retention Cost Calculator is hosted at `https://forms.atlasonesolutions.com/tools/retention-cost/` (source in the
repo under `tools/retention-cost/`, and in `Master_Kit/06 Calculators and Tools (NEW Aug 2026)/`). Produce a static,
branded PNG of a filled-in result for a believable sample: a 25-employee company, two people leaving a year, $52,000
average salary. Use the calculator's OWN result numbers (drive it in headless Chromium, fill the inputs, read the
result); never type a number into the image by hand. Frame it: off-white background, the result panel, a one-line
caption "Sample: 25 employees, two people leave in a year" in DM Sans, logo mark bottom right. 1200 px wide, under 250 KB.
Save to the repo at `tools/assets/retention-sample-25ee.png` so it serves at
`https://forms.atlasonesolutions.com/tools/assets/retention-sample-25ee.png`. Push, wait for Pages, curl the URL and
confirm 200. Put the final URL in the report. (Terminal A inserts it into 45-C in Run Q.)

## Job 2: Back Office Self-Assessment tool (new free tool)
Spec: `<Master_Kit>/_BUILD-LOG/cadence-email-ideas-2026-09-12.md`, section "New tool to build". Build it like the
other free tools in the repo `tools/` folder (copy the structure, webhook posting code and brand shell from an existing
one, for example `tools/vendor-consolidation/`). Ten questions, one screen each on a phone, two minutes:
1. How is payroll run today? (in-house software / a payroll service / a PEO / an accountant / not sure)
2. Who collects certificates of insurance from subs and vendors? (nobody / me / office manager / our insurance agent / no subs)
3. When were benefits last shopped? (this year / 1 to 2 years / 3+ years / we do not offer benefits)
4. Workers comp class codes reviewed in the last 12 months? (yes / no / not sure)
5. How many vendors and subscriptions does the business pay every month? (under 5 / 5 to 10 / 11 to 20 / more than 20 / no idea)
6. Hours a week the owner spends on admin (payroll questions, vendor calls, paperwork)? (under 2 / 2 to 5 / 6 to 10 / more than 10)
7. Result of the last workers comp or tax audit? (never had one / no surprises / a surprise bill / not sure)
8. Age of the employee handbook? (under a year / 1 to 3 years / older / none)
9. Who answers HR questions? (me / office manager / our PEO or HR service / nobody, we look it up)
10. Any two software tools doing the same job? (no / probably / yes, several / not sure)
Score three things, Time, Money, Risk, 0 to 10 each, with a plain explanation of how the score was reached. Result
page: the three scores as form-differentiated tiles (solid, tinted, outlined; never a fifth colour), the three biggest
leaks in one sentence each, and a button "Book the 30 minute Back Office Audit" to
`https://api.leadconnectorhq.com/widget/groups/book-david`. Optional name, company, email, phone at the end, then submit
to the existing tool-capture webhook (same endpoint and payload shape the other tools use; include every answer and
the three scores as fields). Lives at `tools/self-assessment/index.html`; also copy the file into
`Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Back_Office_Self_Assessment.html` and register it in
`_INTERNAL/build_portal.py` (free tools group) and on the Tools Hub and the Master Hub. Test on a 390 px viewport and
desktop with screenshots; submit one test with a unique phone and plus-addressed email and confirm the webhook
returns 2xx. Push and confirm the live URL returns 200.

## Job 3: "Have Atlas One build this for me" button on the document builders
Add one button to each of: Employee Handbook Builder, Safety Manual Builder, W-2 At-Will Employment Agreement Builder,
Independent Contractor Agreement Builder, NDA Builder (all in `06 Calculators and Tools (NEW Aug 2026)/`), plus a card
on `Atlas One — Tools Hub.html` and the Portal. Placement: next to the existing Print / Save buttons, outlined style
(form, not colour), label "Have Atlas One build this for me". Every button links to ONE stable address:
`https://forms.atlasonesolutions.com/build/?doc=<slug>` where slug is handbook, safety-manual, offer-letter,
ic-agreement, nda, or blank from the Hub. Create `build/index.html` in the repo: a small branded page that reads the
`doc` parameter and forwards to a GHL form URL held in ONE constant at the top of the file
(`const GHL_BUILD_FORM = "";`). Until terminal A creates that form (Run R) the constant is empty and the page shows a
branded message: "Tell David which document you need" with a mailto to David@AtlasOneSolutions.com prefilled with the
document name, and the booking link. When the form exists, terminal A only edits the constant. Pass `doc` through as a
query string parameter on the forward so the form can prefill. Rebuild the Portal, verify the stamp, click one button
in headless Chromium and confirm the forward page renders.

## Job 4: master pricing sheet, consolidated (INTERNAL)
Read first: `_INTERNAL (do not share)/Atlas_One_INTERNAL_Master_Pricing_V7*`, `_INTERNAL/Atlas_One_Cost_and_Margin_INTERNAL.xlsx`,
`09 Quick Quote Tool/Atlas_One_Quick_Quote.html` (its 104 service rows and prices are in a JS array), the project
pricing facts in `_BUILD-LOG/BUILD-INDEX.md` (membership tiers with setup fees, four payroll models, AI services Aug 29
set, bookkeeping retail from the Marketing Sheet V7, document services from
`A1_Sales/Atals 1 Membership Pricing/Atlas_One_Document_Services_Pricing_Options_2026-09-06.md`, screening from the Cost & Margin
sheet, Jason Petty web packages if a retail price is recorded anywhere in `4. Brokers_Vendors A1 Solutions/10_Broker_and_Partner_Docs/Jason Petty/`;
if none is recorded, leave the row with "retail TBD" and say so).
Build `_INTERNAL (do not share)/Atlas_One_INTERNAL_Master_Pricing_V8.xlsx` with openpyxl: one sheet per division plus
Membership, AI Services, Payroll Models, Documents, Screening, Web; columns: Service, Unit, Retail price, Vendor cost,
Margin $, Margin %, Setup fee, Notes, Source. Formulas for margin, not typed numbers. Every V7 row and every Cost & Margin
row must appear (write a check that counts them and prints the ones you could not place). A "Retail only" sheet at the end
that is safe to copy into client material. Then a client-facing `A1_Sales/Pricing/Atlas_One_Price_List.html` + `.pdf`
(retail only, no vendor, no margin, no partner names, brand kit, one to two pages, prints clean) and a Master Hub card.
Retire V7 and the Cost & Margin sheet to `_to_delete/superseded-2026-09-12/` ONLY if the row check passes; otherwise keep
them and flag it. Do not touch the bookkeeping Approval sheet (vendor family) at all.

## Job 5: partner and vendor agreements, inventory and consolidation
Folder: `OneDrive-AtlasOneSolutions/4. Brokers_Vendors A1 Solutions/` (several copies of the same agreements exist).
Read `_BUILD-LOG/partner-agreements-2026-09-12.md` and `_BUILD-LOG/agreements-and-proposal-system-brief-2026-09-11.md`
first. Inventory every .docx/.pdf that is an agreement (broker, vendor, referral, rev-share, NDA, CSA, hold harmless):
path, size, modified date, sha256, detected title, counterparty, signed or unsigned, version words in the name. Group
by identical hash and by same title. Pick the current one per group (latest signed beats latest unsigned beats newest
file). Move byte-identical duplicates to `_to_delete/superseded-2026-09-12/agreements/` preserving the relative path.
Do NOT move anything that differs in content; list those pairs for David. Write
`4. Brokers_Vendors A1 Solutions/AGREEMENTS-INDEX-2026-09-12.md` (the current copy of each, where it is, status) and put
the same table in the report. Then draft `A1_Sales/Agreements/Atlas_One_Referral_Partner_Agreement_TEMPLATE_2026-09-12.docx`
(python-docx, brand fonts): parties, referral definition, attribution (first form submission or booked call wins),
rev-share schedule as a table by service line pulled from the Vendor Partner Directory xlsx in `_INTERNAL` (use the
retail-facing percentages only; if the directory holds none, leave the cells blank), payment timing (paid the month
after Atlas One is paid), term, termination, confidentiality, no exclusivity, signature blocks, and a visible header
"DRAFT for attorney review". It is a draft for David and counsel, nothing is sent. Add a Hub card under Agreements or
the nearest section.

## Job 6: website pricing page draft for BRJ
Build `A1_Sales/Website/Atlas_One_Website_Pricing_Page_DRAFT.html` (brand kit, responsive, self-contained) following
this recommendation, already recorded in the project: show Essential ($99, setup waived) and Professional ($399, setup
$495 often waived) with prices; show Enterprise and Concierge as "Built around your business. Starts with a 30 minute
Back Office Audit." with no price on the page; lead with cost against savings (the audit pays for the membership:
33% of an owner's week goes to admin, 88 days a year, 15 to 25 hours a month back, 15 to 30% saved), the Audit
Guarantee (two times the first year membership in documented savings or risk removed, or nothing to buy), the
three-question tier picker, and one CTA to `https://api.leadconnectorhq.com/widget/groups/book-david`. Take the copy
from `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Brochure.html` (built today) so the two agree word for
word. Write a one-page `A1_Sales/Website/Pricing_Page_Notes_for_BRJ.md` (what to build, what not to show, links).
Screenshot at 390 px and 1440 px. Hub card. Mark it DRAFT in the title; David decides before it goes to BRJ.

## Job 7: clean-up and the report
Rebuild the Portal (path argument!), open it headless, confirm the stamp shows today and the new tools appear. Re-check
the Tools Hub and Master Hub open and the new cards resolve. Commit and push. Write `RUN-S-report.md` as described at
the top, including a "Questions for David" section at the very end, and a "Not done" section if anything is left.
Do not start Run O part 2 (the contacts review sheet is not finished).

---

## Progress log (terminal B)

- 2026-09-12: brief copied into the repo. Starting Job 1.
- Job 1 done: tools/assets/retention-sample-25ee.png (1200x507, 104 KB). Calculator inputs: salary 52000, team 25, turnover 8% (2 of 25). Calculator output: $52,000 per departure, $104,000 a year, 2 people lost, ~5.2 months to a productive replacement.
- Job 2 done: tools/self-assessment/index.html (412 KB, fonts embedded). Copy in Master Kit 06 folder as Atlas_One_Back_Office_Self_Assessment.html. Registered in build_portal.py (Calculators & Diagnostics), Tools Hub (Diagnostics & Savings, tag new), Master Hub (Sell & Pitch), and tools/index.html (fourth card). Test submission through the page: webhook returned 200 (email muddybudmods+runs5363335@gmail.com, phone 8015553335). Scoring: 10 = holding, 0 = leaking; each option carries time/money/risk points lost, score = 10 x (1 - lost / max possible).
