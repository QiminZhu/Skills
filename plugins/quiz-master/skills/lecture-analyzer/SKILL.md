---
name: lecture-analyzer
description: Analyze user-uploaded lecture PDFs, slides, or notes into a source-grounded catalog of subjects, lectures, topics, and measurable learning objectives for Quiz Master. Use when asked to extract topics, organize lecture material, or prepare a question blueprint.
---
# Lecture Analyzer

## Role
Read the user's actual uploaded materials and produce a topic catalog, not questions. Preserve lecture terminology, distinguish source facts from inferred objectives, and never fabricate pages or claims. No visuals in v1; diagrams in sources must still be inspected and described if material.

## Procedure
1. Identify each source file, its version if available, and page/slide numbers. Inspect diagrams, tables and figures, not only extracted text. State unreadable or missing sections.
2. Extract a subject > lecture > topic > learning objective hierarchy. Group near-duplicates, retain meaningful subtopics, and avoid overfragmenting slides.
3. Write assessable objectives with observable verbs. Record evidence references for each objective, and distinguish explicit objectives from inferred objectives.
4. Note prerequisite links only when supported or label them as inferred. Flag contradictions or ambiguous source material rather than silently correcting it.
5. Export JSON using `references/topic-contract.md`. Mark the catalog `draft` until reviewed; do not claim it is approved automatically.
6. Hand the catalog and original source to the separate Analysis Validator before Quiz Master. Revise from audit findings and require a fresh audit. Preserve source citations for Question Validator.

## Boundaries
Do not generate questions or answer keys. Do not add EducationLevel or levels. Do not require a database, external API, or backend. Do not infer absent material. Preserve 1-based page numbers.

## Coverage-first analysis
Read the expanded topic contract. Account for every page, image, table, practical command and capture example; explicitly record admin/duplicate/resource-only/unreadable dispositions. Group source content as subject > lecture > topic > concept > atomic objective. Atomic means one independently checkable skill: DHCP message order and message roles need separate objectives; HDLC field order and field lengths need separate objectives. Keep consistent granularity without turning every sentence into an objective. Mark core/supporting as a judgment for review, not a claim of instructor priority. All objectives are required by default; excluding one changes the declared assessment scope and must remain visible. Flag technical errors instead of teaching them or silently correcting them. Fingerprint source bytes and preserve the final catalog hash. An approved catalog cannot guarantee perfect completeness or learner mastery.
