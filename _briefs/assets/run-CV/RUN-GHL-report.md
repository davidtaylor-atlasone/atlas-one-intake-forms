# RUN-GHL report, Run CV (2026-09-30 into 2026-10-01)

**NEEDS CHROME RESTART.** The GoHighLevel Workflows list stopped responding mid run: clicks (page 5 of the list) and typing (the search box) did nothing, the page showed only a spinner, and one Cmd+R reload did not fix it. Per the dead UI rule the run stopped there. Everything that only needs the API is done. Everything that needs the GHL screens is not done and is listed under Skipped. After a Chrome restart, run `/run-ghl` again; the brief is already in `_BUILD-LOG/BRIEF-GHL.md`.

## Built

### Step 0 (read only): PASS
David (Settings, Users, David Taylor, Notification settings) and Charity Taylor: every section expanded, 18 of 18 Email boxes OFF for each user (In-App on, SMS off). Nothing was clicked or saved. Because the Email boxes are off, the bulk steps were allowed to run.
Shots: `_briefs/assets/run-CV/shots/step0-david-notifications.jpg`, `step0-charity-notifications.jpg`.
Note: this account labels the screen "Users" (Settings, Users), not "My Staff".

### Job 1: owner identity in the templates (done through the HighLevel API)
Searched all 70 live templates (69 fetched; "Default - Invoice received" is a builder template and has no owner text). 36 had David hard coded. 33 were fixed and pushed. 3 were deliberately left alone (see Assumption 2). Each push was read back from the live preview URL and diffed against the disk copy: all 33 MATCH, zero "David Taylor" left in any of them.

What changed in each: the signature name `David Taylor` became `{{user.name}}`, `David@AtlasOneSolutions.com` (link and text) became `{{user.email}}`, the sign off `David` became `{{user.first_name}}`, and in the booking emails the title "your call with David" and "You're booked with David" and in the portal email "David added a document" now use `{{user.first_name}}`. Same merge fields as the Run CM 35. Phone 380-225-5217 and the Book time with me link were left as they were (as in Run CM).

| Template | ID | Saved (UTC) |
|---|---|---|
| P-C-0 Instant reply | 6aa0c1de55d1ce8973c2a813 | 2026-10-01T05:21:00Z |
| P-MEMBER-WELCOME | 6aa37036a813792f409bf1a9 | 2026-10-01T05:21:48Z |
| P-BUILDER-DELIVERY | 6aa370697919774ef2ed8f30 | 2026-10-01T05:21:49Z |
| P-PAY-FAILED | 6aa371c107aac9f9aa6a4e75 | 2026-10-01T05:21:50Z |
| A1 | Email-1 | 6aa9c89bbbf4cb7988c03afd | 2026-10-01T05:22:21Z |
| A1 | Email-2 | 6aa9c89db1a9b275e36982ac | 2026-10-01T05:23:02Z |
| A1 | LT-1 | 6aa9c8a096b1ac2874f591ac | 2026-10-01T05:23:03Z |
| A1 | LT-2 | 6aa9c8a19ed784b5df8c500a | 2026-10-01T05:24:51Z |
| A1 | LT-3 | 6aa9c8a3b40c9f3a4ff410a8 | 2026-10-01T05:24:52Z |
| A1 | LT-4 | 6aa9c8a4b40c9f3a4ff410c2 | 2026-10-01T05:24:53Z |
| A1 | LT-5 | 6aa9c8a6bbf4cb7988c03b94 | 2026-10-01T05:24:54Z |
| A1 | Q-1 | 6aa9c8a93029d837f98fd141 | 2026-10-01T05:24:55Z |
| A1 | YE-1 | 6aa9c8abb1a9b275e369839b | 2026-10-01T05:24:56Z |
| A1 | YE-3 | 6aa9c8ac7919774ef2688437 | 2026-10-01T05:26:27Z |
| A1 | B-1 | 6aa9c8ae94dd61786846a646 | 2026-10-01T05:26:28Z |
| A1 | B-2 | 6aa9c8b00bbbc34b5ea9c48f | 2026-10-01T05:26:29Z |
| A1 | B-3 | 6aa9c8b1b40c9f3a4ff411ed | 2026-10-01T05:26:30Z |
| A1 | B-4 | 6aa9c8b33029d837f98fd1b2 | 2026-10-01T05:26:31Z |
| A1 | BQ-1 | 6aa9c8b43029d837f98fd1c5 | 2026-10-01T05:27:58Z |
| A1 | BYE-1 | 6aa9c8b67919774ef26884d4 | 2026-10-01T05:27:59Z |
| A1 | BYE-2 | 6aa9c8b807aac9f9aae4fa66 | 2026-10-01T05:28:00Z |
| A1 | C1 | 6aa9c8bd8fc016e650847ba5 | 2026-10-01T05:28:01Z |
| A1 | C2 | 6aa9c8c15893810abc0c7689 | 2026-10-01T05:28:02Z |
| A1 | C3 | 6aa9c8c37919774ef26885e7 | 2026-10-01T05:29:25Z |
| A1 | 24h reminder | 6aa9c8be96b1ac2874f59462 | 2026-10-01T05:29:26Z |
| A1 | 1h reminder | 6aa9c8c096b1ac2874f5947e | 2026-10-01T05:29:26Z |
| A1 | Cancelled | 6aa9c8c57919774ef268860d | 2026-10-01T05:29:27Z |
| A1 | No show | 6aa9c8c707aac9f9aae4fb90 | 2026-10-01T05:29:28Z |
| A1 | Email 2 (PEO form) send-peo-form | 6aa9c8cab40c9f3a4ff413f7 | 2026-10-01T05:30:41Z |
| A1 | Portal doc-ready | 6aacceeb9ed784b5dfd02b80 | 2026-10-01T05:30:42Z |
| A1 | Audit prep | 6aad411ab397941922a158c5 | 2026-10-01T05:30:43Z |
| A1 | Client more we handle | 6aad97b6cbcc9427cbd4f68b | 2026-10-01T05:30:45Z |
| A1 | 45-A | 6aa9c8a896b1ac2874f5926b | 2026-10-01T05:31:24Z |

Originals (what was live before) are in `_BUILD-LOG/cv-live-backup-2026-09-30/` (one file per template, plus `PUSHED-LOG.txt`). The fixed copies are on disk in `_BUILD-LOG/cadence-emails-2026-09-13/` (same file names as before; P- templates were not on disk before and were not added). Repo copy of the log: `_briefs/assets/run-CV/templates/PUSHED-LOG.txt`.

### Job 2 (partial)
`send-peo-form` (A1 | Email 2 (PEO form)) was pulled live, given the same owner identity change and pushed back with the others (id 6aa9c8cab40c9f3a4ff413f7, saved 2026-10-01T05:30:41Z, read back MATCH).
`45-b` and `45-c` were NOT touched: they are not in the 70 templates. Their copy lives inside the Send Email actions of the "Call: not now" workflow, which can only be read and edited in the GHL screens, so it waits for the restart.

### Extra fix found on the way
`A1 | 45-A` (id 6aa9c8a896b1ac2874f5926b) was corrupted live: the HTML had a second full email pasted inside the first, cut off in the middle of an image address, and a stray internal note ("If the current 45-A body already has a completed David fills a current item sentence...") left in a comment. I rebuilt it clean on the standard wrapper with the same words and the owner merge fields, pushed it and read it back (MATCH). Disk copy: `cadence-emails-2026-09-13/45-a.html`.

## Node values read back after reload
Not applicable this run: no workflow nodes were changed. The template read backs above are from the live preview URLs after each save.

## Skipped (needs the GHL screens, so waits for a Chrome restart)
- **Job 1, second half:** From `{{user.name}}, Atlas One Solutions` / `{{user.email}}` on every Send Email in "Seasonal touches 2026-27". Not done, no Send Email was opened. The templates they use are fixed, so once From is set the whole chain reads as the owner.
- **Job 2:** 45-b and 45-c (see above).
- **Job 3:** "Tech: Installed" welcome email into the branded wrapper as `A1 | Tech | installed-welcome`. Not done. The current wording lives only in the workflow action, and the superseded brief that quoted it (`_to_delete/superseded-2026-09-30/run-cn-part5-and-CO-brief/`) is not at that path in the OneDrive tree, so I could not copy the words from disk. I did not guess them.
- **Job 4:** Form A Privacy Policy and Terms links (example.com to https://forms.atlasonesolutions.com/tools/text/). Needs the form builder.
- **Job 5:** Charity's two calendars, the group, the confirmation workflow triggers, the test booking, and the three links. Not started, so there is nothing half built and nothing bookable. Nothing in David's five calendars or his group was touched. Charity's own steps (she must do these herself, a terminal never types her password): log in to app.ridethehightide.com as Charity@AtlasOneSolutions.com, click her initials (top right), Profile, then under Calendar Settings connect her Outlook (Charity@AtlasOneSolutions.com) and, if she wants video, Zoom. After that a later run switches both calendars from Phone call to Zoom.

## Assumptions
1. Replaced `David Taylor`, the David@ email and the lone `David` sign off on every template that had them, not only the names listed in the brief (the brief said search all 70), using the exact Run CM merge fields.
2. Left P-W7-1, P-W7-2 and P-W7-3 (WSA emails) unchanged. They are sent as David's Cornerstone PEO role: footer "PEO Partner & Business Consultant, Cornerstone PEO", a Cornerstone email address and phone, a Zoom scheduler link. Putting `{{user.name}}` in that footer would make Charity's name sit above David's Cornerstone details. They also name a PEO brand, which breaks the no vendor names rule if they ever reach an Atlas One client. See Question 1.
3. "Talk soon, David" style sign offs inside the booking confirmation titles were changed to `{{user.first_name}}`. That merge field resolves to the contact's assigned user, so it reads Charity only when Charity is the assigned user on her contacts (Job 5e would have tested this).
4. Pushed whole template bodies through the API (as Run CO did) and verified by diffing the live file against disk, whitespace ignored.
5. 45-A was rebuilt clean rather than patched, because the live copy was corrupted (see above).
6. Used a separate brief copy name `_briefs/BRIEF-GHL-2026-09-30-runCV.md` because `BRIEF-GHL-2026-09-30.md` already existed from an earlier run (restored from git after my first copy overwrote it).
7. Saved the live "before" HTML of all 33 pushed templates as a backup instead of deleting anything. The three P-W7 files I briefly wrote to disk by mistake were moved to `_to_delete/superseded-2026-09-30/run-cv/`.
8. Dead UI: I made one click (pagination), one typing attempt and one Cmd+R, then stopped, exactly as the rule says.

## Questions for David
1. The three WSA templates (P-W7-1, 2, 3) are your Cornerstone PEO emails, signed with your Cornerstone footer. Should they stay David only, move to another account, or be retired? They are not safe to send under Charity's name as they are.
2. Booking confirmation, reminder, cancelled and no show emails still say "Book time with me" and link to Book time with David (book-david). Charity's bookings would send her clients to your calendar. Want a Charity version of those templates, or a merge field for the booking link?
3. Several emails say "call me at 380-225-5217". Is that the right number for Charity's clients too, or should those lines use `{{user.phone}}`?
4. Where is the superseded brief with the exact "Tech: Installed" welcome words? It is not at `_to_delete/superseded-2026-09-30/run-cn-part5-and-CO-brief/` in the OneDrive tree. Drop a copy in `_BUILD-LOG` and Job 3 can finish.
5. OK for the next run to treat `{{user.first_name}}` in the booking email titles as final once the Job 5e test booking shows Charity's name?
