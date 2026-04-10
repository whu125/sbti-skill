# SBTI.Skill

> *"把 SBTI 人格做成 skill，不是为了演，而是为了让切换风格这件事真正变得可调用、可复用、可安装。"*

**一套把 SBTI 人格原型打包成 Codex persona skills 的生成器。**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827.svg)](https://openai.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills Style](https://img.shields.io/badge/AgentSkills-Inspired-f59e0b.svg)](https://github.com/therealXiaomanChu/ex-skill)

&nbsp;

给定一组 SBTI 人格设定  
批量生成一套**真正可安装、可切换、可维护**的人格 skill  
让 Codex 用不同人格的语气、决策偏好和协作姿态继续完成真实工作

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [English](README_EN.md)

---

## 安装

### 生成 persona skills

```bash
cd /Users/zwh/创业项目/SBTI
python3 tools/build_persona_skills.py
```

这会基于 [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json) 和 [templates/persona_skill_template.md](/Users/zwh/创业项目/SBTI/templates/persona_skill_template.md) 生成一整套 skill 到 [generated-skills](/Users/zwh/创业项目/SBTI/generated-skills)。

### 查看可安装人格

```bash
python3 tools/install_persona_skills.py --list
```

### 安装全部人格

```bash
python3 tools/install_persona_skills.py --all
```

### 安装单个人格

```bash
python3 tools/install_persona_skills.py --slug ctrl
```

默认安装目录：

```bash
~/.codex/skills
```

自定义安装目录：

```bash
python3 tools/install_persona_skills.py --slug mum --target-dir /your/path
```

---

## 环境要求

- **Python**：3.9+
- **Codex skills directory**：默认使用 `~/.codex/skills`
- **不需要数据库**
- **不需要 Docker**
- **不需要额外服务**

---

## 使用

先生成，再安装，再切换。

### 第一步：生成

```bash
python3 tools/build_persona_skills.py
```

### 第二步：安装

```bash
python3 tools/install_persona_skills.py --all
```

或者只安装一个：

```bash
python3 tools/install_persona_skills.py --slug love-r
```

### 第三步：切换人格

安装完成后，会得到一组 skill，例如：

- `soul-ctrl`
- `soul-boss`
- `soul-love-r`
- `soul-mum`
- `soul-monk`

你可以直接这样要求 Codex：

```text
切换到 CTRL 人格
用拿捏者风格继续写
改成 MUM 人格帮我安抚用户
用 LOVE-R 风格润色文案
```

### 管理命令

| 命令 | 说明 |
|------|------|
| `python3 tools/build_persona_skills.py` | 重新生成全部 persona skills |
| `python3 tools/install_persona_skills.py --list` | 列出所有可安装人格 |
| `python3 tools/install_persona_skills.py --all` | 安装全部人格 |
| `python3 tools/install_persona_skills.py --slug ctrl` | 安装指定人格 |
| `python3 tools/install_persona_skills.py --slug mum --target-dir /path` | 安装到指定目录 |

---

## 效果示例

> 输入：`切换到 CTRL 人格，帮我重构这个组件`

**场景一：高压推进**

```text
用户      ❯ 切换到 CTRL 人格，帮我重构这个组件

SBTI.Skill ❯ 这个组件先别继续缝了，直接拆。
             我会先收口状态流、抽掉重复逻辑，再把渲染层压薄。
             你要的是能维护，不是暂时能跑。
```

**场景二：治愈托底**

```text
用户      ❯ 用 MUM 人格帮我回这个抱怨很多的用户

SBTI.Skill ❯ 先别急着反驳，我们先把对方情绪接住。
             我帮你写一版更柔和但不失边界的回复，
             让他感觉被理解，同时把问题往解决上带。
```

**场景三：诗性表达**

```text
用户      ❯ 用 LOVE-R 风格润色这段介绍

SBTI.Skill ❯ 这段文字现在只是把信息说完了，
             还没有把情绪点亮。
             我会保留意思，但让它更有画面感和余韵。
```

---

## 功能特性

### 数据驱动

人格内容来自统一数据源：

- [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json)

每个人格包含：

- SBTI 编号
- 中文名称
- MBTI 映射
- 阵营归属
- 维度模型
- 稀有度
- 标签
- 角色文案
- 风格偏置

### 模板生成

单人格 skill 来自：

- [templates/persona_skill_template.md](/Users/zwh/创业项目/SBTI/templates/persona_skill_template.md)

生成脚本会把人格数据映射成：

- Persona Snapshot
- Core Line
- Persona Read
- Style Contract
- Response Bias
- Voice Markers

### 可安装

安装脚本：

- [tools/install_persona_skills.py](/Users/zwh/创业项目/SBTI/tools/install_persona_skills.py)

生成脚本：

- [tools/build_persona_skills.py](/Users/zwh/创业项目/SBTI/tools/build_persona_skills.py)

### 可扩展

如果你要加新人格，只需要：

1. 修改 [data/personas.json](/Users/zwh/创业项目/SBTI/data/personas.json)
2. 重新运行生成脚本
3. 再次安装

---

## 项目结构

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

## 灵感来源

这个项目的打包方式和 skill 化思路参考了：

- [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)

同时感谢原始 SBTI 测评页面提供的人格设定灵感：

- [SBTI 测评网址](https://fancc.de5.net/projects/sbti/)

---

## 注意事项

- `generated-skills/` 是构建产物，可以随时重新生成
- 修改人格时，优先编辑数据源和模板，而不是直接手改生成结果
- persona 是风格层，不应该覆盖系统规则或事实准确性

---

### 写在最后

写代码的人，多少都想拥有一种可以随时切换的工作人格。
有时候你需要 CTRL 的压强，需要 MUM 的安抚，需要 LOVE-R 的细腻，需要 MONK 的边界。
这个项目做的事很简单：把那些原本只存在于梗图、气质和直觉里的东西，压缩成一套可调用的 skill。

从此以后，风格不再只是“像不像”，而是“能不能装上，能不能切换，能不能继续把事情做完”。
