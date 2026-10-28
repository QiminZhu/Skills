# Tutor me 0.7.0 — implemented proposal

Baseline: 0.6.0. Published version: 0.7.0. Existing plugin identity and audience remain unchanged.

## Teach

Use readable original lecture slides as the primary source and cite slide/page numbers. Label supplementary knowledge. When a visual materially helps, reuse a suitable source diagram first. Otherwise search for an accurate visual from a reliable source, link its source, and explain its connection and differences in notation, assumptions, or values. Never invent data or use a misleading visual.

## Practice and validation

Present one interactive practice question with immediate local grading where the host supports it. Before rendering, verify the question, answer key, and explanation against source slides; check computations or executable examples with tools where appropriate. Revise or withhold unverifiable or ambiguous questions. Use deterministic local grading only for responses with a validated criterion, accepted alternatives, and appropriate numerical tolerance. Free explanations requiring judgment need model review and must not be represented as locally verified.

Keep keys and explanations hidden from the visible interface until submission; client-side keys are not secure exam secrets. Submission displays feedback locally and does not advance automatically. Provide a grade-challenge action that asks for source-based rechecking through a new message. Explain that local grading does not guarantee a correct answer key.

## Next

Render a separate Next button. It sends a new user message requesting the next step with the lesson objective, source position and submitted practice result needed for continuation. Use an actual supported host message API only after checking availability; never invent a handoff API. If unsupported, disclose the limitation and offer a clear manual Next message. Do not pretend a button works. Verify local submission and message handoff in the intended host before claiming the interactive behavior is tested.

## Session-only learning

No mastery tracker, external learner records, progress synchronization, or recall scheduling for this lesson flow. Maintain only temporary conversation context. Existing optional-record instructions must defer to this explicit constraint. Plugin source versioning in GitHub stores plugin code/instructions, not learner results.

## Acceptance checks

- Relevant source visual is used before online fallback; supplements have source links.
- A deliberately wrong answer key is rejected by source verification.
- Valid alternatives and numerical tolerances are handled fairly.
- Submission grades locally without a new assistant response or automatic advance.
- Next sends one new message only when clicked; unsupported hosts receive an honest fallback.
- No external learner-record tools or tracking writes occur.

Instructions alone cannot guarantee host UI support or grading correctness. Implemented in 0.7.0 with a bundled renderer. Structural and mocked-runtime checks passed; live ChatGPT rendering remains unverified.
