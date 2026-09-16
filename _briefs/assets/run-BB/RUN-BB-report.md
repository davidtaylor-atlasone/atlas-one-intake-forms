# RUN-BB report (2026-09-16)

Terminal: GHL (ghl-browser only). Parts done: 12 (verticals), 13a-13d (template switches + YE-1 build + subject
fix + real test), 14 (logo hosting).

## Part 12: Vertical field options + fallback fix

**12a.** Settings > Custom Fields > Prospecting > Vertical (`contact.vertical`, Dropdown single). Existing 7
options untouched: Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional
Services, Other. Added 13 new options exactly as specified in the brief: Construction and trades, Restaurants
and hospitality, Professional services (law, accounting, agencies), Manufacturing and industrial, Retail and
e-commerce, Home services, Medical practices (non dental), Behavioral health and treatment centers, Veterinary,
Technology and software, Transportation and logistics, Real estate and property management, Nonprofit. Skipped
a 14th "Other" (already exists) — see Assumptions #1.

Verification: after save + full reload, reopened the field editor and confirmed all 20 options present (had to
work around a canvas-virtualization false alarm — see Assumptions #6).

**12b.** The "seven Contact Created vertical-lane trigger workflows" the brief describes turned out to be ONE
workflow, "W0 Set vertical lines" (`de389546-ad9f-42a2-9784-bc231014c8a0`, Draft/unpublished, left unpublished),
with 7 trigger nodes (one per named vertical, plus one on Vertical changed) feeding a single "Route by vertical"
If/Else. Confirmed the bug the brief was worried about: the None/Else branch (covers "Other", blank, and now
all 13 new verticals) went straight to END with **no action** — Vertical Opener/Proof/Tool would stay blank for
any contact whose vertical isn't one of the 6 named branches.

Fix: added an "Update contact field" action named "Set generic lines" on the None branch, setting:
- Vertical Opener: "I work with owners who run payroll, benefits, workers' comp and bookkeeping across four or
  five vendors. I put it under one relationship with one number to call, and most of it costs you nothing extra
  because the vendors pay me."
- Vertical Proof: "One owner was paying five separate vendors for payroll, comp and benefits. The Audit found
  the overlap, fixed the comp classification, and gave the owner hours back every week on top of what it saved."
- Vertical Tool: "Vendor Consolidation calculator: https://forms.atlasonesolutions.com/tools/vendor-consolidation/"

(Text taken verbatim from `Atlas_One_GHL_Prospecting_Workflows_BUILD_SHEET.md` Appendix A, "Other (the Else
branch, generic)" — this was always the intended generic fallback, it had just never been built.)

Saved action, saved workflow, full reload, reopened the action and confirmed all three field values persisted.
Publish toggle untouched (still Draft, matching how it was before this run).

## Part 13: template switches, new YE-1 branch, subject fix, real test

**13a. "Post-Presentation Email" (`304a9fa4-a256-4015-b767-031070f4186f`).** Switched every remaining Quick
Compose send to its template, subject set from `email-templates-map.md`:
- LT-1 (1 copy, general branch) → `A1 | LT-1 | lt-1`
- LT-2 (1 copy, general branch; the construction-branch copy "The $70,000 audit (construction, LT-2)" left on
  Quick Compose per the brief) → `A1 | LT-2 | lt-2`
- LT-3 (2 copies: general + construction branch) → `A1 | LT-3 | lt-3` on both
- LT-4 (2 copies: general + construction branch) → `A1 | LT-4 | lt-4` on both
- LT-5 (1 copy only; the construction branch does not reach LT-5, it ends earlier) → `A1 | LT-5 | lt-5`

Left "Email 4 - Re-engage" (a placeholder send, no map entry, per INDEX.md) untouched. No "Changing template?"
modal appeared on any of these since they were first-time Quick-Compose-to-Template conversions. Saved every
action, saved the workflow, full reload, reopened LT-1 and confirmed the real template body renders (A1
branded, DM Sans, vendor-consolidation copy, correct link).

**13b. "Seasonal touches 2026-27" (`52f414cb-b63e-4425-80c9-adea42a210e3`).**
- BQ-1 (fires 2027-03-02) → `A1 | BQ-1 | bq-1`
- BQ-1 #2 (fires 2027-06-02) → `A1 | BQ-1 | bq-1`
- BYE-1 (fires 2026-11-02) → `A1 | BYE-1 | bye-1`
- BYE-2 (fires 2027-01-05) → `A1 | BYE-2 | bye-2`

Finding for David: the quarterly BQ-1 chain only has 2 real Send Email copies even though Q-1 fires 3x/year and
a "Wait until 2027-09-01 (BQ-1 #3)" node exists — its Condition/Suppressed/None branches lead straight through
with **no BQ-1 #3 send ever built**. I did not build a fix; the brief only asked me to switch the existing
BQ-1/BYE-1/BYE-2 sends to templates, not build a missing 3rd occurrence (unlike Part 12's explicit
fallback-building instruction). See Questions #1.

Built the new YE-1 branch, inserted directly before the YE-3 wait node (YE-2 does not exist as a built node in
this workflow at all — confirmed by search — so "before YE-2" was read as "before the next real node," YE-3):
- Wait action "Wait until 2027-01-01 09:00 (YE-1)": Until a specific date/time, 01/01/2027 09:00:00 AM, "On this
  date and time," "Skip all outbound communication actions till next wait or event start date action" (matches
  the exact pattern used by the adjacent YE-3/YE-4/BYE-1/BYE-2 waits). Could not find any contact-timezone
  control anywhere in this wait-action UI — see Questions #2.
- Send Email "YE-1" right after: template `A1 | YE-1 | ye-1`, subject "January 1 is the easiest start date of
  the year," From Name "David Taylor, Atlas One Solutions," From Email david@atlasonesolutions.com.

Saved both actions, saved the workflow, full reload. Verification note: this workflow's canvas virtualizes/culls
nodes far from the viewport even at "Fit to Screen" (see Assumptions #6) so the new nodes never rendered on
screen after reload no matter how I panned/zoomed, but a DOM query for edges confirmed an edge referencing the
new Send Email node's internal ID still exists after reload — strong evidence the graph data (not just the
render) persisted. Recommend David open this workflow and scroll to right before YE-3 to eyeball the new
branch. Publish toggle and the workflow list's "Published" status both left untouched.

**13c. "Won - Pay Referral Partner" (`548ca35e-07e8-435b-8d37-150fada4f705`), Email 7 - Setup checklist.**
Subject changed from `Setup checklist for {{contact.company_name}}` to
`Setup checklist for {{contact.legal_business_name}}`. Saved action, saved workflow. Also updated
`_BUILD-LOG/email-templates-map.md` and `_BUILD-LOG/cadence-emails-2026-09-13/INDEX.md` (Email 7 rows) so the
map/index carry the fixed subject.

**13d. Real end-to-end test of the new-client-welcome template.** Created contact "Test ZZBB",
david+zzbb@atlasonesolutions.com, phone (385) 555-0299 (unique), tag `send-peo-form` added at creation. The
"Send PEO form on tag" workflow fired within under a minute: contact tagged `form-a-sent`, email delivered with
subject "Thank you, and the one link that gets your business set up" from "David Taylor, Atlas One Solutions."
Opened and read the full rendered body: A1 Solutions logo present, DM Sans body, generic "Hi Test," greeting (no
Dr. Gould / dental-specific language survived from the original acquisition-specific draft), the four links
(PEO form, census tool, what-we-do page, book-time) intact. Matches the new-client-welcome template built in
Run BA Part 11. Deleted the test contact afterward (soft delete, GHL's 60-day recovery window, confirmed by
typing DELETE).

## Part 14: logo hosting

Found the exact logo currently referenced in the cadence email wrapper (`send-peo-form.html` and others):
`https://storage.googleapis.com/highlevel-backend.appspot.com/location/AzTPxnK2vSUj19jYoDmR/form/Cxqawj85qg4ULUl64nMc/header-image/923a20f4-ffe6-4528-8245-d2f698889c5e.png`
— a 900x402 PNG, the full "A1 Solutions" horizontal lockup. I downloaded and inspected this file rather than
guessing from the Master Kit brand-kit folder, since the brand kit's separate "Logo Mark" assets are a different,
portrait-oriented icon-only image that would not match what is actually live in the sent emails (see Assumptions
#5). Committed that exact file into the `atlas-one-intake-forms` repo at `assets/email/logo-mark.png` (commit
`acc4384`, pushed to `origin/main`) so it now serves at:

**https://forms.atlasonesolutions.com/assets/email/logo-mark.png**

Confirmed after the GitHub Pages redeploy: HTTP 200, `content-type: image/png`, `content-length: 26800`. This is
a pure hosting-location change — the bytes are pixel-identical to the current GHL asset, so nothing should look
different once a template's `<img src>` is repointed. Per the brief, did **not** re-push any of the 35 email
templates this run; GHL-JOBS will swap the `<img src>` in its own source files and re-fill the templates.

## Assumptions

1. Part 12a: skipped adding a 14th "Other" option to the Vertical field since one of the 7 existing options was
   already literally "Other" — adding a second option with the same label would create an ambiguous duplicate
   value with no way to tell them apart on a contact record.
2. Part 13b: read "before YE-2" as "before the next node that actually exists" (YE-3), since YE-2 has never been
   built in this workflow (confirmed by text search finding zero matches for "2026-11-15" or a YE-2 node before
   building).
3. Part 13b: did not build a fix for the missing BQ-1 #3 send since the brief's ask for this workflow was
   specifically "switch BQ-1, BYE-1, BYE-2 to their templates," not "audit and complete the quarterly chain" —
   flagged it as a finding/question instead of guessing at scope.
4. Part 13b: the new YE-1 wait uses the same "no explicit timezone" pattern as every adjacent wait node (YE-3,
   YE-4, BYE-1, BYE-2), since this workflow-builder version's Wait action UI has no per-wait timezone selector
   anywhere I could find (checked the "..." menu next to the time field: it only offers Standard vs Dynamic date
   entry). Treating "match the existing pattern" as correct until told otherwise.
5. Part 14: used the exact PNG currently live in GHL's hosted forms (900x402, full horizontal lockup) rather
   than any file from the Master Kit's `A1_Final Brand/1. Logos/Logo Mark/` folder, because those are a
   different, portrait icon-only asset (908x1294) that does not match what recipients have actually been seeing
   in delivered mail. Verified this by downloading the live GHL URL and inspecting its dimensions before
   deciding, rather than guessing from the brand-kit folder name.
6. General (Parts 12b, 13a, 13b): this GHL account's workflow canvas (Vue Flow) virtualizes/culls nodes that are
   far from the current viewport, even when "Fit to Screen" is used at very low zoom on a tall workflow. Several
   times a node I had just built or was looking for appeared to be "missing" after a reload purely because it
   wasn't rendered, not because the save failed (confirmed in two cases: Part 12's field-options false alarm via
   a "Duplicate label" validation error, and Part 13b's YE-1 branch via a DOM query for the edge referencing its
   ID). Recorded this pattern so future runs don't waste time chasing the same false alarm.

## Questions for David

1. The BQ-1 quarterly chain in "Seasonal touches 2026-27" only sends BQ-1 and BQ-1 #2 (March and June), even
   though Q-1 fires a third time (September) and a "Wait until 2027-09-01 (BQ-1 #3)" node already exists with no
   send behind it. Want a BQ-1 #3 Send Email built (same template, `A1 | BQ-1 | bq-1`) to complete the pattern?
2. I could not find a contact-timezone selector anywhere in this workflow version's Wait action UI (for the new
   YE-1 wait or any of the existing YE-3/YE-4/BYE-1/BYE-2 waits either). Is that expected on this GHL plan, or is
   there a timezone setting I'm missing that should be applied?
3. The email-logo hosting change (Part 14) only moves the file to our own domain — it doesn't touch any live
   template's `<img src>` yet. Confirm GHL-JOBS should be the one to swap the `src` and re-push the 35 templates,
   as the brief said, rather than this terminal doing it in a follow-up run.
