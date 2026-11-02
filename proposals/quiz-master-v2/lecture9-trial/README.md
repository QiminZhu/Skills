# Lecture 9 trial (ITCS217, Introduction to Data Link Layer)

A hand-run trial of the v2.0 design on one 59-slide lecture. `qm.py` does not exist yet, so the checks in `gate-report.md` were run in the authoring chat; see that file for which rows are script results and which are judgment.

| File | What it is |
| --- | --- |
| `catalog.json` | 40 knowledge units, page accounting for all 59 slides, 5 source issues with cited references |
| `priority-review.md` | Suggested priorities waiting for human confirmation |
| `preview-bank.json` | 10 draft questions in BankQuestion v4 (not blind-checked, not reviewed) |
| `gate-report.md` | Simulated gate result: blocked at priorities and source issues |
| `app/quiz.template.html` | The quiz app; `__BANK__` and `__UNITS__` are filled at build time |
| `scripts/` | The scripts that built the catalog and preview bank, and the browser playtest |

The lecture PDF is not committed (repository policy: no lecture uploads). The catalog identifies it by SHA-256 `2eb61b8246aad4987e648bf4b71f9597fb67b42e60c97a75841f137912e9a597`. The scripts expect it at `/root/qm-run/lecture9.pdf`.
