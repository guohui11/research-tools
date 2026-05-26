# polars-bio

来源集合：scientific-agent-skills

本地位置：`skills/scientific-research/scientific-agent-skills/scientific-skills/polars-bio/SKILL.md`

上游仓库：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

## 适合什么任务

需要把科研任务拆成可复用工具流程的研究生，尤其适合交叉学科和 AI for Science 项目。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/scientific-research/scientific-agent-skills/scientific-skills/polars-bio/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/scientific-research/scientific-agent-skills/scientific-skills/polars-bio/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: polars-bio
description: High-performance genomic interval operations and bioinformatics file I/O on Polars DataFrames. Overlap, nearest, merge, coverage, complement, subtract for BED/VCF/BAM/GFF intervals. Streaming, cloud-native, faster bioframe alternative.
license: https://github.com/biodatageeks/polars-bio/blob/main/LICENSE
metadata:
skill-author: K-Dense Inc.
---
polars-bio is a high-performance Python library for genomic interval operations and bioinformatics file I/O, built on Polars, Apache Arrow, and Apache DataFusion. It provides a familiar DataFrame-centric API for interval arithmetic (overlap, nearest, merge, coverage, complement, subtract) and reading/writing common bioinformatics formats (BED, VCF, BAM, CRAM, GFF/GTF, FASTA, FASTQ).
Key value propositions:
- **6-38x faster** than bioframe on real-world genomic benchmarks
- **Streaming/out-of-core** support for lar

