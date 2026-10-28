# Question and learner state contracts (v1)

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

## Other entities
- `Concept`: `id`, `name`, `learningObjective`, `prerequisiteIds[]`.
- `Attempt`: `id`, `studentId` (may be local pseudonym), `questionId`, `attemptNumber`, `response`, `confidence` (optional), `hintsUsed`, `timeSpentSeconds` (optional, never invent), `gradingResult` (`score`, `maxScore`, `isCorrect`, `feedback`, `detectedMisconceptions[]`, `needsReview`), `submittedAt` (only if known).
- `Misconception`: `id`, `conceptId`, `description`, `diagnosticEvidence`, `remediationStrategy`.
- `StudentConceptState`: `studentId`, `conceptId`, `masteryScore` (0..1), `masteryStatus`, `totalAttempts`, `successfulAttempts`, `consecutiveIndependentSuccesses`, `activeMisconceptionIds[]`, `nextReviewAt` (nullable), `lastPracticedAt` (nullable).
- `StudentMisconceptionState`: `studentId`, `misconceptionId`, `status` (`suspected|confirmed|remediating|resolved`), `evidenceAttemptIds[]`, `lastObservedAt` (nullable).

## Validation rules
- Reject missing/invalid enums, unverified answers, inconsistent answer format and grading method, multiple correct single-choice options, unsupported source citations, and numerical prompts missing necessary units or assumptions.
- For `numeric`, compare with `abs(actual-expected) <= max(absTol, relTol * abs(expected))`; explicitly choose tolerances; default exact for integer discrete answers.
- For `sequence`, compare ordered normalized elements; do not sort before comparison.
- Avoid generating the same question wording with changed distractor order and treating it as independent evidence of mastery.
