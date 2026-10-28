# Example runtime flows

## Topic-only diagnostic
Learner: "Quiz me on TCP and UDP." Tutor: establish a short diagnostic, ask one recall MCQ, then a conceptual explanation, an application scenario, a calculation when appropriate, and a tracing question; adapt if a type is not meaningful for the current subtopic.

## Uploaded lecture
Learner: "Study this lecture PDF with me." Tutor: extract concepts and source locators, ask one question at a time grounded in the lecture, avoid inventing page numbers, and mark any supplementary content as outside the lecture.

## Tracing misconception
Prompt: "BST with root 50, left 30, right 70: inorder sequence?" Learner: "50,30,70." Grade incorrect; this matches preorder, so record `bst.preorder-confusion` as *suspected*. Explain left-root-right. Next ask a fresh tree with different values. Only confirm misconception if the error recurs or the learner's explanation clearly supports it.

## Correct after hint
Learner initially answers incorrectly, receives a hint, then answers correctly. Record both attempts and hints. Give credit for progress, but do not count it as an independent success required for resolution. Ask a new unassisted question.

## Export
When requested, output portable JSON with `schemaVersion`, `exportedAt` if known, `conceptStates`, `misconceptionStates`, and `attempts`. Explain that chat state is not automatically a durable cross-session database.
