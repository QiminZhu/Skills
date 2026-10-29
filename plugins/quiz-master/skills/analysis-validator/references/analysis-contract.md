# Analysis audit contract

JSON object: `{catalogHash, sourceVersions, decision, checks, issues}`.
- `catalogHash`: SHA-256 of the exact catalog JSON canonicalized with Python `json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")`. Use this same canonicalization for all question/ledger hashes.
- `sourceVersions`: array of `{file, version}` copied from the actual inspected source fingerprints. `version` is the actual SHA-256 source-byte hash; supplied revision labels may be stored separately.
- `decision`: `approved`, `revision_required`, or `rejected`.
- `checks`: `sourceAccess`, `pageAccounting`, `conceptCompleteness`, `sourceGrounding`, `objectiveAtomicity`, `consistency`, `sourceIssues`; each `pass`, `fail`, or `unverified`.
- `issues`: array of `{severity, finding, sourceRefs, objectiveIds?, proposedFix?}`. Severity is `major` or `minor`.
Approve only when all checks pass and every issue is resolved; do not approve with unresolved minor issues. Status `reviewed` on a catalog alone proves nothing. If issuing a revised reviewed catalog copy, hash that final copy, never the earlier draft. Preserve reports independently of catalog and questions.
