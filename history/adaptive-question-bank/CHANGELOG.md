# adaptive-question-bank changelog

## 2.2.1 — 2026-11-03T07:05:56.762719Z

Release ID: `pluginrel_6ae987d4c3348191979df544468c57a1`. Current at import: true.

- Clarified that bounded Exam Mode and preplanned Quiz Mode batches are generated and validated before rendering.
- Clarified that truly adaptive corrective Quiz Mode uses a conversational one-question-at-a-time loop, grading the current item before generating and validating the next.
- Prevented silent replacement of questions inside a preplanned Quiz Mode batch.
- Changed: `.codex-plugin/plugin.json`, `plugin.json`, and `skills/adaptive-question-bank/SKILL.md`.

## 2.2.0 — 2026-11-03T07:02:58.462452Z

Release ID: `pluginrel_6ae98722765481919ff80d652fc0e8fd`. Current at import: false.

- Renamed user-facing modes to Exam Mode and Quiz Mode while preserving legacy commands, stored mode values, and event types.
- Added provisional conceptual/procedural/arithmetic/strategic error diagnosis with mixed/unclear states and qualitative uncertainty.
- Added optional confidence capture before correctness feedback, with separate post-feedback estimates and conservative calibration interpretation.
- Added explicit unassisted/scaffolded/solution-exposed/unknown support tracking and independent-window rules.
- Added guarded unassisted checkpoints, near/far transfer, and multi-session review requirements.
- Preserved fixed Exam Mode questions, locked original scoring, one-question-at-a-time navigation, reliable grading, and post-exam-only remediation.
- Added: `skills/adaptive-question-bank/references/evidence-and-transfer.md`
- Changed: `.codex-plugin/plugin.json`, `plugin.json`, `skills/adaptive-question-bank/SKILL.md`, agent metadata, and supporting references.

## 2.1.0 — 2026-10-31T16:11:25.949610Z

Release ID: `pluginrel_6ae6132df30c8191a6051a245918b4b8`. Current at import: false.

Changes reconstructed by comparing the verified installed release with repository version 2.0.0.

- Added the default single-window multi-question interface with one visible question at a time, Previous/Next controls, direct navigation, retained answers, progress, and one final batch submission.
- Preserved conversational question-by-question practice on explicit request.
- Changed: `.codex-plugin/plugin.json`
- Changed: `plugin.json`
- Changed: `skills/adaptive-question-bank/SKILL.md`

## 2.0.0 — 2026-10-26T14:59:10.737722Z

Release ID: `pluginrel_6adf6abebcd48191add23e46cadc2ae3`. Current at import: true.

Changes reconstructed from stored file differences; original release notes were not returned.

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/adaptive-question-bank/SKILL.md`

## 1.5.0 — 2026-10-25T12:25:54.392433Z

Release ID: `pluginrel_6addf55264648191b83a871ddfbdff34`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/adaptive-question-bank/references/post-exam-diagnosis.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/adaptive-question-bank/SKILL.md`

## 1.4.0 — 2026-10-25T12:09:16.839939Z

Release ID: `pluginrel_6addf16cd7008191b24a4ed89ce53f37`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/adaptive-question-bank/references/layered-exams.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/adaptive-question-bank/SKILL.md`

## 1.3.0 — 2026-10-25T11:59:55.016629Z

Release ID: `pluginrel_6addef3b04388191aad38293280d26f7`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/adaptive-question-bank/SKILL.md`

## 1.2.1 — 2026-10-24T15:33:27.614127Z

Release ID: `pluginrel_6adccfc79d30819188d6348c7927503c`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `plugin.json`

- Changed: `.codex-plugin/plugin.json`

- Changed: `skills/adaptive-question-bank/agents/openai.yaml`

## 1.2.0 — 2026-10-23T05:59:31.242683Z

Release ID: `pluginrel_6adaf7c33e18819192467bd17ab83240`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/adaptive-question-bank/references/visualizations.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `skills/adaptive-question-bank/SKILL.md`

## 1.0.0 — 2026-10-23T05:26:24.539297Z

Release ID: `pluginrel_6adaf0008a088191a5f73ef421ca8c78`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Earliest accessible snapshot; earlier history is unknown.
