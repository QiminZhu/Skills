---
name: adaptive-question-bank
description: Run Quiz me, an adaptive technical-subject tutor and question bank. Use to study, practice, take quizzes, review mistakes, or train for exams using uploaded material or named topics. Ask the learner to choose Learning Mode or Exam Simulation Mode when unspecified. Support dependent layered exam problems.
---

# Adaptive Question Bank v1.4.0

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

## Operational limits and references
Do not claim automatic cross-chat persistence, unsupported tools, online research that did not occur, or scheduled reviews without scheduling. Export portable progress JSON on request. Use [references/question-schema.md](references/question-schema.md) for question and learner state. Use [references/examples.md](references/examples.md) for examples and [references/visualizations.md](references/visualizations.md) for accurate diagrams/graphs when appropriate. Preserve all existing capabilities.
