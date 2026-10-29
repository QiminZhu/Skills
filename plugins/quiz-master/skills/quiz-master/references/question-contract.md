# BankQuestion v3 contract

The output is a JSON array of objects with these fields:

```ts
type QuestionType = "single" | "multiple" | "boolean" | "matching" | "ordering" | "fill_blank";
type Difficulty = "Easy" | "Medium" | "Hard";
type CognitiveLevel = "Remember" | "Understand" | "Apply" | "Analyze" | "Evaluate" | "Create";
type SourceRef = { file: string; page?: number };
type ChoiceQuestion = {
  id: string;
  subject: string;
  topic: string;
  objectiveId: string;
  type: "single" | "multiple" | "boolean";
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

## Discriminated additions (v2 choices remain valid)
All variants are JSON objects sharing the choice metadata fields: id, subject, topic, objectiveId, difficulty, cognitiveLevel, prompt, explanation, sourceRefs, status, version, and optional tags. Every new item starts as draft. Do not include answers/correct/optionExplanations on the new variants, or type-specific keys from a different variant.

```ts
type Common = Omit<ChoiceQuestion, "type" | "answers" | "correct" | "optionExplanations">;
type MatchingQuestion = Common & {
  type: "matching"; leftItems: string[]; rightItems: string[];
  reuseRight: boolean; matches: [number, number][];
  pairExplanations: string[];
};
type OrderingQuestion = Common & {
  type: "ordering"; items: string[]; correctOrder: number[];
  stepExplanations: string[];
};
type TextBlank = {
  id: string; kind: "text"; acceptedAnswers: string[];
  caseSensitive: boolean; trim: boolean; collapseWhitespace: boolean;
  explanation: string;
};
type NumberBlank = {
  id: string; kind: "number"; value: number; absoluteTolerance: number;
  unit: string; rounding: string; explanation: string;
};
type FillBlankQuestion = Common & {type: "fill_blank"; blanks: (TextBlank | NumberBlank)[]};
type BankQuestion = ChoiceQuestion | MatchingQuestion | OrderingQuestion | FillBlankQuestion;
```

### Matching
Require at least two left and two right labels, unique within each side. Each left index occurs exactly once in matches; each pair indexes leftItems and rightItems respectively. If reuseRight=false, right indexes must be distinct; unused right distractors are allowed. pairExplanations align with matches. In the displayed prompt state whether right options may be reused and whether some may be unused. Grade the student's map by pairs, independent of pair-list order.

### Ordering
Require at least three unique item labels. correctOrder is a permutation of all zero-based item indexes, in the requested first-to-last order. stepExplanations align with correctOrder, not presentation order. Present items out of correct order; if shuffling, remap indexes together. Grade the full ordered list; do not sort it.

### Fill-in-the-blank
Each prompt marker is `{{id}}`, with IDs sequential strings "1", "2", ...; each appears once and matches one blanks entry in order. Require at least one blank. Text: normalize the response and each accepted answer identically, using only the declared rules: trim, collapse whitespace, then casefold if caseSensitive=false. Match an exact normalized accepted answer; do not use substring or fuzzy matching. Do not strip punctuation or accept unrelated synonyms silently. Numeric: require finite numbers; reject NaN/infinity and empty responses; convert a complete numeric input, not a numeric prefix. Accept iff abs(response-value) <= absoluteTolerance (inclusive). Units are displayed beside the blank and specified in the prompt; unit strings may be empty only for dimensionless values. State rounding in the prompt, using "none" if no rounding is required. Do not silently convert units. Every blank has its own explanation.

Default grading is all-or-nothing per question; partial credit only when explicitly configured and disclosed by the consumer. Keep answer keys and explanations hidden during attempts. No answer UI or grader is implemented merely by exporting this schema.

## v1.3 optional objective links
Every question retains its existing primary `objectiveId`. Optional `objectiveIds: string[]` lists unique catalog IDs, includes objectiveId, and contains exactly the IDs targeted by the sidecar mapping. These links are author claims until separately validated. They never replace response-part evidence in the coverage ledger. Do not introduce a seventh calculation answer type; numeric calculation remains a fill_blank variant when the source supports it.
