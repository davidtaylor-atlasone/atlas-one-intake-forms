# Run M

## Part A. /tools index page: PASS

`https://forms.atlasonesolutions.com/tools/` returned the GitHub 404 page because the
directory had three tool subfolders and no `index.html`. Added `tools/index.html`.

### Verified live

| URL | Status | Size |
|---|---|---|
| `https://forms.atlasonesolutions.com/tools/` | **200** | 397,241 b |
| `https://forms.atlasonesolutions.com/tools/retention-cost/` | **200** | 420,307 b |
| `https://forms.atlasonesolutions.com/tools/vendor-consolidation/` | **200** | 407,428 b |
| `https://forms.atlasonesolutions.com/tools/wc-premium-check/` | **200** | 17,833 b |

The size of the index matches the file byte for byte, so the deploy is the file that was
pushed and not a cached 404.

### How it is built

Self contained, **zero CDN calls**. Everything the page needs is already in the repo and was
reused verbatim rather than re-sourced:

- **Fonts.** `tools/retention-cost/index.html` already carries three `@font-face` blocks with
  the font binaries embedded as base64 truetype: **Horas** (weight 400 to 700) and **DM Sans**
  at 400 and 700. All three were copied across unchanged. Horas sets the h1, DM Sans sets
  everything else. This is what makes the page 397 KB, the same order as its sibling tool
  pages, and it is the price of not calling Google Fonts.
- **Logo.** The periwinkle laptop mark is the same `data:image/svg+xml;base64` image already
  embedded in the two branded tool pages, copied across unchanged.
- **Brand colours** as specified: `#23304D` navy, `#788DE3` periwinkle, `#FAFAF8` off white,
  `#DBE4ED` soft blue.
- **Phone width first.** Single column by default, three columns only above 700 px.

### Content

Title **Free business calculators**. Three cards, each one sentence of value, no prices, each
with an **Open the calculator** button on a relative path:

| Path | Card heading |
|---|---|
| `retention-cost/` | What does turnover really cost you? |
| `vendor-consolidation/` | How many vendors are you paying? |
| `wc-premium-check/` | Is your workers comp premium right? |

Footer carries **One Call Solves Everything.** and the 15 minute intro link
`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`.

**No dashes anywhere in the copy.** The only hyphen in visible text is the phone number
385-213-7177. Checked by stripping tags and scanning for hyphen, en dash and em dash.

Commit `174d262`.

## Part B. "Call: not now": BUILT, PUBLISHED, TESTED

Workflow **`Call: not now`**, id `ff950be3-829d-4a51-8f9a-825db660796e`, **Published**.
Built on 11 Sep 2026 with the 45 day loop that replaced the single 90 day wait.

### Why the first attempt failed

Mouse clicks never reached GHL. Every GHL screen is an out of process iframe; while the tab
reported `document.hidden = true` (it was a background tab behind the Stripe tab) Chrome
produced no compositor hit test data for that frame, so clicks stopped at the iframe boundary
while keyboard events still got through. Nothing was wrong with GHL. Making the GHL tab the
active tab fixed it instantly.

### Tags

Three created at Settings > Tags and confirmed in the list: **`hold-45`**, **`partner`**,
**`do-not-prospect`** (11 Sep 2026). `not-now`, `booked`, `sequence active`, `reply received`,
`client-current` and `dnc` already existed. Tag count is now **36**.

### Structure as built

```
TRIGGER  Contact tag > Tag added includes "not-now"

Suppressed?            If/Else. Branch "Suppressed" = Tags includes client-current
                       OR do-not-prospect OR partner OR dnc  -> END
                       None branch -> everything below
Email: thanks for the time   subject: Thanks for the time today, {{contact.first_name}}
Add tag hold-45
Remove booked and sequence active
Opportunity to Closed Lost   Status = Lost, Lost Reason = "Not the Right Time"
Wait 45 days (1)
Replied or booked? (1)   Branch "Stop" = Tags includes reply received OR booked -> END
Email 45-A               subject: Quick one, {{contact.first_name}}
#1 Task 45-A             "45-day check-in call: {{contact.name}}", David, due 1 day 9:00 AM
Wait 45 days (2)
Replied or booked? (2)   same two branches
Email 45-B               subject: A number most owners never add up, {{contact.first_name}}
#2 Task 45-B
Wait 45 days (3)
Replied or booked? (3)   same two branches
Email 45-C               subject: What the people who left actually cost, {{contact.first_name}}
#3 Task 45-C
Remove not-now (re-arm)
Add not-now (loop restart)   -> re-fires the trigger, loop starts again
```

**Allow re-entry was already on** in Workflow settings, which the loop needs. Confirmed before
publishing.

The trigger only fires on tags added **after** publishing, per GHL's own note on the trigger.

### Emails

All four use the shared branded wrapper and the same hosted logo the other 16 emails use
(`.../form/Cxqawj85qg4ULUl64nMc/header-image/923a20f4-...png`, verified 200, 26,800 b). Sender
David Taylor / David@AtlasOneSolutions.com on every one. Copy is in
`_briefs/assets/run-M/emails.md`, no dashes anywhere except the phone number and URLs.

### Test: PASS

New contact `RunM LoopTest 202543`, id `pq1ZkuaYm2xu3Pq0Ajpp`, unique phone `+13855553118`,
plus addressed email `david+runm202543@atlasonesolutions.com`. Tag `not-now` added by API at
20:25:51 with the three waits temporarily set to **1 minute**.

| Step | Status | Time |
|---|---|---|
| Email: thanks for the time | Executed | 8:25:54 pm |
| Add tag hold-45 | Executed | 8:25:55 pm |
| Remove booked and sequence active | Executed | 8:25:55 pm |
| Opportunity to Closed Lost | **Skipped** | 8:25:57 pm |
| Wait 45 days (1) | Waiting then Wait Finished | 8:25:58 to 8:26:58 pm |
| Replied or booked? (1) -> None | Executed | 8:26:58 pm |
| Email 45-A | Executed | 8:27:00 pm |
| #1 Task 45-A | Executed | 8:27:02 pm |
| Wait 45 days (2) | Waiting then Wait Finished | 8:27:02 to 8:28:04 pm |
| Email 45-B | Executed | 8:28:04 pm |
| #2 Task 45-B | Executed | 8:28:06 pm |
| Wait 45 days (3) | Waiting then Wait Finished | 8:28:06 to 8:29:07 pm |
| Email 45-C | Executed | 8:29:08 pm |
| #3 Task 45-C | Executed | 8:29:11 pm |
| Remove not-now (re-arm) | Executed | 8:29:11 pm |
| Add not-now (loop restart) | Executed | 8:29:12 pm |
| Removed by End Of Workflow | Finished | 8:29:12 pm |

Every step fired in order and every branch took the None path, as it should for a contact with
none of the stop tags. **The loop did not restart**, see below.

After the test the three waits were set back to **45 days** and each one was reopened and
confirmed. Workflow saved and still Published. The test contact was deleted.

### The loop: solved with a second workflow

GHL skips re-entry while a contact is still enrolled ("If the Contact attempts to re-enter while
it is still enrolled in this workflow, it will get skipped"), so the original last action, adding
`not-now` back, was dropped every time. The tag has to be re-added **after** the contact leaves,
which one workflow cannot do. Fixed with a small second workflow.

**`Loop: re-arm not-now`**, id **`89c10a95-1b5c-41c8-bc6a-b6b492197196`**, Published, re-entry on.

```
TRIGGER  Contact tag > Tag added includes "loop-restart"
1  Wait 2 minutes
2  Remove not-now
3  Add not-now          -> fires "Call: not now" again
4  Remove loop-restart
```

`Call: not now` now ends with a single action, **Add loop-restart (hand off to re-arm)**, in place
of the old remove and re-add pair. New tag **`loop-restart`** created 11 Sep 2026 09:08 PM. Tag
count is now 37.

### Second test: re-entry PROVEN

New contact `RunM LoopTest2 212510`, id `FMv37QRnmCn0azG9XOut`, phone `+1385554962`, email
`david+runm2212510@atlasonesolutions.com`. Tag `not-now` added by API at **21:25:11** with the
three waits at 1 minute.

| Step | Status | Time |
|---|---|---|
| First pass, Email: thanks for the time through #3 Task 45-C | all Executed | 9:25 to 9:28:30 pm |
| Add loop-restart (hand off to re-arm) | Executed | 9:28:31 pm |
| Removed by End Of Workflow | Finished | 9:28:32 pm |
| "Loop: re-arm not-now" runs its 2 minute wait then swaps the tags | tags confirmed by API | by 9:30:49 pm |
| **Add to workflow** | **Added To Workflow** | **9:30:57 pm** |
| Suppression gate, None branch | Executed | 9:30:57 pm |
| Email: thanks for the time (second pass) | Executed | 9:30:59 pm |
| Add tag hold-45 | Executed | 9:30:59 pm |
| Remove booked and sequence active | Executed | 9:31:00 pm |
| Email 45-A, #1 Task 45-A (second pass) | Executed | 9:32:02, 9:32:05 pm |
| Email 45-B, #2 Task 45-B (second pass) | Executed | 9:33:07, 9:33:09 pm |

**The "Add to workflow" row at 9:30:57 pm is the proof**: the contact re-entered "Call: not now"
on its own, 2 minutes and 26 seconds after leaving it. The workflows list confirmed it
independently, Total enrolled went 1 to 3 with Active enrolled 1.

Afterwards the three waits were set back to **45 days**, the workflow saved and re-published, and
each Wait was reopened after a full page reload and read back as 45 days. The test contact was
deleted.

### The opportunity step is gone

`Opportunity to Closed Lost` has been deleted from "Call: not now". It silently skipped on every
run (a tag trigger carries no opportunity, and GHL's plain Update opportunity only touches the one
that triggered the workflow), and a permanently skipped step misleads anyone auditing the log.
**Opportunity stage handling moves to Run P (Quiet stage).**

The lost reason question is moot here now, but for the record the picklist has no "Not now"; the
closest is "Not the Right Time".

### The 45-B and 45-C buttons: retried, still stripped

Both were re-pasted through the `</>` source code dialog, the correct HTML confirmed sitting in the
textarea before saving, then saved, the workflow saved, the page reloaded and the action reopened
and re-read. 45-C was retried with the body cleared to empty first, exactly how E0 and 45-A were
originally built. **The editor strips the inline button styling on save either way.** After reload
both render the call to action as a bold underlined link rather than a filled periwinkle button.

Everything else in those two emails is correct: wrapper, logo, colours, signature, copy, links.
E0 and 45-A still carry the filled button. Leaving the text link in 45-B and 45-C.

The trick that does make the source dialog usable, for the record: **triple click** inside the
textarea before cmd+a. A single click does not move focus into it and cmd+a then selects the whole
page instead.
