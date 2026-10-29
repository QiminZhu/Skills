---
name: quiz-master
description: Generate curated, source-grounded question banks for a static HTML quiz app from an approved lecture topic catalog or supplied educational material. Use when asked to create, revise, export, or blueprint quiz questions with answer keys, option-specific explanations, and validation-ready metadata. Does not administer student sessions or claim independent validation.
---
# Quiz Master v1.3

## Role and boundaries
Generate draft questions from an approved topic catalog produced by Lecture Analyzer, or directly from user-supplied lecture material when no catalog exists. Preserve source terminology and scope. Do not invent citations or unseen lecture content. Do not claim the Question Validator has approved anything; every generated item is `draft` until independently reviewed. No visuals in v1. Do not require a backend, database, or API. The output is static JSON suitable for a browser quiz app.

## Procedure
1. Inspect the complete available source and any approved topic catalog. Identify topic IDs, objective IDs, and page-level evidence. If a source cannot be inspected, ask for it rather than fabricate coverage. If the catalog is absent, derive a provisional objective map and label it as such.
2. Plan the requested count, question types, topic coverage, cognitive levels, and difficulty mix. Honor user-specified counts and distributions. For exam-wide generation, distribute questions across eligible objectives; disclose insufficient coverage. Never infer difficulty solely from cognitive level.
3. Generate `single`, `multiple`, `boolean`, `matching`, `ordering`, and `fill_blank` questions. Follow `references/question-contract.md`. Write an unambiguous prompt with complete assumptions. For choice questions, explain every option; for other types, explain every keyed pair, step, or blank. Keep a distinct overall explanation.
4. Independently solve each final question and check all displayed options, indexes, duplicate meanings, and answer/explanation consistency. Use `scripts/check_bank.py` for structural checks when code execution is available. This is generator self-checking, not independent validation.
5. Export a JSON array of draft questions. Include actual source page references, objective ID, cognitive level, version, and status. If source evidence is missing, flag the question for review rather than invent a page.
6. Hand off drafts and their source material to the separate Question Validator. Only that stage can produce a validation report and approval. Do not mark drafts approved or publish them directly.

## Content rules
- `single`: exactly one valid answer; plausible, mutually distinct distractors.
- `multiple`: two or more valid options and at least one invalid option; explicitly ask to select all correct answers.
- `boolean`: exactly `["True", "False"]`, with exactly one correct index.
- Avoid trick wording, unsupported absolutes, answer cues, and near-duplicate questions.
- For calculations, independently recompute the result, units, and rounding; reject equivalent unkeyed alternatives.
- Use the lecture as the authority for lecture-grounded questions. If external verification or enrichment is requested, label external material separately.
- Preserve exact zero-based `correct` indexes for choice questions; order is not semantically significant for multiple selections. For new types use the type-specific key in the contract, never overload `correct`.
- Never use an `EducationLevel` or `levels` attribute.

## References
Read `references/question-contract.md` for the output schema and `references/quality-checklist.md` before generation. Read `references/blueprints.md` when balancing a multi-topic assessment.

## Added answer formats
- `matching`: match each left item to exactly one right option using indexed pairs. Default to one-to-one; explicitly state if right options may be reused. Explain each pair. Keep both sides in non-revealing order.
- `ordering`: arrange at least three distinct items into one unambiguous sequence. State direction or criterion, shuffle the presented items, and explain each item's position. Avoid processes with equally valid alternative orders.
- `fill_blank`: use numbered markers `{{1}}`, `{{2}}`, etc.; provide a key for every blank. Text keys specify accepted variants and explicit normalization. Numeric keys specify units, rounding, and a finite nonnegative absolute tolerance. Never expose the key as answer choices.
- Select formats supported by actual lecture content: matching for relationships, ordering for defined sequences, blanks for precise recall or calculation. Do not invent calculations or force every format into every lecture. Honor requested format counts and option counts; disclose unsupported coverage.
- Read the full v3 contract before emitting these types. Existing v2 choice objects remain valid. A consumer supporting only v2 needs new renderers and graders; do not claim an existing website was upgraded.

## Coverage and workload gate (v1.3)
Read `references/coverage-contract.md` and `references/blueprints.md` before planning. Use the separate Analysis Validator's exact approved catalog and original sources. For a preview with unverified analysis, disclose that state; withhold full-coverage claims.

1. Establish selected objectives and both question-object and response-part budgets before generation. Defaults, unless overridden, are at most 20 question objects, 50 response units, 4 matching pairs, 6 ordering items, 3 blanks, and 6 options per choice item. These are editable MVP workload policies, not empirically established learning thresholds. Respect explicit user overrides and disclose them. Estimate time only as an uncalibrated range with assumptions; do not equate response parts with independent evidence or minutes.
2. Match format to the objective and source, not equal type quotas. Prefer small coherent matching groups. Separate unrelated facts and avoid multi-objective all-or-nothing bundles. Exceeding the budget requires splitting the assessment or an explicit budget change, never hiding more subparts inside fewer objects.
3. Write a sidecar ledger mapping each separately elicited response part to an atomic catalog objective with the evidence rationale. Preserve the legacy primary objectiveId; optional objectiveIds lists every mapped objective. A broad topic match, supplied cue, answer explanation, or fact embedded in a label cannot count as elicited knowledge.
4. Remove mnemonic answers from ordering stems (e.g. DORA when testing DHCP order), lexical abbreviation expansion cues when testing code interpretation, implausible joke distractors, and verbatim copied definitions mislabeled Apply/Analyze. For header fields, state request/reply context and full protocol assumptions. Do not silently correct source facts: scope to accurate claims or label authoritative external corrections separately.
5. Independently self-solve, run check_bank.py, then hand unchanged drafts, catalog, ledger and original source to Question Validator. Self-check cannot approve mappings or questions. Only validated exact question versions count toward coverage. Rejected, ambiguous, unsupported or stale questions reopen gaps.
6. Run scripts/check_coverage.py with the approved-question copies, validated ledger and analysis report. Deliver quiz plus full/partial/missing/unverified/excluded objective report and workload. A hard count never overrides coverage truth. If any required objective lacks valid adequate evidence, report incomplete, revise within the budget or propose split sessions. Never publish draft keys as independently approved.

The setup interface remains a separate host UI feature; these policies do not install a form or browser grader. Existing six-format BankQuestion v3 items remain compatible.
