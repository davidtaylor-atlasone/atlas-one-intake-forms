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
| Wait 45 days (2) | Waiting | 8:27:02 pm |

### Two things that need David

1. **The opportunity step is skipped.** GHL's plain "Update opportunity" only touches the
   opportunity that triggered the workflow, and a tag trigger carries none, so it no ops. The
   fix is a "Find opportunity" action in front of it, but Find forks the canvas into
   "Opportunity Found" and "Opportunity Not Found" branches and the whole 45 day loop would have
   to be duplicated under both. Left as a no op rather than doubling the workflow. Say the word
   and I will either duplicate the loop or move the opportunity close into its own small
   workflow on the same trigger.
2. **The lost reason is a fixed picklist.** There is no "Not now" option. Closest is
   **"Not the Right Time"**, which is what is set. The list is No response, Other, Benefits not
   competitive, We didn't offer a service they needed, Out of business, Too many services, Not
   the Right Time, Too expensive, Went with competitor.

### One cosmetic difference

45-A uses the same filled periwinkle button as the other emails. 45-B and 45-C had to be pasted
as rich HTML rather than through the source dialog (GHL's source dialog closes itself between
tool calls), and the editor stripped the inline button styling, so their call to action renders
as a bold underlined link instead of a filled button. Everything else matches. Easy to fix by
hand in the two actions.
