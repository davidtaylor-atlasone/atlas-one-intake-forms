# RUN-GHL-JOBS report: Run BL (COMMAND v2 in three zones, Sales Kit file, front door page, PPG one pager, script path hygiene)

Terminal: GHL-JOBS (files and code only, no GHL browser). Ran end to end in one session, no sub agents, per rule 44.

## Built

### Job 1: Atlas One COMMAND, three zones
`_INTERNAL (do not share)/build_command.py` and `catalogue.py` rewritten. The left rail of fourteen sections
is gone. Three top level tabs, in this order: Sales Kit, Tools, Internal. Under 700px the tab bar stays sticky
at the top. Zone is derived mechanically from fields already on each row (`kind`, `division`, `audience`), no
hand tagging:

1. Tools: any row with `kind` tool or builder, regardless of audience, grouped inside the zone by the six
   official divisions, then Cross division for anything else (Pricing & Quotes tools, Start here tools, and
   so on).
2. Sales Kit: rows in Start here, Decks, Sell & Pitch, Industry overlays or Intake & Client (these read as
   "what you present", even when a row happens to be tagged audience internal, meaning David presents it
   rather than a client self serving it), plus every other prospect or client audience row.
3. Internal: rows in Internal (do not share), Pricing & Quotes, Email templates or Agreements, plus every
   other audience internal row.

Every zone shows its own pinned rows pulled to a "Start here" sub section at the top (still also listed under
their real division), and its own "Your queue" sub section for the four rows marked `queue=True` (all four
landed in Internal, since they are the AI Email Assistant live queue links and the client portal admin sign
in). Internal opens only after a passphrase (`atlas1`, one constant at the top of build_command.py, comment
says plainly "curtain, not security") typed into an on page input, remembered in `sessionStorage` for that
browser tab only. The Internal tab shows a CSS drawn lock glyph until opened. **This is a curtain, not
security. The real protection is that Atlas One COMMAND.html never leaves your OneDrive.** Anyone with the
file could read the passphrase straight out of the HTML source.

Same base64 park and decode mechanism as before for inlined tools, same fresh iframe per preview fix, Open in
a new tab, PDF fallback link. Rebuilt in place: `Atlas_One_Master_Kit/Atlas One COMMAND.html`, stamp **Sep 17,
2026 8:47 PM**, **196 items** (Sales Kit 41, Tools 106, Internal 67).

**Catalogue override (the only one this run):** `client-portal-admin-sign-in` (division Intake & Client, which
normally reads Sales Kit) got `zone='Internal'` — it is David's own admin sign in link ("Sign in as
david@atlasonesolutions.com"), not something to show a prospect. Found this by scanning every Sales Kit zone
row's title and blurb for admin/internal/sign-in language after the first render; nothing else in any zone
matched.

### Job 2: Atlas One Sales Kit.html (shareable file)
Second `build()` call in the same script. Same look, only the Sales Kit and Tools zones, only rows with
audience prospect or client, no `_INTERNAL` path can be inlined (belt and suspenders check on top of the
audience filter), no Internal tab, no passphrase. Hero line: "Shared by Atlas One Solutions. Call
380-CALL-A1S (380-225-5217)." Written to
`A1_Sales/Atlas One Sales Kit.html` (same folder as `A1 Agreements`, not under `HR_Docs`), stamp **Sep 17,
2026 8:47 PM**, **56 items** (Sales Kit 7, Tools 53). Added a Start here row for it in the catalogue.

**Forbidden term guard result:** ran, passed. It greps every inlined tool's raw source (before it is base64
parked) for margin, commission, wholesale, cornerstone, g&a, verohcm, using the same allowlist as COMMAND
(every allowlisted hit was hand reviewed 2026-09-14 and is the prospect's own number, not Atlas One's). No new
hits, build did not hard fail.

**Caught before calling this done:** the first build wrote to `HR_Docs/A1_Sales/Atlas One Sales Kit.html`
because `__main__` computed `A1_Sales` as `mk/../A1_Sales` (one level too shallow — `A1_Sales` sits beside
`HR_Docs` under the Marketing root, `mk/../..`, not inside `HR_Docs`). Fixed to `mk/../../A1_Sales`, deleted
the two stray items that first run had created (an empty `HR_Docs/A1_Sales/A1 What we do Overview/` directory
and the misplaced `HR_Docs/A1_Sales/Atlas One Sales Kit.html`, both created this session, nothing
pre-existing touched), reran. `catalogue_check.py` now reports **OK, 196 entries, all paths resolve.**

### Job 3: front door page
`~/Projects/atlas-one-intake-forms/start/index.html`. Self contained, DM Sans from Google Fonts (page is
online only per brief), navy/periwinkle/paper/mist palette matching `index.html`. Hero, the Audit offer block
with the guarantee word for word and both booking buttons, five tool cards, a "See every tool" link to
`../tools/`, the two intake cards linking to `../peo/` and `../bookkeeping/`, footer with `tel:`/`mailto:`.

**The five tools** (each opened and confirmed to exist, public, with its own title used on the card):
`time-savings/` (Time and Cost Savings Discovery), `vendor-consolidation/` (Vendor & Software Audit),
`retention-cost/` (Retention vs. Replacement Cost Calculator), `wc-premium-check/` (COI to Workers Comp
Premium Estimator), `self-assessment/` (Back Office Self-Assessment).

Committed and pushed (commit `8f6b328`, `Run BL: front door page at start/`); live at
`https://forms.atlasonesolutions.com/start/` once GitHub Pages picks it up. Added a Start here catalogue row
pointing at the live URL.

**For David, to put it on start.atlasonesolutions.com:** GoDaddy, atlasonesolutions.com, DNS, Forwarding, add
a subdomain forward for `start` to `https://forms.atlasonesolutions.com/start/` (permanent 301, forward only).
Did not touch DNS.

Verified headless Chromium at 390 and 1440: `scrollWidth` equals viewport at 390, zero console errors.
Screenshots: `_briefs/assets/run-BL-jobs/shots/start-390.png`, `start-1440.png`.

### Job 4: PPG one pager
`A1_Sales/A1 What we do Overview/Atlas_One_Partner_Client_Program_PPG.html`, one printable Letter page
(`@page{size:Letter;margin:0.55in 0.6in}`), fonts embedded from `fonts_embed.css` (Horas, DM Sans), four
colours, no dashes in the prose (the phone number keeps its established hyphenated format, matching every
other Atlas One page and the front door footer), no vendor or PEO brand names, no Atlas One internal numbers
(only the membership and document prices given in the brief). Copy used as written. Rendered to PDF beside it
with Playwright (`prefer_css_page_size`, print media, via the atlas-one-ai-email-assistant venv): **1 page**,
zero console errors. Rendered that PDF page to a PNG and looked at it: nothing clipped, all three blocks under
"What your clients get", all four numbered steps, and all three "Why it fits" items fit on the one page.
Screenshot: `_briefs/assets/run-BL-jobs/shots/ppg-onepager.png`. Added a Sell & Pitch catalogue row.

### Job 5: script path hygiene
Grepped `_INTERNAL (do not share)/*.py` and `tools/*.py` for `/Users/davidtaylor` and `/Users/david/`. Found
and fixed the three real hits:

| Script | Before | After |
|---|---|---|
| `agreements_inventory_2026-09-12.py` | `B="/Users/davidtaylor/.../2. A1 Official Docs/4. Brokers_Vendors A1 Solutions"` | `B = os.path.join(OFFICIAL_DOCS, "4. Brokers_Vendors A1 Solutions")` |
| same | `TD="/Users/davidtaylor/.../OneDrive-AtlasOneSolutions/_to_delete/superseded-2026-09-12/agreements"` | `TD = os.path.join(ONEDRIVE_ROOT, "_to_delete", "superseded-2026-09-12", "agreements")` |
| `build_mutual_nda_2026-09-12.py` | `OUT="/Users/davidtaylor/.../A1_Sales/A1 Agreements/Atlas_One_Mutual_NDA_TEMPLATE_2026-09-12.docx"` | `OUT = os.path.join(MKT, "A1_Sales", "A1 Agreements", "Atlas_One_Mutual_NDA_TEMPLATE_2026-09-12.docx")` |
| `build_referral_partner_agreement_2026-09-12.py` | `OUT="/Users/davidtaylor/.../A1_Sales/A1 Agreements/Atlas_One_Referral_Partner_Agreement_TEMPLATE_2026-09-12.docx"` | `OUT = os.path.join(MKT, "A1_Sales", "A1 Agreements", "Atlas_One_Referral_Partner_Agreement_TEMPLATE_2026-09-12.docx")` |

Each got the same `find_master_kit()` helper: walk up from the script's own file location to a directory
literally named `Atlas_One_Master_Kit`, else the brief's find-by-name command, filtered against
`_to_delete`/`archiv`/`TO DELETE`. `MKT`, `OFFICIAL_DOCS` and `ONEDRIVE_ROOT` are all derived from that one
`MK`.

`render_html_pdfs.py`'s one hit (`/Users/davidtaylor/Projects/atlas-one-ai-email-assistant/.venv/bin/python`)
is a docstring line telling a human which Python has Playwright installed, not a Master Kit relative path
computed at runtime; its own `ROOT` was already derived dynamically. Left unchanged.

**How this was verified:** two of the three scripts (`build_mutual_nda`, `build_referral_partner_agreement`)
build and `d.save(OUT)` a `.docx` at module level with no `--check` flag and no `if __name__=="__main__":`
guard, so importing either would regenerate a document, not just check a path. Ran the new
`find_master_kit()`/path derivation logic in isolation (a standalone snippet, not the real scripts) instead,
and compared every derived path against the four old hardcoded strings: **all four matched byte for byte**,
and the destination directories (`4. Brokers_Vendors A1 Solutions`, `A1_Sales/A1 Agreements`) exist. All three
edited files pass `python3 -m py_compile`.

## Verification (headless Chromium, screenshots in `_briefs/assets/run-BL-jobs/shots/`)
- COMMAND at 1440: Sales Kit (default), Tools, Internal locked, Internal after typing `atlas1` and clicking
  Unlock. COMMAND at 390: Sales Kit, sticky tab bar. `scrollWidth` equals viewport at 390. Zero console
  errors on every load.
- Clicked a Preview button in the Sales Kit zone (inline iframe) and in the Tools zone (inline iframe): both
  opened the fresh-iframe preview pane, zero console errors after interaction. Clicked an Open button:
  opened a new tab/popup, zero console errors.
- Sales Kit file at 1440 and 390: two tabs only (no Internal, no lock), hero line visible, zero console
  errors, `scrollWidth` equals viewport at 390.
- Front door page (Job 3) and PPG PDF (Job 4): covered under their own sections above.

## Assumptions
1. **"Periwinkle laptop mark" on the front door page:** no laptop shaped brand glyph exists in this repo or
   in `A1_Final Brand/4. Images/` (`Laptop.png` there is a stock photo of hands closing a laptop, not a
   mark). Used the same periwinkle "A1" square mark `index.html` already uses for its hero. If a real laptop
   shaped mark exists somewhere else, point me to it and I will swap it in.
2. **Sales Kit zone rule precedence:** read the brief's three zone rules as applying in the order written
   (Tools first, "whatever its audience"; then the Sales Kit divisions list, which can override an
   audience-internal tag; then the Internal divisions list and the general audience-internal catch all). This
   is what makes Decks (all tagged audience internal, since David presents them rather than a prospect
   self-serving them) land in Sales Kit instead of Internal. Flag if this reading is wrong.
3. Dropped the old "Recently opened" per-viewer `localStorage` list that used to live under a single global
   `#sec-start-here` id. That id no longer exists (Start here is now a pseudo section inside each of the
   three zones), and the brief did not ask to keep it. Easy to re-add scoped per zone if wanted.
4. `A1_Sales` and the Marketing root: confirmed by directory listing, not by re-deriving from the brief's
   `$MK/../A1_Sales` shorthand a second time, after that shorthand's literal interpretation produced the
   wrong directory once already (see Job 2 above).

## Skipped
Nothing in the brief was skipped. `build_portal.py` and `build_portal_single.py` were left exactly as they
already were (already print "superseded" and exit; not touched this run, out of scope).

## Questions for David
1. Is `atlas1` fine to keep as the Internal tab passphrase, or do you want a different word? It is in one
   constant at the top of `build_command.py` if you want to change it yourself later.
2. Does the periwinkle "A1" square mark work for the front door page hero, or is there a laptop shaped mark
   somewhere I did not find? (Assumption 1 above.)
3. OK to leave the "Recently opened" feature dropped from COMMAND (Assumption 3), or should it come back,
   scoped per zone?
4. To go live at `start.atlasonesolutions.com`: GoDaddy, atlasonesolutions.com, DNS, Forwarding, add a
   subdomain forward for `start` to `https://forms.atlasonesolutions.com/start/` (permanent 301, forward
   only). I did not touch DNS.
