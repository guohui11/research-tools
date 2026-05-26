# Llama-Factory Skill

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/03-fine-tuning/llama-factory/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/03-fine-tuning/llama-factory/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/03-fine-tuning/llama-factory/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: llama-factory
description: Expert guidance for fine-tuning LLMs with LLaMA-Factory - WebUI no-code, 100+ models, 2/3/4/5/6/8-bit QLoRA, multimodal support
version: 1.0.0
author: Orchestra Research
license: MIT
tags: [Fine-Tuning, LLaMA Factory, LLM, WebUI, No-Code, QLoRA, LoRA, Multimodal, HuggingFace, Llama, Qwen, Gemma]
dependencies: [llmtuner, torch, transformers, datasets, peft, accelerate, gradio]
---
Comprehensive assistance with llama-factory development, generated from official documentation.
This skill should be triggered when:
- Working with llama-factory
- Asking about llama-factory features or APIs
- Implementing llama-factory solutions
- Debugging llama-factory code
- Learning llama-factory best practices
*Quick reference patterns will be added as you use the skill.*
This skill includes comprehensive documentation in `references/`:
- **_images.md** -  Images docume

