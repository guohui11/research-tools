# Systems Paper Writing: Paragraph-Level Structural Blueprint

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/20-ml-paper-writing/systems-paper-writing/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/20-ml-paper-writing/systems-paper-writing/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/20-ml-paper-writing/systems-paper-writing/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: systems-paper-writing
description: Comprehensive guide for writing systems papers targeting OSDI, SOSP, ASPLOS, NSDI, and EuroSys. Provides paragraph-level structural blueprints, writing patterns, venue-specific checklists, reviewer guidelines, LaTeX templates, and conference deadlines. Use this skill for all systems conference paper writing.
version: 1.1.0
author: Orchestra Research
license: MIT
tags: [Systems Paper Writing, OSDI, SOSP, ASPLOS, NSDI, EuroSys, Structural Blueprint, Academic Writing, LaTeX]
---
Fine-grained structural guidance for writing **10–12 page systems papers** targeting top systems venues: OSDI, SOSP, ASPLOS, NSDI, and EuroSys. This skill provides page allocation per section, paragraph-level blueprints, and writing patterns distilled from authoritative guides and best-paper analysis.
| Scenario | Use This Skill | Use ml-paper-writing Instead |
|---------

