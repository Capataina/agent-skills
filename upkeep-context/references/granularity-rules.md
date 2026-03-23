# Granularity and Boundary Rules

## Table of Contents

1. Stable Granularity Goal
2. What Deserves Its Own File
3. What Must Not Drive File Boundaries
4. Boundary Tests
5. Merge Rules
6. Split Rules
7. Preserve Rules
8. Architecture vs System Scope
9. Cross-Cutting Topics

## 1. Stable Granularity Goal

The goal is not "many files" or "few files." The goal is **stable canonical files**.

A good `context/` layout is one where:

- each important topic has one primary home,
- documents can evolve independently when their subsystem changes,
- repeated upkeep does not cause constant renaming or reshuffling,
- the amount of structure is justified by the repository rather than by a template quota.

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
- observation or sensor pipelines,
- controller or brain subsystems,
- determinism or replay infrastructure,
- debug overlays,
- telemetry or observability,
- persistence or snapshots,
- networking,
- job scheduling,
- search or indexing.

## 3. What Must Not Drive File Boundaries

Never split canonical docs by:

- milestone,
- phase,
- release,
- week,
- "recent work",
- task batch,
- chronology,
- developer ownership alone,
- arbitrary repo size labels.

These are unstable slicing axes and produce overlap fast.

## 4. Boundary Tests

Use these tests when deciding whether a topic deserves its own file.

### Independent Change Test

If topic A changes, does topic B usually stay mostly unchanged?

If yes, separate docs may be justified.

### Canonical Home Test

Can a reader answer "where should I document X?" with one obvious file?

If no, the boundaries are too fuzzy.

### Overlap Pressure Test

Will two files repeatedly need to explain the same facts?

If yes, they should probably be merged or reframed.

### Reader Navigation Test

Would a new reader naturally know where to look for this topic?

If not, rename or restructure.

### Stability Test

Will this file still make sense six months from now if the subsystem remains?

If the answer depends on chronology, current project phase, or arbitrary size labels, the boundary is wrong.

## 5. Merge Rules

Merge files when:

- they materially duplicate the same subsystem reality,
- the distinction between them is mostly chronological or artificial,
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

## 7. Preserve Rules

Preserve a layout when:

- file scopes are coherent,
- overlap is limited,
- naming is understandable,
- the current structure already helps reader navigation,
- and reality can be updated without structural churn.

Do not restructure purely because a cleaner theoretical decomposition exists.

## 8. Architecture vs System Scope

Use `architecture.md` for:

- repository structure,
- subsystem map,
- dependency direction,
- execution or data pipelines,
- structural notes.

Use `systems/*.md` for:

- implemented behaviour,
- subsystem boundaries,
- concrete interfaces,
- outputs or artifacts,
- risks,
- partial work,
- durable notes.

If content answers "how is the repo organised overall?", it belongs in architecture.

If content answers "what is true about this subsystem?", it belongs in a system doc.

## 9. Cross-Cutting Topics

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
- independent change pressure,
- and enough reality to justify a canonical home.

Otherwise, keep them embedded in the owning subsystem docs and mention them in architecture where relevant.
