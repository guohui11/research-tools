# GPTQ (Generative Pre-trained Transformer Quantization)

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/10-optimization/gptq/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/10-optimization/gptq/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/10-optimization/gptq/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: gptq
description: Post-training 4-bit quantization for LLMs with minimal accuracy loss. Use for deploying large models (70B, 405B) on consumer GPUs, when you need 4× memory reduction with <2% perplexity degradation, or for faster inference (3-4× speedup) vs FP16. Integrates with transformers and PEFT for QLoRA fine-tuning.
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Optimization, GPTQ, Quantization, 4-Bit, Post-Training, Memory Optimization, Consumer GPUs, Fast Inference, QLoRA, Group-Wise Quantization]
dependencies: [auto-gptq, transformers, optimum, peft]
---
Post-training quantization method that compresses LLMs to 4-bit with minimal accuracy loss using group-wise quantization.
**Use GPTQ when:**
- Need to fit large models (70B+) on limited GPU memory
- Want 4× memory reduction with <2% accuracy loss
- Deploying on consumer GPUs (RTX 4090, 3090)
- Need fast

