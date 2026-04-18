#!/usr/bin/env python3
"""Create a scaffold for a research artefact inside context/references/."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


FILE_TEMPLATE = """<!-- This scaffold is a starting point. Delete any optional section that does
     not serve the research question. See references/anti-patterns.md #6.
     The External Research Trail, Pre-Completion Obligation Audit, and What I
     Did Not Do sections are NOT optional — they encode the tool-call floor
     described in SKILL.md and must be populated before the artefact is
     presented as complete. -->

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

<!-- Evidence class values: "source-backed" (direct quoted passage from a
     primary source), "repository fact" (verified via file:line), "project
     inference" (explicitly labelled inference), "open uncertainty". -->

| Topic | Source-backed signal | Source citation (URL + quoted passage ID) | Current repository state | Citation (file:line) | Project implication | Evidence class |
|---|---|---|---|---|---|---|

## What Fits This Project Well

## What Fits This Project Badly

## Gap Analysis

## Recommended Priority Order

## Open Uncertainties And Validation Needs

## Relationship To Existing Context

## External Research Trail

<!-- Mandatory. Captures the tool-call floor defined in SKILL.md's
     "External Research Floor" section. The floor is at least 3 distinct
     WebSearch calls and at least 3 distinct WebFetch calls across at least
     2 source classes, with at least one direct quoted passage per major
     source-backed claim and at least one contrasting source. -->

### Searches run

| # | Query | Tool | Rationale | Sources surfaced |
|---|---|---|---|---|

### Sources consulted

| URL | Tool | Source class | Key passages quoted below? |
|---|---|---|---|

<!-- Source class examples: foundational paper, official documentation,
     strong reference implementation, benchmark, peer-reviewed evaluation,
     production write-up, contrasting/limiting source. -->

### Quoted passages

<!-- Verbatim passages from primary sources that support specific claims in
     this artefact. Each passage must be attributable to an entry in "Sources
     consulted" and must be cited by at least one row in Research Signal. -->

- **[Passage ID]** — source: [URL]
  > quoted text here

## Pre-Completion Obligation Audit

<!-- Mandatory. Fill every row with concrete evidence before declaring the
     artefact complete. "Evidence" means a specific count, file path, URL,
     or passage ID — not a qualitative assertion. -->

| Obligation | Status | Evidence |
|---|---|---|
| At least 3 distinct WebSearch calls with topic-specific queries |  |  |
| At least 3 distinct WebFetch calls against primary sources |  |  |
| Sources span at least 2 source classes |  |  |
| At least 1 direct quoted passage per major source-backed claim |  |  |
| At least 1 contrasting / limiting / disagreeing source consulted |  |  |
| Relevant `context/` files read before project-specific claims |  |  |
| Relevant code inspected (list file paths) |  |  |
| `scripts/init_research_artifact.py` run (stdout captured) |  |  |
| `scripts/validate_research_artifact.py` run (stdout captured) |  |  |

## What I Did Not Do

<!-- Mandatory. List anything a reader might reasonably expect the research
     to cover that was intentionally or unintentionally skipped. Be specific:
     "did not benchmark against X because Y" is useful; "limited time" is
     not. Silent incompleteness is not permitted. -->

"""


OVERVIEW_TEMPLATE = """<!-- This scaffold is a starting point. Delete any optional section that
     does not serve the folder's purpose. See references/anti-patterns.md #6.
     The External Research Trail, Pre-Completion Obligation Audit, and What I
     Did Not Do sections are NOT optional when this overview stands in for
     the primary artefact of a research pass. If sub-papers in the folder
     carry the full trail, this overview may summarise and link to them
     instead of duplicating passages. -->

# {title}

## Scope / Purpose

- Define the topic area and why it needs a folder rather than one paper.

## Contents

| Artifact | Role |
|---|---|

## Relationship Map

- Explain how the papers in this folder relate to each other.

## Relationship To Existing Context

## External Research Trail

<!-- If individual sub-papers each carry their own External Research Trail,
     summarise here and link to each. Otherwise populate fully, matching the
     structure in the single-file template. -->

### Searches run

| # | Query | Tool | Rationale | Sources surfaced |
|---|---|---|---|---|

### Sources consulted

| URL | Tool | Source class | Key passages quoted below? |
|---|---|---|---|

### Quoted passages

- **[Passage ID]** — source: [URL]
  > quoted text here

## Pre-Completion Obligation Audit

| Obligation | Status | Evidence |
|---|---|---|
| At least 3 distinct WebSearch calls (this folder or sub-papers) |  |  |
| At least 3 distinct WebFetch calls against primary sources |  |  |
| Sources span at least 2 source classes |  |  |
| At least 1 contrasting / limiting / disagreeing source consulted |  |  |
| Relevant `context/` files read before project-specific claims |  |  |
| `scripts/init_research_artifact.py` run for this folder |  |  |
| `scripts/validate_research_artifact.py` run |  |  |

## What I Did Not Do

<!-- Mandatory. Reader-facing summary of scope gaps and intentional exclusions. -->

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


def normalise_target(target_arg: str) -> Path:
    """Normalise the target argument to a path relative to context/references/.

    The script's API expects target to be relative to context/references/, but
    callers naturally pass the path they see in their editor — typically
    "context/references/foo.md". Without normalisation this double-nests into
    "context/references/context/references/foo.md". Strip the leading prefix
    if present so both shapes work.
    """
    normalised = target_arg.replace("\\", "/")
    while normalised.startswith("./"):
        normalised = normalised[2:]
    for prefix in ("context/references/",):
        if normalised.startswith(prefix):
            normalised = normalised[len(prefix):]
            break
    return Path(normalised)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    refs = ensure_references_dir(root)

    if Path(args.target).is_absolute():
        print("Target must be relative to context/references/.", file=sys.stderr)
        return 2

    target = normalise_target(args.target)

    kind = args.kind
    if kind == "auto":
        kind = "file" if target.suffix == ".md" else "folder"

    title = args.title or infer_title(target)
    destination = refs / target

    # Defensive post-check: refuse any destination that would double-nest
    # context/references/, even if a future code path slips past normalisation.
    destination_str = destination.resolve().as_posix()
    if "/context/references/context/references/" in destination_str:
        print(
            f"Refusing to create double-nested path: {destination}",
            file=sys.stderr,
        )
        return 2

    if kind == "file":
        if destination.suffix != ".md":
            destination = destination.with_suffix(".md")
        create_file(destination, title)
    else:
        create_folder(destination, title)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
