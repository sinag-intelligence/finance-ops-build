# LEARNER_STATE.md — Ken

> Live state for the Dynamic Learning Assessor. Updated at the end of every session.
> Detailed numbers live in `data/skill_map.csv` and `data/session_log.csv`.

## Status
- **Week:** 4 of 12 by calendar (week 1 started 2026-10-03). M0 is past its extended end (week 2). Weekly review overdue.
- **Module:** M0 — Setup. All 5 core skills now at mastery 3. Gate check next.
- **Current lesson:** M0-L3 done (2026-10-26). Next: weekly review, then M0 gate check
- **Hours this week:** ~0.3 / 20 (week 4, from 2026-10-24). Session 5 total ~1h (estimated from step minutes + talk).
- **Total hours:** ~4.7 / ~240
- **Sessions done:** 5

## Starting point (no pre-test)
- Accounting graduate (2005), never practised → accounting lessons start at **Guided** level and move up fast if results are strong.
- Has done Claude Code setup basics and some terminal work → Tech lessons start at Guided.
- Everything else starts at **New**.
- The Assessor will correct these guesses within the first 2–3 sessions.

## This week's hour split
| Area | Planned | Done |
|---|---|---|
| Learn | 8 | 0.3 |
| Build | 8 | 0 |
| Clients + content + product | 4 | 0 |

## Next up
1. Weekly review (overdue: Sundays 2026-10-18 and 2026-10-25 missed). Look at hours: far below 20/week.
2. M0 gate check: core skills all 3 ✅; build output (repo live + sessions logged) ✅; Ken explains M0 in 3 sentences ⏳
3. First browser scan (Reddit + Facebook groups) with `market-scan` (M0 step 6)
4. Then M1. Content plan starts after M0 (DECISIONS §9 entries still waiting for Ken's yes)

## Skills due for review
- TECH-01 (Git) — 2026-10-24 (overdue) — commit loop with a twist: commit only one of two changed files
- TECH-02 (terminal) — 2026-10-24 (overdue) — a new command with a flag, read its output
- AI-01 (Claude Project) — 2026-10-28 — (mastery 3) twist: what to do after editing a skill file (rebuild zip + re-upload)
- TECH-03 (VS Code) — 2026-10-31 — (mastery 3) multi-part card/file: check file vs instruction line by line before "done" (Rule B extra variant)
- QBO-01 (QBO sandbox) — 2026-11-02 — (mastery 3) open the sandbox from the card alone; find one report

## Assessor notes
(patterns the Assessor sees — e.g. "fast on concepts, slow on tool clicks")
- 2026-10-03 — Reads tool output well and spots real changes (found new zip files). Needs hints on exact command typing (`!` prefix, missing `git`). Tool gap, not concept gap.
- 2026-10-03 — Good safety instinct (checks for PII before commit), but first guess was not checked against the file. Habit to build: verify with the real file before claiming.
- 2026-10-03 — Strong with analogies (commit = game save slot). Good sign for teach/content level.
- 2026-10-03 — Minutes often not reported. Ask for minutes at the end of each step.
- Practice habit given: "Say it, do it, check it" from memory. First use: session-end commit.
- 2026-10-03 — Session-end practice: forgot `git add` from memory, and put text before `!` 3 times. Both `S`. TECH-01 2→1, TECH-02 1→0. Repair micro-lesson next session before new work.
- 2026-10-15 — After a 12-day gap Ken reported forgetting most Git basics. Recognition was still good (4/4 match). Relearn + own cheat card (`learning/cards/git-loop.md`) worked well.
- 2026-10-16 — Reads error messages and self-fixes (git add hint). Strong habit — keep reinforcing.
- 2026-10-17 — Session 3 reviews: TECH-02 1→2 (git log variant unaided after hints). TECH-03 stays 1: two `H` on exactness (extra `- ` before heading, READ.md vs README.md, "Faked" vs "Fake"). Pattern: says "done" before checking result against the instruction. Habit to build: re-read the instruction line by line before "done". Still sends some commands to chat without `!` (`git add .`).
- 2026-10-17 — Weekly review: M0 extended 1 week. Hours stay 20/week. New rhythm: a session at least every 2 days (DECISIONS §6).
- 2026-10-17 — Session 4 (M0-L2): fast on discovery and terminal (`!` first every time, 2 min vs 10). Strong concept: "a push goes to GitHub, not to Claude.ai". Slips come from context switching: nearly deleted local skill files instead of the Claude.ai copy; typed a fix in chat instead of the file. Exactness pattern continues (replaced a line instead of adding above). Habits: "PC or browser?" before any delete; "is it in the file?" before done.
- 2026-10-26 — Session 5 (reviews + M0-L3), spread over 4 days (10-18, 10-21, 10-24, 10-26). Gaps of 2–3 days; the "every 2 days" rhythm was mostly kept, but hours are very low. Short drills now unaided (TECH-03 1→3, AI-01 2→3). QBO-01 0→3 fast: read both balance columns unasked, explained the balance sheet equation in own words (incl. advances as liabilities). Good habits: asks before filling unknown form fields (role, app name); sources claims (2-year sandbox validity from Intuit page). Exactness slips remain on bigger real files (card: extra copied instruction line, leading spaces, wrong path). Also reports before finishing every part of a step.

## Lesson revisions so far
- M0-L1 v1 — live adapt: Steps 3+4 merged into one real task (Rule A, two `U` in a row).
- M0-L2 v1 — live adapt: Project already existed, so Steps 2+3 merged into one sync step; only the changed skill zip rebuilt (Rule A). v1.1: zip command uses full path to Windows tar.
- M0-L3 v1.1 — Step 2: use Intuit's default US sandbox. Step 5: card must include the click path to open the company.
