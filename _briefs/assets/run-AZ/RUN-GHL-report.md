# RUN-GHL-report.md (Run AZ, 2026-09-15 evening)

## Summary

This run picked up the brief's order (Parts 6, 7, 8, 9; Part 5c skipped because
`email-templates-map.md` does not exist yet). Parts 6, 7, 8 are done and verified. Part 9 could
not start: the `ghl-browser` MCP server was unavailable at the point this session resumed the
run (see "Part 9: blocked" below), needs a Chrome/Claude Code restart before it can run.
Everything below Part 5c in the brief (Parts 6, 7, 8) reuses the same `ghl-browser` (Playwright)
session as Run AY/earlier Run AZ steps; no dead-click reproduced during any of it.

## Part 6: booking notifications to David - DONE

- **Calendar notification prefs**, all 4 calendars in "Book time with David" (15-Minute Intro
  Call, 60-Minute Client Meeting, 45-Minute Client Meeting, 30-Minute Back-Office Audit): opened
  Calendar Settings > edit calendar > Advanced settings > Notifications & policies on each.
  Unchecked "Assigned user" from the recipient list on: the 15-Minute Intro Call's Appointment
  booked (Unconfirmed) and Cancellation notifications (the only two of the four calendars that
  still had Email enabled for those types to an assigned user), plus Reschedule on all 4
  calendars (Reschedule was the only type with assigned-user email enabled on all 4). Confirmed
  contact-facing notification types were already in the brief's expected state (Confirmed OFF,
  Cancellation OFF, Reminder OFF, Reschedule ON) before touching anything. Each save confirmed
  via the "Settings saved!" toast.
- **"Booking: confirm and remind"** (`7200e594-0a7a-47cc-847e-cb8a8e39eb31`, Draft, untouched
  publish state): added an Internal Notification action right after the trigger (Type = Email,
  To User Type = Custom email, To Custom Email = david@atlasonesolutions.com, Subject = "New
  booking: {{contact.name}}, {{appointment.start_time}}", body pasted verbatim from
  `internal-new-booking.html` via the source-code dialog).
- **"Booking: cancelled"** (`c945a4b6-deb8-496f-8c51-88481860bbac`, Draft, untouched publish
  state): same treatment, Subject "Cancelled: {{contact.name}}, {{appointment.start_time}}",
  body from `internal-cancelled.html`, placed right after the trigger, before the existing
  "Email - Cancelled, pick a new time" node.
- **"Booking: rescheduled"**: GHL has no native workflow trigger for a rescheduled appointment
  (the Appointment status trigger's filter only offers new/confirmed/cancelled/Showed/No-show/
  invalid; the only "reschedul" hit anywhere in the trigger picker is a Cal.com integration
  trigger, not a native GHL event). Built an empty shell workflow to confirm this, then deleted
  it (soft delete, 30-day recovery) rather than leave a broken/misleading Draft. Used GHL's own
  native mechanism instead: each of the 4 "Book time with David" calendars' Notifications &
  policies > Reschedule > **Additional emails** field has its own independent Subject and
  source-code-editable body, separate from the contact-facing reschedule email. Set on all 4:
  Additional emails = david@atlasonesolutions.com, Subject = "Rescheduled: {{contact.name}},
  {{appointment.start_time}}", body = `internal-rescheduled.html` verbatim. This delivers the
  brief's exact branded internal notification without the impossible dedicated workflow.
- Every save on every calendar and workflow was verified by reload + re-read of the saved
  source/settings before moving on.

## Part 7: phone number 380-225-5217 (380-CALL-A1S) - DONE, one gap flagged

- **Default outbound number**: already set to +1 380-225-5217 in Phone System > Phone numbers
  (done by a prior run). Confirmed still set.
- **Call forwarding**: Business Phone Number, 3rd priority, already +13852137177 (David's cell)
  from a prior run. Matches the brief exactly, no change made.
- **Business Profile > General Information > Business Phone**: still had the old 385-213-7177.
  Changed to +1 380-225-5217, clicked Update Information, reloaded and re-read: confirmed
  persisted.
- **Voicemail**: Voice > Voicemail & Missed Call TextBack > Voicemail, Incoming Call Timeout
  already at 20 sec (matches brief and the phone-number list's Call Timeout column, no change).
  **Finding**: this page has no plain-text greeting field. "Voicemail Audio" only accepts an
  uploaded audio file (mp3/wav/etc.); there is no text-to-speech box to type the brief's plain
  greeting into. Left the existing setup as is (no audio uploaded, since recording/generating
  one was not something this run could do without David). Flagged below under Questions.
- **Default outbound number, Additional Settings tab**: checked; there is no location-wide
  default-outbound-number setting separate from the per-number "Default Number" flag already
  set above (and only one number exists on this account regardless). Trust Center was not
  touched, as instructed. No SMS was enabled or touched anywhere in this part.

## Part 8: logos on the 30/45/60 minute booking pages - ALREADY DONE (verified, no changes)

Checked all 3 target calendars (30-Minute Back-Office Audit, 45-Minute Client Meeting,
60-Minute Client Meeting) in the calendar's Basic Details admin panel: each already has the
Atlas One Solutions logo set (Square widget shape, "Remove logo" button present, meaning a
logo is already uploaded on all 3 -- this must have been done in an earlier run). Opened all 3
live public scheduling links via ghl-browser and screenshotted each: logo renders correctly at
the top-left on all 3 live pages, matching the working 15-Minute Intro Call page. No upload was
needed; Part 8 is confirmed complete with a verification pass only.

## Part 9: QuickBooks integration and Documents & Contracts readiness check - BLOCKED, not started

This session resumed the run after Parts 6/7/8 had already been completed and logged (per
`TERMINAL-GHL-live.md`) but never committed or written up. On resuming, the `ghl-browser` MCP
tools were unavailable: the first call returned "Browser is already in use for
`/Users/davidtaylor/.ghl-browser`", because Chrome/playwright-mcp processes from the prior,
not-cleanly-closed session were still running. Killing those stale processes (to free the
profile lock, as recommended cleanup) also killed the ghl-browser MCP server's own browser
connection for this session, and it did not reconnect (`ToolSearch` confirms the `ghl-browser`
MCP server "failed to connect" for the rest of this session). A new Chrome window for the
profile did relaunch on its own, but no tool is available in this session to drive it.

Per the run's dead-UI rule (stop cleanly rather than retry blindly when the browser path is not
landing), this run stops here. **Needs Chrome/Claude Code restart** to reconnect the
`ghl-browser` MCP server before Part 9 (QuickBooks Integrations check, Documents & Contracts
Templates list, Products list, Invoices recurring/auto-pay check -- all read-only, no changes)
can be attempted. Nothing in Part 9 was touched; there is nothing to roll back.

## Assumptions

1. Treated Parts 6, 7, 8 as fully complete based on the detailed `TERMINAL-GHL-live.md` entries
   from earlier in this same calendar run (timestamps 16:27-16:58), re-reading each entry
   carefully rather than re-doing verified work, since re-driving the browser through all three
   parts again would have duplicated already-confirmed changes (and risked creating duplicate
   Internal Notification nodes or duplicate calendar edits).
2. Did not attempt to force a `ghl-browser` reconnect (no MCP-reconnect tool is available to
   this session) and did not fall back to the retired Chrome extension path, per the explicit
   "do not call any mcp__claude-in-chrome tool this run" rule -- stopping and flagging for a
   restart is the correct move per the dead-UI rule, not a workaround.
3. Did not re-verify Part 8's "already done" state by re-uploading anything, since the Remove
   Logo button being present on all 3 calendars plus matching live screenshots is conclusive
   evidence a logo is already set; re-uploading would risk overwriting a fine asset for no
   reason.

## Questions for David

1. **Voicemail greeting**: GHL's Voicemail settings page (Voice > Voicemail & Missed Call
   TextBack) only accepts an uploaded audio file for the greeting, no text-to-speech / plain
   text field exists. The brief's plain greeting ("You have reached Atlas One Solutions...")
   cannot be entered as text. Do you want to record or generate an audio file for this (and if
   so, is there a preferred voice/tool), or is there a different GHL settings page that holds a
   text greeting that this run missed?
2. **Part 9 access**: this run needs the `ghl-browser` MCP server reconnected (likely just a
   Claude Code / Chrome restart) before it can do the QuickBooks/Documents & Contracts/Products/
   Invoices read-only check. Should the next run start there before anything else?
3. **Part 5c** (phone + link-color re-paste across ~14 workflows) is still not started; it
   remains blocked on `email-templates-map.md` from GHL-JOBS not existing yet, per the brief's
   own condition. Same open questions as before (see the prior report section, still valid):
   is the next run meant to work through "Post-Presentation Email" to full completion (10+
   nodes across parallel/Construction branches) before moving to the other ~13 named workflows,
   or spread partial effort across all of them first?
