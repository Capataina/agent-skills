# Document Model

This reference defines the canonical file types, their roles, their required section templates, and how canonical ownership should be preserved even when a document uses multiple presentation formats.

## Canonical Context Structure

Default to this structure:

```text
context/
├── architecture.md
├── systems/
├── plans/
├── decisions/
└── references/
```

Only `architecture.md` and `systems/` are universally required.

The other folders are canonical roles, not mandatory filler targets. Create files in them only when their role is justified.

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
6. `Known Issues / Active Risks`
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

## 3. `plans/<topic>.md`

### Role

This is a temporary execution file for immediate implementation work.

It is not part of the stable long-term memory model. It exists only when explicitly requested or clearly needed for active execution.

### Naming Rules

- Place files in `plans/`.
- Use a short stable descriptor.
- Keep only one active implementation plan by default.

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
- Keep it aligned with current work while active.
- Remove or archive it once complete.
- Do not let old implementation plans accumulate indefinitely.

## 4. `decisions/<topic>.md`

### Role

Decision files capture durable cross-cutting project decisions that are too important or too broad to bury inside a single system file.

Examples:

- baseline algorithm choice,
- persistence model choice,
- plugin architecture choice,
- deployment model choice,
- versioning or compatibility strategy.

### Naming Rules

- Place files in `decisions/`.
- Use lowercase hyphenated names.
- Name by decision topic rather than by date.

### Suggested Sections

Use this order when a durable decision file is justified:

1. `Scope / Purpose`
2. `Decision`
3. `Context`
4. `Options Considered`
5. `Trade-Offs`
6. `Consequences / Follow-On Constraints`
7. `Revisit Conditions`

## 5. `references/<topic>.md`

### Role

Reference files hold durable supporting material that informs implementation but is not itself the canonical implementation-state document.

Examples:

- research comparisons,
- external API or protocol summaries,
- schema notes,
- benchmark interpretation notes,
- migration references.

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

## Disallowed Default File Types

Do not create these as part of the normal model:

- `HISTORY.md`
- `CHANGELOG.md`
- `MILESTONES.md`
- `NOTES.md`
- `MISC.md`
- `OPEN_QUESTIONS.md`
- `RECENT_CHANGES.md`

If information from those categories is truly needed, attach it to the relevant canonical system doc instead.
