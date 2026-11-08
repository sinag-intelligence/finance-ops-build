# Job sheet — Fake Builders LLC (FAKE practice client)

> Made from `../_templates/client-job/`. SOP: DECISIONS §6 (2026-11-04).
> Lesson: `learning/lessons/M1-L1_fake-builders-catch-up.md`.

## The job
| Field | Value |
|---|---|
| Client | Fake Builders LLC (small US remodeling contractor, 1 owner, no employees) |
| Offer | Offer 1 — Tax-ready books (catch-up + job costing + 1099 list for the CPA) |
| Software | QBO sandbox "Fake Builders LLC" |
| Period | 2026-08-01 to 2026-10-31 (3 months behind) |
| Basis | cash |
| Status | working (M1-L1 Step 6B) |
| Started | 2026-10-28 |

## Folders
| Folder | What is here |
|---|---|
| `01_from_client/` | Bank CSV (44 lines), 3 monthly PDF statements, owner notes. **Never edit.** |
| `02_requests/` | `requests.md` — what's missing + client questions |
| `03_working/` | My notes: traps, categorization, reconciliations |
| `04_deliverables/` | P&L, Balance Sheet, 1099 list, case study (Steps 8–9) |

`make_bank_statements.py` rebuilds the PDFs from the CSV (practice only — a real client sends the PDFs).

## Intake checklist
- [x] Bank statements (PDF), Business Checking, Aug–Oct
- [x] Bank export (CSV), Business Checking
- [x] Opening balance: $8,500.00 as of 07/31/2026 (from Aug statement beginning balance)
- [ ] All accounts listed — savings 4471 statements missing (see requests)
- [x] Owner notes: projects, customers, savings 4471 = business
- [ ] Subcontractor W-9s (see requests)
- [ ] Receipts for large payments (see requests)
- [x] Software access (sandbox)

## Done checklist
- [ ] Every month reconciled, difference $0.00 (Step 7)
- [ ] Pending = 0 (Step 6B)
- [ ] Open questions listed for the client
- [ ] Deliverables in `04_deliverables/` (Step 8)
- [ ] "True today?" check on the case study (Step 9)
