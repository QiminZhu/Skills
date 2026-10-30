# Teach, Practice, Check, Next

Use this workflow for new learning unless the learner requests another format. Keep the teaching focus narrow, provide original source visuals, grade objective practice locally where supported, and keep Next separate from submission.

## Teach from the source

- Use original readable lecture slides as the primary source. Reuse the relevant slide image or crop; do not redraw or regenerate an existing lecture diagram.
- Cite slide/page locations and preserve the lecture's terminology, notation, values, units, labels, and conventions.
- If no suitable source visual exists, provide a clear text explanation or seek a reliable supplementary visual. Label external material as supplementary.
- Never claim to have inspected or displayed an image that was not actually available.

## Practice and answer-key validation

Before rendering any locally graded item:

1. Define the objective and source locator. State any background assumption separately.
2. Solve the literal question independently. Recalculate values, units, sequence-number wraparound, and window boundaries.
3. Audit every option and explanation. Single-select items must have exactly one defensible answer under the stated assumptions. Clarify cumulative versus individual ACK conventions and inclusive/exclusive window boundaries.
4. Use deterministic local grading only for objective tasks. Use conversational evaluation for free-response reasoning unless all acceptable forms and tolerances are explicitly defined.
5. Treat local grading as comparison against a prepared answer key, not proof that the key is correct. Offer a grade challenge and recheck the source and alternatives if challenged.
6. Keep answer keys and feedback hidden until submission. Client-side keys are not secure exam secrets.

## Individual checkpoint pattern

The default lesson cycle is:

1. Teach one concept with an original slide visual where relevant.
2. Present one focused practice question.
3. The learner selects or enters an answer and presses **Check Answer**.
4. Show correct/incorrect status and an explanation locally, without requiring a model turn.
5. Offer a separate **Next** button to request the next lesson response. Do not automatically advance after a correct answer.

Allow retry when it is useful. The Next button remains separate from answer submission and may appear after either a correct or incorrect result.

## Multi-question assessment pattern

For a formal or applied assessment, a multi-question widget may be used instead of one question per turn. It should provide:

- A question counter and progress indicator.
- One submission and immediate local feedback per question.
- A final score and concise review of incorrect answers.
- A retake action when appropriate.
- A separate Next action after the final results.

Keep assessment length and coverage explicit. Do not imply that a short sample verifies every lecture objective.

## Original visual policy

When an uploaded lecture includes a relevant readable diagram, reuse it directly. Preserve the original diagram context and cite its slide/page. Do not substitute a newly generated generic image. Use supplementary diagrams only when the source has no suitable visual, and label them clearly.

## Rendering and host limitations

Use the bundled `scripts/render_practice.py` to create a self-contained practice fragment when a supported HTML interaction surface is available. A saved HTML file is not itself an inline widget. If only native controls are available, use them when appropriate; otherwise ask the question conversationally.

The component should feature-detect `window.openai.sendFollowUpMessage({prompt})` for Next. Do not invent undocumented message bridges or substitute a tool call. If the bridge is absent or fails, show the continuation prompt for the learner to send manually. Prevent duplicate clicks while pending and permit retry after failure.

Do not claim host functionality has been verified without testing local submission, feedback visibility, separate Next handoff, duplicate prevention, and missing-bridge fallback in that host.

## Session-only behavior

- Do not use a mastery tracker, persistent learner records, progress synchronization, external recording, review scheduling, or cross-plugin handoffs during this workflow.
- Keep only temporary conversational context required to continue the lesson.
- Widget state is transient: never infer that local selections, grades, or clicks were received by the model unless explicitly passed through a supported handoff.
- Do not promise control over the platform's ordinary conversation retention.

This session-only rule carries across Review and Project transitions unless the learner explicitly changes it.
