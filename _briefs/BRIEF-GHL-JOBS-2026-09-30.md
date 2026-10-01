# BRIEF-GHL-JOBS (current run: GHL-JOBS Run CS, 2026-09-30). Charity first, then the locked price book, then COMMAND v2.

Installed by A1 GHL Jobs 4 after auditing Run CR (PASS, see the end of this brief). Archive Run CR's report first.
Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI, never the portal
repo. No questions mid run. No sends, no spending, no new vendors, no deploys. Deleting is a move into
`Master_Kit/_to_delete/superseded-2026-09-30/`. No dashes in anything a client or prospect reads (emails: no
dashes at all). Log a line when each job STARTS and ENDS with the real clock time (`date`). There is NO time
limit: do every job in order and do not stop early. Keep every Run CL to CR guard on. Finish with
`_BUILD-LOG/RUN-GHL-JOBS-report.md`. Charity Taylor is selling NOW: Jobs 0 to 2 are the priority, do them first
and rebuild her kit at the end of Job 2 so she has it even if a later job takes long.

Reference files (read before starting):
- `_BUILD-LOG/price-book-locked-2026-09-30.md` (the locked price decisions, David approved 2026-09-30)
- `_to_delete/superseded-2026-09-30/BRIEF-GHL-JOBS-queued-runCS.md` (full COMMAND v2 detail, its Jobs 0 to 8)
- `_to_delete/superseded-2026-09-30/BRIEF-GHL-JOBS-queued-payroll-minimums.md` (payroll minimums detail)

## Job 0: Charity is live
Do Job 0 of the queued Run CS file exactly (people.json `held` false, her card joins the publish list on
`cards-draft` only, READ ME FIRST says ready to hand over, pending: her own booking link). Do not push or merge.

## Job 1: apply the LOCKED price book everywhere, and lock it
1. prices.json becomes V9 from the price book: add `_locked: "2026-09-30, David"` and a `_changelog` list; add
   payroll tax setup ($250 withholding, $250 unemployment, $50 per additional local or state tax account such as
   Nevada MBT, expedited +$100), payroll minimums ($100 monthly, $150 other cycles, greater of), year end W-2s
   (one extra run at the client's rate), WC audit 25%, rush $150, A/P or A/R standalone $250, bookkeeping with
   bill pay $750 (A/R not included), AI Task Agent Enterprise rate $99; set PEO, ASO, HCM, screening, website,
   hosting, blogging, bookkeeping Medium and Large to quoted text; bookkeeping Small "Starting at $300".
2. Regenerate or edit every file from prices.json. At minimum: Price List (html, pdf, price_list_template.html),
   Bookkeeping Marketing Sheet V8 (via bookkeeping-docs/build.py; QuickBooks $85/$140/$340; Small starting $300;
   payroll minimum rows; W-2 row; payroll tax rows with the $50 local line, remove "no additional charge"),
   Financial Services and Payroll HR and Tech Ops division sheets (division_sheets_build and templates), both
   membership sheets (brochure and comparison: Professional = 3 hours and quarterly review; remove the per hire
   pack and discount percentage rows, say "updates included at Professional and above"; AI Task Agent: $199,
   $99 if bundled or Enterprise, included Concierge), Quick Quote (Professional description, screening and web
   lines to quoted, wh_setup priced, payroll minimum max() logic, QuickBooks values unchanged), Quote Cockpit
   and build_cockpit.py (remove $25 and 0.95% PEO defaults, minimum logic), proposal generator
   (`08 ROI Quote Master Template/PEO_Proposal_Generator_V4.5_MASTER/`: remove rate defaults, and in brands.py
   set ONLY the "Atlas One Solutions" record's phone to 380-225-5217, tel:+13802255217; leave the other four
   brand records alone; regenerate a test deck and render the cover to PNG to prove it), agreements generate.py
   and every Schedule and Sample Proposal it builds (Professional wording, WC schedule 25%, MCSA payment due
   within fifteen days instead of ten, no late fee sentence anywhere), Bookkeeping Client Agreement Packet
   MASTER (remove the "2.9 percent plus $0.30" card surcharge sentence; ACH preferred, no processing fee),
   Service Content Library, Audit Workbench PRICES, Software one pager and marketplace catalogue if they print
   a changed price, Founding Partner Deck v9 (keep, update prices only), Presentation Services Deck, Master
   Blueprint v1 to v3 (update, or retire the older two if v3 supersedes them), Micah packet (Task Agent setup
   $500). Retire to `_to_delete/superseded-2026-09-30/`: HubSpot Products Import csv, the 2026-09-06 Document
   Services Pricing Options md, the loose duplicate `A1_Sales/A1 Agreements/Atlas_One_AI_Services_Schedule.docx`
   (the masters folder copy is current).
3. Guard: extend catalogue_check.py so every check runs (no early exit) and it FAILS on any client facing file,
   Quick Quote row, Cockpit row, generator default or skill text whose price is not in prices.json, and on any
   retired price ($75/$115/$275 QuickBooks, $23/$18/$12 payroll, "10 tickets", $299 bookkeeping, $750 Task Agent
   setup, $0/$299/$899 tiers, $199/$349/$649 or $299 plus $1,500 Email Assistant, $120/hr).
4. Write `_BUILD-LOG/SKILL-atlas-pricing-proposed.md`, the full atlas-pricing skill text generated from
   prices.json (Cowork proposes it to David).
5. Write `_BUILD-LOG/GHL-price-mismatches-2026-09-30.md`: every GHL product whose price or wording differs from
   prices.json (from the GHL product list in the price book); do NOT touch GHL.
6. Rerun the scan: zero retired prices left outside `_to_delete` and `_BUILD-LOG`. Report the before and after counts.

## Job 2: Charity's command center gets everything she needs to pitch (and clean both command centers)
David, 2026-09-30: her command center is missing the email templates, the talk scripts, the objection handling,
the Prospecting Playbook, the Sales Conversation Playbook, the presentation decks and the sales tab pieces.
1. Rep builds (`--person`) include every prospect or client audience piece: all email templates (rendered as
   styled HTML, not raw md), Sales Conversation Playbook, Prospecting Playbook, objection handling, industry
   overlays, the pitch decks (First Meeting deck, Prospect Pitch Deck, Presentation Services Deck, PDF and
   PPTX), every sales tab presentation in David's COMMAND including the current client presentations (she has
   clients of her own), one pagers, division sheets, membership sheets, price list, calculators a prospect sees.
   Still never: Internal, margins, commission, partner programs, BRJ, GHL, vendor ordering.
2. Remove every BRJ item and every GHL system item from BOTH command centers (David's and reps'). BRJ material
   stays in OneDrive only. GHL how to guides stay in OneDrive and the GHL lane's docs.
3. Every email template gets an "Attach these" line: which one pager, deck, sheet or tool link to attach (PDF or
   link), chosen from the kit. Show it on the template card and inside the rendered template.
4. NEW `A1_Sales/Email Templates/Atlas_One_Client_Announcement_Series.md` (and rendered HTML): 6 emails for
   David's and Charity's existing clients announcing Atlas One and the new services, value first. HARD RULE:
   make it unmistakable this is NOT an acquisition; nothing about their payroll, PEO, HR or benefits moves, only
   the rep's company name is changing and services are being added. Emails: (1) the news in plain words, (2)
   what you now get with one call, (3) the Back Office Audit and guarantee, (4) the membership in one page,
   (5) a real saving example, (6) a short check in. Each with subject line and "Attach these". No dashes. Short
   sentences, warm, direct, the way David talks (atlas-voice).
5. NEW `A1_Sales/A1 Playbook Sales/Atlas_One_Talk_Track.html`: who we are, what we solve, the 30 second and 2
   minute explanation, how we simplify the business into one relationship, discovery questions, the Back
   Office Audit ask, the top 12 objections with answers, and a closing line. Pull from the existing playbooks,
   do not invent new offers or prices. Put it at the top of her command center and David's.
6. Rebuild `--person charity`, run the Run CL scanner on her folder, list what she has and what (if anything) is
   still missing.

## Job 3: COMMAND v2 (David's and the reps')
Do Jobs 1 to 4 and 6 of the queued Run CS file (task hubs, one card per piece with format buttons, nothing opens as
code, Fortune 100 look). David's added asks, 2026-09-30: Open and Preview ALWAYS open a new browser tab (right
click "Open in new tab" and Cmd click work too), no Close button to hunt for; the search box searches EVERY hub
and tab at once from anywhere, including Internal; simpler and more streamlined than today. Render at 1440, 1024,
390 and look at the screenshots; redo it if it looks like a generic admin template.

## Job 4: readable on screen share, and toggles you can see
Applies to every HTML tool, calculator, intake page and sales piece in the Master Kit and A1_Sales (not the portal
repo; the PORTAL lane does the portal).
1. Screen share: prospects cannot read the tools when David shares his screen. Raise the base text size (body at
   least 17px, tables 16px, labels 15px) and add a "Presenting" button (top right, remembered on the device) that
   scales the whole page to 130 percent. Check it at 1440 wide in a shared window size of 1280x720.
2. Toggles, sliders, segmented controls, checkboxes and small buttons: clearly visible. Light theme: Dark Blue
   #23304d track or border 2px, knob Off White. Dark theme: Off White track or border, Dark Blue knob. Visible
   focus ring, 44px touch target, a text label ("Basic / In depth") beside every toggle. Brand colors only.
3. Membership comparison sheet ("One membership. Your whole back office."): the bottom rows are cut off; reformat
   so the whole table fits on screen and prints on its pages, nothing clipped, in both html and pdf.
4. Back Office Self Assessment, the "when were benefits last shopped" section: say "shopped with different
   carriers or brokers", and add a short "Why shopping matters" note (renewals creep, one broker quoting one
   carrier is not shopping). No prices.

## Job 5: carried items from the queued Run CS file
Jobs 5 (Scan ID), 7 (booking links website only) and 8 (vendor ordering, internal only) exactly as written there.

## Job 6: rebuild and prove
Rebuild COMMAND, the Sales Kit, `--person charity`; every guard green including the new price guard; headless
Chromium and WebKit at 1440 and 390, zero console errors, screenshots; the new tab test; the Presenting button
test; the price scan counts; old COMMAND retired. Report everything in `_BUILD-LOG/RUN-GHL-JOBS-report.md`.

## Cowork audit of Run CR (2026-09-30, A1 GHL Jobs 4): PASS
Checked on disk: 120 of 120 quiz items carry q_es and a_es; January General Industry prints three pages (talk,
employee quiz with zero answers, supervisor key); calendar carries the Spanish lines; the Toolbox Talks folder is
renamed. Card fixes are on branch cards-draft (repo not in the connected folder, taken from the report and its
committed screenshots). Findings carried forward: the Spanish has no accent marks (Calificacion, Espanol); leave
it for now, fix with the next Spanish pass. catalogue_check exited on its first check (price list prices not in
prices.json): Job 1 fixes the cause and removes the early exit.
