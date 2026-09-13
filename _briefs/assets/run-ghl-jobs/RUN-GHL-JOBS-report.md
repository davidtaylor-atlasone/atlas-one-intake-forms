# RUN GHL-JOBS report (code and files only, no GHL UI)

Built 2026-09-13 by Claude Code, unattended, no questions asked, every permission prompt answered here. Brief read from `<Master_Kit>/_BUILD-LOG/BRIEF-GHL-JOBS.md` (Run AE), copied to `repo:_briefs/RUN-AE-GHL-JOBS.md`. Nothing sent, nothing deployed, nothing spent, nothing deleted (font-embed backups moved to `OneDrive:_to_delete/superseded-2026-09-13/fonts-before/`). Live log: `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`.

Paths are relative to `HR_Docs/Atlas_One_Master_Kit/` unless marked `repo:` (atlas-one-intake-forms) or `A1_Sales/`.

## Main build: the "Everything Atlas One handles" page

- `repo:tools/what-we-do/index.html`, published for **https://forms.atlasonesolutions.com/what-we-do/**. Single self-contained file (410 KB, mostly the embedded Horas and DM Sans fonts, reused byte-for-byte from `tools/self-assessment/index.html`, plus the header mark). No CDN, no Google Fonts, no external script; zero console errors and zero non-`file://` network requests at both 1440 px and 390 px.
- **200 check, not yet confirmed.** The file is confirmed on `main` at GitHub (contents API returns it; `git ls-tree` shows it at HEAD) and GitHub's Pages build API reported `status: built` for the commit four times in a row across about 30 minutes (once more after an unrelated push from another terminal landed on `main`), each with no build error. The live URL still returned GitHub's own generic 404 page the whole time. Stopped polling after 30 minutes per the run rules rather than waiting indefinitely; this reads as a GitHub Pages CDN propagation gap, not a defect in the build or the file, but it needs a look: try `https://forms.atlasonesolutions.com/what-we-do/` again, and if it is still 404, an empty commit push (`git commit --allow-empty` + push) usually forces GitHub Pages to redeploy and clears a stuck cache entry.
- Sections, in the brief's order: hero (vendor-neutral positioning, Book a few minutes button), six division cards, documents built for you as a member, software simplified, free tools plus member tool names, the Audit Guarantee band with membership tier names, close (phone, email, tagline).
- **Service count per division** (names only, from the Quick Quote Tool's 99-entry `SERVICES` catalogue, 6 divisions): Workforce & HR 23, Benefits & Retirement 15, Financial Services 12, Risk & Insurance 9, Technology & Operations 17, Business Consulting 10 (86 shown). The 13 not shown here: the four membership tier line items (Essential/Professional/Enterprise/Concierge, moved to the Audit Guarantee band instead) and six Business Consulting items that duplicate the Documents section (handbook, handbook update, safety manual, safety update, contract build, contract bundle); the AI Email Assistant's two tiers and the three bookkeeping size tiers are each shown as one consolidated line.
- Meta: title "Everything Atlas One handles", one-line description, Open Graph image at `tools/what-we-do/og-image.png` (1200x630, generated with Pillow from the brand Logo Mark in full colour centred on `#FAFAF8`, Horas headline, DM Sans subhead; see Assumption 1).
- Print stylesheet: renders to exactly **2 Letter pages** (confirmed via `page.pdf({preferCSSPageSize:true})`, page count read from the PDF's `/Count`). Printed copy saved to `A1_Sales/Atlas_One_Everything_We_Handle.pdf` and a Master Hub card added ("Everything Atlas One handles (public page)", Quoting & Proposals section); Portal rebuilt (44 tools).
- Renders looked at: `repo:_briefs/assets/run-ghl-jobs/shots/what-we-do-1440-top.png`, `-1440-full.png`, `-390-top.png`, `-390-full.png`; print pages at `repo:_briefs/assets/run-ghl-jobs/print-page-1.png`, `print-page-2.png`.
- Two bugs caught during print QA and fixed before shipping: two `<h2>` elements carried an inline `color:#fff` that is invisible against the print stylesheet's white navy-section background (removed, since the class already supplies the right color in both media); the two-column documents list lost its print font-size override because it was set on the parent instead of the `<li>` (fixed).

## Job A: census tool, retired Zoom Scheduler links

`06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html` and `repo:census/index.html` both had two links to `scheduler.zoom.us/david-taylor-qp71rc`; both replaced with `https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp` in both files. The two files remain byte-identical (`diff` confirms). Rendered offline at 390 px, no console errors. Portal rebuilt.

## Job B: RUN-AC-report.md dollar figures + CLAUDE.md rule

RUN-AC-report.md had lost every dollar amount to an unquoted heredoc (a `$99` vanished, a `$0` ran as a shell command and printed `/bin/zsh`). Repaired, cross-checking each figure against its source:

| Location | Was | Now |
|---|---|---|
| Assumption 4 (Cockpit membership tiers) | `(/bin/zsh /  /  / /bin/zsh)` and blank prices | Essential $99/mo (setup waived), Professional $399/mo ($495 setup), Enterprise $999/mo ($995 setup), Concierge $1,900/mo ($1,500 setup) |
| Assumption 13 (1099-NEC threshold, Nevada rate) | "rising to ,000" / "flat .00 rate" | "$2,000" / "$12.00" |
| Assumption 16 (COI phase 2 pricing) | "( /  a month,  setup)" | "($49/$99 a month, $250 setup)", taken from `coi-collection-phase-2-spec.md`'s own pricing section |
| Question 5 (same pricing, restated) | "the  /  pricing idea" | "the $49/$99 a month, $250 setup pricing idea" |
| Question 8 (Vercel tier) | "Pro ( a month)" | "Pro ($20 a month)" |

I could not recover the exact *retired* tier figures the Cockpit used to show (only the current, correct figures were given in the brief), so Assumption 4 now describes them generically ("an older set of tier prices") rather than guessing numbers. `repo:CLAUDE.md` gained a line: always write reports and logs with a quoted heredoc (`<<'EOF'`) or a file write tool, never an unquoted one, so dollar signs survive. This job touched only OneDrive files plus CLAUDE.md; nothing else in the repo changed.

## Job C: Google Fonts sweep, 27 files outside `CAL/`

All 27 files from the Run AB report's list still linking Google Fonts (`fonts.googleapis.com` / `fonts.gstatic.com`) were swept: each backed up to `OneDrive:_to_delete/superseded-2026-09-13/fonts-before/<same path>`, the `<link rel="preconnect">` and `<link href="...css2...">` tags removed, and the same Horas + DM Sans (400/700) base64 `@font-face` block used everywhere else in the kit inserted as an additive `<style id="a1fonts-2026-09-13">` before the page's own stylesheet. Every file rendered offline at 390 px afterward.

| File | Result |
|---|---|
| `_INTERNAL (do not share)/Atlas_One_Commission_Revenue_Tracker_INTERNAL.html` | Fonts embedded. scrollWidth 946 at 390 px, unchanged from the pre-fix render (948) — a pre-existing fixed-width layout, not caused by this job |
| `_INTERNAL (do not share)/Atlas_One_Cornerstone_Strategy_INTERNAL.html` | Fonts embedded, 390, clean |
| `_INTERNAL (do not share)/Atlas_One_Jotform_Decision_INTERNAL.html` | Fonts embedded, 390, clean |
| `_INTERNAL (do not share)/Atlas_One_Screening_Pricing_Calculator_INTERNAL.html` | Fonts embedded. scrollWidth 699, unchanged from pre-fix (698) — pre-existing |
| `_INTERNAL (do not share)/Command Center (superseded)/atlas-command-center.html` | Fonts embedded, 390, clean |
| `01 Website Pages/labor-law-posters-safety.html` | Fonts embedded, 390, clean |
| `01 Website Pages/templates.html` | Fonts embedded, 390, clean |
| `05 Build Specs (for BRJ)/.../Retention Scorecard (Atlas One).html` | Fonts embedded, 390, clean |
| `08 ROI Quote Master Template/Atlas_One_How_To_Build_A_Quote.html` | Fonts embedded, 390, clean |
| `08 ROI Quote Master Template/Atlas_One_Quote_and_ROI_Builder.html` | Fonts embedded. scrollWidth 403, essentially unchanged from pre-fix (400) — pre-existing |
| `09 Quick Quote Tool/Atlas_One_Quick_Quote.html` | Fonts embedded, 390, clean. `--mono` (DM Mono, used for prices/tape) is not embedded and falls back to its existing system stack (`SFMono-Regular, Menlo, monospace`); brand rule only requires Horas/DM Sans (Assumption 2) |
| `09 Quick Quote Tool/Atlas_One_Quick_Quote.PRE-PRICING-2026-08-28.html` | Fonts embedded, 390, clean, same DM Mono note |
| `10 Health Comparison Tool/Atlas_One_Health_Quote_Tool.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/_HANDOFF BRJ 2026-08-27/Atlas_One_Bookkeeping_Intake_Form.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/_HANDOFF BRJ 2026-08-27/Atlas_One_PEO_Intake_Form.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Atlas_One_Booking_Confirmation.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Atlas_One_Email_Assistant_Install_Support.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Atlas_One_GHL_Build_Playbook.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Bookkeeping_Intake_Form.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Email_Assistant_Setup_Intake.html` | Fonts embedded, 390, clean |
| `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_Get_Quote.html` | Fonts embedded, 390. This page embeds a live GHL form (`link.msgsndr.com`, `api.leadconnectorhq.com`); it already made external requests before this job (19, mostly the old Google Fonts plus the GHL embed) and still does after (48, all GHL/iframe, none to Google Fonts) — it is a live-form wrapper by design, not an offline tool, so "no network" does not apply to it |
| `12 GHL Setup doccs/Branded Intake Forms/Atlas_One_PEO_Intake_Form.html` | Fonts embedded, 390, clean |
| `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Atlas One Business Tools (17 generators).html` | Fonts embedded, then fixed: this file's *first* literal `<style` in the source sits inside a jsPDF iframe-helper string (the same trap Run AC's job 1 hit on the `CAL/` copy), so the naive insertion landed mid-JavaScript-string and threw a syntax error. The file already carried its own Horas + DM Sans `@font-face` block later in the document (from the earlier `CAL/` fix, copied into this BRJ bundle); re-applied the fix as link-removal only, no duplicate font block. Re-rendered clean, 390, 0 errors |
| `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Retention Scorecard (Atlas One).html` | Fonts embedded, 390, clean |
| `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/Retention Scorecard (Espanol).html` | Fonts embedded, 390, clean |
| `Atlas One — Complete Kit for BRJ/2. Interactive Tools (embed these)/templates.html` | Fonts embedded, 390, clean |
| `Atlas One — Complete Kit for BRJ/8. Labor Law Posters/labor-law-posters-safety.html` | Fonts embedded, 390, clean |

Portal rebuilt after the sweep (44 tools, unchanged count since no files were added or removed from the catalogue, only edited in place). None of these 27 files live in the git repo, so nothing was committed or pushed for this job.

## What was looked at

- `repo:_briefs/assets/run-ghl-jobs/shots/what-we-do-1440-top.png`, `-1440-full.png`, `-390-top.png`, `-390-full.png`, `print-page-1.png`, `print-page-2.png`.
- All 27 job-C files rendered at 390 px, screenshots in `repo:_briefs/assets/run-ghl-jobs/shots/jobc/` (one per file, backup-vs-live comparison run in-session for the four flagged rows above).
- Portal reopened after each rebuild; `<title>` stamp and tool count confirmed each time (44 tools, "REBUILT September 13, 2026").

## Assumptions

1. **OG image content.** The brief says "the laptop mark on off-white"; there is no file literally named "laptop mark". I used the brand Logo Mark (the icon that appears in every tool's header bar), full colour, centred on `#FAFAF8`, since that is the mark used everywhere else on these pages. `A1_Final Brand/4. Images/Laptop.png` (a stock photo of a laptop) was not used, since a photo does not read as a "mark".
2. **Quick Quote's `--mono` (DM Mono) was left un-embedded** in the two Quick Quote files fixed in Job C. The brand rule (Horas headlines, DM Sans body) does not mention a monospace face; DM Mono already has a full system fallback stack (`SFMono-Regular, Menlo, monospace`) so the page still reads correctly offline, just not in the exact DM Mono glyphs. Flagged at the end of the Job C table above rather than guessed at silently.
3. **What-we-do page content scope.** Six division cards show every Quick Quote service **except** the four membership tiers (moved to the Audit Guarantee band, where the brief separately asks for tier names) and six Business Consulting items that duplicate the Documents section (handbook, handbook update, safety manual, safety update, contract build, contract bundle) to avoid saying the same document twice on one page. The AI Email Assistant's two tiers (Essentials/Professional) and the three bookkeeping sizes (Small/Medium/Large) are shown as one consolidated line each, since the page names services, not tiers.
4. **Section 5's "member calculators and builders" grouping** was built from `_INTERNAL/build_portal.py`'s catalogue, excluding every item marked "Internal" in that file (Quick Quote itself, the Benefits Routing Tool, the Prospect Onboarding Tracker, Command Center) since those are not member-facing, and excluding the AI one-pagers (internal sell sheets, not member tools).
5. **Print layout** targets 2 pages by removing the forced page-break-after on the hero section that an earlier draft had (it produced 3 pages: a short page 1 and a slightly-too-long page 2 spilling to a page 3); letting the content flow naturally against `@page{margin:0.35in}` lands it at exactly 2.
6. **Job A**: only the census tool's two named files were touched, per the brief; no other file in the kit still references `scheduler.zoom.us/david-taylor-qp71rc` was searched for for this job (out of the brief's stated scope).
7. **Job B**: the *retired* Cockpit tier prices that got corrupted could not be reconstructed from the brief (it only supplied the current correct figures), so Assumption 4 in RUN-AC-report.md now describes them without inventing numbers. See the table above.
8. **Job C scope**: exactly the 27 files named in the Run AB report list; no other file in the kit was scanned for stray Google Fonts links.

## Questions for David

1. **OG image**: is the brand Logo Mark on off-white (Assumption 1) the right look, or did "the laptop mark" mean something else, such as the `A1_Final Brand/4. Images/Laptop.png` lifestyle photo?
2. **What-we-do page division cards**: happy excluding the four membership tiers and the six document-type consulting items from the six division cards (Assumption 3), or should everything from Quick Quote appear there even if it repeats what is already named in the Documents section?
3. **DM Mono in the two Quick Quote files** (Assumption 2): worth embedding, or is the system monospace fallback fine since it is only used for numeric price displays?
4. **RUN-AC-report.md Assumption 4**: the exact retired tier prices that were corrupted are gone; fine as rewritten (generic, no invented numbers), or do you remember what they were so I can put them back precisely?
5. **The what-we-do page's 200 check**: still pending as of the end of this run (see the note under the main build above). Worth a look at `https://forms.atlasonesolutions.com/what-we-do/` next time you are near a browser; if still 404, an empty commit and push usually clears it.
