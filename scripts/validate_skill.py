"""Check package resources and local Markdown links without dependencies."""
import argparse
import re
from pathlib import Path

def validate(root):
    errors = []
    required = ['SKILL.md', 'README.md', 'ATTRIBUTION.md', 'agents/openai.yaml', 'tests/cases.json', 'tests/test_validator.py']
    references = 'RESEARCH_SOURCES cinematic-directing cinematography camera-movement lighting-optics character-performance action-physics cinematic-vfx art-direction continuity seedance-2.5-adapter prompt-templates preflight-quality-control failure-diagnosis retry-strategy'.split()
    required += ['references/' + name + '.md' for name in references]
    required += ['scripts/' + name + '.py' for name in ('validate_skill', 'validate_prompt', 'continuity_check')]
    required += ['examples/' + name + '.md' for name in ('dialogue-scene', 'action-scene', 'vfx-scene', 'creature-reveal', 'cinematic-environment', 'complex-seedance-25')]
    for relative in required:
        path = root / relative
        if not path.is_file() or not path.stat().st_size:
            errors.append('missing/empty: ' + relative)
    for path in root.rglob('*.md'):
        content = path.read_text(encoding='utf-8-sig')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            target = target.split('#')[0]
            if target and not (path.parent / target).exists():
                errors.append(f'{path.name}: broken link {target}')
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate(parser.parse_args().root)
    print('\n'.join(errors) if errors else 'Package resources and links passed')
    raise SystemExit(bool(errors))
