# Run L: GHL payments. Products, payment links, invoice defaults, pay-then-deliver workflows

Location: `AzTPxnK2vSUj19jYoDmR` at app.ridethehightide.com. Date: 2026-09-10.

Ground rules honoured: only this session in GHL, no cornerstonepeo.com sending domain, no
HIPAA feature, no 15-minute calendar changes, **Payments > Integrations (Stripe, QuickBooks)
never opened**, no test invoice sent to a real contact.

Brand: logo is `_briefs/assets/a1-logomark-fullcolor-transparent.png`, the periwinkle laptop
mark. Accent `#23304D`. Never the old globe.

---

## Part 1. Products

Built in Payments > Products. Currency USD on every price. **Tax: none** (no tax category
selected, "Include tax in prices" left at As per Global Settings, no tax rates attached).

| # | Product | Price | Type | Product id |
|---|---|---|---|---|
| 1 | Atlas One Membership: Essential | $99 | recurring monthly | `6aa2fca0eeafa5298906310f` |
| 2 | Atlas One Membership: Professional | $399 | recurring monthly | `6aa2fd1f97fe7f62966dab64` |
| 3 | Setup: Professional | $495 | one time | `6aa2fd7d08d19fea4480d9b1` |
| 4 | Setup: Enterprise | $995 | one time | `6aa2fdba6c4d00c40d3acb9e` |
| 5 | Setup: Concierge | $1,500 | one time | `6aa2fdef275b2c6af20a8fe2` |
| 6 | AI Task Agent: setup | $500 | one time | `6aa2fe22118a3782883690f1` |
| 7 | Employee Handbook Builder (bilingual, 50-state) | $950 | one time | `6aa2fe615b87e7538bce182e` |
| 8 | Safety Manual Builder (OSHA, bilingual) | $1,200 | one time | `6aa2fe97b44c1caf34be77a9` |
| 9 | Agreement build (contractor, W-2 at-will, or NDA) | $450 | one time | `6aa2fecf862ffedce29b693d` |
| 10 | Agreement bundle (all three) | $1,200 | one time | `6aa2ff0b3b4b7ff298dfaee9` |
| 11 | HR policy or document design | $175 | one time | `6aa2ff40899873cb510849a8` |
| 12 | Atlas One Membership: Concierge / Fractional COO | $1,900 | recurring monthly | `6aa2ff8f3b4b7ff298dfbd44` |
| 13 | AI Email Assistant: Essentials | $249 | recurring monthly | `6aa2ffe7b44c1caf34be9bc6` |
| 14 | AI Email Assistant: Professional | $499 | recurring monthly | `6aa3003bb6ce5fd64aa5c26b` |
| 15 | AI Email Assistant: extra mailbox | $75 | recurring monthly | `6aa300a95b87e7538bce5252` |
| 16 | Handbook annual update | $250 | recurring **yearly** | `6aa301545b87e7538bce5ee8` |
| 17 | Safety manual annual refresh | $300 | recurring **yearly** | `6aa301e15b87e7538bce6898` |
| 18 | AI Email Assistant: setup | $750 one time + **$999 "Complex"** | one time, two prices | `6aa30242f0792f8435d8fc52` |
| 19 | AI Task Agent | $199/mo + **$99/mo "Bundled with Email Assistant"** | recurring monthly, two prices | `6aa302b2118a378288370993` |
| 20 | Atlas One Membership: Enterprise | $999/mo + **$11,988/yr "Annual, setup waived"** | recurring, two prices | `6aa30346d32deabb4805a7ae` |

Every document builder description ends with the required sentence: "Compliance templates
built to your policies. Not legal advice. Attorney review available at cost."

### Notes on the product form

- Recurring prices expose **Billing Period, Trial Period, Number of Payments and a Setup Fee
  field**. The Setup Fee field was deliberately left empty because David asked for setup to be
  sold as separate products.
- A price has no name field. Labels for a second price go in **Additional options > Price
  Description** (127 character limit).
- "Essential" membership has **no setup product**, as specified (setup waived).

### A real defect found and fixed: recurring prices silently saved as Onetime

The Type select on the product form is a custom dropdown that **closes itself between the
click that opens it and the click that picks an option**. Several times the option click
missed, the form kept `Onetime`, and the product saved with no error. Confirmed by reopening
the saved price.

**Found and fixed (now Recurring / Monthly, verified after save):**

| Product | Was | Now |
|---|---|---|
| AI Email Assistant: Essentials | Onetime $249 | Recurring monthly $249 |
| AI Email Assistant: Professional | Onetime $499 | Recurring monthly $499 |
| AI Email Assistant: extra mailbox | Onetime $75 | Recurring monthly $75 |

**Still to verify** (created with the same flaky control, not yet reopened and checked):
Membership Essential $99, Membership Professional $399, Membership Concierge $1,900,
Membership Enterprise $999 and $11,988, AI Task Agent $199 and $99, Handbook annual update
$250, Safety manual annual refresh $300. Each needs Payments > Products > the product > click
the price row > confirm **Type = Recurring** and the right **Billing Period**.

**The reliable way to set these dropdowns**: click the control, wait for the list to render,
then use the **keyboard** (Down / Up then Return). Clicking an option directly is unreliable
and, when it misses, it lands on whatever checkbox is underneath (Track Inventory or Add
Margin), which then silently turns on.

---

## Parts 2 to 6: NOT DONE

Part 1 alone took the whole session. Nothing in Parts 2 to 6 was started, so nothing is half
built and no live payment surface was changed:

- **Part 2, payment links**: none created.
- **Part 3, invoice defaults**: Payments > Invoices > Settings never opened. Business name,
  phone, billing email, logo, terms, payment methods, default note and the four reminders are
  all still at their previous values.
- **Part 4, workflows**: W-PAY-1, W-PAY-2 and W-PAY-3 do not exist. The `Membership tier`
  custom field was not created. The three email templates (`P-MEMBER-WELCOME`,
  `P-BUILDER-DELIVERY`, `P-PAY-FAILED`) were not written.
- **Part 5, test invoice**: no test contact, no test product, no invoice. Nothing to clean up.
- **Part 6**: this file plus the commit.

**Payments > Integrations was never opened**, as instructed.
