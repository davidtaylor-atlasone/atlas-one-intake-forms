# Run CL report (GHL terminal, 2026-09-26)

All of Job 0 through Job 6 in the brief are complete. GoHighLevel browser only, no sends, no publish/unpublish
of any existing workflow, no deletes, no spend, HIPAA never touched, QuickBooks/payment provider Connect never
clicked. Screenshots at `_briefs/assets/run-CL/shots/`. Facts for the how-to suite at
`Master_Kit/_BUILD-LOG/ghl-howto-facts-2026-09-25.md`.

## Job 0: WSA Scottsdale conference tracking (published, one exception to the no-publish rule as instructed)

- Finished the "Atlas One - Intro call booking" form: added the existing Promo code field just above Submit,
  label "Promo code (optional)". The "What is this call for?" dropdown offered "My Back Office Audit / I am
  already a client / Something else" -- since one option was audit-specific, deleted that field from this copy
  only (the original Audit booking form was never touched). Saved and previewed
  (`job0a-form-preview.png`).
- Attached the form to calendar "Atlas One 15 Minute Intro Call": Advanced settings > Form & confirmation,
  switched to the custom form. The sticky-contact/consent toggles disappeared from that panel once a custom
  form was selected (that setting moved to the form level, nothing lost). Redirect URL unchanged. Confirmed the
  Promo code box appears on the live booking widget (`job0b-booking-form-promo.png`). Did not book a slot.
- Built and published workflow "WSA Scottsdale 2026: tag by code or UTM" (lives in Home folder; no dedicated
  Atlas One lead-workflow folder exists in this account). Three triggers: Customer Booked Appointment (calendar
  = Atlas One 15 Minute Intro Call), Form Submitted (any form), Contact Changed (Promo code has changed).
  If/Else branch "WSA" (OR): Promo code Contains WSA2026 / wsa2026 / Wsa2026, OR UTM Source (First Attribution)
  Is wsa-conference. GHL has no case-insensitive contains operator and no "UTM Source (Last Attribution)"
  option at all (Last Attribution only exposes Content/Medium/Campaign/Keyword/Match Type) -- hence the three
  explicit case variants and First Attribution only. WSA branch: Add Tag wsa-scottsdale-2026, Add Note "WSA
  conference: $250 Atlas One credit plus Cornerstone offer". None branch empty. Allow re-entry OFF. Published
  (`job0c-published.png`).
- Tested: created contact "TEST WSA Promo" (test-wsa-promo@atlasonesolutions.com, no phone), set Promo code to
  wsa2026, tag and note both appeared within about a minute (`job0d-test-note-confirmed.png`). Removed the tag
  afterward, left the note and the contact.
- Built smart list "WSA Scottsdale 2026" (filter Tag is wsa-scottsdale-2026), captured with the test contact in
  it before removing the tag a second time (`job0e-smartlist-with-test-contact.png`).

## Job 1: stray ">" fix (five templates)

All five templates' source ended in `</table>>` before this run; each now ends in exactly `</table>` with
nothing after, confirmed by reopening each fresh after Save.

| Template | Before (end of source) | After |
|---|---|---|
| P-BUILDER-DELIVERY (6aa370697919774ef2ed8f30) | `...</table>>` | `...</table>` |
| P-MEMBER-WELCOME (6aa37036a813792f409bf1a9) | `...</table>>` | `...</table>` |
| P-W7-1 (6aa0a9f855d1ce8973c141a2) | `...</table>>` | `...</table>` |
| P-W7-2 (6aa0a9f955d1ce8973c141a8) | `...</table>>` | `...</table>` |
| P-W7-3 (6aa0a9fb6ec737a976fa481f) | `...</table>>` | `...</table>` |

Technique note: Monaco virtualizes rendering when the whole file is one long word-wrapped line, so Cmd/Ctrl+End
does not reliably reach true document end. Fix: repeated PageDown until the rendered lines stop changing, then
End, then Backspace once. Added this exact standing-rule line to the top of `email-templates-map.md`. The three
W7 templates keep their Cornerstone identity untouched (guard line already present in the map file).

## Job 2: hide unused Contact/Company/Opportunity fields

**Contacts (done):** Created custom view "Atlas One standard view", assigned to both David Taylor and Charity
Taylor. Removed 14 tabs that were 100% HIDE rows (Multi Account Management, Prospecting Agent Information, SMS
information, Deal information, Sales properties, Facebook Ads properties, Zoom, Conversion information, Social
media information, Outsourcing Offshoring Information, Order Information, Email information, Contact Lifecycle
Stage Properties, Web analytics history, Contact activity, Calculated Contact Information, "Form | ZZ scratch
add-field test"). Reduced two mixed tabs: Additional Info 69 -> 67 fields (removed only two HubSpot
Last-Modified/Created fields, kept every Atlas One field), Contact information 153 -> 4 fields (kept only Job
Title, Industry, Annual Revenue, Number of Employees; used one batch JS click script since the UI has no bulk
remove). Net removed across all folders: ~378 fields (CSV estimated 376). Verified on a live contact (Lydia
Scheller): before/after screenshots `job2-contact-cleared.png` / `job2-contact-after-allfields.png`.

**Companies (stopped, no control exists):** Checked Settings > Objects > Companies (Details/Associations tabs
only) and a company record's edit panel -- no field-hide or custom-view control exists for the Company object
in this GHL account, unlike Contacts. Screenshot `job2-companies-no-hide-control.png`. The 147 Company HIDE
rows from the CSV cannot be hidden here; stopped after one look per the no-thrashing instruction.

**Opportunities:** 0 rows to hide per the CSV, confirmed nothing needed.

`GHL-Hidden-Fields-List-2026-09-24.md` updated: Status line now "DONE, 2026-09-26 (Run CL)" with the Companies/
Opportunity findings noted, and the "How to bring a hidden field back" section rewritten in plain words for
Contacts (open the Atlas One standard view editor, find the folder, click the pencil/edit icon on that folder,
check the field back on, save -- it reappears immediately) plus the Companies/Opportunity findings.

## Job 3: read-only fact capture for the GHL how-to suite

File: `Master_Kit/_BUILD-LOG/ghl-howto-facts-2026-09-25.md`. Nothing was changed anywhere in this job.

- **a) Workflows: all 41** (30 Published, 10 Draft, one Draft workflow completely empty/never built). Every
  trigger with its filter, every tag added/removed, every Send Email action (template, From name, From email),
  every Internal Notification, every Assign action documented as one table per workflow. Notable findings:
  workflow 7's WC/W7 pattern of a human-written "Personal Line" gate before the first email in several
  cadences; workflow 30 (W7 WSA handoff) never sends email itself, only tasks David to send by hand; the 4
  exact duplicate tag names surfaced again inside workflow logic; two Draft workflows (Portal: document ready /
  uploaded) would clear/set tags the Portal app presumably drives, currently inert since unpublished.
- **b) Forms and surveys: all 9 forms + 1 survey.** Each documented with its share link
  (`https://api.leadconnectorhq.com/widget/form/<id>` / `.../widget/survey/<id>`), every field, which workflow
  triggers on it, and whether it has a File Upload (5 of the 9 forms do). "Form 0" is GHL's unfilled default
  template, never used, should never be shared as-is. The one survey ("Free Assessment Form") is not wired to
  any workflow -- a question for David below. Quizzes: 0 built.
- **c) Record-entry screens.** Add Contact (First name only required field), Add Company (Company Name only
  required field, 325 companies exist -- an unrelated import, not linked to Contacts), Add Opportunity (Primary
  contact name is the Contact-to-Opportunity link, Pipeline/Stage picker confirmed reachable). Checked a real
  contact record for a Contact-to-Company link: none exists in this account's UI -- "Business name" is a plain
  per-contact text field, not a picker into the Companies module. Every dialog closed without saving.
- **d) Sending a form by hand.** From a contact's Conversations panel: switch channel to Email, expand the
  composer, use the Insert Link toolbar button > URL mode > paste the form's share link. A "Trigger Link" mode
  also exists in that same dialog but the account has none configured yet (a good future improvement to
  recommend). Also found that opening the Email composer auto-fills a legacy, much longer David Taylor
  signature template with a Zoom scheduler link -- see Job 6 below, now replaced.
- **e) Full tag list: 73 tags** (corrected from the brief's estimate of 71), including the exact 4 duplicate
  pairs the Cowork audit flagged (service-ai-task, service-cert-payroll, service-doc-build, service-other),
  confirmed identical spelling on both rows of each pair, no category on either. Underlying tag ids were not
  individually captured (would need opening each row's Edit dialog; flagged as a follow-up). Also found two
  likely auto-generated tags from a phone-lookup integration ("couldn't find caller name", "name via lookup")
  as a separate, smaller cleanup candidate.

## Job 4: Invoices (read only)

**Payment provider: Stripe, already connected, both live mode and test mode enabled** (Settings > Payments >
Integrations > Stripe > Manage shows a Disconnect button and two green "enabled" checks). Invoice settings:
Business Name "Atlas One Solutions LLC", logo the current A1 mark, phone +1 380-225-5217, address 1672 N. Oak
Dr., Lehi UT 84043, website atlasonesolutions.com. Invoice title "INVOICE", terms already written ("Due on
receipt unless stated. Pay by bank transfer (ACH, no fee) or card..."), Invoice Prefix "INV-", due after 0 days,
Estimate Prefix "EST-", expires after 14 days. Partial payments, late fees, and tip payments are all off.
Products: 36 real products already loaded with live Atlas One pricing (certified payroll tiers $60-$400,
Microsoft 365 tiers $7-$22/user, etc). Recurring invoices live under the same "+New" menu as "New Recurring
Invoice"; Payment Links has its own top-level tab next to Invoices & Estimates. Walked the New Invoice screen
with a TEST contact, searched the live product catalogue inline, then closed via Back, which raised a native
"unsaved changes" browser confirm; accepted it. Verified afterward: still exactly 2 real Draft invoices
(INV-000001 Scheller Enterprises $300, INV-000002 Dr Joel D Gould DDS $894, both pre-existing, untouched), no
INV-000003 was created, nothing sent.

## Job 5: QuickBooks (read only)

**QuickBooks is already connected**, not pending. It does not appear in App Marketplace at all (searched "no
apps found"; also not among the 6 installed marketplace apps) -- it is a native Payments feature reached at
Settings > Integrations > QuickBooks. That screen shows a Disconnect button (only appears when authorized) and
live sync toggles: **Contact sync OFF**, **Invoice sync ON**, Send review requests OFF. This matches the
Cowork plan's own recommendation to keep customer import off, but means every invoice already flows to
QuickBooks automatically. The "Get Started > Connect your accounting > Connect Now" banner elsewhere in
Payments is stale/misleading and does not reflect this real, already-authorized state. Nothing was changed;
no login screen was ever shown since the account is already authorized.

## Job 6: rep identity groundwork

**a) My Staff records** (exactly 2 users):

| Field | David Taylor | Charity Taylor |
|---|---|---|
| Email | David@atlasonesolutions.com | charity@atlasonesolutions.com |
| Phone | +1 385-213-7177 (unchanged) | +1 801-787-8154 |
| Extension | blank | blank |
| Role | ACCOUNT-ADMIN | ACCOUNT-USER |
| Signature before this run | ON, but a long legacy template (Zoom link, "Cell: 801-358-8547", confidentiality footer) | OFF, empty |
| Calendar field | blank ("Select Calendar") | blank |
| Verification | Forgot Password available (verified) | "Verification Email" button shown -- her account is not fully verified, matching the Cowork note that her replies would bounce until fixed |
| Phone channel usage | Available call channel (Web App / Mobile App / My Phone Number / Deskphone SIP all checked) but default Ring All/IVR channel is Web App, not the phone | not checked |

**b) Signatures set exactly as specified**, screenshots before/after save for both:

David Taylor (replacing the old Zoom-link template):
```
David Taylor, Founder
david@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · Book a time [hyperlinked to https://api.leadconnectorhq.com/widget/groups/book-david, opens new window]
Atlas One Solutions · support@atlasonesolutions.com · AtlasOneSolutions.com
```

Charity Taylor (was empty):
```
Charity Taylor, Business Advisor
charity@atlasonesolutions.com · 801-787-8154
Atlas One Solutions · support@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · AtlasOneSolutions.com
```

Both "Enable signature on all outgoing messages" toggles were left exactly as found (David's already on,
Charity's already off) -- neither was turned on by this run. No permission checkboxes were touched. Both
signatures were reopened after save and confirmed to persist exactly, hyperlink included.

**c) Merge field picker**, opened from a live workflow Send Email action's From Name field. Category is
labeled plain **"User"** (not "assigned user"). Exact tokens offered: Full Name, First Name, Last Name, Email,
Phone, Phone (raw format), **Signature**, **Calendar Link**, Twilio Phone, ID. Confirmed the underlying syntax
by inserting one: `{{user.email_signature}}` (immediately reverted, not saved). **From Name and From Email
both accept merge fields** (the picker works from both). **No separate Reply-To field exists on this Email
action type at all** in this account -- nothing to test merge-field support against there. Canceled the
action edit panel afterward; nothing saved.

## Assumptions (numbered)

1. Job 0: the "What is this call for?" dropdown's audit-specific option meant the field should be deleted from
   the Intro call booking form copy, per the brief's instruction; the original Audit booking form was never
   touched.
2. Job 0: no dedicated Atlas One lead-workflow folder exists, so the new WSA workflow was left in Home,
   matching where the only other Atlas One workflow already lives.
3. Job 0: only "UTM Source (First Attribution)" was added to the If/Else since GHL's Last Attribution group has
   no Source field at all.
4. Job 2: a folder was only removed entirely when every field in it was HIDE per the CSV; two mixed folders
   were reduced field-by-field instead and are called out explicitly above.
5. Job 2: Companies has no hide control in this account; stopped after one documented look rather than forcing
   a workaround.
6. Job 3: workflows 16 and 39 are large date-driven cadence trees; documented at the repeating-pattern level
   rather than transcribing every single date node, since the pattern was fully evident and consistent
   throughout.
7. Job 3e: tag ids for the 4 duplicate pairs were not individually captured (would need opening each row's Edit
   dialog); the exact spelling match and workflow-usage question were still answered from the visible list and
   from Job 3a's transcription.
8. Job 4/5: treated "Manage"/"Disconnect" buttons as the authoritative signal of an active connection over the
   stale "Get Started" banner text, since a Disconnect button only appears for something actually connected.
9. Job 6b: interpreted "Do NOT turn on any include-signature toggle" as leave-as-found in both directions (not
   as an instruction to turn an already-on toggle off), since turning David's off would itself be an
   unrequested change.

## Skipped / could not do

- Job 3e: exact tag ids for the two other duplicate-pair rows beyond what the list view shows (would need
  per-row Edit dialogs).
- Job 4: "Manage default stripe payment methods for your invoices" link on the Payment Settings page was seen
  but not opened.
- Job 4: Subscriptions, Payment Links, Orders, Coupons, Gift Cards tabs were noted by location only, not opened
  in detail (out of this job's explicit scope).
- Job 5: QuickBooks step 2 of the setup wizard ("Map your tax agencies") was visible but inactive/greyed out,
  not opened.
- Job 6c: only `{{user.email_signature}}` was directly inserted and confirmed; the other User tokens are read
  from the picker's visible labels only.

## Screenshot list

All screenshots are under `_briefs/assets/run-CL/shots/`. Grouped by job:

- Job 0: `job0a-*`, `job0b-*`, `job0c-*`, `job0d-*`, `job0e-*` (16 files)
- Job 1: `job1-*` (6 files)
- Job 2: `job2-*` (5 files)
- Job 3: `job3-wf-*` (workflow canvases), `job3-workflows-list.png`, `job3-forms-list.png`, `job3-add-*.png`,
  `job3-email-*.png`, `job3-insert-link.png`, `job3-trigger-link*.png`, `job3-channel-dropdown2.png` (24 files)
- Job 4: `job4-*` (17 files)
- Job 5: `job5-*` (5 files)
- Job 6: `job6-*` (18 files)

Plus `00-form-initial-state.png` and `01-form-field-removed.png` from earlier Job 0 exploration.

## Questions for David (batched)

1. **The "Free Assessment Form" survey** (Job 3b) is fully built (7 slides, Back-Office-Audit style) but not
   wired to any workflow and not embedded anywhere found. Keep it, finish wiring it, or retire it?
2. **Companies has no field-hide control** in this GHL account (Job 2). The 147 HubSpot-import Company fields
   from the CSV stay visible. Is that acceptable, or is there appetite to raise it with GoHighLevel support, or
   just live with it since Companies isn't actively used (see #4)?
3. **QuickBooks Invoice sync is already ON** (Job 5) -- every invoice created in GHL, including the 2 real
   Drafts already sitting there, will sync to QuickBooks. Is that the intended state, or should it be paused
   until the two draft invoices are reviewed?
4. **Contacts are not linked to Companies** anywhere in this account's UI (Job 3c) -- the 325 records under
   Contacts > Companies look like a leftover import, unrelated to the 2,155 live Contacts. Worth confirming
   whether Companies should be used at all going forward, or left dormant.
5. **Trigger Links are unused** (Job 3d) -- setting a few up (e.g. one per common form/booking link) would let
   staff pick a named link from a list instead of pasting the raw share URL every time. Worth building as a
   follow-up?
6. **Charity's email is not verified** (Job 6a) -- her replies would bounce until this is resolved, which
   blocks the "swap in the user signature merge field" plan for her templates (per the Cowork plan, item 5).
   Should this be prioritized before Run CM continues that work?
7. **David's old signature had a Zoom scheduler link and a second phone number** (Cell: 801-358-8547) not
   recorded anywhere else in this account. Now replaced per the brief's exact text -- confirm the Zoom link and
   that cell number are no longer needed anywhere, or if they should be added back into the new signature.
