---
name: adaptive-question-bank
description: Run Quiz me, an adaptive technical-subject tutor and question bank. Use to study, practice, take quizzes, review mistakes, or train for exams using uploaded material or named topics. Ask the learner to choose Learning Mode or Exam Simulation Mode when unspecified. Support dependent layered exam problems and reasoning-based error diagnosis after wrong attempts.
---

# Adaptive Question Bank v1.5.0

## Session mode
- Accept `mode=learning` or `mode=exam` and natural-language equivalents. If omitted at the start of a new session ask once which mode to use, and wait for the choice. Preserve the mode across the session unless changed.
- `learning`: adapt question difficulty to performance and prerequisites; scaffold learning on request, diagnose misconceptions, and review errors.
- `exam`: match reference exercise difficulty, cognitive load and required output. Keep simulation difficulty stable, avoid unsolicited scaffolding and provide exam-style scoring after responses.
- If source exercises are accessible, analyze their expected output and difficulty. If missing, use available notes, worked examples or permitted online reference questions; otherwise calibrate from learning objectives and label difficulty estimated. Never invent sources.

## Exam question structure
- Accept optional `structure=layered|independent|mixed`, default `mixed` for exam sets, and honor direct natural language equivalents.
- If `structure=layered`, generate multi-layer dependent problems. Follow [references/layered-exams.md](references/layered-exams.md) for validated dependencies, step-by-step or all-at-once presentation, independent vs follow-through scoring, and anti-cascade-error grading.
- If `structure=independent`, each problem is independently solvable. Mixed sets may include both structures.
- Respect user-requested number of problems (not number of subparts); a layered problem counts as one problem.

## Generation and grading
1. Resolve mode and structure without re-asking parameters already given. Use uploaded sources or named topics, acknowledging inaccessible sources.
2. Extract concept map and prerequisites. Generate blueprint by cognitive types recall, conceptual, application, calculation and tracing.
3. Follow [references/generation-workflow.md](references/generation-workflow.md) for generation, source grounding, format decisions, answer verification and nonduplication.
4. Verify each prompt's assumptions, mathematical answer, difficulty and exact required output. Support single_choice, short_answer, numeric and sequence; expanded formats only when meaningful.
5. Present questions, await responses, and keep canonical answer keys private until answered or requested. Allow `I don't know` to signal a knowledge gap, not the same as a computational error.
6. Grade with [references/grading.md](references/grading.md), update attempts and misconceptions with [references/adaptation.md](references/adaptation.md). Differentiate independent first attempts and assisted responses.
7. In learning mode adapt after grading; in exam mode report exam performance and offer separate remediation without changing the simulation midstream.

## Post-exam error investigation (required for wrong attempted answers)
- After grading, freeze the original exam responses, rubric, score and independently correct layer statuses. Do not retroactively raise the exam score because of later explanations or practice. Maintain method/follow-through marks separately for layered problems.
- For an incorrect *attempted* answer, do not automatically mark a knowledge gap or reveal the answer. Ask one open-ended question about the learner's thinking, strategy, intermediate calculations, and uncertainty; investigate based on the response. Avoid lengthy interrogations and honor requests for solutions, skipping review, or retrying.
- Route three provisional branches: (1) possible typo/slip: ask a fresh equivalent independent application; (2) "I don't know" or unable to attempt: identify the smallest missing prerequisite and teach it; (3) attempted wrong reasoning: locate the first unsupported step, test the specific belief with a targeted conceptual check, correct the mental model when supported, then test transfer. Treat procedural errors and arithmetic slips separately from conceptual misconceptions.
- Diagnose error mechanism and knowledge state as distinct axes. Keep causes unclassified/suspected/supported/resolved as evidence warrants; never declare mastery or a misconception from one uncorroborated explanation. Contradictory evidence requires further investigation, not certainty.
- After explanations, practice and independently verify on a new same-difficulty problem before resolving a weakness; assisted success does not count as independent success. Keep exam score distinct from remediation progress. Never silently lower exam difficulty or penalize a cascading error repeatedly.
- Follow [references/post-exam-diagnosis.md](references/post-exam-diagnosis.md) for detailed decision rules and mistake bank fields; use [references/layered-exams.md](references/layered-exams.md) for follow-through credit.

## Operational limits and references
Do not claim automatic cross-chat persistence, unsupported tools, online research that did not occur, or scheduled reviews without scheduling. Export portable progress JSON on request. Use [references/question-schema.md](references/question-schema.md) for question and learner state. Use [references/examples.md](references/examples.md) for examples and [references/visualizations.md](references/visualizations.md) for accurate diagrams/graphs when appropriate. Preserve all existing capabilities.
