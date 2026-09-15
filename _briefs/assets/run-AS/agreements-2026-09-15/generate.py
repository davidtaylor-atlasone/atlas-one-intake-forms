#!/usr/bin/env python3
"""Atlas One agreements and proposal shell generator (Run AS, 2026-09-15).

Builds the Master Client Services Agreement, the standalone Hold Harmless,
one page Schedules for every service in Job 2 of the brief, the proposal
shell, and a sample proposal per schedule for a fictional client "Tell Me
More LLC". Word masters via python-docx (never edit the output docx by
hand, edit this file and clients/prices below and rebuild); PDF via
LibreOffice headless conversion of the docx (soffice --headless
--convert-to pdf), which keeps a true editable Word master as the source of
truth while still producing a brand-locked PDF, the same "generate, never
hand edit" discipline as tools/bookkeeping-docs/build.py uses for its HTML
+ Playwright pipeline.

Every price in this file comes from prices.json, itself pulled from the
Quick Quote catalogue and Master Pricing V8 (client prices only, no vendor
cost or margin). Fonts (DM Sans, Horas) and the "no dashes in client copy"
rule are the same brand rule bookkeeping-docs/build.py enforces; this
script raises if an em dash or en dash reaches any paragraph.

Run:  python3 generate.py "/path/to/Atlas_One_Master_Kit"
"""
import io
import json
import os
import re
import subprocess
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Cm

HERE = os.path.dirname(os.path.abspath(__file__))

NAVY = RGBColor(0x23, 0x30, 0x4D)
PERI = RGBColor(0x78, 0x8D, 0xE3)
MIST = RGBColor(0xDB, 0xE4, 0xED)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

BODY_FONT = "DM Sans"
HEAD_FONT = "Horas"

with io.open(os.path.join(HERE, "prices.json"), encoding="utf-8") as f:
    PRICES = json.load(f)

DASH_RE = re.compile("[–—]")


def check_no_dash(text):
    if DASH_RE.search(text):
        raise SystemExit(f"generate.py: em/en dash found in client copy, fix the text: {text!r}")
    return text


# ---------------------------------------------------------------- helpers
def set_run(run, size=10.5, bold=False, italic=False, color=NAVY, font=BODY_FONT):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = font
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = rPr.makeelement(qn("w:rFonts"), {})
        rPr.append(rFonts)
    rFonts.set(qn("w:eastAsia"), font)


def add_para(doc, text="", size=10.5, bold=False, italic=False, color=NAVY,
             font=BODY_FONT, space_after=6, align=None):
    text = check_no_dash(text)
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    set_run(r, size, bold, italic, color, font)
    return p


def shaded_cell(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.makeelement(qn("w:shd"), {qn("w:val"): "clear", qn("w:color"): "auto", qn("w:fill"): hexcolor})
    tcPr.append(shd)


def brand_header(doc, doc_title, subtitle):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("ATLAS ONE SOLUTIONS LLC")
    set_run(r, 13, bold=True, color=NAVY, font=HEAD_FONT)
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(2)
    r2 = p2.add_run("One Call Solves Everything.")
    set_run(r2, 9, italic=True, color=PERI, font=BODY_FONT)
    # periwinkle rule
    rule = doc.add_paragraph()
    rule.paragraph_format.space_after = Pt(10)
    rp = rule.paragraph_format
    pPr = rule._p.get_or_add_pPr()
    pBdr = pPr.makeelement(qn("w:pBdr"), {})
    bottom = pPr.makeelement(qn("w:bottom"), {qn("w:val"): "single", qn("w:sz"): "18",
                                               qn("w:space"): "1", qn("w:color"): "788DE3"})
    pBdr.append(bottom)
    pPr.append(pBdr)
    add_para(doc, doc_title, size=17, bold=True, color=NAVY, font=HEAD_FONT, space_after=2)
    if subtitle:
        add_para(doc, subtitle, size=9.5, italic=True, color=NAVY, space_after=12)


def watermark_banner(doc, text):
    """A full-width shaded banner rather than a diagonal Word watermark:
    reliable across Word and LibreOffice and does not need a fifth colour,
    unlike a translucent red diagonal stamp would."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    shaded_cell(cell, "788DE3")
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_run(r, 10, bold=True, color=WHITE)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def h(doc, text, size=12.5, space_before=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(check_no_dash(text))
    set_run(r, size, bold=True, color=NAVY, font=HEAD_FONT)
    return p


def clause(doc, num, title, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(f"{num}  {title}")
    set_run(r, 10.5, bold=True, color=NAVY)
    add_para(doc, text, size=10, space_after=4)


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(check_no_dash(text))
    set_run(r, 10, color=NAVY)


def price_table(doc, rows, headers=("Item", "Amount")):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for i, htext in enumerate(headers):
        hdr[i].text = ""
        shaded_cell(hdr[i], "23304D")
        p = hdr[i].paragraphs[0]
        r = p.add_run(htext)
        set_run(r, 9.5, bold=True, color=WHITE)
    for row in rows:
        cells = table.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            r = p.add_run(check_no_dash(str(val)))
            set_run(r, 9.5, bold=(i == 0), color=NAVY)
    return table


def signature_block(doc, extra_line=None, lead_text=None, skip_heading=False):
    if not skip_heading:
        h(doc, "To accept")
    if lead_text:
        add_para(doc, lead_text, size=10)
    add_para(doc, "Incorporated into and governed by the Atlas One Client Services Agreement.", size=9.5, italic=True)
    if extra_line:
        add_para(doc, extra_line, size=9.5, italic=True)
    table = doc.add_table(rows=2, cols=2)
    table.style = "Table Grid"
    table.cell(0, 0).text = "David Taylor, Atlas One Solutions LLC"
    table.cell(0, 1).text = "Client"
    table.cell(1, 0).text = "Signature / Date: ____________________"
    table.cell(1, 1).text = "Signature / Date: ____________________"
    for row in table.rows:
        for cell in row.cells:
            p = cell.paragraphs[0]
            for r in p.runs:
                set_run(r, 9.5, color=NAVY)


def footer_line(doc):
    add_para(doc, "Atlas One Solutions LLC · Lehi, Utah · 380-225-5217 · David@AtlasOneSolutions.com",
              size=8, color=NAVY, space_after=0)


def new_doc():
    doc = Document()
    section = doc.sections[0]
    section.left_margin = Cm(2.1)
    section.right_margin = Cm(2.1)
    section.top_margin = Cm(1.6)
    section.bottom_margin = Cm(1.6)
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = NAVY
    return doc


def save_and_pdf(doc, out_dir, basename):
    docx_path = os.path.join(out_dir, basename + ".docx")
    doc.save(docx_path)
    r = subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", out_dir, docx_path],
        capture_output=True, text=True, timeout=120,
    )
    pdf_path = os.path.join(out_dir, basename + ".pdf")
    if r.returncode != 0 or not os.path.exists(pdf_path):
        raise SystemExit(f"soffice failed converting {basename}: {r.stdout}\n{r.stderr}")
    return docx_path, pdf_path


# ---------------------------------------------------------------- MSA
def build_msa(out_dir):
    doc = new_doc()
    brand_header(doc, "MASTER CLIENT SERVICES AGREEMENT", "The master agreement. Attach the Schedule for each service the client buys.")
    watermark_banner(doc, "ATTORNEY REVIEW PENDING, DO NOT SEND FOR SIGNATURE UNTIL DAVID CLEARS THIS DOCUMENT")
    add_para(doc, "This Master Client Services Agreement (this Agreement) is entered into as of "
                  "____________________ between Atlas One Solutions LLC, a Utah limited liability company "
                  "(Atlas One), and ____________________ (Client). This Agreement, together with every Schedule "
                  "the Client signs, is the whole agreement between the parties for the services described.", size=10)

    clause(doc, "1.", "Services", "Atlas One provides the services described in each signed Schedule. A Schedule "
           "sets the scope, the deliverables, and any terms specific to that service, and is incorporated into "
           "this Agreement by reference. Adding a new service means signing a new Schedule, not renegotiating "
           "this Agreement.")

    clause(doc, "2.", "Fees and billing", "Fees are set in each Schedule. Monthly fees are billed in advance and "
           "charged automatically to the payment method on file, or invoiced with payment due within ten days of "
           "the invoice date if the Client has not set up automatic payment. A late fee of [__] applies to an "
           "invoice not paid within the stated terms; the exact fee and the day it starts are confirmed by David "
           "before this Agreement is signed. One time and setup fees are due at signing unless the Schedule says "
           "otherwise. Every price in a Schedule is confirmed at signing and does not change mid term without "
           "written notice.")

    clause(doc, "3.", "Term and termination", "This Agreement begins on the date above and continues month to "
           "month unless a Schedule states a different term. Either party may end a service by giving thirty "
           "days written notice; ending one service does not end the others. Atlas One may suspend or end a "
           "service immediately if a payment is more than thirty days past due. On termination, Atlas One "
           "delivers or returns the Client's own data and materials within a reasonable time.")

    clause(doc, "4.", "Confidentiality", "Each party will keep the other's confidential business information "
           "private and use it only to perform this Agreement, except information that is already public, was "
           "already known, or must be disclosed by law. This obligation survives the end of this Agreement.")

    clause(doc, "5.", "Data access", "Where a service requires access to the Client's accounts, software, or "
           "records, the Client grants that access and keeps it active for as long as the service runs. Atlas "
           "One accesses only what a service requires, and the Client's data stays the Client's property at all "
           "times.")

    clause(doc, "6.", "Vendor neutral statement", "Atlas One is vendor neutral. Where a service involves placing "
           "coverage, software, or a service with a third party, Atlas One gathers options, presents them side "
           "by side, and the Client chooses; Atlas One does not steer the Client toward one vendor over another "
           "for its own benefit.")

    clause(doc, "7.", "Independent contractor", "Atlas One provides these services as an independent contractor, "
           "not as the Client's employee, partner, or joint venturer. Nothing in this Agreement creates an "
           "employment relationship between Atlas One and the Client's workforce, except where a separate, "
           "clearly labeled co-employment agreement says otherwise.")

    clause(doc, "8.", "Not legal, tax, or insurance advice", "Atlas One is not a law firm, a CPA firm, or an "
           "insurance carrier. Guidance provided is practical and operational, not legal, tax, or coverage advice; "
           "the Client should have its own attorney, CPA, or licensed agent review any document, filing, or "
           "coverage decision that carries legal or financial weight.")

    clause(doc, "9.", "Limitation of liability", "Atlas One's total liability arising from this Agreement, for "
           "any service, is limited to the fees the Client paid Atlas One for that service in the three months "
           "before the event giving rise to the claim. Neither party is liable to the other for indirect, "
           "incidental, or consequential damages. Nothing in this Agreement limits liability where the law does "
           "not allow it to be limited.")

    clause(doc, "10.", "Hold harmless and indemnification", "The Client will hold Atlas One harmless from, and "
           "indemnify Atlas One against, claims arising from the Client's own decisions, the Client's use of a "
           "deliverable without having it reviewed as recommended, or information the Client provided that Atlas "
           "One reasonably relied on. This clause does not cover Atlas One's own gross negligence or willful "
           "misconduct.")

    clause(doc, "11.", "Governing law", "This Agreement is governed by the laws of the State of Utah, without "
           "regard to conflict of law rules. Any dispute is resolved in the state or federal courts located in "
           "Utah.")

    clause(doc, "12.", "General", "This Agreement, with its Schedules, is the entire agreement between the "
           "parties on this subject and replaces any earlier discussion or proposal. A change to this Agreement "
           "must be in writing and signed by both parties. If a court finds one part of this Agreement "
           "unenforceable, the rest stays in effect.")

    signature_block(doc)
    footer_line(doc)
    return save_and_pdf(doc, out_dir, "Atlas_One_Master_Client_Services_Agreement")


# ---------------------------------------------------------- Hold Harmless
def build_hold_harmless(out_dir):
    doc = new_doc()
    brand_header(doc, "HOLD HARMLESS AND ACKNOWLEDGEMENT",
                  "Standalone, one page. Use for a document only sale that is not covered by a signed Master Agreement.")
    watermark_banner(doc, "ATTORNEY REVIEW PENDING, DO NOT SEND FOR SIGNATURE UNTIL DAVID CLEARS THIS DOCUMENT")
    add_para(doc, "This Hold Harmless and Acknowledgement (this Acknowledgement) is entered into as of "
                  "____________________ between Atlas One Solutions LLC (Atlas One) and ____________________ "
                  "(Client), covering the document or deliverable described below.", size=10)

    clause(doc, "1.", "Deliverable", "Deliverable: ____________________. Atlas One prepared this deliverable "
           "using the information the Client provided and Atlas One's standard templates and practices.")

    clause(doc, "2.", "Not legal advice", "This deliverable is not legal advice, and Atlas One is not a law "
           "firm. The Client is responsible for having its own attorney review this deliverable, and any policy "
           "or agreement built from it, before relying on it, especially for a multi state workforce or an "
           "unusual situation.")

    clause(doc, "3.", "Hold harmless", "The Client will hold Atlas One harmless from, and indemnify Atlas One "
           "against, any claim arising from the Client's use of this deliverable, including a claim arising "
           "from the Client's choice to use it without having it reviewed by counsel as recommended above. This "
           "clause does not cover Atlas One's own gross negligence or willful misconduct in preparing it.")

    clause(doc, "4.", "No ongoing obligation", "This Acknowledgement covers this deliverable only. It does not "
           "create an ongoing service relationship; a future update or a different deliverable is a new "
           "engagement, priced and delivered separately.")

    signature_block(doc, extra_line="Governed by Utah law. This Acknowledgement, not the Master Agreement, "
                                     "covers this document only sale.")
    footer_line(doc)
    return save_and_pdf(doc, out_dir, "Atlas_One_Hold_Harmless_and_Acknowledgement")


# --------------------------------------------------------------- Schedule
def build_schedule(out_dir, key, title, intro, clauses, table_rows, table_headers=("Item", "Amount"),
                    extra_note=None):
    doc = new_doc()
    brand_header(doc, f"SCHEDULE, {title.upper()}", "A Schedule to the Atlas One Client Services Agreement")
    add_para(doc, intro, size=10)
    for num, ctitle, ctext in clauses:
        clause(doc, num, ctitle, ctext)
    h(doc, "Pricing")
    price_table(doc, table_rows, headers=table_headers)
    if extra_note:
        add_para(doc, extra_note, size=9, italic=True, space_after=6)
    signature_block(doc)
    footer_line(doc)
    return save_and_pdf(doc, out_dir, f"Atlas_One_{key}_Schedule")


def schedule_bookkeeping(out_dir):
    pr = PRICES["bookkeeping"]
    rows = [[pr["small"]["label"], pr["small"]["price"]],
            [pr["medium"]["label"], pr["medium"]["price"]],
            [pr["large"]["label"], pr["large"]["price"]],
            [pr["catchup"]["label"], pr["catchup"]["price"]],
            [pr["advisory"]["label"], pr["advisory"]["price"]],
            [pr["quickbooks_sub"]["label"], pr["quickbooks_sub"]["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One provides bookkeeping at the plan level selected below: transactions "
         "categorized, accounts reconciled, and a monthly close delivered on a set schedule. Adding "
         "accounts payable, accounts receivable, job costing, or advisory is a plan change, not a new "
         "engagement."),
        ("2.", "Electronic payment", "The Client pays by the electronic payment method selected on the first "
         "invoice, or by another method the parties agree to in writing."),
        ("3.", "Books access", "The Client grants Atlas One read and write access to the QuickBooks Online "
         "company file (or the accounting software in use) for as long as this Schedule is active."),
    ]
    return build_schedule(out_dir, "Bookkeeping", "Bookkeeping",
                            "This Schedule (Bookkeeping Schedule) covers monthly bookkeeping, catch up work, and "
                            "hourly advisory. It is entered into as of ____________________ and is incorporated "
                            "into the Atlas One Client Services Agreement.",
                            clauses, rows)


def schedule_gl_import(out_dir):
    pr = PRICES["gl_import"]
    rows = [[pr["standard"]["label"], pr["standard"]["price"]],
            [pr["weekly"]["label"], pr["weekly"]["price"]],
            [pr["setup"]["label"], pr["setup"]["price"]],
            [pr["extra"]["label"], pr["extra"]["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One converts every payroll run into a QuickBooks or Sage journal entry, as a "
         "lump sum or split by job, on the schedule the Client's payroll runs."),
        ("2.", "Client review before posting", "The Client reviews every journal entry before it posts to the "
         "Client's books. Atlas One prepares the entry; the Client's own review is the final check before it "
         "becomes part of the Client's official records."),
        ("3.", "Payroll access", "The Client grants Atlas One read access to the payroll reports needed to "
         "build the journal, for as long as this Schedule is active."),
    ]
    return build_schedule(out_dir, "Payroll_to_GL_Converter", "Payroll to GL Converter",
                            "This Schedule (Payroll to GL Converter Schedule) covers converting the Client's "
                            "payroll into accounting journal entries. It is entered into as of "
                            "____________________ and is incorporated into the Atlas One Client Services "
                            "Agreement.",
                            clauses, rows)


def schedule_cert_payroll(out_dir):
    pr = PRICES["cert_payroll"]["monthly"]
    rows = [[pr["label"], pr["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One prepares and files certified payroll reports (WH-347 or the state "
         "equivalent) for each active job the Client identifies, with hours split by classification and "
         "wage determination."),
        ("2.", "Client attestation", "The Client attests that hours worked and the wage determinations the "
         "Client provides are accurate. Atlas One prepares the report from what the Client supplies; the "
         "Client remains responsible for the underlying accuracy of hours and pay."),
        ("3.", "Active jobs", "Billing follows the number of active jobs reported each month. The Client "
         "notifies Atlas One when a job starts or closes so billing stays current."),
    ]
    return build_schedule(out_dir, "Certified_Payroll", "Certified Payroll",
                            "This Schedule (Certified Payroll Schedule) covers prevailing wage reporting per "
                            "active job. It is entered into as of ____________________ and is incorporated into "
                            "the Atlas One Client Services Agreement.",
                            clauses, rows)


def schedule_wc_audit(out_dir):
    pr = PRICES["wc_audit"]["contingency"]
    rows = [[pr["label"], pr["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One reviews the Client's workers compensation experience, classification, and "
         "premium history for overcharges, misclassification, and recoverable premium, and pursues a recovery "
         "with the carrier or the rating bureau on the Client's behalf."),
        ("2.", "Authorization to contact the carrier", "The Client authorizes Atlas One to contact the "
         "Client's workers compensation carrier and rating bureau, and to request and receive the records "
         "needed to complete the review and pursue a recovery."),
        ("3.", "Contingency fee", "Atlas One's fee is a percentage of the premium actually recovered, paid "
         "only when a recovery is made. If no recovery is found or paid, the Client owes nothing under this "
         "Schedule."),
    ]
    return build_schedule(out_dir, "WC_Audit_Recovery", "Workers Comp Audit Recovery",
                            "This Schedule (Audit Recovery Schedule) covers workers compensation premium "
                            "recovery on a contingency basis. It is entered into as of ____________________ and "
                            "is incorporated into the Atlas One Client Services Agreement.",
                            clauses, rows,
                            extra_note="Contingency percentage confirmed by David before this Schedule is sent for signature.")


def schedule_coi(out_dir):
    pr = PRICES["coi_tracking"]["monthly"]
    rows = [[pr["label"], pr["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One tracks certificates of insurance for the Client's subcontractors: "
         "collecting current certificates, flagging an expired or missing certificate, and keeping a record "
         "the Client can review at any time."),
        ("2.", "Client decides who works", "Atlas One tracks coverage status and reports it; the Client alone "
         "decides which subcontractors are allowed to work, including a subcontractor whose certificate has "
         "lapsed. Atlas One does not make that call."),
    ]
    return build_schedule(out_dir, "COI_Tracking", "COI Tracking",
                            "This Schedule (Software Tools Schedule, COI Tracking) covers certificate of "
                            "insurance tracking for subcontractors. It is entered into as of "
                            "____________________ and is incorporated into the Atlas One Client Services "
                            "Agreement.",
                            clauses, rows,
                            extra_note="Price confirmed by David before this Schedule is sent for signature.")


def schedule_ai_services(out_dir):
    pr = PRICES["ai_services"]
    rows = [[pr["setup"]["label"], pr["setup"]["price"]],
            [pr["essentials"]["label"], pr["essentials"]["price"]],
            [pr["professional"]["label"], pr["professional"]["price"]],
            [pr["extra_mailbox"]["label"], pr["extra_mailbox"]["price"]],
            [pr["task_agent_standalone"]["label"], pr["task_agent_standalone"]["price"]],
            [pr["task_agent_bundled"]["label"], pr["task_agent_bundled"]["price"]],
            [pr["task_agent_setup"]["label"], pr["task_agent_setup"]["price"]],
            [PRICES["advisory_support"]["over_allowance"]["label"], PRICES["advisory_support"]["over_allowance"]["price"]]]
    clauses = [
        ("1.", "AI services covered", "Atlas One sets up, configures, and supports the AI Email Assistant, the "
         "AI Task Agent, or both, as selected below. Both run inside the Client's own Microsoft 365 or Google "
         "Workspace account."),
        ("2.", "Human approval, nature of AI output", "The AI services generate drafts and suggestions only. "
         "No email or other communication is sent, and no external action is taken, without the Client's "
         "review and approval. AI output can be inaccurate or incomplete; the Client is responsible for "
         "reviewing it before it is used."),
        ("3.", "Data access consent", "The Client's administrator grants the permissions the services "
         "require and keeps that consent active. The Client's data stays in the Client's own account at all "
         "times; Atlas One does not copy or store the content of the Client's email as part of the service."),
    ]
    return build_schedule(out_dir, "AI_Services", "AI Services",
                            "This Schedule (AI Services Schedule) covers the AI Email Assistant and the AI Task "
                            "Agent. It is entered into as of ____________________ and is incorporated into the "
                            "Atlas One Client Services Agreement. Prices verified against the Quick Quote "
                            "catalogue, 2026-09-15.",
                            clauses, rows)


def schedule_documents(out_dir):
    pr = PRICES["documents"]
    rows = [[pr["handbook"]["label"], pr["handbook"]["price"]],
            [pr["handbook_update"]["label"], pr["handbook_update"]["price"]],
            [pr["safety"]["label"], pr["safety"]["price"]],
            [pr["safety_update"]["label"], pr["safety_update"]["price"]],
            [pr["agreement_each"]["label"], pr["agreement_each"]["price"]],
            [pr["agreement_bundle"]["label"], pr["agreement_bundle"]["price"]],
            [pr["hr_docs"]["label"], pr["hr_docs"]["price"]]]
    clauses = [
        ("1.", "Scope", "Atlas One builds the document the Client selects below (handbook, safety manual, "
         "W-2 at will agreement, 1099 contractor agreement, NDA, or another HR document) from the Client's own "
         "policies and Atlas One's standard, 50 state aware templates."),
        ("2.", "Not legal advice, have counsel review", "These deliverables are not legal advice. The Client "
         "should have its own attorney review a document before relying on it, especially for a multi state "
         "workforce. The standalone Hold Harmless and Acknowledgement is signed before a document builder "
         "deliverable is released."),
    ]
    return build_schedule(out_dir, "Document_Services", "Document Services",
                            "This Schedule (Document Services Schedule) covers handbooks, safety manuals, and "
                            "employment agreements built by Atlas One. It is entered into as of "
                            "____________________ and is incorporated into the Atlas One Client Services "
                            "Agreement.",
                            clauses, rows,
                            extra_note="Signed alongside the standalone Hold Harmless and Acknowledgement before a document is released.")


def schedule_membership(out_dir):
    pr = PRICES["membership"]
    rows = [[pr["essential"]["label"], pr["essential"]["price"]],
            [pr["professional"]["label"], pr["professional"]["price"]],
            [pr["enterprise"]["label"], pr["enterprise"]["price"]],
            [pr["concierge"]["label"], pr["concierge"]["price"]]]
    clauses = [
        ("1.", "Scope", "Membership is the platform layer that ties every Atlas One division together: "
         "self-service tools, the vendor and software audit, and, at higher tiers, concierge support and "
         "dedicated coordination across bookkeeping, benefits, payroll, and risk."),
        ("2.", "Setup fee and annual option", "A one time setup fee applies at some tiers as shown below. "
         "Setup is often waived at signing or on an annual plan; the Client's proposal states the exact setup "
         "due, if any."),
    ]
    return build_schedule(out_dir, "Membership", "Membership",
                            "This Schedule (Membership Schedule) covers the Atlas One membership tier the "
                            "Client selects. It is entered into as of ____________________ and is incorporated "
                            "into the Atlas One Client Services Agreement.",
                            clauses, rows)


# ------------------------------------------------------------- Proposal
PROPOSAL_SECTIONS = ["Overview", "Scope", "What is not included", "Pricing", "How billing works",
                     "What we need from you", "To accept"]


def build_proposal(out_dir, basename, service_label, client_name, overview, scope_items, not_included,
                    table_rows, table_headers, billing, need_from_you, schedule_name):
    doc = new_doc()
    brand_header(doc, "PROPOSAL", f"{service_label}, prepared for {client_name}")
    add_para(doc, "Overview", size=12.5, bold=True, color=NAVY, font=HEAD_FONT, space_after=4)
    add_para(doc, overview, size=10)

    h(doc, "Scope")
    for item in scope_items:
        bullet(doc, item)

    h(doc, "What is not included")
    for item in not_included:
        bullet(doc, item)

    h(doc, "Pricing")
    price_table(doc, table_rows, headers=table_headers)

    h(doc, "How billing works")
    add_para(doc, billing, size=10)

    h(doc, "What we need from you")
    for item in need_from_you:
        bullet(doc, item)

    signature_block(doc, lead_text=f"Sign the Atlas One Client Services Agreement and the {schedule_name} "
                    "attached with this proposal. Work begins once both are signed and, where a setup fee "
                    "applies, that fee is paid.")
    footer_line(doc)
    return save_and_pdf(doc, out_dir, basename)


def build_proposal_shell(out_dir):
    """The blank shell, unfilled, showing the section structure the brief calls for."""
    doc = new_doc()
    brand_header(doc, "PROPOSAL SHELL", "Blank master. Copy this structure for every proposal; do not edit this file directly, edit generate.py.")
    for section in PROPOSAL_SECTIONS:
        h(doc, section)
        add_para(doc, "[ ____________________ ]", size=10, italic=True)
    footer_line(doc)
    return save_and_pdf(doc, out_dir, "Atlas_One_Proposal_Shell")


CLIENT = "Tell Me More LLC"


def sample_proposals(out_dir):
    out = []

    pr = PRICES["bookkeeping"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_Bookkeeping",
        "Bookkeeping", CLIENT,
        f"{CLIENT} gets a monthly close that is accurate, current, and ready whenever a bank, lender, or CPA "
        "asks, plus a single advisor for the books instead of a spreadsheet nobody trusts.",
        ["Transactions categorized and accounts reconciled every month",
         "A clean monthly close delivered on a set schedule",
         "QuickBooks Online managed under Atlas One's ProAdvisor partner pricing"],
        ["Filing tax returns (referred to a CPA partner on request)",
         "Payroll processing itself (see the Payroll to GL Converter proposal if needed)"],
        [[pr["medium"]["label"], pr["medium"]["price"]], [pr["quickbooks_sub"]["label"], pr["quickbooks_sub"]["price"]]],
        ("Item", "Amount"),
        "Monthly fee billed in advance to the payment method on file. Catch up work, if any, is billed at the "
        "plan rate for each month of catch up needed.",
        ["Bank and card statements or read access to the accounts",
         "The most recent tax return or prior bookkeeper's file, if switching"],
        "Bookkeeping Schedule"))

    pr = PRICES["gl_import"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_Payroll_to_GL_Converter",
        "Payroll to GL Converter", CLIENT,
        f"Every payroll run for {CLIENT} becomes a reviewed, ready to post journal entry in QuickBooks, with "
        "no manual re-entry.",
        ["A journal entry prepared for every payroll run, lump sum or split by job",
         f"{CLIENT}'s own review before anything posts to the books"],
        ["Running payroll itself (this converts the output, it does not process pay)"],
        [[pr["standard"]["label"], pr["standard"]["price"]], [pr["setup"]["label"], pr["setup"]["price"]]],
        ("Item", "Amount"),
        "Monthly fee billed in advance. Setup is billed once, at signing.",
        ["Read access to the payroll reports each pay period"],
        "Payroll to GL Converter Schedule"))

    pr = PRICES["cert_payroll"]["monthly"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_Certified_Payroll",
        "Certified Payroll", CLIENT,
        f"{CLIENT} gets certified payroll reports filed correctly and on time for every active job, with hours "
        "split by classification.",
        ["A WH-347 or state equivalent report prepared and filed for each active job",
         "Hours split by classification and wage determination"],
        ["Determining prevailing wage rates themselves (Atlas One applies the rate the Client attests to)"],
        [[pr["label"], pr["price"]]],
        ("Item", "Amount"),
        "Billed monthly based on the number of active jobs reported that month.",
        ["Certified payroll hours and wage determinations for each active job"],
        "Certified Payroll Schedule"))

    pr = PRICES["wc_audit"]["contingency"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_WC_Audit_Recovery",
        "Workers Comp Audit Recovery", CLIENT,
        f"Atlas One reviews {CLIENT}'s workers compensation history for overcharges and recoverable premium, "
        "at no cost unless a recovery is found.",
        ["A full review of experience rating, classification, and premium history",
         "Pursuit of any recovery directly with the carrier or rating bureau"],
        ["A guarantee of recovery; some reviews find nothing to recover"],
        [[pr["label"], pr["price"]]],
        ("Item", "Amount"),
        "No fee unless a recovery is made. The fee is a percentage of the amount actually recovered, paid once.",
        ["Authorization to contact the carrier and rating bureau",
         "Recent workers comp policies and premium audit history"],
        "Audit Recovery Schedule"))

    pr = PRICES["coi_tracking"]["monthly"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_COI_Tracking",
        "COI Tracking", CLIENT,
        f"{CLIENT} stops chasing subcontractors for paperwork. Atlas One tracks every certificate of insurance "
        "and flags a lapse before it becomes a liability.",
        ["Certificates of insurance collected and tracked for every subcontractor",
         "A flag when a certificate is missing or about to expire"],
        ["Deciding which subcontractors are allowed to work (that stays the Client's call)"],
        [[pr["label"], pr["price"]]],
        ("Item", "Amount"),
        "Monthly fee billed in advance.",
        ["A current list of active subcontractors"],
        "Software Tools Schedule"))

    pr = PRICES["ai_services"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_AI_Services",
        "AI Email Assistant", CLIENT,
        f"{CLIENT}'s inbox gets a first pass every day: drafted, sorted, and flagged, with nothing sent "
        "without a human's approval.",
        ["Setup and configuration inside the Client's own Microsoft 365 or Google Workspace account",
         "Drafts, sorting, and flagging on every incoming message",
         "Monthly support allowance included"],
        ["Sending anything without the Client's review and approval"],
        [[pr["setup"]["label"], pr["setup"]["price"]], [pr["essentials"]["label"], pr["essentials"]["price"]]],
        ("Item", "Amount"),
        "Setup billed once at signing. Monthly fee billed in advance thereafter.",
        ["Administrator consent to connect the mailbox"],
        "AI Services Schedule"))

    pr = PRICES["documents"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_Document_Services",
        "Employee Handbook", CLIENT,
        f"A custom, bilingual, fifty state aware handbook built around {CLIENT}'s own policies, not a generic "
        "template.",
        ["A custom handbook drafted from the Client's policies and Atlas One's standard, compliant framework",
         "One round of revisions before delivery"],
        ["Legal review (the Client's own attorney reviews the handbook before it is rolled out, per the "
         "standalone Hold Harmless)"],
        [[pr["handbook"]["label"], pr["handbook"]["price"]], [pr["handbook_update"]["label"], pr["handbook_update"]["price"]]],
        ("Item", "Amount"),
        "One time fee billed at signing. The annual update is optional and billed separately if selected.",
        ["Current policies, if any, and a list of states where employees work"],
        "Document Services Schedule"))

    pr = PRICES["membership"]
    out.append(build_proposal(
        out_dir, "Sample_Proposal_Membership",
        "Membership, Professional", CLIENT,
        f"{CLIENT} gets a concierge team on the line with vendors, priority escalation, and a monthly advisory "
        "call, tying every Atlas One service together.",
        ["Concierge support team", "Priority escalation and up to ten tickets a month", "A monthly advisory call"],
        ["Services outside the six divisions Atlas One covers"],
        [[pr["professional"]["label"], pr["professional"]["price"]]],
        ("Item", "Amount"),
        "Monthly fee billed in advance. Setup is often waived at signing, confirmed on the invoice.",
        ["A short intake call to confirm priorities across the six divisions"],
        "Membership Schedule"))

    return out


# --------------------------------------------------------------------- main
def main():
    mk = sys.argv[1] if len(sys.argv) > 1 else "."
    mkt = os.path.normpath(os.path.join(mk, "..", ".."))
    out_dir = os.path.join(mkt, "A1_Sales", "A1 Agreements", "2026-09-15 masters")
    os.makedirs(out_dir, exist_ok=True)

    built = []
    built.append(build_msa(out_dir))
    built.append(build_hold_harmless(out_dir))
    built.append(schedule_bookkeeping(out_dir))
    built.append(schedule_gl_import(out_dir))
    built.append(schedule_cert_payroll(out_dir))
    built.append(schedule_wc_audit(out_dir))
    built.append(schedule_coi(out_dir))
    built.append(schedule_ai_services(out_dir))
    built.append(schedule_documents(out_dir))
    built.append(schedule_membership(out_dir))
    built.append(build_proposal_shell(out_dir))
    built.extend(sample_proposals(out_dir))

    for docx_path, pdf_path in built:
        print("wrote:", os.path.basename(docx_path), "+", os.path.basename(pdf_path))
    print(f"\n{len(built)} documents built in {out_dir}")


if __name__ == "__main__":
    main()
