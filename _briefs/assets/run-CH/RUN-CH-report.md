# RUN-CH report (link cleanup: 26 fixed templates pasted live, plus the orphan template)

First line: all 27 templates are fixed and verified live -- the orphan "Thank you, and the one link that gets your business set up" email (Job 0, captured to disk for the first time), plus the 26 already-fixed files from `cadence-emails-2026-09-13/` (Jobs 1-26). Every fallback anchor that used to show the raw URL, or the raw `{{appointment.meeting_location}}` merge tag, as its visible link text now shows a short phrase instead. Job 27 fetched all 27 live bodies back through the same Firebase Storage network response used in prior verify runs and diffed each one against its disk master file: all 27 came back clean, with the only differences being GHL's own automatic Outlook-compatibility injections added on every save (see Assumptions). No sends were made and no workflow was published or unpublished at any point in this run.

## Job 0: the orphan template, "A1 | Welcome | new-client-welcome"

1. Opened the template (id `6aa9de78b1a9b275e36afccc`) and captured the live body verbatim via the Firebase Storage `index.html` network response (more reliable than reading the virtualized Monaco code editor's DOM directly, which only renders the visible viewport of lines). Saved unmodified to `cadence-emails-2026-09-13/new-client-welcome.html` -- this is now the master source file this template should have had from the start.
2. Found five raw-URL-as-text anchors, one more than the four the brief named from Run BA's build log: the PEO quote form, the census tool, the "see everything Atlas One handles" page, a second anchor to that same what-we-do page inside the membership paragraph (the un-named fifth), and the booking link.
3. Fixed each one, matching the file's own existing nearby text for the same destination where it existed:
   - PEO quote form -> "Open the quote form" (matches the convention already live in email-1.html and send-peo-form.html)
   - Census tool -> "Open the census tool"
   - Both what-we-do anchors -> "one page, no form" (this file's own existing footer text for that exact href)
   - Booking link -> "Book time with me" (this file's own existing footer text for that exact href)
4. Pasted the fixed HTML back via the in-editor source panel, saved, did a full page reload (root -> Marketing > Emails > Templates > search > reopen), and diffed the live body against disk: clean except Monaco's own auto-indent whitespace.
5. Searched three terms (welcome, practice, set up) across all templates: no second "practice set up" variant exists. new-client-welcome is the only orphan of its kind.
6. Added a row to `cadence-emails-2026-09-13/INDEX.md`'s first table so this file is never an orphan again.

## Jobs 1-26: paste each already-fixed file into its live template

Every row below: template id confirmed live before pasting, matched the brief's table (26 for 26, zero drift). File pasted via `browser_type` directly into the in-editor source panel (never the OS clipboard, see Assumptions), preview checked for the fixed link text before saving, Saved confirmation banner read back after saving.

| # | File | Template name | Id match | Fixed link text (fallback anchor) |
|---|---|---|---|---|
| 1 | b-1.html | A1 \| B-1 \| b-1 | yes | Book a few minutes |
| 2 | b-2.html | A1 \| B-2 \| b-2 | yes | Run your numbers |
| 3 | b-3.html | A1 \| B-3 \| b-3 | yes | Book a few minutes |
| 4 | b-4.html | A1 \| B-4 \| b-4 | yes | Book a few minutes |
| 5 | booking-c1.html | A1 \| C1 \| booking-c1 | yes | Join the Zoom meeting |
| 6 | booking-cancelled.html | A1 \| Cancelled \| booking-cancelled | yes | Pick a new time |
| 7 | booking-no-show.html | A1 \| No show \| booking-no-show | yes | Pick a new time |
| 8 | booking-reminder-1h.html | A1 \| 1 hour reminder \| booking-reminder-1h | yes | Join the Zoom meeting |
| 9 | booking-reminder-24h.html | A1 \| 24 hour reminder \| booking-reminder-24h | yes | Join the Zoom meeting |
| 10 | bq-1.html | A1 \| BQ-1 \| bq-1 | yes | Book a few minutes |
| 11 | bye-1.html | A1 \| BYE-1 \| bye-1 | yes | Book a few minutes |
| 12 | bye-2.html | A1 \| BYE-2 \| bye-2 | yes | Book a few minutes |
| 13 | e0.html | A1 \| E0 \| e0 | yes | Book a few minutes |
| 14 | email-1.html | A1 \| Email-1 \| email-1 | yes | Open the quote form |
| 15 | email-2.html | A1 \| Email-2 \| email-2 | yes | Open the quote form |
| 16 | lt-1.html | A1 \| LT-1 \| lt-1 | yes | Book ten minutes |
| 17 | lt-2.html | A1 \| LT-2 \| lt-2 | yes | Book a 30 minute look at yours |
| 18 | lt-3.html | A1 \| LT-3 \| lt-3 | yes | Book ten minutes |
| 19 | lt-4.html | A1 \| LT-4 \| lt-4 | yes | Run your numbers |
| 20 | q-1.html | A1 \| Q-1 \| q-1 | yes | Book fifteen minutes |
| 21 | send-bookkeeping-form.html | A1 \| Email 2B (bookkeeping form) \| send-bookkeeping-form | yes | Open the bookkeeping form |
| 22 | send-peo-form.html | A1 \| Email 2 (PEO form) \| send-peo-form | yes | Open the quote form |
| 23 | tool-lead-nurture-1.html | A1 \| Email 5A \| tool-lead-nurture-1 | yes | Grab 15 minutes |
| 24 | tool-lead-nurture-2.html | A1 \| Email 5B \| tool-lead-nurture-2 | yes | Pick a time |
| 25 | ye-1.html | A1 \| YE-1 \| ye-1 | yes | Book a few minutes |
| 26 | ye-3.html | A1 \| YE-3 \| ye-3 | yes | Book fifteen minutes |

Booking-c1 and both booking-reminder templates carry the `{{appointment.meeting_location}}` merge tag -- this is the exact defect David originally flagged (the Zoom link in the booking confirmation email showing as a raw URL once GHL fills in the merge tag). All three now show "Join the Zoom meeting" for both the button and the fallback anchor.

## Job 27: verify all 27 templates

Fetched the live saved body of every one of the 27 templates (Job 0 plus Jobs 1-26) via the Firebase Storage `index.html` network response and diffed whitespace-insensitively against the corresponding disk master file. **All 27 came back clean.** The only differences found anywhere were two kinds of markup GHL itself injects automatically on every save, regardless of what is typed in:

1. A `<!-- outlook-fixes-applied -->` comment added to the `<head>`.
2. An `mso-style-textfill-fill-color: #XXXXXX;` property appended to the `style` attribute of colored links (either as its own `style="mso-style-textfill-fill-color: ...;"` attribute, or appended inline to an existing `style` attribute), paired with an `<!--[if mso]><font color="..."><![endif]-->` / `<!--[if mso]></font><![endif]-->` wrapper -- an Outlook font-color fallback pattern already confirmed harmless in Job 0's own verify pass.

No real content, href, or visible-link-text difference was found on any of the 27 templates.

## P- template spot check (read only, nothing changed)

Per the brief, spot-checked 3 of the 21 older P- prospecting templates (from the 2026-09-08 build, never saved to disk) through the source editor after Job 27:

- **P-A-1** (Referral Email 1, id `6aa0a8409256eb9f6cb6b7b7`): no raw-URL-as-text pattern -- the template has a single button link with no fallback line at all.
- **P-W7-3** (WSA Email 3, id `6aa0a9fb6ec737a976fa481f`): no raw-URL-as-text pattern -- the only link uses "Book 30 minutes" as its visible text.
- **P-MEMBER-WELCOME** (id `6aa37036a813792f409bf1a9`): no raw-URL-as-text pattern -- uses "grab a slot on my calendar here" as visible text.

None of the three spot-checked templates carry this run's specific defect. This is not a clearance of all 21 -- a full audit of the remaining 18 is still its own future run if David wants one.

Two unrelated defects surfaced during the spot check and are flagged here rather than fixed (out of scope for this run):

- **P-W7-3 names a vendor to a client.** The signature reads "PEO Partner & Business Consultant, Cornerstone PEO" with a reply address of `david.taylor@cornerstonepeo.com`. The project rule is that client-facing everything is "Atlas One," never naming a vendor or PEO brand -- this template breaks that rule directly in its signature block.
- **P-MEMBER-WELCOME uses "here" as link text.** "Grab a slot on my calendar here" -- the same link-text convention already being enforced across the 26 files fixed in this run (no "here," no raw URL, a short descriptive phrase) is not applied to this template.

## Assumptions

1. **The two "what-we-do" anchors in new-client-welcome both got the phrase "one page, no form."** The file's own footer already uses that exact phrase for that exact href (`https://forms.atlasonesolutions.com/tools/what-we-do/`), so reusing it satisfied the brief's own priority rule ("matching this file's own nearby button text where one exists for the same destination") more directly than inventing a new phrase like "see everything Atlas One handles" for one or both occurrences.
2. **Clipboard collision, found and worked around.** Early in Job 0, this session used the OS clipboard (Cmd+V) to paste, and a concurrent GHL-JOBS terminal running on the same Mac silently overwrote the shared macOS clipboard mid-paste -- the template briefly had a stray line of unrelated chat text pasted into it. Caught immediately via the live preview before saving, cleared, and never saved. From that point on, every paste in this run used `browser_type` directly into the editor field (Playwright's `.fill()`, which sets the field value without touching the OS clipboard), never Cmd+V.
3. **A second stray-text bug, root-caused and fixed.** Immediately after the clipboard incident, one attempt to retype left a literal `<!doctype html>` string visible as body text in the preview. Root cause: the prior clear (select-all + delete) had not actually emptied the editor before the retype began. Fix: always do an explicit select-all + delete, confirm via a snapshot that the editor shows just line "1" and the preview iframe is empty, before typing the replacement content. This sequence was used for every one of the following 26 pastes with no repeat of either bug.
4. **Per-job verification strategy.** Jobs 1-26 were verified in-session via the live preview iframe (confirming the fixed link text appears with no raw URL, immediately before saving) rather than a full page reload after every single paste. The complete reload-and-diff-against-disk verification (the strictest form, matching rule 23's own standard) was done for all 27 templates together as Job 27, exactly as the brief's own Job 27 already asked for -- this avoided 26 redundant full-navigation round trips through the SPA while still getting every template that same rigorous check before the run closed out.
5. **Template ids matched the brief's table for all 26 Job rows, zero drift.** The brief warned this table can go stale (it happened to six P-templates in Run BK); it did not happen here.
6. **The `<!-- outlook-fixes-applied -->` comment and the `mso-style-textfill-fill-color` / `<!--[if mso]>` markup are GHL's own automatic injections, not paste artifacts.** Confirmed because they appear identically whether the pasted HTML included them or not (the disk master files use plain `style="color:#XXXXXX;"` with no mso markup at all, yet the live saved bodies always carry this markup after any save) -- same conclusion Run BO and Run BR reached doing this exact kind of diff.

## What this run did not cover, on purpose

The remaining 18 of the 21 P- prospecting templates were not opened. Three were spot-checked and came back clean of this run's specific defect, but that is not the same as a full audit, and two unrelated defects (vendor name in a signature, "here" as link text) turned up in the three that were checked -- worth treating as a signal that a full P- template audit is its own worthwhile future run.

## Questions for David

1. **Full P- template audit?** The 3-template spot check came back clean of the raw-URL defect this run targeted, but surfaced two other defects (a vendor name leak in P-W7-3's signature, "here" as link text in P-MEMBER-WELCOME) in templates that were never saved to disk and so were never covered by any prior audit. Worth its own run to check all 21?
2. **P-W7-3's vendor-name leak** ("PEO Partner & Business Consultant, Cornerstone PEO" signature, `cornerstonepeo.com` reply address) is a live template wired into a prospecting workflow. Want this queued as a priority fix ahead of a full P- audit, given it directly breaks the never-name-a-vendor rule on every send?
