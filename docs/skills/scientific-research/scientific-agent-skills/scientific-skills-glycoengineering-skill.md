# Glycoengineering

来源集合：scientific-agent-skills

本地位置：`skills/scientific-research/scientific-agent-skills/scientific-skills/glycoengineering/SKILL.md`

上游仓库：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

## 适合什么任务

需要把科研任务拆成可复用工具流程的研究生，尤其适合交叉学科和 AI for Science 项目。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/scientific-research/scientific-agent-skills/scientific-skills/glycoengineering/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/scientific-research/scientific-agent-skills/scientific-skills/glycoengineering/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: glycoengineering
description: Analyze and engineer protein glycosylation. Scan sequences for N-glycosylation sequons (N-X-S/T), predict O-glycosylation hotspots, and access curated glycoengineering tools (NetOGlyc, GlycoShield, GlycoWorkbench). For glycoprotein engineering, therapeutic antibody optimization, and vaccine design.
license: Unknown
metadata:
skill-author: Kuan-lin Huang
---
Glycosylation is the most common and complex post-translational modification (PTM) of proteins, affecting over 50% of all human proteins. Glycans regulate protein folding, stability, immune recognition, receptor interactions, and pharmacokinetics of therapeutic proteins. Glycoengineering involves rational modification of glycosylation patterns for improved therapeutic efficacy, stability, or immune evasion.
**Two major glycosylation types:**
- **N-glycosylation**: Attached to asparagine (N) in t

