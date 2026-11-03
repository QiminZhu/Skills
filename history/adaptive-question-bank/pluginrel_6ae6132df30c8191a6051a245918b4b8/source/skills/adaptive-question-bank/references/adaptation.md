# Adaptive engine v1.0.0

## Candidate eligibility
Filter out invalid questions, unsupported prerequisite concepts, and recently repeated identical questions. Prefer due review and misconception-remediation candidates; fall back to a fresh prerequisite question if none eligible.

## Priority score
Rank eligible questions with `P = 0.40*M + 0.30*C + 0.20*R + 0.10*D`, where `M=1-masteryScore`, `C` is active-misconception relevance, `R` is due-review urgency, and `D` is suitability of difficulty, each normalized 0..1. Weights are heuristics, not learned or validated parameters. Avoid letting a high score override unmet prerequisites.

## Difficulty
- Mastery <0.40: easy, prerequisite and targeted remediation.
- 0.40 <= mastery <0.75: medium, independent application/tracing.
- Mastery >=0.75: hard/transfer questions, unless misconception evidence contradicts apparent mastery.

## Update
For independent graded attempts, `newMastery = 0.8*oldMastery + 0.2*(score/maxScore)`. For assisted attempts, use a smaller weight such as 0.05 or keep mastery unchanged if solution was shown. Initialize uncertain concepts conservatively; explain these are heuristic scores, not calibrated probabilities.

## Misconception state machine
- One diagnostic error -> `suspected`.
- Repeat diagnostic error on a distinct question OR clear reasoning confirming the false belief -> `confirmed`.
- Targeted practice underway -> `remediating`.
- At least two independent correct attempts with varied examples and no recurring error -> `resolved`, but keep history.
Do not equate every wrong answer with a misconception; calculation slips and ambiguous questions require separate handling.

## Review schedule
After initial error, give feedback and a related new item. After first independent success, give a varied item. After two independent successes, move from active remediation to next-day review; successful reviews extend to 3 days, then 7 days. Failure returns to remediation with a shorter interval. These intervals are configurable heuristics. If no reliable clock/date is available, express relative review windows rather than invent timestamps. Never claim to have scheduled notifications.

## Session selection loop
`eligible = validate_and_filter(question_pool)`; `due = due_reviews(states)`; `weak = weak_concepts(states)`; `rank(eligible, priority)`; choose highest relevant candidate with novelty; present; grade; record attempt; update mastery/misconception; repeat. When pool exhausted, generate and verify a new question or tell learner none is currently available.
