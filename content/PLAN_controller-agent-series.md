# Content plan — "The AI Controller, made small"

> Source: `finance/finance-bookkeeper-controller.md` in [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT license, ~160k stars).
> Created: 2026-10-17. Status: **agreed, starts after M0 is done.** Week numbers below shift if M0 runs longer.
> Rule: use it as **inspiration only**, like the JHU brochure (DECISIONS §9). Write in our own words. Always link the source.

---

## 1. What the file is (plain summary)

1. It is a **prompt** that turns an AI into a "Controller" persona called Dana (13+ years, "150 months of closes").
2. It has **8 hard rules**: follow GAAP, reconcile every balance sheet account monthly, split duties, every journal entry needs a reason + proof + approval, close on a fixed schedule, materiality decides effort (not accuracy), disclose old-period fixes, be audit-ready every day.
3. It has a **work rhythm**: daily (AP, cash, bank), weekly (AP aging, high-volume recs), monthly (close + "retro"), quarterly, yearly (1099s, audit).
4. It has **2 templates**: a month-end close checklist and an account reconciliation template.
5. It has **success numbers**: close in X days, 100% of accounts reconciled, <5% of AR past 90 days, cash forecast ±5%.
6. It is written for **mid-size and big companies**: SOX, ASC 606/842/805, NetSuite, BlackLine, FloQast.

## 2. Why it matters for Ken

| The file says | Ken's clients (US SMB on QBO) need |
|---|---|
| SOX, ASC 805, multi-entity | Not needed. Too big. |
| Reconcile every account monthly | **Yes.** This is the core of catch-up / cleanup work. |
| Journal entry = reason + proof + approval | **Yes.** Easy to show in QBO (memo + attachment). |
| Close checklist + recon template | **Yes.** Same as M1 topics 2 and 5. |
| Daily / weekly / monthly rhythm | **Yes.** This *is* the monthly retainer offer. |
| Success numbers | **Yes**, a small version. Good for case studies. |

**The big idea:** the file shows how a *controller* thinks. Most PH bookkeepers are paid $2.50–$15/hr for *data entry*. The gap between the two is Ken's positioning: "I bring controller habits to small business books, with AI and automation."

**The honest angle:** Ken is *not* a controller. Ken is a learner who reads this, cuts it down to small-business size, and tests it on fake data in the QBO sandbox. That is the story. No fake expertise.

## 3. Content pillars (from this one file)

1. **Controller rules, made simple** — one rule per post, with a small-business example.
2. **Trim it down** — "enterprise vs small business": what to keep, what to drop.
3. **Build it** — turn the file into Ken's own Claude skill for QBO cleanup, test it, show results.
4. **Prompt literacy** — "what an AI agent file is, and how to read one" (for VAs who use AI but never read a prompt).

## 4. Short-form plan (3 posts per week, ~20 min each)

Fits inside the 4h/week "clients + content + product" budget. Write in batches of 3 on one day.

| # | Week | Post | Format | Pillar |
|---|---|---|---|---|
| 1 | 3 | "I read the 'AI Controller' file 160k devs starred. Here's what a small-business bookkeeper should steal from it." | story | 2 |
| 2 | 3 | Rule: reconcile **every** balance sheet account, not just the bank | how-to | 1 |
| 3 | 3 | "Speed without accuracy is noise" — my version: a fast wrong close costs more than a late right one | opinion | 1 |
| 4 | 4 | Rule: every journal entry needs 3 things — reason, proof, approval (QBO memo + attachment) | how-to | 1 |
| 5 | 4 | Daily / weekly / monthly rhythm as one simple table (carousel) | carousel | 1 |
| 6 | 4 | "What an AI agent file is — explained like a job description" | how-to | 4 |
| 7 | 5 | Rule: materiality — when a $3 difference matters, and when it doesn't | how-to | 1 |
| 8 | 5 | Enterprise words you can skip (SOX, ASC 805) vs words you must know (accrual, cut-off) | before/after | 2 |
| 9 | 5 | Segregation of duties for a 3-person business (it's possible) | how-to | 1 |
| 10 | 6 | 5 numbers a small business owner should get from a bookkeeper every month | carousel | 1 |
| 11 | 6 | My first test: the AI controller on a fake messy QBO company — what it got wrong | story | 3 |
| 12 | 6 | "Audit-ready every day" for a small business = 4 habits | how-to | 1 |

Rules for every post (from `build-to-content`):
1. Plain English. Taglish version only if Ken asks.
2. No hype words. No income promises.
3. End with a question to the reader.
4. Link the source repo when quoting or summarising it.
5. Fake data only in screenshots.

## 5. Long-form plan (1 piece every 2 weeks, ~2h each)

| # | Week | Piece | Ties to | Also becomes |
|---|---|---|---|---|
| L1 | 3–4 | **"The AI Controller, made small"** — read the file, cut it to SMB size, share Ken's trimmed version (own words) | M0 / M1 start | PDF chapter intro |
| L2 | 5–6 | **"My month-end close checklist for QBO small businesses"** — Ken's own checklist, tested on the sandbox cleanup | M1 build | 💼 client asset + PDF chapter "Catch-up bookkeeping" |
| L3 | 7–8 | **"I gave an AI the controller rules. Here's its error rate."** — test the skill on a known-correct fake data set | M4 (testing AI output) | Case study with numbers |
| L4 | 9–10 | **"Month-end close helper: AI drafts, human approves"** — the M5 build, using the rhythm + recon template | M5 build | Pilot offer for bookkeeping firms |

Format: a long LinkedIn article or a blog post, plus a 5–8 min screen-record video if time allows.

## 6. The build behind the content (so posts have proof)

Do **not** build this now. Ken is in M0. Slot it into the curriculum:

1. **M1 (week 3–4):** write `docs/CONTROLLER_RULES_SMB.md` — Ken's own small-business version of the 8 rules + the rhythm. Pure learning, no code.
2. **M1 build:** use the checklist and recon template ideas while cleaning the fake QBO company.
3. **M4–M5:** turn the SMB rules into a Claude skill (e.g. `close-helper`). Test on fake data. Measure errors. This needs a DECISIONS entry first (new skill — rule "add only when a task repeats 3+ times").

## 7. Weekly rhythm for content (proposal)

1. **One batch day per week** (e.g. Saturday, 1h): write 3 short posts from this plan + `IDEAS.md`.
2. **Post Mon / Wed / Fri.**
3. **Long-form every 2nd week**, right after a build step is done (so it has real proof).
4. Log each published post in `content/posts/` with date + platform + replies.

## 8. Ken's answers (2026-10-17)

1. **Platforms:** use what gives better results. If no clear winner, post to many platforms with automation.
2. **Start:** wait until M0 is done.
3. **Long-form:** yes to video. Format = **long instructional text post + link to the long-form video**.

## 9. Platform test (4 weeks after start)

Two audiences, so two starting platforms:

| Audience | Platform | Why |
|---|---|---|
| Filipino freelancers (content + PDF buyers) | **Facebook** (own page + 3 freelancer groups) | Where the audience already is (see market scan sources) |
| Clients (US SMBs, bookkeeping firms) | **LinkedIn** | Where owners and firm owners look for help |
| Long-form video home | **YouTube** | Searchable, the link works on every platform |

1. Post the same piece on Facebook + LinkedIn for 4 weeks.
2. Track per post in `content/posts/`: reactions, comments, shares, profile visits, DMs. **DMs and leads count most.**
3. After 4 weeks: keep the winner as the main platform. Keep the other only if it gives leads.

## 10. Automated multi-platform posting

1. **Before M3:** post by hand, or use a free scheduler for the FB page + LinkedIn.
2. **Facebook groups can't be auto-posted** (Meta closed the Groups API in 2024). Group posts stay manual, with a human touch. This also fits the "human pace" rule (DECISIONS §7).
3. **M3 build idea:** a Make / n8n workflow: draft in `content/posts/` → Ken approves → posts to FB page + LinkedIn → logs the result in a sheet. This becomes real portfolio proof (build once, use three times).

## 11. Long-form format

1. Instructional text post (8–15 short steps or points). It must be useful on its own.
2. Link to the YouTube video for the full walkthrough. Tip: test the link in the first comment vs. the post body, because platforms may show posts with links to fewer people.
3. Same video → PDF chapter → case study.
