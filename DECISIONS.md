# DECISIONS.md — Finance Ops Build

> The single record of what we decided and why.
> Every AI session reads this file first. Add new decisions at the bottom of each section, with a date.
> Never delete a decision. If it changes, mark the old one `SUPERSEDED` and add the new one.

Last updated: 2026-10-03

---

## 1. Goal

- **2026-10-03** — Main goal: get **freelance clients** for AI-powered finance ops work. Not a job, not enterprise clients.
- **2026-10-03** — Second goal: turn what I learn and build into a **product** for Filipino freelancers. Start as a **PDF learning guide**. Move to a **mini-LMS** only after the PDF sells.
- **2026-10-03** — Third goal: turn progress into **content** for aspiring and current Filipino freelancers.
- **2026-10-03** — Rule: **build once, use three times.** Every module gives (1) a skill, (2) a client asset, (3) a product lesson + content.

## 2. Scope

- **2026-10-03** — This plan is **separate** from the Client-to-Close Assistant plan.
- **2026-10-03** — This plan has **nothing** to do with the gaming audit reconciliation work. Never mix them. Never use its data.
- **2026-10-03** — No real client data in this repo, the portfolio, or the product. Use fake or masked data only.
- **2026-10-03** — Ken's own learning data (`data/session_log.csv`, `data/skill_map.csv`, `learning/LEARNER_STATE.md`) stays **public** in this repo, as build-in-public proof. It contains no PII. Session notes are written in a neutral, professional way.

## 3. Time

- **2026-10-03** — At least **20 hours per week**.
- **2026-10-03** — Default weekly split: 8h learn · 8h build · 4h clients + content + product. The Learning Assessor may change this split (see `learning/LEARNER_STATE.md`).
- **2026-10-03** — First cycle: **12 weeks** (~240 hours).

## 4. Clients and regions

- **2026-10-03** — Clients: small and mid-size businesses and small bookkeeping firms. Not enterprise.
- **2026-10-03** — Start region: **US** (most volume, QuickBooks Online, fixed-price cleanup gigs, no local license needed for automation work).
- **2026-10-03** — Second region: **Australia / NZ**, from month 2–3 (small time-zone gap, "AI-native" bookkeeping firms hiring in PH, but many posts need AU experience).
- **2026-10-03** — Later: Canada, UK, then Europe (except Denmark) and Middle East. Revisit after 6 months.
- **2026-10-03** — Validate the region choice with a test: same offer to 10 US and 10 AU leads in weeks 6–8. More replies wins.
- **2026-10-03** — Client ladder: (1) US SMBs on QuickBooks Online with messy books — niche **construction** or **e-commerce**; (2) small bookkeeping firms going "AI-native"; (3) other regions.
- **2026-10-03** — Positioning: sell **automation + clean books**, not cheap hourly bookkeeping. Plain bookkeeping pay in the market is $2.50–$15/hr.

## 5. Tools

- **2026-10-03** — Accounting: **QuickBooks Online** first (free developer sandbox). **Xero** second (free demo company) for AU.
- **2026-10-03** — Always: **Excel**.
- **2026-10-03** — Automation: **interleave Make and n8n**. Weeks 1–2 Make only (learn the core ideas once). Week 3+ build the same workflow in both. **Zapier** only if the market scan justifies it.
- **2026-10-03** — Depth rule: a tool gets real study time if it appears in **20% or more** of relevant posts in the monthly scan. Below that: basics only.
- **2026-10-03** — AI layer: Claude (Claude.ai Project for thinking/research/writing) + Claude Code (for building).
- **2026-10-03** — Python: light use only.

## 6. Learning method

- **2026-10-03** — **Dropped** the pre-learning skill assessment (quiz + self-rating). SUPERSEDED by the Dynamic Learning Assessor.
- **2026-10-03** — Use a **Dynamic Learning Assessor**: lessons adapt, get revised, and get updated based on how well I complete them. Rules live in `.claude/skills/learning-session/ASSESSOR.md`. State lives in `learning/LEARNER_STATE.md` and `data/skill_map.csv`.
- **2026-10-03** — Background: accounting graduate (2005), never practised. Treat accounting as "known once, needs refresh", not "new".
- **2026-10-03** — Progressive disclosure: one step at a time. Wait for confirmation.
- **2026-10-03** — All instructions in **simple, plain English**. Short sentences. Numbered steps.

## 7. AI stack and setup

- **2026-10-03** — **Files are state.** Nothing important lives only in chat history.
- **2026-10-03** — One chat = one job. Start a fresh chat for each phase or task.
- **2026-10-03** — Two workspaces, one source of truth:
  - Claude.ai **Project** "Finance Ops Build" — planning, research, scans, writing.
  - **Claude Code** + this repo — building, logs, portfolio.
  - The **repo files** are the source of truth. Copy changed files into the Project knowledge when they change.
- **2026-10-03** — Project memory kept **separate** from my other work.
- **2026-10-03** — Start with **3 custom skills** only: `learning-session` (with the Assessor), `market-scan`, `build-to-content`. Add more only when a task repeats 3+ times.
- **2026-10-03** — Not yet: multi-agent setups, custom MCP servers.
- **2026-10-03** — Logged-in sites (Reddit, Facebook groups): use the built-in browser with my sign-in. Read at human pace. No mass scraping.

## 8. Market scan

- **2026-10-03** — Monthly scan, about 2 hours. Sources: onlinejobs.ph, Upwork, JobStreet PH, r/quickbooksonline, 3 Filipino freelancer Facebook groups.
- **2026-10-03** — Output goes to `data/market_signals.csv` and `docs/market-scan/YYYY-MM-DD_scan.md`.
- **2026-10-03** — First scan done: see `docs/market-scan/2026-10-03_scan.md`.

## 9. Product and content

- **2026-10-03** — Audience: aspiring and current Filipino freelancers (bookkeepers, VAs).
- **2026-10-03** — Content angle: "How to become an AI-native bookkeeper."
- **2026-10-03** — Use the JHU "AI and Agentic AI in Finance" brochure as **inspiration only**. Do not copy its text or curriculum. Notes in `docs/JHU_NOTES.md`.

## 10. Open questions

- [ ] Which niche first: construction or e-commerce? (Decide after the first browser scan of Reddit + Facebook.)
- [ ] Price for the PDF guide. (Decide in week 10–11.)
- [ ] Main automation tool after week 4: Make or n8n? (Decide from scan data.)
