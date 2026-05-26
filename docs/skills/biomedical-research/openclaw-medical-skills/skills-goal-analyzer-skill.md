# 健康目标分析器技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/goal-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/goal-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/goal-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: goal-analyzer
description: 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---
分析健康目标数据,识别目标模式和进度,评估目标达成情况,并提供个性化目标管理建议。
验证设定的新目标是否符合SMART原则。
**验证维度**:
- **S**pecific(具体性)
- 目标是否明确具体
- 是否有清晰的定义
- 是否避免模糊表述
- **M**easurable(可衡量性)
- 是否有可量化的指标
- 是否有明确的衡量标准
- 是否可以追踪进度
- **A**chievable(可实现性)
- 目标是否现实可行
- 是否考虑了当前状况
- 是否在合理时间范围内
- 减重目标:建议每周0.5-1公斤
- 运动目标:建议每周3-5次,每次30-60分钟
- **R**elevant(相关性)
- 目标是否与健康相关
- 是否符合用户整体健康计划
- 是否与现有目标协调
- **T**ime-bound(有时限)
- 是否有明确的截止日期
- 时间框架是否合理
- 是否有阶段性里程碑
**输出**:
- SMART评分(每个维度1-5分)
- 总体评分和等级(S级/A级/B级/C级)
- 改进建议
- 目标优化方案
**示例评估**:

