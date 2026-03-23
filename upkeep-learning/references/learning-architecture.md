# Learning Architecture

This file defines the preferred structure and roles inside `learning/`.

## Stable Top-Level Tree

Use this model by default:

```text
learning/
├── LEARNING_MAP.md
├── DIRECTORY_TREE.md
├── GLOSSARY.md
├── STUDY_GUIDE.md
├── paths/
├── concepts/
├── project/
├── exercises/
├── materials/
└── references/
```

This top-level model should remain stable across upkeep unless the repository has a strong reason to differ.

## Top-Level File Roles

### `LEARNING_MAP.md`

The entry point for the learning system.

It should explain:

- what `learning/` is for,
- how to use the folder,
- where different kinds of learners should start,
- how checklist tracking works,
- how the navigation files relate to one another.

### `DIRECTORY_TREE.md`

The structural index.

It should include:

- a tree view of `learning/`,
- brief descriptions for major folders,
- brief descriptions for key files,
- enough detail to make traversal easy without opening every file.

### `GLOSSARY.md`

The global glossary of technical terms used across the learning system.

### `STUDY_GUIDE.md`

The high-level route selector.

It is not a rigid linear curriculum. It should help the learner choose among multiple paths and recommend sensible combinations.

## `paths/`

Contains focused learning-path files rather than one giant master curriculum.

Expected files often include:

- `PATH_INDEX.md`
- `mathematics-path.md`
- `reinforcement-learning-path.md`
- `neuroscience-path.md`
- `systems-and-simulation-path.md`
- `project-architecture-path.md`
- `implementation-first-path.md`
- `interview-preparation-path.md`

Create only the paths the project warrants.

Path files are one of the main checklist-heavy surfaces in the learning system.

## `concepts/`

The main conceptual teaching layer.

Preferred top-level subdivisions:

- `foundations/`
- `core/`
- `domain-patterns/`
- `advanced/`

Deeper topic folders are conditional and should be created only when they materially improve scanability.

## `project/`

The project-specific learning layer.

Preferred subdivisions:

- `architecture/`
- `systems/`
- `decisions/`
- `comparisons/`
- `evolution/`

These folders may be sparse in small projects. Keep them only when they have a clear role.

`systems/` is preferred over `implementations/` because it aligns better with project memory and covers both behavior and implementation.

## `exercises/`

The practice layer.

Expected anchor files:

- `EXERCISE_GUIDE.md`
- `EXERCISE_ORDER.md`
- optional hint index files under `solutions/` if needed

The exercise tree should usually be topic-first:

- `foundations/`
- `core/`
- `domain-patterns/`
- `project/`

Create deeper type-based folders inside those only when justified by file count or complexity.

## `materials/`

Curated external resources organised by topic, not by medium.

## `references/`

Supporting files that help the learner but are not part of the main study progression.

Examples:

- diagrams,
- cheatsheets,
- status conventions,
- supporting notes.

## Status Conventions

Use short status sections only when ambiguity exists.

Examples:

- `Current for this project.`
- `Superseded in the current implementation, but still important for understanding the project's evolution.`
- `Historical background only.`

Do not force status sections into every file.

## Naming Rules

Avoid nested `README.md` files inside `learning/`.

Prefer descriptive role-specific names:

- `LEARNING_MAP.md`
- `DIRECTORY_TREE.md`
- `STUDY_GUIDE.md`
- `PATH_INDEX.md`
- `EXERCISE_GUIDE.md`
- `EXERCISE_ORDER.md`
- `SOLUTION_INDEX.md`

Use lowercase hyphenated names for topic files and subfolders.
