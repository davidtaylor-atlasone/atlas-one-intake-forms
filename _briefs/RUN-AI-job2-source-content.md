# Run AI, Job 2 source content: wrapper, button, and body copy for all 26 sends

This file is reference material only (not itself a deliverable). It is the exact wrapper HTML, button markup, and
body copy needed to build one finished HTML file per cadence send at
`_BUILD-LOG/cadence-emails-2026-09-13/<send>.html` in the Master Kit
(`/Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions Marketing/HR_Docs/Atlas_One_Master_Kit`).

## The wrapper (current version, already updated with the standard signature block in Job 1)

Read the current wrapper verbatim from:
`<Master_Kit>/12 GHL Setup doccs/Atlas_One_Email_HTML_How_To.md`
the fenced ```html block under "## The wrapper (copy this whole thing)". Replace `BODY` with the message body for
each send. Do not alter anything else in the wrapper (logo URLs, signature block, footer lines, the two new grey
footer lines are already in it).

## The button markup (repeat for every button, fill in URL and TEXT)

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:24px 0;"><tr>
  <td bgcolor="#788DE3" style="background:#788DE3;padding:12px 24px;">
    <a href="URL"><span style="color:#FFFFFF;font-family:'DM Sans',Arial,Helvetica,sans-serif;font-size:16px;font-weight:700;text-decoration:none;display:inline-block;">TEXT</span></a>
  </td>
</tr></table>
<p style="margin:0 0 16px 0;font-size:13px;color:#5B6577;">Or open this link: <a href="URL"><span style="color:#788DE3;">URL</span></a></p>
```

Paragraph pattern: `<p style="margin:0 0 14px 0;">Text.</p>` (every paragraph its own tag, no bare `<br>` between
sentences that should be paragraphs). Greeting is always `<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>`.
Sign-off: `<p style="margin:0;">Thanks,<br>David</p>` or `<p style="margin:0;">Talk soon,<br>David</p>` as noted per
send below (the signature block in the wrapper already carries name/phone/email, never repeat them in the body).

Links: every anchor gets `style="color:#23304D;text-decoration:underline;"` plus a nested `<font color="#23304D">`
for Outlook, e.g.:
`<a href="URL" style="color:#23304D;text-decoration:underline;"><font color="#23304D">link text</font></a>`
Never use "here" or a fragment as link text; say what happens ("Book a few minutes", "Run your numbers").

Reference URLs:
- WWD = `https://forms.atlasonesolutions.com/tools/what-we-do/`
- BOOK = `https://api.leadconnectorhq.com/widget/groups/book-david`
- BOOK15 = `https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp`
- TIME = `https://forms.atlasonesolutions.com/tools/time-savings/`
- VENDOR = `https://forms.atlasonesolutions.com/tools/vendor-consolidation/`
- ASSESS = `https://forms.atlasonesolutions.com/tools/self-assessment/`
- RETENTION = `https://forms.atlasonesolutions.com/tools/retention-cost/`

---

## Group 1: from RUN-AD-GHL.md 4.2 verbatim (8 sends)

### Email 1 -- subject: Your next step with Atlas One, {{contact.first_name}}
File: `post-presentation-email-1.html`
```
Hi {{contact.first_name}},
Good talking through how Atlas One can take the payroll, benefits, insurance, books and paperwork load off your plate. Here is the one step that gets your quote built.
[button: "Complete the quote form (about 5 minutes)", URL = https://forms.atlasonesolutions.com/peo/]
It captures what I need to price you accurately the first time, so there is no back and forth later. You can upload documents right on the form, or send them to me separately if that is easier.
What helps me build an accurate side by side:
[bulleted list, exactly as follows, do not edit wording]
1. Your most recent payroll register or report (optional, but it's the difference between an estimate and a real number)
2. Your current payroll invoice (optional)
3. Employee census. The form has a built in census tool you can fill in on the spot, or upload your own
4. If we're quoting benefits: your current medical, dental and vision renewal or summary, and the latest invoice showing who is enrolled
5. If we're reviewing workers' comp or other coverage: the current policy or most recent renewal
One thing worth knowing: Atlas One is vendor neutral. I gather the quotes from several providers, manage the whole quoting process, and present them side by side at the same time. No sales calls from five different companies, no oversell. You choose, and I only recommend what you actually need.
A few setup items come later, and only if you decide to move forward.
If it is easier to talk it through, book a few minutes: [link BOOK, text "Book a few minutes"] or reply and I will call you.
Thanks,
David
```

### Email 2 -- subject: Still here whenever you're ready, {{contact.first_name}}
File: `post-presentation-email-2.html`
```
Hi {{contact.first_name}},
Just circling back. I have not seen your form come through yet, and I do not want your quote to stall on my end while I wait.
[button: "Open the quote form", URL = https://forms.atlasonesolutions.com/peo/]
If it is easier to talk it through, grab ten minutes on my calendar and we will knock most of it out together: [link BOOK, text "Book ten minutes"]. Or reply and I will call you.
Thanks,
David
```

### E0 -- subject: Thanks for the time today, {{contact.first_name}}
File: `call-not-now-e0.html`
```
Hi {{contact.first_name}},
Thanks for taking the call. I know the timing is not right, and that is completely fine.
Here is what I will do. I will leave your file open on my side and check in once in a while with something useful, not a sales pitch. If anything changes before then (a renewal comes up, payroll gets painful, an employee issue lands on your desk, the books fall behind), book a few minutes or call me directly at 385-213-7177.
[button: "Book a few minutes", URL = BOOK]
One favor: if you know another owner who is buried in paperwork, send them my way. That is how most of my clients find me.
Two free tools if you want them, no form required: the [link TIME "Time and Cost Savings calculator"] and the [link VENDOR "Vendor Consolidation calculator"]. And when you are a member, the documents most owners pay a lawyer or an HR firm for are built for you: bilingual employee handbook, safety manual, offer letters, W-2 and 1099 agreements, at-will agreements, NDAs.
None of this matters if it does not get you home by five.
Talk soon,
David
```

### LT-1 -- subject: One thing from our call, {{contact.first_name}}
File: `lt-1.html`
```
Hi {{contact.first_name}},
One thing I forgot to mention on our call.
Almost every business I look at is paying for software and vendors that overlap, and nobody is paid to notice. Payroll here, a benefits portal there, three subscriptions doing one job, an insurance renewal that nobody has shopped in years. Atlas One folds all of it into one relationship and one point of contact, and most owners get 15 to 25 hours a week back plus 15 to 30 percent off the vendor spend.
If you ever want me to look, the vendor list takes ten minutes. No form needed for that.
[button: "Book ten minutes", URL = BOOK]
Talk soon,
David
```

### LT-2 -- subject: A number worth knowing
File: `lt-2.html`
```
Hi {{contact.first_name}},
A quick proof point.
One of my clients was on a payroll company that tracked everyone under one workers comp class code. We moved them to a system that assigns the right class code by task automatically. That fixed how their people were tracked, trimmed the workers comp premium, and cut roughly $12,000 more on payroll and HR processing. About $28,000 a year in hard savings, and 400 hours their admin and assistant got back.
None of it showed up on a single invoice. It showed up when someone looked at all of them together.
[button: "Book a 30 minute look at yours", URL = BOOK]
Talk soon,
David
```

### LT-4 -- subject: Two minutes, your own numbers
File: `lt-4.html`
```
Hi {{contact.first_name}},
No pitch in this one.
Owners I survey spend about a third of their week on admin, roughly 88 days a year. This calculator turns your own numbers into hours and dollars, and shows what those hours are worth in revenue if they went back into the business.
[button: "Run your numbers", URL = TIME]
Two more if you want the fuller picture: the [link ASSESS "Back Office Self Assessment"] (two minutes, shows where the gaps and overlaps are) and the [link RETENTION "Retention Cost calculator"] (what one employee leaving really costs).
Talk soon,
David
```
Note: RETENTION link is `https://forms.atlasonesolutions.com/tools/retention-cost/` per Job 2 instruction (keep the
existing retention link URL).

### LT-5 -- subject: Should I close your file, {{contact.first_name}}?
File: `lt-5.html`
```
Hi {{contact.first_name}},
I would rather hear a no than guess.
If now is not the time, reply "later" and I will check back in a few months with nothing but useful stuff. If you want the quote, book a few minutes and I will call you at that time: [link BOOK "Book a few minutes"]. Or reply "yes" and I will call you today.
Talk soon,
David
```

### 45-A -- subject: Quick one, {{contact.first_name}}
File: `45-a.html`
```
Hi {{contact.first_name}},
It has been a few weeks so I wanted to check in.
One thing worth knowing. Getting quotes from four or five providers takes an owner weeks of calls, forms and follow up emails. Because Atlas One is vendor neutral, I do that part. I gather the quotes, present them side by side on the same day, and you choose. Nobody pushes you one way or the other, and you never pay for something you do not need.
If anything has changed on your side (a renewal, a hire, payroll pain), book a few minutes: [link BOOK "Book a few minutes"] or call me at 385-213-7177.
David
```

---

## Group 2: global-only sends (body copy found, wrapper/rules applied)

### LT-3 -- subject: Want to knock the form out together?
File: `lt-3.html`
```
Hi {{contact.first_name}},
The quote form is still open on my side. If it is easier, grab ten minutes here and we will fill it in together on the call: [link BOOK "Book ten minutes"]. If the timing has changed, just say so and I will stop nudging.
David
```

### Q-1 -- subject: If you are changing anything this quarter, start now
File: `q-1.html`
Base body (RUN-P-cadence.md) plus the additions from RUN-Q-report.md item 4 (time line + calculator link) and item
6 (self assessment line), which are now part of the current live copy for all three Q-1 sends:
```
Hi {{contact.first_name}},
Quarter end is 30 days out. That matters because payroll, benefits and workers comp changes are cleanest on a quarter boundary, and the paperwork takes two to three weeks. If you have been thinking about any of it, this is the week to start.
About a third of an owner's week goes to admin, 88 days a year. [link TIME "See the calculator here"].
If you want the fuller picture, the Back Office Self Assessment takes about two minutes. [link ASSESS "Take the assessment here"].
[button: "Book fifteen minutes", URL = BOOK15]
David
```

### YE-1 -- subject: January 1 is the easiest start date of the year
File: `ye-1.html`
Base body (RUN-P-cadence.md) plus the "home by five" line added per RUN-Q-report.md item 4:
```
Hi {{contact.first_name}},
Two months out from year end. A January 1 start means clean W-2s, one set of quarterly filings, and benefits that line up with open enrollment. If a change to payroll, benefits or insurance is on your list for next year, the decision has to happen by early December to make the date. Happy to walk you through what that would look like.
None of this matters if it does not get you home by five.
David
```

### YE-3 -- subject: Last clean cut-over date
File: `ye-3.html`
```
Hi {{contact.first_name}},
This is the last week to start the paperwork and still go live January 1. After this it becomes a mid quarter switch, which works but is messier. Fifteen minutes and I can tell you whether it is worth doing now or waiting.
[button: "Book fifteen minutes", URL = BOOK15]
David
```

## Group 3: global-only sends, body NOT found anywhere in files -- use placeholder

For each of these, build the file with the full wrapper (logo, signature, footer) and put this HTML comment where
the body goes, plus the subject line found (or "SUBJECT: READ FROM GHL" if the subject itself is unknown), so the
GHL terminal knows to keep the current body and swap only the wrapper/signature around it:
`<!-- BODY: READ FROM GHL, keep as is -->`

- **Email 3** (Post-Presentation Email, fires +3 days after Email 2). Subject unknown, keep current.
- **Email 4** (Post-Presentation Email, fires +7 days after Email 3). Subject unknown, keep current.
- **45-B** (Call: not now). Known context only (RUN-Q-report.md item 5): current live content is "A number most
  owners never add up" (Vendor Consolidation calculator copy), not literally recorded. Use the placeholder; do not
  invent replacement copy.
- **45-C** (Call: not now). Known context only (BUILD-INDEX.md / RUN-Q-report.md item 7): includes an `<img>` of
  the retention sample result (`https://forms.atlasonesolutions.com/tools/assets/retention-sample-25ee.png`, width
  560, alt "Sample retention cost result") above a "See the real cost" button. Use the placeholder for the body
  text but you may note the image reuse in a code comment for the GHL terminal's benefit, e.g.
  `<!-- BODY: READ FROM GHL, keep as is (includes retention-sample-25ee.png above the button) -->`.
- **the construction audit email** ("The $70,000 audit", inserted at the LT-2 slot in Post-Presentation Email and
  above 45-B in Call: not now). Known context only (RUN-Q-report.md item 3): no COI collection means the auditor
  charges premium on every uninsured sub's payroll, a $70,000 recovery example, a sub waiver line, two questions
  ("Have you ever had a non compliant audit?" / "Do you like doing your insurance audits?"), 15 minute booking link
  text "calendar" to BOOK. Use the placeholder; do not invent replacement copy.
- **YE-2** (Seasonal touches, subject: "Your workers comp audit is coming" per RUN-P-cadence.md, but the body given
  there was the brief's own suggested draft, not confirmed as what was actually typed into GHL when "you write" body
  copy was implemented). Use the placeholder.
- **YE-4** (Seasonal touches, subject: "Start the paperwork now, go live January 1" per RUN-P-cadence.md, same
  caveat as YE-2). Use the placeholder.

File names: `post-presentation-email-3.html`, `post-presentation-email-4.html`, `45-b.html`, `45-c.html`,
`construction-audit.html`, `ye-2.html`, `ye-4.html`.

---

## Group 4: the seven bookkeeping sends from Run AH (source:
`<Master_Kit>/A1_Sales/Email Templates/Atlas_One_Bookkeeping_Cadence_2026-09-13.md`), with Job 2's decisions applied

Decisions to apply before building:
1. **Cut the guarantee paragraph from B-1** (the paragraph starting "The same guarantee applies here as everywhere
   else at Atlas One..."). Do not replace it with anything.
2. **Keep the per employee payroll price** ($30/month, $15/pay period bi-weekly, $7.50/pay period weekly) as is.
3. **No $300 to $3,000 plan range appears in the current B-1 draft**, so there is nothing to remove; note this in
   the index/report as a no-op decision (nothing found to strip).
4. Scheduling-only changes (do not affect HTML content, note for Job 4's resume brief and INDEX.md): move BQ-1 to
   fire one day after each Q-1 date instead of "30 days before quarter end" (so it does not collide with Q-1 on the
   same date); move BYE-1 to 2026-11-02 instead of 2026-11-01 (so it does not collide with YE-1, which already fires
   2026-11-01).

### B-1 -- subject: What Atlas One bookkeeping actually looks like, {{contact.first_name}}
File: `books-b1.html`
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">Thanks for the conversation about your books. Here is what the service actually is, not just the invoice.</p>
<p style="margin:0 0 14px 0;">Every month, Atlas One closes your books: transactions entered and categorized, bank and credit card accounts reconciled, a full profit and loss and balance sheet ready before you need them. If your business runs accounts receivable and accounts payable, those get managed too, so invoices go out and bills get paid without you chasing either one.</p>
<p style="margin:0 0 14px 0;">Payroll runs right through the same system: $30 a month per employee, $15 a pay period if you run bi-weekly, or $7.50 a pay period if you run weekly. One point of contact owns your books, your payroll, and your QuickBooks cleanup, so the owner sees one number a month instead of three systems that do not talk.</p>
<p style="margin:0 0 14px 0;">If you want to see what clean books would look like for your business, grab a few minutes.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">Thanks,<br>David</p>
```
(The guarantee paragraph that appeared here in the Run AH draft is cut per decision 1 above.)

### B-2 -- subject: What falling behind on the books actually costs
File: `books-b2.html`
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">A quick number to think about.</p>
<p style="margin:0 0 14px 0;">Books that fall behind cost you three ways. Invoices go out late and get paid later. Deductions get missed because nobody caught the receipt in time. And the tax bill surprises you in April because nobody saw it coming in October.</p>
<p style="margin:0 0 14px 0;">None of those show up as one bad month. They show up as a pattern, and by the time an owner notices, it has already cost real money.</p>
<p style="margin:0 0 14px 0;">This calculator shows what your own time is worth if it went back into the business instead of the books.</p>
[button: "Run your numbers", URL = TIME]
<p style="margin:0;">Talk soon,<br>David</p>
```

### B-3 -- subject: A proof point, no names attached
File: `books-b3.html`
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">A quick proof point, names left out on purpose.</p>
<p style="margin:0 0 14px 0;">One Atlas One bookkeeping client came in with two years of QuickBooks that had never been reconciled. Once the books were cleaned up and closed monthly, the owner found overlapping software subscriptions and a payroll error that had been quietly running for months. Fixing both showed up as real dollars back, and the owner has not touched a reconciliation since.</p>
<p style="margin:0 0 14px 0;">Worth knowing: we can also run basic or self service payroll right inside the books, so your team gets paid and your books stay closed at the same time.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">Talk soon,<br>David</p>
```

### B-4 -- subject: Should I close your file, {{contact.first_name}}?
File: `books-b4.html`
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">I would rather hear a no than guess.</p>
<p style="margin:0 0 14px 0;">If the books are not a priority right now, reply "later" and I will check back in a few months with nothing but useful stuff. If you want to see what clean books would look like for your business, reply "yes" and I will call you today.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">Thanks,<br>David</p>
```

### BQ-1 -- subject: The easiest time to switch bookkeepers is right now
File: `books-bq1.html` (fires one day after each Q-1 date; see decision 4 above)
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">Quarter end is 30 days out, and that is the easiest place to switch bookkeepers cleanly. Start now and the new quarter opens with books that are already reconciled, instead of untangling a mess mid quarter.</p>
<p style="margin:0 0 14px 0;">If your books have been sitting, or nobody has looked at them since the last close, a few minutes tells you where you stand.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">David</p>
```

### BYE-1 -- subject: January is the easiest month to start clean books
File: `books-bye1.html` (fires 2026-11-02, see decision 4 above)
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">Two months out from year end. A January start means your books, your payroll, and your year end filings all come out of one system, including 1099s and W-2s, instead of being pieced together from three places in February.</p>
<p style="margin:0 0 14px 0;">If a change to your bookkeeping is on the list for next year, this is the week to start the conversation.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">David</p>
```

### BYE-2 -- subject: Start the year with a clean set of books
File: `books-bye2.html` (2027-01-05, unchanged)
```html
<p style="margin:0 0 14px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 14px 0;">The first month of the year is the setup month, the month a clean set of books gets built so the rest of the year runs itself. If your books need that reset, now is the easiest time to do it.</p>
[button: "Book a few minutes", URL = BOOK]
<p style="margin:0;">David</p>
```
