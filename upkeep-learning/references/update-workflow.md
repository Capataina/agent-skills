# Update Workflow

## Table of Contents

1. [Low-Churn Rule](#low-churn-rule)
2. [Progress Preservation Rule](#progress-preservation-rule)
3. [Add / Merge / Split / Retire](#add--merge--split--retire)
4. [Current vs Superseded Material](#current-vs-superseded-material)
5. [Navigation Synchronisation](#navigation-synchronisation)
6. [Depth Synchronisation](#depth-synchronisation)

This skill should prefer upkeep over replacement.

## Low-Churn Rule

If an existing file:

- has a coherent scope,
- still fits the project structure,
- and can be updated in place,

then preserve it.

Prefer:

- targeted updates over rewrites,
- content moves over wholesale reorganisation,
- small structural improvements over total folder resets.

Exception:

If the existing archive or skill instructions are deeply underspecified, a full rewrite is justified. Low churn is not a reason to preserve a weak educational standard.

## Progress Preservation Rule

Checklist state is durable learning state.

When updating files such as:

- `STUDY_GUIDE.md`
- `paths/*.md`
- `EXERCISE_ORDER.md`

preserve completed checkboxes whenever there is a clear semantic match between the old and new learning item.

### Examples

If:

- a file is renamed but still teaches the same topic, keep the checkbox checked.
- one learning item is split into two smaller items, preserve completion for the portion clearly covered already and leave genuinely new material unchecked.
- one path is re-ordered, preserve completion state and move the item rather than resetting it.

Do not casually wipe learner progress because the structure changed.

## Add / Merge / Split / Retire

### Add

Add files when:

- the project gained a meaningful new learning surface,
- a prior file is overloaded with multiple independent topics,
- a comparison or evolution file is needed to explain a change in project direction,
- practice coverage is missing for an important system or concept.

### Merge

Merge files when:

- they duplicate ownership,
- they repeatedly explain the same material,
- their topic boundaries are not independently stable.

### Split

Split files when:

- one file has become too broad to scan well,
- the topics change independently,
- the current structure hides useful navigational boundaries.

### Retire

Retire files when:

- the material is stale and no longer educationally useful,
- the topic has been fully absorbed into a more canonical home,
- keeping the file would create confusion about current reality.

Retiring educationally useful material should usually happen by moving or reframing it, not by silently deleting it.

## Current vs Superseded Material

When a project changes direction:

- update current-path files,
- add comparison/evolution material when useful,
- keep old approach files only if they still help the learner understand the project or domain.

Examples:

- keep `rest-api.md` if the project moved to GraphQL but REST still explains the transition,
- add `rest-vs-graphql.md` when the comparison teaches a real trade-off,
- mark ambiguous files with a short status section when needed.

## Navigation Synchronisation

Whenever the tree changes, update the navigation layer as part of the same task:

- `LEARNING_MAP.md` (covers both usage guidance and directory structure)
- `STUDY_GUIDE.md`
- `paths/*.md`
- `EXERCISE_ORDER.md`

Do not leave structural changes unreflected in the navigation files.

## Depth Synchronisation

When a major file is clearly too thin for its topic, do not merely patch a sentence or two.

Expand it to the depth the archive requires, and update:

- relevant path files,
- exercise links,
- glossary references,
- comparison or evolution files if the deeper treatment reveals gaps.
