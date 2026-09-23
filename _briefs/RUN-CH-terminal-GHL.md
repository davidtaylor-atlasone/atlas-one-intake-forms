# BRIEF-GHL (current run: Run CH, 2026-09-22). Link cleanup: paste the 26 corrected cadence/booking/intake email files back into their live GHL templates, plus one orphan template that only exists live.

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser only, at app.ridethehightide.com, in one tab,
with the tab visible. No questions mid run. No sends, no publishing a Draft workflow, no spending. Log
to `_BUILD-LOG/TERMINAL-GHL-live.md`, finish with `_BUILD-LOG/RUN-GHL-report.md`. No time limit. Commit
after each job (repo `~/Projects/atlas-one-intake-forms`). Screenshots to `_briefs/assets/run-CH/`.

## Why this run exists

David spotted two live emails rendering the raw URL as the visible link text instead of a short
phrase: the confirmation email ("Or open this link: " followed by the bare Zoom URL) and a welcome
email with five raw URLs. Cowork audited every file in `_BUILD-LOG/cadence-emails-2026-09-13/` plus
the live template map and found the same pattern in 26 of the finished files: each one has a correct
branded button, then a plain fallback line right under it, "Or open this link: " followed by an
anchor whose visible text was the bare URL (or, on the three Zoom-meeting emails, the bare
`{{appointment.meeting_location}}` merge tag rendering as a raw URL once GHL fills it in). Cowork
already fixed all 26 files on disk directly in this chat (rather than queuing a GHL-JOBS run, since
GHL-JOBS is mid-run on Run CG right now and rule 40 says never rewrite a brief while its terminal is
running): the fallback anchor's visible text now reads the exact same short phrase as that email's own
button above it (href unchanged, span styling unchanged). Nothing else in any file changed. Diffed:
zero raw-URL-as-text anchors remain in any of the 34 finished files in that folder.

This run's only job is pushing those 26 already-fixed files into their live templates, plus finding
and fixing the one email that only exists live (never had a matching file, so it drifted).

## Rule 23 procedure, every job below

Type the email body through the `</>` source-code dialog, never the WYSIWYG. Select all existing
content in the dialog first, delete it, paste the whole file from disk, save, close the dialog with
Escape. Then reload the template (a full page reload, not just closing and reopening the panel) and
read the saved body back to confirm the paste held: an undo can silently revert a paste, and a
disabled "Saved" button right after Save can be misleading if a confirmation modal was missed
(exactly what happened building this same template the first time, see Job 0). Screenshot the
rendered preview (or the source dialog showing the new content) for each one.

## Job 0: the orphan template, "A1 | Welcome | new-client-welcome"

This template (Marketing > Emails > Templates) was built by pasting genericized copy straight into
the Vibe Editor on 2026-09-15 (Run BA Part 11) and was never saved to disk as its own file, so it is
not in the audit above and Cowork could not check or fix it from here. Wired into the "Send PEO form
on tag" workflow's "Email 2 - PEO moving forward" action. Subject "Thank you, and the one link that
gets your business set up." David read the live rendered email on 2026-09-22 and confirmed five raw
URLs.

1. Open the template, open the `</>` source dialog, and copy the current full HTML verbatim. Save it
   to `_BUILD-LOG/cadence-emails-2026-09-13/new-client-welcome.html` exactly as found, unmodified,
   before touching anything. This becomes the master source file this template should have had from
   the start, per rule 23 (build the email as a file first, never compose in the browser).
2. Find every anchor whose visible text is the raw href (a literal `http` string, or a merge tag that
   resolves to a URL) the same way Cowork found them in the 26 files above. Expect four to five: the
   PEO quote form, the census tool, the "see everything Atlas One handles" page, and the booking link
   are the ones Run BA's own build log names as included; there may be a fifth Cowork's log excerpt did
   not name.
3. Fix each one the same way: keep the href, replace the visible text with a short phrase describing
   where it goes (matching this file's own nearby button text where one exists for the same
   destination, otherwise a short phrase in the same voice as the 26 files: "book a few minutes",
   "open the quote form", "see everything Atlas One handles"). No dashes, no "here", no three-word
   fragment (project rule already in force).
4. Save the corrected HTML to the same disk path from step 1 (overwrite), then paste it into the live
   template following the rule 23 procedure above. Add one row for it to
   `_BUILD-LOG/cadence-emails-2026-09-13/INDEX.md`'s first table (Send "Email 2 (PEO form, welcome
   variant)" or similar, wired workflow "Send PEO form on tag", file `new-client-welcome.html`) so it
   is never an orphan again.
5. While the source dialog is open, also check whether a second template exists for "gets your
   practice set up" (a phrase in the same family the terminal live log mentions once, from a reply
   Joel Gould sent) -- search Templates for anything named close to "practice set up" or "welcome". If
   one exists and is different from new-client-welcome, treat it as a second Job 0 target: capture,
   audit, fix, save to disk, re-paste, add to INDEX.md. If it does not exist, note that and move on.

## Jobs 1-26: paste the fixed file into its live template

For each row: open Marketing > Emails > Templates, find the template by name, open it, follow the
rule 23 procedure with the file named, verify, screenshot, move to the next row. The file already has
the fix; do not re-edit anything else in it.

| # | File | Template name | Template id |
|---|---|---|---|
| 1 | `b-1.html` | `A1 | B-1 | b-1` | `6aa9c8ae94dd61786846a646` |
| 2 | `b-2.html` | `A1 | B-2 | b-2` | `6aa9c8b00bbbc34b5ea9c48f` |
| 3 | `b-3.html` | `A1 | B-3 | b-3` | `6aa9c8b1b40c9f3a4ff411ed` |
| 4 | `b-4.html` | `A1 | B-4 | b-4` | `6aa9c8b33029d837f98fd1b2` |
| 5 | `booking-c1.html` | `A1 | C1 | booking-c1` | `6aa9c8bd8fc016e650847ba5` |
| 6 | `booking-cancelled.html` | `A1 | Cancelled | booking-cancelled` | `6aa9c8c57919774ef268860d` |
| 7 | `booking-no-show.html` | `A1 | No show | booking-no-show` | `6aa9c8c707aac9f9aae4fb90` |
| 8 | `booking-reminder-1h.html` | `A1 | 1 hour reminder | booking-reminder-1h` | `6aa9c8c096b1ac2874f5947e` |
| 9 | `booking-reminder-24h.html` | `A1 | 24 hour reminder | booking-reminder-24h` | `6aa9c8be96b1ac2874f59462` |
| 10 | `bq-1.html` | `A1 | BQ-1 | bq-1` | `6aa9c8b43029d837f98fd1c5` |
| 11 | `bye-1.html` | `A1 | BYE-1 | bye-1` | `6aa9c8b67919774ef26884d4` |
| 12 | `bye-2.html` | `A1 | BYE-2 | bye-2` | `6aa9c8b807aac9f9aae4fa66` |
| 13 | `e0.html` | `A1 | E0 | e0` | `6aa9c89e8fc016e6508479a3` |
| 14 | `email-1.html` | `A1 | Email-1 | email-1` | `6aa9c89bbbf4cb7988c03afd` |
| 15 | `email-2.html` | `A1 | Email-2 | email-2` | `6aa9c89db1a9b275e36982ac` |
| 16 | `lt-1.html` | `A1 | LT-1 | lt-1` | `6aa9c8a096b1ac2874f591ac` |
| 17 | `lt-2.html` | `A1 | LT-2 | lt-2` | `6aa9c8a19ed784b5df8c500a` |
| 18 | `lt-3.html` | `A1 | LT-3 | lt-3` | `6aa9c8a3b40c9f3a4ff410a8` |
| 19 | `lt-4.html` | `A1 | LT-4 | lt-4` | `6aa9c8a4b40c9f3a4ff410c2` |
| 20 | `q-1.html` | `A1 | Q-1 | q-1` | `6aa9c8a93029d837f98fd141` |
| 21 | `send-bookkeeping-form.html` | `A1 | Email 2B (bookkeeping form) | send-bookkeeping-form` | `6aa9c8cb94dd61786846a92c` |
| 22 | `send-peo-form.html` | `A1 | Email 2 (PEO form) | send-peo-form` | `6aa9c8cab40c9f3a4ff413f7` |
| 23 | `tool-lead-nurture-1.html` | `A1 | Email 5A | tool-lead-nurture-1` | `6aa9c8cd94dd61786846a953` |
| 24 | `tool-lead-nurture-2.html` | `A1 | Email 5B | tool-lead-nurture-2` | `6aa9c8cf3029d837f98fd3dc` |
| 25 | `ye-1.html` | `A1 | YE-1 | ye-1` | `6aa9c8abb1a9b275e369839b` |
| 26 | `ye-3.html` | `A1 | YE-3 | ye-3` | `6aa9c8ac7919774ef2688437` |

These template ids are the ones on record in `_BUILD-LOG/email-templates-map.md` (Run AW). If the
Templates list shows a different id for any of these names when you open it, Run BK already found
that this table can drift from the live account (it happened to six P- templates); use the live id,
not this table's, and note the mismatch in the report the way Run BK did.

## Job 27: verify, all 27 templates

Fetch each of the 27 templates back through the Email Builder API (the same read-and-diff method Run
BO and Run BR used) and diff against the corresponding local file. Expect no differences except GHL's
own Outlook/mso-fixes markup, the way BO and BR found. Report any real content or link difference by
name.

## What this run does not cover, on purpose

The 21 older `P-` prospecting workflow templates (P-A-1 through P-W7-3, P-MEMBER-WELCOME,
P-PAY-FAILED, P-BUILDER-DELIVERY, from the 2026-09-08 build, listed in
`_BUILD-LOG/email-templates-map.md`) were never captured to disk as files, the way new-client-welcome
was not, so Cowork could not audit them for this same pattern without guessing. Do not assume they are
clean. If time allows after Job 27, open two or three at random through the source dialog and report
what their links look like (raw URL as text, or already a phrase); if any carry the same defect, stop
there and report it as a candidate for its own run rather than folding a 21-template job into this one.

## Report

For each of Jobs 0 through 27: done, what was found, what was pasted, the verify result. Any template
whose live id did not match this brief's table. Whether a second "practice set up" template exists.
The P- template spot check result. No sends were made and no workflow was published or unpublished at
any point in this run.
