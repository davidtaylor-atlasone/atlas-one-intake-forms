# BRIEF-GHL-JOBS (current run: Run CH, 2026-09-22). Finish Charity's kit for real, one command per rep, two guards, Hire date.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run. No sends, no deploy beyond pushing the intake forms repo, no spending. Deleting is a move into
`_to_delete/superseded-2026-09-22/`. No dashes in anything a client or prospect reads. Log to
`_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with `_BUILD-LOG/RUN-GHL-JOBS-report.md`. No time limit;
commit after each job. Screenshots to `_briefs/assets/run-CH-jobs/` (this run's own folder).

Run CG was audited by Cowork on disk (COWORK-AUDIT-run-CG-2026-09-22.md): good work, two defects, both below.
Run CG's three questions are answered below as jobs. Do not re ask them.

## What Cowork already fixed in this chat (do not redo, do not undo)

Run CG's david@ to support@ sweep also rewrote the PERSON line on three sales pieces, so they read
"David Taylor, Founder · Support@AtlasOneSolutions.com". Cowork put david@atlasonesolutions.com back inside the
`a1-footer-person` element only, on: AI Task Agent one pager, AI Email Assistant one pager, Client Dashboard GHL.
Originals are in `_to_delete/superseded-2026-09-22/pre-person-line-fix/`. The company line and tool contact
lines stay support@. Rule going forward: a person line carries that person's own email; support@ lives on the
company line and in tool contact lines, never inside `a1-footer-person`.

## Job 1: David's details outside the footer on Charity's copies

Run CG reported david@ = 0 on Charity's Sales Pieces. Cowork counted on disk: three still carry David:
- Bookkeeping Marketing Sheet V8: the header `.meta` block ("David Taylor, President and Founder ...
  David@AtlasOneSolutions.com").
- Services Overview: the header band contact ("380-CALL-A1S ... David@AtlasOneSolutions.com").
- Employee Benefits Menu: the page's CONFIG object (`email:"David@AtlasOneSolutions.com"`), which renders
  somewhere on the page.
Every person contact that appears OUTSIDE the footer on a sales piece gets a second contract class,
`a1-contact-person` (or, for a CONFIG object, a value `swap_footer_person()` knows to replace), and the swap
handles both. Check every Step 1 piece and the eight Sales Pieces for the same pattern, not only these three.
In David's own masters those header lines stay David; make the Bookkeeping header title read "Founder" to match
people.json.

## Job 2: a guard so this cannot happen silently again

After any `--person <slug>` build, scan every output file (HTML, and the text of every PDF) for the default
person's email and full name. Any hit is a hard failure naming the file and the line. Also add to
`catalogue_check.py` (or the build): any `a1-footer-person` element that contains `support@` fails the build.

## Job 3: one command builds a rep's whole folder (Run CG question 2: yes)

`build_command.py --person <slug> "<Master_Kit>"` rebuilds everything the rep gets, in one go, into
`A1_Sales/_Rep Kits/<Person Name>/`: the Sales Kit file, Division Sheets (six), One Pagers (the five Run CF
built), Sales Pieces (the eight Run CG built) and the Price List (Run CG question 3: yes, it is client facing
now). HTML and PDF each. Delete nothing by hand: the old folder contents are replaced by the rebuild, the
previous copies moved to `_to_delete/superseded-2026-09-22/charity-kit-before-CH/`. Keep READ ME FIRST.txt.
Run it for charity. Report per file: david@ count, Charity Taylor count, 385-213-7177 count, dashes. Every
david@ must be 0, including inside every PDF's text.

## Job 4: Hire date is employee rows only (Run CG question 1: yes)

In the census tool (master and repo copy, kept byte identical), Hire date greys out on Spouse and Child rows
like columns 10 to 13, and the templates' instructions say so. Retest at 1440 and 390, push the repo.

## Job 5: rebuild and verify

`catalogue_check.py`, rebuild COMMAND and the shared Sales Kit (they inline the three pieces Cowork fixed),
then `--person charity`. Headless Chromium at 1440, 1024 and 390 on COMMAND and Charity's Sales Kit, zero
console errors, every zone scrolls. Deploy nothing.

## Not in this run
LTD row on the benefits menu (waiting on David's broker). Charity's GoHighLevel signatures and reply to (GHL
terminal). Charity's Microsoft 365 mailbox (David).

## Report must include
The per file table for Charity's whole folder, the guard's output on the final build, screenshot list,
questions batched at the end.
