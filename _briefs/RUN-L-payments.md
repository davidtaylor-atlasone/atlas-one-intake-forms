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


---

# Run L parts 2 and 3

## Part 0. Verification sweep: PASS, no further defects

Every price reopened and read back. **All seven previously unverified recurring prices were
already correct**, and no stray Track Inventory or Add Margin box was found on any of the 20
products.

| Product | Price | Type | Billing period | Track Inventory | Add Margin |
|---|---|---|---|---|---|
| Atlas One Membership: Essential | $99 | Recurring | Monthly | off | off |
| Atlas One Membership: Professional | $399 | Recurring | Monthly | off | off |
| Atlas One Membership: Concierge / Fractional COO | $1,900 | Recurring | Monthly | off | off |
| Atlas One Membership: Enterprise | $999 | Recurring | Monthly | off | off |
| Atlas One Membership: Enterprise, "Annual, setup waived" | $11,988 | Recurring | **Yearly** | off | off |
| AI Task Agent | $199 | Recurring | Monthly | off | off |
| AI Task Agent, "Bundled with Email Assistant" | $99 | Recurring | Monthly | off | off |
| Handbook annual update | $250 | Recurring | **Yearly** | off | off |
| Safety manual annual refresh | $300 | Recurring | **Yearly** | off | off |
| AI Email Assistant: Essentials | $249 | Recurring | Monthly | off | off | (fixed in part 1) |
| AI Email Assistant: Professional | $499 | Recurring | Monthly | off | off | (fixed in part 1) |
| AI Email Assistant: extra mailbox | $75 | Recurring | Monthly | off | off | (fixed in part 1) |
| AI Email Assistant: setup | $750 + $999 "Complex" | Onetime | n/a | off | off |
| Setup: Professional | $495 | Onetime | n/a | off | off |
| Setup: Enterprise | $995 | Onetime | n/a | off | off |
| Setup: Concierge | $1,500 | Onetime | n/a | off | off |
| AI Task Agent: setup | $500 | Onetime | n/a | off | off |
| Employee Handbook Builder (bilingual, 50-state) | $950 | Onetime | n/a | off | off |
| Safety Manual Builder (OSHA, bilingual) | $1,200 | Onetime | n/a | off | off |
| Agreement build (contractor, W-2 at-will, or NDA) | $450 | Onetime | n/a | off | off |
| Agreement bundle (all three) | $1,200 | Onetime | n/a | off | off |
| HR policy or document design | $175 | Onetime | n/a | off | off |

So the silent-Onetime defect hit exactly three prices, all three in the AI Email Assistant
family, all three fixed in Run L part 1. Everything else was built correctly first time.

Incidental confirmation: each product shows a **Stripe TEST and a Stripe LIVE product id**
under Additional Information, so the catalogue is syncing to Stripe.

## Part 1. Payment links: PASS, 14 of 14 built

All fourteen are **Active** and in **Live** payment mode. Each collects **First name, Last
name, Email and Phone** (phone via "Require customers to add a phone number"), branding on,
call to action "Pay". The four recurring membership links also carry GHL's automatic
subscription terms and conditions.

**Public URL pattern: `https://link.fastpaydirect.com/payment-link/<id>`**

| Product | Price | Payment link |
|---|---|---|
| Setup: Professional | $495 one time | https://link.fastpaydirect.com/payment-link/6aa31729e9a073174b3b5aff |
| Setup: Enterprise | $995 one time | https://link.fastpaydirect.com/payment-link/6aa317aae9a073174b3b5b03 |
| Setup: Concierge | $1,500 one time | https://link.fastpaydirect.com/payment-link/6aa31824e9a073174b3b5b08 |
| AI Task Agent: setup | $500 one time | https://link.fastpaydirect.com/payment-link/6aa31880e9a073174b3b5b0c |
| AI Email Assistant: setup | $750 one time | https://link.fastpaydirect.com/payment-link/6aa34222e9a073174b3b5b7e |
| Employee Handbook Builder | $950 one time | https://link.fastpaydirect.com/payment-link/6aa3426ee9a073174b3b5b7f |
| Safety Manual Builder | $1,200 one time | https://link.fastpaydirect.com/payment-link/6aa34311ceb12d9fc1a8c3f4 |
| Agreement build | $450 one time | https://link.fastpaydirect.com/payment-link/6aa3436ee9a073174b3b5b81 |
| Agreement bundle | $1,200 one time | https://link.fastpaydirect.com/payment-link/6aa343c2ceb12d9fc1a8c3f6 |
| HR policy or document design | $175 one time | https://link.fastpaydirect.com/payment-link/6aa34410ceb12d9fc1a8c3f9 |
| Membership: Essential monthly | $99 / month | https://link.fastpaydirect.com/payment-link/6aa3445ee9a073174b3b5b82 |
| Membership: Professional monthly | $399 / month | https://link.fastpaydirect.com/payment-link/6aa344c8e9a073174b3b5b84 |
| Membership: Enterprise monthly | $999 / month | https://link.fastpaydirect.com/payment-link/6aa34520e9a073174b3b5b85 |
| Membership: Concierge monthly | $1,900 / month | https://link.fastpaydirect.com/payment-link/6aa34566ceb12d9fc1a8c3fb |

The Enterprise link deliberately uses the **$999 monthly** price, not the $11,988 annual one.
The AI Email Assistant setup link uses the **$750 standard** price, not the $999 Complex one.
If David wants links for those two alternates as well, they are two more links on the same
products.

### Four things to know about these links

1. **No company field.** Checkout collects first name, last name, email, phone and
   optionally a postal address. Company is not offered, so it cannot be captured here.
2. **No after-payment message.** The only post payment control is "Enable redirection to
   custom URL". "Thank you. Watch your inbox, your next step is on its way." has to be
   delivered another way: a thank you page behind the redirect, or the first email of the
   pay-then-deliver workflow.
3. **ACH is not appearing on the live page.** The rendered checkout at
   `link.fastpaydirect.com` offers **card only** (plus the Stripe Link saved card widget).
   The payment link builder has no method selector, so which methods appear is decided in the
   Stripe account, which lives behind **Payments > Integrations**. That screen is David's and
   was not opened. To get ACH on links and invoices, ACH Direct Debit has to be enabled on the
   Stripe account.
4. **The public domain is `link.fastpaydirect.com`, not an Atlas One domain.** That is the
   payment domain the HighTide reseller provides. If David wants links to read
   `pay.atlasonesolutions.com` or similar, that is a custom payment domain setting.

Cosmetic note: the checkout heading repeats the product name, for example "AI Email
Assistant: setup AI Email Assistant: setup @ 750". That is because GHL auto-names each price
`<Product> @ <amount>` and then prints product name plus price name together. Renaming each
price to something short, for example "Standard", removes the repetition.

## Part 2. Invoice defaults: MOSTLY PASS, two items GHL would not allow

All of this lives at **Payments > Invoices & Estimates > All Invoices > Settings**, not at
Payments > Settings. Payments > Integrations was never opened.

| Setting | Target | Result |
|---|---|---|
| Business name | Atlas One Solutions LLC | **Done** |
| Phone | 385-213-7177 | **Done** (was +13852137177) |
| Logo | `a1-logomark-fullcolor-transparent.png` | **Done.** Uploaded to Media Storage and set as Business Logo. The periwinkle laptop mark, not the old globe and not the namemark |
| Billing email | Billing@AtlasOneSolutions.com | **Done**, as Communications > From Email. From Name set to Atlas One Solutions LLC |
| Default terms | due on receipt | **Done.** Payment Settings > "Invoice due after X days" changed from 14 to **0** |
| Default note | "Pay by bank (ACH) or card. Questions: reply to this email or call or text 385-213-7177." | **Done**, in Title, Terms and Layout > Invoice Terms/Notes |
| ACH and card both on | both | **Done at the GHL layer.** Payment Settings > Manage opens "Allow my customers to pay via" with exactly two choices, **All Valid Payment Methods** and **Only Bank Transfers**. All Valid Payment Methods is on, which admits every method Stripe has enabled |
| No late fees | off | **Confirmed off.** Allow Partial Payments and Allow Tip Payments are also off |
| Accent #23304D | if offered | **Not offered.** Invoice settings has no brand or accent colour field. The only styling control is "Customize Layout", which rearranges blocks, not colours |
| Reminders 3 before, due date, 3 after, 7 after | four reminders | **BLOCKED.** Reminder Settings shows only an "Add another reminder" button and no rows. The button highlights on click but never adds a reminder row. Tried three times, different click points, 15 second waits. Nothing was saved, so the screen is untouched and still shows zero reminders |

Two things for David:

1. **The reminder builder appears broken on this sub account.** Worth raising with High Tide.
   Until it works, invoice reminders can be done as a workflow instead, on the Invoice sent
   trigger with waits of 3 days and so on.
2. **ACH still will not appear to customers until it is enabled on the Stripe account.** The
   live payment link checkout currently offers card only. The GHL side is set correctly; the
   remaining switch is ACH Direct Debit in Stripe, which is behind Payments > Integrations,
   David's screen.


# Run L part 4: stopped early, GHL logged the session out

## Part 0. Price name cleanup: 1 of 23 done

The rename works and is cheap once you have the variant URL:
`/payments/products/<productId>/variants/<variantId>` opens straight onto **Pricing Name**.
Rename, scroll to the bottom, Save. About three steps per price.

| Product | Price renamed | New name | Confirmed |
|---|---|---|---|
| Atlas One Membership: Essential | `6aa2fca0eeafa52989063117` | **Standard** | Yes, reopened and the left rail now reads "Standard" |

The other 22 prices are untouched and still carry the auto-generated
`<Product> @ <amount>` names.

**A note on cost.** This is 23 prices at roughly three steps each. It is not a quick fix, and
doing it first would consume the session that Parts 1 to 3 need. The order to run next time is
Parts 1, 2 and 3 first, then this cleanup with whatever is left.

**Variant ids already known**, so these need no discovery step:

| Product | Variant id |
|---|---|
| Membership: Professional | `6aa2fd1f97fe7f62966dab6c` |
| Membership: Concierge | `6aa2ff8f3b4b7ff298dfbd4c` |
| Membership: Enterprise, monthly | `6aa30346d32deabb4805a7b6` |
| Membership: Enterprise, annual | `6aa30346d32deabb4805a7be` |
| AI Email Assistant: Essentials | `6aa2ffe7b44c1caf34be9bce` |
| AI Email Assistant: Professional | `6aa3003bb6ce5fd64aa5c273` |
| AI Email Assistant: extra mailbox | `6aa300a95b87e7538bce525a` |
| AI Task Agent, standalone | `6aa302b2118a37828837099b` |
| AI Task Agent, bundled | `6aa302b2118a3782883709a3` |
| Handbook annual update | `6aa301545b87e7538bce5ef0` |
| Safety manual annual refresh | `6aa301e15b87e7538bce68a1` |

The variant id is **not** reliably derivable from the product id, so the remaining ten need
one extra step each: open the product, click the price row, read the id from the URL.

## Why part 4 stopped

`Settings > Custom Fields` would not finish loading. It sat on the spinner through two 18
second waits and then offered "If you having issues loading the app, click here to refresh."
**That refresh logged the GHL session out**, landing on the sign in screen at
`app.ridethehightide.com/?logout=true`.

I do not enter passwords, so the run stops here. David signs back in and the next run picks
up at Part 1.

**Nothing was left half built.** No workflow was created, so nothing is half published. The
one price rename is complete and saved.

## Parts 1 to 4 of run part 4: NOT STARTED

Stopped cleanly at the Part 2 boundary. Nothing is half built and no workflow was published.

- **Part 3, workflows.** W-PAY-1, W-PAY-2 and W-PAY-3 do not exist. The `Membership tier`
  custom field was not created. The three email templates `P-MEMBER-WELCOME`,
  `P-BUILDER-DELIVERY` and `P-PAY-FAILED` were not written. **Which trigger fires for a
  subscription payment is therefore still unanswered**; that test was part of building W-PAY-1.
- **Part 4, the $1 test invoice.** No test contact, no "TEST do not buy" product, no invoice.
  Nothing to clean up.

Payments > Integrations and Settings > Integrations were never opened in any part of this run.

---

# Run L part 5

## Part 1. Custom field and tags: PASS

**`Membership Tier` already existed and was already correct**, so it was reused rather than
duplicated. Dropdown (single) on Contact, key `{{contact.membership_tier}}`, options **None,
Essential, Professional, Enterprise, Concierge**, created 27 Aug 2026. Its description already
carries the pricing.

One deviation from the brief: it sits in folder **Additional Info**, not Billing, and **GHL
disables the Folder field once a field exists**, so it cannot be moved. Creating a second
`Membership tier` in a Billing folder would have left two near identical fields for workflows
to write to, which is worse than the wrong folder.

Tags created and each confirmed by search: **member active**, **builder purchased**,
**payment failed**. Tag count went 22 to 25.

## Part 2. Email templates: PASS, all three

Built by **cloning `P-C-0 Instant reply`**, which carries the branded wrapper, then replacing
the body. The wrapper is preserved exactly: A1 Solutions header image, `#23304D` body text,
the David Taylor signature block with real `tel:`, `mailto:`, site and booking links, ONE CALL
SOLVES EVERYTHING, and the "Atlas One Solutions LLC, Lehi, Utah" footer.

| Template | Id | Body |
|---|---|---|
| `P-MEMBER-WELCOME` | `6aa37036a813792f409bf1a9` | Thanks them, welcome call within one business day, intake link comes on that call, self serve booking link, reply or call or text |
| `P-BUILDER-DELIVERY` | `6aa370697919774ef2ed8f30` | Thanks them, builder file within one business day, books the 20 minute walkthrough |
| `P-PAY-FAILED` | `6aa371c107aac9f9aa6a4e75` | One short friendly paragraph, fresh link today, nothing else changes |

No dashes in any prose. Every URL real:
`https://api.leadconnectorhq.com/widget/groups/book-david` and
`https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`.

**Two notes.** `P-BUILDER-DELIVERY` says "your document builder" rather than a product merge
field, which is the fallback the brief allowed, because no product name merge field is exposed
to a workflow email. `P-MEMBER-WELCOME` describes the intake link as something David sends on
the welcome call rather than linking it, because no intake URL exists yet and the rule is no
placeholder URLs.

**Technique worth keeping:** the email builder is a cross origin iframe, so the HTML cannot be
read or written with JavaScript and typing into it risks auto indent. What works is
`navigator.clipboard.writeText(html)` on the parent page, then click into the code pane,
cmd+a, cmd+v. Clean paste every time. The parent page must have focus first or writeText
throws "Document is not focused".

## Part 3. THE TRIGGER ANSWER, which is what the next build needs

| Question | Answer |
|---|---|
| Which trigger fires for a **subscription** payment? | **Payment received.** "Activates when a payment record posts successfully." A subscription renewal posts a payment record, so it fires on every renewal |
| Which trigger fires for a **one time payment link** payment? | **Payment received.** The same trigger. There is no separate one time versus recurring payment trigger |
| What is the **Subscription** trigger then? | Lifecycle only. "Runs when a new subscription is created or subscription status changes." Use it to catch a new subscription or a move to past due, not to catch each payment |
| Is there a **payment failed** trigger? | **No.** Searching the trigger list for "fail" returns no results. Failed payments are caught as **Payment received with filter Payment status Is Failed** |

**Payment received filter fields** are only three: **Global product**, **Payment status**,
**Source**.

- **Global product** operators are **Is / Is not** only, and the value is a **single select
  product picker**. There is no "contains" text operator.
- **Payment status** operators are Is / Is not, values **Failed** and **Success**.

**This breaks the filter design in the brief.** "Product name contains Membership" and
"contains Builder OR Agreement OR policy" cannot be expressed. The working pattern is the same
one W0 uses for verticals: **one Payment received trigger per product**, each with
`Global product Is <that product>`. So W-PAY-1 needs four triggers, one per membership tier,
and W-PAY-2 needs six, one per builder or agreement or policy product.

### W-PAY-3 Payment failed: BUILT BUT NOT PUBLISHED

Workflow id `6985e8a9-a45c-4f0b-845b-e55f0f412a23`, status **Draft**, deliberately not
published because it is not finished.

Done: trigger **Payment received** named "Payment failed" with `Payment status is "Failed"`;
**Add Tag** `payment failed`; **Internal Notification** type Notification, title "Payment
failed", message `Payment failed for {{contact.name}}. Send a fresh link today.`, to All users,
redirect page Contact.

Still to add before publishing: **task** "Payment failed, send a fresh link" due 0 days, and
**send email** `P-PAY-FAILED`.

Note: the Notification type has a **required Redirect page field**, which is not obvious. It
must be set to Contact or Conversation or the action will not save.

### W-PAY-1 and W-PAY-2: NOT STARTED

Nothing was created for either, so nothing is half built.

## Part 4. Test invoice: NOT STARTED

No test contact, no "TEST do not buy" product, no invoice. Nothing to clean up.

## Where the next run should start

1. Finish W-PAY-3, two actions, then publish.
2. W-PAY-1 with four Payment received triggers, one per membership tier, then tag, the four
   way If/Else on product to set Membership Tier, notification, task, email.
3. W-PAY-2 with six triggers, one per builder or agreement or policy product.
4. Part 4 test invoice.
5. The 22 remaining price renames.
