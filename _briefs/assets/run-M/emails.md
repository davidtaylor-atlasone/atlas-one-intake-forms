# Run M part B: email bodies for "Call: not now"

Each block is the **body only**. It goes inside the shared branded wrapper from
`_briefs/2026-09-07-email-template-pass.md` part 2, between `<!-- BODY START -->` and
`<!-- BODY END -->`, with `LOGO_URL` replaced by the same hosted logo the 16 existing emails
use. Read that URL off an existing Send Email action rather than guessing it.

Paste method (the editor is a cross origin iframe): put the full document on the clipboard with
`navigator.clipboard.writeText(html)` on the parent page, focus the parent first, then click the
code pane, cmd+a, cmd+v.

**No dashes in any of this copy.** The only hyphens are inside the phone number and inside URLs,
which is the same standing exception as the tool pages.

---

## E0. Immediate. Subject: `Thanks for the time today, {{contact.first_name}}`

```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Thanks for taking the call. I know the timing is not right, and that is completely fine.</p>
<p style="margin:0 0 16px 0;">Here is what I will do. I will leave your file open on my side, and I will check in once in a while with something useful, not a sales pitch. If anything changes before then (a renewal comes up, payroll gets painful, an employee issue lands on your desk), you can reach me directly at 385-213-7177 or book a few minutes here.</p>
<p style="margin:24px 0;"><a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Book a few minutes</a></p>
<p style="margin:0 0 16px 0;">One favor: if you know another owner who is buried in paperwork, send them my way. That is how most of my clients find me.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

## E1 (45-A). Day 45. Subject: `Quick one, {{contact.first_name}}`

One useful thing: read the class codes on the workers comp declarations page.

```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">It has been about six weeks since we talked. Your file is still open on my side, and this is the useful thing I promised rather than a sales pitch.</p>
<p style="margin:0 0 16px 0;">Worth doing this month: pull your workers comp declarations page and read the class codes on it. Owners find people sitting in the wrong class more often than you would think, and the correction shows up as real money at the next renewal. This walks you through it in about three minutes.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/tools/wc-premium-check/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Check your premium</a></p>
<p style="margin:0 0 16px 0;">If anything has changed (a renewal coming up, payroll getting painful, an employee issue on your desk), my number is 385-213-7177 and my calendar is at <a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="color:#788DE3;text-decoration:none;">this link</a>.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

## E2 (45-B). Day 90. Subject: `A number most owners never add up, {{contact.first_name}}`

One useful thing: count the vendors and what each one costs a month.

```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Second one of these, then I will leave you alone for a while.</p>
<p style="margin:0 0 16px 0;">Write down every vendor you pay for payroll, benefits, workers comp, HR support and bookkeeping, and what each one costs a month. Most owners I do this with find four or five separate bills and at least one they had forgotten they were paying. The total is almost always higher than the number in their head. This does the arithmetic for you.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/tools/vendor-consolidation/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Add up your vendors</a></p>
<p style="margin:0 0 16px 0;">Nothing to reply to. If the number surprises you, I am at 385-213-7177.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

## E3 (45-C). Day 135. Subject: `What the people who left actually cost, {{contact.first_name}}`

One useful thing: the real cost of a departure.

```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Last one from me for a while.</p>
<p style="margin:0 0 16px 0;">If anyone left this year, it cost you more than the wage you stopped paying. Recruiting time, the manager hours spent covering, and the weeks before the replacement is actually productive. Put your own numbers in and you will see what one departure really costs.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/tools/retention-cost/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">See the real cost</a></p>
<p style="margin:0 0 16px 0;">That is the whole email. If you ever want a second set of eyes on payroll, benefits or a renewal, I am at 385-213-7177 and my calendar is <a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="color:#788DE3;text-decoration:none;">open here</a>.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

---

## One judgement call, flagged

The instruction said to use the RUN-M email as 45-A if the Cowork spec is out of reach. I could
not reach that project, and sending the same email twice to the same person 45 days apart reads
as a broken automation, so **E0 keeps the RUN-M copy verbatim** (it is written for the hour after
a call) and **E1 carries that email's substance and voice into a day 45 version** under the
subject given. Say the word and I will make E1 a literal copy of E0 instead.
