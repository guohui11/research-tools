# PaperSpine Orchestrator

来源集合：PaperSpine

本地位置：`skills/academic-writing/paper-spine/dist/codex/paper-spine/SKILL.md`

上游仓库：[WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)

## 适合什么任务

需要进行论文精读、文献整理、选题梳理、论文草稿写作和修改润色的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/academic-writing/paper-spine/dist/codex/paper-spine/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/academic-writing/paper-spine/dist/codex/paper-spine/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: paper-spine
description: Internal orchestrator — users should use /paperspine to start a full workflow.
---
Use this skill as the suite entrypoint. It is the main orchestrator: it routes
the user to UI, intake, research, citation, rewrite, build, LaTeX,
translate, audit, and update branch skills.
PaperSpine is a research-writing workflow, not a prose patcher. Its job is to
learn the target scene and strong examples first, force a user-confirmed
motivation, design the paper row by row, and only then write or rebuild the
manuscript.
Never fabricate data, metrics, p-values, datasets, citations, figures, or
experimental claims. User materials are authoritative for this paper's results.
External examples teach structure and rhetoric only.
Prefer reading `paper_rewriting_output/paper_spine_config.json`. If it is
missing, route to `paper-spine-intake` or ask the same fields directly.

