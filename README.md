# Finance Ops Build — Starter Pack

Ken's AI-powered finance ops practice: learn → build → get clients → make content → make a product.

This repo is the **source of truth**. Claude Code and the Claude.ai Project both read from it.

## How it works
- **`DECISIONS.md`** — everything decided. Read first.
- **Dynamic Learning Assessor** — lessons adapt to how you actually do. No pre-test. Rules: `.claude/skills/learning-session/ASSESSOR.md`.
- **3 skills** — `learning-session`, `market-scan`, `build-to-content`.
- **Build once, use three times** — every module gives a skill, a client asset, and content/product.

## Setup (Week 1, about 2–3 hours)

1. **Install tools.** Git (from git-scm.com — it does NOT come with VS Code), VS Code, Python 3.10+.
2. **Unzip** this folder somewhere simple, e.g. `Documents/finance-ops-build`.
3. **Open it in VS Code.** File → Open Folder.
4. **Start Git.** In the VS Code terminal (Ctrl + `):
   ```
   git init
   git add .
   git commit -m "Starter pack"
   ```
5. **Put it on GitHub.** Create a **public** repo named `finance-ops-build` (no README). Follow GitHub's "push an existing repository" commands.
6. **Start Claude Code** in the same terminal: `claude`. It reads `CLAUDE.md` and finds the skills by itself.
7. **Test it.** Type: `start session`. You should see a dashboard and Step 1 of the first lesson.
8. **Create the Claude.ai Project.** Follow `docs/PROJECT_INSTRUCTIONS.md`.
9. **First browser scan.** In Claude.ai (desktop app open), sign in to Reddit and Facebook in the built-in browser, then say: `market scan`.

## Daily loop
1. `start session` → reviews first, then one step at a time
2. Do the step → show the result → get scored
3. `log session` → files update
4. `git add . && git commit -m "Session YYYY-MM-DD"`

## Weekly loop
1. `weekly review` → hours move to weak areas, plan updates
2. Re-upload `DECISIONS.md` + `LEARNER_STATE.md` to the Claude.ai Project

## Monthly loop
1. `market scan` → new scan file + proposed changes
2. Confirm or reject changes → update `DECISIONS.md`
