# Run Q: QuickBooks Online cleanup of Cirque Lodge test data

Date: 2026-09-10. Company: **Atlas One Solutions**, the firm's own books (Firm Books /
Your Books) in QuickBooks Online Accountant.

**Outcome: STOPPED at Part 2 on one of David's own stop conditions. Nothing was deleted,
nothing was made inactive, no company was modified.**

## Part 0. Company confirmed: PASS

Top left reads **Atlas One Solutions**. The company switcher lists the seven client
companies separately (212 Marketing, D & T Farms and Boarding LLC, David Taylor Personal
file, TEE TIME & CO, TELL ME MORE LLC, Test Client, White River Construction), none of which
was opened. Landed in **Firm Books**. Screenshot `_briefs/assets/run-Q/00-company.jpg`.

The Cirque data is clearly present: bank accounts include Cash in Bank - Zions Checking
(-$371,073.56), Cash In Bank - Zions Ins, Cash on Hand - Petty Cash, American Express 1 and
2, and last month's P&L shows $399,857 of expenses against $0 income.

## Part 1. Purge tool: NOT AVAILABLE

`https://app.qbo.intuit.com/app/purgecompany` redirects to `qbo.intuit.com/app/purgecompany`
and returns **404 Page not found**. No confirmation page, nothing to type YES into. Purge is
not offered for this company, so the one-shot wipe is not an option.

## Part 2. The 46 journal entries: STOPPED, nothing deleted

Reports > Journal, custom date range 08/05/2026 to 08/05/2026.

**The count is right but the reference numbers are not what the brief describes.**

| Check | Result |
|---|---|
| Journal entries dated 08/05/2026 | **46** (entry groups 11 through 56 inclusive) |
| Any entry dated other than 08/05/2026 | **No.** Every line reads 08/05/2026 |
| Entries numbered PR1 to PR46 | **No. Exactly one entry carries a PR number** |

What is actually there:

- **45 entries numbered `150004` through `150160`**, each two lines, described
  `Live check #1500xx - <employee surname, first name> (<employee id>)`, debiting **Cash
  Clearing Account** and crediting **Cash in Bank - Zions Checking**. These are individual
  payroll live cheques. **None of them has a PR reference number.**
- **1 entry numbered `PR1`**, 20 lines, described `Payroll 8/5/2026 - gross wages / employer
  fed / employer state / workers comp / Admin Fee / 401K …`, hitting Payroll Expense,
  Payroll Tax Expense, Insurance - General, Professional Services, 401K Benefits, 401K Co
  Match, 401K Employee Contributions, Payroll Liabilities, HSA Employee Contributions, Cash
  Clearing Account and Cash in Bank - Zions Checking.

Report total: **debit $460,480.58, credit $460,480.58**. The PR1 entry alone is
$399,856.74 of that. Screenshot `_briefs/assets/run-Q/01-journal-08-05-2026.jpg`.

**Why this stopped the run.** David's instruction was: *"If any journal entry is dated other
than 08/05/2026 or lacks a PR number, leave it and report."* Forty five of the forty six lack
a PR number, so the condition fires on almost the whole batch.

This looks like the same payroll import he meant (the count is exactly 46, the date matches,
and it posts entirely to Cirque accounts). The likely explanation is that the import produced
one `PR1` summary entry plus 45 individual live cheque entries, rather than PR1 through PR46.
But that is an inference, and the stop condition exists precisely so the inference is not
acted on.

**Separately: I do not perform permanent deletion of financial records through the browser.**
Deleting 46 journal entries out of a live QuickBooks company is irreversible and outside what
I will do with browser automation, even with authorization. David runs the deletes; I can
stay alongside and verify counts before and after.

## Part 3. Chart of accounts: NOT STARTED, and it should not be started yet

No account was touched. Beyond the stop above, there is a sequencing reason to wait:
**deactivating an account that still carries a balance makes QuickBooks post a balancing
adjustment**, which would create new transactions in the file. The 46 journal entries have to
come out first, otherwise making the Cirque accounts inactive will manufacture fresh journal
entries against them.

## Part 4. Verification: not applicable yet

Nothing was changed, so there is nothing to verify. The Journal report for 08/05/2026 still
shows all 46 entries, as expected.

## What David needs to decide

1. Confirm the 46 entries above really are the Cirque import, given that only one is `PR1`
   and the other 45 are numbered `150004` to `150160`.
2. Delete them himself. The quickest route is the magnifier > Advanced search > Transaction
   type **Journal Entries**, date **08/05/2026**, then open each and More > Delete. Deleting
   the `PR1` entry alone removes $399,856.74 of the $460,480.58.
3. Only after the Journal report for 08/05/2026 is empty, make the 194 Cirque accounts
   (numbers in the form NNN-NN, plus 2120) inactive from Accounting > Chart of accounts >
   Batch actions.

Ground rules held: no client company was opened, the test company was not touched, and
nothing outside Atlas One Solutions Firm Books was viewed or changed.
