# Job sheet — {Client name} (fake / masked only)

> Copy this whole `client-job` folder for every new job. Rename it `{client-short-name}/`.
> SOP: DECISIONS §6 (2026-11-04). Make it a skill after 3 uses.

## The job
| Field | Value |
|---|---|
| Client | |
| Business type | |
| Offer | (e.g. Offer 1 — Tax-ready books) |
| Software | (e.g. QBO) |
| Period | (from – to) |
| Basis | cash / accrual |
| Price | |
| Status | intake / waiting on client / working / review / delivered |
| Started | |
| Due | |

## Folders
| Folder | What goes here | Rule |
|---|---|---|
| `01_from_client/` | Everything the client gave: bank CSVs, PDF statements, notes, emails | **Never edit.** Save with the date received |
| `02_requests/` | What's missing + questions for the client | One list, update status |
| `03_working/` | My work: notes, categorization log, reconciliations, checks | Date every file |
| `04_deliverables/` | What the client / CPA gets: reports, lists, summary | Final versions only |

## Intake checklist (before any work)
- [ ] Bank + credit card **statements (PDF)** for every account, every month in the period
- [ ] Bank / card **exports (CSV)** or bank feed access
- [ ] Opening balances proof (last statement before the period, or last year's balance sheet)
- [ ] List of all accounts (checking, savings, cards, loans)
- [ ] Owner notes: jobs/projects, customers, what each payee is
- [ ] Subcontractor list + **W-9s** (for the 1099 list)
- [ ] Receipts for large or unclear payments
- [ ] Software access (user invite, not the owner's password)
- [ ] Anything missing → written in `02_requests/requests.md`

## Done checklist (before delivery)
- [ ] Every account reconciled, difference $0.00
- [ ] Uncategorized / Pending = 0
- [ ] Open questions answered or listed for the client
- [ ] Deliverables in `04_deliverables/`
- [ ] "True today?" check on the summary
