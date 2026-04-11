---
name: upkeep-learning
description: "Maintains a repository-level learning/ archive as a comprehensive educational system for mastering a project and its surrounding domain. Use when asked to create, rewrite, expand, update, audit, restructure, or preserve project learning materials, study paths, concept papers, system deep-dives, glossaries, exercises, comparisons, or curriculum navigation. Produces exhaustive, first-principles, example-rich teaching content grounded in existing learning/, context/, the root README, and targeted code inspection. Covers both current implementation reality and README-defined direction or domain territory, even when parts are not implemented yet. Not for release notes, product specs, or bug fixing."
---

# Upkeep Learning

Maintain `learning/` as the repository's educational archive.

This skill is for building and maintaining a large, rigorous, highly navigable teaching system for the project and its domain. The archive should teach thoroughly, explain relentlessly, and remove ambiguity wherever possible. It is allowed to be big. It is allowed to be long. It is allowed to be highly detailed. Do not compress major topics into short summaries when they warrant serious treatment.

## Reference Loading

Before editing or generating any `learning/` files, read the mandatory core. These five files apply to everything:

1. `references/archive-philosophy.md` — core identity and non-negotiable teaching principles
2. `references/operating-modes.md` — determine the mode that applies to this invocation
3. `references/source-model.md` — source roles across learning/, context/, README, and code
4. `references/learning-architecture.md` — stable top-level structure and archive organisation
5. `references/depth-and-writing-standards.md` — the writing bar that applies to all content in this archive

Then apply the following task-based rules. Each one is a hard requirement, not a suggestion:

**Building curriculum, paths, or any navigation file:**
Read `references/curriculum-design.md` and `references/navigation-design.md` before creating or editing any path, guide, or navigation file.

**Writing any exercise file:**
Read `references/exercise-strategy.md` before writing or editing any exercise. Do not skip this regardless of how straightforward the exercise seems.

**Planning coverage decisions across the archive:**
Read `references/coverage-and-organisation.md` before making structural coverage decisions.

**Updating an existing archive:**
Read `references/update-workflow.md` before making changes to an existing `learning/` folder.

**Using or creating files from standard templates:**
Read `references/templates.md` before producing new files that follow standard templates.

**Writing mathematical or scientific content:**
Read `references/mathematical-and-scientific-writing.md` before writing formal technical material.

**Writing or updating glossary entries:**
Read `references/glossary-standards.md` before touching `GLOSSARY.md`.

**Adding significant visual elements, diagrams, or rich formatting:**
Read `references/visual-markdown-patterns.md` before adding substantial visual structure.

**Uncertain about depth standards for a specific file type:**
Read `references/file-type-standards.md` before writing that file type.

## Core Identity

This skill is not a lightweight doc generator.

It maintains a **repository-scale educational archive** that captures:

- first-principles explanations of the project's concepts and domain,
- deep project-specific system and architecture teaching,
- foundational theory needed to understand the README vision,
- major current systems and major future-facing ideas,
- multiple guided learning paths for different learner goals,
- extensive glossary support,
- project-grounded exercises and practice routes,
- comparisons, alternatives, trade-offs, and historical transitions,
- durable learning material that remains valuable across repeated upkeep.

The archive should be:

- exhaustive,
- verbose,
- explanatory,
- narrative — explaining concepts as connected wholes, not as lists of assertions,
- elaborate,
- richly structured,
- visually expressive — using tables, ASCII diagrams, flow charts, and other markdown capabilities wherever they improve understanding,
- cross-linked,
- reader-oriented,
- unafraid of length.

The archive must reject:

- shallow topic summaries for major concepts,
- bullet-point inventories that list a topic without teaching it,
- timid under-explanation,
- generic filler prose,
- pretending current implementation is the whole learning surface,
- answer-heavy exercises that destroy practice value,
- arbitrary brevity,
- decorative structure with weak teaching content,
- narrow coverage caused by `context/` alone,
- deleting educationally useful material because it is not current runtime behaviour.

## Priority Order

When trade-offs exist, optimise in this order:

1. `learning/` must maximise pedagogical completeness.
2. `learning/` must cover both current implementation reality and README-defined project/domain territory.
3. Major topics must be explained thoroughly enough that a motivated learner is not left with obvious unresolved questions.
4. Navigation must remain explicit despite archive scale.
5. Learner progress in checklist files must be preserved across upkeep.
6. Structure should stay stable at the top level and sensible at deeper levels.
7. Repeated upkeep should avoid pointless churn, but not at the cost of weak teaching.

## Supported File Model

This skill should default to this top-level folder model:

```text
learning/
├── LEARNING_MAP.md        (archive overview, usage guide, and directory tree)
├── GLOSSARY.md
├── STUDY_GUIDE.md
├── paths/
├── concepts/
├── project/
├── exercises/
├── materials/
└── references/
```

The top-level model should remain stable unless the repository has a compelling reason to differ. `LEARNING_MAP.md` serves as both the usage guide and the structural overview of the archive — no separate `DIRECTORY_TREE.md` is required.

Deeper topic/type subfolders are conditional, but archive depth is encouraged. Create topic clusters when they improve study flow or reflect the scale of the material. Do not flatten a genuinely large domain just to keep the tree small.

Avoid nested `README.md` files inside `learning/`. Use role-specific filenames such as:

- `LEARNING_MAP.md`
- `STUDY_GUIDE.md`
- `paths/PATH_INDEX.md`
- `exercises/EXERCISE_GUIDE.md`
- `exercises/EXERCISE_ORDER.md`
- `exercises/solutions/SOLUTION_INDEX.md`

## Exercises Are Code Files

Exercises in `learning/exercises/` are code files, not markdown documents.

Use `.py`, `.rs`, or whatever language fits the project. The exercise prompt, goal, tasks, hints, and expected behaviour live as a structured comment block at the top of the file. The working area for the learner starts immediately below.

This allows the learner to implement directly inside the learning folder without maintaining a separate workspace.

Solution files in `exercises/solutions/` are also code files in the same language. They match the exercise file they answer and are named identically, living under `exercises/solutions/`.

Purely conceptual exercises with no sensible code surface (design reasoning, written comparisons) may remain as `.md` files, but implementation, debugging, extension, and reconstruction exercises must be code.

## Operating Rules

### 1. Treat `learning/` as a living, maintained educational archive

This is not a one-shot generation. The archive is evergrowing and dynamic. Routine incremental edits are handled during normal sessions; this skill is invoked for large passes when accumulated change warrants it.

The skill may initialise `learning/` if it does not exist, but it should primarily think in terms of upkeep:

- update and expand existing files in place when possible,
- preserve useful prior material,
- add many new files when the archive is underspecified,
- rework navigation when the project evolves,
- keep the archive current without discarding durable lessons,
- deepen material aggressively when prior coverage is thin.

### 2. Cover the full learning surface, not just current code reality

The archive must teach:

- what exists now,
- what the project is trying to become,
- the theory required to understand both,
- the trade-offs and alternatives around that journey.

If the root `README` makes an area central, that area belongs in `learning/` even when it is not yet implemented in code or fully represented in `context/`.

### 3. Navigation is a first-class artefact

`learning/` must always be traversable through multiple entry points:

- `LEARNING_MAP.md` for overall usage guidance and archive structure,
- `STUDY_GUIDE.md` for high-level route selection,
- `paths/*.md` for focused learning paths,
- `exercises/EXERCISE_ORDER.md` for practice sequencing.

Do not rely on one massive curriculum file as the only path through the learning system.

### 4. Exhaustiveness matters more than restraint

There is no such thing as "too much learning" in this skill.

Do not hold back out of fear that the archive is becoming too large, too descriptive, too explanatory, or too detailed. If a major topic deserves more teaching, write more teaching.

Do not target arbitrary file counts, but do target exhaustive coverage across the major learning surfaces:

- foundations required to understand the project,
- core domain concepts,
- reusable domain patterns,
- project systems and architecture,
- important decisions, trade-offs, and alternatives,
- current, planned, and superseded approaches when the contrast is educationally valuable,
- project-specific implementation exercises where reconstruction or debugging would deepen mastery.

More coverage is better when it remains relevant, well-organised, and genuinely educational.

### 5. Keep top-level structure stable and deeper structure conditional

Use the stable top-level tree above.

Below that, create deeper topic folders whenever they materially improve scanability, progression, or topic separation. Small folders are acceptable if they mark a meaningful boundary in a large educational archive.

### 6. Preserve learner progress

Checklist files are part of the learning system's state and must be preserved across upkeep whenever there is a clear semantic mapping.

Checkbox-heavy files usually include:

- `STUDY_GUIDE.md`
- `paths/*.md`
- `exercises/EXERCISE_ORDER.md`
- optional resource-tracking files when explicitly useful

Concept files, systems files, glossary files, and decision files should generally not contain learner checkboxes.

### 7. Preserve old, planned, and comparative material when it teaches something

When the project replaces one approach with another, do not automatically delete the old learning material.

Preserve it when it remains educationally or architecturally valuable, and make the current state clear through:

- project comparisons,
- evolution notes,
- short status sections in ambiguous files,
- roadmap-facing files for future directions that matter to understanding the project.

Do not preserve obsolete material that adds no learning value.

### 8. Use formatting as a teaching tool

Rich formatting is a teaching tool, not decoration. Tables for comparisons, ASCII diagrams for flows and structures, dependency maps, notation tables, comparison matrices, worked-example layouts — use whatever shape teaches the topic best. See `references/visual-markdown-patterns.md` for the specific patterns this skill uses for educational content.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Read the existing `learning/` folder if present.
2. Read the `context/` folder if present.
3. Read the root `README`.
4. Determine whether the task is initialise, update, extend, or audit.
5. Identify the full learning surfaces that need to exist or be revised, including README-defined future direction and prerequisite theory.
6. Expand or create navigation files before or alongside content changes.
7. Update concept, project, exercise, materials, glossary, and reference files with the depth the archive requires.
8. Inspect code selectively for verification or implementation-specific details.
9. Preserve checklist state and keep useful existing structure where possible.
10. Run the quality checklist before presenting the result.

## Quality Checklist

Before considering `learning/` complete, verify:

- The top-level `learning/` structure is clear and stable.
- `LEARNING_MAP.md` covers both archive usage guidance and structural overview.
- Navigation files exist, are internally consistent, and can support a large archive.
- Coverage is strong across foundations, core concepts, domain patterns, project systems, exercises, glossary support, and README-defined future/project-domain areas.
- Major topics are taught as connected narratives, not as bullet-point inventories of assertions.
- Major topics are explained exhaustively — a motivated learner should have no obvious unresolved questions.
- Technical topics include notation, equations, worked examples, comparisons, or diagrams wherever those improve understanding.
- Exercises are code files (for implementation tasks) with structured comment headers containing the prompt, tasks, hints, and expected behaviour.
- Solution files are code files in `exercises/solutions/` matching the exercise they answer.
- The archive reflects current implementation reality without abandoning project mission, roadmap, or prerequisite theory.
- `EXERCISE_ORDER.md` provides a meaningful recommended sequence.
- Path files provide multiple legitimate study routes rather than one rigid curriculum.
- Learner checklist state was preserved where there is a clear semantic match.
- Current, planned, historical, and superseded material are clearly labelled where ambiguity exists.
- The archive is verbose, explanatory, comprehensive, and unafraid of depth.
- Rich formatting (tables, diagrams, trees, ASCII visualisations) is used wherever it improves understanding.
