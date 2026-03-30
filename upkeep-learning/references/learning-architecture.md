# Learning Architecture

## Table of Contents

1. [Stable Top-Level Tree](#stable-top-level-tree)
2. [Archive-Scale Interpretation](#archive-scale-interpretation)
3. [Top-Level File Roles](#top-level-file-roles)
4. [`paths/`](#paths)
5. [`concepts/`](#concepts)
6. [`project/`](#project)
7. [`exercises/`](#exercises)
8. [`materials/`](#materials)
9. [`references/`](#references)
10. [Status Conventions](#status-conventions)
11. [Naming Rules](#naming-rules)

This file defines the preferred archive structure for `learning/`.

## Stable Top-Level Tree

Use this model by default:

```text
learning/
├── LEARNING_MAP.md
├── GLOSSARY.md
├── STUDY_GUIDE.md
├── paths/
├── concepts/
├── project/
├── exercises/
├── materials/
└── references/
```

Keep this top-level model stable unless the repository has a strong reason to differ.

## Archive-Scale Interpretation

The stable top-level tree is not a request for a small archive. It is a stable shell for a potentially very large archive underneath.

It is acceptable for:

- `concepts/` to contain many topic clusters,
- `project/` to contain deep system and architecture branches,
- `materials/` to contain rich domain-grouped reading maps,
- `references/` to hold supporting diagrams, cheat sheets, notation guides, or status conventions,
- `paths/` to contain many overlapping routes for different learner goals.

## Top-Level File Roles

### `LEARNING_MAP.md`

The archive entry point and structural overview.

It should explain:

- what `learning/` is for,
- how it differs from `context/`,
- how to navigate the archive,
- where different kinds of learners should start,
- how the paths, exercises, and glossary relate,
- how current, planned, foundational, and historical material are labelled.

It should also include a directory tree section with folder and key file descriptions, giving learners a full structural picture without opening everything.

### `GLOSSARY.md`

The global glossary.

For a large archive, this should be substantial, comprehensive, and cross-linked. It should not be a token appendix.

### `STUDY_GUIDE.md`

The high-level route selector.

It should help the learner choose among multiple routes, combinations, and starting points. It is not the only navigation layer, but it is one of the most important.

## `paths/`

Contains focused learning-path files rather than one giant curriculum file.

Expected files often include:

- `PATH_INDEX.md`
- `project-architecture-path.md`
- `implementation-first-path.md`
- `foundations-path.md`
- `domain-theory-path.md`
- `advanced-topics-path.md`
- other domain-specific or goal-specific routes the project warrants

Large archives should usually have several paths. Overlap is fine when it helps different learner intents.

## `concepts/`

The main theory and concept layer.

Preferred top-level subdivisions:

- `foundations/`
- `core/`
- `domain-patterns/`
- `advanced/`

For large projects, expect deeper topic clusters under these. Use deeper folders aggressively when they improve study flow or isolate major subject families.

## `project/`

The project-specific teaching layer.

Preferred subdivisions:

- `architecture/`
- `systems/`
- `decisions/`
- `comparisons/`
- `evolution/`

These may all be substantial in a mature archive.

`systems/` is preferred over `implementations/` when the focus is behaviour, data flow, and design rationale rather than only code anatomy.

## `exercises/`

The practice layer.

Expected anchor files:

- `EXERCISE_GUIDE.md`
- `EXERCISE_ORDER.md`
- optional hint files or `solutions/` support

Organise primarily by topic area, then add deeper type-based folders only when useful.

## `materials/`

Curated domain resources organised by topic, not by medium.

In a strong archive, materials files can themselves be substantial teaching guides rather than just bullet lists of external links.

## `references/`

Supporting files that help interpretation, orientation, or quick lookup.

Examples:

- notation guides,
- diagram collections,
- cheat sheets,
- status conventions,
- quick-reference matrices,
- supporting notes that should not interrupt the main study flow.

## Status Conventions

Use short status sections when ambiguity exists.

Examples:

- `Current for this project.`
- `Foundational domain knowledge.`
- `Planned project direction; not implemented yet.`
- `Superseded in the current implementation, but still educationally important.`

Do not force status sections into every file, but use them wherever the learner might otherwise confuse present reality with future direction or historical context.

## Naming Rules

Avoid nested `README.md` files inside `learning/`.

Prefer descriptive role-specific names:

- `LEARNING_MAP.md`
- `STUDY_GUIDE.md`
- `PATH_INDEX.md`
- `EXERCISE_GUIDE.md`
- `EXERCISE_ORDER.md`
- `SOLUTION_INDEX.md`

Use lowercase hyphenated names for topic files and subfolders.
