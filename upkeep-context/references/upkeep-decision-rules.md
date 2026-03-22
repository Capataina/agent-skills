# Upkeep Decision Rules

## Table of Contents

1. Baseline Behaviour
2. Minimum-Sufficient Restructuring
3. Preserve / Update / Merge / Split / Rename / Delete
4. Existing Context Folder Handling
5. Initialising a New Context Folder
6. Temporary Plan Hygiene
7. Final Review Rules

## 1. Baseline Behaviour

The default behaviour of this skill is **upkeep**, not reinvention.

That means:

- preserve useful structure,
- update reality in place,
- make only the changes required to keep the folder accurate, navigable, and low-overlap.

Do not optimise for elegance at the cost of unnecessary churn.

## 2. Minimum-Sufficient Restructuring

Before reorganising, ask:

- Is the current file clearly wrong, or merely imperfect?
- Is overlap material, or just adjacent-topic mention?
- Will restructuring improve understanding enough to justify the churn?

If the current layout is good enough, preserve it.

“Good enough” means:

- file scopes are coherent,
- overlap is limited,
- names are understandable,
- a new reader can navigate the folder,
- reality can be updated without major confusion.

## 3. Preserve / Update / Merge / Split / Rename / Delete

### Preserve

Preserve a file when:

- its topic remains valid,
- its scope is coherent,
- overlap is low,
- and current reality can be refreshed in place.

### Update

Update a file when:

- the subsystem still exists,
- the ownership boundary still makes sense,
- but implementation details, risks, or plans have changed.

### Merge

Merge files when:

- two files materially own the same topic,
- the split is chronological or artificial,
- or the distinction between them does not survive normal maintenance.

### Split

Split a file when:

- it contains multiple independently changing systems,
- or readers repeatedly need only one subset of it.

### Rename

Rename only when the current filename is actively misleading.

Do not rename simply because a cleaner name exists.

### Delete

Delete when:

- the file has no remaining canonical role,
- its useful content has been moved elsewhere,
- it is obsolete temporary scaffolding,
- or it is a pure anti-pattern such as milestone slicing.

## 4. Existing Context Folder Handling

When `context/` already exists:

1. inventory all files,
2. classify them by type and scope,
3. map each file to a stable subsystem or role,
4. identify overlap, stale reality, bad naming, and missing canonical homes,
5. choose the smallest corrective set of edits.

Do not assume every file needs rewriting.

## 5. Initialising a New Context Folder

When `context/` does not exist:

1. inspect the repository deeply enough to infer the subsystem map,
2. create `architecture.md`,
3. create one file in `systems/` per stable subsystem/feature area,
4. avoid speculative files for uncertain future systems,
5. include durable notes only where there is real evidence.

A new folder should be comprehensive, but not padded with speculative placeholders.

## 6. Temporary Plan Hygiene

Files in `plans/` are temporary execution aids.

Rules:

- create them only on explicit request or when clearly demanded by the workflow,
- keep only one active plan by default,
- remove or archive stale plans,
- never let a completed execution plan silently become part of the long-term memory layer.

## 7. Decisions and References Hygiene

Files in `decisions/` and `references/` should be created only when they add durable value that would otherwise distort `architecture.md` or `systems/`.

Create a file in `decisions/` when:

- the choice is cross-cutting,
- its trade-offs matter later,
- and it does not belong cleanly to one subsystem file.

Create a file in `references/` when:

- research or supporting material is deep enough to deserve its own home,
- it may be revisited later,
- and it is not itself current implementation truth.

Do not let either folder become a dumping ground.

## 8. Final Review Rules

Before finishing, verify:

- every important topic has a clear home,
- overlap is materially lower than before,
- preserved files stayed preserved where possible,
- any rename/delete/merge/split was justified by real structural benefit,
- folder roles are being respected,
- no diary-style or milestone-style files remain,
- the folder reads as a coherent repository memory system rather than a loose pile of notes.
