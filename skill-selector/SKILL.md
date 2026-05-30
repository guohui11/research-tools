# Skill Selector

## 作用

根据用户的研究或写作需求，从 `guohui11/research-tools` 的 skill catalog 中推荐 3-5 个最相关的 skill，并给出每个 skill 的 GitHub 地址、单独下载命令和下载后的使用建议。

默认 catalog 地址：

```text
https://raw.githubusercontent.com/guohui11/research-tools/main/docs/skills-catalog.json
```

不要让用户手动提供或粘贴 catalog。优先使用本 skill 自带的检索脚本读取默认 catalog，并只把少量候选结果带入上下文。

## 快速检索

优先运行：

```bash
python scripts/select_skills.py "<用户需求>"
```

如果当前环境没有 `python`，可以尝试：

```bash
py scripts/select_skills.py "<用户需求>"
```

脚本会：

1. 优先读取用户传入的 `--catalog`。
2. 否则自动读取本地仓库中的 `docs/skills-catalog.json`。
3. 如果本地没有 catalog，则从默认 raw URL 下载。
4. 将下载结果缓存到本机临时目录，后续查询优先复用缓存。
5. 只输出排名靠前的候选 skill，避免完整读取大 catalog。

常用参数：

```bash
python scripts/select_skills.py "<用户需求>" --limit 8
python scripts/select_skills.py "<用户需求>" --refresh
python scripts/select_skills.py "<用户需求>" --catalog path/to/skills-catalog.json
```

## 推荐流程

1. 运行 `scripts/select_skills.py`，用 `--limit 8` 到 `--limit 12` 获取候选。
2. 从候选中选出 3-5 个最小可用集合。
3. 如果多个 skill 功能相似，说明差异，避免让用户重复下载。
4. 只推荐脚本输出中真实存在的 skill，不要臆造 catalog 外的 skill。
5. 下载命令必须使用候选结果里的 `download_command`。

## 输出格式

```markdown
## 推荐结果

### 1. <skill title>

- 适合原因：<为什么匹配用户需求>
- GitHub：<github_url>
- 单独下载：
```bash
<download_command>
```
- 下载后如何使用：<告诉 agent 读取该 skill 的 SKILL.md，并结合用户任务执行>
```

## 推荐原则

- 优先推荐最小可用集合，不要让用户下载整个仓库。
- 文献综述、论文阅读、论文写作相关需求，优先考虑 `paper-spine`、literature review、paper lookup、citation、scientific writing 等相关 skill。
- 如果需求很宽泛，先推荐目录型、编排型或综述型 skill，再补充专门工具型 skill。
- 如果需求涉及医学、临床、药物或生物数据，提醒用户注意数据合规、隐私和结果验证。
- 如果多个 skill 功能相似，要说明差异：例如综述规划、论文检索、引用核查、写作润色分别解决不同阶段。
- 不要推荐 catalog 中不存在的 skill。

## 给用户的简洁说明

如果用户问为什么不用直接读取 catalog，可以说明：完整 catalog 当前包含上千条记录，直接交给模型读取会慢且占上下文；selector 脚本会先在本地完成关键词检索，只把少量候选返回给模型判断，所以更快也更稳定。
