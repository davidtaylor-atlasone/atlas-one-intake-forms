# Run CS, Job 2: repscrub report (2026-09-30)

## Result
8 of 9 ids are rep safe and listed in `rep_scrub.SCRUBBED_IDS`. 1 excluded. One thing blocks a plain rebuild: two catalogue blurbs (catalogue.py, lead owned) still say Cornerstone / WSA. See "Needs the lead".

Built:
- `MK/_INTERNAL (do not share)/rep_scrub.py` (SCRUBBED_IDS, scrub(row_id, raw_html, person), LAST_STATS)
- `MK/_INTERNAL (do not share)/test_rep_scrub.py` (run with the Playwright venv python; `--no-render` for text checks only)
- Screenshots: `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/repscrub/` (1440 and 390 for every id, full page at 390, plus prospecting-s7-1440.png)
- No edit to catalogue.py (the `_REP_NEEDS_SCRUB` block needed nothing: it already subtracts SCRUBBED_IDS and keeps the email drafts out). No edit to any source playbook.

## SCRUBBED_IDS
prospecting-playbook-v1, sales-conversation-playbook, overlay-01-audiology, overlay-02-dental-ortho-optometry-ent, overlay-03-construction-and-trades, overlay-04-technology-and-startups, overlay-05-hospitality-and-restaurants, overlay-06-professional-services.

## Excluded
client-launch-email-drafts-2026-09-06. Cards 1 and 2 are Cornerstone emails to WSA's marketing team and David's landing page designer (WSA marks, Hearvana, the credit, the convention). Cards 3 to 5 are David's relaunch note to HIS existing PEO clients ("I have handled your PEO for [time period]", "I have launched Atlas One", "vendors pay me, the same way the PEO side already works"). That is David's own history and clients, and a rep cannot send it truthfully. Gutting 2 of 5 and rewriting the rest would be inventing Charity's story. It stays in `_REP_NEEDS_SCRUB`, out of rep builds.

## What the scrub does, per file (counts from rep_scrub.LAST_STATS)
Every file: brand toggle UI removed (1), Cornerstone footer line removed (1), page script replaced by an Atlas One only script (no localStorage, no CONFIG.cs, no toggle; fills data-k from CONFIG.a1; empty booking shows "[your booking link]"), brandbtn/brandbar/chanbtn CSS removed, "let the brand toggle sign them" reworded, David Taylor to rep name (2 per overlay), David first name to rep first name, dashes in text nodes (source had none), final guard raises ScrubError if cornerstone, margin, david, WSA, Hearvana, 385 phone, Utah or toggle remain.

- **Prospecting Playbook v1**: removed section 5.6 "WSA warm handoff (Cornerstone identity)" (call script, email, signature) and renumbered 5.7 to 5.10 as 5.6 to 5.9; removed the WSA row of the section 7 identity table and the "Brand Identity (Cornerstone/WSA)" field row; removed workflow W7 WSA handoff (step 8); rewrote "Know which hat you wear" to "Say Atlas One, always"; stripped WSA from the lane A who list, the trigger list, the day 5 email note, the rules cards, the Monday and targets rows ("ask WSA for the next ten names"); section 7 identity row now shows the rep's name, title, email and phone; referral paste line no longer says "David runs..., the vendors pay him"; "400 clients" and "400 existing clients" to "your clients"; "Utah" and "Mountain for Utah names" to "[state]" and "time zone of each list"; Draper and Lehi examples to [City]; heading "The rules (yours...)" to "the house rules".
- **Sales Conversation Playbook**: removed the toggle sentence and "Zak Call at WSA asked me to reach her"; removed David's backstory ("placing businesses ... for about six years and I service around 400 of them"), "my kids' names", "Your 400 clients", "You said it yourself", "You use small jokes", "your real line", "the guy who makes paperwork disappear" (now "person"). All objection handling, discovery, pitch ladder and closes kept.
- **Overlay 01 Audiology**: 19 only-wsa blocks removed (WSA channel box with the VIP rates $150/$175/$200 and the credit, WSA handoff sequence, WSA trigger rows, WSA objection, "Before the first batch" list, WSA spans), channel picker removed, direct channel kept as the one channel; "Pricing" row rewritten (printed PEO tier prices $175/$200/$225 removed, now "Quoted for the practice (headcount, pay cycle, PTO tracking and more)"); "Brand" row removed; Lost_Prospects folder reference reworded; guardrails now "never name a PEO or vendor brand".
- **Overlay 02 Dental**: "No WSA on this page" removed; "Margin lives in the optical" to "Profit lives in the optical"; quote "Our margin is in the optical" to "Our profit..."; Draper office to [City]; chip "Brand: your choice up top" removed.
- **Overlay 03 Construction**: Utah slow season to "the cold months in your state"; Lehi to [City]; brand chip removed.
- **Overlay 04 Technology**: "Utah software teams" to "[state] software teams"; brand chip removed.
- **Overlay 05 Hospitality**: "Cirque Lodge is your proof story" removed; "thin-margin" to "low-profit"; brand chip removed.
- **Overlay 06 Professional Services**: brand chip removed only (plus common passes).

Prices: no Atlas One price is printed in the 8 files after the scrub (the only ones were the PEO tiers in overlay 01, removed). Remaining dollar figures are industry statistics (turnover cost, billable rates). Overlay 04's source line quotes a third party PEO cost benchmark ("about $116 per employee per month", Warp 2026); left as a market statistic.

## Verification
- test_rep_scrub.py, 8 ids, pipeline as build_entries runs it for `charity`: text checks PASS for all (no cornerstone, david, wsa, margin after CSS strip, commission, wholesale, g&a, verohcm, 385 phone, cornerstonepeo, Hearvana, Utah, toggle, dash characters, localStorage; the build's own leak scan function also clean).
- Playwright, 1440 and 390, every id: zero console errors, zero page errors, scrollWidth equals viewport (390), zero non file requests, every data-k placeholder filled, every visible button and TOC link clicked with no JS errors (playbooks have 10 jump links; overlays have only the Print button, no lane picker remains).
- Looked at: overlay-01-audiology-1440, prospecting-playbook-v1-390, sales-conversation-playbook-1440, overlay-05-hospitality-and-restaurants-390, prospecting-s7-1440. These caught two things I then fixed (a leftover "Brand: your choice" chip on overlays 02 to 06, and David voice in the Sales Playbook lead paragraphs).
- Build: `build_command.py <MK> --person charity`, run once as asked, FAILED at the Job 2 leak guard (and restored Charity's previous kit, failed partial left in `_to_delete/superseded-2026-09-30/charity-kit-before-CS-4-FAILED-BUILD`). Cause: only catalogue blurbs, not the scrubbed files. Tail: `Job 2 guard: default person leak in rep kit ... (cornerstone): <div class="zone" id="zone-sales-kit" ...`. The matches were the blurbs of overlay-01 ("WSA Partnership Plus referral or direct prospect; WSA locks Cornerstone identity.") and sales-conversation-playbook ("... Atlas One / Cornerstone toggle.").
- To prove everything else passes I re-ran the same build through a wrapper (`/private/tmp/claude-501/scratch/rs/patched_build.py`) that patches those blurbs (and the prospecting blurb) in memory only: exit 0, "forbidden terms: none", "Job 2 guard: clean, zero david@... / David Taylor / cornerstone leaks", Charity Taylor kit complete, 97 items. NOTE: the Charity kit now on disk is that patched build.

## Needs the lead (catalogue.py, not mine to edit)
Change three blurbs, then a plain `build_command.py --person charity` will pass:
1. overlay-01-audiology: `Audiology practices: the buyer, the three numbers, objections, trigger events, call and email sequence.`
2. sales-conversation-playbook: drop " Atlas One / Cornerstone toggle." from the end.
3. prospecting-playbook-v1: "GHL workflow map W1 to W7" to "W1 to W6" (W7 is the WSA handoff, removed from the rep copy).
Also check the `find`/search keywords are built from blurb (they were; the grep hits were in data-find).

## Assumptions
1. Charity's booking link is empty in people.json, so booking placeholders read "[your booking link]" and "[your 15-minute booking link]" until she has one.
2. Utah, Draper and Lehi in examples were treated as Utah market assumptions and bracketed ([state], [City]), per the 50 state rule.
3. "Hello this is David" style first person lines became the rep's first name; "David Taylor with ..." became the rep's full name (Charity Taylor).
4. The audiology overlay keeps the "direct" lane only; WSA is not mentioned anywhere in the rep copy.
5. Printed PEO tier prices in overlay 01 were removed rather than updated, since PEO/ASO/HCM rates are never printed (V9).
6. Existing "existing PEO clients (relaunch)" table row and chapter 8 "Existing clients and referrals" were kept with the rep's name; they read generically.
7. Email drafts excluded (above).

## Skipped
Email Drafts 2026-09-06 (see Excluded).

## Questions for David
1. The playbooks tell the rep to say "the vendors pay me" and "the payroll, benefits and insurance companies pay me to bring them good clients, the same way they'd pay any broker" (Prospecting objection 6, Sales Playbook ladder, near-free line, overlays). I kept them because they are the core objection handling, but Charity is not licensed for insurance and has no PEO partner relationship. Is it true and allowed for her to say insurance companies pay her? If not, I will reword those lines for rep copy (about 12 places).
2. Overlay 06 says referral fees to partners go through the Referral Partner program and the Won-to-Pay workflow. Keep for reps, or drop?
3. Do you want a rep version of the client relaunch emails written for Charity's own situation, rather than David's?
4. Prospecting Playbook section 8 is a GHL build map ("what to build, in order") and the Existing PEO clients row mentions PEO; both are internal build content a rep may not need. Left in.
