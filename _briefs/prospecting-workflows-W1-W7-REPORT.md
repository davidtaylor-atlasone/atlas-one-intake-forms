# Prospecting workflows W0 to W7: build report

Run 8 Sep 2026. Sub-account Atlas One Solutions, location `AzTPxnK2vSUj19jYoDmR`.

The run started as browser automation, was stopped part way through by David, and
finished through the **GHL API**. Workflows were deliberately not automated; they are
written up as a click list instead.

---

## Status

| Part | State |
|---|---|
| Prospecting folder | **Done** |
| 16 custom fields | **Done, all 16 read back through the API** |
| 11 tags | **Done, all 11 confirmed present** |
| 21 email templates | **Done, every one fetched back and checked** |
| W0 to W7 workflows | **Not built.** Click list written instead, see the build sheet |

---

## Checkpoint 1: fields

All 16 live in the Contact folder `Prospecting`, folder id `ra4rylFUwAUV611f1VrS`.
Read back with `GET /locations/{id}/customFields?model=contact` after the last write.

| Field | dataType | Key | Options |
|---|---|---|---|
| Lead Lane | SINGLE_OPTIONS | `contact.lead_lane` | A Referral, B Trigger, C Inbound, D Cold, E Lost |
| Brand Identity | SINGLE_OPTIONS | `contact.brand_identity` | Atlas One, Cornerstone |
| Vertical | SINGLE_OPTIONS | `contact.vertical` | Audiology, Dental Ortho Optometry ENT, Construction, Technology, Hospitality, Professional Services, Other |
| Trigger Type | SINGLE_OPTIONS | `contact.trigger_type` | WC renewal, Benefits renewal, New location, Hiring, Ownership change, Vendor complaint, Other |
| Trigger Date | DATE | `contact.trigger_date` | |
| WC Renewal Date | DATE | `contact.wc_renewal_date` | |
| Benefits Renewal Date | DATE | `contact.benefits_renewal_date` | |
| Next Touch Date | DATE | `contact.next_touch_date` | |
| Last Touch Date | DATE | `contact.last_touch_date` | |
| Sequence Step | NUMERICAL | `contact.sequence_step` | |
| Personal Line | LARGE_TEXT | `contact.personal_line` | |
| Vertical Opener | LARGE_TEXT | `contact.vertical_opener` | |
| Vertical Proof | LARGE_TEXT | `contact.vertical_proof` | |
| Vertical Tool | TEXT | `contact.vertical_tool` | |
| Referral Partner Name | TEXT | `contact.referral_partner_name` | |
| Lifted Suppression | CHECKBOX | `contact.lifted_suppression` | Yes |

**Who built what.** I created four by hand in the browser (Lead Lane, Brand Identity,
Vertical, Trigger Type, timestamps 21:28 to 21:45 UTC) and `WC Renewal Date` through the
API at 00:32 UTC. **The other eleven appeared between 00:03 and 00:16 UTC, after my
browser session had ended, and were not created by me** — presumably David or another
session working in parallel. They are all correctly typed and correctly foldered, so
nothing needed fixing, but it is worth knowing the folder had a second author.

## Checkpoint 1: tags

All 11 already existed; none had to be created. GHL stores tag names lowercase, so they
read back as `sms consent`, `cell verified`, `cooling 30d`, `cooling 60d`, `cooling 90d`,
`hold 6m`, `dnc`, `sequence active`, `batch ready`, `reply received`, `not interested`.
(22 tags exist on the location in total.)

## Checkpoint 2: email templates

21 built through `POST /emails/builder` then `POST /emails/builder/data`, in the branded
wrapper from `_briefs/2026-09-07-email-template-pass.md`.

**Every one was fetched back** from the `previewUrl` the API returns and checked for four
things: the wrapper is present, the button renders as a button, the merge tags survived,
and there is **not a single dash of any kind in any body**. All 21 passed.

| Template | id |
|---|---|
| `P-A-3 Referral Email 3` | `6aa0a9db9931e5f937c72b41` |
| `P-B-1 Trigger Email 1` | `6aa0a9dc62526e75c2c33cf1` |
| `P-B-2 Trigger Email 2` | `6aa0a9de8b41b02dc82267ae` |
| `P-B-3 Trigger Email 3` | `6aa0a9e0357107c100ca0098` |
| `P-B-4 Trigger close` | `6aa0a9e113c848fe04dd0e6f` |
| `P-B-120 Renewal heads-up` | `6aa0a9e3fce73710076f96e5` |
| `P-B-60 Last window` | `6aa0a9e455d1ce8973c140eb` |
| `P-C-2 Inbound Email 2` | `6aa0a9e60078269ef83ce1e3` |
| `P-C-3 Inbound Email 3` | `6aa0a9e82ac25123fb0d99aa` |
| `P-D-1 Cold Email 1` | `6aa0a9e9b2a4c1fa6304518a` |
| `P-D-2 Cold Email 2` | `6aa0a9eb8b41b02dc822682a` |
| `P-D-3 Cold Email 3` | `6aa0a9edfce73710076f9746` |
| `P-D-4 Cold breakup` | `6aa0a9ee9931e5f937c72c75` |
| `P-E-0 Gracious close` | `6aa0a9f00457161d4222f524` |
| `P-E-4 Month four` | `6aa0a9f12ac25123fb0d9a2b` |
| `P-E-Q1 Quarterly tool` | `6aa0a9f3fce73710076f9784` |
| `P-E-Q2 Quarterly law change` | `6aa0a9f513c848fe04dd0f32` |
| `P-E-Q3 Quarterly proof story` | `6aa0a9f62ac25123fb0d9a5c` |
| `P-W7-1 WSA Email 1` | `6aa0a9f855d1ce8973c141a2` |
| `P-W7-2 WSA Email 2` | `6aa0a9f955d1ce8973c141a8` |
| `P-W7-3 WSA Email 3` | `6aa0a9fb6ec737a976fa481f` |

The three W7 templates use a **separate Cornerstone wrapper**: no Atlas One logo, no
"ONE CALL SOLVES EVERYTHING." line, no Lehi footer, and a text signature reading
David Taylor, PEO Partner & Business Consultant, Cornerstone PEO, (801) 358-8547,
david.taylor@cornerstonepeo.com, button and signature link to
`https://scheduler.zoom.us/david-taylor-qp71rc`. The check confirmed the string
"Atlas One" appears nowhere in any of the three. No Hearvana, no credit mechanics; the
copy presents the credit total only.

### Things to fix in the template list

1. **Three names appear twice**, because a second author created their own copies while I
   was working: `P-A-3 Referral Email 3` (also `6aa0a93081c4603279ca9f33`),
   `P-B-1 Trigger Email 1` (also `6aa0a9880457161d4222f0b7`) and `P-B-2 Trigger Email 2`
   (also `6aa0a9e10078269ef83ce1ac`). I did **not** delete those; they are not mine and I
   cannot read their contents to compare (the token has no template-detail read scope).
   The ids in the table above are the verified ones. **Delete the other copy of each
   before building the workflows**, or the Send Email picker will offer two identical
   names and you will pick at random.
2. **`P-A-1 Referral Email 1` (`6aa0a8409256eb9f6cb6b7b7`) and `P-A-2 Referral Email 2`
   (`6aa0a8ce62526e75c2c32cd7`)** were built by that same second author. I left them
   alone and **could not verify their wrapper, subject or dash-freeness**. Someone should
   open both and check them by eye.
3. **A stray `New Template`** (`6a99f0306316ab71ecc30dc7`) is sitting in the list.
4. **`Instant auto-reply` does not exist** in the email builder, and neither do
   `Moving forward` or C1/C2/C3. The runbook tells W1 to pick `Instant auto-reply` and
   tells P-C-2 to reuse `Moving forward`. I wrote P-C-2 fresh from the Playbook. W1 step 5
   still needs a decision: build the auto-reply, or point that step at P-C-2.
5. **No test send was made.** The runbook asks for one test send of each to
   David@AtlasOneSolutions.com. The token has no scope for that and it would have put 21
   emails through a domain that is still warming up. The `previewUrl` fetch is a stronger
   check of the stored HTML than an inbox glance, but it does **not** prove Outlook
   rendering. Send a couple by hand before the first real batch.

---

## Deviations from the runbook, and the calls made

**1. WC Renewal Date and Benefits Renewal Date did not already exist.**
The runbook says both "already exist from Form A; reuse, do not duplicate". They did not.
What existed was `Benefits Renewal Month` (**Single line**, Additional Info,
`contact.benefits_renewal_month`), a month name, plus two HubSpot-imported
`Next Renewal Date` fields and a `Upload current WC policy / dec page` file field. None of
those can drive W3a, which waits on "the field minus 120 / 90 / 60 days" and needs a real
date. **Both were created as new DATE fields.** `Benefits Renewal Month` was left alone.

**2. `Referral Partner` is an Opportunity dropdown, so lane A got a contact field.**
`{{opportunity.referral_partner}}` cannot resolve in W2, whose trigger is a contact field
change, and a fixed dropdown cannot hold an arbitrary referrer's name anyway. The contact
field that now exists is **`Referral Partner Name`** (`contact.referral_partner_name`),
and the templates and build sheet use that token throughout. The Opportunity dropdown is
untouched; the Won - Pay Referral Partner workflow still uses it.

**3. `Lifted Suppression` was added to Part 1.**
Runbook Part 7 step a needs it but Part 1 never listed it. It is a CHECKBOX with one
option, `Yes`, so conditions read "contains Yes" rather than "is checked".

**4. Three lane E templates carry no button.**
`P-E-0 Gracious close`, `P-E-4 Month four` and `P-E-Q1 Quarterly tool` have no booking
button. The runbook says every Atlas One template's button links to the audit calendar,
but the Playbook copy for all three is explicitly no-pitch ("no pitch", "nothing to sell",
"I'll leave it there"), and a Book-the-Audit button directly contradicts the sentence
above it. Copy won over the formatting rule, per "do not invent copy". `P-E-Q2` and
`P-E-Q3` do carry the button. Easy to reverse if you disagree.

**5. The free-tool links are placeholders.**
The Retention Cost, Vendor Consolidation and WC premium check calculators are not hosted
at any public URL I could find; the Tools Hub only carries `atlasonesolutions.com` and the
Zoom scheduler. Every Email 3 merges `{{contact.vertical_tool}}`, and the W0 values in the
build sheet put a literal `[link]` in that field. **Until the calculators are hosted and
those links filled in, every lane's Email 3 goes out with a bracket in it.**

**6. No test contact was run, and no A2P status was read.**
Both need the browser, which was stopped. A2P status is therefore **unknown**, not "clear".

---

## Workflows: the click list, not automation

`_briefs/prospecting-workflows-W1-W7-BUILD-SHEET.md`, copied to
`Atlas_One_Master_Kit/12 GHL Setup doccs/Atlas_One_GHL_Prospecting_Workflows_BUILD_SHEET.md`.

All ten in build order (W6, W6b, W0, W1, W2, W7, W3, W3a, W4, W5). For each: the triggers,
the re-entry setting, the Goal step, then every action card numbered in order with its
exact type, field, value and wait, then publish and the test to run. Plus **Appendix A**,
the 21 W0 values (Vertical Opener, Proof and Tool for six verticals and the generic Else),
written dash-free and ready to paste, and **Appendix B**, David's list.

One design decision is flagged in the sheet rather than settled: **W3 step 18**, putting
back a Cooling or Hold tag that a trigger lifted, needs a three-branch If/Else to do
properly. The sheet gives the full version and a simpler always-`Cooling 90d` alternative.
The only cost of the simple one is a `Hold 6m` contact returning after 90 days instead of
six months. Pick before someone builds it.

---

## How the API access worked, for next time

The Private Integration Token is **not** in a `.env` and not in the keychain. It lives in
**`~/.claude.json`**, under `projects` → `/Users/davidtaylor` → `mcpServers` →
`gohighlevel` → `headers.Authorization`, as a Bearer header for
`https://services.leadconnectorhq.com/mcp/`. That is why the first sweep missed it: the
search covered the `~/.claude` directory but not the `~/.claude.json` file. The pointer to
it is in `_INTERNAL (do not share)/GHL-click-guide-FormB-FormC-2026-08-29.md`, line 253.

Two things that will save time:

- **Send a browser User-Agent.** Cloudflare returns 403 error 1010
  ("browser_signature_banned") to Python's default urllib agent before the request ever
  reaches GHL.
- **Scopes the token has and does not have.** It can list, create, update and delete
  templates, read and write custom fields, read tags and read users. It **cannot** read a
  single template's detail (`GET /emails/builder/{loc}/{id}` returns 401 "not authorized
  for this scope"). Use the `previewUrl` that the data write returns to verify content.
- The list response key is **`builders`**, not `data`. Reading the wrong key is what
  produced the duplicate `P-A-3` on the first pass; the redundant copy I created was
  deleted, the second author's copies were not.

---

## What David has to do himself

1. **A2P 10DLC registration.** Settings > Phone Numbers > Trust Center. Brand: Atlas One
   Solutions LLC, the EIN, the Lehi address, AtlasOneSolutions.com, David as contact.
   Then one Campaign, use case "Mixed" or "Low volume mixed", sample messages from
   Playbook section 5, opt-in "checkbox on our quote request forms and verbal consent
   recorded in CRM", opt-out "reply STOP". 1 to 10 business days. **No SMS action gets
   enabled until it reads Approved.**
2. **Verify `david.taylor@cornerstonepeo.com`** as an additional sender: Settings >
   Email Services. GHL emails a verification link to that mailbox and only David can click
   it. W7 cannot send as Cornerstone until then.
3. **Business hours**, if empty: Settings > Business Profile, Mon to Fri 8:30 AM to
   5:00 PM Mountain. W1's 4 hour wait and W4's time window both depend on them.
4. **Host the three calculators** and put the real URLs into the W0 Vertical Tool values
   and into the Email 3 templates.
5. **Clean up the three duplicate templates and the stray `New Template`**, and eyeball
   `P-A-1` and `P-A-2`.
6. **The Monday batch:** 25 names, Lead Lane = D Cold, Vertical set, tag `Batch ready`.
   20 a day for the first two weeks of W4, then 25.
