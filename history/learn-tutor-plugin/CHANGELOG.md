# learn-tutor-plugin changelog

## 0.8.0 — 2026-10-30

- Make the default Learning Mode sequence explicit: Teach → Practice → Check Answer → Next.
- Require original uploaded lecture visuals when available; do not generate or redraw replacement diagrams for source visuals.
- Specify immediate local correctness feedback and explanation for objective practice, with a separate Next action that does not auto-advance.
- Add a defined multi-question assessment experience: question count, per-item feedback, final score, incorrect-answer review, retake and separate Next.
- Tighten answer-key QA for distractor uniqueness, cumulative versus individual ACK semantics, sequence-number wraparound, and window boundaries.
- Keep learning session-only with no mastery tracker, persistent records, progress sync, external recording, review scheduling or cross-plugin handoffs.
- Preserve existing project/review skills, renderer and plugin identity.
- Validation: both manifests parsed; overlay archive inventory checked; plugin update succeeded; all four changed plugin paths read back at v0.8.0. Live host rendering and message handoff were not verified.
- Publication: backend release ID: `pluginrel_6ae4ba02ad40819192044207ba1e0ad2`; overlay archive SHA-256: `92c59cb42667d26888f2eb887fce43b240f2dfc5fe00dea31b35770c31605317`.

# learn-tutor-plugin changelog

## 0.7.0 — 2026-10-28

- Add slide-first visual reuse and reliable online visual fallback.
- Require source-based answer-key verification, independent solving, per-option explanations and grade challenges.
- Add a reusable local single-select practice renderer with separate Next message handoff, duplicate prevention and manual fallback.
- Make the lesson flow session-only, including transitions to Review and Project Mode.
- Preserve plugin identity, audience, existing assessment guidance and all unrelated files.
- Validation: Python renderer input checks, script-escaping checks, mocked JavaScript interaction checks, YAML/JSON parsing, retained-file and metadata comparison. Live ChatGPT widget rendering/message handoff not verified.
- Publication: saved and all 15 files verified. Backend release ID: `pluginrel_6ae208d059e081918046a836d0f57c8d`. Created: 2026-10-28T14:38:08.351237Z.


## 0.6.0 — 2026-10-28T07:07:25.929481Z

Release ID: `pluginrel_6ae19f2dedec819187b85f56bacb6427`. Current at import: true.

Changes reconstructed from stored file differences; original release notes were not returned.

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/learn-combined/SKILL.md`

- Removed: `skills/learn-combined/references/mastery-integration.md`

## 0.5.0 — 2026-10-27T12:36:29.538423Z

Release ID: `pluginrel_6ae09acd89cc8191a3548dbf5a681cf8`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/learn-combined/references/lecture-coverage.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/learn-combined/SKILL.md`

## 0.4.0 — 2026-10-26T14:59:29.909541Z

Release ID: `pluginrel_6adf6ad1e8d08191beba10bead736249`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/learn-combined/references/mastery-integration.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/learn-combined/SKILL.md`

## 0.3.0 — 2026-10-26T05:23:57.729636Z

Release ID: `pluginrel_6adee3edbac08191bc1d0ece9491f667`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/review-mode/SKILL.md`

- Added: `skills/review-mode/references/review-policy.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/learn-combined/SKILL.md`

## 0.2.0 — 2026-10-25T12:06:23.002474Z

Release ID: `pluginrel_6addf0bf009c8191a79cd1a951647970`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Added: `skills/project-assessment/SKILL.md`

- Added: `skills/project-assessment/references/project-records.md`

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

- Changed: `skills/learn-combined/SKILL.md`

## 0.1.1 — 2026-10-24T15:33:45.428682Z

Release ID: `pluginrel_6adccfd96db48191bc50517576eb54d2`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Changed: `.codex-plugin/plugin.json`

- Changed: `plugin.json`

## 0.1.0 — 2026-10-22T06:52:26.509796Z

Release ID: `pluginrel_6ad9b2aa82788191b515540ec162bb9c`. Current at import: false.

Changes reconstructed from stored file differences; original release notes were not returned.

- Earliest accessible snapshot; earlier history is unknown.
