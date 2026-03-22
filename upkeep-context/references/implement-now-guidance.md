# Implement-Now Guidance

This reference defines how to write a high-quality `plans/<topic>.md` file.

These files are temporary execution guides. They exist to turn a chosen task into a precise, teaching-oriented implementation plan that removes ambiguity about where changes go, how the logic should work, and how progress should be verified.

## When To Create One

Create a file in `plans/` only when:

- the user explicitly wants an execution plan,
- the next implementation scope is concrete and bounded,
- the work benefits from a temporary high-detail guide,
- or a subsystem is complex enough that execution details would otherwise be easy to lose.

Do not create one for vague brainstorming.

Do not create one just because a task exists.

## What It Is For

A strong `implement-now` file should:

- clarify exact implementation scope,
- map modules and responsibilities,
- list the affected surfaces,
- teach the intended logic in procedural English,
- define checkpoints and verification criteria,
- stay aligned with reality while the work is active.

It is not:

- a generic design document,
- a changelog,
- a scratchpad,
- production code,
- or a permanent system-memory file.

## Required Sections

Use this section order:

1. `Header`
2. `Implementation Structure`
3. `Algorithm / System Sections`
4. `Integration Points`
5. `Debugging / Verification`
6. `Completion Criteria`

## Section Guidance

### 1. Header

Must include:

- status,
- scope,
- exit rule.

This section should make it obvious when the file is complete and ready to be removed or archived.

### 2. Implementation Structure

This section removes ambiguity about where things go.

It should include:

- expected modules/files affected,
- responsibility boundaries,
- function inventory for major tasks,
- a short wiring summary.

For each function or responsibility entry, capture:

- name,
- location,
- inputs/outputs in English,
- whether it is a helper or orchestrator,
- integration point or caller.

### 3. Algorithm / System Sections

Create one subsection per major task.

Each subsection must include, in this order:

- short explanation paragraphs,
- bounded discovery steps,
- implementation playbook,
- stop-and-verify checkpoints,
- invariants / sanity checks,
- minimal explicit test requirements.

The explanation paragraphs should come first. They teach the concept and make the procedural checklist understandable.

### 4. Integration Points

Define:

- where the new work plugs into the existing system,
- execution order,
- lifecycle placement,
- pre-conditions,
- post-conditions.

This section is where “what else might be affected” becomes explicit.

### 5. Debugging / Verification

Capture:

- required logs or assertions,
- manual inspection steps,
- focused runtime signals to check,
- common failure patterns specific to the task.

### 6. Completion Criteria

Include:

- functional correctness,
- integration correctness,
- tests passing,
- context updates completed,
- file removal or archival condition.

## Writing Rules

- The file is an implementation teaching guide, not a vague plan.
- Prefer procedural English over code-shaped pseudocode.
- Avoid bullets that just say “implement X” without explaining how.
- Explanatory paragraphs should stay short but must come before checklists.
- All actionable items should be checkboxes.
- Separate primitives from orchestration.
- Name the affected interfaces and invariants explicitly.
- Include a recommended default when a choice is needed, plus one alternative only if useful.

## Quality Bar

A good `implement-now` file lets a strong engineer answer:

- what exactly is changing,
- where each part belongs,
- how the logic should work,
- how to know it is correct,
- and what neighbouring systems are at risk.

If the file does not reduce ambiguity materially, it is too weak.

## Anti-Patterns

Avoid:

- vague verbs with no procedure,
- giant code dumps,
- restating the entire architecture,
- open-ended brainstorming lists,
- multiple unrelated tasks in one file,
- leaving stale completed plan files in `context/`.
