# Wikipedia Search Skill

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/wikipedia-search/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/wikipedia-search/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/wikipedia-search/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: wikipedia-search
description: Search and fetch structured content from Wikipedia using the MediaWiki API for reliable, encyclopedic information
metadata:
openclaw:
emoji: "📚"
requires:
bins: ["python3"]
---
This skill enables Claude to search and fetch content from Wikipedia using the MediaWiki API. It provides more reliable, structured access to Wikipedia than general web search, with support for summaries, full article content, and multi-language access.
Use this skill when you need:
- **Encyclopedic knowledge** — Factual information about people, places, events, concepts
- **Historical information** — Well-documented historical facts, dates, and events
- **Scientific and technical concepts** — Definitions, explanations, and overviews
- **Biographical information** — Details about notable people
- **Geographic information** — Countries, cities, landmarks, and their details
-

