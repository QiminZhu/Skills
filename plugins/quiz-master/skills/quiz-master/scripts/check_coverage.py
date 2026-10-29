#!/usr/bin/env python3
"""Verify exact approvals, objective coverage and workload; not semantic truth.
Usage: check_coverage.py catalog analysis bank question_reports ledger ledger_review
All six inputs are JSON files. Exit 0 complete, 1 blocked/incomplete, 2 input error.
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from check_bank import validate_bank

DEFAULTS = dict(maxQuestions=20, maxResponseUnits=50, maxMatchingPairs=4,
                maxOrderingItems=6, maxBlanks=3, maxChoiceOptions=6)
ANALYSIS_CHECKS = {'sourceAccess', 'pageAccounting', 'conceptCompleteness',
                   'sourceGrounding', 'objectiveAtomicity', 'consistency', 'sourceIssues'}
QUESTION_CHECKS = {'schema', 'independentAnswer', 'overallExplanation', 'sourceGrounding',
                   'objectiveAlignment', 'ambiguity', 'distractors', 'difficulty',
                   'cognitiveLevel', 'coverageMappings'}
LEDGER_CHECKS = {'sourceEvidence', 'responseDemand', 'granularity', 'scope', 'workload'}


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode('utf-8')).hexdigest()


def approved(report, required):
    if not isinstance(report, dict):
        return False
    checks = report.get('checks')
    return (report.get('decision') == 'approved' and report.get('issues') == []
            and isinstance(checks, dict) and required.issubset(checks)
            and all(v == 'pass' for v in checks.values()))


def response_parts(q):
    kind = q.get('type')
    if kind in ('single', 'boolean'):
        return ['response']
    if kind == 'multiple':
        return [f'option:{i}' for i in range(len(q.get('answers', [])))]
    if kind == 'matching':
        return [f'pair:{i}' for i in range(len(q.get('matches', [])))]
    if kind == 'ordering':
        return [f'position:{i}' for i in range(len(q.get('correctOrder', [])))]
    if kind == 'fill_blank':
        return [f"blank:{b['id']}" for b in q.get('blanks', [])]
    return []


def evaluate(catalog, analysis, bank, reports, ledger, ledger_review):
    problems, analysis_problems = [], []
    catalog_hash = canonical_hash(catalog)
    sources = catalog.get('sourceFiles', [])
    source_versions, page_counts = {}, {}
    for s in sources:
        if not isinstance(s, dict) or not isinstance(s.get('file'), str) or not s['file'].strip():
            analysis_problems.append('Invalid source file'); continue
        name, version, count = s['file'], s.get('version'), s.get('pageCount')
        if name in source_versions:
            analysis_problems.append('Duplicate source filename: ' + name)
        source_versions[name] = version
        if not isinstance(version, str) or not re.fullmatch(r'[a-f0-9]{64}', version):
            analysis_problems.append('Source requires byte SHA-256: ' + name)
        if type(count) is not int or count < 1:
            analysis_problems.append('Source requires pageCount: ' + name)
        else:
            page_counts[name] = count
    if not source_versions:
        analysis_problems.append('No source files')
    objectives, concepts = {}, set()
    for lecture in catalog.get('lectures', []):
        for topic in lecture.get('topics', []):
            local_concepts = set()
            for c in topic.get('concepts', []):
                cid = c.get('conceptId')
                if not isinstance(cid, str) or not cid or cid in concepts:
                    analysis_problems.append('Missing/duplicate concept ID'); continue
                concepts.add(cid); local_concepts.add(cid)
            for o in topic.get('objectives', []):
                oid = o.get('objectiveId')
                if not isinstance(oid, str) or not oid or oid in objectives:
                    analysis_problems.append('Missing/duplicate objective ID'); continue
                objectives[oid] = o
                if o.get('conceptId') not in local_concepts:
                    analysis_problems.append('Unknown concept for ' + oid)
                if not isinstance(o.get('statement'), str) or not o['statement'].strip():
                    analysis_problems.append('No atomic statement for ' + oid)
                if o.get('priority') not in ('core', 'supporting') or type(o.get('required')) is not bool:
                    analysis_problems.append('Missing scope/priority for ' + oid)
                if o.get('required') is False and not str(o.get('exclusionReason', '')).strip():
                    analysis_problems.append('Excluded objective without reason: ' + oid)
                refs = o.get('sourceRefs', [])
                if not refs:
                    analysis_problems.append('No source evidence for ' + oid)
                for ref in refs:
                    file, page = ref.get('file'), ref.get('page')
                    if file not in page_counts or type(page) is not int or not 1 <= page <= page_counts[file]:
                        analysis_problems.append('Invalid objective reference: ' + oid)
    if not objectives:
        analysis_problems.append('No catalog objectives')
    used_concepts = {o.get('conceptId') for o in objectives.values()}
    if concepts - used_concepts:
        analysis_problems.append('Substantive concept lacks an assessable objective')
    expected_pages = {(f, i) for f, count in page_counts.items() for i in range(1, count + 1)}
    accounted = set()
    page_objectives = {}
    for item in catalog.get('pageAccounting', []):
        key = (item.get('file'), item.get('page'))
        if key not in expected_pages or key in accounted:
            analysis_problems.append('Invalid/duplicate accounted page'); continue
        accounted.add(key)
        page_objectives[key] = item.get('objectiveIds', [])
        disposition = item.get('disposition')
        if disposition not in ('included', 'duplicate', 'administrative', 'external_resource', 'unreadable') or not str(item.get('reason', '')).strip():
            analysis_problems.append('Invalid page disposition/reason')
        if disposition == 'unreadable':
            analysis_problems.append('Unreadable source content')
        ids = item.get('objectiveIds', [])
        if not isinstance(ids, list) or any(i not in objectives for i in ids):
            analysis_problems.append('Invalid page objective links')
        elif disposition in ('included', 'duplicate') and not ids:
            analysis_problems.append('Included page lacks objective link')
    for oid, obj in objectives.items():
        for ref in obj.get('sourceRefs', []):
            if oid not in page_objectives.get((ref.get('file'), ref.get('page')), []):
                analysis_problems.append('Objective source page lacks accounting backlink: ' + oid)
    if accounted != expected_pages:
        analysis_problems.append('Page accounting incomplete')
    if any(i.get('status') != 'resolved' for i in catalog.get('sourceIssues', [])):
        analysis_problems.append('Unresolved source issues')
    versions = analysis.get('sourceVersions', [])
    observed = {s.get('file'): s.get('version') for s in versions}
    if len(observed) != len(versions) or observed != source_versions:
        analysis_problems.append('Analysis source versions mismatch')
    if analysis.get('catalogHash') != catalog_hash or not approved(analysis, ANALYSIS_CHECKS):
        analysis_problems.append('Analysis approval missing, unverified or stale')
    problems.extend(analysis_problems)
    analysis_valid = not analysis_problems

    budgets = ledger.get('budgets', {})
    if set(budgets) != set(DEFAULTS) or any(type(v) is not int or v < 1 for v in budgets.values()):
        problems.append('Invalid workload budgets'); budgets = dict(DEFAULTS)
    overrides = ledger.get('budgetOverrides', [])
    for field, value in budgets.items():
        if value != DEFAULTS[field] and not any(o.get('field') == field and o.get('value') == value and str(o.get('reason', '')).strip() for o in overrides):
            problems.append('Undocumented budget override: ' + field)
    ledger_valid = (analysis_valid and ledger.get('catalogHash') == catalog_hash
                    and ledger_review.get('catalogHash') == catalog_hash
                    and ledger_review.get('ledgerHash') == canonical_hash(ledger)
                    and approved(ledger_review, LEDGER_CHECKS))
    if not ledger_valid:
        problems.append('Ledger approval missing, unverified or stale')
    report_map = {}
    for r in reports:
        key = r.get('questionId')
        if key in report_map:
            problems.append('Duplicate question review: ' + str(key))
        report_map[key] = r
    qmap, eligible, units = {}, set(), 0
    for q in bank:
        qid = q.get('id')
        if qid in qmap:
            problems.append('Duplicate question ID: ' + str(qid))
        qmap[qid] = q
        structure = validate_bank([dict(q, status='draft')])
        if structure:
            problems.extend(f'{qid}: {i}' for i in structure); continue
        parts = response_parts(q); units += len(parts)
        source_valid = all(ref.get('file') in page_counts and type(ref.get('page')) is int
                           and 1 <= ref['page'] <= page_counts[ref['file']]
                           for ref in q.get('sourceRefs', []))
        if not source_valid:
            problems.append(f'{qid}: question reference outside catalog source/page bounds')
        kind = q['type']
        limit = {'matching': ('maxMatchingPairs', len(q.get('matches', []))),
                 'ordering': ('maxOrderingItems', len(q.get('items', []))),
                 'fill_blank': ('maxBlanks', len(q.get('blanks', [])))}.get(kind)
        if kind in ('single', 'multiple', 'boolean'):
            limit = ('maxChoiceOptions', len(q['answers']))
        if limit and limit[1] > budgets[limit[0]]:
            problems.append(f'{qid}: exceeds {limit[0]}')
        r = report_map.get(qid, {})
        required = QUESTION_CHECKS | ({'optionExplanations'} if kind in ('single', 'multiple', 'boolean') else {'responseExplanations'})
        if (source_valid and q.get('status') == 'approved' and approved(r, required)
                and r.get('questionVersion') == q.get('version')
                and r.get('contentHash') == canonical_hash(q)):
            eligible.add(qid)
        else:
            problems.append(f'{qid}: question approval missing, unverified or stale')
    if len(bank) > budgets['maxQuestions']:
        problems.append('Question-object budget exceeded')
    if units > budgets['maxResponseUnits']:
        problems.append('Response-unit budget exceeded')
    evidence = {oid: [] for oid in objectives}
    mapping_ids, tuples, mapped_ids = set(), set(), {}
    for m in ledger.get('mappings', []):
        mid, oid, qid, part = m.get('mappingId'), m.get('objectiveId'), m.get('questionId'), m.get('part')
        key = (oid, qid, part)
        if not isinstance(mid, str) or not mid or mid in mapping_ids or key in tuples:
            problems.append('Missing/duplicate mapping ID or evidence tuple'); continue
        mapping_ids.add(mid); tuples.add(key)
        if oid not in objectives or qid not in qmap:
            problems.append('Mapping names unknown objective/question'); continue
        q = qmap[qid]
        mapped_ids.setdefault(qid, set()).add(oid)
        valid = (ledger_valid and qid in eligible and part in response_parts(q)
                 and m.get('questionHash') == canonical_hash(q)
                 and m.get('questionVersion') == q.get('version')
                 and isinstance(m.get('rationale'), str) and bool(m['rationale'].strip())
                 and m.get('coverage') in ('adequate', 'partial', 'unverified'))
        if not valid:
            problems.append('Invalid/stale mapping: ' + mid)
        evidence[oid].append({'questionId': qid, 'part': part,
                              'coverage': m.get('coverage') if valid else 'unverified'})
    for qid, q in qmap.items():
        actual = mapped_ids.get(qid, set())
        if q.get('objectiveId') not in actual:
            problems.append(f'{qid}: primary objective has no response evidence mapping')
        if 'objectiveIds' in q and set(q['objectiveIds']) != actual:
            problems.append(f'{qid}: objectiveIds disagree with mappings')
    rows = []
    for oid, objective in objectives.items():
        entries = evidence[oid]; states = {e['coverage'] for e in entries}
        status = ('excluded' if objective.get('required') is False else
                  'adequate' if 'adequate' in states else
                  'partial' if 'partial' in states else
                  'unverified' if entries else 'missing')
        rows.append({'objectiveId': oid, 'priority': objective.get('priority'),
                     'statement': objective.get('statement'), 'status': status,
                     'exclusionReason': objective.get('exclusionReason'), 'evidence': entries})
    counts = dict(Counter(r['status'] for r in rows))
    complete = bool(rows) and not problems and all(r['status'] in ('adequate', 'excluded') for r in rows)
    return {'complete': complete, 'fullLectureCoverage': complete and not counts.get('excluded'),
            'counts': counts, 'workload': {'questionObjects': len(bank), 'responseUnits': units,
                                         'budgets': budgets},
            'eligibleQuestionIds': sorted(eligible), 'objectives': rows,
            'problems': list(dict.fromkeys(problems)),
            'limitation': 'Integrity checks rely on actual independent source/response review; they do not prove semantic truth or mastery.'}


def main():
    if len(sys.argv) != 7:
        print(__doc__, file=sys.stderr); return 2
    try:
        inputs = [json.loads(Path(p).read_text()) for p in sys.argv[1:]]
        result = evaluate(*inputs)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result['complete'] else 1
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        print(json.dumps({'complete': False, 'error': str(exc)})); return 2


if __name__ == '__main__':
    sys.exit(main())
