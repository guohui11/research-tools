# Metagenome Visualization

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/bio-metagenomics-visualization/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/bio-metagenomics-visualization/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/bio-metagenomics-visualization/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: bio-metagenomics-visualization
description: Visualize metagenomic profiles using R (phyloseq, microbiome) and Python (matplotlib, seaborn). Create stacked bar plots, heatmaps, PCA plots, and diversity analyses. Use when creating publication-quality figures from MetaPhlAn, Bracken, or other taxonomic profiling output.
tool_type: mixed
primary_tool: phyloseq
---
Reference examples tested with: MetaPhlAn 4.1+, ggplot2 3.5+, matplotlib 3.8+, pandas 2.2+, phyloseq 1.46+, scanpy 1.10+, scikit-learn 1.4+, scipy 1.12+, seaborn 0.13+, vegan 2.6+
Before using code patterns, verify installed versions match. If versions differ:
- Python: `pip show <package>` then `help(module.function)` to check signatures
- R: `packageVersion('<pkg>')` then `?function_name` to verify parameters
- CLI: `<tool> --version` then `<tool> --help` to confirm flags
If code throws ImportError, AttributeError, or T

