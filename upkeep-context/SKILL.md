---
name: upkeep-context
description: "Maintains a repository-level context folder as durable implementation memory. Use when asked to create, initialise, regenerate, audit, clean up, restructure, repair, or update a project's context/ documentation by reading the repository, running the bundled repo scan and context lint scripts, and producing canonical architecture and subsystem documents grounded in current code reality. Prefers feature-adjacent or subsystem-adjacent files over milestone slices, preserves durable lessons, supports richer markdown structures such as trees, tables, matrices, and diagrams when they improve comprehension, and keeps context docs comprehensive without redundancy. Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs."
---

# Upkeep Context

Maintain a `context/` folder as the repository's working memory layer. The goal is durable, implementation-grounded memory that lets a future engineer or agent understand the repository quickly without re-deriving everything from code.

## Reference Loading

Before editing or generating any `context/` files, read the **mandatory core**. These three files apply to every invocation of this skill:

1. `references/context-principles.md` — what `context/` is for, what it must contain, and what it must never become.
2. `references/document-model.md` — the canonical file types, section templates, and how canonical ownership works.
3. `references/upkeep-decision-rules.md` — when to preserve, update, merge, split, rename, or delete files with low churn.

Then apply the following task-based rules. Read the additional file before doing the matching kind of work:

**Choosing file boundaries or restructuring the folder:**
Read `references/granularity-rules.md` before deciding how to split, merge, or scope files in `systems/`.

**Diagnosing or correcting a folder that looks broken:**
Read `references/anti-patterns.md` before declaring a structural problem and before proposing a corrective restructure.

**Running the bundled scripts (always required for non-audit runs):**
Read `references/script-contract.md` before running `scan_repo.py` or `lint_context.py`, and before deciding what to do if a script cannot run.

**Expanding architecture or system documents:**
Read `references/content-depth-standards.md` before writing or expanding `architecture.md` or any `systems/*.md` file. It defines the depth bar these documents must clear.

**Adding rich visual structure to a context document:**
Read `references/markdown-presentation-patterns.md` before adding substantial tables, diagrams, trees, or ASCII visualisations. It documents the patterns this skill uses for dense visual content.

**Creating or maintaining a plan file:**
Read `references/plan-file-guidance.md` before creating, updating, or restructuring any file in `plans/`.

**Uncertain about how a structural decision should land in practice:**
Read `references/examples.md` for worked examples of good decompositions, supportive multi-format presentation, and common corrections.

The mandatory core is always required because it carries the principles, document model, and decision rules that every operation depends on. The task-based files carry depth on specific patterns and should be read when the work calls for them — read them eagerly when in doubt rather than guessing.

## Core Identity

This skill is not a generic summariser, changelog generator, or planning assistant.

It maintains a **repository memory layer** that captures:

- current implementation reality,
- subsystem boundaries and interfaces,
- dependency and execution flows,
- active risks and partial work,
- durable lessons from prior attempts,
- project preferences, design rationale, and guiding principles as evolving notes,
- maintainable reference material whose relevance depends on current project reality,
- temporary execution plans only when explicitly requested or clearly necessary.

The standard for `context/` completeness is high: a reader working only from `context/` should be able to understand the entire project. If that is not possible after reading `context/`, the documentation is insufficient, not just imperfect. Architecture files, system files, and reference material should be written at a depth that makes immediate code rediscovery unnecessary.

It must reject:

- milestone-based or phase-based slicing,
- diary-style history,
- duplicated canonical ownership across files,
- speculative subsystem files,
- static research archives that are never revisited as the repository changes,
- cosmetic rewrites that create churn without improving understanding.

## Priority Order

When trade-offs exist, optimise in this order:

1. `context/` must match current implementation reality.
2. `context/` must be comprehensive enough that a reader working only from it can understand the project.
3. Each important topic must have one canonical home.
4. Repeated upkeep must produce low churn.
5. Writing should be thorough and clear — depth is a virtue, not a problem.
6. Formatting should improve comprehension, not become decoration.

## Supported File Model

Default to this folder model:

```text
context/
├── architecture.md
├── notes.md
├── systems/
├── plans/
├── notes/
└── references/
```

`architecture.md`, `systems/`, and `notes.md` are universally essential.

`notes/` should contain files whenever there are project preferences, design rationale, or durable lessons worth preserving. `plans/` and `references/` are canonical folders, but they should contain files only when justified. Do not create filler files just to mirror the model.

`references/` is not a museum. Research and supporting papers there may need upkeep when implementation reality changes. Update, merge, split, condense, or prune reference material only when that materially improves accuracy, canonical ownership, or long-term usability. Do not apply aggressive pruning pressure by default.

Some `references/` artefacts may follow a richer research-paper structure, including topic folders and analysis-heavy papers. Preserve that stronger structure when it still matches the topic and remains maintainable.

Do not create default files such as:

- `history.md`
- `changes.md`
- `milestone-1.md`
- `open-questions.md`
- `misc.md`

Durable historical knowledge belongs in the owning system document, a topical note file, or a reference file — not in a rolling log.

## Naming Rules

Prefer lowercase hyphenated filenames because they scan better in IDEs and keep the meaningful topic visible early.

Use:

- `architecture.md`
- `systems/analytics.md`
- `systems/debug-overlays.md`
- `systems/agent-observations.md`
- `plans/auth-migration.md`
- `notes/caching-strategy.md`
- `references/rest-vs-graphql.md`

Avoid:

- all-caps filenames such as `ARCHITECTURE.md`,
- vague filenames,
- milestone or chronology words,
- names that exist only to mirror a temporary project phase.

Prefer the shortest stable topic name that is still unambiguous in its folder and in the repository.

## Living System

`context/` is not a one-shot output. It is an evergrowing, maintained memory layer.

The coordinating personality maintains `context/` incrementally during normal sessions — creating files when new systems are added, updating owning documents when behaviour changes, and making targeted edits without invoking this skill. This skill is invoked for large passes when accumulated drift is too broad for inline edits to handle reliably.

## Operating Modes

Choose the mode that matches the user's intent and the repository state:

- `Initialise`: create an initial `context/` for a repo that does not yet have one.
- `Upkeep`: refresh an existing coherent `context/` in place with minimal churn.
- `Repair`: correct stale, inconsistent, or structurally drifting files without broad reorganisation.
- `Restructure`: merge, split, rename, or delete files when the current layout is actively misleading or duplicative.
- `Audit-only`: diagnose the state of `context/` and recommend actions without rewriting files.
- `Plan-support`: create or maintain a temporary `plans/` file only when explicitly requested or clearly necessary for active execution.

Do not choose a mode based on repository size labels such as "small" or "large." Choose it based on evidence about structure quality, overlap pressure, missing canonical homes, and user intent.

## Evidence Standard

Use the repository as primary evidence for implementation truth. Existing `context/` files are prior memory, not unquestionable truth.

Inspect enough of the repository to justify each major claim about:

- top-level structure,
- major subsystem boundaries,
- dependency direction,
- key execution or data flows,
- what appears implemented, partial, missing, or obsolete.

When a statement is inferred rather than directly observed in code or configuration, write it as an inference rather than as a verified fact.

## Script Usage

This skill is a script-backed workflow. The bundled scripts are mandatory parts of the process, not optional conveniences.

- Run `scripts/scan_repo.py` near the start of every non-auditless run to inventory repository structure, existing `context/` files, and likely subsystem roots.
- Run `scripts/lint_context.py` before presenting a completed `context/` update.
- Use the scripts as deterministic scaffolding, not as semantic decision-makers.
- If a script genuinely cannot run, follow the fallback rules in `references/script-contract.md` and say so explicitly in the final handoff.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Determine the operating mode from user intent and repository state.
2. Run `scripts/scan_repo.py` and inspect key entrypoints plus any existing `context/` files.
3. Map stable subsystem and feature boundaries from repository evidence.
4. Decide whether the current `context/` should be preserved, updated, repaired, or restructured.
5. Update or create `architecture.md`.
6. Update, create, merge, split, rename, or delete files in `systems/` as justified.
7. Update or create `notes.md` and `notes/` files — capture any design rationale, project preferences, or trial-and-error outcomes that surfaced since the last upkeep. Audit existing notes for staleness.
8. Check all active `plans/` files — tick completed checkboxes, update status, remove plans whose completion criteria are fully met. Plan files produced by analysis workflows (code health audits, refactoring sweeps) follow the same lifecycle.
9. Check `references/` for staleness — if the repository now implements something a reference says is missing, or if a comparison reflects outdated constraints, refresh or prune the reference.
10. Create or update other files in `plans/` or `references/` only when justified by their role.
11. Run `scripts/lint_context.py`.
12. Fix any hard failures and review any warnings with judgment.
13. Present the resulting tree, major decisions, and any remaining risks or caveats.

## Architecture and System Separation

`architecture.md` is the top-down structural map. It should describe the repository shape, subsystem responsibilities, dependency direction, and major execution/data flows.

`systems/*.md` files are the canonical homes for feature- or subsystem-level reality. They should capture implemented behaviour, boundaries, interfaces, active risks, partial work, likely change pressure, and durable lessons for one stable topic.

Do not let `architecture.md` duplicate all system docs. It is the map, not the territory.

`references/` files are durable supporting memory, including project-grounded research. They may discuss external findings, comparisons, or implementation lessons, but they still need upkeep when the repository changes enough to make their project-specific claims stale.

When a reference artefact clearly follows a research-paper structure with analytical sections and topic folders, upkeep should preserve its research-specific sections and analytical structure unless there is a clear reason to simplify or consolidate it.

## Composition

Output is rich, expressive, and depth-friendly — tables for dense inventories and comparisons, trees for repository structure, ASCII diagrams for flows and relationships, ASCII visualisations when information has spatial or density structure, bullets for digestible takeaways, and combined formats when one representation helps scanning and another helps reasoning. The full expressive range of markdown and ASCII is available; reach for whatever conveys the information clearest. See `references/markdown-presentation-patterns.md` for the specific patterns this skill uses for dense visual content.

Supportive duplication inside the same document is allowed when it improves comprehension — a table followed by bullets that interpret it, a diagram followed by prose that explains the failure modes. Canonical duplication across documents is not allowed: if two files both fully own the same topic, pick one canonical home and reduce the other to interface-level mention.

## Quality Checklist

Before considering the `context/` folder complete, verify:

- `architecture.md` exists and is structurally deep enough to orient a new reader.
- every important subsystem or feature has one canonical home,
- folder roles are respected: systems for implementation truth, notes for evolving project knowledge, plans for active execution, references for supporting material,
- naming is lowercase and stable rather than chronological or vague,
- the repo scan was run unless a documented fallback was genuinely necessary,
- the context lint was run unless a documented fallback was genuinely necessary,
- architecture and system docs are comprehensive enough to avoid immediate rediscovery from code,
- supportive formatting improves comprehension without replacing canonical ownership,
- existing good-enough files were preserved rather than rewritten for cosmetic reasons,
- system docs describe current reality rather than aspiration,
- durable lessons are attached to the owning subsystem rather than placed in a history log,
- `notes.md` exists and accurately indexes all files in `notes/`,
- note files are topical and current, not stale or redundant with system files,
- research references that depend on current implementation reality were refreshed when they had gone stale,
- `references/` was kept useful without aggressive or cosmetic pruning,
- active plan files have up-to-date checkbox status reflecting current progress,
- completed plans have been removed,
- material overlap between files is low.
