---
name: implement-tests
description: Implements a test plan end-to-end. Reads the plan, executes test groups in dependency waves, spawning parallel implementors. No code review. Run after /plan-tests. Takes a test plan name as argument.
user_invocable: true
---

# Implement Tests

You are orchestrating the implementation of a test plan. Read the plan, form dependency waves, spawn implementor agents in parallel, and run the results.

## Philosophy: Failing Tests Are Valuable

**Do not treat test failures as problems to fix.** A failing test is a discovery — it reveals a bug, a missing edge case, an undocumented assumption, or a limitation in the current code. These are exactly the things tests exist to find.

Write tests that correctly assert the expected behavior from the plan. If the code doesn't meet that expectation, the test *should* fail. Do not weaken assertions, skip tests, or adjust expectations to make tests pass. The goal is an honest picture of the codebase, not a green dashboard.

## Setup

The argument is the test plan name (kebab-case). The test plan directory is `docs/tests/$ARGUMENTS/`.

1. **Create an isolated worktree** using the `EnterWorktree` tool with the test plan name as the worktree name (e.g., name: `$ARGUMENTS`). All implementation work happens in this worktree.

2. Verify this file exists:
   - `docs/tests/$ARGUMENTS/plan.md`

   If missing, tell the user to run `/plan-tests $ARGUMENTS` first.

3. Read `docs/tests/$ARGUMENTS/plan.md` to understand the test groups and dependency graph.

4. **Check for prior progress.** If `docs/tests/$ARGUMENTS/progress.md` exists:
   - Read it to determine which waves are already complete.
   - Resume from the first incomplete wave — skip all completed waves entirely.
   - Report to user: "Resuming from wave N. Previously completed: <list>."

5. If no `progress.md` exists, create it:
   ```markdown
   # Progress: $ARGUMENTS

   ## Completed Steps
   ```

## Phase 1: Implementation Waves

Read the task dependency graph from `plan.md`. Execute test groups in dependency order:

### For each wave of parallelizable groups:

Identify groups whose dependencies are all satisfied. For each group in the wave, spawn an **implementor** agent:
- Tell it to **write tests** (not source code) — it is implementing a test group from a test plan
- Tell it which group (ID + description + test cases) to implement
- Tell it to read:
  - `docs/tests/$ARGUMENTS/plan.md` (focus on its group — conventions, mocking strategy, test cases)
  - The source files under test (listed in the group)
  - Existing test files in the codebase (for pattern matching)
  - `CLAUDE.md` for project conventions
- Tell it the key rules:
  - Follow existing test patterns exactly (imports, setup, naming, structure)
  - Test the public contract, not internal implementation details
  - Use descriptive test names that explain the expected behavior
  - Mock only what the plan says to mock
  - Write assertions for the **correct expected behavior** as defined in the plan — do NOT weaken or skip assertions to make tests pass. A failing test that correctly asserts the right behavior is a valuable finding, not an error to fix.
- Tell it to append any deviations or decisions to `docs/tests/$ARGUMENTS/decisions.md`

**Spawn parallel groups simultaneously** using multiple Agent tool calls in one message.

After each wave completes:
1. Run `npm test` to check results
2. Stage all changes and create a checkpoint commit: `wip: $ARGUMENTS tests — wave N (G1, G2)`
3. Update `progress.md` — append: `- Wave N: G1, G2 (X tests, Y passing, Z failing)`
4. Report to user: "Wave N complete. X new tests. Y passing, Z failing."

Continue waves until all groups are complete.

## Phase 2: Verification

After all waves complete:
1. Run the full test suite: `npm test`
2. Run typecheck: `npx tsc --noEmit`
3. Report final status to user: total new tests, passing count, failing count

## Phase 3: Commit

1. Stage all remaining changes.
2. Create a final commit:
   ```
   test: $ARGUMENTS — <one-line description of what was tested>
   ```
   Derive the description from the plan's Target section.
3. Update `progress.md` — append: `- Final commit`

## Completion

After the commit:
1. Present a summary to the user:
   - How many test files created
   - How many tests total
   - Pass/fail status
   - Any test groups that had issues (from decisions.md)
2. Remind the user that implementation was done in a worktree. They can review with `git diff` and merge when ready.
