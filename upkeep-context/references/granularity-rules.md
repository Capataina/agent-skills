# Granularity and Boundary Rules

## Table of Contents

1. Stable Granularity Goal
2. What Deserves Its Own File
3. What Must Not Drive File Boundaries
4. Boundary Tests
5. Merge Rules
6. Split Rules
7. Architecture vs System Scope
8. Cross-Cutting Topics

## 1. Stable Granularity Goal

The goal is not “many files” or “few files.” The goal is **stable canonical files**.

A good `context/` layout is one where:

- each important topic has one primary home,
- documents can evolve independently when their subsystem changes,
- and repeated upkeep does not cause constant renaming or reshuffling.

## 2. What Deserves Its Own File

A topic deserves its own file in `systems/` when most of these are true:

- it has a distinct responsibility,
- it owns a meaningful implementation surface,
- it changes on a somewhat independent axis,
- it has interfaces with multiple neighbouring systems,
- it carries its own risks, constraints, or durable lessons,
- keeping it separate reduces confusion rather than creating it.

Examples that often justify separate files:

- analytics,
- environment simulation,
- observation/sensor pipeline,
- controller/brain subsystem,
- determinism/replay infrastructure,
- debug overlays,
- telemetry/observability,
- persistence/snapshots,
- networking,
- job scheduling,
- search/indexing.

## 3. What Must Not Drive File Boundaries

Never split canonical docs by:

- milestone,
- phase,
- release,
- week,
- “recent work,”
- task batch,
- chronology,
- developer ownership alone.

These are unstable slicing axes and produce overlap fast.

Bad examples:

- `milestone-1.md`
- `phase-2.md`
- `systems/recent-changes.md`
- `training-updates.md`

## 4. Boundary Tests

Use these tests when deciding whether a topic deserves its own file.

### Independent Change Test

If topic A changes, does topic B usually stay mostly unchanged?

If yes, separate docs may be justified.

### Canonical Home Test

Can a reader answer “where should I document X?” with one obvious file?

If no, the boundaries are too fuzzy.

### Overlap Pressure Test

Will two files repeatedly need to explain the same facts?

If yes, they should probably be merged or reframed.

### Reader Navigation Test

Would a new reader naturally know where to look for this topic?

If not, rename or restructure.

### Stability Test

Will this file still make sense six months from now if the subsystem remains?

If the answer depends on chronology or current project phase, the boundary is wrong.

## 5. Merge Rules

Merge files when:

- they materially duplicate the same subsystem reality,
- the distinction between them is mostly chronological,
- one file exists only because of temporary project sequencing,
- one file is too thin to justify independence,
- readers cannot tell which file truly owns the topic.

When merging:

- pick one file as canonical,
- move durable content into it,
- remove redundant wording,
- delete or rename the losing file only after its useful content has a clear home.

## 6. Split Rules

Split a file when:

- it covers multiple subsystems that change independently,
- different sections have distinct ownership boundaries,
- the file has become too broad to stay current,
- readers must skim large irrelevant sections to find what they need,
- one subsystem's risks and durable notes are being buried under another.

When splitting:

- define the new ownership line explicitly,
- move content without rewriting everything unnecessarily,
- keep the old filename only if one resulting file clearly matches it.

## 7. Architecture vs System Scope

Use `architecture.md` for:

- repository structure,
- subsystem map,
- dependency direction,
- execution/data pipelines,
- structural notes.

Use `systems/*.md` for:

- implemented behaviour,
- subsystem boundaries,
- concrete interfaces,
- outputs/artifacts,
- risks,
- partial work,
- durable notes.

If content answers “how is the repo organised overall?”, it belongs in architecture.

If content answers “what is true about this subsystem?”, it belongs in a system doc.

## 8. Cross-Cutting Topics

Some topics span multiple systems:

- determinism,
- observability,
- performance,
- security,
- deployment,
- configuration.

Give them their own file in `systems/` only if they have:

- meaningful implementation surface,
- stable identity,
- and future change pressure independent of the systems they touch.

Otherwise, keep them embedded in the owning subsystem docs and mention them in architecture where relevant.

Do not create cross-cutting files in `systems/` just because a topic is conceptually broad. Create them only if they are implementation-real and stable.
