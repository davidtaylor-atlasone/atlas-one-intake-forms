# BRIEF for the GHL-JOBS terminal: Run AR (one launcher, OneDrive clean-up, calculator restyle)

Terminal name: GHL-JOBS. Files, code and headless Chromium only. Never open the GoHighLevel browser.
Read this whole brief, then build end to end. Do not ask questions. Answer every permission prompt yourself,
make the reasonable call, log it under Assumptions, and put every question in "Questions for David" at the END
of the report. Log every step to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; write `_BUILD-LOG/RUN-GHL-JOBS-report.md`
at the end (quoted heredoc or a file tool, never an unquoted heredoc). Back up the prior report to
`_to_delete/superseded-2026-09-14/prior-reports/RUN-GHL-JOBS-report-RunAQ.md` first.
Known limits: you cannot overwrite an existing OneDrive docx/pptx/xlsx and cannot deploy to Azure. Moving files
with mv into `_to_delete/` works. Writing NEW html/py/json files works. Rebuilding the Portal works.
Use /compact between jobs.

Master Kit: `~/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/`
Marketing root (one level above HR_Docs): `.../2. Atlas 1 Solutions Marketing/`
OneDrive root: `~/Library/CloudStorage/OneDrive-AtlasOneSolutions/` (holds `_to_delete/` and `_reference-archive/`)
Repo: `~/Projects/atlas-one-intake-forms` (commit and push at the end of each job).

## Why this run exists (David, 2026-09-14 evening)
David opens three launchers today and cannot tell them apart:
1. `2. Atlas 1 Solutions Marketing/Atlas_One_MASTER_HUB.html`: 167 cards in 14 categories (sales docs, decks,
   pricing, agreements, internal, plus tool cards), links by relative path, left rail, only works from OneDrive
   on a Mac. Internal only.
2. `Master_Kit/Atlas One — Tools Hub.html`: 32 tool links in 9 categories, relative paths, meant to be shared
   with prospects but only works if the whole folder travels with it.
3. `Master_Kit/Atlas One PORTAL.html`: 44 tools INLINED (20 MB), six sections, works offline on iPhone, iPad
   and Mac. Internal only (carries the rate card). Built by `_INTERNAL (do not share)/build_portal_single.py`
   from the catalogue in `_INTERNAL (do not share)/build_portal.py`.
The Tools Hub and the Portal are the same idea twice. The Master Hub is the third copy of the tool list plus the
sales documents. David wants ONE file to open, in the layout of the client portal app (left navigation, search
at the top, structured rows, not a wall of identical cards), that works offline on his phone at a prospect's
office. He also wants the prospect-shareable version to be a single self-contained file.

## Job 1: build "Atlas One COMMAND" (one internal launcher) and "Atlas One Tools" (one shareable file)

### 1a. One catalogue
Create `_INTERNAL (do not share)/catalogue.py`: a single Python list of entries, the only source of truth for
both outputs. Merge three sources, deduplicating by resolved file path (same file listed twice keeps the richer
blurb): the `build_portal.py` sections (44 tools), the Master Hub `ITEMS` array (167 rows: category, title,
blurb, relative path, type) and the Tools Hub link list (32). Each entry: `id`, `title`, `blurb` (one line, no
dashes), `path` (relative to the Marketing root), `kind` (tool | builder | deck | doc | pdf | sheet | link |
note), `division` (one of the six divisions, or Sales, Internal, Start here), `audience` (internal | prospect |
client), `inline` (True for html tools that get embedded), `badge` (NEW, UPDATED, INTERNAL or blank),
`pinned` (True for the twelve things David opens most: Quick Quote, Quote Cockpit, Health Quote Tool, Time and
Cost Savings, Vendor and Software Audit, Prospect Pitch Deck, First Meeting cut, Membership Pricing, Proof
Sheet, Sales Conversation Playbook, Onboarding Tracker, Payroll to GL Converter). Keep `build_portal.py`'s
per-tool "What is this for?" text. Write `catalogue_check.py` that fails if any `path` does not exist, and run
it. Anything in the three old launchers that points at a file that no longer exists: drop it and list it in
the report.

### 1b. The layout (copy the client portal app, not the old hubs)
Reference: `~/Projects/atlas-one-portal` (left navigation, "Go to a page" search with Cmd+K, DM Sans, Horas
headings, paper background, periwinkle primary button). Render it in headless Chromium first and match it.
- Left rail: Start here (pinned twelve + recently opened, stored in localStorage), then the six divisions in
  the official order (Workforce & HR, Benefits & Retirement, Financial Services, Risk & Insurance, Technology
  & Operations, Business Consulting), then Sell & Pitch, Decks, Pricing & Quotes, Agreements, Email templates,
  Intake & Client, Industry overlays, Internal (do not share). Counts beside each. Collapses to a top bar on a
  phone (test at 390px).
- Main area: a section header, then ROWS, not cards: a one-line row per item (kind icon, title, one-line
  blurb, badge chip, an Open button, a Preview button for html and pdf). Rows are grouped under small
  sub-headings inside a section (for example, in Workforce & HR: Tools, Builders, Documents, Decks). Dense,
  scannable, one item per line on desktop; the blurb wraps under the title on a phone.
- Search at the top filters every section at once; results show the section name on each row.
- Preview opens inlined tools in a full-height panel inside the page (same as the Portal today); decks, Word
  and Excel open in their app; PDFs preview inline when inlined, otherwise open.
- Status is shown by FORM (solid, tinted, outlined chip, left rule), never a fifth colour. Four brand colours
  only. Check contrast in light and dark before calling it done.
- Header shows the build stamp (date and time) exactly like the Portal does today, in the tab title too.
- Fonts embedded (Horas and DM Sans as @font-face data), zero network requests, works from file:// on iPhone.

### 1c. Two outputs from one builder
Write `_INTERNAL (do not share)/build_command.py` (start from `build_portal_single.py`; keep its inlining,
size handling and stamp logic). It writes:
1. `Master_Kit/Atlas One COMMAND.html`: every entry with audience internal, prospect or client; html tools
   inlined; docs, decks, sheets and PDFs linked by relative path from the Master Kit (they open on the Mac;
   on the phone the row says "Open in OneDrive").
2. `Master_Kit/Atlas One Tools (share with prospects).html`: audience prospect only, everything inlined, no
   Internal section, no rate card, no margins, no vendor names. Grep the output for "margin", "commission",
   "wholesale", "Cornerstone", "G&A", "VeroHCM" and fail the build if any appear.
Refuse to write `Atlas One PORTAL.html` (same guard as build_portal.py). Both files get the stamp.

### 1d. Retire the three old launchers (David gets confused by duplicates)
After both outputs render clean, mv `Atlas One PORTAL.html`, `Atlas One — Tools Hub.html` and
`2. Atlas 1 Solutions Marketing/Atlas_One_MASTER_HUB.html` into `_to_delete/superseded-2026-09-14/launchers/`.
Then grep the Master Kit, A1_Sales, the repo and `_BUILD-LOG/*.md` for the three old file names and list every
reference in the report (do not edit docx/pptx; do fix html/md/py references you find). Update
`_INTERNAL (do not share)/README` or CLAUDE.md notes so the rebuild command becomes
`python3 "_INTERNAL (do not share)/build_command.py" "<Master_Kit path>"`. Keep `build_portal_single.py` in
place but make it print "superseded by build_command.py" and exit.

### 1e. Verify (the report must show these, not claim them)
Render COMMAND at 1440 and 390 in light and dark, screenshots in `_briefs/assets/run-AR/shots/`; zero console
errors; zero non-file network requests; open six rows (two tools, one builder, one deck link, one pdf, one
internal) and confirm each resolves; confirm the pinned row count is twelve; confirm the shareable file has no
Internal section and passes the grep guard; report both file sizes.

## Job 2: OneDrive duplicate and old-version audit (inventory first, then safe moves)

Scope: `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/` (A1_Sales, HR_Docs, the Master Kit). Exclude
`_to_delete/`, `_gold_backup*`, `3. Cornerstone PEO/`, `_reference-archive/`. About 2,500 files after Cowork
moved the 3.1 GB `04 Safety Library/Programs & Checklists/Safety Resources` folder (WCF and old training
material, nothing linked to it) into `OneDrive/_reference-archive/` on 2026-09-14.

2a. Inventory: write `_BUILD-LOG/onedrive-audit-2026-09-14.md` with these tables:
- Exact duplicates (same SHA-256, different paths). Keep the copy inside the Master Kit or A1_Sales in the
  most specific folder; list the other.
- Version families: files whose names differ only by V1/V2/v7.0, a date, "(1)", "copy", "old", "FINAL",
  "draft". Show the newest by modified time and the others.
- Zip files (about 26) and whether their contents already exist unzipped beside them (compare file lists).
  The 14 brand zips in `A1_Final Brand/` are the brand kit deliverable: keep, do not touch.
- `~$` lock files, `.DS_Store`, empty folders.
- Anything still carrying the OLD globe A1 logo file name, the old phone 385-213-7177, or retired prices
  ($0/$299/$899 membership, $199/$349/$649 AI assistant) in html, md, txt (docx/pptx are read-only for you:
  list, do not edit).
- Files nothing links to: html/pdf/docx in the Master Kit and A1_Sales that no launcher catalogue entry, no
  Master Hub row and no other html references. Mark them "unreferenced", do not move them.

2b. Safe moves (do these; they are reversible, David empties `_to_delete` himself):
- Exact byte-for-byte duplicates: mv the extra copy to `_to_delete/superseded-2026-09-14/duplicates/<same
  relative path>`.
- Zips whose contents exist unzipped beside them: mv the zip to `.../duplicates/zips/`.
- `~$` lock files and `.DS_Store`: mv to `.../duplicates/junk/`.
Everything else (version families, unreferenced files, retired-price hits in Office files) is a LIST for
David, with a recommended action per row. Do not move them.

## Job 3: restyle the 53 Business Calculators tool to the same layout as Job 1

File: the 53-calculator hub in `06 Calculators and Tools (NEW Aug 2026)/` (find it by title; the file with the
category pills such as "Payroll and Labor Cost 10" across the top). Back it up to
`_to_delete/superseded-2026-09-14/calculators-before/` first, then rebuild the shell only: left navigation of
categories with counts (collapses to a top bar at 390px), search at the top, calculators as rows (title, one
line, Open) that expand in place, the calculator forms themselves untouched. Four colours, DM Sans and Horas
embedded, no network calls, print button kept. Do the same for the 28 business-document generators file
"(17 generators).html" (do not rename it). Render both at 1440 and 390, zero console errors, then rebuild
COMMAND so the inlined copies are current.

## Do not do
No GHL browser. No Azure. No edits to docx/pptx/xlsx. Do not touch `A1_Final Brand/`, `_INTERNAL` pricing
sheets, `12 DEMO Proposal Set` or any prospect folder. Do not delete anything; mv only.

## Report: RUN-GHL-JOBS-report.md
Sections: Built (paths), Retired (paths moved), Verification (what you opened and saw, sizes, screenshots),
Assumptions, Skipped, Questions for David (at the end).
