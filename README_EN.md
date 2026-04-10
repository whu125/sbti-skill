# SBTI.Skill

> *"Turning personas into skills is not about performance. It is about making style switching callable, reusable, and installable."*

**A generator that turns SBTI persona archetypes into installable agent skills.**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-111827.svg)](https://openai.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills Style](https://img.shields.io/badge/AgentSkills-Inspired-f59e0b.svg)](https://github.com/therealXiaomanChu/ex-skill)

&nbsp;

Given a structured set of SBTI personas  
this project generates a full pack of **installable, switchable, maintainable** persona skills  
so your AI coding assistant can continue real work with different tones, collaboration styles, and decision biases

[Installation](#installation) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

---

## Installation

### Option 1: Install into Claude Code

> Claude Code reads skills from `.claude/skills/` in the current project or from the global skills directory.

Install into the current project:

```bash
mkdir -p .claude/skills
git clone https://github.com/whu125/sbti-skill .claude/skills/create-sbti
```

Install globally:

```bash
git clone https://github.com/whu125/sbti-skill ~/.claude/skills/create-sbti
```

### Option 2: Use as a generic skill project

If your agent environment supports `SKILL.md`-style skills, you can also clone this repository directly and use the build/install scripts below.

### Build persona skills

```bash
cd /Users/zwh/创业项目/SBTI
python3 tools/build_persona_skills.py
```

This generates the full persona pack from [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json) and [templates/persona_skill_template.md](/Users/zwh/创业项目/SBTI/templates/persona_skill_template.md) into [generated-skills](/Users/zwh/创业项目/SBTI/generated-skills).

### List available personas

```bash
python3 tools/install_persona_skills.py --list
```

### Install all personas

```bash
python3 tools/install_persona_skills.py --all
```

### Install one persona

```bash
python3 tools/install_persona_skills.py --slug ctrl
```

Default install target:

```bash
~/.codex/skills
```

Custom install target:

```bash
python3 tools/install_persona_skills.py --slug mum --target-dir /your/path
```

---

## Requirements

- **Python**: 3.9+
- **Claude Code**: supported through `.claude/skills/`
- **Compatible skill directory**: installer defaults to `~/.codex/skills`
- **No database required**
- **No Docker required**
- **No extra service required**

---

## Usage

Build first, install second, switch third.

### Step 1: Build

```bash
python3 tools/build_persona_skills.py
```

### Step 2: Install

```bash
python3 tools/install_persona_skills.py --all
```

Or install just one:

```bash
python3 tools/install_persona_skills.py --slug love-r
```

### Step 3: Switch persona

After installation, you will get a set of skills such as:

- `soul-ctrl`
- `soul-boss`
- `soul-love-r`
- `soul-mum`
- `soul-monk`

You can then ask your assistant to continue in one of those personas:

```text
Use CTRL persona for this refactor
Switch to MUM persona and rewrite this support reply
Use LOVE-R persona to polish this copy
```

### Commands

| Command | Description |
|------|------|
| `python3 tools/build_persona_skills.py` | Rebuild all persona skills |
| `python3 tools/install_persona_skills.py --list` | List available persona slugs |
| `python3 tools/install_persona_skills.py --all` | Install all personas |
| `python3 tools/install_persona_skills.py --slug ctrl` | Install one persona |
| `python3 tools/install_persona_skills.py --slug mum --target-dir /path` | Install into a custom directory |

---

## Examples

> Input: `Use CTRL persona and help me refactor this component`

**Scenario 1: High-pressure execution**

```text
User        ❯ Use CTRL persona and help me refactor this component

SBTI.Skill  ❯ Stop patching this component. We should split it properly.
              I’ll first collapse the state flow, remove duplicated logic,
              and thin the render layer. You need maintainability, not a temporary pass.
```

**Scenario 2: Supportive grounding**

```text
User        ❯ Use MUM persona to answer this upset user

SBTI.Skill  ❯ Let’s not argue first. We should receive the emotion before solving the issue.
              I’ll draft a softer response that still keeps your boundaries,
              so the user feels understood while the conversation moves forward.
```

**Scenario 3: Poetic polish**

```text
User        ❯ Use LOVE-R persona to polish this introduction

SBTI.Skill  ❯ Right now the paragraph only delivers information.
              It does not glow yet.
              I’ll keep the meaning, but give it more imagery and emotional aftertaste.
```

---

## Features

### Data-driven

Persona content comes from a single structured dataset:

- [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json)

Each persona includes:

- SBTI code
- Chinese title
- MBTI mapping
- camp
- dimension model
- rarity
- traits
- core line
- descriptive style bias

### Template-based generation

Single persona skills are generated from:

- [templates/persona_skill_template.md](/Users/zwh/创业项目/SBTI/templates/persona_skill_template.md)

The generated skill includes:

- Persona Snapshot
- Core Line
- Persona Read
- Style Contract
- Response Bias
- Voice Markers

### Installable

Install script:

- [tools/install_persona_skills.py](/Users/zwh/创业项目/SBTI/tools/install_persona_skills.py)

Build script:

- [tools/build_persona_skills.py](/Users/zwh/创业项目/SBTI/tools/build_persona_skills.py)

### Extensible

To add a new persona:

1. Edit [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json)
2. Rebuild generated skills
3. Reinstall them into your Codex skills directory

---

## Project Structure

```text
SBTI/
├── SKILL.md
├── README.md
├── README_EN.md
├── data/
│   └── personas.json
├── templates/
│   └── persona_skill_template.md
├── tools/
│   ├── build_persona_skills.py
│   └── install_persona_skills.py
└── generated-skills/
    └── soul-*/
        └── SKILL.md
```

---

## Inspiration

This project’s packaging style and skill-oriented workflow were inspired by:

- [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)

Special thanks as well to the original SBTI test page for the underlying persona inspiration:

- [Original SBTI page](https://fancc.de5.net/projects/sbti/)

---

## Notes

- `generated-skills/` is build output and can be regenerated anytime
- edit the dataset and template first instead of hand-editing generated results
- personas are style layers, not permission to ignore truth, safety, or task quality

---

### Final Note

People who build things often wish they could switch working personas on demand.
Sometimes you need CTRL’s force, MUM’s softness, LOVE-R’s sensitivity, or MONK’s distance.
This repository takes what used to live only in vibe, jokes, and instinct, and compresses it into an actual skill pack.

From here on, style is no longer just something that feels similar.
It becomes something you can install, switch, and keep working with.
