"""Build the M1-L1 answer key from the fake bank CSV.

Run:  python -I data/practice/answer_keys/build_m1l1_key.py
Writes m1l1_answer_key.md next to this script. Fake data only.
"""
import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
CSV_PATH = HERE.parent / "fake-builders" / "01_from_client" / "fake_builders_bank_2026-08_to_10.csv"
OUT_PATH = HERE / "m1l1_answer_key.md"
OPENING = 8500.00
STATEMENT_ENDS = {"08": 9271.76, "09": 10070.69, "10": 7109.12}  # from the lesson
NEC_THRESHOLD = 2000.00  # payments made in 2026+; confirm on IRS.gov

# (description contains, account, payee, report group)
RULES = [
    ("DEPOSIT HILL", "Sales / Income", "Hill", "Income"),
    ("DEPOSIT ORTIZ", "Sales / Income", "Ortiz", "Income"),
    ("BUILDMART", "Job Materials", "BuildMart Supply", "Job cost"),
    ("ACE DRYWALL", "Subcontractors", "Ace Drywall LLC", "Job cost"),
    ("RIVERA ELECTRIC", "Subcontractors", "Rivera Electric", "Job cost"),
    ("BOLT PLUMBING", "Subcontractors", "Bolt Plumbing Co", "Job cost"),
    ("TOOLRENT", "Equipment Rental", "ToolRent", "Job cost"),
    ("QUIKFUEL", "Fuel", "QuikFuel", "Overhead"),
    ("TCELL", "Phone", "TCell Wireless", "Overhead"),
    ("SAFESHIELD", "Insurance", "SafeShield Insurance", "Overhead"),
    ("CLOUDJOB", "Software", "CloudJob", "Overhead"),
    ("SERVICE FEE", "Bank Fees", "(bank)", "Overhead"),
    ("LUNCHBOX", "Meals", "Lunchbox Deli", "Overhead"),
    ("OWNER DRAW", "Owner Draw (equity)", "Owner", "Not P&L"),
    ("SAVINGS 4471", "Transfer to Business Savings", "-", "Not P&L"),
]

# Owner's project list from the lesson (date + payee keyword)
PROJECTS = {
    "Hill Kitchen": ["DEPOSIT HILL", "08/03 BUILDMART", "08/10 BUILDMART", "08/29 BUILDMART",
                     "10/01 BUILDMART", "08/06 ACE", "09/05 ACE", "08/20 RIVERA", "08/25 TOOLRENT"],
    "Ortiz Bath": ["DEPOSIT ORTIZ", "09/09 BUILDMART", "09/17 BUILDMART", "10/30 BUILDMART",
                   "10/20 ACE", "09/22 RIVERA", "09/12 BOLT", "10/06 BOLT", "10/22 TOOLRENT"],
}


def classify(desc):
    for key, account, payee, group in RULES:
        if key in desc:
            return account, payee, group
    raise ValueError(f"No rule for: {desc}")


def project_for(date, desc):
    for project, keys in PROJECTS.items():
        for k in keys:
            if " " in k and k[2] == "/":
                d, word = k.split(" ", 1)
                if date.startswith(d) and word in desc:
                    return project
            elif k in desc:
                return project
    return ""


rows = list(csv.DictReader(CSV_PATH.open()))
lines, balance, month_end = [], OPENING, {}
seen = defaultdict(int)
for r in rows:
    amt = float(r["Amount"])
    balance += amt
    month_end[r["Date"][:2]] = round(balance, 2)
    account, payee, group = classify(r["Description"])
    seen[(r["Date"], r["Description"], amt)] += 1
    lines.append((r["Date"], r["Description"], amt, account, payee,
                  project_for(r["Date"], r["Description"]), group))

pnl, proj, vendor_1099 = defaultdict(float), defaultdict(lambda: defaultdict(float)), defaultdict(float)
for date, desc, amt, account, payee, project, group in lines:
    if group != "Not P&L":
        pnl[(group, account)] += amt
    if project:
        proj[project]["Income" if group == "Income" else "Costs"] += amt
    if account == "Subcontractors":
        vendor_1099[payee] += -amt

out = ["# M1-L1 answer key (generated — do not edit by hand)", "",
       "> Made by `build_m1l1_key.py` from the fake CSV. **Ken: don't open this before the step check.**", "",
       f"Lines: {len(lines)}", "", "## Month-end balances (Step 7)", "",
       "| Month | From CSV | Statement | Match |", "|---|---|---|---|"]
for m, stmt in STATEMENT_ENDS.items():
    out.append(f"| {m} | {month_end[m]:,.2f} | {stmt:,.2f} | {'yes' if month_end[m] == stmt else 'NO'} |")

out += ["", "## Every line (Step 6)", "", "| Date | Description | Amount | Account | Payee | Project |",
        "|---|---|---|---|---|---|"]
out += [f"| {d} | {ds} | {a:,.2f} | {ac} | {p} | {pr} |" for d, ds, a, ac, p, pr, _ in lines]

out += ["", "## Traps (Step 6)", ""]
dups = [k for k, n in seen.items() if n > 1]
for d, ds, a in dups:
    out.append(f"- **Duplicate charge** {d} {ds} {a:,.2f}: both lines are on the bank statement "
               "(the balances only match with both). Keep both. Ask the owner if BuildMart charged twice "
               "and a refund is coming. Excluding one breaks the September reconcile by that amount.")
out += ["- **Return** 09/17 BUILDMART SUPPLY RETURN +184.50: money in, but **not income**. "
        "Job Materials (reduces cost), project Ortiz Bath.",
        "- **Owner draw**: equity, not an expense. No project.",
        "- **Transfer to savings 4471**: transfer to Business Savings. Not income, not expense.",
        "- **BuildMart rule**: lines go to 2 projects, so the rule should **suggest**, not auto-add. "
        "If the rule is not limited to Money out, it also catches the return line.",
        "", "## Project profitability (Step 6 check)", "",
        "| Project | Income | Costs | Profit |", "|---|---|---|---|"]
for p, v in proj.items():
    out.append(f"| {p} | {v['Income']:,.2f} | {-v['Costs']:,.2f} | {v['Income'] + v['Costs']:,.2f} |")

income = sum(v for (g, _), v in pnl.items() if g == "Income")
expenses = -sum(v for (g, _), v in pnl.items() if g != "Income")
out += ["", "## Profit and Loss, cash basis, Aug 1 – Oct 31 2026 (Step 8)", "",
        "| Group | Account | Amount |", "|---|---|---|"]
out += [f"| {g} | {a} | {v:,.2f} |" for (g, a), v in sorted(pnl.items())]
out += [f"| | **Total income** | {income:,.2f} |", f"| | **Total expenses** | {expenses:,.2f} |",
        f"| | **Net income** | {income - expenses:,.2f} |", "",
        "## Balance Sheet checks, 10/31/2026 (Step 8)", "",
        f"- Business Checking: {month_end['10']:,.2f}",
        f"- Business Savings: {sum(-a for _, d, a, *_ in lines if 'SAVINGS 4471' in d):,.2f} "
        "(transfers only; no savings statement in the case)",
        f"- Owner Draw: {sum(a for _, d, a, *_ in lines if 'OWNER DRAW' in d):,.2f}", "",
        f"## 1099-NEC list (Step 8) — threshold ${NEC_THRESHOLD:,.0f} (2026 payments)", "",
        "| Vendor | Paid Aug–Oct | Over threshold? |", "|---|---|---|"]
out += [f"| {v} | {t:,.2f} | {'yes' if t >= NEC_THRESHOLD else 'no'} |" for v, t in sorted(vendor_1099.items())]
out += ["", "Note: the case covers Aug–Oct only. The real test is the **full calendar year**.", "",
        "## Sources", "",
        "- 1099-NEC $2,000 threshold for payments made after 2025: secondary sources "
        "(1800accountant.com, anchin.com). **Confirm on IRS.gov** (Form 1099-NEC instructions).",
        "- Owner draws are equity, transfers are not income/expense, returns reduce cost: "
        "OpenStax *Principles of Accounting, Vol. 1* (free, openstax.org).",
        "- QBO bank rules, Projects, reconcile: Intuit QuickBooks Help (quickbooks.intuit.com/learn-support)."]

OUT_PATH.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"Wrote {OUT_PATH} ({len(lines)} lines)")
