# CURRICULUM.md — 12-Week Adaptive Plan (v1)

> This is the **starting** plan. The Dynamic Learning Assessor changes pace, order, and lesson content based on real results.
> Weeks are targets, not rules. Gates are rules. See `.claude/skills/learning-session/ASSESSOR.md`.

**Total:** ~240 hours · 20 h/week · Default split: 8 learn / 8 build / 4 clients + content + product

Every module gives three outputs:
- 🛠 **Build** — a working thing (portfolio piece)
- 💼 **Client asset** — something you can sell or show to a client
- 📣 **Content + product** — a post idea and a chapter for the PDF guide

---

## M0 — Setup (Week 1)

**Core skills:** TECH-01, TECH-02, TECH-03, AI-01, QBO-01

1. Install Git, VS Code, Python. Set up GitHub.
2. Put this repo on GitHub (**public** repo for portfolio; `data/practice/` only fake data).
3. Run Claude Code in this folder. Run the first `start session`.
4. Create the Claude.ai Project. Paste instructions. Upload knowledge files.
5. Open a QuickBooks Online developer sandbox.
6. First browser scan of Reddit + Facebook groups (`market-scan`).

- 🛠 Repo live, first session logged
- 💼 —
- 📣 Post: "Day 1: My AI finance ops setup as a Filipino freelancer"

---

## M1 — Accounting refresh + QuickBooks Online core (Weeks 2–3)

**Core skills:** ACC-01 to ACC-05, QBO-02 to QBO-05

1. Double-entry refresh with real small-business examples
2. Bank reconciliation (by hand, then in QBO)
3. Accrual vs cash, cut-off
4. AP and AR cycle
5. Month-end close checklist
6. QBO: chart of accounts, bank feeds, bank rules, reconcile, reports

- 🛠 **Clean up a messy fake company** in the QBO sandbox (8 months behind)
- 💼 QBO cleanup checklist + fixed-price "catch-up" offer draft
- 📣 Chapter: "Catch-up bookkeeping, step by step"

---

## M2 — Excel for finance data (Week 4)

**Core skills:** XL-01 to XL-04

1. Clean messy exports (TRIM, text vs number, dates, Power Query basics)
2. XLOOKUP and matching
3. PivotTables
4. Bank vs ledger matching in Excel

- 🛠 **Bank-vs-ledger matcher** workbook (flags unmatched items)
- 💼 Reusable reconciliation template
- 📣 Chapter: "Excel skills that clients actually pay for"

---

## M3 — Automation core: Make, then n8n (Weeks 5–6)

**Core skills:** AUTO-01 to AUTO-06

1. Triggers, actions, data mapping (Make only, week 5 first half)
2. Filters, routers, iterators
3. Error handling and retries
4. Connect to QBO sandbox
5. Human approval step (Slack/email/sheet)
6. **Interleave:** rebuild the same workflow in n8n. Compare.

- 🛠 **Invoice inbox → extract → approve → QBO bill** (sandbox)
- 💼 Demo video + one-page "how it works"
- 📣 Post: "Make vs n8n — same workflow, honest comparison"

---

## M4 — AI inside finance workflows (Weeks 6–7)

**Core skills:** AI-02 to AI-06

1. Structured extraction (JSON) from invoices and receipts
2. Validation checks (line items = total, duplicates, date sanity)
3. Prompt chaining with a check after each step
4. Client data safety (PII, masking, tool data policies)
5. Testing AI output against a known-correct test set

- 🛠 **Expense / invoice policy checker** (claims vs a written policy, with an audit log)
- 💼 Case study with error rate numbers
- 📣 Chapter: "Why AI makes mistakes with numbers — and how to catch them"

---

## Week 8 — Break + client test

**Core skills:** CLIENT-01 to CLIENT-03

1. Review weak skills (Assessor picks)
2. Write the offer (one page)
3. Region test: 10 US leads + 10 AU leads, same offer
4. First discovery calls

- 💼 Offer page + outreach message
- 📣 Post: "My first 20 outreach messages — what happened"

---

## M5 — Agents + month-end close helper (Weeks 9–10)

**Core skills:** AI-07, AI-08, XERO-01

1. Agent loop with human checkpoints (Claude Code)
2. Cost per task: is it worth it?
3. Xero basics (for the AU lane, only if the region test supports it)

- 🛠 **Month-end close helper**: pulls data, reconciles, drafts the close notes, waits for approval
- 💼 Case study + pilot offer for a bookkeeping firm
- 📣 Chapter: "AI agents for small-firm month-end close"

---

## M6 — Package (Weeks 11–12)

**Core skills:** AI-09, CLIENT-04

1. Governance checklist for small clients (approval, logs, data safety)
2. Portfolio: 3 case studies in `artifacts/`
3. PDF guide v1 from the chapters
4. Pricing and proposal template

- 🛠 Public portfolio
- 💼 Proposal template + price list
- 📣 Launch PDF guide v1

---

## Change log
- v1 — 2026-10-03 — created
