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
- current `context/` file inventory,
- likely subsystem roots that reduce blind traversal.

Use it to narrow exploration, not to replace reasoning.

### What `lint_context.py` Is For

`lint_context.py` should check:

- canonical filenames and folder structure,
- required sections,
- plan hygiene,
- suspicious naming patterns,
- likely shallow or structurally weak output via warnings.

Use it to catch consistency drift before handoff.

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

## Open Constraints / Follow-Up Questions

- If the linter remains too weak, strengthen it rather than downgrading its role.
- If the scanner output is too shallow for some repo shapes, expand the script output rather than telling agents to ignore it.
