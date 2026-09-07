# Brief: Run E, branded email template and rewrite pass (2026-09-07)

Read all of this, then execute end to end. Batch questions to the end. Work in the one Chrome tab. Email bodies go in through the </> source dialog; subjects typed as plain text. Never save an action whose subject or body does not match this brief.

Goal: every automated email David sends looks like it came from a person at a well run company. One branded wrapper, real spacing, a button instead of a bare URL, a proper signature with logo and website, and copy with no dashes in it anywhere.

## Part 0: the sender (report only, David does the setting)

Open Settings > Email Services. Report which provider is active (LC Email with dedicated domain lc.atlasonesolutions.com, or SMTP) and whether an SMTP option exists in this build. Do not change anything. Outlook shows "lc.atlasonesolutions.com on behalf of David@AtlasOneSolutions.com" because the envelope sender differs from the From address; the fix is SMTP through David's own Microsoft 365 mailbox, which needs his password and is his step.

## Part 1: find the logo URL

Open https://forms.atlasonesolutions.com/peo/ in the tab, view the page source or inspect the header, and copy the absolute URL of the Atlas One logo image it uses. Report it. Use it as LOGO_URL below. If the form embeds the logo as a data URI instead of a hosted file, upload `a1-primary-fullcolor-transparent.png` from the repo to Settings > Media Storage (the media library upload accepts a file through the file_upload tool) and use that URL.

## Part 2: the wrapper

Every email below is this HTML with the body swapped in. Paste the full document into the </> source dialog each time. Replace LOGO_URL. Do not add anything else.

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAFAF8;padding:32px 0;font-family:'DM Sans',Arial,Helvetica,sans-serif;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#FFFFFF;border:1px solid #DBE4ED;border-radius:8px;">
<tr><td style="padding:28px 40px 8px 40px;"><img src="LOGO_URL" alt="Atlas One Solutions" width="150" style="display:block;width:150px;height:auto;border:0;"></td></tr>
<tr><td style="padding:16px 40px 8px 40px;color:#23304D;font-size:16px;line-height:1.6;">
<!-- BODY START -->
BODY
<!-- BODY END -->
</td></tr>
<tr><td style="padding:24px 40px 32px 40px;border-top:1px solid #DBE4ED;">
<table role="presentation" cellpadding="0" cellspacing="0"><tr>
<td style="vertical-align:top;padding-right:16px;"><img src="LOGO_URL" alt="" width="44" style="display:block;width:44px;height:auto;border:0;"></td>
<td style="vertical-align:top;color:#23304D;font-size:14px;line-height:1.5;">
<strong style="font-size:15px;">David Taylor</strong><br>
Founder, Atlas One Solutions<br>
<a href="tel:13852137177" style="color:#23304D;text-decoration:none;">385-213-7177</a> &nbsp;·&nbsp; <a href="mailto:David@AtlasOneSolutions.com" style="color:#788DE3;text-decoration:none;">David@AtlasOneSolutions.com</a><br>
<a href="https://atlasonesolutions.com" style="color:#788DE3;text-decoration:none;">AtlasOneSolutions.com</a> &nbsp;·&nbsp; <a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="color:#788DE3;text-decoration:none;">Book time with me</a>
</td></tr></table>
<p style="margin:20px 0 0 0;color:#788DE3;font-size:12px;letter-spacing:0.04em;">ONE CALL SOLVES EVERYTHING.</p>
</td></tr>
</table>
<p style="margin:16px 0 0 0;color:#9AA3B2;font-size:11px;">Atlas One Solutions LLC · Lehi, Utah</p>
</td></tr></table>
```

Body conventions inside BODY:
- Paragraphs: `<p style="margin:0 0 16px 0;">text</p>`
- Button: `<p style="margin:24px 0;"><a href="URL" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Button text</a></p>`
- Lists: `<ul style="margin:0 0 16px 20px;padding:0;"><li style="margin:0 0 8px 0;">item</li></ul>`
- Closing line before the signature block: `<p style="margin:0;">Thanks,<br>David</p>` (the signature block below the rule carries the rest, so the body never repeats name, phone or email).

## Part 3: replace the bodies in the published workflows

Open each workflow, open each Send Email action, replace the body with the wrapper plus the body below, keep the subject as given, save, and confirm the workflow is still Published. Do not change triggers or waits.

### Booking: confirm and remind

C1, subject: You're booked with David, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">You're on my calendar for <strong>{{appointment.start_time}}</strong>. The calendar invite is on its way and you'll get a reminder the day before.</p>
<p style="margin:24px 0;"><a href="{{appointment.meeting_location}}" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Join the Zoom meeting</a></p>
<p style="margin:0 0 16px 0;">Nothing to prepare. If it helps, jot down the vendors you use today for payroll, benefits, insurance and bookkeeping, and roughly what each costs. If you don't have that handy, we'll work from memory.</p>
<p style="margin:0 0 16px 0;">If something comes up, reply here or text me at 385-213-7177 and we'll move it.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

24 hour reminder, subject: Reminder: your call with David is tomorrow
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Quick reminder that we talk tomorrow at <strong>{{appointment.start_time}}</strong>.</p>
<p style="margin:24px 0;"><a href="{{appointment.meeting_location}}" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Join the Zoom meeting</a></p>
<p style="margin:0;">Reply to this email if you need to move it.<br>David</p>
```

1 hour reminder, subject: Talk in an hour
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">We talk in an hour. Here's the link.</p>
<p style="margin:24px 0;"><a href="{{appointment.meeting_location}}" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Join the Zoom meeting</a></p>
<p style="margin:0;">See you soon,<br>David</p>
```

### Booking: after the call

C2, subject: Thanks for the time today, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Thanks for the time today. Good conversation.</p>
<p style="margin:0 0 16px 0;">Here's what happens next on my end. I'll pull together what we discussed and get you the next step within one business day. If we talked about a quote, you'll get a short form from me that captures exactly what I need to price it accurately the first time.</p>
<p style="margin:0 0 16px 0;">If anything comes to mind before then, reply here or call me at 385-213-7177.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

C3, subject: Still thinking it over, {{contact.first_name}}?
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Just checking in after our call. No pressure either way.</p>
<p style="margin:0 0 16px 0;">If you'd like me to put numbers together, reply "yes" and I'll send the short form. If the timing isn't right, reply "not now" and I'll check back down the road.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

### Intake: Instant reply

Email 1, subject: We've got it, {{contact.first_name}}. Here's what happens next
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Thanks for sending that over. I have everything and I'm already looking at it.</p>
<p style="margin:0 0 16px 0;">Here's what happens next. I'll review your details and get back to you within one business day with the right next step. Usually that's a short call so I can put the smartest setup in front of you, the one that fits your business, not just the cheapest line item.</p>
<p style="margin:0 0 16px 0;">If anything is time sensitive, reply right here or call me at 385-213-7177.</p>
<p style="margin:0;">Talk soon,<br>David</p>
```

### Send PEO form on tag

Email 2, subject: Your next step with Atlas One, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Good talking through how Atlas One can take the HR, payroll and benefits load off your plate. Here is the one step that gets your quote built.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/peo/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Complete the quote form (about 5 minutes)</a></p>
<p style="margin:0 0 16px 0;">It captures what I need to price you accurately the first time, so there is no back and forth later. You can upload documents right on the form, or send them to me separately if that's easier.</p>
<p style="margin:0 0 8px 0;"><strong>What helps me build an accurate side by side:</strong></p>
<ul style="margin:0 0 16px 20px;padding:0;">
<li style="margin:0 0 8px 0;">Your most recent payroll register or report (optional, but it's the difference between an estimate and a real number)</li>
<li style="margin:0 0 8px 0;">Your current payroll invoice (optional)</li>
<li style="margin:0 0 8px 0;">Employee census. The form has a built in census tool you can fill in on the spot, or upload your own</li>
<li style="margin:0 0 8px 0;">If we're quoting benefits: your current medical, dental and vision renewal or summary, and the latest invoice showing who is enrolled</li>
<li style="margin:0 0 8px 0;">If we're reviewing workers' comp or other coverage: the current policy or most recent renewal</li>
</ul>
<p style="margin:0 0 16px 0;">One thing worth knowing: Atlas One is vendor neutral. I can bring you one recommended option, or several to compare. The form asks which you prefer, and most owners choose the one recommendation.</p>
<p style="margin:0 0 16px 0;">Setup items like a voided check come later, only if you decide to move forward.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

### Send bookkeeping form on tag

Email 2B, subject: One more short form for your books, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">You mentioned bookkeeping or accounting, so here is the short form that tells me how your books are set up today. It takes about three minutes.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/bookkeeping/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Complete the bookkeeping form</a></p>
<p style="margin:0 0 16px 0;">Have handy if you can: the last three months of bank and card statements, your most recent tax return, and the name of your accounting software (or I'll send a secure invite).</p>
<p style="margin:0 0 16px 0;">That gives me what I need to quote your books, payroll and tax work together, in one number.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

### Post-Presentation Email (Emails 3 and 4)

Email 3, subject: Still here whenever you're ready, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Just circling back. I haven't seen your form come through yet, and I don't want your quote to stall on my end while I wait.</p>
<p style="margin:24px 0;"><a href="https://forms.atlasonesolutions.com/peo/" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Open the quote form</a></p>
<p style="margin:0 0 16px 0;">If it's easier to talk it through, reply with a couple of times that work and I'll call you. We can knock most of it out together in ten minutes.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

Email 4, subject: Should I keep your quote open, {{contact.first_name}}?
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">I know how fast things get buried, no worries at all. I just want to respect your time.</p>
<p style="margin:0 0 16px 0;">Two quick options. Still interested but slammed? Reply "keep it open" and I'll hold everything ready for whenever you surface. Timing shifted? Reply "not right now" and I'll check back down the road, no pressure.</p>
<p style="margin:0 0 16px 0;">Either way, you're not losing your spot.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

### Tool-Lead Nurture (Emails 5A and 5B)

Email 5A, subject: The number's only half the story, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">You ran the numbers on our site. Nice. Here's the part a calculator can't tell you: which setup actually captures that saving without breaking your service, your compliance, or your team's day to day.</p>
<p style="margin:0 0 16px 0;">That's the conversation I'm good at, and it's free. Fifteen minutes, no pitch, just a straight read on what's worth doing for a business like yours.</p>
<p style="margin:24px 0;"><a href="https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Grab 15 minutes</a></p>
<p style="margin:0;">Thanks,<br>David</p>
```

Email 5B, subject: One thing most owners in your spot are overpaying for
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Quick one. The businesses I talk to usually aren't overpaying because their prices are too high. It's because their HR, payroll, benefits and books are spread across four vendors that don't talk to each other, and nobody is watching the seams.</p>
<p style="margin:0 0 16px 0;">Consolidating that is where the real money and the reclaimed time hide. If that sounds familiar, it's worth fifteen minutes.</p>
<p style="margin:24px 0;"><a href="https://api.leadconnectorhq.com/widget/bookings/atlas-one-15-minute-intro-call-hoswp" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Pick a time</a></p>
<p style="margin:0;">Thanks,<br>David</p>
```

### Won - Pay Referral Partner (Email 6, plus a NEW onboarding documents email)

Email 6, subject: Welcome to Atlas One, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Welcome aboard. You made a smart call, and I'm glad to have {{contact.company_name}} with us.</p>
<p style="margin:0 0 16px 0;">Here's what happens now so nothing sits on your shoulders. I handle the setup, and you'll get any remaining document requests in one clean list, not a drip. We lock your start date together this week. And you get one point of contact: me.</p>
<p style="margin:0 0 16px 0;">I'll be in touch within one business day to schedule your kickoff. In the meantime, save my number: 385-213-7177.</p>
<p style="margin:0;">Looking forward to making your life simpler,<br>David</p>
```

NEW action, add directly after Email 6: Wait 1 day, then Send Email. Subject: Setup checklist for {{contact.company_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Here is the one list I need to get {{contact.company_name}} set up. Send what you have, and I'll chase the rest with you on the kickoff call.</p>
<ul style="margin:0 0 16px 20px;padding:0;">
<li style="margin:0 0 8px 0;">A voided check or bank letter for payroll funding</li>
<li style="margin:0 0 8px 0;">Your most recent payroll register, if you haven't already sent it</li>
<li style="margin:0 0 8px 0;">Employee details for anyone not already on the census</li>
<li style="margin:0 0 8px 0;">Current benefits enrollment, if we're moving coverage</li>
<li style="margin:0 0 8px 0;">Your workers' comp policy and loss runs, if we're moving coverage</li>
</ul>
<p style="margin:0 0 16px 0;">Reply with attachments, or upload them through the secure link I'll give you on the call.</p>
<p style="margin:0;">Thanks,<br>David</p>
```

## Part 4: two new small workflows

"Booking: cancelled" (new). Trigger: Appointment Status = Cancelled, In calendar group = Book time with David. Send Email, subject: No problem, {{contact.first_name}}. Want to pick a new time?
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Saw the cancellation. No problem at all, things come up.</p>
<p style="margin:0 0 16px 0;">If you'd like to pick a new time, the calendar is below. If the timing isn't right, no reply needed and I'll check back down the road.</p>
<p style="margin:24px 0;"><a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Pick a new time</a></p>
<p style="margin:0;">Thanks,<br>David</p>
```
Then Remove tag "booked". Allow re-entry ON. Publish.

"Booking: no show" (new). Trigger: Appointment Status = No Show, In calendar group = Book time with David. Send Email, subject: We missed each other, {{contact.first_name}}
```html
<p style="margin:0 0 16px 0;">Hi {{contact.first_name}},</p>
<p style="margin:0 0 16px 0;">Looks like we missed each other today. No worries. Grab another time below and we'll pick it up from there.</p>
<p style="margin:24px 0;"><a href="https://api.leadconnectorhq.com/widget/groups/book-david" style="background:#788DE3;color:#FFFFFF;text-decoration:none;padding:12px 24px;border-radius:6px;font-weight:600;display:inline-block;">Pick a new time</a></p>
<p style="margin:0;">Thanks,<br>David</p>
```
Allow re-entry ON. Publish.

## Part 5: the calendar invite body

The .ics invite David's Outlook sends carries GHL's default event description ("==========", "Phone:-", "Email:-", raw reschedule and cancel links). On each of the four calendars, look in Advanced settings and Notifications for a field that controls the appointment or event description (names vary: "Appointment description", "Event description", "Notes"). If it exists, set it to:

Your meeting with David Taylor, Atlas One Solutions.
Join: {{appointment.meeting_location}}
Need to change it? Reschedule: {{appointment.reschedule_link}}  Cancel: {{appointment.cancellation_link}}
Questions: 385-213-7177 or David@AtlasOneSolutions.com

Use the exact merge tags from the picker if the names differ. If no such field exists, report that and leave it.

## Part 5b: make the four booking cards match

1. Copy the prepared logo to David's Desktop so he can drag it: `cp "<scratchpad>/a1-logo-180.png" ~/Desktop/atlas-one-calendar-logo.png`. Then try the file_upload tool on the Calendar logo box of the 30, 45 and 60 minute calendars. If it works, done. If not, report that David drags ~/Desktop/atlas-one-calendar-logo.png onto the Calendar logo box on each of the three calendars.
2. The 15-minute calendar's description shows a raw merge tag and an em dash on the public page ("Atlas One Intro Call — {{contact.company}} & David Taylor"). Merge tags do not render on booking pages. Replace the description with exactly: "A relaxed 15 minutes to understand your business and where your back office is costing you time or money. No pitch, no pressure, just a straight read on whether Atlas One can simplify things and what it could be worth to you. Come as you are. I'll bring the questions." Do not touch the name, slug or URL.
3. The 15-minute booking page uses periwinkle widget colors; the other three use GHL's default blue. Open the 15-minute calendar's Customizations (widget style / primary color) and apply the same values to the 30, 45 and 60 minute calendars.

## Part 6: turn off the duplicates and test

1. Pause the BRJ workflow "Call Scheduling Confirmation" (do not delete it).
2. On all four calendars: Appointment booked (Confirmed) EMAIL channel OFF, Reminder and Follow-Up emails OFF. In-app, Cancellation and Reschedule stay ON.
3. Tell David to book the 60-minute through https://api.leadconnectorhq.com/widget/groups/book-david from his phone as david+seedb@atlasonesolutions.com (the extension cannot reach that domain). Wait for him to confirm, then check Conversations for the seed: exactly one confirmation email (C1) with the button rendering, the logo showing, the Zoom link behind the button, and {{appointment.start_time}} rendered as a full date and time. If start_time is time only or blank, swap all three uses for the Start Date Time tag from the picker and report its exact string. Check the Outlook event exists. If the contact received no calendar invite with the calendar email off, turn the Confirmed email back on and remove C1 instead.
4. Cancel the seed appointment (that also tests "Booking: cancelled"; report whether that email arrived).

## Part 7: report

For every email touched: workflow, action name, subject, and a screenshot of one rendered email from Conversations showing the wrapper, button and signature. The logo URL used. The Email Services finding from Part 0. The Part 5 finding. Then stop.
