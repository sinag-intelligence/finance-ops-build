# M1-L1 — Fake Builders LLC: catch-up in QBO (v1.1)

**Skills:** QBO-02, QBO-03, QBO-04, QBO-05, ACC-01, ACC-02 (+ TECH-03 for files)
**Default level:** Guided (mastery 1) for accounting, New for QBO-02 to QBO-05
**Time:** ~4–5 hours, split over several short sessions
**Practice data:** fake — `data/practice/fake_builders_bank_2026-08_to_10.csv` (44 bank lines, Aug–Oct 2026, opening balance $8,500.00)

## Why this matters for clients
Offer 1 is "Tax-ready books before Jan 31" for US contractors (DECISIONS §4). A real client will be 3 months behind, with a pile of bank lines that nobody has categorized. This lesson is that exact job on fake data. When it is done, it becomes your first portfolio case study and your proof for Upwork.

## The fake client story
- **Fake Builders LLC** — a small US remodeling contractor. One owner. No employees. Pays subcontractors.
- Books are **3 months behind** (Aug–Oct 2026). Only the bank account is in QBO.
- Two jobs: **Hill Kitchen** (remodel) and **Ortiz Bath** (remodel).
- Three subcontractors: **Ace Drywall LLC**, **Rivera Electric**, **Bolt Plumbing Co**.
- The owner wants: clean books, profit per job, and a 1099 list for the CPA.

## Words to know
| Word | Plain meaning |
|---|---|
| Catch-up | Bringing books that are months behind up to date |
| Categorize | Telling QBO which account a bank line belongs to (e.g. Materials) |
| Bank rule | A saved instruction: "lines that say X always go to account Y" |
| Job costing | Tracking income and costs **per job**, to see profit per job. In QBO: **Projects** |
| Subcontractor | A person or company the contractor pays to do part of a job. Not an employee |
| 1099 / 1099-NEC | US tax form for paying non-employees $600+ in a year. Ken makes the **list**; the CPA files it |
| Owner draw | Money the owner takes out for personal use. **Not** an expense |
| Transfer | Money moved between the owner's own accounts. **Not** income or expense |
| Reconcile | Checking QBO against the bank statement, so both show the same ending balance |

## Bank statement ending balances (for reconciling)
| Month end | Ending balance |
|---|---|
| 2026-07-31 (opening) | $8,500.00 |
| 2026-08-31 | $9,271.76 |
| 2026-09-30 | $10,070.69 |
| 2026-10-31 | $7,109.12 |

## Note on the UI
Intuit changes QBO menus often. The click paths here are correct as far as I know in 2026, but may move. If you can't find a button, tell me what you see.

## Steps

### Step 1 — A clean company for Fake Builders (~15 min)
Your current sandbox (Sandbox Company US 7f9a) is full of Intuit sample data. A catch-up case study needs a cleaner start.
1. Open the Intuit Developer **Sandboxes** page (your card has the path).
2. Find out: can you **add** a second US sandbox company? Add one if you can.
3. Open the new company. Look at **Chart of accounts** and **Banking**.

**Check:** tell me (a) the new company name, (b) is there sample data in it (customers, bank lines)? yes/no.

### Step 2 — Company name + turn on Projects (~10 min)
1. Settings ⚙ → **Account and settings** → Company → change the name to **Fake Builders LLC**.
2. Settings ⚙ → Account and settings → **Advanced** → turn on **Projects** (if it is there).

**Check:** screenshot or tell me the name at the top left, and where you found Projects.

### Step 3 — Explain-back: the money map (~10 min)
No clicks. In your own words, for each line, say **income, expense, or neither**, and why:
1. DEPOSIT HILL KITCHEN REMODEL DEPOSIT
2. OWNER DRAW TRANSFER
3. ONLINE TRANSFER TO SAVINGS 4471
4. ZELLE TO ACE DRYWALL LLC

**Check:** I score your answers. Own words first, no AI polish.

### Step 4 — Bank account + upload the CSV (~20 min)
1. Add a bank account in the chart of accounts: **Business Checking**, opening balance **$8,500.00** as of **07/31/2026**.
2. Banking → **Upload transactions** (manual upload / "Upload from file").
3. Upload `data/practice/fake_builders_bank_2026-08_to_10.csv` into Business Checking. Map: Date, Description, one Amount column.

**Check:** tell me how many lines are in **For review**. (It should be 44.)

### Step 5 — Set up the lists: accounts, customers, projects, vendors (~30 min)
1. Accounts (Chart of accounts → New): Job Materials, Subcontractors, Equipment Rental (job costs); Fuel, Phone, Insurance, Software, Bank Fees, Meals (overhead); Owner Draw (equity); Business Savings (bank).
2. Customers: **Hill**, **Ortiz**. Projects: **Hill Kitchen** (customer Hill), **Ortiz Bath** (customer Ortiz).
3. Vendors: Ace Drywall LLC, Rivera Electric, Bolt Plumbing Co — tick **Track payments for 1099**. Also BuildMart Supply, ToolRent.

**Check:** list what you created. Tell me where the 1099 tick box was.

### Step 6 — 2 bank rules + categorize with projects (~45 min)
1. Make **2 bank rules**: BUILDMART SUPPLY → Job Materials; QUIKFUEL → Fuel.
2. Categorize all 44 lines. Add the **payee** and, for job costs and deposits, the **project**.
3. Watch for traps (there are at least 3).

**Project assignment list** (the owner told us this):
| Line | Project |
|---|---|
| All HILL deposits | Hill Kitchen |
| All ORTIZ deposits | Ortiz Bath |
| BuildMart 08/03, 08/10, 08/29, 10/01 | Hill Kitchen |
| BuildMart 09/09, 09/17 return, 10/30 | Ortiz Bath |
| Ace Drywall 08/06, 09/05 | Hill Kitchen |
| Ace Drywall 10/20 | Ortiz Bath |
| Rivera Electric 08/20 | Hill Kitchen |
| Rivera Electric 09/22 | Ortiz Bath |
| Bolt Plumbing 09/12, 10/06 | Ortiz Bath |
| ToolRent 08/25 | Hill Kitchen |
| ToolRent 10/22 | Ortiz Bath |
| Fuel, phone, insurance, software, bank fees, meals | no project (overhead) |
| Savings 4471 | treat as the **business** savings account (owner confirmed) |

**Check:** For review = 0. Tell me the traps you found and what you did with each. Then Project profitability: income and costs per project.

### Step 7 — Reconcile Aug, Sep, Oct (~40 min)
Reconcile Business Checking month by month with the table above.

**Check:** difference = $0.00 for each month. Tell me what you fixed if it wasn't 0.

### Step 8 — Reports for the owner and the CPA (~20 min)
1. Profit and Loss, Aug 1 – Oct 31, 2026.
2. Balance Sheet as of 10/31/2026.
3. 1099 contractor list (vendor 1099 report or Contractors page).

**Check:** net income, bank balance on the Balance Sheet, and the 3 subcontractors with totals.

### Step 9 — Case study draft (~30 min)
Write the before → after story in your own words. Then run `build-to-content`.

**Check:** "true today?" check — every claim is something you really did.

## Harder variant (for fast progress)
- Add a 4th month with a split deposit (one deposit paying two invoices).
- Find a missing receipt problem and write the client question you would send.

## Repair micro-lessons
- vocab: draw vs expense vs transfer — sort 6 cards into 3 piles.
- concept: why a duplicate charge breaks the reconcile — walk through the numbers.
- tool: find "For review" and "Categorize" with a guided screenshot tour.

## Revision log
- v1 — 2026-10-28 — created. Contractor niche (DECISIONS 2026-10-27).
- v1.1 — 2026-10-28 — Steps 5/6 swapped: lists first, then categorize once with projects (avoids editing ~20 lines twice). Added project assignment list. Step 2 = Projects only (Ken named the company in Step 1); Basic costing chosen. Case uses cash basis.
