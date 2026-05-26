#!/usr/bin/env python3
"""
Merge per-skill tutorial Markdown files into large Markdown documents.

Default input:
  C:\\Users\\<user>\\Desktop\\skill教程

Default outputs:
  C:\\Users\\<user>\\Desktop\\skill教程合集.md
  C:\\Users\\<user>\\Desktop\\AI研究全流程Skills教程.md
  C:\\Users\\<user>\\Desktop\\生物医学研究Skills教程.md
  C:\\Users\\<user>\\Desktop\\通用科学研究Skills教程.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Category:
    slug: str
    title: str
    output_name: str


CATEGORIES = [
    Category("ai-research-lifecycle", "AI研究全流程 Skills 教程", "AI研究全流程Skills教程.md"),
    Category("biomedical-research", "生物医学研究 Skills 教程", "生物医学研究Skills教程.md"),
    Category("scientific-research", "通用科学研究 Skills 教程", "通用科学研究Skills教程.md"),
]


def default_input_dir() -> Path:
    return Path.home() / "Desktop" / "skill教程"


def default_output_dir() -> Path:
    return Path.home() / "Desktop"


def normalize_heading_levels(text: str, offset: int = 1) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})(\s+.*)$", line)
        if match:
            level = min(6, len(match.group(1)) + offset)
            lines.append("#" * level + match.group(2))
        else:
            lines.append(line)
    return "\n".join(lines).strip()


def first_heading(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def tutorial_files(root: Path, category: Category | None = None) -> list[Path]:
    search_root = root / category.slug if category else root
    files = []
    for path in search_root.rglob("*.md"):
        if path.name.lower() == "readme.md":
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix().lower())


def build_document(title: str, root: Path, files: list[Path]) -> str:
    today = dt.date.today().isoformat()
    toc = "\n".join(
        f"- {index}. {first_heading(path.read_text(encoding='utf-8', errors='replace'), path.stem)}"
        for index, path in enumerate(files, start=1)
    )

    sections: list[str] = [
        f"# {title}",
        "",
        f"生成时间：{today}",
        "",
        f"来源文件夹：`{root}`",
        "",
        f"共合并 {len(files)} 篇 skill 教程。",
        "",
        "## 目录",
        "",
        toc or "- 没有找到 Markdown 教程文件。",
        "",
    ]

    for index, path in enumerate(files, start=1):
        raw = path.read_text(encoding="utf-8", errors="replace")
        heading = first_heading(raw, path.stem)
        relative = path.relative_to(root).as_posix()
        sections.extend(
            [
                "",
                "---",
                "",
                f"## {index}. {heading}",
                "",
                f"来源文件：`{relative}`",
                "",
                normalize_heading_levels(raw, offset=2),
                "",
            ]
        )

    return "\n".join(sections).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge skill tutorial Markdown files.")
    parser.add_argument("--input-dir", type=Path, default=default_input_dir())
    parser.add_argument("--output-dir", type=Path, default=default_output_dir())
    parser.add_argument("--skip-all", action="store_true", help="Only generate category Markdown files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not input_dir.exists():
        raise FileNotFoundError(f"Input folder not found: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    if not args.skip_all:
        all_files = tutorial_files(input_dir)
        all_output = output_dir / "skill教程合集.md"
        all_output.write_text(build_document("Skill 教程合集", input_dir, all_files), encoding="utf-8")
        print(f"Wrote {all_output} ({len(all_files)} files)")

    for category in CATEGORIES:
        files = tutorial_files(input_dir, category)
        output = output_dir / category.output_name
        output.write_text(build_document(category.title, input_dir, files), encoding="utf-8")
        print(f"Wrote {output} ({len(files)} files)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
