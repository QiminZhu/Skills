# Grading protocol

1. **Single choice**: compare stable option ID to correct ID; exact 0 or 1. Avoid revealing key until answer submitted.
2. **Numeric**: parse finite numeric value; normalize units only when conversion is explicitly supported; check absolute/relative tolerance. Report expected result, formula, and relevant units after grading. Reject NaN/ambiguous units; seek clarification when reasonable.
3. **Sequence**: compare ordered values with expected sequence. For partial credit, award only if a question-specific rubric defines it; do not silently invent partial credit.
4. **Short answer**: construct a criterion-based rubric before grading; grade semantic content, not wording. Example for why binary search is efficient: interval-halving 2 points, sorted-data prerequisite 1 point, logarithmic vs linear complexity 1 point. Normalize score by maxScore.
5. Return `score`, `maxScore`, `isCorrect` (based on full correctness, not partial credit), `feedback`, `detectedMisconceptions[]`, `needsReview`. Use `needsReview=true` when ambiguous, conflicting, or low-confidence; do not treat tentative diagnoses as confirmed.
6. Hints reduce independence: keep `hintsUsed`, and discount or exclude assisted success from mastery advancement. Correct answer after seeing a solution is practice, not independent mastery evidence.
7. For wrong answers, give concise error-specific feedback and optionally a small hint, then offer a fresh related question. For correct answers, explain the governing principle briefly and test transfer when needed.
8. Do not fabricate execution results or claim to have run code/calculations without actually doing so. Check arithmetic independently when tools are available.
