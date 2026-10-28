# Teach, Practice, Next

Use this flow for new teaching unless the learner requests a different format. Keep one concept and one practice item per step. Honor direct explanation or solution requests.

## Teach and visual sources

Use the original readable lecture slides as the primary source. Cite slide/page numbers and retain the lecture's terminology. When a graph, diagram, or image materially helps explain a knowledge point, inspect the relevant slide visual and reuse it first. Show the image or an accurate crop when the host supports it; a citation alone is not displaying the visual. Preserve axes, units, labels, legends and context. Never claim an unseen diagram was inspected.

If no suitable slide visual exists, search online for an accurate visual from a reliable primary or educational source, inspect it, and link the source. Explain how it supports the concept and label it as supplementary. Explain differences in assumptions, notation, values or conventions. Do not substitute an attractive but misleading visual, invent measurements, or silently imply an online image came from the lecture. If search or image display is unavailable, say so and provide the best supported explanation.

## Validate before presenting practice

Local grading compares the response with a prepared key; it cannot establish that the key is true. Before rendering:

1. Define the observable objective and a source-grounded answer criterion with a slide/page locator. Identify any necessary background knowledge separately.
2. Solve the literal question independently of the intended answer. For calculations or code, run appropriate checks where tools are available. Check units, rounding, boundary cases and the displayed values.
3. Check every option and its explanation. Require exactly one defensible answer for single-select questions; revise ambiguous, duplicated or unverifiable items. Do not mark an item validated just because a key exists.
4. Use deterministic local grading only for appropriate objective tasks. For free responses, include all defensible accepted forms and explicitly stated tolerances, or use conversational model review. Do not represent keyword matching as validation of reasoning.
5. Keep the key, verdict and explanations hidden from the visible interface until submission. Client-side keys are not secure exam secrets. Offer a non-revealing hint only on request and preserve the distinction between supported and independent attempts.

Use the bundled `scripts/render_practice.py` to create a self-contained fragment from validated single-select question JSON when an HTML interaction surface is available. Read the script's help and supply the real item, source locator, feedback for each choice, source-based validation evidence, and a concrete continuation prompt. The script checks structure, not factual correctness. It does not replace steps 1–4.

## Practice locally

Render the fragment through the host's supported interactive HTML surface, applying that surface's skill when available. A saved HTML file alone is not an inline widget. If only a supported native quiz widget is available, use it only when its task restrictions fit; do not force a subjective question into it. If no interactive renderer exists, explain the limitation and ask the question conversationally.

Submission shows the result and option-specific explanation inside the component without a model call, network request, external write, or automatic lesson advance. Allow a grade challenge; it requests a source-based recheck through a new message. Recheck the source, calculations, alternatives and criterion before confirming or correcting a challenged grade. Correct erroneous feedback openly.

## Separate Next button

Keep Next separate from answer submission. On click, request the next lesson response through a supported host bridge and pass only the current objective, source position, question ID, submitted answer and result needed for continuation. Do not send a message on load, option selection, submission or grading. Prevent duplicate clicks while a message is pending, and permit retry after errors. Do not automatically advance after a correct answer.

The bundled component feature-detects `window.openai.sendFollowUpMessage({prompt})`, documented at https://developers.openai.com/plugins/reference (checked 2026-10-28). Availability in a ChatGPT app does not prove availability in every HTML surface. Do not add undocumented postMessage protocols or call external tools as a substitute. If the bridge is missing or fails, show the continuation text for the learner to send manually; never claim it was sent.

Continue from conversation context after Next. If practice state has not reached the model, ask only for what is necessary or accept an explicit skip; never infer local clicks, grades, or mastery from the displayed component alone.

## Session-only operation and verification

Keep this flow session-only. Do not read or write learner records, invoke mastery trackers, synchronize progress, export assessment evidence, create review schedules or send results to another plugin or repository. Do not use browser storage, analytics, telemetry, or persistent widget state for practice. This restriction overrides optional record/scheduling instructions during this flow and carries across mode transitions unless the learner explicitly changes it. GitHub versioning stores plugin source only.

Keep source coverage and assistance context only as needed in the conversation. Do not promise control over the platform's normal chat retention. Before claiming that the UI works in a particular host, verify local submission, hidden-before-submit feedback, separate message handoff, duplicate prevention and missing-bridge fallback there. Report implementation checks separately from live host verification.
