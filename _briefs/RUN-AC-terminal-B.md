# RUN AC (terminal B, code and files only, no GHL UI): the Sunday unattended batch

Written by Cowork 2026-09-13. David is away. Do every job end to end, in order, without asking a single question.
Answer every permission prompt yourself. Make the reasonable call, log it under Assumptions, put every question in
"Questions for David" at the END of `<Master_Kit>/_BUILD-LOG/RUN-AC-report.md`. Never send an email, never enable
anything in production, never spend money, never delete (mv to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-13/`).
Brand rules: four colours (#23304D, #788DE3, #FAFAF8, #DBE4ED), Horas headlines, DM Sans body, fonts embedded as
base64 woff2, no CDN, no dashes in copy, status by form not colour, every tool works offline on iPhone, iPad and
desktop (scrollWidth equals viewport at 390 px). Verify by rendering in headless Chromium and looking. Commit and
push after every job. Master Kit: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete
-e archiv -e "TO DELETE"` (use the OneDrive one). Copy this file to `_briefs/RUN-AC-terminal-B.md` and log there.

## Job 0: live log rule (do this first, it applies to every job below)
Create `<Master_Kit>/_BUILD-LOG/TERMINAL-B-live.md` and append a dated line after every step of every job
("done: ...", "next: ..."). Add the same rule to the repo `CLAUDE.md` (create it if missing) so every future run in
this repo does it automatically: read the brief from disk, append to `_BUILD-LOG/TERMINAL-<A|B>-live.md` after every
step, write `RUN-<X>-report.md` at the end with Assumptions and Questions for David, never ask questions mid-run,
answer permission prompts yourself, never send / enable SMS / enable HIPAA / delete / deploy / spend. Commit.

## Job 1: fonts offline (this was Run AB; do it here)
Every HTML tool in `06 Calculators and Tools (NEW Aug 2026)/` and the Master Kit root that still loads a font from
fonts.googleapis.com or fonts.gstatic.com (thirteen at last count): back up to `_to_delete/superseded-2026-09-13/
fonts-before/`, remove the Google link, embed DM Sans 400 and 700 (500 only where used) as base64 woff2 the way
`repo:tools/self-assessment/index.html` does; Horas only if used and not already embedded. Render each at 1440 px
with the network blocked and confirm the computed font on body is DM Sans, no errors, no layout change beyond the
font. Table in the report. Rebuild the Portal (path argument), confirm the stamp, open two fixed tools inside it offline.

## Job 2: client portal deploy-readiness kit (the portal is BUILT, not deployed; David does the 10-minute part)
Repo `~/Projects/atlas-one-portal` (CI green, commit 3a5478a or later). Produce everything so David's part is
clicks only: (a) `DEPLOY.md` in the repo written for a non-technical reader: create the Vercel account, import the
repo, the exact environment variables to paste (names from the code, values marked "from GHL Private Integration"
or "generate with this command"), the CNAME record for portal.atlasonesolutions.com in GoDaddy (exact host, exact
target), the two GHL custom fields to create (`services`, `savings_to_date`, exact types) and the key scope
`locations/customFields.readonly`; (b) `vercel.json` and any build settings so the import works first try; (c) a
`scripts/preflight.mjs` that checks env vars are set and the GHL token works, printing plain-English pass/fail;
(d) run the full test suite once more and confirm green. Copy `DEPLOY.md` to `<Master_Kit>/_BUILD-LOG/portal-DEPLOY-
for-David.md`. Do NOT create the Vercel project, do NOT touch DNS.

## Job 3: Quote & ROI Builder, PowerPoint export
`08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html` (or the Quote & ROI Builder if the Cockpit is not the
current one; check the Master Hub Pricing cards and use the one they call current). Add an "Export deck (.pptx)"
button that builds a 10-slide branded deck in the browser (pptxgenjs embedded as base64, no CDN): cover, the
prospect's situation, itemized quote, PEO separate, savings and ROI, time value, guarantee, membership tier picked,
next steps, contact. Numbers come only from the page state. Render the exported deck to images (python-pptx +
the Run U HTML renderer) and look. Then retire the old Excel-in / deck-out ROI generator only if the Hub marks it
"older"; otherwise leave it and note.

## Job 4: benefits routing decision tool (new, spec in `13 Benefits Strategy/Atlas_One_Member_Program_Spec_2026-08-29.docx` section 6)
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Benefits_Routing_Tool.html`: inputs entity type, headcount,
states, current coverage, owner-only or employees, budget per employee; output the recommended route (group plan
through carrier partners, PEO plan through co-employment, ICHRA, alternative funding whole-group, individual) with
a two-sentence why and the one question David should ask next. Encode the rules from the spec and the carrier rules
in BUILD-INDEX (under 500 lives one carrier; alternative funding is never a tier; never say Atlas One has a health
plan; AHPs closed to solo owners; ICHRA needs no employment relationship). Portal + Tools Hub + Master Hub cards.

## Job 5: HR and payroll compliance calendar by state (sellable, subscription idea from the growth review)
`06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Compliance_Calendar.html`: pick states and headcount, get the
dated calendar for the next 12 months (federal: ACA 1095, W-2/1099, 941/940, EEO-1 if applicable, poster updates,
OSHA 300A posting Feb 1 to Apr 30; state: new hire reporting windows, pay frequency rules, sick leave accrual starts,
minimum wage change dates, harassment training deadlines, wage notice rules) for UT, AZ, FL, NV, CA, CO, ID, TX, OR,
WA to start. Every line carries a "confirm before relying" note and a source URL; nothing invented, if unsure mark
"verify". Export to .ics and print. Brand shell, Portal + Tools Hub + Master Hub cards.

## Job 6: COI collection and sub payment hold, phase 1 (David's product idea; construction first)
Research first (30 minutes, write findings at the top of the job log): what do myCOI, Jones, TrustLayer, Billy and
GHL-native options charge and do; what a construction client with 5 to 50 subs actually needs. Then build the
self-contained MVP: `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_COI_Tracker.html`: sub list (name, trade,
email, phone), certificate on file (GL yes/no with expiry, WC yes/no with expiry, waiver signed yes/no), auto-flag
expiring within 30 days and missing, "hold payment" status by form, request email text generator (no dashes), CSV
in and out, JSON save and reload, print report. Plus a one-page spec `_BUILD-LOG/coi-collection-phase-2-spec.md`
for the GHL automation (auto-request on new sub, expiry chase) and the client portal plug-in. Portal + Hub cards.

## Job 7: software and partner marketplace catalog for BRJ
`A1_Sales/Website/Atlas_One_Marketplace_Catalog_for_BRJ.xlsx` and `.md`: every software and partner Atlas One
resells or refers (from the Vendor Partner Directory in `_INTERNAL`, V8 pricing Technology sheet, Quick Quote
technology rows): name, category, one-line what it does, retail or "quote", where BRJ gets the OFFICIAL logo (the
vendor's brand or press page URL, never a scraped image), status (signed / pending / do not sign). No vendor costs,
no margins, no partner rev-share numbers. Hub card.

## Job 8: email-safe marketing HTML how-to
`12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`: the booking wrapper from Run E is the template; document exactly
how to build a GHL email that survives Outlook (table button with bgcolor, no inline styles on anchors, logo URL,
signature block, no dashes), with a copy-paste skeleton and the source-dialog rules from BUILD-INDEX rule 23 and 31.

## Job 9: Census v2
`06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html` and `repo:census/index.html`:
add relationship column, full address with ZIP-only under 10 employees, remove tobacco, optional SSN (masked, never
posted, local export only), dependent and spouse expansion, "multiple plan options?" question. Keep the webhook
payload backward compatible (new fields only). Render, test a sample, push, confirm 200.

## Job 10: help desk panel
Add a "What is this for?" panel to the Portal (one paragraph per tool, drawn from each tool's own header copy, in
`build_portal.py` so it is generated) and to the Tools Hub. Rebuild the Portal, confirm.

## Job 11: report
Rebuild the Portal a final time (path argument), confirm the stamp and count. Self-audit: reopen every file
produced, links resolve, no dashes in new copy, scrollWidth 390 on every new tool. `RUN-AC-report.md` with paths,
what was looked at, assumptions, skipped items, then Questions for David. Commit and push.
