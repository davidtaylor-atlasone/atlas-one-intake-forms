# RUN CS, helper "content", Job 2 content pieces (2026-09-30)

MKT = `/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing`. MK = `MKT/HR_Docs/Atlas_One_Master_Kit`.

## Built
1. Renderer: `MK/_INTERNAL (do not share)/render_md_pages.py` (built in converter, the `markdown` package is not installed). Run it with no arguments to render all and rewrite the manifest. Fonts embedded from `tools/agreements/fonts_faces.css` (Horas, DM Sans 400 and 700). 17px body, sticky Copy button per email card (clipboard API with textarea fallback, copies plain text, leaves out the Attach box, bullets copy as a dot, no dashes added), Attach box at the top of every card. Cadence emails written as HTML source are shown as the readable email.
2. Manifest: `MK/_INTERNAL (do not share)/rendered_md_manifest.json` (rendered, already_html_no_md, skipped with reasons).
3. Rendered pages (HTML next to each md, md never overwritten), all in `MKT/A1_Sales/Email Templates/`:
   - Atlas_One_Prospect_Email_Templates.html (8 emails)
   - Atlas_One_Email_Blast_Library.html (34 emails, card titles prefixed with the service name)
   - Atlas_One_Referral_Request_Emails.html (2)
   - Atlas_One_Bookkeeping_Onboarding_Emails.html (3)
   - Atlas_One_Bookkeeping_Cadence_2026-09-13.html (7; GHL wrapper, render notes and assumptions sections hidden on the page, title and intro replaced by an override in the renderer; the md is untouched)
   - Atlas_One_Client_Announcement_Series.html (6, new)
4. Attach lines: `MK/_INTERNAL (do not share)/email_attach_tool.py` added `**Attach these:** ...` under every email heading in the six md files (60 emails) and refreshes them if rerun. Only those lines were added to existing md files (diff checked). Map: `MK/_INTERNAL (do not share)/email_attach_map.json` (template, html path, per email list, union list, each piece as kind file with path, or kind link with url plus the local source path). 80 references, all paths verified to exist.
5. NEW `MKT/A1_Sales/Email Templates/Atlas_One_Client_Announcement_Series.md` plus `.html`: six emails (news, one call, Audit and guarantee, membership, savings example, check in). "Not an acquisition, nothing about payroll, PEO, HR or benefits moves, only the rep's company name changes and services are added" is in emails 1 and 6 and in the rep notes. Merge fields `{{rep_name}}`, `{{rep_title}}`, `{{rep_phone}}`, plus `{{first_name}}` and `{{rep_booking_link}}`. No dashes (scanned), no vendor or PEO brand, no Utah.
6. NEW `MKT/A1_Sales/A1 Playbook Sales/Atlas_One_Talk_Track.html` (builder: `MK/_INTERNAL (do not share)/build_talk_track.py`): who we are, what we solve, 30 second and 2 minute read aloud boxes (21px), one relationship, discovery questions, Audit ask with guarantee, 12 objections, closing line, an existing client line. Rep neutral, no person's name, only price is "starting at $99 a month" read from prices.json V9.

## Looked at (shots in `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/content/`)
All seven pages at 1440 and 390: scrollWidth equals the viewport on all 14 loads, zero console errors, zero network requests other than file and data. Looked at: series (1440, 390, full page, card 3), talk track (1440 top, 30 and 2 minute boxes, objections, 390 top, Audit section), prospect (1440 and 390), blast (intro, TOC, a card), onboarding card 1, cadence (1440, card at 390), referral, plus the copy test (clicked Copy, confirmed plain text, Subject line, no Attach text).
Fixes made after looking: attach chips split on a comma, Attach line glued to the Subject line, repeated card names in the blast TOC, emoji in the Attach label (removed, four colours only), cadence subject missing from the copied text.

## Dash and price scan
New files (series md and html, talk track): no em dash, no en dash, no spaced hyphen. One compound word "I-9s" in the talk track. price_scan.py over A1_Sales: 0 hits in Email Templates and A1 Playbook Sales files (the hits it reports are in other folders, not mine).

## Skipped (not rendered)
Sales_Partner_Welcome_Email.md (partner program), Document_Services_Pricing_Options md (internal memo), Agreements_How_They_Fit.md (names PEO vendors, legal notes), both WSA Industry Playbooks md (live partner deal), blog markdown, BRJ website packages, portal and website copy md, QR plan, Dr Gould, GHL setup docs, Tools Cheat-Sheet, Command Center md, prospecting playbook build log. Already pages, no md: Sales Conversation Playbook (objection handbook inside), Prospecting Playbook, six Industry Overlays.

## Assumptions
1. The Proof Sheet is the real savings source for email 5 (masonry $16,000, medical practice $28,000 and 400 hours). Both are quoted as written, with a plain "yours will differ" line. No annual math was added.
2. Membership copy uses prices.json V9 only. Enterprise setup waiver on an annual plan is left out because annual plans are open.
3. Concierge inclusions follow prices.json (AI Task Agent, certified payroll, GL converter, handbook and safety manual). The atlas-pricing skill also says it includes the AI Email Assistant, which prices.json does not say, so the email does not claim it.
4. Cadence page hides GHL build sections but the md is unchanged. Its Sequence A trigger line still says "David" and names GHL tags.
5. "Providers pay us" wording in the talk track comes from the Sales Conversation Playbook near free line. Email 4 is more careful: shopping benefits and comp is paid by providers, bookkeeping is priced up front.
6. Attach pieces are chosen per service and campaign type (rules in email_attach_tool.py). Proof Sheet and the AI one pagers attach as the PDFs from the Charity Taylor rep kit because only the HTML exists in their main folders. Re engagement emails attach only the Self Assessment link.
7. Referral Request Email 2 (to a broker or vendor, mentions commission) was rendered because it is a referral request email, but it touches the partner program. Easy to drop.

## Existing copy problems found (not changed, outside my brief)
- Prospect Email Templates: A1 example says "Utah construction companies"; A2 says "I'm paid by the vendors" and signs "David"; B1 quotes the $2,198 example; stale "reply with a couple of times" calls to action; many em dashes.
- Bookkeeping Onboarding Email 2 says catch up at "$175 a month", prices.json says catch up is billed at the plan's monthly rate. Needs David's call.
- Blast Library and Referral emails sign as David, and are full of em dashes.
- Cadence B-1 prints payroll $30, $15, $7.50 per employee without the monthly minimum ($100 and $150) that V9 added.

## Questions for David
1. Charity has no booking link yet (people.json booking is null). The series uses `{{rep_booking_link}}`. What should the email show for her until she has one?
2. Should the existing templates (Prospect, Blast, Referral, Onboarding, Cadence) be cleaned of em dashes, "David" signatures, the Utah example and the $175 catch up price? I rendered them as they are.
3. Concierge: does it include the AI Email Assistant, or only the AI Task Agent (prices.json)?
4. Referral Request Email 2 mentions commission or revenue share with outside referrers. Keep it on Charity's page?
5. The series says "I now work under the name Atlas One". Is that the right framing for Charity's existing clients, or does she need a different line for where she came from?
