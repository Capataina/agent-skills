---
name: upkeep-learning
description: "Maintains a repository-level learning/ system that teaches a software project from first principles using the existing learning folder, the context folder, the root README, and targeted code inspection when needed. Use when asked to create, initialize, update, extend, restructure, audit, or preserve project learning materials, learning paths, concept files, systems deep-dives, exercises, glossaries, or study navigation. Prefers iterative upkeep over one-shot generation, preserves learner progress in checklist files, keeps navigation explicit, and adds project-specific exercises without arbitrary file-count quotas. Not for generic code documentation, release notes, product specs, or bug fixing."
---

# Upkeep Learning

Maintain a `learning/` folder as the repository's learning system. The goal is a deep, navigable, first-principles teaching layer that evolves with the project and remains useful across repeated upkeep.

Before editing or generating any `learning/` files, read the reference files in this order:

1. Read `references/operating-modes.md` first.
   It defines the four supported workflows: initialise, update, extend, and audit.
2. Read `references/source-priority.md` second.
   It defines which project sources to trust first and when targeted code inspection is justified.
3. Read `references/learning-architecture.md` third.
   It defines the stable top-level `learning/` structure, navigation files, learning paths, and status conventions.
4. Read `references/coverage-and-organisation.md` fourth.
   It defines coverage-based generation, conditional folder depth, and anti-redundancy rules.
5. Read `references/exercise-strategy.md` fifth.
   It defines exercise types, hint-oriented solutions, order files, and checkbox placement rules.
6. Read `references/update-workflow.md` sixth.
   It defines low-churn upkeep, learner progress preservation, and when to add, merge, split, rename, or retire files.
7. Read `references/templates.md` last.
   It contains the standard templates for navigation files, paths, concepts, systems, comparisons, exercises, and hint files.

## Core Identity

This skill is not a one-shot curriculum generator.

It maintains a **repository learning layer** that captures:

- first-principles explanations of the project's concepts,
- project-specific systems and decisions,
- reusable domain patterns,
- navigable learning paths and study guidance,
- practice material and recommended exercise order,
- durable educational lessons from current and superseded approaches.

It must reject:

- arbitrary file-count quotas,
- giant linear curriculum files as the only navigation model,
- answer-heavy exercises that defeat learning,
- full-codebase traversal by default,
- redundant or vanity folder nesting,
- historical logs that do not improve understanding.

## Priority Order

When trade-offs exist, optimise in this order:

1. `learning/` must stay aligned with the current project reality.
2. `learning/` must maximise real educational coverage without arbitrary quotas.
3. Navigation must stay explicit and easy to scan.
4. Learner progress in checklist files must be preserved across upkeep.
5. Structure should stay stable at the top level and conditional at deeper levels.
6. Repeated upkeep must produce low churn.

## Supported File Model

This skill should default to this top-level folder model:

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

The top-level model should remain stable unless the repository has a compelling reason to differ.

Deeper topic/type subfolders are **conditional**, not mandatory. Create them only when they improve navigation or match real topic boundaries. Do not introduce extra nesting only for symmetry.

Avoid nested `README.md` files inside `learning/`. Use role-specific filenames such as:

- `LEARNING_MAP.md`
- `DIRECTORY_TREE.md`
- `STUDY_GUIDE.md`
- `PATH_INDEX.md`
- `EXERCISE_GUIDE.md`
- `EXERCISE_ORDER.md`
- `SOLUTION_INDEX.md`

## Operating Rules

### 1. Treat `learning/` as a maintained system

The skill may initialise `learning/` if it does not exist, but it should primarily think in terms of upkeep:

- update existing files in place when possible,
- preserve useful prior material,
- add new files for new concepts or systems,
- rework navigation when the project evolves,
- keep the learning system current without discarding durable lessons.

### 2. Use project memory before code mining

Default source priority is:

1. existing `learning/`
2. `context/`
3. root `README`
4. targeted code inspection

Do not traverse the full codebase by default. Inspect code only when a project-specific implementation claim, file location, or systems deep-dive needs verification.

### 3. Navigation is a first-class artifact

`learning/` must always be traversable through multiple entry points:

- `LEARNING_MAP.md` for overall usage guidance,
- `DIRECTORY_TREE.md` for structure and file descriptions,
- `STUDY_GUIDE.md` for high-level route selection,
- `paths/*.md` for focused learning paths,
- `exercises/EXERCISE_ORDER.md` for practice sequencing.

Do not rely on one massive curriculum file as the only path through the learning system.

### 4. Coverage is judged by learning surfaces, not counts

Do not target a fixed number of concept files, exercises, or materials.

Instead, cover the important learning surfaces present in the repository:

- foundations required to understand the project,
- core domain concepts,
- reusable domain patterns,
- project systems and architecture,
- important decisions and trade-offs,
- current and superseded approaches when the contrast is educationally valuable,
- project-specific implementation exercises where reconstruction or debugging would deepen mastery.

More coverage is better when it remains relevant and non-redundant.

### 5. Keep top-level structure stable and deeper structure conditional

Use the stable top-level tree above.

Below that, create deeper topic folders only when they materially improve scanability. If a deeper folder would hold only one or two files and is unlikely to grow, prefer a flatter layout.

### 6. Preserve learner progress

Checklist files are part of the learning system's state and must be preserved across upkeep whenever there is a clear semantic mapping.

Checkbox-heavy files usually include:

- `STUDY_GUIDE.md`
- `paths/*.md`
- `exercises/EXERCISE_ORDER.md`
- optional resource-tracking files when explicitly useful

Concept files, systems files, glossary files, and decision files should generally not contain learner checkboxes.

### 7. Preserve old approaches when they still teach something

When the project replaces one approach with another, do not automatically delete the old learning material.

Preserve it when it remains educationally or architecturally valuable, and make the current state clear through:

- project comparisons,
- evolution notes,
- short status sections in ambiguous files.

Do not preserve obsolete material that adds no learning value.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Read the existing `learning/` folder if present.
2. Read the `context/` folder if present.
3. Read the root `README`.
4. Determine whether the task is initialise, update, extend, or audit.
5. Identify the learning surfaces that need to exist or be revised.
6. Update navigation files before or alongside content changes.
7. Update concept, project, exercise, materials, and reference files with minimal necessary churn.
8. Inspect code selectively only for verification or implementation-specific details.
9. Preserve checklist state and existing good-enough structure where possible.
10. Run the quality checklist before presenting the result.

## Quality Checklist

Before considering `learning/` complete, verify:

- The top-level `learning/` structure is clear and stable.
- Navigation files exist and are internally consistent.
- Deeper folder nesting is justified by real navigational benefit.
- Coverage is strong across foundations, core concepts, domain patterns, project systems, and exercises where warranted.
- No arbitrary numeric targets were used as the decision-maker.
- Exercises are educationally useful and do not include full solutions in the exercise file itself.
- `EXERCISE_ORDER.md` provides a meaningful recommended sequence.
- Path files provide multiple legitimate study routes rather than one rigid linear curriculum.
- Learner checklist state was preserved where there is a clear semantic match.
- Current vs superseded project approaches are clear where ambiguity exists.
- The learning system reflects current project reality without losing durable educational value.
