# Project attempt records

Use an authorized learner-record root if available, otherwise keep session-only evidence and explicitly say that nothing was persisted. Do not invent automatic syncing, a backend, GitHub connection, or cross-session storage.

When persistence is authorized, store each project's attempts under `<learning-root>/projects/<project-slug>.json`, separately from learning concept schedules. Use one schema:

```json
{
  "schema_version": "project-attempts-v1",
  "project_id": "project-slug",
  "title": "Project title",
  "source_locator": null,
  "requirements": [],
  "attempts": [
    {
      "id": "stable-unique-id",
      "timestamp": "ISO-8601-with-timezone",
      "task": "task identifier",
      "artifact_summary": "what was submitted",
      "test_evidence": [],
      "criterion_results": {
        "correctness": "observed / failed / unknown",
        "completeness": "observed / missing / unknown",
        "reasoning": "independent / supported / unknown",
        "debugging": "independent / supported / unknown"
      },
      "support_history": [
        {"level": 0, "kind": "assessment", "summary": "feedback only"}
      ],
      "highest_assistance_level": 0,
      "feedback": "specific evidence, no invented mastery score",
      "next_action": "one concrete step"
    }
  ]
}
```

Use unique attempt IDs, append rather than overwrite, preserve unknown fields, and track fresh attempts separately. Level 0 means no solution help, not proof of independence: independence is evidenced by the work's provenance and reasoning. If the learner explicitly requests that project findings inform Learning Mode practice, cross-reference relevant concept IDs without inserting invented recall ratings. Never overwrite existing learning schedule records with project results. On close, disclose storage destination only if an actual write succeeded.
