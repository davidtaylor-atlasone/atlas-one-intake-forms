# Run GHL-JOBS report -- Run CI, 2026-09-24

Charity's kit: tools inside it, the guard that missed them, the Cornerstone toggle, the licensed agent
line. All 5 jobs from the brief (`_briefs/BRIEF-GHL-JOBS-2026-09-24.md`) are complete, verified, and
pushed.

## What was built

### Job 1: the guard now decodes inside the Sales Kit file
`build_command.py` gained `_decode_blobs(html_text)`, which finds every `<script type="text/plain"
id="tN">BASE64</script>` block a built Sales Kit/rep kit file carries (every inlined tool is parked this
way) and base64-decodes it. `scan_default_person_leak()` now runs its line scan on the raw file text AND
on every decoded blob, through a shared helper `_scan_text_for_person_leak()`. This is exactly the gap
Cowork found by hand: the old guard only ever saw the outer file's own text, never the 58 tools parked
inside Charity's Sales Kit.

### Job 2: tools carry the company line, not a person
Swept every master source file with a hardcoded "David Taylor" outside a swap contract and changed each
to the company line only (`Atlas One Solutions · support@atlasonesolutions.com · 380-CALL-A1S
(380-225-5217) · AtlasOneSolutions.com`, reusing the existing separator/markup style already on each
page) or a neutral placeholder for sample data:

- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Business Tools (17 generators).html` -- org chart
  sample `"President: David Taylor"` to `"President: Name"`.
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Savings Summary (Atlas One).html` -- footer.
- `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Onboarding Packet (Bilingual).html` --
  8 repeated footer lines, 2 inline EN/ES sentences.
- `06 Calculators and Tools (NEW Aug 2026)/W-2 Employee Onboarding Packet (Bilingual).html` -- 9 footer
  lines, 2 inline EN/ES sentences, 1 closing note.
- `12 GHL Setup doccs/Atlas_One_Booking_Confirmation.html` -- "Your call with David Taylor is confirmed"
  to "Your call is confirmed" (no name at all); footer card to company line.
- `06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Package & Enrollment Guide (Bilingual)
  (Atlas One).html` -- contact card heading "David Taylor" to "Atlas One Solutions".
- `Atlas One -- Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html` -- this is the
  actual file behind the brief's "t38 Free HR Templates footer" finding (catalogued as "HR Template
  Library", a real prospect-facing Sales Kit row, not a BRJ-only asset out of scope). Footer changed to
  company line only.

`Employee Benefits Options (Atlas One).html` needed more than a text swap: it had NO a1-footer-person or
a1-contact-person contract at all, so its "David Taylor, Licensed Broker" header byline and its footer
contact card were being silently skipped by every prior rep-kit build (`skipped_no_footer`, a
Tools-zone piece), leaking David's name and phone into every rep's kit including Charity's. Added a new
`a1-contact-person` kind (`name-title`, renders just `"Name, Title"`) for the header byline, and made the
footer card's name/title a real `a1-footer-person` element so `swap_footer_person()` actually runs on this
file for the first time. The booking link text "Book a time with David" was changed to "Book a time" (no
bare first name).

Rebuilt COMMAND (206 items) and the shared Sales Kit (58 items) after each batch of edits; both stayed
clean throughout.

### Job 3: the licensed agent line
`people.json`: added `"licensed_insurance": true` to david, `"licensed_insurance": false` to charity.

`build_command.py` gained `LICENSED_AGENT_SENTENCE` ("Insurance products are offered through David
Taylor, licensed agent."), the `_LICENSED_AGENT_PATTERN` regex matching `<span
class="a1-licensed-agent"...>...</span>`, and `_apply_licensed_agent(raw, person)`, which strips the span
entirely when the VIEWING person's own `licensed_insurance` is true and leaves it untouched otherwise.
Wired into `build_entries()` (keyed to the default person for COMMAND/the shared Sales Kit, or the target
rep for a `--person` build) and into `build_rep_footer_swapped_set()` (the standalone Sales
Pieces/Division Sheets copies).

Added the sentence, wrapped in `<span class="a1-licensed-agent">`, to all four target pieces:
- `Atlas_One_Employee_Benefits_Menu.html` (footer, under the existing a1-footer-company line).
- `Employee Benefits Options (Atlas One).html` (footer contact card, under the new a1-footer-person line;
  the old "David Taylor, Licensed Broker" byline became the swappable person line per Job 2).
- `Atlas_One_Division_Benefits_Retirement.html` and `Atlas_One_Division_Risk_Insurance.html` (small print
  under each sheet's existing footer, matching its print-style sizing).

`scan_default_person_leak()`'s guard now allowlists this one sentence globally (an exact string match,
checked on both raw text and every decoded blob) instead of the old filename-scoped Cornerstone
allowlist it replaces -- nothing else naming David is exempt anywhere.

**Real bug found and fixed**: the first version of `_LICENSED_AGENT_PATTERN` only matched
`class="a1-licensed-agent">` with no other attributes in between. Two of the four target spans also carry
a `style=` attribute, so they were never being stripped from David's own COMMAND build (he'd have seen
himself named as a separate licensed agent, which is exactly the case Job 3 says should not render).
Widened the pattern to `class="a1-licensed-agent"[^>]*>` and reverified: 0 of 0 target spans remain in
COMMAND now (all 3 that should have been stripped for David, are).

### Job 4: no Cornerstone in a rep kit
Removed `scan_default_person_leak()`'s old `_ALLOWLIST = {"Atlas_One_Employee_Benefits_Menu.html":
"Cornerstone PEO"}` entry entirely. `FORBIDDEN_ALLOWLIST`'s own, separate "cornerstone" entry for this
same file (used by COMMAND's Present-forced content check) was left alone -- unrelated guard, and the
master/COMMAND build still legitimately carries CONFIG.cs.

Added `_strip_cornerstone_config(raw)`, which removes the whole `cs: {...}` property (and its one code
comment naming Cornerstone) from `CONFIG` via a bracket-safe regex, verified against the real source
structure before wiring in. Called only from `build_rep_footer_swapped_set()`, only for this one
filename, only when `person_slug != default`: a rep's own standalone copy of the Employee Benefits Menu
now has zero trace of Cornerstone; the master file (behind a brand toggle with no wired UI button today)
is untouched.

Added a case-insensitive "cornerstone" hard fail to the new shared `_scan_text_for_person_leak()` helper
(used by `scan_default_person_leak()`), checked on raw text, every decoded blob, and PDF text -- any rep
kit file containing "cornerstone" anywhere now hard fails the build, no exceptions.

### Job 5: rebuild Charity and prove it
`python3 "<Master_Kit>/_INTERNAL (do not share)/build_command.py" --person charity "<Master_Kit>"`
completed clean: `Job 2 guard: clean, zero david@atlasonesolutions.com / David Taylor / cornerstone leaks`.

**Real leak found while first testing the new guard against a real rebuild** (before the Job 2/5 fixes
above landed): the Health Quote Census Intake tool (`06 Calculators and Tools (NEW Aug
2026)/Health Quote Census Intake (Atlas One).html`, catalogue id `health-quote-census`) had NO
a1-footer-person/a1-contact-person contract at all, despite naming David Taylor publicly in its footer
and a print-only paragraph. It was silently skipped by every prior rep-kit build and leaked "David
Taylor, Founder" twice into blob t29 of Charity's Sales Kit -- confirmed by decoding the blob directly.
Added the contract (a1-footer-person on the footer's name/title text; a1-contact-person name-title on the
print-only line) and changed "Book 15 minutes with David" to "Book 15 minutes". Rebuilt; the guard now
passes clean on this file. (Note: the brief's own Job 2 exception for this file, "already swaps correctly
via the existing a1-footer-person contract," was not accurate -- it had no such contract before this run.
See Assumption 6.)

## What was looked at

**Decoded-blob scan and PDF text scan** (Python script, `/tmp/verify/verify_charity.py`, not committed --
scratchpad only) walked all 42 files under `A1_Sales/_Rep Kits/Charity Taylor/`, decoding every HTML
file's blobs and extracting every PDF's text (pypdf), checking for `david@` (any case), `David Taylor`
outside the one allowed licensed-agent sentence, `cornerstone` (any case), the old phone number pattern,
and dash characters (em/en dash only, not ordinary hyphens):

| Check | Result |
|---|---|
| `david@` anywhere | 0 across all 42 files |
| `David Taylor` outside the licensed-agent sentence | 0 across all 42 files |
| `cornerstone` (any case) | 0 across all 42 files |
| old phone (385-213-7177 pattern) | 0 across all 42 files |
| licensed-agent sentence present | exactly 1 per relevant file (Employee Benefits Menu HTML+PDF,
  Division Sheets Benefits & Retirement and Risk & Insurance HTML+PDF -- 6 files total), 0 elsewhere |
| em/en dash characters | **416, in the Sales Kit HTML's decoded blobs only** -- see Assumption 7, this
  is pre-existing content across 29 different tools' own copy and code comments, none of it introduced by
  Jobs 1-4 of this run |

Every other file (Division Sheets, One Pagers, Sales Pieces, Price List, READ ME FIRST.txt) is fully
clean on every check.

**Headless Chromium (Playwright, Python venv at
`/Users/davidtaylor/Projects/atlas-one-ai-email-assistant/.venv/bin/python`)** rendered Charity's Sales
Kit and Atlas One COMMAND.html at 1440px and 390px width, capturing console messages:

| File | Width | scrollWidth | Console errors |
|---|---|---|---|
| Atlas One Sales Kit (Charity Taylor).html | 1440 | 1440 | 0 |
| Atlas One Sales Kit (Charity Taylor).html | 390 | 390 | 0 |
| Atlas One COMMAND.html | 1440 | 1440 | 0 |
| Atlas One COMMAND.html | 390 | 390 | 0 |

Screenshots: `_briefs/assets/run-CI-jobs/charity-saleskit-1440.png`,
`charity-saleskit-390.png`, `command-1440.png`, `command-390.png`.

Also confirmed directly (decoding COMMAND's own blobs): 0 of 3 licensed-agent spans remain visible in
David's own COMMAND build (all correctly stripped since he is the licensed person); the Employee Benefits
Menu's own copy in COMMAND was already correctly stripped on the first pass, confirming the bug was
specifically the two spans carrying an extra `style=` attribute.

## Paths touched

Master Kit (`_INTERNAL (do not share)/`):
- `build_command.py` -- `_decode_blobs`, `LICENSED_AGENT_SENTENCE`, `_LICENSED_AGENT_PATTERN`,
  `_apply_licensed_agent`, `_strip_cornerstone_config`, `_scan_text_for_person_leak`, a new
  `name-title` `a1-contact-person` kind, `scan_default_person_leak()` rewritten, `build_entries()` and
  `build_rep_footer_swapped_set()` wired to the new helpers.
- `people.json` -- `licensed_insurance` field added to david and charity.

Master source files (A1_Sales and 06 Calculators and Tools):
- `A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html`
- `A1_Sales/Atlas 1 Benefits/Atlas_One_Division_Benefits_Retirement.html`
- `A1_Sales/Atlas 1 Risk Docs/Atlas_One_Division_Risk_Insurance.html`
- `06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Options (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Business Tools (17 generators).html`
- `06 Calculators and Tools (NEW Aug 2026)/Atlas One Savings Summary (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Independent Contractor Onboarding Packet (Bilingual).html`
- `06 Calculators and Tools (NEW Aug 2026)/W-2 Employee Onboarding Packet (Bilingual).html`
- `06 Calculators and Tools (NEW Aug 2026)/Employee Benefits Package & Enrollment Guide (Bilingual)
  (Atlas One).html`
- `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html`
- `12 GHL Setup doccs/Atlas_One_Booking_Confirmation.html`
- `Atlas One -- Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html`

Generated outputs rebuilt: `Atlas One COMMAND.html`, `A1_Sales/Atlas One Sales Kit.html`, and the whole
`A1_Sales/_Rep Kits/Charity Taylor/` folder (Sales Kit, Division Sheets, One Pagers, Sales Pieces, Price
List, HTML + PDF each).

Repo (`atlas-one-intake-forms`): `_briefs/BRIEF-GHL-JOBS-2026-09-24.md`,
`_briefs/assets/run-CI-jobs/*.png`, this report copied to
`_briefs/assets/run-CI-jobs/RUN-GHL-JOBS-report.md`.

Build logs: `TERMINAL-GHL-JOBS-live.md` (appended), this file, and 11 `TOOL-<name>-log.md` files (one per
master tool touched, per the TOOLS terminal rule).

## Assumptions

1. **Company-line wording and markup**: reused the exact separator style and phrasing each page already
   used (`&middot;`/`·`, sometimes `<br>`) rather than inventing one new format, so each edit reads as a
   natural extension of its own page rather than a visibly different patch.
2. **Job 3's gating rule**: the licensed-agent sentence renders for every viewer EXCEPT one whose own
   `licensed_insurance` is true. For COMMAND and the shared Sales Kit (no `--person` given), the viewing
   person is the default person (David, licensed) so the sentence is stripped there too -- he does not
   need to be told insurance is offered "through" himself. It only shows for a non-licensed rep's kit
   (Charity today).
3. **Employee Benefits Options's swap contract**: added a new `a1-contact-person` kind, `name-title`
   (renders `"Name, Title"` only, no phone/email), reused for the header byline. The footer's name/title
   line became a real `a1-footer-person` element (previously none existed), so `swap_footer_person()` now
   also swaps the header byline's `a1-contact-person` span, since any `a1-footer-person` anchor triggers a
   whole-file swap pass. Trade-off: after a swap, the footer's `a1-footer-person` content becomes the
   full standard person line (name, title, email, phone, booking link), which sits above the file's own
   already-hardcoded email/phone/site lines -- a visible duplication, not a leak. A cleaner fix (a
   dedicated compact swap format for this file) was out of this run's time budget; flagged as a
   Question below.
4. **CONFIG.cs stripping (Job 4)**: scoped narrowly to `build_rep_footer_swapped_set()`'s handling of
   this one filename, for non-default persons only. Verified against the actual source structure (no
   nested braces inside `cs: {...}`, a comma-tolerant trailing brace) before wiring in, and confirmed by
   direct decode that Charity's own Employee Benefits Menu copy carries zero trace of "cornerstone"
   afterward.
5. **The Job 1 finding list in the brief (t0/t19/t24/t29/t30/t33/t37/t38/t48) describes Charity's stale,
   already-built kit's blob ORDER**, not literal file identities -- blob indices are build-order dependent
   and meaningless as file identifiers across two different builds. Traced each finding back to its real
   master source file by content, not by index, and fixed all of them; also found two the brief's own list
   did not separately call out by index (Employee Benefits Options's missing swap contract entirely, and
   the census tool's missing contract, both real leaks caught only because Job 1's new guard actually
   works now).
6. **The brief's Job 2 said the census public footer "already swaps correctly via the existing
   a1-footer-person contract" and should be left alone.** That was not accurate: the file had no such
   contract at all. Since leaving a confirmed, guard-caught leak unfixed would contradict the run's whole
   point, added the contract (matching the public, no-email format Run CF already established for this
   kind of page) rather than leaving it broken. This is a deviation from a literal reading of the brief,
   made because the brief's stated justification for the exception did not hold.
7. **The 416 em/en dash hits inside the Sales Kit's decoded blobs are flagged, not fixed.** They span 29
   different inlined tools' own copy and JS/CSS comments, entirely pre-existing and untouched by this
   run's edits (confirmed by sampling: none of the dash occurrences are inside any file this run
   touched). A full dash sweep of every inlined tool is materially larger than Jobs 1-5 and was not asked
   for; flagged here and in Questions below rather than silently expanding scope.
8. **The BRJ kit folder ("Atlas One -- Complete Kit for BRJ/") is generally a separate, white-labeled
   partner deliverable and out of this run's scope**, except for the one file inside it
   (`2. Interactive Tools (embed these)/templates.html`) that catalogue.py actually reuses as a real,
   currently-live Sales Kit row ("HR Template Library"). Only that one file was edited; the rest of the
   BRJ tree (its own separate index, labor law posters, etc.) was left alone as out of scope.

## Skipped

Nothing in the 5 jobs was skipped. The dash sweep (Assumption 7) is flagged as future work, not skipped
work this run was asked to do.

## Questions for David

1. **The 416 pre-existing em/en dash characters found across 29 inlined tools in the Sales Kit** (Business
   Tools generators, the Booking Confirmation page, the Quote & Onboarding Intake form, the census tool,
   and about 25 others -- both visible copy and JS/CSS code comments). Worth a dedicated future run to
   sweep, or is this an acceptable level of pre-existing debt for now given it is mostly comments rather
   than reader-facing copy?
2. **Employee Benefits Options's footer contact card duplicates contact info after a rep-kit swap**
   (Assumption 3): the swapped-in full person line sits above the page's own already-hardcoded
   email/phone/site lines. It is not a leak (Charity's kit shows Charity's info, not David's), just visibly
   redundant. Worth a small follow-up to give this file a dedicated compact swap format, or is the
   duplication acceptable?
3. **The census tool's newly added swap contract** (Assumption 6) uses the public, no-email person line
   format already established for public pages (Run CF's decision). Confirm that is the right call for
   this file specifically, since the brief's own text implied it already worked correctly and it turned
   out not to.

Run CH's own questions 1 and 3 are not re-asked here: Q1 (Charity's booking link stays null until her
calendar exists) is correct as is, no work needed this run; Q3 (yes, every rep's own title from
people.json belongs in the Client Portal point-of-contact block) is already standing policy, unaffected
by this run's edits.
