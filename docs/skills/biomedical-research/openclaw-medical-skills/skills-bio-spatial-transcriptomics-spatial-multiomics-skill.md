# Spatial Multi-omics Analysis

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/bio-spatial-transcriptomics-spatial-multiomics/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/bio-spatial-transcriptomics-spatial-multiomics/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/bio-spatial-transcriptomics-spatial-multiomics/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: bio-spatial-transcriptomics-spatial-multiomics
description: Analyze high-resolution spatial platforms like Slide-seq, Stereo-seq, and Visium HD. Use when working with subcellular resolution or high-density spatial data.
tool_type: python
primary_tool: squidpy
---
Reference examples tested with: Cellpose 3.0+, matplotlib 3.8+, numpy 1.26+, scanpy 1.10+, scipy 1.12+, spatialdata 0.1+, squidpy 1.3+
Before using code patterns, verify installed versions match. If versions differ:
- Python: `pip show <package>` then `help(module.function)` to check signatures
If code throws ImportError, AttributeError, or TypeError, introspect the installed
package and adapt the example to match the actual API rather than retrying.
**"Analyze my high-resolution spatial data"** → Process subcellular-resolution spatial platforms (Xenium, MERFISH, Slide-seq, Stereo-seq) including cell segmentation, binn

