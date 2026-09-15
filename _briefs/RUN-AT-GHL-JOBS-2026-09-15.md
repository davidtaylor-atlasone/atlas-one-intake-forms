# BRIEF for the GHL-JOBS terminal: Run AT (fix the agreement fonts, build the web pitch page)

Terminal name: GHL-JOBS. Files, code and headless Chromium only. Never the GoHighLevel browser. Build end to
end, no questions, answer every permission prompt yourself, assumptions logged, questions at the END of the
report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; report `_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted
heredoc). Back up the prior report to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAS.md`.
One terminal at a time on OneDrive; no parallel forks that move files. /compact between jobs. Commit and push.
FACT for every client-facing word you write: Atlas One serves clients in all 50 states. Never write "Utah
businesses"; "serving businesses in all 50 states" is fine. Lehi, UT is the office address only.

Master Kit: `~/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit/`
A1_Sales: `.../2. Atlas 1 Solutions Marketing/A1_Sales/`   Repo: `~/Projects/atlas-one-intake-forms`

## Job 1: the Run AS PDFs are in the wrong fonts (Cowork audit 2026-09-15 09:30)
Every PDF in `A1_Sales/A1 Agreements/2026-09-15 masters/` embeds FrankRuhlHofshi and LinuxLibertine, not DM Sans
and Horas (checked with `strings <pdf> | grep BaseFont`). The Run AS report's claim that the brand fonts were
installed for LibreOffice is wrong on this machine. Fix it properly:
- Make the docx masters reference the exact font family names in the TTFs (`DM Sans`, `Horas`), install the
  TTFs into `~/Library/Fonts/`, run `fc-cache -f` if fontconfig is present, and confirm with
  `soffice --headless --convert-to pdf` on ONE file, then `strings out.pdf | grep BaseFont`: it must list
  DMSans and Horas subsets and nothing else (OpenSymbol allowed). If LibreOffice still substitutes, switch the
  PDF step to the bookkeeping-docs pipeline (render the same content to HTML with the embedded @font-face
  block and print with Playwright), keeping the docx as the editable master.
- Regenerate all 19 PDFs, re-render page one of each with `sips` to PNG and LOOK at them (headings in Horas,
  body in DM Sans). Move the wrong-font PDFs to `_to_delete/superseded-2026-09-15/agreements-wrong-fonts/`.
- Rebuild COMMAND. Report the BaseFont list for two PDFs as proof.

## Job 2: the web pitch page (spec: `claude/jason-petty-web-deck-review-2026-09-15.md`, copied below)
Build `tools/pitch/index.html` in the repo (live at https://forms.atlasonesolutions.com/tools/pitch/ on push).
- Source of truth: the 16-slide Prospect Pitch Deck (`A1_Sales/A1_Pitch Decks Inv/Atlas_One_Prospect_Pitch_Deck.pptx`,
  find it by name if the folder differs). Extract every slide's text with python-pptx into
  `tools/pitch/slides.json` (one object per slide: title, body lines, notes). The page renders from that
  JSON; never hand-type slide copy into the HTML.
- Tabs across the top on desktop, a dropdown on phone: Overview, The problem, Six divisions, How it works,
  A sample number, Proof, Membership, Next step (map the 16 slides into those eight tabs; keep every slide's
  content, group where it belongs). One screen per tab, no scrolling walls at 1440; the phone may scroll.
- `?for=Company&ee=25&industry=construction` personalizes the header ("Prepared for Company") and the
  sample-number tab: run the same math the Total Impact Model page runs (`A1_Sales/Total Impact Model/
  build_tim.py` or the page itself; reuse its formulas, do not invent new ones). Without parameters, show the
  25-employee sample the deck already uses.
- Membership tab: only Essential $99 and Professional $399 with setup fees; Enterprise and Concierge read
  "Built around your business. Starts with a 30 minute Back Office Audit." (website decision 2026-09-13).
- Brand: four colours, Horas + DM Sans embedded as @font-face data (copy the block from
  `tools/self-assessment/index.html`), laptop logo mark, tagline in the header, no vendor names, no dashes,
  "Serving businesses in all 50 states" in the footer, phone 380-225-5217 (tel:+13802255217), a booking
  button on every tab (https://api.leadconnectorhq.com/widget/groups/book-david), Download PDF button
  linking to `tools/pitch/Atlas_One_Prospect_Pitch_Deck_First_Meeting.pdf` (copy the current PDF from
  A1_Sales), Print stylesheet. Zero external requests other than the booking link click.
- Verify: 1440 and 390, light and dark, zero console errors, scrollWidth equals viewport at 390, screenshots
  in `_briefs/assets/run-AT/shots/`, every tab opened, one `?for=` render. Add the page to `catalogue.py`
  (Sell & Pitch) and rebuild COMMAND. Commit and push; confirm the live URL returns 200 (propagation lag is
  fine, say so).

## Report
Built, Retired, Verification (BaseFont proof, PNGs looked at, URLs), Assumptions, Skipped, Questions for David.
