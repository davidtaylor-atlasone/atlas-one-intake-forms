# Atlas One prospecting workflows: click list for the GHL workflow builder

Written 8 Sep 2026. This is the hand-build companion to
`Atlas_One_GHL_Prospecting_Workflows_Runbook.md`. The runbook explains why; this sheet is
what to click, in order, with the exact value for every box.

Everything happens at **app.ridethehightide.com** (not app.gohighlevel.com), sub-account
**Atlas One Solutions**, location `AzTPxnK2vSUj19jYoDmR`, under **Automation > Workflows**.

Build them in the order below. Each one is self contained; you can stop after any of them.

---

## Before you start

**These must already exist** (Settings > Custom Fields, folder `Prospecting`, and
Settings > Tags). Anything missing here will not appear in the workflow dropdowns.

Fields, all on the **Contact** object:

| Field | Type | Merge token |
|---|---|---|
| Lead Lane | Dropdown (single): A Referral, B Trigger, C Inbound, D Cold, E Lost | `{{contact.lead_lane}}` |
| Brand Identity | Dropdown (single): Atlas One, Cornerstone | `{{contact.brand_identity}}` |
| Vertical | Dropdown (single): Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional Services, Other | `{{contact.vertical}}` |
| Trigger Type | Dropdown (single): WC renewal, Benefits renewal, New location, Hiring, Ownership change, Vendor complaint, Other | `{{contact.trigger_type}}` |
| Trigger Date | Date picker | `{{contact.trigger_date}}` |
| WC Renewal Date | Date picker | `{{contact.wc_renewal_date}}` |
| Benefits Renewal Date | Date picker | `{{contact.benefits_renewal_date}}` |
| Next Touch Date | Date picker | `{{contact.next_touch_date}}` |
| Last Touch Date | Date picker | `{{contact.last_touch_date}}` |
| Sequence Step | Number | `{{contact.sequence_step}}` |
| Personal Line | Multi line | `{{contact.personal_line}}` |
| Vertical Opener | Multi line | `{{contact.vertical_opener}}` |
| Vertical Proof | Multi line | `{{contact.vertical_proof}}` |
| Vertical Tool | Single line | `{{contact.vertical_tool}}` |
| Referral Partner Name | Single line | `{{contact.referral_partner_name}}` |
| Lifted Suppression | Checkbox, one option `Yes` | `{{contact.lifted_suppression}}` |

**All 16 are built and verified through the API as of 8 Sep 2026.** They live in the
Contact folder `Prospecting` (folder id `ra4rylFUwAUV611f1VrS`).

> `Referral Partner Name` is the **contact** field. There is also a `Referral Partner`
> dropdown on the **Opportunity** object; they are not the same thing and the contact one
> is what these workflows use. W2 is triggered by a contact field change, so it has no
> opportunity in context and `{{opportunity.referral_partner}}` would merge as blank.
> Leave the Opportunity one alone, the Won - Pay Referral Partner workflow uses it.

> `Lifted Suppression` is a CHECKBOX with a single option, `Yes`. In an If/Else, the
> condition reads `Lifted Suppression` **contains** `Yes`; to set it, Update Contact Field
> to `Yes`; to clear it, set it empty.

Tags: all 11 exist already. GHL stores tag names lowercase, so they appear as
`sms consent`, `cell verified`, `cooling 30d`, `cooling 60d`, `cooling 90d`, `hold 6m`,
`dnc`, `sequence active`, `batch ready`, `reply received`, `not interested`. Pick them
from the dropdown rather than typing them, so you never create a near miss.

**Email templates.** All the `P-` templates named in this sheet are built and verified in
Marketing > Emails > Templates. Three names differ slightly from the runbook, use these:
`P-E-Q1 Quarterly tool`, `P-E-Q2 Quarterly law change`, `P-E-Q3 Quarterly proof story`.

> **Watch for duplicates when you pick a template.** Three names currently appear twice in
> the template list: `P-A-3 Referral Email 3`, `P-B-1 Trigger Email 1` and
> `P-B-2 Trigger Email 2`. The verified copies are the ones listed in the report file;
> delete the other copy of each before you build the workflows, or you will pick the wrong
> one at random. There is also a stray called `New Template`.

> **`Instant auto-reply` does not exist** in the email builder, and neither do
> `Moving forward` or C1/C2/C3. W1 step 5 calls for it. Either build it first, or swap
> that step for `P-C-2 Inbound Email 2` and drop step 12.

**Rules that apply to every workflow below**

1. **No text sends until A2P is Approved.** Settings > Phone Numbers > Trust Center.
   Build every Send SMS action anyway, then set the toggle on the action card to
   **disabled**. Turn them on only after the campaign reads Approved.
2. **Never tag `SMS consent` by hand.** It comes from the form checkbox or a recorded
   verbal yes, nothing else.
3. **Save is not Publish.** The Publish toggle is top right. Save while you build, publish
   only after the test in that section passes.
4. **One trigger per value.** Filters inside a single trigger are ANDed, so "Form A or
   Form B" is two triggers, not one trigger with two filters.
5. **Emails are picked, not written.** Every Send Email step selects an existing template
   from Marketing > Emails > Templates. If the template is not built yet, build it first.
6. **The Goal step goes at the top**, before the first wait, on every sequence workflow.

**Where to find each control in the builder:** click the **+** under the trigger to add an
action, then pick the action type from the list. "Wait" is under Timing. "If/Else" is under
Conditions. "Goal" is the flag icon on the canvas toolbar.

---

## W6 Suppression and caps

**Build this first.** It is the brake, and nothing else should be live without it.

**Create:** Automation > Workflows > Create workflow > Start from scratch.
**Name:** `W6 Suppression and caps`
**Settings (gear, top right):** Allow re-entry **ON**.

**Triggers** (three separate triggers, added one at a time):
1. **Customer Replied** with channel: Any.
2. **Contact Tag Added** with filter: Tag **is** `Not interested`.
3. **Contact Tag Added** with filter: Tag **is** `DNC`.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | Remove Contact Tag | Tag: `Sequence Active` |
| 2 | Remove From Workflow | Choose **All workflows** |
| 3 | If/Else | Branch 1 condition: Contact Tag **is** `DNC`. Branch 2 condition: Contact Tag **is** `Not interested`. Else: everything else (a reply). |
| 3a | *(inside Branch 1, DNC)* Update Contact Field | Field: `Next Touch Date`, value: **empty / clear** |
| 3b | *(inside Branch 1)* End | Leave the branch with no further steps |
| 3c | *(inside Branch 2, Not interested)* Add Contact Tag | Tag: `Hold 6m` |
| 3d | *(inside Branch 2)* Wait | **6 months** |
| 3e | *(inside Branch 2)* Remove Contact Tag | Tag: `Hold 6m` |
| 3f | *(inside Else, a reply)* Add Contact Tag | Tag: `Reply received` |
| 3g | *(inside Else)* Create Task | Title: `Reply from {{contact.first_name}} {{contact.last_name}}: read and respond`. Assigned to: David. Due: **today**. |
| 4 | Internal Notification | To: David, channel SMS or app push. Body: `Reply from {{contact.company_name}}` |

**Publish.**

**Test:** on a test contact, add the tag `Not interested`. In Automation > Execution logs
the contact should show W6 running, `Sequence Active` removed, `Hold 6m` added.

---

## W6b Sequence stalled

**Create:** new workflow from scratch.
**Name:** `W6b Sequence stalled`
**Settings:** Allow re-entry **ON**.

**Trigger:** Contact Tag Added with filter: Tag **is** `Sequence Active`.

**Actions:**

| # | Action type | Settings |
|---|---|---|
| 1 | Wait | **5 days** |
| 2 | If/Else | Condition: `Last Touch Date` **is within the last** 5 days |
| 2a | *(if true)* End | No steps |
| 2b | *(else)* Create Task | Title: `Sequence stalled: {{contact.company_name}}`. Assigned to David, due today. |

**Publish.**

---

## W0 Set vertical lines

The lookup table the templates read from. Build it before any sequence that merges
`{{contact.vertical_opener}}`, `{{contact.vertical_proof}}` or `{{contact.vertical_tool}}`.

**Create:** new workflow from scratch.
**Name:** `W0 Set vertical lines`
**Settings:** Allow re-entry **ON**.

**Trigger:** Contact Field Updated on field: `Vertical` (any value).

**Action 1: If/Else** with **seven** branches, one per Vertical value. In each branch add
three **Update Contact Field** steps in this order: Vertical Opener, Vertical Proof,
Vertical Tool. The exact text for all 21 boxes is in **Appendix A** at the end of this
sheet; paste it in, do not retype it.

Branch order (the seventh is the Else):
1. Vertical **is** `Audiology`
2. Vertical **is** `Dental Ortho Optometry ENT`
3. Vertical **is** `Construction`
4. Vertical **is** `Technology`
5. Vertical **is** `Hospitality`
6. Vertical **is** `Professional Services`
7. Else (covers `Other` and blank): use the generic set

**Publish.**

**Test:** set Vertical = Construction on a test contact, then reopen the contact. The three
fields should be filled with the Construction text within a few seconds.

---

## W1 Inbound speed to lead (lane C)

**Create:** new workflow from scratch.
**Name:** `W1 Inbound speed to lead`
**Settings:** Allow re-entry **OFF**.

**Triggers:**
1. **Form Submitted** with filter: Form **is** `PEO / Prospect Quote Request` (Form A).
2. **Form Submitted** with filter: Form **is** Form B.
3. *(optional)* **Inbound Webhook** (only if you want tool captures in this workflow
   rather than Tool-Lead Nurture). Skip it for now.

> Filter every Form Submitted trigger to its form. An unfiltered one fires on every form
> on the site, including the intake forms.

**Goal step (add first, at the top of the canvas):** Event **Customer Replied**, on match
**skip to end**.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | Update Contact Field | `Lead Lane` = `C Inbound` |
| 2 | Add Contact Tag | `Sequence Active` |
| 3 | Update Contact Field | `Last Touch Date` = `{{right_now.date}}` |
| 4 | If/Else | Condition: Contact Tag **is one of** `Cooling 30d`, `Cooling 60d`, `Cooling 90d`, `Hold 6m`, `DNC` |
| 4a | *(if true)* Create Task | Title: `Inbound from a suppressed contact: {{contact.company_name}}. Decide by hand.` Assigned David, due today. |
| 4b | *(if true)* End | Stop the branch here. Inbound is the one lane where a human decides. |
| 5 | Send Email | Template: **Instant auto-reply** (already built, pick it) |
| 6 | If/Else | Condition: Contact Tag **is** `SMS consent` |
| 6a | *(if true)* Send SMS | Body: `Got it. I'll call you within the hour. If now is bad, reply with a better time. Reply STOP to opt out.` **Set the card toggle to disabled.** |
| 7 | Create Task | Title: `CALL NOW: {{contact.company_name}} {{contact.phone}}. {{contact.services_requested}}`. Assigned David. Due: **in 5 minutes**. |
| 8 | Internal Notification | To David's phone. Same text as the task title. |
| 9 | Wait | **4 hours**, tick **Only during business hours** |
| 10 | If/Else | Condition: Contact Tag **is** `Reply received` |
| 10a | *(if true)* End | |
| 10b | *(else)* Create Task | Title: `Call 2 + voicemail: {{contact.company_name}}`. Due **today 3:00 PM**. |
| 11 | Wait | **1 day** |
| 12 | Send Email | Template: `P-C-2 Inbound Email 2` |
| 13 | Wait | **2 days** |
| 14 | Create Task | Title: `Call 3: {{contact.company_name}}`. Due today. |
| 15 | If/Else | Condition: Contact Tag **is** `SMS consent` |
| 15a | *(if true)* Send SMS | Body: `{{contact.first_name}}, David at Atlas One. Still want the net number? Reply with a day and I'll send the invite. Reply STOP to opt out.` **Disabled.** |
| 16 | Wait | **3 days** |
| 17 | Send Email | Template: `P-C-3 Inbound Email 3` |
| 18 | Add Contact Tag | `Cooling 30d` |
| 19 | Remove Contact Tag | `Sequence Active` |
| 20 | Wait | **30 days** |
| 21 | Remove Contact Tag | `Cooling 30d` |

**Business hours:** step 9 needs Settings > Business Profile to have hours set (Mon to Fri,
8:30 AM to 5:00 PM, Mountain). If they are empty the wait behaves as a plain 4 hours.

**Publish.**

**Test:** submit Form A with your own email and company "TEST Atlas". Expect the
auto-reply in Outlook, the CALL NOW task on your phone inside a minute, and the contact
showing Lead Lane = C Inbound with tag `Sequence Active`.

---

## W2 Warm referral (lane A)

**Create:** new workflow from scratch.
**Name:** `W2 Warm referral`
**Settings:** Allow re-entry **OFF**.

**Trigger:** Contact Field Updated on field `Lead Lane`, value **is** `A Referral`.

**Goal step at the top:** Customer Replied, on match **skip to end**.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | If/Else | Condition: `Brand Identity` **is** `Cornerstone` |
| 1a | *(if true)* End | Cornerstone referrals belong to W7, not here. This is the mirror of W7's gate, and it is what keeps a contact from running both. |
| 2 | If/Else | Condition: Contact Tag **is one of** `Cooling 30d`, `Cooling 60d`, `Cooling 90d`, `Hold 6m`, `DNC` |
| 2a | *(if true)* Create Task | `Referral for a suppressed contact: {{contact.company_name}}. Decide by hand.` Then End. |
| 3 | Add Contact Tag | `Sequence Active` |
| 4 | Update Contact Field | `Sequence Step` = `1` |
| 5 | Create Task | Title: `Reply-all to the intro within 1 hour: {{contact.company_name}} (referred by {{contact.referral_partner_name}})`. Due: **in 1 hour**. |
| 6 | Wait | **Event / condition**: Contact Field Updated, `Personal Line` **is not empty**. Timeout: **2 days**. |
| 6a | *(on timeout)* Create Task | `Write the personal line for {{contact.company_name}}`, due today. Then a second **Wait** on the same condition, timeout 2 days. |
| 7 | Create Task | `Call + voicemail 1: {{contact.company_name}}`. Due **today 10:00 AM**. |
| 8 | Send Email | Template: `P-A-1 Referral Email 1` |
| 9 | Update Contact Field | `Last Touch Date` = `{{right_now.date}}` |
| 10 | Wait | **2 days** |
| 11 | Create Task | `Call 2, different hour: {{contact.company_name}}`. Due **today 4:00 PM**. |
| 12 | Wait | **2 days** |
| 13 | Send Email | Template: `P-A-2 Referral Email 2` |
| 14 | Update Contact Field | `Last Touch Date` = `{{right_now.date}}` |
| 15 | Wait | **3 days** |
| 16 | Create Task | `Call + voicemail 2: {{contact.company_name}}`. Due today. |
| 17 | Wait | **2 days** |
| 18 | Send Email | Template: `P-A-3 Referral Email 3` |
| 19 | Create Task | `Tell {{contact.referral_partner_name}} you could not reach {{contact.company_name}}`. Due today. |
| 20 | Add Contact Tag | `Cooling 60d` |
| 21 | Remove Contact Tag | `Sequence Active` |
| 22 | Wait | **60 days** |
| 23 | Remove Contact Tag | `Cooling 60d` |

> **Step 6 is the approval gate.** Email 1 will not send until David types the personal
> sentence into the Personal Line field on the contact. That is deliberate; a referral
> email with a generic first line wastes the referral.

**Publish.**

---

## W7 WSA handoff (Cornerstone)

Build it as a **duplicate of W2** (three dot menu on W2 > Duplicate), then change what is
listed here. Everything not listed stays as W2 built it.

**Name:** `W7 WSA handoff (Cornerstone)`
**Settings:** Allow re-entry **OFF**.

**Trigger:** same as W2: Contact Field Updated, `Lead Lane` **is** `A Referral`.

**Changes from W2:**

| # | What changes | To |
|---|---|---|
| 1 | Action 1's If/Else | Condition becomes `Brand Identity` **is** `Cornerstone`. **If true, continue**; **else End**. (W2 is the exact opposite, so a contact runs one or the other, never both.) |
| 5 | Task title | `WSA: reply-all to Zak's intro within 1 hour: {{contact.company_name}}` |
| 7 | Task title | `WSA: call + voicemail 1: {{contact.company_name}}` |
| 8 | Email template | `P-W7-1 WSA Email 1` |
| 11 | Task title | `WSA: call, different hour: {{contact.company_name}}` |
| 13 | Email template | `P-W7-2 WSA Email 2` |
| 16 | Task title | `WSA: call + voicemail 2: {{contact.company_name}}` |
| 18 | Email template | `P-W7-3 WSA Email 3` |
| 19 | Task title | `Tell Zak Call at WSA you could not reach {{contact.company_name}}` |

**On all three Send Email cards in W7**, set:
- **From name:** `David Taylor, Cornerstone PEO`
- **From address:** `david.taylor@cornerstonepeo.com`

That address must be verified first: Settings > Email Services > add it as an additional
sender; GHL emails a verification link to that mailbox and David has to click it. Until
then the three emails will fall back to the Atlas One sender, which is wrong for this
channel.

**Guardrails baked into the W7 templates:** Cornerstone identity only, PEO scope only,
never Atlas One, never Hearvana, never the credit mechanics. Present the credit **total**
only.

**Publish.**

**Test:** a test contact with `Brand Identity` = Cornerstone, then set `Lead Lane` =
A Referral. The execution log should show W7 running and **W2 ending at action 1**. Leave
Personal Line empty and confirm the sequence stops at the gate, then fill it and confirm
Email 1 sends.

---

## W3 Trigger sequence (lane B)

**Create:** new workflow from scratch.
**Name:** `W3 Trigger sequence`
**Settings:** Allow re-entry **ON**. (It runs once per trigger event; the 90 day cooling at
the end plus the gate at the top stop it looping.)

**Trigger:** Contact Field Updated on field `Trigger Date` (any value).

**Goal step at the top:** Customer Replied, skip to end.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | If/Else | Condition: Contact Tag **is** `DNC` |
| 1a | *(if true)* End | DNC is absolute. |
| 2 | If/Else | Condition: Contact Tag **is one of** `Cooling 30d`, `Cooling 60d`, `Cooling 90d`, `Hold 6m` |
| 2a | *(if true)* Update Contact Field | `Lifted Suppression` = `Yes`. Then continue. A real trigger outranks a cooling period; step 8 puts the tag back. |
| 3 | Add Contact Tag | `Sequence Active` |
| 4 | Wait | Event: Contact Field Updated, `Personal Line` **is not empty**. Timeout **2 days**, then task `Write the personal line for {{contact.company_name}}` and wait again. |
| 5 | Create Task | `Call + voicemail: {{contact.company_name}}, trigger {{contact.trigger_type}}`. Due today 10:00 AM. |
| 6 | Send Email | Template: `P-B-1 Trigger Email 1` |
| 7 | Update Contact Field | `Last Touch Date` = `{{right_now.date}}` |
| 8 | Wait | **2 days** |
| 9 | Send Email | Template: `P-B-2 Trigger Email 2` |
| 10 | Wait | **2 days** |
| 11 | Create Task | `Call, no voicemail: {{contact.company_name}}`. Due today 4:00 PM. |
| 12 | Wait | **2 days** |
| 13 | Create Task | `Call: {{contact.company_name}}`. Due today. |
| 14 | Send Email | Template: `P-B-3 Trigger Email 3` |
| 15 | Wait | **1 day** |
| 16 | Send Email | Template: `P-B-4 Trigger close` |
| 17 | Remove Contact Tag | `Sequence Active` |
| 18 | If/Else | Condition: `Lifted Suppression` **contains** `Yes` |
| 18a | *(if true)* If/Else, three branches | Re-add whichever tag was lifted: branch on `Cooling 30d` / `Cooling 60d` / `Cooling 90d` / `Hold 6m` as recorded, Add Contact Tag for that one, then Update Contact Field `Lifted Suppression` empty. |
| 18b | *(else)* Add Contact Tag | `Cooling 90d`, then **Wait 90 days**, then Remove Contact Tag `Cooling 90d` |

> Step 18a is the fiddly one. If you want it simpler and can live with a slightly blunter
> rule, replace 18 entirely with: Add Contact Tag `Cooling 90d`, Wait 90 days, Remove
> Contact Tag `Cooling 90d`, and skip the `Lifted Suppression` field. The only cost is that
> a contact who was in `Hold 6m` comes back after 90 days instead of the rest of the six
> months. Decide before you build it, not after.

**Publish.**

---

## W3a Renewal calendar

The thing that makes lane B fire on its own, a year at a time.

**Create:** new workflow from scratch.
**Name:** `W3a Renewal calendar`
**Settings:** Allow re-entry **ON**.

**Triggers:**
1. Contact Field Updated on field `WC Renewal Date` (any value).
2. Contact Field Updated on field `Benefits Renewal Date` (any value).

**Action 1: If/Else**: Branch 1: `WC Renewal Date` **is not empty**. Branch 2:
`Benefits Renewal Date` **is not empty**. Build the same five steps inside each branch,
swapping the field name and the Trigger Type value.

**Inside the WC branch:**

| # | Action type | Settings |
|---|---|---|
| 1 | Wait | Type: **Contact date field**. Field: `WC Renewal Date`. Offset: **120 days before**. |
| 2 | Send Email | Template: `P-B-120 Renewal heads-up` |
| 3 | Wait | Contact date field `WC Renewal Date`, **90 days before** |
| 4 | Update Contact Field | `Trigger Type` = `WC renewal` |
| 5 | Update Contact Field | `Trigger Date` = `{{contact.wc_renewal_date}}` |
| 6 | Wait | Contact date field `WC Renewal Date`, **60 days before** |
| 7 | Create Task | `Last window to quote: {{contact.company_name}}`. Due today. |
| 8 | Send Email | Template: `P-B-60 Last window` |

**Inside the Benefits branch:** identical, with `Benefits Renewal Date` as the wait field,
`Trigger Type` = `Benefits renewal`, and `Trigger Date` = `{{contact.benefits_renewal_date}}`.

> Steps 4 and 5 are what hands off to W3: writing Trigger Date fires W3's trigger, so the
> lane B sequence starts on its own at renewal minus 90. Do not also add a "start
> workflow" action; you would run it twice.

**Publish.**

**Test:** on a test contact set `WC Renewal Date` to a date **100 days out**. In the
execution log the minus 120 wait should already have passed, and the **minus 90 wait
should show as scheduled** with a date 10 days from now.

---

## W4 Cold cadence (lane D)

Nine touches over 14 business days, then a 90 day rest.

**Create:** new workflow from scratch.
**Name:** `W4 Cold cadence`
**Settings:**
- Allow re-entry **OFF**.
- **Time window:** Mon to Fri, 8:00 AM to 5:00 PM, Mountain.

**Trigger:** Contact Tag Added with filter: Tag **is** `Batch ready`.

**Goal step at the top:** Customer Replied, skip to end.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | If/Else | Condition: Contact Tag **is one of** `Cooling 30d`, `Cooling 60d`, `Cooling 90d`, `Hold 6m`, `DNC` |
| 1a | *(if true)* Remove Contact Tag | `Batch ready` |
| 1b | *(if true)* Create Task | `Skipped, suppressed: {{contact.company_name}}`. Then End. |
| 2 | Remove Contact Tag | `Batch ready` |
| 3 | Add Contact Tag | `Sequence Active` |
| 4 | Update Contact Field | `Sequence Step` = `1` |
| 5 | Create Task | `Call + VM1 10 AM: {{contact.company_name}}`. Due **today 10:00 AM**. |
| 6 | Send Email | Template: `P-D-1 Cold Email 1`. Tick **Send with a random delay** (or add a Wait of 1 to 60 minutes, random) so the batch does not all fire on the same minute. |
| 7 | Update Contact Field | `Last Touch Date` = `{{right_now.date}}` |
| 8 | Wait | **2 days**, tick **business hours only** |
| 9 | Send Email | Template: `P-D-2 Cold Email 2`. Tick **Send as reply to previous email** if the builder offers it; if not, the template's subject is already `Re: ...`. |
| 10 | Wait | **2 days**, business hours only |
| 11 | Create Task | `Call, no VM, 4 PM: {{contact.company_name}}`. Due **today 4:00 PM**. |
| 12 | Wait | **2 days**, business hours only |
| 13 | Create Task | `Call + VM2, 10 AM: {{contact.company_name}}`. Due today 10:00 AM. |
| 14 | Send Email | Template: `P-D-3 Cold Email 3` |
| 15 | If/Else | Condition: Contact Tag **is** `SMS consent` |
| 15a | *(if true)* Send SMS | Body: `{{contact.first_name}}, David at Atlas One. Sent you the calculator this morning; it takes three minutes and it's yours either way. Reply with a time if you want me to walk through it. Reply STOP to opt out.` **Disabled.** |
| 16 | Wait | **2 days**, business hours only |
| 17 | Create Task | `LinkedIn note or handwritten card (top accounts only): {{contact.company_name}}`. Due today. |
| 18 | Wait | **2 days**, business hours only |
| 19 | Create Task | `Call 3, 4 PM, last live attempt: {{contact.company_name}}`. Due today 4:00 PM. |
| 20 | Wait | **3 days**, business hours only |
| 21 | Send Email | Template: `P-D-4 Cold breakup` |
| 22 | Add Contact Tag | `Cooling 90d` |
| 23 | Remove Contact Tag | `Sequence Active` |
| 24 | Wait | **90 days** |
| 25 | Remove Contact Tag | `Cooling 90d` |

**Warm-up cap.** The sending domain `lc.atlasonesolutions.com` is new. For the **first two
weeks** W4 exists, tag no more than **20 contacts a day** with `Batch ready`; from week
three, 25. Put that in the calendar. Lanes A, B, C and E are low volume and are not
capped.

**Publish.**

**Test:** one test contact, tag `Batch ready`. The execution log should show all nine
touches laid out with business-day waits, and the first email should carry the branded
wrapper in Outlook.

---

## W5 Lost deal re-approach (lane E)

Four touches a year, forever, at the lowest cadence in the system.

**Create:** new workflow from scratch.
**Name:** `W5 Lost deal re-approach`
**Settings:** Allow re-entry **ON**.

**Trigger:** Opportunity Status Changed, to **Lost**, any pipeline.

**Goal step at the top:** Customer Replied, skip to end.

**Actions, in order:**

| # | Action type | Settings |
|---|---|---|
| 1 | Update Contact Field | `Lead Lane` = `E Lost` |
| 2 | Create Task | `Record: provider chosen, reason, renewal date, the one thing they wanted: {{contact.company_name}}`. Due today. |
| 3 | Wait | Event: Contact Field Updated, `Personal Line` **is not empty**. Timeout 2 days, then task, then wait again. |
| 4 | Send Email | Template: `P-E-0 Gracious close` |
| 5 | Update Contact Field | `Next Touch Date` = **today + 120 days** |
| 6 | Wait | **4 months** |
| 7 | Send Email | Template: `P-E-4 Month four` |
| 8 | Wait | **90 days** |
| 9 | Send Email | Template: `P-E-Q1 Quarterly tool` |
| 10 | Wait | **90 days** |
| 11 | Send Email | Template: `P-E-Q2 Quarterly law change` |
| 12 | Wait | **90 days** |
| 13 | Send Email | Template: `P-E-Q3 Quarterly proof story` |
| 14 | Wait | **90 days** |
| 15 | Send Email | Template: `P-E-Q1 Quarterly tool` |
| 16 | End | Four a year is the ceiling. |

> When a renewal date is later set on one of these contacts, **W3a takes over on its own**
> and the lane B sequence runs at renewal minus 90. That is the intended path back in; do
> not add a renewal branch here.

**Publish.**

---

## Part 10: the old shells, the smart lists, and the final check

**Old workflows:**
- **Missing-Info Follow-up** and **Tool-Lead Nurture** are empty shells. Either delete
  them, or leave them in Draft and rename them with ` (superseded by W1)` on the end.
- **Won - Pay Referral Partner** and **Post-Presentation Email** stay exactly as they are.
  Do not open them.
- The four booking workflows and the intake forms are out of scope. Leave them alone.

**Two smart lists** (Contacts > Smart Lists > new):
1. **Sequence Active** with filter: Tag **is** `Sequence Active`.
2. **Stalled** with filters: Tag **is** `Sequence Active` **AND** `Last Touch Date`
   **is before** 5 days ago.

**Final check, all of it in one pass:**
- Every SMS action card shows **disabled**, in W1 (two of them) and W4 (one).
- Settings > Phone Numbers > Trust Center: record the A2P status in the report.
- Published: W0, W1, W2, W3, W3a, W4, W5, W6, W6b, W7: ten workflows, each with its
  trigger noted.
- Delete the test contacts.

---

## Appendix A: the W0 vertical values

Paste these into the three Update Contact Field steps in each W0 branch. No dashes, no
em dashes; they merge into email bodies. `[link]` is a placeholder: the free-tool
calculators are not hosted at a public URL yet, so **fill the link in once they are**, or
the Email 3 in every lane will go out with a bracket in it.

### Audiology
- **Vertical Opener:** `Most hearing practices I work with lose about an hour a day per clinician to payroll, benefits and insurance admin. That hour is a fitting.`
- **Vertical Proof:** `A two audiologist practice was running ADP, an accountant and a broker who showed up once a year. The comp classification was wrong, the front desk was spending a full day a month on payroll and benefits questions, and there was no group plan to recruit with. The owner got about six hours a week back and hired a second clinician the next quarter.`
- **Vertical Tool:** `Retention Cost calculator: [link]`

### Dental Ortho Optometry ENT
- **Vertical Opener:** `An open hygiene chair costs a practice about $15,000 to $25,000 a month, and in this market the role takes 60 to 90 days to fill. The practices that fill it fast are the ones that can offer real group benefits and a real onboarding, not just a higher hourly rate.`
- **Vertical Proof:** `A three doctor practice was replacing a front desk person every year and had lost two hygienists to the corporate group down the street. Group benefits through the pool, a corrected comp classification and a real onboarding packet dropped turnover, filled the hygiene schedule, and gave the office manager her Fridays back.`
- **Vertical Tool:** `Retention Cost calculator: [link]`

### Construction
- **Vertical Opener:** `Your workers' comp renewal is the one window where a carrier will actually compete for you, and the mod and the class codes are what decide the number. Most owners find out the number after it is too late to move.`
- **Vertical Proof:** `A 30 man electrical contractor had the expense constant charged in both states, three guys on the wrong class code, and certified payroll eating the office's whole Friday. Fixing the classifications and getting the constant charged once brought the mod down at the next renewal and gave the office a day a week back.`
- **Vertical Tool:** `WC premium check: [link]`

### Technology
- **Vertical Opener:** `A team your size buys health coverage as a group of your headcount. Through a co-employment pool it buys as part of thousands, which is usually the single biggest line I can move for a company your size.`
- **Vertical Proof:** `A 14 person software company was in four states, registered in two, and buying health coverage as a group of 14. Moving them into the pool, cleaning up the registrations and putting a real handbook and onboarding in place dropped the benefits line and closed the next offer letter.`
- **Vertical Tool:** `Vendor Consolidation calculator: [link]`

### Hospitality
- **Vertical Opener:** `Every hourly person a restaurant replaces costs about $10,000 to $17,000 once hiring, training and the slow weeks are counted, and most of those quits happen in the first 90 days. The fix is usually not pay; it is the first week, the schedule, and a couple of benefits a small group can actually afford.`
- **Vertical Proof:** `A resort with about 50 seasonal and year round staff was replacing a third of them every year and running payroll with tips by hand. Tips, comp classes for kitchen and floor, a bilingual onboarding packet and two benefits the group could afford dropped the first 90 day quits and gave the GM a shift a week back.`
- **Vertical Tool:** `Retention Cost calculator: [link]`

### Professional Services
- **Vertical Opener:** `A partner billing $300 an hour who gives three hours a week to payroll, benefits and vendors is $45,000 a year of revenue that did not happen, and the office manager is spending her Fridays on the rest.`
- **Vertical Proof:** `A 12 person firm had a partner spending three hours a week on benefits and vendors, an office manager doing payroll on Fridays, and a remote associate in a state the firm was not registered in. Payroll, pooled benefits and the registrations under one relationship dropped the benefits line, gave the partner the hours back, and moved the office manager to collections.`
- **Vertical Tool:** `Vendor Consolidation calculator: [link]`

### Other (the Else branch, generic)
- **Vertical Opener:** `I work with owners who run payroll, benefits, workers' comp and bookkeeping across four or five vendors. I put it under one relationship with one number to call, and most of it costs you nothing extra because the vendors pay me.`
- **Vertical Proof:** `One owner was paying five separate vendors for payroll, comp and benefits. The Audit found the overlap, fixed the comp classification, and gave the owner hours back every week on top of what it saved.`
- **Vertical Tool:** `Vendor Consolidation calculator: [link]`

---

## Appendix B: what David has to do himself

None of these can be done from a script or a browser session.

1. **A2P 10DLC registration.** Settings > Phone Numbers > Trust Center. Brand: Atlas One
   Solutions LLC, the EIN, the Lehi address, AtlasOneSolutions.com, David as contact. Then
   one Campaign, use case "Mixed" or "Low volume mixed", sample messages from Playbook
   section 5, opt-in description "checkbox on our quote request forms and verbal consent
   recorded in CRM", opt-out "reply STOP". 1 to 10 business days. **No SMS action gets
   enabled until this reads Approved.**
2. **Verify david.taylor@cornerstonepeo.com** as an additional sender: Settings > Email
   Services > add sender. GHL emails a verification link to that mailbox; only David can
   click it. W7 cannot send as Cornerstone until this is done.
3. **Business hours**, if they are empty: Settings > Business Profile, Mon to Fri 8:30 AM
   to 5:00 PM Mountain. W1 step 9 and W4's time window both depend on them.
4. **Host the three calculators** and put their real URLs into the W0 Vertical Tool values
   (Appendix A) and into the Email 3 templates.
5. **The Monday batch:** 25 names, set Lead Lane = D Cold, set Vertical, add tag
   `Batch ready` in bulk. 20 a day for the first two weeks, then 25.
