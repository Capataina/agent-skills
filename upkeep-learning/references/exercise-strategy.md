# Exercise Strategy

Exercises are the practical layer of `learning/`. They should increase mastery, not spoil it.

## Core Exercise Rule

Exercise files must not contain complete answer-heavy implementations.

Exercise files should contain:

- the task framing,
- skeleton code or constrained scaffolding when appropriate,
- realistic starting state,
- hints or staged goals when needed,
- expected behavior,
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

## Hint-Oriented Solutions

If `solutions/` exists, it should be hint-oriented rather than answer-heavy.

Preferred structure:

- `SOLUTION_INDEX.md`
- topic-grouped hint files

Hint files should usually provide:

1. a first nudge,
2. a stronger directional hint,
3. a near-complete explanation only if appropriate for the repository.

Do not make the solutions layer so complete that it undermines the exercises.

## Project-Specific Practice

Project-specific exercises are required when reconstructing, debugging, or extending a real project mechanism would materially improve understanding.

Examples:

- rebuild a centreline construction system,
- debug reward shaping,
- extend the observation vector,
- compare two algorithmic choices in the project's own context.

Do not limit exercises to toy math or generic algorithm drills when the project has important systems worth practising directly.
