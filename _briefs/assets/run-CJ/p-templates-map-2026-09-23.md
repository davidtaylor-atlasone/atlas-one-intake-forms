# P- prospecting templates: reconciled live map (Run CJ, 2026-09-23)

Source: live Email Builder API (`GET /emails/builder?...&name=P-&templatesOnly=false`), called from
inside the GHL Email Marketing Templates iframe (`email-home-prod.leadconnectorhq.com`) at
app.ridethehightide.com, the only surface that can reach it (see BRIEF-GHL.md). Total returned by the
API itself: **27**. This matches the 27 names listed in BRIEF-GHL.md exactly (which were themselves
pulled from `email-templates-map.md`'s main table plus the six templates Run BK found live on
2026-09-17 that table never listed). No name was dropped and no new P- name appeared.

The only drift found: **P-B-2 Trigger Email 2**, id on record `6aa0a9de8b41b02dc82267ae`, live id
**`6aa0a9e10078269ef83ce1ac`** (already documented, Run BK 2026-09-17). Every other id matched the
brief's table exactly, 26 for 26.

| Template | Live id | Note |
|---|---|---|
| P-A-1 Referral Email 1 | 6aa0a8409256eb9f6cb6b7b7 | matches record |
| P-A-2 Referral Email 2 | 6aa0a8ce62526e75c2c32cd7 | matches record |
| P-A-3 Referral Email 3 | 6aa0a9db9931e5f937c72b41 | matches record |
| P-B-1 Trigger Email 1 | 6aa0a9dc62526e75c2c33cf1 | matches record |
| P-B-2 Trigger Email 2 | 6aa0a9e10078269ef83ce1ac | **drift**, was 6aa0a9de8b41b02dc82267ae |
| P-B-3 Trigger Email 3 | 6aa0a9e0357107c100ca0098 | matches record |
| P-B-4 Trigger close | 6aa0a9e113c848fe04dd0e6f | matches record |
| P-B-120 Renewal heads-up | 6aa0a9e3fce73710076f96e5 | matches record |
| P-B-60 Last window | 6aa0a9e455d1ce8973c140eb | matches record |
| P-C-0 Instant reply | 6aa0c1de55d1ce8973c2a813 | matches record |
| P-C-2 Inbound Email 2 | 6aa0a9e60078269ef83ce1e3 | matches record |
| P-C-3 Inbound Email 3 | 6aa0a9e82ac25123fb0d99aa | matches record |
| P-D-1 Cold Email 1 | 6aa0a9e9b2a4c1fa6304518a | matches record |
| P-D-2 Cold Email 2 | 6aa0a9eb8b41b02dc822682a | matches record |
| P-D-3 Cold Email 3 | 6aa0a9edfce73710076f9746 | matches record |
| P-D-4 Cold breakup | 6aa0a9ee9931e5f937c72c75 | matches record |
| P-E-0 Gracious close | 6aa0a9f00457161d4222f524 | matches record |
| P-E-4 Month four | 6aa0a9f12ac25123fb0d9a2b | matches record |
| P-E-Q1 Quarterly tool | 6aa0a9f3fce73710076f9784 | matches record |
| P-E-Q2 Quarterly law change | 6aa0a9f513c848fe04dd0f32 | matches record |
| P-E-Q3 Quarterly proof story | 6aa0a9f62ac25123fb0d9a5c | matches record |
| P-W7-1 WSA Email 1 | 6aa0a9f855d1ce8973c141a2 | matches record |
| P-W7-2 WSA Email 2 | 6aa0a9f955d1ce8973c141a8 | matches record |
| P-W7-3 WSA Email 3 | 6aa0a9fb6ec737a976fa481f | matches record |
| P-BUILDER-DELIVERY | 6aa370697919774ef2ed8f30 | matches record |
| P-MEMBER-WELCOME | 6aa37036a813792f409bf1a9 | matches record |
| P-PAY-FAILED | 6aa371c107aac9f9aa6a4e75 | matches record |

This file is the new source of truth for this family of templates going forward, same role Run CH's
Job 0 gave the fixed orphan template's record.
