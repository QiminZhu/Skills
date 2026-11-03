# Teach, Practice, Check, Next

Use this workflow for new learning unless the learner requests another format. Keep one concept and one practice item per step for ordinary teaching. Honor direct explanation, solution and batch-assessment requests.

## Teach from the source

- Use original readable lecture slides as the primary source. Reuse the relevant slide image or accurate crop; do not redraw, regenerate or substitute a generic diagram when the original lecture visual is available.
- Cite slide/page locations and preserve the lecture's terminology, notation, values, units, labels, axes and conventions.
- If no suitable source visual exists, provide a clear text explanation or seek a reliable supplementary visual. Label external material as supplementary.
- Never claim to have inspected or displayed an image that was not actually available.

## Practice and answer-key validation

Before rendering any locally graded item:

1. Define the observable objective and source locator. State any background assumption separately.
2. Solve the literal question independently of the intended answer. Recalculate values, units, rounding, sequence-number wraparound, and sender/receiver window boundaries.
3. Audit every option and explanation. Single-select items must have exactly one defensible answer under the stated assumptions. Clarify cumulative versus individual ACK conventions and inclusive/exclusive window boundaries.
4. Use deterministic local grading only for objective tasks. Use conversational evaluation for free-response reasoning unless all acceptable forms and tolerances are explicitly defined.
5. Treat local grading as comparison against a prepared answer key, not proof that the key is correct. Offer a grade challenge and recheck the source and alternatives if challenged.
6. Keep answer keys and feedback hidden until submission. Client-side keys are not secure exam secrets.

## Individual checkpoint pattern

1. Teach one concept with an original slide visual where relevant.
2. Present one focused practice question.
3. The learner selects or enters an answer and presses **Check Answer**.
4. Show correct/incorrect status and a concise, option-specific explanation locally, without requiring a model turn to grade.
5. Offer a separate **Next** button to request the next lesson response. Do not automatically advance after a correct answer.

Allow retry when useful. The Next button remains separate from answer submission and may appear after either a correct or incorrect result. Checking an answer must not itself send a chat message or advance the lesson.

## Multi-question assessment pattern

When the learner requests a batch, quiz, exam or applied final assessment, use a multi-question sequence rather than forcing one chat turn per question. It should provide:

- A clear question count and progress indicator.
- One submission and immediate local feedback per question.
- A final score and concise review of incorrect answers.
- A retake action when appropriate.
- A separate Next action after the final results.

Keep assessment length and objective coverage explicit. Validate every item independently. Do not imply that a short sample verifies every lecture objective.

## Rendering and host limitations

Use the bundled \`scripts/render_practice.py\` to create a self-contained practice fragment when a supported HTML interaction surface is available. A saved HTML file is not itself an inline widget. If supported native controls are available and suit the task, use them; otherwise ask the question conversationally. Apply the host's relevant UI skill before implementation where one exists.

The HTML component should feature-detect \`window.openai.sendFollowUpMessage({prompt})\` for the separate Next action. Do not invent undocumented message bridges or substitute an external tool call. If the bridge is absent or fails, show the continuation prompt for the learner to send manually. Prevent duplicate clicks while pending and permit retry after failure.

Do not claim host functionality has been verified without testing local submission, feedback visibility, separate Next handoff, duplicate prevention and missing-bridge fallback in that host. Distinguish implementation checks from live-host verification.

## Session-only behavior

- Do not use a mastery tracker, persistent learner records, progress synchronization, external recording, review scheduling, browser storage, analytics, telemetry or cross-plugin handoffs during this workflow.
- Keep only temporary conversational context required to continue the lesson.
- Widget state is transient: never infer that local selections, grades or clicks were received by the model unless explicitly passed through a supported handoff.
- Do not promise control over the platform's ordinary conversation retention.

This session-only rule carries across Review and Project transitions unless the learner explicitly requests a change to persistent tracking.
