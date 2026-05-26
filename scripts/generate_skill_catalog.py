#!/usr/bin/env python3
"""
Generate a lightweight skill catalog for search/recommendation.

Outputs:
  docs/skills-catalog.json
  docs/skills-catalog.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


GITHUB_REPO_URL = "https://github.com/guohui11/research-tools"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "skill"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def compact_summary(text: str, frontmatter: dict[str, str], limit: int = 260) -> str:
    if frontmatter.get("description"):
        return frontmatter["description"][:limit].strip()

    lines: list[str] = []
    in_code = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line or line.startswith("#") or line == "---":
            continue
        if ":" in line and len(line.split(":", 1)[0]) < 24:
            continue
        lines.append(line)
        if sum(len(item) for item in lines) > limit:
            break
    return " ".join(lines)[:limit].strip()


def extract_tags(text: str, frontmatter: dict[str, str], path: Path) -> list[str]:
    tags: set[str] = set()
    raw_tags = frontmatter.get("tags", "")
    raw_tags = raw_tags.strip("[]")
    for tag in re.split(r"[,，]", raw_tags):
        clean = tag.strip().strip('"').strip("'")
        if clean:
            tags.add(clean)

    name_bits = re.split(r"[-_/\\\s]+", path.as_posix())
    for bit in name_bits:
        clean = bit.strip().lower()
        if len(clean) >= 3 and clean not in {"skill", "skills", "research"}:
            tags.add(clean)

    keyword_patterns = [
        "LoRA", "QLoRA", "RAG", "LLM", "MCP", "Agent", "arXiv", "PubMed",
        "genomics", "single-cell", "protein", "drug", "clinical", "LaTeX",
        "evaluation", "fine-tuning", "alignment", "visualization", "bioinformatics",
    ]
    lower_text = text.lower()
    for keyword in keyword_patterns:
        if keyword.lower() in lower_text:
            tags.add(keyword)

    return sorted(tags, key=str.lower)[:24]


def discover_skill_files(skills_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in skills_root.rglob("*"):
        if not path.is_file():
            continue
        lower = path.name.lower()
        if lower in {"skill.md", "skills.md"} or lower.endswith("_skill.md"):
            files.append(path)
    return sorted(files, key=lambda item: item.as_posix().lower())


def collection_parts(relative: Path) -> tuple[str, str, Path]:
    parts = relative.parts
    category = parts[0] if len(parts) > 0 else "unknown"
    collection = parts[1] if len(parts) > 1 else "unknown"
    skill_relative = Path(*parts[2:]) if len(parts) > 2 else relative
    return category, collection, skill_relative


def github_tree_url(path: Path) -> str:
    return f"{GITHUB_REPO_URL}/tree/main/{path.as_posix()}"


def svn_export_url(path: Path) -> str:
    return f"{GITHUB_REPO_URL}/trunk/{path.as_posix()}"


def build_catalog(repo_root: Path) -> list[dict[str, object]]:
    skills_root = repo_root / "skills"
    catalog: list[dict[str, object]] = []
    for skill_file in discover_skill_files(skills_root):
        text = read_text(skill_file)
        frontmatter = parse_frontmatter(text)
        relative = skill_file.relative_to(skills_root)
        category, collection, skill_relative = collection_parts(relative)
        skill_dir = skill_file.parent.relative_to(repo_root)
        skill_file_repo_path = skill_file.relative_to(repo_root)
        name = frontmatter.get("name") or first_heading(text, skill_file.parent.name)
        summary = compact_summary(text, frontmatter)
        tags = extract_tags(text, frontmatter, relative)
        catalog.append(
            {
                "id": slugify(f"{category}-{collection}-{skill_relative.parent.as_posix()}-{skill_file.stem}"),
                "name": name,
                "title": first_heading(text, name),
                "category": category,
                "collection": collection,
                "summary": summary,
                "tags": tags,
                "skill_file": skill_file_repo_path.as_posix(),
                "skill_dir": skill_dir.as_posix(),
                "github_url": github_tree_url(skill_dir),
                "download_command": f"svn export {svn_export_url(skill_dir)}",
            }
        )
    return catalog


def write_json(path: Path, catalog: list[dict[str, object]]) -> None:
    payload = {
        "generated_at": dt.date.today().isoformat(),
        "repository": GITHUB_REPO_URL,
        "count": len(catalog),
        "skills": catalog,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown(path: Path, catalog: list[dict[str, object]]) -> None:
    grouped: dict[str, list[dict[str, object]]] = {}
    for item in catalog:
        grouped.setdefault(str(item["category"]), []).append(item)

    lines = [
        "# Skills 能力目录索引",
        "",
        f"生成时间：{dt.date.today().isoformat()}",
        "",
        f"仓库：[{GITHUB_REPO_URL}]({GITHUB_REPO_URL})",
        "",
        f"共收录 {len(catalog)} 个 skill。这个索引用来先按需求筛选 skill，再只下载需要的目录。",
        "",
        "## 使用方式",
        "",
        "把你的需求描述给 agent，让它先读取 `docs/skills-catalog.json` 或本 Markdown，然后推荐 3-5 个最相关的 skill。推荐结果应包含原因和下载命令。",
        "",
    ]

    for category in sorted(grouped):
        items = sorted(grouped[category], key=lambda item: str(item["name"]).lower())
        lines.extend([f"## {category}", ""])
        for item in items:
            tags = ", ".join(str(tag) for tag in item["tags"])
            lines.extend(
                [
                    f"### {item['title']}",
                    "",
                    f"- 集合：`{item['collection']}`",
                    f"- 简介：{item['summary']}",
                    f"- 标签：{tags}",
                    f"- GitHub：[{item['skill_dir']}]({item['github_url']})",
                    "- 下载命令：",
                    "",
                    "```bash",
                    str(item["download_command"]),
                    "```",
                    "",
                ]
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate skill catalog.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path, default=None)
    parser.add_argument("--md-output", type=Path, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    catalog = build_catalog(repo_root)
    json_output = args.json_output or repo_root / "docs" / "skills-catalog.json"
    md_output = args.md_output or repo_root / "docs" / "skills-catalog.md"
    write_json(json_output, catalog)
    write_markdown(md_output, catalog)
    print(f"Generated {len(catalog)} skills")
    print(f"Wrote {json_output}")
    print(f"Wrote {md_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
