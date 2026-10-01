# BRIEF-GHL Run CV (GHL lane, installed 2026-09-30 by Cowork, chat A1 GHL how-to 4)

Installed from `_BUILD-LOG/BRIEF-GHL-queued-next.md`, written by chat A1 GHL how-to 3 after it audited Run CN part 5
and Run CO live through the API (PASS, inbound webhook still pending). The previous brief (RESUME 5) and the queued
note are backed up in `_to_delete/superseded-2026-09-30/run-cn-part5-and-CO-brief/`. Do not redo anything from Run
CN or Run CO. The Tech: Order updates (inbound) webhook stays a draft; it waits for a real vendor sample after the
Dylan Bailey call and is NOT part of this run.

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser at app.ridethehightide.com, one visible tab, plus the
HighLevel API connector and the disk. No questions mid run; batch them at the end. Log lines as "Run CV" to
`_BUILD-LOG/TERMINAL-GHL-live.md`. Before writing the report, move the current `_BUILD-LOG/RUN-GHL-report.md`
(Run CN part 5 and Run CO) to `_to_delete/superseded-<date>/run-co-report/`, then write the new
`_BUILD-LOG/RUN-GHL-report.md`. Commit after each job, only this run's own files. Screenshots to
`_briefs/assets/run-CV/shots/`. Copy this brief to `_briefs/BRIEF-GHL-<date>.md` at the start.

## Step 0 (first action, read only)
Open Settings, My Staff, David, Notification Settings, and the same for Charity. Confirm every Email box is OFF.
Screenshot each. If any Email box is on, do not change it; skip every bulk step and put it in the questions.

## Hard stops
Never turn on any Email box in a user's Notification Settings. No sends of any kind except the one test booking in
Job 5e to the david+ address, never SMS, never the HIPAA feature, no spending. No deleting records, calendars,
forms or workflows, EXCEPT the one test booking and its test contact in Job 5e. Never change the slug, name or URL
of "Atlas One 15 Minute Intro Call" or any of David's five calendars or his group "Book time with David". Never
type anyone's password or log in as Charity. Do not touch anything for Dr. Gould (another chat owns that account).
Do not edit people.json (GHL-JOBS lane). No dashes as punctuation and no provider or distributor names in any
client facing copy.

Dead UI rule: start at app.ridethehightide.com/, navigate inside the app, one low stakes click first, one Cmd+R
retry, then stop cleanly, write the report with what is done, and put "needs Chrome restart" at the top.

## Jobs

Job 1. Owner identity, the templates Run CM never covered. These live templates still hard code "David Taylor" and
   David's email in the body (Cowork checked LT-1 live): A1 | LT-1..LT-4, A1 | YE-1, A1 | YE-3, A1 | Q-1,
   A1 | BQ-1, A1 | BYE-1, A1 | BYE-2, A1 | Email-1, A1 | Email-2, and any other template whose body has
   "David Taylor" (search all 70). Fix the disk copy in _BUILD-LOG/cadence-emails-2026-09-13/ first (same merge
   fields and signature block as the Run CM 35), then push through the API like Run CO did. Then set From
   {{user.name}}, Atlas One Solutions / {{user.email}} on every Send Email in "Seasonal touches 2026-27".
Job 2. 45-b, 45-c and send-peo-form: pull the LIVE template HTML to disk (replace the "READ FROM GHL" placeholders),
   apply the same owner identity change, push back.
Job 3. "Tech: Installed" welcome email: move it into the branded wrapper with the logo block, same as the P- templates.
   Save it as a template "A1 | Tech | installed-welcome" and point the workflow at it. Same words, no dashes, no
   provider or distributor names.
Job 4. Form A Privacy Policy and Terms links still point to example.com: set both to
   https://forms.atlasonesolutions.com/tools/text/ (same as Form D). Read back on the live widget.
Job 5. Charity's booking calendars (David, 2026-09-30). Cowork checked through the API: no Charity calendar and no
   Charity group exist yet; the only group is "Book time with David" (book-david). DO NOT edit any of David's five
   calendars or his group.
   a) Copy David's "Quick call with David" (l2imyO3hRZo34zZwXymb) settings into a NEW calendar "Quick call with
      Charity", 15 minutes, slug quick-call-with-charity, team member Charity only (her GHL user), event title
      "{{contact.first_name}} + Charity Taylor: 15 Minute Intro Call", same cover logo, same booking form
      (jnesTr2nZpXOsGddGLka), same buffers and booking window. Description: same words, written as Charity
      ("I'll bring the questions" stays). No photo.
   b) New calendar "Back Office Audit with Charity", 30 minutes, slug back-office-audit-charity, copied from
      David's "30-Minute Back-Office Audit" (mRbFII938P3HrfODYH2K), Charity only, form SHhITMEwWONx08AE4VJT,
      Atlas One logo as the cover.
   c) Meeting location: Charity's GHL user has no Zoom connected, and connecting it (or her Outlook calendar for
      conflict checking) needs HER login, which a terminal must never type. So set location to "Phone call" (the
      contact's number, Charity calls them) for now, and list in the report the exact steps Charity does herself:
      log in to app.ridethehightide.com as Charity@AtlasOneSolutions.com, click her initials (top right), Profile,
      then under Calendar Settings connect her Outlook (Charity@AtlasOneSolutions.com) and, if she wants video,
      Zoom. After that, switch both calendars to Zoom in a later run.
   d) New group "Book time with Charity", slug book-charity, both calendars in it, description "Pick the length
      that fits. New to Atlas One? Start with the 15 minute call."
   e) Confirmations: add both new calendars to the triggers of "Booking: confirm and remind" (and the cancelled,
      no show and after the call workflows if they filter by calendar) exactly as David's calendars are listed, so
      Charity's bookings get the same branded emails. Those emails already send as {{user.name}} after Job 6;
      confirm the appointment owner is Charity so the sender reads Charity. Test ONE booking on the quick call as
      "Charity Test", david+charitycal-test@atlasonesolutions.com, check the confirmation shows Charity's name,
      then cancel it and delete the test contact (test leftover).
   f) Report the two booking links and the group link on their own lines:
      https://api.leadconnectorhq.com/widget/bookings/quick-call-with-charity
      https://api.leadconnectorhq.com/widget/bookings/back-office-audit-charity
      https://api.leadconnectorhq.com/widget/groups/book-charity
      (read them back from the live calendars, do not just copy these). Do NOT edit people.json (it belongs to
      the GHL-JOBS lane); Cowork hands the group link to that lane for Charity's kit.

## Report must include
Step 0 result with shots. Job 1: every template changed (name, id, saved time) and every Seasonal touches Send Email
with its new From. Job 2: the three live templates pulled, changed and pushed. Job 3: new template id and the workflow
action now pointing at it. Job 4: Form A links read back from the live widget. Job 5: both calendar ids, the group id,
the three links read back live on their own lines, the workflows whose triggers changed, the test booking result
(sender name shown) and proof the test booking and contact were removed, and Charity's own steps in plain words.
Questions batched at the end.
