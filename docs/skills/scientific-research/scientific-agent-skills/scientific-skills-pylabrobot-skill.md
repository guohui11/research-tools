# PyLabRobot

来源集合：scientific-agent-skills

本地位置：`skills/scientific-research/scientific-agent-skills/scientific-skills/pylabrobot/SKILL.md`

上游仓库：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

## 适合什么任务

需要把科研任务拆成可复用工具流程的研究生，尤其适合交叉学科和 AI for Science 项目。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/scientific-research/scientific-agent-skills/scientific-skills/pylabrobot/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/scientific-research/scientific-agent-skills/scientific-skills/pylabrobot/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: pylabrobot
description: Vendor-agnostic lab automation framework. Use when controlling multiple equipment types (Hamilton, Tecan, Opentrons, plate readers, pumps) or needing unified programming across different vendors. Best for complex workflows, multi-vendor setups, simulation. For Opentrons-only protocols with official API, opentrons-integration may be simpler.
license: MIT license
metadata:
skill-author: K-Dense Inc.
---
PyLabRobot is a hardware-agnostic, pure Python Software Development Kit for automated and autonomous laboratories. Use this skill to control liquid handling robots, plate readers, pumps, heater shakers, incubators, centrifuges, and other laboratory automation equipment through a unified Python interface that works across platforms (Windows, macOS, Linux).
Use this skill when:
- Programming liquid handling robots (Hamilton STAR/STARlet, Opentrons OT-2, Tecan

