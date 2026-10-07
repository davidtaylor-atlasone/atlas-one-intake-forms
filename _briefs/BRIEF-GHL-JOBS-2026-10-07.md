# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CX, 2026-10-07): Charity kit, vendor logins, Provo cleanup

Installed by A1 GHL Jobs 4 after the Run CW audit (PASS with one blocker, claude/ghl-jobs-run-CW-audit-2026-10-07.md).
Archive Run CW's report first. Files and code only, never the GHL UI. No questions mid run, no sends, no spending, no
deploys, no git push to main of atlas-one-intake-forms. No dashes in anything a client, prospect or BRJ reads. Log real
clock times. Finish with RUN-GHL-JOBS-report.md. RETIRE RULE: overwrite in place, list replaced files under "Retire".

## Job 1: Charity's kit, overwrite in place (David's written approval)
David's rule, CHAT-ROSTER 2026-10-03, in his words: "delete never park". That is his written yes to this change.
Edit `build_command.py` `build_rep_everything()` so `--person` overwrites the rep folder in place, never moves anything
into `_to_delete` or `superseded-*`, and prints each replaced file as a RETIRE line. Then remove the opt in `--move`
from `tools/agreements_inventory_2026-09-12.py` the same way.
FALLBACK if the edit is denied again: do not retry another way. Run `--person charity` with the existing code ONCE,
note the exact `_to_delete/superseded-<date>/` path it made under "Retire", and carry on. Cowork deletes that folder.
Either way: rebuild Charity's kit and `Charity Taylor.zip`, run `--check-zip`, grep proof of zero annual plan phrases
and zero pay lines in her folder and zip. Her stale pieces from Run CW: Price List PDF, both Prospect pitch decks (pptx
and pdf), Membership Brochure PDF, Membership Pricing PDF.

## Job 2: vendor login rows in COMMAND (internal only, hubs.py)
Replace "link needed" with these. Show the username beside each button. NEVER store or print a password anywhere.

| Row | Opens | Username |
|---|---|---|
| Cornerstone CRM (Dynamics 365) | https://underwriting.crm.dynamics.com | david.taylor@cornerstonepeo.com |
| G&A Partners Salesforce | https://login.salesforce.com/ | dtaylor@gnapartners.com |
| VeroHCM sales tool | https://salestool.verohcm.com/login | david@verohcm.com |
| GoHighLevel (keep) | https://app.ridethehightide.com | David@atlasonesolutions.com |

These rows live only in David's COMMAND. Strip them from every rep build and the shared Sales Kit; add a guard to
catalogue_check that fails if any of these hosts or usernames appears in a rep kit, the Sales Kit, client or BRJ
material. Microsoft Partner Center and QuickBooks Online Accountant stay "link needed".

## Job 3: Provo and Utah sample defaults (clients are national)
Independent Contractor Agreement Builder sample address, W-2 At-Will Agreement Builder "Provo, UT office" placeholder,
GHL Client Import Template.csv example row: use [City], [State], [ZIP]. Lehi stays only as the company address line.

## Job 4: decisions recorded (no work unless noted)
- Tools Cheat Sheet stays off COMMAND (archived 2026-10-03 on purpose).
- AI Email demo deck $499 a month and $750 setup are current (Professional tier, prices.json). No change.
- Dr Gould documents: owned by the A1 AGENT operator lane. Do not touch.

## Job 5: rebuild and prove
Rebuild COMMAND, Sales Kit and `--person charity`; all guards green; Chromium and WebKit at 1440 and 390, zero console
errors; click each of the four vendor buttons in Chromium (new tab, right host); grep proof that the vendor hosts and
usernames are absent from her zip and the Sales Kit. Report every file changed and the Retire list.
