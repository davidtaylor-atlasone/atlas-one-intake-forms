# BRIEF for the GHL-JOBS terminal: Run AZ (software lines in Quick Quote, prices.json and the Total Impact model)

Written by the PARTNER STACK chat 2026-09-16, installed by the build chat after Run AY was audited. Run AY is done.

Terminal name: GHL-JOBS. Files and code only, no browser. Build the whole run end to end, answer every permission
prompt yourself, make the reasonable call and log it under Assumptions, and put every question in a
"Questions for David" section at the END of the report. Append to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md` after
every job. Write `_BUILD-LOG/RUN-GHL-JOBS-report.md` at the end (quoted heredoc or a file tool, never an unquoted
heredoc). Back up the prior report to `_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunAY.md`.
Commit and push the repo when done. No dashes in any text you write for David.

Master Kit path: find it by name, never hardcode a username:
`find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv`

## The pricing decision this run implements (decided 2026-09-15, do not re-ask)
Client prices for resold software are the vendor's published US prices. Microsoft 365 on an annual term: Business
Basic $7, Business Standard $14, Business Premium $22 per user per month. Microsoft 365 Copilot $21 per user per
month (annual). QuickBooks Online: Simple Start $38, Essentials $85, Plus $140, Advanced $340 per month.
Atlas One's cost is whatever the Pax8 Marketplace shows; the cost side is INTERNAL and never goes in a client file.

## Job 1: Quick Quote gets per product software lines
File: `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`. Back it up first to
`_to_delete/superseded-2026-09-16/Atlas_One_Quick_Quote_before_runAZ.html`.
1. In the `tech` division, directly after the existing `sw_marketplace` item, add these items. Follow the exact
   shape of the existing `qbo` item (model `flat_mo` with `editable:true`, rateLabel, and a qty control if the
   catalogue supports per user quantity; if it does not, add a `perUser:true` flag only if a similar flag already
   exists, otherwise use the existing quantity mechanism and say so in Assumptions):
   - id `m365_basic`, nm "Microsoft 365 Business Basic", ds "Business email, Microsoft Teams, web and mobile
     Office apps, 1 TB of cloud storage per person. Annual term, per user.", rate 7, rateLabel "$/user/mo".
   - id `m365_standard`, nm "Microsoft 365 Business Standard", ds "Everything in Basic plus desktop Office apps on
     five devices, webinars and bookings. Annual term, per user.", rate 14.
   - id `m365_premium`, nm "Microsoft 365 Business Premium", ds "Everything in Standard plus Defender for
     Business, Intune device management and data loss protection. Annual term, per user.", rate 22.
   - id `m365_copilot`, nm "Microsoft 365 Copilot (add on)", ds "AI assistant inside Word, Excel, Outlook and
     Teams. Requires a Business plan. Annual term, per user.", rate 21.
   - id `m365_other`, nm "Microsoft 365: other plans (Frontline, Enterprise, no Teams)", model `quoted`.
2. Change the `sw_marketplace` item's ds to: "Any other cloud product (backup, email security, password
   management, endpoint protection, electronic signature, phone) sourced through our marketplace partner: one
   invoice, one number to call." (removes the dash and the word "negotiated"). Keep model `quoted`.
3. Fix the `qbo` item in the `financial` division: choices become
   `[["38","Simple Start"],["85","Essentials"],["140","Plus"],["340","Advanced"]]`, default rate 85 (Essentials),
   ds "Set up and supported by Atlas One. Add QuickBooks Time or QuickBooks Payroll when needed." Drop the
   "50% off the first three months" promise (it is Intuit's promotion, not ours, and it changes). Drop Ledger and
   Solopreneur unless David has quoted them; log it.
4. Add a second quantity aware line for QuickBooks Time: id `qb_time`, div `tech`, nm "QuickBooks Time", model
   `quoted` (Intuit prices it per user plus a base fee and the numbers move; keep it quoted).
5. Keep every price editable in the UI as the rest of the catalogue is. Confirm the quote log and the search still
   work after the edit (open the file in Playwright headless, run a quote with two Microsoft lines and 12 users,
   read the total, screenshot to `_BUILD-LOG/runAZ-quickquote.png`).

## Job 2: prices.json software block gets real prices
File: `tools/agreements/prices.json` in the atlas-one-intake-forms repo (the copy under
`_INTERNAL (do not share)/tools/agreements/` is a mirror; update both if both exist). Replace the `software` block
with real client prices and remove the `_note` that says no price exists:
- `m365_business_basic` "$7 per user per month, annual term"
- `m365_business_standard` "$14 per user per month, annual term"
- `m365_business_premium` "$22 per user per month, annual term"
- `m365_copilot` "$21 per user per month, annual term, requires a Business plan"
- `quickbooks_online` "Simple Start $38, Essentials $85, Plus $140, Advanced $340 per month"
- `other_resold` "Quoted per product, confirmed on the client's invoice"
Also fix `bookkeeping.quickbooks_sub` to "Simple Start $38, Essentials $85, Plus $140 or Advanced $340 per month,
set up and supported by Atlas One". Then run `generate.py` so the Software and Licenses Schedule and its sample
proposal (fictional "Tell Me More LLC") regenerate into `A1_Sales/A1 Agreements/2026-09-15 masters/` and confirm
the prices print (docx read back, BaseFont check on the PDF: Horas and DM Sans only).

## Job 3: proposal generator and the Total Impact model show software
Files: `08 ROI Quote Master Template/Total_Impact_Model/total_impact_model.py`, `build_tim.py`, the prospect JSON
schema, and `PEO_Proposal_Generator_V4.5_MASTER/service_deck.py` (or whichever deck reads the quote lines).
1. The Technology & Operations division already carries a "Software stack consolidated" line (`software_stack`,
   "stack calc"). Add a second line in the same division: `software_resold`, label "Software supplied through
   Atlas One (Microsoft 365, QuickBooks Online)". It is a COST line (an Atlas One fee, printed as a negative like the
   membership fee, never a saving) unless the prospect JSON provides `current_software_spend`, in which case the
   line prints the difference (current spend minus the Atlas One resale total) and the memo says where the current
   number came from. Nothing is invented: with no verified current spend, the line prints the resale total as a
   cost and the memo "resale at vendor list price; savings come from the stack line above, not from this one".
2. Prospect JSON: add optional fields `m365_users`, `m365_plan` (basic, standard, premium), `m365_copilot_users`,
   `qbo_plan` (simple_start, essentials, plus, advanced), `current_software_spend`. Read prices from prices.json
   (Job 2) so there is one source of truth; never hardcode $7 / $14 / $22 in the model.
3. Run the model for `prospects/big_red_jelly.json` before and after; the before number must not change when the
   new fields are absent. Save both outputs to `_BUILD-LOG/runAZ-tim-before.txt` and `runAZ-tim-after.txt`.
4. Add the same line to the service proposal deck's quote table if the deck renders quote lines; render one deck
   to PNG with the fictional client and look at it (no clipped footnote below y=6.82 in).

## Job 4: Quote Cockpit
File: `08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`. If the Cockpit carries its own copy of the
service list rather than reading Quick Quote, add the same five Microsoft lines and the QuickBooks fix there, and
log that the two files now need keeping in step. If it reads Quick Quote, confirm the new lines appear and log it.

## Job 5: COMMAND rebuild and check
After the edits run `python3 "_INTERNAL (do not share)/catalogue_check.py" "<Master_Kit path>"` and
`python3 "_INTERNAL (do not share)/build_command.py" "<Master_Kit path>"`. Confirm the stamp in the tab title is
current.

## Report
Built, paths, screenshots, Assumptions, Skipped, Questions for David. Questions expected: whether Ledger and
Solopreneur stay in the QuickBooks picker; whether QuickBooks Time should carry a fixed price; whether the
Cockpit's older deck buttons should be retired now that software is in the quote.
