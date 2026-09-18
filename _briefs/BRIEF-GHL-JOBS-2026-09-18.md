# BRIEF for the GHL-JOBS terminal: Run BO (Back Office Audit: fields, three audit emails as templates, the audit intake landing page)

Terminal name: GHL-JOBS. Files, code and the GHL API only (no browser clicks in GHL). Build end to end, no
questions, answer permission prompts yourself, log assumptions, questions at the END. Never fork or
background (rule 44). Do only the jobs written here. Commit and push. Repo assets in
`_briefs/assets/run-BO-jobs/`. No dashes in copy. Log to `TERMINAL-GHL-JOBS-live.md`; report to
`Master_Kit/_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted heredoc) plus a copy in the repo assets folder.
Prior report already backed up. Token: `GHL_PIT` in `.env`, never printed, never `~/.claude.json`.
Location `AzTPxnK2vSUj19jYoDmR`, `Version: 2021-07-28`, browser User-Agent. Reuse `tools/ghl_custom_fields.py`
and `tools/ghl_email_builder.py`. Source design: `_BUILD-LOG/back-office-audit-run-design-2026-09-18.md`.

## Job 1: audit contact fields
Read all contact fields first. Create in folder `AmY51esJO2QF0v3wvODu` only what is missing: `audit_code`
(TEXT, name "Audit Code"), `audit_offer_expires` (DATE, name "Audit Offer Expires"). For WC policy expiration
and benefits renewal date: search the existing fields (Form A captured both on 2026-09-04, likely under names
like "WC policy expiration" and "Benefits renewal"); if they exist, record their ids and keys, create nothing.
Save the JSON (no token) to the assets folder; list ids and keys in the report.

## Job 2: the audit intake landing page (stable link for the emails)
In `~/Projects/atlas-one-intake-forms` build `audit/index.html`, same shell as `start/index.html` (laptop mark,
four colours, DM Sans). Title "Back Office Audit: send your documents". Lede: "Four documents, five minutes.
Upload them here before our call and the Audit starts the moment we sit down." A list of the four
documents in plain words (bank or card statements for the last three months, or the QuickBooks Expenses by
Vendor report, or the Ramp vendor export; last payroll register or provider invoice; workers comp
declarations page; benefits renewal or current carrier invoice). Then a container `<div id="audit-form">`
holding, for now, one line "The upload form is being switched on. If you see this, email the documents to
David@atlasonesolutions.com and we will take it from there." and a constant at the top of the file's script
`const AUDIT_FORM_ID = ""`; when it is non empty the script writes the GHL form embed iframe
(`https://api.leadconnectorhq.com/widget/form/<id>` plus the standard form_embed.js) into that div and hides
the fallback line, and passes `?audit_code=` from the page URL through to the form URL. Footer with the 380
number. Verify 390 and 1440 headless, zero console errors. Commit and push. Live URL:
https://forms.atlasonesolutions.com/audit/ . The GHL terminal will report the form id; the next JOBS run fills
the constant.

## Job 3: three audit emails pushed as templates (Email Builder API, as Run BN)
a. `cadence-emails-2026-09-13/audit-prep.html` exists (AUDIT chat, 13:23). Replace the literal `FORM_D_URL`
   with `https://forms.atlasonesolutions.com/audit/?audit_code={{contact.audit_code}}` (confirm the merge key
   from Job 1; if the custom key differs, use the real one). Push as `A1 | Audit | prep`.
b. Write `audit-offer-day20.html`, template `A1 | Audit | offer-day20`, subject "Ten days left on your Audit
   offer, {{contact.first_name}}". Same wrapper and signature as `portal-doc-ready.html`. Body, no dashes:
   "Hi {{contact.first_name}}, your Back Office Audit offer is good through {{contact.audit_offer_expires}}.
   The numbers in it are yours: the Total Impact figure, the three fixes and the guarantee (two times your
   first year membership in documented savings or risk removed, or there is nothing to buy). If you want to
   walk through it once more before you decide, grab a time below. If the timing is wrong, reply and tell
   me, I will not chase." Button "Book 15 minutes" to the 15 minute intro link.
c. `audit-offer-day28.html`, template `A1 | Audit | offer-day28`, subject "Your Audit offer closes in two
   days". Body: "Hi {{contact.first_name}}, two days left on the offer dated in your Audit report. After
   {{contact.audit_offer_expires}} the pricing in it is no longer held. Nothing dramatic happens, I just
   cannot promise the same setup fee waiver later. Book a time or reply with a yes and I will send the
   agreement." Same button.
Push all three, fetch back, diff, before and after copies in the assets folder, rows in
`email-templates-map.md`. Send nothing. Report the three template ids.

## Report
Field ids and keys (including the existing WC and benefits date fields), the landing page URL and the
constant's name, three template ids, assumptions, "Questions for David" at the end.
