# ClinicalTrials.gov Database

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/clinicaltrials-database/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/clinicaltrials-database/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/clinicaltrials-database/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: clinicaltrials-database
description: "Query ClinicalTrials.gov via API v2. Search trials by condition, drug, location, status, or phase. Retrieve trial details by NCT ID, export data, for clinical research and patient matching."
---
ClinicalTrials.gov is a comprehensive registry of clinical studies conducted worldwide, maintained by the U.S. National Library of Medicine. Access API v2 to search for trials, retrieve detailed study information, filter by various criteria, and export data for analysis. The API is public (no authentication required) with rate limits of ~50 requests per minute, supporting JSON and CSV formats.
This skill should be used when working with clinical trial data in scenarios such as:
- **Patient matching** - Finding recruiting trials for specific conditions or patient populations
- **Research analysis** - Analyzing clinical trial trends, outcomes, or stud

