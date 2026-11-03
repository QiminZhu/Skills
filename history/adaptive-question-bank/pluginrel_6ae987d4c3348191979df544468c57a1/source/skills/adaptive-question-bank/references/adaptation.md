# Quiz Mode adaptive engine v2.2.0

Run this engine only in Quiz Mode or after the learner explicitly switches a scored Exam Mode attempt into unscored Quiz Mode. Never adapt a frozen Exam Mode blueprint, order, difficulty, key or weights.

## Candidate eligibility
Filter out invalid questions, unsupported prerequisite concepts, and recently repeated identical questions. Prefer due review and misconception-remediation candidates; fall back to a fresh prerequisite question if none eligible.

## Priority score
Rank eligible questions with `P = 0.40*M + 0.30*C + 0.20*R + 0.10*D`, where `M=1-masteryScore`, `C` is active-misconception relevance, `R` is due-review urgency, and `D` is suitability of difficulty, each normalized 0..1. Weights are heuristics, not learned or validated parameters. Avoid letting a high score override unmet prerequisites.

## Difficulty
- Mastery <0.40: easy, prerequisite and targeted remediation.
- 0.40 <= mastery <0.75: medium, independent application/tracing.
- Mastery >=0.75: hard/transfer questions, unless misconception evidence contradicts apparent mastery.

## Update
For provisional Quiz Mode selection only, an independent graded attempt may use `newMastery = 0.8*oldMastery + 0.2*(score/maxScore)`. Keep authorized mastery unchanged for scaffolded, solution-exposed or unknown attempts. These values are heuristic selection state, not calibrated probabilities or permission to update an external mastery record. Keep aggregates separate by support condition.

## Misconception state machine
- One diagnostic error -> `suspected`.
- Repeat diagnostic error on a distinct question OR clear reasoning confirming the false belief -> `confirmed`.
- Targeted practice underway -> `remediating`.
- At least two independent correct attempts with varied examples and no recurring error -> `resolved`, but keep history.
Do not equate every wrong answer with a misconception; calculation slips and ambiguous questions require separate handling.

## Review schedule
After an initial error, diagnose provisionally and give a related new item. After the first fresh unassisted success, a near-transfer item may be offered; far transfer requires successful near transfer with the principle explained and verified prerequisites. Two varied independent successes may justify a next-day review recommendation; successful comparable reviews may extend to 3 days, then 7 days. These are configurable heuristics, not automatic schedules. If no reliable clock, persistence, consent or scheduling tool is available, express a relative window and never claim a notification exists.

## Session selection loop
`eligible = validate_and_filter(question_pool)`; `due = authorized_due_reviews(states)`; `weak = weak_concepts(states)`; `rank(eligible, priority)`; choose highest relevant candidate with novelty; present; capture optional confidence before feedback; grade; record response and actual support condition; update provisional Quiz Mode state; repeat. When the pool is exhausted, generate and verify a new question or tell the learner none is currently available.

## Review and transfer gate

Do not infer a longitudinal trend without at least three comparable attempts across at least two sessions including one unassisted result. Otherwise report observations separately or offer baseline goal-setting. Apply the complete gates in `evidence-and-transfer.md`.
