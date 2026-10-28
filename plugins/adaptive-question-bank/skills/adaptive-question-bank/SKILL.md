---
name: adaptive-question-bank
description: Run Quiz me, a technical-subject question bank with formal fixed assessments and optional adaptive learning practice. Use to generate quizzes, exams, evaluate answers, investigate errors after formal quizzes, and export topic-specific evidence.
---
# Quiz me v2.0 — Formal Assessment + Learning Practice

## Routing
Default to formal assessment when user requests a quiz or exam; preserve optional Learning Practice mode on explicit request. If intent unclear ask whether Formal (Auto/Manual) or Learning Practice. Do not claim a mastery update without confirmed authorized persistence.

## Formal assessment — mandatory protocol
1. Resolve course/lecture/topic scope. Before generating questions, retrieve current topic IDs, objectives and mastery scores using an actually available authorized Update it or Google Sheets connector. If unavailable, request an export or supplied topic snapshot and clearly mark offline mode. Do not fabricate mastery.
2. Offer Auto (system selects blueprint from objectives and mastery) or Manual (student selects count, difficulty, cognitive mix, topic coverage, independent/layered/mixed structure). For Auto, ensure >=3 scored items per topic for mastery eligibility and cover conceptual plus applied/tracing objectives. State topics with insufficient planned coverage before starting.
3. Generate and verify the entire question set, canonical answers, scoring rubric, difficulty and topic mapping BEFORE the first question. Freeze immutable blueprint ID, order, answer keys, weights, cognitive types and topic IDs. Match reference exercise difficulty where provided. For layered questions preserve follow-through credit and do not double-penalize cascades.
4. Present one question at a time by default, collect independent answers and preserve first attempt, including `I don't know`. During the formal quiz: NO correctness feedback, hints, unsolicited scaffolding, difficulty adaptation, replacement questions or diagnosis. On user request to reveal a solution or receive a hint, explain that this compromises formal assessment eligibility; allow explicit switch to unscored practice.
5. Maintain session states created/in_progress/paused/completed/scored/saved. On interruption, resume the SAME frozen questions and answer key from durable session storage when genuinely available. If storage unavailable, offer portable checkpoint JSON and disclose that automatic recovery is not guaranteed. Never regenerate a paused formal exam silently.
6. After all required responses, freeze the original score and attempts. Grade by precommitted rubric, report overall and per-topic score, cognitive coverage, independent performance, and insufficient evidence. For any topic with <3 independent scored items, record results but prohibit mastery increase.
7. Submit an immutable `formal_assessment_completed` event to Update it through a verified available tool; require confirmed successful write before claiming spreadsheet synchronization. If unavailable, export structured JSON and clearly report not synced. Only Update it determines advancement, including two distinct qualifying sessions for Nailed it; never write mastery directly from Quiz me.
8. After scoring and initial save/export, OFFER optional diagnosis. For wrong attempts ask for reasoning, distinguish slips, missing knowledge and misconceptions, reteach only now, and independently verify with fresh questions. Append separate `diagnosis_completed` evidence; never alter original exam score or use diagnosis to increase mastery.

## Learning Practice (preserved)
Adaptive question generation for recall, conceptual, application, calculation and tracing; single-choice, short answer, numeric, sequence, independent or layered problems. Give feedback and scaffolding when requested; adapt difficulty, track mistakes, and use fresh verification. Practice evidence is NOT mastery-authorizing. Preserve source grounding, validated answers and nonduplication. Never claim mastery from one success.

## Operational boundaries
Reuse the existing generation, grading, adaptation, layered exam, post-exam diagnosis, question schema and visualization references. Respect user requests for direct solutions in learning mode. Never invent tool access, scheduled reviews, cross-chat persistence or spreadsheet writes. Keep session evidence portable as JSON if integration unavailable.
