# 家庭健康分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/family-health-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/family-health-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/family-health-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: family-health-analyzer
description: 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议
allowed-tools: Read, Write, Grep, Glob
---
本技能提供家庭健康数据的深度分析,包括:
- 遗传风险评估
- 家族疾病模式识别
- 家庭共同问题分析
- 个性化预防建议
- 可视化报告生成
当用户请求以下内容时,使用此技能:
- "家庭健康报告"
- "家族病史分析"
- "遗传风险评估"
- "家庭健康趋势"
- 执行 `/family report` 命令
- 执行 `/family risk` 命令
识别用户请求类型:
- 家族病史分析
- 遗传风险评估
- 家庭健康趋势
- 家庭健康报告
**数据源:**
1. 主数据文件: `data/family-health-tracker.json`
2. 集成模块数据:
- `data/hypertension-tracker.json`
- `data/diabetes-tracker.json`
- `data/profile.json`
**验证项目:**
- 关系完整性
- 年龄合理性
- 数据一致性
**识别算法:**
1. 家族聚集性分析
2. 遗传模式识别
3. 早发病例识别(通常<50岁)
**加权计算:**

