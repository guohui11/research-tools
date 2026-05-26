# 营养分析器技能

来源集合：OpenClaw-Medical-Skills

本地位置：`skills/biomedical-research/openclaw-medical-skills/skills/nutrition-analyzer/SKILL.md`

上游仓库：[FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)

## 适合什么任务

医学、生信、药物发现、临床 NLP、组学分析方向的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/biomedical-research/openclaw-medical-skills/skills/nutrition-analyzer/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/biomedical-research/openclaw-medical-skills/skills/nutrition-analyzer/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: nutrition-analyzer
description: 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---
分析饮食和营养数据，识别营养模式，评估营养状况，并提供个性化营养改善建议。
分析营养素摄入的变化趋势，识别改善或需要关注的方面。
**分析维度**：
- 宏量营养素趋势（蛋白质、碳水、脂肪、纤维、卡路里）
- 微量营养素趋势（维生素、矿物质）
- 热量来源分布变化
- 餐食模式（饮食时间、频率）
- 食物类别偏好
**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议
评估营养素摄入是否达到推荐标准（RDA/AI）。
**评估内容**：
- **宏量营养素评估**：
- 蛋白质摄入量和质量
- 碳水化合物类型分布（精制 vs 复杂碳水）
- 脂肪类型分布（饱和/单不饱和/多不饱和/反式脂肪）
- 膳食纤维摄入量
- **维生素评估**：
- 维生素A、C、D、E、K
- 维生素B族（B1、B2、B3、B6、B12、叶酸、泛酸、生物素）
- 与RDA对比
- 缺乏风险评估
- **矿物质评估**：
- 常量矿物质：钙、磷、镁、钠、钾、氯、硫
- 微量矿物质：铁、锌、铜、锰、碘、硒、铬、钼
- 与RDA对比
- 缺乏风险评估
- **特殊营养素评估**：
- Omega-3脂肪酸（EPA、DHA、ALA）
- 胆碱
- 辅酶Q10
- 植物化学物（类黄酮、类胡萝卜素等）
**输出**：
- 每种营养素的达成率
- 缺乏/不足/充足/过量分级
- 缺乏风险识别
- 优先改善建议
综合评估用户的营养状况。
**评估内容**：
- **整体营养质量评分**：
- 营养密度评分
- 食物多样性评分
- 均衡饮食评分
- **营养模式识别**：
- 饮食模式类型（地中海式、DASH、素食等）
- 饮食时间模式（进食频率、进食窗口）
- 零食和加餐模式
- **营养风险

