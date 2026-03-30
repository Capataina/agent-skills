# File Type Standards

## Table of Contents

1. [`LEARNING_MAP.md`](#learning_mapmd)
2. [`GLOSSARY.md`](#glossarymd)
3. [`STUDY_GUIDE.md`](#study_guidemd)
4. [`paths/*.md`](#pathsmd)
5. [Concept Files](#concept-files)
6. [`project/architecture/*.md`](#projectarchitecturemd)
7. [`project/systems/*.md`](#projectsystemsmd)
8. [`project/decisions/*.md`](#projectdecisionsmd)
9. [`project/comparisons/*.md`](#projectcomparisonsmd)
10. [`project/evolution/*.md`](#projectevolutionmd)
11. [`materials/*.md`](#materialsmd)
12. [`EXERCISE_GUIDE.md`](#exercise_guidemd)
13. [`EXERCISE_ORDER.md`](#exercise_ordermd)
14. [Exercise Files](#exercise-files)
15. [Reference Files In `learning/references/`](#reference-files-in-learningreferences)

This file defines the minimum depth expectations for major file classes.

Use these standards aggressively. Thin files are not acceptable for major topics.

## `LEARNING_MAP.md`

Should include:

- archive purpose,
- difference from `context/`,
- major coverage areas,
- a tree block with role descriptions for major folders,
- one-line descriptions for key files (enough detail that the learner can orient without opening everything),
- how to start,
- how routes differ,
- where progress is tracked,
- how status labels work.

## `GLOSSARY.md`

Should be comprehensive.

Entries should usually include:

- term name,
- precise definition,
- plain-language interpretation,
- concrete example,
- project-specific relevance when applicable,
- link to a deeper file.

Do not make the glossary a list of dictionary fragments.

## `STUDY_GUIDE.md`

Should include:

- route selection,
- learner-intent framing,
- recommended combinations,
- starting-point advice for different backgrounds,
- assumptions about the learner.

## `paths/*.md`

Should include:

- who the path is for,
- what it assumes,
- what it covers,
- recommended sequence,
- notes on overlaps and what to do next.

Longer path files may also include milestones or branch options.

## Concept Files

Major concept files should usually include:

- why this matters here,
- prerequisites,
- notation if useful,
- intuition,
- formal definition or mechanism,
- build-up or decomposition,
- worked examples,
- project connection,
- trade-offs or alternatives,
- misconceptions,
- related files.

For mathematical or scientific topics, see `mathematical-and-scientific-writing.md`.

## `project/architecture/*.md`

Should usually include:

- system or runtime role,
- major boundaries,
- data flow,
- subsystem interactions,
- why the architecture looks this way,
- limitations or future tension points,
- related systems and paths.

Use diagrams, tables, or dependency maps when useful.

## `project/systems/*.md`

Should usually include:

- what the system does,
- where it fits,
- inputs and outputs,
- key mechanics,
- important calculations or behaviours,
- trade-offs,
- debugging or observability notes when relevant,
- learning links,
- status if ambiguity exists.

Thin “this system exists and does X” files are not enough for important systems.

## `project/decisions/*.md`

Should usually include:

- decision summary,
- alternatives considered,
- why the chosen path won,
- trade-offs accepted,
- downstream consequences,
- links to related concept and system files.

## `project/comparisons/*.md`

Should usually include:

- why the comparison matters,
- what stayed the same,
- what changed,
- why the current or preferred approach was chosen,
- what the learner should take away,
- when the older or alternative approach is still useful to understand.

## `project/evolution/*.md`

Should usually include:

- current state,
- missing pieces,
- roadmap tension points,
- what changed over time,
- what still needs to be learned or built.

## `materials/*.md`

Materials files live in `learning/materials/` and curate external or supplementary resources that support the archive's teaching but are not concept files or exercises themselves.

### What belongs in materials

- supplementary PDFs, papers, or book chapter references,
- images, diagrams, or visual aids not generated inline,
- data files or sample datasets used by exercises or concept explanations,
- external tool documentation or API references,
- configuration samples or environment setup files,
- video or course links with context on what they cover.

### Naming conventions

Use descriptive, topic-scoped names: `distributed-systems-resources.md`, `linear-algebra-foundations.md`, `project-setup-references.md`. Do not use generic names like `links.md` or `resources.md`. Group by learning area, not by resource type.

### Organisation within `learning/materials/`

Keep materials files flat unless the archive has enough resources to warrant topic subfolders (e.g. `materials/mathematics/`, `materials/domain/`). Each file should cover one coherent topic area. If a materials file grows past 200 lines, consider splitting by sub-topic.

### When to use materials vs inline content

Use a materials file when:

- the resource is external and needs context, sequencing guidance, or commentary,
- multiple archive files would otherwise repeat the same resource links,
- the resource is supplementary (useful but not essential to the core explanation),
- the content is a static asset (PDF, dataset, config sample) rather than authored teaching.

Keep content inline in concept or system files when it is integral to the explanation and would lose context if separated.

### Content expectations

Each materials file should usually include:

- what the topic area is,
- why it matters to this repository,
- how to use the resource list,
- suggested sequencing,
- what each resource is good for,
- what archive files to read before or after.

Do not reduce materials files to bare link dumps when they could guide study productively.

## `EXERCISE_GUIDE.md`

Should include:

- exercise philosophy,
- exercise types,
- how to use hints,
- where to start by confidence level,
- how the exercise layer relates to the archive.

## `EXERCISE_ORDER.md`

Should include:

- grouped recommended sequence,
- dependencies,
- checkpoint-style progression,
- exercise jumps after major concept or system files,
- preserved checkbox state.

## Exercise Files

Should usually include:

- framing,
- goal,
- starting point,
- tasks or checkpoints,
- hints,
- expected behaviour or evaluation criteria,
- links back to the concept/system files they reinforce.

## Reference Files In `learning/references/`

Should usually serve quick lookup or interpretation:

- notation guides,
- status conventions,
- diagrams,
- compact reference tables,
- mini-cheat sheets.

Keep these useful and focused rather than generic.
