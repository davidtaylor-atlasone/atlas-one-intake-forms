# RUN-GHL report (Run AK, 2026-09-13)

Terminal: GHL (the only session allowed in the GoHighLevel browser UI). Brief: `BRIEF-GHL.md` (Run AK = finish
Part 4 with pre-built emails, then Part 1 item 3, then Run R), full text of `BRIEF-GHL-part4-resume.md` followed
for the cadence email pass. Hand-off mode was declared at the top of the brief, but every workflow open this run
loaded cleanly on a direct click (no FirebaseError, no dead UI), so after Part 0's one hand-off click to open
Post-Presentation Email, all further navigation (workflow-to-workflow, via the Workflows list search box) was done
directly with no hand-off needed and no dead-UI incidents.

## What was built / fixed

Read `_BUILD-LOG/cadence-emails-2026-09-13/INDEX.md` first as instructed. No template ids were present, so every
send used the paste path (source-code dialog), never "select existing template."

### Post-Presentation Email (id `304a9fa4-a256-4015-b767-031070f4186f`)
| Send | Path | Confirmed correct |
|---|---|---|
| Email 1 | replace whole body | Yes -- rendered preview matches file |
| Email 2 | replace whole body | Yes |
| Email 4 - Re-engage (see Assumption 1) | wrapper only (footer lines added) | Yes |
| LT-1 | replace whole body | Yes |
| LT-2 | replace whole body | Yes |
| The $70,000 audit (construction, LT-2 slot) | wrapper only (footer lines added) | Yes |
| LT-3 | wrapper only (footer lines added) | Yes |
| LT-4 | replace whole body | Yes |
| LT-5 | replace whole body | Yes |

From Name (`David Taylor, Atlas One Solutions`) / From Email (`david@atlasonesolutions.com`) set on every one of
the above (Email 1/2 already had it from Run AG; the rest were missing it or had it in a different form and were
fixed).

### Call: not now (id `ff950be3-829d-4a51-8f9a-825db660796e`)
| Send | Path | Confirmed correct |
|---|---|---|
| E0 (Email: thanks for the time) | replace whole body | Yes |
| 45-A | replace whole body | Yes |
| 45-B | wrapper only (footer lines added) | Yes |
| The $70,000 audit (construction, second instance, 45-B slot) | wrapper only (footer lines added) | Yes |
| 45-C | wrapper only (footer lines added) | Yes |

### Seasonal touches 2026-27 (id `52f414cb-b63e-4425-80c9-adea42a210e3`)
| Send | Path | Confirmed correct |
|---|---|---|
| YE-1 | replace whole body (see Assumption 2) | Yes |
| YE-2 | wrapper only (footer lines added) | Yes |
| YE-3 | wrapper only (footer lines added) | Yes |
| YE-4 | wrapper only (footer lines added) | Yes |
| Q-1 (all 3 occurrences: fires 2027-03-01, 2027-06-01, 2027-09-01) | wrapper only, body untouched (see
Assumption 3) | Yes |

All sends above were verified by reopening the action after saving and reading the rendered preview (not raw
source) -- signature block, both grey footer lines, tagline, and address line all present and correctly formatted
on every send. Screenshots for a representative sample are in `_briefs/assets/run-AK/shots/`.

## Assumptions

1. **INDEX.md assumed two placeholder sends in Post-Presentation Email (Email 3, Email 4). Only one exists live**,
   named "Email 4 - Re-engage" (subject: "Should I keep your quote open, {{contact.first_name}}?"), positioned
   after Wait 3 days > Email 2 > Wait 4 days > "Still not moved?" gate > "Has intake-received?" gate. There is no
   separate "Email 3" node anywhere in this workflow. Treated this single node as the one wrapper-only placeholder
   in this position (covering whatever INDEX.md called Email 3 and/or Email 4), left its real subject and body
   untouched, only added the two missing footer lines.
2. **YE-1 was fully body-replaced rather than wrapper-only** as INDEX.md's mode column suggested. The live body had
   a leftover "My calendar is open here" text link (the exact thing the global no-"here"-links rule targets) where
   `ye-1.html` already has the corrected version with a real button. Since the file's body was the corrected
   version and not a substance change, did a full paste rather than a partial wrapper edit.
3. **Q-1's live body was NOT actually reworded per the global "here" rule**, contradicting INDEX.md's claim ("with
   'here' link text reworded per global rule"). All 3 occurrences still read "See the calculator here" / "Take the
   assessment here", plus an odd extra line "Fifteen minutes here" linking to a different booking widget URL
   (`atlas-one-15-minute-intro-call-hoswp`) than the standard `book-david` widget used everywhere else. Per the
   mode's explicit instruction ("wrapper only, body copy unchanged"), left the body exactly as found and did not
   correct the "here" links or the stray booking-widget line -- flagging both for a future run's global link pass.
4. **The Long Tail loop (LT-1 through LT-5, 45-A/B/C, and the construction-audit send) all live inside
   Post-Presentation Email and Call: not now**, not in a separate "Call: not now (Long Tail loop)" or "Call: not
   now (45 day pass)" workflow as INDEX.md's Workflow column implied. Confirmed by opening each node directly;
   there is no third workflow by either of those names in the account.
5. **"Books: after the call" and "Books: quarter and year end" do not exist.** Searched the Workflows list for
   "Books" (0 results) and "after the call" (only the pre-existing, unrelated "Booking: after the call" booking-
   confirmation workflow, Draft, 0 enrolled). An earlier line in this run's live log incorrectly assumed the Books
   workflow was already built, based on misreading "Booking: after the call" in the workflows list at the very
   start of the run -- that assumption is wrong and is corrected here.

## Not attempted this run

- **B-1 through B-4, BQ-1, BYE-1, BYE-2** (`_BUILD-LOG/cadence-emails-2026-09-13/b-1.html` through `bye-2.html`):
  cannot be pasted anywhere because the two workflows that would hold them ("Books: after the call", "Books:
  quarter and year end") do not exist yet. Building them from scratch (trigger, wait/condition/tag scaffolding
  matching the pattern of the workflows fixed this run, then 7 paste-path email sends, then the two scheduling
  offsets from Run AI Job 2 -- BQ-1 one day after each Q-1 date, BYE-1 on 2026-11-02) is a new-build task, not a
  content fix, and was not started.
- **Run X Part 1 item 3** (duplicate the remaining chain into every construction dead end in both workflows):
  confirmed again this run that the construction branch pattern recurs at multiple gates (found and fixed the
  wrapper on 2 separate "$70,000 audit" instances, one in each workflow, at different positions in the LT/45-day
  chains) but did not do the node-by-node duplication work itself.
- **Run R** (`_briefs/RUN-A-batch-2026-09-12.md`: forms C1/C2, two intake workflows, `GHL_BUILD_FORM` repo edit):
  not attempted. Did not test the Sites > Forms click first as the brief's fast-fail check requires.
- **Part 4.4 test send** (contact `david+zzak1@atlasonesolutions.com` / `david+zzad1@...` per the two brief
  versions, trigger Email 1 and E0, screenshot both, delete contact): not attempted.

## Questions for David

1. Do you want a "Books: after the call" / "Books: quarter and year end" build to happen in the next run, using
   the same wait/condition/tag pattern as Post-Presentation Email and Call: not now? The 7 email HTML files are
   already finished and waiting in `cadence-emails-2026-09-13/`.
2. For Q-1: should the "here" links (calculator, assessment) actually get reworded per the global link rule now,
   and should the stray "Fifteen minutes here" line (pointing at a different booking widget than the rest of the
   account) be removed or fixed? INDEX.md assumed this was already done; it was not.
3. For Post-Presentation Email's "Email 4 - Re-engage": is this meant to be the only trailing email after Email 2
   (i.e., was "Email 3" ever built and later merged/removed), or should a genuine second placeholder ("Email 3")
   be added back in before it?
