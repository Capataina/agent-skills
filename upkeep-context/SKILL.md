---
name: upkeep-context
description: "Maintains a repository-level context folder that reflects the current implementation state. Use when asked to create, initialize, regenerate, audit, clean up, restructure, upkeep, or update a project's context/ documentation by reading the repository and producing canonical architecture and feature/system documents. Prefers feature-adjacent or subsystem-adjacent files over milestone-based or time-sliced files, preserves durable project memory, removes overlap, merges duplicated coverage, and keeps context docs aligned with code reality rather than aspirations or changelog-style history. Not for writing product specs, roadmaps, release notes, or general-purpose prose documentation."
---

# Upkeep Context

Maintain a `context/` folder as the repository's working memory layer. The goal is a deep, concise, reality-based documentation set that lets someone understand the whole repository faster than re-deriving it from code, while keeping one canonical home per important topic.

Before editing or generating any `context/` files, read the reference files in this order:

1. Read `references/context-principles.md` first.
   It defines what `context/` is for, what it must contain, and what it must never become.
2. Read `references/document-model.md` second.
   It defines the only canonical file types this skill should create and the required section templates.
3. Read `references/granularity-rules.md` third.
   It defines how to choose document boundaries and how to avoid overlap, milestone slicing, and vague catch-all files.
4. Read `references/upkeep-decision-rules.md` fourth.
   It defines when to preserve, update, merge, split, rename, or delete files and how to keep churn low.
5. Read `references/anti-patterns.md` fifth.
   It lists failure modes that commonly corrupt `context/`.
6. Read `references/implement-now-guidance.md` sixth if an execution-plan file is present or needs to be created.
   It defines the writing standards for high-quality `implement-now` files.
7. Read `references/examples.md` last.
   It contains worked examples of good and bad decompositions.

## Core Identity

This skill is not a generic summariser, a changelog generator, or a planning assistant.

It maintains a **repository memory layer** that captures:

- current implementation reality,
- subsystem boundaries and interfaces,
- active risks and partially implemented work,
- durable lessons from prior attempts,
- temporary execution plans only when explicitly requested.

It must reject:

- milestone-based or phase-based slicing,
- diary-style history,
- duplicated ownership across files,
- cosmetic rewrites that create churn without improving understanding.

## Priority Order

When trade-offs exist, optimise in this order:

1. `context/` must match current implementation reality.
2. `context/` must be sufficient to understand the repository as a whole.
3. Each important topic must have one canonical home.
4. Repeated upkeep must produce low churn.
5. Writing should stay concise without becoming shallow.

## Supported File Model

This skill should default to this folder model:

```text
context/
├── architecture.md
├── systems/
├── plans/
├── decisions/
└── references/
```

Only `architecture.md` and `systems/` are universally essential.

`plans/`, `decisions/`, and `references/` are part of the canonical structure, but they should contain files only when justified. Do not create filler files just because the folders exist.

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

- all-caps prefixes that push the meaningful topic off-screen,
- vague filenames,
- milestone or chronology words,
- names that exist only to mirror a temporary project phase.

Prefer the shortest stable topic name that is still unambiguous in its folder and in the repository.

Examples:

- prefer `systems/agent-observations.md` over `systems/sensors-and-observations.md` when the shorter name still captures the scope clearly
- prefer `systems/environment.md` over `systems/game-environment.md` when there is only one meaningful environment subsystem
- keep the longer name only when the shorter one would collide with another real subsystem

Optimise topic names for:

- IDE scanability,
- quick recognition,
- stability over time,
- low collision risk.

For existing repositories, do not rename files purely to enforce the convention unless the current names are actively harmful or you are already making a substantial structural update. Low churn still applies.

## Operating Rules

### 1. Read the repository as evidence

Use the codebase itself as the source of truth for implementation reality. Existing `context/` files are prior memory, not unquestionable truth.

Always inspect enough of the repository to answer:

- what the top-level structure is,
- what the major subsystems are,
- how they connect,
- what appears implemented, partial, missing, or obsolete,
- whether the existing `context/` structure still fits the codebase.

### 2. Treat architecture and system documents differently

`architecture.md` is the top-down structural map. It should describe the repository shape, subsystem responsibilities, dependency direction, and major execution/data flows.

`systems/*.md` files are the canonical homes for feature- or subsystem-level reality. They should contain the implementation state, boundaries, interfaces, risks, future-relevant gaps, and durable lessons for one stable topic.

`plans/*.md` files are temporary execution guides for active work.

`decisions/*.md` files hold durable cross-cutting project decisions and their trade-offs.

`references/*.md` files hold durable supporting material such as research, external-context summaries, schema notes, or comparative studies.

Do not let `architecture.md` become a duplicate of all system documents. It is the map, not the territory.

### 3. Preserve good-enough structure

Low churn is mandatory.

If an existing file already has:

- a coherent scope,
- low material overlap,
- and reality that can be updated in place,

preserve it.

Prefer:

- in-place updates over renames,
- content moves over full rewrites,
- targeted merges or splits over folder-wide reorganisation.

Only restructure when the current layout is actively misleading, duplicative, stale, or too vague to remain stable.

### 4. Keep one canonical home per topic

Every important subsystem, feature area, or cross-cutting concern must have one primary home.

If two files both own the same topic:

- move content so one file becomes canonical, or
- merge them if they are not independently stable topics.

If a file contains multiple independently changing topics:

- split it.

### 5. Keep durable memory, not chronological memory

Preserve information that remains useful over time:

- discarded approaches,
- failed experiments,
- constraints revealed by prior work,
- future revisit guidance,
- migration notes that still affect current work.

Do not preserve:

- daily progress logs,
- time-stamped “we did X today” notes,
- stacked milestone summaries,
- narrative release history.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Read the repository structure and key entrypoints.
2. Read the existing `context/` folder if present.
3. Identify stable subsystem and feature boundaries.
4. Map existing documents to those boundaries.
5. Detect gaps, overlap, stale files, bad naming, and missing canonical homes.
6. Choose the minimum restructuring needed.
7. Update or create `architecture.md`.
8. Update, create, merge, split, rename, or delete files in `systems/` as justified.
9. Create or update files in `plans/`, `decisions/`, or `references/` only when justified by their role.
10. Run the quality checklist before presenting the result.

## Architecture Depth Rules

`architecture.md` must be deep enough to orient a new engineer or agent.

It should include:

- a repository overview,
- a structured repository tree inside a text code block,
- meaningful depth into important source/config/test/doc directories,
- one-line descriptions for significant directories and files,
- subsystem responsibilities,
- dependency direction,
- major execution or data-flow pipelines,
- brief structural reality notes where needed.

Do not stop at shallow folder names like `src/` or `app/`. Go deep enough that the structure is genuinely informative.

Use `scripts/scan_repo.py` if Python is available and the script would speed up structural inventory. The script is optional. If it is unavailable, perform the same structural analysis manually.

## Script Usage

This skill may use bundled scripts, but scripts are helpers, not decision-makers.

- `scripts/scan_repo.py` inventories repository structure, existing `context/` files, and likely subsystem roots.
- `scripts/lint_context.py` checks structure, naming, required sections, suspicious file patterns, and temporary-plan hygiene.

Rules for script usage:

- The skill must still work without scripts.
- Do not rely on scripts to decide semantic boundaries.
- Do not auto-generate prose directly from script output.
- Use script output as deterministic scaffolding for human-quality documentation decisions.

## Quality Checklist

Before considering the `context/` folder complete, verify:

- `architecture.md` exists and is structurally deep enough to orient a new reader.
- Every important subsystem or feature has one canonical home.
- Folder roles are respected: systems for implementation truth, plans for active execution, decisions for durable cross-cutting choices, references for supporting material.
- No file is named by milestone, phase, chronology, or vague miscellany.
- Existing good-enough files were preserved rather than rewritten for cosmetic reasons.
- System docs describe current reality, not aspiration.
- Durable lessons are attached to the owning subsystem rather than placed in a history log.
- Temporary plan files exist only when currently relevant.
- Material overlap between files is low.
- Reading `context/` is faster than rediscovering the same information from code.

Begin now.
