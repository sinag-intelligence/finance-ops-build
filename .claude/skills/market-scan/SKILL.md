---
name: market-scan
description: Run Ken's monthly finance-ops job market and community scan, and the weekly lead-signals hunt, as checked prompt chains. Use when Ken says "market scan", "run the scan", "what's the market saying", "lead signals", "find leads", or on the monthly or weekly schedule.
---

# Market Scan (prompt chain)

Find out what clients are hiring for, which tools they use, and what they complain about. The results decide tool depth, niche, and region.

Write in simple, plain English.

## Sources

| Source | How | Login? |
|---|---|---|
| onlinejobs.ph | Web fetch the job search | No |
| Upwork | Web search / fetch public job pages | No |
| JobStreet PH | Web fetch | No |
| r/quickbooksonline | Built-in browser | Yes (Ken's) |
| Filipino freelancer Facebook groups (links in `docs/market-scan/SOURCES.md`) | Built-in browser | Yes (Ken's) |

Logged-in sites: read at human pace. Read only what Ken can see. No bulk copying. Never save people's names or private details — only the pain point, in your own words.

If the browser isn't available (computer off, app closed), do the public sources and say clearly which sources were skipped.

## The chain — each step checks the one before

### Step 1 — Collect
Keywords: `bookkeeper`, `QuickBooks`, `Xero`, `automation`, `AI bookkeeping`.
Collect up to **30 job posts** from the last 30 days. For each: source, region, tool(s), main task, pay, AI mentioned (yes/no).

**Check:** Every row has a source and a date. Drop posts older than 30 days. Drop duplicates (same company + same title).

### Step 2 — Filter
Keep posts that fit Ken's lane: SMB or small firm, finance ops / bookkeeping / automation. Drop enterprise, pure tax filing, and non-finance VA work.

**Check:** Write one line on why each dropped post was dropped. If more than half were dropped, say so — the keywords may need changing.

### Step 3 — Pain points (communities)
From Reddit + Facebook groups, collect the **top 5 complaints** or questions from the last 30 days. Paraphrase. Note how many posts touch each one.

**Check:** Each pain point is backed by at least 2 posts. Single posts go to "weak signals".

### Step 4 — Count
- Tool share (% of kept posts naming each tool)
- Region share
- Top 5 tasks
- Pay range by region
- % of posts mentioning AI or automation

**Check:** Re-count once from the rows. Numbers must match.

### Step 5 — Compare and decide
Read `DECISIONS.md` §4–5 and the last scan file. Compare.
Apply the **20% depth rule**: any tool in 20%+ of relevant posts gets real study time.
List any change worth making (tool, niche, region). **Do not change DECISIONS.md yourself** — propose, and let Ken confirm.

## Outputs

1. Append rows to `data/market_signals.csv` (same columns).
2. Write `docs/market-scan/YYYY-MM-DD_scan.md`:
   - 5-line summary
   - Tables from Step 4
   - Top 5 pain points
   - Proposed changes (with the numbers behind them)
   - Sources skipped (if any)
3. If a proposed change affects lessons, tell the `learning-session` Assessor by adding a line under "Assessor notes" in `learning/LEARNER_STATE.md`.
4. Add 1–3 content ideas to `content/IDEAS.md` (pain points make good posts).

## Weekly: Lead signals (added 2026-10-27)

Use when Ken says "lead signals", "find leads", or once a week. 30–45 minutes. Goal: find **buyers who already know they have a problem** we can fix (DECISIONS §4, §8).

**Target:** US contractors and home-service businesses. Also small US bookkeeping/CPA firms serving them.

**Pain types to look for:**
- `books-behind` — books behind, need cleanup, CPA or tax deadline coming
- `job-costing` — can't see profit per job
- `1099` — subcontractor payments / 1099 panic
- `sync-mess` — Jobber / Housecall Pro / other app ↔ QuickBooks duplicates or errors
- `bookkeeper-gone` — bookkeeper quit, looking for help
- `automate` — "how do I automate X" (invoices, receipts, payments)

**Sources:** see "Weekly lead signals" in `docs/market-scan/SOURCES.md`. Reddit and Upwork: Ken reads and pastes the post text or link. Claude reads the rest (public pages, or the browser at human pace).

**Steps:**
1. **Find** posts from the last 7 days that match a pain type. **Check:** each has a date, platform and link.
2. **Score awareness:** `hiring` (says they will pay) · `asking` (asks how to fix) · `venting` (just complains). Keep `hiring` and `asking`. **Check:** drop posts older than 7 days and duplicates.
3. **Draft a reply** for each kept post: a public, useful answer, 2–4 sentences, one real tip, **no pitch, no link**. For `hiring` posts, also draft a short DM or proposal. **Ken edits and sends. Claude never posts or sends.**
4. **Save** leads to `private/leads.csv` (gitignored — check with `git check-ignore private/leads.csv` before writing). Columns: `date_found,platform,link,pain_type,industry,awareness,status,next_step,note`.
5. **Count** for the public repo: append rows to `data/lead_signals.csv` (`week,platform,pain_type,awareness,count`). **No names, links or quotes** in public files.
6. Follow up older leads in `private/leads.csv`: list any with `status=replied` and no next step.

**Rules:** follow each group's self-promotion rules. Read only what Ken can see. Never store personal details beyond the post link.
