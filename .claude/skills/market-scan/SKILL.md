---
name: market-scan
description: Run Ken's monthly finance-ops job market and community scan as a checked prompt chain. Use when Ken says "market scan", "run the scan", "what's the market saying", or on the monthly schedule.
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
