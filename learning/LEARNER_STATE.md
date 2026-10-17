# LEARNER_STATE.md — Ken

> Live state for the Dynamic Learning Assessor. Updated at the end of every session.
> Detailed numbers live in `data/skill_map.csv` and `data/session_log.csv`.

## Status
- **Week:** 2 of 12 (M0 extended by 1 week)
- **Module:** M0 — Setup (extended to week 2)
- **Current lesson:** M0-L2 done (2026-10-17). Next: M0-L3 (QBO developer sandbox)
- **Hours this week:** ~2.2 / 20 (week 2). Week 1 ended at ~1.5 / 20.
- **Total hours:** ~3.7 / ~240
- **Sessions done:** 4

## Starting point (no pre-test)
- Accounting graduate (2005), never practised → accounting lessons start at **Guided** level and move up fast if results are strong.
- Has done Claude Code setup basics and some terminal work → Tech lessons start at Guided.
- Everything else starts at **New**.
- The Assessor will correct these guesses within the first 2–3 sessions.

## This week's hour split
| Area | Planned | Done |
|---|---|---|
| Learn | 8 | 2.2 |
| Build | 8 | 0 |
| Clients + content + product | 4 | 0 |

## Next up
1. M0-L3 — QBO developer sandbox
2. First browser scan (Reddit + Facebook groups) with `market-scan`
3. M0 gate check (all core skills 2+; TECH-03 and QBO-01 still below)

## Skills due for review
- TECH-03 (VS Code) — 2026-10-18 — rename a file with F2 + edit Markdown exactly as asked (self-check before "done"; "add above" vs "replace")
- TECH-01 (Git) — 2026-10-24 — (mastery 3) commit loop with a twist: commit only one of two changed files
- AI-01 (Claude Project) — 2026-10-20 — say from memory: what goes in instructions vs knowledge; which 3 files to re-sync
- TECH-02 (terminal) — 2026-10-24 — (mastery 3) a new command with a flag, read its output

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

## Lesson revisions so far
- M0-L1 v1 — live adapt: Steps 3+4 merged into one real task (Rule A, two `U` in a row).
- M0-L2 v1 — live adapt: Project already existed, so Steps 2+3 merged into one sync step; only the changed skill zip rebuilt (Rule A). v1.1: zip command uses full path to Windows tar.
