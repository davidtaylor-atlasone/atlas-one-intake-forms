# Cockpit catalog vs Quick Quote service list, 2026-09-17 (Run BF)

Quick Quote (`09 Quick Quote Tool/Atlas_One_Quick_Quote.html`, the SERVICES array, 104 rows) is the source of
truth for which services Atlas One sells and at what price. This is a full diff of every row in the Quote
Cockpit's catalog (`08 ROI Quote Master Template/Atlas_One_Quote_Cockpit.html`, the `cat()` function, 31 rows)
against it, by matching service name and concept.

Three retired items were already pulled out ahead of this diff (see the report): AI Email Concierge ($649),
Employee Handbook basic ($299) and Safety Manual basic ($299). Those do not appear below since they no longer
exist in either tool.

## (a) Rows that match

| Cockpit row | Cockpit price/model | Quick Quote row | Quick Quote price/model | Note |
|---|---|---|---|---|
| mem (Membership) | $99 / $399 / $999 / $1,900 per mo | mem_ess / mem_pro / mem_ent / mem_con | same four figures | generated from prices.json (Run BE) |
| certpay | $125/mo per active job | cert_payroll | $125/mo per active job | generated from prices.json |
| ats | $95/mo | ats | $95/mo | |
| hbCustom (Employee Handbook, custom) | $950 setup | handbook | $950 one time | generated from prices.json |
| newhire | $20/hire | onboard | $20/new hire | |
| scorp | $250/quarter | scorp | $250/quarter ($83.33/mo amortized) | same figure, different unit label |
| qfile | $130/filing | quarterly | $130/quarter ($43.33/mo amortized) | same figure |
| f1099 | $75 setup | filing_1099 | $75 setup | |
| safeCustom (Safety Manual, custom) | $1,200 setup | safety | $1,200 one time | generated from prices.json |
| safeTrain | quoted | safety_train | quoted | |
| aiemail (AI Email Assistant) | $249/mo, $750 setup, +$75/extra mailbox | ai_email_ess / ai_email_pro | $249 / $499 per mo, $750 setup, +$75/mailbox | generated from prices.json; Concierge tier removed this run |
| aitask (AI Task Agent) | $99/mo (bundled default) | ai_tasks | $199 standalone, $99 bundled | Cockpit's default matches the bundled figure |
| qbo | $38/$85/$140/$340 by plan | qbo | same four figures | generated from prices.json |
| m365basic/std/prem/copilot | $7/$14/$22/$21 per user | m365_basic/standard/premium/copilot | same four figures | generated from prices.json |
| tax | quoted | tax | quoted | |
| cfo | quoted | cfo | quoted | |
| wcaudit | quoted (WC audit dispute/reconciliation) | wc_audit | quoted, 25% contingency | |
| ins (P&C lines, itemized: GL, E&O, Property, Cyber, Bonds, etc.) | all quoted | gl, eo, cyber, keyman, bonds | all quoted, itemized as separate rows | Cockpit bundles what Quick Quote lists as five separate quoted rows; both are "quoted", no number to reconcile |
| crm | quoted | crm | quoted | |
| qbtime | quoted | qb_time | quoted | |
| vaudit | quoted | vendor_audit | quoted | |
| jot (Jotform forms, itemized Bronze/Silver/Gold/Enterprise) | $34/$39/$99/quoted | sw_marketplace | quoted ("any other cloud product ... sourced through our marketplace partner") | Quick Quote has no named Jotform row; it covers resold software generically. Jotform's own itemized tiers are Cockpit's own vendor pricing, not something Quick Quote prices at all, so there is nothing to conflict with. Left in place. |
| ta (Time & Attendance, itemized: Essentials/Standard/Advanced/SwipeClock/Connecteam x3/TLM/QB Time/Prism HCM) | $3 to $12/EE/mo by vendor | connectteam | $5/EE/mo (Operations Hub) | The one line that overlaps (Connecteam Operations Hub, $5) matches exactly. The rest of the list is Cockpit's own vendor comparison, not itemized in Quick Quote. Left in place, same treatment as the bookkeeping anchors below. |
| screen (Background & drug screening, itemized 17 check types $10 to $65 each) | itemized per type | bg_check ($30/test), drug ($20/test) | flat per test | Quick Quote prices two flat categories; the Cockpit itemizes actual vendor line items within them for internal quoting. Not a like for like number to fix. Left in place. |
| bk (Bookkeeping, anchors Small $600/Medium $1,500/Large $2,500) | flat anchors | books_s/m/l | $300 to $1,000 / $1,000 to $2,000 / $2,000 to $3,000 (ranges) | Per Run BE and this brief: the Cockpit's flat anchors sit inside Quick Quote's quoted ranges and may stay as the Cockpit's own editable starting points. |
| whset / whboth | $250 / $500 setup | wh_setup | quoted, no default | Quick Quote leaves this fully quoted; the Cockpit's defaults are a reasonable starting point, not a conflicting number. Left in place. |

## (b) Rows fixed to match Quick Quote

| Cockpit row | Old | New | Fixed through |
|---|---|---|---|
| k401 (401(k) administration) | setup $350 | setup $450 | hand edit in the Cockpit's `cat()` (not prices.json generated; prices.json has no retirement section) |
| qbgl (QuickBooks integration / GL export-import) | $0/mo, $0 setup (fully quoted) | $50/mo, $250 setup | build_cockpit.py now reads prices.json's `gl_import.monthly` and `gl_import.setup`, new `GL_IMPORT_PRICE`/`GL_IMPORT_SETUP` constants, matching Quick Quote's `gl_import` row ("Payroll to GL import", $50/mo default, $250 setup) |
| strat (Business strategy consulting) | $0/mo (fully quoted) | $250/mo shown as the per hour rate field | hand edit in the Cockpit's `cat()`; Quick Quote's `strategy` row defaults to $250/hour, billed per hour typed in |

## (c) Rows in the Cockpit with no Quick Quote counterpart

None. Every Cockpit row maps to either a specific Quick Quote row or one of Quick Quote's generic "quoted"
catch-alls (software marketplace, general liability and related insurance lines, withholding setup). Nothing
was removed under this heading.

## What this run did not touch

- Sub-option vendor lists (TALINES, SCREEN, INSLINES, JOTF's own tiers, the m365/QBO/AI Email pick lists) stay
  as the Cockpit's own itemized, editable pricing tools. Quick Quote does not itemize at that level, so there is
  no single number to reconcile against; only the one line in each that does overlap Quick Quote (Connecteam,
  the flat AI Email/QBO/M365 figures) was checked and already matched or was already fixed in Run BE.
- "apar" (A/P + A/R management) bundles what Quick Quote prices as two separate rows, `ap` and `ar`, $250/mo
  each. The Cockpit shows it as a single fully quoted line ($0). Left alone rather than guessing whether the
  right default is $250 or $500; flagged in Questions for David below.
