# needs Chrome restart

Run AG (the rest of Run AD: Part 4 copy pass, then Part 1 item 3 construction branches, then Run R, in one
session) did not start. Part 0's dead-UI click test failed and the standing rule says stop, not push through.

## Part 0: what happened

1. `tabs_context_mcp` found no existing app.ridethehightide.com tab for this session. Created a new tab,
   navigated to https://app.ridethehightide.com/, waited. Landed authenticated directly on
   `/v2/location/AzTPxnK2vSUj19jYoDmR/dashboard` (app shell rendered fine: Atlas One Solutions, Lehi UT, DT
   avatar).
2. Clicked Automation in the left nav. Workflows list loaded fully with real data (Atlas One Tool Results
   Capture, Booking workflows, Call Scheduling Confirmation, Call: not now Published/7 enrolled, etc), same rows
   seen in every prior session.
3. Dead-UI click test: clicked the "Call: not now" row text directly. No navigation, URL unchanged, no visible
   change. Also tried the small external-link icon next to the row name (in case that is the actual click
   target): no new tab, no navigation either.
4. Did the one allowed Cmd+R. Page reloaded, Workflows list rendered again with the same data. Clicked
   "Call: not now" again: a loading spinner appeared briefly over the table, then vanished. The row never
   navigated to an editor.
5. Console at that point showed `FirebaseError: Missing or insufficient permissions` (chunk.CALMQSNm.js), plus a
   session-recording null-property error and a WhatsApp init 400 -- the exact same error signature logged in the
   three prior "needs Chrome restart" reports earlier today (RUN-GHL-report.md history, before this run).
6. Per the dead UI rule (one Cmd+R, then stop if still dead), stopped the whole run before Part 4, Part 1 item 3,
   and Run R. Closed the tab.

## What this means for the next run

This is not a new problem: it is the same FirebaseError-driven editor lockup that has now blocked workflow-editor
access in 4 of the last 5 GHL terminal sessions today (this one included), with exactly one clean session in
between (the one that completed Part 1 items 1-2 and Part 2 items 4-5, reported previously). The pattern so far:
sometimes the editor opens fine on the first try in a fresh tab, sometimes it never does even after a reload, and
there is no reliable trigger identified yet (not a specific workflow, not a specific navigation path -- this run
failed on the exact same "Call: not now" row that opened cleanly in the RUN AD hand-off-mode session).

Given the brief's own hand-off-mode history (BRIEF-GHL's prior revision already tried "David clicks, terminal does
the rest" as a workaround for this exact FirebaseError before this revision removed it again), the next run should
probably either: (a) go straight to hand-off mode without wasting a cold attempt first, or (b) have David restart
Chrome / clear the extension's tab state before the terminal starts, since a same-session Cmd+R has now failed to
clear the error twice.

## Not attempted (blocked before start)

- Part 4: cadence email copy pass (Post-Presentation Email 1-2, Call: not now E0/LT-1/2/4/5/45-A, Seasonal
  touches Q-1 x3, global signature/link/button changes, test send).
- Part 1 item 3: construction branch duplication into every dead end in both workflows.
- Part 3 (Run R): forms C1/C2, intake workflows, GHL_BUILD_FORM.

None of these were started, so there is nothing to verify or roll back.

## Assumptions

1. Confirmed WWD is live before attempting anything: `curl -o /dev/null -w "%{http_code}" https://forms.atlasonesolutions.com/tools/what-we-do/` returned 200. This is ready for whenever Part 4 actually runs; not used this session since Part 4 never started.
2. Treated the repeated FirebaseError signature (identical wording and source chunk to the last three "needs Chrome restart" reports) as sufficient to invoke the dead-UI stop rule rather than attempting further workarounds (e.g. a second reload, a brand new tab) that the brief does not authorize.

## Questions for David

1. This FirebaseError pattern has now blocked 4 of the last 5 GHL sessions today. Do you want the next run to
   start in hand-off mode by default (skip the cold attempt, go straight to "David clicks the row, terminal
   continues") until this clears up, or keep trying cold first since it did work once today?
2. Is there a known cause on the High Tide / GoHighLevel side for this permissions error (an account role change,
   a session/cookie issue, a browser extension conflict), or should the support note drafted earlier
   (`GHL-support-note-DRAFT-2026-09-13.md`) go out to High Tide now that it has recurred again after being
   reported clear once today?
