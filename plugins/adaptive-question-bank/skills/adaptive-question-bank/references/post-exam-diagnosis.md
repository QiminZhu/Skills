# Reasoning-based post-exam error diagnosis (v1.5.0)

## Trigger and invariants
After a submitted exam is scored, inspect each incorrect attempted answer (including dependent layers). Keep original answer, correct answer, rubric, first-attempt score, partial marks and source intact. Preserve the original exam score; post-exam explanations, retries and diagnostics are separate attempts. Do not show reference answers prematurely during an opted-in diagnosis-first review. For blank responses or "I don't know", mark `not_attempted`/`knowledge_gap_suspected` rather than fabricating a wrong approach.

## Default balanced diagnostic sequence
1. **Collect reasoning:** Ask one open-ended question: "How did you approach this? Walk me through the steps and anything you were unsure about." If the student already gave reasoning, do not ask it again.
2. **Identify evidence:** Find the first demonstrably incorrect step, not just the incorrect final value. Map dependencies in layered problems and distinguish upstream causes from later follow-through errors. Verify calculations and avoid interpreting correct follow-through from unsupported intermediate memory data.
3. **Categorize provisionally:** Two independent axes: `errorMechanism` = `unclassified|possible_typo|arithmetic_slip|procedural_error|conceptual_misconception|knowledge_gap|guess|cascading_error`; `knowledgeState` = `unknown|prerequisite_gap_suspected|misconception_suspected|developing|independent_evidence|resolved`. Separately keep `evidenceStatus` = `unclassified|suspected|supported|resolved`. These are qualitative evidence labels, not numeric probabilities.
4. **Disambiguate with one targeted follow-up at a time:**
   - Possible typo: do not simply accept a claim of a typo. Offer a fresh parallel problem with changed values and no answer key or help; independent success supports a slip, but does not prove it. If student cannot solve it, switch to identifying a prerequisite gap; do not keep the typo diagnosis.
   - "I don't know" or no method: ask what component is unfamiliar or a short prerequisite diagnostic; teach only the missing material, then test independently. Do not count an abstention as an attempted numerical calculation.
   - Wrong approach: restate the suspected false assumption neutrally; ask one discriminating conceptual question that distinguishes it from the correct rule without leaking the answer. Repeated wrong application or a clearly stated false rule supports a misconception; if the student knows the rule but executes incorrectly, record procedural error. Contrast the mistaken rule with the correct concept, give one focused practice and then novel exam-level transfer.
   - Arithmetic/slip: check a corresponding calculation or original method; remediate accuracy/verification only if repeated. A single slip is not a confirmed misconception.
5. **Update after evidence:** Withhold irreversible labels. A single wrong answer creates a suspected issue, not confirmed permanent weakness. A clear false belief corroborated by new evidence supports misconception; preserve competing explanations when ambiguity remains. After correction, demand at least two varied independent successful attempts plus later review before resolving; recent assisted answers only count as practice.
6. **Choose next action:** Ask diagnostic, review prerequisite, corrective explanation, focused practice, exam-level transfer, or defer. Do not force additional questions if learner explicitly requests complete solutions or to move on.

## Scoring and adaptation safeguards
- `examScore` is immutable after final grading, except genuine grader correction with explicit audit; `remediationProgress` and `verificationAttempts` are separate. Follow-through/method credit for dependent layers follows the predeclared rubric and must not be mistaken for canonical correctness.
- Do not automatically reduce difficulty because of one wrong answer or a self-reported lack of confidence; adjust *remediation* tasks according to evidence, then return to original exam difficulty.
- Do not automatically mark mastered because student can verbally explain a method after feedback, says typo, or gets the same item right on retry. Use a new independent item; keep assisted and unassisted trials distinct.
- Missing information about intermediate state means follow-through credit is unverified, not assumed.

## Mistake bank extension (JSON-compatible logical record)
`diagnosisId`, `originalAttemptId`, `questionId`, `layerId` (optional), `originalExamScore`, `initialResponse`, `reasoningNarrative`, `suspectedFirstFault`, `errorMechanism`, `knowledgeState`, `evidenceStatus`, `evidence[]` (each with kind, itemId, response, independence, outcome), `affectedLayerIds[]`, `verificationAttempts[]`, `remediationAction`, `resolutionStatus`, `reviewDue` (only when actually available). Do not claim persistent storage beyond the conversation; export structured JSON on request.

## Behavioral test fixtures
- Original `addi $t0,$t1,-13`, answer `0x2128000D`; learner says "I might have mistyped": status = possible typo, require fresh negative-immediate encoding; no mastery increase yet.
- Same original; fresh `addi ...,-7` receives "I don't know": retain original incorrect score, withdraw unverified typo inference, suspect missing knowledge, ask shortest prerequisite question.
- Same original; learner explicitly believes magnitude 13 is stored and processor interprets the minus sign automatically: identify false-rule hypothesis, probe two's-complement distinction, correct and independently verify; do not label confirmed solely on first answer.
- A layered answer is wrong solely due to upstream incorrect intermediate but operation is correct: follow-through method credit under specified rubric, no duplicate misconception label.
