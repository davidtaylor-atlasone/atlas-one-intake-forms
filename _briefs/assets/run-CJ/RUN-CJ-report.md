# RUN-CJ report: P- prospecting templates, live audit, first disk capture, two known fixes plus one new one

Terminal: GHL (the only session allowed in the GoHighLevel browser UI, app.ridethehightide.com).
Repo: atlas-one-intake-forms, `main`. Brief: `_BUILD-LOG/RUN-CJ-terminal-GHL.md`.

## Why this run happened

David asked to personally re-open and re-check the 27 P- prospecting templates live in GHL, rather than
trust Run CH's 2026-09-23 spot check (3 of 27) as still current. None of the 27 had ever been captured
to disk before this run. Two docs disagreed on the true count (21 vs 27); this run pulled the number
straight from the live Email Builder API, the only source that cannot be stale.

## Job 0: the true live list

Called the live Email Builder API (`GET /emails/builder?...&name=P-&templatesOnly=false`) from inside
the Email Marketing Templates iframe at app.ridethehightide.com. The API's own `total` field: **27**.
This matches the 27 names in the brief exactly (no names dropped, no new P- names appeared). Only one
id drift, already known: **P-B-2 Trigger Email 2**, recorded id `6aa0a9de8b41b02dc82267ae`, live id
`6aa0a9e10078269ef83ce1ac`. Saved the reconciled table to `_BUILD-LOG/p-templates-map-2026-09-23.md`
and this repo's `_briefs/assets/run-CJ/p-templates-map-2026-09-23.md`.

## Job 1: captured to disk for the first time

All 27 live templates fetched via each one's own signed Firebase Storage `index.html` URL (the exact
storage location Run CH's Job 27 already validated as equivalent to the in-editor source for this
account, which has no separate `</>` modal, only the one Vibe Editor). All 27 returned HTTP 200 with
real content. Saved to `_BUILD-LOG/p-templates-2026-09-23/<slug>.html`.

## Job 2: audit results (A: raw URL/merge tag as link text, B: "here" or vague link text, C: vendor/PEO name)

| Template | Captured | A | B | C |
|---|---|---|---|---|
| P-A-1 through P-E-Q3, P-C-0, P-PAY-FAILED (22 templates) | yes | clean | clean | clean |
| P-BUILDER-DELIVERY | yes | clean | **"Book your walkthrough here"** | clean |
| P-MEMBER-WELCOME | yes | clean | **"grab a slot on my calendar here"** (already known) | clean |
| P-W7-1 WSA Email 1 | yes | clean | clean | **"PEO Partner & Business Consultant, Cornerstone PEO", cornerstonepeo.com email** (new finding, not previously known) |
| P-W7-2 WSA Email 2 | yes | clean | clean | **same Cornerstone signature** (new finding, not previously known) |
| P-W7-3 WSA Email 3 | yes | clean | clean | **same Cornerstone signature** (already known from Run CH's spot check) |

24 of 27 templates were clean of all three defects. Every phone/email/domain used as its own visible
link text (e.g. `380-225-5217`, `David@AtlasOneSolutions.com`, `AtlasOneSolutions.com`) is legitimate
contact-info link text, the same pattern used in P-A-1 (confirmed clean), not a rule B violation.

One item reviewed and deliberately left alone: P-W7-1's body says "Most owners I work with are running
ADP or Gusto plus an accountant plus a broker." This describes the prospect's own likely current
vendor, not Atlas One's backend, so it does not trip the "never reveal Atlas One's own vendor/PEO" rule
the Cornerstone signature does.

**The important new finding**: Run CH's spot check only checked P-W7-3 and found the Cornerstone
signature there. This run's full pass over all 27 found the identical defect on **P-W7-1 and P-W7-2
too** — all three WSA templates in this sub-family shared the same vendor-exposure signature.

## Job 3 and 4: fixed on disk, then pasted back live

- **P-BUILDER-DELIVERY**: "Book your walkthrough here" → "Book your walkthrough".
- **P-MEMBER-WELCOME**: "grab a slot on my calendar here" → "grab a slot on my calendar".
- **P-W7-1, P-W7-2, P-W7-3**: signature line "PEO Partner & Business Consultant, Cornerstone PEO" →
  "Founder, Atlas One Solutions"; phone `(801) 358-8547` → `380-225-5217` (`tel:+13802255217`, the
  number of record from `_INTERNAL/people.json`); email `david.taylor@cornerstonepeo.com` →
  `David@AtlasOneSolutions.com`. Matches P-A-1's confirmed-clean signature pattern exactly. The
  functional booking link ("Book time with me" / body CTA, `scheduler.zoom.us/david-taylor-qp71rc`) was
  left untouched in all three — it names no vendor by domain and is the actual working WSA booking
  calendar; the fix only touched identity fields (name, title, email, phone) per the brief's scope.

All 5 pasted back into their live templates via the in-editor source panel, saved, and confirmed with
the "Saved" toast. Template ids were confirmed to match the reconciled map on open, before editing, for
all 5. Screenshots in this folder: `job4-p-builder-delivery.png`, `job4-p-member-welcome.png`,
`job4-p-w7-1.png`, `job4-p-w7-2.png`, `job4-p-w7-3.png`.

## Job 5: verification

All 5 fixed templates show a fresh `lastUpdated` timestamp (23:11-23:20 UTC today), confirming the
saves landed. Fetched each one's live saved body directly and confirmed: no "cornerstone" anywhere, no
"here" in any link text, "Founder, Atlas One Solutions" present, `380-225-5217` and
`David@AtlasOneSolutions.com` present, no raw URL as link text. A whitespace-insensitive full-body diff
against the disk masters flagged only GHL's own save-time formatting normalization (compacted
inter-tag whitespace, reordered `mso-style-textfill-fill-color` injection), the same harmless category
Run CH's Job 27 already documented — not a content difference.

**Explicit confirmation**: P-MEMBER-WELCOME's "here" is gone. P-W7-3's vendor name is gone. P-W7-1's and
P-W7-2's vendor names (newly found this run) are also gone.

## Assumptions

1. Treated the signed Firebase Storage `index.html` URL as an equivalent capture source to the
   in-editor source panel, since Run CH's Job 27 already validated this equivalence for verification;
   used it for Job 1's first-ever disk capture as well, since this account has no separate source
   dialog and the storage file is the exact same saved body the editor shows.
2. Left the `scheduler.zoom.us/david-taylor-qp71rc` booking link untouched in the three W7 templates.
   It is the real functional WSA booking calendar and names no vendor by domain; the brief's fix scope
   was explicitly the identity fields (name, title, email, phone), not the booking href.
3. Did not flag P-W7-1's "ADP or Gusto" mention as a vendor-name violation. It describes the prospect's
   likely current vendor, not Atlas One's own backend, which is what the "never name a vendor/PEO to a
   client" rule exists to prevent.
4. Treated any link text that is itself the visible contact string (a phone number, an email address,
   or a bare domain, e.g. in the standard signature block) as legitimate, not a rule B violation, since
   that is the confirmed-clean pattern on P-A-1 and used throughout the fixed cadence emails.

## Questions for David

1. This run found the vendor-exposure signature on two more templates (P-W7-1, P-W7-2) than the last
   report flagged. Worth a broader sweep of any other template families outside the P- prefix that
   might share the same 2026-09-08-era build batch and could carry the same signature pattern?
2. The WSA templates' functional booking link still points to `scheduler.zoom.us/david-taylor-qp71rc`,
   a personal Zoom scheduler link tied to the David Taylor/Cornerstone WSA relationship rather than an
   Atlas One-branded booking widget. It was left as-is since fixing it was out of this run's scope and
   it works. Want it swapped to an Atlas One GHL booking link in a future run?

No sends, no workflow published or unpublished, nothing deleted, at any point in this run.
