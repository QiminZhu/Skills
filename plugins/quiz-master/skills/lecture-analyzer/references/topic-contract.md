# Topic Catalog contract

Produce JSON with:
- `catalogId`: stable identifier; `status`: `draft` or `reviewed`.
- `subject`: source-supported subject name.
- `lectures`: array of `{lectureId, title, sourceFiles, topics}`.
- `sourceFiles`: array of `{file, version?}` where version is a hash or provided revision if known.
- `topics`: array of `{topicId, name, summary, objectives, sourceRefs, prerequisites?}`.
- `objectives`: array of `{objectiveId, statement, cognitiveTargets, sourceRefs, origin}` where origin is `explicit` or `inferred`.
- `sourceRefs`: array of `{file, page?}` with actual 1-based page numbers.
- `cognitiveTargets`: values from Remember, Understand, Apply, Analyze, Evaluate, Create; these are intended cognitive operations, not estimated difficulty.

Ensure unique IDs and real source references. Mark unsupported inferences for review. Quiz Master maps each BankQuestion `objectiveId` to a catalog objective. Keep source text and files available for validation.

## v1.3 coverage additions
Preserve the existing lectures/topics hierarchy. Add root `sourceFiles: [{file, version, pageCount}]`, where version is actual SHA-256 of source bytes. Add each topic's `concepts: [{conceptId, name, sourceRefs}]`. Every objective additionally has `conceptId`, `priority: "core" | "supporting"`, `required: boolean` (default true; require an explicit reason for false), and `exclusionReason` when not required. Objective statements are atomic and assessable; each objective belongs to exactly one concept in its topic. All objective IDs and concept IDs are globally unique.

Add root `pageAccounting: [{file, page, disposition, reason, objectiveIds}]`, one entry for every 1-based page of every source. Dispositions: `included`, `duplicate`, `administrative`, `external_resource`, `unreadable`. Included/duplicate entries reference valid source-supported objective IDs; exclusions state substantive reasons. Unreadable required content blocks complete analysis. Explicitly label any unreachable external resource as uninspected. Changing required scope cannot make excluded material disappear: report it separately.

Add root `sourceIssues: [{sourceRefs, finding, status, resolution, externalRefs?}]`, status `unresolved` or `resolved`. External corrections must be labeled and carry real authoritative references; never invent citations. Unresolved assessable contradictions block analysis approval. Preserve source terminology where accurate. An analysis approval report binds the exact catalog and source versions; catalog status alone is not approval.
