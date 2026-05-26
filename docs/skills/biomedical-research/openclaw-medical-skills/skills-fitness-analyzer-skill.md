# 运动分析器技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/fitness-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/fitness-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/fitness-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: fitness-analyzer
description: 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---
分析运动数据，识别运动模式，评估健身进展，并提供个性化训练建议。
分析运动量、频率、强度的变化趋势，识别改善或需要调整的方面。
**分析维度**：
- 运动量趋势（时长、距离、卡路里）
- 运动频率趋势（每周运动天数）
- 强度分布变化（低/中/高强度占比）
- 运动类型偏好变化
**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议
追踪特定运动类型的进步情况，量化健身效果。
**支持的进步追踪**：
- **跑步进步**：配速提升、距离增加、心率改善
- **力量训练进步**：重量增加、容量提升、RPE变化
- **耐力进步**：运动时长增加、距离延长
- **柔韧性进步**：关节活动度改善
**输出**：
- 开始值 vs 当前值
- 改善百分比
- 进步可视化
- 达成的里程碑
识别用户的运动习惯和模式。
**分析内容**：
- 常用运动时间（早晨/下午/晚上）
- 运动频率模式（每周几天）
- 运动类型偏好
- 休息日分布
- 运动一致性评分
**输出**：
- 习惯总结
- 一致性评分（0-100）
- 优化建议
- 习惯养成建议
分析运动与其他健康指标的相关性。
**支持的相关性分析**：
- **运动 ↔ 体重**：运动消耗与体重变化的关系
- **运动 ↔ 血压**：运动对血压的长期影响
- **运动 ↔ 血糖**：运动对血糖控制的效果
- **运动 ↔ 情绪/睡眠**：运动对情绪和睡眠的影响
**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议
基于用户数据生成个性化运动建议。
**建议类型**：
- **运动频率建议**：是否需要增加/减少运动频率
- **运动强度建议**：强度调整

