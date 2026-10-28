# Validation report contract

Return JSON `{questionId, questionVersion, contentHash?, checks, issues, decision}` per item. `checks` has `schema`, `independentAnswer`, `optionExplanations`, `overallExplanation`, `sourceGrounding`, `objectiveAlignment`, `ambiguity`, `distractors`, `difficulty`, `cognitiveLevel`; each is `pass`, `fail`, or `unverified`. `issues` is an array of `{severity, field, finding, evidence?, proposedFix?}`. `decision` is `approved`, `revision_required`, or `rejected`.

Only approve when all critical checks pass and evidence is available. The validated content hash must cover the exact question payload, including prompt, answer ordering, correct indexes, explanations, references and version. Store reports separately from published BankQuestion JSON. Never assert an item was approved if the independent review was not actually performed.
