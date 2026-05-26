# COPYRIGHT NOTICE

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/scrna-qc/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/scrna-qc/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/scrna-qc/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

<!--
-->
---
name: scrna-qc
description: Execute the MAD-based single-cell RNA-seq QC workflow (scripts + Python API) to filter low-quality cells and emit reports plus filtered AnnData files.
measurable_outcome: Produce filtered .h5ad files, before/after plots, and qc_summary.json within 20 minutes per dataset.
allowed-tools:
- read_file
- run_shell_command
---
- **description (10-20 chars):** QC autopilot
- **keywords:** scRNAseq, MAD, h5ad, QC, plots
1. Accept `.h5ad`, 10x `.h5`, or 10x directory inputs; set mitochondrial/ribosomal patterns as needed.
2. Run `qc_analysis.py` (CLI) or call `qc_core` helpers to compute metrics, apply MAD thresholds, and filter cells/genes.
3. Generate standard plots (metrics before/after, threshold overlays) plus filtered data artifacts.
4. Document parameters (mad_counts/genes/mt, mt_threshold, min_cells, log1p flag) inside the summary JSON.
5. Provide

