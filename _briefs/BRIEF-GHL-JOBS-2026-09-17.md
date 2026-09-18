# BRIEF for the GHL-JOBS terminal: Run BL (COMMAND v2 in three zones, Sales Kit file, front door page, PPG one pager, script path hygiene)

Terminal name: GHL-JOBS. Files and code only (no browser clicks in GHL, no GHL API needed this run). Build end
to end, no questions, answer permission prompts yourself, log assumptions, questions at the END of the report.
Back up the prior report first: copy `_BUILD-LOG/RUN-GHL-JOBS-report.md` to
`_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-JOBS-report-RunBK.md` (already copied; overwrite is fine).
Run everything in this session: never fork, background or delegate to a sub agent (rule 44). Do only the jobs
written here. Commit and push the forms repo. Repo assets in `_briefs/assets/run-BL-jobs/`. No dashes in any
copy you write (commas, periods, colons, parentheses instead). Log every step to `TERMINAL-GHL-JOBS-live.md`
as you go; report to `RUN-GHL-JOBS-report.md` (quoted heredoc).

Master Kit path: find it by name, never hardcode a username:
`MK=$(find ~ -type d -name "Atlas_One_Master_Kit" 2>/dev/null | grep -vi -e _to_delete -e archiv | head -1)`.
`A1_Sales` is `$MK/../A1_Sales` (same Marketing folder). Fonts: `$MK/_INTERNAL (do not share)/fonts_embed.css`.

## Job 1: COMMAND v2, three zones (David 2026-09-17: "I do not like the layout")
Edit `_INTERNAL (do not share)/build_command.py` (and `catalogue.py` only where a row needs a zone). Keep the
park and decode mechanism, the forbidden term guard, the search box and the counts. Change the layout:

1. Three top level zones, in this order, as three big tabs across the top of the page (not a left rail of
   fourteen sections): **Sales Kit**, **Tools**, **Internal**. Under 700px the tabs stay as a sticky top bar.
   Zone rule, derived from fields that already exist, so no row needs hand tagging:
   - Tools: every row with `kind` of tool, calculator, builder or generator (any inlined html tool), whatever
     its audience. Group inside the zone by the six divisions in the official order (Workforce & HR, Benefits &
     Retirement, Financial Services, Risk & Insurance, Technology & Operations, Business Consulting), then
     "Cross division" for anything unassigned. Start here rows that are tools go to Tools.
   - Internal: every row with `audience='internal'` that is not a tool, plus every row in the divisions
     `Internal (do not share)`, `Pricing & Quotes`, `Email templates`, `Agreements`. Group by those divisions.
   - Sales Kit: everything else (audience prospect or client, plus decks, Sell & Pitch, Industry overlays,
     Intake & Client, Start here non tool rows). Group: Start here, Decks, Sell & Pitch, Industry overlays,
     Intake & Client, then the six divisions for any remaining rows.
   If a row lands somewhere that reads wrong, add an optional `zone=` field on that row in `catalogue.py` that
   overrides the rule; list every override in the report. Do not move files on disk.
2. Internal zone is collapsed by default and opens only after a passphrase prompt (client side, session only,
   `sessionStorage`). Passphrase `atlas1` for now; put it in one constant at the top of build_command.py with a
   comment "curtain, not security; the file lives in David's OneDrive". The Internal tab shows a lock glyph
   (CSS only, no icon font) until opened. The report tells David plainly that this is a curtain and that the
   real protection is that COMMAND never leaves the Master Kit.
3. Rows stay rows (title, blurb, kind badge, Open / Preview buttons) but each zone gets a short lede line under
   the tab explaining who it is for: Sales Kit "What you show and send to prospects and clients", Tools
   "Calculators, builders and converters, all offline", Internal "Pricing, margins, agreements and build notes.
   Never shared." Status by form (solid, tinted, outlined, left rule), four colours only, Horas and DM Sans
   embedded, no CDN calls, works offline on iPhone and iPad.
4. Keep the previous fix (fresh iframe per preview, Open in new tab, fallback link). Verify Preview and Open on
   at least one row per zone in headless Chromium, zero console errors, screenshots at 1440 and 390 of each
   zone (Internal both locked and unlocked) into `_briefs/assets/run-BL-jobs/shots/`.
5. Rebuild `$MK/Atlas One COMMAND.html` in place (same filename; the stamp must show today). Move nothing else.

## Job 2: the shareable Sales Kit file
Add a second output to build_command.py: `Atlas One Sales Kit.html`, written to
`$MK/../A1_Sales/Atlas One Sales Kit.html`. Same look, only the Sales Kit and Tools zones, and only rows with
audience prospect or client. No Internal zone, no passphrase, no row whose `path` is under `_INTERNAL`. The
forbidden term guard runs against every row and every inlined tool in this file with the existing allowlist;
a hit hard fails the build. Add one line to the hero: "Shared by Atlas One Solutions. Call 380-CALL-A1S
(380-225-5217)." This is the file David hands to BRJ, Thomas and referral partners instead of COMMAND. Add a
row for it in the catalogue (Sales Kit zone, Start here, audience internal, blurb "The shareable launcher.
Hand this to partners and BRJ, never COMMAND.").

## Job 3: front door page (start.atlasonesolutions.com, spec item 7 in the growth review)
In `~/Projects/atlas-one-intake-forms` build `start/index.html`, self contained, same brand as `index.html`
(four colours, DM Sans from Google Fonts is fine here because this page is online only). Content, top to
bottom, no prices anywhere:
1. Hero: the periwinkle laptop mark (copy the asset the peo/ page uses), "Atlas One Solutions", tagline
   "One Call Solves Everything." Subhead: "Payroll, benefits, insurance and books for growing businesses in all
   50 states. One relationship replaces ten to twenty vendors."
2. The Audit offer block: "Start with a Back Office Audit" and the guarantee, word for word: "Two times your
   first year membership in documented savings or risk removed, or there is nothing to buy." Button "Book the
   30 minute Audit" to https://api.leadconnectorhq.com/widget/groups/book-david and a second button "15 minute
   intro call" to https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp.
3. Five curated tools, as cards linking to the public tool pages that already exist under `tools/` in this
   repo: `time-savings/` first (Time and Cost Savings Discovery), then `vendor-consolidation/`,
   `retention-cost/`, `wc-premium-check/` and `self-assessment/` (open each, confirm it loads and is public, and
   use its own title). One line each on why it matters, no HR wording in the lede (HR stays in the background).
   A sixth small link "See every tool" to `../tools/`.
4. "Already talking with David?" with the two intake cards from `index.html` (Quote & Onboarding Intake,
   Accounting, Bookkeeping & Payroll) linking to `../peo/` and `../bookkeeping/`.
5. Footer: "Call 380-CALL-A1S (380-225-5217)" with `tel:+13802255217`, david@atlasonesolutions.com, "Serving
   businesses in all 50 states."
Test at 390 and 1440 headless, zero console errors, no horizontal scroll at 390. Commit and push so it is live
at https://forms.atlasonesolutions.com/start/ . Do not touch DNS. Report line for David: "To put it on
start.atlasonesolutions.com: GoDaddy, atlasonesolutions.com, DNS, Forwarding, add a subdomain forward for
`start` to https://forms.atlasonesolutions.com/start/ (permanent 301, forward only)." Also add a card for the
page in the catalogue (Sales Kit, Start here, audience prospect, path is the live URL).

## Job 4: PPG client program one pager (referral partner offer)
Build `$MK/../A1_Sales/A1 What we do Overview/Atlas_One_Partner_Client_Program_PPG.html`, one printable page
(Letter, print CSS, `@page` margins), self contained, fonts embedded from `fonts_embed.css`, four colours,
laptop mark, no dashes, no vendor or PEO brand names, no Atlas One internal numbers. Audience: Jasmine Wickens
at PeoplePay Global, to hand to her clients. Copy (use as written, tighten only for fit):

Title: "Atlas One for PeoplePay Global clients"
Sub: "Back office help your clients can switch on in a week, through the relationship you already have."

Block 1, "What your clients get" (three columns):
- Membership: one point of contact for payroll, benefits, insurance and books. Essential $99 a month,
  Professional $399 a month, Enterprise $999 a month, Concierge $1,900 a month. Setup fees shown at quote time.
- Documents built for them: employment agreements, contractor agreements, NDAs, offer letters, handbooks and
  safety manuals, state specific, 50 states. Agreement build $450 per document, agreement bundle $1,200,
  policy or document design $175, employee handbook and safety manual quoted on the membership.
- The Audit Guarantee: two times the first year membership in documented savings or risk removed, or there is
  nothing to buy.

Block 2, "How the program works" (four numbered steps): 1. PPG introduces the client by email or the Send a
referral link. 2. David books a 30 minute Audit with the client. 3. The client chooses a membership or a
document build; Atlas One does the work and bills the client directly. 4. PPG is paid on every closed client
under the referral agreement already in place. (No percentage on the page; the agreement governs.)

Block 3, "Why it fits PPG clients": three short lines: growing teams hiring across states, founders who want
one call instead of ten vendors, companies that need documents right the first time (the Vet-Ai California
hire package is the example, unnamed: "a California executive hire packaged in two days: offer letter,
commission agreement, state guide and hold harmless").

Footer: "David Taylor, Founder, Atlas One Solutions. Call 380-CALL-A1S (380-225-5217).
david@atlasonesolutions.com. Book: https://api.leadconnectorhq.com/widget/groups/book-david"

Render to PDF beside it (`Atlas_One_Partner_Client_Program_PPG.pdf`, use `tools/render_html_pdfs.py` or
headless Chromium). Look at the PDF page image and confirm one page, nothing clipped. Add a catalogue row
(Sales Kit, Sell & Pitch, audience prospect).

## Job 5: script path hygiene
Grep `_INTERNAL (do not share)/*.py` and `_INTERNAL (do not share)/tools/*.py` for `/Users/davidtaylor` and
`/Users/david/`. Known hits: `tools/agreements_inventory_2026-09-12.py`, `tools/build_mutual_nda_2026-09-12.py`,
`tools/build_referral_partner_agreement_2026-09-12.py`, `tools/render_html_pdfs.py`. Replace each hardcoded
path with a `find_master_kit()` helper (walk up from the script's own location to the folder named
`Atlas_One_Master_Kit`, else the find-by-name command) and derive every other path from it. Dry run each
script (`--check` or import only) so nothing regenerates a document. Report the before and after line for each.

## Report
`RUN-GHL-JOBS-report.md`: built, paths, screenshots, catalogue overrides, forbidden guard result for the Sales
Kit, the five tools chosen for the front door, assumptions, skipped, then "Questions for David" at the end.
