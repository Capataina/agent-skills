# Source Priority

This skill should not treat codebase traversal as the default source of truth for learning generation.

The preferred source order is:

1. existing `learning/`
2. `context/`
3. root `README`
4. targeted code inspection

## Why this order exists

`learning/` is the current educational layer.

`context/` is the repository memory layer and should capture the project's current structure, systems, and durable implementation knowledge more cheaply than re-deriving everything from raw code.

The root `README` usually captures project purpose, direction, and framing that a learning system should preserve.

Code inspection is still important, but it should be used selectively for validation and implementation-specific detail, not as the first-pass discovery mechanism for every repository.

## Use each source for the right job

### Existing `learning/`

Use to determine:

- current folder structure,
- existing navigation model,
- learner progress state,
- already-covered concepts,
- already-preserved historical material.

Do not discard it casually.

### `context/`

Use to determine:

- subsystem boundaries,
- current implementation reality,
- architectural decisions,
- durable lessons,
- naming conventions that the repository already uses.

This is especially important for naming consistency between `context/` and `learning/`.

### Root `README`

Use to determine:

- project mission,
- high-level scope,
- core technologies,
- intended learning framing,
- important project language and terminology.

Do not let nested documentation files overshadow the root README.

### Targeted code inspection

Use only when needed for:

- validating implementation-specific claims,
- finding exact file locations for system deep-dives,
- clarifying ambiguous behavior not resolved in `context/` or `README`,
- checking whether a system, algorithm, or pattern is actually present.

Do not perform full-repository traversal unless the repository lacks usable context and the task cannot be completed responsibly without it.

## Conflict resolution

If sources disagree:

1. code reality outranks stale docs,
2. `context/` usually outranks older `learning/` prose,
3. the root `README` provides framing, not implementation truth.

When a conflict is discovered, update `learning/` to match current reality while preserving educationally useful historical material in the right place.
