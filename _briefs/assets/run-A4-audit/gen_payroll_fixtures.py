#!/usr/bin/env python3
"""Run A4 Job 1: invented payroll register fixtures, csv + xlsx pairs (and (e) as text).
All data invented, no real company or person."""
import csv, os
from openpyxl import Workbook

OUT = os.path.join(os.path.dirname(__file__), "fixtures", "payroll")
os.makedirs(OUT, exist_ok=True)

DEPTS = ["Sales", "Operations", "Admin"]
NAMES = [
    "Avery Chen","Blake Nguyen","Casey Rivera","Dana Okafor","Elliot Brooks",
    "Frankie Silva","Gray Patel","Harper Lund","Iris Novak","Jules Bianchi",
    "Kai Thompson","Lane Whitfield","Morgan Reyes","Noor Haddad","Oakley Vance",
    "Parker Sung","Quinn Delacroix","Riley Osei","Sage Falk","Toby Marchetti",
]

def money(n):
    return round(n, 2)

def build_employees():
    """20 invented employees, 3 depts, one biweekly pay period."""
    rows = []
    for i, name in enumerate(NAMES):
        dept = DEPTS[i % 3]
        gross = money(1400 + (i * 37.5) % 900)
        er_fica = money(gross * 0.062)
        er_med = money(gross * 0.0145)
        er_futa = money(gross * 0.006)
        er_suta = money(gross * 0.014)
        ee_401k = money(gross * 0.03) if i % 4 != 0 else 0
        er_match = money(ee_401k * 0.5)
        ee_health = 45.0 if i % 3 == 0 else 0
        fed_wh = money(gross * 0.11)
        state_wh = money(gross * 0.045)
        net = money(gross - ee_401k - ee_health - fed_wh - state_wh)
        rows.append({
            "id": f"EE{100+i}", "name": name, "dept": dept, "gross": gross,
            "er_fica": er_fica, "er_med": er_med, "er_futa": er_futa, "er_suta": er_suta,
            "ee_401k": ee_401k, "er_match": er_match, "ee_health": ee_health,
            "fed_wh": fed_wh, "state_wh": state_wh, "net": net,
        })
    return rows

EMP = build_employees()

def write_csv(path, header, body_rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        for r in header:
            w.writerow(r)
        for r in body_rows:
            w.writerow(r)

def write_xlsx(path, all_rows):
    wb = Workbook()
    ws = wb.active
    for r in all_rows:
        ws.append(r)
    wb.save(path)

# ---------- (a) modern online payroll journal ----------
def fixture_a():
    header = ["Employee ID","Employee Name","Department","Gross Pay","Employer FICA","Employer Medicare",
               "Employer FUTA","Employer SUTA","401k Employee","Employer 401k Match","Health Employee",
               "Federal Withholding","State Withholding","Net Pay"]
    body = []
    for e in EMP:
        body.append([e["id"], e["name"], e["dept"], e["gross"], e["er_fica"], e["er_med"], e["er_futa"],
                     e["er_suta"], e["ee_401k"], e["er_match"], e["ee_health"], e["fed_wh"], e["state_wh"], e["net"]])
    write_csv(os.path.join(OUT, "a-modern-journal.csv"), [header], body)
    write_xlsx(os.path.join(OUT, "a-modern-journal.xlsx"), [header]+body)

# ---------- (b) legacy big provider register ----------
def fixture_b():
    header_block = [
        ["Big Provider Payroll Register (invented, fixture only)"],
        ["Client: Fixture Client B, LLC"],
        ["Pay Period: 09/01/2026 to 09/14/2026    Check Date: 09/18/2026"],
        [""],
    ]
    header = ["Emp #","Employee Name","Dept","Gross Pay","ER FICA","ER Medicare","ER FUTA","ER SUTA","EE Ded 401k","Net Check"]
    body = []
    subtotals_needed = {}
    for e in EMP:
        row = [e["id"], e["name"], e["dept"], e["gross"], e["er_fica"], e["er_med"], e["er_futa"], e["er_suta"], e["ee_401k"], e["net"]]
        body.append(row)
        subtotals_needed.setdefault(e["dept"], []).append(e)
    # group rows by dept with subtotal after each group (register is dept-sorted)
    grouped = []
    for d in DEPTS:
        dept_rows = [r for r in body if r[2] == d]
        grouped.extend(dept_rows)
        sub_gross = round(sum(r[3] for r in dept_rows), 2)
        sub_fica = round(sum(r[4] for r in dept_rows), 2)
        sub_med = round(sum(r[5] for r in dept_rows), 2)
        sub_futa = round(sum(r[6] for r in dept_rows), 2)
        sub_suta = round(sum(r[7] for r in dept_rows), 2)
        sub_401k = round(sum(r[8] for r in dept_rows), 2)
        sub_net = round(sum(r[9] for r in dept_rows), 2)
        grouped.append([f"Subtotal {d}", "", "", sub_gross, sub_fica, sub_med, sub_futa, sub_suta, sub_401k, sub_net])
    grand_gross = round(sum(r[3] for r in body), 2)
    grand_fica = round(sum(r[4] for r in body), 2)
    grand_med = round(sum(r[5] for r in body), 2)
    grand_futa = round(sum(r[6] for r in body), 2)
    grand_suta = round(sum(r[7] for r in body), 2)
    grand_401k = round(sum(r[8] for r in body), 2)
    grand_net = round(sum(r[9] for r in body), 2)
    grand = ["Grand Total", "", "", grand_gross, grand_fica, grand_med, grand_futa, grand_suta, grand_401k, grand_net]
    fee_line = ["Processing Fee", "", "", "", "", "", "", "", "", 275.00]
    all_csv_rows = header_block + [header] + grouped + [grand, fee_line]
    with open(os.path.join(OUT, "b-legacy-register.csv"), "w", newline="") as f:
        w = csv.writer(f)
        for r in all_csv_rows:
            w.writerow(r)
    write_xlsx(os.path.join(OUT, "b-legacy-register.xlsx"), all_csv_rows)
    return {"grand_gross": grand_gross, "fee": 275.00}

# ---------- (c) PEO invoice ----------
def fixture_c():
    header_block = [
        ["Fixture PEO Services Invoice (invented, fixture only)"],
        ["Invoice #: INV-90210    Pay Date: 09/18/2026"],
        [""],
        ["Employee Charges"],
    ]
    header = ["Employee Name","Department","Gross Wages","Employer Taxes","401k Match","Admin Fee Per Check","Net Pay"]
    body = []
    admin_fee_per_check = 6.50
    for e in EMP:
        er_taxes = round(e["er_fica"]+e["er_med"]+e["er_futa"]+e["er_suta"], 2)
        body.append([e["name"], e["dept"], e["gross"], er_taxes, e["er_match"], admin_fee_per_check, e["net"]])
    total_gross = round(sum(r[2] for r in body), 2)
    total_er_tax = round(sum(r[3] for r in body), 2)
    total_match = round(sum(r[4] for r in body), 2)
    total_fee = round(admin_fee_per_check*len(body), 2)
    totals = ["Invoice Total", "", total_gross, total_er_tax, total_match, total_fee, round(sum(r[6] for r in body),2)]
    all_rows = header_block + [header] + body + [totals]
    with open(os.path.join(OUT, "c-peo-invoice.csv"), "w", newline="") as f:
        w = csv.writer(f)
        for r in all_rows:
            w.writerow(r)
    write_xlsx(os.path.join(OUT, "c-peo-invoice.xlsx"), all_rows)
    # (e) same PEO invoice as pasted text (tab-separated, like a copy/paste from a PDF table)
    lines = []
    lines.append("Fixture PEO Services Invoice (invented, fixture only)")
    lines.append("Invoice #: INV-90210\tPay Date: 09/18/2026")
    lines.append("")
    lines.append("Employee Charges")
    lines.append("\t".join(header))
    for r in body:
        lines.append("\t".join(str(x) for x in r))
    lines.append("\t".join(str(x) for x in totals))
    with open(os.path.join(OUT, "e-peo-invoice-pasted.txt"), "w") as f:
        f.write("\n".join(lines))
    return {"total_gross": total_gross, "total_fee": total_fee, "admin_fee_per_check": admin_fee_per_check}

# ---------- (d) accounting suite payroll summary, transposed (employees as columns) ----------
def fixture_d():
    names = [e["name"] for e in EMP[:10]]  # keep it to 10 for width
    rows = []
    rows.append(["Fixture Accounting Suite Payroll Summary (invented, fixture only)"])
    rows.append(["Pay Period 09/01/2026 - 09/14/2026"])
    rows.append([""])
    rows.append(["Wages"] + names)
    rows.append(["Regular Pay"] + [e["gross"] for e in EMP[:10]])
    rows.append([""])
    rows.append(["Employer Taxes"] + names)
    rows.append(["FICA"] + [e["er_fica"] for e in EMP[:10]])
    rows.append(["Medicare"] + [e["er_med"] for e in EMP[:10]])
    rows.append(["FUTA"] + [e["er_futa"] for e in EMP[:10]])
    rows.append(["SUTA"] + [e["er_suta"] for e in EMP[:10]])
    rows.append([""])
    rows.append(["Deductions"] + names)
    rows.append(["401k Employee"] + [e["ee_401k"] for e in EMP[:10]])
    rows.append(["Health Employee"] + [e["ee_health"] for e in EMP[:10]])
    with open(os.path.join(OUT, "d-suite-summary-transposed.csv"), "w", newline="") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow(r)
    write_xlsx(os.path.join(OUT, "d-suite-summary-transposed.xlsx"), rows)
    return {"names": names, "gross": [e["gross"] for e in EMP[:10]]}

if __name__ == "__main__":
    fixture_a()
    b = fixture_b()
    c = fixture_c()
    d = fixture_d()
    import json
    print(json.dumps({"b": b, "c": c, "d_gross_total": round(sum(d["gross"]),2), "headcount": len(EMP)}, indent=2))
