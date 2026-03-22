#!/usr/bin/env python3
"""Validate context folder structure for the upkeep-context skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SYSTEM_SECTIONS = [
    "## Scope / Purpose",
    "## Boundaries / Ownership",
    "## Current Implemented Reality",
    "## Key Interfaces / Data Flow",
    "## Implemented Outputs / Artifacts",
    "## Known Issues / Active Risks",
    "## Partial / In Progress",
    "## Planned / Missing / Likely Changes",
    "## Durable Notes / Discarded Approaches",
    "## Obsolete / No Longer Relevant",
]

REQUIRED_ARCH_SECTIONS = [
    "## Scope / Purpose",
    "## Repository Overview",
    "## Repository Structure",
    "## Subsystem Responsibilities",
    "## Dependency Direction",
    "## Core Execution / Data Flow",
    "## Structural Notes / Current Reality",
]

REQUIRED_SYSTEM_DIR = "systems"

BAD_NAME_PATTERNS = [
    re.compile(r"milestone", re.IGNORECASE),
    re.compile(r"phase", re.IGNORECASE),
    re.compile(r"history", re.IGNORECASE),
    re.compile(r"recent[_ -]?changes", re.IGNORECASE),
    re.compile(r"misc", re.IGNORECASE),
]


def validate_sections(path: Path, required: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for section in required:
        if section not in text:
            errors.append(f"{path.name}: missing required section `{section}`")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a context folder.")
    parser.add_argument("context_dir", nargs="?", default="context", help="Path to context directory")
    args = parser.parse_args()

    context_dir = Path(args.context_dir)
    errors: list[str] = []
    warnings: list[str] = []

    if not context_dir.exists() or not context_dir.is_dir():
        errors.append(f"{context_dir} does not exist or is not a directory")
    else:
        arch = context_dir / "architecture.md"
        if not arch.exists():
            errors.append("architecture.md is missing")
        else:
            validate_sections(arch, REQUIRED_ARCH_SECTIONS, errors)

        systems_dir = context_dir / REQUIRED_SYSTEM_DIR
        if not systems_dir.exists() or not systems_dir.is_dir():
            errors.append("systems/ directory is missing")
        else:
            for path in sorted(systems_dir.glob("*.md")):
                validate_sections(path, REQUIRED_SYSTEM_SECTIONS, errors)

        plans_dir = context_dir / "plans"
        if plans_dir.exists():
            plan_files = sorted(plans_dir.glob("*.md"))
            if len(plan_files) > 1:
                warnings.append("more than one active plan file exists in plans/")

        for path in sorted(context_dir.rglob("*.md")):
            rel = path.relative_to(context_dir)
            if rel.as_posix() == "architecture.md":
                continue

            for pattern in BAD_NAME_PATTERNS:
                if pattern.search(path.name):
                    warnings.append(f"{rel.as_posix()}: suspicious filename pattern `{pattern.pattern}`")

            top = rel.parts[0]
            if top == "systems":
                continue
            if top in {"plans", "decisions", "references"}:
                continue
            warnings.append(f"{rel.as_posix()}: markdown file outside canonical context structure")

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
