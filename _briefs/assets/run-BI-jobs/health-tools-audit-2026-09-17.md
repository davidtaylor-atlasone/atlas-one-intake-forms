# Health tools audit, Run BI Job 2 (2026-09-17)

Note: this job ran in two passes inside the same run (a fork restart). The first pass fixed Quick
Quote's coinsurance wording/picker, the Health Quote Tool's coinsurance display and title, and
health_compare.py's coinsurance printing; it also located a wrong path for the last file group and
flagged it as a Question. This second pass verified every one of those fixes is actually live in the
files, found and fixed two more real bugs in the Health Comparison Builder, found the correct path for
the last file group (it lives outside the Master Kit tree) and audited it, and closes the open Question
from the first pass. This is the single up to date report; do not read it as two separate audits.

2026 IRS HDHP/HSA figures (Revenue Procedure 2025-19): minimum annual deductible $1,700 self only /
$3,400 family; out of pocket maximum $8,500 self only / $17,000 family.
Source: https://www.irs.gov/pub/irs-drop/rp-25-19.pdf

## Table

| Tool | Finding | Fixed |
|---|---|---|
| `09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, Health step | Coinsurance dropdown read as a plan picker ("COINSURANCE IN YOUR PASTE MEANS", "What the MEMBER pays" / "What the CARRIER pays") | Yes, verified live: heading "How the carrier sheet shows coinsurance", options "As the member's share (10%, 20%, 30%)" / "As the carrier's share (90%, 80%, 70%)", helper line "Either way the comparison shows both, for example 80/20." |
| same, plan cards and comparison table | Coinsurance shown as a lone number | Yes, verified live: `coinsPair()` renders carrier / member everywhere (plan form, ranked table, current-plan row) |
| same, "Add one by hand" and current plan form | Coinsurance was free text, ambiguous | Yes, verified live: picker with 100%/0% through 50%/50% presets plus Other (free text) |
| same, coinsurance parser | Must accept 100, 100%, 100/0, 0 as a 100% plan | Yes, verified live: `parseCoinsOther()` handles all four, and a lone number over 50 is read as the carrier's share |
| same, HSA/HDHP hide filter | Deductible threshold | Verified live at $3,400, matches the 2026 family HDHP minimum deductible exactly (the tool stores one deductible per plan, not per tier, so the higher family threshold is the right one to avoid hiding ordinary non-HDHP PPOs) |
| `10 Health Comparison Tool/Atlas_One_Health_Quote_Tool.html` | Coinsurance shown as a lone member percent, title had an em dash | Yes, verified live: title is "Atlas One Health Quote Tool" (no dash), coinsurance renders as carrier/member pair with a hint line clarifying the member's share convention |
| `10 Health Comparison Tool/health_compare.py` | Coinsurance printed as a lone member percent in CLI output | Yes, verified live: prints carrier/member pair |
| same | Single carrier under 500 lives rule (rule 14) | Verified enforced: `SINGLE_CARRIER_MAX = 500` (line 184), used in the scoring path |
| same | One remaining em dash in a CLI print line (`COMPARABLE — {n} priced options...`) missed by the first pass | Yes, fixed this pass: `COMPARABLE: {n} priced options...` |
| `06 Calculators and Tools (NEW Aug 2026)/Health Comparison Builder (Atlas One).html` | Redirect Health catalog table showed "Member coinsurance" as a lone member percent (e.g. "20%"), the first pass's grep missed this because the field label ("Member coinsurance %") looked unambiguous even though the *displayed value* was not | Yes, fixed this pass: now renders carrier / member (e.g. "80% / 20%"), row label reworded to "Coinsurance (carrier / member)" |
| same | `#benSrc` rendered an internal broker negotiator name and an internal OneDrive folder path ("CF Partners Jack", "Atlas 1 Solutions Vendors_Brokers / 10_Broker_and_Partner_Docs") client facing, contradicting the code's own comment that this must never print | Yes, fixed this pass: `#benSrc` now stays empty, nothing internal renders |
| same | Group size note named three alt funding vendors (Redirect Health, New Journe, BeniComp) client facing, again contradicting the file's own "who quoted it is internal" comment | Yes, fixed this pass: reworded to describe alternative funding generically, matching the wording already used in the Benefits Routing Tool |
| same | Under 500 lives, one carrier rule | Verified enforced and correctly worded |
| same | Redirect Health catalog section itself (headers, doc filenames) names that one carrier by design | Not fixed, see Questions: this is the tool's whole premise (comparing that vendor's own plan designs), different from the two leaks above which were accidental |
| `06 Calculators and Tools (NEW Aug 2026)/Health Quote Census Intake (Atlas One).html` | No coinsurance display (intake form, not a comparator); phone, fonts, no CDN all correct; dashes found are only inside HTML/JS comments, never rendered | No fix needed |
| `06 Calculators and Tools (NEW Aug 2026)/Atlas_One_Benefits_Routing_Tool.html` | Rule 14 correctly encoded in both the standing-rules callout and the routing logic (`ee<500` / `ee>=500`); no coinsurance field (routes funding models, not specific plans); no vendor names client facing; no dashes | No fix needed |
| `A1_Sales/Atlas 1 Benefits/Atlas_One_Employee_Benefits_Menu.html` | Path resolved this pass (it lives under `2. A1 Official Docs/2. Atlas 1 Solutions Marketing/A1_Sales/Atlas 1 Benefits/`, a sibling of the Master Kit's HR_Docs folder, not inside the Master Kit tree, which is why the first pass's Master-Kit-only search missed it). No coinsurance field, phone/fonts/CDN/dashes/vendor names all correct. | No fix needed |
| `A1_Sales/Atlas 1 Benefits/Atlas_One_Division_Benefits_Retirement.html` | Same path note. Content clean (no coinsurance, phone/fonts/CDN/dashes/vendor names all correct). Layout: fixed `.page{width:8.5in}` print sheet does not reflow at 390px (scrollWidth 816 vs viewport 390) | Content: no fix needed. Layout: not fixed, see Questions |

## HSA / HDHP handling

Quick Quote's hide-unless-they-have-one threshold ($3,400) matches the 2026 family HDHP minimum
deductible. None of the other six files gate on a numeric HDHP threshold: Health Comparison Builder's
Redirect Health catalog rows carry a fixed `hsa:true/false` flag per named plan design rather than
deriving it from the deductible, so there was nothing to update against the 2026 figures there.

## Deductible embedded vs non embedded

None of these seven files distinguish embedded vs non embedded deductibles in copy or logic (that
distinction matters for family-tier plan design, not for the single deductible-per-plan or
enrolled-lives-count fields these tools use). Nothing to flag.

## Verification

Headless Chromium (Playwright, `file://`), 390px and 1440px, on all seven files: zero console errors,
zero non-`file://` network requests on every file, `scrollWidth` equals the viewport at both widths on
six of the seven. `Atlas_One_Division_Benefits_Retirement.html` is 816px wide at 390 (see table and
Questions, it is a fixed letter-size print sheet). Screenshots in
`_briefs/assets/run-BI-jobs/shots/` in the forms repo.

## Questions

1. Health Comparison Builder's "Redirect Health catalog" section names that carrier throughout its own
   headers and plan doc filenames by design (it is a dedicated side by side viewer for that vendor's
   own plan designs, distinct from the two accidental internal-info leaks fixed this run). Left as is;
   flagging so David can decide whether this section should become vendor neutral or stay an
   intentionally vendor specific internal viewer, and whether its GAP/ShaRx program names ever reach a
   prospect-facing export or stay in the working UI only.
2. `Atlas_One_Division_Benefits_Retirement.html` is a fixed 8.5in x 11in print sheet (a one-pager built
   to print or save as PDF), so it does not reflow to 390px width. Did not force it to be responsive
   since that risks breaking the print/PDF layout it is built for. If this needs to work as a live tool
   on a phone rather than a print/PDF handout, it needs a second, responsive layout, not a CSS tweak.
