# 中医体质辨识分析器技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/tcm-constitution-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/tcm-constitution-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/tcm-constitution-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: tcm-constitution-analyzer
description: 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---
分析中医体质数据,识别体质类型,评估体质特征,并提供个性化养生改善建议。
基于《中医体质分类与判定》标准进行体质辨识。
**评估维度**:
- 9种体质类型评分(平和质、气虚质、阳虚质、阴虚质、痰湿质、湿热质、血瘀质、气郁质、特禀质)
- 主体质判定
- 兼夹体质识别
- 体质特征分析
**评估方法**:
- 60题标准化问卷
- 5分制评分(没有/很少/有时/经常/总是)
- 转化分数计算(0-100分)
**输出**:
- 体质类型判定结果
- 各体质评分
- 体质特征描述
- 个体化养生建议
综合评估用户的体质特征。
**分析内容**:
- **形体特征**:
- 体型特点
- 面色表现
- 舌象脉象
- **心理特征**:
- 性格特点
- 情绪倾向
- **发病倾向**:
- 易感疾病
- 健康风险
- **适应能力**:
- 环境适应
- 季节适应
**输出**:
- 体质类型分类
- 特征描述
- 风险评估
- 调理优先级
追踪体质变化,评估调理效果。
**分析内容**:
- 多次评估对比
- 评分变化趋势
- 体质稳定性分析
- 调理效果评估
**输出**:
- 趋势图表
- 改善幅度
- 稳定性评估
- 继续调理建议
分析体质与其他健康指标的相关性。
**支持的相关性分析**:
- **体质 ↔ 营养**:
- 体质类型与饮食偏好的关系
- 营养状况对体质的影响
- 个性化饮食建议
- **体质 ↔ 运动**:
- 不同体质适合的运动类型
- 运动对体质改善的作用
- **体质 ↔ 睡眠**:
- 体质与睡眠质量的关系
- 睡眠对体质的影响
- **体质 ↔ 慢性病**:
- 不同体质易患疾病
- 体质与疾病的关系
**输出**:
- 相关系数
- 相关性强度

