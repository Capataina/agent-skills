---
name: upkeep-context
description: "Maintains a repository-level context folder as durable implementation memory. Use when asked to create, initialize, regenerate, audit, clean up, restructure, repair, or update a project's context/ documentation by reading the repository, running the bundled repo scan and context lint scripts, and producing canonical architecture and subsystem documents grounded in current code reality. Prefers feature-adjacent or subsystem-adjacent files over milestone slices, preserves durable lessons, supports richer markdown structures such as trees, tables, matrices, and diagrams when they improve comprehension, and keeps context docs comprehensive without redundancy. Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs."
---

# Upkeep Context

Maintain a `context/` folder as the repository's working memory layer. The goal is durable, implementation-grounded memory that lets a future engineer or agent understand the repository quickly without re-deriving everything from code.

Before editing or generating any `context/` files, read the reference files in this order:

1. Read `references/context-principles.md` first.
   It defines what `context/` is for, what it must contain, and what it must never become.
2. Read `references/document-model.md` second.
   It defines the canonical file types, section templates, and how canonical ownership works.
3. Read `references/granularity-rules.md` third.
   It defines how to choose file boundaries through stable ownership rather than chronology.
4. Read `references/upkeep-decision-rules.md` fourth.
   It defines when to preserve, update, merge, split, rename, or delete files with low churn.
5. Read `references/anti-patterns.md` fifth.
   It lists common failure modes that make `context/` shallow, noisy, or contradictory.
6. Read `references/script-contract.md` sixth.
   It defines the mandatory role of `scan_repo.py` and `lint_context.py`, plus fallback rules when a script genuinely cannot run.
7. Read `references/content-depth-standards.md` seventh.
   It defines what "comprehensive but non-redundant" means for architecture and system documents.
8. Read `references/markdown-presentation-patterns.md` eighth.
   It defines when to use bullets, tables, matrices, trees, and diagrams, including when supportive multi-format presentation is appropriate.
9. Read `references/implement-now-guidance.md` ninth if a plan file is present or needs to be created.
   It defines the writing standards for high-quality temporary execution plans.
10. Read `references/examples.md` last.
    It contains worked examples of good decompositions, stronger formatting patterns, and common corrections.

## Core Identity

This skill is not a generic summariser, changelog generator, or planning assistant.

It maintains a **repository memory layer** that captures:

- current implementation reality,
- subsystem boundaries and interfaces,
- dependency and execution flows,
- active risks and partial work,
- durable lessons from prior attempts,
- temporary execution plans only when explicitly requested or clearly necessary.

It must reject:

- milestone-based or phase-based slicing,
- diary-style history,
- duplicated canonical ownership across files,
- speculative subsystem files,
- cosmetic rewrites that create churn without improving understanding.

## Priority Order

When trade-offs exist, optimise in this order:

1. `context/` must match current implementation reality.
2. `context/` must materially reduce first-pass code rediscovery.
3. Each important topic must have one canonical home.
4. Repeated upkeep must produce low churn.
5. Writing should be comprehensive without padding.
6. Formatting should improve comprehension, not become decoration.

## Supported File Model

Default to this folder model:

```text
context/
├── architecture.md
├── systems/
├── plans/
├── decisions/
└── references/
```

Only `architecture.md` and `systems/` are universally essential.

`plans/`, `decisions/`, and `references/` are canonical folders, but they should contain files only when justified. Do not create filler files just to mirror the model.

Do not create default files such as:

- `history.md`
- `changes.md`
- `milestone-1.md`
- `open-questions.md`
- `notes.md`
- `misc.md`

Durable historical knowledge belongs in the owning system document or an explicit decision/reference file, not in a rolling log.

## Naming Rules

Prefer lowercase hyphenated filenames because they scan better in IDEs and keep the meaningful topic visible early.

Use:

- `architecture.md`
- `systems/analytics.md`
- `systems/debug-overlays.md`
- `systems/agent-observations.md`
- `plans/a2c.md`
- `decisions/controller-baseline.md`
- `references/a2c-vs-sac.md`

Avoid:

- all-caps filenames such as `ARCHITECTURE.md`,
- vague filenames,
- milestone or chronology words,
- names that exist only to mirror a temporary project phase.

Prefer the shortest stable topic name that is still unambiguous in its folder and in the repository.

## Operating Modes

Choose the mode that matches the user's intent and the repository state:

- `Initialize`: create an initial `context/` for a repo that does not yet have one.
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
7. Create or update files in `plans/`, `decisions/`, or `references/` only when justified by their role.
8. Run `scripts/lint_context.py`.
9. Fix any hard failures and review any warnings with judgment.
10. Present the resulting tree, major decisions, and any remaining risks or caveats.

## Architecture and System Separation

`architecture.md` is the top-down structural map. It should describe the repository shape, subsystem responsibilities, dependency direction, and major execution/data flows.

`systems/*.md` files are the canonical homes for feature- or subsystem-level reality. They should capture implemented behaviour, boundaries, interfaces, active risks, partial work, likely change pressure, and durable lessons for one stable topic.

Do not let `architecture.md` duplicate all system docs. It is the map, not the territory.

## Composition Rules

The default output should be readable by both humans and LLMs. Use the clearest representation for the information at hand:

- use bullets for concise takeaways, ownership points, and digestible lists,
- use tables for dense inventories, comparisons, or interface summaries,
- use trees for repository structure,
- use diagrams or mermaid graphs when flows or relationships are awkward in prose,
- use combined formats when one representation helps scanning and another helps reasoning.

Supportive duplication inside the same document is allowed when it improves comprehension, such as a table followed by bullets that interpret the table.

Canonical duplication across documents is not allowed. If two files both fully own the same topic, pick one canonical home and reduce the other to interface-level mention.

## Quality Checklist

Before considering the `context/` folder complete, verify:

- `architecture.md` exists and is structurally deep enough to orient a new reader.
- every important subsystem or feature has one canonical home,
- folder roles are respected: systems for implementation truth, plans for active execution, decisions for durable cross-cutting choices, references for supporting material,
- naming is lowercase and stable rather than chronological or vague,
- the repo scan was run unless a documented fallback was genuinely necessary,
- the context lint was run unless a documented fallback was genuinely necessary,
- architecture and system docs are comprehensive enough to avoid immediate rediscovery from code,
- supportive formatting improves comprehension without replacing canonical ownership,
- existing good-enough files were preserved rather than rewritten for cosmetic reasons,
- system docs describe current reality rather than aspiration,
- durable lessons are attached to the owning subsystem rather than placed in a history log,
- temporary plan files exist only when currently relevant,
- material overlap between files is low.
