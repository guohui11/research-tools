# AI健康分析器

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/ai-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/ai-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/ai-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: ai-analyzer
description: AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。
allowed-tools: Read, Grep, Glob, Write
---
基于AI技术的综合健康分析系统，提供智能健康洞察、风险预测和个性化建议。
- **多维度数据整合**: 整合基础指标、生活方式、心理健康、医疗历史等4类数据源
- **异常模式识别**: 使用CUSUM、Z-score等算法检测异常值和变化点
- **相关性分析**: 计算不同健康指标之间的相关性（皮尔逊、斯皮尔曼）
- **趋势预测**: 基于历史数据进行趋势分析和预测
- **高血压风险**: 基于Framingham风险评分模型
- **糖尿病风险**: 基于ADA糖尿病风险评分标准
- **心血管疾病风险**: 基于ACC/AHA ASCVD指南
- **营养缺乏风险**: 基于RDA达成率和饮食模式分析
- **睡眠障碍风险**: 基于PSQI和睡眠模式分析
- **基础个性化**: 基于年龄、性别、BMI、活动水平等静态档案
- **建议分级**: Level 1（一般性）、Level 2（参考性）、Level 3（医疗建议）
- **循证依据**: 基于医学指南和循证医学证据
- **可操作性**: 提供具体、可行的改进建议
- **智能问答**: 支持健康数据查询、趋势分析、相关性查询等
- **上下文理解**: 维护对话历史，支持多轮对话
- **意图识别**: 识别用户查询意图，提供精准回复
- **综合报告**: 包含所有维度健康数据、AI洞察、风险评估
- **快速摘要**: 关键指标概览、异常警示、主要建议
- **风险评估报告**: 各类疾病风险、风险因素分析、预防措施
- **趋势分析报告**: 多维度趋势、变化点识别、预测分析
- **HTML交互式报告**: ECharts图表、Tailwind CSS样式
当用户提到以下场景时，使用此技能：
**通用询问**

