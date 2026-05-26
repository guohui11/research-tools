#!/usr/bin/env python3
"""
Sync research-oriented skill collections into this repository.

The script downloads curated skill repositories listed in
handsome-rich/Awesome-Auto-Research-Tools, copies them into categorized local
folders, and generates Chinese Markdown introductions plus per-skill usage docs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


GITHUB_REPO_URL = "https://github.com/guohui11/research-tools"


@dataclass(frozen=True)
class Collection:
    slug: str
    title: str
    category_slug: str
    category_title: str
    repo_url: str
    upstream: str
    description: str
    recommended_for: str
    usage_focus: str


COLLECTIONS: list[Collection] = [
    Collection(
        slug="scientific-agent-skills",
        title="scientific-agent-skills",
        category_slug="scientific-research",
        category_title="通用科学研究 Skills",
        repo_url="https://github.com/K-Dense-AI/scientific-agent-skills.git",
        upstream="K-Dense-AI/scientific-agent-skills",
        description=(
            "面向科学计算和实验研究的通用技能集合，覆盖生物信息学、药物发现、"
            "临床研究、医学影像和材料科学等方向。"
        ),
        recommended_for="需要把科研任务拆成可复用工具流程的研究生，尤其适合交叉学科和 AI for Science 项目。",
        usage_focus="把具体任务描述清楚，让 agent 选择对应技能目录中的方法、依赖和执行步骤。",
    ),
    Collection(
        slug="ai-research-skills",
        title="AI-Research-SKILLs",
        category_slug="ai-research-lifecycle",
        category_title="AI 研究全流程 Skills",
        repo_url="https://github.com/Orchestra-Research/AI-research-SKILLs.git",
        upstream="Orchestra-Research/AI-research-SKILLs",
        description=(
            "围绕 AI 研究生命周期构建的技能集合，覆盖文献综述、想法生成、"
            "实验设计、训练评估、结果分析和论文写作。"
        ),
        recommended_for="做机器学习、深度学习、LLM、Agent 或数据科学课题的研究生。",
        usage_focus="按研究阶段选择技能：先综述与选题，再实验与复现，最后分析、绘图和写作。",
    ),
    Collection(
        slug="openclaw-medical-skills",
        title="OpenClaw-Medical-Skills",
        category_slug="biomedical-research",
        category_title="生物医学研究 Skills",
        repo_url="https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills.git",
        upstream="FreedomIntelligence/OpenClaw-Medical-Skills",
        description=(
            "面向医学 AI 和生物医学研究的技能集合，覆盖临床报告、基因组学、"
            "药物发现、生物信息学、结构生物学和医学数据库。"
        ),
        recommended_for="医学、生信、药物发现、临床 NLP、组学分析方向的研究生。",
        usage_focus="先确认数据合规和任务边界，再按疾病、数据类型或实验阶段选择技能。",
    ),
]


def parse_sources_yml(path: Path) -> list[Collection]:
    if not path.exists():
        return COLLECTIONS

    sources: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_sources = False
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.strip() == "sources:":
            in_sources = True
            continue
        if not in_sources:
            continue
        if raw_line.startswith("  - "):
            if current:
                sources.append(current)
            current = {}
            line = raw_line[4:].strip()
            if ":" in line:
                key, value = line.split(":", 1)
                current[key.strip()] = value.strip()
            continue
        if current is not None and raw_line.startswith("    ") and ":" in raw_line:
            key, value = raw_line.strip().split(":", 1)
            current[key.strip()] = value.strip()
    if current:
        sources.append(current)

    loaded: list[Collection] = []
    required = {
        "slug",
        "title",
        "category_slug",
        "category_title",
        "repo_url",
        "upstream",
        "description",
        "recommended_for",
        "usage_focus",
    }
    for index, item in enumerate(sources, start=1):
        missing = sorted(required - item.keys())
        if missing:
            raise ValueError(f"sources.yml item #{index} missing fields: {', '.join(missing)}")
        loaded.append(Collection(**{field: item[field] for field in required}))
    return loaded or COLLECTIONS


README_HEADER = """# research-tools

科研人专属 skills 和自动化研究工具。

本仓库当前聚焦研究生常用的科研 agent skills：文献调研、课题构思、实验复现、代码执行、数据分析、论文写作和同行评审辅助。

"""


def run(cmd: list[str], cwd: Path | None = None) -> None:
    printable = " ".join(cmd)
    print(f"$ {printable}")
    env = os.environ.copy()
    env.setdefault("GIT_LFS_SKIP_SMUDGE", "1")
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True, env=env)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "skill"


def ensure_inside(path: Path, root: Path) -> None:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise RuntimeError(f"Refusing to write outside {resolved_root}: {resolved_path}")


def remove_generated_path(path: Path, root: Path) -> None:
    if not path.exists():
        return
    ensure_inside(path, root)
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def copy_repo(src: Path, dest: Path, generated_root: Path) -> None:
    remove_generated_path(dest, generated_root)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if os.name == "nt":
        run_robocopy(src, dest)
        remove_lfs_pointer_files(dest)
        return

    def ignore(_: str, names: list[str]) -> set[str]:
        ignored = {".git", ".gitattributes", ".gitmodules", "__pycache__", ".pytest_cache", ".ruff_cache"}
        return {name for name in names if name in ignored}

    shutil.copytree(src, dest, ignore=ignore)
    remove_lfs_pointer_files(dest)


def remove_lfs_pointer_files(root: Path) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            if path.stat().st_size > 512:
                continue
            with path.open("rb") as handle:
                first_line = handle.readline(128)
            if first_line.startswith(b"version https://git-lfs.github.com/spec/"):
                path.unlink()
        except OSError:
            continue


def run_robocopy(src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    cmd = [
        "robocopy",
        str(src),
        str(dest),
        "/E",
        "/XD",
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        "/XF",
        ".gitattributes",
        ".gitmodules",
        "/NFL",
        "/NDL",
        "/NJH",
        "/NJS",
        "/NP",
    ]
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False)
    if result.returncode > 7:
        raise subprocess.CalledProcessError(result.returncode, cmd)


def clone_or_update(collection: Collection, cache_root: Path, shallow: bool) -> Path:
    cache_root.mkdir(parents=True, exist_ok=True)
    cache_dir = cache_root / collection.slug
    if (cache_dir / ".git").exists():
        run(["git", "-c", "core.longpaths=true", "fetch", "--depth", "1", "origin"], cwd=cache_dir)
        run(["git", "-c", "core.longpaths=true", "reset", "--hard", "origin/HEAD"], cwd=cache_dir)
    elif cache_dir.exists():
        shutil.rmtree(cache_dir)
        args = ["git", "-c", "core.longpaths=true", "clone"]
        if shallow:
            args += ["--depth", "1"]
        args += [collection.repo_url, str(cache_dir)]
        run(args)
    else:
        args = ["git", "-c", "core.longpaths=true", "clone"]
        if shallow:
            args += ["--depth", "1"]
        args += [collection.repo_url, str(cache_dir)]
        run(args)
    return cache_dir


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def compact_excerpt(text: str, limit: int = 900) -> str:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("```"):
            break
        lines.append(line)
        if sum(len(item) for item in lines) > limit:
            break
    excerpt = "\n".join(lines).strip()
    return excerpt[:limit].strip()


def discover_skill_files(repo_dir: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in repo_dir.rglob("*"):
        if not path.is_file():
            continue
        lower = path.name.lower()
        if lower in {"skill.md", "skills.md"} or lower.endswith("_skill.md"):
            candidates.append(path)
    return sorted(candidates)


def collection_by_slug(slug: str) -> Collection:
    for collection in COLLECTIONS:
        if collection.slug == slug:
            return collection
    raise KeyError(slug)


def write_skill_doc(
    skill_file: Path,
    repo_copy_dir: Path,
    docs_dir: Path,
    collection: Collection,
) -> Path:
    relative_skill = skill_file.relative_to(repo_copy_dir)
    raw = skill_file.read_text(encoding="utf-8", errors="replace")
    title = first_heading(raw, relative_skill.parent.name if relative_skill.parent.name != "." else skill_file.stem)
    excerpt = compact_excerpt(raw)
    doc_slug = slugify(str(relative_skill.with_suffix("")).replace("\\", "-").replace("/", "-"))
    doc_path = docs_dir / f"{doc_slug}.md"
    source_link = Path("skills") / collection.category_slug / collection.slug / relative_skill

    body = f"""# {title}

来源集合：{collection.title}

本地位置：`{source_link.as_posix()}`

上游仓库：[{collection.upstream}](https://github.com/{collection.upstream})

## 适合什么任务

{collection.recommended_for}

## 使用方法

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中说明你的研究目标、数据类型和预期输出。
2. 指定本地 skill 文件路径：`{source_link.as_posix()}`。
3. 让 agent 先阅读该 skill 的说明，再执行检索、代码、实验、分析或写作步骤。
4. 对涉及论文、医学、临床或实验数据的任务，要求 agent 输出引用来源、关键假设和可复现实验步骤。

## 建议提示词

```text
请读取并使用 {source_link.as_posix()} 这个 skill。
我的研究任务是：<写清楚课题、数据、目标和限制>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

## 原始 skill 摘要

{excerpt or "该 skill 文件没有可自动提取的摘要，请直接阅读本地源文件。"}

"""
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(body, encoding="utf-8")
    return doc_path


def github_tree_url(path: Path) -> str:
    return f"{GITHUB_REPO_URL}/tree/main/{path.as_posix()}"


def svn_export_url(path: Path) -> str:
    return f"{GITHUB_REPO_URL}/trunk/{path.as_posix()}"


def skill_download_path(collection: Collection, relative_skill: Path) -> Path:
    root = Path("skills") / collection.category_slug / collection.slug
    if relative_skill.parent == Path("."):
        return root / relative_skill
    return root / relative_skill.parent


def write_skill_tutorial(
    skill_file: Path,
    repo_copy_dir: Path,
    tutorial_dir: Path,
    collection: Collection,
) -> Path:
    relative_skill = skill_file.relative_to(repo_copy_dir)
    raw = skill_file.read_text(encoding="utf-8", errors="replace")
    title = first_heading(raw, relative_skill.parent.name if relative_skill.parent.name != "." else skill_file.stem)
    excerpt = compact_excerpt(raw, limit=1200)
    doc_slug = slugify(str(relative_skill.with_suffix("")).replace("\\", "-").replace("/", "-"))
    doc_path = tutorial_dir / collection.category_slug / collection.slug / f"{doc_slug}.md"
    skill_file_path = Path("skills") / collection.category_slug / collection.slug / relative_skill
    download_path = skill_download_path(collection, relative_skill)
    export_url = svn_export_url(download_path)
    tree_url = github_tree_url(download_path)

    body = f"""# {title}

## Skill 简介

- 所属分类：{collection.category_title}
- 所属集合：{collection.title}
- 上游仓库：[{collection.upstream}](https://github.com/{collection.upstream})
- 你的仓库位置：[{download_path.as_posix()}]({tree_url})
- Skill 文件：`{skill_file_path.as_posix()}`

{excerpt or "该 skill 文件没有可自动提取的摘要，请直接打开 skill 文件阅读完整说明。"}

## 下载这个 skill

只下载这个 skill 目录：

```bash
svn export {export_url}
```

如果本机没有 `svn`，可以先克隆整个仓库：

```bash
git clone {GITHUB_REPO_URL}.git
```

## 如何使用

1. 在 Codex、Claude Code、Cursor、Gemini CLI 或其他支持 skills 的 agent 中打开你的研究项目。
2. 告诉 agent 先阅读这个 skill 文件：`{skill_file_path.as_posix()}`。
3. 说明你的研究目标、输入数据、期望输出、运行环境和限制条件。
4. 要求 agent 先给计划，再执行检索、代码、实验、分析或写作步骤。
5. 对论文、医学、临床、实验数据相关任务，要求 agent 输出引用来源、关键假设和可复现步骤。

## 推荐提示词

```text
请读取并使用 {skill_file_path.as_posix()} 这个 skill。
我的研究任务是：<写清楚课题、数据、目标、约束和预期输出>。
请先给出执行计划，再开始执行；需要联网、运行代码或修改文件前先说明理由。
```

"""
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(body, encoding="utf-8")
    return doc_path


def write_tutorial_index(tutorial_root: Path, tutorial_docs: dict[str, list[Path]]) -> None:
    today = dt.date.today().isoformat()
    blocks: list[str] = []
    for collection in ACTIVE_COLLECTIONS:
        docs = tutorial_docs.get(collection.slug, [])
        rel_links = "\n".join(
            f"- [{path.stem}]({path.relative_to(tutorial_root).as_posix()})" for path in sorted(docs)
        ) or "- 未发现可生成教程的 skill。"
        blocks.append(
            f"""## {collection.category_title}

### {collection.title}

- 上游仓库：[{collection.upstream}](https://github.com/{collection.upstream})
- 你的仓库集合位置：[{collection.slug}]({github_tree_url(Path("skills") / collection.category_slug / collection.slug)})
- 教程数量：{len(docs)}

{rel_links}
"""
        )

    body = f"""# Skill 教程索引

生成时间：{today}

这些 Markdown 由 `scripts/sync_research_skills.py` 自动生成。每个 skill 教程都包含简介、使用方法、推荐提示词，以及指向 `guohui11/research-tools` 对应 skill 目录的下载命令。

{chr(10).join(blocks)}
"""
    tutorial_root.mkdir(parents=True, exist_ok=True)
    (tutorial_root / "README.md").write_text(body, encoding="utf-8")


def write_collection_doc(
    collection: Collection,
    docs_root: Path,
    skill_docs: list[Path],
) -> None:
    doc_path = docs_root / collection.category_slug / collection.slug / "README.md"
    links = "\n".join(
        f"- [{path.stem}]({path.name})" for path in sorted(skill_docs)
    ) or "- 未发现独立 `SKILL.md` 文件，请查看本地仓库内容。"
    body = f"""# {collection.title}

分类：{collection.category_title}

上游仓库：[{collection.upstream}](https://github.com/{collection.upstream})

## 简介

{collection.description}

## 研究生使用建议

{collection.recommended_for}

{collection.usage_focus}

## 本集合中的 skill 用法文档

{links}

"""
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(body, encoding="utf-8")


def write_index(repo_root: Path, generated_root: Path, docs_root: Path, counts: dict[str, int]) -> None:
    today = dt.date.today().isoformat()
    category_blocks: list[str] = []
    for collection in ACTIVE_COLLECTIONS:
        local_dir = Path("skills") / collection.category_slug / collection.slug
        docs_dir = Path("docs") / "skills" / collection.category_slug / collection.slug
        count = counts.get(collection.slug, 0)
        category_blocks.append(
            f"""## {collection.category_title}

### {collection.title}

- 上游：[{collection.upstream}](https://github.com/{collection.upstream})
- 本地内容：`{local_dir.as_posix()}`
- 使用文档：`{docs_dir.as_posix()}/README.md`
- 自动发现 skill 数量：{count}
- 简介：{collection.description}
- 适合：{collection.recommended_for}
"""
        )

    index_body = f"""# Research Skills Index

更新时间：{today}

这些内容由 `scripts/sync_research_skills.py` 生成，来源于 Awesome Auto Research 中的 Research Skills & Plugin Collections。

{chr(10).join(category_blocks)}
"""
    (repo_root / "docs").mkdir(parents=True, exist_ok=True)
    (repo_root / "docs" / "index.md").write_text(index_body, encoding="utf-8")

    readme_body = README_HEADER + f"""## 已同步分类

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
"""
    (repo_root / "README.md").write_text(readme_body, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync research skill collections.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--no-download", action="store_true", help="Only regenerate docs from existing skills directory.")
    parser.add_argument("--full-history", action="store_true", help="Clone full git history instead of shallow clones.")
    parser.add_argument(
        "--tutorial-output",
        type=Path,
        default=None,
        help="Optional directory for standalone per-skill tutorial Markdown files.",
    )
    return parser.parse_args()


ACTIVE_COLLECTIONS = COLLECTIONS


def main() -> int:
    global ACTIVE_COLLECTIONS
    args = parse_args()
    repo_root = args.repo_root.resolve()
    ACTIVE_COLLECTIONS = parse_sources_yml(repo_root / "sources.yml")
    generated_root = repo_root / "skills"
    docs_root = repo_root / "docs" / "skills"
    cache_root = repo_root / ".cache" / "research-skill-sources"
    counts: dict[str, int] = {}
    tutorial_root = args.tutorial_output.resolve() if args.tutorial_output else None
    tutorial_docs: dict[str, list[Path]] = {}

    ensure_inside(generated_root, repo_root)
    ensure_inside(docs_root, repo_root)
    generated_root.mkdir(parents=True, exist_ok=True)
    docs_root.mkdir(parents=True, exist_ok=True)
    if tutorial_root:
        tutorial_root.mkdir(parents=True, exist_ok=True)

    for collection in ACTIVE_COLLECTIONS:
        print(f"\n==> {collection.title}")
        repo_copy_dir = generated_root / collection.category_slug / collection.slug
        if not args.no_download:
            cache_dir = clone_or_update(collection, cache_root, shallow=not args.full_history)
            copy_repo(cache_dir, repo_copy_dir, generated_root)
        elif not repo_copy_dir.exists():
            print(f"Missing {repo_copy_dir}; run without --no-download first.", file=sys.stderr)
            return 2

        collection_docs_dir = docs_root / collection.category_slug / collection.slug
        remove_generated_path(collection_docs_dir, docs_root)
        collection_docs_dir.mkdir(parents=True, exist_ok=True)

        skill_files = discover_skill_files(repo_copy_dir)
        doc_paths = [
            write_skill_doc(skill_file, repo_copy_dir, collection_docs_dir, collection)
            for skill_file in skill_files
        ]
        if tutorial_root:
            tutorial_docs[collection.slug] = [
                write_skill_tutorial(skill_file, repo_copy_dir, tutorial_root, collection)
                for skill_file in skill_files
            ]
        counts[collection.slug] = len(doc_paths)
        write_collection_doc(collection, docs_root, doc_paths)
        print(f"Generated {len(doc_paths)} skill docs.")

    write_index(repo_root, generated_root, docs_root, counts)
    if tutorial_root:
        write_tutorial_index(tutorial_root, tutorial_docs)
        print(f"Generated tutorial markdown in {tutorial_root}.")
    print("\nDone. Review README.md and docs/index.md, then commit the generated files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
