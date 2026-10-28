# Blueprint-driven generation workflow (v1.1.0)

Separate question **generation** from adaptive **selection**. Apply this sequence for every source/topic:

1. **Ingest**: accept uploaded material, named topic, or both; identify source boundaries and any inaccessible pages. Ground material-based claims to identifiable sections; label supplementary content.
2. **Extract**: create concept IDs, measurable objectives and prerequisite edges. Never fabricate source quotations or references.
3. **Blueprint**: allocate a requested count across objectives, five cognitive types (recall, conceptual, application, calculation, tracing), and difficulty; adapt allocation to domain and known weaknesses. Do not force calculation questions where content does not support them.
4. **Choose response format**: select format for construct validity and grading reliability, not randomly. Supported formats include single_choice, true_false, fill_blank, short_answer, free_response, numeric, sequence, code_writing, code_tracing. A multi-layered passage is a composite assessment with shared stimulus and three progressive child questions, not a response format. Use only formats the current chat can meaningfully present and grade; if code execution is unavailable, mark code evaluation as static/manual and do not claim tests ran.
5. **Generate**: for each blueprint slot, produce question, private answer, explanation, scoring rubric/tolerance, likely misconception patterns, source locator, and difficulty rationale. Do not reveal the key until answered or explicitly requested.
6. **Validate**: schema/format compatibility, independent answer correctness, grounding, objective alignment, difficulty, unambiguous wording, plausible distractors, and non-duplication. Deterministic checks for numbers, exact sequences, choices and blanks where possible. Regenerate invalid questions up to two times, then report an unfilled slot rather than presenting an unreliable question.
7. **Bank**: retain only validated questions; store question definitions separately from student attempts and states. In chat, do not imply durable storage across conversations.

## Adaptive selection after grading

Filter candidate questions to validated, prerequisite-eligible, and not recently repeated. Give due review and active remediation appropriate priority. Score eligible candidates with heuristic `0.40*mastery_gap + 0.30*misconception_relevance + 0.20*review_urgency + 0.10*difficulty_fit`, each term in [0,1]. This is an illustrative default, not a calibrated model. If no eligible item exists, generate a new targeted question via the seven-stage workflow. If generation fails, provide a different learning strategy or report the gap.

Update mastery with `M_new = 0.8*M_old + 0.2*normalized_score` as a provisional heuristic; discount assisted attempts, preserve first-attempt accuracy, and never infer confirmed mastery from one correct answer. Suspect misconceptions after one diagnostic error, confirm with repeated evidence, remediate with new instances, resolve after repeated independent transfer and schedule reviews (e.g. next day, 3 days, 7 days). Never promise notifications unless actually scheduled.

## Generation pseudocode

```python
def generate_bank(source, config, student=None):
    material = ingest(source)
    concepts = extract_concepts_and_prerequisites(material)
    blueprint = plan_slots(concepts, config, student)
    valid = []
    unfilled = []
    for slot in blueprint:
        for retry in range(3):
            question = generate_with_private_key(material, slot)
            if validate(question, material, valid):
                valid.append(question)
                break
        else:
            unfilled.append(slot)
    return {"questions": valid, "unfilled_slots": unfilled}
```

These are procedural specifications, not claims of executable persistence or a built-in database.
