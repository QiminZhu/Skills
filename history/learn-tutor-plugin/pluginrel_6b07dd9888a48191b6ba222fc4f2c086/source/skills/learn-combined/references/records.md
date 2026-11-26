# Canonical learner records

Use one topic JSON file at `<learning-root>/topics/<topic-slug>.json`. Keep preferences in `<learning-root>/profile.json` only when useful; do not require onboarding. Use safe relative slugs and stable concept IDs. Human-readable values follow the learner's language; field names remain stable English identifiers.

A topic record has `schema_version`, `topic`, `updated_at`, and `concepts`. Each concept has `id`, `label`, `prerequisite_ids`, `attempts`, and `schedule`. Each attempt has a unique `id`, ISO timestamp with timezone, `session_id`, objective, question or task summary, source locator if available, evidence category, response summary, outcome, support (`independent`, `prompted`, `scaffolded`), specific feedback, and optional misconception note. Recognition, explanation, familiar application, and transfer are evidence categories; keep their results separate.

Schedule fields include method, last review time, next review date, and the state required by that method. For FSRS retain library/version, parameters, retention target, timezone policy, item state, and review log; never discard information required to reproduce the next interval.

Use a stable recall item ID and prompt/answer criterion per schedulable item. A concept may have multiple recall items. Different transfer tasks contribute understanding evidence without automatically becoming reviews of the same memory item.

Read before writing and preserve unknown fields. Write an updated copy atomically where supported, retain a recoverable previous copy, and deduplicate attempts by ID on retries. If concurrent changes are detected, merge append-only attempts by ID and recalculate derived values; do not overwrite unseen work. Report write failures accurately and retain a session summary for recovery.

Derive dashboards from attempts and scheduling state; do not maintain separately editable summary totals. Show due items, evidence by category and support, recurring gaps, and last assessment dates. Label unassessed abilities as unknown. Do not turn interval length into proficiency badges.
