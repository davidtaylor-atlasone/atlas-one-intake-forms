# BRIEF-AGENT (Run AG3, 2026-09-27): fix the AG2 loader, build the Salesforce loader. APPROVED BY DAVID.

Terminal: AGENT. Written by Cowork after auditing David's 10 row test (log ag2-load-log-2026-09-27.csv, contacts read
back live in GoHighLevel). **This run writes NOTHING into GoHighLevel.** Claude Code's own permission check blocks this
terminal from GHL writes, so every write command is run by David in the plain Terminal app. Your job is to make the
scripts right, prove them read only, and hand David exact one line commands.

## What the 10 row test showed (verified live by Cowork)
1. Tags, Owner (David), address, Employee Count and the note all landed. No DND was set. Good.
2. DEFECT: `companyName` is never set. AAMCOR's new contact is Digna Gittins with no company on the record.
3. DEFECT: rows with no named contact (5G Hearing LLC, 24 Hour Express, and every "company phone only" row) were
   created with no first name, no last name and no company. The contact is a bare phone number. Emails would print "Hi ,".
4. DEFECT: David ran dryrun10 twice and every one of the 10 contacts now has TWO identical notes titled
   "Book of business import 2026-09". The note step is not idempotent and dryrun10 ignores the resume log.
5. The Cornerstone Connect notes carry FEINs in plain text (5G Hearing's note shows "FEIN # 33-18xxxxx").
6. Check, do not change: Book row "5B USA LLC" matched GHL contact Mihkel Jaatma at realeyes.ai (Real Eyes). Confirm from
   the Cornerstone export or the folders whether 5B USA LLC is Real Eyes' US legal entity. Report the answer.

## Update 2026-09-28 (Cowork, before this run started): use master book v5
- Point BOOK_PATH at `master-book-v5-2026-09-28.xlsx` (same folder, same Book columns as v4, Status now reconciled across
  Cornerstone CRM, G&A Salesforce and the folders; 61 v4 "Former Teamworks client" rows are active G&A clients, 173 v4
  "G&A Client" rows are terminated in Salesforce). Read the Status column exactly as before.
- A Book row with a value in the new column "Needs your review" also gets the tag `status-review` so David can find it.
- `sf-load-2026-09-27.json` tags were rewritten by `sf_unify.py` to agree with v5 (372 rows). Do not retag.
- 5G Hearing LLC has no contact person in the Book. Its Cornerstone note names the owners Paul Campoamor
  (paul@amhchearing.com, 352-406-1985) and Michael Rice. Use Paul Campoamor as its contact in the --fix pass.
- AAMCOR's contact Digna Gittins is correct (she is the admin David works with). Only the missing company name is wrong.

## Job 1: fix `_briefs/job_ag2_load.py` (keep every existing rule from the AG2 brief)
- Set `companyName` from the Book's Company on create, and on update when the GHL field is blank.
- No named contact: create with companyName only (no invented first name), tag `no-contact-name` added.
- Notes idempotent: before adding, GET the contact's notes; if any note has the same title, skip. Same rule in every mode.
- Mask FEIN and SSN shapes in every note body before sending (`\b\d{2}-?\d{7}\b` near FEIN/EIN/Tax ID becomes
  `XX-XXX` plus the last four; `\b\d{3}-\d{2}-\d{4}\b` becomes `XXX-XX-` plus the last four).
- Every mode (dryrun10 and all) reads the resume log and never reprocesses an `ok` row unless `--fix` is passed.
  `--fix` is the mode that reruns the 10 test rows to fill companyName.
- New mode `plan N`: read only, prints what it WOULD do for N rows (search result, create or update, fields, tags,
  note length) and writes nothing. Run `plan 40` yourself and put the output in the report.

## Job 2: new `_briefs/job_ag3_sf_load.py` (Salesforce load)
Input is Cowork's prepared file, do not rebuild it:
`Master_Kit/_INTERNAL (do not share)/Book of Business/sf-load-2026-09-27.json` (7,747 rows, 4,387 accounts;
built by `sf_build_load.py` beside it). Each row already carries firstName, lastName, email, phone, title, companyName,
address1, city, state, postalCode, website, employees, tags, dndEmail, note (only on the account's main row), label.
- Reuse Job 1's functions (import them, do not copy). Same rules: search by email; search by phone ONLY when the row has
  no email; create or fill blanks only; tags add only; assign to David; Employee Count custom field; one note per
  account titled "G&A Salesforce import 2026-09", idempotent; resumable log `sf-load-log-2026-09-27.csv`; about 4.5
  calls a second with backoff.
- `dndEmail: true` (354 people who unsubscribed from email in Salesforce): set DND on the EMAIL channel only
  (`dndSettings.Email.status = active`), nothing else. This is David's approved exception: these people asked not to be
  emailed, and emailing them is the fastest way into spam. Every other contact: no DND anywhere, ever.
- Never set Lead Source "Website Tool/Calculator", Lead Lane, Trigger Date or Type, WC or Benefits Renewal Date, Last
  Touch Date. The tags in the file are the only tags.
- Modes: `plan N` (read only), `test20` (20 rows: 5 Client, 5 book-sf-touched, 5 book-sf-intent, 5 with dndEmail),
  `all`.

## Job 3: `_briefs/job_ag2_dedupe_notes.py`
Lists every contact whose notes contain more than one note with the title "Book of business import 2026-09" or
"G&A Salesforce import 2026-09". Default is list only. `--apply` deletes only the newer duplicate(s), keeps the oldest,
never touches any other note. David runs `--apply`, not you.

## Job 4: David's run sheet
Write `_INTERNAL (do not share)/Book of Business/RUN-SHEET-load-2026-09-27.md`: the exact commands, in order, each one
line, for the plain Terminal app, using `~/atlas-one-venv/bin/python` and full paths. Order: dedupe notes --apply,
AG2 --fix, AG2 all, SF test20, (Cowork checks), SF all. For each: how long it takes, what the last line looks like when
it worked, and "if it stops, run the same line again, it picks up where it left off".

## Rules
- No GHL writes from this terminal. No deletes. Commit and push the scripts and report (push may be refused by the
  permission check; if so say so and leave it committed).
- Report: `RUN-AGENT-report.md` with the plan 40 output, the 5B USA answer, anything you assumed, questions at the end.
