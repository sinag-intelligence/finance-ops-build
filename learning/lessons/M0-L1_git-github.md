# M0-L1 — Git + GitHub: put this repo online (v1)

**Skills:** TECH-01, TECH-02
**Default level:** Guided (mastery 1)
**Time:** ~60 min
**Practice data:** none needed — we use this repo

## Why this matters for clients
Clients and bookkeeping firms want proof, not promises. A public GitHub repo with real builds and a steady commit history shows you can work in a clean, careful way. Later, every client build (Make/n8n exports, Excel templates, Claude Code helpers) will live in Git, so you can undo mistakes and show what changed.

## Words to know
| Word | Plain meaning |
|---|---|
| repo (repository) | A project folder that Git watches |
| commit | A saved snapshot of your files, with a short message |
| stage (`git add`) | Pick which changes go into the next commit |
| push | Send your commits from your PC to GitHub |
| pull | Bring commits from GitHub down to your PC |
| remote / `origin` | The online copy of the repo (on GitHub) |
| branch / `main` | A line of work. We use only `main` for now |
| `.gitignore` | A list of files Git must never save |

## Note on starting point
The repo is **already on GitHub** (`sinag-intelligence/finance-ops-build`) with one commit, "Starter pack". So this lesson does not set it up from zero. It checks that you **understand** what is there, and that you can run the daily loop alone.

## Steps

### Step 1 — Read the current state (~10 min)
In the terminal, inside this folder, run:
1. `git status`
2. `git log --oneline`
3. `git remote -v`

Then tell me, in your own words:
- a. Are there any unsaved changes?
- b. How many commits are there?
- c. Where is the online copy?

**Check:** your 3 answers match the real output.

### Step 2 — Check the repo is safe to be public (~10 min)
1. Open the repo page on github.com in your browser.
2. Find if it is **Public** or **Private** (look next to the repo name).
3. Open `.gitignore` in VS Code. Name 2 kinds of files it blocks, and say why.

**Check:** you report Public/Private correctly, and your 2 examples are in the file.

### Step 3 — Make one small change and commit it (~15 min)
1. Open `README.md`. Add one line at the bottom: `Started: 2026-10-03`.
2. Run `git status`. What colour / section is the file in?
3. Run `git add README.md`, then `git status` again. What changed?
4. Run `git commit -m "Add start date to README"`.

**Check:** `git log --oneline` shows 2 commits.

### Step 4 — Push and confirm online (~10 min)
1. Run `git push`.
2. Refresh the GitHub page. Find your new line in the README.

**Check:** `git status` says "up to date with 'origin/main'", and the line shows on GitHub.

### Step 5 — Explain it back (~10 min)
In 3 short sentences, explain to a new Filipino VA: what a commit is, what push is, and why `.gitignore` matters for client data.

**Check:** all 3 ideas are correct. (This is a mastery-4 / content check.)

## Harder variant (for fast progress)
- Undo a change before commit: edit a file, then run `git restore <file>`. Explain what happened.
- See what changed: `git diff` before `git add`, and `git diff --staged` after.

## Repair micro-lessons
- **vocab:** Use the "Words to know" table. Say each word as a sentence: "I *commit* to save a snapshot."
- **concept:** Picture three boxes: *working folder* → (`git add`) → *staging box* → (`git commit`) → *local history* → (`git push`) → *GitHub*. Draw it on paper.
- **tool:** Run `git status` after every command. It always tells you the next step.
- **tech:** If push asks for login, use the GitHub sign-in window from Git Credential Manager. Do not paste passwords into chat.

## Revision log
- v1 — 2026-10-03 — created. Adapted: repo was already online, so lesson checks understanding instead of first-time setup.
- v1 (live change) — 2026-10-03 — Two `U` in a row on TECH-01 (Rule A). Skipped the README practice change. Steps 3+4 merged into one real task: add `*.zip` to `.gitignore`, use `git diff`, commit, push. Not bumped to v2 (no struggle; one-off adapt).
