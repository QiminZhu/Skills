# Tutor me 0.11.0 acceptance scenarios

These are synthetic policy walkthroughs reviewed against the packaged instructions, not automated learner conversations. Runtime tests cover the HTML handoff separately. Re-run these scenarios in a live host to assess model adherence; structural checks alone cannot prove learning outcomes.

| Scenario | Required result | Policy walkthrough |
| --- | --- | --- |
| A concept appears only in a diagram label | Inspect the diagram and map the instructional detail to an objective | Covered by complete inventory and second semantic pass |
| An exercise introduces a skill absent from headings | Extract and source the skill, rather than relying on headings | Covered by source-to-objective audit |
| A theoretical concept has no implementation content | Mark not_found or not_applicable with a reason; no fabricated required code | Covered by facet classification |
| The unreadable last page might contain implementation | Mark unresolved/uninspected; do not claim not_found or analysis complete | Covered by uncertainty rule and completion gate |
| Two source sections disagree | Flag the conflict; no silent reconciliation or complete-analysis claim | Covered by inventory and audit |
| A concept spans two lectures | Keep one concept with both locators and preserve distinct objectives | Covered by concept map |
| The learner asks only about one slide | Give a scoped short summary and answer; no compulsory whole-lecture audit | Covered by scope and summary exceptions |
| A whole lecture is uploaded | Analyze, then summarize big picture, connected concepts, outcomes, order and gaps BEFORE tutoring or diagnostic | Covered by opening sequence |
| The lecture contains no exercises | Generate aligned practice; browse when requested/useful and available | Covered by practice-sourcing policy |
| Browsing is unavailable | Disclose that fact and use labeled tutor-created practice | Covered by sourcing fallback |
| An online problem requires untaught concepts | Reject/adapt or explicitly teach and label extra prerequisites; do not alter required coverage | Covered by external-item scope checks |
| An online key is incorrect or ambiguous | Solve independently, revise/reject, permit defensible alternatives | Covered by answer-key validation |
| The learner independently solves a basic item clearly | Advance to the next meaningful demand for that objective | Covered by evidence-based progression |
| The learner guesses correctly | Check the missing evidence; do not treat recognition as reasoning | Covered by ambiguous-answer rule |
| The learner answers correctly after a hint | Fresh comparable unassisted check before evidence-based advancement | Covered by assistance and checkpoint rules |
| Wrong answer, feedback, then correct widget retry | Handoff preserves both attempts and marks prior feedback; success is supported | Exercised in practice-runtime.cjs |
| The learner changes selection after feedback without submitting | Latest attempt is null but history/feedback remain; do not invent new success | Exercised in practice-runtime.cjs |
| The learner presses Next without answering | No success inferred; no attempt and empty history | Exercised in practice-runtime.cjs |
| Advanced tracing but weak complexity explanation | Adapt separately; preserve tracing evidence | Covered by per-objective progression |
| A correct basic answer for a reasoning target | Leave target-depth verification pending | Covered by evidence criterion and completion gate |
| A simple factual objective | Do not force five levels or transfer | Covered by relevant-level rule |
| One arithmetic slip in otherwise sound reasoning | Diagnose and correct locally; no blanket reset | Covered by adaptive next-task rule |
| The learner skips one required concept | Deferral visible; full-lecture teaching completion false | Covered by completion gates |
| An explanation needs an essential condition | Expand beyond brief default for accuracy | Covered by brief-first exception |
| A learner asks for the answer or harder questions | Honor the request; label support and do not fabricate passed levels | Covered by learner-choice rules |
| A single independent success | Report demonstrated depth only; no durable mastery/retention claim | Covered by evidence boundaries |

## Release verification boundaries
- Verify all local Markdown references, both manifest versions, preserved identity/configuration and file inventory.
- Run existing renderer tests plus retry-history cases.
- Preserve an exact pre-update source snapshot with per-file hashes and a reconstructed ZIP.
- Reconstruct the rollback package, test ZIP integrity and compare every payload file to the snapshot before publishing.
- After publishing, compare every returned plugin file with the candidate (JSON semantically), then update release metadata.
- Live teaching, live browsing, and the actual host message bridge remain unverified unless explicitly exercised.
