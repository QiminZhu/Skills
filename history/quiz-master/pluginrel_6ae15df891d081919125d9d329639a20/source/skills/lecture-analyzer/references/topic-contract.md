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
