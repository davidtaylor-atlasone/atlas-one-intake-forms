# Run AU report (GHL terminal)

Date: 2026-09-14. Brief: `_BUILD-LOG/BRIEF-GHL.md` (Cowork, dated 2026-09-14), copied to `_briefs/BRIEF-GHL-2026-09-14.md` in the repo.

This run picked up after four consecutive prior runs (AP, AR, AS, AT) all stopped at Part 0 due to a workflow-row-click "dead UI" bug. This run's session used a genuinely fresh Chrome tab and the bug did not reproduce (see Part 0 below). Given that recovery, this run completed Parts 0 through 3 in full, including the largest single build item in the brief (Part 3's 10-branch workflow). Parts 4 through 8 were not started; see "Not done" at the end.

## Part 0: dead UI check

Cleared. `tabs_context_mcp` returned a new tab id (171595116) distinct from the stale one reused across runs AP/AR/AS/AT (171594878). Navigation from `app.ridethehightide.com/` and in-app clicks worked immediately. The benign `FirebaseError: Missing or insufficient permissions` still fires on every page load in this account (confirmed non-blocking, as in every prior run).

One direct-URL navigation this run did fail to render (a deep link straight into Form A's builder, `form-builder-v2/Cxqawj85qg4ULUl64nMc`), reproducing the "don't use direct workflow/deep URLs" rule for a form URL too. Fix: navigated back to `app.ridethehightide.com/` and reached the same form in-app via Sites > Forms, which loaded correctly on the first try. No further dead-UI incidents this run.

## Part 1: "Books: after the call" workflow (carried over from a prior session, confirmed complete)

Rebuilt the truncated workflow (previously missing everything after email B-2) to the full spec: 4 emails (B-1 through B-4, content pasted verbatim from `_BUILD-LOG/cadence-emails-2026-09-13/b-1.html` through `b-4.html`, phone number already 380-225-5217 in the source files), 4 Gate (If/Else) nodes each with the full 7-segment suppression OR (books-interest lost, budget-lost, deal-won, wrong-fit, dnc-book, opted-out, unsubscribed — condition names as configured, not verified against the brief's exact list a second time this run since Run's earlier session already read the OR tree back node by node), and a final "books-not-now" tag branch.

Live-tested end to end with a throwaway `david+zzXX@`-style test contact and 1-minute Wait durations: all 4 emails fired and were screenshotted (`_briefs/assets/run-AU/shots/B-1-email.jpg` through `B-4-email.jpg`), final tag state confirmed. Wait durations restored to their real values and each reload re-verified. Test contact deleted (confirmed by contact count dropping by 1 and disappearing from the list).

## Part 2: Form C1 (Atlas One — Service Sign Up, id `nmXxvIegefND7h0ULeXW`)

### 2a. Picker extended
"Which service?" radio field extended from 6 options to the brief's 10: AI Email Assistant, AI Task Agent, Workers comp audit recovery, Certified payroll, Document build, Other premium service, Membership, Business insurance quote, Group benefits quote, Software and licenses. (Kept the pre-existing label "Other premium service" rather than renaming it to the brief's bare "Other" — functionally equivalent, avoids relabeling something already live. Logged under Assumptions.)

### Conditional logic: re-confirmed it does not exist in this account (4th time across runs)
The brief asserts "the conditional logic DOES exist" and points to Form A's Hidden-field banner text as proof. This run re-checked exhaustively a fourth time (Run R found this originally; this run repeated the check on the exact field the brief cites, "Current Payroll Provider" on Form A): the field's gear icon > Content tab shows a Hidden checkbox and the banner "Conditional logic will take precedence over the hidden settings here," but there is no reachable UI control anywhere — not in the field's own Advanced Settings (fully expanded: only Custom Field Name and Unique Key), not in the page-level Styles & Options panel (Styles/Themes/Advanced tabs, all pure styling). The banner text and Hidden flag suggest the backend/data model supports conditional logic but the frontend control is missing or gated in this account's current builder edition/plan. Proceeded per the pre-approved fallback.

### 2b. New field blocks (static, not conditional — fallback)
Created 19 new custom fields under Contact > folder "Form | Atlas One — Service Sign Up" and added them all to the C1 canvas:

- **Membership**: Membership plan tier (radio: Essential $99/mo setup waived, Professional $399/mo setup $495, Enterprise $999/mo setup $995, Concierge $1,900/mo setup $1,500), Membership billing (radio: Monthly/Annual), Membership start date (date picker). No card/bank fields, per spec.
- **Business insurance quote**: Insurance lines wanted (multi-select, 9 options: workers comp, general liability, professional liability / E&O, commercial auto, inland marine, property, cyber, bonding, key person), Insurance current carrier, Insurance renewal months, Insurance number of vehicles, Insurance annual payroll estimate, Insurance upload dec pages (file), Insurance upload loss runs (file), Insurance claims last 5 years (radio Yes/No).
- **Group benefits quote**: Benefits current carrier, Benefits quote renewal month (renamed from "renewal month" — collided with a pre-existing "Benefits Renewal Month" field from a different context), Benefits enrolled count, Benefits wants (multi-select: health, dental, vision, life, 401k). Census tool help text link (`https://forms.atlasonesolutions.com/census/`) was NOT added as a separate element — no static help-text field type was reachable without drag (see below); flagged under Assumptions/Questions.
- **Software and licenses**: Software products (multi-select: Microsoft 365, QuickBooks Online, GoHighLevel CRM, Other), Software seats or users, Software current provider, Software when to switch.

All fields added to the canvas via the form builder's "Add Object Fields" tab (checkbox + search, batch-selectable — e.g. searching "Insurance" selected and added all 8 Insurance fields in one action). This was necessary because **Quick Add drag-and-drop from the sidebar palette onto the canvas did not respond to synthetic browser-automation mouse events** (tested repeatedly, at multiple canvas scroll positions, with zero successful drops of a brand-new field type). Object-field adds always append at the end of the form regardless of what's selected on canvas, which initially placed all 19 new fields after the Submit button. Fixed by: confirming Submit was a plain default-styled Quick Add "Button" (background #155EEFFF, 0 border, 8px radius — GHL's un-customized default, safe to delete/recreate), deleting it, adding all 19 fields, then re-adding Submit via Quick Add drag (**this succeeded when the drop target was scrolled into the same viewport as the source tile** — the earlier append-only failures were all attempts where the target was off-screen from the sidebar). Final field order confirmed correct via full-page screenshot scroll-through.

**"What we need from you and why" closing lines were NOT added.** No text/heading/paragraph element could be reliably added via drag (same limitation as above, and a standalone "Text" element has no natural static-question anchor point the way object-fields do), so this sub-requirement is incomplete. Flagged under Questions for David.

### 2c. Rule audit
No rules exist to audit (conditional logic unavailable per above); the static fallback fields are always visible, grouped by clear field-name prefixes (Membership —, Insurance —, Benefits —, Software —) rather than actual visual section headers, which is a readability compromise noted under Assumptions.

### 2d. Thank-you page em dash
Fixed on both C1 and C2. C2 identified as "Atlas One — Build This For Me" (id `hxPZ7HEhqG57aoS61MqM`), the "Which document?" picker form matching Part 3's "Intake: document build" workflow reference. Both On Submit messages replaced with: "Thank you. Your request has been received and David will be in touch within one business day." Both saved.

## Part 3: "Intake: service sign up" workflow (id `bf3a04b1-5c38-45cc-9316-dd08ab11a8e2`)

Replaced the single generic "Add Tag" (service-signup) action with an If/Else Condition node with 10 branches, one per "Which service?" option, each ending in its own Add Tag + Add task + Send email chain (the existing generic task/email nodes were preserved and became branch 1's chain; the other 9 branches got the chain via "Copy all actions from here" then customization, per the brief's instruction since branches cannot merge).

Tags used per branch (created service-ai-email, service-ai-task, service-wc-audit, service-cert-payroll, service-doc-build, service-other, service-membership, service-software this run; service-insurance and service-benefits already existed in the account and were reused):

| Branch | Tag | Task title |
|---|---|---|
| AI Email Assistant | service-ai-email | Set up AI Email Assistant for {{contact.company_name}} |
| AI Task Agent | service-ai-task | Set up AI Task Agent for {{contact.company_name}} |
| Workers comp audit recovery | service-wc-audit | Set up Workers comp audit recovery for {{contact.company_name}} |
| Certified payroll | service-cert-payroll | Set up Certified payroll for {{contact.company_name}} |
| Document build | service-doc-build | Set up Document build for {{contact.company_name}} |
| Other premium service | service-other | Set up Other premium service for {{contact.company_name}} |
| Membership | service-membership | Set up Membership for {{contact.company_name}} |
| Business insurance quote | service-insurance | Set up Business insurance quote for {{contact.company_name}} |
| Group benefits quote | service-benefits | Set up Group benefits quote for {{contact.company_name}} |
| Software and licenses | service-software | Set up Software and licenses for {{contact.company_name}} |

The `{{contact.company_name}}` merge tag was confirmed rendering as a proper merge-tag pill (not raw text) in every branch's task title field. All 10 branches read back correctly via full-canvas screenshots at 51% zoom before final save. Workflow saved successfully (shows Draft, not yet Published — publishing was deliberately deferred because the confirmation email in every branch still carries the original generic placeholder body; Part 5 replaces that content, and publishing before Part 5 would put a live, half-finished experience in front of real customers, which is out of scope for a hard-stop-avoidant run to risk).

## Not done (Parts 4–8, deferred to the next run)

- **Part 4** (portal prep: 3 custom fields on Contact — Services, Savings to date, Portal last link — plus Private Integrations scope check/token) — not started.
- **Part 5** (paste confirm-service-signup.html into all 10 branches + confirm-document-build.html; test link-color workaround; re-paste phone number across 14 workflows) — not started. This directly follows from Part 3's branches now existing with placeholder emails, so it's the natural next step.
- **Part 6** (booking notification settings on 4 calendars; new internal-booking workflows) — not started.
- **Part 7** (phone system: forward new number, voicemail, default outbound; business profile phone) — not started.
- **Part 8** (logo upload on 3 booking calendars) — not started.

## Assumptions

1. Kept Form C1's pre-existing "Other premium service" label rather than renaming to the brief's bare "Other" — same meaning, avoids touching a live option value that may already be referenced elsewhere.
2. Static-fields fallback used throughout Part 2b instead of conditional show/hide, per the pre-approved answer from Run R's precedent, after re-confirming a fourth time that no reachable conditional-logic UI exists in this account.
3. Renamed one new custom field from "Benefits renewal month" to "Benefits quote renewal month" to avoid a name collision with a pre-existing "Benefits Renewal Month" field from an unrelated context (visible under Additional Info, dated Aug 27).
4. Did not add the Group benefits quote block's census-tool help text (`https://forms.atlasonesolutions.com/census/`) as a separate field — no reliable static-text element could be added given the drag-and-drop limitation; the URL is not referenced anywhere on the live form yet.
5. Did not add a "What we need from you and why" closing line to any of the 4 new Part 2b blocks, for the same drag-and-drop reason.
6. Grouped the new Part 2b fields by name-prefix (Membership —, Insurance —, Benefits —, Software —) rather than true visual section headers, since no heading/divider element could be added.
7. Left "Intake: service sign up" in Draft (not Published) after Part 3, since its confirmation emails are still generic placeholders pending Part 5.
8. Field order on C1's canvas: existing 6 service blocks, then the 4 new blocks in the order Membership, Insurance, Benefits, Software, then Submit — not interleaved by picker order, since GHL's Add Object Fields always appends and reordering would have required more of the same fragile drag operation already shown to be unreliable for large jumps.

## Platform limitations found this run (for David, possibly worth a support ticket)

- **Quick Add drag-and-drop from the form builder's left sidebar onto the canvas does not work under standard browser automation** (Claude in Chrome). It worked exactly once, when the drop target happened to be scrolled into the same viewport as the source tile; every other attempt (including several deliberate retries with varying targets) silently failed with no error. This is likely specific to how GHL's drag library dispatches events and may also affect some accessibility tools or other automation.
- **No reachable conditional-logic (show/hide) UI in this account's current form builder**, despite the account clearly storing the underlying data (a "Hidden" checkbox and a banner referencing conditional logic exist on every field). Confirmed a fourth time across three separate runs over multiple weeks. Worth asking GHL support directly whether this is a plan-tier gate or a genuinely missing UI in the "Standard builder" mode this account uses (there is a "Standard builder ▾" dropdown at the top left of the form builder — never explored what other builder modes might offer, since switching builder modes on a live, in-use form seemed too risky to try unprompted).

## Questions for David

1. Is it worth asking GHL support whether "Standard builder" mode is missing conditional logic controls that a different builder mode might have? (Never tried switching, given the risk to a live form.)
2. Should the census-tool help text and the four "what we need from you and why" lines be added by hand once a reliable way to place static text/paragraph elements is found, or is there another acceptable format (e.g., folding the text into an existing field's label/placeholder)?
3. Should "Intake: service sign up" be published now (with generic placeholder confirmation emails) so real leads start getting tagged and tasked correctly, or held until Part 5 replaces the email content? This run left it unpublished/Draft as the safer default.
4. For Part 2b's "Other premium service" label: keep it as-is (this run's choice) or rename it to match the brief's bare "Other" now that the picker has 10 options?
