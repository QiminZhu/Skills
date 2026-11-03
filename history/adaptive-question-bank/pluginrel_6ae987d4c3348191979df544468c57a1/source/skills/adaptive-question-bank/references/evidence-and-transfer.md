# Learning evidence, calibration and transfer policy (v2.2.0)

## Mode boundary

`exam` is fixed, scored and feedback-locked until final submission. `quiz` is adaptive practice. Accept legacy labels and stored values, but render **Exam Mode** and **Quiz Mode**. Preserve legacy event names and raw imported values for round-trip compatibility.

No calibration, diagnosis, remediation, transfer or review activity may change a locked Exam Mode score, response, key, weight, order or blueprint. Post-exam work creates linked evidence records with new attempt IDs.

## Confidence lifecycle

Confidence is optional self-report, not a grade or probability estimate produced by the system.

1. Define the current question's success criteria.
2. Capture the learner's answer.
3. If enabled, invite `confidenceBeforeFeedback` (0–100, verbal, or skipped).
4. Only then provide correctness feedback or reveal the key.
5. Optionally capture `confidenceAfterFeedback` as predicted success on a future comparable task.

Never backfill a missing value, convert words to a number, or infer calibration from a confidence change. Compare prospective confidence with actual performance only when task, rubric, difficulty and support conditions are sufficiently comparable. Describe a single mismatch as tentative and task-specific; require repeated comparable pairs before describing a pattern.

## Support conditions

Use one explicit value on every attempt:

- `unassisted`: no target-skill hint, cue, worked step, answer exposure or evaluative feedback before submission.
- `scaffolded`: the learner received target-skill questions, hints, partial steps, corrective prompts or a warm start.
- `solution_exposed`: a complete answer or solution was available before the attempt finished.
- `unknown`: support history cannot be established.

Record `supportEvents[]` in order, such as `confidence_prompt`, `clarification_non_target`, `hint`, `worked_step`, `answer_reveal`, `feedback`, and `mode_switch`. Accessibility accommodations do not make an attempt assisted unless they supply target-skill reasoning; record `accessConditions[]` separately.

An independent window closes when target-skill help is accepted. Save submitted independent work separately, then create a scaffolded continuation. A correct scaffolded or solution-exposed response is useful practice but not independent evidence.

## Error diagnosis contract

Record a learner-facing `errorCategory` only when supported by response/reasoning evidence:

- `conceptual`: the governing idea, relationship or interpretation is missing or false.
- `procedural`: the learner knows the relevant concept but executes a method or sequence incorrectly.
- `arithmetic`: the setup and method are sound but a calculation slip changes the result.
- `strategic`: the selected approach is unsuitable or inefficient for the task features.
- `mixed`: evidence supports more than one interacting category.
- `unclear`: evidence is insufficient or competing explanations remain.

Keep `diagnosticStatus = unclassified|suspected|supported|resolved`, `diagnosticConfidence = low|medium|high` as a qualitative judgment about the classification evidence, and `alternativeHypotheses[]`. Do not use confidence as a numeric probability. Ask for reasoning only when it can disambiguate. For a clear arithmetic slip, use one brief self-check. For `I don't know` or blank, record an abstention/possible knowledge gap rather than inventing a method error.

Map legacy mechanisms without destroying them: `conceptual_misconception -> conceptual`, `procedural_error -> procedural`, `arithmetic_slip -> arithmetic`, and strategy-related records to `strategic`; preserve `legacyErrorMechanism` on import/export. `possible_typo`, `knowledge_gap`, `guess`, and `cascading_error` remain mechanisms/evidence notes and may map to `unclear` until supported.

## Unassisted checkpoint gate

Offer after scaffolded Quiz Mode work when the learner wants to test independence. Use a fresh, comparable item and agree the no-target-skill-help window before starting. The learner may submit, defer, stop, or resume with support. Record one result as one current-performance observation; do not claim durable learning.

Compare scaffolded and unassisted results only when concept, criteria and difficulty are comparable. Otherwise report the observations separately.

## Transfer gates

Near transfer requires all of:

- one correct fresh unassisted attempt on the concept;
- verified prerequisites for the proposed task;
- a validated question whose underlying mechanism matches the original;
- learner opt-in.

Far transfer additionally requires successful near transfer with the learner able to name or justify the principle, a genuinely different context, and explicit verification that the mechanism and assumptions apply. Do not call a relabelled problem far transfer. Record introduction cues and all bridge help. Immediate prompted success is `scaffolded` transfer, not independent delayed transfer.

Transfer status is `passed|failed|skipped`; describe mixed near/far results in prose. A pass is limited to the recorded tasks and support conditions.

## Multi-session review gate

Use a trend review only with authorized or learner-supplied evidence that normally includes:

- at least three comparable attempts;
- at least two distinct sessions or dates when genuinely known;
- at least one unassisted result;
- enough rubric/difficulty/support metadata to compare like with like.

If the gate is not met, offer baseline goal-setting or a qualitative summary labelled as recollection. Present the minimal evidence first and ask the learner to correct it before interpretation. Do not infer calibration from pre/post confidence change, causes from correlation, or persistence from absent records.

Review scheduling is a recommendation unless an actual tool confirms a schedule. Without durable storage, export a relative window such as `next day` and state that no notification was created.

## Performance summaries

Keep separate aggregates for `unassisted`, `scaffolded`, `solution_exposed`, and `unknown`. Use first-attempt results for independent performance. Never combine these into a single mastery-like percentage without displaying the support mix and explaining the limitation. Quiz Mode evidence may guide practice selection but cannot authorize mastery.
