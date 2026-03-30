# Templates

## Table of Contents

1. [`LEARNING_MAP.md`](#1-learning_mapmd)
2. [`STUDY_GUIDE.md`](#2-study_guidemd)
3. [`paths/*.md`](#3-pathsmd)
4. [`paths/PATH_INDEX.md`](#4-pathspath_indexmd)
5. [Concept Files](#5-concept-files)
6. [`project/systems/*.md`](#6-projectsystemsmd)
7. [`project/architecture/*.md`](#7-projectarchitecturemd)
8. [`project/comparisons/*.md`](#8-projectcomparisonsmd)
9. [`project/evolution/*.md`](#9-projectevolutionmd)
10. [`exercises/EXERCISE_GUIDE.md`](#10-exercisesexercise_guidemd)
11. [`exercises/EXERCISE_ORDER.md`](#11-exercisesexercise_ordermd)
12. [Exercise Files (Python)](#12-exercise-files-python)
13. [Exercise Files (Rust)](#13-exercise-files-rust)
14. [Solution Files](#14-solution-files)
15. [`GLOSSARY.md` entry pattern](#15-glossarymd-entry-pattern)
16. [`exercises/solutions/SOLUTION_INDEX.md`](#16-exercisessolutionssolution_indexmd)
17. [Hint Files](#17-hint-files)

Use these templates as structural baselines. Expand them aggressively when the topic warrants it. These are minimum shapes, not upper bounds.

## 1. `LEARNING_MAP.md`

````markdown
# Learning Map

[1-3 paragraph explanation of what `learning/` is for, how it relates to `context/`,
and how learners should use it.]

## Archive Structure

```text
learning/
├── LEARNING_MAP.md     (this file — usage guide and structural overview)
├── GLOSSARY.md
├── STUDY_GUIDE.md
├── paths/              [what lives here]
├── concepts/           [what lives here]
├── project/            [what lives here]
├── exercises/          [what lives here]
├── materials/          [what lives here]
└── references/         [what lives here]
```

[Add one-line descriptions for any important files below the tree.]

## Start Here

- If you want route guidance: see `STUDY_GUIDE.md`
- If you want a specific path: see `paths/PATH_INDEX.md`
- If you want to practise: see `exercises/EXERCISE_ORDER.md`

## Progress Tracking

[Explain which files contain checkboxes and how they are preserved across upkeep.]
````

## 2. `STUDY_GUIDE.md`

````markdown
# Study Guide

[High-level orientation. This is not a strict linear curriculum.]

## Choose a Route

- [ ] Start with `paths/project-architecture-path.md` if you want a top-down overview
- [ ] Start with `paths/mathematics-path.md` if you want foundations first
- [ ] Start with `paths/implementation-first-path.md` if you want to rebuild systems quickly
- [ ] Start with `paths/interview-preparation-path.md` if your immediate goal is explanation fluency

## Suggested Combinations

- [ ] Foundations + core concepts
- [ ] Systems + project architecture
- [ ] Domain theory + practical application
````

## 3. `paths/*.md`

````markdown
# [Path Name]

## Who This Path Is For

[1-3 sentences]

## Recommended Sequence

- [ ] `concepts/...`
- [ ] `concepts/...`
- [ ] `project/...`
- [ ] `exercises/...`
- [ ] `materials/...`

## Notes

[Explain how this path overlaps with others and what to do next.]
````

## 4. `paths/PATH_INDEX.md`

````markdown
# Path Index

[Short framing paragraph explaining how the path system works.]

## Available Paths

- `paths/project-architecture-path.md` — [who it is for, what it emphasises]
- `paths/implementation-first-path.md` — [who it is for, what it emphasises]
- `paths/domain-theory-path.md` — [who it is for, what it emphasises]
- `paths/advanced-topics-path.md` — [who it is for, what it emphasises]

## How To Choose

- If you want current runtime understanding first: ...
- If you want domain theory first: ...
- If you want the fastest route to safe contributions: ...

## Recommended Pairings

- [ ] Path A + Path B
- [ ] Path C + exercises/project/...
````

## 5. Concept Files

````markdown
# [Concept Name]

## Why This Matters Here

[Project-relevant motivation.]

## Prerequisites

- ...
- ...

## Notation

| Symbol | Meaning |
|---|---|
| ... | ... |

## Core Idea

[First-principles explanation.]

## Build-Up

### Step 1: ...
### Step 2: ...
### Step 3: ...

## Worked Examples

### Example 1: ...
### Example 2: ...
### Example 3: ...

## Alternatives Or Contrasts

- ...
- ...

## How This Appears In The Project

[Link back to project systems or decisions where useful.]

## Common Misunderstandings

❌ ...
✅ ...

## Terms Used Here

[Local glossary or links back to `GLOSSARY.md` as appropriate.]

## Related Files

- ...
- ...
````

## 6. `project/systems/*.md`

````markdown
# [System Name]

## What This System Does

[Responsibility and scope.]

## Where It Fits

[How it connects to the wider project.]

## Key Mechanics

[Implementation-facing explanation.]

## Data Flow

```text
[input] -> [transform] -> [output]
```

## Important Parameters Or Ranges

| Item | Value / Shape | Why It Matters |
|---|---|---|
| ... | ... | ... |

## Important Trade-Offs

[Why the system looks like this.]

## Learning Links

- Related concepts: ...
- Related exercises: ...
- Related comparisons or decisions: ...

## Status

[Only include if current vs superseded state could confuse the learner.]
````

## 7. `project/architecture/*.md`

````markdown
# [Architecture Topic]

## Why This Architecture Matters

[Why the learner should care.]

## High-Level Shape

```text
[subsystem] -> [subsystem] -> [subsystem]
```

## Major Boundaries

- ...
- ...

## Runtime Or Data Flow

[Detailed explanation.]

## Design Rationale

[Why the architecture looks this way.]

## Pressure Points And Future Tension

- ...
- ...

## Related Systems And Paths

- ...
- ...
````

## 8. `project/comparisons/*.md`

````markdown
# [A vs B]

## Why This Comparison Matters

[Why the contrast is educationally relevant.]

## What Stayed The Same

...

## What Changed

...

## Why The Project Preferred [Current Approach]

...

## What To Learn From The Older Approach

...
````

## 9. `project/evolution/*.md`

````markdown
# [Evolution Topic]

## Current State

[What exists now.]

## Missing Or Future Pieces

[What still does not exist.]

## Why This Gap Matters

[Why the learner should care.]

## How The Archive Covers It

- Foundations: ...
- Current systems: ...
- Comparisons: ...
````

## 10. `exercises/EXERCISE_GUIDE.md`

````markdown
# Exercise Guide

[What the exercise layer is for.]

## Exercise Types

- Reconstruction
- Debugging
- Extension
- Comparison
- Design reasoning

## How To Use Hints

[When to use them and how not to spoil learning.]

## Where To Start

- If you are new: ...
- If you want project-specific practice: ...
- If you want debugging-heavy work: ...
````

## 11. `exercises/EXERCISE_ORDER.md`

````markdown
# Exercise Order

## Foundations

- [ ] `exercises/foundations/[exercise-name].py`
- [ ] `exercises/foundations/[exercise-name].py`

## Core Concepts

- [ ] `exercises/core/[exercise-name].py`
- [ ] `exercises/core/[exercise-name].py`

## Project Systems

- [ ] `exercises/project/[exercise-name].py`
- [ ] `exercises/project/[exercise-name].py`

## Suggested Jumps

- After `exercises/core/basic-pipeline.py`, do ...
- Before `exercises/project/rebuild-auth-flow.py`, read ...
````

## 12. Exercise Files (Python)

````python
"""
Exercise: [Exercise Name]

[Short framing paragraph explaining what this exercise is about and why it matters.]

Goal:
    [What the learner is trying to build, debug, compare, or extend.]

Starting Point:
    [What is already provided in this file and what the learner needs to supply.]

Tasks:
    - [ ] [staged milestone — only include when the exercise has natural internal stages]
    - [ ] [staged milestone]

Hints:
    1. [Light nudge — directional without giving away the answer]
    2. [Stronger directional hint]
    3. [Near-complete direction — only include if appropriate for the repository]

Expected Behaviour:
    [What success looks like — outputs, assertions, or observable behaviour.]

Related Files:
    Concepts:        learning/concepts/...
    Project systems: learning/project/systems/...
    Paths:           learning/paths/...
"""

# ── Your implementation starts here ──────────────────────────────────────────


````

## 13. Exercise Files (Rust)

````rust
//! Exercise: [Exercise Name]
//!
//! [Short framing paragraph explaining what this exercise is about.]
//!
//! Goal:
//!     [What the learner is trying to build, debug, compare, or extend.]
//!
//! Starting Point:
//!     [What is already provided and what needs to be implemented.]
//!
//! Tasks:
//!     - [ ] [staged milestone]
//!     - [ ] [staged milestone]
//!
//! Hints:
//!     1. [Light nudge]
//!     2. [Stronger directional hint]
//!     3. [Near-complete direction if appropriate]
//!
//! Expected Behaviour:
//!     [What success looks like.]

// ── Your implementation starts here ──────────────────────────────────────────


````

## 14. Solution Files

Solution files live in `exercises/solutions/` and mirror the exercise folder structure. They use the same language as the exercise they answer.

````python
"""
Solution: [Exercise Name]

[Brief explanation of the approach taken and any key decisions.]
"""

# ── Solution ──────────────────────────────────────────────────────────────────

[working implementation]
````

## 15. `GLOSSARY.md` entry pattern

````markdown
### [Term]

[Precise definition.]

[Plain-language explanation.]

[Concrete example.]

[Project-specific relevance if applicable.]

See: `concepts/...`, `project/...`
````

## 16. `exercises/solutions/SOLUTION_INDEX.md`

````markdown
# Solution Index

Solutions are code files in `exercises/solutions/`, mirroring the exercise folder structure.

## Foundations

- `solutions/foundations/[exercise-name].py` — [one-line description]

## Core Concepts

- `solutions/core/[exercise-name].py` — [one-line description]

## Project Systems

- `solutions/project/[exercise-name].py` — [one-line description]
````

## 17. Hint Files

````markdown
# [Exercise Name] Hints

## Hint 1

[Light nudge]

## Hint 2

[Stronger directional guidance]

## Hint 3

[Near-complete explanation only if warranted]
````
