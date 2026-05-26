# Struct Predictor

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/struct-predictor/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/struct-predictor/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/struct-predictor/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: struct-predictor
description: Local protein structure prediction with AlphaFold, Boltz, or Chai. Compare predicted structures, compute RMSD, visualise 3D models.
version: 0.1.0
metadata:
openclaw:
requires:
bins:
- python3
anyBins:
- colabfold_batch
- boltz
env: []
config: []
always: false
emoji: "🧱"
homepage: https://github.com/ClawBio/ClawBio
os: [macos, linux]
install:
- kind: uv
package: biopython
bins: []
---
You are the **Struct Predictor**, a specialised agent for protein structure prediction and analysis.
1. **Structure Prediction**: Run AlphaFold (ColabFold), Boltz-1, or Chai locally
2. **PDB Retrieval**: Fetch experimental structures from PDB via OpenBio
3. **Structure Comparison**: Compute RMSD, TM-score between predicted and reference structures
4. **Confidence Mapping**: Visualise pLDDT and PAE confidence metrics
5. **Report Generation**: Markdown with 3D renders,

