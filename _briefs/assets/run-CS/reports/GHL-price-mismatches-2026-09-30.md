# GHL products versus prices.json V9 (written by GHL-JOBS Run CS, 2026-09-30)

For the GHL lane (A1 GHL how-to chat and terminal). GHL-JOBS did NOT open GoHighLevel and did NOT call its API.

## Where this comes from, and its limit
The locked price book (`price-book-locked-2026-09-30.md`) does not contain a GHL product list, so this comparison is built
from the GHL lane's own records on disk: the 2026-09-15 read of all 21 products (`TERMINAL-GHL-live.md` Run BA Part 9),
the Part 17 additions (31 products), the Run CM Job 3 additions (45 products, 2026-09-27) and the Job G1 product made on
2026-09-28 (Bookkeeping with bill pay). It is NOT a live read. The GHL lane must confirm each row against the live
Payments > Products list before changing anything. Source of truth for every number: `_INTERNAL (do not share)/tools/agreements/prices.json` V9.

Status key: MATCH (price and wording agree), MISMATCH (change it), MISSING (no product found in the logs, add it),
VERIFY (the log does not record enough to tell).

## Mismatches (change these)
| GHL product (as logged) | In GHL | prices.json V9 | Change |
|---|---|---|---|
| Handbook annual update | $250.00 | Handbook update, $250 per update, ONE TIME, included at Professional and above | Rename to "Handbook update", make it a one time price, not annual or recurring |
| Safety manual annual refresh | $300.00 | Safety manual update, $300 per update, ONE TIME, included at Professional and above | Rename to "Safety manual update", one time price, not annual or recurring |
| Certified payroll per active job | $125.00 a month | Certified payroll (WH-347) state monthly job $125 a month per active job | Price agrees. Rename to say "state monthly job"; the federal weekly job ($250 a month) is a separate product, see Missing |
| Agreement build (contractor, W-2 at-will, or NDA) | $450.00 | $450 each for W-2 at will, 1099 contractor, NDA, offer letter and commission agreement | Price agrees. Add offer letter and commission agreement to the product name or description |
| Atlas One Membership: Professional (description) | $399 a month | Professional includes 3 hands on hours a month and a quarterly review; "10 tickets" and the monthly advisory call are retired | VERIFY the description text in GHL and replace any "10 tickets" or "monthly advisory call" wording |
| AI Task Agent (2 prices) | two prices, amounts not logged | $199 a month standalone, $99 when bundled with the AI Email Assistant or on Enterprise, included in Concierge | VERIFY the two amounts are $199 and $99 and that the description says "$99 on Enterprise" and "included in Concierge" |

## Missing from GHL (add these)
| Product | prices.json V9 |
|---|---|
| Payroll tax account setup, state withholding | $250 per account, one time |
| Payroll tax account setup, state unemployment | $250 per account, one time |
| Additional local or state tax account setup (for example Nevada MBT) | $50 per account, one time |
| Expedited payroll tax account setup | plus $100 per account |
| Payroll through Atlas One Bookkeeping, monthly minimum | $100 a month (monthly cycle), billed as the greater of the minimum or $30 per employee |
| Payroll through Atlas One Bookkeeping, monthly minimum, other cycles | $150 a month (semi monthly, bi weekly, weekly) |
| Payroll through Atlas One Bookkeeping, per employee rates | $30 per employee per month, $15 per employee per pay period semi monthly or bi weekly, $7.50 weekly |
| Payroll setup, quarterly filing, new hire onboarding | $199 one time, $130 per filing, $20 each |
| Year end W-2s | One additional payroll run at the client's rate (no separate price, bill as a run) |
| Certified payroll (WH-347) setup | $300 one time per company |
| Certified payroll per report | $60 per report |
| Certified payroll federal weekly job | $250 a month per active job |
| Certified payroll done for you | $400 a month per active job |
| A/R added to bookkeeping with bill pay | $250 a month |
| A/P or A/R standalone | $250 a month each |
| Handbook, basic generated from your answers | $299 one time |
| Safety manual, basic generated from your answers | $299 one time |
| Same day rush on any document | $150 |
| Advisory and support beyond the allowance | $150 an hour, 15 minute increments, 30 minute minimum |
| Strategy consulting | $250 an hour |
| AI Task Agent, on Enterprise | $99 a month (can be a price on the existing AI Task Agent product) |

## Matches (no change)
Membership Essential $99 a month. Membership Professional $399 a month with Setup: Professional $495. Membership Enterprise with
Setup: Enterprise $995. Membership Concierge / Fractional COO $1,900 a month with Setup: Concierge $1,500. AI Email Assistant
Essentials $249, Professional $499, extra mailbox $75, setup (two prices, $750 and $999: VERIFY). AI Task Agent setup $500.
HR policy or document design $175. Agreement bundle (all three) $1,200. Safety Manual Builder (OSHA, bilingual) $1,200 and
Employee Handbook Builder (bilingual, 50 state) $950 (David is checking whether the portal shows a higher handbook number; the
price book says $950). Payroll to GL Converter monthly $50, semi monthly or bi weekly $75, weekly $125, setup $250, extra entity or
state $25. Payroll to GL import run by Atlas One $35 per run. GL import plus certified payroll setup bundle $300. Microsoft 365
Business Basic $7, Standard $14, Premium $22, Copilot $21 per user per month. Safety training program setup $295, up to 25
employees $79 a month, 26 to 75 employees $129 a month. COI tracking setup $150, up to 15 subcontractors $49, up to 50 $99, up to
100 $149 a month. Bookkeeping with bill pay $750 a month (created 2026-09-28, A/R not included).

## Not in prices.json (leave alone, or tell David)
- "Security Deposit" (0 prices): no price in the book, nothing to match.
- Annual membership prices: OPEN, David to answer. GHL already carries two prices on Enterprise; do not change them until David decides.
- Bookkeeping Small, Medium and Large products: none appear in the logs. If any exist, Small reads "Starting at $300, exact price after a
  15 minute look at your books" and Medium and Large read "Priced after a 15 minute look at your books".
- PEO, ASO, HCM, background screening and drug testing, website build, hosting and care, content and blogging: Quoted. Any GHL
  product with a number on these must lose the number.

## Invoice and agreement terms to match the price book (not products)
Net 15 on every invoice and recurring invoice template (due date set automatically 15 days from the send date), no late fee, ACH
preferred with no processing fee. The MCSA now says payment within fifteen days.
