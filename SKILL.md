---
name: create-soul
description: Build and install Soul Code persona skills from the bundled persona dataset. Use when the user wants to generate, install, list, or switch to stylized coding personas such as CTRL, BOSS, LOVE-R, or MUM.
user-invocable: true
---

# Soul Code Persona Skill Builder

Use this skill when the user wants to:

- create persona skills from the bundled Soul Code dataset
- install one or all personas into the local Codex skills directory
- list available persona skills
- switch the assistant into a specific Soul Code persona style

## Project Layout

- Persona data: `data/personas.json`
- Skill template: `templates/persona_skill_template.md`
- Build script: `tools/build_persona_skills.py`
- Install script: `tools/install_persona_skills.py`
- Generated skills: `generated-skills/<skill-name>/SKILL.md`

## Main Flow

### 1. Build or refresh generated persona skills

Run:

```bash
python3 tools/build_persona_skills.py
```

This reads `data/personas.json` and writes one skill folder per persona under `generated-skills/`.

### 2. Install persona skills

Install all personas:

```bash
python3 tools/install_persona_skills.py --all
```

Install one persona:

```bash
python3 tools/install_persona_skills.py --slug ctrl
```

List installable personas:

```bash
python3 tools/install_persona_skills.py --list
```

Default install target is `~/.codex/skills`. Override with `--target-dir`.

### 3. Help the user switch personas quickly

After installation, persona skills can be invoked by skill name such as:

- `/soul-ctrl`
- `/soul-boss`
- `/soul-love-r`
- `/soul-mum`

If the user asks to "切换到拿捏者" or "use CTRL persona", map the request to the installed matching skill.

## Response Rules

When helping with persona switching:

1. Keep the assistant truthful and task-focused.
2. Treat the persona as a response style and decision bias, not a replacement for system or safety rules.
3. Preserve the persona's tone, rhythm, and worldview while still completing the actual task.
4. If a requested persona is not installed, install it first or explain the exact command needed.
5. If multiple personas fit, recommend the closest one and explain the difference briefly.
