# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CP, 2026-09-27). TD SYNNEX distribution vendors, the Thomas email, two contact@ leftovers, rebuild and prove.

Installed by chat A1 GHL Jobs 3 after its on disk audit of Run CO (`_BUILD-LOG/COWORK-AUDIT-run-CO-2026-09-27.md`, read
it first; it lists a defect Cowork fixed after Run CO). Run CO's brief is archived at
`_BUILD-LOG/BRIEF-GHL-JOBS-runCO-done-2026-09-27.md`. Queued after this run, one job each so they finish:
Run CQ digital business cards, Run CR safety quiz split and Spanish, Run CS COMMAND v2 (files
`BRIEF-GHL-JOBS-queued-runCQ.md`, `-runCR.md`, `-runCS.md`). Do not start them in this run.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI and never the portal
repo. No questions mid run. No sends, no spending, no new vendors. The intake forms repo main may be pushed. Deleting is
a move into `Master_Kit/_to_delete/superseded-2026-09-27/`. No dashes in anything a client, prospect or Thomas reads.
Log a line when each job STARTS and ends, using the real clock (`date`), never an estimated time. There is NO time
limit; this run is sized to finish, so do every job. Finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md` (archive Run CO's
report first). Keep every Run CL to CO guard on. Name this run "GHL-JOBS Run CP" everywhere.

## Job 1: TD SYNNEX Distribution tier (Job 8 of project doc claude/td-synnex-catalog-gap-2026-09-26.md)
Job 7 of that doc already shipped in Run CN (the 13 Cloud Marketplace Hold rows are Available, quote on request).
Its Nerdio line stays as Run CN left it, an internal MSP tooling row, not client facing: Nerdio Manager for MSP is
software an IT provider runs, and whether Atlas One sells managed Azure virtual desktops is an open question for
David. Now add the general distribution vendors, confirmed as orderable lines in Atlas One's TD SYNNEX account:
- Security: Check Point, SonicWall, Barracuda Networks, ESET, Ivanti, Absolute Software, ThreatLocker, Arctic Wolf
  (managed detection and response), Cynet, GoSecure, OPSWAT, Cofense, Ping Identity, Infoblox, Cato Networks (SASE),
  WinMagic (encryption), Utimaco.
- Backup and recovery: Veeam, Carbonite, N-able, NinjaOne, Altaro.
- IT and infrastructure software: Red Hat, SUSE, Progress Software, EnterpriseDB (Postgres), Paessler PRTG,
  Devolutions, Checkmk, Parallels, NVIDIA (AI and GPU licensing).
- Business apps and productivity: ServiceNow, DocuSign, TeamViewer, Corel, Foxit, JetBrains, Faronics.
- Print and document management: PrinterLogic.
- Communications: Five9, Avaya, AudioCodes, Oracle Communications.
- Training and HR adjacent: NINJIO (security awareness training), CurrentWare (employee monitoring and DLP),
  GoGuardian (education content filtering).
Rules: every one is Available, quote on request (the same bar as Pax8 and the Cloud Marketplace rows) until the A1
PARTNER TD SYNNEX lane says otherwise. Before adding a name, check the catalog for it (many may already be Pax8 rows,
e.g. N-able, NinjaOne, Veeam, Carbonite, ESET, SonicWall): if present, add TD SYNNEX as a second source on that row,
never a duplicate row. New group in the catalog: "TD SYNNEX Distribution" (internal label; the catalog xlsx and md are
internal and BRJ facing). One line of what each product does, in plain words, written from the vendor's own public
product description; no prices (distributor prices are cost and are never published). Logos only where the existing
logo pipeline already has them; otherwise a text tile. Do NOT add the Vendor Solutions directory names (AWS,
Cloudflare, RingCentral and the rest) or AnyCloud, Equinix, HPE, IBM, Meta, NexGen Technologies or Mirantis.
Update the same file set Run CL Job 6 and Run CN Job 7 touched: catalogue.py, the Software Marketplace Catalog v2 xlsx
(Website NOW, Marketplace (Available), ALL rows) and md, the Software Marketplace Sheet (A1_Sales copy and the BRJ
package copy, PDFs re-rendered, tiles grouped so the page stays readable: consider a compact "Also available" text
grid for this tier), both software one pagers only if a line needs to change, the website copy md, Charity's rep kit
copies on rebuild. Client facing wording always says "our marketplace partners", never TD SYNNEX or Pax8.

## Job 2: regenerate the Thomas email and the BRJ zip
Rewrite `A1_Sales/Website/Email_to_Thomas_BRJ_website_update_followup_2026-09-26.txt` as
`Email_to_Thomas_BRJ_website_update_followup_2026-09-27.txt` and retire the 09-26 version. David's voice (atlas-voice):
plain, warm, short sentences, NO dashes of any kind, no distributor names, no prices. Keep what is still true from the
09-26 text (folder 1 notes, contact@ is the only site email, Book a Call and the free audit confirmed, Industry
Starter Kits retired, Connecteam with the partner logos, "our marketplace partners", Browse the store button, quote on
request). Change: the Hold tab is now small (the Cloud Marketplace products moved to Available), and there is a new
group of well known names (list the headline ones: ServiceNow, DocuSign, Veeam, Red Hat, Check Point, TeamViewer and
the security set) that go on the page as a text list, quote on request. IMPORTANT: the website Book a Call button is
the 15 minute intro calendar and stays on the website only; say nothing that changes that. Rebuild
`A1_Sales/Website/Atlas One for BRJ 2026-09-26.zip` as `Atlas One for BRJ 2026-09-27.zip` with the corrected catalog,
sheet and website copy (retire the old zip). Do not send anything; David sends it.

## Job 3: two contact@ leftovers and the live site
- `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Prospect_Web_Pitch.html` and
  `A1_Sales/AI Services and Assistants/Atlas_One_Background_Screening_OnePager.html` still print support@ as the
  company line on prospect pieces. Swap to contact@ and find out why the guard missed them (probably not in the
  catalogue as prospect audience, or a capital S); fix the guard so it is case insensitive and scans every html in
  06 Calculators and A1_Sales, not only catalogued rows.
- The live site copies on forms.atlasonesolutions.com still say support@ (for example `/census/` and
  `/tools/what-we-do/`). Sync every public tool copy in the intake forms repo from its Master Kit source and push main.
- Add a guard that fails on any email address that is not exactly one of the approved Atlas One addresses
  (catches typos like the "sontact@" one below).

## Job 4: rebuild and prove (also Run CO's skipped Job 4)
Rebuild COMMAND, the shared Sales Kit and `--person charity`. Rerun the Run CL scanner over Charity's folder, decoded
blobs and PDF text; confirm zero support@ on her prospect pieces and her line one reads charity@. catalogue_check.py
clean except the documented Price List retail note. Headless 1440 and 390 on the Software Marketplace Sheet (both
copies) and one tool that got the contact@ swap; zero console errors; screenshots. Report the vendor row count before
and after, every new row, every second source added, and every file changed.

## Waiting on David, do not do
Sending the Thomas email. Nerdio or managed Azure virtual desktops as a service. The workers comp audit recovery
percentage (25% on the Price List, blank in prices.json). Handing Charity her kit (her mailbox does not exist yet).
