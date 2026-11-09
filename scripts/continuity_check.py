"""Compare explicit shot boundary states; no inference from prose."""
import argparse
import json
from pathlib import Path

def check(shots):
    errors = []
    if not isinstance(shots, list) or not shots or any(not isinstance(s, dict) for s in shots):
        return ['nonempty object shots required']
    for i, shot in enumerate(shots):
        for field in ('start_state', 'end_state'):
            if not isinstance(shot.get(field), dict) or not shot[field]:
                errors.append(f'shot {i}: missing {field}')
        if i:
            previous = shots[i-1].get('end_state', {})
            current = shot.get('start_state', {})
            transitions = shot.get('transitions', {})
            previous = previous if isinstance(previous, dict) else {}
            current = current if isinstance(current, dict) else {}
            transitions = transitions if isinstance(transitions, dict) else {}
            for key in previous.keys() | current.keys():
                if (key not in previous or key not in current or previous[key] != current[key]) and not transitions.get(key):
                    errors.append(f'shot {i}: unexplained boundary change: {key}')
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    errors = check(json.loads(args.file.read_text(encoding='utf-8-sig'))['shots'])
    print(json.dumps(errors, ensure_ascii=False, indent=2))
    raise SystemExit(bool(errors))
