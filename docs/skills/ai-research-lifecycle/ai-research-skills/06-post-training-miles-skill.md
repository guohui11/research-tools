# miles: Enterprise-Grade RL for Large-Scale Model Training

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/06-post-training/miles/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/06-post-training/miles/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/06-post-training/miles/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: miles-rl-training
description: Provides guidance for enterprise-grade RL training using miles, a production-ready fork of slime. Use when training large MoE models with FP8/INT4, needing train-inference alignment, or requiring speculative RL for maximum throughput.
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Reinforcement Learning, MoE, FP8, INT4, Enterprise, SGLang, Megatron-LM]
dependencies: [sglang-router>=0.2.3, ray, torch>=2.0.0, transformers>=4.40.0]
---
miles is a high-performance, enterprise-ready RL framework optimized for large-scale model post-training. Built as a production fork of slime, it addresses critical challenges in MoE training stability, low-precision training, and train-inference alignment.
**Choose miles when you need:**
- Training 1TB+ MoE models (DeepSeek V3, Qwen3-MoE)
- FP8 or INT4 quantization-aware training
- Bit-wise identical tr

