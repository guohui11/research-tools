# COPYRIGHT NOTICE

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/biomni-general-agent/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/biomni-general-agent/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/biomni-general-agent/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

<!--
-->
---
name: biomni-general-agent
description: Use the local Biomni checkout to orchestrate its 150+ biomedical tools, databases, and know-how workflows for complex research questions.
allowed-tools:
- read_file
- run_shell_command
---
- **description (10-20 chars):** Omni bio agent
- **keywords:** multi-tool, know-how, tutorials, protocols, databases
- **measurable_outcome:** Execute a Biomni workflow that touches ≥2 tool categories and returns a cited research summary or artifact within 15 minutes per request.
1. **Environment:** `cd repo && pip install .` (or follow tutorials env set up). Activate the environment with required GPUs if using heavy models.
2. **Select mode:** Choose Standard (full stack), Light (API-only), or Commercial (license-safe) per task.
3. **Plan tools:** Query the Know-How library for relevant protocols/databases before executing.
4. **Execute notebooks/s

