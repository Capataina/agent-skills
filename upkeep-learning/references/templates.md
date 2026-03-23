# Templates

Use these templates as structural baselines. Adapt them to the repository, but preserve the role of each file.

## 1. `LEARNING_MAP.md`

````markdown
# Learning Map

[1-3 paragraph explanation of what `learning/` is for, how it relates to `context/`,
and how learners should use it.]

## Start Here

- If you want a broad overview: see `DIRECTORY_TREE.md`
- If you want route guidance: see `STUDY_GUIDE.md`
- If you want a specific path: see `paths/PATH_INDEX.md`
- If you want to practise: see `exercises/EXERCISE_ORDER.md`

## Progress Tracking

[Explain which files contain checkboxes and how they are preserved across upkeep.]
````

## 2. `DIRECTORY_TREE.md`

````markdown
# Directory Tree

```text
learning/
├── ...
```

## Key Locations

- `paths/` — [what lives here]
- `concepts/` — [what lives here]
- `project/` — [what lives here]
- `exercises/` — [what lives here]
- `materials/` — [what lives here]
````

## 3. `STUDY_GUIDE.md`

````markdown
# Study Guide

[High-level orientation. This is not a strict linear curriculum.]

## Choose a Route

- [ ] Start with `paths/project-architecture-path.md` if you want a top-down overview
- [ ] Start with `paths/mathematics-path.md` if you want foundations first
- [ ] Start with `paths/implementation-first-path.md` if you want to rebuild systems quickly
- [ ] Start with `paths/interview-preparation-path.md` if your immediate goal is explanation fluency

## Suggested Combinations

- [ ] Foundations + reinforcement learning
- [ ] Systems + project architecture
- [ ] Neuroscience + project evolution
````

## 4. `paths/*.md`

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

## 5. Concept Files

````markdown
# [Concept Name]

## Why This Matters Here

[Project-relevant motivation.]

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

## How This Appears In The Project

[Link back to project systems or decisions where useful.]

## Common Misunderstandings

❌ ...
✅ ...

## Terms Used Here

[Local glossary or links back to `GLOSSARY.md` as appropriate.]
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

## Important Trade-Offs

[Why the system looks like this.]

## Learning Links

- Related concepts: ...
- Related exercises: ...
- Related comparisons or decisions: ...

## Status

[Only include if current vs superseded state could confuse the learner.]
````

## 7. `project/comparisons/*.md`

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

## 8. `exercises/EXERCISE_ORDER.md`

````markdown
# Exercise Order

## Foundations

- [ ] `exercises/foundations/...`
- [ ] `exercises/foundations/...`

## Core Concepts

- [ ] `exercises/core/...`
- [ ] `exercises/core/...`

## Project Systems

- [ ] `exercises/project/...`
- [ ] `exercises/project/...`

## Suggested Jumps

- After `simple-mlp.py`, do ...
- Before `rebuild-centreline-construction.py`, read ...
````

## 9. Exercise Files

````markdown
# [Exercise Name]

[Short framing paragraph.]

## Goal

[What the learner is trying to build, debug, compare, or extend.]

## Starting Point

[What is already provided.]

## Tasks

- [ ] [Only include internal checkboxes when the exercise naturally has staged milestones]

## Hints

1. ...
2. ...
3. ...

## Expected Behaviour

[What success looks like.]
````

## 10. Hint Files

````markdown
# [Exercise Name] Hints

## Hint 1

[Light nudge]

## Hint 2

[Stronger directional guidance]

## Hint 3

[Near-complete explanation only if warranted]
````
