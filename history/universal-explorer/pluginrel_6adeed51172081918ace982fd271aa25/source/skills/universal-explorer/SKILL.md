---
name: universal-explorer
description: Explore unfamiliar concepts, ideas, techniques, apps, products, technologies, and proposals through structured critical questioning. Use when the user encounters something new and wants to understand it deeply, challenge claims, compare alternatives, investigate evidence, or decide whether to use or implement it. Supports quick, deep, and research exploration with adaptive follow-up questions.
---

# Universal Explorer v1.0.0

## Mission
Turn an unfamiliar subject into an evidence-aware, adaptive investigation. Maximize useful uncertainty reduction rather than the number of questions asked. Do not automatically convert exploration into a quiz.

## Intake
Identify the subject, category (concept/theory, technique/technology, app/product, idea/proposal), goal (understand, evaluate, apply), and depth (quick, deep, research) from the user's message. Ask only for essential missing information; default to deep understanding if unspecified. Accept pasted descriptions, documents, links, or just a topic. Distinguish known facts, provisional interpretations, and unknowns. Use available tools for source retrieval where warranted, never invent source contents.

## Seven-stage investigation
Use the question bank in [references/questions.md](references/questions.md). Adapt the order and skip irrelevant stages.
1. Orientation: define, classify, map components, establish prerequisites.
2. Motivation: problem, origins, prior solutions, historical context.
3. Mechanism: steps, dependencies, assumptions, causal links.
4. Relationships: alternatives, comparisons, connections, trade-offs.
5. Critical evaluation: evidence, counterexamples, limitations, confounders, uncertainties.
6. Application: use cases, feasibility, tests, prediction, improvement.
7. Reflection: summarize in own words, check understanding, identify gaps, prioritize next question.

## Operating loop
1. Start with a compact orientation (2-5 sentences) clearly marking uncertainty.
2. Propose 3-7 high-value, subject-specific questions grouped by the most relevant stages. For quick mode use 3-5 total; for deep mode investigate 1-3 branches thoroughly; for research mode systematically seek primary evidence, alternatives, and limitations.
3. Prioritize questions by relevance to user's goal, expected information gain, specificity, and testability. These are qualitative heuristics, not numerical evidence.
4. Answer or investigate the leading question, showing the key evidence and reasoning. Do not imply unverified claims are proven.
5. Branch according to discoveries: performance claim -> evidence and benchmark conditions; architectural novelty -> mechanism and comparison; unclear claim -> operational definition; unknown jargon -> prerequisite; failure -> constraints and counterexamples; practical interest -> small experiment.
6. Periodically summarize established findings, assumptions, unresolved questions, and recommended next investigation. Stop or pivot when marginal value declines.
7. If user wants interactive inquiry, ask ONE targeted question at a time and await response. If user asks for a full report, provide a structured multi-question analysis without unnecessary interruptions.

## Contextual adaptation
- Concepts/theories: favor definition, assumptions, causal models, falsifiability, counterexamples.
- Techniques/technologies: favor mechanism, prerequisites, architecture, alternatives, trade-offs, reproducible tests.
- Apps/products: favor user problem, differentiators, evidence for claims, pricing/constraints when sourced, privacy/security considerations when material.
- Ideas/proposals: favor target problem, assumptions, feasibility, alternatives, failure modes, minimal experiments.
- Do not assume all 24 patterns are necessary. Treat them as a toolbox, not a checklist.

## Quality and safeguards
- Separate observation from inference and speculation; cite retrieved evidence when available.
- Prefer precise, falsifiable questions over broad rhetorical questions. Challenge premises when necessary.
- Do not assert that a technology is superior without comparative evidence and stated conditions.
- Match depth to user intent; avoid repetitive lists and superficial question inflation.
- Offer transitions to structured Learning, Review, or Project work when the user requests them; do not claim integration with another plugin or persistent tracking.

## Default output
**Orientation:** brief explanation and relevant context.
**Question map:** prioritized questions with thinking-pattern labels and short rationale.
**Investigation:** evidence, comparisons, limitations, examples/experiments as relevant.
**Synthesis:** what is established, uncertain, and the highest-value next question.
For interactive mode, replace the full investigation with one question and await response.
