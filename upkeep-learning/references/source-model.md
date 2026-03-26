# Source Model

Do not treat the sources as a simple ranking where one source determines the entire learning archive.

Use each source for its proper teaching job.

## Source Roles

### Existing `learning/`

Use existing `learning/` to determine:

- current archive structure,
- existing file scopes,
- study routes,
- learner progress state,
- already-covered material,
- historical educational choices worth preserving.

Existing `learning/` is the current archive state, not a reason to keep weak material weak. Improve aggressively where coverage is thin.

### `context/`

Use `context/` to determine:

- current implementation reality,
- subsystem boundaries,
- architecture understanding,
- stable naming conventions,
- active technical plans,
- durable implementation lessons.

`context/` is the main maintained source for implementation-facing truth.

### Root `README`

Use the root `README` to determine:

- project mission,
- project scope,
- intellectual territory,
- future direction,
- research goals,
- domain areas the project considers central,
- terminology and framing the archive should preserve.

If the `README` makes an area central, it belongs in `learning/` even when it is not yet implemented in code or fully represented in `context/`.

This is critical. The learning archive must teach the project the repository is trying to become, not only the project that exists at this exact moment.

### Code

Use targeted code inspection to:

- verify implementation-specific claims,
- identify real file locations and runtime boundaries,
- confirm whether a system, pattern, or algorithm is actually implemented,
- resolve ambiguity between docs.

Do not perform broad code mining by default when `context/` and `README` already provide enough direction.

## Required Learning Surfaces

The archive should draw from all four sources to cover at least:

1. current implementation reality,
2. project mission and roadmap,
3. prerequisite domain theory,
4. comparisons between current state and intended direction.

## Status Labelling

Because the archive covers more than current implementation, label material clearly when needed.

Useful status types include:

- `Current in the project runtime`
- `Current in the maintained implementation`
- `Foundational domain knowledge`
- `Planned project direction`
- `Historical but still educationally useful`
- `Superseded in implementation`

Do not let “not implemented yet” erase important learning surfaces.

## Conflict Resolution

When sources disagree:

1. code determines implementation reality,
2. `context/` is the maintained implementation-facing memory layer,
3. `README` determines mission, intended scope, and roadmap,
4. existing `learning/` should be updated to reflect the right distinction.

Do not force the archive to choose between present reality and future direction. Teach both, and label them honestly.
