# Brief: GHL calendars and the post-booking flow (Run D, 2026-09-06)

Read all of this, then execute end to end. Batch questions to the end. Report per item with screenshots.
Email bodies go in through the </> source-code dialog. Allow re-entry OFF and Allow multiple opportunities
OFF on every workflow below.

Goal: one booking door for everything. Two event types on David's GHL calendar, an automatic thank-you,
reminder and follow-up, and a one-click way for David to send the PEO form or the bookkeeping form after
the call.

## Part 1: calendars

Open Calendars. There is an existing 15-minute discovery calendar. Rename or configure it as:

A. "15-Minute Intro Call with David"
   - Duration 15, buffer 10 after, minimum notice 2 hours, max 6 weeks out, availability Mon to Fri
     8:00 to 5:00 Mountain, no double booking.
   - Meeting location: Zoom (if the GHL Zoom integration is connected, use it; otherwise phone, and
     add a Zoom link line to the confirmation email).
   - Form fields: first name, last name, email, phone, company, and one custom question "What would you
     like to talk about?" (single line, optional).
   - Confirmation page text: "You're booked. Watch for the calendar invite and a text reminder."
   - Slug: /15-min-intro. Report the full booking link.

B. "30-Minute Back-Office Audit" (new)
   - Duration 30, buffer 15 after, minimum notice 24 hours, max 6 weeks, same availability.
   - Same fields plus "Roughly how many employees?" (number, optional).
   - Slug: /back-office-audit. Report the full booking link.

## Part 2: workflow "Booking: confirm and remind" (new)

Trigger: Appointment Status = Confirmed (or Customer Booked Appointment), calendars A and B.
1. Send Email, from David@AtlasOneSolutions.com, subject "You're booked with David, {{contact.first_name}}",
   body = Email C1 below (use {{appointment.start_time}} and {{appointment.meeting_location}} merge fields
   as GHL names them; verify the tag names in the merge field picker).
2. Add tag "booked".
3. Wait until 24 hours before appointment. Send SMS: "Reminder: your call with David Taylor (Atlas One) is
   tomorrow at {{appointment.start_time}}. Reply here if you need to move it." (If the SMS number is not
   yet configured in GHL, send this as email instead and report that SMS is not set up.)
4. Wait until 1 hour before. Send SMS: "Talk in an hour. Here's the link: {{appointment.meeting_location}}".
Publish. Test by booking calendar A as the seed contact david+seedb@atlasonesolutions.com and confirming
the C1 email in Conversations.

## Part 3: workflow "Booking: after the call" (new)

Trigger: Appointment Status = Showed (fallback: Appointment Status = Confirmed, then Wait until 1 hour
after the appointment end).
1. Send Email = Email C2 below (thank you + next step), 1 hour after the call.
2. Wait 3 days. If/Else: tag "form-a-sent" OR "form-b-sent" OR "proposal-sent" exists -> end.
   Else: Send Email = Email C3 (soft follow-up). Create Task for David "Follow up with
   {{contact.first_name}} after intro call".
Publish.

## Part 4: the one-click form send (David's hands after the call)

David does not want to decide the flow in advance. After a call he opens the contact and adds one tag.
Build two small workflows:

- "Send PEO form on tag": trigger Contact Tag Added = "send-peo-form". Send Email = Email 2 from the
  2026-09-06 workflows brief (the "moving forward" email with https://forms.atlasonesolutions.com/peo/).
  Add tag "form-a-sent". Remove tag "send-peo-form". Publish.
- "Send bookkeeping form on tag": trigger Contact Tag Added = "send-bk-form". Send Email = Email 2B from
  that brief (https://forms.atlasonesolutions.com/bookkeeping/). Add tag "form-b-sent". Remove tag
  "send-bk-form". Publish.
Test both on the seed contact. Report the tag names exactly as created so David can type them.

## Part 5: report

Both booking links, all four workflow names with Published status, screenshots, the merge field names
GHL actually uses for appointment time and location, and whether SMS is configured. Then stop.

---

## Email texts

### Email C1: booking confirmation
Subject: You're booked with David, {{contact.first_name}}

Hi {{contact.first_name}},

You're on my calendar for {{appointment.start_time}}. The invite is on its way and you'll get a reminder
the day before.

Where we'll meet: {{appointment.meeting_location}}

Nothing to prepare. If it helps, jot down the vendors you use today for payroll, benefits, insurance and
bookkeeping, and roughly what each costs. If you don't have that handy, we'll work from memory.

If something comes up, reply here or text me at 385-213-7177 and we'll move it.

David Taylor
Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email C2: after the call
Subject: Thanks for the time today, {{contact.first_name}}

Hi {{contact.first_name}},

Thanks for the time today. Good conversation.

Here's what happens next on my end: I'll pull together what we discussed and get you the next step within
one business day. If we talked about a quote, you'll get a short form from me that captures exactly what I
need to price it accurately the first time.

If anything comes to mind before then, reply here or call me at 385-213-7177.

One call solves everything. Talk soon.

David Taylor
Founder, Atlas One Solutions
385-213-7177 · David@AtlasOneSolutions.com

### Email C3: soft follow-up (3 days, no next step sent)
Subject: Still thinking it over, {{contact.first_name}}?

Hi {{contact.first_name}},

Just checking in after our call. No pressure either way.

If you'd like me to put numbers together, reply "yes" and I'll send the short form. If the timing isn't
right, reply "not now" and I'll check back down the road.

David Taylor · Atlas One Solutions
385-213-7177
