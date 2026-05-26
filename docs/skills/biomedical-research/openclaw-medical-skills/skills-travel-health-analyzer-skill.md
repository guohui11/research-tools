# 旅行健康分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/travel-health-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/travel-health-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/travel-health-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: travel-health-analyzer
description: 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。
allowed-tools: Read, Write, Grep, Glob
---
**本技能提供的所有健康建议和信息仅供参考,不能替代专业医疗建议。**
- ⚠️ **所有建议必须由专业医生审核**
- ⚠️ **疫苗接种和用药方案必须由医生制定**
- ⚠️ **不提供具体的医疗处方或诊断**
- ⚠️ **健康风险数据来源于WHO/CDC,可能存在滞后性**
- ⚠️ **紧急情况下请立即就医**
---
分析用户的旅行计划,提供全面的健康准备建议。
**输入**: 旅行目的地、日期、旅行目的
**输出**:
- 目的地健康风险评估
- 必要和推荐的疫苗接种清单
- 旅行药箱建议清单
- 预防措施建议
- 旅行前准备时间表
**分析要点**:
- 识别目的地传染病风险
- 评估食物和饮水安全
- 确认环境风险(高温、高原等)
- 检查当前疫情爆发信息
- 提供WHO/CDC参考链接
---
基于WHO/CDC数据,对旅行目的地进行专业级健康风险评估。
**数据源**:
- 世界卫生组织(WHO)国际旅行健康
- 美国疾控中心(CDC)旅行健康
- 当地卫生部门官方数据
**评估维度**:
- 传染病风险(登革热、疟疾、霍乱、甲肝等)
- 食物和饮水安全
- 环境风险(高温、高原、空气污染)
- 季节性风险
- 当前疫情爆发警报
**风险等级**:
- 🟢 **低风险** - 常规预防措施
- 🟡 **中等风险** - 需要特别注意
- 🔴 **高风险** - 需要采取严格预防措施
- ⚫ **极高风险** - 建议推迟旅行或采取特殊防护
**输出格式**:

