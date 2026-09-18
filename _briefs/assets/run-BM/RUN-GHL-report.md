# RUN-GHL-report.md (Run BM, 2026-09-18)

David still needs to publish: Post-Presentation Email, Intake: onboarding documents, Reply task closed.

Run BM covered Part 34 (publish state check, read only) and Part 35 (Referral Partner dropdown sync). Part 0
cleared with the ghl-browser MCP: root, one click into Automation, Workflows list loaded fine, no dead click.

## Part 34: publish state, read only

Fresh navigation to Automation > Workflows (listTab=all), status column read for each of the seven named
workflows. Nothing clicked or changed.

| Workflow | Status |
|---|---|
| Post-Presentation Email | Draft |
| Intake: onboarding documents | Draft |
| Reply task closed | Draft |
| Intake: Instant reply | Published |
| W1 Inbound speed to lead (duplicate instant reply removed 2026-09-16) | Published |
| Tool-Lead Nurture | Published |
| Call: not now | Published |

Screenshot: `_briefs/assets/run-BM/part34-workflows-list.png`.

All three of the first-listed workflows (Post-Presentation Email, Intake: onboarding documents, Reply task
closed) are still Draft, unchanged from the prior session's read (RUN-BJ's status-only note). Nothing else in
this run touched any Publish/Draft switch.

## Part 35: Referral Partner dropdown sync

Settings > Custom Fields > searched "Referral Partner". Two fields matched:

- **Referral Partner** — Dropdown (single), folder "Opportunity Details", key `opportunity.referral_partner`.
  This is the dropdown the brief means.
- **Referral Partner Name** — Single line, folder "Prospecting" (Contact object), key
  `contact.referral_partner_name`. A free-text field, not a dropdown, holds no options. Left alone; not in scope.

So there is one field, opportunity-side only; no separate contact-side dropdown exists under this exact name.

**Options before** (10, in order): None / Direct, Website or Tool, Hoffman and Company (Kris), Apex Tax
Services (Kayden), Other, Ramp, Jotform, Deel, QuickBooks, Big Red Jelly.

Cross-checking against the brief's add list: Ramp, Jotform, Deel, QuickBooks and Big Red Jelly were already
present with exactly the spelling requested, so nothing was added for those (would have been duplicates).
"Hoffman and Company" and "Apex Tax Services" already existed, but only as "Hoffman and Company (Kris)" and
"Apex Tax Services (Kayden)" (the rep's name appended); the brief bars renaming or removing an existing option
(would strand contacts on the old value), so those exact-spelling labels needed as new options were added
separately rather than editing the existing ones. "PeoplePay Global" did not exist yet.

**Added** (3): PeoplePay Global, Hoffman and Company, Apex Tax Services.

**Options after** (13, in order): None / Direct, Website or Tool, Hoffman and Company (Kris), Apex Tax Services
(Kayden), Other, Ramp, Jotform, Deel, QuickBooks, Big Red Jelly, PeoplePay Global, Hoffman and Company, Apex
Tax Services.

Saved via the field's "Update field" button. Verified by fresh navigation (root, Settings, Custom Fields,
searched again, reopened the field) and reading every option back in order; all 13 confirmed, none renamed or
removed. Screenshot: `_briefs/assets/run-BM/part35-referral-partner-options-after.png`.

## Assumptions

1. "Referral Partner" in the brief means the Dropdown (single) field on the Opportunity object
   (`opportunity.referral_partner`); the similarly named "Referral Partner Name" single-line contact field is a
   different, unrelated field and was left untouched.
2. Where a requested option's exact text already existed as a differently-labeled option (rep name in
   parentheses), the rule "never rename or remove an existing option" was read literally: the existing labeled
   option stays exactly as-is, and the new exact-spelling label is added as a separate option rather than
   merged into or replacing the old one. This does create two entries that both effectively mean the same
   referral partner (e.g. "Hoffman and Company (Kris)" and "Hoffman and Company"); flagged below for David.
3. Options already present with exact matching spelling (Ramp, Jotform, Deel, QuickBooks, Big Red Jelly) were
   not re-added, since the brief's intent is to add missing options, not create duplicates.

## Skipped

Nothing skipped this run; both parts completed as scoped.

## Questions for David

1. Post-Presentation Email, Intake: onboarding documents and Reply task closed are all still Draft. These need
   you to publish them when ready; no run has touched their switches.
2. The Referral Partner dropdown now carries both "Hoffman and Company (Kris)" and a new plain "Hoffman and
   Company", and likewise both "Apex Tax Services (Kayden)" and a new plain "Apex Tax Services". If the
   parenthetical-rep-name versions are the ones actually in use on contacts/opportunities, you may want to
   decide whether to standardize going forward (a future run can migrate values from one label to the other,
   but per the no-rename rule this run left both in place rather than guessing).
