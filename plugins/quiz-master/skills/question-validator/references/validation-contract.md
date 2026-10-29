# Validation report contract

Return JSON `{questionId, questionVersion, contentHash?, checks, issues, decision}` per item. `checks` has `schema`, `independentAnswer`, `optionExplanations`, `overallExplanation`, `sourceGrounding`, `objectiveAlignment`, `ambiguity`, `distractors`, `difficulty`, `cognitiveLevel`; each is `pass`, `fail`, or `unverified`. `issues` is an array of `{severity, field, finding, evidence?, proposedFix?}`. `decision` is `approved`, `revision_required`, or `rejected`.

Only approve when all critical checks pass and evidence is available. The validated content hash must cover the exact question payload, including prompt, answer ordering, correct indexes, explanations, references and version. Store reports separately from published BankQuestion JSON. Never assert an item was approved if the independent review was not actually performed.

For new types replace the choice-only optionExplanations check with responseExplanations (pair, step, or blank explanations). Keep all other checks. Hash every variant-specific key, explanation, normalization, reuse and numerical grading policy as part of the exact payload.

## v1.3 coverage binding
Use the canonical hashing defined in the Analysis Validator contract. `decision: approved` requires every applicable check pass and issues empty. `contentHash` binds the exact final approved question copy; questionVersion must match. Add `coverageMappings` check when a ledger is supplied. Mapping verdicts are issued separately in the ledger and bind the same question hash and canonical catalog hash. Any question or ledger edit requires revalidation. Preserve generated draft originals separately; never infer approval from status alone.
