# Question and learner state contracts (v2.2)

Use JSON-compatible records. These are logical schemas, not a claim that data is persisted to a database.

## Question
Required: `schemaVersion` (1), `id` (stable unique string), `conceptIds` (nonempty array), `cognitiveType` (`recall|conceptual|application|calculation|tracing`), `answerFormat` (`single_choice|short_answer|numeric|sequence`), `difficulty` (`easy|medium|hard`), `prompt`, `grading`, `explanation`, `status` (`draft|validated|rejected`). Optional: `options` (single-choice only), `misconceptionRules`, `source` (`type`, `documentId`, `locator`), `generation` (`origin`, `validationStatus`).

Grading: `method` (`exact_option|numeric_tolerance|exact_sequence|rubric`), `correctAnswer` (appropriate type), `maxScore` (>0), optional `rubric` and `tolerance` (`absolute`, `relative`). Never send grading fields to a learner before the answer.

```json
{
  "schemaVersion": 1,
  "id": "bst-tracing-001",
  "conceptIds": ["bst.inorder-traversal"],
  "cognitiveType": "tracing",
  "answerFormat": "sequence",
  "difficulty": "easy",
  "status": "validated",
  "prompt": "Give the inorder traversal of a BST with root 50, left child 30, and right child 70.",
  "grading": {"method": "exact_sequence", "correctAnswer": [30, 50, 70], "maxScore": 1},
  "explanation": "Inorder visits left, root, right.",
  "misconceptionRules": [{"id": "bst.preorder-confusion", "matchSequence": [50, 30, 70]}],
  "source": {"type": "topic", "documentId": null, "locator": null}
}
```

## Session and mode compatibility

- `Session`: `id`, `mode` (`exam|quiz`), `modeLabel` (`Exam Mode|Quiz Mode`), optional `legacyModeValue`, `state`, `blueprintId`, `questionIds[]`, `confidenceEnabled`, `createdAt` (known only), `lockedScore` (Exam Mode after scoring), and optional persistence/sync status.
- Import aliases: `assessment|formal|formal_assessment|exam_simulation -> exam`; `practice|learning|learning_practice|learning_mode -> quiz`. Preserve the raw legacy value rather than rewriting historical records.
- Compatible event types include `formal_assessment_completed` and `diagnosis_completed`. Event names are storage contracts, not required user-facing labels.

## Other entities
- `Concept`: `id`, `name`, `learningObjective`, `prerequisiteIds[]`.
- `Attempt`: `id`, `studentId` (may be local pseudonym), `sessionId`, `questionId`, `attemptNumber`, `response`, optional legacy `confidence`, `confidenceBeforeFeedback` and `confidenceAfterFeedback` (each learner-supplied number/string/null plus capture timing), `supportCondition` (`unassisted|scaffolded|solution_exposed|unknown`), `supportEvents[]`, `accessConditions[]`, `hintsUsed`, `answerExposed`, `timeSpentSeconds` (optional, never invent), `gradingResult` (`score`, `maxScore`, `isCorrect`, `feedback`, `detectedMisconceptions[]`, `needsReview`), `submittedAt` (only if known). Preserve the first submitted response and its support condition.
- `ErrorDiagnosis`: `id`, `attemptId`, `errorCategory` (`conceptual|procedural|arithmetic|strategic|mixed|unclear`), `diagnosticStatus` (`unclassified|suspected|supported|resolved`), `diagnosticConfidence` (`low|medium|high`), `alternativeHypotheses[]`, `reasoningEvidence[]`, optional `legacyErrorMechanism`, `createdAt` (only if known). Qualitative confidence describes evidence for the category, not probability or learner confidence.
- `TransferCheck`: `id`, `conceptId`, `nearTask`, optional `farTask`, `prerequisiteEvidence[]`, `introductionCues[]`, `supportEvents[]`, `nearResult` and `farResult` (`passed|failed|skipped`), `principleNamed` (`yes|no|not_captured`), `supportCondition`, and `limitations`.
- `ReviewSummary`: `period`, `source` (`authorized_records|learner_export|recollection`), `comparableAttemptIds[]`, `sessionCount`, `hasUnassistedEvidence`, `gateMet`, `observations[]`, `learnerCorrections[]`, `interpretations[]`, optional `strategyGoal`, and optional `recommendedReviewWindow`; never imply a notification unless a schedule confirmation is stored.
- `Misconception`: `id`, `conceptId`, `description`, `diagnosticEvidence`, `remediationStrategy`.
- `StudentConceptState`: `studentId`, `conceptId`, `masteryScore` (0..1), `masteryStatus`, `totalAttempts`, `successfulAttempts`, `consecutiveIndependentSuccesses`, `activeMisconceptionIds[]`, `nextReviewAt` (nullable), `lastPracticedAt` (nullable).
- `StudentMisconceptionState`: `studentId`, `misconceptionId`, `status` (`suspected|confirmed|remediating|resolved`), `evidenceAttemptIds[]`, `lastObservedAt` (nullable).

## Validation rules
- Reject missing/invalid enums, unverified answers, inconsistent answer format and grading method, multiple correct single-choice options, unsupported source citations, and numerical prompts missing necessary units or assumptions.
- For `numeric`, compare with `abs(actual-expected) <= max(absTol, relTol * abs(expected))`; explicitly choose tolerances; default exact for integer discrete answers.
- For `sequence`, compare ordered normalized elements; do not sort before comparison.
- Avoid generating the same question wording with changed distractor order and treating it as independent evidence of mastery.
- Reject confidence captured after correctness feedback when labeled `confidenceBeforeFeedback`; keep it only as a post-feedback reflection with honest timing.
- Reject `unassisted` when a target-skill hint, worked step, answer reveal or evaluative feedback occurred before submission. Accessibility support alone is not disqualifying.
- Do not coerce an error diagnosis into a single category when evidence is mixed or unclear. Preserve legacy mechanisms during import/export.
- Exam Mode scoring fields become immutable after scoring except a documented grader correction; linked Quiz Mode attempts never mutate them.
