# DECISIONS.md — Finance Ops Build

> The single record of what we decided and why.
> Every AI session reads this file first. Add new decisions at the bottom of each section, with a date.
> Never delete a decision. If it changes, mark the old one `SUPERSEDED` and add the new one.

Last updated: 2026-10-28

---

## 1. Goal

- **2026-10-03** — Main goal: get **freelance clients** for AI-powered finance ops work. Not a job, not enterprise clients.
- **2026-10-03** — Second goal: turn what I learn and build into a **product** for Filipino freelancers. Start as a **PDF learning guide**. Move to a **mini-LMS** only after the PDF sells.
- **2026-10-03** — Third goal: turn progress into **content** for aspiring and current Filipino freelancers.
- **2026-10-03** — Rule: **build once, use three times.** Every module gives (1) a skill, (2) a client asset, (3) a product lesson + content.
- **2026-10-27** — (Strategy grill) Goal for the next 8 weeks: **first paid client by 2026-12-22**. Success is earning, not finishing modules.
- **2026-10-27** — Identity: the go-to **AI/automation person, with an edge in bookkeeping and accounting**. Brand: **"Sinag — AI back office for contractors. Clean books. Less paperwork. Paid faster."**

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
- **2026-10-03** — `SUPERSEDED 2026-10-27` Second region: **Australia / NZ**, from month 2–3 (small time-zone gap, "AI-native" bookkeeping firms hiring in PH, but many posts need AU experience).
- **2026-10-03** — Later: Canada, UK, then Europe (except Denmark) and Middle East. Revisit after 6 months.
- **2026-10-03** — `SUPERSEDED 2026-10-27` Validate the region choice with a test: same offer to 10 US and 10 AU leads in weeks 6–8. More replies wins.
- **2026-10-03** — Client ladder: (1) US SMBs on QuickBooks Online with messy books — niche **construction** or **e-commerce**; (2) small bookkeeping firms going "AI-native"; (3) other regions.
- **2026-10-03** — Positioning: sell **automation + clean books**, not cheap hourly bookkeeping. Plain bookkeeping pay in the market is $2.50–$15/hr.
- **2026-10-27** — **US only, QBO only, until the first paid client.** Australia/NZ and the US vs AU test move to after the first client. Reason: one region, one tool, one time zone; half of AU posts need AU experience.
- **2026-10-27** — Niche: **US contractors and home-service businesses** (8-week test). Reason: trades showed up ~6 times in the 2026-10-27 scan, and they need both bookkeeping and automation.
- **2026-10-27** — Sell what the market buys; AI is *how* Ken works, not the product. Buyers must already know they have the problem.
  - **Offer 1:** "Tax-ready books before Jan 31" — QBO catch-up, job costing (projects), 1099 subcontractor payment list **for their CPA**. Ken does not file taxes.
  - **Offer 2 (upsell):** Jobber / Housecall Pro ↔ QBO sync cleanup + monthly bookkeeping + automations.
  - Later: small bookkeeping firms serving contractors, after 2–3 clients.
- **2026-10-27** — Fixed test prices: catch-up **from $200** (≤3 months behind, <150 transactions/month) · monthly **from $250/month** · one automation **from $300**. Raise after the first 2 clients.
- **2026-10-27** — Client channels: **Upwork** + **DMs to 20 small US bookkeeping/CPA firms or contractors** + **weekly lead signals** (§8). onlinejobs.ph is backup only.
- **2026-10-27** — Proof (2 weeks max, apply while building): (1) "Fake Builders LLC" QBO sandbox catch-up case study; (2) 2-minute demo of an AI-assisted sync-mess cleanup (fake data).
- **2026-10-27** — Sprint Oct 28 – Nov 10: 10 applications · 10 helpful replies · 20 DMs · 4 posts. If 0 replies by Nov 10, change the offer, not the plan.

## 5. Tools

- **2026-10-03** — Accounting: **QuickBooks Online** first (free developer sandbox). **Xero** second (free demo company) for AU.
- **2026-10-03** — Always: **Excel**.
- **2026-10-03** — Automation: **interleave Make and n8n**. Weeks 1–2 Make only (learn the core ideas once). Week 3+ build the same workflow in both. **Zapier** only if the market scan justifies it.
- **2026-10-03** — Depth rule: a tool gets real study time if it appears in **20% or more** of relevant posts in the monthly scan. Below that: basics only.
- **2026-10-03** — AI layer: Claude (Claude.ai Project for thinking/research/writing) + Claude Code (for building).
- **2026-10-03** — Python: light use only.
- **2026-10-27** — Scan 2026-10-27: QuickBooks 42%, Xero 31% (both pass the depth rule), but Xero stays basics-only until the first client (§4). Make + n8n stay in the plan, learned **only when Offer 2 needs them**. 0% of job posts mention automation tools.

## 6. Learning method

- **2026-10-03** — **Dropped** the pre-learning skill assessment (quiz + self-rating). SUPERSEDED by the Dynamic Learning Assessor.
- **2026-10-03** — Use a **Dynamic Learning Assessor**: lessons adapt, get revised, and get updated based on how well I complete them. Rules live in `.claude/skills/learning-session/ASSESSOR.md`. State lives in `learning/LEARNER_STATE.md` and `data/skill_map.csv`.
- **2026-10-03** — Background: accounting graduate (2005), never practised. Treat accounting as "known once, needs refresh", not "new".
- **2026-10-03** — Progressive disclosure: one step at a time. Wait for confirmation.
- **2026-10-03** — All instructions in **simple, plain English**. Short sentences. Numbered steps.
- **2026-10-17** — Session rhythm: **short sessions, often**. At least one session every **2 days**, even 30 min. Reason: a 12-day gap after session 1 caused most Git basics to be forgotten. Weekly target stays **20 hours**.
- **2026-10-27** — **Just-in-time learning.** The curriculum is a reference list, not a gate before selling. Learn a topic only when a real client task or sales asset needs it this week.
- **2026-10-27** — Hours check on **Sunday 2026-11-01**: if weekly hours have not improved, lower the target to a real minimum (proposed 8h/week).

## 7. AI stack and setup

- **2026-10-03** — **Files are state.** Nothing important lives only in chat history.
- **2026-10-03** — One chat = one job. Start a fresh chat for each phase or task.
- **2026-10-03** — `SUPERSEDED 2026-10-28` Two workspaces, one source of truth:
  - Claude.ai **Project** "Finance Ops Build" — planning, research, scans, writing.
  - **Claude Code** + this repo — building, logs, portfolio.
  - The **repo files** are the source of truth. Copy changed files into the Project knowledge when they change.
- **2026-10-03** — Project memory kept **separate** from my other work.
- **2026-10-03** — Start with **3 custom skills** only: `learning-session` (with the Assessor), `market-scan`, `build-to-content`. Add more only when a task repeats 3+ times.
- **2026-10-03** — Not yet: multi-agent setups, custom MCP servers.
- **2026-10-28** — **One home: Claude Code + this repo** for everything (learning, building, scans, lead signals, writing). Claude.ai is **optional**: phone or quick drafting only. No routine Project sync. If a Claude.ai chat makes something useful, paste it into a repo file. Reason: two workspaces were hard to track, and sync can't be automated (no tool reaches Claude.ai Project knowledge).
- **2026-10-03** — Logged-in sites (Reddit, Facebook groups): use the built-in browser with my sign-in. Read at human pace. No mass scraping.

## 8. Market scan

- **2026-10-03** — Monthly scan, about 2 hours. Sources: onlinejobs.ph, Upwork, JobStreet PH, r/quickbooksonline, 3 Filipino freelancer Facebook groups.
- **2026-10-03** — Output goes to `data/market_signals.csv` and `docs/market-scan/YYYY-MM-DD_scan.md`.
- **2026-10-03** — First scan done: see `docs/market-scan/2026-10-03_scan.md`.
- **2026-10-27** — Second scan: `docs/market-scan/2026-10-27_scan.md`. Upwork/JobStreet blocked WebFetch; Reddit blocked for the browser tool.
- **2026-10-27** — Add a **weekly Lead signals** step (30–45 min) to `market-scan`. Platforms: Reddit (r/smallbusiness, r/Bookkeeping, r/Contractor, r/quickbooksonline — Ken reads), Upwork (Ken, logged in), LinkedIn, US contractor/small-business Facebook groups, Intuit QuickBooks Community. Monthly scan stays.
- **2026-10-27** — Leads live in gitignored `private/leads.csv`. Public repo gets anonymous counts only.
- **2026-10-27** — Reply rules: (1) first reply is a public, useful answer, no pitch; (2) DM only if they reply or the post says "looking for someone"; (3) Claude drafts, **Ken edits and sends**; (4) follow each group's self-promo rules.

## 9. Product and content

- **2026-10-03** — Audience: aspiring and current Filipino freelancers (bookkeepers, VAs).
- **2026-10-03** — Content angle: "How to become an AI-native bookkeeper."
- **2026-10-27** — PDF guide **waits until after the first paid client** (it sells on real proof).
- **2026-10-27** — Two audiences: contractors get **helpful replies** (§8) + a pinned case study; Filipino freelancers get **2 short build-in-public posts/week** (same post on Facebook + LinkedIn), topics picked from trends and scan numbers.
- **2026-10-03** — Use the JHU "AI and Agentic AI in Finance" brochure as **inspiration only**. Do not copy its text or curriculum. Notes in `docs/JHU_NOTES.md`.

## 10. Open questions

- [x] Which niche first: construction or e-commerce? → **Contractors / home services** (2026-10-27, §4).
- [ ] Price for the PDF guide. (Decide in week 10–11.)
- [ ] Main automation tool after week 4: Make or n8n? (Decide from scan data.)
