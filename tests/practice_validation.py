"""Run with python3 tests/practice_validation.py from the repository root."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('practice_renderer', root / 'plugins/learn-tutor-plugin/skills/learn-combined/scripts/render_practice.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
question = dict(id='fixture', question='What is 2 + 2?', source='Synthetic arithmetic fixture, not lecture content', objective='Add two integers', continuation='Teach the next arithmetic concept.', correct_id='right', explanation='2 + 2 equals 4.', validation=dict(source_checked=True, independent_check='Python independently computed 2 + 2 == 4'), options=[dict(id='right', label='4', feedback='Adding two pairs gives four.'), dict(id='wrong', label='5', feedback='Five is one more than the sum.')])
assert 2 + 2 == int(question['options'][0]['label'])
for field in ['source', 'correct_id', 'validation']:
    bad = question.copy()
    bad.pop(field)
    try:
        module.render(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(field)
bad = dict(question, options=[question['options'][0], question['options'][0]])
try:
    module.render(bad)
except ValueError:
    pass
else:
    raise AssertionError('duplicate options')
assert module.render(dict(question, explanation='</script><script>alert(1)</script>')).count('<script>') == 1
with tempfile.TemporaryDirectory() as tmp:
    output = Path(tmp) / 'practice.html'
    source = Path(tmp) / 'question.json'
    source.write_text(json.dumps(question))
    subprocess.run(['python3', str(spec.origin), str(source), str(output)], check=True)
    subprocess.run(['node', str(root/'tests/practice-runtime.cjs'), str(output)], check=True)
print('Practice renderer validation passed. Host message API is mocked; live ChatGPT rendering remains unverified.')
