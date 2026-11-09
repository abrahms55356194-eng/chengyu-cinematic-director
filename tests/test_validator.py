import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_prompt import validate
from continuity_check import check
CASES = json.loads(Path(__file__).with_name('cases.json').read_text(encoding='utf-8'))

class ValidatorTests(unittest.TestCase):
    def test_cases(self):
        for case in CASES:
            with self.subTest(case=case['name']):
                self.assertTrue(validate(case)['passed'])

    def test_mutations_every_case(self):
        for case in CASES:
            mutations = [lambda p: p['locked_facts'].append('changed ending'),
                         lambda p: p['shots'][0]['camera'].pop('route'),
                         lambda p: p['shots'][0]['lighting'].pop('source'),
                         lambda p: p['shots'][0]['action'].pop('force'),
                         lambda p: p['shots'][0].update(start=1),
                         lambda p: p['shots'][0].update(end=float('nan')),
                         lambda p: p['shots'][0].update(end_state={}),
                         lambda p: p['shots'][0].update(characters=['unknown']),
                         lambda p: p.update(dialogue=['invented dialogue']),
                         lambda p: p['shots'][0].update(contradictions=['locked-off and orbit simultaneously'])]
            if case['needs_vfx']:
                mutations.append(lambda p: p['shots'][0]['vfx'].pop('source'))
            for index, mutate in enumerate(mutations):
                with self.subTest(case=case['name'], mutation=index):
                    changed = copy.deepcopy(case)
                    mutate(changed)
                    self.assertFalse(validate(changed)['passed'])

    def test_boundary(self):
        plan = copy.deepcopy(CASES[-1])
        plan['shots'][1]['start_state']['prop'] = '左手持信'
        self.assertTrue(check(plan['shots']))
        plan['shots'][1]['transitions'] = {'prop': '镜间明确展示换手'}
        self.assertFalse(check(plan['shots']))

    def test_invalid_shape(self):
        for value in (None, [], {}, {'shots': [None]}):
            self.assertFalse(validate(value)['passed'])

    def test_nested_types_and_assets(self):
        for key in ('camera', 'lighting', 'action', 'start_state', 'end_state', 'characters', 'references'):
            for value in (None, 3, True):
                plan = copy.deepcopy(CASES[-1])
                plan['shots'][1][key] = value
                self.assertFalse(validate(plan)['passed'], (key, value))
        plan = copy.deepcopy(CASES[0])
        plan['shots'][0]['references'] = ['@Image 1']
        self.assertFalse(validate(plan)['passed'])
        plan['assets'] = {'@Image 1': {'scope': 'identity', 'exclude': 'background'}}
        self.assertTrue(validate(plan)['passed'])
        self.assertFalse(validate(plan)['text_quality_passed'])
        plan['semantic_review'] = {'passed': True, 'evidence': 'Reviewed source and all shots manually'}
        self.assertTrue(validate(plan)['text_quality_passed'])

    def test_unrequested_vfx(self):
        plan = copy.deepcopy(CASES[6])
        plan['needs_vfx'] = False
        self.assertFalse(validate(plan)['passed'])

    def test_numeric_edges(self):
        for key in ('start', 'end'):
            for value in (True, False, float('nan'), float('inf'), -float('inf'), None, '6'):
                with self.subTest(key=key, value=value):
                    plan = copy.deepcopy(CASES[0])
                    plan['shots'][0][key] = value
                    self.assertFalse(validate(plan)['passed'])
        for value in (True, False, float('nan'), float('inf'), None, '6'):
            plan = copy.deepcopy(CASES[0])
            plan['duration'] = value
            self.assertFalse(validate(plan)['passed'])

    def test_missing_boundary_keys(self):
        plan = copy.deepcopy(CASES[-1])
        plan['shots'][0]['end_state']['optional'] = None
        self.assertTrue(check(plan['shots']))
        plan['shots'][1]['start_state']['optional'] = None
        self.assertFalse(check(plan['shots']))
        for value in (None, [], {}, [None]):
            self.assertTrue(check(value))

if __name__ == '__main__':
    unittest.main()
