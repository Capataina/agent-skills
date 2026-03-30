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

MIN_ARCH_LINES = 25
MIN_SYSTEM_LINES = 30


def non_empty_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip()]


def validate_sections(path: Path, required: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for section in required:
        if section not in text:
            errors.append(f"{path.name}: missing required section `{section}`")


def warn_for_shallow_content(path: Path, text: str, warnings: list[str], minimum_lines: int) -> None:
    lines = non_empty_lines(text)
    if len(lines) < minimum_lines:
        warnings.append(
            f"{path.name}: document looks shallow ({len(lines)} non-empty lines; expected at least {minimum_lines} for a healthy default)"
        )

    bullet_lines = [line for line in lines if line.lstrip().startswith("- ")]
    if len(lines) >= 12 and len(bullet_lines) / max(len(lines), 1) > 0.65:
        warnings.append(
            f"{path.name}: document is heavily bullet-dominated; consider tables, trees, or diagrams where they would clarify dense information"
        )


def warn_for_reference_shape(references_dir: Path, warnings: list[str]) -> None:
    for path in sorted(references_dir.iterdir()):
        if path.is_dir():
            markdown_files = sorted(child for child in path.iterdir() if child.is_file() and child.suffix == ".md")
            nested_dirs = sorted(child for child in path.iterdir() if child.is_dir())
            if len(markdown_files) == 1 and not nested_dirs:
                warnings.append(
                    f"references/{path.name}/: folder contains only one markdown file; verify the folder shape is still justified"
                )
            if not markdown_files and not nested_dirs:
                warnings.append(f"references/{path.name}/: empty reference folder")


def is_distinct_path(a: Path, b: Path) -> bool:
    try:
        return not a.samefile(b)
    except (FileNotFoundError, OSError):
        return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a context folder.")
    parser.add_argument("context_dir", nargs="?", default="context", help="Path to context directory")
    args = parser.parse_args()

    context_dir = Path(args.context_dir)

    # Auto-detect: if the path looks like a repo root (has context/ subdir
    # but no architecture.md), use context/ inside it instead.
    candidate = context_dir / "context"
    if (
        candidate.exists()
        and candidate.is_dir()
        and not (context_dir / "architecture.md").exists()
    ):
        context_dir = candidate

    errors: list[str] = []
    warnings: list[str] = []

    if not context_dir.exists() or not context_dir.is_dir():
        errors.append(f"{context_dir} does not exist or is not a directory")
    else:
        arch = context_dir / "architecture.md"
        legacy_arch = context_dir / "ARCHITECTURE.md"
        if legacy_arch.exists() and is_distinct_path(legacy_arch, arch):
            warnings.append("ARCHITECTURE.md exists; prefer lowercase architecture.md")

        if not arch.exists():
            errors.append("architecture.md is missing")
        else:
            validate_sections(arch, REQUIRED_ARCH_SECTIONS, errors)
            arch_text = arch.read_text(encoding="utf-8")
            warn_for_shallow_content(arch, arch_text, warnings, MIN_ARCH_LINES)
            if "```text" not in arch_text:
                warnings.append("architecture.md: repository structure should normally use a fenced text tree")

        systems_dir = context_dir / REQUIRED_SYSTEM_DIR
        if not systems_dir.exists() or not systems_dir.is_dir():
            errors.append("systems/ directory is missing")
        else:
            for path in sorted(systems_dir.glob("*.md")):
                validate_sections(path, REQUIRED_SYSTEM_SECTIONS, errors)
                text = path.read_text(encoding="utf-8")
                warn_for_shallow_content(path, text, warnings, MIN_SYSTEM_LINES)

        plans_dir = context_dir / "plans"
        if plans_dir.exists():
            plan_files = sorted(plans_dir.glob("*.md"))
            if not plan_files:
                warnings.append("plans/ directory exists but contains no plan files")

        references_dir = context_dir / "references"
        if references_dir.exists() and references_dir.is_dir():
            warn_for_reference_shape(references_dir, warnings)

        # Top-level files that are part of the canonical context model.
        CANONICAL_TOP_FILES = {"architecture.md", "notes.md"}
        # Subdirectories that are part of the canonical context model.
        CANONICAL_DIRS = {"systems", "plans", "notes", "references"}

        for path in sorted(context_dir.rglob("*.md")):
            rel = path.relative_to(context_dir)
            if rel.as_posix() in CANONICAL_TOP_FILES:
                continue

            for pattern in BAD_NAME_PATTERNS:
                if pattern.search(path.name):
                    warnings.append(f"{rel.as_posix()}: suspicious filename pattern `{pattern.pattern}`")

            top = rel.parts[0]
            if top in CANONICAL_DIRS:
                continue
            warnings.append(f"{rel.as_posix()}: markdown file outside canonical context structure")

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
