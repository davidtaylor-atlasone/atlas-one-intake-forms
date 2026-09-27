# Run CP (GHL-JOBS), 2026-09-27

All four jobs in BRIEF-GHL-JOBS.md complete: TD SYNNEX Distribution, the Thomas email and BRJ zip, the two
contact@ leftovers plus a rewritten guard and live site sync, and rebuild and prove. Files and code only;
never opened the GoHighLevel browser UI or the portal repo.

## Job 1: TD SYNNEX Distribution tier

Extracted the software catalog's generator source from `_BUILD-LOG/software-catalog-src-2026-09-26.tgz`
(`catalog/data.py`, `catalog/build_catalog.py`), added the 34 vendors the brief named as a new
`TD SYNNEX Distribution` catalogue group, then repacked the tarball with the edits in place.

- 21 vendors had no existing row and got one: SonicWall, ESET, Ivanti, Arctic Wolf, GoSecure, OPSWAT, Cofense,
  Ping Identity, Infoblox, WinMagic, Utimaco, Altaro, Red Hat, SUSE, Progress Software, EnterpriseDB, Paessler
  PRTG, Devolutions, Checkmk, Parallels, NVIDIA, ServiceNow, TeamViewer, Corel, JetBrains, Faronics,
  PrinterLogic, Avaya, AudioCodes, Oracle Communications, NINJIO, CurrentWare, GoGuardian.
- 13 vendors already had a Pax8 or TD SYNNEX Cloud Marketplace row and got a second source note added to
  that row instead of a duplicate: Check Point, Barracuda, Absolute Software, ThreatLocker, Cynet, Cato
  Networks, Veeam, Carbonite, N-able, NinjaOne (via the Dropsuite row), DocuSign, Foxit, Five9.
- Did not add the Vendor Solutions directory names or AnyCloud, Equinix, HPE, IBM, Meta, NexGen Technologies
  or Mirantis, as instructed.

Rendered the new tier on the Software Marketplace Sheet as a compact "Also available through our marketplace
partners" text table (not full tiles, per the brief's own readability note), grouped by category. Found and
fixed a mobile layout bug before shipping: the new table overflowed to 518px against a 390px viewport; added a
stacked mobile layout, re-rendered, scrollWidth now matches viewport on both breakpoints. Also fixed the
sheet's CTA band mailto, which still said support@, to contact@, as part of the same rebuild.

Files updated: `catalog/data.py`, `catalog/build_catalog.py` (both repacked into the tgz), and the built
outputs copied into both live copies: `A1_Sales/Website/BRJ Software Marketplace Package 2026-09-26/`
(Catalog v2 xlsx, md, Sheet HTML+PDF) and `A1_Sales/Atlas 1 Software and Licenses/` (Sheet HTML+PDF).
`catalogue.py`'s two blurbs for these rows updated with the real count and the change history.

**Correcting a pre-existing count.** The actual build has always produced 28 Hold rows (13 in TD SYNNEX Cloud
Marketplace plus 15 confirmed-not-on-Pax8), not the 15 that catalogue.py's blurb claimed after Run CN. That
blurb was already wrong before this run; not something this job broke, but corrected here since it was
touched anyway. Real count after this job: 191 rows (was 158): Signed 45, Available 103 (was 83), Pending 3,
Hold 28 (was mislabeled 15), Internal 12.

The website copy md and both software one pagers name no individual vendors, so nothing to change there.
`catalogue_check.py` clean except the one pre-existing documented Price List finding.

## Job 2: the Thomas email and the BRJ zip

Wrote `A1_Sales/Website/Email_to_Thomas_BRJ_website_update_followup_2026-09-27.txt`, keeping what was still
true from the 09-26 version (folder 1 notes, contact@ is the only site email, Book a Call and the free audit
confirmed, Industry Starter Kits retired, Connecteam with partner logos, "our marketplace partners", Browse
the store button, quote on request), and changing the Hold tab line to say it is small now, plus a new
sentence naming the headline TD SYNNEX Distribution names (ServiceNow, DocuSign, Veeam, Red Hat, Check Point,
TeamViewer and the security set) as a plain text list, quote on request. No dashes, no distributor names, no
prices. Retired the 09-26 txt to `_to_delete/superseded-2026-09-27/`.

Rebuilt `Atlas One for BRJ 2026-09-27.zip` from the 09-26 zip: unzipped, swapped in the fresh Software
Marketplace Sheet PDF, Catalog v2 xlsx and md from Job 1, added the new Thomas email txt, rezipped. Retired
the 09-26 zip to `_to_delete/superseded-2026-09-27/`. Neither file is referenced by name in catalogue.py, so
no path edit was needed there.

Did not send anything; David sends it.

## Job 3: the two contact@ leftovers, the guard, and the live site sync

**Root cause, both files.** `check_role_and_support_emails` in `catalogue_check.py` only ever scans catalogue
entries with `inline=True` and `audience in (client, prospect)`. `Atlas_One_Prospect_Web_Pitch.html` is
`audience='prospect'` but `inline=False` (a linked live page, never inlined into COMMAND);
`Atlas_One_Background_Screening_OnePager.html` is `audience='internal'` despite being a genuine client-facing
sell sheet. Both fell straight through the filter. Not a case bug in the strict sense (the guard already
lowercases before comparing) but both files did carry `Support@` (capital S) in three of their six
occurrences.

Fixed both files: `support@`/`Support@` to `contact@`/`Contact@`, case preserved, 6 occurrences total,
verified character by character afterward (no `sontact@`, no leftover `support@`).

**New guard.** Added `check_html_email_addresses(mkt)` to `catalogue_check.py`: walks every `.html` file on
disk under `06 Calculators and Tools (NEW Aug 2026)/` and `A1_Sales/`, with no catalogue filter of any kind,
and fails on any `*@atlasonesolutions.com` address whose local part is not exactly one of the five addresses
confirmed legitimate by scanning every html file in both trees (`david`, `contact`, `support`, `charity`,
`bookkeeping`). This is the guard that would have caught Run CO's `sontact@` typo, since a substring check for
the correct spelling can never catch a misspelling.

**Self-inflicted bug found and fixed during verification.** The first version of this guard used one greedy
`[A-Za-z0-9._%+-]+@atlasonesolutions\.com` regex over the whole file. On the two 27&nbsp;MB rep kit Sales Kit
files (base64 blobs are one giant run of characters that mostly overlap the local-part character class, with
few or no `@` signs in them), that pattern backtracks character by character at every starting position: an
O(n²) hang. It ran over 5 CPU minutes at 100% with no result before being killed by hand. Rewrote it to find
the literal `@atlasonesolutions.com` domain first (fast, non-backtracking), then check only the 64 characters
immediately before each match for a local part. Re-ran: 0.1 seconds. That run surfaced one real thing to
look at, not a defect: `Atlas_One_Compliance_Calendar.html`'s `.ics` export builds a per-event calendar UID in
JavaScript (`'a1cal-'+ds+'-'+i+'@atlasonesolutions.com'`), where the character immediately before `@` is a
quote mark, not a real local part. Added a rule skipping any match with no local-part character directly
against the `@`, since that can only be JS-constructed text, never something a person could actually be
mailed at.

Final state: `check_html_email_addresses` 0 hits, `check_role_and_support_emails` 0 hits, full
`catalogue_check.py` clean except the one pre-existing documented Price List finding.

**Live site sync.** Grepped the whole intake-forms repo for `support@atlasonesolutions`: two hits,
`census/index.html` and `tools/what-we-do/index.html`, exactly the two the brief named as examples. Their
Master Kit sources (`Atlas_One_Everything_We_Handle.html`, `Health Quote Census Intake (Atlas One).html`) were
already current; the repo copies were several runs stale (still said "Book a call with David", "Email to
David", a dash in the census title, and a leftover support@ contact block the master no longer has). Copied
both master files over the repo copies wholesale. Repo-wide grep for `support@atlasonesolutions` now returns
zero. Committed and pushed to `main`: **e40286f**, `Run CP Job 3: sync census and what-we-do from Master Kit,
fix contact@ leftovers`.

## Job 4: rebuild and prove

Rebuilt COMMAND (206 items, 57.7&nbsp;MB) and the shared Sales Kit (59 items, 27.0&nbsp;MB), both clean.
Rebuilt `--person charity` end to end (Sales Kit, 6 Division Sheets, 5 One Pagers, 8 Sales Pieces, 1 Price
List, all HTML+PDF pairs); the build's own default-person-leak guard passed clean.

Deep-verified Charity's whole 42-file folder the way Run CL/CN did it: decoded every base64 blob in every
non-PDF file and read every PDF's extracted text (20 PDFs, via pypdf) for `david@atlasonesolutions.com`,
`scheduler.zoom.us`, the retired 385-213-7177 number, `cornerstone`, and em/en dashes. Zero hits on every
axis, across every file, blob, and PDF. `charity@atlasonesolutions.com` appears 40 times in plain text (more
inside blobs). Her Price List correctly reads "Charity Taylor, Business Advisor" with no personal email line
(that piece is `public=True`, a pre-existing Run CG rule, not a defect) and `contact@` on the company line.

Full `catalogue_check.py`: clean except the one pre-existing documented Price List finding.

Headless Chromium (Playwright) at 1440px and 390px: the Software Marketplace Sheet (both the A1_Sales and
BRJ package copies) and the fixed `Atlas_One_Prospect_Web_Pitch.html`. Zero console errors, zero non-`file://`
requests, `scrollWidth` equals viewport at both widths on every file. Screenshots in the intake-forms repo at
`_briefs/assets/run-CP/shots/` (6 files).

## Assumptions

1. Where the brief's TD SYNNEX Distribution vendor list overlapped an existing Pax8 or TD SYNNEX Cloud
   Marketplace row (13 vendors), added a second-source note to the existing row rather than a duplicate,
   per the brief's own instruction; picked the most relevant existing row where a vendor had more than one
   (e.g. NinjaOne's backup product, Dropsuite (NinjaOne), rather than the internal MSP-tooling list entry).
2. Wrote one-line product descriptions for the 21 net-new TD SYNNEX Distribution rows from each vendor's own
   public product description, in plain words, with no prices (matching the brief's own rule that distributor
   prices are cost and never published).
3. Rendered the new distribution tier as a compact "also available" text table rather than full tiles, per
   the brief's explicit suggestion to keep the page readable at 33 new rows.
4. Corrected catalogue.py's stale "Hold 15" count to the real, always-been-true "Hold 28" while touching that
   blurb anyway, rather than leaving a known-wrong number next to a freshly updated one.
5. Categorized the net-new vendors using the existing taxonomy where it fit (Security, Backup and recovery)
   and added new categories only where none of the existing ones fit (IT and infrastructure, Business apps,
   Print and document management, Communications, HR and training), matching the brief's own subheadings.
6. Treated the Compliance Calendar's `.ics` UID string as a false positive for the new email guard (JS-built
   text, never a mailbox) rather than editing the calendar generator code, since the string is correct and
   intentional as written.

## Waiting on David, not done, per the brief

- Sending the Thomas email (David sends it).
- Nerdio or managed Azure virtual desktops as a service.
- The workers comp audit recovery percentage (25% on the Price List, blank in prices.json).
- Handing Charity her kit (her mailbox does not exist yet).

## Questions for David

1. None of this run's own work raised a new open question; the four items above are carried forward exactly
   as the brief listed them, still waiting on you.
