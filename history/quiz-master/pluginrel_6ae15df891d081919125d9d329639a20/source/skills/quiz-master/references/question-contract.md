# BankQuestion v2 contract

The output is a JSON array of objects with these fields:

```ts
type QuestionType = "single" | "multiple" | "boolean";
type Difficulty = "Easy" | "Medium" | "Hard";
type CognitiveLevel = "Remember" | "Understand" | "Apply" | "Analyze" | "Evaluate" | "Create";
type SourceRef = { file: string; page?: number };
type BankQuestion = {
  id: string;
  subject: string;
  topic: string;
  objectiveId: string;
  type: QuestionType;
  difficulty: Difficulty;
  cognitiveLevel: CognitiveLevel;
  prompt: string;
  answers: readonly string[];
  correct: readonly number[];
  explanation: string;
  optionExplanations: readonly string[];
  sourceRefs: readonly SourceRef[];
  status: "draft" | "pending_review" | "approved" | "rejected";
  version: number;
  tags?: readonly string[];
};
```

All newly generated questions have `status: "draft"`. `objectiveId` must match the provided catalog or a clearly provisional generated objective. Use actual file names and 1-based PDF page numbers. Missing citations must not be filled with invented references; flag the item separately for review. `optionExplanations[i]` must justify or refute `answers[i]` under the complete prompt. The published website can consume this same format, filtering for approved questions. Validation reports and source material should be stored separately.
