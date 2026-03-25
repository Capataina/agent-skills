# Examples

## Table of Contents

1. Milestone Decomposition to System Decomposition
2. Preserve Good-Enough Structure
3. Merge Duplicate Ownership
4. Durable Note vs History Log
5. Architecture Depth Expectation
6. Supportive Multi-Format Presentation
7. Condense Mature Research Carefully

## 1. Milestone Decomposition to System Decomposition

### Bad layout

```text
context/
├── architecture.md
├── milestone-1.md
├── milestone-2.md
└── milestone-3.md
```

Why it is bad:

- each milestone repeats prior state,
- current reality is scattered across time slices,
- readers must synthesise the present manually.

### Better layout

```text
context/
├── architecture.md
├── systems/
│   ├── environment.md
│   ├── agent-observations.md
│   ├── analytics.md
│   ├── telemetry.md
│   └── agent-learning.md
├── decisions/
├── references/
└── plans/
```

Why it is better:

- each file has a stable scope,
- future upkeep updates one canonical home per topic,
- milestone progress becomes subsystem reality instead of additive clutter.

## 2. Preserve Good-Enough Structure

Suppose a project already has:

```text
context/
├── architecture.md
├── systems/
│   ├── debug-overlays.md
│   ├── telemetry.md
│   └── analytics.md
├── decisions/
├── references/
└── plans/
```

The files are adjacent topics, but:

- each has a coherent responsibility,
- overlap is limited,
- a new reader can navigate them.

Correct action:

- preserve the layout,
- tighten boundaries in place,
- avoid merging just because the topics are related.

Incorrect action:

- merge them into `systems/observability.md` purely for tidiness.

## 3. Merge Duplicate Ownership

Suppose a project has:

```text
context/
└── systems/
    ├── reward.md
    └── training-signal.md
```

Both files explain:

- reward terms,
- value targets,
- terminal penalties,
- rollout reward accumulation.

Correct action:

- choose one canonical file,
- move durable material into it,
- reduce the other file to interface-level mention or delete it if no stable role remains.

## 4. Durable Note vs History Log

### Bad

```markdown
## History

- 2026-03-01: tried lidar
- 2026-03-02: lidar looked noisy
- 2026-03-03: switched to raycasts
```

### Good

```markdown
## Durable Notes / Discarded Approaches

- A lidar-style observation attempt was discarded because the current environment geometry and sampling approach produced noisy, unstable signals relative to the implementation cost.
- If lidar is revisited later, retry only with a clearer spatial aggregation model, explicit normalisation strategy, and dedicated validation tooling so the result can be compared cleanly against raycasts.
```

Why the second version is better:

- no chronology,
- preserves the useful lesson,
- remains relevant months later.

## 5. Architecture Depth Expectation

### Too shallow

```text
repo/
├── src/
├── tests/
└── README.md
```

### Better

```text
repo/
├── src/
│   ├── main.rs                 # App entrypoint and runtime wiring
│   ├── game/                   # Environment simulation and gameplay truth
│   ├── agent/                  # Stable controller-facing interfaces
│   ├── analytics/              # Run-level tracking and export
│   └── debug/                  # Runtime inspection overlays and HUD
├── tests/                      # Regression and unit coverage
├── context/                    # Repository memory layer
└── README.md                   # Project mission and scope
```

The second version is still brief, but it already orients the reader. Strong architecture files should usually go deeper than this into important source, config, test, and doc directories.

## 6. Supportive Multi-Format Presentation

When comparing several modules, a table plus bullets can be better than either one alone.

### Good

```markdown
## Boundaries / Ownership

| Module | Owns | Depends on | Change Pressure |
| --- | --- | --- | --- |
| `scheduler` | job orchestration | queue, config | medium |
| `queue` | task persistence | storage | medium |
| `workers` | task execution | queue, external APIs | high |

- `workers` is the most failure-prone boundary because it touches external APIs directly.
- `scheduler` and `queue` should remain separate canonical topics because orchestration changes do not always require persistence changes.
```

Why it is good:

- the table compresses comparable fields cleanly,
- the bullets pull out the implications a future engineer should notice,
- one document still owns the topic canonically.

### Bad

```markdown
## Boundaries / Ownership

- scheduler owns jobs
- queue owns persistence
- workers execute jobs

## Another File Elsewhere

- scheduler owns jobs
- queue owns persistence
- workers execute jobs
```

Why it is bad:

- the second file creates duplicate ownership,
- the repetition is no longer supportive presentation,
- readers cannot tell which file to trust.

## 7. Condense Mature Research Carefully

Suppose a project once had:

```text
context/
└── references/
    └── actor-critic/
        ├── overview.md
        ├── a2c.md
        └── sac-vs-a2c.md
```

This was justified when:

- the repository was still deciding which baseline direction to trust,
- the subtopics were changing independently,
- the broader research area still needed room to grow.

Later, the repository stabilises around one implemented direction and most of the actionable lessons now belong to one stable topic.

Correct action:

- update stale repository-specific claims,
- preserve the durable research insights,
- condense the folder into one richer canonical file such as `references/actor-critic.md` only if that shape is now easier to maintain and navigate,
- cross-reference any remaining neighbouring files rather than duplicating their content.

Incorrect action:

- delete the broader research simply to make the folder smaller,
- keep the folder expanded forever even after it has become overlapping maintenance overhead,
- collapse the folder into a thin summary that loses the durable insights which justified the research in the first place.
