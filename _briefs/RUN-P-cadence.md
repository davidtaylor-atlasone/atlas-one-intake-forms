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

### Step 0 ANSWERS (tested 2026-09-11, throwaway workflow "ZZ Step 0 test (delete me)" c3498a76-a36b-49fe-93ec-1096f471f5d1, deleted after the test)

**Answer 1: a past specific date does NOT hold the contact, and GHL DOES give you a skip option.**
The Wait action, wait type "Until a specific date/time", exposes two setting groups:
- "When should the contact proceed?" = On this date and time / Before this date / After this date
- "If this date has already passed" = Continue to next action / Exit contact from automation / Go to specific step /
  **Skip all outbound communication actions till next wait or event start date action** (Email, SMS, call & voicemail). This
  last one is the GHL default.

Live test: workflow trigger tag zz-step0, then Wait until 2026-09-11 09:40:00 PM (one hour in the past, default
"Skip all outbound communication" selected), then Email, then Add tag zz-done. Test contact "ZZ Step0 Probe" was tagged
at 10:49:47 pm Mountain. Execution log:

| Time (MDT) | Action | Status |
|---|---|---|
| 10:49:48 pm | Add to workflow | Added To Workflow |
| 10:49:48 pm | Wait | Wait Finished |
| 10:49:49 pm | Email | **Skipped** |
| 10:49:49 pm | Add Tag | Executed |
| 10:49:50 pm | Removed by  End Of Workflow | Finished |

So the wait releases instantly on a past date, the outbound email is suppressed, and non communication actions still run.
**Design consequence: build Part C as ONE chained workflow** ("Seasonal touches 2026-27"), waits in date order, default
"Skip all outbound communication actions till next wait or event start date action" on every date wait. A contact enrolled
in, say, March 2027 walks past every date that has already gone by without receiving those emails, and stops at the next
future date. No seven workflow fan out, and no need for a "Date added to workflow" guard.

**Answer 2: NO. An If/Else cannot compare a custom DATE field to a relative date.**
In If/Else, choosing the custom DATE field "Last Touch Date" offers exactly four operators: Is, Is not, Is not empty,
Is empty. There is no greater than, no less than, and no "today minus N days".
**Design consequence: use the cooldown TAG pattern** for Part C (tag recent-touch plus the "Touch cooldown" workflow that
strips it after 10 days). The date field is still written on every send so a human can read the last touch date on the
contact record, but no automation branches on it.

**Field note:** a custom DATE field named **"Last Touch Date"** already exists (Date picker, folder Prospecting). Reusing
it rather than creating a second "Last touch" field.


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

---

## Build log (Run P, terminal A, 2026-09-11 / 12)

### Done
- **Step 0 answers recorded above.** Throwaway workflow built, tested, drafted and deleted. Test contact deleted.
  Scratch tags `zz-step0` and `zz-done` deleted (note: single tag delete silently does nothing in Settings > Tags; the
  working path is to tick the rows and use the bulk **Delete tags** button, which asks you to type DELETE).
- **Tags:** `quiet` and `recent-touch` created and verified. `client-current` already existed.
- **Field:** reusing the existing custom DATE field **"Last Touch Date"** (Date picker, folder Prospecting) rather than
  creating a second "Last touch" field.
- **Part D stage:** stage **"Quiet"** added to the **Sales / Setup** pipeline (id 2WMB5ZfbHxOvE6hb0Ann), probability 5%,
  saved and re-read after a full reload. Note: the stage editor drops everything you typed if an empty stage row is left
  behind; remove the trailing blank row first, then Save becomes enabled.
- **Part A, "Post-Presentation Email" (304a9fa4-a256-4015-b767-031070f4186f):**
  - Deleted the whole Closed Lost block: the `Opportunity - Closed Lost (no response)` action, the `Which pipeline?`
    If/Else and both `Stage - Closed Lost` actions under it.
  - Added `Tag quiet` (Add contact tag = quiet) in its place.
  - Added `Wait 4 days (before LT-1)`.
  - Built `Gate 1` (If/Else). Branch **Suppressed** = Tags Includes `reply received` OR `booked` OR `client-current`
    OR `do-not-prospect` OR `partner` OR `dnc`. It saved and published cleanly once.
  - **Gate 1 was then removed again and is NOT in the workflow now.** See "Where it stopped" below.

### Where it stopped and why (read this first)
Part way through adding the LT-1 email I opened the `</>` source dialog, and the triple click that is supposed to put the
caret inside the dialog's textarea landed outside it. The following `cmd+a` selected the whole canvas instead of the
textarea's contents and `cmd+v` pasted the Gate action that was sitting in GHL's action clipboard, creating a second
`Gate 1` nested inside the first. Deleting that duplicate also tore the branch structure off the original `Gate 1`, which
then failed publish validation with "1 issue needs to be resolved: yes".

Nothing bad reached the live workflow: every attempt to save the broken state was refused by GHL's own publish
validation, so the saved version never contained the damage. I deleted the damaged `Gate 1`, saved, and confirmed
"Saved!". Right after that the GHL builder stopped rendering entirely (blank canvas past 20 seconds, still blank after
an in-app Dashboard round trip), which is the same dead UI seen in Runs L and M, so I stopped rather than keep pushing
edits into an unresponsive builder holding a published workflow.

**"Post-Presentation Email" is live and coherent right now:**
`... Email 4 - Re-engage -> #2 Task - Call about open quote -> Wait -> Tag quiet -> Wait 4 days (before LT-1) -> END`
Contacts who used to be marked Closed Lost now get the `quiet` tag instead and then stop. No emails were added, so
nothing can go out that should not. The workflow is still Published.

### Opportunity stage note (decision, needs David's eye)
The brief asked to move the opportunity to stage **Quiet**. "Post-Presentation Email" is triggered by pipeline stage
changes in **two** pipelines (Sales / Setup and PEO & Benefits), and the old Closed Lost step handled that with a
`Which pipeline?` fork. Moving the stage automatically would mean re-introducing that fork and then duplicating the whole
five email Long Tail chain under both branches, which the brief explicitly forbids. So the workflow now sets the tag
`quiet` linearly instead, and the Quiet **stage** is available in Sales / Setup for David (or Run O part 2) to move from
the "Quiet / long tail" smart list. If you want it automated later, the clean way is a separate small workflow triggered
by the `quiet` tag, but Run M proved that opportunity actions silently skip on a tag trigger, so it would need a
pipeline-stage trigger instead.

### GHL UI notes learned this run (for future runs)
- Dropdown options often ignore the first click because the list re-renders after the screenshot. The reliable pattern is
  click the field, wait, then click the option twice, or use the keyboard: open the list, then **Up/Down + Return**.
- The If/Else operator list is ordered Includes / Does not include / Is not empty / Is empty. From a fresh field,
  **Down + Return** lands on "Does not include"; **Up + Return** corrects it to "Includes".
- Tags "Includes" with two or more tags means **ALL of them**. OR needs one condition per tag joined with the OR selector.
- `cmd+a` inside an action panel selects the whole page and wipes the field you were editing. Never use it there.

### Still to do
- Part A: rebuild `Gate 1` (paste it back or rebuild the six OR conditions), then LT-1..LT-5 emails with Last Touch Date
  + `recent-touch` after each, gates 2..6, waits 4/4/14/14/3 days, ending with Add tag `not-now`.
- Part B: Last Touch Date + `recent-touch` after E0, 45-A, 45-B, 45-C in "Call: not now"; add `client-current`, `quiet`
  and `dnc` to its suppression gate.
- Part C: "Touch cooldown" workflow and the single chained "Seasonal touches 2026-27" workflow (Step 0 answer 1 decided
  the single workflow design).
- Part D: smart lists "Quiet / long tail" and "Seasonal audience".
- Both tests, restore waits, delete test contacts.

### Annual maintenance
Every December the seasonal dates in "Seasonal touches 2026-27" have to be advanced one year. Put it on the Claude Code
task list for the first week of December.

### Two more GHL findings worth keeping
- **"Copy action" works and is the cheap way to build the five remaining gates.** The node three dots menu has
  Copy action; it says "Action copied to clipboard. Paste it into any workflow." and every `+` on the canvas then shows
  a paste icon beside it. Build one gate, copy it, paste it at the other five points. Do NOT use `cmd+v` for this, only
  the on canvas paste icon: `cmd+v` pastes the copied action wherever the canvas has focus.
- **The `</>` source dialog is the dangerous step.** Take a screenshot after the dialog opens, confirm the caret is
  inside the textarea (the dialog shifts ~7px after it renders, so coordinates from the screenshot that opened it are
  stale), and only then use cmd+a. If the caret is not in the textarea, cmd+a selects the whole builder.
