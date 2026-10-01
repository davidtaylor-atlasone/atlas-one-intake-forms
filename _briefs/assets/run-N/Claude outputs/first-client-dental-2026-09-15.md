# First full Atlas One client: California dental practice (acquisition, payroll live October 1)

Date: 2026-09-15. Prospect: a dentist buying an existing dental practice in California (works for an Atlas One
client, Modern American Dentistry). Wants everything: PEO payroll, benefits, workers comp, general liability,
professional liability, bookkeeping and accounting, and the business streamlined so it runs without him.
Second business (health and wellness) later; formation and registration for that one comes after.
Membership was not discussed on the call; the email introduces it softly and the brochure is attached.

## The email (send from david@atlasonesolutions.com in Outlook, attach the membership brochure PDF)

Subject: Thank you, and the one link that gets your practice set up

Hi [First name],

Thank you for the time today. I enjoyed hearing about the practice you are taking over and what you want it
to feel like once it is running. You said you are a dentist, not a business manager, and you want the
business side to run without you managing a pile of software and vendors. That is exactly what Atlas One is
built for. You get one point of contact for all of it, and I coordinate the rest.

Here is what I heard you need for the practice, and I can handle every piece of it:

Payroll and HR through our PEO, so your team is paid correctly from the first check on October 1, with taxes,
filings and employee paperwork handled for you.
Workers comp, general liability and professional liability, quoted together so nothing overlaps and nothing
is missed.
Employee benefits (health, dental, vision, 401(k)) if you want to offer them, with real group pricing.
Bookkeeping and accounting, so you see one clean set of numbers each month and your CPA has what they need.
The software behind all of it set up once and kept simple.

The one step that starts everything (about 10 minutes):
https://api.leadconnectorhq.com/widget/form/Cxqawj85qg4ULUl64nMc

That form tells me what to quote. Check every service you want, even the ones you are not sure about, and I
will sort out what belongs in the first phase. Where it asks for a workers comp policy or a payroll report,
upload whatever the current owner can give you. If you do not have something yet, skip it and keep going.

For the employee list, this short census tool builds it in the format the carriers need:
https://forms.atlasonesolutions.com/census/

If you want to see everything Atlas One handles in one place, this page lays it out:
https://forms.atlasonesolutions.com/tools/what-we-do/

I attached a short brochure on the Atlas One membership. It is the part that keeps the business running after
setup: one named person watching renewals, compliance dates and vendors, and the tools your office will use
every week. Based on what you described, the Concierge level is probably the right fit, since it is built for
an owner who wants the business side handled, not just processed. We can talk through it on the next call.

To hit October 1, here is the timing. If I have the form and census by Friday, September 18, I can have
payroll, workers comp and the setup paperwork ready to sign the following week, and your first payroll runs
on time. Benefits usually need a few weeks with the carriers, so those may start November 1 unless the
current plan can carry the team for a month. I will confirm once I see the details.

If it is easier to walk through the form together, grab a time here and we will do it on a screen share:
https://api.leadconnectorhq.com/widget/groups/book-david

Congratulations on the practice. This is going to be a good one.

David Taylor
Founder, Atlas One Solutions
Call 380-CALL-A1S (380-225-5217)
David@AtlasOneSolutions.com
Serving businesses in all 50 states

## What David clicks, in order

1. GoHighLevel (app.ridethehightide.com): Contacts, then "+ Add contact". Enter first name, last name, email,
   phone, and Business Name (the new practice entity, or "New dental practice, name pending"). Under
   Additional Info set Lead Source to Referral and Vertical to Healthcare or Dental (whichever is in the
   list). Add the tag `form-a-sent` (so the system knows the form link already went out and does not nudge
   him for it). Save.
2. Still in GHL: Opportunities, pipeline "PEO & Benefits", "+ Add opportunity", pick the contact, stage
   "Inquiry", name it "<Practice name> PEO, insurance, books", value blank for now. Save.
3. Outlook (david@atlasonesolutions.com): new email to the dentist, paste the email above, replace [First name],
   attach `A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Brochure.pdf` (full path:
   /Users/davidtaylor/Library/CloudStorage/OneDrive-AtlasOneSolutions/2. A1 Official Docs/2. Atlas 1 Solutions
   Marketing/A1_Sales/Atals 1 Membership Pricing/Atlas_One_Membership_Brochure.pdf). Send.
   Why Outlook and not GHL for this one: it is a personal note with attachments, and GHL's editor rewrites
   pasted HTML. The automated emails take over once the form arrives.
4. What happens on its own after that: when he submits the form, GHL matches him by email, fires "Intake:
   Instant reply" (branded confirmation to him within a minute), tags `intake-received`, and creates a CALL
   NOW task for David. David then drags the opportunity to "Census & documents collected".
5. Books: the bookkeeping form (https://api.leadconnectorhq.com/widget/form/V2EzO3FlRnsthXfHUT7g) is NOT sent
   yet on purpose. A practice that has not closed has no transactions to book; David sends it once the
   acquisition closes and the bank account exists (tag `send-bk-form` on the contact, the workflow sends it).
6. After the form: build the quote in Quick Quote, present, then the Post-Presentation workflow runs. Move the
   opportunity stage as it goes (Submitted to carriers, Quotes received, Presented, Verbal, Signed).

## Realities for October 1 (what David should know before he promises)
- A new entity means a new EIN and a new California EDD employer account before the first payroll. California
  is a client-reporting state for PEOs, so the practice needs its own EDD number even under the PEO. New
  employer SUTA in California is a fixed new-employer rate for the first years. Formation, EIN and tax
  accounts go to the Apex / Hoffman vendor, not the bookkeeping vendor.
- Payroll October 1 is realistic if the signed agreement, census, EIN and EDD number are in hand by about
  September 23. Benefits October 1 is unlikely (carrier lead time). Ask the seller when the current health plan
  ends; the team may need it carried through October, or COBRA, with Atlas One benefits November 1.
- Professional liability for a dentist is malpractice, a specialty line (dental carriers, not the general
  E&O market). Confirm carrier appetite before quoting it, or place it through a dental malpractice carrier
  and count it in the "one relationship" anyway. Also check whether the seller's policy has tail coverage.
- The employees are terminated by the seller and hired by the new entity on the closing date. Get the
  seller's final payroll date and YTD reports so nothing is double taxed.
- Two entities eventually (practice plus the wellness business): the GL converter and bookkeeping pricing
  carry a $25 a month extra-entity line; the membership covers both under one owner.

## Pricing decisions made 2026-09-15 (David)
- Late fee: 1.5% per month on amounts more than 15 days past due (standard US commercial term). Approved.
- GL converter: $50/mo monthly payroll, $75/mo semi-monthly or bi-weekly, $125/mo weekly, $250 setup waived
  Professional and above and included in Concierge, $25/mo per extra entity or state journal. Approved;
  build queued as GHL-JOBS Run AX (`_BUILD-LOG/BRIEF-GHL-JOBS-queued-runAX.md`).
- Discount control on proposals and Quick Quote (percent or dollar, list price always shown): queued in Run AX.
- Certified payroll: currently $125 a month per active job in Quick Quote and the schedule; the 2026-08-16
  options doc proposed onboarding $250 to $400 and a federal weekly tier. Recommendation to David: $300
  onboarding, $125/mo per state monthly-filing job, $250/mo per federal weekly-filing job, extra jobs half.
  Waiting on a yes.
- Microsoft 365 client prices: charge Microsoft's published retail (Business Basic $7, Standard $14, Premium
  $22 per user per month, annual term, since the July 2026 increase); cost comes from the Pax8 marketplace.
