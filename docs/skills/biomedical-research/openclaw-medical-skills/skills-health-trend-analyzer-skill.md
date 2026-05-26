# 健康趋势分析器

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/health-trend-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/health-trend-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/health-trend-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: health-trend-analyzer
description: 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（ECharts图表）。
allowed-tools: Read, Grep, Glob, Write
---
分析一段时间内健康数据的趋势和模式，识别变化、相关性，并提供数据驱动的健康洞察。
- **体重/BMI 趋势**：追踪体重和BMI随时间的变化，评估健康趋势
- **症状模式**：识别反复出现的症状、频率变化、潜在诱因
- **药物依从性**：分析用药规律，识别漏服模式和改善空间
- **化验结果趋势**：追踪生化指标变化（胆固醇、血糖、血压等）
- **情绪与睡眠**：关联情绪状态与睡眠质量，识别心理健康趋势
- **药物-症状相关性**：识别新药物是否与症状变化相关
- **生活方式影响**：关联饮食/睡眠与症状和情绪
- **治疗效果评估**：衡量治疗是否导致改善
- **周期-症状相关性**：女性健康追踪中的周期相关性
- **显著变化**：警告快速体重变化、新症状、药物变化
- **恶化模式**：早期识别健康状况下降
- **改善识别**：强调积极的健康变化
- **阈值警报**：接近危险水平时警告（辐射、BMI极值）
- **风险评估**：基于趋势识别风险因素
- **预防建议**：基于模式建议预防措施
- **早期预警**：在问题变得严重之前预测
当用户提到以下场景时，使用此技能：
**通用询问**：
- ✅ "过去一段时间我的健康有什么变化？"
- ✅ "分析我的健康趋势"
- ✅ "我的身体状况有什么变化？"
- ✅ "健康状况总结"
**具体维度**：
- ✅ "我的体重/BMI有什么趋势？"
- ✅ "分析我的症状模

