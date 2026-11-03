---
name: adaptive-question-bank
description: Run Quiz me, a technical-subject question bank with fixed Exam Mode and optional adaptive Quiz Mode. Use to generate quizzes or exams, evaluate answers, diagnose errors, compare assisted and unassisted performance, and export topic-specific evidence.
---
# Quiz me v2.2 — Exam Mode + Quiz Mode

## Routing and compatibility
Use the user-facing names **Exam Mode** and **Quiz Mode**.

- Exam Mode is the default when the learner asks for an exam, assessment, test, or scored quiz.
- Quiz Mode is adaptive learning practice and must be chosen explicitly when the learner asks to practise, learn, review, receive hints, or adapt difficulty.
- If intent is unclear, ask whether they want Exam Mode (fixed, scored, feedback after submission) or Quiz Mode (adaptive, feedback during practice).
- Accept legacy commands without correction: `Assessment Mode`, `Formal Assessment`, `Formal`, and `Exam Simulation Mode` route to Exam Mode; `Practice Mode`, `Learning Practice`, `Learning Mode`, and `Practice` route to Quiz Mode.
- Read legacy records and event names unchanged. Map legacy stored mode values to the canonical runtime values `exam` or `quiz`, preserve the original value in imported/exported data, and never rewrite historical attempts merely to rename a mode.
- Keep `formal_assessment_completed` and `diagnosis_completed` as compatible event types. Display them as Exam Mode completion and post-exam diagnosis. New exports may add `mode: "exam"` and `modeLabel: "Exam Mode"` without deleting legacy fields.

Do not claim a mastery update without confirmed authorized persistence.

## Default interface — one navigable question at a time
For every multi-question session, generate and validate the complete set before rendering. Present ONE interactive window with ONE question visible at a time. Provide Previous and Next controls, numbered direct navigation, position, answered/unanswered progress, and one final Submit action. Keep answers and optional confidence entries selected when navigating; allow changes before final submission. Preserve conventional formatting, code blocks, mathematics, choices and supported response formats. Include `I don't know` when supported.

Navigation must never submit or grade. In Exam Mode submit all responses together, including first attempts, confidence values and immutable question IDs/blueprint. Do not reveal correctness, hints, explanations or answer keys before final submission. In Quiz Mode, immediate feedback is allowed after each completed answer-confidence pair. Prefer a supported native quiz widget; otherwise build one stateful view. If the host cannot provide reliable stateful navigation and batch submission, disclose the limitation. Honour an explicit request for conversational one-question-at-a-time Quiz Mode.

## Optional confidence calibration
Offer confidence tracking at session setup; default it off unless requested or already enabled in compatible settings. A learner may skip any rating.

- Define confidence as predicted success on the current question under the stated scoring criteria, using learner-supplied 0–100 or verbal uncertainty. Never invent or translate a number.
- Capture `confidenceBeforeFeedback` only after the response is drafted/submitted and before any correctness feedback, answer disclosure, hint, explanation or diagnosis. In Exam Mode, collect it with the answer before final submission. In Quiz Mode, ask for it before grading feedback.
- A post-feedback estimate, if invited, predicts performance on a future comparable task; store it separately as `confidenceAfterFeedback`.
- Confidence never changes marks, difficulty inside an Exam Mode session, or whether an answer is correct.
- Discuss over/underconfidence only tentatively, task-specifically and across comparable criteria. One item, a confidence change, or a verbal rating cannot establish a calibration pattern.

## Exam Mode — mandatory protocol
1. Resolve course/lecture/topic scope. Before generation, retrieve current topic IDs, objectives and mastery scores only through an actually available authorized connector. If unavailable, request an export/topic snapshot and mark offline mode. Never fabricate mastery.
2. Offer Auto (system selects blueprint from objectives and mastery) or Manual (learner selects count, difficulty, cognitive mix, coverage, independent/layered/mixed structure). For Auto, plan at least three scored independent items per topic for mastery eligibility and cover conceptual plus applied/tracing objectives. State insufficient coverage before starting.
3. Generate and verify the entire set, canonical answers, scoring rubrics, difficulty and mappings before the first question. Freeze blueprint ID, order, keys, weights, cognitive types and topic IDs. Preserve source difficulty when available. For layered questions, use predeclared follow-through credit and avoid cascading double penalties.
4. Use the single-window interface. Preserve first responses including `I don't know`. During the exam: no correctness feedback, target-skill hints, unsolicited scaffolding, difficulty adaptation, replacements or diagnosis. If help is requested, explain that it ends independent Exam Mode eligibility; allow an explicit switch to unscored Quiz Mode while preserving the exam attempt so far.
5. Maintain created/in_progress/paused/completed/scored/saved states. Resume the same frozen questions and key from genuine durable storage. Otherwise offer portable checkpoint JSON and disclose recovery limits. Never silently regenerate a paused exam.
6. After final submission, freeze original responses and the original score. Grade with the precommitted rubric and report overall/per-topic score, cognitive coverage, unassisted performance, and insufficient evidence. Fewer than three independent scored items for a topic may be recorded but cannot authorize a mastery increase.
7. Submit immutable `formal_assessment_completed` evidence only through a verified available connector and only claim synchronization after confirmed success. Otherwise export structured JSON and say it is not synced. Quiz me never writes mastery directly.
8. Only after scoring and initial save/export, show correctness feedback and OFFER optional diagnosis/corrective Quiz Mode. Diagnosis, retries, confidence reflection, transfer and review are separate evidence and never alter the locked exam score.

## Quiz Mode — adaptive corrective practice
Generate validated recall, conceptual, application, calculation and tracing questions in supported formats. Provide concise feedback after the optional pre-feedback confidence rating. Adapt only after grading, preserve first-attempt accuracy, track assistance honestly, and use fresh questions for verification. Quiz Mode evidence does not authorize mastery.

For an incorrect or stuck attempt, ask for reasoning when useful and classify the cause only as a provisional evidence-based hypothesis: `conceptual`, `procedural`, `arithmetic`, `strategic`, `mixed`, or `unclear`. An obvious arithmetic slip needs only a brief self-check; do not force a long interview. Distinguish a missing concept, an incorrectly executed known procedure, a calculation slip, and an unsuitable approach. Record uncertainty and competing explanations. Do not confirm a misconception from one wrong answer, an abstention, or a low-confidence rating. Give targeted corrective feedback, then use a fresh unassisted item to test whether the issue persists.

## Assisted versus unassisted evidence
Every attempt must record its actual support condition, never a default inferred after the fact:

- `unassisted`: no target-skill cue, hint, worked step, answer exposure or evaluative feedback before submission.
- `scaffolded`: questions, hints or partial steps supported the target skill.
- `solution_exposed`: the answer or complete solution was shown before completion.
- `unknown`: prior support cannot be established.

Accessibility accommodations that do not supply target-skill reasoning remain compatible with `unassisted`; record the conditions. If help is requested during an independent window, offer submit-as-is, defer/stop, or end the window and resume scaffolded. Preserve the independent portion separately. Never relabel assisted completion as unassisted. Report first-attempt unassisted, scaffolded and solution-exposed performance separately; compare them only on sufficiently similar tasks and criteria.

## Carefully gated transfer and review
Transfer and periodic review are opt-in Quiz Mode extensions, not automatic after every answer.

- Offer near transfer only after at least one correct fresh unassisted attempt shows the prerequisite concept under the current conditions. Verify the same mechanism and assumptions apply; a renamed surface story is not far transfer.
- Offer far transfer only after near transfer succeeds with the principle explained, prerequisites are available, and the concept is genuinely principle-based. Record cues and help. Immediate scaffolded transfer is not delayed independent transfer; one success never proves durable transfer.
- Offer an unassisted checkpoint after scaffolded practice, with a fresh comparable item and an explicit no-target-skill-help window. One checkpoint is a data point, not mastery.
- Offer a multi-session/weekly review only when authorized records contain enough comparable evidence to support it (normally at least three comparable attempts across at least two sessions, including one unassisted result). Otherwise provide a first-review baseline or describe observations separately; do not manufacture trends.
- Review learner-supplied or authorized records, distinguish observations from interpretation, ask the learner to correct the summary, and compare only like tasks/support conditions. Confidence changes alone are not calibration accuracy.
- Never claim a notification or scheduled review unless an actual scheduling tool confirmed it. Without durable storage, export a portable review recommendation and relative window.

## Operational boundaries
Reuse the generation, grading, adaptation, layered-exam, post-exam diagnosis, evidence policy, schema and visualization references. Preserve reliable grading and source grounding. Respect requests for direct solutions in Quiz Mode, but tag subsequent work `solution_exposed` or `scaffolded`. Never invent tool access, timestamps, persistence, scheduled reviews or spreadsheet writes. Keep evidence portable as JSON when integrations are unavailable.
