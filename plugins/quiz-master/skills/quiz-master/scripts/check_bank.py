#!/usr/bin/env python3
"""Check structural integrity of a draft BankQuestion JSON array.

Usage: python scripts/check_bank.py questions.json
Does not verify factual correctness or source grounding.
"""
import json
import sys
from pathlib import Path

TYPES = {'single', 'multiple', 'boolean'}
DIFFICULTIES = {'Easy', 'Medium', 'Hard'}
COGNITIVE = {'Remember', 'Understand', 'Apply', 'Analyze', 'Evaluate', 'Create'}
REQUIRED = {'id', 'subject', 'topic', 'objectiveId', 'type', 'difficulty', 'cognitiveLevel', 'prompt', 'answers', 'correct', 'explanation', 'optionExplanations', 'sourceRefs', 'status', 'version'}


def validate_bank(bank):
    issues = []
    if not isinstance(bank, list):
        return ['Root must be a JSON array']
    ids = set()
    for i, q in enumerate(bank):
        p = f'question[{i}]'
        if not isinstance(q, dict):
            issues.append(f'{p}: must be an object')
            continue
        for key in sorted(REQUIRED - q.keys()):
            issues.append(f'{p}: missing {key}')
        if 'levels' in q:
            issues.append(f'{p}: forbidden levels attribute')
        ident = q.get('id')
        if not isinstance(ident, str) or not ident.strip() or ident in ids:
            issues.append(f'{p}: missing or duplicate id')
        else:
            ids.add(ident)
        for key in ('subject', 'topic', 'objectiveId', 'prompt', 'explanation'):
            if not isinstance(q.get(key), str) or not q[key].strip():
                issues.append(f'{p}: invalid {key}')
        if q.get('type') not in TYPES or q.get('difficulty') not in DIFFICULTIES or q.get('cognitiveLevel') not in COGNITIVE:
            issues.append(f'{p}: invalid classification')
        if q.get('status') != 'draft':
            issues.append(f'{p}: generated items must be draft')
        if type(q.get('version')) is not int or q['version'] < 1:
            issues.append(f'{p}: invalid version')
        a, c, e = q.get('answers'), q.get('correct'), q.get('optionExplanations')
        if not isinstance(a, list) or len(a) < 2 or any(not isinstance(x, str) or not x.strip() for x in a):
            issues.append(f'{p}: invalid answers')
            continue
        if len(set(x.strip().casefold() for x in a)) != len(a):
            issues.append(f'{p}: duplicate answer labels')
        if not isinstance(e, list) or len(e) != len(a) or any(not isinstance(x, str) or not x.strip() for x in e):
            issues.append(f'{p}: optionExplanations must align with answers')
        if not isinstance(c, list) or any(type(x) is not int or x < 0 or x >= len(a) for x in c) or len(c) != len(set(c)):
            issues.append(f'{p}: invalid correct indexes')
            continue
        if q.get('type') in ('single', 'boolean') and len(c) != 1:
            issues.append(f'{p}: expected exactly one correct index')
        if q.get('type') == 'multiple' and not (2 <= len(c) < len(a)):
            issues.append(f'{p}: multiple requires 2+ correct and at least one incorrect')
        if q.get('type') == 'boolean' and a != ['True', 'False']:
            issues.append(f'{p}: boolean answers must be True, False')
        refs = q.get('sourceRefs')
        if not isinstance(refs, list) or not refs or any(not isinstance(r, dict) or not isinstance(r.get('file'), str) or not r['file'].strip() or ('page' in r and (type(r['page']) is not int or r['page'] < 1)) for r in refs):
            issues.append(f'{p}: invalid sourceRefs')
    return issues


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    bank = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    issues = validate_bank(bank)
    for issue in issues:
        print('ERROR:', issue)
    print(f'{len(bank) if isinstance(bank, list) else 0} questions, {len(issues)} structural issues')
    return 1 if issues else 0


if __name__ == '__main__':
    sys.exit(main())
