# Navigation Design

## Table of Contents

1. [Required Navigation Surfaces](#required-navigation-surfaces)
2. [`LEARNING_MAP.md`](#learning_mapmd)
3. [`STUDY_GUIDE.md`](#study_guidemd)
4. [`PATH_INDEX.md`](#path_indexmd)
5. [Exercise Navigation](#exercise-navigation)
6. [Local Cross-Linking](#local-cross-linking)
7. [Navigation Failure Modes](#navigation-failure-modes)

Navigation must scale with archive size.

The larger the archive becomes, the more deliberate the navigation layer must be.

## Required Navigation Surfaces

The archive should usually include:

- `LEARNING_MAP.md`
- `STUDY_GUIDE.md`
- `paths/PATH_INDEX.md`
- `exercises/EXERCISE_GUIDE.md`
- `exercises/EXERCISE_ORDER.md`

For larger archives, add more local navigation where helpful rather than forcing everything through one file.

## `LEARNING_MAP.md`

This file is the single entry point for archive orientation. It combines usage guidance with structural overview — no separate `DIRECTORY_TREE.md` is required.

It should answer:

- what this archive covers,
- how it differs from `context/`,
- where to start,
- how the major folders relate,
- how status labels work,
- where progress is tracked.

It should also include a directory tree block with concise file descriptions, folder role explanations, and major-topic summaries, so a reader can understand both the purpose and the structure of the archive from one file.

## `STUDY_GUIDE.md`

This file should act as a route selector.

It should:

- offer multiple starting routes,
- explain who each route is for,
- recommend route combinations,
- suggest first files for different learner backgrounds,
- avoid pretending there is one universally correct order.

## `PATH_INDEX.md`

This file should:

- list all path files,
- explain what each path emphasises,
- indicate overlap and prerequisites,
- help the learner choose between them quickly.

## Exercise Navigation

`EXERCISE_GUIDE.md` should explain:

- exercise types,
- when to use hints,
- how to choose exercises by difficulty or goal,
- how the exercise layer supports the archive.

`EXERCISE_ORDER.md` should:

- provide a recommended sequence,
- group exercises into coherent runs,
- preserve checkboxes,
- support resuming after interruptions.

## Local Cross-Linking

Navigation is not only the top-level files.

Individual files should also guide the learner through the archive using:

- prerequisites,
- related files,
- next-step sections,
- comparison links,
- glossary references,
- exercise links,
- path references.

## Navigation Failure Modes

Treat these as failures:

- a large archive with weak route guidance,
- top-level files that do not reflect the real tree,
- paths that are difficult to distinguish from each other,
- isolated deep files with no entry points,
- important README-defined topics missing from the route system.
