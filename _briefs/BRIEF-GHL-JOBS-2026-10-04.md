# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CU, 2026-10-01): Charity's playbooks, vendor links, Run CT follow ups

Installed by A1 GHL Jobs 4 after auditing Run CT on disk (PASS: prices.json V10 locked; Technology and Connectivity
on the Software Marketplace Sheet; BRJ zip and website copy carry zero AppDirect, SYNNEX or myappdirect strings; 24
guards green). Archive Run CT's report first. Same rules as every GHL-JOBS run: files and code only, never the GHL UI,
no questions mid run, no sends, no spending, no deploys and NO git push to main of atlas-one-intake-forms (that
publishes the live site; David says "publish" himself), no dashes in anything a client, prospect or BRJ reads, retire
old versions to `Master_Kit/_to_delete/superseded-<date>/` using the real clock date, log real clock times, finish
with RUN-GHL-JOBS-report.md. Local commits on a branch are fine.

## Job 1: Charity's playbooks, vendor pay (David, 2026-10-01)
Vendors pay David only. Charity is not paid on any insurance or PEO deal; David does every insurance and PEO deal and
pays Charity only for other items (her rates are not set yet). In every rep build (`--person`, rep_scrub.py): remove
or reword every line in the playbooks, overlays, talk track and email templates that says vendors or carriers pay the
rep, or that implies the rep earns on insurance or PEO. Insurance and PEO questions go to "David Taylor, our licensed
agent" by name. Never print a commission rate or commission language for a rep. Overlay 06's referral fee mention
stays only in David's copy. Add the rule to rep_scrub tests and the catalogue_check rep guard.

## Job 2: Charity's booking link (only if it exists)
If people.json or the GHL lane's docs (`_BUILD-LOG/RUN-GHL-report.md`, `TERMINAL-GHL-live.md`) show a booking link for
Charity, put it in people.json (`booking`), rebuild her card on `cards-draft` (not pushed), her kit and her
announcement series, and remove the phone call fallback. If no link exists yet, skip and say so.

## Job 3: vendor ordering links (COMMAND Systems hub, internal only, never in a rep build)
Fill from what is on disk: `_INTERNAL (do not share)/Atlas_One_Vendor_Partner_Directory.xlsx`, the partner audit
xlsx, the AppDirect and TD SYNNEX notes in `_BUILD-LOG`. Known: GoHighLevel https://app.ridethehightide.com (login
David@AtlasOneSolutions.com); Microsoft Partner Center https://partner.microsoft.com/dashboard; QuickBooks Online
Accountant https://qbo.intuit.com. Cornerstone PEO gets its own login row. Any URL you cannot confirm on disk (likely
Cornerstone CRM, G&A, Vero) shows as "link needed" and is listed in the report.

## Job 4: Run CT follow ups (Cowork decided)
1. Software Marketplace Sheet and catalog: keep the "Browse the store" button pointing at the storefront, but never
   print the storefront URL as visible text (it contains a distributor name). Same on the BRJ copy; rebuild the BRJ
   zip with the real clock date and retire the old one.
2. Quote Cockpit: the year end W-2 label says "one extra payroll run at your rate, monthly minimum applies".
3. Embed DM Sans in the 17 generators package file under `05 Build Specs (for BRJ)` (offline rule).
4. "Lehi, Utah" stays only as the company address line; never in an example or a "local" claim.
5. Leave annual plan lines untouched (David has not decided).

## Job 5: rebuild and prove
Rebuild COMMAND, the shared Sales Kit and `--person charity` (re-zip her kit); all guards green; Chromium and WebKit
at 1440 and 390, zero console errors; grep proof that her kit has zero "commission", "paid by the carrier", "vendor
pays" style lines and zero David booking links. Report every file changed.
