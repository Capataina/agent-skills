# agent-skills

A curated archive of agent skills for software development workflows.

## Skill Pipelines

Most skills are designed to be used in sequence. Each pipeline takes work from idea through implementation.

### Feature Pipeline

Build new features from concept to working code.

| Order | Skill | What it does |
|-------|-------|-------------|
| 1 | `/new-feature` | Interactive design session to explore a feature idea from the user's perspective — UX, edge cases, assumptions. Produces a feature spec. |
| 2 | `/architect-feature` | Explores the codebase and collaboratively designs an implementation plan — requirements, component design, dependency mapping. |
| 3 | `/implement-feature` | Implements the architected plan end-to-end in an isolated worktree — writes tests, builds in dependency order, reviews, documents. |

### Refactor Pipeline

Improve existing code structure safely and incrementally.

| Order | Skill | What it does |
|-------|-------|-------------|
| 1 | `/new-refactor` | Interactive session to identify and scope a refactoring opportunity — code smells, coupling, missed abstractions. Produces a refactor brief. |
| 2 | `/architect-refactor` | Maps dependencies, designs the migration path, and produces a step-by-step transformation plan. |
| 3 | `/implement-refactor` | Implements the plan in an isolated worktree — writes characterization tests, transforms in dependency order, reviews, documents. |

### Test Pipeline

Add tests to existing code methodically.

| Order | Skill | What it does |
|-------|-------|-------------|
| 1 | `/plan-tests` | Explores the codebase and designs a structured test plan — test groups, dependency waves, mocking strategy. |
| 2 | `/implement-tests` | Executes the plan by spawning parallel implementor agents per dependency wave. Treats failing tests as valuable discoveries, not problems. |

## Standalone Skills

### `/quick-fix`

Triage for bugs, small fixes, and minor improvements. Diagnoses scope and either implements directly or escalates to `/new-feature` or `/new-refactor` when scope creep is detected.

### `/define-vision`

Interactive session to define or refine a project's product vision. Produces `docs/VISION.md` covering purpose, design pillars, audience, constraints, and non-goals.

## Upkeep Skills

Long-lived maintenance skills that keep project documentation grounded in code reality.

### `/upkeep-context`

Maintains a `context/` folder as durable implementation memory — architecture docs, subsystem descriptions, and decisions grounded in the current codebase. Not product specs or changelogs.

### `/upkeep-learning`

Maintains a `learning/` folder that teaches a project from first principles — learning paths, concept files, deep-dives, exercises, and glossaries that evolve with the code.
