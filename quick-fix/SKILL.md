---
name: quick-fix
description: Interactive triage for bugs, small fixes, and minor improvements. Diagnoses scope — implements directly if small, escalates to /new-feature or /new-refactor if scope creep is detected.
user_invocable: true
---

# Quick Fix

You are now in **quick-fix triage mode**. Your role is to help the user diagnose a bug, small fix, or minor improvement — and either implement it directly or escalate it to the right pipeline.

## Before you begin

As soon as the user describes their problem, **build context before asking a single question**:

1. Read `docs/VISION.md` to understand the project's purpose and design pillars.
2. Read `docs/features/INDEX.md` and `docs/refactors/INDEX.md` to see which recent work touches the systems the user is describing.
3. Check the relevant system memories from `MEMORY.md` (e.g., if the user mentions the turn pipeline, read `project_turn_pipeline.md`).
4. If the indices list features or refactors that overlap, read their `summary.md` and `decisions.md` to understand what already exists and what was deferred.
5. **Read the actual code** — use Glob, Grep, and Read to examine the area in question. You cannot diagnose a problem without reading the code.

Use this context to ground the conversation — reference what the code currently does, what recent changes happened, and what constraints exist.

## Your approach

1. **Listen first** — let the user describe the problem, bug, or improvement
2. **Build context** — immediately look up relevant systems, features, and code (see above)
3. **Diagnose concretely** — identify the specific files, functions, and lines involved. Show the user what you found.
4. **Ask focused questions** — one or two at a time:
   - "I see the issue is in X — is this the behavior you're seeing?"
   - "This touches Y and Z — do you also want to address Z or just Y?"
   - "There's a related edge case with W — should we handle it now or is it out of scope?"
5. **Assess scope continuously** — as the picture comes into focus, track what's growing

## Scope assessment

A fix is **quick** when ALL of these hold:

- Touches **5 or fewer files** (not counting test files)
- Requires **no new abstractions** (no new modules, services, or patterns)
- Requires **no schema/migration changes**
- Requires **no new LLM integration** (no new prompts, tools, or agent loops)
- Requires **no changes to core pipeline flow** (turn lifecycle, orchestration, streaming)
- The fix is **obvious and well-understood** after diagnosis — no open design questions remain
- No conflict with vision design pillars

A fix is **scope creep** when ANY of these hold:

- Touches **6+ files** across multiple systems
- Requires **new abstractions, services, or modules**
- Requires **schema changes or migrations**
- Requires **new LLM prompts or agent behavior**
- Changes **core pipeline flow**
- Has **unresolved design questions** that need interactive exploration
- Would benefit from **architectural planning** to get right
- Conflicts with or extends the vision in ways that need discussion

## Conversation style

- Be technical and direct
- Show code snippets when discussing problems — "line 47 of X does Y, which causes Z"
- Keep the conversation short and focused — this is triage, not a design session
- If you're confident about the fix after reading the code, propose it immediately — don't interrogate the user when the answer is clear

## Outcome A: Quick fix — implement directly

When you and the user agree the fix is small and well-understood:

1. **Summarize the plan** — list the specific changes to make, file by file. Get user confirmation.
2. **Create an isolated worktree** using the `EnterWorktree` tool with a descriptive name (e.g., `fix-npc-greeting-crash`).
3. **Spawn implementor agents** — one per independent change. Parallelize where possible.
   - Each agent gets:
     - A clear task description (what to change, in which file, why)
     - The relevant file paths to read
     - Instructions to run tests after their change
   - For dependent changes, execute in waves (like the implement-feature pipeline).
4. After all agents complete, **run the full test suite**: `npm test`
5. If tests fail, make ONE attempt to fix — spawn an implementor focused on the failures.
6. If tests pass, **run type-check**: `npx tsc --noEmit`
7. Stage and commit with message:
   ```
   fix: <concise description of what was fixed>
   ```
8. Present a summary to the user:
   - What was changed and why
   - Test status
   - Any edge cases to watch for
9. Remind the user the fix was done in a worktree — they can review with `git diff` and merge when ready.

## Outcome B: Scope creep — escalate

When the fix is growing beyond quick-fix territory:

1. **Tell the user directly** — explain what's pushing it out of scope:
   - "This is touching X, Y, and Z systems — that's beyond a quick fix"
   - "There are open design questions about how A should interact with B"
   - "This needs a schema change which requires migration planning"
2. **Determine the type** — is this a **feature** (new capability) or a **refactor** (structural improvement)?
   - Bug fixes that require structural changes → refactor
   - New behaviors or capabilities → feature
   - If unclear, ask the user
3. **Ask for a kebab-case name** (e.g., `fix-npc-scheduling`, `item-durability`)
4. **Create the directory and task description**:
   - For features: `docs/features/<name>/task-description.md`
   - For refactors: `docs/refactors/<name>/task-description.md`

   Write the task description with this structure:

   ```markdown
   # Task: <name>

   ## Origin
   Quick-fix triage on <today's date>. Escalated because: <reason>.

   ## Problem Statement
   <what the user originally described — the bug, issue, or improvement>

   ## Diagnosis
   <what you found during triage — specific files, functions, root cause analysis>

   ## Affected Systems
   | System | How It's Affected |
   |--------|-------------------|
   | <system> | <description> |

   ## Scope Indicators
   - Files involved: <list>
   - Schema changes needed: yes/no
   - New abstractions needed: yes/no
   - Open design questions: <list>

   ## Initial Direction
   <any insights from triage that should inform the design — approaches considered, constraints discovered, edge cases identified>
   ```

5. **Tell the user the next step**:
   - For features: "Run `/new-feature <name>` to design this properly. The task description I wrote captures our triage findings."
   - For refactors: "Run `/new-refactor <name>` to scope this properly. The task description I wrote captures our triage findings."
