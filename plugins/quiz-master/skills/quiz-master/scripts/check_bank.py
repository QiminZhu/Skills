#!/usr/bin/env python3
"""Check structural integrity of a draft BankQuestion JSON array.

Usage: python scripts/check_bank.py questions.json
Does not verify factual correctness or source grounding.
"""
import json
import math
import re
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
        if 'levels' in q or 'EducationLevel' in q:
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


_legacy_validate_bank = validate_bank

def _strings(v, minimum=1):
    return isinstance(v, list) and len(v) >= minimum and all(isinstance(x, str) and x.strip() for x in v)

def _unique_labels(v, minimum):
    return _strings(v, minimum) and len({x.strip().casefold() for x in v}) == len(v)

def _finite(v):
    return type(v) in (int, float) and math.isfinite(v)

def validate_bank(bank):
    if not isinstance(bank, list):
        return ['Root must be a JSON array']
    issues, projected = [], []
    new_types = {'matching', 'ordering', 'fill_blank'}
    fields = {'matching': {'leftItems','rightItems','reuseRight','matches','pairExplanations'},
              'ordering': {'items','correctOrder','stepExplanations'}, 'fill_blank': {'blanks'}}
    variant_fields = set().union(*fields.values())
    for i, q in enumerate(bank):
        prefix = f'question[{i}]'
        def err(message):
            issues.append(f'{prefix}: {message}')
        if not isinstance(q, dict):
            projected.append(q); continue
        if 'objectiveIds' in q:
            links = q['objectiveIds']
            if (not isinstance(links, list) or not links or
                    any(not isinstance(x, str) or not x.strip() for x in links) or
                    len(set(x for x in links if isinstance(x, str))) != len(links) or
                    q.get('objectiveId') not in links):
                err('objectiveIds must be unique nonempty IDs including primary objectiveId')
        kind = q.get('type')
        if not isinstance(kind, str) or kind not in new_types:
            if variant_fields.intersection(q): err('foreign variant fields on choice question')
            projected.append(q); continue
        if {'answers','correct','optionExplanations'}.intersection(q): err('choice fields on non-choice question')
        if (variant_fields - fields[kind]).intersection(q): err('foreign variant fields')
        proxy = dict(q, type='single', answers=['placeholder A','placeholder B'], correct=[0], optionExplanations=['placeholder A','placeholder B'])
        projected.append(proxy)
        if kind == 'matching':
            left, right, pairs = q.get('leftItems'), q.get('rightItems'), q.get('matches')
            if not _unique_labels(left,2) or not _unique_labels(right,2): err('matching sides require distinct labels'); continue
            if type(q.get('reuseRight')) is not bool: err('reuseRight must be boolean')
            valid = isinstance(pairs,list) and all(isinstance(pair,list) and len(pair)==2 and type(pair[0]) is int and type(pair[1]) is int and 0<=pair[0]<len(left) and 0<=pair[1]<len(right) for pair in pairs)
            if not valid: err('invalid matching pairs'); continue
            if sorted(pair[0] for pair in pairs) != list(range(len(left))): err('each left item must be matched exactly once')
            if q.get('reuseRight') is False and len({pair[1] for pair in pairs}) != len(pairs): err('right option reused')
            if not _strings(q.get('pairExplanations')) or len(q['pairExplanations'])!=len(pairs): err('pair explanations must align')
        elif kind == 'ordering':
            items, order = q.get('items'), q.get('correctOrder')
            if not _unique_labels(items,3): err('ordering needs three distinct items'); continue
            if not isinstance(order,list) or any(type(x) is not int for x in order) or sorted(order)!=list(range(len(items))): err('correctOrder must be a full permutation')
            elif order == list(range(len(items))): err('ordering presentation reveals correct sequence')
            if not _strings(q.get('stepExplanations')) or len(q['stepExplanations'])!=len(items): err('step explanations must align')
        else:
            blanks=q.get('blanks')
            if not isinstance(blanks,list) or not blanks: err('blanks required'); continue
            expected=[str(x+1) for x in range(len(blanks))]
            prompt=q.get('prompt','')
            markers=re.findall(r'\{\{([^{}]+)\}\}',prompt) if isinstance(prompt,str) else []
            if markers!=expected: err('markers must occur exactly once in sequential order')
            for j,b in enumerate(blanks):
                if not isinstance(b,dict): err('blank must be object'); continue
                if b.get('id')!=expected[j] or not isinstance(b.get('explanation'),str) or not b['explanation'].strip(): err('invalid blank id or explanation')
                if b.get('kind')=='text':
                    if {'value','absoluteTolerance','unit','rounding'}.intersection(b): err('numeric fields on text blank')
                    if not _strings(b.get('acceptedAnswers')): err('accepted text answers required')
                    if any(type(b.get(k)) is not bool for k in ('caseSensitive','trim','collapseWhitespace')): err('explicit text normalization required')
                elif b.get('kind')=='number':
                    if {'acceptedAnswers','caseSensitive','trim','collapseWhitespace'}.intersection(b): err('text fields on numeric blank')
                    if not _finite(b.get('value')) or not _finite(b.get('absoluteTolerance')) or b.get('absoluteTolerance',-1)<0: err('invalid numeric value or tolerance')
                    if not isinstance(b.get('unit'),str) or not isinstance(b.get('rounding'),str) or not b['rounding'].strip(): err('numeric unit and rounding required')
                else: err('unknown blank kind')
    # Legacy checks now see only original choices or common-field proxies.
    # Malformed input must produce findings rather than crash the CLI.
    try:
        issues.extend(_legacy_validate_bank(projected))
    except (TypeError, ValueError, KeyError) as exc:
        issues.append(f'Malformed schema value: {type(exc).__name__}')
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
