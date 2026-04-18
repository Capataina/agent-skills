---
name: upkeep-learning
description: "Maintains a repository-level learning/ archive as a comprehensive educational system for mastering a project and its surrounding domain. Use when asked to create, rewrite, expand, update, audit, restructure, or preserve project learning materials, study paths, concept papers, system deep-dives, glossaries, exercises, comparisons, or curriculum navigation. Produces exhaustive, first-principles, example-rich teaching content grounded in existing learning/, context/, the root README, and targeted code inspection. Covers both current implementation reality and README-defined direction or domain territory, even when parts are not implemented yet. Not for release notes, product specs, bug fixing, or implementation-facing memory/notes. For durable implementation memory (`context/`), use upkeep-context instead."
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

**Default stance for the task-based rules below:** when in doubt, read the reference. The rules below are triggers for *required* reads; they are not the complete universe of useful reads. If your current edit touches a topic covered by a reference file, read it before editing, even if the trigger wording does not exactly describe your situation.

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

**Making any claim about how something is implemented, or writing project-specific systems/exercises:**
Read `references/code-inspection-protocol.md` before asserting implementation behaviour, teaching a project system, or building a reconstruction/debugging/extension exercise.

### Reference-Load Receipt

Before writing content, emit a short receipt listing the references loaded this pass, in the order they were read, with timestamps or a simple ordered list. For each task-based reference, mark one of: `read`, `not triggered`, or `triggered but skipped — [specific reason]`. "Triggered but skipped" is a failure unless the reason is concrete and narrow; generic reasons like "didn't feel necessary" are not acceptable. When a reference file is skipped this pass, the Promoted Imperatives below still apply.

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

The top-level model should remain stable unless the repository has a compelling reason to differ. `LEARNING_MAP.md` serves as both the usage guide and the structural overview — no separate `DIRECTORY_TREE.md` is required.

Deeper topic subfolders are conditional, but archive depth is encouraged. Create topic clusters when they improve study flow or reflect the scale of the material. Do not flatten a genuinely large domain just to keep the tree small.

## Promoted Imperatives From References

These imperatives live in full form in the reference files but matter enough that they are restated here verbatim. When any reference file is skipped this pass (see the Reference-Load Receipt above), these imperatives still apply.

- **Exercise files must not contain complete answer-heavy implementations.** (from `exercise-strategy.md`) Exercise scaffolds must withhold the answer. If a learner could run the file as-is and see the solution, the exercise has failed.
- **Avoid nested `README.md` files inside `learning/`.** (from `learning-architecture.md`) Use role-specific names: `LEARNING_MAP.md`, `STUDY_GUIDE.md`, `PATH_INDEX.md`, `EXERCISE_GUIDE.md`, `EXERCISE_ORDER.md`, `SOLUTION_INDEX.md`.
- **Check coverage across all ten Main Learning Surfaces.** (from `coverage-and-organisation.md`) Foundational prerequisites; core domain concepts; reusable domain patterns; current project architecture and systems; important decisions and trade-offs; future project direction and README-defined domain territory; current vs planned vs superseded contrasts where the contrast teaches something; project-specific practice tasks; glossary support and terminology; curated supporting materials. The archive does not need equal depth everywhere, but it must intentionally evaluate all ten.
- **If the README makes an area central, it belongs in `learning/` even when it is not yet implemented.** (from `source-model.md`) The archive teaches the project the repository is trying to become, not only the project that exists at this exact moment.
- **Narrative Standard.** (from `depth-and-writing-standards.md`) For every major concept file, ask: could a motivated learner build a working understanding from this file alone, or are they left with a list of things to look up elsewhere? If the latter, the file is a topic inventory, not a teaching document. Expand it.

## Exercises Are Code Files

Exercises in `learning/exercises/` are code files, not markdown documents.

Use `.py`, `.rs`, or whatever language fits the project. The exercise prompt, goal, tasks, hints, and expected behaviour live as a structured comment block at the top. The working area for the learner starts immediately below. Solution files in `exercises/solutions/` are code files in the same language, named identically to the exercise they answer.

Purely conceptual exercises with no code surface (design reasoning, written comparisons) may remain as `.md`, but implementation, debugging, extension, and reconstruction exercises must be code.

## Operating Rules

### 1. Treat `learning/` as a living, maintained educational archive

This is not a one-shot generation. The archive is evergrowing and dynamic. The skill may initialise `learning/`, but it should primarily think in terms of upkeep: update and expand existing files in place, preserve useful prior material, add new files when the archive is underspecified, rework navigation when the project evolves, and deepen material aggressively when prior coverage is thin.

### 2. Cover the full learning surface, not just current code reality

The archive must teach what exists now, what the project is trying to become, the theory required to understand both, and the trade-offs and alternatives around that journey. If the root `README` makes an area central, that area belongs in `learning/` even when not yet implemented.

### 3. Navigation is a first-class artefact

`learning/` must always be traversable through multiple entry points: `LEARNING_MAP.md`, `STUDY_GUIDE.md`, `paths/*.md`, `exercises/EXERCISE_ORDER.md`. Do not rely on one massive curriculum file as the only path.

### 4. Exhaustiveness matters more than restraint

There is no such thing as "too much learning" in this skill. If a major topic deserves more teaching, write more teaching. Target exhaustive coverage across foundations, core concepts, domain patterns, project systems, decisions, trade-offs, current/planned/superseded approaches where contrast is educational, and project-specific exercises.

**Signal-over-volume guard.** "More is better" does not mean longer files are better. A 400-line concept file is valuable only if the additional length carries additional teaching — new angles, worked examples, comparisons, misconceptions, cross-links. If a section can be removed without the learner losing something, it is volume, not coverage. In the Completeness Audit, state the *new-information density* of major expansions, not the raw line count.

### 5. Keep top-level structure stable and deeper structure conditional

Use the stable top-level tree above. Below that, create deeper topic folders whenever they materially improve scanability, progression, or topic separation.

### 6. Preserve learner progress

Checklist files are part of the learning system's state. Preserve them across upkeep whenever there is a clear semantic mapping. Checkbox-heavy files usually include `STUDY_GUIDE.md`, `paths/*.md`, `exercises/EXERCISE_ORDER.md`, and optional resource-tracking files.

For every pre-existing checkbox (including `- [x]` ticks, in-progress markers, and path/order entries), the Obligation Completion Ledger must record one of: `preserved at [new path]`, `moved from [old path] to [new path]`, `reset because [specific semantic-change reason]`, or `intentionally absent because [reason]`. A missing entry or a generic reason ("restructured") is a failure — name the change that invalidated the progress.

Concept files, systems files, glossary files, and decision files should generally not contain learner checkboxes.

### 7. Preserve old, planned, and comparative material when it teaches something

When the project replaces one approach with another, do not automatically delete the old learning material. Preserve it through project comparisons, evolution notes, short status sections, or roadmap-facing files.

### 8. Use formatting as a teaching tool

Rich formatting is a teaching tool, not decoration. Tables for comparisons, ASCII diagrams for flows and structures, dependency maps, notation tables — use whatever shape teaches the topic best. See `references/visual-markdown-patterns.md`.

## Failure Modes To Name And Resist

Name these failure modes out loud when you catch yourself heading toward them. Self-labelling is cheaper than recovery.

- **Potemkin archive.** Rich navigation over shallow content. Many files, many cross-links, little actual teaching. Detect by asking: does the median concept file satisfy the Narrative Standard, or does it just exist?
- **Narrative inversion.** Bullet lists where connected explanation is needed. A list of assertions is not a mental model.
- **Present-tense collapse.** README-defined future direction quietly dropped because it is not implemented yet. The archive ends up teaching a smaller, safer project than the README describes.
- **Silent progress reset.** Existing learner checkbox state wiped without acknowledgement during restructure. The Operating Rule 6 ledger defends against this; skipping it is the failure.
- **Reference-load pretence.** Claiming a reference was consulted without actually loading it, or loading it so shallowly that its imperatives do not propagate into the output. The Reference-Load Receipt defends against this.
- **Tool-asymmetry on investigation.** This skill is comfortable with `Read` and `Write` over markdown but treats `Grep`/`Glob`/code reads as optional overhead. Code inspection has lower pretraining support for this skill than prose editing, so the urge to skip it is a systematic bias, not a signal that inspection is unnecessary. **Treat the urge to skip code inspection as a signal to do it.**
- **"Be exhaustive" satisficing.** Producing volume that looks exhaustive (line count, file count) while leaving the same topics shallow as before. The Signal-over-Volume Guard in Operating Rule 4 defends against this.

## Execution Workflow

When this skill is triggered, follow this sequence. Steps 4 and 9 are explicit pattern-breaker checkpoints — do not skip them even when the task feels close to done.

1. **Read the root `README` first** and immediately extract a bullet list of every area the README treats as central. This list is your **coverage contract** for the pass. Nothing on it is optional by default; anything scoped out must appear in the Skipped-Work Declaration with a reason.
2. **Read the existing `learning/` folder** if present. For each README-area from step 1, note which have corresponding files and which do not.
3. **Read the `context/` folder** if present, for implementation-facing truth.
4. **Pattern-breaker checkpoint.** Emit the Reference-Load Receipt (above). Declare the operating mode (Initialise / Update / Extend / Audit) with a one-sentence justification quoting or paraphrasing the user's ask. Name the top three learning surfaces most at risk of remaining shallow after this pass, and commit to addressing them before the pass closes.
5. **Expand or create navigation files** (`LEARNING_MAP.md`, `STUDY_GUIDE.md`, `paths/*`, `EXERCISE_ORDER.md`) before or alongside content changes.
6. **Update concept, project, exercise, materials, glossary, and reference files** with the depth the archive requires. The at-risk surfaces named in step 4 are not optional for this pass. **Before writing each concept or system file**, reason out loud: name the file path, list the major concepts it will cover, name its prerequisites, list three or more angles or explanation layers it will use, and name at least one worked example or misconception clarification it will include. Cite all of the above before you start writing the file body. Apply the same pattern before producing a new path file, a new exercise, or a new glossary cluster.
7. **Inspect code selectively** per `references/code-inspection-protocol.md`. For any claim that a system/feature/algorithm is implemented, use `Glob`/`Grep` to locate it and spot-check in one to five minutes. Note discrepancies. List every inspection in the Completeness Audit (files inspected, claims verified, uncertainties). **A pass with zero code inspections while teaching implementation-facing content is structurally incomplete.** Aim to verify at least five implementation claims across the pass.
8. **Preserve checklist state** per Operating Rule 6 and produce the checkbox ledger described there.
9. **Mid-pass pattern-breaker.** Re-read the README-area coverage contract from step 1. Mark each area addressed or unaddressed. For each unaddressed area, either return to step 6 and address it, or send it explicitly into the Skipped-Work Declaration with a concrete reason.
10. **Produce the Obligation Completion Ledger and the Skipped-Work Declaration** (see below).
11. **Run the narrative quality rubric** (see Quality Rubric below).

### Mode-conditional completion

The Quality Checklist / Obligation Ledger applies differently depending on the mode declared in step 4:

- **Initialise and Update** — the full ledger and skipped-work declaration apply as written.
- **Extend** — the ledger applies to the extended area and its immediate neighbours in the archive. Unrelated areas are not required to be re-audited; declare scope explicitly and do not pretend the pass covered everything.
- **Audit** — audit mode produces diagnosis, not generation. The ledger is replaced by a structured diagnosis (gaps, weaknesses, missing surfaces, broken progress, recommended follow-up passes). Do not generate new teaching files in audit mode unless the user asks for generation as well.

## Infrastructure and Verification Tier

This section is optional and descriptive. The archive's quality floor is enforced by the ledger and skipped-work declaration regardless of whether infrastructure is in place.

A repository using this skill may additionally configure:

- **A Stop hook** that runs after the skill completes, verifying that the final message contains the Obligation Completion Ledger and Skipped-Work Declaration, and that any claimed file edits actually exist on disk.
- **A SessionStart compact matcher** that re-injects the mandatory-core references into context when conversation compaction would otherwise drop them.
- **A cross-family verifier** that checks consistency between `learning/`, `context/`, and the root `README` — for example, that systems taught in `learning/project/systems/` correspond to real files and that README-central areas appear in `learning/` or are explicitly marked planned.

**Absence of runtime hooks does not relax the ledger requirement.** The ledger is the minimum quality floor; infrastructure is a safety net, not a substitute.

## Skipped-Work Declaration

Before presenting any result, output a Skipped-Work Declaration listing every obligation that was not met this pass. Silent omission is a failure; explicit declaration is not.

You are licensed and required to admit work that was scoped out, blocked, or intentionally shallower than the archive standard. This is a **structural obligation**, not a judgement about competence. Declare it before the result, even if the list is long.

The declaration must list:

- Each of the ten **Main Learning Surfaces** (from `coverage-and-organisation.md`) that was not evaluated or updated this pass, with a one-sentence reason.
- Each **README-defined future area** from your coverage contract (step 1) that was not addressed, with a one-sentence reason.
- Each existing file not expanded despite appearing thin against the Narrative Standard, with a one-sentence reason.
- Each exercise / glossary entry / path file not created despite being warranted by the archive's current state, with a one-sentence reason.

If nothing was skipped, write "Nothing skipped" followed by a single sentence justifying that claim against the coverage contract.

## Obligation Completion Ledger

The ledger is a binary, evidence-based record of what was actually done. Every item must be verifiable against the repository state, not a self-rating.

Produce the ledger as a structured block before the narrative quality rubric. The ledger must include:

- **Sources read.** List each file read this pass with its path and approximate line count. At minimum: root `README`, existing `learning/` top-level files, `context/` top-level files.
- **Mandatory-core references loaded.** The five core references, in the order they were read, with timestamps or ordered list.
- **Operating mode.** Declared mode plus the justification quote or paraphrase from step 4.
- **Task-based references.** One of `read` / `not triggered` / `triggered but skipped — [specific reason]` for each task-based reference in the Reference Loading section.
- **Coverage contract execution.** For each README-defined area in your coverage contract: `addressed — [file path + what was done]` or `skipped — [specific reason, appears in Skipped-Work Declaration]`.
- **Learner progress preservation.** Per Operating Rule 6: every pre-existing checkbox accounted for (`preserved` / `moved` / `reset` / `intentionally absent` with reason).
- **Files touched.** Each file created, edited, moved, or deleted, with a one-sentence rationale.
- **Shallow-coverage audit.** For every major topic file that is part of this pass (and every major topic file over ~500 lines that was edited), state the file path, section count, at least one worked example or misconception clarification it includes, and whether it meets the Narrative Standard. A major topic file with no worked examples and no cross-links is incomplete; name it as such.
- **Code inspections.** Per `code-inspection-protocol.md`: files inspected, claims verified (one sentence each), uncertainties flagged. Zero inspections while teaching implementation content is a failure.
- **Artefact floors.** Concrete counts where applicable: `LEARNING_MAP.md` line count; count of concept files in `concepts/`; count of project-specific exercises; count of paths in `paths/`. These are not arbitrary numeric targets — they are visibility for whether the archive has the breadth its scale implies.

## Quality Rubric (Narrative)

Run this rubric *after* the Obligation Completion Ledger. These are the subjective quality bars; the ledger is the objective one. The rubric is not a substitute for the ledger — both must pass.

- The top-level `learning/` structure is clear and stable.
- `LEARNING_MAP.md` covers both archive usage guidance and structural overview.
- Navigation files exist, are internally consistent, and support a large archive.
- Major topics are taught as connected narratives, not as bullet-point inventories of assertions.
- Technical topics include notation, equations, worked examples, comparisons, or diagrams wherever those improve understanding.
- Current, planned, historical, and superseded material are clearly labelled where ambiguity exists.
- Rich formatting (tables, diagrams, trees, ASCII visualisations) is used wherever it improves understanding, and is not decorative.
- The archive is verbose, explanatory, comprehensive, and unafraid of depth — but the depth carries teaching, not volume (Signal-over-Volume Guard).
