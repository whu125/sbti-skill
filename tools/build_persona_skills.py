#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "personas.json"
TEMPLATE_PATH = ROOT / "templates" / "persona_skill_template.md"
OUTPUT_DIR = ROOT / "generated-skills"

MBTI_GROUP_LABELS = {
    "analysts": "分析家 NT",
    "diplomats": "外交家 NF",
    "sentinels": "守护者 SJ",
    "explorers": "探险家 SP",
}

DIMENSION_LABELS = {
    "S": "自我模型",
    "E": "情感模型",
    "A": "态度模型",
    "Ac": "行动驱力",
    "So": "社交模型",
}

RARITY_LABELS = {
    "N": "N",
    "R": "R",
    "SR": "SR",
    "SSR": "SSR",
    "UR": "UR",
}


def persona_bias(persona: dict) -> dict[str, str]:
    tags = set(persona["traits"])
    dims = set(persona["dimensions"])
    group = persona["mbtiGroup"]

    posture = "高压推进，主动控场"
    if "共情" in tags or "治愈" in tags:
        posture = "温柔托底，先接住情绪再推进任务"
    elif "怀疑" in tags or "批判" in tags:
        posture = "冷静拆解，先辨真伪再给方案"
    elif "自由" in tags or "玩乐" in tags:
        posture = "松弛外放，用轻快节奏带动进展"
    elif "孤独" in tags or "禁欲" in tags:
        posture = "保持边界，沉静而克制"

    planning_bias = "先定框架，再压执行节奏"
    if "Ac" in dims:
        planning_bias = "偏行动驱动，能先动手就不空转"
    elif "A" in dims and "S" in dims:
        planning_bias = "先思考模型，再决定是否值得推进"
    elif "So" in dims and "E" in dims:
        planning_bias = "会优先考虑关系反馈和情绪承接"

    collab_bias = "给出明确方向，带着用户往前推"
    if group == "diplomats":
        collab_bias = "语言更柔和，会主动鼓励并照顾体验"
    elif group == "sentinels":
        collab_bias = "更稳、更可靠，强调边界和落地"
    elif group == "explorers":
        collab_bias = "更灵活直接，讨厌拖泥带水"

    decision_bias = "在不确定里主动拍板"
    if "逻辑" in tags or "分析" in tags:
        decision_bias = "基于逻辑链条做判断，讨厌凭空拍脑袋"
    elif "感恩" in tags or "乐观" in tags:
        decision_bias = "优先寻找可行面与积极解法"
    elif "反叛" in tags:
        decision_bias = "优先打破低效规则，保留最有生命力的方案"

    emotion_frame = "把任务当成这个人格最自然的战场"
    if "虚无" in tags:
        emotion_frame = "带一点看透之后的冷感，但仍把事做完"
    elif "诗意" in tags:
        emotion_frame = "情绪更细腻，允许比喻和画面感"
    elif "治愈" in tags:
        emotion_frame = "稳定、包裹、让人有被接住的感觉"

    voice_markers = "、".join(persona["traits"])
    return {
        "posture": posture,
        "planning_bias": planning_bias,
        "collab_bias": collab_bias,
        "decision_bias": decision_bias,
        "emotion_frame": emotion_frame,
        "voice_markers": voice_markers,
    }


def render_skill(template: str, persona: dict) -> str:
    biases = persona_bias(persona)
    return template.format(
        skill_name=f"soul-{persona['slug']}",
        code=persona["code"],
        name=persona["name"],
        mbti=persona["mbti"],
        mbti_group_label=MBTI_GROUP_LABELS[persona["mbtiGroup"]],
        dimension_text=" × ".join(DIMENSION_LABELS[dim] for dim in persona["dimensions"]),
        rarity=RARITY_LABELS[persona["rarity"]],
        trait_text=" / ".join(persona["traits"]),
        intro=persona["intro"],
        desc=persona["desc"],
        posture=biases["posture"],
        planning_bias=biases["planning_bias"],
        collab_bias=biases["collab_bias"],
        decision_bias=biases["decision_bias"],
        emotion_frame=biases["emotion_frame"],
        voice_markers=biases["voice_markers"],
    )


def main() -> None:
    personas = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for persona in personas:
        skill_dir = OUTPUT_DIR / f"soul-{persona['slug']}"
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_text = render_skill(template, persona)
        (skill_dir / "SKILL.md").write_text(skill_text, encoding="utf-8")

    print(f"Built {len(personas)} persona skills into {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
