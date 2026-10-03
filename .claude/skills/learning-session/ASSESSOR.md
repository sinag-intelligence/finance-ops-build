# Dynamic Learning Assessor — Rules

The Assessor watches every step Ken does. It changes the lessons based on real performance, not on a test taken at the start.

There is **no pre-test**. The first time a skill comes up, the Assessor starts at the lesson's default level and adjusts fast.

---

## 1. What the Assessor tracks

Every skill in `data/skill_map.csv` has:

| Field | Meaning |
|---|---|
| `skill_id` | Short id, e.g. `ACC-02` |
| `area` | Accounting, QBO, Xero, Excel, Automation, AI, Tech, Client |
| `mastery` | 0–4 (see below) |
| `evidence` | Last 3 outcome codes, newest first, e.g. `U,H,U` |
| `last_practiced` | Date |
| `next_review` | Date for spaced review |
| `gap_type` | Last diagnosed gap: `vocab`, `concept`, `tool`, `tech`, `none` |

**Mastery levels**

| Level | Name | Meaning |
|---|---|---|
| 0 | New | Never done |
| 1 | Guided | Can do it with help |
| 2 | Solo | Can do it alone |
| 3 | Fluent | Fast, correct, can handle a twist |
| 4 | Teach | Can explain it — ready for product/content |

---

## 2. Scoring one step

After each step, record **one outcome code**:

| Code | Name | When |
|---|---|---|
| `U` | Unaided | Done correctly, no hints |
| `H` | Hinted | Done correctly after 1–2 hints |
| `S` | Shown | Needed the solution shown |
| `F` | Failed | Wrong or not finished, even with help |

Also ask Ken one quick question: **"Confidence: 1 low, 2 ok, 3 high?"**

How to tell if a step is correct: check the actual result (the number matches, the workflow runs, the file opens). Never mark `U` or `H` from Ken's word alone when a check is possible.

---

## 3. Adapting — the core rules

Apply after each step, in this order.

### Rule A — Move up (fast learner)
- `U` + confidence 2–3 → mastery +1 (max 4).
- Two `U` in a row on the same skill → **skip** the next practice step for that skill. Jump to a harder variant or the next skill.
- Mastery reaches 3 → mark the skill **ready for build work**.

### Rule B — Stay (normal learning)
- `H` → mastery stays. Add **one** extra practice variant (same idea, different data).

### Rule C — Move down and repair (struggle)
- `S` or `F` → mastery −1 (min 0).
- Diagnose the gap. Ask one short question to find out which one:
  - `vocab` — did not know a word ("What does 'accrual' mean to you?")
  - `concept` — knew the words, not the idea ("Why does this entry need two sides?")
  - `tool` — knew the idea, not where to click/what to type
  - `tech` — setup, file, terminal, or install problem
- Insert a **repair micro-lesson** (10–20 min) for that gap **before** retrying.
- Two `F` on the same step → **revise the lesson** (see section 5).

### Rule D — Confidence mismatch
- `U` but confidence 1 → don't raise mastery yet. Do one more variant to build confidence.
- `S`/`F` but confidence 3 → flag "overconfidence" in the session notes. Add a self-check step to future lessons in this area.

### Rule E — Time
- Each step has an estimate. If Ken takes **more than 2x** the estimate, treat `U` as `H`.
- If Ken finishes in **less than half** the time with `U`, apply Rule A even with one result.

---

## 4. Spaced review

Set `next_review` from mastery:

| Mastery | Review after |
|---|---|
| 0–1 | 1 day |
| 2 | 3 days |
| 3 | 7 days, then 14, then 30 |
| 4 | 30 days |

At the start of each session, any skill with `next_review` ≤ today gets **one quick review task** (5 min max) before new work. If the review is `S` or `F`, apply Rule C.

---

## 5. Revising lessons

A lesson is revised when:
1. Two `F` on the same step, or
2. Three sessions in a row with `H` or worse on the same lesson, or
3. The market scan changes what the lesson should teach (tool or task shift).

How to revise:
1. Keep the old version. Add a `## Revision log` entry at the bottom of the lesson file: date, reason, what changed.
2. Change the smallest thing that fixes the problem:
   - split a big step into two smaller ones,
   - add a worked example before the exercise,
   - add a missing vocabulary box,
   - change the practice data to something more familiar.
3. Bump the lesson version: `v1` → `v2`.

---

## 6. Re-planning the week

Every **Sunday** (or the first session of the week), run the weekly review:

1. Count outcomes by area for the last 7 days.
2. Move hours toward weak areas:
   - Area with most `S`/`F` → +2 hours next week.
   - Area with all `U` → −2 hours (min 1 hour, for review).
   - Keep the total at 20 hours.
3. Update the **Next Up** queue in `learning/LEARNER_STATE.md`.
4. If a whole module is at mastery 3+ on its core skills → mark the module **done early** and pull the next one forward.
5. If a module's core skills are still at 0–1 after its planned weeks → **extend** it by up to 1 week. Note the reason. Push later modules back.

---

## 7. Gates (move to the next module)

A module is done when:
1. All its **core** skills are at mastery **2+**, and
2. Its **build output** works on test data, and
3. Ken can explain the build in 3 sentences (checks mastery 4 for content).

Gates can't be skipped. Pace can change; quality can't.

---

## 8. What to write after every session

1. One row per step in `data/session_log.csv`.
2. Updated rows in `data/skill_map.csv`.
3. Updated `learning/LEARNER_STATE.md` (status, hours, next up, notes).
4. Any lesson revision in the lesson file.
5. If the session produced something worth sharing → add a line to `content/IDEAS.md`.
