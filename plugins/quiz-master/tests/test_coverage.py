"""Synthetic integrity fixtures, not genuine source or question approvals."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/quiz-master/scripts'))
from check_coverage import evaluate, canonical_hash, DEFAULTS, ANALYSIS_CHECKS, QUESTION_CHECKS, LEDGER_CHECKS
from check_bank import validate_bank


def fixture():
    catalog = {'catalogId':'test','status':'draft','sourceFiles':[{'file':'fixture.pdf','version':'a'*64,'pageCount':1}],
               'lectures':[{'lectureId':'l1','topics':[{'topicId':'t1','concepts':[{'conceptId':'c1','name':'Fixture'}],
               'objectives':[{'objectiveId':'o1','conceptId':'c1','statement':'Identify the fixture value.',
               'priority':'core','required':True,'sourceRefs':[{'file':'fixture.pdf','page':1}]}]}]}],
               'pageAccounting':[{'file':'fixture.pdf','page':1,'disposition':'included','reason':'Fixture teaching page','objectiveIds':['o1']}], 'sourceIssues':[]}
    q = dict(id='q1',subject='Fixture',topic='Fixture',objectiveId='o1',objectiveIds=['o1'],type='single',difficulty='Easy',
             cognitiveLevel='Remember',prompt='Fixture value?',answers=['One','Two'],correct=[0],
             explanation='Fixture says one.',optionExplanations=['Fixture value.','Other value.'],
             sourceRefs=[{'file':'fixture.pdf','page':1}],status='approved',version=1)
    h=canonical_hash(catalog)
    audit={'catalogHash':h,'sourceVersions':[{'file':'fixture.pdf','version':'a'*64}],
           'decision':'approved','checks':{k:'pass' for k in ANALYSIS_CHECKS},'issues':[]}
    reviews=[{'questionId':'q1','questionVersion':1,'contentHash':canonical_hash(q),'decision':'approved',
              'checks':{k:'pass' for k in QUESTION_CHECKS|{'optionExplanations'}},'issues':[]}]
    ledger={'catalogHash':h,'budgets':dict(DEFAULTS),'budgetOverrides':[],
            'mappings':[{'mappingId':'m1','objectiveId':'o1','questionId':'q1','questionVersion':1,
            'questionHash':canonical_hash(q),'part':'response','coverage':'adequate','rationale':'Synthetic fixture response evidence.'}]}
    ledger_review={'catalogHash':h,'ledgerHash':canonical_hash(ledger),'decision':'approved',
                   'checks':{k:'pass' for k in LEDGER_CHECKS},'issues':[]}
    return [catalog,audit,[q],reviews,ledger,ledger_review]


def rebind(x):
    h=canonical_hash(x[0]);x[1]['catalogHash']=h;x[4]['catalogHash']=h;x[5]['catalogHash']=h
    for q,r in zip(x[2],x[3]):
        r['contentHash']=canonical_hash(q)
        for m in x[4]['mappings']:
            if m['questionId']==q['id']:m['questionHash']=canonical_hash(q)
    x[5]['ledgerHash']=canonical_hash(x[4])


class CoverageTests(unittest.TestCase):
    def test_complete_fixture(self):
        r=evaluate(*fixture());self.assertTrue(r['complete']);self.assertTrue(r['fullLectureCoverage'])
    def test_draft_cannot_close_gap(self):
        x=fixture();x[2][0]['status']='draft';rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_invalid_question_reference(self):
        for ref in [{'file':'absent.pdf','page':999},{'file':'fixture.pdf','page':2},{'file':'fixture.pdf'}]:
            x=fixture();x[2][0]['sourceRefs']=[ref];rebind(x);r=evaluate(*x);self.assertFalse(r['complete']);self.assertEqual(r['eligibleQuestionIds'],[])
    def test_edited_question_invalidates(self):
        x=fixture();x[2][0]['prompt']='Edited';r=evaluate(*x);self.assertFalse(r['complete']);self.assertEqual(r['counts']['unverified'],1)
    def test_edited_catalog_invalidates(self):
        x=fixture();x[0]['lectures'][0]['topics'][0]['objectives'][0]['statement']='Edited';self.assertFalse(evaluate(*x)['complete'])
    def test_edited_ledger_invalidates(self):
        x=fixture();x[4]['mappings'][0]['rationale']='Edited';self.assertFalse(evaluate(*x)['complete'])
    def test_unverified_analysis(self):
        x=fixture();x[1]['checks']['sourceAccess']='unverified';self.assertFalse(evaluate(*x)['complete'])
    def test_wrong_source_hash(self):
        x=fixture();x[1]['sourceVersions'][0]['version']='b'*64;self.assertFalse(evaluate(*x)['complete'])
    def test_page_missing(self):
        x=fixture();x[0]['pageAccounting']=[];rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_unresolved_source_issue(self):
        x=fixture();x[0]['sourceIssues']=[{'status':'unresolved'}];rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_orphan_concept(self):
        x=fixture();x[0]['lectures'][0]['topics'][0]['concepts'].append({'conceptId':'c2','name':'Untested concept'});rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_missing_page_backlink(self):
        x=fixture();x[0]['pageAccounting'][0]['objectiveIds']=['unknown'];rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_missing_objective(self):
        x=fixture();o=copy.deepcopy(x[0]['lectures'][0]['topics'][0]['objectives'][0]);o['objectiveId']='o2';x[0]['lectures'][0]['topics'][0]['objectives'].append(o);x[0]['pageAccounting'][0]['objectiveIds'].append('o2');rebind(x)
        r=evaluate(*x);self.assertFalse(r['complete']);self.assertEqual(r['counts']['missing'],1)
    def test_partial_never_closes(self):
        x=fixture();x[4]['mappings'][0]['coverage']='partial';rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_major_question_issue(self):
        x=fixture();x[3][0]['decision']='revision_required';x[3][0]['issues']=[{'severity':'major','finding':'Ambiguous'}];self.assertFalse(evaluate(*x)['complete'])
    def test_minor_question_issue(self):
        x=fixture();x[3][0]['issues']=[{'severity':'minor','finding':'Cue'}];self.assertFalse(evaluate(*x)['complete'])
    def test_mapping_scope(self):
        x=fixture();x[4]['mappings'][0]['part']='option:99';rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_question_primary_link(self):
        x=fixture();x[2][0]['objectiveIds']=['o2'];rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_duplicate_mapping(self):
        x=fixture();x[4]['mappings'].append(copy.deepcopy(x[4]['mappings'][0]));rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_pair_cap_and_workload(self):
        x=fixture();q=x[2][0]
        for k in ['answers','correct','optionExplanations']:q.pop(k)
        q.update(type='matching',leftItems=['a','b','c','d','e'],rightItems=['u','v','w','x','y'],reuseRight=False,matches=[[i,4-i] for i in range(5)],pairExplanations=['Fixture']*5)
        x[3][0]['checks'].pop('optionExplanations');x[3][0]['checks']['responseExplanations']='pass';x[4]['mappings'][0]['part']='pair:0';rebind(x)
        r=evaluate(*x);self.assertFalse(r['complete']);self.assertEqual(r['workload']['responseUnits'],5);self.assertTrue(any('maxMatchingPairs' in e for e in r['problems']))
    def test_total_workload_cap(self):
        x=fixture();x[4]['budgets']['maxResponseUnits']=1
        x[4]['budgetOverrides']=[{'field':'maxResponseUnits','value':1,'reason':'Explicit test policy'}]
        x[2][0]['type']='multiple';x[2][0]['answers']=['One','Two','Three'];x[2][0]['correct']=[0,1];x[2][0]['optionExplanations']=['a','b','c'];x[4]['mappings'][0]['part']='option:0';rebind(x)
        r=evaluate(*x);self.assertFalse(r['complete']);self.assertEqual(r['workload']['responseUnits'],3)
    def test_undocumented_override(self):
        x=fixture();x[4]['budgets']['maxQuestions']=21;rebind(x);self.assertFalse(evaluate(*x)['complete'])
    def test_exclusion_not_full_lecture(self):
        x=fixture();o=copy.deepcopy(x[0]['lectures'][0]['topics'][0]['objectives'][0]);o.update(objectiveId='o2',required=False,exclusionReason='Explicit narrow scope');x[0]['lectures'][0]['topics'][0]['objectives'].append(o);x[0]['pageAccounting'][0]['objectiveIds'].append('o2');rebind(x)
        r=evaluate(*x);self.assertTrue(r['complete']);self.assertFalse(r['fullLectureCoverage']);self.assertEqual(r['counts']['excluded'],1)
    def test_all_six_formats_remain_supported(self):
        base=fixture()[2][0]
        variants=[dict(type='single',answers=['A','B'],correct=[0],optionExplanations=['yes','no']),
                  dict(type='multiple',answers=['A','B','C'],correct=[0,1],optionExplanations=['yes','yes','no']),
                  dict(type='boolean',answers=['True','False'],correct=[1],optionExplanations=['no','yes']),
                  dict(type='matching',leftItems=['a','b'],rightItems=['x','y'],reuseRight=False,matches=[[0,1],[1,0]],pairExplanations=['x','y']),
                  dict(type='ordering',items=['c','a','b'],correctOrder=[1,2,0],stepExplanations=['a','b','c']),
                  dict(type='fill_blank',prompt='Value {{1}}',blanks=[dict(id='1',kind='number',value=4,absoluteTolerance=0.01,unit='ms',rounding='none',explanation='Fixture')])]
        bank=[]
        for i,v in enumerate(variants):
            q={k:value for k,value in base.items() if k not in ('answers','correct','optionExplanations')}
            q.update(v,id=str(i),status='draft');bank.append(q)
        self.assertEqual(validate_bank(bank),[])

if __name__=='__main__':unittest.main()
