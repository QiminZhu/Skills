# Quiz Master v2.0 — design spec

Nov 2, 2026 · status: proposal (not implemented, not published)

Living copy with comments: the "Quiz Master v2.0 — design spec" Claude doc. This file is an export of it.

## Summary

Version 2.0.0 keeps v1.3's integrity checks and adds the proposal's teaching design. It is a major version because the catalog and question schema change.

| Area | v1.3 today | v2.0 |
| --- | --- | --- |
| Starting point | One pipeline for every quiz | Purpose and tier chosen first |
| Inventory | Model-ranked atomic objectives | Knowledge units; a human confirms every priority |
| Coverage | 1 adequate mapping per required objective | Core: 2 questions, recall + application. Supporting: 1. Distinction: 1 comparison |
| Bank vs quiz | Bank = quiz, 20-question cap | Bank larger than the quiz; each attempt draws by rule |
| Answer-key check | Validator in the same conversation | Blind re-answer in a fresh context, then human spot-check |
| Integrity | Hashes computed by hand | `qm.py` hashes real source files, binds approvals and runs the gate |
| Learner experience | None | Static quiz app: confidence check, feedback, spaced retakes |

Sources: the current `plugins/quiz-master` code and the proposal "Building Effective Quizzes from Lectures with AI" (Nov 2, 2026).

## Purpose and tier

Every run starts by recording one purpose and one tier in the bank's `meta` block. Mixing purposes in one quiz is not allowed; a second purpose means a second bank.

| Purpose | Design it drives | Default tier |
| --- | --- | --- |
| Practice (retrieval) | Low stakes, repeatable attempts, spaced retakes | Practice |
| Diagnosis | Every distractor names a misconception; summary groups misses by unit | Practice |
| Calibration | Confidence check on every scored item; confident-but-wrong list | Practice |
| Measurement | Fixed attempt, no feedback until the end, no retake within a session | Exam |

The two tiers share one pipeline and one gate. They differ only in how much review the gate demands.

| Check | Practice tier | Exam tier |
| --- | --- | --- |
| Source fingerprints, page accounting, schema | Required | Required |
| Human-confirmed priorities | Required | Required |
| Blind re-answer in a fresh context | Required | Required |
| Human spot-check | Core questions + flagged items | Every question |
| Separate analysis audit | Optional | Required |
| Separate ledger review | Optional | Required |

Because `qm.py` automates hashing, the integrity checks cost almost nothing in either tier. The extra cost of the exam tier is human reading time.

## Workflow

The pipeline has ten stages; two of them are human decisions, and nothing reaches students until `qm.py gate` passes.

1. Purpose and tier
2. Lecture analyzer: knowledge units, page accounting
3. **Human priorities**: confirms core, supporting, detail
4. Analysis audit (exam tier only)
5. Generate per unit: drafts, ledger, `qm.py check`
6. Blind check: fresh context, no answer key
7. **Human spot-check**: core and flagged; every item in the exam tier
8. `qm.py gate`: hashes, coverage, draw, fairness
9. Export: approved items and draw policy
10. Quiz app

A blind-check disagreement sends the item back to generation; a coverage gap or stale approval at the gate does the same, or splits the lecture into two banks.

## Catalog: knowledge units

The catalog lists knowledge units: one line per thing a student could get wrong, not one per slide. The model suggests a priority for each unit; a human confirms or changes it, and the gate refuses any unit still marked as a suggestion.

| Field | Values | Notes |
| --- | --- | --- |
| `unitId` | Stable, globally unique | Kept across revisions when the unit is unchanged |
| `kind` | `fact`, `concept`, `procedure`, `distinction` | A distinction also lists the units it separates in `contrasts` |
| `statement` | One assessable sentence | Observable verb; one skill per unit |
| `priority` | `core`, `supporting`, `detail` | Detail units are optional and count as deliberate gaps |
| `prioritySource` | `suggested`, `human` | Must be `human` before the gate passes |
| `misconceptions` | List of known wrong ideas | Seeds distractors; may be empty |
| `sourceRefs` | File + 1-based page, or video + timestamp | At least one per unit |

These parts of v1.3 stay unchanged:

- Root `sourceFiles` with SHA-256 of the file bytes and a page count.
- `pageAccounting`: one entry per page, with a disposition and the units it supports.
- `sourceIssues` for slide errors; corrections need a labeled external reference.

The old objective fields (`cognitiveTargets`, `origin`, per-lecture `sourceFiles`) are removed, so there is one catalog contract instead of two.

Human priority review is a required step, not a suggestion. The analyzer shows a short table of units with suggested priorities and asks the person to raise what the professor stressed, what the syllabus lists and what past quizzes tested.

## Coverage rules and draw model

Coverage is judged across the whole bank; each attempt then draws a smaller quiz from it. This removes v1.3's dead end, where one capped bank had to cover every objective.

### Minimum coverage per unit

Only approved questions count, and only through response parts the ledger maps to the unit with `adequate` evidence.

| Unit | Minimum in the bank | Required cognitive roles |
| --- | --- | --- |
| Core | 2 questions | At least one `recall` and one `application` |
| Supporting | 1 question | Any |
| Distinction | 1 question | `comparison` of the contrasted units side by side |
| Detail | 0 | Optional; listed as a deliberate gap |

`cognitiveRole` is a new question field: `recall`, `application`, `comparison`, `explain` or `predict`. It is separate from `type`, which stays the answer format.

### Bank and draw policy

- The bank should hold about 2 to 3 times the attempt size. The default target is 25 questions for a 10-question attempt.
- Default attempt: 10 questions, adjustable from 8 to 12.
- Default attempt structure: 2 to 3 warm-up recall, 4 to 6 application, 1 to 2 explain-why, and 1 to 2 review questions from earlier lectures.
- Every attempt includes at least one question for each core unit. If core units outnumber the non-review slots, the gate fails and proposes splitting the lecture into two banks.
- v1.3's workload caps apply per attempt, not per bank.

### Workload counting

Units per attempt keep v1.3's caps: matching pairs, ordering items, blanks and options. One change: a `multiple` question now costs 1 unit, the same as `single`. Coverage mapping can still point at individual options.

## Blind answer-key check

The answer key is checked by a solver that never sees it. The solver runs in a fresh context: a new chat, a sub-agent or a different model, with only the source slides and a keyless copy of the bank.

1. `qm.py strip bank.json` writes `blind-bank.json`. It removes `correct`, `matches`, `correctOrder`, blank answers, every explanation and every `misconception` label, and shuffles options so position gives nothing away.
2. The fresh-context solver answers every question from the slides alone. For each one it records its answer, a confidence level and any flag: ambiguous, unsupported by the slides, or more than one defensible answer.
3. `qm.py compare` matches the blind answers against the real key and lists every disagreement and every flag.
4. Each disagreement is resolved by fixing the question, fixing the key, or rejecting the item. A fixed item goes back through steps 1 to 3.

The blind-answer file is bound to the hash of the exact keyless bank it answered. Any later edit to a question makes its blind check stale.

`qm.py` cannot prove the context was fresh. The report records how the check ran (`context`, `model`, `sessionRef`) as a stated claim, and the instructions forbid running it in the authoring chat.

### Human spot-check

After the blind check, a person reads the questions the tier requires (see Purpose and tier). The person signs `review.json` with their name and each reviewed question's hash. Flagged items cannot pass on the model's word alone; a person must clear each one.

The Question Validator's other checks stay: distractor plausibility, answer cues, option-length patterns, source citations and cognitive level.

## Integrity: qm.py

One script, `qm.py`, replaces `check_bank.py` and `check_coverage.py` and takes over all hashing. No model computes a hash by hand.

| Command | What it does |
| --- | --- |
| `fingerprint <files>` | Hashes the actual source files and counts their pages; writes `sourceFiles` |
| `check bank.json` | Schema and structure checks for all question formats |
| `strip bank.json` | Writes the keyless, shuffled copy for the blind check |
| `compare` | Compares blind answers with the key; lists disagreements and flags |
| `bind <report>` | Writes the current hashes into a report, an approval or the review file |
| `gate --tier practice\|exam` | Runs every check below; exit 0 only when all pass |
| `export` | Writes `quiz-bank.json` for the app: approved items only, plus draw policy |
| `migrate` | Converts a v1.3 catalog and bank to v2 (see Migration) |

### What the gate checks

- **Source bytes.** The gate re-hashes the real source files and compares them with the catalog. In v1.3 this was only a pattern check.
- **Bindings.** Every approval, blind check, review and ledger mapping must match the current hash of what it covers. An edit makes it stale.
- **Priorities.** Every unit has `prioritySource: human`.
- **Coverage.** The unit minimums and required cognitive roles hold, using approved questions only.
- **Draw feasibility.** At least one valid attempt exists that meets the attempt structure and includes every core unit.
- **Blind check.** Every approved question has a matching blind answer with no unresolved disagreement or flag.
- **Human review.** The questions the tier requires are signed off by hash.
- **Fairness.** No matching question shows its pairs in answer order. No choice tier, including each part of a two-tier question, has a correct answer that is the unique longest option and at least 1.2 times the average distractor length. For multiple-select, no correct option may be longer than every distractor.

The gate reports adequate, partial, missing, unverified and excluded units, as v1.3 does. Its limit is unchanged: it proves the bookkeeping, not that the content is true.

## Question schema v4

BankQuestion v4 keeps all six v3 formats and their grading rules. It adds the fields below and two new formats.

| Field | Applies to | Purpose |
| --- | --- | --- |
| `unitId` (replaces `objectiveId`) | All | Primary knowledge unit |
| `cognitiveRole` | All | `recall`, `application`, `comparison`, `explain`, `predict` |
| `lectureId` | All | Lets later lectures draw this item as review |
| `misconceptions` | Choice options, matching pairs, numeric blanks | Names the wrong idea behind each distractor; `null` on correct answers |
| `sourceRefs[].timestamp` | All | Optional video position, beside the page |
| `confidenceCheck` | All scored items | Default `true` |

Example of a choice option list in v4:

```json
"answers": ["Light intensity", "Soil water"],
"correct": [0],
"optionExplanations": ["In a dim room, light limits the rate.", "Water is plentiful in this scenario."],
"misconceptions": [null, "Water is always the limiting factor"]
```

### New formats

- **`two_tier`**: a choice question ("Which happens?") followed by a choice question on the reason ("Why?"). Both tiers are graded, and the summary shows right-answer-wrong-reason separately.
- **`self_explain`**: the learner writes 2 to 3 sentences, then sees a model answer and a checklist of 2 to 5 points to grade themselves. Self-grades are never counted as `adequate` coverage evidence and never enter the score.

v3 items migrate automatically. `cognitiveRole` and `unitId` are filled by `qm.py migrate` from the v1.3 catalog and must be confirmed in review before the item counts.

## Learner experience: the quiz app

v2.0 ships the consumer v1.3 lacked: `app/quiz.html`, one static HTML file that loads `quiz-bank.json`. It needs no login and no server.

### One attempt

1. The app draws an attempt by the bank's draw policy, then shuffles options, ordering items and matching sides in code.
2. The learner answers. Answers and feedback stay hidden until they commit.
3. Before the result appears, the learner picks a confidence level: Guessing, Fairly sure or Certain.
4. Feedback shows right or wrong, the explanation for the chosen option, the misconception it reflects, and a link to the slide or timestamp.
5. A separate Next button moves on. Checking an answer never advances by itself.

### End-of-attempt summary

- Score, and how many questions came from each unit.
- **Confident but wrong**: questions answered Certain or Fairly sure and missed, listed first.
- Missed questions grouped by knowledge unit, each with its misconception and slide link.
- For `two_tier`, right-answer-wrong-reason shown separately.
- Self-explanation answers with the learner's own checklist ticks, kept apart from the score.

### Repetition and review

- Progress lives in the browser's localStorage: attempt history, missed questions and confidence. The app works normally when storage is unavailable.
- Missed questions are favoured in the next draw.
- Suggested retakes: later today, in 2 to 3 days, and before the exam date if the learner sets one.
- Each attempt mixes in 1 to 2 review questions from earlier lectures' banks loaded in the same app.

### Tone

The app says plainly that mistakes here are useful and that nothing is graded or recorded anywhere else. Exam-tier banks switch to measurement mode: no feedback until the end and no retake in the same session.

## Layout, migration and tests

### Skill and file layout

Each skill is rewritten as one current procedure, with no appended v1.x sections. Networking examples (DHCP, HDLC, ARP) move to an optional example file.

| Path | Role |
| --- | --- |
| `skills/lecture-analyzer/` | Knowledge units, page accounting, suggested priorities, the human priority step |
| `skills/analysis-validator/` | Separate analysis audit; required in the exam tier |
| `skills/quiz-master/` | Purpose and tier, per-unit generation, ledger, orchestration |
| `skills/blind-checker/` | Replaces question-validator: fresh-context solving, compare, quality review |
| `references/catalog-contract.md` | The single catalog contract |
| `references/question-contract.md` | BankQuestion v4 |
| `references/coverage-and-draw.md` | Unit minimums, draw policy, workload |
| `references/examples/networking.md` | Course-specific pitfalls, optional |
| `scripts/qm.py` | Fingerprint, check, strip, compare, bind, gate, export, migrate |
| `app/quiz.html` | The learner-facing quiz app |

### Migration from v1.3

1. `qm.py migrate` turns objectives into units. `core` and `supporting` carry over with `prioritySource: suggested`, so a person must confirm them.
2. v3 questions gain `unitId` and a proposed `cognitiveRole`; `misconceptions` start empty.
3. All existing approvals become stale, because the payloads change. Each item needs a blind check and review again.
4. The release is tagged `quiz-master/v2.0.0`, and the missing v1.3 tag is added first. (v1.2.0 cannot be tagged: its files were never imported.)

### Acceptance tests

The 24 v1.3 coverage tests are kept where they still apply. New tests cover these cases:

- [ ] A source file edited after fingerprinting fails the gate.
- [ ] A unit with `prioritySource: suggested` fails the gate.
- [ ] A core unit with two recall questions and no application fails.
- [ ] A distinction with no comparison question fails.
- [ ] More core units than attempt slots fails, with a split proposal.
- [ ] A question edited after its blind check is stale.
- [ ] An unresolved blind disagreement or flag blocks approval.
- [ ] The stripped bank contains no key, explanation or misconception text.
- [ ] A matching question listed in answer order fails.
- [ ] `self_explain` results never count as coverage.
- [ ] The app grades all eight formats, shuffles correctly and works without localStorage.
- [ ] A CI workflow runs all tests on every push.

## Revisions after the Lecture 9 trial

A hand-run trial on ITCS217 Lecture 9 (59 slides) exposed six gaps. Each is now part of the spec. The trial files are in `lecture9-trial/`.

| Gap found | Rule added |
| --- | --- |
| A split bank can pass draw feasibility while its supporting units are never drawn | **Rotation.** Every supporting unit must be drawable within 3 consecutive attempts. The gate simulates 3 draws and fails if any supporting unit is missed. |
| The first lecture of a course has no earlier banks for its review slots | **Empty review slots.** With no earlier bank loaded, review slots become extra current-lecture questions, filled first from supporting units. |
| A bank-wide 40% length-cue limit was noise on small banks, skipped two-tier questions, and was passed by padding distractors | **Per-question cue check** (see Integrity). A flagged item is fixed by rewriting the correct answer; lengthening distractors alone does not clear the flag in review. |
| Gate rows checked by the authoring model read like independent passes | **Who checked.** Every gate row states Script or Author. Only `qm.py` results on the files may say Pass; author judgments say Unverified until the blind check or a human confirms them. |
| Source issues were "resolved" with facts from the model's memory | **Fetched references.** A source issue that relies on an outside fact needs a fetched, cited page in `externalRefs`. A person accepts each resolution before the issue counts as resolved. |
| The analyzer read some diagram slides as text only and missed two units | **Every slide as an image.** Page accounting records `inspection` per page; a page inspected only as extracted text is unverified. |

A seventh rule covers previews: an **author preview** of a blocked bank may be published for the author and reviewers only, with a visible draft banner. It is never shared with students until the gate passes.

## Open questions

- [ ] Where will the quiz app be hosted: a GitHub Pages site, a Claude artifact, or files students open locally?
- [ ] Should Quiz me (`quiz-me`, formerly `adaptive-question-bank`) adopt BankQuestion v4, so both plugins share one question format?
- [ ] Which model or setup runs the blind check by default in Codex: a sub-agent, a second session, or a different model?
- [ ] Should supporting units be guaranteed within 3 attempts, or a different number?
