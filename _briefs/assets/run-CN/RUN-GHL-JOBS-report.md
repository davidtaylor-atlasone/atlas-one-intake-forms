# RUN-GHL-JOBS report: Run CN (2026-09-26)

Terminal: GHL-JOBS. Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` (copy at `_briefs/BRIEF-GHL-JOBS-2026-09-26.md` in the
intake forms repo). Order run: Job 0, Job 8, Job 2, Job 1, Job 3 (partial), Job 4, Job 7, Job 6. Job 5 (business
cards) was not started. Live log: `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`. The previous file at this path (Run
CL's report) is archived at `_to_delete/superseded-2026-09-26/RUN-GHL-JOBS-report-RunCL.md`.

## Job 0: finish Run CM Job 6 (Charity's folder). DONE

Root cause found and fixed, not just patched: `build_rep_footer_swapped_set` (generalized in Run CH) hard fails
the moment it reads a source piece with no `a1-footer-person` element. Five of the six Division Sheet source
files (Payroll & HR, Benefits & Retirement, Risk & Insurance, Technology & Operations, Business Consulting) never
got a Job 2 footer, only a plain `.foot` div with no `mailto`/`tel` links and no `a1-footer-person`/
`a1-footer-company` classes. That is why Charity's Division Sheets folder came back empty: the build died on the
very first piece, before writing anything. It was not a hung PDF render.

Fixed at the source:
- Wrapped each of the 5 division sheets' existing `.foot` block in proper `a1-footer-person` (David, mailto/tel/
  booking) and `a1-footer-company` (Atlas One Solutions, contact@, phone, site) spans, matching the one division
  sheet that already worked (Financial Services).
- The Bookkeeping Marketing Sheet V8 had two separate gaps: its footer line carried no classes at all, and it
  also has a masthead `.meta` block (David's name/title/phone/email) that lives outside the footer entirely.
  Added footer classes, and marked the masthead `class="meta a1-contact-person" data-a1-kind="meta-inline"` --
  the exact kind `build_command.py` already implements for this one file.
- The Price List's booking/call/email sentence and its `.foot` company line got the same class treatment.
- Folded in Job 3's people.json change here since I was already touching every footer: added
  `company.contact_email` and used contact@ (not support@) on all these prospect-facing pieces.

Ran the full `python3 build_command.py <Master_Kit> --person charity` end to end: Sales Kit, 6 Division Sheets,
5 One Pagers, 8 Sales Pieces, 1 Price List, all HTML+PDF, all clean. Job 2's default-person-leak guard passes
(zero david@/David Taylor/cornerstone). Charity's folder: 42 files, identical relative paths to the CH-9 backup.

## Job 8: kill the `/build/` flash, fix two broken live links. DONE, pushed

`intake-forms` repo, commit `8342efe`, pushed to `main`.

- Rewrote `build/index.html` as a tiny head-redirect page (meta refresh + immediate `location.replace`), the same
  shape as `/peo/` and `/bookkeeping/`: maps the 10 known `doc` slugs through to the GHL form
  (`hxPZ7HEhqG57aoS61MqM`), passes none for an unknown or blank slug. Retired the ~400KB inline-font holding page
  from the live path.
- Kept that old holding page as the internal COMMAND preview copy (`06 Calculators/
  Atlas_One_Build_This_For_Me.html`) with `GHL_BUILD_FORM` left empty and a comment explaining why, so its inline
  preview inside COMMAND does not also flash.
- Added a `GHL_BUILD_FORM_URL` constant to catalogue.py (single source of truth) and repointed the 5 `06
  Calculators` builders (Handbook, NDA, Safety Manual, W-2 At-Will, IC Agreement) plus the WSA booth demo copy of
  the handbook builder straight at the GHL form -- they already had `target="_blank"` and `?doc=<slug>`, they
  were just going through the `/build/` hop first. The `have-atlas-one-build-this-for-me` COMMAND/Sales Kit row's
  path now reads that same constant with no `?doc=` (it is the general row). Confirmed in `build_command.py` that
  every `http(s)` "Open" button already calls `window.open(href, "_blank", "noopener")`, so no separate "opens in
  a new tab" change was needed there.
- Fixed both broken live links: added `tools/handbook-basic/index.html` (the folder held 51 state PDFs and no
  index at all, so `/tools/handbook-basic/` 404'd -- built a 50-state-plus-DC picker page, zero console errors,
  scrollWidth matches viewport at 1440 and 390) and corrected `/what-we-do/` to `/tools/what-we-do/` in the
  self-referencing `og:image`/`og:url` meta tags on the live page itself, plus `catalogue.py`, `build_portal.py`
  and `Atlas_One_Everything_We_Handle.html`'s blurb text.
- Verified with headless Chromium: `build/?doc=handbook` and bare `build/` each do exactly one navigation
  straight to the GHL form, zero console errors.
- Did **not** touch `tools/onboarding/send/index.html`. It also paints content then redirects, but it is an
  intentional "here is what will be prefilled, redirecting now" confirmation page, not stale wrong content like
  `/build/` was, and Cowork's live-site sweep did not flag it. Flagging as observed, not changed.

## Job 2: the two new GL converter prices. DONE

Both David-approved lines added everywhere in lockstep:
- GL converter, Atlas One runs it and sends the files: $35 per payroll run.
- GL import plus certified payroll setup, bought together: one $300 setup covers both.

Touched: `prices.json` (new `gl_import.done_for_you`, `cert_payroll.bundle_setup_with_gl_import`), the Quick
Quote catalogue (new `gl_import_dfy` line, a bundle note on `cert_payroll_setup`), the Bookkeeping Marketing
Sheet V8 (both the A1_Sales copy and the `_INTERNAL/tools/bookkeeping-docs` copy, kept identical per the audit's
own rule; both PDFs re-rendered), the Price List (PDF re-rendered), and the Service Content Library (unpacked
`service-content-library-src-2026-09-26.tgz`, added a `gl_import_dfy` row to `lib/rows_financial.py` and
`qq.json`, ran `build.py` clean at 108 rows, copied the 5 outputs back, repacked the tgz, updated README.md).
Updated both queued notes (`BRIEF-PORTAL-queued-tool-pricing.md`, `BRIEF-GHL-queued-products.md`) so the lines
are no longer "unapproved there." Quote Cockpit checked: it carries no GL pricing at all, nothing to add.

## Job 1: the Run CM audit findings. MOSTLY DONE, one item carried forward

1. **Audit Workbench's stale embedded prices.json.** Re-embedded from the live file. Added two new
   `catalogue_check.py` guards: `check_price_placeholders` (fails on "price pending" or "[__]" anywhere on a
   client/prospect piece) and `check_embedded_prices_copies` (diffs every `var PRICES = {...}` a tool embeds
   against the live prices.json). Both pass clean today. Left a regeneration one-liner in a comment above the
   embed for next time.
2. **catalogue.py's COI Tracking Schedule blurb** ("Price pending David") rewritten with the real tiers.
3. **Price List wording drift** from prices.json fixed: handbook/safety manual updates now read "per update ...
   included Professional and above" instead of "/yr"; the safety training done for you rows now carry "waived
   Enterprise and above" / "larger quoted" / "included in Concierge"; the COI done for you row now says "a
   month" / "over 100 quoted" / "included in Concierge up to 25 subs". PDF re-rendered.
4. **Workers comp 25% vs prices.json's blank.** Untouched, per the brief. Still a question for David (below).
5. **Retired** `Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html` to `_to_delete/superseded-2026-09-26/`
   (checked catalogue.py first, not referenced).
6. **Connecteam naming.** No action needed, already ruled allowed by Cowork's own audit.

### Safety Training Program (brief's own Job 1 item 5)

Did the two mechanical pieces across all 25 files (24 month pages + the calendar):
- Stripped the `a1-footer-person` div entirely (and, once found, its now-dead CSS rule -- see Job 6 below) so
  every page carries the company line only, support@ (correctly *kept*, not switched to contact@, since these
  are client service handouts per the brief's own distinction).
- Fixed "Construction - Jobsite Safety Checklist" to "Construction Jobsite Safety Checklist" everywhere it is
  **printed** (6 HTML files, plus `safety-calendar.json`'s `checklist` field), without touching the real PDF
  filename on disk (`Construction - Jobsite Safety Checklist.pdf`), which legitimately keeps the hyphen -- that
  is just the file's own name in the Safety Checklists folder, not something this brief item is about.

**Not done, carried forward:**
- Splitting each month's quiz into a no-answer employee page and a separate supervisor answer key, and adding
  Spanish to the quiz questions/answers and the sign in sheet headings. `safety-calendar.json` needs `q_es`/`a_es`
  added to all 24 x 5 quiz items before the pages can be regenerated. This is real bilingual content authoring
  across 24 files, not a mechanical fix, and did not fit in this run.
- **Correction to the audit, not an action item:** searched the entire Master Kit for the 14 Construction
  toolbox talk PDF names outside `Safety Training Program/Construction/Toolbox Talks (reused from Safety
  Library)/` and found no other copy anywhere. This folder appears to be the *only* copy of that content, not a
  duplicate of some Safety Library original. Retiring it as the audit instructed would destroy the only copy, so
  it was left in place. Question for David below.

## Job 3: contact@ as the company line. SOURCE PLUMBING DONE, sweep not started

- `people.json`'s company block now carries `contact_email` alongside `support_email` (done as part of Job 0).
- Added `check_role_and_support_emails` to `catalogue_check.py`, covering all four rules in the brief at once:
  AR@/AP@/Info@/Sales@/Bookkeeping@ never on a client/prospect piece (one named exception for Bookkeeping@ on the
  QuickBooks Accountant Access Guide), support@ never on a prospect piece, contact@ never standing in for the
  `a1-footer-person` line.
- Ran it: **40 hits**, almost entirely "support@ on a prospect piece" across the `06 Calculators` tools and
  several `A1_Sales` one pagers and builders, plus 2 role-mailbox hits that need a look (info@/sales@ in the
  Email Assistant Setup Intake form, bookkeeping@ in the Bookkeeping Intake Form -- both need checking to tell
  whether they are a footer company line that must become contact@, or a legitimate operational routing address
  that should stay). Full list is in the live log's Job 3 entry.

Did not attempt the 40-file remediation in this run: each one needs the same care Job 0's footer fixes took
(confirm it really is the company line, not some other legitimate use of the address, before swapping), and there
was not room to do that carefully 40 times over. The guard itself is the real deliverable here -- it now names
the exact punch list for whoever picks this up next, instead of a vague "sweep everywhere."

## Job 4: queued notes for other lanes. DONE

- New: `BRIEF-GHL-queued-contact-routing.md` (GHL workflow: an inbound contact@ message about a rep owned
  prospect must notify that rep, default to David when the owner is not obvious).
- New: `BRIEF-EMAIL-queued-contact-routing.md` (email assistant: file a contact@ message under the right
  prospect and flag the owner).
- Added to `BRIEF-GHL-queued-products.md`: the COI notices' `custom_values` per-contractor field gap, and the GHL
  external tracking script note for the cards (once built).
- Did not touch `BRIEF-GHL.md` or `BRIEF-EMAIL.md`.

## Job 5: digital business cards. NOT STARTED

Everything in the brief's Job 5 (phone page, vCard with embedded logo photo, two QRs per card with decode
verification, lock screen image, show page, text-my-card copy, iPhone Contacts/NameDrop instructions, print PDFs,
Playwright tests, the QR plan document) was not attempted this run. There was not room left after Jobs 0, 1, 2, 3,
4, 6, 7 and 8. Carried whole to the next run. No branch was created; nothing under `A1_Sales/Business Cards/`
exists yet.

## Job 6: rebuild and prove. DONE

Rebuilt COMMAND, the shared Sales Kit and `--person charity` three times over, as Jobs 0/1/7 kept surfacing new
gaps in the footer machinery -- most notably the Safety Training calendar's catalogue.py entry falling through
`zone_of()`'s default "Sales Kit" zone (it needed an explicit `zone='Tools'` override, since it is a client
handout with no `a1-footer-person` by design), and then, even after that override, still hard failing because a
leftover `.a1-footer-person{...}` CSS rule (dead after Job 1 stripped the actual HTML element, but not the style
block that referenced it) still tripped the crude `"a1-footer-person" in raw` substring check that decides
whether to attempt a swap. Stripped the dead CSS from all 25 Safety Training files; the rebuild went clean after.

Final state:
- `catalogue_check.py`: clean except the one pre-existing, already-documented finding (the Price List carries
  retail numbers outside prices.json's narrow subset -- noted in the queued portal pricing note, out of scope
  for this run, not a regression).
- Charity's folder: 42 files, identical relative paths to the CH-9 backup.
- Decoded her Sales Kit's 51 base64-parked blobs directly (plain grep cannot see inside them): charity@ 14
  occurrences, david@ zero, support@ 12 (matches the known Job 3 gap exactly, not a new leak).
- Manually swept her whole folder for 385, scheduler.zoom.us and em/en dashes: zero hits on all three.
- Her Price List correctly shows "Charity Taylor, Business Advisor" with no email on the person line (that piece
  is `public=True` by design, no address shown -- a pre-existing Run CG rule, not a defect) and contact@ on the
  company line.
- Headless Chromium at 1440 and 390 on the Price List, Quick Quote, the safety calendar and the January General
  Industry month page: zero console errors, `scrollWidth` equals the viewport on all four at both widths.
  Screenshots: `_briefs/assets/run-CN-jobs/shots/` in the intake forms repo (also `job8-handbook-basic-*.png`
  there from Job 8).
- Did not build or screenshot a card page (Job 5 not attempted).

## Job 7: TD SYNNEX catalog undercount. DONE (run before Job 6, as instructed)

Could not find `claude/td-synnex-catalog-gap-2026-09-26.md` anywhere on disk -- not in the Master Kit, not in any
local project under `~/Projects`. It is likely a claude.ai project document from a different chat, not reachable
from this terminal. Proceeded from the brief's own explicit instructions instead.

Reclassified all 13 TD SYNNEX Cloud Marketplace rows that were on Hold purely on a channel technicality (Google
Workspace, Adobe, Dropbox Business, Cisco Duo and Cisco security, Fortinet, Palo Alto Networks, Trend Micro,
Symantec, CyFlare, CyberArk, DigiCert / Entrust, StorageCraft, Autodesk) to Available, quote on request:
- Catalog `.md`: counts now Signed 45 / Available 83 / Pending 3 / Hold 15 / Internal 12 (was 70/28).
- Catalog `.xlsx`: moved the 13 rows from the Hold sheet to the Marketplace (Available) sheet, updated the ALL
  rows sheet, rewrote both sheets' header notes.
- Software Marketplace Sheet HTML, both the A1_Sales copy and the BRJ package copy: all 13 vendor tiles upgraded
  from the dimmer "Ask us / line" style to "Available / tint". Both PDFs re-rendered, zero console errors.
- catalogue.py's stale row-count blurb (still said 141 rows from before even Run CL's TD SYNNEX addition).

Nerdio: confirmed it already sits correctly as an "Internal only, MSP tooling" row, not client or website facing
-- no catalog change needed, just a question for David (below). Confirmed AnyCloud, Equinix, HPE, IBM, Meta,
NexGen Technologies and Mirantis are absent everywhere already; nothing to undo.

Regenerated the BRJ zip (`Atlas One for BRJ 2026-09-26.zip`) with the corrected catalog files inside; the old zip
moved to `_to_delete/superseded-2026-09-26/`. Read `Email_to_Thomas_BRJ_website_update_followup_2026-09-26.txt`:
its Hold-tab instructions ("ask us list, no logos") are still accurate regardless of the count, so it was not
regenerated -- no factual error was found in it to fix.

## Assumptions

1. Used the OneDrive copy of the Master Kit found via the standard `find` command; A1_Sales confirmed as a
   sibling of `HR_Docs` under `2. Atlas 1 Solutions Marketing`, per the project's own CLAUDE.md.
2. Job 0's footer fixes used contact@ (not support@) on all 6 division sheets, the Bookkeeping Marketing Sheet
   V8 and the Price List, since these are prospect pieces under the Job 3 standard, even though Job 3 itself was
   only partly done this run -- doing the two together where they overlapped avoided a second pass on the same
   footers later.
3. The Bookkeeping Marketing Sheet V8's masthead `.meta` block used the `meta-inline` `a1-contact-person` kind
   `build_command.py` already implements by name for this exact file, rather than inventing a new kind.
4. Safety Training Program footers keep support@ (not contact@), per the brief's own explicit instruction that
   these are client service handouts, distinct from the prospect pieces Job 0/Job 3 touch.
5. The Safety Training calendar catalogue.py entry got an explicit `zone='Tools'` override rather than being
   added to `TOOL_KINDS` or `SALESKIT_ONLY_DIVISIONS`, since those are broader switches that would have changed
   behavior for many other unrelated entries; the per-entry override touches only this one file.
6. Did not rename the real "Construction - Jobsite Safety Checklist.pdf" file on disk; the brief's "print
   checklist names without the spaced hyphen" instruction was read as being about how the name is printed in the
   month pages and JSON, not the actual PDF filename in the Safety Checklists folder.
7. Regenerated the BRJ zip and moved the old one to `_to_delete/`, judging this a "move superseded content"
   action already authorized by the standing "never delete, move to `_to_delete`" rule, not a new distinct
   action needing separate sign off.
8. Left `tools/onboarding/send/index.html` untouched (Job 8's flash rule, read literally, would also catch it),
   since on inspection it is an intentional confirmation page design, not the bug Job 8 was written to fix, and
   Cowork's own live-site sweep did not flag it.

## Skipped

- Job 5 (digital business cards): not started, whole job carried to the next run.
- Job 1's Safety Training Program bilingual quiz/answer-key split: not started, carried to the next run.
- Job 3's 40-file support@/role-email sweep: guard built and run, remediation not started, carried to the next
  run with the guard's own output as the punch list.
- The Toolbox Talks (reused from Safety Library) folder was not retired -- see the question below.

## Questions for David

1. **Workers comp audit recovery percentage.** The Price List says 25% of the premium recovered; prices.json
   says blank. Carried forward from Run CM/CL. Which is the approved number?
2. **Nerdio / managed Azure Virtual Desktop.** The TD SYNNEX catalog correctly lists Nerdio as internal-only MSP
   tooling, not a client-facing product. Does David want Atlas One to offer managed Azure Virtual Desktop as a
   new service (which would make Nerdio a real product line), or does it stay purely internal tooling for if
   Atlas One ever runs IT support in house?
3. **The Toolbox Talks (reused from Safety Library) folder.** The Run CM audit said this folder duplicates
   content that should instead be a relative-path pointer to a Safety Library original. A full search of the
   entire Master Kit found no other copy of any of the 14 talk PDFs anywhere else. Either the audit's premise is
   wrong, or the true original toolbox talks live somewhere this search did not think to look (a different name,
   a different top-level folder, or content that has since moved). Left the folder in place rather than guess
   and risk deleting the only copy. Where should these 14 talks actually live, if not here?
4. **AnyCloud, Equinix, HPE, IBM, Meta, NexGen Technologies, Mirantis.** Confirmed absent from every catalog copy,
   per the brief. They wait on the TD SYNNEX portal login (A1 PARTNER TD SYNNEX lane).
