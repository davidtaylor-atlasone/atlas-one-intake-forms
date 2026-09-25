# BRIEF-GHL-JOBS (current run: Run CI, 2026-09-23). Charity's kit: tools inside it, the guard that missed them, the Cornerstone toggle, the licensed agent line.

Terminal name: GHL-JOBS. Model: Sonnet 5. Files and code only, never the GoHighLevel browser UI. No questions
mid run. No sends, no deploy beyond pushing the intake forms repo, no spending. Deleting is a move into
`Master_Kit/_to_delete/superseded-2026-09-23/` (the OneDrive root _to_delete was emptied by David). No dashes
in anything a client or prospect reads. Log to `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`, finish with
`_BUILD-LOG/RUN-GHL-JOBS-report.md`. No time limit; commit after each job. Screenshots to
`_briefs/assets/run-CI-jobs/`. Name this run "GHL-JOBS Run CI" everywhere (the GHL terminal also used CH).

Run CH was audited by Cowork on disk (COWORK-AUDIT-run-CH-2026-09-23.md). The 41 swapped files are clean,
including PDF text. Two things are not, and the guard reported clean because it does not decode the base64
blobs inside the Sales Kit file.

## Job 1: the guard must read inside the Sales Kit file

`scan_default_person_leak()` reads each HTML file as text. The rep Sales Kit stores every tool as a base64
blob, so the guard never sees inside them. Decode every blob (`<script ... id="tN">` base64 content) and scan
the decoded text too. Cowork's decode of Charity's current kit finds "David Taylor" 35 times, all inside
inlined tools: t0 Business Tools (org chart sample "President: David Taylor"), t19 booking confirmation ("Your
call with David Taylor is confirmed"), t24 Employee Benefits Options ("David Taylor, Licensed Broker"), t29
census public footer, t30 Savings Summary footer, t33 IC Onboarding Packet (10), t37 Benefits Package and
Enrollment Guide, t38 Free HR Templates footer, t48 New Employee Onboarding Packet (15).

## Job 2: tools carry the company line, not a person (rule for every build)

A tool is used by whoever opens it, so its contact line is the company line only:
"Atlas One Solutions · support@atlasonesolutions.com · 380-CALL-A1S (380-225-5217) · AtlasOneSolutions.com".
In the MASTER tools, remove "David Taylor" (and "President & Founder") from every tool footer and contact
line, in both the visible HTML and any jsPDF or print strings. Sample data becomes a neutral name: the org
chart sample reads "President: Name". The booking confirmation page reads "Your call is confirmed" with no
name. Two exceptions stay person based and go through the swap instead:
- The census public footer (`public=True`, David's decision): swap to the rep's public line in a rep kit.
- The licensed agent line, Job 3.
Rebuild COMMAND and the shared Sales Kit after the master edits.

## Job 3: the licensed agent line on insurance pieces

David is the licensed insurance agent. Until he confirms Charity holds a producer license, a rep's copy of any
piece that sells insurance keeps David named as the licensed agent while the rep is the contact. Add one line,
class `a1-licensed-agent`, that the swap never touches: "Insurance products are offered through David Taylor,
licensed agent." Put it on: Employee Benefits Menu, Employee Benefits Options (replacing "David Taylor,
Licensed Broker" as the header byline, which becomes the person line and swaps), the Benefits and Retirement
division sheet and the Risk and Insurance division sheet. The guard allowlists exactly this sentence and
nothing else. Make it one setting per person in people.json, `"licensed_insurance": false` for Charity, so the
day she is licensed the line drops out of her kit on the next build.

## Job 4: no Cornerstone in a rep kit (Run CH question 2)

A non default person's copy of the Employee Benefits Menu drops the Cornerstone PEO toggle and the whole
`CONFIG.cs` block. Remove the "Cornerstone PEO" allowlist entry Run CH added to the guard. Then add to the
guard: any rep kit file (decoded) containing "cornerstone" fails the build.

## Run CH questions 1 and 3, answered
- Charity's booking link: stays null until her calendar exists; empty is correct. No work.
- A rep's own title on the Client Portal point of contact block: yes, every rep, from people.json.

## Job 5: rebuild Charity and prove it

`--person charity`. Then report per file, decoding every blob in the Sales Kit file and reading every PDF's
text: david@, "David Taylor" outside the one licensed agent sentence, Cornerstone, 385-213-7177, dashes. All
zero. Headless at 1440 and 390 on her Sales Kit and COMMAND, zero console errors. Deploy nothing.

## Not in this run
LTD row (waiting on David's broker). Charity's GoHighLevel signatures and calendar (GHL terminal). Her mailbox.
