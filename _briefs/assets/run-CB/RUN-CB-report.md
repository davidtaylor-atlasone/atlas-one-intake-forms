# RUN-CB Report (2026-09-20)

Conversation AI and Knowledge Base are available and fully configurable on this account (not locked behind the agency); a Knowledge Base already exists with one entry from 29 Aug 2026.

Client: 90 day pulse is now ready for David to publish (Part 67 rebuilt it to match the brief exactly).

## Part 67: Client: 90 day pulse made ready to publish

Workflow `52bf136f-2f90-4524-bc8a-8851fd1b3052`, still Draft (David publishes).

What was found: the Draft had a trigger (Contact Tag added includes `client-current`), a Wait - 90 days step, and a Task step wired directly to each other with **no If/Else gate at all**, and the task's title/description did not match the brief's exact wording.

What was built:
- Trigger: Contact Tag added includes `client-current` (unchanged, already correct).
- Wait: 90 days (unchanged, already correct).
- Added a new If/Else gate named "Still a client?": Yes branch = Tags includes `client-current`; None branch (renamed from default) ends the workflow.
- On the Yes branch: the existing Task action, edited to match the brief exactly:
  - Title: `90 day staff pulse: {{Contact.Company Name}}`
  - Description: "Open portal.atlasonesolutions.com/admin/pulse, pick this client, create a round named 90 day, copy the one click link and send the owner the ready made email from that page, then compare the new score with the Audit round."
  - Assigned to David Taylor, due 0 days (same day) — both already correct, left as is.
  - Then End Workflow.
- No client-facing email step existed anywhere in the Draft, so there was nothing to remove per that part of the brief.

**Assumption 1:** The gate's first build attempt landed *before* the Wait step (checking the tag immediately at trigger time, which is always true right after the tag is added) rather than after the 90-day wait. Caught this before finishing, used the builder's "Move action" feature to relocate the Wait step above the gate so the check now correctly happens 90 days later. Verified the final order via fresh navigation and reload: Trigger → Wait 90 days → Still a client? → Yes: Task → End; None: End.

Screenshots 01–25 in `_briefs/assets/run-CB/shots/`.

## Part 68: 15-Minute Strategy Session calendar renamed

Read first, recorded (read only):
- Calendar `Atlas One — 15-Minute Strategy Session` (id `HMzFRKKpw63vc5QHNbcH`, 30 min) is **not** in the "Book time with David" group (Group column blank, matches "Not grouped: 01" in the sidebar).
- Custom URL slug: `atlas-one-15-minute-intro-call-hoswpko53su` — this oddly carries "intro-call" naming despite being the Strategy Session calendar. **Flagging this for Cowork/David as a naming mismatch worth a closer look.**
- Only team member: David Taylor (Zoom meeting location).
- Zero upcoming appointments on this calendar (checked the Appointment list view; all 8 upcoming rows were on other calendars).

Renamed: display name only, via Calendars > Meetings > Calendars > edit pencil > Basic details. `Atlas One — 15-Minute Strategy Session` → `Atlas One 15 Minute Strategy Session` (em dash removed). Slug confirmed unchanged before and after (`atlas-one-15-minute-intro-call-hoswpko53su`), so no booking URL changed. Nothing else touched; other calendars untouched.

Verified via fresh navigation (root → Calendars → Calendar settings): row reads the new name, same Id, Date updated bumped to Sep 20 2026 11:53 AM.

Screenshots 26–32 in `_briefs/assets/run-CB/shots/`.

## Part 69: Chat widget greeting bubble stopped

Widget id `6aa875b1c8d7749cb09681cf` ("A2P Compliance Chat Widget Mixed"), opened via Sites > Chat Widget > Library.

Read and screenshotted every current setting first: Style tab (Sticky placement, Chat prompt toggle ON — this was showing the floating "Hi there! Have a question? Chat with us here." bubble — chat icon, theme, widget customization all default); Chat window tab (Title & intro text, contact form fields Name/Phone/Message, Additional options had "Load on user interaction" OFF, Agency branding locked by A2P compliance, a Redirect call-to-action toggle off with a note it's "not suggested if Conversation AI is active"); Messaging tab (Acknowledgement and Language sections only, no auto-open setting there).

The exact setting controlling the bubble: **Style > Appearances > Chat prompt** toggle. Turned it **off**. Live preview confirmed the bubble disappeared while the round launcher icon stayed visible and clickable. Nothing else changed — colors, texts, agent, routing, and channel options all left exactly as found.

Saved (confirmed with a "Chat widget saved successfully" banner). Verified via fresh navigation (root → Sites → Chat Widget → Library, reopened the row showing "Updated on Sep 20 2026 11:59 am"): Chat prompt toggle reads off, no bubble in the reloaded preview, launcher icon still present.

**Setting changed:** Style > Appearances > Chat prompt. Before: ON (bubble auto-displayed). After: OFF (bubble suppressed, launcher icon unaffected).

This closes the "greeting bubble covers the cross-sell card" defect from the P9 audit on the GHL side.

Screenshots 33–43 in `_briefs/assets/run-CB/shots/`.

## Part 70: Conversation AI / Knowledge Base availability (read only, nothing enabled)

**Answer: Conversation AI and Knowledge Base ARE present and fully configurable on this white label account, not locked behind the agency.** A Knowledge Base already has one existing entry (quota 1/15, created 29 Aug 2026) — someone has already started using it.

Checked, without clicking Enable/Create/Activate/Upgrade/Subscribe/Buy on anything:
- Left nav "AI Agents" — present, not locked.
- "Getting Started" tab — a sales/marketing landing page with a "Get Started" button; not a config screen, left un-clicked.
- "Conversation AI" tab — present, Agents List / Dashboard sub-tabs, empty agent list, a "Create Bot" button visible but **not clicked**.
- "Knowledge Base" tab — present, one row "Existing knowledge base", KB gaps 0, created/updated 29 Aug 2026 8:21 AM, a "Create knowledge base" button visible but **not clicked**; did not open or edit the existing entry.
- Settings > Billing > Wallet & Transactions > Usage Overview (Sep 2026): total spend $26.96, top spend "A2P Registration" $22.05; product categories are Messaging / Email / Voice / Workflow Actions / Other — **no AI or Conversation AI line item anywhere**, so no AI usage has been billed yet and there is no AI-specific pricing text on this account to copy word for word.
- Chat widget settings (Part 69's widget): no dedicated AI or bot toggle in Style, Chat window, or Messaging tabs — only the note under Chat window > Title & intro > Redirect call-to-action that enabling it "is not suggested if Conversation AI is active," confirming the two features are meant to interact but the widget itself has no AI on/off switch.

No card or confirmation screen was ever shown since nothing was clicked.

Screenshots 44–48 in `_briefs/assets/run-CB/shots/`.

## Part 71: read only checks, nothing changed

**(a) ZZTest cleanup:** Contacts search for "ZZTest" returned **0 contacts** ("No contacts found") — none remain; David's own cleanup pass already removed them all. Appointment list view (Upcoming tab) searched by title for "ZZTest" also returned **zero results** ("No upcoming appointments") — confirmed nothing survives on the 30-Minute Back-Office Audit calendar (or anywhere) for Sep 22–30 or any other date. One unrelated test-named row remains on that calendar in the general Upcoming list (`RunBW-TestA + David Taylor`, Sep 22) but its contact is not named ZZTest, so it is out of scope for this check.

**(b) Booking: after the call** (`d928c199-70af-4134-9bc2-000cfe7d2b30`): confirmed **Published**. Reopened the "Next step already sent?" gate and confirmed all four segments — `Tags includes form-a-sent` OR `Tags includes form-b-sent` OR `Tags includes proposal-sent` OR `Tags includes audit-offer-sent` — all four joined by OR, matching Part 64's fix. Closed via Cancel; the workflow-level Save button stayed disabled/"Saved," confirming no accidental change survived.

**(c) Audit: prep email** (`f9162dd7-692e-4f91-80af-76c4d034ccb6`): confirmed **Published**. Reopened the "Skip prep email?" gate and confirmed all three segments — `Tags includes client-current` OR `Call purpose Is I am already a client` OR `Call purpose Is Something else` — matching Part 63's fix. Closed via Cancel.

Screenshots 49–56 in `_briefs/assets/run-CB/shots/`.

## Assumptions

1. Part 67: the Draft's task title/description did not match the brief's exact wording, so I rewrote both to match the brief verbatim rather than leaving the pre-existing (different) copy in place.
2. Part 67: after discovering the gate had landed before the Wait step on first attempt, I used the builder's "Move action" feature to correct the order rather than deleting and rebuilding, since deleting the If/Else node would have deleted its nested Wait and Task actions too (confirmed via the delete-confirmation dialog's warning before backing out of it).
3. Part 68: renamed display name only; left the mismatched intro-call-flavored slug untouched since the brief said "if renaming would change the booking URL, stop," and a slug change was never attempted so the URL never changed.
4. Part 69: "Chat prompt" was judged to be the "automatic greeting or auto open behaviour" the brief asked to disable, distinct from "Load on user interaction" (which delays the entire widget including the launcher icon and was already off) — chosen because turning it off left the launcher icon behavior unchanged in the live preview, matching the brief's requirement exactly.
5. Part 70: treated the presence of an actual "Create Bot" / "Create knowledge base" button (versus a paywall, lock icon, or upsell screen) as proof the features are "present and configurable," not merely "present but locked."

## Questions for David

1. Part 68: the Strategy Session calendar's custom URL slug (`atlas-one-15-minute-intro-call-hoswpko53su`) is named for the Intro Call, not the Strategy Session. Was this calendar cloned from the Intro Call calendar at some point? Worth deciding whether to fix the slug (which would change the booking URL) or leave it as a historical artifact.
2. Part 70: since Knowledge Base already has one entry from 29 Aug 2026 (before this run), who created it and what does it contain? This affects whether the support-desk-and-knowledge-base plan can build on existing work or needs to start over.
3. Part 71a: the `RunBW-TestA + David Taylor` appointment on Sep 22 on the 30-Minute Back-Office Audit calendar is a leftover test booking from an earlier run (not ZZTest-named, so out of this Part's scope) — should it be cancelled?
4. Part 67: Client: 90 day pulse is Draft and ready — should it be published now, or is there anything else you want checked first before it goes live?
