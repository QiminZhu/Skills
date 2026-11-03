#!/usr/bin/env python3
"""Render one source-validated single-select practice item as an HTML fragment.

Input fields: id, question, source, objective, continuation, correct_id,
explanation, validation {source_checked: true, independent_check: nonempty},
options [{id, label, feedback}, ...]. Factual validation remains the tutor's job.
"""
import argparse
import html
import json
import re
from pathlib import Path


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Question must be a JSON object")
    for key in ("id", "question", "source", "objective", "continuation", "correct_id", "explanation"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"Missing nonempty {key}")
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", data["id"]):
        raise ValueError("id must contain 1–64 letters, digits, hyphens or underscores")
    evidence = data.get("validation", {})
    if not isinstance(evidence, dict) or evidence.get("source_checked") is not True or not isinstance(evidence.get("independent_check"), str) or not evidence["independent_check"].strip():
        raise ValueError("Source and independent-check evidence required; structure is not factual verification")
    options = data.get("options")
    if not isinstance(options, list) or not 2 <= len(options) <= 6:
        raise ValueError("Supply 2–6 defensible options")
    ids, labels = [], []
    for option in options:
        if not isinstance(option, dict) or any(not isinstance(option.get(k), str) or not option[k].strip() for k in ("id", "label", "feedback")):
            raise ValueError("Each option requires id, label and feedback")
        ids.append(option["id"])
        labels.append(option["label"].strip().casefold())
    if len(set(ids)) != len(ids) or len(set(labels)) != len(labels) or data["correct_id"] not in ids:
        raise ValueError("Options must be unique and include exactly one correct_id")
    return data


def render(data):
    validate(data)
    root = "tutor-practice-" + data["id"]
    escape = html.escape
    options = "\n".join(
        f'<label class="form-check"><input class="form-check-input" type="radio" name="{root}-answer" value="{escape(o["id"], quote=True)}"><span class="form-check-label">{escape(o["label"])}</span></label>'
        for o in data["options"]
    )
    # JSON script text cannot terminate the enclosing script, even for source text
    # containing HTML. All dynamic text is inserted through textContent.
    config = json.dumps(data, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    markup = f'''<section id="{root}" aria-label="Practice">
  <form>
    <fieldset><legend>{escape(data['question'])}</legend>{options}</fieldset>
    <button type="submit" class="btn btn-primary">Check answer</button>
  </form>
  <p data-result aria-live="polite" hidden></p>
  <p data-explanation hidden></p>
  <p class="text-small">Source: {escape(data['source'])}</p>
  <div class="viz-row">
    <button type="button" class="btn" data-next>Next</button>
    <button type="button" class="btn" data-challenge hidden>Challenge grade</button>
  </div>
  <p data-status aria-live="polite"></p>
  <textarea class="form-control" data-manual aria-label="Message to send manually" readonly hidden></textarea>
</section>
<script>
(() => {{
  const root = document.getElementById({json.dumps(root)});
  const config = {config};
  const form = root.querySelector('form');
  const result = root.querySelector('[data-result]');
  const explanation = root.querySelector('[data-explanation]');
  const next = root.querySelector('[data-next]');
  const challenge = root.querySelector('[data-challenge]');
  const status = root.querySelector('[data-status]');
  const manual = root.querySelector('[data-manual]');
  let attempt = null;
  let pending = false;
  form.addEventListener('change', () => {{
    attempt = null;
    result.hidden = explanation.hidden = challenge.hidden = true;
    manual.hidden = true;
    status.textContent = '';
  }});
  form.addEventListener('submit', event => {{
    event.preventDefault();
    const selected = root.querySelector('input:checked');
    if (!selected) {{ status.textContent = 'Choose an answer first.'; return; }}
    const option = config.options.find(option => option.id === selected.value);
    if (!option) return;
    attempt = {{answer_id: option.id, answer: option.label, correct: option.id === config.correct_id}};
    result.textContent = attempt.correct ? 'Correct for the prepared key.' : 'Incorrect for the prepared key.';
    explanation.textContent = option.feedback + ' ' + config.explanation;
    result.hidden = explanation.hidden = challenge.hidden = false;
    status.textContent = '';
  }});
  async function send(kind) {{
    if (pending || (kind === 'challenge' && !attempt)) return;
    const context = JSON.stringify({{objective: config.objective, source: config.source, question_id: config.id, question: config.question, attempt}});
    const prompt = kind === 'challenge'
      ? 'Tutor me: recheck this practice grade against the original source, independently checking the key and valid alternatives. Keep this session-only. Context: ' + context
      : config.continuation + '\\nContinue Tutor me in this conversation without mastery tracking or external recording. Context: ' + context;
    manual.value = prompt;
    if (typeof window.openai?.sendFollowUpMessage !== 'function') {{
      status.textContent = 'Automatic messages are unavailable here. Send the text below in chat.';
      manual.hidden = false;
      return;
    }}
    pending = true;
    next.disabled = challenge.disabled = true;
    try {{
      await window.openai.sendFollowUpMessage({{prompt}});
      status.textContent = 'Message requested. Continue in chat.';
      manual.hidden = true;
      // Keep controls disabled after success to avoid duplicate continuation.
    }} catch (error) {{
      status.textContent = 'The message could not be sent. Retry or send the text below in chat.';
      manual.hidden = false;
      next.disabled = challenge.disabled = false;
      pending = false;
    }}
  }}
  next.addEventListener('click', () => send('next'));
  challenge.addEventListener('click', () => send('challenge'));
}})();
</script>
'''
    return markup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question_json", type=Path)
    parser.add_argument("output_html", type=Path)
    args = parser.parse_args()
    try:
        content = render(json.loads(args.question_json.read_text(encoding="utf-8")))
    except (ValueError, OSError) as error:
        parser.error(str(error))
    args.output_html.write_text(content, encoding="utf-8")
    print(args.output_html)


if __name__ == "__main__":
    main()
