# RUN-GHL-report.md (Run AV, 2026-09-15)

**needs Chrome restart** - stopped at the start of Part 5 because the workflow list's row clicks, pagination,
and search box all went dead (see Part 5 section below). This is the same FirebaseError-linked dead-UI pattern
that stopped Runs AP, AR, AS and AT on 2026-09-14; Run AU cleared it with a full Chrome quit-and-reopen (not
just a tab reload/new tab). David: please fully quit and reopen Chrome, then the next GHL-terminal run can pick
up at Part 5.

## What this run covers

Run AV picked up the brief at Part 4 (Parts 0-3 were completed in Run AU on 2026-09-14, confirmed complete via
the live log before starting). Part 4 finished cleanly. Part 5 could not start due to the dead-UI issue below.

## Part 4: portal prep inside GHL - COMPLETE

**Custom fields created** (Settings > Custom Fields > Contact folder, all three per `atlas-one-portal/DEPLOY.md`):

| Field name | Type | Key (verified via get_page_text after save) |
|---|---|---|
| Services | Checkbox (GHL's multi-select checkbox-list; DEPLOY.md's "Multiple Options" type) | `{{contact.services}}` |
| Savings to date | Monetary | `{{contact.savings_to_date}}` |
| Portal last link | Single line | `{{contact.portal_last_link}}` |

Services field's 7 options confirmed in the live preview before saving: PEO, Payroll, Benefits, Workers comp,
Bookkeeping, HR support, Atlas One membership - matches DEPLOY.md exactly.

All three keys read back from the Custom Fields list page (not just the create dialog) after saving, per rule 17.

**Private Integrations**: DEPLOY.md's "Atlas One portal" integration turned out to already exist under a
different name, "Atlas One apps" (description: "Read and write access for Atlas One internal apps: contacts,
notes, tasks, calendars, conversations, opportunities."). Confirmed this is the same integration the portal app
uses by comparing token prefixes: the GHL UI shows `pit-cb9d****-****-****-****a830`, and
`~/Projects/atlas-one-portal/.env`'s `GHL_PRIVATE_INTEGRATION_TOKEN` starts `pit-cb9d2c...` - exact match. Did
NOT create a duplicate integration.

Checked its scopes (Edit > Scopes tab): 9 scopes already present covered 5 of DEPLOY.md's 6 needed scopes
(`contacts.readonly`, `contacts.write`, `conversations.readonly`, `conversations/message.readonly`,
`conversations/message.write`), missing only `locations/customFields.readonly`. Added it via the scope search box
("View Custom Fields - locations/customFields.readonly") and clicked Update. The token was NOT rotated by this
edit (rotation is a separate explicit action, not triggered by a scope change), so there is **no new token for
David to paste into Azure** - none needed this run.

**Note on the brief's "seven scopes"**: `DEPLOY.md` itself lists only 6 scope strings under "Scopes needed"
(`contacts.readonly`, `contacts.write`, `conversations.readonly`, `conversations/message.readonly`,
`conversations/message.write`, `locations/customFields.readonly`). I could not find a 7th scope named anywhere
in DEPLOY.md, so I granted exactly the 6 listed and did not add anything beyond them. Flagged under Questions.

## Part 5: client-facing emails - BLOCKED, not started

Navigated in-app to Automation > Workflows to open "Intake: service sign up" (the first target of Part 5a).
Symptoms, in order:

1. Clicking a workflow row's name (tested on "Booking: after the call" as a neutral probe, not a target workflow)
   did nothing - URL stayed on `?listTab=all`, no editor opened, no new tab in the tab group.
2. Clicking the row's external-link icon: same, nothing happened.
3. Clicking pagination controls (page "2", "Next", the "10 / page" size dropdown): none responded, still showing
   page 1 of 4.
4. Clicking into the workflow search box and typing: no text appeared in the box and no results filtered.
5. `read_console_messages` confirmed `FirebaseError: Missing or insufficient permissions` firing on this page -
   the exact same signature Runs AP/AR/AS/AT hit on 2026-09-14, which Run AU's report says was only cleared by a
   **full Chrome quit-and-reopen**, not a same-window tab reload.
6. Per the dead-UI rule: did one Cmd+R reload, retried the row click once more - still dead. Stopped cleanly here
   rather than repeating failed clicks.

No workflow, form, or setting was changed during this Part 5 attempt. Part 4's changes (already saved before this
started) are unaffected.

## Assumptions

1. The "Atlas One apps" private integration is the portal integration DEPLOY.md calls "Atlas One portal" - based
   on exact token-prefix match against the deployed `.env`, not on the integration's name (which is generic and
   could describe other tools). Did not rename it, since renaming wasn't asked for and risks confusing anything
   else that references it by name.
2. Granted exactly DEPLOY.md's 6 listed scopes, not the 7 the brief's Part 4 text mentions - could not find a 7th
   scope named anywhere in DEPLOY.md to add. See Questions.
3. Used GHL's "Checkbox" field type for Services (DEPLOY.md's "Multiple Options (checkbox list)") - this is the
   correct multi-select type in this account's current custom-field type list (there is no separately-named
   "Multiple Options" type; "Checkbox" is it, confirmed by its option-list builder UI matching the description).
4. Put all three new fields in the existing generic "Contact" folder rather than creating a new "Portal" folder,
   per DEPLOY.md's "Contact folder, any group" instruction.

## Skipped

Parts 5, 6, 7, 8, 9 - not started, blocked by the dead-UI issue at the very start of Part 5. Once Chrome is fully
restarted, the next run should pick up at Part 5a using this same brief file.

## Questions for David

1. Chrome needs a full quit-and-reopen (not just a tab close/reload) before the next GHL-terminal run - same as
   Run AU needed on 2026-09-14. Can you do that before the next run starts?
2. DEPLOY.md's Part 4 text (both in this run's brief and in the file itself) lists exactly 6 Private Integration
   scopes, but the brief's Part 4 instructions say "the seven scopes listed in DEPLOY.md." I granted the 6 I could
   find. If there's a 7th scope you intended (maybe `contacts/task.write` alongside the existing
   `locations/tasks.write`, since the Requests page files notes and tasks), let me know and I'll add it next run.
3. Should the "Atlas One apps" private integration be renamed to something clearer like "Atlas One portal + apps"
   now that it's confirmed to be the portal's token, or left as-is since other things may already reference the
   current name?
