#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "personas.json"
BUILD_SCRIPT = ROOT / "tools" / "build_persona_skills.py"
GENERATED_DIR = ROOT / "generated-skills"
DEFAULT_TARGET = Path.home() / ".codex" / "skills"


def load_personas() -> list[dict]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def ensure_built() -> None:
    if GENERATED_DIR.exists() and any(GENERATED_DIR.iterdir()):
        return
    subprocess.run([sys.executable, str(BUILD_SCRIPT)], check=True)


def list_personas(personas: list[dict]) -> None:
    for persona in personas:
        print(f"{persona['slug']:10}  soul-{persona['slug']:16}  {persona['code']:8}  {persona['name']}")


def install_skill(skill_slug: str, target_dir: Path) -> None:
    source = GENERATED_DIR / f"soul-{skill_slug}"
    if not source.exists():
        raise FileNotFoundError(f"Missing generated skill: {source}")

    destination = target_dir / source.name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    print(f"Installed {source.name} -> {destination}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Soul Code persona skills")
    parser.add_argument("--slug", help="Install one persona by slug, such as ctrl or mum")
    parser.add_argument("--all", action="store_true", help="Install all persona skills")
    parser.add_argument("--list", action="store_true", help="List all persona slugs")
    parser.add_argument("--target-dir", default=str(DEFAULT_TARGET), help="Target skills directory")
    args = parser.parse_args()

    personas = load_personas()
    slug_map = {persona["slug"]: persona for persona in personas}

    if args.list:
        list_personas(personas)
        return

    if not args.slug and not args.all:
        parser.error("Use --list, --slug <slug>, or --all")

    ensure_built()

    target_dir = Path(args.target_dir).expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    if args.all:
        for persona in personas:
            install_skill(persona["slug"], target_dir)
        return

    if args.slug not in slug_map:
        valid = ", ".join(sorted(slug_map))
        parser.error(f"Unknown slug '{args.slug}'. Valid values: {valid}")

    install_skill(args.slug, target_dir)


if __name__ == "__main__":
    main()
