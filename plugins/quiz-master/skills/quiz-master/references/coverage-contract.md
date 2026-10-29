# Coverage ledger and gate

Run `python scripts/check_coverage.py catalog.json analysis-report.json approved-bank.json question-reports.json ledger.json ledger-review.json`. Output is JSON; exit 0 only when all required objectives have adequate validated evidence, all bindings/checks pass, and workload fits. Exit 1 means incomplete/blocked, exit 2 unreadable input. Missing artifacts never imply approval. This is an integrity and accounting checker, not an independent semantic reviewer.

## Bindings
Canonical SHA-256: JSON with sorted keys, compact separators, UTF-8, ensure_ascii=False, allow_nan=False. Source versions are actual source-byte SHA-256 hashes. Reports bind the final immutable payloads. Approval of an earlier draft is invalid for an edited version. Preserve all original drafts.

The catalog follows Lecture Analyzer's expanded contract. The analysis report follows Analysis Validator's contract. Question reports are an array using Question Validator's contract; approved items have status approved and all applicable checks pass, with issues empty. New-type reports use responseExplanations; choices use optionExplanations. `coverageMappings` is required for this gate. Approved reports hash the final approved copy, not the earlier draft.

## Ledger
JSON object:
```
{
  "catalogHash": "sha256",
  "budgets": {"maxQuestions":20,"maxResponseUnits":50,"maxMatchingPairs":4,
              "maxOrderingItems":6,"maxBlanks":3,"maxChoiceOptions":6},
  "budgetOverrides": [],
  "mappings": [{"mappingId":"m1","objectiveId":"o1","questionId":"q1",
    "questionVersion":1,"questionHash":"sha256","part":"response",
    "coverage":"adequate","rationale":"Required response actually demonstrates this atomic skill."}]
}
```
Every budget must be a positive integer. When a value differs from defaults, `budgetOverrides` must contain `{field, value, reason}` documenting the user's explicit setting. The script can inspect that record, not independently prove authorization. Never write an override merely to pass the gate.

Each mapping ID and objective/question/part tuple is unique. `coverage` is adequate, partial, or unverified (reviewer's final judgment, not author's automatic claim). Rationale explains elicited evidence, not the topic's name. Unmapped objectives become missing. Primary objectiveId must be mapped for each question; optional objectiveIds must equal the actual mapped IDs.

Parts: single/boolean `response`; multiple `option:0`, `option:1`, etc.; matching `pair:0` etc., indexing matches; ordering `position:0` etc., indexing correctOrder; fill_blank `blank:1` etc., using blank IDs. Count response workload as single/boolean1, multiple each option, matching each pair, ordering each position, and blanks each blank. These are not psychometrically independent units.

## Separate ledger review
JSON `{catalogHash, ledgerHash, decision, checks, issues}`. ledgerHash hashes the full ledger above. Checks `sourceEvidence`, `responseDemand`, `granularity`, `scope`, and `workload` must all pass; decision approved and issues empty. Obtain this from a separate Question Validator pass reviewing mappings and whole-quiz scope, not a generator self-signature. A ledger edit invalidates this approval.

## Interpretation
A question contributes only if its exact final payload is approved with source evidence and valid structural schema. Incorrect, ambiguous, stale, draft, rejected or unsupported questions never close gaps. A ledger edit or stale catalog binding blocks all its mappings. A valid partial mapping never becomes adequate merely because other partial mappings exist; the validator must justify complete coverage explicitly.

The report lists adequate/partial/missing/unverified/excluded objectives, question IDs and reasons, analysis and binding problems, workload, and scope exclusions. `complete` means complete for declared required scope. `fullLectureCoverage` also requires no excluded objectives. Every exclusion remains visible with a reason; scope narrowing cannot masquerade as covering all lecture concepts. These claims rely on independent semantic audit and the completeness of the approved catalog, and never establish learner mastery.

Every question sourceRefs entry must name a catalog source and an actual page within its pageCount. Missing page references block the full-coverage gate even when an older standalone choice bank allowed them. Put labeled external correction URLs in the catalog source-issue externalRefs record and question explanation; do not disguise them as lecture-file references. A separately supplied supplemental PDF can be cataloged and fingerprinted explicitly.
