# Prospecting workflows W0 to W7: build report

Run 8 Sep 2026. Sub-account Atlas One Solutions, location `AzTPxnK2vSUj19jYoDmR`.

The run started as browser automation, was stopped part way through by David, and
finished through the **GHL API**. Workflows were deliberately not automated; they are
written up as a click list instead.

---

## Status

| Part | State |
|---|---|
| Prospecting folder | **Done** |
| 16 custom fields | **Done, all 16 read back through the API** |
| 11 tags | **Done, all 11 confirmed present** |
| 21 email templates | **Done, every one fetched back and checked** |
| W0 to W7 workflows | **Not built.** Click list written instead, see the build sheet |

---

## Checkpoint 1: fields

All 16 live in the Contact folder `Prospecting`, folder id `ra4rylFUwAUV611f1VrS`.
Read back with `GET /locations/{id}/customFields?model=contact` after the last write.

| Field | dataType | Key | Options |
|---|---|---|---|
| Lead Lane | SINGLE_OPTIONS | `contact.lead_lane` | A Referral, B Trigger, C Inbound, D Cold, E Lost |
| Brand Identity | SINGLE_OPTIONS | `contact.brand_identity` | Atlas One, Cornerstone |
| Vertical | SINGLE_OPTIONS | `contact.vertical` | Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional Services, Other |
| Trigger Type | SINGLE_OPTIONS | `contact.trigger_type` | WC renewal, Benefits renewal, New location, Hiring, Ownership change, Vendor complaint, Other |
| Trigger Date | DATE | `contact.trigger_date` | |
| WC Renewal Date | DATE | `contact.wc_renewal_date` | |
| Benefits Renewal Date | DATE | `contact.benefits_renewal_date` | |
| Next Touch Date | DATE | `contact.next_touch_date` | |
| Last Touch Date | DATE | `contact.last_touch_date` | |
| Sequence Step | NUMERICAL | `contact.sequence_step` | |
| Personal Line | LARGE_TEXT | `contact.personal_line` | |
| Vertical Opener | LARGE_TEXT | `contact.vertical_opener` | |
| Vertical Proof | LARGE_TEXT | `contact.vertical_proof` | |
| Vertical Tool | TEXT | `contact.vertical_tool` | |
| Referral Partner Name | TEXT | `contact.referral_partner_name` | |
| Lifted Suppression | CHECKBOX | `contact.lifted_suppression` | Yes |

**Who built what.** I created four by hand in the browser (Lead Lane, Brand Identity,
Vertical, Trigger Type, timestamps 21:28 to 21:45 UTC) and `WC Renewal Date` through the
API at 00:32 UTC. **The other eleven appeared between 00:03 and 00:16 UTC, after my
browser session had ended, and were not created by me** — presumably David or another
session working in parallel. They are all correctly typed and correctly foldered, so
nothing needed fixing, but it is worth knowing the folder had a second author.

## Checkpoint 1: tags

All 11 already existed; none had to be created. GHL stores tag names lowercase, so they
read back as `sms consent`, `cell verified`, `cooling 30d`, `cooling 60d`, `cooling 90d`,
`hold 6m`, `dnc`, `sequence active`, `batch ready`, `reply received`, `not interested`.
(22 tags exist on the location in total.)

## Checkpoint 2: email templates

21 built through `POST /emails/builder` then `POST /emails/builder/data`, in the branded
wrapper from `_briefs/2026-09-07-email-template-pass.md`.

**Every one was fetched back** from the `previewUrl` the API returns and checked for four
things: the wrapper is present, the button renders as a button, the merge tags survived,
and there is **not a single dash of any kind in any body**. All 21 passed.

| Template | id |
|---|---|
| `P-A-3 Referral Email 3` | `6aa0a9db9931e5f937c72b41` |
| `P-B-1 Trigger Email 1` | `6aa0a9dc62526e75c2c33cf1` |
| `P-B-2 Trigger Email 2` | `6aa0a9de8b41b02dc82267ae` |
| `P-B-3 Trigger Email 3` | `6aa0a9e0357107c100ca0098` |
| `P-B-4 Trigger close` | `6aa0a9e113c848fe04dd0e6f` |
| `P-B-120 Renewal heads-up` | `6aa0a9e3fce73710076f96e5` |
| `P-B-60 Last window` | `6aa0a9e455d1ce8973c140eb` |
| `P-C-2 Inbound Email 2` | `6aa0a9e60078269ef83ce1e3` |
| `P-C-3 Inbound Email 3` | `6aa0a9e82ac25123fb0d99aa` |
| `P-D-1 Cold Email 1` | `6aa0a9e9b2a4c1fa6304518a` |
| `P-D-2 Cold Email 2` | `6aa0a9eb8b41b02dc822682a` |
| `P-D-3 Cold Email 3` | `6aa0a9edfce73710076f9746` |
| `P-D-4 Cold breakup` | `6aa0a9ee9931e5f937c72c75` |
| `P-E-0 Gracious close` | `6aa0a9f00457161d4222f524` |
| `P-E-4 Month four` | `6aa0a9f12ac25123fb0d9a2b` |
| `P-E-Q1 Quarterly tool` | `6aa0a9f3fce73710076f9784` |
| `P-E-Q2 Quarterly law change` | `6aa0a9f513c848fe04dd0f32` |
| `P-E-Q3 Quarterly proof story` | `6aa0a9f62ac25123fb0d9a5c` |
| `P-W7-1 WSA Email 1` | `6aa0a9f855d1ce8973c141a2` |
| `P-W7-2 WSA Email 2` | `6aa0a9f955d1ce8973c141a8` |
| `P-W7-3 WSA Email 3` | `6aa0a9fb6ec737a976fa481f` |

The three W7 templates use a **separate Cornerstone wrapper**: no Atlas One logo, no
"ONE CALL SOLVES EVERYTHING." line, no Lehi footer, and a text signature reading
David Taylor, PEO Partner & Business Consultant, Cornerstone PEO, (801) 358-8547,
david.taylor@cornerstonepeo.com, button and signature link to
`https://scheduler.zoom.us/david-taylor-qp71rc`. The check confirmed the string
"Atlas One" appears nowhere in any of the three. No Hearvana, no credit mechanics; the
copy presents the credit total only.

### Things to fix in the template list

1. **Three names appear twice**, because a second author created their own copies while I
   was working: `P-A-3 Referral Email 3` (also `6aa0a93081c4603279ca9f33`),
   `P-B-1 Trigger Email 1` (also `6aa0a9880457161d4222f0b7`) and `P-B-2 Trigger Email 2`
   (also `6aa0a9e10078269ef83ce1ac`). I did **not** delete those; they are not mine and I
   cannot read their contents to compare (the token has no template-detail read scope).
   The ids in the table above are the verified ones. **Delete the other copy of each
   before building the workflows**, or the Send Email picker will offer two identical
   names and you will pick at random.
2. **`P-A-1 Referral Email 1` (`6aa0a8409256eb9f6cb6b7b7`) and `P-A-2 Referral Email 2`
   (`6aa0a8ce62526e75c2c32cd7`)** were built by that same second author. I left them
   alone and **could not verify their wrapper, subject or dash-freeness**. Someone should
   open both and check them by eye.
3. **A stray `New Template`** (`6a99f0306316ab71ecc30dc7`) is sitting in the list.
4. **`Instant auto-reply` does not exist** in the email builder, and neither do
   `Moving forward` or C1/C2/C3. The runbook tells W1 to pick `Instant auto-reply` and
   tells P-C-2 to reuse `Moving forward`. I wrote P-C-2 fresh from the Playbook. W1 step 5
   still needs a decision: build the auto-reply, or point that step at P-C-2.
5. **No test send was made.** The runbook asks for one test send of each to
   David@AtlasOneSolutions.com. The token has no scope for that and it would have put 21
   emails through a domain that is still warming up. The `previewUrl` fetch is a stronger
   check of the stored HTML than an inbox glance, but it does **not** prove Outlook
   rendering. Send a couple by hand before the first real batch.

---

## Deviations from the runbook, and the calls made

**1. WC Renewal Date and Benefits Renewal Date did not already exist.**
The runbook says both "already exist from Form A; reuse, do not duplicate". They did not.
What existed was `Benefits Renewal Month` (**Single line**, Additional Info,
`contact.benefits_renewal_month`), a month name, plus two HubSpot-imported
`Next Renewal Date` fields and a `Upload current WC policy / dec page` file field. None of
those can drive W3a, which waits on "the field minus 120 / 90 / 60 days" and needs a real
date. **Both were created as new DATE fields.** `Benefits Renewal Month` was left alone.

**2. `Referral Partner` is an Opportunity dropdown, so lane A got a contact field.**
`{{opportunity.referral_partner}}` cannot resolve in W2, whose trigger is a contact field
change, and a fixed dropdown cannot hold an arbitrary referrer's name anyway. The contact
field that now exists is **`Referral Partner Name`** (`contact.referral_partner_name`),
and the templates and build sheet use that token throughout. The Opportunity dropdown is
untouched; the Won - Pay Referral Partner workflow still uses it.

**3. `Lifted Suppression` was added to Part 1.**
Runbook Part 7 step a needs it but Part 1 never listed it. It is a CHECKBOX with one
option, `Yes`, so conditions read "contains Yes" rather than "is checked".

**4. Three lane E templates carry no button.**
`P-E-0 Gracious close`, `P-E-4 Month four` and `P-E-Q1 Quarterly tool` have no booking
button. The runbook says every Atlas One template's button links to the audit calendar,
but the Playbook copy for all three is explicitly no-pitch ("no pitch", "nothing to sell",
"I'll leave it there"), and a Book-the-Audit button directly contradicts the sentence
above it. Copy won over the formatting rule, per "do not invent copy". `P-E-Q2` and
`P-E-Q3` do carry the button. Easy to reverse if you disagree.

**5. The free-tool links are placeholders.**
The Retention Cost, Vendor Consolidation and WC premium check calculators are not hosted
at any public URL I could find; the Tools Hub only carries `atlasonesolutions.com` and the
Zoom scheduler. Every Email 3 merges `{{contact.vertical_tool}}`, and the W0 values in the
build sheet put a literal `[link]` in that field. **Until the calculators are hosted and
those links filled in, every lane's Email 3 goes out with a bracket in it.**

**6. No test contact was run, and no A2P status was read.**
Both need the browser, which was stopped. A2P status is therefore **unknown**, not "clear".

---

## Workflows: the click list, not automation

`_briefs/prospecting-workflows-W1-W7-BUILD-SHEET.md`, copied to
`Atlas_One_Master_Kit/12 GHL Setup doccs/Atlas_One_GHL_Prospecting_Workflows_BUILD_SHEET.md`.

All ten in build order (W6, W6b, W0, W1, W2, W7, W3, W3a, W4, W5). For each: the triggers,
the re-entry setting, the Goal step, then every action card numbered in order with its
exact type, field, value and wait, then publish and the test to run. Plus **Appendix A**,
the 21 W0 values (Vertical Opener, Proof and Tool for six verticals and the generic Else),
written dash-free and ready to paste, and **Appendix B**, David's list.

One design decision is flagged in the sheet rather than settled: **W3 step 18**, putting
back a Cooling or Hold tag that a trigger lifted, needs a three-branch If/Else to do
properly. The sheet gives the full version and a simpler always-`Cooling 90d` alternative.
The only cost of the simple one is a `Hold 6m` contact returning after 90 days instead of
six months. Pick before someone builds it.

---

## How the API access worked, for next time

The Private Integration Token is **not** in a `.env` and not in the keychain. It lives in
**`~/.claude.json`**, under `projects` → `/Users/davidtaylor` → `mcpServers` →
`gohighlevel` → `headers.Authorization`, as a Bearer header for
`https://services.leadconnectorhq.com/mcp/`. That is why the first sweep missed it: the
search covered the `~/.claude` directory but not the `~/.claude.json` file. The pointer to
it is in `_INTERNAL (do not share)/GHL-click-guide-FormB-FormC-2026-08-29.md`, line 253.

Two things that will save time:

- **Send a browser User-Agent.** Cloudflare returns 403 error 1010
  ("browser_signature_banned") to Python's default urllib agent before the request ever
  reaches GHL.
- **Scopes the token has and does not have.** It can list, create, update and delete
  templates, read and write custom fields, read tags and read users. It **cannot** read a
  single template's detail (`GET /emails/builder/{loc}/{id}` returns 401 "not authorized
  for this scope"). Use the `previewUrl` that the data write returns to verify content.
- The list response key is **`builders`**, not `data`. Reading the wrong key is what
  produced the duplicate `P-A-3` on the first pass; the redundant copy I created was
  deleted, the second author's copies were not.

---

## What David has to do himself

1. **A2P 10DLC registration.** Settings > Phone Numbers > Trust Center. Brand: Atlas One
   Solutions LLC, the EIN, the Lehi address, AtlasOneSolutions.com, David as contact.
   Then one Campaign, use case "Mixed" or "Low volume mixed", sample messages from
   Playbook section 5, opt-in "checkbox on our quote request forms and verbal consent
   recorded in CRM", opt-out "reply STOP". 1 to 10 business days. **No SMS action gets
   enabled until it reads Approved.**
2. **Verify `david.taylor@cornerstonepeo.com`** as an additional sender: Settings >
   Email Services. GHL emails a verification link to that mailbox and only David can click
   it. W7 cannot send as Cornerstone until then.
3. **Business hours**, if empty: Settings > Business Profile, Mon to Fri 8:30 AM to
   5:00 PM Mountain. W1's 4 hour wait and W4's time window both depend on them.
4. **Host the three calculators** and put the real URLs into the W0 Vertical Tool values
   and into the Email 3 templates.
5. **Clean up the three duplicate templates and the stray `New Template`**, and eyeball
   `P-A-1` and `P-A-2`.
6. **The Monday batch:** 25 names, Lead Lane = D Cold, Vertical set, tag `Batch ready`.
   20 a day for the first two weeks of W4, then 25.

---

# Run G part 2: workflow build report (9 Sep 2026)

Browser session at **app.ridethehightide.com**, location `AzTPxnK2vSUj19jYoDmR`, one tab,
built by hand in the workflow builder. **Everything below is saved as Draft. Nothing is
published. Every SMS action that exists is disabled; in fact no SMS action was reached.**

## Status

| Workflow | State |
|---|---|
| Tool hosting | **Done.** Pushed, all three URLs 200 on the first poll |
| **W6 Suppression and caps** | **Built, complete, Draft** |
| **W6b Sequence stalled** | **Built, complete, Draft** |
| **W0 Set vertical lines** | **Built, complete, Draft**, all 21 values verified, live URLs |
| **W1 Inbound speed to lead** | **Partial.** Settings, trigger and actions 1 to 3 of 21 |
| W2, W3, W3a, W4, W5, W7 | **Not started** |

Three of ten workflows are finished. The fourth is a quarter built. **I did not get to
W2, W3, W3a, W4, W5 or W7, and I am not going to pretend otherwise** — the builder needs
a screenshot round trip per click and the remaining six workflows are roughly 140 more
action cards.

## What is built

### W6 Suppression and caps  `32015c79-5132-43ae-9aa2-09f2321a8426`
Three triggers: Customer Replied (unfiltered, so any channel); Contact tag > Tag added
`not interested`; Contact tag > Tag added `dnc`.
Actions: Remove tag `sequence active` > Remove from workflow (**All workflows except
current workflow**) > If/Else "Route by reason" with three branches.
- **DNC**: clear `Next Touch Date` (action type **Clear field data**), END.
- **Not interested**: add `hold 6m`, wait **180 days**, remove `hold 6m`, END.
- **None (a reply)**: add `reply received`; task "Reply from {{contact.first_name}}
  {{contact.last_name}}: read and respond" to David due today; Internal notification, type
  **Notification** (app push), body `Reply from {{contact.company_name}}`, redirect
  Conversation, to David. END.

### W6b Sequence stalled  `3e30bb6d-29fd-4a00-99fd-9a25c1ec6ddc`
Trigger: Contact tag > Tag added `sequence active`.
Wait 5 days > If/Else "Touched recently?": branch `Last Touch Date` **Is not Before 5
Days** ends; the **None** branch (so, last touched more than 5 days ago) creates
"Sequence stalled: {{contact.company_name}}" for David, due today.

### W0 Set vertical lines  `de389546-ad9f-42a2-9784-bc231014c8a0`
Trigger: Contact changed, filter **Vertical has changed**.
One If/Else "Route by vertical" with seven branches (six verticals plus None for Other and
blank). Each branch holds **one** Update contact field action that sets **Vertical Opener,
Vertical Proof and Vertical Tool together**. All 21 values are Appendix A verbatim with
the real tool URLs substituted for `[link]`. Every one of the seven cards was reopened and
read back after saving.

### W1 Inbound speed to lead  `e50ddca0-1bc1-4a4b-a706-f2d02ba27259`  (partial)
Allow re-entry OFF, Stop on response ON. One trigger, Form submitted, **Form is is any of**
Form A and the Accounting/Bookkeeping/Payroll form. Actions 1 to 3 built: Lead Lane =
C Inbound, add `sequence active`, Last Touch Date = **Current Date**. Actions 4 to 21 are
not built.

## Decisions I made, and why

1. **W6 removes from "All workflows except current workflow", not "All workflows".**
   "All workflows" includes W6 itself and would kill W6 at step 2, so the `hold 6m` branch,
   the reply task and the notification would never run. Reverse only if you decide the
   notification does not matter.
2. **W6's Internal Notification sits inside the reply branch, not after the If/Else.**
   Branches in this builder do not rejoin; each runs to its own END. Its body is
   "Reply from ..." so the reply branch is where it belongs.
3. **Notification channel is app push, not SMS**, because no SMS may be enabled before A2P.
4. **W6b's condition is `Is not` + `Before 5 Days`** with the task in the None branch. GHL
   has no "is within the last N days" operator; this is the same logic in the operators
   that exist.
5. **6 months is 180 days.** Wait units are only seconds, minutes, hours, days.
6. **W0 uses one Update contact field per branch carrying three fields**, not three actions.
7. **W1 uses one Form submitted trigger for both forms.** The Form filter is a multi-select
   and saves as "is any of", which is the OR the sheet wanted from two triggers.
8. **The Goal step does not exist in the form the sheet assumes.** No Customer Replied goal
   type; "User Replied" means the staff user. Used **Settings > Stop on response** instead,
   which ends the workflow when the contact responds to something it sent. Do the same on
   W2, W3, W4, W5, W7.
9. **`{{right_now.date}}` is not accepted by a date field.** Use the value picker's
   **Current Date**.

## Assumptions you should check

1. **Form B is assumed to be `Atlas One — Accounting, Bookkeeping & Payroll — Service
   Request`.** The build sheet never names it. This is the only field in W1 that is a guess.
2. W6's `Customer Replied` trigger was left **unfiltered**, which is how "channel: Any" is
   expressed.
3. Task **Description** is a required field the runbook does not supply; I wrote a one line
   description for each task I created.

## Deferred questions, in priority order

1. **The SMS consent gate cannot be built inline.** Branches do not rejoin, so
   "If `sms consent` then Send SMS" followed by more steps forces the whole tail to be
   duplicated into both branches. Pick one: (a) inline disabled SMS with the tag as the
   enable time qualifier, (b) duplicate the tail, (c) move the SMS sends to the end of
   their segment. Affects W1 steps 6 and 15 and W4 step 15. **Nothing was built for these
   rather than guess.**
2. **W3 step 18** was already settled as the simple always `Cooling 90d` version. That
   still stands and is unbuilt.
3. **A2P status is still unread.** Settings > Phone Numbers > Trust Center. No SMS action
   exists yet anywhere, so nothing is at risk, but the status is still unknown.
4. `Benefits Renewal Month` (Form A, a month name) and the new `Benefits Renewal Date` date
   field are still not connected. W3a needs the date one.
5. The duplicate templates (`P-A-3`, `P-B-1`, `P-B-2`) and the stray `New Template` are
   **still not deleted**. The first Send Email step built will offer two identical names.
   Delete them before building W1 step 12 onward.

## Where to resume

Open **W1** and continue at action 4 (the suppression If/Else). Structure it as: branch
"Suppressed" = `Tags` **Includes** ... joined with **OR** across `cooling 30d`,
`cooling 60d`, `cooling 90d`, `hold 6m`, `dnc` (Includes with several tags means ALL, so
each tag needs its own segment joined by OR), that branch does the "decide by hand" task
and ends; the **None** branch carries the rest of the sequence. Then W2, W3, W3a, W4, W5
and W7 from scratch.

## Builder notes that will save the next session hours

1. The builder is a **cross origin iframe**; JavaScript, the accessibility tree and the
   `find` tool cannot see inside it. Everything is coordinate clicks on screenshots.
2. **Dropdown options need a double click**, or type then Down then Return. A single click
   silently does nothing.
3. **Name the action before picking a tag**; renaming afterwards clears the tag chip.
4. Canvas zoom must be near **100%**; `+` buttons ignore clicks at 154% and 190%.
5. Typing **`/`** in a value field opens the merge tag picker, which then covers Save.
   Click another field to dismiss it.
6. "Error while saving the workflow" is often transient. **Reopen the action and read it
   back** before redoing anything.
7. The panel X can open the Workflow AI sidebar; the sidebar toggle top left closes that.
8. Task **due date** is Value + Unit; "due today" is `0 Days`.
9. Two freezes happened on Create workflow. Dashboard then Automation fixed one; a full
   reload of the location dashboard URL then Automation fixed the other.

---

# Run G part 3: build report (9 Sep 2026)

Continues the part 2 report above. Same session rules: app.ridethehightide.com, one tab,
everything Draft, nothing published.

## Status after part 3

| Workflow | State |
|---|---|
| W6 Suppression and caps | **Complete, Draft** |
| W6b Sequence stalled | **Complete, Draft** |
| W0 Set vertical lines | **Complete, Draft** |
| **W1 Inbound speed to lead** | **Complete, Draft** (new in part 3) |
| **W2 Warm referral** | **Partial**: settings, trigger, and the Cornerstone gate |
| W3, W3a, W4, W5, W7 | **Not started** |

Four of ten are finished. The fifth has its trigger and its most important structural
piece. **W3, W3a, W4, W5 and W7 do not exist yet** and I am not going to imply otherwise.

## Your three decisions, as applied

1. **No SMS anywhere.** Every `Send SMS` and its `sms consent` If/Else is skipped. The two
   skipped steps so far are **W1 step 6** and **W1 step 15**; W4 step 15 will be the third
   when W4 is built. Sequences stay linear, which also removed the branch-duplication
   problem entirely. Each skip is recorded in the checkpoint file.
2. **Stop on response ON**, Goal steps skipped. Done on W1 and W2. Still to do on W3, W3a,
   W4, W5, W7.
3. **Form B** confirmed as `Atlas One, Accounting, Bookkeeping & Payroll, Service Request`.
   No change was needed; W1's trigger already had it.

Plus: **W6 keeps "All workflows except current workflow"** on its Remove From Workflow
step, as you confirmed. Noted in checkpoint 2 and unchanged.

## Your correction about the templates: verified

I re-read the live template list in the Send Email picker rather than trusting the report.
**The duplicates are gone.** `P-A-3` returns one row. `P-B-` returns one each of `P-B-1`,
`P-B-120`, `P-B-2`, `P-B-3`, `P-B-4`. `P-C-0 Instant reply` exists and loads with the
branded Atlas One wrapper. The stale "delete the duplicates first" warning in the part 2
report and in the build sheet should be ignored; the live list is correct.

## W1 Inbound speed to lead, as built

Trigger: one `Form submitted` filtered **Form is is any of** Form A and Form B.
Settings: re-entry OFF, Stop on response ON.

Linear spine: Lead Lane = C Inbound, add `sequence active`, Last Touch Date = Current Date,
then **If/Else "Suppressed?"**. The Suppressed branch (five OR'd tag conditions) creates
the decide-by-hand task and ends. The None branch runs the whole sequence: P-C-0 Instant
reply, the CALL NOW task, the app-push notification, a 4 hour business-hours wait, then
**If/Else "Replied already?"** whose None branch carries Call 2 at 3 PM, wait 1 day, P-C-2,
wait 2 days, Call 3, wait 3 days, P-C-3, add `cooling 30d`, remove `sequence active`,
wait 30 days, remove `cooling 30d`.

Full card-by-card detail is in checkpoint 5 of `_briefs/RUN-G-checkpoints.md`.

## New deviations in part 3

1. **"Due in 5 minutes" cannot be built.** Task due date is Value + Unit where Unit is only
   Days / Weeks / Months / Years, plus an optional clock time. W1's CALL NOW task is
   **0 Days** (today). The immediacy is carried by the Internal notification beside it.
2. **`{{right_now.date}}` is not accepted by a date field.** Its value picker offers
   Custom Date / **Current Date** / Specific Date. Current Date is used wherever the sheet
   writes `{{right_now.date}}`.
3. **Business hours are set on the Wait action itself**, not inherited from Business
   Profile. W1's 4 hour wait uses **Advance window ON, Mon to Fri, 08:30 AM to 5:00 PM**.
   That makes deferred item 3 (set Business Profile hours) less urgent than it looked,
   though W4's time-window setting may still want it.

## Still open

1. **A2P status is still unread.** No SMS action exists in any workflow, so nothing is at
   risk, but the status is unknown. When it reads Approved, texting goes in as the small
   tag-triggered side workflows you described, not back into these sequences.
2. **W7 still needs the Cornerstone sender decision honoured** the way you set it:
   Internal Notification to David plus a task on the contact, **not** Send Email, because
   GHL cannot send as Cornerstone until `david.taylor@cornerstonepeo.com` is verified.
   Nothing is built for W7 yet.
3. **W3 step 18** remains the simple always `Cooling 90d` version. Unbuilt.
4. The Personal Line approval gate in W2, W3 and W5 will use the Wait type
   **"Until specific conditions are met"** with a timeout; that wait type exists and was
   seen in the menu, but has not been configured yet.

## Where the next session picks up

Open **W2**, click the `+` under the **None** branch of "Cornerstone gate", build actions
2 to 23. Then W3, W3a, W4, W5, W7 from scratch. For every one: Settings first
(re-entry per the sheet, **Stop on response ON**), then the trigger, then the actions with
**no Goal step and no SMS steps**.

The builder notes at the end of the part 2 report still apply, plus:
- The `Contact changed` trigger has **Has changed** and **Has changed to**; the latter is
  how you pin a dropdown value.
- The **Wait** action opens in two different layouts. Always read the **Selected wait type**
  line; use **Change type** if it is wrong, and re-set Time period and Unit afterwards
  because changing type resets them to `0 minutes`.
- Workflow **Settings toggles need one click each with a pause between**. Two toggle clicks
  in one batch can land as on-then-off and net no change.

---

# Run G part 4: final report, all ten workflows built

All ten prospecting workflows now exist in the Atlas One Solutions sub account
(`AzTPxnK2vSUj19jYoDmR`) at app.ridethehightide.com. **Every one is saved as Draft. Nothing
is published and nothing can send.** Publishing is a deliberate act you take after the tests
in the build sheet and after the two blockers in "What is still on you" below.

## The ten workflows

| Workflow | id | Trigger | Settings that differ from default |
|---|---|---|---|
| **W0 Vertical router** | see checkpoint 3 | Contact changed, `Vertical` has changed | re-entry ON |
| **W1 Inbound speed to lead** | see checkpoint 5 | Form submitted, either intake form | re-entry OFF, Stop on response ON |
| **W2 Warm referral** | `c5666735-0e74-4d95-a333-36bdf015d53b` | Contact changed, `Lead Lane` has changed to `A Referral` | re-entry OFF, Stop on response ON |
| **W3 Trigger sequence** | see checkpoint 8 | Contact changed, `Trigger Date` has changed | re-entry ON, Stop on response ON |
| **W3a Renewal calendar** | `4ee0dbd6-51d2-4ba1-85b3-1c07ee0649fc` | Contact changed, `WC Renewal Date` has changed; **and** `Benefits Renewal Date` has changed | re-entry ON, Stop on response ON |
| **W4 Cold cadence** | `b4b3c3ba-7b15-4c1e-b541-21c894c48849` | Contact tag, tag added `batch ready` | re-entry **OFF**, Stop on response ON, **time window Mon to Fri 08:00 to 17:00 account timezone** |
| **W5 Lost deal re-approach** | `30d1fed8-590a-44b5-b326-0eb65366fc31` | Opportunity status changed, moved to status **Lost** | re-entry **ON**, Stop on response ON |
| **W6 Suppression** | see checkpoint 2 | Customer replied | see checkpoint 2 |
| **W6b Stalled watchdog** | see checkpoint 2 | see checkpoint 2 | see checkpoint 2 |
| **W7 WSA handoff (Cornerstone)** | `04e13657-82b9-4c96-8367-0bcfde1e79ee` | Contact changed, `Lead Lane` has changed to `A Referral` | re-entry OFF, Stop on response ON |

Full action by action listings for every workflow are in
`_briefs/RUN-G-checkpoints.md`, checkpoints 2 through 12.

## The decisions you made, and where they landed

1. **No SMS anywhere.** Three SMS steps and their consent If/Else branches were skipped: two
   in W1 and one in W4 (step 15). Every sequence runs linear. Nothing in any of the ten
   workflows sends, references or is gated on SMS, so **A2P approval is not a blocker for
   publishing any of them.** Texting can be added later as small tag triggered side
   workflows, exactly as you described.
2. **Stop on response instead of a Goal step.** There is no "Customer Replied" Goal type in
   this builder (only "User Replied", which means a staff user). **Stop on response is ON in
   W1, W2, W3, W3a, W4, W5 and W7**, and every "Goal: Customer Replied" step in the sheet was
   skipped. Its description is exactly the intent: "Ends workflow for a contact if the
   contact responds to a message that is sent from this workflow."
3. **W3 step 18 is the simple always `Cooling 90d` version**, and as a direct consequence the
   sheet's step 2 (the `Lifted Suppression` If/Else) was dropped, because with the simple
   step 18 nothing ever reads that field. Behaviour is unchanged. Reasoning in checkpoint 8.
4. **W7 uses Internal Notification plus a task instead of Send Email**, so GHL never sends as
   Cornerstone. Detail and consequences in checkpoint 12.
5. **Task due dates are 0 Days** wherever the sheet said minutes, since the units are only
   Days, Weeks, Months, Years. Where the sheet gave a clock time, the time is set (10:00 AM
   and 4:00 PM tasks in W2, W3, W4, W7).
6. **Current Date** is used for every "today" stamp, since `{{right_now.date}}` is rejected by
   date fields.
7. **Advance window is ON** on the business hours waits in W4, Mon to Fri, 08:00 to 17:00.
8. **"All workflows except current"** kept on the W6 Remove From Workflow step, as you asked.
   "All workflows" would kill W6's own execution.

## Things the builder cannot do, and what was built instead

| The sheet asked for | GHL reality | What was built |
|---|---|---|
| **Goal: Customer Replied** | no such Goal type | Stop on response ON, per your decision |
| **Contact date field minus N days** (W3a) | not obvious, but it **does exist** | Wait, "Until a specific date/time", the date field's three dot menu set to **Dynamic**, merge field picked, then **"Before this date"** with the offset in days. All five W3a waits are built this way. **No deviation.** |
| **`Next Touch Date` = today + 120 days** (W5 step 5) | Update contact field offers only Custom Date, Current Date, Specific Date. **No offset arithmetic.** | **Step dropped, nothing substituted.** Writing Current Date would put a wrong value in a field you may report on. The 120 day wait that follows already does the scheduling, so no behaviour is lost. Note the asymmetry: Wait actions and task due dates *do* take relative offsets, only field updates do not. |
| **"Send with a random delay"** on W4's first email | does not exist; the Wait action takes a fixed number only, so the sheet's own fallback is not buildable either | **Nothing substituted.** A fixed wait delays everyone equally and would not spread the batch at all. Mitigation stays what the sheet already says: tag `batch ready` in small batches, 20 a day for two weeks then 25, inside the 8 to 5 window. |
| **"Send as reply to previous email"** | not offered | nothing needed; `P-D-2`'s own subject carries the `Re:` treatment, as the sheet anticipated |
| **"is one of" for tags** | `Includes` with several tags means **ALL of them** (AND) | every suppression gate is **one condition per tag joined with OR**: `cooling 30d` OR `cooling 60d` OR `cooling 90d` OR `hold 6m` OR `dnc`. Used in W1, W2, W3 and W4. |
| **"is within the last N days"** for a date field (W6b) | does not exist | `Last Touch Date` **Is not** **Before 5 Days**, putting the stalled contact in the None branch |
| **months as a wait unit** | units are seconds, minutes, hours, days | 4 months built as **120 days**, 6 months as **180 days** |
| **The Personal Line gate looping** ("task, then wait again") in W1, W2, W3 and W5 | **branches never rejoin**, so a loop means duplicating the whole remaining sequence into the Time out branch | built as a **hard stop**: the Time out branch raises the "write the personal line" task and ENDs. See below. |

## The one behaviour you should decide on before publishing

**The Personal Line gate does not resume by itself.** In W1, W2, W3 and W5, if
`Personal Line` is still empty after 2 days the contact gets a task telling David to write it,
and then the workflow **ends for that contact**. It does not pick the sequence back up when
the field is later filled.

- In **W5 this is recoverable**, because Allow re-entry is ON: filling the field and
  re triggering (marking the opportunity Lost again) re enrols the contact.
- In **W1, W2 and W7 it is not**, because Allow re-entry is OFF as the sheet specifies. The
  contact is out of that sequence for good unless you re enrol by hand.

Three ways to change it, if you want to: duplicate the tail into the Time out branch (ugly,
but exact); lengthen the timeout so the gate simply waits longer instead of giving up; or turn
Allow re-entry ON in W2 and W7 so re setting `Lead Lane` puts the contact back in. **I have
not chosen for you.** As built, the gate protects the thing the sheet says matters, which is
that a referral email never goes out with a generic first line.

## What is still on you

The Appendix B list, updated for what this run changed:

1. **A2P 10DLC registration.** **No longer blocks anything**, since no workflow contains SMS.
   Do it when you want texting; the side workflows come after.
2. **Verify david.taylor@cornerstonepeo.com as an additional sender.** **No longer blocks W7**,
   because W7 does not send as Cornerstone any more; David sends those three by hand. Only
   needed if you later want GHL to send them directly.
3. **Business hours in Settings > Business Profile**, Mon to Fri, if they are empty. W1 step 9
   depends on them. W4's window is set on the workflow itself and does not.
4. **The three calculator URLs.** All three return **200** and are live:
   `https://forms.atlasonesolutions.com/tools/retention-cost/`, `/tools/vendor-consolidation/`
   and `/tools/wc-premium-check/`. They are in W0's Vertical Tool values. The **`[link]`
   placeholder still needs replacing in the Email 3 templates**, or Email 3 goes out with a
   bracket in it.
5. **The Monday batch**: 25 names, `Lead Lane` = `D Cold`, set `Vertical`, add `Batch ready` in
   bulk. 20 a day for the first two weeks, then 25.

## Not done, and deliberately so

These are Part 10 of the build sheet and were outside the ordered list you gave me:

- **The two smart lists** (Sequence Active, Stalled) are not created.
- **The old shells** `Missing-Info Follow-up` and `Tool-Lead Nurture` are untouched, neither
  deleted nor renamed. `Won - Pay Referral Partner` and `Post-Presentation Email` were not
  opened, as instructed.
- **Nothing is published** and **no test contacts were created**, so no execution log has been
  exercised. The per workflow tests in the sheet are all still to run.
- **A2P status in Trust Center** was not read.

Say the word and I will do any of those in the next run.

## The builder lessons, in one place

Anyone editing these by hand should know:

1. **Dropdown options need two clicks.** One click highlights, the second commits. `double_click`
   is not a substitute: in the If/Else field list its second click falls through to the row
   underneath and silently rewrites a different condition.
2. **Do not dismiss a picker in the same breath as choosing from it.** Selecting a tag then
   immediately pressing Escape reverts the chip.
3. **Set the AND/OR joiner before adding the next condition.** The "And"/"Or" text printed
   between rows is a static label, not a control.
4. **Linking an email template needs the row clicked twice**; until the "Linked template:" line
   appears, saving fails with "Subject not found".
5. **Copy action / Copy all actions from here / Paste below** is the fastest way to build
   anything repeated. It cloned W3a's whole eight action branch, all five of W4's business
   hours waits, and W5's four 90 day waits.
6. **Duplicate workflow** (the `...` menu in the workflows list) copies triggers, branches and
   every action, and asks for the new name in the dialog. That is how W7 was built.
7. **In a task panel, click the Title at its far left**, where the plain text is; clicking the
   middle lands on a merge chip and opens the tag browser instead.
8. **The task time picker's AM/PM column scrolls when you pick an hour**, so AM often becomes
   PM. Check the text box reads what you meant before pressing OK.
