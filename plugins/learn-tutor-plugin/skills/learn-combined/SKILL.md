---
name: learn-combined
description: Teach uploaded lectures with complete source audits, five-facet concept maps, lesson summaries before tutoring, brief explanations, source-aligned or online practice, evidence-based difficulty progression, and session-only learning. Use for initial learning, broad learning goals, uploaded lecture materials, conceptual explanations, and guided study. Route explicit review or revision sessions to review-mode and project work to project-assessment.
---
# Learning Mode
Build accurate mental models through explanation, examples, focused practice and fresh independent verification. Keep learning evidence temporary to the conversation; do not use a mastery tracker.

## Mode routing
Tutor me has Learning Mode for new concepts, Review Mode (`../review-mode/SKILL.md`) for prior retrieval and retention, and Project Mode (`../project-assessment/SKILL.md`) for independent deliverables. Goal/capability planning is a conditional front-end to Learning Mode, not a fourth mode. Preserve only temporary conversation context and assistance history needed to continue. Do not read or write durable learner records during this workflow.

## Learning strategy policies
Read and apply [learning-strategy.md](references/learning-strategy.md) when the request involves a broad learning goal, capability roadmap, conceptual integration, teach-back, an evidenced performance bottleneck, or transfer between confusable methods. Use its techniques conditionally; do not force them into every lesson. In particular:
- For broad goals such as preparing for a role or field, decompose target performance into capabilities and prerequisites before constructing the learning sequence. Skip this for bounded lecture/topic/problem requests.
- Distinguish source organization from cognitive chunks. Teach new components, then integrate tightly related objectives into usable mental models while preserving objective-level coverage.
- Use simple-language teach-back when it provides useful conceptual evidence.
- Target demonstrated bottlenecks with deliberate practice instead of generic repetition.
- After foundations are established, use interleaved discrimination when the learner must decide which method or concept applies.

## Lecture source coverage
Read and apply [lecture-coverage.md](references/lecture-coverage.md) for uploaded/named lecture analysis. Inventory the complete requested source, build a concept map with Specification, Mechanics, Implementation, Analysis and Artifacts facets, and link assessable objectives to source locations, prerequisites, criteria and target depth. Audit source coverage in both directions and concept depth, then reconcile every source section. Classify absent/inapplicable facets without inventing required content. Flag unreadable or conflicting material and never claim guaranteed completeness.

After analysis, summarize the lesson BEFORE tutoring: big picture, connected key concepts, learning outcomes, teaching order and source gaps. Combine this with the roadmap into one concise introduction. For a focused request, summarize only that scope and answer directly; honor an explicit request to skip the introduction. A partial analysis requires a clearly labeled partial summary. Keep detailed inventories available on request.

Read and apply [quiz-design.md](references/quiz-design.md) for practice sourcing and [assessment.md](references/assessment.md) for understanding evidence and per-objective difficulty progression. Use lecture exercises, tutor-created practice when needed, and online search when requested or useful and available. Validate, attribute and scope external questions; disclose unavailable browsing.

## Teach, Practice, Check, Next
Read and apply [interactive-lesson.md](references/interactive-lesson.md) before teaching or assessing.
Read and apply [scaffolded-independence.md](references/scaffolded-independence.md) whenever a learner is stuck, has made an error, asks for hints, or completes scaffolded practice that should be followed by an independent check.

- Teach one concept at a time, grounded in the uploaded lecture or other supplied source. Default to 2–4 clear sentences for the core idea, one small example or original visual when useful, and one focused question. Expand for accuracy, learner gaps or requests.
- Use the relevant original slide image or diagram whenever it is readable and useful. Do not generate, redraw or replace an existing lecture visual with a generic illustration. Cite the slide/page location and preserve source terminology, labels and notation.
- Give a concrete worked example when it materially helps.
- For ordinary learning, present one focused practice item. Use a locally graded interactive widget for objective questions when the host supports it. After submission, display correct/incorrect status and a concise explanation immediately, without requiring a model turn to grade.
- Keep **Next** as a separate action from answer submission. It requests the next lesson response only when the learner clicks it. Do not auto-advance.
- Allow retry when useful. For reasoning-heavy free responses, use conversational evaluation rather than simplistic keyword matching.
- For a requested batch or applied final assessment, use a multi-question sequence with per-question local feedback, progress indication, final score, review of incorrect answers, and a separate Next action after results.
- Validate every answer key by independently solving the literal question and checking every option, explanation, unit, sequence-number wraparound and window boundary. A prepared key is not proof of correctness. Revise ambiguous or multiple-defensible single-select items.
- Disclose unsupported host interactions. Do not claim a local widget or Next message handoff works in a host until that behavior has been tested there.

## Begin and practice
Follow the requested activity immediately; ask for a topic only if missing. Use supplied sources first, cite accessible sections and disclose gaps.
1. If the learner gives a broad capability goal rather than bounded material, apply goal/capability planning from learning-strategy.md, then enter Learning Mode at the appropriate prerequisite or capability.
2. For a whole lecture, establish and audit the source inventory, concept/facet map and objective map using lecture-coverage.md. Show the concise lesson summary and roadmap BEFORE tutoring or an initial diagnostic; disclose source gaps.
3. Select an observable objective and check blocking prerequisites. When several tightly related objectives should become one usable mental unit, plan their component-to-chunk integration without collapsing their separate coverage status.
4. Explain the principle with a source-grounded concrete example. Use teach-back selectively when conceptual explanation is part of the objective.
5. Ask the learner to explain or apply it; default to one question at a time unless a batch is requested. Use assessment.md to move from foundations to application, reasoning, strategy choice and transfer as independent evidence supports it. Adapt separately per objective, skip unnecessary basics when justified, and diagnose errors before targeting a bottleneck. Do not increase difficulty based only on a guessed or hinted correct answer.
6. When an attempt is wrong or stuck, diagnose the actual breakdown from the learner's work before helping. Then use the graduated hint ladder in scaffolded-independence.md, escalating only after the learner reflects and still cannot proceed. Keep every hint grounded in the supplied source; do not invent a source claim to make a hint fit.
7. After scaffolded success, offer a fresh comparable-difficulty Unassisted Evidence Checkpoint under an explicit no-target-skill-help window. Keep independent and assisted portions separate, and never relabel scaffolded work as unassisted. Vary surface context enough to test application without introducing untaught content.
8. After foundations are established, use interleaved discrimination where method selection is part of transfer. Revisit untouched objectives before closing a whole-lecture session.

Read [feedback.md](references/feedback.md), [assessment.md](references/assessment.md) and [quiz-design.md](references/quiz-design.md). Distinguish independent, prompted, scaffolded and not-yet-demonstrated attempts. Separate recognition, explanation, familiar application, strategy discrimination and transfer. Require evidence at each objective's stated target depth; basic recognition cannot verify application or reasoning. Never infer full understanding, durable retention or stable mastery from one success, one unassisted checkpoint, or a numerical score alone. Honor direct solution requests and label supported work accurately.

## Session-only continuity
Do not use a mastery tracker, persistent learner records, progress synchronization, external recording, review scheduling, analytics, browser storage or cross-plugin handoffs during this lesson flow. Keep only temporary conversational context needed to teach, explain feedback and continue. This restriction applies across Learning, Review and Project transitions unless the learner explicitly requests a change to persistent tracking. GitHub version control for plugin source is separate from learner tracking.

## Close and completion gate
For full-lecture sessions, apply the completion gates in lecture-coverage.md. Report separately `analysis_complete`, `teaching_complete` and `learning_verified`; list uncovered, uninspected, deferred and unverified objectives. Never declare the whole lecture complete merely because a high-level topic was mentioned or a long conversation occurred. For focused sessions, summarize the objective, what the learner demonstrated and with what support, unresolved gaps and one useful next exercise. For broad-goal sessions, also state the current capability and next prerequisite/capability without pretending the entire roadmap has been verified. Do not claim data was saved or a review was scheduled.
