# BRIEF-GHL (current run: Run CJ, 2026-09-23). The P- prospecting templates: live audit, first-ever disk capture, and two known fixes.

Terminal name: GHL. Model: Sonnet 5. GoHighLevel browser only, at app.ridethehightide.com, in one tab,
with the tab visible. No questions mid run. No sends, no publishing a Draft workflow, no spending. Log
to `_BUILD-LOG/TERMINAL-GHL-live.md`, finish with `_BUILD-LOG/RUN-GHL-report.md`. No time limit. Commit
after each job (repo `~/Projects/atlas-one-intake-forms`). Screenshots to `_briefs/assets/run-CJ/`.

## Why this run exists

David asked to personally re-open and re-check the P- prospecting templates live in GHL, not trust
Run CH's 2026-09-23 spot check as still current, since other chats and terminals may have touched them
since. Cowork (this chat) tried to do that directly through its own browser tool first and hit a real
wall: the GHL Email Marketing Templates and Campaigns tabs at app.ridethehightide.com render inside a
cross origin iframe (email-home-prod.leadconnectorhq.com) that Cowork's browser extension cannot see or
click into at all. Confirmed three ways: the accessibility tree shows zero elements from that iframe,
network request logging shows zero requests to that domain, and every click and keyboard strategy tried
against the coordinates the parent page reports did nothing (including a control test on a button
outside the iframe, which worked fine). This matches BUILD-INDEX rule 18, GHL's builder canvases do not
accept input under cloud session Chrome automation; only the GHL terminal's Playwright browser with its
own persistent profile reaches this surface. So this run does the live re-check David asked for, with
the tool that actually works there.

Also found a real discrepancy pulling this brief together, worth knowing before this run starts: two
project docs disagree on how many P- templates exist. The 2026-09-08 build log and Run CH's own brief
both say 21. But `_BUILD-LOG/email-templates-map.md` lists 21 in its main table, then separately names
six more that Run BK (2026-09-17) found live and says "this table never listed": P-A-1, P-A-2,
P-BUILDER-DELIVERY, P-C-0 Instant reply, P-MEMBER-WELCOME, P-PAY-FAILED. That is 27 named templates
across that one file, not 21. Do not assume either number. Job 0 below gets the true live count and
names from the Email Builder API itself, the only source that cannot be stale.

## Job 0: establish the true live list

1. Call the live Email Builder API listing (the same call Run BK used to get the true id for P-B-2, and
   the same one Run CH used for its Job 27 live-vs-disk diff) and pull every template whose name starts
   with `P-`.
2. Compare that live list against the 27 names below (pulled from `_BUILD-LOG/email-templates-map.md`,
   ids as last recorded 2026-09-17). Note in the report: any name below no longer live, any live P-
   template not listed below, and the current id for every one, since ids drift (already documented for
   P-B-2: recorded id `6aa0a9de8b41b02dc82267ae`, live id `6aa0a9e10078269ef83ce1ac`).

| Template | id on record (2026-09-17) |
|---|---|
| P-A-1 Referral Email 1 | 6aa0a8409256eb9f6cb6b7b7 |
| P-A-2 Referral Email 2 | 6aa0a8ce62526e75c2c32cd7 |
| P-A-3 Referral Email 3 | 6aa0a9db9931e5f937c72b41 |
| P-B-1 Trigger Email 1 | 6aa0a9dc62526e75c2c33cf1 |
| P-B-2 Trigger Email 2 | 6aa0a9de8b41b02dc82267ae (live id 6aa0a9e10078269ef83ce1ac) |
| P-B-3 Trigger Email 3 | 6aa0a9e0357107c100ca0098 |
| P-B-4 Trigger close | 6aa0a9e113c848fe04dd0e6f |
| P-B-120 Renewal heads-up | 6aa0a9e3fce73710076f96e5 |
| P-B-60 Last window | 6aa0a9e455d1ce8973c140eb |
| P-C-0 Instant reply | 6aa0c1de55d1ce8973c2a813 |
| P-C-2 Inbound Email 2 | 6aa0a9e60078269ef83ce1e3 |
| P-C-3 Inbound Email 3 | 6aa0a9e82ac25123fb0d99aa |
| P-D-1 Cold Email 1 | 6aa0a9e9b2a4c1fa6304518a |
| P-D-2 Cold Email 2 | 6aa0a9eb8b41b02dc822682a |
| P-D-3 Cold Email 3 | 6aa0a9edfce73710076f9746 |
| P-D-4 Cold breakup | 6aa0a9ee9931e5f937c72c75 |
| P-E-0 Gracious close | 6aa0a9f00457161d4222f524 |
| P-E-4 Month four | 6aa0a9f12ac25123fb0d9a2b |
| P-E-Q1 Quarterly tool | 6aa0a9f3fce73710076f9784 |
| P-E-Q2 Quarterly law change | 6aa0a9f513c848fe04dd0f32 |
| P-E-Q3 Quarterly proof story | 6aa0a9f62ac25123fb0d9a5c |
| P-W7-1 WSA Email 1 | 6aa0a9f855d1ce8973c141a2 |
| P-W7-2 WSA Email 2 | 6aa0a9f955d1ce8973c141a8 |
| P-W7-3 WSA Email 3 | 6aa0a9fb6ec737a976fa481f |
| P-BUILDER-DELIVERY | 6aa370697919774ef2ed8f30 |
| P-MEMBER-WELCOME | 6aa37036a813792f409bf1a9 |
| P-PAY-FAILED | 6aa371c107aac9f9aa6a4e75 |

3. Save the reconciled list as `_BUILD-LOG/p-templates-map-2026-09-23.md` (name, live id, note) so it
   becomes the new source of truth for this family of templates, the same way Run CH's Job 0 fixed the
   orphan template's record.

## Job 1: capture every one to disk, for the first time

None of these have ever been saved to disk (per `ghl-cadence-link-cleanup-2026-09-22.md` and the
2026-09-08 build log). For each live P- template found in Job 0: open it, open the `</>` source dialog,
copy the current full HTML verbatim, save unmodified to `_BUILD-LOG/p-templates-2026-09-23/<slug>.html`
before touching anything. This becomes the master source file each of these should have had from the
start (rule 23, build the email as a file first, never compose only in the browser).

## Job 2: audit every captured file for three things

Same method Cowork used to find the 26 cadence email defect, applied fresh here since these are an
older, different build (single plain links rather than a branded button plus fallback line):

A. Raw URL or an unresolved merge tag as the visible link text, anywhere in the template, not only under
   a button.
B. "Here" or a three word or shorter fragment as link text (the project's standing link text rule).
C. A vendor or PEO brand name anywhere in the template, footer, signature or body. Client facing
   everything is Atlas One, never a vendor or PEO brand name. Run CH's 2026-09-23 spot check already
   found this exact defect in P-W7-3's signature ("PEO Partner & Business Consultant, Cornerstone PEO",
   a cornerstonepeo.com reply address). Check every other P- template's signature for the same pattern,
   not only P-W7-3; these were built in the same 2026-09-08 batch and may share it.

Log every file's result even when clean, for example "P-A-1: clean".

## Job 3: fix what Job 2 finds

Fix the disk copy first, then move to Job 4. Link text: keep the href, replace the visible text with a
short phrase describing where it goes, in the voice already used elsewhere in this template or the
nearest of the 26 already-fixed cadence files (examples already in use: "book a few minutes", "open the
quote form"). No dashes, no "here", no three word fragment. Vendor name: replace with Atlas One
branding only, name, title, an atlasonesolutions.com email, the current phone number (check the number
of record before typing it in, do not guess it) -- never a PEO or vendor brand name or their domain,
anywhere in the signature or body.

Two already-confirmed findings to fix, not re-investigate (Run CH already found these; this run only
needs to confirm they are still there and fix them, or confirm they are already fixed and move on,
per the standing rule to verify the live file yourself before changing anything):

- P-MEMBER-WELCOME: visible link text currently "grab a slot on my calendar here". Drop "here", keep
  the rest as the visible text, for example "grab a slot on my calendar".
- P-W7-3: signature currently reads "PEO Partner & Business Consultant, Cornerstone PEO" with a
  cornerstonepeo.com reply address. Rewrite to Atlas One only, matching the signature format already
  standard on a clean sibling template in this same batch (P-A-1 is confirmed clean, use its pattern).

If either one is already fixed by the time this run opens the live template, log "already fixed, no
change" and move on rather than redoing it.

## Job 4: paste every fix back to the live template

Rule 23 procedure (same as Run CH used): `</>` source dialog, select all existing content, delete,
paste the corrected file, save, close the dialog with Escape, then a full page reload (not just closing
the panel), read the saved body back to confirm the paste held. Screenshot each one.

## Job 5: verify every fixed template

Fetch each fixed template's live saved body back through the Email Builder API and diff whitespace
insensitively against the corrected disk file, the same method Run CH's Job 27 used. Report any real
content or link difference by name; GHL's own automatic Outlook-compatibility markup is expected and
harmless (already documented in Run CH's report).

## Report

For Job 0: the reconciled true count and list, anything added or dropped versus the 27 named above. For
every P- template found live: captured to disk (yes), Job 2 result (clean, or which of A/B/C), Job 3
fix applied or already-fixed, Job 5 verify result. Explicit confirmation, in plain words: is
P-MEMBER-WELCOME's "here" gone, is P-W7-3's vendor name gone. No sends, no workflow published or
unpublished, nothing deleted, at any point in this run.
