# Skill Selector

## 作用

根据用户的研究需求，从 `docs/skills-catalog.json` 或 `docs/skills-catalog.md` 中推荐最相关的 skill，并给出只下载这些 skill 的命令。

这个 skill 本身不需要读取完整 `skills/` 目录。优先读取轻量目录索引，减少上下文 token 和本地存储占用。

## 使用流程

1. 读取 `docs/skills-catalog.json`。
2. 提取用户需求中的任务、领域、数据类型、工具偏好和输出目标。
3. 根据 `name`、`summary`、`tags`、`category`、`collection` 做匹配。
4. 推荐 3-5 个最相关的 skill。
5. 每个推荐项必须说明推荐理由，并附上 `download_command`。

## 输出格式

```markdown
## 推荐结果

### 1. <skill title>

- 适合原因：<为什么匹配用户需求>
- 目录：`<skill_dir>`
- 下载：

```bash
<download_command>
```

- 使用建议：<下载后如何让 agent 使用>
```

## 推荐原则

- 优先推荐最小可用集合，不要让用户下载整个仓库。
- 如果需求很宽泛，先推荐目录型或综述型 skill。
- 如果需求涉及医学、临床、药物或生物数据，提醒用户注意数据合规、隐私和结果验证。
- 如果多个 skill 很相似，说明差异，避免重复下载。
- 不要臆造 catalog 中不存在的 skill。

## 示例提示词

```text
请使用 skill-selector。我的需求是：我想做 LoRA 微调，并且显存有限，希望能找到适合 QLoRA 的 skill。
请只读取 docs/skills-catalog.json，然后推荐 3-5 个 skill，并给出每个 skill 的下载命令。
```
