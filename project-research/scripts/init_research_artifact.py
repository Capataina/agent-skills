#!/usr/bin/env python3
"""Create a scaffold for a research artefact inside context/references/."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


FILE_TEMPLATE = """<!-- This scaffold is a starting point. Delete any section that does not
     serve the research question. See references/anti-patterns.md #6. -->

# {title}

## Scope / Purpose

- Define the repository-specific research question.
- Define what this artefact covers and what it intentionally excludes.

## Current Project Relevance

- Explain why this topic matters for the repository right now.

## Current State Snapshot

- Record the verified current project state relevant to this topic.
- Distinguish verified repository facts from working inference.

## Research Signal

| Topic | Source-backed signal | Current repository state | Project implication |
|---|---|---|---|

## What Fits This Project Well

## What Fits This Project Badly

## Gap Analysis

## Recommended Priority Order

## Open Uncertainties And Validation Needs

## Relationship To Existing Context

"""


OVERVIEW_TEMPLATE = """<!-- This scaffold is a starting point. Delete any section that does not
     serve the folder's purpose. See references/anti-patterns.md #6. -->

# {title}

## Scope / Purpose

- Define the topic area and why it needs a folder rather than one paper.

## Contents

| Artifact | Role |
|---|---|

## Relationship Map

- Explain how the papers in this folder relate to each other.

## Relationship To Existing Context

"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialise a research artefact inside context/references/."
    )
    parser.add_argument(
        "target",
        help="Path to the artefact relative to context/references/, for example 'event-sourcing.md' or 'caching-strategies'.",
    )
    parser.add_argument(
        "--title",
        help="Optional display title. Defaults to a titleised version of the target name.",
    )
    parser.add_argument(
        "--kind",
        choices=("auto", "file", "folder"),
        default="auto",
        help="Whether to create a single-file paper or a topic folder scaffold.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root containing context/references/. Defaults to the current directory.",
    )
    return parser.parse_args()


def infer_title(target: Path) -> str:
    stem = target.stem if target.suffix else target.name
    return stem.replace("-", " ").replace("_", " ").title()


def ensure_references_dir(root: Path) -> Path:
    refs = root / "context" / "references"
    refs.mkdir(parents=True, exist_ok=True)
    return refs


def create_file(path: Path, title: str) -> None:
    if path.exists():
        print(f"Exists: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FILE_TEMPLATE.format(title=title), encoding="utf-8")
    print(f"Created file scaffold: {path}")


def create_folder(path: Path, title: str) -> None:
    path.mkdir(parents=True, exist_ok=True)
    overview = path / "overview.md"
    if overview.exists():
        print(f"Exists: {overview}")
    else:
        overview.write_text(OVERVIEW_TEMPLATE.format(title=title), encoding="utf-8")
        print(f"Created folder scaffold: {path}")
        print(f"Created overview scaffold: {overview}")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    refs = ensure_references_dir(root)
    target = Path(args.target)

    if target.is_absolute():
        print("Target must be relative to context/references/.", file=sys.stderr)
        return 2

    kind = args.kind
    if kind == "auto":
        kind = "file" if target.suffix == ".md" else "folder"

    title = args.title or infer_title(target)
    destination = refs / target

    if kind == "file":
        if destination.suffix != ".md":
            destination = destination.with_suffix(".md")
        create_file(destination, title)
    else:
        create_folder(destination, title)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
