# Brief: GHL workflows pass (2026-09-06)

Read all of this, then execute end to end. Batch questions to the end. Save each workflow before
moving on. Report per item with the workflow name, its status (Draft or Published) and a screenshot
of the canvas.

Context. Both GHL-native intake forms are live and seeded:
- Form A (PEO) id Cxqawj85qg4ULUl64nMc, widget https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc
- Form B (Bookkeeping) id V2EzO3FlRnsthXfHUT7g, widget https://api.leadconnectorhq.com/widget/form/V2EzO3FlRnsthXfHUT7g
- Seed contact "Seed Test" (both submissions merged on phone). Use it to test triggers; do not delete it.
- Native forms write straight to custom fields, so the old webhook field-mapping task is dead. Do not
  build it.
- Email bodies go in through the </> source-code dialog, never the WYSIWYG (it fires canvas shortcuts).
  Close with Escape after saving.
- Rule from David: Form B is only sent when the prospect asked for bookkeeping or accounting. Never
  send it to everyone.

## Part 0: pretty URLs keep working

In the repo (davidtaylor-atlasone/atlas-one-intake-forms), replace `peo/index.html` and
`bookkeeping/index.html` with redirect stubs (meta refresh 0 plus a JS location.replace) to the two
widget URLs above. Keep the page title "Atlas One Solutions". Move the old branded HTML forms into
`_to_delete/branded-html-forms-2026-09-06/` inside the repo (git mv). Commit "Redirect /peo and
/bookkeeping to GHL native forms", push. Verify in a browser that
https://forms.atlasonesolutions.com/peo/ lands on Form A and /bookkeeping/ on Form B. The census page
is untouched.

## Part 1: Workflow "Intake: Instant reply" (new)

Trigger: Form Submitted, form = Form A. Add a second trigger: Form Submitted, form = Form B.
Action 1: Send Email, from David@AtlasOneSolutions.com, subject and body = Email 1 below.
Action 2: Add tag "intake-received".
Action 3: Internal notification (email to David@AtlasOneSolutions.com): "New intake from
{{contact.first_name}} {{contact.last_name}}, {{contact.company_name}}. Open: {{contact.url}}".
Publish it. Test by resubmitting Form A as the seed contact (same identity); confirm the email lands
in the Conversations tab of the seed contact.

## Part 2: Workflow "Intake: Send bookkeeping form" (new)

Trigger: Form Submitted, form = Form A, with a filter on the "Which core services" field. GHL
workflow filters on a multi-select field offer "includes" or "is any of"; use whichever is present and
pick every option whose label contains Bookkeeping, Accounting, Tax or QuickBooks. If the trigger
filter cannot see that field, use an If/Else step right after the trigger on the same field, with
the "no" branch ending the workflow.
Action: Wait 10 minutes (so it arrives after the instant reply), then Send Email = Email 2B below.
Add tag "form-b-sent". Publish. Test with the seed contact by submitting Form A once with
Bookkeeping selected and once without; report that the email went out only on the first.

## Part 3: Finish "Post-Presentation Email" (exists, Draft)

It already has: both triggers, Wait 2h, doc-request email with form link, Wait 3d, nudge email.
Replace every `https://forms.atlasonesolutions.com/peo/` in its emails with the same URL (it now
redirects, so no change needed) and confirm the email texts match Email 2 and Email 3 below. Add:
Wait 4 days -> If/Else "tag intake-received exists" -> No branch: Send Email 4, then Create Task for
David "Call {{contact.first_name}} about open quote", then Wait 3 days -> Update Opportunity stage to
Closed Lost with reason "No response". Yes branch: end. Publish.

## Part 4: "Tool-Lead Nurture" (exists, empty shell)

Trigger: Contact Created with filter Lead Source = "Website Tool/Calculator". Wait 2 days -> If/Else
"has opportunity in any pipeline" (if that condition is not available, use "tag intake-received does
not exist") -> No branch: Send Email 5A, Wait 4 days, Send Email 5B, Add tag "nurtured". Yes branch:
end. Publish.

## Part 5: "Won welcome" (add to the existing Won -> Pay Referral Partner shell, or new if cleaner)

Trigger: Opportunity stage changed to Won (PEO pipeline) and the same for Sales/Setup pipeline.
Action: Send Email 6. Then Create Task for David: "Kickoff call with {{contact.company_name}}", due
in 1 business day. Then, if the "Referral Partner" custom field is filled: Create Task for David
"Pay referral partner: {{contact.referral_partner}} for {{contact.company_name}}". Publish.

## Part 6: Report

For each workflow: name, Published or Draft, trigger(s), step list, screenshot. Then the two redirect
URLs verified. Then anything you could not do and why. Line counts are not needed for this pass.

---

## Email texts (paste exactly, {{ }} are GHL merge fields)

### Email 1: Instant reply
Subject: We've got it, {{contact.first_name}}. Here's what happens next

Hi {{contact.first_name}},

Thanks for sending that over. I have everything, and I'm already looking at it.

Here's what happens next: I'll review your details and get back to you within one business day with
the right next step. Usually that's a short call so I can put the smartest setup in front of you, the
one that actually fits your business, not just the cheapest line item.

If anything is time-sensitive, reply right here or call me directly at 385-213-7177.

One call solves everything. Talk soon.

David Taylor
Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email 2: Moving forward (PEO)
Subject: You're moving forward with Atlas One. Your 5-minute next step

Hi {{contact.first_name}},

Great talking through how Atlas One can take the HR, payroll and benefits load off your plate. I'm
glad you're moving forward. Here is the one step that gets your quote built and your setup moving.

Complete your quote and onboarding form (about 5 minutes):
https://forms.atlasonesolutions.com/peo/

It captures exactly what I need to price you accurately and set you up cleanly the first time, so
there is no back-and-forth later.

Please have these ready to upload or send over:
- Most recent payroll report or register
- Current payroll invoice
- Employee census: names, comp, coverage (if we're quoting benefits)
- Current insurance policy or most recent renewal (if we're reviewing coverage)
- A voided check or bank letter (for setup)

The sooner this is in, the sooner I put real numbers in front of you and lock your start date.

One call solves everything. If anything is unclear, just reply or call me.

David Taylor · Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email 2B: Bookkeeping form (sent only when bookkeeping/accounting was requested)
Subject: One more short form for your books, {{contact.first_name}}

Hi {{contact.first_name}},

You mentioned bookkeeping or accounting, so here is the short form that tells me how your books are
set up today. It takes about three minutes:
https://forms.atlasonesolutions.com/bookkeeping/

Have handy if you can: the last three months of bank and card statements, your most recent tax return,
and the name of your accounting software (or I'll send a secure invite).

That gives me what I need to quote your books, payroll and tax work together, in one number.

David Taylor · Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email 3: Nudge
Subject: Still here whenever you're ready, {{contact.first_name}}

Hi {{contact.first_name}},

Just circling back. I haven't seen your intake form come through yet, and I don't want your quote to
stall on my end while I wait.

Whenever you get a few minutes, here's the link again: https://forms.atlasonesolutions.com/peo/

And if it's easier to just talk it through, reply with a couple of times that work and I'll call you.
We can knock most of it out together in ten minutes.

David Taylor · Atlas One Solutions
385-213-7177

### Email 4: Re-engage
Subject: Should I keep your quote open, {{contact.first_name}}?

Hi {{contact.first_name}},

I know how fast things get buried, no worries at all. I just want to make sure I'm respecting your time.

Two quick options:
1. Still interested but slammed? Reply "keep it open" and I'll hold everything ready for whenever you
   surface.
2. Timing's shifted? Reply "not right now" and I'll check back down the road, no pressure.

Either way, you're not losing your spot. One call solves everything when you're ready.

David Taylor · Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email 5A: Tool lead, touch A
Subject: The number's only half the story, {{contact.first_name}}

Hi {{contact.first_name}},

You ran the numbers on our site. Nice. Here's the part a calculator can't tell you: which setup
actually captures that saving without breaking your service, your compliance, or your team's
day-to-day.

That's the conversation I'm good at, and it's free. Fifteen minutes, no pitch, just a straight read on
what's worth doing for a business like yours.

Want to grab fifteen minutes? Reply with a couple of times that work and I'll get you on my calendar.

David Taylor · Founder, Atlas One Solutions

### Email 5B: Tool lead, touch B
Subject: One thing most owners in your spot are overpaying for

Hi {{contact.first_name}},

Quick one. The businesses I talk to usually aren't overpaying because their prices are too high. It's
because their HR, payroll, benefits and books are spread across four vendors that don't talk to each
other, and nobody's watching the seams.

Consolidating that is where the real money (and the reclaimed time) hides. If that sounds familiar,
it's worth a 15-minute call. Reply and I'll find a time that works for you.

One call solves everything.

David Taylor · Atlas One Solutions

### Email 6: Won welcome
Subject: Welcome to Atlas One, {{contact.first_name}}. Here's your kickoff

Hi {{contact.first_name}},

Welcome aboard. You made a smart call, and I'm glad to have {{contact.company_name}} with us.

Here's what happens now so nothing sits on your shoulders:
1. I handle the setup. You'll get any remaining document requests in one clean list, not a drip.
2. We lock your start date together this week.
3. You get one point of contact: me. Questions, changes, curveballs, one call solves everything.

I'll be in touch within one business day to schedule your kickoff. In the meantime, save my number:
385-213-7177.

Looking forward to making your life simpler.

David Taylor · Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com
