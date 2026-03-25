#!/usr/bin/env python3
"""Validate basic structural expectations for research artefacts in context/references/."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


REQUIRED_HEADINGS = (
    "## Scope / Purpose",
    "## Current Project Relevance",
    "## Relationship To Existing Context",
)

REQUIRED_SIGNALS = (
    "repository",
    "research",
    "project",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a research artefact created by the project-research skill."
    )
    parser.add_argument(
        "target",
        help="Path to a file or folder inside context/references/, relative to the repository root or absolute.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root. Defaults to the current directory.",
    )
    return parser.parse_args()


def resolve_target(root: Path, target_arg: str) -> Path:
    target = Path(target_arg)
    if target.is_absolute():
        return target.resolve()
    return (root / target).resolve()


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    if not text.lstrip().startswith("# "):
        errors.append(f"{path}: missing top-level title")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{path}: missing required heading '{heading}'")

    lowered = text.lower()
    for token in REQUIRED_SIGNALS:
        if token not in lowered:
            warnings.append(f"{path}: does not visibly mention '{token}'")

    if "## Research Signal" not in text and "## Current State Vs Research-Backed Expectations" not in text:
        warnings.append(
            f"{path}: missing both '## Research Signal' and '## Current State Vs Research-Backed Expectations'"
        )

    if "## Recommended Priority Order" not in text and "## Recommendation" not in text:
        warnings.append(f"{path}: missing recommendation-oriented section")

    return errors, warnings


def validate_folder(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    overview = path / "overview.md"
    if not overview.exists():
        errors.append(f"{path}: topic folder is missing overview.md")
        return errors, warnings

    nested = sorted(
        child for child in path.iterdir() if child.is_file() and child.suffix == ".md"
    )
    if len(nested) < 2:
        warnings.append(f"{path}: topic folder has no supporting markdown files beyond overview.md")

    file_errors, file_warnings = validate_file(overview)
    errors.extend(file_errors)
    warnings.extend(file_warnings)
    return errors, warnings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    target = resolve_target(root, args.target)

    if not target.exists():
        print(f"Target does not exist: {target}", file=sys.stderr)
        return 2

    refs_root = (root / "context" / "references").resolve()
    if refs_root not in target.parents and target != refs_root:
        print(
            f"Target must live inside {refs_root}. Got: {target}",
            file=sys.stderr,
        )
        return 2

    if target.is_dir():
        errors, warnings = validate_folder(target)
    else:
        if target.suffix != ".md":
            print(f"Target file must be markdown: {target}", file=sys.stderr)
            return 2
        errors, warnings = validate_file(target)

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
