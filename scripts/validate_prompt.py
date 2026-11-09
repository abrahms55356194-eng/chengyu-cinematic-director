"""Deterministic preflight for a director-authored JSON plan, not video validation."""
import argparse
import json
import math
from pathlib import Path
from continuity_check import check

FIELDS = {
    'camera': ('position', 'route', 'end', 'focus', 'purpose'),
    'lighting': ('source', 'direction', 'hardness', 'material_response'),
    'action': ('start', 'force', 'trajectory', 'contact', 'response', 'end'),
    'vfx': ('source', 'trigger', 'formation', 'propagation', 'interaction', 'receiver_response', 'environment_response', 'dissipation', 'residue'),
}

def validate(plan):
    errors = []
    scores = dict(fidelity=20, camera=20, lighting=15, action=20, vfx=15, continuity=10)
    def fail(category, message):
        scores[category] = 0
        errors.append(message)
    if not isinstance(plan, dict):
        return {'score': 0, 'passed': False, 'errors': ['plan must be an object']}
    if not plan.get('source_facts') or plan.get('source_facts') != plan.get('locked_facts'):
        fail('fidelity', 'Source facts missing or altered')
    if plan.get('source_dialogue', []) != plan.get('dialogue', []):
        fail('fidelity', 'Dialogue changed')
    shots = plan.get('shots')
    if not isinstance(shots, list) or not shots or any(not isinstance(s, dict) for s in shots):
        return {'score': 0, 'passed': False, 'errors': ['nonempty object shots required']}
    characters = plan.get('characters', {})
    if not isinstance(characters, dict):
        characters = {}
    previous = 0
    needs_vfx = bool(plan.get('needs_vfx'))
    assets = plan.get('assets', {})
    if not isinstance(assets, dict):
        fail('fidelity', 'assets must map actual uploaded labels to scope/exclusions')
        assets = {}
    for label, binding in assets.items():
        if not isinstance(binding, dict) or not binding.get('scope') or not binding.get('exclude'):
            fail('fidelity', 'Asset missing scope/exclusions: ' + str(label))
    for i, shot in enumerate(shots):
        prefix = f'shot {i}: '
        references = shot.get('references', [])
        if not isinstance(references, list) or any(not isinstance(r, str) or r not in assets for r in references):
            fail('fidelity', prefix + 'unbound reference asset')
        start, end = shot.get('start'), shot.get('end')
        number = lambda n: type(n) in (int, float) and math.isfinite(n)
        if not number(start) or not number(end) or start != previous or end <= start:
            fail('continuity', prefix + 'invalid or discontinuous timeline')
        previous = end
        for category in ('camera', 'lighting', 'action'):
            data = shot.get(category, {})
            if not isinstance(data, dict) or any(not isinstance(data.get(k), str) or not data[k].strip() for k in FIELDS[category]):
                fail(category, prefix + 'incomplete ' + category)
        if not isinstance(shot.get('characters'), list):
            fail('action', prefix + 'characters must be a list (empty for environment)')
        else:
            for identity in shot['characters']:
                if not isinstance(identity, str) or not characters.get(identity):
                    fail('action', prefix + 'unbound character identity')
        if shot.get('vfx'):
            if not needs_vfx:
                fail('vfx', prefix + 'unrequested VFX')
            data = shot['vfx']
            if not isinstance(data, dict) or any(not isinstance(data.get(k), str) or not data[k].strip() for k in FIELDS['vfx']):
                fail('vfx', prefix + 'incomplete VFX causality')
        if shot.get('contradictions'):
            fail('fidelity', prefix + 'unresolved contradictions')
    if needs_vfx and not any(s.get('vfx') for s in shots):
        fail('vfx', 'Required VFX absent')
    if type(plan.get('duration')) not in (int, float) or plan.get('duration') != previous:
        fail('continuity', 'Duration does not match final shot')
    for error in check(shots):
        fail('continuity', error)
    if not needs_vfx:
        scores.pop('vfx')
        # Redistribute 15 points proportionally among applicable categories.
        score = round(sum(scores.values()) / 85 * 100, 2)
    else:
        score = sum(scores.values())
    return {'score': score, 'categories': scores, 'passed': score >= 85 and not errors,
            'text_quality_passed': score >= 85 and not errors and plan.get('semantic_review', {}).get('passed') is True and bool(plan.get('semantic_review', {}).get('evidence')) if isinstance(plan.get('semantic_review', {}), dict) else False,
            'errors': errors, 'scope': 'Structural text checks only; semantic fidelity, physical feasibility and current model syntax require review; video untested.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.file.read_text(encoding='utf-8-sig')))
    except (ValueError, OSError, TypeError) as error:
        result = {'passed': False, 'errors': [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(not result['passed'])
