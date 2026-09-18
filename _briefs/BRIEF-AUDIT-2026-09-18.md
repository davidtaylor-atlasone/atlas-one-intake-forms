# BRIEF for the AUDIT terminal: Run A1 (the Back Office Audit Workbench)

Terminal name: AUDIT. Files and code only: the Master Kit on OneDrive, A1_Sales, and the repo
`~/Projects/atlas-one-intake-forms` (assets in `_briefs/assets/run-A1-audit/`). Never the GoHighLevel browser,
never the portal repo (those parts are queued for their own terminals). Build end to end, no questions, answer
every permission prompt yourself, make the reasonable call and log it under Assumptions, questions at the END of
the report. Never fork, background or delegate to a sub agent. Do only the jobs written here.

Log to `<Master_Kit>/_BUILD-LOG/TERMINAL-AUDIT-live.md` (one dated line after every step). Report to
`<Master_Kit>/_BUILD-LOG/RUN-AUDIT-report.md` (quoted heredoc or file tool) AND a copy in the repo assets
folder. Commit and push after each job. Hard stops: sending an email, enabling SMS, enabling GHL's HIPAA
feature, deleting a file (move to `OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-18/` instead),
deploying to production, spending money.

Find the Master Kit by name: `find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete
-e archiv`. Call it `$MK`. A1_Sales is `$MK/../../A1_Sales`. Read before building: `$MK/_BUILD-LOG/
back-office-audit-run-design-2026-09-18.md` (the design, section 3 is the spec), `$MK/08 ROI Quote Master
Template/Total_Impact_Model/README — Total Impact Model.md`, `total_impact_model.py`, `build_tim.py`,
`SAMPLE_Tell_Me_More_LLC.json`, the Vendor & Software Audit tool, the Payroll to GL Import Converter (its column
classifier), the COI to WC Premium Estimator, `$MK/09 Quick Quote Tool/` prices.json, the atlas-offer,
atlas-pricing, atlas-brand, atlas-voice and atlas-ship skills in `~/.claude/skills/`.

Brand and build rules (non negotiable): four colours (#23304D, #788DE3, #FAFAF8, #DBE4ED), Horas headlines,
DM Sans body, DM Mono for numbers, fonts embedded as base64 from the existing tools (no CDN, no Google Fonts),
status by form not colour, no dashes anywhere in copy (a phone number keeps its hyphens), works offline on
iPhone, iPad and desktop (scrollWidth equals viewport at 390 px), verified by rendering in headless Chromium
and looking at the screenshots. Client facing files: no vendor or PEO brand names, no margins, no internal
prices. Phone on every footer 380-CALL-A1S (380-225-5217). Booking link for the follow up:
https://api.leadconnectorhq.com/widget/groups/book-david.

## Job 1: the prospect JSON gains an `audit` block (schema first, nothing else changes)
File: `$MK/08 ROI Quote Master Template/Total_Impact_Model/`. Add `AUDIT_SCHEMA.md` describing the optional
top level `audit` object the model IGNORES (prove it: run `total_impact_model.py` on the sample before and after
adding an `audit` block; outputs identical; save both to `_BUILD-LOG/runA1-tim-before.txt` and `-after.txt`).
```
"audit": {
  "code": "TMM-2026-09",            (short id, letters and digits, used by the pulse link)
  "date": "2026-09-18", "headcount": 25, "states": ["UT"], "pay_frequency": "biweekly",
  "vendors": {"source":"card statements Jun to Aug 2026","monthly_spend":0,"annual_spend":0,"count":0,
              "overlaps":[], "moves":[], "cancel":[], "hours_month":0, "score":0, "rows":[...]},
  "payroll": {"source":"register 2026-09-05","gross_annual":0,"employer_taxes_annual":0,
              "provider_fee_per_check":0,"provider_fee_annual":0,"by_department":{},"atlas_one_quote_annual":0,
              "atlas_one_model":"peo"},
  "wc": {"carrier_page_date":"","expiration":"","mod":1.0,"expense_constant":0,
         "classes":[{"code":"8810","payroll_estimate":0,"rate":0,"premium":0,"actual_payroll":0}],
         "premium_total":0,"rerated_premium":null,"subs":{"spend":0,"coi_pct":0,"labor_share":1}},
  "benefits": {"renewal":"","carrier_named_on_report":false,"section_125":false,"employer_share_pct":0,
               "tiers":[{"tier":"EE","rate":0,"enrolled":0}],"employee_share_annual":0},
  "pulse": {"sent":0,"responses":0,"averages":{},"free_text":[]},
  "fixes": [{"line":"wc_premium","rank":1,"value":0,"confidence":0.8,"effort_days":14,"why":""}],
  "offer": {"tier":"professional","monthly":399,"setup":495,"lines":[],"good_through":"2026-10-18",
            "guarantee":"2x"}
}
```
Every dollar in `audit` is evidence; the model still reads only `lines`, `atlas_one_fees`, `reconcile_against`.

## Job 2: Vendor & Software Audit hand off (edit the master, then the copies)
File: `$MK/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Vendor_Software_Audit.html` (master). Add:
(a) multi file drop and multi paste (three statements or exports at once; rows de duplicated by normalized
merchant + amount + date; months counted across files); (b) a "Send to Audit" button that downloads
`<Company>_audit_vendors.json` containing the `audit.vendors` block above plus the two Total Impact lines it
justifies: `software_stack` = duplicate and cancelled annual spend (note lists the vendors), `vendor_audit` =
annual spend that moves under one relationship as a MEMO line (shown, not added: consolidated spend is not a
saving, the note says so), and `hr_hours` contribution as hours only (no dollars). Nothing else on the tool
changes. Apply the same edit to the Spanish twin and to `repo:tools/vendor-audit/index.html` (public copy,
same button, label "Save my results"). Screenshot before and after at 1200 and 390.

## Job 3: the Audit Workbench (new, internal, one file)
File: `$MK/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Audit_Workbench.html`, self contained, internal
(carries prices), same shell as the other 2026-09 tools (the restyled 53 calculator shell). Left rail of six
stages, right pane per stage, the Total Impact number pinned in the header from stage 1 onward. Load and Save
the prospect JSON (Load button, drag and drop, paste; Save writes the whole file back, `audit` block included),
same as the Total Impact page. Everything in the browser; nothing posted anywhere.

Stage 1 Vendors: drop the `_audit_vendors.json` from Job 2 (or paste a statement directly: embed the vendor
tool's engine, do not duplicate its UI, import the same catalog and functions). Shows the table, writes the
lines.

Stage 2 Payroll: drop a payroll register (xlsx or csv) or a provider invoice (paste text). Reuse the GL
Converter's column classifier (copy the functions, note the source lines in a comment; do not change the
Converter). Produce headcount (distinct employees), pay frequency (from check dates), annualized gross,
employer taxes, provider fee per check and annual (from any fee, admin, service or PEO column or invoice line;
if none found show "no provider fee line found" and leave `payroll_admin` not quoted), payroll by department.
Atlas One quote for the same headcount and frequency from prices.json for each of the four payroll models
(PEO per EE per check, PEO percent of gross, ASO, HCM, bookkeeping payroll), picker defaults to PEO per EE.
`lines.payroll_admin` = provider fee annual minus the Atlas One quote annual (can be negative, prints as such,
like BRJ). Never invent a provider fee.

Stage 3 Workers comp and benefits: two typed entry cards with live math. WC: rows per class code (code,
payroll estimate, rate per $100, premium computed), mod, expense constant, premium total (computed and
overridable to the dec page figure), expiration, and the actual payroll per class from Stage 2 departments
(David maps department to class with a dropdown). Shows over or under reported payroll per class and "audit
exposure" (under reported payroll x rate x mod) as a MEMO. Subs block (spend, COI percent, labor share) using
the estimator's math writes `lines.subcontractor`. `lines.wc_premium` is written ONLY when David types a
re-rated premium or a market indication in the "re-rated" box (note says where it came from); blank leaves it
not quoted. Benefits: tiers table (tier, monthly rate, enrolled), employer share percent, renewal date, Section
125 in place yes or no. Computes employee share annual and, when Section 125 is "no",
`lines.section_125` = employee share annual x 0.0765 with the note "employer FICA on pre tax premium, no
cafeteria plan today". `health_premium` is never written by the bench (the health engine owns it); the card
says so. Both dates (WC expiration, benefits renewal) print in a "Dates for GHL" box for David to type into the
contact until the GHL part lands.

Stage 4 Pulse: paste box for the aggregate the portal will export later (JSON) plus a manual grid (eight
questions x up to five responses, 1 to 5) for the interim. Computes averages, shows the two lowest scoring
questions, writes `audit.pulse`. Writes `hr_hours` and `turnover` only as MEMO lines and only when David enters
a loaded rate (hours from the vendor stage plus the pulse's "hours a week chasing admin" average x headcount x
52) or the retention calculator's replacement cost; otherwise nothing. The eight questions (build them into the
bench and into `_BUILD-LOG/pulse-questions-2026-09-18.md` for the portal terminal; 1 to 5 scale unless noted):
1. I know exactly who to ask when I have a pay, benefits or HR question.
2. My paycheck has been right every time this year.
3. I understand what my benefits cost me and what they cover.
4. Getting a form, a letter or a document from the company is quick.
5. About how many hours a week do you spend chasing admin (timesheets, forms, approvals, logins)? (0, 1, 2 to 3, 4 to 6, more than 6)
6. How many different apps or logins do you use to get paid, request time off and find company documents? (1, 2, 3, 4, 5 or more)
7. If a good friend asked, I would recommend working here. (1 to 5)
8. One thing that would make your week easier: (free text, optional)
No name, no email, no department. The intro line: "Three minutes, anonymous, sent to a few people so your
company can fix what wastes your time. Your answers go to Atlas One, not to your manager."

Stage 5 Total Impact and fixes: run the model's arithmetic in JS (port `build`, `fee_row`,
`verify_no_double_count`, `three_year` from `total_impact_model.py` one to one; test against
`SAMPLE_Tell_Me_More_LLC.json` and `prospects/big_red_jelly.json`, the bench must print $13,117 and the BRJ
figures to the dollar, save the check to `_BUILD-LOG/runA1-parity.txt`). Fee row from the tier picker (Essential
under 10, Professional 10 to 49, Enterprise 50 to 149, Concierge 150 plus, editable) with prices and setup fees
from prices.json; `atlas_one_fees.source` = "Audit Workbench". Ranker: every non memo, non fee line with a
figure; score = value x confidence (1.0 verified from a document, 0.8 David's entry, 0.5 estimate; set per line,
default by source); effort days table (software_stack 7, vendor_audit 14, payroll_admin 30, wc_premium 45,
subcontractor 14, section_125 30, bookkeeping 30, epli 14, retirement_401k 60, ai_assistant 14, turnover 90),
tiebreak lower effort. Top three shown with a one line "why" David can edit, written to `audit.fixes`. Prints
the 2x test: documented savings (non memo total) vs 2 x first year membership (12 x monthly + setup), pass or
"not yet documented", by form.

Stage 6 Offer: picks the tier, lists the quoted lines with prices (read from prices.json by key, never typed),
good through = report date + 30, guarantee line from atlas-offer ("2x first year membership in documented
savings or risk removed, or there is nothing to buy"). "Save prospect file" then "Build report" (shows the
python command below with the file path filled in, and a Print button that prints a client safe version of
the same page: internal boxes hidden, prices shown, vendor rows shown, no margins anywhere).

## Job 4: the written offer, `build_audit_report.py`
File: `$MK/08 ROI Quote Master Template/Total_Impact_Model/build_audit_report.py` (beside `build_tim.py`,
reuse its font embedding and template approach). `python3 build_audit_report.py prospects/<file>.json` writes
`Atlas_One_Back_Office_Audit_<Client>_<YYYY-MM-DD>.html` and `.pdf` (Playwright, same as Run AT) into the
folder given by `--out` (default: next to the JSON). Client facing, four sections on two printed Letter pages:
(1) hero: "Your Back Office Audit", client, date, the Total Impact number (net first year, fees visible as a line),
six division subtotals with "not in scope" where nothing was quoted, memo lines under "shown, not added";
(2) "The three fixes, ranked": rank, division, the fix in one sentence, what it is worth a year, what it takes
(effort days as "about two weeks"), the source in plain words ("from your July card statement");
(3) "What we found": the vendor count and overlaps, the payroll read, the WC read, the benefits read, the pulse
averages (only if five or more responses; otherwise "pulse in progress"), each three lines at most;
(4) "Your offer, good through <date>": tier, monthly, setup, the quoted lines, what happens in the first 30
days (from the Client Launch Deck timeline), the Audit Guarantee, one button "Book the 45 minute follow up"
(group booking link), footer with phone and AtlasOneSolutions.com. Zero dashes, zero vendor names, no
"licensed in all 50 states" (say "serving businesses in all 50 states"). Render the sample, rasterize both pages,
look at them, no clipped text, no orphan headings.

## Job 5: sample audit, prep email, COMMAND, skill
a. Sample: extend `SAMPLE_Tell_Me_More_LLC.json` with a full `audit` block (fictional, consistent with its
   existing lines: 25 employees, biweekly, the same $4,200, $7,600, $1,900, $3,100, $1,600) and build the sample
   report into `$MK/12 DEMO Proposal Set/Atlas One — DEMO Proposal Set/` beside the other Tell Me More pieces.
   The Total Impact page must still load the sample and show $13,117.
b. Prep email as a finished file `$MK/_BUILD-LOG/cadence-emails-2026-09-13/audit-prep.html` (same wrapper,
   signature, button and rules as the booking emails; read `INDEX.md` and `Atlas_One_Email_HTML_How_To.md`
   first; add the INDEX row; workflow "Booking: confirm and remind", mode queued for the GHL terminal).
   Subject: "What to have ready for your Back Office Audit". Body, plain and short, no dashes: thanks for
   booking; the audit takes 30 minutes and you leave with a number, three fixes and a written offer; to make it
   count, have these nearby (three months of bank or card statements, or the QuickBooks report Expenses by
   Vendor Summary for the last 90 days, or your Ramp vendor export; your last payroll register or provider
   invoice; your workers comp declarations page; your benefits renewal or a current carrier invoice); one line
   asking them to forward the staff pulse link to five people when it arrives (three minutes, anonymous);
   "nothing is shared and nothing leaves the call unless you say so"; button "Upload them ahead of time" pointing
   at the Form D placeholder URL `FORM_D_URL` (a literal token the GHL terminal replaces); standard signature.
c. COMMAND: add the Workbench (Sell & Pitch, pinned) and `build_audit_report.py` (Internal) to
   `_INTERNAL (do not share)/catalogue.py`, run `catalogue_check.py` then `build_command.py` with the Master Kit
   path, confirm the stamp in the tab title.
d. Skill: write `~/.claude/skills/atlas-audit/SKILL.md` (frontmatter name `atlas-audit`, description under 200
   characters, in David's own phrases: "Use when running, prepping, scoring or writing up a Back Office Audit,
   the audit workbench, the staff pulse, the three fixes, the 30 day offer or the Total Impact number") with:
   the six stages in order, the file paths, the rule that the prospect JSON is the only data file, what is never
   invented (health_premium, wc_premium without a re-rate, provider fee), the ranker weights, the tier rule, the
   2x wording, the report command, and the pulse and GHL parts still queued. Zip it to
   `_BUILD-LOG/skills-for-claude-app/atlas-audit.zip` like the other eight and add a line to
   `skills-system-2026-09-17.md` under a "2026-09-18 atlas-audit" heading.

## Job 6: verify and retire
- Playwright: Workbench at 1200 and 390 (every stage, sample loaded, no console errors, no horizontal scroll),
  vendor tool before and after, report pages as PNG. Save screenshots to the repo assets folder.
- Parity: bench, page and script agree on the sample and on BRJ to the dollar (file from Job 3).
- Nothing is retired in this run (no file is replaced). If you find an older audit or vendor JSON format in the
  kit, say so in the report rather than moving it.
- Public repo: commit `tools/vendor-audit/index.html` only; do NOT push anything else public.

## Report
Built (paths), the parity file, screenshots, the sample report, Assumptions, Skipped, and "Questions for
David" at the end (start with the five in the design doc section 6 if the run did not settle them).
