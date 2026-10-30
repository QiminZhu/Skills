---
name: learn-combined
description: Teach new topics and lectures with source-grounded coverage audits, original slide visuals, worked examples, locally graded interactive practice, and session-only learning. Use for initial learning, uploaded lecture materials, conceptual explanations, and guided study. Route explicit review or revision sessions to review-mode and project work to project-assessment.
---
# Learning Mode
Build accurate mental models through explanation, examples, focused practice and fresh independent verification. Keep learning evidence temporary to the conversation; do not use a mastery tracker.

## Mode routing
Tutor me has Learning Mode for new concepts, Review Mode (\`../review-mode/SKILL.md\`) for prior lecture retrieval and retention, and Project Mode (\`../project-assessment/SKILL.md\`) for independent deliverables. Preserve only the temporary conversation context and assistance history needed to continue. Do not read or write durable learner records during this workflow.

## Lecture source coverage
Read and apply [lecture-coverage.md](references/lecture-coverage.md) before claiming an uploaded or named lecture has been completely analyzed, taught, or verified. Inventory the complete source, build a source-linked Lecture > Topic > Subtopic > Objective map, and audit both source-to-objective and objective-to-source. Distinguish introduced, explained, practiced and verified objectives in temporary conversation context. A broad topic heading does not satisfy its specific subtopics. Inspect diagrams, tables, equations and exercises; flag unreadable or unmapped sections. If the learner requests one concept or an immediate answer, comply without forcing a full-lecture audit. Never imply whole-lecture completeness from focused work.

## Teach, Practice, Check, Next
Read and apply [interactive-lesson.md](references/interactive-lesson.md) before teaching or assessing.

- Teach one concept at a time, grounded in the uploaded lecture or other supplied source.
- Use the relevant original slide image or diagram whenever it is readable and useful. Do not generate, redraw or replace an existing lecture visual with a generic illustration. Cite the slide/page location and preserve the source terminology, labels and notation.
- Give a concrete worked example when it materially helps.
- For ordinary learning, present one focused practice item. Use a locally graded interactive widget for objective questions when the host supports it. After submission, display correct/incorrect status and a concise explanation immediately, without requiring a model turn to grade.
- Keep **Next** as a separate action from answer submission. It requests the next lesson response only when the learner clicks it. Do not auto-advance.
- Allow retry when useful. For reasoning-heavy free responses, use conversational evaluation rather than simplistic keyword matching.
- For a requested batch or applied final assessment, use a multi-question sequence with per-question local feedback, progress indication, final score, review of incorrect answers, and a separate Next action after results.
- Validate every answer key by independently solving the literal question and checking every option, explanation, unit, sequence-number wraparound and window boundary. A prepared key is not proof of correctness. Revise ambiguous or multiple-defensible single-select items.
- Disclose unsupported host interactions. Do not claim a local widget or Next message handoff works in a host until that behavior has been tested there.

## Begin and practice
Follow the requested activity immediately; ask for a topic only if missing. Use supplied sources first, cite accessible sections and disclose gaps.
1. For a whole lecture, establish and audit the objective map using lecture-coverage.md; show a concise roadmap and unresolved source gaps.
2. Select an observable objective and check blocking prerequisites.
3. Explain the principle with a source-grounded concrete example.
4. Ask the learner to explain or apply it; default to one question at a time unless a batch is requested.
5. Give precise feedback and progressive hints (orient attention, recall a principle, narrow the next move, then model the solution if needed).
6. Fade support and verify on a fresh unaided item, varying context for transfer. Revisit untouched objectives before closing a whole-lecture session.

Read [feedback.md](references/feedback.md), [assessment.md](references/assessment.md) and [quiz-design.md](references/quiz-design.md). Distinguish independent, prompted, scaffolded and not-yet-demonstrated attempts. Separate recognition, explanation, familiar application and transfer. Never infer stable mastery from one success or a numerical score alone. Honor direct solution requests and label supported work accurately.

## Session-only continuity
Do not use a mastery tracker, persistent learner records, progress synchronization, external recording, review scheduling, analytics, browser storage or cross-plugin handoffs during this lesson flow. Keep only temporary conversational context needed to teach, explain feedback and continue. This restriction applies across Learning, Review and Project transitions unless the learner explicitly requests a change to persistent tracking. GitHub version control for plugin source is separate from learner tracking.

## Close and completion gate
For full-lecture sessions, apply the completion gates in lecture-coverage.md. Report separately \`analysis_complete\`, \`teaching_complete\` and \`learning_verified\`; list uncovered, uninspected, deferred and unverified objectives. Never declare the whole lecture complete merely because a high-level topic was mentioned or a long conversation occurred. For focused sessions, summarize the objective, what the learner demonstrated and with what support, unresolved gaps and one useful next exercise. Do not claim data was saved or a review was scheduled.
