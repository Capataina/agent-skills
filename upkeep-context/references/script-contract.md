# Script Contract

## Scope / Purpose

This reference defines the role of the bundled scripts in `upkeep-context`, when they must be run, and what fallback behaviour is allowed when they genuinely cannot run.

## Current Relevance

This skill is a Pattern B skill. The scripts are not decorative helpers. They are mandatory deterministic supports for repo inventory and context linting.

## Content

### Required Script Sequence

For any run that creates, updates, repairs, or restructures `context/`:

1. Run `scripts/scan_repo.py` near the start.
2. Inspect the repository and existing `context/` using the scan output as scaffolding.
3. Write or update the context files.
4. Run `scripts/lint_context.py` before presenting the result.

For an audit-only run:

- `scan_repo.py` is still expected,
- `lint_context.py` should be run if the audit evaluates an existing `context/` structure.

### What `scan_repo.py` Is For

`scan_repo.py` should provide:

- a deterministic inventory of repository structure,
- language and top-level counts,
- current `context/` file inventory.

Use it to narrow exploration, not to replace reasoning.

#### Import / Dependency Detection

`scan_repo.py` also detects import statements across common languages (Python, JavaScript, TypeScript, Rust, Go, Java, Kotlin, C/C++, Swift) using lightweight regex patterns. It outputs source-file-to-imported-module relationships.

This is a structural hint, not an authoritative dependency graph. The scanner uses regex, not AST parsing, so it may miss dynamic imports, re-exports, or unusual patterns. It may also pick up commented-out imports or imports inside string literals. Treat the output as a starting point for understanding how files relate to each other and for identifying which modules are central to the codebase.

Use import data to inform relationship documentation in `architecture.md` and system files. Do not treat it as a complete or precise dependency map.

### What `lint_context.py` Is For

`lint_context.py` should check:

- canonical filenames and folder structure,
- required sections in `architecture.md` and `systems/*.md`,
- plan folder health (flags empty plan directories),
- suspicious naming patterns,
- likely shallow or structurally weak output via warnings.

Use it to catch consistency drift before handoff.

#### Cross-Reference Validation

`lint_context.py` checks that `architecture.md` and `systems/` are consistent with each other. It warns when architecture.md references a system file that does not exist, and when a system file exists but is not mentioned anywhere in architecture.md.

These are warnings, not errors. A system file might be intentionally undocumented in architecture.md (perhaps it is an implementation detail rather than an architectural subsystem). A reference to a missing file might indicate a planned-but-not-yet-written system doc. Use the warnings to verify that omissions are intentional rather than accidental drift.

#### Coverage Gap Detection

When given a `--root` argument (or when it can infer the repo root), `lint_context.py` checks whether significant source directories have plausible system file coverage. A source directory is "significant" if it contains 5 or more files or 3 or more subdirectories within one of the standard source roots (`src/`, `lib/`, `app/`, `pkg/`, `cmd/`, `internal/`).

Matching is loose: the directory name must appear as a substring of any system file name. A warning means "consider whether this source directory deserves its own system document," not "you must create a file." Small utility directories, vendored code, and generated output directories often do not need dedicated system files.

### Hard Rule

Do not describe either script as optional in normal operation.

The only allowed fallback is when a script genuinely cannot run because of environment constraints, absence of Python, or another concrete execution failure.

### Fallback Rules

If a required script genuinely cannot run:

- say which script failed,
- say why it failed,
- perform the equivalent reasoning manually as far as possible,
- note the missing validation in the final handoff.

Do not silently skip the script.

## Implications for the Repository

The context upkeep workflow should be:

- deterministic in inventory,
- judgment-driven in semantic boundaries,
- deterministic again in final linting.

That balance keeps the skill efficient without pretending the scripts can decide document architecture on their own.