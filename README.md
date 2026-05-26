# research-tools

科研人专属 skills 和自动化研究工具。

本仓库当前聚焦研究生常用的科研 agent skills：文献调研、课题构思、实验复现、代码执行、数据分析、论文写作和同行评审辅助。

## 已同步分类

- 通用科学研究 Skills：`skills/scientific-research/scientific-agent-skills`
- AI 研究全流程 Skills：`skills/ai-research-lifecycle/ai-research-skills`
- 生物医学研究 Skills：`skills/biomedical-research/openclaw-medical-skills`

## 文档入口

- 总索引：[`docs/index.md`](docs/index.md)
- 每个 skill 的使用说明：[`docs/skills/`](docs/skills/)

## 更新方法

PowerShell：

```powershell
./scripts/sync_research_skills.ps1
```

通用 Python：

```bash
python scripts/sync_research_skills.py
```

脚本会更新上游缓存、按分类复制 skill 内容，并重新生成 README、总索引和每个 skill 的使用说明。
