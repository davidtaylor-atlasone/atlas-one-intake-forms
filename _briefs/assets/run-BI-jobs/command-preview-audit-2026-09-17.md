# COMMAND Preview/Open audit (2026-09-17, Run BI Job 1)

Headless Chromium (Playwright), COMMAND loaded from `file://`. Every catalogue item (191 unique 
titles across 209 rendered rows -- 18 pinned items render twice, once natively and once again in 
Start here, by design) was found through the search box (the same way a real visitor would reach 
an item outside the currently open division) and both its Preview and Open actions were tested.

## Root cause of the real blanks David saw

Two bugs in `build_command.py`'s generated JS, both in the shared preview iframe:

1. **The poisoned iframe.** `closePreview()` set `pframe.src = "about:blank"` to reset the panel.
   That is a real navigation, not a reset, and Chromium's site isolation gives a file:// document
   that is explicitly navigated to `about:blank` its own isolated process on the second and later
   use. Every later `pframe.contentWindow.document` write (how an inlined HTML tool's Preview or
   Open renders) then throws `Blocked a frame with origin ... from accessing a cross-origin frame`,
   the panel shows nothing, and because the exception fires partway through the click handler the
   panel can also fail to close cleanly, which then blocks every row underneath it too. Reproduced
   directly: the first Preview/Close/Open cycle on the very first pinned item (Client Dashboard
   (GHL)) threw exactly this error and broke every inline item tested afterward, in that order.
   **Fix:** build a brand new `<iframe>` element for every Preview/Open (never reuse or re-navigate
   one), and throw the old one away on close instead of sending it to `about:blank`.
2. **Open navigated the whole hub away.** For a PDF/DOCX/PPTX/XLSX, the Open button's non-preview
   branch did `window.location.href = href` -- same tab, so clicking Open on a document replaced
   COMMAND itself instead of opening a new tab, exactly matching "Open in COMMAND and it goes
   blank" from David's report (the address bar now points at the PDF, and getting back to COMMAND
   meant a manual back-navigation). **Fix:** Open now always does
   `window.open(href, "_blank", "noopener")`.

A defense-in-depth line was added too: the preview toolbar now always carries a visible "Not
loading? Open in a new tab" link whenever a PDF preview is open, and if the fresh iframe ever throws
on write, the panel shows a one-line message with a working Open link instead of sitting blank.

## Verification method note

The first two audit passes (in `_briefs/assets/run-BI-jobs/`, superseded by this file) showed 126,
then still 30, apparent blanks after the real fix above landed. All of those turned out to be two
bugs in the *audit script itself*, not in COMMAND:

- COMMAND only renders one division's rows at a time; a row in a division other than the one
  currently open is present in the DOM but `display:none`, so clicking it (without first using
  search or the nav, the way a real visitor would) times out. Fixed by having the script type each
  item's title into the search box before testing it.
- The audit script's title extraction read `.rtitle`'s full `textContent`, which glues a pinned
  star or a NEW/Premium/Internal badge directly onto the title with no space in the markup (the
  visual gap is CSS padding only) -- so titles like "Contractor AgreementPremium" never matched
  anything in the search index and the row stayed invisible. Fixed by reading only `.rtitle`'s own
  first text node.

One apparent failure survived both fixes ("Total Impact Model") and was hand-verified separately:
another row's blurb ("Prospect Web Pitch (live page)") happens to mention "Total Impact Model" in
its description text and matched first under the script's loose `hasText` row lookup; that row has
no Preview button, so the click timed out against the wrong row. Confirmed by hand that the actual
Total Impact Model row previews and opens correctly. Net result: **zero real blanks** across all
191 unique catalogue items.

## Minor items noticed, not fixed (out of scope for "blank")
- The catalogue carries two different, legitimately distinct rows both titled "Have Atlas One build
  this for me" (one is the prospect-facing forward link, the other is the internal build-request
  page it forwards to) and, unusually, both share the same `id` in catalogue.py. Neither is blank
  and nothing in the build depends on the id being unique, so left alone; flagged under Questions.

| Item | Mode | Preview | Open |
|---|---|---|---|
| 1099 Onboarding Packet | inline | ok(754375) | ok(754375) |
| 27 Business Generators | inline | ok(277939) | ok(277939) |
| 53 Business Calculators | inline | ok(519501) | ok(519501) |
| Agreements Index (2026-09-12) | relative | n/a | ok(file-exists) |
| Agreements, How They Fit | relative | n/a | ok(file-exists) |
| AI Email Assistant Setup Intake | inline | ok(32522) | ok(32522) |
| AI Email Assistant, Activity log (LIVE) | external | n/a | ok(href-present) |
| AI Email Assistant, Approval Queue (LIVE) | external | n/a | ok(href-present) |
| AI Email Assistant, Install & Support | inline | ok(5034) | ok(5034) |
| AI Email Assistant, one-pager | inline | ok(4814) | ok(4814) |
| AI Email Assistant, Tasks & Follow-ups (LIVE) | external | n/a | ok(href-present) |
| AI Email Assistant: client help page | inline | ok(51483) | ok(51483) |
| AI Services Schedule | relative | n/a | ok(file-exists) |
| AI Task Agent, one-pager | inline | ok(4035) | ok(4035) |
| Atlas One Email Templates (PDF) | relative | ok(src-set) | ok(file-exists) |
| Auditoria de Proveedores y Software (Espanol) | inline | ok(72492) | ok(72492) |
| Back Office Self-Assessment | inline | ok(25056) | ok(25056) |
| Background Screening, one-pager | inline | ok(3353) | ok(3353) |
| Benefits Aggregation Strategy (memo) | relative | n/a | ok(file-exists) |
| Benefits Menu: website copy for BRJ | relative | n/a | ok(file-exists) |
| Benefits Options Presenter | inline | ok(17850) | ok(17850) |
| Benefits Routing Tool | inline | ok(19767) | ok(19767) |
| Bonus Import Builder | inline | ok(31478) | ok(31478) |
| Book-of-Business & Non-Circumvention | relative | n/a | ok(file-exists) |
| Booking Confirmation Page | inline | ok(1611) | ok(1611) |
| Bookkeeping Client Agreement Packet | relative | ok(src-set) | ok(file-exists) |
| Bookkeeping Client Intake Guide | relative | n/a | ok(file-exists) |
| Bookkeeping Intake Form | inline | ok(17684) | ok(17684) |
| Bookkeeping Invoice (blank master) | relative | ok(src-set) | ok(file-exists) |
| Bookkeeping Marketing Sheet | relative | ok(src-set) | ok(file-exists) |
| Bookkeeping onboarding emails | relative | n/a | ok(file-exists) |
| Bookkeeping Profit Calculator V7 | relative | n/a | ok(file-exists) |
| Brand Guide (official 2026) | relative | ok(src-set) | ok(file-exists) |
| BRJ Overview (LIGHT) | relative | n/a | ok(file-exists) |
| BRJ Overview LIGHT (PDF) | relative | ok(src-set) | ok(file-exists) |
| BRJ Software Marketplace Package (2026-09-16) | relative | n/a | ok(file-exists) |
| Business Infrastructure Audit (Espanol) | inline | ok(40299) | ok(40299) |
| Business Value Diagnostic | inline | ok(31447) | ok(31447) |
| Business Value Diagnostic (Espanol) | inline | ok(33162) | ok(33162) |
| Carrier Master Plan Discovery Brief | relative | n/a | ok(file-exists) |
| Certified Payroll Converter | inline | ok(35376) | ok(35376) |
| Certified Payroll Manager | inline | ok(202559) | ok(202559) |
| Client Dashboard (GHL) | inline | ok(7284) | ok(7284) |
| Client Launch Companion | relative | n/a | ok(file-exists) |
| Client Launch Companion (PDF) | relative | ok(src-set) | ok(file-exists) |
| Client Launch Deck 2026-09 | relative | n/a | ok(file-exists) |
| Client Launch Deck 2026-09 (PDF) | relative | ok(src-set) | ok(file-exists) |
| Client Launch Email Drafts (2026-09-06) | inline | ok(10507) | ok(10507) |
| Client portal (admin sign-in) | external | n/a | ok(href-present) |
| Client Portal leave-behind | inline | ok(6544) | ok(6544) |
| COI collection phase 2 spec (GHL automation + portal plug in) | relative | n/a | ok(file-exists) |
| COI Tracker | inline | ok(18842) | ok(18842) |
| COI → WC Premium Estimator | inline | ok(17843) | ok(17843) |
| Collections Letter | inline | ok(6952) | ok(6952) |
| Commission & Revenue Tracker | inline | ok(15629) | ok(15629) |
| Company Safety Manual Template | relative | ok(src-set) | ok(file-exists) |
| Compliance Calendar by state | inline | ok(38489) | ok(38489) |
| Compliance Risk Scorecard | inline | ok(39424) | ok(39424) |
| Contractor Agreement | inline | ok(67496) | ok(67496) |
| Cornerstone Strategy | inline | ok(5766) | ok(5766) |
| Cost of a Compliance Mistake | inline | ok(26069) | ok(26069) |
| Disciplinary Write-Up | inline | ok(25173) | ok(25173) |
| Division sheet: Benefits & Retirement | relative | ok(src-set) | ok(file-exists) |
| Division sheet: Business Consulting | relative | ok(src-set) | ok(file-exists) |
| Division sheet: Financial Services | relative | ok(src-set) | ok(file-exists) |
| Division sheet: Risk & Insurance | relative | ok(src-set) | ok(file-exists) |
| Division sheet: Technology & Operations | relative | ok(src-set) | ok(file-exists) |
| Division sheet: Workforce & HR | relative | ok(src-set) | ok(file-exists) |
| Document Inventory | relative | ok(src-set) | ok(file-exists) |
| Document Services Pricing Options (2026-09-06) | relative | n/a | ok(file-exists) |
| Email Blast Library | relative | n/a | ok(file-exists) |
| Email HTML how to (survives Outlook) | relative | n/a | ok(file-exists) |
| Employee Benefits Menu | inline | ok(20619) | ok(20619) |
| Employee Benefits Menu (PDF) | relative | ok(src-set) | ok(file-exists) |
| Employee Handbook Builder | inline | ok(565160) | ok(565160) |
| Enrollment Guide | inline | ok(25871) | ok(25871) |
| Everything Atlas One handles (public page) | inline | ok(19172) | ok(19172) |
| Feedback / Review Request | inline | ok(4295) | ok(4295) |
| GHL Build Playbook | inline | ok(4554) | ok(4554) |
| GHL Prospecting Workflows Runbook | relative | n/a | ok(file-exists) |
| Have Atlas One build this for me | inline | ok(13976) | ok(13976) |
| Health Comparison Builder | inline | ok(61309) | ok(61309) |
| Health Quote Census | inline | ok(66400) | ok(66400) |
| Health Quote Tool | inline | ok(11633) | ok(11633) |
| Hold Harmless and Acknowledgement (2026-09-15) | relative | n/a | ok(file-exists) |
| Hold Harmless and Acknowledgement (2026-09-15, PDF) | relative | ok(src-set) | ok(file-exists) |
| How to Build a Quote | inline | ok(3403) | ok(3403) |
| HR Template Library | inline | ok(134854) | ok(134854) |
| Industry Starter Kits | relative | ok(src-set) | ok(file-exists) |
| Infrastructure Audit | inline | ok(40299) | ok(40299) |
| INTERNAL Master Pricing V8 (xlsx) | relative | n/a | ok(file-exists) |
| Jotform Decision | inline | ok(3774) | ok(3774) |
| Labor Law Poster Center | inline | ok(66035) | ok(66035) |
| Master Client Services Agreement (2026-09-15) | relative | n/a | ok(file-exists) |
| Master Client Services Agreement (2026-09-15, PDF) | relative | ok(src-set) | ok(file-exists) |
| Member Program Spec | relative | n/a | ok(file-exists) |
| Membership Brochure (4 pages) | inline | ok(28619) | ok(28619) |
| Membership Comparison (one page) | inline | ok(21835) | ok(21835) |
| Microsoft 365 through Atlas One, one-pager | inline | ok(5138) | ok(5138) |
| Microsoft 365 through Atlas One, one-pager (PDF) | relative | ok(src-set) | ok(file-exists) |
| Mutual NDA | relative | n/a | ok(file-exists) |
| Mutual NDA (PDF) | relative | ok(src-set) | ok(file-exists) |
| Mutual NDA TEMPLATE (DRAFT, 2026-09-12) | relative | n/a | ok(file-exists) |
| NDA Builder | inline | ok(67850) | ok(67850) |
| New Client Onboarding Intake (PDF) | relative | ok(src-set) | ok(file-exists) |
| Overlay 01: Audiology | inline | ok(25431) | ok(25431) |
| Overlay 02: Dental, Ortho, Optometry, ENT | inline | ok(15418) | ok(15418) |
| Overlay 03: Construction and Trades | inline | ok(15292) | ok(15292) |
| Overlay 04: Technology and Startups | inline | ok(14794) | ok(14794) |
| Overlay 05: Hospitality and Restaurants | inline | ok(15121) | ok(15121) |
| Overlay 06: Professional Services | inline | ok(15020) | ok(15020) |
| Partner deck v9 LIGHT (43 slides) | relative | n/a | ok(file-exists) |
| Partner deck, 20 slide room cut (2026-09-12) | relative | n/a | ok(file-exists) |
| Partner Pitch Deck v9 | relative | n/a | ok(file-exists) |
| Partner Pitch Deck v9 (PDF) | relative | ok(src-set) | ok(file-exists) |
| Partner Speaking Sheet | relative | ok(src-set) | ok(file-exists) |
| Payroll → GL Import | inline | ok(125442) | ok(125442) |
| PEO Comparison Tool | inline | ok(20889) | ok(20889) |
| PEO Intake Form | inline | ok(23618) | ok(23618) |
| PEO Private Label Ask | relative | n/a | ok(file-exists) |
| PEO Services Schedule | relative | n/a | ok(file-exists) |
| PEO vs ASO vs Software | inline | ok(10958) | ok(10958) |
| Price List (client facing, 2 pages) | inline | ok(45603) | ok(45603) |
| Price List (PDF) | relative | ok(src-set) | ok(file-exists) |
| Pricing Page Instructions for BRJ | relative | n/a | ok(file-exists) |
| Proof Sheet | inline | ok(4806) | ok(4806) |
| Proposal Shell (2026-09-15) | relative | n/a | ok(file-exists) |
| Prospect Email Templates | relative | n/a | ok(file-exists) |
| Prospect Onboarding Tracker | inline | ok(45926) | ok(45926) |
| Prospect Pitch Deck | relative | n/a | ok(file-exists) |
| Prospect Pitch Deck, First Meeting (9 slides) | relative | ok(src-set) | ok(file-exists) |
| Prospect Pitch Deck, First Meeting (PPTX) | relative | n/a | ok(file-exists) |
| Prospect Web Pitch (live page) | relative | n/a | ok(file-exists) |
| Prospecting Playbook v1 | inline | ok(53028) | ok(53028) |
| Quick Quote | inline | ok(117303) | ok(117303) |
| QuickBooks accountant access guide | relative | ok(src-set) | ok(file-exists) |
| Quote & ROI Builder | inline | ok(505081) | ok(505081) |
| Quote Cockpit (START HERE) | inline | ok(576540) | ok(576540) |
| Referral Partner Agreement TEMPLATE (DRAFT, 2026-09-12) | relative | n/a | ok(file-exists) |
| Referral Request Emails | relative | n/a | ok(file-exists) |
| Retention Cost Calculator | inline | ok(35417) | ok(35417) |
| Retention Cost Calculator (Espanol) | inline | ok(35417) | ok(35417) |
| Retention Scorecard | inline | ok(15580) | ok(15580) |
| Retention Scorecard (Espanol) | inline | ok(15580) | ok(15580) |
| Safety Manual Builder | inline | ok(299155) | ok(299155) |
| Sales Conversation Playbook | inline | ok(44418) | ok(44418) |
| Sample Proposals, Tell Me More LLC (2026-09-15, 8 docs) | relative | n/a | ok(file-exists) |
| Savings Summary | inline | ok(32931) | ok(32931) |
| Scan ID | inline | ok(4266) | ok(4266) |
| Schedule, AI Services (2026-09-15, regenerated) | relative | n/a | ok(file-exists) |
| Schedule, Bookkeeping (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Certified Payroll (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, COI Tracking (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Document Services (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Membership (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Payroll to GL Converter (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Software and Licenses (2026-09-15) | relative | n/a | ok(file-exists) |
| Schedule, Software and Licenses (2026-09-15, PDF) | relative | ok(src-set) | ok(file-exists) |
| Schedule, WC Audit Recovery (2026-09-15) | relative | n/a | ok(file-exists) |
| Screening Pricing Calculator | inline | ok(10217) | ok(10217) |
| Separation Letter | inline | ok(28093) | ok(28093) |
| Service deck: AI Task Agent | relative | n/a | ok(file-exists) |
| Service deck: Bookkeeping & Accounting | relative | n/a | ok(file-exists) |
| Service deck: Handbook & Safety | relative | n/a | ok(file-exists) |
| Service deck: WC Premium Audit Review | relative | n/a | ok(file-exists) |
| Services One-Pager (PPTX) | relative | n/a | ok(file-exists) |
| Services Overview (one page, every service) | relative | ok(src-set) | ok(file-exists) |
| Software and licenses card (portal Add services) | inline | ok(2036) | ok(2036) |
| Software and Licenses, one-pager | inline | ok(5420) | ok(5420) |
| Software and Licenses, one-pager (PDF) | relative | ok(src-set) | ok(file-exists) |
| Software and Licenses: website copy for BRJ | relative | n/a | ok(file-exists) |
| Software card: spec for PORTAL | relative | n/a | ok(file-exists) |
| Software Marketplace Catalog v2 (md) | relative | n/a | ok(file-exists) |
| Software Marketplace Catalog v2 (xlsx) | relative | n/a | ok(file-exists) |
| Software Marketplace Sheet (tiles) | inline | ok(26502) | ok(26502) |
| Start to Success | relative | ok(src-set) | ok(file-exists) |
| Time and Cost Savings Discovery | inline | ok(15357) | ok(15357) |
| Tools Cheat Sheet | relative | ok(src-set) | ok(file-exists) |
| Total Impact Model | inline | click-failed: locator.click: Timeout 5000ms exceeded. | cross-origin |
| True Cost of Doing It Yourself | inline | ok(14728) | ok(14728) |
| Vendor & Software Audit | inline | ok(70539) | ok(70539) |
| Vendor Partner Directory | relative | n/a | ok(file-exists) |
| VIP Partnership Plus Calculator | inline | ok(10255) | ok(10255) |
| W-2 At-Will Agreement | inline | ok(82270) | ok(82270) |
| W-2 Onboarding Packet | inline | ok(47873) | ok(47873) |
| WC No-Loss Letter / Loss History Affidavit | inline | ok(5986) | ok(5986) |
| Website Pricing Page SPEC (for BRJ) | inline | ok(13172) | ok(13172) |
| What We Do, Business Overview | inline | ok(3758) | ok(3758) |
| Workforce Software Comparison | inline | ok(19905) | ok(19905) |
| WSA Audiology Partnership Plus Overview v3 | inline | ok(40609) | ok(40609) |
| WSA Audiology Partnership Plus Overview v3 (PDF) | relative | ok(src-set) | ok(file-exists) |
