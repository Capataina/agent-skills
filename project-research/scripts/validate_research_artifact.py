#!/usr/bin/env python3
"""Validate structural and evidence expectations for research artefacts in context/references/.

This script is deliberately strict on transcript-verifiable things (required sections,
URL counts, quoted-passage counts, evidence-class labels) and lenient on judgment calls
(section mix, prose quality). Hard failures (errors) prevent the artefact from being
presented as complete; soft failures (warnings) are flagged for the agent to address.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse
import sys


# -------------------------------------------------------------------
# Required and recommended sections
# -------------------------------------------------------------------

REQUIRED_HEADINGS = (
    "## Scope / Purpose",
    "## Current Project Relevance",
    "## Relationship To Existing Context",
)

OVERVIEW_REQUIRED_HEADINGS = (
    "## Scope / Purpose",
    "## Relationship To Existing Context",
)

# Sections introduced by the post-2026-04-18 template. Absence is a WARNING on
# existing artefacts (backward compatibility) and an ERROR on new ones that
# claim to follow the current template. The validator cannot always tell which
# is which, so presence of any of the sections below implies the artefact
# follows the new template and then all of them are required.
NEW_TEMPLATE_SECTIONS = (
    "## External Research Trail",
    "## Pre-Completion Obligation Audit",
    "## What I Did Not Do",
)

REQUIRED_SIGNALS = (
    "repository",
    "research",
    "project",
)

# Evidence-class labels the agent must use to separate claim provenance.
# Skill's source-priority-and-evidence.md mandates these.
EVIDENCE_CLASS_LABELS = (
    "repository fact",
    "source-backed",
    "project inference",
    "open uncertainty",
)

# Vague-exhortation adverbs that should not appear as the primary depth
# descriptor in the artefact body. We warn when they show up outside
# quoted passages; the agent should be stating what the research required,
# not using "substantial" or "thorough" as a self-congratulatory adverb.
EXHORTATION_ADVERBS = (
    "substantial",
    "substantially",
    "thoroughly",
    "comprehensively",
    "extensively",
)


# -------------------------------------------------------------------
# Result accumulator
# -------------------------------------------------------------------


class Result:
    """Collect errors, warnings, and deterministic check status for the final table."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks: list[tuple[str, str, str]] = []  # (check, status, detail)

    def add_check(self, check: str, status: str, detail: str = "") -> None:
        self.checks.append((check, status, detail))

    def error(self, check: str, detail: str) -> None:
        self.errors.append(f"{check}: {detail}")
        self.add_check(check, "FAIL", detail)

    def warn(self, check: str, detail: str) -> None:
        self.warnings.append(f"{check}: {detail}")
        self.add_check(check, "WARN", detail)

    def ok(self, check: str, detail: str = "") -> None:
        self.add_check(check, "OK", detail)

    def extend(self, other: "Result") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)
        self.checks.extend(other.checks)


# -------------------------------------------------------------------
# CLI
# -------------------------------------------------------------------


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
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat new-template-section warnings as errors. Use for artefacts produced after 2026-04-18.",
    )
    return parser.parse_args()


def resolve_target(root: Path, target_arg: str) -> Path:
    target = Path(target_arg)
    if target.is_absolute():
        return target.resolve()
    return (root / target).resolve()


# -------------------------------------------------------------------
# Helpers for parsing artefact content
# -------------------------------------------------------------------


# Markdown headings that end a section: another ## or deeper at the start of a line.
HEADING_RE = re.compile(r"^##+ ", re.MULTILINE)


def extract_section(text: str, heading: str) -> str | None:
    """Return the body of the named section (excluding the heading itself), or None."""
    idx = text.find(heading)
    if idx == -1:
        return None
    # Move to the end of the heading line.
    body_start = text.find("\n", idx)
    if body_start == -1:
        return ""
    body_start += 1
    # Find the next ## heading at the same or shallower level.
    rest = text[body_start:]
    match = HEADING_RE.search(rest)
    if match is None:
        return rest
    return rest[: match.start()]


# Matches blockquoted passages (one or more consecutive lines starting with >).
BLOCKQUOTE_RE = re.compile(r"(?:^> .*(?:\n|$))+", re.MULTILINE)


def find_blockquotes(text: str) -> list[str]:
    return BLOCKQUOTE_RE.findall(text)


# Matches markdown links [text](url) and bare URLs http(s)://...
LINK_URL_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"(?<![\(\[\w])https?://[^\s)\]<>`]+")


def extract_urls(text: str) -> list[str]:
    urls: list[str] = []
    urls.extend(LINK_URL_RE.findall(text))
    urls.extend(BARE_URL_RE.findall(text))
    # De-duplicate preserving order.
    seen: set[str] = set()
    deduped: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def unique_domains(urls: list[str]) -> set[str]:
    domains: set[str] = set()
    for url in urls:
        parsed = urlparse(url)
        if parsed.netloc:
            # Strip leading www. for de-duplication.
            host = parsed.netloc.lower()
            if host.startswith("www."):
                host = host[4:]
            domains.add(host)
    return domains


def strip_blockquotes(text: str) -> str:
    """Return text with blockquote blocks removed, so adverb detection does not
    flag quoted passages from external sources."""
    return BLOCKQUOTE_RE.sub("", text)


def strip_html_comments(text: str) -> str:
    """Return text with <!-- ... --> comments removed, so validator rules do not
    flag comment-content intended as guidance within the scaffold template."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


# -------------------------------------------------------------------
# Checks
# -------------------------------------------------------------------


def check_required_sections(
    text: str,
    required: tuple[str, ...],
    path: Path,
    result: Result,
) -> None:
    for heading in required:
        if heading not in text:
            result.error(f"{path.name} required section", f"missing '{heading}'")
        else:
            result.ok(f"{path.name} required section", f"'{heading}' present")


def check_title(text: str, path: Path, result: Result) -> None:
    if not text.lstrip().startswith("# ") and not text.lstrip().startswith("<!--"):
        result.error(f"{path.name} title", "missing top-level title")
    else:
        result.ok(f"{path.name} title", "present")


def check_signals(text: str, path: Path, result: Result) -> None:
    lowered = text.lower()
    for token in REQUIRED_SIGNALS:
        if token not in lowered:
            result.warn(f"{path.name} signal", f"does not visibly mention '{token}'")
        else:
            result.ok(f"{path.name} signal", f"'{token}' present")


def check_new_template_sections(
    text: str,
    path: Path,
    result: Result,
    strict: bool,
) -> bool:
    """Return True if the artefact appears to follow the new template.

    If any of the new-template sections are present, all of them must be.
    If none are present, emit warnings (or errors under --strict) that the
    artefact has not been updated to the post-2026-04-18 template.
    """
    present = [s for s in NEW_TEMPLATE_SECTIONS if s in text]
    if not present:
        if strict:
            for heading in NEW_TEMPLATE_SECTIONS:
                result.error(
                    f"{path.name} template section",
                    f"missing '{heading}' (required by post-2026-04-18 template)",
                )
        else:
            result.warn(
                f"{path.name} template",
                "none of External Research Trail / Pre-Completion Obligation Audit / What I Did Not Do present; artefact may predate the 2026-04-18 template",
            )
        return False
    # Any present means all required.
    for heading in NEW_TEMPLATE_SECTIONS:
        if heading not in text:
            result.error(
                f"{path.name} template section",
                f"'{heading}' missing (other new-template sections are present, so this one is required)",
            )
        else:
            result.ok(f"{path.name} template section", f"'{heading}' present")
    return True


def check_external_research_trail(
    text: str,
    path: Path,
    result: Result,
) -> None:
    """Count URLs and unique domains inside the External Research Trail section."""
    section = extract_section(text, "## External Research Trail")
    if section is None:
        return  # Caller handles the missing-section case.

    urls = extract_urls(section)
    domains = unique_domains(urls)

    # URL floor: 0 is an error; < 3 unique domains is a warning.
    if not urls:
        result.error(
            f"{path.name} research trail",
            "no URLs found in External Research Trail (the tool-call floor requires ≥3 WebSearch + ≥3 WebFetch; at minimum, sources consulted must cite URLs)",
        )
    else:
        result.ok(
            f"{path.name} research trail URL count",
            f"{len(urls)} URL(s), {len(domains)} unique domain(s)",
        )
        if len(domains) < 3:
            result.warn(
                f"{path.name} research trail variety",
                f"only {len(domains)} unique source domain(s); floor is ≥3 for substantive research passes",
            )

    # Quoted-passage floor: 0 is a warning (external research without any direct
    # quote is unusual, but a limited-research artefact may legitimately lack
    # passages if it explicitly declares the floor unmet).
    quotes = find_blockquotes(section)
    if not quotes:
        result.warn(
            f"{path.name} research trail quotes",
            "no quoted passages found; the floor requires ≥1 direct quoted passage per major source-backed claim",
        )
    else:
        result.ok(f"{path.name} research trail quotes", f"{len(quotes)} quoted passage(s)")


def check_evidence_labels(text: str, path: Path, result: Result) -> None:
    """Confirm evidence-class labels appear in the artefact when the body is
    non-trivial. For very short artefacts (<60 lines of substantive content),
    absence is a warning rather than an error because the section mix may not
    yet include a Research Signal table."""
    lowered = strip_html_comments(text).lower()
    found = [label for label in EVIDENCE_CLASS_LABELS if label in lowered]
    non_comment_lines = [
        line
        for line in strip_html_comments(text).splitlines()
        if line.strip() and not line.strip().startswith("|---")
    ]
    if not found:
        # Short scaffolds legitimately lack labels.
        if len(non_comment_lines) < 60:
            result.warn(
                f"{path.name} evidence labels",
                "no evidence-class labels present (scaffold may be early-stage)",
            )
        else:
            result.error(
                f"{path.name} evidence labels",
                "no evidence-class labels found (repository fact / source-backed / project inference / open uncertainty); source-priority-and-evidence.md requires these",
            )
    else:
        result.ok(
            f"{path.name} evidence labels",
            f"{len(found)}/4 label classes present ({', '.join(found)})",
        )


def check_exhortation_adverbs(text: str, path: Path, result: Result) -> None:
    """Warn about adverbs that typically signal vague depth claims. Quoted
    passages are stripped first so genuine source quotes are not flagged."""
    body = strip_blockquotes(strip_html_comments(text)).lower()
    hits: dict[str, int] = {}
    for adverb in EXHORTATION_ADVERBS:
        # Word-boundary match, lower-case body.
        pattern = re.compile(rf"\b{re.escape(adverb)}\b")
        count = len(pattern.findall(body))
        if count:
            hits[adverb] = count
    if hits:
        detail = ", ".join(f"{k}×{v}" for k, v in hits.items())
        result.warn(
            f"{path.name} exhortation adverbs",
            f"found outside quoted passages: {detail}. Prefer operationalised language (WebSearch count, URL count, quoted passage count) over adverbs.",
        )
    else:
        result.ok(f"{path.name} exhortation adverbs", "none outside quoted passages")


def check_legacy_sections(text: str, path: Path, result: Result) -> None:
    """Maintain the original warnings about Research Signal and Recommendation sections."""
    if "## Research Signal" not in text and "## Current State Vs Research-Backed Expectations" not in text:
        result.warn(
            f"{path.name} analysis section",
            "missing both '## Research Signal' and '## Current State Vs Research-Backed Expectations'",
        )
    if "## Recommended Priority Order" not in text and "## Recommendation" not in text:
        result.warn(
            f"{path.name} recommendation", "missing recommendation-oriented section"
        )


# -------------------------------------------------------------------
# File and folder validation
# -------------------------------------------------------------------


def validate_file(
    path: Path,
    required_headings: tuple[str, ...] = REQUIRED_HEADINGS,
    strict: bool = False,
) -> Result:
    result = Result()
    text = path.read_text(encoding="utf-8")

    check_title(text, path, result)
    check_required_sections(text, required_headings, path, result)
    check_signals(text, path, result)
    follows_new_template = check_new_template_sections(text, path, result, strict)
    if follows_new_template:
        check_external_research_trail(text, path, result)
    check_evidence_labels(text, path, result)
    check_exhortation_adverbs(text, path, result)
    check_legacy_sections(text, path, result)

    return result


def validate_folder(path: Path, strict: bool = False) -> Result:
    result = Result()

    overview = path / "overview.md"
    if not overview.exists():
        result.error(f"{path.name} folder", "topic folder is missing overview.md")
        return result

    nested = sorted(
        child for child in path.iterdir() if child.is_file() and child.suffix == ".md"
    )
    if len(nested) < 2:
        result.warn(
            f"{path.name} folder",
            "topic folder has no supporting markdown files beyond overview.md",
        )

    result.extend(validate_file(overview, OVERVIEW_REQUIRED_HEADINGS, strict))
    for child in nested:
        if child.name == "overview.md":
            continue
        result.extend(validate_file(child, REQUIRED_HEADINGS, strict))

    return result


# -------------------------------------------------------------------
# Output rendering
# -------------------------------------------------------------------


def render_status_table(checks: list[tuple[str, str, str]]) -> str:
    if not checks:
        return "(no checks run)"
    # Column widths.
    name_w = max(len(c[0]) for c in checks)
    status_w = max(len(c[1]) for c in checks)
    name_w = max(name_w, len("CHECK"))
    status_w = max(status_w, len("STATUS"))

    lines = []
    lines.append(f"{'CHECK'.ljust(name_w)}  {'STATUS'.ljust(status_w)}  DETAIL")
    lines.append(f"{'-' * name_w}  {'-' * status_w}  {'-' * 40}")
    for name, status, detail in checks:
        lines.append(f"{name.ljust(name_w)}  {status.ljust(status_w)}  {detail}")
    return "\n".join(lines)


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------


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
        result = validate_folder(target, args.strict)
    else:
        if target.suffix != ".md":
            print(f"Target file must be markdown: {target}", file=sys.stderr)
            return 2
        result = validate_file(target, strict=args.strict)

    # Emit deterministic status table so the agent can cite the validator's
    # output in its Pre-Completion Obligation Audit.
    print(render_status_table(result.checks))
    print()

    for error in result.errors:
        print(f"ERROR: {error}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")

    if result.errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
