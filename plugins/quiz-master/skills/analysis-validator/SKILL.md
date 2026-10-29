---
name: analysis-validator
description: Independently audit a Quiz Master lecture concept/objective catalog against every original source page, diagram, and table before question generation. Use to check analysis completeness, consistency, contradictions, source grounding, and measurable objective scope.
---
# Analysis Validator

Read the original sources and `../lecture-analyzer/references/topic-contract.md`; do not trust the analyzer's catalog. Read `references/analysis-contract.md` before reporting.

1. Independently inspect substantive content, diagrams, tables, commands, and captures before comparing the catalog. If any relevant source cannot be read, mark checks unverified and withhold approval.
2. Check every source page has a disposition and reason; every included concept has atomic measurable objectives and actual source references. Page accounting alone is not evidence of completeness. Spot-check page-to-objective mappings against required response skills, not merely topic labels.
3. Check stable unique IDs, consistent granularity/terminology, duplicates, prerequisite labels, concept-parent links, and core/supporting priority. Split compound objectives so order, role, field size, interpretation, and application cannot hide behind one checkmark. Do not invent an arbitrary target objective count.
4. Flag misleading source statements and unreadable details. Do not silently substitute external knowledge. Require explicit externally verified correction records or scope questions to uncontested purposes. Never teach a known falsehood merely to match the lecture. Supplemental content is distinct from lecture coverage.
5. Return precise issues to Lecture Analyzer; request a fresh audit of revisions. Any substantive omission, unsupported objective, unresolved contradiction in assessable material, or unreadable required content blocks approval. There is no automatic approval score.
6. Only after a genuinely separate audit passes, emit approval bound to the exact catalog hash and original source hashes. A later edit invalidates approval. Do not claim an independent model/human review unless it occurred; separate passes can share errors.

Do not generate questions or mark a catalog reviewed by self-check alone. The source-analysis audit must precede full-coverage generation. A user may request a draft preview before approval, but label its analysis unverified and never call it full coverage.
