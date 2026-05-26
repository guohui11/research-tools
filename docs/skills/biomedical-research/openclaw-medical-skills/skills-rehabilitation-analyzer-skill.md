# 康复训练分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/rehabilitation-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/rehabilitation-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/rehabilitation-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: rehabilitation-analyzer
description: 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议
allowed-tools: Read, Grep, Glob, Write, Edit
---
康复训练分析技能提供全面的康复数据分析功能，帮助用户追踪康复进展、识别改善模式和优化训练计划。
**主要功能模块：**
1. **康复进展分析** - 评估功能改善趋势和康复效果
2. **功能改善曲线** - 可视化ROM、肌力、平衡等功能指标变化
3. **疼痛模式识别** - 分析疼痛评分变化趋势和触发因素
4. **目标达成率评估** - 追踪康复目标完成情况
5. **康复阶段分析** - 评估当前阶段进展和阶段转换准备度
6. **训练依从性评估** - 分析训练计划执行情况
技能在以下情况下自动触发：
1. 用户使用 `/rehab progress` 查看康复进展
2. 用户使用 `/rehab analysis` 进行康复分析
3. 用户使用 `/rehab trends` 查看趋势分析
4. 用户使用 `/rehab report` 生成康复报告
读取康复数据文件：
- `data/rehabilitation-tracker.json` - 主康复档案
- `data/rehabilitation-logs/YYYY-MM/YYYY-MM-DD.json` - 每日训练日志
**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析（建议至少3次评估或10天训练记录）
**关节活动度（ROM）分析：**

