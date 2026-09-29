# RUN CN part 2 report (2026-09-28)

Resume brief installed by Cowork with David's answers to part 1's questions. Order run this session: **Job G first**
(Dr. Gould drafts, urgent), then Job 6, Job 2, Job 4, Job 3, Job 5. Jobs 0, 1 and the Job 2 structure-mapping from
part 1 are already done and were not touched again.

## What got done this session (in order)

### Job G — Dr. Gould invoice, agreement and products (DRAFTS ONLY, nothing sent)

**G1. Products.** Checked Payments > Products (45 products) before creating anything:
- "Atlas One Membership: Professional" $399/mo recurring already existed (id `6aa2fd1f97fe7f62966dab64`) — reused.
- "Setup: Professional" $495 one time already existed (id `6aa2fd7d08d19fea4480d9b1`) — reused. This is the
  "Membership setup, Professional" product the brief named; the live product name differs slightly in wording but
  the price and terms match exactly.
- "Payroll to GL Converter: semi-monthly or bi-weekly payroll" $75/mo (id `6aaa11679f907ff444a40c13`) and
  "Payroll to GL Converter: setup" $250 (id `6aaa11b89f907ff444a4232e`) already existed — reused, no duplicate.
- "Bookkeeping with bill pay" $750/mo did **not** exist. Created it new (id `6abb3aa5d885033ef32372fb`), recurring
  monthly, description exactly as the brief specified: "Monthly bookkeeping with bill pay (accounts payable).
  Accounts receivable not included, priced separately."

**G2.** Old draft invoice INV-000002 (id `6ab802c4543c55f014bd6611`, contact Joel Gould id `3MBRxpll6eLI4bvtIdfh`)
retitled to "DO NOT SEND, replaced 2026-09-28" and Saved (never Sent). Confirmed by reopening fresh. Not deleted —
David deletes it himself per the brief.

**G3.** New recurring invoice template built (id `6abb3d6e863acd218fc72b38`):
- Lines: Atlas One Membership, Professional $399.00; Setup: Professional $495.00; a custom line item "Setup fee
  waived" at **-$495.00**.
- **Discount mechanics note:** GHL's native "Add Discount" button has no field to label the discount, so I used a
  third product line instead (name "Setup fee waived", price -495, "Save for later use" left unchecked so it did
  not get added to the product catalog). This satisfies the brief's "a discount line or GHL Add Discount" either/or
  instruction with the exact wording it asked for.
- Subtotal / Amount Due: **$399.00**.
- Terms replaced with the brief's exact text: "ACH bank payment preferred, no fee."
- Charge Processing Fees: left OFF.
- Recurring: Monthly, on Date, 1st, starting **2026-10-01**, End: **Never**.
- "Send Invoice ___ days in advance" was a required field with no default (blocked Save with a validation error).
  The brief didn't specify a lead time, so I set it to **0** (send same day) — logged as an Assumption below.
- Attached `Dr_Gould_Professional_Membership_Inclusions_2026-09-28.pdf` (had to upload it into GHL's Media Storage
  library first — invoice attachments pull from there, not a direct file picker).
- Clicked **only Save**, never Schedule or Activate. Confirmed by reopening the template fresh at its saved id: the
  Schedule button is still there unclicked, and every field (lines, discount line, terms, dates, attachment)
  persisted correctly.
- **Open item:** the contact record's business name is not "Joel D. Gould DDS, A Professional Corporation" in GHL —
  the invoice's "Billed to" block shows only "Joel Gould". I did not edit the contact record (out of scope for
  drafting an invoice/agreement). Flagged in Questions below.

**G4. Agreement — BLOCKED, documented in detail.** Built the document draft (Payments, Documents & Contracts, New
Document, id `6abb3dc687e9880fcba875e0`):
- Named exactly "Dr Gould Membership Agreement (ATTORNEY REVIEW PENDING)" per the brief.
- Primary Client recipient set to Joel Gould.
- **Could not add the agreement body text.** GHL's document builder only lets you add a Text/Image/Table/Product
  list/Page break block by **dragging** it from a palette onto the page — there is no click-to-insert. Every drag
  method available in this browser session failed to register with the app:
  1. The tool's native drag helper timed out ("pages-wrapper intercepts pointer events").
  2. A synthetic HTML5 `DragEvent` dispatch via JS was a no-op.
  3. A real `page.mouse` down/move/up sequence was a no-op.
  4. Playwright's high-level `frame.dragAndDrop(..., { force: true })` reported success but nothing appeared.
  I confirmed via `document.elementFromPoint()` that an invisible `pages-wrapper` element sits on top of the block
  palette at the exact coordinates of the visible "Text" label, even right after a hard page reload — this is not a
  timing issue, it blocks all pointer interaction with the palette consistently. This is the same "Claude Code's
  browser cannot drag" limitation the brief calls out for form-building (Job 2), just hitting it in a different GHL
  screen.
- Left the draft in a safe state: correct title, correct recipient, one blank page, **Saved, never Sent**.
- **What still needs to go in the body** (for David, or a future run with working drag support, to paste in): the
  Atlas One Membership Schedule text (source: `A1_Sales/A1 Agreements/2026-09-15 masters/Atlas_One_Membership_Schedule.docx`),
  filled in for the Professional tier ($399/mo, $495 setup **waived**), plus the itemized inclusions list from
  `Dr_Gould_Professional_Membership_Inclusions_2026-09-28.pdf` (attach the PDF instead of retyping it, if the
  document builder's per-page "Add PDF's" option is used instead of a Text block — that option didn't require
  dragging and was visible in the page's own context menu), signature fields for both parties, and today's date. No
  "attorney review pending" banner should appear in this client-facing body — only the internal draft title says
  that.

### Job 6 — finish Run CM's owner-identity work (PARTIAL)

Confirmed "Intake: Instant reply" (id `94b34c50-2ad7-4650-a42d-35a74365555b`) already has From Name
`{{user.name}}, Atlas One Solutions` set on its Email 1 action from a prior run — screenshot taken as the Job 2e
proof the brief asked for.

Opened "W2 Warm referral" (id `c5666735-0e74-4d95-a333-36bdf015d53b`) to do the same check, but it's a large
branching workflow (Cornerstone gate, Lead Lane conditions, a Suppressed? branch) and I ran out of session budget
before locating its Send Email actions among the branches.

**Everything else in Job 6 is not done this session.** The Run CM brief this job point back to
(`_to_delete/superseded-2026-09-27/briefs/BRIEF-GHL-runCM.md`) does not actually exist anywhere in the Master Kit —
I searched the whole tree and it isn't there (may have been swept up in a later cleanup). I reconstructed the exact
scope from the copy of that brief already saved in this repo (`_briefs/RUN-CM-terminal-GHL.md`, Job 2), which is
accurate and complete. Full remaining checklist for the next run:

**Templates still to paste from disk into Marketing > Emails > Templates** (already fixed on disk, only 4 of 35
pasted so far — audit-offer-day20, audit-offer-day28, e0, 45-a):
- From `_BUILD-LOG/cadence-emails-2026-09-13/`: 45-b, 45-c, intake-instant-reply, confirm-document-build,
  confirm-service-signup, new-client-welcome, send-bookkeeping-form, tool-lead-nurture-1, tool-lead-nurture-2.
- won-email-6 and won-email-7-checklist (I could not find these two files under either template source folder —
  they may be under a different name; check `_BUILD-LOG/email-templates-map.md` for the current filename).
- From `_BUILD-LOG/p-templates-2026-09-23/`: p-c-2-inbound-email-2, p-c-3-inbound-email-3,
  p-a-1/2/3-referral-email, p-b-1/2/3/4-trigger-email/close, p-b-120-renewal-heads-up, p-b-60-last-window,
  p-d-1/2/3/4-cold-email/breakup, p-e-0-gracious-close, p-e-4-month-four, p-e-q1/q2/q3-quarterly.

For each: open in Marketing > Emails > Templates, replace the source with the disk file, Cmd+End and check for a
stray ">" at the end (per `email-templates-map.md`), Save, Preview on a contact owned by David, screenshot the
signature.

**Workflows still needing From Name `{{user.name}}, Atlas One Solutions` / From Email `{{user.email}}` on every
Send Email action** (Call: not now and W2 already had this set in an earlier run; Instant Reply confirmed above):
Audit: offer follow up, Intake: Send bookkeeping form (+ edit its inline Email 2B text to use the merge fields),
Send PEO form on tag, Send bookkeeping form on tag, Intake: document build, Intake: service sign up (all 10
branches), Tool-Lead Nurture, W1 Inbound, W2 Warm referral (started, not finished), W3 Trigger sequence, W3a
Renewal calendar, W4 Cold cadence, W5 Lost deal, Won: Pay Referral Partner. Top-level Save after each, reopen fresh
to confirm.

**Notifications and tasks (Job 2d):** in every one of those workflows, Internal Notifications that go to a fixed
David address need the recipient switched to the contact's assigned user, with David kept as a second recipient;
task actions need "Assign to" set to the assigned user where that option exists.

**The "$70,000 audit (construction)" inline email fix** in Call: not now (replace the typed signature with merge
fields, screenshot before/after) — not started.

Booking workflows and W7 stay on David per the brief — no change needed there.

### Jobs 2, 4, 3, 5 — not started this session

Job G took most of this run given the drag-and-drop blocker investigation (documented above so the next run doesn't
have to rediscover it), and Job 6's real scope turned out to be far larger than what was left in the session budget
after that. Job 2 (finish Form D) picks up exactly where part 1 of this run left it: the duplicate form
"Atlas One — Business Insurance Quote Request" (id `LguXr1X9YMjD4WHrJt9D`) exists and is fully mapped in the part 1
report, but zero fields have been added or removed yet — David confirmed no review is needed, continue directly
from that structure map.

## Assumptions

1. Reused "Setup: Professional" as the brief's "Membership setup, Professional" product — same price/terms, name
   differs in wording only.
2. Set the new recurring invoice's "Send Invoice ___ days in advance" to 0 (send same day) since the brief did not
   specify a lead time and GHL required a value to save.
3. Named the "Setup fee waived" discount as a third invoice line item (not GHL's native Add Discount, which has no
   label field) so the exact wording the brief asked for actually appears on the invoice.
4. Left "Save for later use" unchecked on the "Setup fee waived" line item so it was not added as a permanent
   catalog product (it's specific to this one invoice).
5. Did not edit the Joel Gould contact record's business name field even though it doesn't match "Joel D. Gould
   DDS, A Professional Corporation" — out of scope for a drafts-only job, flagged as a question instead.
6. Treated the missing `BRIEF-GHL-runCM.md` source file as non-blocking since an accurate copy already existed in
   this repo (`_briefs/RUN-CM-terminal-GHL.md`) and used that as the source of truth for Job 6's scope.

## Questions for David

1. **Dr. Gould invoice/agreement:** the invoice's "Billed to" shows only "Joel Gould", not "Joel D. Gould DDS, A
   Professional Corporation" — do you want the contact record's business name field filled in so it shows on
   invoices and documents going forward?
2. **Dr. Gould agreement body:** GHL's document builder needs a real drag gesture to add a Text block to a page,
   which this browser session cannot perform (confirmed with several different techniques, detailed above under Job
   G4). Do you want to (a) paste the agreement text in yourself in the GHL UI (I can hand you the exact text), (b)
   have a different terminal/session try again with a tool that can do a true OS-level drag, or (c) attach the
   existing Membership Schedule PDF as a page instead of retyping it as native text (via that page's own "Add
   PDF's" option, which does not require dragging)?
3. **Send Invoice lead time:** I set the new recurring invoice to send 0 days in advance (same day) since the field
   was required and the brief didn't say. Keep that, or do you want a specific lead time (e.g. 3 or 5 days)?
4. **won-email-6 / won-email-7-checklist:** I could not find files by these exact names under either template
   source folder for Job 6 — have they been renamed? Check `email-templates-map.md` or point me to the right file
   names for the next run.
5. **Job 6 scope:** given how large the remaining checklist is (20+ more email templates to paste, ~12 more
   workflows needing From/Email + notification changes), do you want a dedicated GHL run focused only on finishing
   Job 6 before Jobs 2/4/3/5 continue, or should the next run pick up Job 2 (Form D) first since it's mid-build and
   smaller in scope?
