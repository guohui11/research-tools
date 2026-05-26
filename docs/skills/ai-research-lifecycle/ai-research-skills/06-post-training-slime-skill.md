# slime: LLM Post-Training Framework for RL Scaling

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/06-post-training/slime/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/06-post-training/slime/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/06-post-training/slime/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: slime-rl-training
description: Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. Use when training GLM models, implementing custom data generation workflows, or needing tight Megatron-LM integration for RL scaling.
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Reinforcement Learning, Megatron-LM, SGLang, GRPO, Post-Training, GLM]
dependencies: [sglang-router>=0.2.3, ray, torch>=2.0.0, transformers>=4.40.0]
---
slime is an LLM post-training framework from Tsinghua's THUDM team, powering GLM-4.5, GLM-4.6, and GLM-4.7. It connects Megatron-LM for training with SGLang for high-throughput rollout generation.
**Choose slime when you need:**
- Megatron-LM native training with SGLang inference
- Custom data generation workflows with flexible data buffers
- Training GLM, Qwen3, DeepSeek V3, or Llama 3 models
- Research-grade framew

