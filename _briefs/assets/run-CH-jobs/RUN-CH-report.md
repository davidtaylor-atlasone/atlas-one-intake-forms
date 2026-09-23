# RUN-GHL-JOBS report: Run CH (2026-09-23)

Terminal: GHL-JOBS. Brief: `_BUILD-LOG/BRIEF-GHL-JOBS.md` (copied to the repo at
`_briefs/RUN-CH-jobs-terminal.md`). Five jobs, all complete. Zero hard stops (no email or SMS
sent, no HIPAA toggle, no file deleted, nothing deployed, no spend).

Note on the name: the GHL terminal (browser UI session) separately used "Run CH" the same day for
an unrelated GHL email template job (commits 6685dca, cd6d079). That is not this run. This report
covers only the GHL-JOBS terminal's Run CH: Charity's kit, the guard, `--person`, and Hire date.

## Job 1: David's details outside the footer on Charity's copies

Scanned every Step 1 piece and the eight Sales Pieces for `david@atlasonesolutions` occurrences
that fall outside the `a1-footer-person` element (a small script comparing every hit's position
against every footer element's span). Found four, matching Cowork's three plus one more:

- **Services Overview** (`A1_Sales/A1 What we do Overview/Atlas_One_Services_Overview.html`): the
  header `.ovmeta` div (phone and email, no name).
- **Bookkeeping Marketing Sheet V8** (`A1_Sales/Atlas 1 Bookkeeping/Atlas_One_Bookkeeping_Marketing_Sheet_V8.html`):
  the header `.meta` block (name, title, phone, email).
- **Employee Benefits Menu** (`A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html`):
  the page's `CONFIG.a1` JavaScript object (`me`, `title`, `email`, `phone`, `book15`, `book30`).
- **Client Portal** (`A1_Sales/Client Portal/Atlas_One_Client_Portal.html`): the `.poc` "your one
  point of contact" block (name, title, phone, email). Not one of the three Cowork already found
  by hand, but the same pattern.

Every person contact outside the footer now carries the second contract the brief asked for:
markup gets the `a1-contact-person` class plus a `data-a1-kind` attribute naming its layout
(`phone-email`, `meta-inline`, `poc-block`); a CONFIG object gets matched by its own `a1: { ... }`
key. `swap_footer_person()` in `build_command.py` now swaps both, not just the footer.

Bookkeeping's header title changed from "David Taylor, President and Founder" to "David Taylor,
Founder" to match `people.json`, per the brief.

**A real bug found and fixed along the way:** the first version of the `a1-contact-person` swap
reused the same non-greedy backreference pattern `a1-footer-person` uses (match up to the first
closing tag of the same name). The `poc-block` layout wraps four nested `<div>`s inside its own
`<div class="a1-contact-person">`, so the non-greedy match stopped at the very first nested
`</div>` and left the old content dangling after the new line. Replaced with a proper
balanced-tag scanner (`_find_matching_close`) that counts nested opens and closes of the same tag
name, the same class of fix Run CF made to `swap_footer_person()`'s own pattern. Verified with a
direct test swap to `charity` on all four files: `david@`=0 and `Charity Taylor` present on every
one, confirmed again inside the real rep kit build below.

## Job 2: a guard so this cannot happen silently again

Two independent guards, both live now:

1. **`check_footer_no_support_leak()`** (`build_command.py`): runs on every inlined tool's raw
   source inside `build_entries()`, and again inside `build_rep_footer_swapped_set()` before any
   swap. Hard fails, naming the file, if any `a1-footer-person` element's content contains
   `support@` (the exact Run CG regression Cowork fixed by hand).
2. **`catalogue_check.py`**: independently scans every `inline=True` catalogue path's raw file for
   the same defect, so a piece that somehow skipped the build path still cannot ship with it.
3. **`scan_default_person_leak()`** (`build_command.py`): the brief's actual "after any --person
   build, scan every output file" ask. Walks every file written into a rep's kit folder after a
   `--person <slug>` build and hard fails, naming the file and the line, on any leftover trace of
   the DEFAULT person's email or full name. Reads PDF text via `pypdf`, HTML/text files directly.
   Wired into the new `build_rep_everything()` so it runs once, automatically, at the end of every
   rep-kit build.

**Guard output on the final build** (after the fix below):

```
Job 2 guard: clean, zero david@atlasonesolutions.com / David Taylor leaks under
/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/
2. Atlas 1 Solutions Marketing/A1_Sales/_Rep Kits/Charity Taylor
```

The guard caught one real, expected finding on its first run: the Employee Benefits Menu's
`CONFIG.cs` sub-object (a separate, toggle-gated CORNERSTONE PEO partner contact, already reviewed
and allowlisted for the forbidden-term guard as "nothing renders unless clicked") also names David
Taylor. That is a different business relationship than the Atlas One person line Job 1 fixed
(`CONFIG.a1`), not a leak of the same kind. Added one narrowly scoped allowlist entry (exact
filename plus the exact phrase "Cornerstone PEO") to `scan_default_person_leak()` so it still hard
fails on any OTHER appearance of David's name. Reran clean, output above.

`catalogue_check.py` also passes clean: `OK, 206 entries, all paths resolve, 17 present.py ids all
present, zero a1-footer-person/support@ leaks.`

## Job 3: one command builds a rep's whole folder

`build_command.py --person <slug> "<Master_Kit>"` now calls a new `build_rep_everything()`, which:

1. Moves any existing rep folder to `_to_delete/superseded-2026-09-22/charity-kit-before-CH/`
   (never overwrites an existing backup: a same-day rerun gets `-2`, `-3`, ... instead -- found and
   fixed after the first attempt below would otherwise have clobbered the real Run CF/CG backup
   with its own guard-failed output).
2. Keeps `READ ME FIRST.txt` as is.
3. Builds the Sales Kit file (`build_rep_kit`, unchanged), the Division Sheets (six, new
   `DIVISION_SHEETS_REP` list), the One Pagers (five, new `ONE_PAGERS_REP` list), the Sales Pieces
   (eight, existing `SALES_PIECES`), and the Price List (one, new `PRICE_LIST_REP` list, answering
   Run CG's own Question 3: yes) -- all through one shared `build_rep_footer_swapped_set()` helper,
   HTML and PDF each.
4. Runs Job 2's `scan_default_person_leak()` guard once over the whole finished folder.

Ran for Charity: `python3 build_command.py --person charity "<Master_Kit>"`. First run's guard
caught the Job 2 finding above (fixed, see Job 2); second run completed clean.

**Per file table, Charity's whole folder** (41 files: 20 pieces, HTML + PDF each, one HTML-only
Sales Kit):

| File | david@ | Charity Taylor | 385-213-7177 | dash |
|---|---|---|---|---|
| Atlas One Sales Kit (Charity Taylor).html | 0 | 3 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Benefits_Retirement.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Benefits_Retirement.pdf | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Business_Consulting.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Business_Consulting.pdf | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Financial_Services.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Financial_Services.pdf | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Payroll_HR.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Payroll_HR.pdf | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Risk_Insurance.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Risk_Insurance.pdf | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Technology_Operations.html | 0 | 1 | 0 | 0 |
| Division Sheets/Atlas_One_Division_Technology_Operations.pdf | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_AI_Email_Assistant_OnePager.html | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_AI_Email_Assistant_OnePager.pdf | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_AI_Task_Agent_OnePager.html | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_AI_Task_Agent_OnePager.pdf | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Background_Screening_OnePager.html | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Background_Screening_OnePager.pdf | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Microsoft_365_OnePager.html | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Microsoft_365_OnePager.pdf | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Software_and_Licenses_OnePager.html | 0 | 1 | 0 | 0 |
| One Pagers/Atlas_One_Software_and_Licenses_OnePager.pdf | 0 | 1 | 0 | 0 |
| Price List/Atlas_One_Price_List.html | 0 | 1 | 0 | 0 |
| Price List/Atlas_One_Price_List.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Bookkeeping_Marketing_Sheet_V8.html | 0 | 2 | 0 | 0 |
| Sales Pieces/Atlas_One_Bookkeeping_Marketing_Sheet_V8.pdf | 0 | 2 | 0 | 0 |
| Sales Pieces/Atlas_One_Employee_Benefits_Menu.html | 0 | 3 | 0 | 0 |
| Sales Pieces/Atlas_One_Employee_Benefits_Menu.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Everything_We_Handle.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Everything_We_Handle.pdf | 0 | 0 | 0 | 0 |
| Sales Pieces/Atlas_One_Membership_Brochure.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Membership_Brochure.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Membership_Pricing.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Membership_Pricing.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Proof_Sheet.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Proof_Sheet.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_QuickBooks_Accountant_Access_Guide.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_QuickBooks_Accountant_Access_Guide.pdf | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Services_Overview.html | 0 | 1 | 0 | 0 |
| Sales Pieces/Atlas_One_Services_Overview.pdf | 0 | 1 | 0 | 0 |

`Everything We Handle.pdf` shows 0 for "Charity Taylor" because it is the one `public=True` piece
(no name or email shown by design, matching Run CG's own rule for public pages); its HTML shows 1
because the person's first name appears in the "Book 15 minutes with Charity" booking-link text --
except Charity has no booking link yet (see Assumption 2 below), so that specific link renders
empty.

## Job 4: Hire date is employee rows only

`census/index.html` (repo and Master Kit master, byte identical, confirmed by diff): Hire date's
input now gets the same `disabled` treatment as Employee status, Position, Pay type and Salary on
a Spouse or Child row, both in `renderRow()` (the `isDep` branch) and in `rowData()` (the `dep`
branch, so an imported CSV/Excel value on a dependent row is dropped on export the same way the
other four fields already are). Instructions text (the inline paragraph and the downloadable
Excel/CSV instructions tab) now lists Hire date under "Employee rows only, leave blank on a
Spouse/Child row" instead of under "optional, leave blank if you don't have it". This answers Run
CG's own Question 1: yes, Employee rows only.

`node --check` passed on all four embedded script blocks. Playwright verified at 1440 and 390
(jumped straight to the Census step panel, the same panel a real user reaches after completing
steps 1 to 3): added a Spouse row and a Child row, both show Hire date disabled while the Employee
row's stays enabled; `scrollWidth` equals viewport at both widths; zero console errors. Synced the
finished repo file onto the Master Kit master copy (diff confirms byte identical). Pushed to the
repo, commit `6c4c867` ("Run CH: Job 4, census Hire date greys out on dependent rows").

## Job 5: rebuild and verify

`catalogue_check.py`: `OK, 206 entries, all paths resolve, 17 present.py ids all present, zero
a1-footer-person/support@ leaks.` Rebuilt COMMAND (206 items, 57.7MB, Present decks 1.87MB) and the
shared Sales Kit (58 items, 27.0MB) with the default person; both inline the three pieces Cowork
hand fixed earlier in this chat (AI Task Agent, AI Email Assistant, Client Dashboard GHL) plus
every Job 1 fix from this run, clean.

Playwright verified COMMAND and Charity's rebuilt Sales Kit at 1440, 1024 and 390: every zone tab
opened and scrolled to bottom (COMMAND: Sales Kit, Tools, Internal, Present; Charity's kit: Sales
Kit, Tools -- it never carries Internal or Present, by construction). `scrollWidth` equals viewport
at all three widths on both files, zero console errors throughout. Deployed nothing.

## Screenshots

- `_briefs/assets/run-CH-jobs/shots/census-hiredate-1440.png`
- `_briefs/assets/run-CH-jobs/shots/census-hiredate-390.png`
- `_briefs/assets/run-CH-jobs/shots/COMMAND-1440.png`
- `_briefs/assets/run-CH-jobs/shots/COMMAND-1024.png`
- `_briefs/assets/run-CH-jobs/shots/COMMAND-390.png`
- `_briefs/assets/run-CH-jobs/shots/CharitySalesKit-1440.png`
- `_briefs/assets/run-CH-jobs/shots/CharitySalesKit-1024.png`
- `_briefs/assets/run-CH-jobs/shots/CharitySalesKit-390.png`

## Assumptions

1. **`a1-contact-person` layout names are per file, not generic.** The brief asks for "a second
   contract class" without specifying its shape. Since the three markup files use genuinely
   different layouts (two lines with no name; name/title/phone/email on one line each; a name row
   plus three labeled rows), gave each its own `data-a1-kind` value and generator rather than
   forcing one shared template that would have broken at least two of the three visually.
2. **CONFIG.a1's booking fields (`book15`/`book30`) go empty, not David's own link, for a person
   with no booking link of their own.** Charity's `people.json` entry has `booking: null` today.
   Leaving David's calendar link in place for Charity would double book his calendar under her
   name; an empty string disables the link cleanly on the page's own JS. `Everything We Handle`'s
   booking link text is empty for the same reason (`people.py`'s public-line renderer already
   skips the booking link entirely when a person has none). See Question 1 below.
3. **The `CONFIG.cs` (Cornerstone PEO) sub-object in the Employee Benefits Menu was left untouched
   for Charity's kit**, still naming David as the Cornerstone PEO partner. That is David's own,
   separate business relationship with a different brand, not an Atlas One contact line Job 1's
   scope covers, and it sits behind a toggle that never renders unless clicked (already reviewed
   and allowlisted for the forbidden-term guard on the same reasoning). Allowlisted this one exact
   phrase in the new `scan_default_person_leak()` guard rather than either leaving the guard
   trippable forever or silently reassigning David's Cornerstone relationship to Charity.
4. **The rep-kit backup collision fix (numbered `-2`, `-3`, ... destinations) is new,
   not something the brief asked for by name**, but follows directly from brief rule 5 (never drop
   a record silently) once the first build attempt's own guard failure exposed that the original
   one-shot `shutil.rmtree()` would have destroyed the real Run CF/CG backup on any retry.

## Skipped

Nothing in the brief was skipped.

## Questions for David

1. **Charity's booking link.** She has no GoHighLevel booking link yet (`people.json`:
   `"booking": null`). Once GHL is set up for her (the GHL terminal's own job, not this one), her
   `people.json` entry should get a real link so `book15`/`book30` and the Sales Pieces' booking
   text stop rendering empty in her kit. Worth a rebuild the day that lands.
2. **The Cornerstone PEO toggle on the Employee Benefits Menu, in a rep's kit.** Right now every
   rep's copy of this piece still carries the David/Cornerstone toggle option (Assumption 3), even
   though only David has that relationship. Should a non-default person's kit drop that toggle
   entirely, or is it fine as a hidden option nobody but David would ever click?
3. **Client Portal's `.poc` block title, for a rep.** The swap now renders a rep's `people.json`
   title there (e.g. Charity's "Business Advisor") rather than keeping David's own "Founder &
   President" wording, matching the approach used for the Bookkeeping header. Confirm that is the
   right call for every future rep, not just Charity.
