# Deepspeed Skill

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/08-distributed-training/deepspeed/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/08-distributed-training/deepspeed/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/08-distributed-training/deepspeed/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: deepspeed
description: Expert guidance for distributed training with DeepSpeed - ZeRO optimization stages, pipeline parallelism, FP16/BF16/FP8, 1-bit Adam, sparse attention
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [DeepSpeed, Distributed Training, ZeRO, Pipeline Parallelism, Mixed Precision, Optimization, Microsoft, Large-Scale Training, FP16, FP8]
dependencies: [deepspeed, torch, transformers, accelerate]
---
Comprehensive assistance with deepspeed development, generated from official documentation.
This skill should be triggered when:
- Working with deepspeed
- Asking about deepspeed features or APIs
- Implementing deepspeed solutions
- Debugging deepspeed code
- Learning deepspeed best practices
**Pattern 1:** DeepNVMe Contents Requirements Creating DeepNVMe Handles Using DeepNVMe Handles Blocking File Write Non-Blocking File Write Parallel File Write Pin

