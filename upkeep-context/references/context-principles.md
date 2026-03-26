# Context Principles

This reference defines what `context/` is, what it must achieve, and what it must never become.

## Core Definition

`context/` is the repository's working memory layer.

Its job is to let a capable engineer or agent understand:

- what the repository contains,
- how the major systems fit together,
- what currently exists,
- what is partial, fragile, or missing,
- what previous attempts still matter,
- where a change will likely have downstream effects.

It is not a generic documentation bucket. It is a maintained implementation-state layer.

## Required Qualities

### Comprehensive, not thin

Someone who reads `context/` should be able to understand the repository as a whole without doing a first-pass rediscovery from code.

Comprehensive means the folder captures:

- repository structure,
- subsystem boundaries,
- core interfaces and flows,
- implementation reality,
- known issues and risks,
- durable lessons from past attempts.

It does not mean verbosity for its own sake.

### Thorough, not redundant

The standard is:

> say as much as needed without redundancy or padding

`context/` should be faster to read than re-exploring the repository. If a document becomes so sparse that a reader must immediately re-derive the basics from code, the memory layer has failed.

### Dynamic, not archival

`context/` must change with the repository.

It should track current reality, not preserve every intermediate state that once existed. Files must be updated, merged, split, renamed, or deleted as the repository changes.

### Durable, not chronological

Preserve durable knowledge:

- why an approach was discarded,
- what failed and why,
- what constraints remain because of it,
- what would need to be true to revisit it safely.

Do not preserve chronological accumulation:

- "today we did X",
- "yesterday we tried Y",
- weekly change logs,
- stacked milestone records.

### Adaptive, not threshold-driven

Do not decide depth or structure from arbitrary repo-size labels or fixed numeric cutoffs.

Instead, adapt to:

- boundary clarity,
- overlap pressure,
- dependency complexity,
- change independence,
- and how much explanation a future reader would need to act safely.

## Truth Model

When maintaining `context/`, treat the repository itself as primary evidence for implementation truth.

Use the existing `context/` folder as prior memory:

- valuable when accurate,
- correctable when stale,
- replaceable when structurally wrong.

Do not let polished old documents override the actual codebase.

## Evidence Standard

Context claims should be grounded in inspected repository evidence.

That means:

- inspect representative entrypoints and owning modules,
- read enough code and configuration to justify major subsystem boundaries,
- distinguish direct observation from inference,
- avoid confident claims about behaviour that was not actually verified.

The skill does not need a fixed file-count quota. It needs enough evidence to support its claims.

## What Belongs In Context

`context/` should capture:

- architecture and repository shape,
- subsystem responsibilities,
- dependency direction and important flows,
- current implemented reality,
- partial work and active risks,
- planned or missing work tied to the owning subsystem,
- durable notes from prior attempts,
- obsolete approaches when still relevant to future decisions.

## What Does Not Belong In Context

Avoid:

- product specifications,
- roadmap documents detached from implementation ownership,
- release notes,
- changelogs,
- meeting notes,
- brainstorming dumps,
- milestone-by-milestone narrative progress files,
- generic history files,
- vague catch-all notes files.

## Canonical Ownership Principle

Every important topic should have one primary home.

Examples:

- architecture belongs in `architecture.md`,
- analytics implementation reality belongs in `systems/analytics.md`,
- a failed lidar experiment belongs inside the owning system doc if it still affects future decisions,
- a durable controller-baseline choice may belong in `decisions/controller-baseline.md`,
- an A2C versus SAC research comparison may belong in `references/a2c-vs-sac.md`.

This rule reduces overlap and prevents memory drift.

## Supportive Presentation Principle

Different markdown structures can support the same canonical topic inside one document.

For example:

- a table may inventory interfaces,
- bullets may summarize the operational implications,
- a diagram may show the same flow at a glance.

That is supportive presentation, not duplicate ownership.

The line is simple:

- multiple formats inside one owning document are allowed when they improve comprehension,
- multiple documents acting as co-owners of the same topic are not.

## Stability Principle

Repeated upkeep should not thrash a healthy folder.

The skill should preserve existing structure when it is:

- coherent,
- low-overlap,
- and still aligned with the codebase.

Good-enough structure is often preferable to perfect theoretical structure if perfect structure would create needless churn.
