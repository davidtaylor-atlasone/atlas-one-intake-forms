# Run BN report (2026-09-18)

Terminal: GHL. Scope: Part 36 only, removing the two duplicate Referral Partner options that Run BM added by
mistake. Prior report backed up to `_to_delete/superseded-2026-09-17/prior-reports/RUN-GHL-report-RunBM.md`
before this run started (per brief instruction, overwrite was fine since it already existed).

## Part 36: remove the two duplicate Referral Partner options

### Built
Opened Settings, Custom Fields, searched Referral Partner, opened the Dropdown (single) field in Opportunity
Details (key `opportunity.referral_partner`). Options before this run (13 total, in order):
None / Direct, Website or Tool, Hoffman and Company (Kris), Apex Tax Services (Kayden), Other, Ramp, Jotform,
Deel, QuickBooks, Big Red Jelly, PeoplePay Global, Hoffman and Company, Apex Tax Services.

Removed exactly two options using each row's Action delete control: "Hoffman and Company" (the one without
"(Kris)") and "Apex Tax Services" (the one without "(Kayden)"). Kept "Hoffman and Company (Kris)", "Apex Tax
Services (Kayden)" and "PeoplePay Global" untouched. Nothing else touched. No "in use" warning appeared on
either delete, so both went through in the editor without stopping. Saved with the Update field button.

### Verification
Fresh navigation: closed back to app.ridethehightide.com/, clicked Settings, then Custom Fields, searched
Referral Partner again, reopened the field. Read all options back and counted 11, in this exact order:
1. None / Direct
2. Website or Tool
3. Hoffman and Company (Kris)
4. Apex Tax Services (Kayden)
5. Other
6. Ramp
7. Jotform
8. Deel
9. QuickBooks
10. Big Red Jelly
11. PeoplePay Global

This matches the brief's expected order exactly. Screenshot saved to
`_briefs/assets/run-BN/part36-options-after.png` and looked at; it matches the read back list. Dialog was
closed with Cancel afterward, no further edits made.

## Assumptions
1. The two removed options were minutes old (added by Run BM in the same day) and nothing had been assigned to
   them yet, so removing them stranded no record, consistent with the brief's own note.
2. "Update field" (rather than any autosave) is the save action for this dropdown; the change persisted across
   a full fresh navigation and reopen, so this is confirmed correct.

## Skipped
Nothing skipped. Part 36 was the only scope for this run and it completed in full.

## Questions for David
None.
