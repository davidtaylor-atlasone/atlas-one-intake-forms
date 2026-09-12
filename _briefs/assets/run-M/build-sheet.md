# Run M part B: build sheet for "Call: not now"

Workflow id `ff950be3-829d-4a51-8f9a-825db660796e`, currently named
`New Workflow : 1789164293568`, Draft, empty. Rename to **Call: not now**.

## Tags this needs

| Tag | Purpose | Exists? |
|---|---|---|
| `not-now` | trigger, and the loop re-arm | yes, created Run M |
| `hold-45` | marks the contact as parked in this loop | check, create if missing |
| `booked` | suppression and early exit | yes |
| `sequence active` | removed so other sequences do not double up | yes |
| `reply received` | early exit | check, create if missing |
| `client-current` | suppression gate | check, create if missing |
| `do-not-prospect` | suppression gate | check, create if missing |
| `partner` | suppression gate | check, create if missing |
| `dnc` | suppression gate | check, create if missing |

Every tag created here goes into the list in `_briefs/RUN-G-checkpoints.md` with the new count.

## Workflow settings

**Re-entry must be allowed**, or the loop dies after one pass. Workflow > Settings >
allow the contact to re-enter. Confirm it is on before publishing.

## Structure

```
TRIGGER  Contact Tag Added = not-now

1  If/Else  "Suppressed?"
     Branch "Suppressed": contact tag is any of client-current, do-not-prospect, partner, dnc
        -> nothing. The branch ends, contact leaves.
     Else -> everything below.

2  Send Email   E0   subject: Thanks for the time today, {{contact.first_name}}
3  Add Contact Tag        hold-45
4  Remove Contact Tag     booked, sequence active
5  Update Opportunity     stage Closed Lost, lost reason "Not now"
                          (no opportunity on the contact means this step no ops)

6  Wait 45 days           exit early if tag reply received or booked is added,
                          if this build of the Wait action offers an exit condition
7  If/Else  "Replied or booked?"
     Branch "Stop": tag reply received OR tag booked -> ends
     Else -> continue
8  Send Email   E1   subject: Quick one, {{contact.first_name}}
9  Create Task        "45-day check-in call: {{contact.name}}"  assigned David, due same day

10 Wait 45 days           same exit condition
11 If/Else "Replied or booked?"   same two branches
12 Send Email   E2   subject: A number most owners never add up, {{contact.first_name}}
13 Create Task        "45-day check-in call: {{contact.name}}"  assigned David

14 Wait 45 days           same exit condition
15 If/Else "Replied or booked?"   same two branches
16 Send Email   E3   subject: What the people who left actually cost, {{contact.first_name}}
17 Create Task        "45-day check-in call: {{contact.name}}"  assigned David

18 Remove Contact Tag     not-now
19 Add Contact Tag        not-now      <- re-fires the trigger, loop restarts at step 1
```

### Why step 18 exists

The trigger is **Tag Added**. Adding a tag the contact already carries fires nothing, so the
loop would run once and stop. Removing it immediately before re-adding it makes the add a real
state change. The contact keeps `not-now` the whole way through the 135 days, which is what the
smart lists expect, and only loses it for the instant between steps 18 and 19.

If the 1 minute test shows GHL collapsing those two steps and not re-firing, the fallback is a
1 minute Wait between 18 and 19.

## Email bodies

`_briefs/assets/run-M/emails.md`. Wrapper from `_briefs/2026-09-07-email-template-pass.md`
part 2. Sender David@AtlasOneSolutions.com on every one.

## Test

1. Set all three Wait steps to **1 minute**.
2. Publish.
3. New contact, unique phone, plus addressed email, add tag `not-now`.
4. Watch Execution logs for a full pass: E0, tags, opportunity step, the three loop emails and
   three tasks, then the re-arm firing a second pass.
5. Check the suppression gate separately: second test contact carrying `dnc`, add `not-now`,
   confirm it lands in the Suppressed branch and sends nothing.
6. Set the three Waits back to **45 days**. Reopen each one and confirm.
7. Confirm still Published.
