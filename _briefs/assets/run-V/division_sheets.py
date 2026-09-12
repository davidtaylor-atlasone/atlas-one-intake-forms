#!/usr/bin/env python3
"""Run V job 3: rebuild five division sheets from the Financial Services template.
Prices only from A1_Sales/Pricing/Atlas_One_Price_List.html; no vendor or PEO brand names; no dashes."""
import sys, re, os, html
TEMPLATE, FIN_HTML, OUTROOT = sys.argv[1], sys.argv[2], sys.argv[3]
tpl = open(TEMPLATE, encoding='utf-8').read()
fin = open(FIN_HTML, encoding='utf-8').read()
FONTS = '\n'.join(re.findall(r'@font-face\{[^}]*\}', fin))
LOGO = re.search(r'<img src="([^"]+)" alt="Atlas One Solutions"', fin).group(1)
PILLS = ['Workforce & HR','Benefits & Retirement','Financial Services','Risk & Insurance','Technology & Operations','Business Consulting']

D = {}
D['Workforce & HR'] = dict(
 size='tight',
 file='Atlas 1 Payroll PEO/Atlas_One_Division_Payroll_HR',
 h1=('Payroll, HR and workforce:', 'run your way, through one point of contact.'),
 lede='Run payroll and manage your team on an enterprise grade HR platform, and choose how much you hand off. Four ways to run payroll, one compliance backbone, one person to call: PEO co-employment through Atlas One\'s PEO partners, ASO administration, HCM software only, or payroll through Atlas One Bookkeeping.',
 why_sub='Same platform, four levels of support.',
 why=[('Four delivery models','PEO, ASO, software only, or through Atlas One Bookkeeping; switch as you grow'),
      ('Your checks, your way','Direct deposit, pay cards, or live checks printed in your office'),
      ('All 50 states','Multi state payroll, filings and new hire reporting handled in one place'),
      ('Fixed, quoted prices','Retail per employee prices below; final quote after the 30 minute Back Office Audit')],
 cards=[
  ('Payroll, four ways to run it',[
    ('PEO (co-employment), per employee per check','$23'),
    ('PEO, as a percentage of gross payroll','0.80% to 0.95%'),
    ('ASO (administrative services), per employee per check','$18'),
    ('HCM software only (self service), per employee','$12/mo'),
    ('Through Atlas One Bookkeeping, per employee: monthly / bi-weekly / weekly','$30 / $15 / $7.50'),
    ('1099 contractor payroll, per contractor: monthly / bi-weekly / weekly','$20 / $10 / $5')]),
  ('Payroll tax and filings',[
    ('Withholding or payroll tax account setup, per account','$250'),
    ('State withholding plus unemployment, both accounts','$500'),
    ('Quarterly payroll filing, per return','$130'),
    ('S-Corp owner payroll, per quarter, annual W-2 included','$250'),
    ('Year end 1099s, automated: setup / per form','$75 / $17'),
    ('Certified payroll (WH-347), per active job','$125')]),
  ('Hiring, screening and onboarding',[
    ('Applicant tracking system','$95'),
    ('New hire onboarding, per hire (digital W-4, I-9, W-9, direct deposit)','$20'),
    ('E-Verify, per verification','$8'),
    ('Comprehensive criminal search','$55'),
    ('Drug test','$65'),
    ('Motor vehicle record','$12')]),
  ('Time, labor and the HR platform',[
    ('HRIS and employee management, per employee (included in a PEO engagement)','$4'),
    ('Time tracking and attendance, per user','$1 to $15'),
    ('Performance management, per employee','$3'),
    ('Learning management (LMS), per employee','$4'),
    ('Certification and training tracking, per employee','$2'),
    ('Employee self service: pay history, W-2s, time off requests, team chat',None)]),
  ('HR compliance and employee relations',[
    ('Employee handbook, bilingual, 50 state, one time','$950'),
    ('Handbook annual update','$250/yr'),
    ('HR document and policy design, per document','$175'),
    ('Garnishment administration, per garnishment per month','$15'),
    ('Unemployment claims administration, per claim','$25'),
    ('Worksite posters, EEO-1 and ACA compliance support, HR hotline',None)]),
  ('Safety, agreements and separation',[
    ('Safety manual (OSHA), bilingual, one time','$1,200'),
    ('Safety manual annual refresh','$300/yr'),
    ('Contract or agreement build (NDA, at-will, contractor), per document','$450'),
    ('Contract bundle, all three','$1,200'),
    ('COBRA administration','$35'),
    ('Harassment prevention training, offboarding and unemployment hearing support',None)])],
 fine='Prices as of September 2026, before member discounts. PEO co-employment, EPLI and master benefit programs are delivered through Atlas One\'s PEO and carrier partners under their own terms. Atlas One is not a law firm; documents are compliance templates built to your policies.',
 changed='Delivery model narrative rewritten from "we become your co-employer" to PEO co-employment through Atlas One\'s PEO partners; four models instead of three (adds payroll through Atlas One Bookkeeping); retail prices added from the price list; "W-2 and 1099 issuance no charge" and "401(k) fee covered" claims dropped; dashes removed.')

D['Benefits & Retirement'] = dict(
 size='roomy',
 file='Atlas 1 Benefits/Atlas_One_Division_Benefits_Retirement',
 h1=('Employee benefits and retirement:', 'attract, retain and protect your people.'),
 lede='Competitive benefits without the enterprise overhead. Atlas One arranges and administers health, ancillary and retirement plans through its carrier and plan partners, and taps PEO master programs where co-employment earns your team large group pricing, so a small or mid size business can offer big company benefits through a single point of contact.',
 why_sub='Marketplace, not a single carrier.',
 why=[('Market shopped','Quotes from several carriers through Atlas One\'s carrier partners, never captive to one'),
      ('Group and individual','Large group, small group and ICHRA, matched to your budget'),
      ('PEO master programs','Large group rates through co-employment where it lowers cost'),
      ('Concierge enrollment','Guided open enrollment and year round support for your people')],
 cards=[
  ('Medical and health plans',[
    ('Group major medical through Atlas One\'s carrier partners','Quoted'),
    ('Level funded and self funded options','Quoted'),
    ('ICHRA / individual coverage administration, per employee','$20'),
    ('PEO master medical access through co-employment',None),
    ('Multi carrier quoting and benchmarking',None),
    ('Plan design built around your budget',None)]),
  ('Ancillary and voluntary',[
    ('Dental and vision','Quoted'),
    ('Life, AD&D, short and long term disability','Quoted'),
    ('Accident, critical illness and hospital indemnity','Quoted'),
    ('Pet insurance','Quoted'),
    ('Voluntary and worksite benefits',None),
    ('Supplemental coverage coordination',None)]),
  ('Retirement and 401(k)',[
    ('401(k) PEP / MEP, per participant per year, setup $450','$65'),
    ('Solo 401(k), SEP or IRA setup, one time','$350'),
    ('Safe Harbor and profit sharing design',None),
    ('Roth and traditional options',None),
    ('Fiduciary 3(16) / 3(38) support through plan partners',None),
    ('Employee education and enrollment',None)]),
  ('Pre tax and spending accounts',[
    ('Section 125, HSA, FSA, HRA administration, per employee','$5'),
    ('Premium only plans (POP)',None),
    ('Dependent care accounts',None),
    ('Commuter and transit benefits',None),
    ('Plan documents and compliance',None),
    ('Payroll deductions synced with your payroll',None)]),
  ('Enrollment and administration',[
    ('Benefits administration, per employee (included in a PEO engagement)','$7'),
    ('Open enrollment support, per year','$500'),
    ('COBRA administration','$35'),
    ('New hire enrollment and carrier feeds',None),
    ('Benefits administration technology',None),
    ('Dedicated benefits support',None)]),
  ('Compliance and advisory',[
    ('ACA compliance and 1095 filing, per employee per year','$8'),
    ('5500 filing and nondiscrimination testing, per year','$950'),
    ('ERISA and ACA compliance review',None),
    ('Total rewards benchmarking',None),
    ('Renewal strategy and negotiation',None),
    ('Year round advisory access',None)])],
 fine='Prices as of September 2026, before member discounts. Health, ancillary and retirement coverage is placed through Atlas One\'s carrier and plan partners; Atlas One does not hold a health plan of its own.',
 changed='"Atlas One brokers and administers" and "vetted, A-rated carriers" replaced by "arranges and administers through its carrier and plan partners"; "Fortune-500-caliber" dropped; retail prices added (ICHRA $20, 401(k) PEP $65, Section 125 $5, benefits admin $7, open enrollment $500, COBRA $35, ACA $8, 5500 $950); no health plan of its own stated in the fine print; dashes removed.')

D['Risk & Insurance'] = dict(
 size='roomy',
 file='Atlas 1 Risk Docs/Atlas_One_Division_Risk_Insurance',
 h1=('Commercial insurance and risk:', 'coverage that protects what you have built.'),
 lede='One relationship across every commercial line. Atlas One shops the market through its licensed agency and carrier partners, manages renewals and certificates, and ties workers comp to PEO master programs where co-employment lowers the cost, so you are properly protected without juggling agents or waiting on paperwork.',
 why_sub='One advisor, the whole market.',
 why=[('Market shopped','Several carriers through Atlas One\'s agency and carrier partners, never captive'),
      ('Fast certificates','Certificates of insurance in minutes through the portal, not days'),
      ('PEO master programs','Workers comp and EPLI through co-employment where it lowers cost'),
      ('One renewal calendar','Every policy, one point of contact, one renewal conversation')],
 cards=[
  ('Workers compensation',[
    ('Workers comp policy review, flat fee','$495'),
    ('Workers comp premium audit review, 25% of the premium recovered','Contingent'),
    ('Workers comp master plan through PEO co-employment','Quoted'),
    ('Pay as you go premium',None),
    ('Experience mod and class code review',None),
    ('Claims management and return to work',None)]),
  ('Property and liability',[
    ('General liability','Quoted'),
    ('Commercial property',None),
    ('Business owner\'s policy (BOP)',None),
    ('Inland marine and equipment',None),
    ('Umbrella and excess liability',None),
    ('Product and completed operations',None)]),
  ('Commercial auto and fleet',[
    ('Owned, hired and non owned auto',None),
    ('Fleet and commercial vehicle programs',None),
    ('Driver motor vehicle record, per record','$12'),
    ('Cargo and transit coverage',None),
    ('Telematics options',None),
    ('Certificate management for your fleet',None)]),
  ('Management and professional',[
    ('Professional liability (E&O)','Quoted'),
    ('Employment practices (EPLI)','Quoted'),
    ('Cyber liability and data breach','Quoted'),
    ('Key person coverage','Quoted'),
    ('Surety and license bonds','Quoted'),
    ('Directors and officers (D&O)',None)]),
  ('Certificates and service',[
    ('On demand certificate of insurance generation',None),
    ('Self serve certificate portal',None),
    ('Additional insured tracking',None),
    ('Renewal management',None),
    ('Mid term change requests',None),
    ('Dedicated account servicing',None)]),
  ('Risk management and safety',[
    ('Safety manual (OSHA), bilingual, one time','$1,200'),
    ('Safety manual annual refresh','$300/yr'),
    ('Workplace safety training','Quoted'),
    ('OSHA compliance support',None),
    ('Loss control consulting',None),
    ('Premium reduction strategy',None)])],
 fine='Prices as of September 2026, before member discounts. Coverage is quoted and placed through Atlas One\'s licensed agency and carrier partners under their own terms; premiums are set by the carrier.',
 changed='"One brokerage relationship" and "Atlas One shops the market through multiple A-rated carriers" replaced by placement through Atlas One\'s licensed agency and carrier partners; retail prices added (WC policy review $495, premium audit review 25% of recovered, MVR $12, safety manual $1,200 / $300); "Quoted" only on the lines the price list names; dashes removed.')

D['Technology & Operations'] = dict(
 size='medium',
 file='Atlas 1 Risk Docs/Atlas 1 Tech Operations/Atlas_One_Division_Technology_Operations',
 h1=('Technology and operations:', 'the systems that run your business, handled.'),
 lede='The right tools, set up right, supported by people. Atlas One matches, implements and supports the technology that runs your operation, from IT and networking to your software stack, workforce systems, documents, payments and AI assistants, through one accountable, vendor neutral partner and one consolidated invoice.',
 why_sub='Matched to you, set up and supported.',
 why=[('Vendor neutral','Matched to your needs, not a quota'),
      ('One marketplace','Vetted stack, one consolidated invoice'),
      ('Set up and supported','Implemented, trained and kept running by people you can call'),
      ('Integrated','Payroll, books, CRM, POS and documents that talk to each other')],
 cards=[
  ('IT support and networking',[
    ('IT support and helpdesk','$125'),
    ('Annual security audit','$2,500/yr'),
    ('Compliance package (HIPAA, SOC 2)','$500'),
    ('Network, Wi-Fi and cabling setup',None),
    ('Email and productivity suite setup',None),
    ('Backup and disaster recovery',None)]),
  ('Software marketplace and payments',[
    ('Software marketplace, vetted catalog with partner pricing','Quoted'),
    ('Point of sale and merchant services','Quoted'),
    ('Needs based matching and consolidated billing',None),
    ('License and subscription management',None),
    ('Invoicing, ACH and card on file tools',None),
    ('Onboarding and training',None)]),
  ('Workforce systems',[
    ('HCM software only (self service), per employee','$12/mo'),
    ('HRIS and employee management, per employee','$4'),
    ('Time tracking and attendance, per user','$1 to $15'),
    ('Applicant tracking system','$95'),
    ('Learning management (LMS), per employee','$4'),
    ('Scheduling, job costing and employee self service',None)]),
  ('CRM, website and automation',[
    ('CRM setup and management','Quoted'),
    ('Website design and build, hosting and care','Quoted'),
    ('Workflow and task automation',None),
    ('Marketing automation, lead capture and forms',None),
    ('Reporting dashboards',None),
    ('Sales pipeline tools',None)]),
  ('Documents and digitisation',[
    ('Document digitisation and form design, per form','$95'),
    ('Digital forms and e-signature',None),
    ('Document management and storage',None),
    ('Paper to digital conversion',None),
    ('Records retention',None),
    ('Secure file sharing',None)]),
  ('AI services',[
    ('AI Email Assistant, Essentials (one mailbox), setup $750','$249'),
    ('AI Email Assistant, Professional (up to three mailboxes), setup $750','$499'),
    ('Additional mailbox','$75'),
    ('AI Task Agent, standalone, setup $500','$199'),
    ('AI Task Agent, bundled with the Email Assistant','$99'),
    ('Support beyond the included time','$150/hr')])],
 fine='Prices as of September 2026, before member discounts. Software, hardware and payment processing are supplied by Atlas One\'s technology partners under their own terms; Atlas One sets them up, supports them and bills them on one invoice.',
 changed='Six cards now IT, software marketplace and payments (merged), workforce systems, CRM and website, documents, and a new AI services card; retail prices added (helpdesk $125, security audit $2,500, compliance package $500, HCM $12, ATS $95, LMS $4, form design $95, AI assistant tiers); dashes removed.')

D['Business Consulting'] = dict(
 size='roomy',
 file='Atlas 1 Consulting/Atlas_One_Division_Business_Consulting',
 h1=('Business consulting:', 'a strategic partner in your corner.'),
 lede='More than vendors, an advisor. Atlas One brings operator level experience to the decisions that move your business: structure, growth, financing and efficiency. One relationship that already understands your operation, helping you build it stronger, with no sales pitch attached. Membership is the platform; consulting is added as you need it.',
 why_sub='Advice from someone who has done it.',
 why=[('Operator led','Built and sold real companies'),
      ('Whole business view','Sees across all six divisions'),
      ('Vendor neutral','Guidance, not a quota'),
      ('On call access','Counsel when you need it; Concierge members get a fractional COO')],
 cards=[
  ('Membership',[
    ('Essential, setup waived','$99/mo'),
    ('Professional, setup $495, often waived','$399/mo'),
    ('Enterprise, setup $995, waived on annual','$999/mo'),
    ('Concierge, your fractional COO, setup $1,500','$1,900/mo'),
    ('The Audit Guarantee: the 30 minute Back Office Audit finds at least two times your first year membership in documented savings or risk removed, or there is nothing to buy',None)]),
  ('Entity and structure',[
    ('Business formation and structure, plus state fees','$750'),
    ('Federal EIN and business formation','Quoted'),
    ('Multi entity structuring',None),
    ('Ownership and equity guidance',None),
    ('Registered agent and compliance coordination',None),
    ('Tax advantaged setup with specialists',None)]),
  ('Growth and strategy',[
    ('Business strategy consulting, per hour','$250'),
    ('ROI analysis and reporting','$750'),
    ('Go to market planning',None),
    ('Scaling and hiring strategy',None),
    ('KPI and dashboard design',None),
    ('Exit and succession planning',None)]),
  ('Financing and capital',[
    ('Banking and treasury setup','$750'),
    ('SBA loan packaging','Quoted'),
    ('Lender relationships and preparation',None),
    ('Working capital strategy',None),
    ('Equipment financing',None),
    ('Loan package preparation',None)]),
  ('Efficiency and cost',[
    ('Vendor and spend audit','Quoted'),
    ('Brand, flyer and collateral design','$1,200'),
    ('Software stack consolidation',None),
    ('Labor and time leakage review',None),
    ('Process automation',None),
    ('Margin and pricing analysis',None)]),
  ('People, organisation and continuity',[
    ('Org design and role clarity','Quoted'),
    ('Business continuity planning and SOPs','Quoted'),
    ('HR document and policy design, per document','$175'),
    ('Comp and commission plan design',None),
    ('Leadership and accountability systems',None),
    ('Culture and retention strategy',None)])],
 fine='Prices as of September 2026, before member discounts. Atlas One is not a law firm or a CPA firm; legal, tax and audit work is coordinated with licensed specialists.',
 changed='New Membership card with the confirmed tiers ($99 / $399 / $999 / $1,900 with setup fees) and the Audit Guarantee, replacing the June "Risk & Compliance Advisory" card (its continuity and SOP lines moved to People, organisation and continuity); retail prices added (formation $750, strategy $250/hr, ROI $750, treasury $750, collateral $1,200, policy design $175); dashes removed.')

def esc(t): return html.escape(t, quote=False)
def build(name, d):
    out = tpl.replace('{{FONTS}}', FONTS).replace('{{LOGO}}', LOGO)
    out = out.replace('<title>Atlas One Solutions, Financial Services division sheet</title>', '<title>Atlas One Solutions, %s division sheet</title>' % esc(name))
    out = out.replace('Division service sheet, Financial Services', 'Division service sheet, %s' % esc(name))
    out = out.replace('<div class="ey">Atlas One Solutions, Financial Services</div>', '<div class="ey">Atlas One Solutions, %s</div>' % esc(name))
    out = re.sub(r'<h1>.*?</h1>', '<h1>%s <span>%s</span></h1>' % (esc(d['h1'][0]), esc(d['h1'][1])), out, flags=re.S)
    out = re.sub(r'<p class="lede">.*?</p>', '<p class="lede">%s</p>' % esc(d['lede']), out, flags=re.S)
    out = re.sub(r'<h2>Why it is different <small>.*?</small></h2>', '<h2>Why it is different <small>%s</small></h2>' % esc(d['why_sub']), out)
    why = ''.join('<div><b>%s</b><span>%s</span></div>' % (esc(b), esc(s)) for b, s in d['why'])
    out = re.sub(r'<div class="why">.*?</div>\s*</div>', '<div class="why">%s</div>' % why, out, count=1, flags=re.S)
    cards = []
    for title, items in d['cards']:
        lis = ''.join('<li>%s%s</li>' % (esc(t), ('<b>%s</b>' % esc(p)) if p else '') for t, p in items)
        cards.append('<div class="card"><h3>%s</h3><ul>%s</ul></div>' % (esc(title), lis))
    out, n = re.subn(r'<div class="grid">.*?</ul></div>\s*</div>\s*<p class="fine">.*?</p>', lambda m: '<div class="grid">%s</div>\n  <p class="fine">%s</p>' % (''.join(cards), esc(d['fine'])), out, count=1, flags=re.S); assert n == 1, 'grid not replaced'
    assert 'Bookkeeping and accounting' not in out.replace(FONTS, '')
    SIZES = {'roomy': '.page.roomy .card li{font-size:10.5px;padding:3px 0 3px 12px;line-height:1.4}.page.roomy .card ul{padding:8px 10px 8px}.page.roomy .card h3{font-size:12px;padding:7px 10px}.page.roomy .why div{padding:9px 8px}.page.roomy .why span{font-size:10px}.page.roomy .lede{font-size:11px}.page.roomy .grid{gap:12px}.page.roomy h2{margin:14px 0 8px}',
             'medium': '.page.medium .card li{font-size:10px;padding:2px 0 2px 11px}.page.medium .card ul{padding:7px 10px 7px}.page.medium .why div{padding:8px 8px}.page.medium .grid{gap:11px}',
             'tight': '.page.tight .card li{padding:1px 0 1px 11px}.page.tight .card ul{padding:5px 10px 5px}.page.tight .why div{padding:6px 8px}'}
    if d.get('size'):
        out = out.replace('@page{size:Letter;margin:0}', SIZES[d['size']] + '\n@page{size:Letter;margin:0}')
        out = out.replace('<div class="page">', '<div class="page %s">' % d['size'])
    pills = ''.join('<span class="pill%s">%s</span>' % (' on' if p == name else '', esc(p)) for p in PILLS)
    out = re.sub(r'<span class="pill">Workforce.*?Business Consulting</span>', pills, out, flags=re.S)
    assert out.count('<div class="card">') == 6, name
    assert '—' not in out.replace(FONTS, '') and '–' not in out.replace(FONTS, ''), 'dash in ' + name
    for bad in ('Cornerstone', 'Sherweb', 'Redirect', 'Connecteam', 'Vero', 'G&A', 'Justworks', 'ADP', 'Gusto', 'Paychex', 'our health plan', 'our master plan'):
        assert bad not in out.replace(FONTS, '').replace(LOGO, ''), bad + ' in ' + name
    path = os.path.join(OUTROOT, d['file'] + '.html')
    open(path, 'w', encoding='utf-8').write(out); print('built', path)
    return path
if __name__ == '__main__':
    paths = [build(n, d) for n, d in D.items()]
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'division_sheets_paths.txt'), 'w').write('\n'.join(paths))
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'division_sheets_changed.md'), 'w').write('\n'.join('- **%s**: %s' % (n, d['changed']) for n, d in D.items()))
