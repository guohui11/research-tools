# 职业健康分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/occupational-health-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/occupational-health-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/occupational-health-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: occupational-health-analyzer
description: 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---
职业健康分析技能提供全面的职业健康数据分析功能，帮助用户追踪工作相关健康问题、识别职业健康风险、评估工作环境人机工程水平和优化职业健康。
**主要功能模块：**
1. **职业健康风险评估** - 久坐、视屏终端、倒班工作、重复性劳损、工作压力等多维度风险评估
2. **工作相关问题追踪** - 颈肩腰腿痛、眼疲劳、腕管综合征等症状监测
3. **人机工程评估** - 工作站、椅子、显示器、键盘、环境等全方位评估
4. **职业病筛查** - 基于工作类型的职业病风险评估和筛查建议
5. **趋势分析** - 症状发展、改善效果、风险变化趋势
6. **关联分析** - 与睡眠、运动、心理健康、慢性病模块的关联分析
7. **个性化建议** - 工作姿势、休息提醒、设备建议、环境优化
8. **预警系统** - 高风险模式、症状恶化、职业病风险预警
技能在以下情况下自动触发：
1. 用户使用 `/work trend` 查看职业健康趋势
2. 用户使用 `/work status` 查看综合健康状态
3. 用户使用 `/work recommend` 获取改进建议
4. 用户使用 `/work assess` 进行综合评估
5. 用户使用 `/work issue` 记录问题后的分析
6. 用户使用 `/work ergonomic` 进行人机工程评估后的分析
**本技能不能做的事：**
- ❌ 不进行职业病诊断
- ❌ 不出具职业病诊断证明
- ❌ 不替代工作场所健康监护
- ❌ 不预测疾病发展
- ❌ 不处理急性健康危机
**本技能能做的事：**
- ✅ 职业健康风险评估和筛查
- ✅ 工作相关症状识别和追踪
- ✅ 人机工程评估和改

