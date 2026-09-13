#!/usr/bin/env python3
"""Run AC job 7: Atlas_One_Marketplace_Catalog_for_BRJ (.xlsx and .md). Public facing for BRJ: no vendor costs, margins or
rev share. Sources: _INTERNAL Vendor Partner Directory (status), V8 Technology & Operations sheet and Quick Quote (retail)."""
import sys, os, datetime, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
out_base = sys.argv[1]
# name, category, one line, retail, logo source (official page), status, note for BRJ
ROWS = [
 ("Ramp", "Finance: corporate card, expense, AP, travel", "Corporate cards, expense management, bill pay and travel in one platform, with the client's setup handled by Atlas One.", "Free to the client; quote for implementation", "https://ramp.com/press (press kit)", "Signed", "Use the tracked Atlas One landing page ramp.com/partners/atlasone for every link."),
 ("QuickBooks Online (Intuit)", "Finance: accounting software", "Cloud accounting managed under ProAdvisor partner pricing, 50% off the first three months.", "$115 per month (Plus tier; other tiers quoted)", "https://www.intuit.com/company/press-room/ (Intuit press room; logo use per Intuit brand guidelines)", "Signed", "Intuit trademark rules are strict: only the official lockup, never recoloured."),
 ("Big Red Jelly", "Web and marketing: website, SEO, branding", "Website design, marketing, search and AI search optimisation, branding.", "Quote", "https://bigredjelly.com/ (BRJ supplies its own logo)", "Signed", "BRJ's own card; BRJ owns the artwork."),
 ("Microsoft 365", "Software: productivity and email licensing", "Microsoft 365 licences supplied and supported by Atlas One as reseller, with the AI Email Assistant running inside it.", "Quote (per user per month, Microsoft list)", "https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks (Microsoft trademark and brand guidelines)", "Signed", "Microsoft logo use requires following the brand guidelines page; partner badge only if the partner programme grants it."),
 ("G&A Partners", "Workforce and HR: PEO, ASO, HCM", "Full service PEO and HR outsourcing platform, one of the payroll delivery models Atlas One quotes.", "Quote", "https://www.gnapartners.com/about-us/ (request logo from the partner team)", "Signed", "Legacy active agreement. Never print who quoted a plan on client material."),
 ("Deel", "Workforce and HR: global payroll, EOR, contractors", "Employer of record in 120 plus countries, contractor payments, global HR and device management.", "Quote", "https://www.deel.com/press (press page)", "Pending", "Partner agreement in progress; do not publish until signed."),
 ("Jotform", "Software: online forms and workflows", "Online forms, data collection, e-sign and workflows; the intake layer behind several Atlas One tools.", "From $34 per month (Bronze); Silver $39, Gold $99; Enterprise quoted", "https://www.jotform.com/about/ (request press assets from Jotform partnerships)", "Pending", "Referral agreement ready but not signed; retail prices are Jotform's own list."),
 ("Connecteam", "Software: time, scheduling, workforce hubs", "Time clocks, GPS geofencing, job costing, PTO, LMS and company communications for deskless teams.", "$5 per employee per month (Operations hub); all three hubs $11", "https://connecteam.com/press (press page)", "Pending", "Referral rate not confirmed; list only after the agreement is signed."),
 ("Cornerstone PEO", "Workforce and HR: PEO, ASO", "Utah based PEO and ASO; a payroll delivery model Atlas One quotes.", "Quote", "https://www.cornerstonepeo.com/about-us/ (request logo from Cornerstone)", "Pending", "Priority partner, agreement terms still open. Never print who quoted a plan."),
 ("Vero HCM", "Workforce and HR: PEO, ASO, HCM", "PEO, ASO and HR self service platform.", "Quote", "https://verohcm.com/ (request logo from Vero)", "Pending", ""),
 ("Row Partners", "Workforce and HR: PEO, ASO, HCM", "PEO, ASO and HCM services.", "Quote", "https://rowrowrow.io/ (request logo from Row)", "Pending", ""),
 ("Rhino Insurance", "Risk and insurance: commercial P&C broker", "Commercial property and casualty placement.", "Quote", "https://rhinoinsurance.com/ (request logo from Rhino)", "Pending", ""),
 ("CF Partners", "Benefits and retirement: 401(k), advisory", "401(k) plans, financial advisory, estate and acquisition planning.", "Quote", "https://thecfpartners.com/ (request logo from CF Partners)", "Pending", "Ask which specific services to list."),
 ("Excel Health", "Benefits: employee health plans", "Employee health benefits programme; relationship in development.", "Quote", "https://excelhealthplans.com/ (request logo from Excel Health)", "Pending", "In development; do not publish yet."),
 ("Amplified Resource Group", "Benefits: large group", "Large group benefits.", "Quote", "https://amplifiedresourcegroup.com/ (request logo)", "Pending", "Confirm relationship to ARG Healthcare Group before either is listed."),
 ("Redirect Health", "Benefits: alternative funded health plans", "Health plan designs offered through Atlas One's carrier partners; never a tier inside a carrier menu.", "Quote", "https://www.redirecthealth.com/ (request logo from Redirect Health)", "Pending", "Say 'health coverage through Atlas One's carrier partners'. Never 'the Atlas One health plan'."),
 ("New Journe Consulting", "Benefits: health plan consulting", "Health benefits consulting and plan sourcing.", "Quote", "https://newjourneconsulting.com/ (request logo)", "Pending", "Never print who quoted a plan."),
 ("Hoffman and Company", "Financial services: bookkeeping, tax strategy", "Bookkeeping, tax strategy and financial advisory.", "Quote", "https://hoffmanandcompany.com/ (request logo from Kris Hoffman)", "Pending", "Compliance: describe as bookkeeper and tax strategist, never as a CPA."),
 ("Experienced Payroll Pros", "Financial services: bookkeeping, tax", "Accounting, bookkeeping and tax strategy.", "Quote", "Website did not resolve on 2026-09-13; confirm the domain before listing", "Pending", "Domain check failed; verify the vendor is still active."),
 ("Apex Tax Services", "Financial services: tax preparation, business setup", "Tax preparation and business formation services.", "Quote", "https://apextax.net/ (request logo from Apex)", "Pending", ""),
 ("GoReboot", "Technology: IT support", "Outsourced IT support and helpdesk.", "$125 per month IT support and helpdesk (Atlas One retail); vendor quote otherwise", "https://goreboot.com/ (request logo from GoReboot)", "Pending", ""),
 ("Pax8", "Software: cloud marketplace", "Cloud software marketplace through which Atlas One provisions Microsoft and other licences.", "Quote", "https://www.pax8.com/en-us/about/ (request partner logo kit)", "Pending", "Behind the scenes supplier; usually not shown to clients."),
 ("PartnerStack and AppDirect networks", "Software: marketplace networks", "Referral networks covering many SaaS vendors; individual products listed once chosen.", "Quote", "https://partnerstack.com/about and https://www.appdirect.com/about", "Pending", "Pick the vendors worth pushing before any card goes on the site."),
 ("SimpliVerified", "Workforce and HR: background checks, drug testing", "FCRA background screening and drug testing; Atlas One retail is per report.", "Background check from $30 per report; drug test from $20 (Atlas One retail)", "https://simpliverified.com/ (request logo from SimpliVerified)", "Do not sign", "Reseller agreement under review; do not list as a partner and do not sign until counsel clears the FCRA reseller terms."),
 ("SwipeClock", "Software: time and attendance", "Time and attendance quoted through the payroll platform.", "$6 per user per month (Atlas One quote line)", "https://www.swipeclock.com/ (request logo)", "Pending", "Sold through the PEO or HCM platform; no direct agreement on file."),
 ("PrismHR", "Software: HCM platform", "HCM and time tracking platform behind several PEO offerings.", "$6 per user per month time tracking (Atlas One quote line)", "https://www.prismhr.com/about/ (request logo)", "Pending", "Platform partner of the PEOs; no direct agreement on file."),
 ("QuickBooks Time", "Software: time tracking", "Time tracking that feeds QuickBooks payroll.", "$8 per user per month (Atlas One quote line)", "https://www.intuit.com/company/press-room/ (Intuit press room)", "Signed", "Covered by the Intuit referral enrolment; confirm QuickBooks Time is an eligible SKU before listing."),
 # Atlas One's own services (no vendor)
 ("Atlas One AI Email Assistant", "Technology: Atlas One service", "Runs inside the client's Microsoft 365 or Google account; drafts, sorts and files, never sends without the owner.", "Essentials $249 per month, Professional $499 per month, setup $750", "Atlas One brand kit (A1_Final Brand)", "Signed", "Atlas One's own product."),
 ("Atlas One AI Task Agent", "Technology: Atlas One service", "Turns commitments in email and meetings into a tracked task list with reminders.", "$199 per month, $99 bundled with the Email Assistant, setup $500", "Atlas One brand kit (A1_Final Brand)", "Signed", "Atlas One's own product."),
 ("Atlas One Website design and care", "Web: Atlas One service (built with Big Red Jelly)", "Website design and build with the tools and forms embedded, then hosting and care.", "Build from $2,500; care $150 per month; content $400 per month", "Atlas One brand kit (A1_Final Brand)", "Pending", "Jason Petty web card pricing is a separate open question; confirm before publishing."),
]
STATUS_NOTE = {"Signed": "agreement on file", "Pending": "not yet signed, do not publish", "Do not sign": "hold, counsel review"}
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "Catalog"
navy = "23304D"; peri = "788DE3"; mist = "DBE4ED"
ws.append(["Atlas One Solutions: software and partner marketplace catalog for Big Red Jelly"]); ws["A1"].font = Font(name="DM Sans", size=14, bold=True, color=navy)
ws.append([f"Prepared {datetime.date.today():%B %d, %Y}. Public safe: no vendor costs, margins or revenue share appear here. Status tells BRJ what may be published: only Signed rows go on the website. Logos come only from the vendor's own brand or press page named in column E, never scraped from search."])
ws["A2"].alignment = Alignment(wrap_text=True); ws.merge_cells("A2:G2"); ws.row_dimensions[2].height = 45
ws.append([])
hdr = ["Name", "Category", "What it does (one line)", "Retail price or quote", "Where BRJ gets the official logo", "Status", "Note for BRJ"]
ws.append(hdr)
for c in range(1, len(hdr) + 1):
    cell = ws.cell(row=4, column=c); cell.font = Font(name="DM Sans", bold=True, color="FFFFFF"); cell.fill = PatternFill("solid", fgColor=navy); cell.alignment = Alignment(vertical="center", wrap_text=True)
thin = Side(style="thin", color=mist)
for r in ROWS:
    ws.append(list(r))
    row = ws.max_row
    for c in range(1, len(hdr) + 1):
        cell = ws.cell(row=row, column=c); cell.alignment = Alignment(vertical="top", wrap_text=True); cell.font = Font(name="DM Sans", size=10, color=navy); cell.border = Border(bottom=thin)
    sc = ws.cell(row=row, column=6); sc.font = Font(name="DM Sans", size=10, bold=True, color=navy if r[5] != "Signed" else "FFFFFF")
    sc.fill = PatternFill("solid", fgColor=navy if r[5] == "Signed" else (mist if r[5] == "Pending" else "FFFFFF"))
    if r[5] == "Do not sign": sc.border = Border(left=Side(style="thick", color=navy), bottom=thin)
for i, w in enumerate([28, 34, 62, 40, 58, 13, 60], 1): ws.column_dimensions[get_column_letter(i)].width = w
ws.freeze_panes = "A5"; ws.auto_filter.ref = f"A4:G{ws.max_row}"
# legend sheet
lg = wb.create_sheet("Read me")
for line in ["How to use this catalog",
             "Status by form: Signed rows are solid navy (publish), Pending rows are tinted (hold), Do not sign rows carry a thick left rule (never publish).",
             "Logos: open the page in column E and download from the vendor's own press or brand kit. If the page has no kit, email the vendor contact and ask for an SVG or PNG on transparent. Never take a logo from a search result or a third party site.",
             "Prices: 'Quote' means Atlas One quotes it per client. Where a retail figure is shown it is Atlas One's published retail or the vendor's public list price on the date above. No wholesale, cost or commission figures exist in this file by design.",
             "Compliance wording for benefits rows: 'health coverage through Atlas One's carrier partners', never 'the Atlas One health plan'; never print who quoted a plan.",
             "Source files (internal, not for BRJ): _INTERNAL/Atlas_One_Vendor_Partner_Directory.xlsx, _INTERNAL/Atlas_One_INTERNAL_Master_Pricing_V8.xlsx (Technology & Operations), 09 Quick Quote Tool."]:
    lg.append([line])
lg.column_dimensions["A"].width = 120
for row in lg.iter_rows(): row[0].alignment = Alignment(wrap_text=True); row[0].font = Font(name="DM Sans", size=10, color=navy)
lg["A1"].font = Font(name="DM Sans", size=13, bold=True, color=navy)
wb.save(out_base + ".xlsx")
# markdown
md = ["# Atlas One Solutions: software and partner marketplace catalog for Big Red Jelly", "",
      f"Prepared {datetime.date.today():%B %d, %Y}. Public safe: no vendor costs, margins or revenue share appear here. Only **Signed** rows may be published; Pending rows are held until the agreement is signed; Do not sign rows never appear. Logos come only from the vendor's own brand or press page named below, never from a search result.", "",
      "| Name | Category | What it does | Retail or quote | Official logo source | Status | Note for BRJ |", "|---|---|---|---|---|---|---|"]
for r in ROWS: md.append("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
md += ["", "## Counts", "", f"Signed: {sum(1 for r in ROWS if r[5]=='Signed')}. Pending: {sum(1 for r in ROWS if r[5]=='Pending')}. Do not sign: {sum(1 for r in ROWS if r[5]=='Do not sign')}.", "",
       "## Wording rules for benefits rows", "", "Say 'health coverage through Atlas One's carrier partners'. Never 'the Atlas One health plan' or 'our master plan'. Never print who quoted a plan.", "",
       "Sources (internal, not for BRJ): the Vendor Partner Directory, the V8 pricing workbook's Technology and Operations sheet, and the Quick Quote technology rows, all as of the date above."]
open(out_base + ".md", "w", encoding="utf-8").write("\n".join(md) + "\n")
print("wrote", out_base + ".xlsx", out_base + ".md", len(ROWS), "rows")
