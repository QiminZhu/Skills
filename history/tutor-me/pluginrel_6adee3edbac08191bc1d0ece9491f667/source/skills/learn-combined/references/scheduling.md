# Scheduling recall separately from understanding

Schedule an item after its first recall assessment, including failure. A successful explanation during instruction or a hinted answer does not establish unaided recall.

## FSRS when an implementation is available

Use an installed, tested FSRS library through the environment's execution tools. Identify its version and preserve its required state and settings. Use its documented default parameters and retention target unless a valid existing configuration or user preference supplies them. Do not hand-calculate approximate equations and call them FSRS. Record review timestamps and the learner's local timezone. Preserve existing schedule configuration on resume.

For each fixed recall item, rate only its unaided response: Again for failure; Hard for correct recall with substantial difficulty; Good for ordinary correct recall; Easy only for clearly effortless correct recall. Partial or incorrect recall is Again, not Hard. If effort is ambiguous, use Good for a correct response rather than inferring Easy from prose. Support before answering means unaided recall was not demonstrated; retain the assisted practice evidence separately. Do not infer a rating for a different item from success on a transfer problem. Apply the library's handling of elapsed time and same-day reviews.

## Transparent fallback

When FSRS cannot run, disclose `simple-review-v1`; it is a heuristic, not FSRS. Start a new fallback item at stage 0. After an independent correct review, advance one stage through intervals of 1, 3, 7, 14, and 30 calendar days; cap at 30. After failed recall, reset to stage 0 and recommend the next calendar day, with optional fresh practice now. Do not change the stage for instruction or unscored supported practice. Use the learner's local date and record the actual review time. Keep earlier review history if changing methods; do not translate stages into invented FSRS stability.

If dates or execution are unavailable, recommend a next review in plain language without claiming calculated FSRS dates. Never promise reminders unless a separate reminder mechanism has actually been authorized and configured.
