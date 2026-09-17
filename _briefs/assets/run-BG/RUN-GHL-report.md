# RUN-GHL-report.md (Run BG, 2026-09-17)

Both parts this run were read only. No workflow, tag, task, contact, form or setting was
changed anywhere in GHL.

## Part 0

Existing ghl-browser tabs were already open and logged in, one of them on the W1 workflow
editor with the builder rendered (nodes, Fit to Screen, zoom controls all interactive). Used
that tab directly; no login and no Chrome restart were needed.

## Part 27: W1 nurture review

Full detail in `_BUILD-LOG/w1-nurture-review-2026-09-17.md` (also present at
`_briefs/assets/run-BG/` in the repo copy path, see below). Summary:

- Mapped W1 "Inbound speed to lead"'s entire sequence after the Suppressed? gate: every wait,
  task, email, tag add/remove and the two END branches, in order, with wait lengths (4 hours,
  1 day, 2 days, 3 days, 30 days).
- Opened the two live email nodes directly (P-C-2 Inbound Email 2, P-C-3 Inbound Email 3): both
  are template based, not Quick Compose, and both are in email-templates-map.md already. Both
  still carry the **stale footer phone 385-213-7177** (should be 380-225-5217, the number fixed
  elsewhere by Run BE). The email-templates-map.md phone fix from Run BE evidently did not reach
  these two P-prospecting templates.
- **Finding needing David's attention:** W1's Internal Notification action shows as **currently
  enabled** in the builder today. Run BF's live log (2026-09-16) recorded disabling this exact
  node and confirmed the disabled state on reload ("Internal Notification (Disabled)"). Today the
  node has no "(Disabled)" marker and offers a "Disable action" option, meaning it is live again.
  Not re-disabled this run since Part 27 is read only; see Questions below.
- Opened Post-Presentation Email, Tool-Lead Nurture and Call: not now for their triggers and
  suppression gates only (per the brief, full node maps were not required for these three).
  Found that **none of the three cross-checks W1's suppression tags**, and W1 does not check
  theirs either, so overlapping sends are structurally possible; the review file has the full
  overlap table and a recommendation with the exact node changes a future run should make
  (disable the still-live Internal Notification node again, fix the two stale template phones,
  add cross-workflow suppression checks to the three other gates).

## Part 28: Dr. Joel Gould's contact (read only)

Contact `3MBRxpll6eLI4bvtIdfh`.

- **Tags (3):** `form-a-sent`, `reply received`, `intake-received`. `send-bk-form` is **not**
  present.
- **Opportunity:** "Gould dental practice, PEO, insurance, books", Pipeline "PEO & Benefits",
  stage **Inquiry** (unchanged since creation on 2026-09-15), value $0.00.
- **Open tasks (6):**
  - "Reply from Joel Gould: read and respond" -- due Today, 7:05 AM (MDT)
  - "Reply from Joel Gould: read and respond" -- due Yesterday, 1:39 PM (MDT)
  - "Reply from Joel Gould: read and respond" -- due Yesterday, 11:36 AM (MDT)
  - "Reply from Joel Gould: read and respond" -- due Yesterday, 11:30 AM (MDT)
  - "CALL NOW: (310) 722-0705" -- description "Services requested:" (blank; his task predates
    the Part 21c fix to the CALL NOW task template, which only affects tasks created after that
    fix) -- due Yesterday, 11:19 AM (MDT)
  - "Reply from Dr. Joel Gould: read and respond" -- due Yesterday, 6:42 AM (MDT)
  All six show as still open/overdue in the Tasks panel.
- **"Send bookkeeping form on tag" execution log:** checked the workflow's own Execution Logs
  tab (date range defaults to the last 60 days) with no contact filter applied -- result: **"No
  logs found. Execution logs are available for the last 60 days."** This confirms the workflow
  has not executed for any contact in that window, Joel Gould included, consistent with the
  absent `send-bk-form` tag.
- **Last three Conversations items** (time and direction):
  1. Insurance quote thread -- inbound from "Dr. Joel Gould" (attachment) -- 11:36 AM yesterday
  2. "Life Insurance Requirement -- Enterprise Bank & Trust" -- outbound from
     david@AtlasOneSolutions.com ("Dr. Gould, Yes, I can actually put this in place for you...")
     -- 1:55 PM yesterday
  3. "quotes" thread -- inbound from drjoeldgould@gmail.com ("Hi David, this is a quote that I
     received from a company...") -- 7:04 AM today

Nothing on this contact was touched: no tags, tasks, opportunity stage or messages were
changed.

## Assumptions

1. W1's Suppressed? gate condition count badge read "11" but only 5 tag entries were read on
   screen before moving on (cooling 30d, cooling 60d, cooling 90d, hold 6m, dnc); treated as "at
   least these 5", not a complete enumeration.
2. Treated the "No logs found" result on the Execution Logs tab (no contact filter, default 60
   day range) as sufficient proof "Send bookkeeping form on tag" never fired for Joel Gould,
   rather than filtering to his contact specifically, since an empty logs list for the whole
   workflow already implies an empty list for any one contact within it.
3. Call: not now's Suppressed? gate condition list may have more than the 4 entries read
   (client-current, do-not-prospect, partner, dnc); not fully scrolled since the brief only
   asked for the trigger and the gate, not the full condition list, for this workflow.

## Skipped

- Did not open every node inside "Call: not now" past its Suppressed? gate (E0, LT-1 through
  LT-5, 45-A, their waits) -- out of scope for Part 27b, which only asked for triggers and
  suppression gates on that workflow.
- Did not attempt to re-disable W1's Internal Notification node, or fix the stale P-C-2/P-C-3
  footer phones, or build the cross-workflow suppression checks recommended in the review file --
  all are edits, and both parts of this run were read only per the brief.

## Questions for David

1. W1's Internal Notification action is live again after Run BF confirmed it was disabled on
   2026-09-16. Do you want it disabled again on the next run, or was there a reason to turn it
   back on that I'm missing?
2. The stale 385-213-7177 footer phone was supposed to be fixed to 380-225-5217 as part of Run
   BE's phone cleanup, but it's still present on the P-C-2 and P-C-3 templates (both in the P-
   prospecting section of email-templates-map.md). Should a future run push that fix to those
   two templates, and should it also check the rest of the P- prospecting template set (P-A, P-B,
   P-D, P-E, P-W7) for the same stale number while it's in there?
3. Do you want the cross-workflow suppression gates (Post-Presentation Email, Tool-Lead Nurture,
   Call: not now all currently blind to each other's and to W1's tags) built on a future run, or
   is the current risk of an occasional double-send acceptable for now?
4. Joel Gould has 6 open/overdue tasks stacking up on his contact, including 5 separate "reply
   and respond" tasks that look like duplicates of the same underlying need (he keeps replying,
   each reply spawns a new task). Is that intentional, or should reply-triggered tasks be
   deduplicated so only the newest one stays open per thread?
