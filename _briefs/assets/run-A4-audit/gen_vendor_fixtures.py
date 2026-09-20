#!/usr/bin/env python3
"""Run A4 Job 2: invented vendor/software fixtures for the Vendor & Software Audit xlsx path."""
import csv, os
from openpyxl import Workbook

OUT = os.path.join(os.path.dirname(__file__), "fixtures", "vendors")
os.makedirs(OUT, exist_ok=True)

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow(r)

def write_xlsx(path, rows):
    wb = Workbook(); ws = wb.active
    for r in rows:
        ws.append(r)
    wb.save(path)

# (a) bank checking CSV, three monthly files, invented recurring vendors
BANK_VENDORS = [("GUSTO PAYROLL FEE", 189.00), ("MICROSOFT 365 BUSINESS", 49.00), ("ZOOM VIDEO COMMUNICATIONS", 14.99)]
for i, month in enumerate(["2026-06", "2026-07", "2026-08"]):
    rows = [["Date", "Description", "Amount", "Balance"]]
    bal = 42000.0 - i * 500
    for vendor, amt in BANK_VENDORS:
        bal -= amt
        rows.append([f"{month}-05", vendor, f"-{amt:.2f}", f"{bal:.2f}"])
    # a one-off noise transaction each month, should be dropped (not recurring, uncategorized)
    bal -= 220.00
    rows.append([f"{month}-18", f"OFFICE SUPPLY RUN {i+1}", "-220.00", f"{bal:.2f}"])
    write_csv(os.path.join(OUT, f"a-bank-checking-{month}.csv"), rows)

# (b) card CSV, three monthly files, middle month duplicated across two files (dedupe test)
CARD_VENDORS = [("ADOBE CREATIVE CLOUD", 54.99), ("DROPBOX BUSINESS", 20.00), ("SLACK TECHNOLOGIES", 12.50)]
def card_rows(month):
    rows = [["Date", "Description", "Amount", "Balance"]]
    bal = 8000.0
    for vendor, amt in CARD_VENDORS:
        bal -= amt
        rows.append([f"{month}-10", vendor, f"-{amt:.2f}", f"{bal:.2f}"])
    return rows
write_csv(os.path.join(OUT, "b-card-2026-06.csv"), card_rows("2026-06"))
write_csv(os.path.join(OUT, "b-card-2026-07-fileA.csv"), card_rows("2026-07"))
write_csv(os.path.join(OUT, "b-card-2026-07-fileB.csv"), card_rows("2026-07"))  # duplicate of month 07, different file
write_csv(os.path.join(OUT, "b-card-2026-08.csv"), card_rows("2026-08"))

# (c) QuickBooks "Expenses by Vendor Summary" export, xlsx, title rows, Vendor/Total columns, no dates, TOTAL row
QB_VENDORS = [("Fixture Insurance Brokers", 4500.00), ("Fixture Cleaning Co", 900.00), ("Fixture IT Services LLC", 2100.00)]
qb_rows = [
    ["Fixture Client C, LLC"],
    ["Expenses by Vendor Summary"],
    ["January - March 2026"],
    [""],
    ["Vendor", "Total"],
]
grand = 0.0
for v, amt in QB_VENDORS:
    qb_rows.append([v, amt]); grand += amt
qb_rows.append(["TOTAL", grand])
write_xlsx(os.path.join(OUT, "c-quickbooks-vendor-summary.xlsx"), qb_rows)

# (d) Ramp transactions export, xlsx and csv (merchant, amount, date, cardholder, category, memo)
RAMP_MERCHANTS = [("Notion Labs", 96.00), ("Figma Inc", 45.00), ("Calendly", 12.00)]
ramp_rows = [["Merchant", "Amount", "Date", "Cardholder", "Category", "Memo"]]
for month in ["2026-06", "2026-07", "2026-08"]:
    for merchant, amt in RAMP_MERCHANTS:
        ramp_rows.append([merchant, amt, f"{month}-15", "Jordan Ellis", "Software", "Fixture, invented"])
write_csv(os.path.join(OUT, "d-ramp-transactions.csv"), ramp_rows)
write_xlsx(os.path.join(OUT, "d-ramp-transactions.xlsx"), ramp_rows)

print("vendor fixtures written")
