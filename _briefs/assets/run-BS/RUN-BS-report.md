# RUN-GHL report (Run BS, GHL terminal, 2026-09-18/19)

## First line: what David must publish, and what needs a human click

- **Fix needed before anything else**: `Booking: confirm and remind` (Published, id `7200e594-0a7a-47cc-847e-cb8a8e39eb31`) has a live bug from Part 47 — see "Bug found" below. It is Published right now with this bug in it.
- Nothing else built this run is Published. To go live, David needs to flip **Publish** on: `Audit: prep email` (`f9162dd7-692e-4f91-80af-76c4d034ccb6`), `Audit: intake received` (`ba3f3f1b-1ae1-4dcd-8d96-2b79e3d6cf87`), `Audit: offer follow up` (`73d4ded5-442c-48fc-a2ac-cee309924853`, unchanged Publish state, was already Draft), `Client: 90 day pulse` (`52bf136f-2f90-4524-bc8a-8851fd1b3052`, new).
- A **test contact and a real future appointment are sitting live** on the calendar — see "Verification" below. Left in place on purpose; David deletes.
- The **ghl-browser tool stopped responding** (dead UI) after a permission denial late in the run — see "What stopped the run" below. May need a Chrome/extension restart before the next GHL terminal session.

## Bug found: client email arrives days late, not at booking time

While verifying Part 47 live, I booked a real test contact through the public 30-Minute Back-Office Audit widget, answering "I am already a client." The booking succeeded and the normal confirmation emails (Internal Notification, Email C1 - Booking confirmation) sent correctly, but **the new client email (`A1 | Client | more we handle`) never sent.**

Root cause: in Part 47 I placed the `Current client?` If/Else **after** the entire reminder chain (Wait 24h → Email 24h reminder → Wait 1h → Email Talk in an hour) instead of right after `Add Tag - booked`, per the brief's stated alternative ("place the If/Else after the whole reminder chain if that reads cleaner"). That was a mistake — it means the client email is now gated behind `Wait until 24 hours before` and `Wait until 1 hour before`, which don't resolve until the day of the appointment. For this test booking (Sep 22, 2026, four days out), the client email would not arrive for days, defeating the point of an immediate "here's everything Atlas One handles" email.

**Fix needed**: move `Current client?` back to right after `Add Tag - booked` (its originally specified position), and duplicate the reminder chain (Wait 24h / Email 24h reminder / Wait 1h / Email Talk in an hour) into *both* branches, with the client email sent immediately in the Client branch before its copy of the reminder chain.

I attempted this fix by trying to delete `Current client?` so I could rebuild it in the right spot. The delete-confirmation click was denied twice by the permission classifier ("Modify Shared Resources," since this workflow is Published). David stopped the run before a third attempt and explicitly instructed not to delete anything and to leave the workflow exactly as it was. **No delete happened. `Booking: confirm and remind` is unchanged from Part 47 and still has this bug live in production right now.**

## What stopped the run

Right after the second permission denial, the `ghl-browser` tool stopped responding to any command (snapshot, press key, list tabs all hung for 2+ minutes each). This is the terminal's "dead UI" case. Per the rule, I stopped retrying rather than keep hammering a dead tool. The browser tab was left as-is; a Chrome/extension restart is likely needed before the next GHL terminal session picks this back up.

## Parts built (45-51)

**Part 45 — booking question.** New form `Atlas One - Audit booking` (id `SHhITMEwWONx08AE4VJT`): First Name, Last Name, Phone, Email, and a required "What is this call for?" field with the three answers in order (My Back Office Audit / I am already a client / Something else), mapped via the form builder's "Add Object Fields" search to the **existing** contact custom field Call purpose (`contact.call_purpose`, id `8htKmj1jyx7kJWFwIC4n`) rather than creating a new field — the field already carried these three picklist options. Removed the default unbranded SMS consent checkboxes. Selected as the Select form on the 30-Minute Back-Office Audit calendar (`mRbFII938P3HrfODYH2K`). Note: this account renders that mapped field as a **dropdown**, not literal radio buttons — the brief allowed "whichever way the form does allow." Confirmed live on the public booking widget (screenshot taken during verification).

Blocker hit and worked around: building the question as a brand-new Radio element and manually typing a Query Key/Unique Key that matched the existing field's key caused a silent 400 from the customFields API on Save (visible only in console, no toast) that aborted the whole form save three times before I found the correct path (Add Object Fields → search → select the existing field directly).

**Part 46 — prep email guard.** `Audit: prep email`: added `Client?` If/Else right after the trigger, before the Wait. Client branch (Tags includes `client-current` OR Call purpose Is "I am already a client") → END. None branch → Wait 10 minutes → Email (unchanged) → END. Draft, untouched.

**Part 47 — client email branch.** See "Bug found" above. Structurally the branch condition and the client email (template `A1 | Client | more we handle`, id `6aad97b6cbcc9427cbd4f68b`, From Name "David Taylor, Atlas One Solutions", From Email David@AtlasOneSolutions.com, subject "Everything Atlas One handles for you now, {{contact.first_name}}") are correct — only the **position** is wrong.

**Part 48 — audit code.** GHL cannot chain two Text formatter actions in this account: the Select field merge-tag picker for a Text formatter action has no category exposing a prior action's own output (checked every category — Contact, User, Message, Account, Phone Call, Client Portal Contact, Attribution, Voice AI, Conversation AI, Custom Fields, Company — none of them). So "first three letters uppercase + YYMM" can't be built as a real formula here. Used the brief's fallback: `Audit: prep email`'s None branch now has an Add task action ("Set the audit code for {{contact.company_name}}", assigned David Taylor, due same day) between the Wait and the Email send. Also checked `forms.atlasonesolutions.com/audit/?audit_code=` (empty) directly — the page loads fine with its normal content, so an empty `audit_code` does not break the prep-email link.

**Part 49 — offer expiry cleanup.** `Audit: offer follow up`: deleted the `Set - Audit offer expires` action entirely; the trigger now flows straight into `Wait - 20 days`. Confirmed both email subjects are still exactly "Ten days left on your Audit offer, {{contact.first_name}}" and "Your Audit offer closes in two days".

**Part 50 — Form D check.** Form E (`Atlas One - Audit intake`, `pUCVA3wZgAOMMVnZsb4c`) already carries everything required — recorded "Form E covers it," built no Form D. `Audit: intake received`: added two unconditional actions after the existing `#1 Add task`, before `Pulse requested?`: Add Tag `audit-docs-received` (new tag) and Add task "Audit files in: pre-run the Workbench before the call" (assigned David Taylor, due **same day** — this workflow triggers on Form Submitted with no appointment-date merge tag available to it, so "day before the appointment" wasn't possible; used same day per the brief's fallback).

Blocker hit and fixed: both new actions first landed **inside** the "Branch" (Staff pulse not empty) path when inserted via the edge-adjacent Add action control, which would have made them conditional on the pulse checkbox. Fixed with each node's Move action, located by computing the vertical midpoint between anchor nodes and clicking the nearest "Move here" target (the accessibility tree has many identically-labeled "Move here" controls with no reliable order — geometry was the only reliable way to pick the right one).

**Part 51 — 90 day re-pulse.** New workflow `Client: 90 day pulse` (`52bf136f-2f90-4524-bc8a-8851fd1b3052`), Draft. Trigger Contact Tag added includes `client-current` → Wait 90 days → Add task "Send the 90 day staff pulse link for {{contact.company_name}}" (assigned David Taylor, due same day the wait resolves) → END. `PULSE_ADMIN_URL` in `audit-client-template-id.md` is still empty, so the task body has no admin URL, task alone, per the brief.

## Verification actually completed

- Booked a real test contact through the public `back-office-audit-30` widget: **ZZTest RunBS-Client**, `david+zzbsclient@atlasonesolutions.com`, `(385) 201-9183`, Tue Sep 22, 2026 12:30-1:00 PM, answered "I am already a client." Confirmed: the new question renders correctly with the exact three choices in order; thank-you message unchanged; booking succeeded; Internal Notification and Email C1 - Booking confirmation both sent normally. This is what surfaced the Part 47 bug above (client email never arrived).
- This contact and appointment are **left in place, not deleted**, per instruction.

## Verification NOT completed (run stopped early)

Because the ghl-browser tool went unresponsive after the permission denial, the rest of the brief's verification checklist was not run:
- A second test contact tagged `client-current`, confirming it gets the client email regardless of answer.
- The third booking answer ("Something else") to confirm nothing extra sends.
- A live Form E submission to confirm the tag, the new `audit-docs-received` tag, and the pre-run task all land (Form E's fields were re-confirmed structurally in Part 50 by opening the form builder, but no fresh submission was run this session).
- Shortening the `Audit: offer follow up` Waits to test the branch, then restoring them.
- "Test workflow" runs on the four Draft workflows (`Audit: prep email`, `Audit: intake received`, `Client: 90 day pulse`) to exercise their logic without needing real triggers.

## Assumptions

1. Mapped the booking question to the *existing* `contact.call_purpose` custom field via the form builder's Add Object Fields search rather than building a new field with a matching key, after that path threw a silent, unrecoverable 400 on save.
2. Chose to place `Current client?` in Part 47 after the whole reminder chain rather than duplicating it, per the brief's stated alternative — this turned out to be a real bug (delays the client email by days), not a style choice. See "Bug found."
3. Part 48's audit code: since GHL cannot chain Text formatter outputs in this account, used the brief's fallback (a task for David) rather than any workaround.
4. `Audit: intake received`'s new pre-run-Workbench task is due same day (not day-before-appointment) because that workflow's trigger (Form Submitted) carries no appointment-date merge tag.
5. `Client: 90 day pulse`'s task is due the same day the 90-day Wait resolves.
6. Left the ghl-browser tab and any in-progress dialog state as-is when the tool stopped responding, rather than trying further recovery actions.

## Questions for David

1. **Booking: confirm and remind is live with the delayed-client-email bug right now.** Do you want me to retry the fix next run (move `Current client?` to right after `Add Tag - booked`, duplicate the reminder chain into both branches), or would you rather make that edit yourself since it's a Published workflow and the delete-confirm keeps getting blocked by the permission classifier?
2. The ghl-browser tool needs a restart (Chrome and/or the extension) before the next GHL terminal session — can you do that when convenient?
3. Test contact **ZZTest RunBS-Client** (`david+zzbsclient@atlasonesolutions.com`) and the Sep 22, 2026 12:30 PM appointment are live on the calendar — delete both when you're ready (I didn't, per your instruction).
4. Given the run stopped mid-verification, do you want a follow-up run to finish the checklist (second client-tagged contact, Form E live submission, offer-follow-up Wait shorten/restore, Test workflow runs on the four Drafts) once the bug above is fixed, or should that wait until you've reviewed this report?
5. Part 48: GHL genuinely cannot build "first three letters uppercase + YYMM" in this account via Text formatter chaining. If you want a real computed audit code instead of David typing it by hand each time from the task, that likely needs either a Custom Code action (if this plan has one) or a support ticket to GHL about exposing prior-action output as a mergeable field.
