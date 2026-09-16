# RUN-GHL-report.md (Run BD, 2026-09-16)

Scope this run: Part 20 (Joel Gould contact, read only), Part 18 (internal "new intake" notice), Part 19
(Hold Harmless template re-upload). Parts 1-17 were completed in prior runs and are not repeated here.

## Part 20: Joel Gould contact (read only, nothing changed)

Contact `3MBRxpll6eLI4bvtIdfh`, drjoeldgould@gmail.com, (310) 722-0705.

**Tags (3):** form-a-sent, reply received, intake-received.

**Opportunity:** "Gould dental practice, PEO, insurance, books\"" in pipeline "PEO & Benefits", stage
Inquiry, $0.00.

**CALL NOW task:** exists. Title "CALL NOW: (310) 722-0705", description "Services requested:" (the value
after the colon is blank -- same pattern as the internal email bug this run fixes), due today 11:19 AM
(MDT), not yet completed.

**Activity / uploads:** Activity shows only "Form submitted" and "Page visited" for the "Atlas One -- PEO /
Prospect Quote Request" form. The three custom fields that would hold uploads (File Upload 1tge, Census &
Benefits Documents, Upload current WC policy / dec page) are all empty ("Click to upload" placeholder). **No
census, payroll report, or WC policy file actually exists on this contact** -- the checklist item in the
internal notice email assumes uploads happen, but on this real lead none were attached.

**Custom fields with a value** (folder / field label / merge key / value):
- General Info / State / `{{contact.state}}` / CA
- Form | Form 1 / Legal Business Name / `{{contact.legal_business_name}}` / "Dr Joel D Gould DDS a professional corp"
- Form | Form 1 / DBA / Trade Name / `{{contact.dba_trade_name}}` / "Premier Dental"
- Form | Form 1 / Entity Type / (picker) / S-Corp
- Form | Form 1 / FEIN / EIN / `{{contact.fein_ein}}` / 020593720
- Form | Form 1 / Estimated Annual Gross Revenue ($) / `{{contact.estimated_annual_gross_revenue}}` / 2.4M
- Form | Form 1 / Estimated Annual Gross Payroll ($) / `{{contact.estimated_annual_gross_payroll}}` / 800k
- Form | Form 1 / # Full-time W-2 Employees / `{{contact.full_time_w_2_employees}}` / 10
- Form | Form 1 / # Part-time W-2 Employees / `{{contact.part_time_w_2_employees}}` / 3
- Form | Form 1 / # 1099 Contractors / `{{contact.1099_contractors}}` / -- (empty)
- Form | Form 1 / Pay Period Frequency / (picker) / Semi-Monthly
- Form | Form 1 / On a PEO currently? / (picker) / No
- Form | Form 1 / Do you currently have Workers' Comp coverage? / (picker) / No
- Form | Form 1 / Review or quote employee benefits? / (picker) / Yes
- Form | Form 1 / Review or quote other business insurance? / (picker) / Yes
- Form | Form 1 / Which other policies would you like reviewed or quoted? / (multi-select) / General
  Liability, Cyber, Property / Inland Marine / Tools & Equipment, Umbrella
- Form | Form 1 / Which core services would you like included in your quote? / (multi-select) / PEO
  Payroll, ASO Payroll, HCM Self-Service (Basic), HR Support, Benefits Administration, Retirement 401(k)
  PEP Master
- Prospecting / Lead Lane / (picker) / C Inbound
- Prospecting / Vertical / `{{contact.vertical}}` / "Dental Ortho Optometry ENT"
- Prospecting / Vertical Opener / `{{contact.vertical_opener}}` / (a hygiene-chair-cost paragraph, dental
  specific)
- Prospecting / Vertical Tool / `{{contact.vertical_tool}}` / "Retention Cost calculator:
  https://forms.atlasonesolutions.com/tools/retention-cost/"
- Prospecting / Vertical Proof / `{{contact.vertical_proof}}` / (a three-doctor-practice case study
  paragraph)
- Prospecting / Last Touch Date / Sep 16, 2026
- Contact / Contact source / `{{contact.source}}` / "Referal from Modern American Dentistry (Current Client
  G&A)" (typo "Referal" is the data as entered, not something this run touched)

**Merge keys found for Part 18** (Settings > Custom Fields, confirmed by search):
- State: `{{contact.state}}` (General Info)
- W-2 counts: `{{contact.full_time_w_2_employees}}` and `{{contact.part_time_w_2_employees}}` (Form | Form 1)
- 1099 count: `{{contact.1099_contractors}}` (Form | Form 1)
- Services requested picker: `{{contact.which_service}}` (Form | Atlas One -- Service Sign Up)
- Vertical: `{{contact.vertical}}` (Prospecting)
- Source: `{{contact.source}}` (Contact) -- confirmed matches the file's assumption
- Legal business name: `{{contact.legal_business_name}}` (Form | Form 1) -- confirmed matches

## Part 18: internal "new intake" notice

**(a) File.** Wrote `_BUILD-LOG/cadence-emails-2026-09-13/internal-new-intake.html`, same wrapper as
`internal-new-booking.html` (same head, table, logo width 120, grey footer line). Subject: `New intake:
{{contact.first_name}} {{contact.last_name}} ({{contact.legal_business_name}})`. Body: 17px bold heading,
soft blue (#DBE4ED) info box with Company / Phone / Email / State / Employees (full-time W-2, part-time
W-2, 1099, one line, plain words) / Services requested / Vertical / Source, a periwinkle (#788DE3) button
"Open the contact" linking to
`https://app.ridethehightide.com/v2/location/AzTPxnK2vSUj19jYoDmR/contacts/detail/{{contact.id}}`, a bold
"What to do next" line and the six-item numbered list from the brief. Confirmed the file contains no
"380-225-5217" and no "385" (internal mail carries no signature) and no dashes. Added a row to `INDEX.md`
and to `email-templates-map.md`.

**(b) "Intake: Instant reply" workflow** (`94b34c50-2ad7-4650-a42d-35a74365555b`). Found the "Internal
Notification" Send Email action and confirmed the bug the brief described: body was literally "New intake
from {{contact.first_name}} {{contact.last_name}}, {{contact.company_name}}. Open: {{contact.url}}" --
`{{contact.company_name}}` and `{{contact.url}}` are not real merge tags in this account, so the delivered
mail always showed the company and link blank, exactly as David reported. Replaced the subject with the
file's subject and the body verbatim through the source code dialog (Quick Compose). To/From left
unchanged (David@AtlasOneSolutions.com both directions). Saved, confirmed the top-level Save button flipped
Save -> Saved, reloaded by leaving and reopening the workflow from the list, reopened the node and confirmed
subject, body, and the button's href (with `{{contact.id}}`) all persisted. Publish state untouched (stayed
Published).

**(c) "Intake: service sign up" and "Intake: document build".** Opened both and used Fit to Screen to see
every node. Neither workflow has an internal notification node at all: "Intake: service sign up" is ten
parallel branches (Tag -> Task -> Email) each ending in the prospect-facing confirmation email only;
"Intake: document build" is Add Tag -> Task -> Email (confirmation) -> Wait 1 day -> Task -> END. There is
nothing to fix in either -- skipped both, per the brief's own "skip a workflow whose notice already shows
the answers" clause (these simply have no notice node to begin with).

**(d) Real test.** Submitted Form A
(https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc) as a new contact: first/last name "Run
BD" / "Test Co", email david+zzbd@atlasonesolutions.com, phone +1 (702) 555-0199 (the 555-area-code form
`+15550192026` was rejected as an invalid phone number by the form's validator; the real fictional-exchange
format `(702) 555-0199` was accepted), Legal Business Name "Run BD Test Co", Entity Type LLC, one core
service picked (ASO Payroll, which is what revealed the W-2/1099 employee-count fields: 5 full-time, 2
part-time, 1 contractor), Workers' Comp coverage "No", one upload (a placeholder PDF), and checked
"Workers' compensation" in the "quote or explore" list. **Form A has no State field anywhere on it, even
after every conditional section is opened** -- Joel Gould's State=CA must have come from somewhere other
than this form (his contact record shows "Created by: Manual addition by David Taylor", so it was likely
typed in by hand), not from a form field. This is a pre-existing gap, not something this run's changes
caused, and nothing to fix under this brief.

Confirmed via the workflow's Execution logs that "Internal Notification" ran and its status was **Success**
for the test contact. GHL's execution-log detail panel does not expose the rendered subject/body text, and
because the send goes to the static David@AtlasOneSolutions.com address rather than to the test contact,
it does not show up in that contact's own Conversations thread either (only the contact-facing "Email 1 -
Instant reply" confirmation appears there, and it is clean: correct company/service copy, no dashes).
Merge-field resolution was confirmed the reliable way available in this UI: reopening the saved node
renders the full HTML preview with every tag present and none blank, matching the same rendering pattern
that already resolves correctly for `{{contact.legal_business_name}}` etc. on Joel Gould's real, populated
contact. **Recommend David glance at his own inbox once** to see the actual delivered copy with a real
lead's data filled in.

Deleted the test contact (typed `DELETE` to confirm); GHL's own confirmation dialog states this also
removes the contact's task/opportunity/conversation, with a 60-day restore window. No opportunity had been
auto-created for this test contact (confirmed via its Opportunities tab), so there was nothing else to
clean up.

## Part 19: Hold Harmless template re-upload

Confirmed the updated PDF exists at the real masters folder (`2. Atlas 1 Solutions Marketing/A1_Sales/A1
Agreements/2026-09-15 masters/Atlas_One_Hold_Harmless_and_Acknowledgement.pdf`), modified 1:51 PM today
(matches "GHL-JOBS Run BB, 1:51 PM"), and visually confirmed clause 5, "California, release and waiver of
unknown claims (Civil Code 1542)", is present on the page.

Built the template again exactly as in Part 16: Payments > Documents & Contracts > Templates > New > Upload
existing PDF's, title auto-matched the filename exactly
(`Atlas_One_Hold_Harmless_and_Acknowledgement`). Added the same four fields as the other 10 templates, using
the FILLABLE FIELDS drag panel (this required raw mouse down/move/up since the document preview is not a
normal DOM tree and Playwright's built-in drag-and-drop locator API does not reach it):
- Signature field assigned to **David Taylor (You)**, placed over the Atlas One column
- Signature field assigned to **Contact**, placed over the Client column
- Text Field, placeholder "Printed Name (Client)", assigned to Contact
- Date field, placeholder "Date Signed", assigned to Contact

Saved -- "Template saved successfully" toast confirmed. Screenshot of the new signature page saved to
`_briefs/assets/run-BD/shots/hold-harmless-new-signature-page.png`.

**Deleting the old (9:16 PM) template was blocked by the permission classifier** ("Irreversible Deletion")
on the row's actions menu, on two separate attempts with different element descriptions. Followed the
brief's own fallback: opened the old template and renamed it, via its own title field, to "OLD do not use
Atlas_One_Hold_Harmless_and_Acknowledgement", then saved (confirmed by the same "Template saved
successfully" toast). The template list now shows the new one first (Sep 16, 2:33 PM) and the old one
clearly marked and dated (Sep 15, 9:16 PM), so no one will paste the stale PDF's signature page by mistake.
Screenshot of the final list saved to `_briefs/assets/run-BD/shots/templates-list-after-part19.png`.

The other 10 templates from Run BC (Master_Client_Services_Agreement, AI_Services, Bookkeeping,
Certified_Payroll, COI_Tracking, Document_Services, Membership, Payroll_to_GL_Converter,
Software_and_Licenses, WC_Audit_Recovery) were left completely alone, per the brief -- their content did
not change in the Run BB regeneration. Noted `Sample_Proposal_Software_and_Licenses.pdf` (and its sibling
Sample_Proposal_*.pdf/.docx files for every service) now exist in the masters folder; nothing to build from
them this run, per the brief.

## Assumptions

1. **Employees line wording** ("Part 18a"). The brief said "use whatever Form A collects; one line, plain
   words" -- Form 1 collects three separate counts (full-time W-2, part-time W-2, 1099), so the line reads
   "{{contact.full_time_w_2_employees}} full time W-2, {{contact.part_time_w_2_employees}} part time W-2,
   {{contact.1099_contractors}} 1099" rather than a single combined W-2 figure.
2. **Part 18c "skip" wording.** The brief's skip condition ("skip a workflow whose notice already shows the
   answers and a working link") assumes every intake workflow has a notice node to evaluate. Neither
   "Intake: service sign up" nor "Intake: document build" has one at all, so there was nothing to switch or
   skip in the sense of choosing between "bare" and "already correct" -- I'm treating "no node exists" as
   equally out of scope this run and saying so here rather than silently doing nothing.
3. **Test phone number.** `+15550192026` (555 as the area code) was rejected by Form A's phone validator as
   invalid; used the standard fictional-exchange format `(702) 555-0199` instead, which was accepted.
4. **State field gap.** Form A/Form 1 has no State input anywhere in its visible or conditionally-revealed
   fields. This means every future Form A submission's internal notice will show a blank
   `{{contact.state}}` unless State gets added to the form, or set by hand as it apparently was for Joel
   Gould. Not fixed this run since it is out of the Part 18 scope (the brief only asked to wire the merge
   tag, not to audit the form for missing fields), but flagged below.
5. **Old template rename vs. delete.** Followed the brief's explicit fallback instruction when the delete
   was blocked by the permission classifier; did not attempt to bypass the classifier by other means.

## Skipped

- Part 18c: no internal notice node exists in "Intake: service sign up" or "Intake: document build" to
  switch (see Assumption 2).
- Deleting the old Hold Harmless template: blocked by the permission classifier; renamed instead per the
  brief's own fallback (see Part 19).

## Questions for David

1. **Form A has no State field.** Every future PEO/Prospect Quote submission's internal notice will show a
   blank State unless a State field gets added to Form A (or Form 1's custom-field set), or GHL-JOBS wires
   one in from the browser's IP-geolocation field (`{{contact.ip_state_code}}` exists as a separate field
   already, populated automatically, and could be a decent fallback). Want that added, and if so, to Form A
   directly or as a fallback merge tag in the email?
2. **No census/payroll/WC-policy uploads on Joel Gould's real contact.** The internal notice's checklist
   item 2 tells whoever calls him to "download the uploads: census, payroll report, WC policy" but none
   exist on his contact. Is that because he was told to bring them to the call instead, or should the
   checklist line be softened to "if uploaded" language so it doesn't send someone hunting for files that
   were never attached?
3. Please glance at your own inbox for the "New intake: Run BD Test Co (Run BD Test Co)" email that went
   out today around 2:21 PM MDT and confirm it actually rendered with every field filled in as expected
   (company, phone, email, employees, services, vertical, source, and the "Open the contact" button) --
   GHL's UI does not let this terminal see the delivered copy directly since it was addressed to your own
   mailbox, not to the test contact.
