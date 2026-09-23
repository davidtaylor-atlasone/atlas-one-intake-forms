# RUN-GHL-JOBS-report.md (Run CF, 2026-09-22)

GHL-JOBS terminal. Files and code only, GoHighLevel browser UI never touched. Brief:
`_BUILD-LOG/BRIEF-GHL-JOBS.md` (current run: Run CF) — finish the footer rollout Run CE left, wire the rep kit
swap, put David's name on the public pages. Copied to repo `_briefs/RUN-CF-terminal-GHL-JOBS.md`.

**Status: complete.** All four steps of the brief are done and verified. This run picked up from an earlier
pass of itself that had completed Step 2 in full and one Step 1 piece (the Employee Benefits Menu) before
stopping; everything below Step 2 in this report is new work from this continuation.

## Step 1: footer rollout — done, per piece

For each piece: generator used or HTML edited, and why (from the Rule 1 diff where a generator existed).
Before/after contact and grep results are summarized at the end of this section; every piece is `385-213-7177`
grep = 0 and em/en dash grep = 0, checked file by file as each was edited.

| Piece | Path | Generator or direct edit | Notes |
|---|---|---|---|
| Employee Benefits Menu | `A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html` | Direct edit (no generator exists — confirmed, matches Cowork's own finding) | Done in the prior pass. |
| Six division sheets | `A1_Sales/{Atals 1 Financial Services, Atlas 1 Payroll PEO, Atlas 1 Benefits, Atlas 1 Risk Docs, Atlas 1 Risk Docs/Atlas 1 Tech Operations, Atlas 1 Consulting}/Atlas_One_Division_*.html` | `_INTERNAL (do not share)/tools/division_sheets_build_2026-09-12.py`, TEMPLATE=FIN_HTML=Financial Services sheet | Financial Services sheet's absolute-positioned `.foot` rewritten in place with `a1-footer-person`/`a1-footer-company` classes; first pass wrapped and overlapped the platform pill row (caught by screenshot, fixed with tighter CSS). Reran the generator into scratch, diffed all five outputs against live: footer-only differences. Applied; PDFs regenerated for all six. |
| Industry overlays 01–06 | `A1_Sales/Industry Playbooks/Atlas_One_Industry_Overlay_0{1..6}_*.html` | Direct edit (HTML is the source per Cowork's rule 1 note) | Internal (audience=internal, call-prep playbooks). Added a real `a1-footer` shown only in Atlas One brand mode (`.only-a1`), reading the page's own `CONFIG.a1` via its existing `data-k` mechanism; Cornerstone mode keeps the original colophon untouched, per brief. Verified the brand toggle both directions headless (including unlocking overlay 01's WSA channel lock first). No PDFs (none existed). |
| Services Overview, Partner Client Program PPG | `A1_Sales/A1 What we do Overview/Atlas_One_{Services_Overview,Partner_Client_Program_PPG}.html` | Direct edit | Services Overview's `.ovfoot` rebuilt; also drops a leftover "Lehi, Utah" line (aligns with the standing no-Utah-only-market rule, a side effect not the primary reason). PPG's plain-paragraph `.foot` rebuilt into a real `<footer>`. PDFs regenerated. |
| AI Task Agent, AI Email Assistant, Background Screening one pagers | `A1_Sales/AI Services and Assistants/Atlas_One_*_OnePager.html` | Direct edit | Dark-navy `.cta` box rebuilt with scoped white-text CSS. Also found and fixed 19 pre-existing em dashes across Task Agent and Background Screening (title tags and body copy) while editing — Email Assistant had none. No PDFs exist for these three. |
| Proof Sheet | `A1_Sales/Proof & Case Studies/Atlas_One_Proof_Sheet.html` | Direct edit | `.cta .c` rebuilt. Found and fixed 5 pre-existing em dashes. No PDF exists. |
| Membership Pricing, Membership Brochure | `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_{Pricing,Brochure}.html` | Direct edit | Pricing: only personal contact block on this fixed 11×8.5in landscape page is the header `.right` div (its own bottom `.contact` line is a generic no-name tagline, left alone); rebuilt, verified no overflow on the `overflow:hidden` fixed page. Brochure: page 4's `.pfoot` rebuilt the same way. PDFs regenerated for both. |
| Total Impact Model | `A1_Sales/Total Impact Model/Atlas_One_Total_Impact_Model.html` | `08 ROI Quote Master Template/Total_Impact_Model/build_tim.py`, template = its own prior output | `tim_template.html`'s `.cta .c` rebuilt; ran `build_tim.py`, diffed output against the previously-live file: footer and build-date stamp only. No PDF exists (worked interactively as HTML/JSON). |
| Bookkeeping Marketing Sheet V8, QuickBooks Accountant Access Guide | `A1_Sales/Atlas 1 Bookkeeping/Atlas_One_{Bookkeeping_Marketing_Sheet_V8,QuickBooks_Accountant_Access_Guide}.html` | Direct edit | Marketing Sheet: left the header `.meta` identifier alone, rebuilt the real bottom `.close` contact line (dark navy box). Guide: rebuilt its `.foot`. PDFs regenerated for both. |
| Atlas One Client Portal, Client Dashboard GHL | `A1_Sales/Client Portal/Atlas_One_Client_{Portal,Dashboard_GHL}.html` | Direct edit | Both `.cta`/`.foot` contact lines rebuilt. Found and fixed 21 pre-existing em/en dashes across both files (titles, hero stat ranges rewritten "10 to 20" style to match the kit's own convention, sentence-break dashes), plus one UI placeholder dash (an "active services" stat shown before JS fills it) swapped for a static "0". No PDFs (interactive preview pages). |
| Pricing/Atlas_One_Price_List.html | `A1_Sales/Pricing/Atlas_One_Price_List.html` | **Skipped, per brief's own condition** | catalogue.py lists both `price-list-pdf` and `price-list-client-facing-2-pages` with `audience='internal'` (despite the title literally saying "client facing" — a naming inconsistency worth a look separately, not acted on here). Brief: apply only if catalogue audience is prospect or client. Not touched. |
| Software and Licenses OnePager, Microsoft 365 OnePager | `A1_Sales/Atlas 1 Software and Licenses/Atlas_One_{Software_and_Licenses,Microsoft_365}_OnePager.html` | `_BUILD-LOG/software-licenses-src-2026-09-16.tgz`'s `build.py`/`shell.py` | The tgz was missing `fonts_only.css` (referenced but never shipped); reconstructed it from the live file's own embedded `@font-face` blocks so the generator could run. Patched `shell.py`'s shared footer, ran `build.py` to scratch, diffed against live: footer-only differences (the live copies already carried a company-only support@ footer from an earlier run; this upgrades them to the full David person+company line). Applied to the two named files; the generator's third output (`Software_Card_Portal_Add_Services.html`) has no live counterpart and isn't named in the brief, so nothing was created for it. `Software_Marketplace_Sheet.html` left untouched (on Run CE's explicit leave-alone list). PDFs regenerated for both applied files. |
| Generators wired to `people.py` | `build_tim.py` (done above), `build_audit_report.py`, `service_deck.py`/`brands.py`, `08 ROI Quote Master Template/PEO_Proposal_Generator_V4.5_MASTER/generate.py` | — | See "Generator wiring" below. |
| Cadence email wrapper | — | **No generator exists** | Searched the repo and Master Kit; `tools/ghl_email_builder.py` is a pure GHL API pusher (create/fill/fetch calls only, no HTML logic). The ~40 files in `_BUILD-LOG/cadence-emails-2026-09-13/` are individually hand-built, each copying an existing file's wrapper/signature by hand (confirmed against the Run BN/BR live-log entries describing exactly this pattern). Noted so nobody searches for one again. Cadence emails aren't on Step 1's named piece list regardless. |

### Generator wiring detail

- **`build_audit_report.py`** (`08 ROI Quote Master Template/Total_Impact_Model/`): wired its footer to
  `people.py`'s `footer_html(None)` (company-only, matching the report's arms-length tone). Found the schema
  the `<footer>` used was a literal `Atlas One Solutions · 380-CALL-A1S · AtlasOneSolutions.com · built
  {build_date}` string; replaced with a `{a1_footer}` placeholder fed from `people.py` and fixed a nested-`<footer>`
  bug that would have resulted (footer_html already returns a full `<footer>` element). Tested against the
  existing sample JSON (`SAMPLE_Tell_Me_More_LLC.json`, `--no-ghl`): renders correctly, headless verified, grep
  clean. The sample report/PDF were regenerated as a side effect of testing (same as Run BT's own practice).
- **`service_deck.py` / `brands.py`** (`08 ROI Quote Master Template/PEO_Proposal_Generator_V4.5_MASTER/`):
  `brands.py`'s `"Atlas One Solutions"` brand entry now syncs `email`/`office` from `people.py`'s default person
  at import time. The other PEO partner brands (G&A, Cornerstone, Vero HCM, PEOPilot) are separate identities
  David works under and were left untouched. Tested by building a real deck (`bookkeeping` pack) and converting
  it to PDF with LibreOffice (`soffice --headless --convert-to pdf`, available on this Mac); rendered the cover
  and closing slides to PNG with PyMuPDF — both correct, no text overflow despite the phone display format
  roughly doubling in length (`(380) 225-5217` → `380-CALL-A1S (380-225-5217)`).
- **Agreements/packets `generate.py`** (`_INTERNAL (do not share)/tools/agreements/`): wired both its docx and
  HTML footer render paths to `people.py`'s company block, which also drops a leftover **"Lehi, Utah"** line (the
  standing never-imply-clients-are-in-Utah rule) — this was on every agreement and schedule document. Rule 1
  diff on two representative docs (MSA, Bookkeeping Schedule) showed footer-only differences (docx text and PDF
  text compared directly, not just re-rendered and eyeballed). Ran the real generator against the live output
  directory (`A1_Sales/A1 Agreements/2026-09-15 masters/`).
  **Found and left a pre-existing bug**, confirmed unrelated to this edit by reproducing it against the
  unmodified backup copy: `schedule_cert_payroll()` reads `PRICES["cert_payroll"]["monthly"]`, a key that no
  longer exists in the current `prices.json` (its schema was restructured into
  `setup`/`report`/`state_monthly`/`federal_weekly`/`done_for_you` at some point after `generate.py` was last
  fully exercised). This aborts that one schedule and, because `sample_proposals()` depends on it, all 9
  `Sample_Proposal_*.pdf` files too. Regenerated the other 11 of 12 docs for real with the new footer (MSA, Hold
  Harmless, 8 other schedules, Proposal Shell) — confirmed via direct PDF text diff and docx paragraph read, zero
  `Lehi`/`385-213-7177`/dash. `Atlas_One_Certified_Payroll_Schedule.pdf` and the 9 sample proposals are
  **unchanged, still carrying the old footer** — flagged below, not silently left for someone to rediscover.

## Step 2: David's name on public pages — done (prior pass, unchanged this run)

`footer_html(public=True)` prints the person line without an email address (name, title, tel link, "Book 15
minutes with David"), company line underneath. Applied to 8 repo files under `tools/` plus `census/index.html`.
See the prior pass's report section (preserved from before this continuation) for the full before/after table;
nothing in Step 2 changed in this pass.

## Step 3: rep kit swap — done, with one real bug found and fixed

`build_command.py` changes:
1. `build_entries()` accepts `person_slug`; on every inline blob, if `person_slug` is set it looks for
   `a1-footer-person` in the raw source. Present → calls `swap_footer_person()`. Absent and the row's zone is
   **Sales Kit** → hard failure naming the file (`SystemExit`). Absent and the zone is **Tools** → skipped and
   listed (a tool/calculator, not a sales piece).
2. `build()`/`build_rep_kit()` thread `person_slug` through and print the skip list.
3. The Sending-as `<label>`/`<select>` are now built as a single `{{SENDINGAS_HTML}}` template placeholder,
   populated with the real markup only when `include_present=True` (COMMAND) and left empty otherwise — stripped
   entirely from the Sales Kit and every rep kit, not just CSS-hidden as Run CE left it.

**Bug found and fixed:** `swap_footer_person()`'s regex used a non-greedy `(.*?)` that matched the *first*
closing tag anywhere inside the `a1-footer-person` element — always an inner `</a>`, since every real footer
this run built nests at least one mailto/tel link. The swap replaced only up to that first `</a>`, leaving the
rest of the old person's markup (including their **phone number**) appended after the new line instead of
replaced. First-pass output on all 11 of Charity's own-copy files had this defect (verified directly:
`"801-787-8154</a> · 380-CALL-A1S"` leftover after the swap). Fixed with a tag-name backreference
(`<(\w+)...class="...a1-footer-person...">...</\1>`) so the regex matches the element's own closing tag; unit
tested, then all 11 files regenerated clean.

**Important finding, not acted on:** catalogue.py currently marks every one of Step 1's rollout pieces
(division sheets, Benefits Menu, TIM, Proof Sheet, Membership docs, Bookkeeping, Client Portal, Software/Licenses
one pagers) `audience='internal'`, and the three pieces that are `audience=prospect/client` (Services Overview,
PPG, QuickBooks Guide) are `inline=False` (relative links, not embedded blobs). Neither category ever reaches
the Sales-Kit-zone inline-blob code path in a rep-kit or Sales Kit build. This means the swap machinery, though
correctly built and gated, currently has **nothing to act on** — Charity's rep-kit HTML file contains **none**
of the Step 1 pieces at all, regardless of footer content. Confirmed by directly inspecting `build_entries()`'s
output for a real Charity build: 0 rows land in Sales Kit zone as inline blobs from this piece list. This is a
catalogue configuration question (should these pieces' `audience`/`inline` flags change so they flow through
Sales Kit builds and the swap machinery), not something decided unilaterally here — see Questions for David.

**Charity's own copies**, the brief's separate explicit requirement, fulfilled directly (not through the
catalogue/blob path, since nothing in Step 1 reaches it today): built
`A1_Sales/_Rep Kits/Charity Taylor/Division Sheets/` (all six) and `/One Pagers/` (AI Task Agent, AI Email
Assistant, Background Screening, Software and Licenses, Microsoft 365), HTML and PDF, via `swap_footer_person()`
applied straight to each source file. All 11 verified clean after the bug fix: `david@atlasonesolutions`=0,
`Charity Taylor`=1, no stray double-close tags, `385-213-7177`=0, dash=0.

### Blob-decode counts (Charity's Sales Kit, 49 inline blobs)

- **Sales-Kit-zone rows** (7 total; the actual client-facing pieces cataloged for a rep kit today): `david@`=0,
  `Charity Taylor`=0 — none of these 7 rows are inline blobs (see the catalogue finding above), so there's
  nothing to swap and nothing leaking either.
- **Tools-zone rows** (46 skipped, correctly, per Step 3's own rule): 96 `david@atlasonesolutions` occurrences
  remain, all inside calculator/intake-form tool content that never carried an `a1-footer-person` contract to
  begin with (e.g. a hardcoded contact tip inside "Atlas One Business Tools (17 generators).html"). This is
  expected and out of scope for the footer swap — not a leak of a swappable sales-piece contact line.
- **Forbidden terms** (margin, commission, wholesale, cornerstone, g&a, verohcm): `build()`'s own
  `forbidden_check=True` pass (audience-scoped, allowlist-aware) already ran against this exact file during the
  real build and did **not** raise — that's the authoritative gate. A naive raw-text recount (no allowlist, no
  audience scoping) shows non-zero hits for margin/commission/wholesale/g&a, all inside Tools-zone or
  allowlisted content the official check intentionally does not scan.

## Step 4: rebuild and verify — done

- `catalogue_check.py`: OK, 206 entries, all paths resolve.
- Rebuilt COMMAND (206 items) and the shared Sales Kit (57 items) with the new `build_command.py` — both clean.
- Rebuilt Charity's rep kit (`--person charity`): 57 items, 46 Tools-zone pieces correctly skipped, zero hard
  failures.
- **Headless Chromium (Playwright) at 1440, 1024, 390** on COMMAND: `scrollWidth` equals viewport at all three,
  zero console errors at all three; every zone (Sales Kit, Tools, Internal, Present) scrolls to its last row
  with no clipping at all three widths.
- **Internal tab**: opens with no passphrase gate (confirmed both by the build log —
  `INTERNAL_PASSPHRASE: (none, curtain removed)` — and by a headless check finding zero gate text). Approval
  Queue opens in one click (confirmed the popup's URL is the correct external Azure queue login page); Activity
  log and Tasks & Follow ups each open in one click via the in-page viewer.
- **All eight Present playlists** (client/prospect × 15/30/45/60 minutes) opened via Start and stepped through
  via Next to their last page (12–20 steps depending on length), zero console errors throughout.
- **Sending-as picker**: present only on COMMAND (grep count 1), absent on the shared Sales Kit and Charity's
  rep kit (grep count 0 both). Switched to Charity in Preview and decoded the live iframe content directly (the
  swap mechanism creates a new sibling element and CSS-hides the original rather than replacing in place, so a
  DOM text-content read rather than a locator was used): `Charity Taylor` present, `david@` absent. The swap JS
  only ever targets `a1-footer-person` elements — `a1-footer-company` is never touched by it, so the company
  line is identical for every person **by construction**, not merely by observation.
- **Charity's rep kit**: reverified clean at 1440/1024/390 (scrollWidth matches viewport, zero console errors),
  Sending-as select confirmed fully absent.
- Ten sampled footer pieces spot-checked across this run's own screenshots (two division sheets, one overlay in
  each brand mode, both software one pagers, the benefits menu, the proof sheet, one public page at mobile
  width): all clean.
- Deployed nothing.

## Screenshots

All in `_briefs/assets/run-CF-jobs/shots/` in the intake-forms repo:
`division-financial-services{,-v2}.png`, `division-{consulting,risk,payroll}.png`, `overlay01-{a1,cs}-mode.png`,
`services-overview.png`, `ppg.png`, `Atlas_One_AI_Task_Agent_OnePager.png`,
`Atlas_One_AI_Email_Assistant_OnePager.png`, `Atlas_One_Background_Screening_OnePager.png`, `proof-sheet.png`,
`membership-{pricing,brochure}.png`, `tim{,-hero-only}.png`, `bookkeeping-marketing.png`,
`quickbooks-guide.png`, `client-{portal,dashboard-ghl}.png`, `software-licenses.png`, `microsoft-365.png`,
`msa-page2.png`, `service-deck-page{1,7}.png`, `audit-report-sample.png`, `charity-division-financial.png`,
`command-{1440,1024,390}.png`, `present-{zone,after-run}.png`, `sendingas-{charity,david}-preview.png`,
`charity-kit-{1440,1024,390}.png`, `public-what-we-do-final.png`.

## Assumptions

1. Footer visual wrappers vary by piece (absolute-positioned print pages, dark CTA boxes, light contact bands)
   — each got the `a1-footer-person`/`a1-footer-company` *classes* and *content contract* rather than forcing a
   single visual template everywhere; this was necessary to avoid breaking fixed-height print layouts (verified
   with screenshots after each edit, one real overflow bug caught and fixed on the Financial Services division
   sheet before it propagated to the other five).
2. Industry overlays (internal call-prep docs): the page's static bottom colophon is not the "contact block"
   the brief means (it carries no name/email, it's a document note); the real per-brand identity lives in the
   `CONFIG.a1`/`CONFIG.cs` objects already wired to the page's `data-k` system. Built the new `a1-footer` to read
   from that existing system rather than duplicating contact data a third time.
3. Kept `tools/wc-premium-check`'s existing Zoom scheduler button rather than replacing it (from Step 2, prior
   pass) — unchanged this pass.
4. Did not touch `census/index.html`'s JS-built results-email mailto (visitor-triggered function, not a printed
   contact line) — unchanged this pass.
5. `schedule_cert_payroll()`'s prices.json mismatch and the resulting stale Certified Payroll Schedule / 9
   sample proposals: left unfixed rather than guessing at a repricing scheme for a schedule whose price
   structure changed underneath the generator. This is a business-pricing call, not a footer swap.
6. Cadence emails: confirmed no generator exists and left the ~40 individual files untouched (not on Step 1's
   piece list; a hand-copy pattern, not code).

## Questions for David

1. **Catalogue audience/inline flags.** Every Step 1 rollout piece (division sheets, Benefits Menu, TIM, Proof
   Sheet, Membership docs, Bookkeeping, Client Portal, Software/Licenses one pagers) is `audience='internal'` in
   catalogue.py, and the three that are prospect/client-facing are `inline=False`. This means none of them ever
   flow through a Sales Kit or rep-kit build today — Charity's kit contains none of them, regardless of any
   footer work. Should these pieces' catalogue entries change so they actually appear (as inline blobs) in a
   portable Sales Kit / rep kit, or is Present-from-COMMAND the only intended distribution path for them and
   the current internal/relative-link settings are correct as-is?
2. **`schedule_cert_payroll()` / prices.json mismatch.** The Certified Payroll Schedule agreement and all 9
   sample proposal PDFs cannot currently be regenerated — `prices.json`'s `cert_payroll` entry was restructured
   into five sub-keys (setup/report/state_monthly/federal_weekly/done_for_you) at some point, but the generator
   still asks for a flat `["monthly"]` key. Someone who knows the intended pricing needs to update
   `schedule_cert_payroll()` in `generate.py` to read the new structure before that schedule (and the samples)
   can be regenerated again — this run left both stale rather than guess.
3. **`Atlas_One_Price_List.html`/`.pdf` catalogue audience.** Both catalogue entries say `audience='internal'`
   but the title literally reads "Price List (client facing, 2 pages)" and the blurb calls it "Retail only" —
   worth a second look to confirm which is correct; not changed here per the brief's own condition.
4. **`tools/wc-premium-check`'s dual booking CTAs** (from Step 2, carried over): is it fine to keep both the
   Zoom scheduler link and the new leadconnectorhq "Book 15 minutes" link side by side long term, or should one
   replace the other?
