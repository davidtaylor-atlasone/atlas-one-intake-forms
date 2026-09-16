# BRIEF for the GHL-JOBS terminal: Run AY (small: portal link in Your queue)

Run AX is done and audited (COMMAND filter, light theme, text sizes, Your queue, GL prices, discount line). Answers
to its questions: (1) the client portal admin link is https://portal.atlasonesolutions.com (David signs in as
david@atlasonesolutions.com); (2) keep one GL row in Master Pricing V8, the note column is enough; (3) the
--discount flag is fine for now, the client portal will carry discounts later.

Terminal name: GHL-JOBS. Files and code only. Back up the prior report to
`_to_delete/superseded-2026-09-16/prior-reports/RUN-GHL-JOBS-report-RunAX.md`. Commit and push.

## Job 1
In `_INTERNAL (do not share)/catalogue.py` add a link entry "Client portal (admin sign-in)", URL
https://portal.atlasonesolutions.com, blurb "The live client portal. Sign in as david@atlasonesolutions.com to see
what any client sees and to switch their tools on.", division Intake & Client, audience internal, queue=True,
queue_order after the three AI Email Assistant links, pinned. Remove the queue flag from "Client Dashboard (GHL)"
(keep the entry, keep it pinned). Rebuild COMMAND, run catalogue_check.py, verify in headless Chromium at 1440
and 390 that Start here shows "Your queue" with four rows and the new link opens in a new tab. Screenshot in
`_briefs/assets/run-AY/shots/`.

## Report
Built, Verification, Assumptions, Questions for David.
