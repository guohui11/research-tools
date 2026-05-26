# 心理健康分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/mental-health-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/mental-health-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/mental-health-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: mental-health-analyzer
description: 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---
心理健康分析技能提供全面的心理健康数据分析功能，帮助用户追踪心理状态、识别情绪模式、监测危机风险和优化应对策略。
**主要功能模块：**
1. **心理健康评估分析** - PHQ-9/GAD-7等量表评分趋势分析
2. **情绪模式识别** - 识别常见情绪、触发因素和应对方式效果
3. **心理治疗进展追踪** - 治疗目标达成和症状改善评估
4. **危机风险评估** - 多级危机风险检测（高/中/低）和预警
5. **睡眠-心理关联分析** - 睡眠质量与心理状态的关联性分析
6. **运动-情绪关联分析** - 运动与情绪改善的关系分析
7. **营养-心理关联分析** - 饮食对情绪和焦虑的影响分析
8. **慢性病-心理关联分析** - 慢性疾病与心理健康的关系分析
技能在以下情况下自动触发：
1. 用户使用 `/mental trend` 查看心理状况趋势
2. 用户使用 `/mental pattern` 分析情绪模式
3. 用户使用 `/mental therapy progress` 查看治疗进展
4. 用户使用 `/crisis assessment` 进行危机风险评估
5. 用户使用 `/mental report` 生成心理健康报告
**本技能不能做的事：**
- ❌ 不进行心理疾病诊断
- ❌ 不开具精神药物处方
- ❌ 不预测自杀风险或自伤行为
- ❌ 不替代专业心理治疗
- ❌ 不处理急性精神危机
**本技能能做的事：**
- ✅ 识别心理健康趋势和模式
- ✅ 评估危机风险等级并发出预警
- ✅ 提供应对策略建议（非治疗性）
- ✅ 追踪治疗进展和目标达成
- ✅ 提供就医建议和专业资源信息
- ✅ 分析心理健康与其他健康因素

