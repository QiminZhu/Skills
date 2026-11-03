
## Shared mastery integration v0.4
- Preserve Learning, Review and Project workflows and immediate learning feedback.
- If available and authorized, retrieve topic IDs and mastery from Update it before targeted teaching or review. If not available, use supplied materials and state that current tracker status was not retrieved.
- Emit structured learning evidence with topicId, eventId, sessionId, cognitiveType, firstAttemptCorrect, reasoning, supportLevel, timestamp and source `tutor-me`. Submit through a verified shared tool only when available; otherwise offer portable JSON at session end.
- Learning, review, project and post-teaching verification evidence NEVER authorizes increasing mastery. Only Update it can apply mastery changes from qualifying completed Quiz me formal assessments.
- Avoid per-turn remote writes; batch at session end where possible without relying on inaccessible old chat context. Do not promise background work or claim writes succeeded without confirmation.
