# 减肥分析技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/weightloss-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/weightloss-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/weightloss-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: weightloss-analyzer
description: 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段
---
分析减肥数据，计算代谢率，追踪能量缺口，管理减肥阶段。
**BMI计算与分类**
- BMI = 体重(kg) / 身高(m)²
- 分类标准（WHO亚洲标准）：
- 偏瘦：BMI < 18.5
- 正常：18.5 ≤ BMI < 24
- 超重：24 ≤ BMI < 28
- 肥胖：BMI ≥ 28
**体脂率评估**
- 男性：15-20%（正常），20-25%（偏高），>25%（肥胖）
- 女性：20-25%（正常），25-30%（偏高），>30%（肥胖）
**围度分析**
- 腰围评估
- 男性：< 90cm（正常），≥ 90cm（腹部肥胖）
- 女性：< 85cm（正常），≥ 85cm（腹部肥胖）
- 腰臀比
- 男性：< 0.9（正常），≥ 0.9（腹部肥胖）
- 女性：< 0.85（正常），≥ 0.85（腹部肥胖）
**理想体重计算**
- BMI法：理想体重 = 身高(m)² × 22
- Broca法修正：理想体重 = (身高cm - 100) × 0.9
**Harris-Benedict公式（1919原始版）**
- 男性：BMR = 88.362 + (13.397 × 体重kg) + (4.799 × 身高cm) - (5.677 × 年龄)
- 女性：BMR = 447.593 + (9.247 × 体重kg) + (3.098 × 身高cm) - (4.330 × 年龄)
**Mifflin-St Jeor公式（推荐，更准确）**
- 男性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) + 5
- 女性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) - 161
**Katch-McArdle公式（基于瘦体重）**
- BMR = 370 + (21.6 × 瘦体重kg)
- 瘦体重 = 体重kg × (1 -

