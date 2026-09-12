# RUN P: follow-up cadence in GHL (Long Tail loop, seasonal touches, Quiet stage)

Written by Cowork 2026-09-12 for terminal A (the only session allowed in the GHL browser UI).
Copy this file to `_briefs/RUN-P-cadence.md` in the repo first, then work from there and record everything in it.
Same rules as every GHL run: app.ridethehightide.com only, one tab, Chrome in front, never click "click here to refresh",
type email bodies through the </> source dialog (triple click inside the textarea before pasting), reload and re-read after
every save, every test contact has a unique phone AND a unique plus-addressed email, delete test contacts when done,
no dashes anywhere in email copy. Build everything end to end, then report. Batch questions at the end.

## What already exists (do not rebuild)
- "Call: not now" ff950be3-829d-4a51-8f9a-825db660796e (Published): trigger tag not-now, suppression gate, E0, hold-45,
  three 45-day passes (45-A, 45-B, 45-C + tasks), ends with Add tag loop-restart.
- "Loop: re-arm not-now" 89c10a95-1b5c-41c8-bc6a-b6b492197196 (Published): loop-restart -> wait 2 min -> swap tags.
- "Post-Presentation Email": Email 2 at +2h, Email 3 at +3d, Email 4 at +7d, then Closed Lost after 3 more days.
- W6 adds tag "reply received". Booking workflows add tag "booked". Tags hold-45, partner, do-not-prospect, loop-restart exist.
  Tag client-current may not exist yet (Run O part 2 creates it); create it if missing so the gates can reference it.
- Email copy for LT-1, LT-3, LT-5, 45-A, Q-1, YE-1, YE-3 is in the spec section at the bottom. LT-2, LT-4, YE-2, YE-4 you write
  to the same rules (short, one idea, something useful, no dashes, existing branded wrapper, David's signature block).

## Step 0: two GHL facts to test before building (10 minutes, saves hours)
1. Does a Wait step set to a specific date that is already in the past fire immediately, or does GHL offer a "skip if the
   date has passed" option? Test with a throwaway workflow and a date one hour ago.
2. Can an If/Else compare a custom DATE field to "today minus N days" (relative date)? If not, use the cooldown-tag pattern below.
Record both answers in RUN-P-cadence.md before going further; they decide the design of Part C.

## Part A: Long Tail loop (change Post-Presentation Email)
After Email 4, delete the Closed Lost action. Instead:
- Try to move the opportunity to a new stage "Quiet" in the Sales / Setup pipeline (create the stage if missing). If the
  Update Opportunity action is skipped because the trigger carries no opportunity (same problem Run M hit), do NOT fork the
  canvas; add tag "quiet" instead and note it. Run O part 2 or David moves the stage by hand from the smart list.
- Then: Wait 4 days -> If/Else exit if tag reply received OR booked OR client-current OR do-not-prospect OR partner OR dnc
  -> LT-1 -> Wait 4 days -> gate -> LT-2 -> Wait 4 days -> gate -> LT-3 -> Wait 14 days -> gate -> LT-4 -> Wait 14 days -> gate
  -> LT-5 -> Wait 3 days -> gate -> Add tag not-now (this hands off to "Call: not now") -> end.
- Every email send in this loop also: Update contact field "Last touch" = today (create it: custom DATE field, group Sales)
  and Add tag recent-touch (see Part C).
- Any reply (tag reply received) already creates a task via W6; do not duplicate it.

## Part B: Call: not now touches (small edits to the existing workflow)
- After each of E0, 45-A, 45-B, 45-C: Update field Last touch = today, Add tag recent-touch.
- Add client-current, quiet and dnc to the suppression gate if any are missing.

## Part C: Seasonal touches
Dates for the next twelve months (all 9:00 AM Mountain):
- 2026-11-01 YE-1, 2026-11-15 YE-2, 2026-12-01 Q-1 and YE-3 (send YE-3 only on Dec 1, it covers both), 2026-12-15 YE-4,
  2027-03-01 Q-1, 2027-06-01 Q-1, 2027-09-01 Q-1.
Who: contacts with tag hold-45 OR not-now OR quiet. Never anyone with client-current, do-not-prospect, partner, dnc, booked.
Cooldown: before every seasonal send, If/Else: if tag recent-touch present, skip that send. Workflow "Touch cooldown"
(trigger tag recent-touch added, re-entry on, Wait 10 days, Remove tag recent-touch) keeps the tag honest.
If Step 0 says relative date compares work, use Last touch older than 10 days instead of the tag and still build the field.
Design, depending on Step 0 answer 1:
- If a past date does NOT fire immediately (or a skip option exists): one workflow "Seasonal touches 2026-27", trigger tag
  added (hold-45, not-now, quiet: one trigger each), re-entry on, linear chain of Wait-until-date -> gate -> cooldown check
  -> send -> Last touch/recent-touch, in date order. Bulk-add everyone currently tagged from the Hold smart list once.
- If a past date DOES fire immediately: one workflow per date (seven small workflows, same trigger and gates). At each
  date the send goes only to contacts already enrolled; a contact tagged after a date has passed must not get that email,
  so put an If/Else "Date added to workflow"/"Created" guard if GHL offers one, otherwise accept the seven-workflow design
  and document that late enrollees skip past dates by design.
Annual maintenance: note in RUN-P-cadence.md that every December the dates advance one year (Claude Code task).

## Part D: smart lists and stage
- Smart list "Quiet / long tail": tag quiet OR opportunity stage Quiet.
- Smart list "Seasonal audience": tag hold-45 OR not-now OR quiet, minus the suppression tags.
- Stage "Quiet" in Sales / Setup pipeline if it could be created.

## Test
One test contact through Part A with waits at 1 minute (all five LT emails, hand-off to not-now proven by the contact
entering "Call: not now"), one test contact through one seasonal workflow with the date set 2 minutes ahead (send proven,
then blocked on a second pass because recent-touch is present). Put every wait and date back, reopen and re-read each one
after a full reload, delete both test contacts, commit and push, then report: workflow ids, the two Step 0 answers, test
times, and anything skipped.

## Email copy (no dashes; use the branded wrapper already in GHL)
LT-1 subject: One thing from our call, {{contact.first_name}}
Hi {{contact.first_name}}, one thing I forgot to mention on our call. Most owners your size are paying for two or three vendors that overlap, and nobody is paid to notice. If you ever want me to look, the vendor list takes ten minutes. No form needed for that. David

LT-2 subject: A number worth knowing
Hi {{contact.first_name}}, a quick proof point. [PULL ONE STORY, with its real figures, from A1_Sales/Atlas_One_Proof_Sheet.html on OneDrive; do not invent a number.] None of it showed up on a single invoice. It showed up when someone looked at all of them together. If you want that look, my calendar is here: https://api.leadconnectorhq.com/widget/groups/book-david. David

LT-3 subject: Want to knock the form out together?
Hi {{contact.first_name}}, the quote form is still open on my side. If it is easier, grab ten minutes here and we will fill it in together on the call: https://api.leadconnectorhq.com/widget/groups/book-david. If the timing has changed, just say so and I will stop nudging. David

LT-4 subject: Two minutes, your own numbers
Hi {{contact.first_name}}, no pitch in this one. This calculator shows what one employee leaving actually costs once you count the hiring time, the manager hours and the ramp up: https://forms.atlasonesolutions.com/tools/retention-cost/. Put your numbers in. Most owners are surprised. David

LT-5 subject: Should I close your file, {{contact.first_name}}?
Hi {{contact.first_name}}, I would rather hear a no than guess. If now is not the time, reply "later" and I will check back in a few months with nothing but useful stuff. If you want the quote, reply "yes" and I will call you today. David

Q-1 subject: If you are changing anything this quarter, start now
Hi {{contact.first_name}}, quarter end is 30 days out. That matters because payroll, benefits and workers comp changes are cleanest on a quarter boundary, and the paperwork takes two to three weeks. If you have been thinking about any of it, this is the week to start. Fifteen minutes here: https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp. David

YE-1 subject: January 1 is the easiest start date of the year
Hi {{contact.first_name}}, two months out from year end. A January 1 start means clean W-2s, one set of quarterly filings, and benefits that line up with open enrollment. If a change to payroll, benefits or insurance is on your list for next year, the decision has to happen by early December to make the date. Happy to walk you through what that would look like. David

YE-2 subject: Your workers comp audit is coming
Hi {{contact.first_name}}, most workers comp policies renew around year end, and the audit that follows is where owners get surprised: a class code that is off, an officer who should have been excluded, payroll counted twice. Fifteen minutes now saves the letter in February. https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp. David

YE-3 subject: Last clean cut-over date
Hi {{contact.first_name}}, this is the last week to start the paperwork and still go live January 1. After this it becomes a mid-quarter switch, which works but is messier. Fifteen minutes and I can tell you whether it is worth doing now or waiting. David

YE-4 subject: Start the paperwork now, go live January 1
Hi {{contact.first_name}}, if you want a January 1 start on payroll, benefits or insurance, the paperwork has to be in motion this week. It is mostly signatures and a census; my team does the rest. Reply "go" and I will send the short list of what I need. David
