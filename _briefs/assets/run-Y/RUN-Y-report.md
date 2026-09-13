# RUN Y report (terminal B, files only)

Built 2026-09-12 by Claude Code, unattended, no GHL UI, no questions asked. Job: publish the Time and Cost Savings Discovery calculator as a hosted tool. Build notes and renders in `repo:_briefs/assets/run-Y/`. Nothing sent (the webhook was exercised only with the request intercepted and aborted locally), nothing deployed beyond the normal Pages push, nothing deleted. The Master Kit source file was not changed.

Paths: `repo:` is atlas-one-intake-forms (main, pushed, commit `aea64a1`); the source is `HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Time_Savings_Discovery.html` (the copy after Run W's dash pass).

## What was built

- `repo:tools/time-savings/index.html` (411 KB, fonts embedded), live at **https://forms.atlasonesolutions.com/tools/time-savings/** (curl 200; the served file is byte-identical to the pushed one).
- Same shell as the other hosted tools: the navy `.hbar` with the white logo and the eyebrow "Time and Cost Savings Discovery" replaces the tool's own A1 mark row; the Print / Save as PDF button stays; the `.cta-band` ("Turn the estimate into a plan", Book the 30 minute Back Office Audit, `book-david`) and the `.afoot` footer are the self-assessment's, same CSS.
- No CDN: the Google Fonts `<link>` is gone; DM Sans 400 and 700 are embedded as base64 exactly as in `tools/self-assessment/index.html` (Horas was already embedded). Loading the live page makes exactly one request (the page itself); the only outbound URLs in the file are the booking link and the webhook.
- Same webhook posting: a "Keep a copy of these results" card (name, company, email, phone; email or phone required) posts to the GHL inbound webhook `services.leadconnectorhq.com/hooks/AzTPxnK2vSUj19jYoDmR/webhook-trigger/d96dfd5e-...` with the same field names as the other hosted tools (`first_name`, `last_name`, `phone`, `email`, `company`, `atlas_tool` = "Time and Cost Savings Discovery", `atlas_headline`, `atlas_results_text`, `atlas_source_url`, `atlas_generated_at`) plus `hours_saved_year`, `time_savings_year`, `software_savings_year`, `total_savings_year`, `pay_runs_year`, `hourly_value`. `atlas_results_text` lists every task with hours and the annual total, and every subscription with its monthly cost. `mode:"no-cors"`, like the others. Verified locally by intercepting the POST (aborted, never delivered): the payload keys and text read back as expected; the "Saved" confirmation shows and the button disables.
- `repo:tools/index.html`: fifth card, "Time and Cost Savings Discovery / What is your back office costing you by hand? / List the tasks you still do manually and the software you could drop, and see the hours and dollars that come back every year." Lede now says "Five quick tools". Live at `/tools/` (200, identical to the pushed file).
- Mobile: the two tables were five and three cramped columns at 390 px (task names clipped to "Process & er"); under 560 px they now stack, task name on its own line, then hours / frequency / hours per year / remove with small labels. scrollWidth is 390 at 390 px and 1440 at 1440 px, no JavaScript errors at either width, local and live.
- Sample: rate 40, first task 2 hours per pay run (26 runs), first subscription $120 a month gives 264 hours, $10,560 time savings, $1,440 software savings, $12,000 total, checked by hand against the defaults. Defaults, task list and the calculation are unchanged from the kit file.
- Looked at: `repo:_briefs/assets/run-Y/time-savings_390_live.png`, `time-savings_1440_live.png`, `tools-index_1440_live.png` (and the local renders before the push).

## Assumptions

1. Audience: the kit file is written for David to fill in during a meeting ("Fill this in with the prospect", "their time", "their business", "the number you drop into the proposal"). The hosted page is the one the cadence emails will link to, so those six phrases speak to the owner on the hosted copy only: headline "What are you still doing by hand?", "Fill this in for your business", "your time", "your business", "you could drop", and the "How to use it" note ("the number to bring to the call"). Nothing else in the copy changed; the kit file still reads for the meeting.
2. The card copy on the tools index is new (the kit file has no card text).
3. The stacked mobile table is an additive media query in the hosted copy only; the kit file was not touched (it has the same cramped 390 px table, question 2).
4. Print: the header bar, CTA band, capture card and footer are hidden in print, the way the other hosted tools hide theirs.

## Not done

- Nothing skipped. The Portal was not rebuilt (no kit file changed in this run; Run W rebuilt it at 9:01 PM).

## Questions for David

1. The hosted copy now addresses the owner (assumption 1). If you would rather the public page keep the meeting voice, it is a six-line revert.
2. Want the kit copy of the Time Savings tool to get the same stacked mobile table (and the prospect voice), so the Portal version matches the hosted one?
3. On `/tools/` the logo in the header is white on the off-white page (pre-existing, visible in `tools-index_1440_live.png`); the hosted tools put it on a navy bar. Want the index to get the same navy `.hbar`?
4. The webhook was not fired for real. If you want a test contact in the CRM to confirm the fields map, say so and it can be sent with a plus-addressed email and deleted afterwards.
