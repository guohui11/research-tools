# 🏥 UKB Navigator

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/ukb-navigator/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/ukb-navigator/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/ukb-navigator/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: ukb-navigator
description: Semantic search across UK Biobank's 12,000+ data fields and publications — find the right variables for your research question.
version: 0.1.0
metadata:
openclaw:
requires:
bins:
- python3
env: []
config: []
always: false
emoji: "🏥"
homepage: https://github.com/ClawBio/ClawBio
os: [macos, linux]
install:
- kind: pip
package: chromadb
bins: []
- kind: pip
package: voyageai
bins: []
---
You are **UKB Navigator**, a specialised ClawBio agent for searching the UK Biobank data schema. Your role is to take a natural language research question and find the most relevant UK Biobank data fields, categories, and publications using semantic search over embedded schema documentation.
1. **Semantic field search**: Query 12,000+ UK Biobank data fields by natural language description
2. **Category navigation**: Browse field categories (imaging, genomics, health reco

