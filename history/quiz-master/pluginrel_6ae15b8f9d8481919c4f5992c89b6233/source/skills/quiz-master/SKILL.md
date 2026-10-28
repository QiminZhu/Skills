---
name: quiz-master
description: Generate curated, source-grounded question banks for a static HTML quiz app from an approved lecture topic catalog or supplied educational material. Use when asked to create, revise, export, or blueprint quiz questions with answer keys, option-specific explanations, and validation-ready metadata. Does not administer student sessions or claim independent validation.
---
# Quiz Master v1.0

## Role and boundaries
Generate draft questions from an approved topic catalog produced by Lecture Analyzer, or directly from user-supplied lecture material when no catalog exists. Preserve source terminology and scope. Do not invent citations or unseen lecture content. Do not claim the Question Validator has approved anything; every generated item is `draft` until independently reviewed. No visuals in v1. Do not require a backend, database, or API. The output is static JSON suitable for a browser quiz app.

## Procedure
1. Inspect the complete available source and any approved topic catalog. Identify topic IDs, objective IDs, and page-level evidence. If a source cannot be inspected, ask for it rather than fabricate coverage. If the catalog is absent, derive a provisional objective map and label it as such.
2. Plan the requested count, question types, topic coverage, cognitive levels, and difficulty mix. Honor user-specified counts and distributions. For exam-wide generation, distribute questions across eligible objectives; disclose insufficient coverage. Never infer difficulty solely from cognitive level.
3. Generate `single`, `multiple`, and `boolean` questions only. Follow `references/question-contract.md`. Write an unambiguous prompt with complete assumptions. For each option, write an explanation specific to why that exact option is or is not correct. Keep a distinct overall explanation.
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
- Preserve exact zero-based `correct` indexes; order is not semantically significant for multiple selections.
- Never use an `EducationLevel` or `levels` attribute.

## References
Read `references/question-contract.md` for the output schema and `references/quality-checklist.md` before generation. Read `references/blueprints.md` when balancing a multi-topic assessment.
