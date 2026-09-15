# Email templates map (Run AW, 2026-09-15)

One row per template pushed through the Email Builder API (create + fill two-call sequence).
The subject is not stored on the template; the GHL terminal sets it on each workflow's Send
Email action, taken from this Subject column (sourced from INDEX.md).

## New cadence/booking/intake templates (35, this run)

| Send | Workflow | Template name | Template id | Subject | File |
|---|---|---|---|---|---|
| Email-1 | Post-Presentation Email | `A1 | Email-1 | email-1` | `6aa9c89bbbf4cb7988c03afd` | Your next step with Atlas One, {{contact.first_name}} | `email-1.html` |
| Email-2 | Post-Presentation Email | `A1 | Email-2 | email-2` | `6aa9c89db1a9b275e36982ac` | Still here whenever you're ready, {{contact.first_name}} | `email-2.html` |
| E0 | Call: not now | `A1 | E0 | e0` | `6aa9c89e8fc016e6508479a3` | Thanks for the time today, {{contact.first_name}} | `e0.html` |
| LT-1 | Call: not now (Long Tail loop) | `A1 | LT-1 | lt-1` | `6aa9c8a096b1ac2874f591ac` | One thing from our call, {{contact.first_name}} | `lt-1.html` |
| LT-2 | Call: not now (Long Tail loop) | `A1 | LT-2 | lt-2` | `6aa9c8a19ed784b5df8c500a` | A number worth knowing | `lt-2.html` |
| LT-3 | Call: not now (Long Tail loop) | `A1 | LT-3 | lt-3` | `6aa9c8a3b40c9f3a4ff410a8` | Want to knock the form out together? | `lt-3.html` |
| LT-4 | Call: not now (Long Tail loop) | `A1 | LT-4 | lt-4` | `6aa9c8a4b40c9f3a4ff410c2` | Two minutes, your own numbers | `lt-4.html` |
| LT-5 | Call: not now (Long Tail loop) | `A1 | LT-5 | lt-5` | `6aa9c8a6bbf4cb7988c03b94` | Should I close your file, {{contact.first_name}}? | `lt-5.html` |
| 45-A | Call: not now (45 day pass) | `A1 | 45-A | 45-a` | `6aa9c8a896b1ac2874f5926b` | Quick one, {{contact.first_name}} | `45-a.html` |
| Q-1 | Seasonal touches 2026-27 | `A1 | Q-1 | q-1` | `6aa9c8a93029d837f98fd141` | If you are changing anything this quarter, start now | `q-1.html` |
| YE-1 | Seasonal touches 2026-27 | `A1 | YE-1 | ye-1` | `6aa9c8abb1a9b275e369839b` | January 1 is the easiest start date of the year | `ye-1.html` |
| YE-3 | Seasonal touches 2026-27 | `A1 | YE-3 | ye-3` | `6aa9c8ac7919774ef2688437` | Last clean cut-over date | `ye-3.html` |
| B-1 | Books: after the call (same day) | `A1 | B-1 | b-1` | `6aa9c8ae94dd61786846a646` | What Atlas One bookkeeping actually looks like, {{contact.first_name}} | `b-1.html` |
| B-2 | Books: after the call (+3 days) | `A1 | B-2 | b-2` | `6aa9c8b00bbbc34b5ea9c48f` | What falling behind on the books actually costs | `b-2.html` |
| B-3 | Books: after the call (+7 days) | `A1 | B-3 | b-3` | `6aa9c8b1b40c9f3a4ff411ed` | A proof point, no names attached | `b-3.html` |
| B-4 | Books: after the call (+14 days) | `A1 | B-4 | b-4` | `6aa9c8b33029d837f98fd1b2` | Should I close your file, {{contact.first_name}}? | `b-4.html` |
| BQ-1 | Books: quarter and year end | `A1 | BQ-1 | bq-1` | `6aa9c8b43029d837f98fd1c5` | The easiest time to switch bookkeepers is right now | `bq-1.html` |
| BYE-1 | Books: quarter and year end | `A1 | BYE-1 | bye-1` | `6aa9c8b67919774ef26884d4` | January is the easiest month to start clean books | `bye-1.html` |
| BYE-2 | Books: quarter and year end | `A1 | BYE-2 | bye-2` | `6aa9c8b807aac9f9aae4fa66` | Start the year with a clean set of books | `bye-2.html` |
| Confirm: service sign up | Service picker form submitted | `A1 | Confirm: service sign up | confirm-service-signup` | `6aa9c8b9b0cd6d0085962db6` | Your {{contact.which_service}} request is in, {{contact.first_name}} | `confirm-service-signup.html` |
| Confirm: document build | Document build request submitted | `A1 | Confirm: document build | confirm-document-build` | `6aa9c8bb94dd61786846a795` | Your {{contact.which_document}} is in the queue, {{contact.first_name}} | `confirm-document-build.html` |
| C1 | Booking: confirm and remind | `A1 | C1 | booking-c1` | `6aa9c8bd8fc016e650847ba5` | You're booked with David, {{contact.first_name}} | `booking-c1.html` |
| 24 hour reminder | Booking: confirm and remind | `A1 | 24 hour reminder | booking-reminder-24h` | `6aa9c8be96b1ac2874f59462` | Reminder: your call with David is tomorrow | `booking-reminder-24h.html` |
| 1 hour reminder | Booking: confirm and remind | `A1 | 1 hour reminder | booking-reminder-1h` | `6aa9c8c096b1ac2874f5947e` | Talk in an hour | `booking-reminder-1h.html` |
| C2 | Booking: after the call | `A1 | C2 | booking-c2` | `6aa9c8c15893810abc0c7689` | Thanks for the time today, {{contact.first_name}} | `booking-c2.html` |
| C3 | Booking: after the call | `A1 | C3 | booking-c3` | `6aa9c8c37919774ef26885e7` | Still thinking it over, {{contact.first_name}}? | `booking-c3.html` |
| Cancelled | Booking: cancelled | `A1 | Cancelled | booking-cancelled` | `6aa9c8c57919774ef268860d` | No problem, {{contact.first_name}}. Want to pick a new time? | `booking-cancelled.html` |
| No show | Booking: no show | `A1 | No show | booking-no-show` | `6aa9c8c707aac9f9aae4fb90` | We missed each other, {{contact.first_name}} | `booking-no-show.html` |
| Email 1 (intake) | Intake: Instant reply | `A1 | Email 1 (intake) | intake-instant-reply` | `6aa9c8c894dd61786846a8c7` | We've got it, {{contact.first_name}}. Here's what happens next | `intake-instant-reply.html` |
| Email 2 (PEO form) | Send PEO form on tag | `A1 | Email 2 (PEO form) | send-peo-form` | `6aa9c8cab40c9f3a4ff413f7` | Your next step with Atlas One, {{contact.first_name}} | `send-peo-form.html` |
| Email 2B (bookkeeping form) | Send bookkeeping form on tag | `A1 | Email 2B (bookkeeping form) | send-bookkeeping-form` | `6aa9c8cb94dd61786846a92c` | One more short form for your books, {{contact.first_name}} | `send-bookkeeping-form.html` |
| Email 5A | Tool-Lead Nurture | `A1 | Email 5A | tool-lead-nurture-1` | `6aa9c8cd94dd61786846a953` | The number's only half the story, {{contact.first_name}} | `tool-lead-nurture-1.html` |
| Email 5B | Tool-Lead Nurture | `A1 | Email 5B | tool-lead-nurture-2` | `6aa9c8cf3029d837f98fd3dc` | One thing most owners in your spot are overpaying for | `tool-lead-nurture-2.html` |
| Email 6 | Won - Pay Referral Partner | `A1 | Email 6 | won-email-6` | `6aa9c8d0b40c9f3a4ff41498` | Welcome to Atlas One, {{contact.first_name}} | `won-email-6.html` |
| Email 7 (new) | Won - Pay Referral Partner | `A1 | Email 7 (new) | won-email-7-checklist` | `6aa9c8d294dd61786846a99e` | Setup checklist for {{contact.company_name}} | `won-email-7-checklist.html` |

## P- prospecting workflow templates (21, built 2026-09-08, Checkpoint 2)

Included here so the GHL terminal has every template id in one place. Ids and wrapper notes are
from `_briefs/prospecting-workflows-W1-W7-REPORT.md` (Checkpoint 2); this run did not touch these.

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

## Placeholder sends (7, not pushed, per brief)

`45-b.html`, `45-c.html`, `construction-audit.html`, `email-3.html` (does not exist),
`email-4.html`, `ye-2.html`, `ye-4.html` -- these keep their current live GHL body; the GHL
terminal edits the wrapper around the existing body by hand.

## Internal notification sends (3, not pushed, pasted by hand)

`internal-new-booking.html`, `internal-cancelled.html`, `internal-rescheduled.html` -- the GHL
terminal pastes these by hand, per the brief.
