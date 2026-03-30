# Coverage And Organisation

## Table of Contents

1. [Coverage Rule](#coverage-rule)
2. [Main Learning Surfaces](#main-learning-surfaces)
3. [Exhaustiveness Rule](#exhaustiveness-rule)
4. [Organisation Rule](#organisation-rule)
5. [Folder Depth](#folder-depth)
6. [Progression Rule](#progression-rule)
7. [Anti-Redundancy Rule](#anti-redundancy-rule)

This skill should maximise educational coverage and depth aggressively.

## Coverage Rule

Do not use arbitrary quotas to decide scope.

Do not think:

- "I only need a handful of concept files."
- "This is probably enough detail."
- "The archive may be getting too big."

Instead ask:

- what must the learner understand deeply?
- what foundations must exist before the project files make sense?
- what future directions in the `README` need theory coverage now?
- what comparisons or alternatives would remove confusion?
- what project systems deserve their own deep teaching documents?
- what exercises would materially improve mastery?

## Main Learning Surfaces

Check for coverage across these surfaces:

1. foundational prerequisites,
2. core domain concepts,
3. reusable domain patterns,
4. current project architecture and systems,
5. important decisions and trade-offs,
6. future project direction and README-defined domain territory,
7. current vs planned vs superseded approaches where the contrast teaches something,
8. project-specific practice tasks,
9. glossary support and terminology,
10. curated supporting materials.

The archive does not need equal depth everywhere, but it must intentionally evaluate all of these surfaces.

## Exhaustiveness Rule

When a topic is central, cover it thoroughly.

This may mean:

- several concept files for one broad theme,
- long glossary support,
- multiple comparison documents,
- several study paths touching the same area from different directions,
- extensive project-grounded exercises.

Do not compress a large domain into one short file because it feels tidier.

## Organisation Rule

Organisation is mandatory, but under-organisation is also a failure mode in a large archive.

Use:

- stable top-level structure,
- meaningful deeper topic clustering,
- explicit navigation files,
- topic boundaries that reflect real conceptual distinctions.

### Good organisation

- makes scanning easier,
- groups related files by stable topics,
- supports progressive study,
- keeps large domains legible,
- matches the repository's actual conceptual boundaries.

### Bad organisation

- forces large domains into flat dumping grounds,
- creates deep folder chains with no real pedagogical value,
- hides major topics behind weak names,
- keeps the tree artificially small while the content becomes hard to navigate.

## Folder Depth

Use deeper topic or type folders whenever they materially improve navigation, progression, or conceptual grouping.

Small folders are acceptable if they represent a meaningful boundary in a large archive.

## Progression Rule

The archive should support multiple study routes:

- bottom-up,
- top-down,
- implementation-first,
- domain-theory-first,
- subsystem-specific,
- roadmap/future-direction,
- explanation or interview fluency where relevant.

## Anti-Redundancy Rule

Depth is good. Repetition without a teaching purpose is not.

Before creating a new file, ask:

- does this file have a distinct teaching job?
- does it isolate a genuinely large topic?
- does it serve a different learner route?
- does it cover theory, context, practice, or comparison that another file does not?

If yes, create it confidently.

If no, strengthen an existing file instead.
