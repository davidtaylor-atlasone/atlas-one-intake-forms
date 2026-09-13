# RUN W report (terminal B, files only)

Built 2026-09-12 by Claude Code, unattended, no GHL UI, no questions asked. Run W had not started when this session opened (no repo copy of the brief, no progress log, no report), so it was run from the top. Brief copied to `repo:_briefs/RUN-W-terminal-B.md` with a progress log; scripts, before/after captures and renders in `repo:_briefs/assets/run-W/`. Nothing sent, nothing deployed beyond the normal Pages push, nothing deleted (copies from before the pass are in `OneDrive:_to_delete/superseded-2026-09-12/tools-before-dash-pass/`, repo copies under `repo-tools/`). Pricing numbers, agreements, division sheets, decks and BUILD-INDEX.md were not touched.

Paths are relative to `HR_Docs/Atlas_One_Master_Kit/06 Calculators and Tools (NEW Aug 2026)/` unless marked `repo:` (atlas-one-intake-forms, main, pushed) or `OneDrive:`.

## Job 1: inventory (before the pass)

Method: `repo:_briefs/assets/run-W/inventory.py` walks each HTML file and classifies every em dash, en dash, entity form (`&mdash;`, `&ndash;`, `&#8212;`, `\u2014` and friends) and spaced hyphen by where it sits: text node, visible attribute (placeholder, title, alt, aria-label, and the bilingual `data-en` / `data-es` strings that are rendered into the page), or JavaScript string literal (including template-literal chunks, which are what the builders render). CSS, JavaScript operators and regexes, HTML comments, base64 blobs and non-visible attributes are excluded. Hyphens inside compound words (W-2, co-employment, E-Verify, 1099-NEC) never matched because only *spaced* hyphens were counted.

| File | Em before | En before | Spaced hyphen before | After (all three) |
|---|---:|---:|---:|---:|
| Atlas One — Your Savings Summary.html | 18 | 2 | 0 | 0 |
| Atlas One Business Tools (17 generators).html | 191 | 7 | 1 | 0 |
| Atlas One Calculators (53 tools).html | 415 | 156 | 0 | 0 |
| Atlas One Savings Summary (Atlas One).html | 18 | 2 | 0 | 0 |
| Atlas_One_Collections_Letter.html | 5 | 0 | 0 | 0 |
| Atlas_One_Feedback_Request.html | 3 | 0 | 0 | 0 |
| Atlas_One_Onboarding_Tracker.html | 20 | 0 | 0 | 0 |
| Atlas_One_PEO_vs_ASO_vs_Software.html | 9 | 0 | 0 | 0 |
| Atlas_One_Scan_ID.html | 4 | 0 | 0 | 0 |
| Atlas_One_Time_Savings_Discovery.html | 1 | 0 | 0 | 0 |
| Atlas_One_True_Cost_Calculator.html | 6 | 0 | 0 | 0 |
| Atlas_One_WC_No_Loss_Letter.html | 4 | 0 | 0 | 0 |
| atlas-command-center.html | 10 | 0 | 0 | 0 |
| Business Infrastructure Audit (Atlas One).html | 10 | 0 | 0 | 0 |
| Business Infrastructure Audit (Espanol).html | 1 | 0 | 0 | 0 |
| Business Value Diagnostic (Atlas One).html | 15 | 7 | 0 | 0 |
| Business Value Diagnostic (Espanol).html | 15 | 5 | 0 | 0 |
| Certified Payroll Converter (WH-347) (Atlas One).html | 31 | 1 | 0 | 0 |
| Certified Payroll Manager (Atlas One).html | 155 | 4 | 0 | 0 |
| COI to Workers Comp Premium Estimator (Atlas One).html | 15 | 0 | 0 | 0 |
| Compliance Risk Scorecard (Atlas One).html | 11 | 0 | 0 | 0 |
| Cost of a Compliance Mistake (Atlas One).html | 10 | 6 | 0 | 0 |
| Disciplinary Write-Up Notice Generator (Atlas One).html | 18 | 0 | 0 | 0 |
| Employee Benefits Options (Atlas One).html | 51 | 0 | 0 | 0 |
| Employee Benefits Package & Enrollment Guide (Bilingual) (Atlas One).html | 27 | 0 | 0 | 0 |
| Employee Handbook Builder (Bilingual 50-State).html | 194 | 0 | 0 | 0 |
| Health Comparison Builder (Atlas One).html | 68 | 1 | 0 | 0 |
| Health Quote Census Intake (Atlas One).html | 33 | 0 | 0 | 0 |
| Independent Contractor Agreement Builder (Atlas One).html | 6 | 0 | 0 | 0 |
| Independent Contractor Onboarding Packet (Bilingual).html | 18 | 3 | 0 | 0 |
| Meeting Bonus Import Builder (Atlas One).html | 12 | 0 | 0 | 0 |
| NDA Builder (Atlas One).html | 13 | 0 | 0 | 0 |
| Payroll to GL Import Converter (Atlas One).html | 2 | 0 | 33 | 0 |
| Retention Cost Calculator (Atlas One).html | 28 | 19 | 0 | 0 |
| Retention Cost Calculator (Espanol).html | 28 | 19 | 0 | 0 |
| Retention Scorecard (Atlas One).html | 14 | 0 | 0 | 0 |
| Retention Scorecard (Espanol).html | 14 | 0 | 0 | 0 |
| Safety Manual Builder (Bilingual OSHA).html | 196 | 0 | 0 | 0 |
| Separation Letter Generator (Atlas One).html | 21 | 0 | 0 | 0 |
| Vendor Consolidation Savings (Atlas One).html | 5 | 0 | 0 | 0 |
| Vendor Consolidation Savings (Espanol).html | 1 | 0 | 0 | 0 |
| W-2 At-Will Employment Agreement Builder (Atlas One).html | 8 | 2 | 0 | 0 |
| W-2 Employee Onboarding Packet (Bilingual).html | 18 | 0 | 0 | 0 |
| tools/retention-cost/index.html | 28 | 19 | 0 | 0 |
| tools/vendor-consolidation/index.html | 5 | 0 | 0 | 0 |
| tools/wc-premium-check/index.html | 15 | 0 | 0 | 0 |
| **Total (46 files)** | **1790** | **253** | **34** | **0** |

Files with no visible dashes before (unchanged): Atlas_One_Back_Office_Self_Assessment.html, Atlas_One_Build_This_For_Me.html, tools/index.html, tools/self-assessment/index.html


Not counted anywhere: `Atlas One PORTAL.html` and the Tools Hub (outside the brief's two folders); comments and CSS inside the files (for the record, 125 non-visible dashes remain in the 53 tools file's code comments and CSS, 40 in the Certified Payroll Manager's).

## Job 2: the pass

- Rewriter: `repo:_briefs/assets/run-W/dashpass.py` plus 17 exact-string overrides in `overrides.json`. Every one of the 1,706 proposed unit rewrites was listed in `dash-review-proposed.md` and read through before the files were touched; rules were tightened seven times on that review before the first apply.
- The rules, in the order applied: (1) numeric, date and word ranges become "to" (`$288–$2,861` to `$288 to $2,861`, `Mon–Fri` to `Mon to Fri`, `low–high` to `low to high`); (2) "label — value" and any dash after a short lead (five words or fewer, or a short heading-like line) becomes a colon (`Section 1 — Governing Principles` to `Section 1: Governing Principles`, `Zone 7 — Very Cold` to `Zone 7: Very Cold`, the QuickBooks memo `Payroll 09/12 - gross wages` to `Payroll 09/12: gross wages`); (3) a dash mid-sentence becomes a comma, always a comma when the right side starts with a conjunction; (4) a pair of dashes around an aside becomes a pair of commas, or parentheses when the aside carries its own commas (`Disrespectful behavior — including spreading rumors, making untruthful statements, or similar conduct — undermines` to `Disrespectful behavior (including ...) undermines`; Spanish `—incluidos ...—` the same way); (5) wrapped option labels `— none —` become `(none)`; hint spans after a label become parentheses (`Party A — Disclosing Party` to `Party A (Disclosing Party)`); (6) a lone "—" or "$—" standing in for a value that has not been calculated or entered yet becomes "…" / "$…" (assumption 2); (7) a trailing dash before a dynamic value becomes a colon (`Atlas One results —` to `Atlas One results:`). No number, merge field, URL, class name or id changed; nothing was deleted.
- Spanish files (Business Value Diagnostic, Business Infrastructure Audit, Retention Cost Calculator, Retention Scorecard, the three bilingual packets, and the Spanish halves of the Handbook and Safety Manual data) went through the same rules.
- Two places where the copy edit touched JavaScript, both logged because the brief said not to change logic: the Handbook and Safety Manual builders strip the "Section N — " prefix from group names with a regex (`shortGroup`) when building the optional-section toggle list; with the prefix now "Section N: " that regex would have left the whole string, so the character class gained a colon (`[\u2014-]` to `[\u2014:-]`, one character, both files). In Cost of a Compliance Mistake the low/high total range is two spans with a `<span class="dash">` between them; the scanner's generic rule would have made it a bare hyphen, so it was set to "to" by hand. No other JS changed; the pass never touched code outside string literals.
- Verification per file (all 46): opened headless in Chromium at 1440 px, zero JavaScript errors on load, before and after (`render-log.json`). One deterministic sample run per tool: every input, select, checkbox and textarea filled from a fixed pattern, every calculate/generate/preview button fired (never print, download, save, send, submit, reset), and for the Business Tools page all 28 generators walked through `select()`; the visible text, field values and every number on the page captured before (`sample-before-kit.json`, run on the copies in `_to_delete`) and after (`sample-after-kit.json`). `compare.py`: the number sequences are identical on all 46 files, the words are identical apart from the dash rewrites themselves (inserted "to" and "…"), and the error counts match, including the two tools whose synthetic run trips their own guards (Business Tools 10, command center 2, identical before and after, zero on plain load). One residual, an improvement: the Handbook toggle list showed a literal "&mdash;" as raw text (`Protected Rights &mdash; Savings Clause`, the group name is inserted as text, not HTML); it now reads "Protected Rights: Savings Clause".
- Rendered at 390 px (mobile, touch) and 1440 px, full page, all 46: `contact-390.png` and `contact-1440.png` in `repo:_briefs/assets/run-W/`, looked at. No layout change from the copy edits. Six files scroll horizontally at 390 px (Onboarding Tracker 522, Employee Benefits Options 413, Handbook Builder 855, NDA Builder 470, Safety Manual Builder 833, W-2 Agreement Builder 439); the same six give the same widths on the before copies, so pre-existing (question 3).
- After counts: 0 em, 0 en, 0 spaced hyphens visible in every file (`inventory-after.json`).

### Claims flagged, not changed (for David)

Marketing-facing wording that reads as a guarantee or a superlative. The only permitted guarantee wording is the Audit Guarantee; none of the tools use it. Disclaimers ("not a guarantee of savings", "does not guarantee compliance") and the Handbook / Safety Manual / agreement legal text (at-will "no guarantee of employment", the personal guaranty on the credit application, "to the best of my knowledge" on the W-9 and W-4, EEO "guarantees equal treatment") are left out as not marketing claims.

1. Business Value Diagnostic (EN and ES), L61: "The Fortune-500 view" / "La perspectiva Fortune 500" (section heading).
2. Employee Benefits Options: "Guaranteed rates confirmed before you enroll" (L411), "Guaranteed monthly rate" (L445, L582), "Guaranteed rates: David will confirm" (L466, L510, L604), "MEC plans with guaranteed pricing" (L577), "a stable, guaranteed price" (L578), "You'll get guaranteed rates across the options" (L693), "Guaranteed rates, confirmed before you ever enroll" (L709); the L724 footnote already limits this to "guaranteed only once confirmed by David in writing".
3. Atlas One Calculators (53 tools): "rebuild your handbook to bulletproof standards" (L676); "download a fully compliant COI in under a minute" (L1019); "Atlas One's payroll partners get this right every time" (L2918); "The cheapest way to fix a bad hire is to not make one" (L4293, a saying, low risk).
4. Business Infrastructure Audit (EN L26, ES L26): "Payroll runs on time with taxes filed correctly, every time." (a checklist statement the owner rates, low risk).
5. PEO vs ASO vs Software: "Usually the best value" (L125, PEO card), "the lowest true cost" (L139, L141).
6. Atlas One Calculators: "Most SMBs get health-plan and workers-comp pricing they could never negotiate alone" (L4085); "Atlas One typically saves clients 15 to 30% on workers comp" (L2780, a typical-savings figure, not a guarantee, but worth a source).
7. Retention Cost Calculator (EN/ES and repo): "retention ... is the cheapest dollar you spend" (L423).
8. No "A-rated", "#1", "world-class", "industry-leading", "risk-free" or "100% guaranteed" wording in any of the 46 files. The word "always" appears 27 times and "never" 53 times, almost all in instructions ("Always verify your state's rules", "never silently dropped", "Never had one" as an answer) rather than claims; the full list is in `repo:_briefs/assets/run-W/claims.txt` (183 lines).

## Job 3: publish

- Repo: `repo:tools/retention-cost/index.html`, `repo:tools/vendor-consolidation/index.html` and `repo:tools/wc-premium-check/index.html` rewritten with the same pass (the retention and vendor files are byte-identical to the kit copies; the WC file keeps its pre-existing repo-only differences). `repo:tools/self-assessment/index.html` and `repo:tools/index.html` had no visible dashes and were not touched. Pushed on main (`2ed5f83`).
- Live: `https://forms.atlasonesolutions.com/tools/retention-cost/`, `/tools/vendor-consolidation/`, `/tools/wc-premium-check/` all return 200 and the served file is byte-identical to the pushed one (checked after Pages redeployed); `/tools/self-assessment/` 200, unchanged.
- Portal rebuilt with the path argument: **BUILD Sep 12, 2026 9:01 PM**, 38 tools, 10.34 MB. Opened headless: title and hero chip carry the stamp, no errors; the inlined payloads carry the new copy (checked inside the base64 for the 53 tools file and the retention calculator).

## Assumptions

1. "Visible copy" includes the `data-en` / `data-es` strings in the bilingual packets (they are what the language toggle renders) and every JavaScript string literal in the builders and generators (that is where their document text lives), but not code comments, CSS or the `[·•\-–]` parsing regexes in the Payroll to GL converter.
2. A lone "—" that stands in for a not-yet-calculated result (`<span id="cf_runway">—</span>`, `$—`, `— / 10`) or an empty document field in the generators (`fmtDate(v.due)||'—'`) is now "…" (`$…`, `… / 10`, `Effective …`). "n/a" was tried first and read wrong on score tiles ("n/a / 100"); "0" would invent a number. The ellipsis is the one placeholder that is not a dash; say the word if you want blank instead.
3. En dash ranges became "to" without touching the digits, so "2025–26" is now "2025 to 26" (Retention Cost Calculator EN/ES and repo; Business Value Diagnostic EN/ES). Writing "2025 to 2026" would have been clearer but adds digits (question 2).
4. The `shortGroup` regex and the compliance-range span are the only two non-string edits; both are one-token changes needed so the rendered output stays identical, logged above.
5. The 53 tools file and the Business Tools file are single pages; their sample runs fill all 418 / all 28 generators' inputs, so "the tool's own sample calculation" there is a synthetic pass rather than a hand-picked scenario. Numbers matched exactly.
6. The Certified Payroll Manager's `Gross — all work` / `Gross — this project` column labels are quoted in its help text ("Leave 'gross — all work' blank if..."); label and quote were changed together to the colon form.
7. `Atlas One — Your Savings Summary.html` is a byte-identical duplicate of `Atlas One Savings Summary (Atlas One).html`; both were rewritten; the file name with the em dash was left alone because Hub cards may link to it (question 4).
8. The tools index card copy (`repo:tools/index.html`) had no dashes and was left as is.

## Not done / skipped

- Nothing in the brief was skipped. The six pre-existing 390 px overflows and the Portal's own title ("Atlas One Portal — build ...", generated by `build_portal_single.py`, outside the brief's folders) were noted, not fixed.

## Questions for David

1. Placeholders: "…" for a result that has not been calculated yet (assumption 2), or would you rather see a blank?
2. "2025 to 26" (from "2025–26") appears in four files; OK to write "2025 to 2026"?
3. Six tools still scroll sideways on a 390 px phone (Onboarding Tracker, Employee Benefits Options, Handbook Builder, NDA Builder, Safety Manual Builder, W-2 Agreement Builder); they did before this run. Want a mobile pass on those like Run V did for the calculators?
4. The file name `Atlas One — Your Savings Summary.html` still has an em dash and is a duplicate of `Atlas One Savings Summary (Atlas One).html`. Retire the duplicate to `_to_delete`?
5. The Portal page title reads "Atlas One Portal — build Sep 12, 2026 9:01 PM"; that comes from `_INTERNAL/build_portal_single.py`. Change it to a colon in the builder?
6. The Employee Benefits Options presenter says "guaranteed rates" nine times (claims item 2). Keep, given the written-confirmation footnote, or soften to "confirmed rates"?
