# RUN CS generators report, 2026-09-30

## Changed (MK = Master Kit)
Proposal generator, `MK/08 ROI Quote Master Template/PEO_Proposal_Generator_V4.5_MASTER/`:
- `inputs.py`: every rate default removed (admin per check, admin percent, EPLI, ConnectTeam, 401k setup and per EE, background, drug, posters, ATS, ASO/HCM/self service constants all 0). Added `QUOTED_TEXT` and `opt1_quoted` / `opt2_quoted`.
- `peo_deck.py`: no admin rate gives a cover banner "Quoted for your company (headcount, pay cycle, PTO tracking and more)", drops the hard cost, savings waterfall and ROI slides, agenda reworded; EPLI, ConnectTeam, background, drug, posters, ATS lines say Quoted when blank; 401k slide no longer prints "$50/EE/yr, not $75 to 100".
- `light_deck.py`: ASO, HCM and self service always quoted; removed "+$2.50/EE" and "+~$8,840/yr"; fixed a crash (`inp.cs_wc_rate` never existed, ASO/HCM/self service decks could not build at all).
- `brands.py`: ONLY the "Atlas One Solutions" record: mobile and office 380-225-5217, new `tel` "tel:+13802255217". Other four records untouched (diff checked).
- `generate_proposals.py`: brand comparison deck skipped when no rate is entered.
- `WC_Master_Template.xlsx` Inputs rows 16, 17, 18, 21, 24, 25, 27 to 30 now blank, notes say "Leave blank: output says Quoted for your company"; `build_template.py` and `README.md` match.
- `service_deck.py` (and the identical copy at `A1_Sales/Dr Gould Dental/Proposal_Generator/service_deck.py`, a code file, copied over as instructed): bookkeeping Starting at $300 and priced after a 15 minute look, QuickBooks $38/$85/$140/$340, $150 advisory and $250 strategy, AI Email Assistant $249/$499, $75 mailbox, $750/$999 setup, annual pay option removed, Task Agent $199/$99/included in Concierge, setup $500, handbook and safety updates "included at Professional and above", WC flat fee $495 row replaced with "nothing owed".

Agreements generator, `MK/_INTERNAL (do not share)/tools/agreements/generate.py` (prices already came from prices.json V9):
- MCSA clause 2: payment within fifteen days (was ten). No late fee text anywhere.
- Membership Schedule: new clause 3 (3 hands on hours a month, quarterly review, updates included at Professional and above, $150 and $250 hourly). Sample Membership proposal: "10 tickets" and monthly advisory call gone, now 3 hands on hours and quarterly review.
- WC Audit Schedule note now says 25 percent of premium recovered, nothing owed if none (an internal "confirmed by David" note was removed). Sample proposal billing text says the same.
- Bookkeeping Schedule gets the strategy consulting row; AI Services intro no longer cites "Quick Quote catalogue"; Document Services sample says updates included at Professional and above.
- Regenerated all 22 documents (DOCX + PDF) into `A1_Sales/A1 Agreements/2026-09-15 masters/`.

## Retired (copied before overwrite, originals now overwritten in place)
- Old agreements DOCX/PDF (44 files) to `MK/_to_delete/superseded-2026-09-30/agreements-before-V9/`.
- Generator files to `MK/_to_delete/superseded-2026-09-30/proposal-generator-before-V9/`; Gould service_deck.py to `.../gould-service-deck/`.

## Looked at
- `/Users/davidtaylor/Projects/atlas-one-intake-forms/_briefs/assets/run-CS/shots/generators/cover_PEO_Option1_no_rate.png` (cover shows 380-225-5217 and the Quoted phrase, no rate), `price_bookkeeping.png`, `price_task_agent.png`; test decks (PEO Option 1, five service decks) in the same folder.
- All 5 decks (PEO 1 and 2, ASO, HCM, Self Service) text scanned: no $25, 0.95, $11, $40, $20, $95, $350, 0.12 percent. PDF text of all 22 agreement PDFs grepped: no late fee, ten days, 10 tickets, advisory call, retired prices.

## price_scan (my files)
Before: not measured separately; generators printed many retired prices. After: 0 hits in the proposal generator folder and in the masters folder. agreements/ folder shows 5 hits, all inside `prices.json` changelog text (lead owned).

## Assumptions
1. Atlas phone printed as 380-225-5217 (mobile and office); people.json still prints "380-CALL-A1S (380-225-5217)" as the office line.
2. Workbook rate cells blanked with openpyxl; the _GenMap cached values are dropped but inputs.py already falls back to Inputs.
3. ASO/HCM/Self Service have no workbook rate input so are always quoted.
4. Handbook plus safety bundle "$1,950 saves $200" removed (not in the price book), shown as $2,150.
5. "A/P and A/R included at Medium and above" replaced with "Scoped at your books review" (not in the price book).
6. Test decks use a blank WC sheet, so WC slides show $0 (no data), unrelated to rates.

## Skipped
- Em dashes and "$7,200 at $50/hr loaded cost" (time savings assumption) remain in other deck copy of PEO and service decks; the PEO palette also uses red and green panels (pre-existing brand issue).
- MCSA says "a Utah limited liability company" and Utah governing law (entity facts, left).
- Loose `A1 Agreements/Atlas_One_AI_Services_Schedule.docx`, Gould documents, Bookkeeping Packet, Quick Quote: not touched.

## Questions for David
1. Should the Handbook plus Safety manual bundle be a price (we show $2,150 sum)?
2. Do Medium and Large bookkeeping include A/P and A/R, or is it bill pay at $750 plus A/R $250 only?
3. Annual plan wording is still open; I printed none.
