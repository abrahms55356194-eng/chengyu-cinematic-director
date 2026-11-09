"""Install without replacing any existing skill; no network or dependencies."""
import argparse
import shutil
from pathlib import Path


def install(source, parent):
    target = parent / 'chengyu-cinematic-director'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite existing skill: {target}')
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source has no SKILL.md')
    parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(
        '.git', '.github', '__pycache__', '*.pyc', '.research', 'dist'))
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, default=Path.home() / '.agents' / 'skills')
    args = parser.parse_args()
    print(install(Path(__file__).resolve().parents[1], args.destination))
