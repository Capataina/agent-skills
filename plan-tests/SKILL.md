---
name: plan-tests
description: Interactive session to design a test plan for existing code. Explores the codebase, identifies test boundaries, and produces a structured plan with test groups, dependency waves, and mocking strategy. Takes a name as argument.
user_invocable: true
---

# Plan Tests

You are now in **test planning mode**. Your role is to collaboratively design a comprehensive test plan for existing code — exploring the codebase, understanding behaviors, and defining what tests to write.

## Core Principles

### Test Behavior, Not Implementation

Tests should verify what the code **does**, not how it does it internally. Test the public contract — inputs, outputs, side effects, error cases. A good test survives a refactor that preserves behavior.

### Pragmatic Coverage

Not every line needs a test. Focus testing effort where it matters most:
- **Critical paths** — business logic, state transitions, data integrity
- **Boundary conditions** — edge cases, error handling, empty/null/overflow
- **Integration seams** — where systems connect and contracts must hold
- **Bug-prone areas** — complex conditionals, stateful logic, concurrency

Skip trivial getters, simple pass-through functions, and framework boilerplate.

### Match Existing Patterns

Study how tests are already written in this codebase and follow those conventions exactly. Consistency matters more than any individual best practice.

## Setup

The argument is the test plan name (kebab-case). The test plan directory is `docs/tests/$ARGUMENTS/`.

1. Create the directory `docs/tests/$ARGUMENTS/` if it doesn't exist.
2. Read `CLAUDE.md` for project conventions, test tooling, and rules.
3. Create `docs/tests/$ARGUMENTS/decisions.md`:
   ```markdown
   # Decision Log: $ARGUMENTS

   Decisions and rationale recorded during test planning.

   ---
   ```

## Phase 1: Understand the Target

Ask the user what they want to test if it's not clear from the argument name. Clarify:
- **Scope** — specific files, a service, a system, or a broader area?
- **Motivation** — backfilling coverage? Locking behavior before a refactor? Confidence for a risky area?
- **Depth** — thorough coverage or just the critical paths?

## Phase 2: Codebase Exploration (interactive)

### Step 1: Explore the target code

Use Glob, Grep, and Read to deeply understand:
- **The code under test** — its public API surface, data flow, state transitions
- **Existing tests** — what's already covered, what patterns are used, what's missing
- **Dependencies** — what the code calls, what needs mocking vs real usage
- **Integration points** — where this code connects to other systems

Share findings as you go. Ask questions:
- "This function has 3 code paths — should we test all of them or just the happy path?"
- "I see this service depends on LLM calls — mock those, right?"
- "There are no existing tests for X — is that intentional or a gap?"

### Step 2: Identify test boundaries

Determine:
- **What to test directly** — the public contract of the target code
- **What to mock** — external dependencies, LLM calls, etc. (but NOT the database per project rules)
- **What to test via integration** — behaviors that only manifest when systems interact
- **What's already covered** — existing tests that don't need duplication

### Step 3: Design test groups

Work with the user to define logical test groups. For each group:
- What behavior does it verify?
- Which source files does it exercise?
- What are the specific test cases?
- Does it depend on any other group (shared fixtures, setup, etc.)?

### Step 4: Converge

When you and the user are aligned, ask: **"Ready for me to write this up?"**

## Save the Test Plan

When the user confirms, write `docs/tests/$ARGUMENTS/plan.md`:

```markdown
# Test Plan: <name>

## Target
<what code is being tested and why>

## Scope
- **In scope**: <what will be tested>
- **Out of scope**: <what will NOT be tested and why>

## Existing Coverage
- <what tests already exist for this area>
- <gaps identified>

## Conventions
- **Test framework**: <from CLAUDE.md>
- **File naming**: <pattern, e.g., `*.test.ts` colocated>
- **Patterns to follow**: <reference existing test files>

## Mocking Strategy
- **Mock**: <what to mock and how>
- **Real**: <what to use real implementations for>

## Test Groups

### Task Dependency Graph
\`\`\`mermaid
graph TD
  G1[G1: description] --> G3[G3: description]
  G2[G2: description] --> G3
  G3 --> G4[G4: description]
\`\`\`

### G1: <title>
- **File**: `path/to/test-file.test.ts`
- **Tests**: <source files exercised>
- **Depends on**: none
- **Parallel**: yes
- **Test cases**:
  - <describe block> → <test case>: <what it verifies>
  - <describe block> → <test case>: <what it verifies>
  - ...

### G2: <title>
...

## Decisions
- <key decisions made during the session with rationale>
```

Also append key decisions to `docs/tests/$ARGUMENTS/decisions.md`.

Then confirm and remind the user to run `/implement-tests $ARGUMENTS` when ready.
