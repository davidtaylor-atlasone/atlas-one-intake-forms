# RUN-GHL-JOBS-report, Run CX, 2026-10-07

## Built
| Job | Status |
|---|---|
| 1 Charity's kit, overwrite in place | DONE. `build_rep_everything()` already overwrote in place and printed RETIRE lines (no `_to_delete`, no `superseded-*`). The opt in `--move` is removed from `_INTERNAL (do not share)/tools/agreements_inventory_2026-09-12.py`; it is now always a dry run and prints duplicates as RETIRE lines. `--person charity` run once, `Charity Taylor.zip` rebuilt in place (77 entries, 68 files), `--check-zip` clean. |
| 2 Vendor login rows | DONE in `hubs.py` VENDOR_ROWS: Cornerstone CRM (Dynamics 365), G&A Partners Salesforce, VeroHCM sales tool, GoHighLevel, each with the username shown in the row text beside the Open button. No password stored or printed anywhere. New guard `_c_vendor_logins` in `catalogue_check.py` (26 of 26 checks green). |
| 3 Provo and Utah samples | DONE. IC Agreement Builder sample address, W-2 At-Will Builder placeholder, GHL Client Import Template example row all use [City], [State], [ZIP]. |
| 4 Decisions | Recorded, no work. Tools Cheat Sheet off COMMAND, AI Email demo deck prices current, Dr Gould files untouched. |
| 5 Rebuild and prove | DONE. COMMAND (stamp "Oct 7, 2026 1:37 PM", 216 items), Sales Kit (62 items), Charity kit and zip. |

## Paths
- `Atlas_One_Master_Kit/Atlas One COMMAND.html`, `A1_Sales/Atlas One Sales Kit.html`
- `A1_Sales/_Rep Kits/Charity Taylor/` and `Charity Taylor.zip`
- `_INTERNAL (do not share)/hubs.py`, `catalogue_check.py`, `tools/agreements_inventory_2026-09-12.py`
- `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Agreement Builder (Atlas One).html`, `W-2 At-Will Employment Agreement Builder (Atlas One).html`
- `12 GHL Setup doccs/Atlas_One_GHL_Client_Import_Template.csv`
- Evidence: `_briefs/assets/run-CX/` (grep-proof.txt, render-results.json, shots/)

## Looked at
- Chromium and WebKit, 1440 and 390, COMMAND and Sales Kit: scrollWidth equals viewport in all 8 loads, zero console errors, zero non file requests (`render-results.json`).
- Clicked all four vendor buttons in Chromium; each opened a new tab on the right host (Cornerstone redirects to Microsoft sign in, as expected). Screenshot `shots/vendor-rows.png` shows usernames beside the buttons.
- Grep proof (`grep-proof.txt`): Charity folder and zip, 68 files each, 0 annual plan phrases, 0 pay lines, 0 vendor hosts or usernames. Sales Kit: 0 vendor hosts or usernames, 0 annual plan hits.

## Retire (files replaced in place; the auditing chat deletes nothing here, these are overwritten copies)
No file was moved or parked. `--person charity` rewrote files in `A1_Sales/_Rep Kits/Charity Taylor/`, including the stale pieces named in the brief: Price List PDF, both Prospect pitch decks (pptx and pdf), Membership Brochure PDF, Membership Pricing PDF. The build also printed RETIRE lines for the Client Presentations (Launch Companion docx and pdf, Launch Deck pdf and pptx), the Division Sheet PDFs, One Pager PDFs, Service Decks (pptx and pdf), Sales Pieces PDFs and the Bookkeeping Cadence email html. The terminal scrollback only kept the last part of that list, so treat every file under her folder dated 2026-10-07 as replaced. `Charity Taylor.zip` replaced in place. Nothing in `_to_delete`.

## Assumptions
1. `build_rep_everything()` already had the overwrite in place code when this run started (mtime Oct 7 13:30), so Job 1 code work was only the agreements script. I ran `--person charity` once with that code.
2. Usernames show in the row text (the "why" line) because COMMAND renders no separate username field. GoHighLevel's username is shown as David@atlasonesolutions.com (lowercase domain per brand).
3. Microsoft Partner Center and QuickBooks Online Accountant rows were not changed; they never said "link needed" and already carry confirmed links.
4. Guard scope: hosts must be absent from all of A1_Sales (including zips), the BRJ kit and the prospect Tools file. Partner usernames are checked only in rep kits, Sales Kit, BRJ and Website material, the Big Red Jelly handoff and Client Portal, because david.taylor@cornerstonepeo.com is also David's own contact line on his personal sales pieces (Industry Playbooks, Benefits Menu, Email Drafts). The GHL username is David's public email and is covered by its host only.
5. Import template phone 801 (a Utah area code) changed to 555-555-0111 beside the [City], [State], [ZIP] change.
6. Repo commit is local on the current branch only; the brief says no push to main.
7. Run CY brief (`BRJ queued`) was not started, as instructed ("install after the Run CX audit").

## Skipped
Nothing skipped.

## Questions for David
1. Both agreement builders still print "governed by the laws of the State of Utah" in the Governing Law clause. Clients are in all 50 states. Should that become a state picker driven by the client's state? I did not change it, it is a legal term.
2. The Dr Gould Proposal_Generator (operator lane, untouched) contains the three partner usernames. Fine for the operator lane, or should the A1 AGENT lane be told?
