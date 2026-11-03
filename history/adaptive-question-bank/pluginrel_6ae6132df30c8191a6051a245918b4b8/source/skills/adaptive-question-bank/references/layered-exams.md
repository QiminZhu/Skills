# Dependent layered exam problems

In Exam Simulation Mode, support single integrated multi-part problems with genuine dependencies. A layer must consume a result or justified conclusion from at least one earlier layer; unrelated multi-part prompts are not dependent.

## Blueprint
- Select a coherent technical scenario supported by source material. Identify relevant concepts, realistic givens, explicit assumptions, and calibrated complexity.
- Pre-plan 2–6 layers, or user-specified count, and a dependency DAG. Each layer has: layerId, conceptIds, cognitiveType, expectedOutput, answerFormat, maxPoints, dependsOn, referenceAnswer, gradingRubric, expectedDifficulty and sourceLocator if supported.
- Dependencies may branch and merge: not all layers must form a simple chain. At least one downstream layer must explicitly use an upstream result.
- Ensure all necessary information is available at the time each layer is asked. Distinguish genuinely dependent computation from simply reusing a shared scenario.
- Preserve the source problem's output granularity and difficulty when reference questions exist. Never invent exam provenance. If no reference questions exist, label difficulty estimated.
- Verify the full problem from initial data through final results independently, including valid numerical bounds, instruction formats, assumptions, dependencies, timing and precision. Generate and check alternative values before release.

## Interaction
- The user's `mode=exam` selects Exam Simulation Mode. Accept optional `structure=layered` or `structure=independent`, with `structure=mixed` default for exam sets. When the user explicitly asks for layered questions, use `layered`.
- Present shared scenario and either all parts at once (written-exam style) or successive parts (interactive style); preserve a learner's explicit preference. In successive style, do not reveal reference answers or intermediate hints before later parts unless the user requests help; use submitted earlier responses as the stated working assumption for dependencies.
- Offer original-source question comparisons when requested without claiming exact matching if reference questions do not support it.
- Avoid increasing layer count just to make a problem harder. Difficulty should reflect reasoning, dependencies and calculation complexity rather than answer-field count.

## Grading: independent correctness and follow-through
- Retain the canonical answer of every layer computed from correct inputs.
- Grade each layer for independent correctness and for method/follow-through on the learner's previous answers. When a later response correctly applies the required operation to a prior incorrect result, award method/follow-through credit according to the declared rubric, but never claim the later numerical answer is independently correct.
- Prevent cascading double penalties. A copied wrong intermediate result should not automatically zero all dependent layers. Likewise do not grant full credit if the later calculation is itself incorrect.
- Record each layer's answer, canonical outcome, learner-dependent outcome, detected misconception and marks. Explain where the first error occurred only after submission or by explicit request.
- In exam mode, preserve planned difficulty and scoring; offer an opt-in separate learning-mode remediation after the exam.
- Track whether a misconception is upstream or downstream to target practice intelligently.

## Example structure (not an existing textbook question)
Scenario: load-add-branch instruction sequence, with explicit register and memory values, stated pipeline stage model, forwarding assumptions, and branch resolution stage.
Layer 1: encode the load instruction (32-bit hex).
Layer 2: compute the effective address using load instruction's operands and base register.
Layer 3: compute the loaded register value from provided memory contents.
Layer 4: use loaded value to determine the arithmetic instruction's result.
Layer 5: use computed result to determine branch outcome and cycle count including necessary hazards.
Validate that all input values, assumptions and output keys are consistent before showing this problem.
