# BRIEF-GHL-JOBS (current run: Run CF, 2026-09-22). Finish the footer rollout Run CE left, wire the rep kit swap, David's name on the public pages.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run. No sends, no deploy, no spending. Deleting is a move into `_to_delete/superseded-2026-09-22/`. No
dashes in anything a client or prospect reads. Log to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with
`_BUILD-LOG/RUN-GHL-JOBS-report.md`. Screenshots to `_briefs/assets/run-CF-jobs/` in the intake forms repo.

**THERE IS NO TIME LIMIT ON THIS RUN.** Run CE stopped after ten minutes and reported Job 2 as "too large for
the time remaining". Nothing set a time limit. Work every piece on the list below to the end. Commit after
each numbered step so a run that is interrupted by something outside your control still lands what it
finished. Stopping early for time is not an acceptable outcome in this run.

Written by Cowork (chat A1 GHL Jobs) after auditing Run CE on disk. Decisions are David's, do not re ask them.

## What Run CE left, checked by Cowork on disk (not from the report)

Done and verified: `INTERNAL/people.json` (david, charity), `INTERNAL/people.py` (`load_people`,
`load_contact`, `footer_html`), `contact.json` retired, `INTERNAL_PASSPHRASE = None`, the Sending as picker
in COMMAND hooked into Preview and Present, `build_command.py --person`, `swap_footer_person()` written.

NOT done, and it matters: Charity's kit at `A1_Sales/_Rep Kits/Charity Taylor/` was decoded blob by blob.
It carries `david@atlasonesolutions.com` 102 times and Charity's name zero times inside the inlined pages.
Only the hero line changed. It must not reach her until this run is done (the READ ME FIRST says so).

## Rules for this run that Run CE did not have

1. **Stale sources.** `_BUILD-LOG/prospecting-kit-src-2026-09-08.tgz` still carries the RETIRED number
   385-213-7177 nine times and none of the current 380 number. The industry overlays were phone swept in
   their HTML on 2026-09-14/15, after that snapshot. Regenerating from the tgz would put David's retired cell
   number back on client pages. So for every piece: if a generator exists, run it into a scratch folder,
   diff its output against the current HTML, and use the generator ONLY if the only differences are the
   footer you are adding. Any other difference means the current HTML is the source of record: edit the HTML
   in place with a script (never retype it), and log which pieces went which way.
2. **The Employee Benefits Menu has no source on disk.** Cowork searched: `build_benefits.py` and
   `benefits_body.html` are in no tgz, no folder on OneDrive and no repo (they were built in a cloud session
   on 2026-09-14 and never saved). The HTML in `A1_Sales/Atlas 1 Benefits/` is now the source of record. Edit
   it in place; regenerate its PDF with the same Playwright print recipe Run CE used for Everything We Handle.
   Note the finding in the report so nobody searches for it again.
3. Every edited HTML gets a grep afterwards for `385-213-7177` and for dashes in visible text. Zero of each.

## Step 1: the footer on every piece in the list

Same list as Run CE Job 2 (repeated so you do not need the old brief). Every piece gets the `a1-footer`
block from `footer_html()` with the default person (David), replacing its current contact block:
- Six division sheets (`INTERNAL/tools/division_sheets_build_2026-09-12.py`, apply rule 1), HTML and PDF.
- Industry overlays 01 to 06 (HTML is the source, rule 1). The Cornerstone brand toggle must keep working:
  in Cornerstone mode the footer is the Cornerstone block the page carries today, untouched.
- `A1 What we do Overview/`: Services Overview, Partner Client Program PPG.
- `AI Services and Assistants/`: AI Task Agent, AI Email Assistant, Background Screening one pagers.
- `Proof & Case Studies/Atlas_One_Proof_Sheet.html`.
- `Atals 1 Membership Pricing/`: Membership Pricing, Membership Brochure.
- `Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html` (rule 2).
- `Total Impact Model/Atlas_One_Total_Impact_Model.html` through
  `08 ROI Quote Master Template/Total_Impact_Model/build_tim.py` (rule 1).
- `Atlas 1 Bookkeeping/`: Bookkeeping Marketing Sheet V8, QuickBooks Accountant Access Guide.
- `Client Portal/`: Atlas One Client Portal, Client Dashboard GHL.
- `Pricing/Atlas_One_Price_List.html` only if its catalogue audience is prospect or client.
- `Atlas 1 Software and Licenses/`: Software and Licenses one pager and Microsoft 365 one pager, person line
  back to David, through `software-licenses-src-2026-09-16.tgz` (it carries the 380 number, so it is likely
  current; still apply rule 1).
- Every PDF of the above regenerated from its HTML or generator.
Leave alone exactly what Run CE left alone (marketplace sheets, email assistant help page, Dr Gould folder,
Email Templates, Thomas emails, BRJ pricing SPEC, Blog Set, WSA Partnership Plus folder, internal playbooks).

Generators to wire to `people.py` instead of a literal, where they exist: `build_tim.py`,
`build_audit_report.py`, `08 ROI Quote Master Template/PEO_Proposal_Generator_V4.5_MASTER/service_deck.py`
(one line company contact on slides), the agreement and packet generators, the cadence email wrapper.

## Step 2: David's name on the public pages (decided by David 2026-09-22)

Add `public=True` to `footer_html()`: it prints the person line WITHOUT an email address, as
"David Taylor, Founder · 380-CALL-A1S (380-225-5217) as a tel link · Book 15 minutes with David" linking to
https://api.leadconnectorhq.com/widget/groups/book-david, and the normal company line with support@ under it.
Reason: public pages get scraped for email addresses, and the booking link is the action that converts.
Apply it to every public page in the repo: what we do (replacing the company only footer Run CE put there),
census, self assessment, time savings, vendor audit, retention cost, and any other page under `tools/` that
carries a contact block. Give the Master Kit copy of Everything We Handle the same footer so it matches its
repo twin, regenerate `A1_Sales/Atlas_One_Everything_We_Handle.pdf`. Commit and push the repo.

## Step 3: wire the rep kit swap and rebuild Charity's kit

Wire `swap_footer_person()` into the blob inlining for rep kit builds only. A blob whose source is on the
Step 1 list and lacks `a1-footer-person` is a hard failure naming the file. A blob that is a tool or a
calculator with no contact block at all is skipped and listed (tools are not sales pieces). Public pages
built with `public=True` get Charity's line without an email the same way.
Also produce her own copies of the one pagers and division sheets (HTML and PDF) in her folder, as Run CE's
brief asked.
Strip the Sending as `<select>` from the markup entirely on non COMMAND builds (Run CE left it hidden but
present; a rep file should not carry it).
Rebuild `--person charity`. Then prove it by DECODING every inlined blob (they are base64): count
`david@atlasonesolutions` (must be 0 outside any page that is company only), count `Charity Taylor` (must be
one per sales piece), and the six forbidden terms plus margin outside CSS (0). Put the counts in the report.

## Step 4: rebuild and verify, all three widths

`catalogue_check.py`, rebuild COMMAND and the Sales Kit, then Charity's kit. Headless Chromium at 1440, 1024
and 390: every COMMAND zone scrolls to its last row; all eight Present playlists run end to end; the two line
footer renders on ten sampled pieces (two division sheets, one overlay in each brand mode, both software one
pagers, the benefits menu, the proof sheet, one public page); the Sending as picker swaps the person line to
Charity and back in Preview and in Present with the company line identical in every screenshot; the Internal
tab opens with no gate and the Approval Queue, Activity log and Tasks and Follow ups each open in one click.
Deploy nothing.

## Not in this run

LTD row on the benefits menu (waiting on David's broker). Charity's GoHighLevel signature merge fields and
reply to (GHL terminal). The census v3 columns: queued as Run CG in `BRIEF-GHL-JOBS-queued-census-v3.md`.

## Report must include

Per piece: generator used or HTML edited (and why, from the rule 1 diff); before and after contact; 385 and
dash grep results. The decoded blob counts for Charity's kit. Screenshot list. Questions batched at the end.
