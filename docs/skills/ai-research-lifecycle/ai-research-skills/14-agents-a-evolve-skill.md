# Evolving AI Agents with A-Evolve

来源集合：AI-Research-SKILLs

本地位置：`skills/ai-research-lifecycle/ai-research-skills/14-agents/a-evolve/SKILL.md`

上游仓库：[Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs)

## 适合什么任务

做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`skills/ai-research-lifecycle/ai-research-skills/14-agents/a-evolve/SKILL.md`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 skills/ai-research-lifecycle/ai-research-skills/14-agents/a-evolve/SKILL.md 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

---
name: evolving-ai-agents
description: Provides guidance for automatically evolving and optimizing AI agents across any domain using LLM-driven evolution algorithms. Use when building self-improving agents, optimizing agent prompts and skills against benchmarks, or implementing automated agent evaluation loops.
version: 1.0.0
author: A-EVO Lab
license: MIT
tags: [Agent Evolution, Self-Improving Agents, Prompt Optimization, LLM, Benchmark Evaluation, Skill Discovery, Agentic AI]
dependencies: [a-evolve>=0.1.0, pyyaml>=6.0]
---
A-Evolve is universal infrastructure for evolving any AI agent across any domain using any evolution algorithm with zero manual engineering. It represents all evolvable agent state as files (prompts, skills, memory, tools), runs iterative solve-observe-evolve cycles against benchmarks, and uses LLM-driven mutation to improve agent performance automatically.
**Ben

