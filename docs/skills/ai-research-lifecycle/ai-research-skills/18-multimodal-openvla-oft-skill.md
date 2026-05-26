# OpenVLA-OFT

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/18-multimodal/openvla-oft/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/18-multimodal/openvla-oft/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/18-multimodal/openvla-oft/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: fine-tuning-openvla-oft
description: Fine-tunes and evaluates OpenVLA-OFT and OpenVLA-OFT+ policies for robot action generation with continuous action heads, LoRA adaptation, and FiLM conditioning on LIBERO simulation and ALOHA real-world setups. Use when reproducing OpenVLA-OFT paper results, training custom VLA action heads (L1 or diffusion), deploying server-client inference for ALOHA, or debugging normalization, LoRA merge, and cross-GPU issues.
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [OpenVLA, OpenVLA-OFT, VLA, Robotics, Fine-Tuning, LIBERO, ALOHA, LoRA, FiLM, Action Chunking, Deployment, Continuous Actions]
dependencies: [torch==2.2.0, transformers>=4.40.0, peft==0.11.1, draccus==0.8.0, accelerate>=0.25.0, wandb>=0.16.0, fastapi>=0.100.0, uvicorn>=0.24.0, tensorflow==2.15.0, robosuite==1.4.0]  # Exact pins: OpenVLA-OFT paper results were validated on

