# RUN-GHL-JOBS report (Run AI, 2026-09-13): make the GHL email pass cheap

Brief: `<Master_Kit>/_BUILD-LOG/BRIEF-GHL-JOBS.md`, copied to `repo:_briefs/BRIEF-GHL-JOBS-2026-09-13-RunAI.md`.
Live log: `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`.

All four jobs done. A duplicate general-purpose agent was found mid-run independently working the same brief in
this session (its origin is unclear; possibly the `run-ghl-jobs` skill's own background execution path). It was
told to stand down before it wrote anything to the Master Kit that this run had not already produced or reviewed;
its research file (`repo:_briefs/RUN-AI-job2-source-content.md`) and its draft of Job 4's resume brief were folded
in after being checked against the underlying source reports myself, not trusted verbatim.

## Job 1: the standard signature block

Rebuilt in `12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`, in the wrapper's signature section: logo mark (44px),
David Taylor / Founder, Atlas One Solutions / phone / email / website / book link, the "ONE CALL SOLVES EVERYTHING"
tagline, then the two new grey (`#9AA3B2`) footer lines:
- "Vendor neutral. I quote several providers, show them side by side, and you choose. You never pay for anything you do not need."
- "Payroll, benefits, insurance, bookkeeping, software, IT and the paperwork in between. See everything Atlas One handles: **one page, no form**." (linked to `https://forms.atlasonesolutions.com/tools/what-we-do/`)

then the existing "Atlas One Solutions LLC, Lehi, Utah" address line. Marked in the doc as THE standard; E0 will be
updated to match it (not the other way round) the next time the GHL terminal touches that workflow.

## Job 2: one finished HTML file per send

`_BUILD-LOG/cadence-emails-2026-09-13/` (26 files + `INDEX.md`), copied to `repo:_briefs/assets/run-AI/cadence-emails/`.
Screenshots at 390px in `repo:_briefs/assets/run-AI/shots/`.

Breakdown:
- **19 full replacements** ("replace whole body" in INDEX.md): Email 1, Email 2, E0, LT-1, LT-2, LT-4, LT-5, 45-A
  (verbatim from RUN-AD-GHL.md 4.2, including Email 1's five sourcing bullets read back from RUN-GHL-report.md),
  and the seven bookkeeping sends B-1 through BYE-2 (from `A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md`,
  with this run's three decisions applied: cut B-1's guarantee paragraph; kept the per employee payroll price
  unchanged; added "plans start under a few hundred a month; the call sets the number" to B-1, since **no**
  $300 to $3,000 range existed anywhere in the current draft to remove, so this decision was a no-op on the removal
  half, addition-only; moved BQ-1 to fire one day after each Q-1 date; moved BYE-1 to 2026-11-02).
- **4 wrapper-only, confirmed-live body copy** (Q-1, YE-1, YE-3, LT-3): found in `RUN-P-cadence.md`, then corrected
  against `RUN-Q-report.md` and `RUN-A-batch-2026-09-12.md` (the more recent, authoritative build log), which
  revealed the original seasonal-touch date plan changed during Run Q/the Sept 12 batch: **YE-3 fires alone on
  2026-12-01** (not combined with a Q-1 send that day as `RUN-P-cadence.md` first planned), and **Q-1 only fires
  three times, 2027-03-01/06-01/09-01** (no 2026-12-01 occurrence). Global rules applied: converted bare URLs to
  the button pattern, and reworded every "here" link ("See the calculator here" to "See the calculator", "grab ten
  minutes here" to "grab ten minutes") per the no-"here"-links rule, since the live copy predates that rule.
- **7 keep-as-is placeholders**: Email 3, Email 4, 45-B, 45-C, the construction audit email, YE-2, YE-4. No report
  anywhere records these bodies verbatim (Email 3/4: never documented at all; 45-B/45-C/construction audit: only
  described by theme in `RUN-Q-report.md` items 3/5/7, never quoted; YE-2/YE-4: `RUN-P-cadence.md` left these two
  for whoever built the workflow to write, and no later report confirms what was actually saved). Each file carries
  `<!-- BODY: READ FROM GHL, keep as is -->` plus a note on what is known about the body's theme, so the GHL
  terminal wraps the existing body rather than inventing or guessing replacement copy.

All 26 files render clean: `scrollWidth` 390 at a 390px viewport, 0 console errors, 0 dashes (checked by script,
not by eye alone). One overflow bug was caught and fixed: the plain-text fallback link under each button (for
images-off readers) did not wrap long booking URLs, pushing `scrollWidth` to 411 to 423px on six files; fixed with
`word-break:break-all;overflow-wrap:break-word` on that paragraph and its link.

## Job 3: GHL Email Builder API, stopped per the brief

Used the Private Integration token from `~/Projects/atlas-one-portal/.env` (`GHL_PRIVATE_INTEGRATION_TOKEN`,
location `AzTPxnK2vSUj19jYoDmR`). Both endpoints returned an auth error before touching any template:

```
GET https://services.leadconnectorhq.com/emails/builder?locationId=AzTPxnK2vSUj19jYoDmR
-> HTTP 401 {"statusCode":401,"message":"The token is not authorized for this scope."}

POST https://services.leadconnectorhq.com/emails/builder  (body: {"locationId":"...","name":"A1 TEST delete me"})
-> HTTP 401 {"statusCode":401,"message":"The token is not authorized for this scope."}
```

No test template was created (the 401 fires before any processing), so there is nothing to delete. The token is
valid (a bad/expired token returns a different error), it is simply missing the Email Builder scopes. **What David
needs to click:** Settings > Integrations > Private Integrations, open the integration this token belongs to
(named for the portal, in location Atlas One Solutions), and add the two scopes `emails/builder.readonly` and
`emails/builder.write` to its scope list, then save (this issues the same token with expanded scope; no new token
needed on the portal side). Once added, Job 2's 26 files are ready to push through the API in one pass instead of
one paste per send.

## Job 4: `_BUILD-LOG/BRIEF-GHL-part4-resume.md`

Written (the duplicate agent's draft, reviewed and one correction made: it originally stated Email 1/2's Run AG
signature was "confirmed to match" the new Job 1 standard; corrected to say it was only assumed consistent, since
Run AG's own report never actually opened E0 to check byte for byte). Covers: the paste-path vs placeholder-path
per send, the order of operations across all four workflows, the two BQ-1/BYE-1 scheduling notes, the test send,
Run X Part 1 item 3, and Run R, with `/compact` checkpoints between sections. Copied to `repo:_briefs/assets/run-AI/`.

## Assumptions

1. **B-1's "$300 to $3,000 plan range."** The brief's Job 2 instructed removing this range and replacing it with
   "plans start under a few hundred a month; the call sets the number." No such range exists anywhere in the
   current B-1 draft (`A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md`) to remove; only the
   per-employee payroll figures are present. Added the replacement sentence anyway since it reads naturally next to
   the payroll pricing and the brief clearly wants that framing present, but nothing was actually removed.
2. **Q-1/YE-1/YE-3/LT-3 body copy is the CONFIRMED live version**, not the original draft in `RUN-P-cadence.md`,
   because `RUN-Q-report.md` and `RUN-A-batch-2026-09-12.md` (both later) record specific edits made on top of that
   draft (added lines, a typo fix, a corrected date plan). Used the later, more authoritative source.
3. **YE-2 and YE-4 were NOT treated as "confirmed live"** even though `RUN-P-cadence.md` contains draft body text
   for both, because that file explicitly left them for "whoever builds it" to write, and no later report confirms
   what was actually typed and saved. Marked as keep-as-is placeholders rather than risk overwriting real live copy
   with an unconfirmed draft.
4. **YE-1 and YE-3 got a button added** where the live copy (per the reports) had no link or button at all, since
   the global rule requires a primary CTA button on every send. Used the generic `Book a few minutes` / `Book
   fifteen minutes` pattern already used elsewhere rather than inventing new copy.
5. **The duplicate agent.** A second `general-purpose` agent (`abf3a6f1b0f7871bc`) was running the same brief in
   this session in parallel, discovered via `ListAgents` partway through Job 2. Sent it a stop message; it had
   already written two files to the repo/Master Kit before that message was delivered (its research file, and Job
   4's resume brief) but had not touched the `cadence-emails-2026-09-13/` folder or made any commits. Both of its
   files were reviewed against source material before being kept; nothing from it was used un-verified.

## Skipped / not applicable

Nothing skipped. Job 3 stopped by design once the scope gap was confirmed, per the brief's own instruction.

## Questions for David

1. **GHL Email Builder scopes.** Add `emails/builder.readonly` and `emails/builder.write` to the Private
   Integration token's scope list (Settings > Integrations > Private Integrations) if you want future cadence
   sends pushed through the API instead of pasted by hand. No other action needed on the portal side.
2. **The 7 placeholder sends** (Email 3, Email 4, 45-B, 45-C, the construction audit email, YE-2, YE-4) have never
   been recorded verbatim anywhere in this project's history. When the GHL terminal next opens each one, its
   actual body becomes the first real record of it; worth having that terminal paste each one's final body back
   into a report once confirmed, so this gap does not recur.
3. **B-1's pricing sentence** ("plans start under a few hundred a month; the call sets the number") was added on
   the assumption that this is what the brief wanted even though there was no existing range to remove (Assumption
   1). Confirm this sentence is accurate before it goes live; the per-employee payroll prices next to it are firm,
   but "a few hundred a month" for the plan itself was not independently sourced from the client-facing sheet for
   this run.
4. **BQ-1 and BYE-1's new dates** (BQ-1 one day after each Q-1 date: 2027-03-02/06-02/09-02; BYE-1 moved to
   2026-11-02) assume the seasonal-touch schedule confirmed in `RUN-A-batch-2026-09-12.md` (Q-1 only fires three
   times, not four; YE-3 alone on 2026-12-01) is still what is actually live in GHL. If a later session changed
   those dates again, BQ-1/BYE-1's placement needs re-checking before the bookkeeping cadence is built.
