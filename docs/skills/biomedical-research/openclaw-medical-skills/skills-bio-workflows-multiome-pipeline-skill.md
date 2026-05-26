# COPYRIGHT NOTICE

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-multiome-pipeline/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-multiome-pipeline/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/bio-workflows-multiome-pipeline/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

<!--
-->
---
name: bio-workflows-multiome-pipeline
description: End-to-end multiome workflow for joint scRNA-seq + scATAC-seq analysis. Covers data loading, separate modality processing, and WNN integration with Seurat/Signac. Use when analyzing joint scRNA+scATAC data.
tool_type: r
primary_tool: Seurat
workflow: true
depends_on:
- single-cell/data-io
- single-cell/preprocessing
- single-cell/clustering
- single-cell/multimodal-integration
- single-cell/scatac-analysis
qc_checkpoints:
- after_loading: "Both modalities detected per cell"
- after_rna_qc: "RNA quality filters passed"
- after_atac_qc: "TSS enrichment >2, nucleosome signal <4"
- after_wnn: "Joint embedding separates cell types"
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
- read_file
- run_shell_command
---
Complete workflow for 10X Multiome (joint scRNA + scATAC)

