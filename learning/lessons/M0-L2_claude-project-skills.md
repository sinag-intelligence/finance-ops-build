# M0-L2 — Claude Project + Skills setup (v1)

**Skills:** AI-01 (main), TECH-02, TECH-03
**Default level:** New (mastery 0)
**Time:** ~75 min (can split over 2 short sessions)
**Practice data:** none needed — we use this repo's own files

## Why this matters for clients
AI-native bookkeeping firms want people who can set up Claude so it "knows" the client's rules, not people who paste the same long prompt every day. A Project with clear instructions + the right knowledge files, and a Skill that runs a repeat task the same way every time, is exactly what you will later build for clients (e.g. a "month-end checklist" Project). Doing it first for yourself is your practice run.

## Words to know
| Word | Plain meaning |
|---|---|
| Project (Claude.ai) | A workspace in Claude.ai with its own instructions, files, and chats |
| Project instructions | Text Claude reads before every chat in that Project |
| Project knowledge | Files you upload so Claude can read them in every chat |
| Skill | A folder with a `SKILL.md` file that teaches Claude one repeat task |
| zip | One file that packs a folder inside it. Claude.ai takes skills as zips |
| source of truth | The one place where the real, latest version lives. For us: **the repo** |
| sync | Copy the latest repo files into Claude.ai, replacing old copies |

## Note on the UI
Claude.ai changes its menus often. The names below (Projects, Settings → Capabilities → Skills) are correct as of late 2025 / 2026, but might move. If you can't find a button, tell me what you see and we find it together.

## Steps

### Step 1 — Check what already exists (~10 min)
1. Open claude.ai in your browser.
2. Go to **Projects**. Is there a Project called "Finance Ops Build"?
3. Go to **Settings → Capabilities** (look for **Skills**). Which custom skills are listed, if any?

Tell me:
- a. Does the Project exist? If yes, does it have instructions and files?
- b. Which skills (if any) are uploaded?

**Check:** a screenshot or the exact names you see.

### Step 2 — Project + instructions (~15 min)
1. Create the Project "Finance Ops Build" (or open it if it exists).
2. Open `docs/PROJECT_INSTRUCTIONS.md` in VS Code. Copy **only** the text inside the box in part A.
3. Paste it into the Project instructions. Save.
4. Set memory for this Project to **separate** from your other work (part D), if the setting exists.

**Check:** in a new chat inside the Project, ask: *"What 6 rules do you follow in this Project?"* The answer must match the 6 rules you pasted.

### Step 3 — Upload the knowledge files (~15 min)
1. Upload the 6 files from part B of `docs/PROJECT_INSTRUCTIONS.md`.
2. Do **not** upload the JHU PDF.

**Check:** in a new Project chat, ask: *"What is my main goal, and which week am I in?"* The answer must match `DECISIONS.md` §1 and `learning/LEARNER_STATE.md`.

### Step 4 — Rebuild a skill zip (~15 min)
The `.zip` files in `.claude/skills/` are old copies (and Git ignores them). After you change a skill, you must rebuild its zip.

1. In Claude Code, with `!` first, run:
   `C:/Windows/System32/tar.exe -a -cf .claude/skills/learning-session.zip -C .claude/skills learning-session`
2. Then look inside the zip:
   `C:/Windows/System32/tar.exe -tf .claude/skills/learning-session.zip`

**Check:** the list shows `learning-session/SKILL.md` and `learning-session/ASSESSOR.md` (the folder name comes first).

### Step 5 — Upload the skills to Claude.ai (~10 min)
1. Rebuild the other 2 zips the same way (`market-scan`, `build-to-content`).
2. In Claude.ai Skills settings: if an old version is there, delete it first. Then upload each new zip.
3. Make sure each skill is switched **on**.

**Check:** in a Project chat, say *"run the scan — just tell me the first step, don't run it."* Claude should name the `market-scan` skill and its first step.

### Step 6 — Explain it back (~5 min)
In 3 sentences, in your own words:
1. What goes in Project instructions vs Project knowledge?
2. When must you re-upload files or zips?
3. Why is the repo the source of truth, not Claude.ai?

**Check:** all 3 points correct, plain English.

## Harder variant (for fast progress)
- Change one line in `market-scan/SKILL.md` (e.g. a source name), rebuild only that zip, re-upload, and prove Claude.ai sees the new line.
- Write your own sync card: `learning/cards/claude-sync.md` (what to re-upload, when, and the zip command).

## Repair micro-lessons
- vocab: match 7 words (table above) to 7 meanings, then use 3 in one sentence each.
- concept: draw (on paper) repo → Claude.ai arrows. Which way do files flow? (Only repo → Claude.ai.)
- tool: do one upload + one delete together on a screen share / screenshots, step by step.
- tech: if `tar` fails, check you are in the repo folder (`! pwd`) and the folder name is spelled exactly.

## Revision log
- v1 — 2026-10-17 — created
- v1.1 — 2026-10-17 — Step 4: use full path to Windows tar (`C:/Windows/System32/tar.exe`). Plain `tar` in Git Bash is GNU tar and does not make real zip files.