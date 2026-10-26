# M0-L3 — QuickBooks Online developer sandbox (v1)

**Skills:** QBO-01 (main), TECH-03
**Default level:** New (mastery 0)
**Time:** ~60 min (can split over 2 short sessions)
**Practice data:** the sandbox's own sample company (fake data from Intuit)

## Why this matters for clients
The market scan shows QuickBooks in **50%** of bookkeeper posts, and US clients are the main lane. You need a safe place to practise cleanup, bank rules, and automation **without real client books**. The free developer sandbox is that place. It is also the company you will connect to Make and n8n in M3.

## Words to know
| Word | Plain meaning |
|---|---|
| Intuit Developer | Intuit's website for people who build apps on QuickBooks |
| Sandbox company | A free, fake QuickBooks Online company for testing. Not a real business |
| Sample data | Fake customers, bills, and bank lines that come with the sandbox |
| Chart of accounts | The list of all accounts (bank, income, expenses, etc.) |
| Balance Sheet | Report: what the company owns, owes, and the owner's share, on one date |
| Credentials | Your username and password. **Never** put these in the repo |

## Note on the UI
Intuit changes its developer site often. The names below (Dashboard, Sandbox, "Add a sandbox") are correct as far as I know in 2026, but might move. If you can't find a button, tell me what you see. Official help: https://developer.intuit.com (search "sandbox").

## Safety rules for this lesson
1. Do not save your password or email in any repo file.
2. Before you save a screenshot to the repo, crop out your email and name.
3. Only the sandbox company. Never connect a real company.

## Steps

### Step 1 — Make an Intuit Developer account (~10 min)
1. Go to https://developer.intuit.com.
2. Sign up (or sign in if you have an Intuit account).
3. Open your **Dashboard**.

**Check:** tell me what you see on the Dashboard (menu names are enough). No screenshot needed yet.

### Step 2 — Create a US sandbox company (~10 min)
1. Find the **Sandbox** area (often under your account menu or the Dashboard).
2. Intuit may have made a **default US sandbox** for you already. If yes, use it. If not, add one: choose **United States** (QuickBooks Online Plus or Advanced if asked).
3. Open the sandbox company (QuickBooks opens in a new tab).

**Check:** tell me the **company name** shown at the top, and the **expiry date** if the Sandbox page shows one.

### Step 3 — Find the chart of accounts (~10 min)
1. In the sandbox company, find the **Chart of accounts** (hint: it is under the accounting menu, or search for it).
2. Find the bank account(s).

**Check:** tell me the name of one bank account and its balance in QuickBooks.

### Step 4 — Run the Balance Sheet (~10 min)
1. Open **Reports**. Find **Balance Sheet**.
2. Run it for "This year to date" (or today).

**Check:** tell me **Total Assets** and **Total Liabilities and Equity**. They must be equal. Why must they be equal? Answer in one sentence.

### Step 5 — Your sandbox card (~10 min)
In VS Code, create `learning/cards/qbo-sandbox.md` with:
1. A `#` heading: `# QBO sandbox card`
2. These items as a list (`- `):
   - where to open it: the website link **and** the click path to open the company
   - the company name
   - the expiry date (or "not shown")
   - one safety rule from this lesson, in your words
3. **No** email or password.

**Self-check before "done":** read each line of this step again and tick it.

**Check:** I read the file.

### Step 6 — Explain it back (~5 min)
In 3 sentences, your own words:
1. What is a sandbox company, and why do we use it instead of a real one?
2. Why must the Balance Sheet balance?
3. What will we connect to this sandbox later?

**Check:** all 3 points correct, plain English.

## Harder variant (for fast progress)
- Open the **Profit and Loss** report for this year. Name the biggest expense account.
- Find one **bank transaction** in the bank feed that is not yet categorised (if any).

## Repair micro-lessons
- vocab: match the 6 words above to their meanings, then use 2 in a sentence.
- concept: Balance Sheet in one line: *owns = owes + owner's share*. Do 2 tiny fake examples with numbers.
- tool: find the menu together, step by step, with screenshots.
- tech: if the sandbox won't open, try a new browser window (private mode), or sign out and in again.

## Revision log
- v1 — 2026-10-18 — created
- v1.1 — 2026-10-21 — Step 2: Intuit makes a default US sandbox; use it. Step 5: card must include the click path to open the company (Rule B extra variant after `H` on Step 2).
