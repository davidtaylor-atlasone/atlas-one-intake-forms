# BRIEF for the GHL-JOBS terminal: Run AU (Pax8 flow-down into the agreement set)

Terminal name: GHL-JOBS. Files, code and headless Chromium only. Never the GoHighLevel browser. Build end to
end, no questions, answer every permission prompt yourself, assumptions logged, questions at the END of the
report. Live log `_BUILD-LOG/TERMINAL-GHL-JOBS-live.md`; report `_BUILD-LOG/RUN-GHL-JOBS-report.md` (quoted
heredoc). Back up the prior report to `_to_delete/superseded-2026-09-15/prior-reports/RUN-GHL-JOBS-report-RunAT.md`.
One terminal at a time on OneDrive. Commit and push. Clients are in all 50 states; never write "Utah" client-facing.
Context: Pax8 (the distributor behind the Microsoft 365 and other software Atlas One resells) changed its Partner
Terms effective 2026-09-15. Summary and the exact clauses to pass down: `_BUILD-LOG/pax8-partner-terms-2026-09-15.md`.

## Job 1: Software and Licenses Schedule + master agreement additions
Generator: `_INTERNAL (do not share)/tools/agreements/generate.py` (Run AT's HTML-to-PDF path; keep it).
1. New `Atlas_One_Software_and_Licenses_Schedule` (docx + PDF, one page, "ATTORNEY REVIEW PENDING" banner):
   what is covered (subscriptions and licences Atlas One resells or provisions, named by product, never by
   distributor); the client accepts the product vendor's terms by reference and may not resell or redistribute;
   commitment term matches the vendor term, annual products auto-renew and cannot be cancelled mid-term, the
   client owes the full term if it leaves early; seat counts, additions and true-ups are the client's
   responsibility and are billed as they happen; vendor price changes pass through with 30 days notice; auto-pay
   (ACH or card in GHL) is required for resold software; Atlas One provisions and supports the tenant, the
   vendor provides the service; on termination the client keeps its own data and tenant per the vendor's terms.
   Prices come from `prices.json` (add a software section: Microsoft 365 plans and any other resold products at
   the client prices in Quick Quote; if Quick Quote has no line for a product, print "quoted" and list it in
   the report).
2. Master Client Services Agreement: add (a) a client indemnity for third-party claims arising from the
   client's misuse of resold products or AI output, viruses the client introduces, or violation of a vendor's
   product terms; (b) a liability cap for resold software equal to the fees the client paid Atlas One for that
   product in the two months before the claim; (c) late fee clause changed to "1.5% per month on amounts more
   than 15 days past due, or the highest rate the law allows" (fill the bracket; this matches the distributor
   terms and is David's recommended default pending his answer); (d) a sentence that AI features inside resold
   products can produce inaccurate output and the client keeps a human in the loop.
3. Hold Harmless and Acknowledgement: extend the AI acknowledgement from "Atlas One assistants" to "any AI
   product or feature Atlas One provides or resells".
4. Regenerate every docx and PDF, check BaseFont on two PDFs (Horas and DM Sans only), render page one of
   the new schedule and the master agreement to PNG and look at them, no dashes anywhere. Update
   `Atlas_One_Agreements_How_They_Fit.md` and `catalogue.py`; rebuild COMMAND.

## Job 2: the software cards notice (files only; PORTAL and GHL do the UI)
Write `cadence-emails-2026-09-13/software-terms-line.md`: the one-line notice "Annual licences renew
automatically and cannot be cancelled mid-term; by ordering you accept the product vendor's terms" and a
two-sentence plain explanation, for the PORTAL terminal (software cards) and the GHL terminal (Form C1
software block first-field label) to paste. No build beyond the file.

## Report
Built, Retired, Verification (BaseFont proof, PNGs looked at), Assumptions, Skipped, Questions for David
(include any resold product with no price in Quick Quote).
