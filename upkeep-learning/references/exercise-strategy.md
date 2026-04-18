# Exercise Strategy

## Table of Contents

1. [Exercise File Format](#exercise-file-format)
2. [Core Exercise Rule](#core-exercise-rule)
3. [Exercise Categories](#exercise-categories)
4. [Topic-First Structure](#topic-first-structure)
5. [Exercise Navigation Files](#exercise-navigation-files)
6. [Checkboxes](#checkboxes)
7. [Solution Files](#solution-files)
8. [Project-Specific Practice](#project-specific-practice)
9. [Archive-Scale Exercise Expectation](#archive-scale-exercise-expectation)
10. [Exercise Verification Gate](#exercise-verification-gate)

Exercises are the practical layer of `learning/`. They should increase mastery, not spoil it.

## Exercise File Format

Exercises are code files, not markdown documents.

Use `.py`, `.rs`, or whatever language fits the project. The exercise prompt, goal, tasks, hints, and expected behaviour live as a structured comment block (docstring or block comment) at the top of the file. The learner's working area starts immediately below that header. This allows the learner to implement directly inside the learning folder without maintaining a separate workspace.

Purely conceptual exercises — design reasoning, written comparisons, thought experiments — may remain as `.md` files when no sensible code surface exists. Implementation, debugging, extension, and reconstruction exercises must be code.

## Core Exercise Rule

Exercise files must not contain complete answer-heavy implementations.

Exercise files should contain:

- the task framing,
- skeleton code or constrained scaffolding when appropriate,
- realistic starting state,
- hints or staged goals when needed,
- expected behaviour,
- progress markers only when the exercise naturally has multiple internal milestones.

They should not contain:

- the full final implementation,
- comments that directly reveal the bug,
- "solutions" disguised as starter code.

## Exercise Categories

Use the type that best teaches the concept:

- minimal implementation,
- debugging,
- extension,
- comparison,
- reconstruction,
- design/explanation exercise.

Not every topic needs every exercise type.

## Topic-First Structure

Organise `exercises/` primarily by topic area:

- `foundations/`
- `core/`
- `domain-patterns/`
- `project/`

Create deeper type folders inside those only when the amount of content justifies it.

## Exercise Navigation Files

Two navigation files are usually required:

### `EXERCISE_GUIDE.md`

Explains:

- what kinds of exercises exist,
- how to use hint files,
- where to start depending on confidence level.

### `EXERCISE_ORDER.md`

Contains the recommended practice order with checkboxes.

This file should:

- group exercises into sensible runs,
- explain dependencies where needed,
- help learners resume after breaks,
- stay in sync with the actual exercise tree.

## Checkboxes

Checkboxes belong mainly in:

- `STUDY_GUIDE.md`
- `paths/*.md`
- `EXERCISE_ORDER.md`
- optional resource-tracking files when explicitly useful

They generally do **not** belong in:

- concept files,
- systems files,
- glossary files,
- comparison files,
- most exercise body content.

### Multi-part exercises

If an exercise naturally contains several stages, the exercise file may include a small internal checklist for those stages.

Example:

- [ ] Implement forward pass
- [ ] Implement loss
- [ ] Implement backward pass
- [ ] Verify expected output

Use this only when the sub-steps are genuinely part of the learner's progress, not as decorative formatting.

## Solution Files

Solutions live in `exercises/solutions/` as code files in the same language as their corresponding exercises. A solution file for `exercises/core/simple-mlp.py` lives at `exercises/solutions/core/simple-mlp.py`. This preserves the folder structure and makes pairing obvious.

`SOLUTION_INDEX.md` remains as a markdown index listing exercises and their solution files.

Solutions should be working implementations, not walkthroughs. Keep them readable but do not over-explain the code — the learning should happen through the exercise, not through reading a heavily commented solution.

Do not make the solution layer so complete or so visible that it undermines the exercises. The solutions folder exists for verification and unblocking, not for bypassing practice.

## Project-Specific Practice

Project-specific exercises are required when reconstructing, debugging, or extending a real project mechanism would materially improve understanding.

Examples:

- rebuild an authentication flow from scratch,
- debug a caching invalidation strategy,
- extend the API pagination system,
- compare two algorithmic choices in the project's own context.

Do not limit exercises to toy math or generic algorithm drills when the project has important systems worth practising directly.

## Archive-Scale Exercise Expectation

In a serious archive, the exercise layer should be broad and substantial.

It should cover:

- foundations,
- core concepts,
- domain patterns,
- project systems,
- debugging,
- comparison and design reasoning,
- roadmap-facing thought exercises where useful.

Do not keep the exercise layer small out of caution. If the archive is large, the practice layer should also be rich.

## Exercise Verification Gate

Before an exercise is considered done, every implementation, debugging, extension, or reconstruction exercise must pass an explicit verification gate. Verification is not optional polish — it is the gate between "looks like an exercise" and "is an exercise". The failure mode being defended against is the exercise file that has the right shape but is unsolvable, over-scaffolded, or quietly contains the answer.

For each exercise file, verify:

- **File type is code, not markdown.** Implementation, debugging, extension, and reconstruction exercises must be `.py`, `.rs`, `.ts`, or whatever language fits the project. A purely conceptual exercise may be markdown; anything that asks the learner to write or modify code must not be.
- **Header and working space proportions are real.** The structured comment header (prompt, goal, tasks, hints, expected behaviour) should be roughly 50 lines or more for a substantive exercise, and the learner working area should be at least 20 lines of scaffolded or empty code. A 200-line header with 3 blank lines beneath is a brief in exercise clothing; a 5-line header with an empty body is a missing prompt.
- **The exercise is solvable.** Sketch a rough solution mentally (or on paper) before finalising the exercise. If you cannot sketch the solution in a few minutes, the exercise is either underspecified, too large, or missing information the learner will need. Fix it now rather than leaving the learner stuck.
- **Completion time is realistic.** Estimate how long a motivated learner should spend — roughly 30 minutes to 2 hours for a standard exercise. Much shorter suggests the exercise is trivial or gives away the answer; much longer suggests it should be split into staged exercises.
- **No silent answer leakage.** Re-scan the scaffolding for comments that reveal the bug, variable names that encode the answer, or starter code that is one rename away from the solution.

For each solution file, verify:

- **File name and location match the exercise.** `exercises/core/simple-mlp.py` pairs with `exercises/solutions/core/simple-mlp.py`. Mismatched names or folders break the pairing and make `SOLUTION_INDEX.md` lie.
- **Solution is a working implementation, not a walkthrough.** The solution file should run (or compile) and produce the expected behaviour. It should not be a heavily commented essay that substitutes prose for code — that undermines the exercise.
- **Solution is not more instructive than the exercise.** If learners will read the solution to learn the topic, the exercise file has already failed. Teaching belongs in the concept files; the solution file exists for verification and unblocking.

For exercise ordering in `EXERCISE_ORDER.md`, verify:

- **Pedagogical progression is real.** Each exercise should build on genuine prerequisites, not just sit in the next slot. If two exercises are independent, group them side by side rather than implying an order that does not matter.
- **Dependencies are stated where they exist.** When an exercise requires a concept taught in a specific concept file or an earlier exercise, say so explicitly in the order file.
- **The order file matches the exercise tree.** After any rename, move, or addition, reconcile `EXERCISE_ORDER.md` with the current tree before the pass ends.

If any of these checks fail, fix the exercise before presenting the pass as complete. A broken exercise is worse than a missing one — it teaches the learner to distrust the archive.
