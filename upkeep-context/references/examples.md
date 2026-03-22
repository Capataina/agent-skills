# Examples

## Table of Contents

1. Milestone Decomposition to System Decomposition
2. Preserve Good-Enough Structure
3. Merge Duplicate Ownership
4. Durable Note vs History Log
5. Architecture Depth Expectation

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

## 6. Decisions and References Placement

### Good

```text
context/
├── architecture.md
├── systems/
│   ├── analytics.md
│   └── agent-learning.md
├── decisions/
│   └── controller-baseline.md
├── references/
│   └── a2c-vs-sac.md
└── plans/
    └── actor-critic-stabilisation.md
```

Why it is good:

- current implementation truth stays in `systems/`,
- the durable choice lives in `decisions/`,
- the deeper supporting comparison lives in `references/`,
- the active execution guide lives in `plans/`.

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

The second version is still brief, but it already orients the reader. Strong architecture files should usually go deeper than this into important source/config/test/doc directories.
