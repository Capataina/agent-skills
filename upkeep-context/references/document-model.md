# Document Model

## Table of Contents

1. [Canonical Context Structure](#canonical-context-structure)
2. [Canonical Ownership Rule](#canonical-ownership-rule)
3. [`architecture.md`](#1-architecturemd)
4. [`systems/<topic>.md`](#2-systemstopicmd)
5. [`notes.md`](#3-notesmd)
6. [`notes/<topic>.md`](#4-notestopicmd)
7. [`plans/<topic>.md`](#5-planstopicmd)
8. [`references/<topic>.md`](#6-referencestopicmd)
9. [System File Maturity Indicators](#system-file-maturity-indicators)
10. [Disallowed Default File Types](#disallowed-default-file-types)

This reference defines the canonical file types, their roles, their required section templates, and how canonical ownership should be preserved even when a document uses multiple presentation formats.

## Canonical Context Structure

Default to this structure:

```text
context/
├── architecture.md
├── notes.md
├── systems/
├── plans/
├── notes/
└── references/
```

`architecture.md`, `systems/`, and `notes.md` are universally essential.

`notes/` should contain files whenever there are project preferences, design rationale, or durable lessons worth preserving. `plans/` and `references/` should contain files only when their role is justified. Do not create filler files just to mirror the model.

## Canonical Ownership Rule

Every important topic should have one primary home.

Allowed:

- one file owns a topic canonically,
- neighbouring files mention that topic only at interface level,
- one document uses both a table and bullets to express the same topic more clearly.

Not allowed:

- two files both fully documenting the same subsystem as if they were both canonical,
- architecture repeating entire system documents,
- references or plans quietly becoming shadow system docs.

Supportive duplication within one document is acceptable. Canonical duplication across documents is not.

## 1. `architecture.md`

### Role

This is the top-down structural truth for the repository.

It should answer:

- what the repository contains,
- how it is organised,
- what the major subsystems are,
- how they depend on one another,
- what the major runtime or data pipelines look like.

### Required Sections

Use this section order:

1. `Scope / Purpose`
2. `Repository Overview`
3. `Repository Structure`
4. `Subsystem Responsibilities`
5. `Dependency Direction`
6. `Core Execution / Data Flow`
7. `Structural Notes / Current Reality`

### Optional Sections

These sections are not universally needed. Include them when the project's shape justifies the additional navigational or analytical value.

- **`Inter-System Relationships`** — data flows between systems, dependency chains, shared state. Include when the project has multiple interacting systems. Not needed for single-system projects.
- **`Critical Paths and Blast Radius`** — end-to-end dependency chains, what breaks when key interfaces change. Include when the project has deep dependency chains worth tracing.
- **`State Ownership`** — which systems own which state, how state is shared or accessed across boundaries. Include when shared state is a significant source of complexity.
- **`Reading Guide`** — which system files cluster together by common task type, suggested reading orders for common questions. Include when the project has enough system files that navigation guidance saves time.

### Structure Rules

- `Repository Structure` must use a text tree in a fenced code block.
- Important directories and files should have short one-line descriptions.
- Depth should be meaningful rather than shallow.
- Structural sections may include a supporting table or diagram when it clarifies the same information better than bullets alone.
- Keep `architecture.md` structural rather than status-heavy; detailed subsystem reality belongs in `systems/`.

## 2. `systems/<topic>.md`

### Role

A system document is the canonical home for one stable subsystem or feature area.

It should capture:

- what the subsystem is for,
- what it owns,
- how it works now,
- where it interfaces with other systems,
- what is risky, partial, missing, or historically important.

### Naming Rules

- Place files in `systems/`.
- Use lowercase hyphenated names.
- Prefer short stable topic names.
- Name by subsystem or feature, not by milestone or chronology.
- Keep the most distinguishing topic word early when possible for better IDE scanning.

Examples:

- `systems/analytics.md`
- `systems/agent-observations.md`
- `systems/environment.md`

Avoid:

- `systems/phase-2.md`
- `systems/recent-updates.md`
- `systems/misc.md`

### Topic Naming Guidance

Prefer the shortest stable topic name that remains clear inside the repository.

Good:

- `systems/agent-observations.md`
- `systems/environment.md`
- `systems/replay.md`
- `systems/telemetry.md`

Keep the longer name only when:

- the shorter name would collide with another real subsystem,
- the broader shorter word is ambiguous,
- or the longer name is already well established and renaming would create needless churn.

### Required Sections

Use this section order:

1. `Scope / Purpose`
2. `Boundaries / Ownership`
3. `Current Implemented Reality`
4. `Key Interfaces / Data Flow`
5. `Implemented Outputs / Artifacts`
6. `Known Issues / Active Risks` — document downstream impact, not just local risk. When a known issue could affect systems that depend on this one, state what would break and how. A risk entry that says "cache invalidation is unreliable" is less useful than one that says "cache invalidation is unreliable — downstream analytics will serve stale aggregates until the next full refresh."
7. `Partial / In Progress`
8. `Planned / Missing / Likely Changes`
9. `Durable Notes / Discarded Approaches`
10. `Obsolete / No Longer Relevant`

### Writing Rules

- Use bullets for digestible current-state statements and takeaways.
- Add tables when inventories, interfaces, or comparisons are dense enough that bullets alone become noisy.
- Add a simple flow or diagram only when it materially clarifies relationships.
- Describe reality rather than aspiration in the current section.
- Tie future work to the subsystem itself rather than to a project timeline.
- Put durable past lessons in the durable-notes section rather than in diary format.
- Cross-reference other system files at interface points. When system A sends data to system B, both system files should reference each other at the relevant boundary — this keeps navigation reliable as the project grows, because an engineer reading either file can find the other side of the interface.
- When a system owns a significant data structure — a schema, config format, API contract, message format, or state shape — document its structure explicitly: fields, types, constraints, and why it is shaped that way. Include this when the data structure is important enough that engineers need to understand it to work with the system correctly.

## 3. `notes.md`

### Role

This is the compact index and summary of all project notes in `notes/`. It is always read on startup alongside `architecture.md` to give the agent immediate access to project preferences, design rationale, and durable lessons without reading every individual note file.

### Required Qualities

- Short — one bullet per note file, summarising the key takeaway in a single line.
- Always up to date — when a note file is created, updated, or deleted, this index must reflect the change.
- Navigational — each entry should point to its detail file for full context.

### Format

```markdown
# Notes

- [caching-strategy](notes/caching-strategy.md) — LRU with 5-minute TTL; invalidate on write
- [deployment-model](notes/deployment-model.md) — single-region for now; multi-region deferred until latency data justifies it
- [api-versioning](notes/api-versioning.md) — URL-based versioning; no breaking changes within a major version
```

Keep entries concise — one line each. The detail lives in the note files, not in the index.

## 4. `notes/<topic>.md`

### Role

Note files capture evolving project knowledge that the agent needs to remember across sessions. This includes:

- design rationale and the reasoning behind choices,
- project preferences and guiding principles,
- trial-and-error outcomes — what was tried, what failed, and why,
- constraints and trade-offs that are not obvious from the code,
- cross-cutting observations that do not belong to a single system file.

Notes are **topical**, not chronological. Each file covers one topic and evolves as the project evolves. When the project's understanding of a topic changes, the note is updated in place — the old version is not preserved (git has the history).

Notes are distinct from system files: a system file documents *what is implemented and how*. A note documents *why things are the way they are and what preferences or lessons guide future work*.

### Naming Rules

- Place files in `notes/`.
- Use lowercase hyphenated names.
- Name by topic, not by date or session.

Examples:

- `notes/reward-system.md`
- `notes/gameplay-goals.md`
- `notes/training-strategy.md`

Avoid:

- `notes/session-3.md`
- `notes/march-changes.md`
- `notes/misc.md`

### Suggested Sections

Adapt to the content, but favour:

1. `Current Understanding` — what is currently true about this topic
2. `Rationale` — why the current approach was chosen
3. `What Was Tried` — previous approaches and why they were abandoned (only when relevant to future decisions)
4. `Guiding Principles` — preferences or constraints that should guide future work on this topic

Not every note needs all sections. A note that captures a single guiding principle ("entertainment value over optimal performance") may be just a few lines. A note about a complex design trade-off (reward shaping) may be substantial.

### Note Types

These are suggested patterns to guide capture, not a taxonomy the agent must pick from. A note can blend multiple types or follow none of them. The goal is to make it easier to recognise what kind of knowledge is being captured and what sections would serve it well.

- **Decision notes** — what was decided, what alternatives were considered, what constraints shaped the choice, and what would change the decision. Useful when a decision is non-obvious and future sessions may question it.
- **Discovery notes** — non-obvious things learned during work: surprising behaviour, hidden dependencies, undocumented interactions. Useful when the discovery would be expensive to re-derive.
- **Convention notes** — recurring patterns, idioms, and conventions used across the codebase that are not enforced by tooling. Useful when the project has implicit standards that new contributors (or new agent sessions) would not discover from the code alone.
- **Constraint notes** — external requirements, platform limitations, or organisational rules that shape decisions but are not visible in the repository. Useful when a constraint would otherwise appear arbitrary.

### Cross-Referencing

Notes should reference related system files, and system files should reference relevant notes. This creates a navigable web rather than two parallel collections. When a note captures the rationale behind a system's design, link the note from the system file's durable-notes section. When a system file documents behaviour that a note explains the reasoning for, link the system file from the note.

### Lifecycle

- Notes are living documents — they evolve, they do not accumulate.
- When a note becomes irrelevant because the project moved past the topic entirely, delete it and remove its index entry.
- When two notes converge on the same topic, merge them.
- Do not let notes become stale — a stale note is worse than no note, because it actively misleads.

## 5. `plans/<topic>.md`

### Role

This is a temporary execution file for immediate implementation work.

It is not part of the stable long-term memory model. It exists only when explicitly requested or clearly needed for active execution.

### Naming Rules

- Place files in `plans/`.
- Use a short stable descriptor.

### Required Sections

Use this section order:

1. `Header`
2. `Implementation Structure`
3. `Algorithm / System Sections`
4. `Integration Points`
5. `Debugging / Verification`
6. `Completion Criteria`

### Lifecycle Rules

- Create only when there is a concrete active execution scope.
- Multiple active plans are allowed when different systems have independent active work.
- Keep each plan aligned with current work while active.
- Tick checkboxes and update status within plan files as implementation progresses — do not leave completed items unchecked.
- Remove or archive a plan once all its completion criteria are met.
- Do not let old implementation plans accumulate indefinitely.

## 6. `references/<topic>.md`

### Role

Reference files hold durable supporting material that informs implementation but is not itself the canonical implementation-state document.

Examples:

- research comparisons,
- project-grounded research papers that relate external findings back to the repository,
- external API or protocol summaries,
- schema notes,
- benchmark interpretation notes,
- migration references.

Reference material is durable, but not static. If a research paper includes project-specific gap analysis, implementation comparisons, or recommendations tied to current repository reality, upkeep may need to revise it when the repository changes.

### Naming Rules

- Place files in `references/`.
- Use lowercase hyphenated names.
- Name by subject matter rather than chronology.

### Suggested Sections

Adapt structure to the reference type, but favour:

1. `Scope / Purpose`
2. `Current Relevance`
3. `Content`
4. `Implications for the Repository`
5. `Open Constraints / Follow-Up Questions` when needed

### Research-Shaped References

Some reference artefacts will be deeper project-grounded research papers or topic folders following a research-paper structure with topic folders and analytical sections.

These may use stronger section patterns such as:

1. `Scope / Purpose`
2. `Current Project Relevance`
3. `Research Signal`
4. `Current State Vs Research-Backed Expectations`
5. `Gap Analysis`
6. `Recommended Priority Order`
7. `Relationship To Existing Context`

They may also appear as topic folders with an `overview.md` plus supporting papers.

When these shapes are justified, preserve them. Do not flatten them into the generic reference pattern unless the broader research structure no longer improves navigation, ownership, or upkeep.

### Upkeep Rules

- Preserve a reference artefact when it still has a coherent topic and its project-specific claims remain substantially accurate.
- Update a reference artefact when implementation reality has changed enough to stale its repository-specific analysis.
- Merge or condense a research folder when multiple artefacts now act as one stable topic and the broader split no longer improves navigation or upkeep.
- Do not collapse a reference folder just because it is possible. Only condense when the result remains rich, accurate, and clearly more maintainable than the expanded shape.

## System File Maturity Indicators

This is an optional, lightweight convention for projects with many system files at different levels of completeness. When present, it helps the agent (and human readers) quickly judge how much to trust a system file's coverage without reading the whole document.

Three levels:

- **stub** — minimal coverage, created as a placeholder or during initial discovery. Enough to establish the file's scope but not enough to rely on for implementation decisions.
- **working** — covers the basics: scope, boundaries, current reality, key interfaces. Sufficient for most day-to-day work but may have thin sections or missing edge cases.
- **comprehensive** — full depth across all relevant sections. Reflects sustained investment in documenting the subsystem.

The marker can appear in the system file's header (e.g., `*Maturity: working*`) or in `architecture.md`'s subsystem table as an additional column. Either location works — pick one per project and stay consistent.

This convention is not required. Consider adopting it when the project has enough system files that a quick maturity signal saves time deciding which files to trust and which to expand.

## Disallowed Default File Types

Do not create these as part of the normal model:

- `HISTORY.md`
- `CHANGELOG.md`
- `MILESTONES.md`
- `MISC.md`
- `OPEN_QUESTIONS.md`
- `RECENT_CHANGES.md`

If information from those categories is truly needed, attach it to the relevant canonical system doc or to a topical note file instead.

Note: `notes.md` (the index) and `notes/<topic>.md` (topical note files) are canonical file types, not catch-all dumping grounds. The disallowed pattern is a single undifferentiated notes file with no topical structure — not the structured notes system.
