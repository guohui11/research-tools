#!/usr/bin/env python3
"""Select relevant research-tools skills from the public catalog."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_CATALOG_URL = (
    "https://raw.githubusercontent.com/guohui11/research-tools/main/docs/skills-catalog.json"
)

BOOST_TERMS = {
    "文献综述": ["literature", "review", "survey", "paper", "citation", "writing", "research"],
    "综述": ["literature", "review", "survey", "paper", "citation", "writing"],
    "论文": ["paper", "academic", "writing", "citation", "research"],
    "写论文": ["paper", "academic", "writing", "paper-spine", "scientific-writing"],
    "引用": ["citation", "reference", "bibliography"],
    "检索": ["lookup", "search", "literature", "paper", "research"],
    "阅读": ["reading", "paper", "research", "review"],
    "润色": ["rewrite", "humanize", "writing", "latex"],
    "latex": ["latex", "paper", "writing"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recommend skills from research-tools catalog.")
    parser.add_argument("query", nargs="+", help="User need, for example: 我想写论文文献综述")
    parser.add_argument("--catalog", type=Path, default=None, help="Local skills-catalog.json path.")
    parser.add_argument("--catalog-url", default=DEFAULT_CATALOG_URL, help="Remote catalog URL.")
    parser.add_argument("--limit", type=int, default=10, help="Number of candidates to print.")
    parser.add_argument("--refresh", action="store_true", help="Refresh cached remote catalog.")
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of Markdown.")
    return parser.parse_args()


def cache_path() -> Path:
    base = Path(os.environ.get("LOCALAPPDATA") or tempfile.gettempdir())
    return base / "research-tools-skill-selector" / "skills-catalog.json"


def find_repo_catalog(script_path: Path) -> Path | None:
    for parent in script_path.resolve().parents:
        candidate = parent / "docs" / "skills-catalog.json"
        if candidate.exists():
            return candidate
    return None


def download_catalog(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(url, headers={"User-Agent": "research-tools-skill-selector"})
    with urllib.request.urlopen(request, timeout=30) as response:
        dest.write_bytes(response.read())


def load_catalog(args: argparse.Namespace) -> tuple[list[dict[str, Any]], str]:
    if args.catalog:
        path = args.catalog
        return read_catalog(path), str(path)

    local = find_repo_catalog(Path(__file__))
    if local:
        return read_catalog(local), str(local)

    cached = cache_path()
    if args.refresh or not cached.exists():
        download_catalog(args.catalog_url, cached)
    return read_catalog(cached), str(cached)


def read_catalog(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    skills = data.get("skills") if isinstance(data, dict) else data
    if not isinstance(skills, list):
        raise ValueError(f"Catalog has no skills list: {path}")
    return [item for item in skills if isinstance(item, dict)]


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-z0-9][a-z0-9._-]*|[\u4e00-\u9fff]{2,}", text)
    expanded: list[str] = []
    for token in tokens:
        expanded.append(token)
        for zh, aliases in BOOST_TERMS.items():
            if zh in token:
                expanded.extend(aliases)
    for zh, aliases in BOOST_TERMS.items():
        if zh in text:
            expanded.extend(aliases)
    return expanded


def skill_text(skill: dict[str, Any]) -> str:
    parts = [
        str(skill.get("title", "")),
        str(skill.get("name", "")),
        str(skill.get("summary", "")),
        str(skill.get("category", "")),
        str(skill.get("collection", "")),
        str(skill.get("skill_dir", "")),
        " ".join(str(tag) for tag in skill.get("tags", []) if tag),
    ]
    return " ".join(parts)


def weighted_skill_terms(skill: dict[str, Any]) -> list[str]:
    terms: list[str] = []
    fields = [
        ("title", 5),
        ("name", 4),
        ("summary", 3),
        ("category", 2),
        ("collection", 2),
        ("skill_dir", 1),
    ]
    for field, weight in fields:
        terms.extend(tokenize(str(skill.get(field, ""))) * weight)
    terms.extend(tokenize(" ".join(str(tag) for tag in skill.get("tags", []) if tag)))
    return terms


def is_literature_review_query(query: str) -> bool:
    return any(term in query.lower() for term in ["文献", "综述", "literature", "review", "survey"])


def is_biomedical_query(query: str) -> bool:
    return any(
        term in query.lower()
        for term in ["医学", "临床", "生物", "药物", "基因", "pubmed", "medical", "clinical", "biomedical", "drug", "genomics"]
    )


def variant_priority(skill: dict[str, Any]) -> int:
    path = str(skill.get("skill_dir", "")).lower()
    if "/dist/codex/" in path or "\\dist\\codex\\" in path:
        return 0
    if "/dist/claude/" in path or "\\dist\\claude\\" in path:
        return 1
    if "/dist/openclaw/" in path or "\\dist\\openclaw\\" in path:
        return 2
    return 3


def canonical_key(skill: dict[str, Any]) -> str:
    title = re.sub(r"\s+", " ", str(skill.get("title") or skill.get("name") or "")).strip().lower()
    summary = re.sub(r"\s+", " ", str(skill.get("summary") or "")).strip().lower()
    if title and summary:
        return f"{title}|{summary}"
    return str(skill.get("id") or skill.get("skill_dir") or title)


def dedupe_variants(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best: dict[str, dict[str, Any]] = {}
    for item in results:
        key = canonical_key(item)
        current = best.get(key)
        if current is None:
            best[key] = item
            continue
        current_rank = (variant_priority(current), -float(current.get("_score", 0)))
        item_rank = (variant_priority(item), -float(item.get("_score", 0)))
        if item_rank < current_rank:
            best[key] = item
    return sorted(best.values(), key=lambda item: item["_score"], reverse=True)


def score_skills(query: str, skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    query_terms = tokenize(query)
    query_counts = Counter(query_terms)
    docs = [weighted_skill_terms(skill) for skill in skills]
    df = Counter(term for doc in docs for term in set(doc))
    total = max(len(docs), 1)
    is_lit = is_literature_review_query(query)
    is_bio = is_biomedical_query(query)
    query_lower = query.lower()

    results: list[dict[str, Any]] = []
    for skill, doc in zip(skills, docs):
        doc_counts = Counter(doc)
        score = 0.0
        matches: set[str] = set()
        for term, q_count in query_counts.items():
            freq = doc_counts.get(term, 0)
            if not freq:
                continue
            idf = math.log((1 + total) / (1 + df[term])) + 1
            score += q_count * (1 + math.log(freq)) * idf
            matches.add(term)

        text = skill_text(skill).lower()
        title = str(skill.get("title", "")).lower()
        summary = str(skill.get("summary", "")).lower()
        collection = str(skill.get("collection", "")).lower()
        if is_lit and title == "literature review":
            score += 35.0
            if collection == "scientific-agent-skills" and not is_bio:
                score += 16.0
            if collection == "openclaw-medical-skills" and not is_bio:
                score -= 12.0
        if is_lit and ("literature review" in summary or "systematic literature" in summary):
            score += 18.0
        if "paper-spine" in text and any(term in query for term in ["论文", "文献", "综述", "写作"]):
            score += 5.0
        if is_lit and title == "paperspine orchestrator":
            score += 30.0
        if "paper-spine-research" in text and is_lit:
            score += 45.0
        if "paper-spine-citation" in text and is_lit:
            score += 24.0
        if "paper-spine-rewrite" in text and is_lit:
            score += 10.0
        if "latex" in title and "latex" not in query_lower:
            score -= 120.0
        if "poster" in text and all(term not in query_lower for term in ["poster", "海报", "展板"]):
            score -= 140.0
        if "market research" in text and all(term not in query_lower for term in ["market", "市场", "行业"]):
            score -= 90.0
        if "systems paper" in text and all(term not in query_lower for term in ["system", "系统", "osdi", "sosp", "nsdi"]):
            score -= 30.0
        if "literature" in text and any(term in query for term in ["文献", "综述", "阅读"]):
            score += 4.0
        if "citation" in text and any(term in query for term in ["引用", "参考文献", "综述"]):
            score += 2.0
        if "writing" in text and any(term in query for term in ["写", "论文", "综述"]):
            score += 2.0

        if score <= 0:
            continue
        item = dict(skill)
        item["_score"] = round(score, 3)
        item["_matched_terms"] = sorted(matches)
        results.append(item)

    return dedupe_variants(sorted(results, key=lambda item: item["_score"], reverse=True))


def print_markdown(results: list[dict[str, Any]], source: str) -> None:
    print(f"Catalog source: {source}\n")
    print("## Candidate skills\n")
    for index, skill in enumerate(results, start=1):
        tags = ", ".join(str(tag) for tag in skill.get("tags", [])[:8])
        print(f"### {index}. {skill.get('title') or skill.get('name')}")
        print(f"- score: {skill.get('_score')}")
        print(f"- id: `{skill.get('id')}`")
        print(f"- collection: `{skill.get('collection')}`")
        print(f"- summary: {skill.get('summary')}")
        print(f"- tags: {tags}")
        print(f"- GitHub: {skill.get('github_url')}")
        print("- download:")
        print("```bash")
        print(skill.get("download_command"))
        print("```")
        print()


def main() -> int:
    args = parse_args()
    query = " ".join(args.query).strip()
    skills, source = load_catalog(args)
    results = score_skills(query, skills)[: max(args.limit, 1)]
    if args.json:
        print(json.dumps({"catalog_source": source, "results": results}, ensure_ascii=False, indent=2))
    else:
        print_markdown(results, source)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
