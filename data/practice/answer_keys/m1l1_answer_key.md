# M1-L1 answer key (generated — do not edit by hand)

> Made by `build_m1l1_key.py` from the fake CSV. **Ken: don't open this before the step check.**

Lines: 44

## Month-end balances (Step 7)

| Month | From CSV | Statement | Match |
|---|---|---|---|
| 08 | 9,271.76 | 9,271.76 | yes |
| 09 | 10,070.69 | 10,070.69 | yes |
| 10 | 7,109.12 | 7,109.12 | yes |

## Every line (Step 6)

| Date | Description | Amount | Account | Payee | Project |
|---|---|---|---|---|---|
| 08/01/2026 | DEPOSIT HILL KITCHEN REMODEL DEPOSIT | 6,000.00 | Sales / Income | Hill | Hill Kitchen |
| 08/03/2026 | BUILDMART SUPPLY #112 | -1,842.37 | Job Materials | BuildMart Supply | Hill Kitchen |
| 08/04/2026 | QUIKFUEL STATION 44 | -86.20 | Fuel | QuikFuel |  |
| 08/06/2026 | ZELLE TO ACE DRYWALL LLC | -1,500.00 | Subcontractors | Ace Drywall LLC | Hill Kitchen |
| 08/08/2026 | TCELL WIRELESS AUTOPAY | -74.99 | Phone | TCell Wireless |  |
| 08/10/2026 | BUILDMART SUPPLY #112 | -412.08 | Job Materials | BuildMart Supply | Hill Kitchen |
| 08/12/2026 | ONLINE TRANSFER TO SAVINGS 4471 | -1,000.00 | Transfer to Business Savings | - |  |
| 08/15/2026 | SAFESHIELD INSURANCE PREMIUM | -318.00 | Insurance | SafeShield Insurance |  |
| 08/15/2026 | OWNER DRAW TRANSFER | -1,200.00 | Owner Draw (equity) | Owner |  |
| 08/18/2026 | QUIKFUEL STATION 44 | -91.45 | Fuel | QuikFuel |  |
| 08/20/2026 | CHECK 1031 RIVERA ELECTRIC | -950.00 | Subcontractors | Rivera Electric | Hill Kitchen |
| 08/22/2026 | DEPOSIT ORTIZ BATH REMODEL DEPOSIT | 3,500.00 | Sales / Income | Ortiz | Ortiz Bath |
| 08/25/2026 | TOOLRENT EQUIPMENT RENTAL | -265.00 | Equipment Rental | ToolRent | Hill Kitchen |
| 08/28/2026 | MONTHLY SERVICE FEE | -15.00 | Bank Fees | (bank) |  |
| 08/29/2026 | BUILDMART SUPPLY #087 | -973.15 | Job Materials | BuildMart Supply | Hill Kitchen |
| 09/02/2026 | DEPOSIT HILL KITCHEN PROGRESS PAYMENT | 5,000.00 | Sales / Income | Hill | Hill Kitchen |
| 09/03/2026 | QUIKFUEL STATION 44 | -79.60 | Fuel | QuikFuel |  |
| 09/05/2026 | ZELLE TO ACE DRYWALL LLC | -1,750.00 | Subcontractors | Ace Drywall LLC | Hill Kitchen |
| 09/08/2026 | TCELL WIRELESS AUTOPAY | -74.99 | Phone | TCell Wireless |  |
| 09/09/2026 | BUILDMART SUPPLY #087 | -1,205.44 | Job Materials | BuildMart Supply | Ortiz Bath |
| 09/09/2026 | BUILDMART SUPPLY #087 | -1,205.44 | Job Materials | BuildMart Supply | Ortiz Bath |
| 09/12/2026 | ZELLE TO BOLT PLUMBING CO | -1,300.00 | Subcontractors | Bolt Plumbing Co | Ortiz Bath |
| 09/15/2026 | SAFESHIELD INSURANCE PREMIUM | -318.00 | Insurance | SafeShield Insurance |  |
| 09/15/2026 | OWNER DRAW TRANSFER | -1,200.00 | Owner Draw (equity) | Owner |  |
| 09/17/2026 | BUILDMART SUPPLY RETURN | 184.50 | Job Materials | BuildMart Supply | Ortiz Bath |
| 09/19/2026 | QUIKFUEL STATION 44 | -88.10 | Fuel | QuikFuel |  |
| 09/22/2026 | CHECK 1032 RIVERA ELECTRIC | -1,100.00 | Subcontractors | Rivera Electric | Ortiz Bath |
| 09/24/2026 | DEPOSIT ORTIZ BATH PROGRESS PAYMENT | 4,000.00 | Sales / Income | Ortiz | Ortiz Bath |
| 09/26/2026 | CLOUDJOB SOFTWARE SUBSCRIPTION | -49.00 | Software | CloudJob |  |
| 09/28/2026 | MONTHLY SERVICE FEE | -15.00 | Bank Fees | (bank) |  |
| 10/01/2026 | BUILDMART SUPPLY #112 | -688.92 | Job Materials | BuildMart Supply | Hill Kitchen |
| 10/03/2026 | QUIKFUEL STATION 44 | -94.30 | Fuel | QuikFuel |  |
| 10/06/2026 | ZELLE TO BOLT PLUMBING CO | -1,450.00 | Subcontractors | Bolt Plumbing Co | Ortiz Bath |
| 10/08/2026 | TCELL WIRELESS AUTOPAY | -74.99 | Phone | TCell Wireless |  |
| 10/10/2026 | DEPOSIT HILL KITCHEN FINAL PAYMENT | 4,500.00 | Sales / Income | Hill | Hill Kitchen |
| 10/13/2026 | ONLINE TRANSFER TO SAVINGS 4471 | -1,500.00 | Transfer to Business Savings | - |  |
| 10/15/2026 | SAFESHIELD INSURANCE PREMIUM | -318.00 | Insurance | SafeShield Insurance |  |
| 10/15/2026 | OWNER DRAW TRANSFER | -1,500.00 | Owner Draw (equity) | Owner |  |
| 10/17/2026 | LUNCHBOX DELI | -38.75 | Meals | Lunchbox Deli |  |
| 10/20/2026 | ZELLE TO ACE DRYWALL LLC | -900.00 | Subcontractors | Ace Drywall LLC | Ortiz Bath |
| 10/22/2026 | TOOLRENT EQUIPMENT RENTAL | -310.00 | Equipment Rental | ToolRent | Ortiz Bath |
| 10/26/2026 | CLOUDJOB SOFTWARE SUBSCRIPTION | -49.00 | Software | CloudJob |  |
| 10/28/2026 | MONTHLY SERVICE FEE | -15.00 | Bank Fees | (bank) |  |
| 10/30/2026 | BUILDMART SUPPLY #087 | -522.61 | Job Materials | BuildMart Supply | Ortiz Bath |

## Traps (Step 6)

- **Duplicate charge** 09/09/2026 BUILDMART SUPPLY #087 -1,205.44: both lines are on the bank statement (the balances only match with both). Keep both. Ask the owner if BuildMart charged twice and a refund is coming. Excluding one breaks the September reconcile by that amount.
- **Return** 09/17 BUILDMART SUPPLY RETURN +184.50: money in, but **not income**. Job Materials (reduces cost), project Ortiz Bath.
- **Owner draw**: equity, not an expense. No project.
- **Transfer to savings 4471**: transfer to Business Savings. Not income, not expense.
- **BuildMart rule**: lines go to 2 projects, so the rule should **suggest**, not auto-add. If the rule is not limited to Money out, it also catches the return line.

## Project profitability (Step 6 check)

| Project | Income | Costs | Profit |
|---|---|---|---|
| Hill Kitchen | 15,500.00 | 8,381.52 | 7,118.48 |
| Ortiz Bath | 7,500.00 | 7,808.99 | -308.99 |

## Profit and Loss, cash basis, Aug 1 – Oct 31 2026 (Step 8)

| Group | Account | Amount |
|---|---|---|
| Income | Sales / Income | 23,000.00 |
| Job cost | Equipment Rental | -575.00 |
| Job cost | Job Materials | -6,665.51 |
| Job cost | Subcontractors | -8,950.00 |
| Overhead | Bank Fees | -45.00 |
| Overhead | Fuel | -439.65 |
| Overhead | Insurance | -954.00 |
| Overhead | Meals | -38.75 |
| Overhead | Phone | -224.97 |
| Overhead | Software | -98.00 |
| | **Total income** | 23,000.00 |
| | **Total expenses** | 17,990.88 |
| | **Net income** | 5,009.12 |

## Balance Sheet checks, 10/31/2026 (Step 8)

- Business Checking: 7,109.12
- Business Savings: 2,500.00 (transfers only; no savings statement in the case)
- Owner Draw: -3,900.00

## 1099-NEC list (Step 8) — threshold $2,000 (2026 payments)

| Vendor | Paid Aug–Oct | Over threshold? |
|---|---|---|
| Ace Drywall LLC | 4,150.00 | yes |
| Bolt Plumbing Co | 2,750.00 | yes |
| Rivera Electric | 2,050.00 | yes |

Note: the case covers Aug–Oct only. The real test is the **full calendar year**.

## Sources

- 1099-NEC $2,000 threshold for payments made after 2025: secondary sources (1800accountant.com, anchin.com). **Confirm on IRS.gov** (Form 1099-NEC instructions).
- Owner draws are equity, transfers are not income/expense, returns reduce cost: OpenStax *Principles of Accounting, Vol. 1* (free, openstax.org).
- QBO bank rules, Projects, reconcile: Intuit QuickBooks Help (quickbooks.intuit.com/learn-support).
