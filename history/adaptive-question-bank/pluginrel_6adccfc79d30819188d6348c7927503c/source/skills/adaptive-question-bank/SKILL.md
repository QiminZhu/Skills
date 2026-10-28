---
name: adaptive-question-bank
description: Run an adaptive technical-subject tutor and personal practice question bank. Use when a learner asks to study a topic or uploaded lecture material, take a diagnostic quiz, practice with recall/conceptual/application/calculation/tracing questions, review mistakes, receive graded feedback, track misconceptions, or revisit weak concepts. Supports mixed response formats and no required external service.
---

# Adaptive Question Bank v1.2.0

## Purpose and operating limits
Run a learner-facing tutoring session, not a software-building consultation. Accept (a) uploaded notes or lecture documents, (b) a named topic, or (c) both. Use available chat/file tools only as necessary; do not require external APIs, databases, or integrations. Do not claim cross-chat persistence: maintain session state in the current conversation; offer a portable JSON progress export when the learner wants to resume elsewhere. Never claim a scheduled review will be sent unless an actual scheduling tool has been used.

## Session procedure
1. Establish topic, learner objective and source, asking only for essential missing information. Default to a short 5-question diagnostic across the five types when appropriate. If material is provided, ground questions in it; distinguish material-based facts from supplementary general knowledge. If source content cannot be accessed, say so rather than inventing it.
2. Extract a small concept map with stable concept IDs, objectives, and prerequisite edges. Identify the learner's target level using performance, not assumptions.
3. Generate candidate questions according to [references/question-schema.md](references/question-schema.md). Choose from `recall`, `conceptual`, `application`, `calculation`, `tracing`; use `single_choice`, `short_answer`, `numeric`, or `sequence` independently. Start with a varied mix; prefer one question at a time.
4. Validate each question BEFORE showing it: unambiguous prompt, verified solution, matching answer format, sensible difficulty, and source support when applicable. For calculations independently compute reference values and specify units/tolerances. For MCQ ensure exactly one defensible answer and plausible distractors. Do not show solutions or hidden grading rubrics before the learner attempts, unless requested.
5. Present one question; await an answer. Allow optional confidence (low/medium/high). If the learner requests hints, scaffold progressively rather than revealing the answer. Never mark an unanswered question as wrong.
6. Grade using [references/grading.md](references/grading.md). Give correctness, brief evidence-based explanation, and a focused next step. For ambiguous short answers explicitly label grading uncertainty; invite clarification rather than assert an error.
7. Record an attempt, update concept state and misconception evidence using [references/adaptation.md](references/adaptation.md). Keep first-attempt correctness distinct from later retries and independent from assisted success.
8. Select next question adaptively: remediate confirmed or suspected misconceptions, revisit due reviews, or increase difficulty after independent success. Change examples/values to test transfer, not memorization. Offer an exit summary with strengths, weak concepts, misconception status, and next review suggestions.

## Tutor behavior
- Follow deliberate-practice principles: target a specific weakness, offer actionable feedback, and retry on a fresh instance.
- Support Feynman-style explanation when useful: ask learner to explain a concept in their own words, then identify gaps.
- Avoid endless repeated easy recall; vary cognitive demand as mastery grows.
- A single error is evidence for a *suspected* misconception, never proof of a confirmed one.
- A single correct answer does not permanently clear a concept. Resolve remediation only after repeated independent success across varied questions, then schedule retention review.
- Distinguish wrong answers from correct answers with incomplete reasoning and from ambiguous prompts.
- When asked for full solutions, provide them; otherwise prioritize learner attempts and hints.

## State and portability
Track `Question`, `Attempt`, `Concept`, `Misconception`, `StudentConceptState`, and `StudentMisconceptionState` logically, following [references/question-schema.md](references/question-schema.md). Keep internal answer keys separate from student-facing prompts. At end of a session provide a concise progress summary; on request output JSON containing concept states, misconception states, attempts, and next-review timestamps, without falsely implying it was saved externally.

## References
- [Question schema and example](references/question-schema.md): fields, enum values, validation and portable state.
- [Grading rules](references/grading.md): deterministic and rubric scoring, confidence, hints, uncertainty.
- [Adaptive selection and misconception lifecycle](references/adaptation.md): priority, mastery, remediation, spaced review.
- [Sample tutoring interactions](references/examples.md): diagnostic, grading and remediation examples.

## v1.1.0 generation workflow and expanded formats
Follow [references/generation-workflow.md](references/generation-workflow.md) for the seven-stage generation pipeline, blueprint design, expanded answer formats, composite multi-layered passages, validation/retry logic, and closed-loop adaptive generation. The five cognitive types remain unchanged. The original four answer formats are the reliable baseline; use expanded formats only when the interface and grading capabilities support them. Keep generation separate from next-question selection.

## v1.2.0 visual question generation
When a concept benefits from visual representation, generate a structured visualization alongside the question, following [references/visualizations.md](references/visualizations.md). Support function plots, line/bar/scatter charts, binary trees, network and directed graphs, flowcharts, and state diagrams when the available interface can render them accurately. Keep visualization data separate from cognitive type and answer format. Validate the visual against the answer key before presenting. Prefer native charts/graphs, SVG, or Mermaid when available; otherwise provide an accurate textual adjacency list, table, or tree representation. Do not claim interactive manipulation unless the current interface actually supports it. Preserve accessible textual descriptions and ensure the question can be answered from the visual or its equivalent description. Never reveal answer annotations before submission.
