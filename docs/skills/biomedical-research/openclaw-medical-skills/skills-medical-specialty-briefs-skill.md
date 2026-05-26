# Medical Specialty Briefs

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/medical-specialty-briefs/SKILL.MD`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/medical-specialty-briefs/SKILL.MD`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/medical-specialty-briefs/SKILL.MD 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: medical-specialty-briefs
description: Generate daily or on-demand medical research briefs for any medical specialty. Searches latest research from top-tier journals, delivers concise summaries with 1-sentence takeaways, images when available, and direct links. Use when user asks for medical news, research updates, journal briefs, or specialty-specific medical updates for specialties like endocrinology, cardiology, oncology, neurology, etc.
---
Generate curated medical research briefs for any medical specialty in a Google News-style format.
- User asks for "medical news" or "research updates" for a specific specialty
- User wants a "daily brief" for their medical field
- User mentions journal names (NEJM, JAMA, Lancet, etc.) with research queries
- User is a clinician seeking specialty-specific updates
Each brief item should include:
1. **Headline** - Clear, concise title
2. **O

