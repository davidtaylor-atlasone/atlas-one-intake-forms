#!/usr/bin/env python3
"""Run AC job 5: Atlas_One_Compliance_Calendar.html. Federal plus UT AZ FL NV CA CO ID TX OR WA.
Every line carries a confirm-before-relying note and a source URL. Amounts that change each year are marked verify.
usage: build_compliance_calendar.py <out.html>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a1shell import head, topbar

# Dated items. when: {"kind":"annual","m":M,"d":D} | {"kind":"quarterly"} (last day of month after quarter) | {"kind":"range","m":M,"d":D,"m2":M2,"d2":D2}
# applies: {"min":N} headcount at or above N, {"max":N}, {"flag":"ale"|"osha"|"benefits"|"selffunded"|"rx"|"contractor"}, or {} for everyone
# conf: "rule" (statutory rule and date are settled) | "verify" (date or amount is set each year or we could not confirm)
ITEMS = [
 # ---------- Federal ----------
 dict(scope="Federal", title="Form W-2 to employees and to the SSA (with W-3)", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="Paper or electronic, same date. Ten or more information returns in total must be filed electronically.", src="https://www.irs.gov/forms-pubs/about-form-w-2"),
 dict(scope="Federal", title="Form 1099-NEC to contractors and to the IRS", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="For nonemployee compensation of $600 or more (the threshold rises to $2,000 for payments made in 2026, verify).", src="https://www.irs.gov/forms-pubs/about-form-1099-nec"),
 dict(scope="Federal", title="Form 940 annual FUTA return", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="Due February 10 if every FUTA deposit was made on time.", src="https://www.irs.gov/forms-pubs/about-form-940"),
 dict(scope="Federal", title="Form 941 quarterly payroll tax return", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Deposits follow your monthly or semiweekly schedule and are separate from the return. Ten extra days if every deposit was on time.", src="https://www.irs.gov/forms-pubs/about-form-941"),
 dict(scope="Federal", title="FUTA deposit if the quarter's liability is over $500", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Under $500 carries forward to the next quarter. Pay through EFTPS.", src="https://www.irs.gov/businesses/small-businesses-self-employed/depositing-and-reporting-employment-taxes"),
 dict(scope="Federal", title="Form W-4 renewals for employees who claimed exempt last year", when=dict(kind="annual", m=2, d=15), applies={}, conf="rule",
      note="Without a new W-4 by this date, withhold as single with no adjustments.", src="https://www.irs.gov/publications/p15"),
 dict(scope="Federal", title="OSHA Form 300A summary posted in the workplace (through April 30)", when=dict(kind="range", m=2, d=1, m2=4, d2=30), applies=dict(min=11, flag="osha"), conf="rule",
      note="Employers with more than 10 employees at any point last year, unless the establishment is in a partially exempt low hazard industry. Post from February 1 to April 30.", src="https://www.osha.gov/recordkeeping"),
 dict(scope="Federal", title="OSHA electronic injury data submission (300A, and 300 and 301 for larger establishments)", when=dict(kind="annual", m=3, d=2), applies=dict(min=20, flag="osha"), conf="rule",
      note="Establishments with 20 to 249 employees in designated high hazard industries, and 250 or more in all recordkeeping industries. Submit through the ITA.", src="https://www.osha.gov/injuryreporting"),
 dict(scope="Federal", title="ACA Form 1095-C furnished to full time employees", when=dict(kind="annual", m=3, d=2), applies=dict(min=50, flag="ale"), conf="rule",
      note="Applicable large employers only (50 or more full time equivalents in the prior year). Since the 2024 Paperwork Burden Reduction Act a posted notice plus furnishing on request can replace mailing to everyone; confirm the notice is posted.", src="https://www.irs.gov/affordable-care-act/employers/information-reporting-by-applicable-large-employers"),
 dict(scope="Federal", title="ACA Forms 1094-C and 1095-C e-filed with the IRS", when=dict(kind="annual", m=3, d=31), applies=dict(min=50, flag="ale"), conf="rule",
      note="Paper filing (allowed only under 10 returns) is due February 28. Electronic filing is required for 10 or more returns.", src="https://www.irs.gov/affordable-care-act/employers/information-reporting-by-applicable-large-employers"),
 dict(scope="Federal", title="EEO-1 Component 1 report (collection window set each year by the EEOC)", when=dict(kind="annual", m=5, d=20), applies=dict(min=100), conf="verify",
      note="Private employers with 100 or more employees, and federal contractors with 50 or more. The EEOC announces the opening date and deadline each spring; the date shown is a placeholder from the 2025 cycle. Verify at the source before planning.", src="https://www.eeocdata.org/eeo1"),
 dict(scope="Federal", title="Form 5500 for calendar year ERISA benefit plans", when=dict(kind="annual", m=7, d=31), applies=dict(min=100, flag="benefits"), conf="rule",
      note="Last day of the seventh month after the plan year ends. Fully insured and unfunded welfare plans with fewer than 100 participants are generally exempt; 401(k) plans of any size file (small plans use the 5500-SF). Extension to October 15 by Form 5558.", src="https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500"),
 dict(scope="Federal", title="PCORI fee on Form 720 (self funded health plans and HRAs)", when=dict(kind="annual", m=7, d=31), applies=dict(flag="selffunded"), conf="rule",
      note="Applies to self insured plans including most HRAs. Fully insured plans pay it through the carrier.", src="https://www.irs.gov/affordable-care-act/patient-centered-outcomes-research-trust-fund-fee-questions-and-answers"),
 dict(scope="Federal", title="Summary Annual Report to plan participants", when=dict(kind="annual", m=9, d=30), applies=dict(min=100, flag="benefits"), conf="rule",
      note="Within nine months after the plan year ends, or two months after an extended Form 5500. Only plans that file a 5500.", src="https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500"),
 dict(scope="Federal", title="Medicare Part D creditable coverage notice to plan participants", when=dict(kind="annual", m=10, d=15), applies=dict(flag="rx"), conf="rule",
      note="Any employer offering prescription drug coverage. Before October 15 every year, plus a disclosure to CMS within 60 days of the plan year start.", src="https://www.cms.gov/medicare/employers-plan-sponsors/creditable-coverage"),
 dict(scope="Federal", title="Review federal workplace posters for the year (FLSA, EEO, OSHA, EPPA, USERRA, FMLA at 50 or more)", when=dict(kind="annual", m=1, d=15), applies={}, conf="rule",
      note="No statutory date; posters change when the agencies revise them. The FMLA poster applies at 50 or more employees. Free from the DOL, never buy them.", src="https://www.dol.gov/general/topics/posters"),
 dict(scope="Federal", title="Employer health plan open enrollment and SBC distribution (plan year start)", when=dict(kind="annual", m=11, d=15), applies=dict(flag="benefits"), conf="verify",
      note="Placeholder for a January plan year: the Summary of Benefits and Coverage goes out with open enrollment materials. Set to your renewal date.", src="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/affordable-care-act/for-employers-and-advisers/summary-of-benefits"),
 # ---------- Utah ----------
 dict(scope="UT", title="Utah quarterly unemployment wage report and contribution (Form 33H)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter through the Employer Portal.", src="https://jobs.utah.gov/ui/employer/employerhome.aspx"),
 dict(scope="UT", title="Utah annual withholding reconciliation (TC-941E) and W-2s to the Tax Commission", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="Filed electronically through TAP.", src="https://tax.utah.gov/withholding"),
 dict(scope="UT", title="Utah workplace poster check (Labor Commission required postings)", when=dict(kind="annual", m=1, d=15), applies={}, conf="rule",
      note="Utah minimum wage follows the federal $7.25; no annual change. Confirm the poster set each January.", src="https://laborcommission.utah.gov/divisions/uald/"),
 # ---------- Arizona ----------
 dict(scope="AZ", title="Arizona minimum wage adjusts for inflation (amount announced each fall)", when=dict(kind="annual", m=1, d=1), applies={}, conf="verify",
      note="Under the Fair Wages and Healthy Families Act the rate changes every January 1; Flagstaff and Tucson set higher local rates. Verify the new amount at the Industrial Commission in October.", src="https://www.azica.gov/labor-minimum-wage-main-page"),
 dict(scope="AZ", title="Arizona quarterly unemployment tax and wage report (UC-018)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter.", src="https://des.az.gov/services/employment/unemployment-employer"),
 dict(scope="AZ", title="Arizona annual withholding reconciliation (A1-R) and W-2s", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="Filed through AZTaxes.", src="https://azdor.gov/business/withholding-tax"),
 # ---------- Florida ----------
 dict(scope="FL", title="Florida minimum wage steps up on September 30", when=dict(kind="annual", m=9, d=30), applies={}, conf="verify",
      note="Amendment 2 raises the rate $1.00 each September 30 until it reaches $15.00 on September 30, 2026; after that it is indexed to inflation each September 30. Update the poster the same day. Verify the indexed amount from 2027 on.", src="https://www.floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices"),
 dict(scope="FL", title="Florida reemployment tax quarterly report (RT-6)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter; electronic filing required for 10 or more employees.", src="https://floridarevenue.com/taxes/taxesfees/pages/reemployment.aspx"),
 # ---------- Nevada ----------
 dict(scope="NV", title="Nevada quarterly unemployment report and Modified Business Tax", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="UI through ESD (last day of the month after the quarter). The Modified Business Tax return to the Department of Taxation is due the same day; the MBT threshold and rate change by legislation, verify.", src="https://ui.nv.gov/ESS.html"),
 dict(scope="NV", title="Nevada minimum wage and daily overtime poster check", when=dict(kind="annual", m=7, d=1), applies={}, conf="verify",
      note="Since July 1, 2024 the single rate is $12.00 (no health benefit tier). It changes only by legislation or a federal increase; confirm each July 1 when the Labor Commissioner issues bulletins.", src="https://labor.nv.gov/Employer/Minimum_Wage/"),
 # ---------- California ----------
 dict(scope="CA", title="California minimum wage adjusts January 1 (amount set the prior August)", when=dict(kind="annual", m=1, d=1), applies={}, conf="verify",
      note="Statewide CPI adjustment each January 1; fast food and health care sectors have their own higher rates, and many cities set local rates on January 1 or July 1. Exempt salary floor moves with it (twice the minimum wage, full time).", src="https://www.dir.ca.gov/dlse/faq_minimumwage.htm"),
 dict(scope="CA", title="California DE 9 and DE 9C quarterly wage reports (EDD)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter through e-Services for Business.", src="https://edd.ca.gov/en/payroll_taxes/required_filings_and_due_dates/"),
 dict(scope="CA", title="California pay data report to the Civil Rights Department", when=dict(kind="annual", m=5, d=13), applies=dict(min=100), conf="verify",
      note="Employers with 100 or more employees (or 100 or more labor contractor workers). Due the second Wednesday of May; the exact date changes each year.", src="https://calcivilrights.ca.gov/paydatareporting/"),
 dict(scope="CA", title="California harassment prevention training cycle check", when=dict(kind="annual", m=1, d=15), applies=dict(min=5), conf="rule",
      note="Employers with 5 or more employees: one hour for nonsupervisory and two hours for supervisory staff every two years, new hires within six months. Track each person's two year date; this line is a reminder to pull the list.", src="https://calcivilrights.ca.gov/shpt/"),
 dict(scope="CA", title="Cal/OSHA Form 300A posting and workplace violence prevention plan annual review", when=dict(kind="annual", m=2, d=1), applies=dict(min=11), conf="rule",
      note="Same February 1 to April 30 posting as federal. SB 553 requires the written workplace violence prevention plan to be reviewed at least annually and training given.", src="https://www.dir.ca.gov/dosh/"),
 # ---------- Colorado ----------
 dict(scope="CO", title="Colorado minimum wage adjusts January 1 (statewide and Denver)", when=dict(kind="annual", m=1, d=1), applies={}, conf="verify",
      note="CPI adjustment announced each fall in the new COMPS Order; Denver and Boulder County set higher local rates. Replace the COMPS poster the same day.", src="https://cdle.colorado.gov/wage-and-hour-law/minimum-wage"),
 dict(scope="CO", title="Colorado FAMLI quarterly wage report and premium", when=dict(kind="quarterly"), applies={}, conf="verify",
      note="Premium is a percentage of wages split with employees; employers with fewer than 10 employees remit only the employee share. The rate is set by the division each year, verify.", src="https://famli.colorado.gov/employers"),
 dict(scope="CO", title="Colorado quarterly unemployment premium report (MyUI Employer+)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter.", src="https://cdle.colorado.gov/employers/unemployment-insurance"),
 # ---------- Idaho ----------
 dict(scope="ID", title="Idaho quarterly unemployment report", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter through the Idaho Department of Labor employer portal.", src="https://www.labor.idaho.gov/businesses/"),
 dict(scope="ID", title="Idaho annual withholding reconciliation (Form 967) and W-2s", when=dict(kind="annual", m=1, d=31), applies={}, conf="rule",
      note="Filed through TAP. Idaho minimum wage follows the federal $7.25.", src="https://tax.idaho.gov/taxes/income-tax/withholding/"),
 # ---------- Texas ----------
 dict(scope="TX", title="Texas quarterly unemployment tax report (C-3 and C-4)", when=dict(kind="quarterly"), applies={}, conf="rule",
      note="Due the last day of the month after each quarter through the TWC Unemployment Tax Services portal. No state income tax withholding.", src="https://www.twc.texas.gov/programs/unemployment-tax"),
 dict(scope="TX", title="Texas Payday Law poster and paydays notice check", when=dict(kind="annual", m=1, d=15), applies={}, conf="rule",
      note="Minimum wage follows the federal $7.25. The Payday Law poster and the notice of designated paydays must stay posted.", src="https://www.twc.texas.gov/programs/wage-and-hour/texas-payday-law"),
 # ---------- Oregon ----------
 dict(scope="OR", title="Oregon minimum wage adjusts July 1 (standard, Portland metro, nonurban)", when=dict(kind="annual", m=7, d=1), applies={}, conf="verify",
      note="BOLI announces the three new rates each April for July 1. Replace posters the same day.", src="https://www.oregon.gov/boli/workers/pages/minimum-wage.aspx"),
 dict(scope="OR", title="Oregon combined quarterly payroll report (Form OQ) and Paid Leave Oregon contributions", when=dict(kind="quarterly"), applies={}, conf="verify",
      note="Filed through Frances Online; covers withholding, unemployment, transit taxes, Workers Benefit Fund and Paid Leave Oregon. Employers with fewer than 25 employees pay no employer share of Paid Leave; the contribution rate is set each year, verify.", src="https://paidleave.oregon.gov/employers/"),
 dict(scope="OR", title="Oregon anti harassment policy (Workplace Fairness Act) annual check", when=dict(kind="annual", m=1, d=15), applies={}, conf="rule",
      note="Every Oregon employer must have a written policy that meets ORS 659A.375 and give it to new hires. No training mandate; this line is the annual reminder to re issue it.", src="https://www.oregon.gov/boli/employers/pages/default.aspx"),
 # ---------- Washington ----------
 dict(scope="WA", title="Washington minimum wage and exempt salary threshold adjust January 1", when=dict(kind="annual", m=1, d=1), applies={}, conf="verify",
      note="L&I announces the CPI adjusted rate every September 30; Seattle, SeaTac, Tukwila, Renton and others set higher local rates. The overtime exempt salary threshold is a multiple of the minimum wage and moves with it.", src="https://lni.wa.gov/workers-rights/wages/minimum-wage/"),
 dict(scope="WA", title="Washington quarterly reports: ESD unemployment, Paid Family and Medical Leave and WA Cares, L&I workers comp", when=dict(kind="quarterly"), applies={}, conf="verify",
      note="All three are due the last day of the month after each quarter. Paid Leave premium and WA Cares (0.58% employee paid) rates are set each year; employers under 50 employees pay no employer share of Paid Leave, verify.", src="https://paidleave.wa.gov/employers/"),
]

# Standing (event based) rules per state, shown as a table, not dated.
STANDING = {
 "Federal": [
  ("New hire reporting", "Within 20 days of hire to the state directory (states may require sooner, see the state rows).", "https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting"),
  ("Form I-9", "Section 1 on or before the first day; Section 2 within three business days of the start date. Keep three years after hire or one year after separation, whichever is later.", "https://www.uscis.gov/i-9"),
  ("Health insurance marketplace notice", "To each new hire within 14 days of start (all FLSA covered employers).", "https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/affordable-care-act/for-employers-and-advisers/coverage-options-notice"),
  ("COBRA", "Federal COBRA applies at 20 or more employees; initial notice within 90 days of coverage, election notice within 44 days of a qualifying event (employer as administrator).", "https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/cobra"),
  ("FMLA", "50 or more employees within 75 miles: poster, policy in the handbook, eligibility notice within five business days of a leave request.", "https://www.dol.gov/agencies/whd/fmla"),
 ],
 "UT": [
  ("New hire reporting", "Within 20 days of hire to the Utah New Hire Registry.", "https://jobs.utah.gov/ui/employer/employerhome.aspx"),
  ("Pay frequency", "At least semimonthly on regular paydays set in advance; wages due within 10 days after the pay period ends (Utah Code 34-28-3). Final pay within 24 hours of an involuntary separation.", "https://le.utah.gov/xcode/Title34/Chapter28/34-28-S3.html"),
  ("Sick leave", "No state mandate.", "https://laborcommission.utah.gov/"),
  ("Harassment training", "No state mandate (recommended).", "https://laborcommission.utah.gov/divisions/uald/"),
  ("Wage notice", "No state hire notice requirement; provide a pay statement each payday.", "https://laborcommission.utah.gov/divisions/uald/"),
 ],
 "AZ": [
  ("New hire reporting", "Within 20 days of hire (Arizona New Hire Reporting Center).", "https://az-newhire.com/"),
  ("Pay frequency", "At least two paydays a month, not more than 16 days apart (ARS 23-351). Final pay within seven working days or the next regular payday, whichever is sooner, after a discharge.", "https://www.azleg.gov/ars/23/00351.htm"),
  ("Paid sick time", "Accrues from the first day of employment at one hour per 30 hours worked; up to 24 hours a year under 15 employees, 40 hours at 15 or more. Usable as accrued (a 90 day wait may be set for new hires).", "https://www.azica.gov/labor-earned-paid-sick-time-main-page"),
  ("Harassment training", "No state mandate.", "https://www.azag.gov/civil-rights"),
  ("Wage notice", "Post the minimum wage and earned paid sick time notices; pay statements each payday.", "https://www.azica.gov/labor-minimum-wage-main-page"),
 ],
 "FL": [
  ("New hire reporting", "Within 20 days of hire to the Florida New Hire Reporting Center (includes independent contractors paid $600 or more).", "https://servicesforemployers.floridarevenue.com/"),
  ("Pay frequency", "No state law setting frequency; follow the written policy consistently.", "https://www.floridajobs.org/"),
  ("Sick leave", "No state mandate; local mandates are preempted.", "https://www.floridajobs.org/"),
  ("Harassment training", "No state mandate.", "https://fchr.myflorida.com/"),
  ("Wage notice", "Post the Florida minimum wage notice; update it every September 30.", "https://www.floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices"),
 ],
 "NV": [
  ("New hire reporting", "Within 20 days of hire (Nevada New Hire Reporting).", "https://dwss.nv.gov/"),
  ("Pay frequency", "At least semimonthly (NRS 608.060). Final pay immediately on discharge, within seven days or the next payday on resignation.", "https://www.leg.state.nv.us/nrs/nrs-608.html"),
  ("Paid leave", "Employers with 50 or more employees: 0.01923 hours of paid leave per hour worked (about 40 hours a year), usable for any reason after 90 days (NRS 608.0197).", "https://labor.nv.gov/"),
  ("Harassment training", "No state mandate.", "https://detr.nv.gov/Page/Nevada_Equal_Rights_Commission"),
  ("Wage notice", "Post the annual minimum wage and daily overtime bulletins from the Labor Commissioner; itemized pay statement each payday.", "https://labor.nv.gov/Employer/Minimum_Wage/"),
 ],
 "CA": [
  ("New hire reporting", "Within 20 days of hire (DE 34 to the EDD); independent contractors on the DE 542 within 20 days of a $600 contract.", "https://edd.ca.gov/en/payroll_taxes/new_hire_reporting/"),
  ("Pay frequency", "At least twice a month on designated paydays; work done 1st to 15th paid by the 26th, 16th to month end by the 10th (Labor Code 204). Itemized wage statements (226) each payday. Final pay immediately on discharge.", "https://www.dir.ca.gov/dlse/faq_paydays.htm"),
  ("Paid sick leave", "Accrues from day one at one hour per 30 hours (or a 40 hour front load); usable from the 90th day; at least 40 hours or five days a year (SB 616). Local ordinances may require more.", "https://www.dir.ca.gov/dlse/paid_sick_leave.htm"),
  ("Harassment training", "5 or more employees: one hour nonsupervisory, two hours supervisory, every two years and within six months of hire or promotion.", "https://calcivilrights.ca.gov/shpt/"),
  ("Wage notice", "Written notice at hire to nonexempt employees under Labor Code 2810.5 (Wage Theft Prevention Act) with rate, payday, employer and workers comp carrier details; re notice within seven days of a change.", "https://www.dir.ca.gov/dlse/Governor_signs_Wage_Theft_Protection_Act_of_2011.html"),
 ],
 "CO": [
  ("New hire reporting", "Within 20 days of hire (Colorado State Directory of New Hires).", "https://newhire.state.co.us/"),
  ("Pay frequency", "Pay periods of no more than one calendar month or 30 days; wages due within 10 days after the period ends (Colorado Wage Act). Final pay immediately on discharge.", "https://cdle.colorado.gov/wage-and-hour-law"),
  ("Paid sick leave", "Healthy Families and Workplaces Act: accrues from hire at one hour per 30 hours up to 48 hours a year, usable as accrued; plus up to 80 hours during a declared public health emergency.", "https://cdle.colorado.gov/hfwa"),
  ("Harassment training", "No state mandate; the POWR Act (2023) lowered the harassment standard and requires records of complaints for five years.", "https://ccrd.colorado.gov/"),
  ("Wage notice", "COMPS Order poster (replaced every January 1) and a copy of the Order with the handbook; itemized pay statements. FAMLI notice posted and given at hire.", "https://cdle.colorado.gov/laws-regulations-guidance"),
 ],
 "ID": [
  ("New hire reporting", "Within 20 days of hire to the Idaho Department of Labor.", "https://www.labor.idaho.gov/businesses/"),
  ("Pay frequency", "At least once a month on a regular payday; wages due within 15 days after the pay period ends (Idaho Code 45-608). Final pay by the next payday or within 10 days, sooner on written demand.", "https://legislature.idaho.gov/statutesrules/idstat/title45/t45ch6/sect45-608/"),
  ("Sick leave", "No state mandate.", "https://www.labor.idaho.gov/"),
  ("Harassment training", "No state mandate.", "https://humanrights.idaho.gov/"),
  ("Wage notice", "Post the Idaho minimum wage and required posters; pay statements each payday on request.", "https://www.labor.idaho.gov/businesses/idaho-labor-laws/"),
 ],
 "TX": [
  ("New hire reporting", "Within 20 days of hire (Texas Employer New Hire Reporting).", "https://www.texasattorneygeneral.gov/child-support/employers/new-hire-reporting"),
  ("Pay frequency", "Nonexempt employees at least twice a month, exempt at least once a month, on designated paydays that are posted (Texas Payday Law). Final pay within six days of a discharge.", "https://www.twc.texas.gov/programs/wage-and-hour/texas-payday-law"),
  ("Sick leave", "No state mandate; city ordinances are preempted (HB 2127).", "https://www.twc.texas.gov/"),
  ("Harassment training", "No state mandate; state harassment law reaches employers of any size and individuals (2021 amendments).", "https://www.twc.texas.gov/programs/civil-rights"),
  ("Wage notice", "Post the Texas Payday Law notice and the paydays notice; written pay statements each payday.", "https://www.twc.texas.gov/programs/wage-and-hour/texas-payday-law"),
 ],
 "OR": [
  ("New hire reporting", "Within 20 days of hire (Oregon Employer Services Portal).", "https://www.oregon.gov/dcbs/pages/index.aspx"),
  ("Pay frequency", "At least every 35 days on a regular payday (ORS 652.120); itemized statements each payday. Final pay by the end of the next business day on discharge.", "https://www.oregon.gov/boli/workers/pages/paychecks.aspx"),
  ("Sick time", "Accrues from hire at one hour per 30 hours worked up to 40 hours a year; paid at 10 or more employees (6 or more in Portland), otherwise unpaid; usable after 90 days.", "https://www.oregon.gov/boli/workers/pages/sick-time.aspx"),
  ("Harassment policy", "Workplace Fairness Act: every employer needs a written anti harassment policy given to new hires and available to all. No training mandate.", "https://www.oregon.gov/boli/employers/pages/default.aspx"),
  ("Wage notice", "Pay transparency and predictive scheduling rules apply to specific sectors; itemized wage statements each payday. Paid Leave Oregon poster and notice at hire.", "https://paidleave.oregon.gov/employers/"),
 ],
 "WA": [
  ("New hire reporting", "Within 20 days of hire (Washington DSHS New Hire Reporting).", "https://www.dshs.wa.gov/esa/division-child-support/new-hire-reporting"),
  ("Pay frequency", "At least once a month on a regular payday (WAC 296-126-023); itemized pay statements. Final pay by the end of the established pay period.", "https://lni.wa.gov/workers-rights/wages/getting-paid/"),
  ("Paid sick leave", "Accrues from hire at one hour per 40 hours worked, usable after 90 days, carry over at least 40 hours; written notice of the policy at hire and balances each pay period.", "https://lni.wa.gov/workers-rights/leave/paid-sick-leave/"),
  ("Harassment training", "No general mandate (hospitality, retail, security and property services employers have specific sexual harassment policy and training duties under RCW 49.60.515).", "https://www.hum.wa.gov/"),
  ("Wage notice", "Pay transparency: job postings by employers with 15 or more employees must show the wage scale and benefits (RCW 49.58.110). Paid Leave and WA Cares notices at hire.", "https://lni.wa.gov/workers-rights/wages/equal-pay-opportunities-act/"),
 ],
}

CSS = """
.month{margin-top:18px}.month h3{font-size:15px;margin:0 0 6px;padding-bottom:4px;border-bottom:2px solid var(--soft)}
.ev{display:grid;grid-template-columns:78px 1fr;gap:10px;padding:9px 0;border-bottom:1px solid #eef1f6;font-size:13.5px}
.ev .dt{font-family:'Horas';font-size:15px;color:var(--navy);line-height:1.2}.ev .dt small{display:block;font-family:'DM Sans';font-size:10.5px;color:var(--muted);font-weight:600}
.ev .t{font-weight:700}.ev .n{color:var(--muted);font-size:12.5px;margin-top:2px}.ev .n a{color:var(--navy)}
.ev .meta{margin-top:4px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.stand{margin-top:8px}.stand th:first-child{width:150px}
.count{font-family:'Horas';font-size:22px}
@media(max-width:480px){.ev{grid-template-columns:1fr}}
@media print{.ev{break-inside:avoid}}
"""
BODY_TOP = r"""
<div class="wrap">
<div class="hero"><h1>HR and payroll compliance calendar</h1><p>Pick the states you have employees in and your headcount. The next twelve months of federal and state dates appear below, each with a source you can open and a note to confirm before you rely on it. Export to your calendar or print it.</p></div>

<div class="card">
  <h2>Your business</h2><p class="sub">Every line below is filtered by these answers. Nothing you type leaves the device.</p>
  <div class="g3">
    <div><label>Employees (W-2 headcount)</label><input id="ee" inputmode="numeric" placeholder="e.g. 24"></div>
    <div><label>Health plan offered?</label><select id="ben"><option value="no">No group health plan</option><option value="ins">Yes, fully insured</option><option value="self">Yes, self funded or level funded, or an HRA</option></select></div>
    <div><label>OSHA recordkeeping</label><select id="osha"><option value="yes">Not in a partially exempt industry (construction, manufacturing, trades, warehousing, etc.)</option><option value="no">Partially exempt low hazard industry (most offices, retail, finance)</option></select></div>
  </div>
  <div style="margin-top:10px"><label>States with employees (tap each)</label><div class="chips" id="states"></div></div>
  <div class="g3" style="margin-top:10px">
    <div><label>Company name (for the export)</label><input id="co" placeholder="Company name"></div>
    <div><label>Start the 12 months from</label><input id="from" type="date"></div>
    <div><label>Show</label><select id="show"><option value="all">Everything that applies</option><option value="rule">Settled dates only</option><option value="verify">Only lines marked verify</option></select></div>
  </div>
</div>

<div class="card">
  <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;justify-content:space-between"><div><h2>The next twelve months</h2><p class="sub" id="summary">Choose at least one state.</p></div><div class="count" id="count"></div></div>
  <div class="callout" style="margin-top:6px">How to read a line: <span class="tag solid">Settled</span> means the rule and its date are fixed in statute or regulation. <span class="tag">Verify</span> means the date or the amount is set each year by an agency and must be checked at the source before you act. Every line, either way, carries "confirm before relying": laws change and this calendar is a planning aid, not legal advice. Dates that land on a weekend are moved to the next business day; federal holidays are not adjusted.</div>
  <div id="cal"></div>
</div>

<div class="card">
  <h2>Standing rules for your states</h2><p class="sub">Not dated. These trigger on a hire, a payday or an accrual, so they belong in the onboarding checklist and the payroll setup rather than on a calendar.</p>
  <div id="stand"></div>
</div>

<div class="help"><b>What is this for?</b> A member benefit and a sales tool: the owner sees every federal and state deadline that applies to their headcount and states in one place, exports it to their calendar, and Atlas One takes over watching it. Sources are official agency pages; nothing here is invented, and anything an agency sets each year is marked verify rather than guessed. Not legal or tax advice.</div>
</div>
"""

JS = r"""
<script>
var ITEMS=%s;var STANDING=%s;
var STLIST=["UT","AZ","FL","NV","CA","CO","ID","TX","OR","WA"];
function $(id){return document.getElementById(id);}
function n(v){return parseFloat(String(v==null?'':v).replace(/[^0-9.\-]/g,''))||0;}
var st={};
function ymd(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function bday(d){var x=new Date(d);while(x.getDay()===0||x.getDay()===6)x.setDate(x.getDate()+1);return x;}
function lastDay(y,m){return new Date(y,m,0);} // m 1..12 -> last day of that month
function occurrences(it,from,to){
 var out=[];var w=it.when;
 if(w.kind==='annual'||w.kind==='range'){for(var y=from.getFullYear();y<=to.getFullYear();y++){var d=new Date(y,w.m-1,w.d);if(d>=from&&d<=to)out.push({d:d,label:w.kind==='range'?('through '+(w.m2)+'/'+w.d2):''});}}
 if(w.kind==='quarterly'){for(var y=from.getFullYear();y<=to.getFullYear();y++){[1,4,7,10].forEach(function(m){var d=lastDay(y,m);var q={1:'Q4 of last year',4:'Q1',7:'Q2',10:'Q3'}[m];if(d>=from&&d<=to)out.push({d:d,label:'for '+q});});}}
 return out;
}
function applies(it,ee,ben,osha){var a=it.applies||{};
 if(a.min&&ee<a.min)return false;if(a.max&&ee>a.max)return false;
 if(a.flag==='ale'&&ee<50)return false;
 if(a.flag==='osha'&&osha==='no')return false;
 if(a.flag==='benefits'&&ben==='no')return false;
 if(a.flag==='rx'&&ben==='no')return false;
 if(a.flag==='selffunded'&&ben!=='self')return false;
 return true;}
var CUR=[];
function build(){
 var ee=n($('ee').value),ben=$('ben').value,osha=$('osha').value,show=$('show').value;
 var states=STLIST.filter(function(s){return st[s];});
 var from=$('from').value?new Date($('from').value+'T00:00:00'):new Date();from.setHours(0,0,0,0);
 var to=new Date(from);to.setFullYear(to.getFullYear()+1);
 var scopes=['Federal'].concat(states);var rows=[];
 ITEMS.forEach(function(it){if(scopes.indexOf(it.scope)<0)return;if(!applies(it,ee,ben,osha))return;if(show!=='all'&&it.conf!==show)return;
  occurrences(it,from,to).forEach(function(o){var due=bday(o.d);rows.push({it:it,d:o.d,due:due,label:o.label});});});
 rows.sort(function(a,b){return a.due-b.due||a.it.scope.localeCompare(b.it.scope);});CUR=rows;
 var byM={};rows.forEach(function(r){var k=r.due.getFullYear()+'-'+String(r.due.getMonth()+1).padStart(2,'0');(byM[k]=byM[k]||[]).push(r);});
 var MN=['January','February','March','April','May','June','July','August','September','October','November','December'];
 var h='';Object.keys(byM).sort().forEach(function(k){var y=k.split('-')[0],m=+k.split('-')[1];h+='<div class="month"><h3>'+MN[m-1]+' '+y+'</h3>';
  byM[k].forEach(function(r){var moved=r.due.getTime()!==r.d.getTime();
   h+='<div class="ev"><div class="dt">'+MN[r.due.getMonth()].slice(0,3)+' '+r.due.getDate()+(moved?'<small>statutory '+MN[r.d.getMonth()].slice(0,3)+' '+r.d.getDate()+', weekend</small>':'')+(r.label?'<small>'+r.label+'</small>':'')+'</div>'+
    '<div><div class="t">'+r.it.title+'</div><div class="n">'+r.it.note+' <b>Confirm before relying.</b> <a href="'+r.it.src+'" target="_blank" rel="noopener">Source</a></div>'+
    '<div class="meta"><span class="tag '+(r.it.scope==='Federal'?'solid':'tint')+'">'+r.it.scope+'</span><span class="tag '+(r.it.conf==='rule'?'solid':'')+'">'+(r.it.conf==='rule'?'Settled':'Verify')+'</span>'+(r.it.applies&&r.it.applies.min?'<span class="mini">applies at '+r.it.applies.min+'+ employees</span>':'')+'</div></div></div>';});
  h+='</div>';});
 $('cal').innerHTML=states.length?h:'<p class="hint">Tap at least one state above.</p>';
 $('count').textContent=states.length?rows.length+' dates':'';
 $('summary').textContent=states.length?('Federal plus '+states.join(', ')+(ee?(' for '+ee+' employees'):'')+', '+ymd(from)+' to '+ymd(to)+'.'):'Choose at least one state.';
 var sh='';scopes.forEach(function(s){if(!STANDING[s])return;sh+='<h3 style="font-size:14px;margin:12px 0 4px">'+(s==='Federal'?'Federal':s)+'</h3><table class="stand"><tbody>'+STANDING[s].map(function(r){return '<tr><td><b>'+r[0]+'</b></td><td>'+r[1]+' <a href="'+r[2]+'" target="_blank" rel="noopener">Source</a></td></tr>';}).join('')+'</tbody></table>';});
 $('stand').innerHTML=states.length?sh:'<p class="hint">Tap at least one state above.</p>';
 try{localStorage.setItem('a1cal',JSON.stringify({ee:$('ee').value,ben:ben,osha:osha,co:$('co').value,from:$('from').value,st:st}));}catch(e){}
}
function icsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/;/g,'\\;').replace(/,/g,'\\,').replace(/\n/g,'\\n');}
function ics(){if(!CUR.length){alert('Pick at least one state first.');return;}
 var co=$('co').value||'Your company';var now=new Date();var stamp=now.toISOString().replace(/[-:]/g,'').replace(/\.\d+Z$/,'Z');
 var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Atlas One Solutions//Compliance Calendar//EN','CALSCALE:GREGORIAN','X-WR-CALNAME:'+icsEsc('Compliance calendar: '+co)];
 CUR.forEach(function(r,i){var d=r.due;var ds=ymd(d).replace(/-/g,'');var e=new Date(d);e.setDate(e.getDate()+1);var de=ymd(e).replace(/-/g,'');
  L.push('BEGIN:VEVENT','UID:a1cal-'+ds+'-'+i+'@atlasonesolutions.com','DTSTAMP:'+stamp,'DTSTART;VALUE=DATE:'+ds,'DTEND;VALUE=DATE:'+de,
   'SUMMARY:'+icsEsc('['+r.it.scope+'] '+r.it.title+(r.label?(' ('+r.label+')'):'')),
   'DESCRIPTION:'+icsEsc(r.it.note+' Confirm before relying. '+(r.it.conf==='rule'?'Settled rule.':'Verify: set each year by the agency.')+' Source: '+r.it.src+' Prepared by Atlas One Solutions for '+co+'.'),
   'URL:'+r.it.src,'BEGIN:VALARM','TRIGGER:-P7D','ACTION:DISPLAY','DESCRIPTION:'+icsEsc(r.it.title+' due in 7 days'),'END:VALARM','END:VEVENT');});
 L.push('END:VCALENDAR');
 function fold(l){var o=[];while(l.length>73){o.push(l.slice(0,73));l=' '+l.slice(73);}o.push(l);return o.join('\r\n');}
 var blob=new Blob([L.map(fold).join('\r\n')+'\r\n'],{type:'text/calendar'});var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='Atlas_One_Compliance_Calendar_'+co.replace(/[^A-Za-z0-9]+/g,'_')+'.ics';document.body.appendChild(a);a.click();a.remove();}
$('states').innerHTML=STLIST.map(function(s){return '<span class="chip" data-st="'+s+'">'+s+'</span>';}).join('');
document.querySelectorAll('.chip').forEach(function(c){c.onclick=function(){st[c.dataset.st]=!st[c.dataset.st];c.classList.toggle('on',!!st[c.dataset.st]);build();};});
['ee','ben','osha','co','from','show'].forEach(function(id){$(id).oninput=build;$(id).onchange=build;});
$('btnIcs').onclick=ics;
try{var s=JSON.parse(localStorage.getItem('a1cal')||'null');if(s){$('ee').value=s.ee||'';$('ben').value=s.ben||'no';$('osha').value=s.osha||'yes';$('co').value=s.co||'';$('from').value=s.from||'';st=s.st||{};document.querySelectorAll('.chip').forEach(function(c){c.classList.toggle('on',!!st[c.dataset.st]);});}}catch(e){}
if(!$('from').value)$('from').value=ymd(new Date());
build();
</script>
</body></html>
"""
out = sys.argv[1]
html = head('Atlas One: HR and Payroll Compliance Calendar', CSS) + '<body>' + topbar('Compliance calendar by state', '<button class="b" id="btnIcs">Export .ics</button>') + BODY_TOP + JS % (json.dumps(ITEMS, ensure_ascii=False), json.dumps(STANDING, ensure_ascii=False))
open(out, 'w', encoding='utf-8').write(html)
print('wrote', out, len(html.encode()), 'bytes', len(ITEMS), 'dated items', sum(len(v) for v in STANDING.values()), 'standing rules')
