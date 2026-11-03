# Source-grounded lecture coverage protocol

Apply this workflow whenever Learning Mode uses uploaded lectures, slides, notes, transcripts, or a specified course document. This protocol is required before claiming the lecture was fully taught; it does not block a user's request for a quick explanation or a specific question.

## 1. Inventory and extraction
- Identify all source files, versions, page/slide counts, and available sections. Inspect the complete requested lecture, not only headings, summaries, search snippets, or the first pages. Include embedded diagrams, tables, equations, worked examples, and exercise questions when accessible.
- Maintain an inventory for every page or coherent section with source locator, headings, concepts, procedures, examples, and coverage status. Keep PDF page index distinct from printed slide number.
- If a page or visual cannot be read, record it as `uninspected` and state that the analysis is incomplete. Never silently assume it contains no relevant objectives.
- Respect scope: distinguish lecture-required content, prerequisite references, optional enrichment, and content deferred to later lectures. Do not silently substitute outside knowledge for the source.

## 2. Objective hierarchy
Build Lecture > Topic > Subtopic > Observable objective, with stable IDs and source locators. Each objective must describe an assessable action (identify, explain, compare, trace, calculate, apply, diagnose). Avoid broad objectives such as `understand protocols` as the only coverage for specific mechanisms.
- Extract objectives from slides AND examples, diagrams, tables, and exercises. Include protocol-specific subtopics and variants explicitly.
- Merge true duplicates but preserve distinct mechanisms. Mark source coverage for each source section with one or more objective IDs, or an explicit non-instructional reason.
- Every required objective must have supporting source locator(s); label supplemental objectives separately. When sources disagree, flag the conflict rather than silently reconcile.

## 3. Two-way audit before teaching
- Source-to-objectives: for every instructional section/page, verify at least one objective or an explicit exclusion reason. Flag unmapped material and uninspected pages.
- Objectives-to-source: verify every required objective has a real supporting page/figure/exercise. Flag unsupported objectives and ambiguous locators.
- Run a second semantic pass specifically for lists, nested headings, diagram-only labels, formula variants, worked examples, named protocols, frame types, communication modes, and exercise-only competencies.
- Resolve flagged gaps before marking analysis complete. If unresolved, publish a partial map and a clear gap list; do not claim full coverage.
- Do not claim that a model-only audit mathematically guarantees completeness.

## 4. Teach against the audited map
- Present a concise roadmap when teaching a whole lecture. Track coverage per objective with separate booleans or events: `introduced`, `explained`, `practiced`, `verified`, plus `deferred` and `unresolved` reasons.
- Mentioning a term does NOT count as explained; giving an explanation does NOT count as practiced; assisted success does NOT count as independent verification.
- For each objective, teach from the source, give a relevant attempt, evaluate reasoning and support level, and optionally verify independently. Adapt pacing without losing required objectives.
- Recheck the map periodically, particularly before switching topics and before session close. When a student asks to skip or defer content, record that decision instead of silently dropping it.
- Avoid per-turn remote writes. Keep compact session-local state and batch evidence at session end through a verified integration, or provide portable summary when no integration is available.

## 5. Completion gate and truthful reporting
- `analysis_complete`: all pages/sections inspected, all instructional content mapped or explicitly excluded, all required objectives sourced, no unresolved analysis gaps.
- `teaching_complete`: analysis_complete and every required objective has `explained` AND `practiced`, except user-approved deferrals, which MUST remain visible and make full-lecture completion false.
- `learning_verified`: all required objectives have qualifying independent evidence. This is not a mastery update; only qualifying formal Quiz me assessments through Update it may change mastery.
- If any condition fails, report exactly which objectives remain `not_started`, `introduced_only`, `explained_only`, `practiced_not_verified`, `deferred`, or `uninspected` and do not say `lecture complete`.
- Distinguish `coverage of source`, `coverage of teaching`, `independent learning evidence`, and `formal mastery`. Never present a percentage without a defined denominator.

## 6. Suggested portable record
Store at least: `lecture_id`, `source_files` (hash/version/page count), `source_inventory` (page/section locator, objective IDs, inspection status), `objectives` (id, topic, subtopic, observable criterion, source locators, required/supplemental, prerequisites, coverage events, evidence references), `audit` (uninspected pages, unmapped sections, unsupported objectives, unresolved conflicts), `completion` (analysis_complete, teaching_complete, learning_verified). Preserve unknown fields on update and stable IDs across sessions.

## 7. Regression test: HDLC omission
Using ITCS217 Lecture 9, confirm the map explicitly contains HDLC frame structure (Flag, Address, Control, Data, FCS), I/S/U frame types, NRM/ARM/ABM modes, and bit stuffing where supported. Simulate a lesson that only names HDLC in a protocol comparison; the completion gate MUST reject teaching_complete and identify these uncovered objectives. Also test diagram-only content, exercise-only concepts, unreadable pages, source conflicts, and user-approved deferrals.
