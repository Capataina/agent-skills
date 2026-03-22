#!/usr/bin/env python3
"""Inventory repository structure for context upkeep.

This script is intentionally conservative. It gathers filesystem structure and
lightweight hints to support architecture writing; it does not make semantic
documentation decisions.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_IGNORES = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".DS_Store",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
    "target",
    ".venv",
    "venv",
}

SOURCE_EXTENSIONS = {
    ".rs": "rust",
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".go": "go",
    ".java": "java",
    ".kt": "kotlin",
    ".swift": "swift",
    ".c": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".h": "c-family",
    ".hpp": "cpp",
}


@dataclass
class Entry:
    path: str
    kind: str
    depth: int
    language: str | None = None


def iter_entries(root: Path, max_depth: int, ignores: set[str]) -> Iterable[Entry]:
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        parts = rel.parts
        if any(part in ignores for part in parts):
            continue
        depth = len(parts)
        if depth > max_depth:
            continue
        kind = "dir" if path.is_dir() else "file"
        language = None
        if path.is_file():
            language = SOURCE_EXTENSIONS.get(path.suffix.lower())
        yield Entry(path=str(rel), kind=kind, depth=depth, language=language)


def summarise(entries: list[Entry]) -> dict:
    languages: dict[str, int] = {}
    context_files: list[str] = []
    top_level: dict[str, int] = {}

    for entry in entries:
        top = entry.path.split("/", 1)[0]
        top_level[top] = top_level.get(top, 0) + 1
        if entry.language:
            languages[entry.language] = languages.get(entry.language, 0) + 1
        if entry.path.startswith("context/"):
            context_files.append(entry.path)

    return {
        "top_level_counts": dict(sorted(top_level.items())),
        "language_counts": dict(sorted(languages.items())),
        "context_files": sorted(context_files),
        "has_context": any(path == "context" or path.startswith("context/") for path in top_level),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scan repository structure for context upkeep.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--max-depth", type=int, default=5, help="Maximum relative depth to include")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format",
    )
    return parser


def render_text(entries: list[Entry], summary: dict) -> str:
    lines = []
    lines.append("Repository inventory")
    lines.append("")
    lines.append("Top-level counts:")
    for name, count in summary["top_level_counts"].items():
        lines.append(f"- {name}: {count}")
    lines.append("")
    lines.append("Languages:")
    for name, count in summary["language_counts"].items():
        lines.append(f"- {name}: {count}")
    lines.append("")
    lines.append("Paths:")
    for entry in entries:
        marker = "/" if entry.kind == "dir" else ""
        lines.append(f"- {entry.path}{marker}")
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    root = Path(args.root).resolve()
    entries = list(iter_entries(root, max_depth=args.max_depth, ignores=DEFAULT_IGNORES))
    summary = summarise(entries)

    if args.format == "json":
        payload = {
            "root": str(root),
            "summary": summary,
            "entries": [entry.__dict__ for entry in entries],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(render_text(entries, summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
