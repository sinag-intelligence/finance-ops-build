"""Make fake monthly PDF bank statements from the fake Fake Builders CSV.

Fake data only. The bank, the address and the account number are made up.
Run: python data/practice/fake-builders/make_bank_statements.py  (needs fpdf2)
Output: 01_from_client/bank_statements/fake_builders_statement_2026-MM.pdf
"""
import csv
from collections import defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path

from fpdf import FPDF

HERE = Path(__file__).parent
CSV_FILE = HERE / "01_from_client" / "fake_builders_bank_2026-08_to_10.csv"
OUT_DIR = HERE / "01_from_client" / "bank_statements"
OPENING = Decimal("8500.00")
MONTH_ENDS = {8: date(2026, 8, 31), 9: date(2026, 9, 30), 10: date(2026, 10, 31)}


def money(x):
    return f"{x:,.2f}"


def read_lines():
    by_month = defaultdict(list)
    with open(CSV_FILE, newline="") as f:
        for row in csv.DictReader(f):
            m, d, y = (int(p) for p in row["Date"].split("/"))
            by_month[m].append((date(y, m, d), row["Description"], Decimal(row["Amount"])))
    return by_month


def make_statement(month, lines, beginning):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 8, "PINE RIVER COMMUNITY BANK", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "FAKE BANK - PRACTICE DOCUMENT ONLY", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    start = date(2026, month, 1)
    end = MONTH_ENDS[month]
    pdf.set_font("Helvetica", "", 10)
    for text in ["FAKE BUILDERS LLC", "100 Sample Street", "Springfield, ST 00000"]:
        pdf.cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.cell(0, 5, "Business Checking   Account number: XXXXXX2290", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, f"Statement period: {start:%m/%d/%Y} to {end:%m/%d/%Y}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    deposits = sum((a for _, _, a in lines if a > 0), Decimal("0"))
    withdrawals = sum((a for _, _, a in lines if a < 0), Decimal("0"))
    ending = beginning + deposits + withdrawals

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Account summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    summary = [
        ("Beginning balance", beginning),
        (f"Deposits and other credits ({sum(1 for l in lines if l[2] > 0)})", deposits),
        (f"Withdrawals and other debits ({sum(1 for l in lines if l[2] < 0)})", withdrawals),
        ("Ending balance", ending),
    ]
    for label, value in summary:
        pdf.cell(110, 6, label)
        pdf.cell(40, 6, money(value), align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 9)
    widths = (20, 95, 35, 35)
    for head, w in zip(("Date", "Description", "Amount", "Balance"), widths):
        pdf.cell(w, 6, head, border="B", align="L" if w in (20, 95) else "R")
    pdf.ln()
    pdf.set_font("Helvetica", "", 9)
    balance = beginning
    for d, desc, amount in lines:
        balance += amount
        pdf.cell(widths[0], 5, f"{d:%m/%d}")
        pdf.cell(widths[1], 5, desc)
        pdf.cell(widths[2], 5, money(amount), align="R")
        pdf.cell(widths[3], 5, money(balance), align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(6)
    pdf.set_font("Helvetica", "I", 8)
    pdf.multi_cell(0, 4, "Questions about your statement? Report any error or unknown "
                         "transaction to the bank within 60 days.")

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / f"fake_builders_statement_2026-{month:02d}.pdf"
    pdf.output(str(out))
    return ending, out


def main():
    by_month = read_lines()
    beginning = OPENING
    for month in sorted(by_month):
        beginning, out = make_statement(month, by_month[month], beginning)
        print(f"{out.name}: ending {money(beginning)}")


if __name__ == "__main__":
    main()
