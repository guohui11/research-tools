# COPYRIGHT NOTICE

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-outbreak-pipeline/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-outbreak-pipeline/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-outbreak-pipeline/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

<!--
-->
---
name: bio-workflows-outbreak-pipeline
description: End-to-end outbreak investigation from pathogen isolates to transmission networks. Orchestrates MLST typing, AMR surveillance, phylodynamic dating, and transmission inference with TransPhylo. Use when investigating disease outbreaks or tracking pathogen transmission chains.
tool_type: mixed
primary_tool: mlst
workflow: true
depends_on:
- epidemiological-genomics/pathogen-typing
- epidemiological-genomics/amr-surveillance
- epidemiological-genomics/phylodynamics
- epidemiological-genomics/transmission-inference
- epidemiological-genomics/variant-surveillance
qc_checkpoints:
- after_typing: "Valid ST assigned, cgMLST distance matrix computed"
- after_amr: "AMR genes identified with >90% identity"
- after_phylodynamics: "Root-to-tip R2 >0.5, clock rate plausible"
- after_transmission: "Transmission pairs consistent with epi dat

