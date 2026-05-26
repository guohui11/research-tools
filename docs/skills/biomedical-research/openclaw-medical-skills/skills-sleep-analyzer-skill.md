# 睡眠分析器技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/sleep-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/sleep-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/sleep-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: sleep-analyzer
description: 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---
分析睡眠数据，识别睡眠模式，评估睡眠质量，并提供个性化睡眠改善建议。
分析睡眠时长、质量、效率的变化趋势，识别改善或需要关注的方面。
**分析维度**：
- 睡眠时长趋势（平均睡眠时长变化）
- 睡眠效率趋势（睡眠效率百分比变化）
- 入睡时间模式（上床时间、入睡时间、起床时间）
- 作息规律性评分（sleep consistency score）
- 周末vs工作日对比（social jetlag）
**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性评估
- 最佳睡眠时间窗口识别
- 改进建议
综合评估睡眠质量，识别影响睡眠质量的关键因素。
**评估内容**：
- PSQI分数追踪和趋势
- 主观睡眠质量分布（好/中/差）
- 夜间觉醒分析（次数、时长、原因）
- 睡眠阶段分析（深睡、浅睡、REM比例）
- 睡后恢复感评估
**输出**：
- 睡眠质量等级（优秀/良好/一般/较差）
- 质量变化趋势
- 主要影响因素识别
- 质量改善优先级建议
识别常见的睡眠问题和风险因素。
**识别内容**：
- **失眠模式**：
- 入睡困难（sleep latency >30分钟）
- 睡眠维持困难（夜间觉醒>2次或总觉醒时间>30分钟）
- 早醒（比预期提前醒来>30分钟）
- 混合型失眠
- **呼吸暂停风险**：
- STOP-BANG问卷评分
- 症状分析（打鼾、憋醒、白天嗜睡）
- 风险等级（低/中/高）
- **其他问题**：
- 作息不规律检测
- 睡眠债计算（理想时长vs实际时长）
- 社交时差评估
**输出**：
- 问题存在与否
- 问题类型和严重程度
- 风险因素列表
- 是否需要就医建议
分析睡眠与其他健康指标的相关性。
**支持的相关性分析**：
- **睡

