# PaperSpine Citation

来源集合：PaperSpine

本地位置：`skills/academic-writing/paper-spine/dist/claude/skills/paper-spine-citation/SKILL.md`

上游仓库：[WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)

## 适合什么任务

需要进行论文精读、文献整理、选题梳理、论文草稿写作和修改润色的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/academic-writing/paper-spine/dist/claude/skills/paper-spine-citation/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/academic-writing/paper-spine/dist/claude/skills/paper-spine-citation/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: paper-spine-citation
description: Builds a citation support bank for Introduction, Discussion, and background claims.
---
Use this branch after research and before final writing. Its job is not to learn
paper structure. Its job is to build a verified citation support bank that can
support literature statements in the user's manuscript.
Read `paper_rewriting_output/paper_spine_config.json`, especially:
- `target_name`
- `scene`
- `output_language`
- `reference_mode`
- `reference_paths`
- `citation_target_count` defaulting to `20`
- `materials_dir`
- `draft_path`
- `research_dossier.md`
- `sota_gap_map.md`
- `reference_materials/source_index.md`
Create:

