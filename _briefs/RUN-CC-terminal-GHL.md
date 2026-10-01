# BRIEF-GHL (current run: Run CC, 2026-09-20 evening MT). DONE: Parts 1 to 71, the Back Office Audit side is complete and proven live, Run CB is audited PASS. THIS RUN: Parts 72 to 77, the support desk: load the Knowledge Base, build and test the Conversation AI bot on the web chat widget, wire the human handover so every escalation is a task with an owner, stop at the one switch that costs money.

History for older runs is in this repo's `_briefs/` copies and in each `RUN-*-report.md`. Run CB's report is
`_briefs/assets/run-CB/RUN-CB-report.md`. Installed by Cowork chat "A1 GHL support desk". The plan this run
executes is `_BUILD-LOG/support-desk-and-knowledge-base-2026-09-20.md` (step 3); the content it loads was built by
`_BUILD-LOG/service-content-library-2026-09-20.md` (step 2). Do not rebuild anything from Run CB or earlier.

Terminal rules unchanged: ghl-browser only, start at app.ridethehightide.com/, never a deep URL, one low
stakes click first, stop cleanly after one Cmd+R if it does not land. Never fork or background (rule 44).
Fresh navigation before trusting state (rule 42). Never touch a Publish or Draft switch on a workflow. Send
nothing to a real prospect or client, no SMS, no HIPAA, delete no files, spend nothing, accept no billing,
start no paid trial. No dashes in any copy you type (bot prompt, messages, names). Assets
`_briefs/assets/run-CC/`, screenshots in `shots/`. Log to `TERMINAL-GHL-live.md` after every step. Read merge
field names from the picker, never type them from memory.

Answers to Run CB's questions, decided, do not re-ask: (1) **Client: 90 day pulse is now PUBLISHED. David published
it himself on 2026-09-20, after this brief was written.** Part 77 only fixes its Skip weekends toggle, and because
the workflow is live it follows Run BX's lesson: save the action, then click the top level workflow Save, then read
back after a full reload. Never touch its Publish switch; it stays Published. (2) The Strategy Session calendar is
**NOT to be touched and is no longer a delete candidate.** Cowork checked every Atlas One file on 2026-09-20: its
slug appears nowhere outside Run CB's own report, and every booking link in the sales material is the Intro Call,
the book-david group, or the Audit calendar. It stays as it is. Do not rename, move or delete it, and do not raise
it again. (3) The "Existing knowledge base" row is read in Part 72, not edited. (4) The AI price is
answered by Part 76, by reaching the screen that shows it and backing out.

## What may and may not be clicked in this run
HighLevel's own pricing article says bot training and the bot trial are free and only messages sent to a
contact by a live bot are billed. So in this run you MAY click Create knowledge base, Add source, Create Bot,
Save, Train, and the bot's built in test or trial chat. You may NOT click anything that says Enable, Activate,
Upgrade, Subscribe, Buy, Add card, Start plan, Accept, or any consent checkbox, and you may NOT set the bot
status to Suggestive or Auto Pilot. If any screen in this run shows a price, a card form, a wallet top up or a
consent box, screenshot it, copy its text word for word into the report, and back out with Cancel or the X.
The bot is left in status Off at the end; David flips it on after reading the price. That is the design, not
a failure.

## Part 72: the Knowledge Base
File: `<Master_Kit>/14 Service Content Library/Atlas_One_Service_Content_Library_KB.txt` (132 KB, 2,453 lines,
one article per service for all 106 services, six division sections, a Sources section, then "Standing answers
the bot should always give" and "Referral partners and vendors"). It is a plain text copy of the `.md` beside
it, because HighLevel's Knowledge Base accepts PDF, DOC, DOCX, PPT, TXT and CSV and not `.md`. Upload the
`.txt`. Do not edit the content; if the uploader rejects the file for size, split it at the `## ` division
headings into six files named `Atlas One KB 1 Workforce and HR.txt` through `Atlas One KB 6 Business
Consulting.txt` plus `Atlas One KB 7 Standing answers.txt` (Sources plus the two closing sections) and upload
all seven, and say so in the report.
1. AI Agents > Knowledge Base. Open the existing row "Existing knowledge base" read only: screenshot its source
   list and record what it holds (Run CB's guess is that it is an empty HighLevel default). Change nothing in
   it and do not delete it.
2. Create knowledge base, name exactly `Atlas One support`. Add source > File upload > the `.txt` above. Wait
   for processing to finish (status Ready or Trained, not Processing). Screenshot the source row with its
   status and the KB gaps count.
3. If the Knowledge Base screen has a retrieval tester, ask it "What does the Professional membership cost?"
   and "Do you do certified payroll?" and screenshot both answers. If it has no tester, skip; Part 75 tests
   through the bot instead.
Record the KB quota after creation (Run CB read 1 of 15 before).

## Part 73: the bot
AI Agents > Conversation AI > Create Bot. If it offers Guided Form, Prompt Based or Flow Based, choose
Prompt Based, start from scratch (no template). If the screen only offers a guided form, choose General Q&A and
put the prompt below into whatever personality, instructions or additional prompt box it offers.
Bot name exactly `Atlas One Support`.
Bot Settings:
- Channels: Live Chat (the web chat widget) ONLY. Do not turn on SMS, WhatsApp, Facebook, Instagram or Email
  for this bot; a bot answering on SMS is texting and this run may not text. If the only channel offered is
  SMS, stop this part and report what the screen offers.
- Brand voice or tone: professional, warm, plain, short sentences. If a Brand Voice must be created, name it
  `Atlas One` and paste the first paragraph of the prompt below as its description.
- Business hours or bot hours: 24 hours, every day (the point of the bot is instant answers at any hour).
- Response wait time or delay: the shortest offered.
- If there is a field for the business website, use https://portal.atlasonesolutions.com. If there is one for
  a booking calendar, pick the group "Book time with David" or the 30 Minute Back Office Audit calendar.
Bot Training: attach the `Atlas One support` knowledge base from Part 72 and nothing else. Do not add URLs,
do not crawl the website (the public site is BRJ's and is being rebuilt; the KB is the source of truth).
Prompt, paste exactly (it is written without dashes on purpose; if the editor shows it as one paragraph that
is fine):

You are the support assistant for Atlas One Solutions. You answer on the Atlas One client portal and website chat. Atlas One is a vendor neutral back office advisor for small and mid sized businesses in all 50 states, across six divisions: Workforce and HR, Benefits and Retirement, Financial Services, Risk and Insurance, Technology and Operations, and Business Consulting. One relationship replaces a dozen vendors. Speak as we. Be warm, plain and brief: two to four short sentences, then a question or a next step. Answer only from the knowledge base. If the knowledge base does not cover it, say so and open a support request instead of guessing.

Rules you never break. Never name a payroll, PEO, benefits or bookkeeping vendor or partner; every service is delivered by Atlas One. Carrier and software product names are fine. Never quote a price that is not in the knowledge base. PEO, ASO and HCM rates are quoted per client after a look at payroll and states, so never give a rate or a range for them; explain the process and offer the Back Office Audit. Health coverage is through Atlas One's carrier partners; never say master plan and never say licensed in all 50 states. Never give David Taylor's personal cell number or personal email. Never discuss cost, margin or referral percentages. Never use dashes in your replies; use commas, periods or colons.

When you cannot answer, or the person needs something done for them, do not say email us or call us. Say you will open a support request from this chat, collect their name, company, what they need and how urgent it is, then hand over to the team. Tell them the response time for their membership: Essential, next business day; Professional, next business day by phone from a named advisor; Enterprise, same business day; Concierge, same business day plus direct phone access to the team. If you do not know their tier, say next business day, sooner on Professional and above. Only if someone asks how to reach a human directly, give support@atlasonesolutions.com and 380-CALL-A1S, which is 380-225-5217. If the person says it is urgent, for example payroll will not run, an employee is hurt, or a deadline is today, tell them to call 380-225-5217 right now whatever their tier, and still open the request marked urgent.

For anyone who is not yet a client, the front door is the free 30 minute Back Office Audit, booked at https://api.leadconnectorhq.com/widget/groups/book-david. The Audit Guarantee is two times the first year membership in documented savings or risk removed, or there is nothing to buy. Referral partners quote the same prices clients pay; the referral percentage lives in their agreement and you never quote it. A vendor asking about a client gets a support request for the team and no client details.

Save. Bot status stays Off. Read back after a full reload and screenshot Bot Settings, the channel list and the
training tab showing the KB attached.

## Part 74: human handover, the ticket
AI Agents > Conversation AI > open `Atlas One Support` > Bot Goals. Goal type General Q&A (or Support, if the
list has it). Under Setup Your Actions choose Human Handover and set:
- Human Requested: enabled. Add phrases: "talk to a person", "speak to someone", "real person", "can someone
  call me", "I need help from the team", "open a request", "submit a ticket".
- Lack of Information: enabled.
- Failed to Resolve Issue: enabled, at the default number of attempts.
- Assign to user: David Taylor. Skip if already assigned: on.
- Closing message, paste exactly: Thank you. I have opened a support request for you and someone on the
  Atlas One team will reply by the next business day, sooner on Professional and above. If this cannot wait,
  call 380-225-5217 now.
- Pause bot: 1 day.
- Create task: on (due within 24 hours is the default; keep it).
- Tag: `support-handover` (create the tag if the picker does not have it; do not reuse `human_handover`).
Save, read back after reload, screenshot every field.
Then Settings > My Staff > David Taylor > Notification settings: turn on the notifications for a task assigned
to me and a conversation assigned to me, email and in app, if they are off. Screenshot before and after. This
is an internal notification to David, not a send to a contact, so it is allowed. Change nothing else on his
user.
Do not build a workflow for this. The handover action already creates the task, assigns it and tags the
contact; a workflow on the `support-handover` tag is queued for the day a support person is hired and the
routing list exists (support desk plan section 7).

## Part 75: test the bot for free
Use the bot's built in test or trial chat (the preview inside the bot editor, or the Trial or Test Bot button on
the bot page). Do not test through the live widget, do not create a contact, do not switch the status on.
Ask these, screenshot each answer, and paste the answer text into the report:
1. What does the Professional membership cost?  Expect $399 a month with setup $495, often waived.
2. Do you do certified payroll and what does it cost?  Expect the setup $300 and the three ways to buy.
3. What is your PEO rate?  Expect no number, the process, and an offer of the Back Office Audit.
4. Who is your payroll vendor?  Expect no vendor name.
5. Is your health plan a master plan?  Expect carrier partners wording and no master plan.
6. I need to talk to a person.  Expect the request flow and the closing message; note whether the test chat
   shows the handover firing.
7. Payroll will not run tomorrow, help.  Expect the urgent line with 380-225-5217.
8. What is David's cell number?  Expect a refusal and the support address or main number only if asked.
Mark each answer PASS or FAIL against the expectation in the report. Fix nothing in the KB; if an answer is
wrong because of the prompt, adjust the prompt once, save, retest that one question, and record both versions.
If the test chat is itself gated behind a price or consent screen, screenshot it and skip this part; Cowork
will test through the live widget after David turns it on.

## Part 76: reach the price, then back out
Open the bot's status control (Off, Suggestive, Auto Pilot, or however it is labelled). Select Auto Pilot ONLY
IF selecting it opens a confirmation, price or consent screen before anything is saved; screenshot that screen,
copy every price and every sentence on it word for word into the report, then Cancel or X out and confirm the
status still reads Off after a full reload. If selecting Auto Pilot would take effect immediately with no
confirmation screen (the control is a plain toggle or dropdown that saves on change), do NOT select it; instead
look for the price in Settings > Billing (any AI, Conversation AI or AI Employee line, plan card or usage rate)
and in AI Agents > Getting Started (read the page, do not click Get Started), and report what you found and
what you could not find. Either way the report's first line states the price or states that it is not shown
anywhere reachable without switching the bot on.

## Part 77: Skip weekends on the 90 day pulse task
Automation > Workflows > Client: 90 day pulse (`52bf136f`, **PUBLISHED** since David published it on 2026-09-20;
this brief said Draft, which is out of date). Open the Task step on the Yes branch and turn Skip weekends on, the
same as the task in Booking: after the call. Because the workflow is live, Run BX's lesson applies: save the
action, then click the top level workflow Save as well (a red dot appears on Save when an unsaved workflow level
change exists), then read back after a full reload and screenshot. Do NOT touch the Publish switch; it stays
Published. Nothing else in the workflow changes.

## Report
First line: the AI price on this account, word for word, or "not shown without switching the bot on".
Second line: the bot `Atlas One Support` exists, status Off, trained on `Atlas One support` (N sources), with
human handover to David and the task on; and the Part 75 score, for example 8 of 8 PASS.
Then per part: what was done, what was read back, screenshots, numbered assumptions, and "Questions for
David" at the end, only questions that block the next run. Write `RUN-GHL-report.md` in the Master Kit and
copy it to `_briefs/assets/run-CC/RUN-CC-report.md`, commit and push.
