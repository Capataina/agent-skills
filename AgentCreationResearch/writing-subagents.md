# How to Write Effective Subagent Configurations

A comprehensive reference for designing subagent prompts, orchestrating multi-agent workflows, and avoiding the known failure modes of parallel and delegated agent work.

## Table of Contents

1. [When to Use Subagents](#1-when-to-use-subagents)
2. [The Three Coordination Models](#2-the-three-coordination-models)
3. [Subagent Instruction Writing](#3-subagent-instruction-writing)
4. [Parallelisation Strategies](#4-parallelisation-strategies)
5. [Worktree Isolation](#5-worktree-isolation)
6. [Context Management](#6-context-management)
7. [Coordination and Communication](#7-coordination-and-communication)
8. [Error Handling and Recovery](#8-error-handling-and-recovery)
9. [Anti-Patterns and Known Failure Modes](#9-anti-patterns-and-known-failure-modes)
10. [Quality Verification for Subagent Configurations](#10-quality-verification-for-subagent-configurations)
11. [Practical Guidelines](#11-practical-guidelines)
12. [Sources](#12-sources)

---

## 1. When to Use Subagents

### Use the Main Conversation When

- The task needs frequent back-and-forth or iterative refinement with the user.
- Multiple phases share significant context (planning, implementation, testing).
- You are making a quick, targeted change.
- Latency matters — subagents start fresh and need time to gather context.

### Use Subagents When

- The task produces verbose output you do not need in your main context (research, exploration, analysis).
- You want to enforce specific tool restrictions or permissions.
- The work is self-contained and can return a summary.
- You want to protect your main context window from token-heavy exploration.

### Use Agent Teams When

- Teammates need to share findings, challenge each other, and coordinate independently.
- Work requires discussion and collaboration between workers.
- Complex research with competing hypotheses benefits from parallel exploration.

### The Core Insight

Subagents exist primarily for **context management**, not for role-playing. The primary use case is delegating search, summarisation, or analysis work to fresh context windows, preventing research clutter from consuming parent agent bandwidth. Each subagent explores extensively (tens of thousands of tokens) but returns only condensed summaries (1,000–2,000 tokens).

---

## 2. The Three Coordination Models

### Solo Agent

A single autonomous actor handles tasks end-to-end. It reads code, makes updates, runs tests, and completes work without delegation.

**Best for:** Most tasks. Start here and only add complexity when genuinely needed.

### Orchestrated Subagents

A primary agent functions as tech lead, assigning specialised work to subordinate agents. The main agent owns the flow, order, and coordination. Subagents work either in parallel or sequentially, with the orchestrating agent collecting and integrating results.

**Best for:** Tasks with clearly separable, independent subtasks — parallel code review, multi-file analysis, independent research queries.

### Collaborative Teams

Multiple independent agents operate without strict hierarchical control, negotiating and sharing perspectives. No single agent is the boss. They exchange information, provide feedback, and collaborate.

**Best for:** Complex investigations where competing hypotheses benefit from debate and cross-checking.

### The Hierarchy Principle

If you need many subagents, do not spawn them all from the orchestrator. Use hierarchical delegation: orchestrator → feature leads → specialists. The parent orchestrator only talks to 2–3 agents, keeping its context clean. Each feature lead then spawns its own specialists. This prevents context fragmentation at the top level.

---

## 3. Subagent Instruction Writing

### The Invocation Quality Problem

Most subagent failures are invocation failures, not execution failures. Poor inputs produce poor outputs regardless of agent capability.

**Bad:** "Fix authentication"

**Good:** "Fix OAuth redirect loop where successful login redirects to /login instead of /dashboard. Reference the auth middleware in src/lib/auth.ts."

### Complete Invocations Include

- Comprehensive context and scope.
- Explicit instructions with specifics.
- Relevant file references.
- Clear success criteria.
- What the subagent should return to the parent.

### System Prompt vs Task Prompt

The subagent's markdown body (its definition file) becomes its system prompt. The specific task goes in the invocation prompt. Keep them separate:

- **System prompt (definition file):** Role, scope, tool policy, quality standards.
- **Task prompt (invocation):** Specific work, file references, success criteria.

### What Subagents Inherit and What They Do Not

**Subagents receive:** Their custom system prompt, basic environment details (working directory), project context (CLAUDE.md, explicitly listed skills).

**Subagents do NOT receive:** The parent's conversation history, the full Claude Code system prompt, skills from the parent (must be listed explicitly).

This means the invocation prompt must be self-contained. The subagent has no memory of what you discussed in the main conversation.

### Writing the Definition File Body

The subagent's markdown body becomes its system prompt — its permanent identity and behavioural framework. This is distinct from the task-specific invocation prompt. The body should answer: "Who is this agent, what is it good at, and how should it approach work?"

**Keep it focused.** A subagent definition file should be shorter than a personality file because the subagent has a narrower scope. A code reviewer does not need startup routines, session modes, or documentation upkeep instructions. It needs: role, quality standards, output format, and constraints.

**Define the role concisely.** One paragraph establishing identity: "You are a code reviewer. When invoked, analyse the code for quality, security, and best practices. Provide specific, actionable feedback with file paths and line numbers."

**Establish output expectations.** What should the subagent return to the parent? Be explicit: "Return a structured summary of findings, grouped by severity. Include the file path, line number, issue description, and suggested fix for each finding. Keep the total response under 2,000 tokens."

**Set scope boundaries.** What should the subagent touch? What is off-limits? "Focus on the files specified in the invocation. Do not explore unrelated parts of the codebase. Do not make changes — analysis only."

**Include quality standards relevant to the role.** A research subagent needs standards about source quality and grounding. A code modification subagent needs standards about testing and verification. Only include standards that are relevant to what this subagent does.

### Calibrating Context in Invocations

How much context to include in the invocation prompt is a balancing act:

**Too little context:** The subagent wastes turns rediscovering what the parent already knows. It may make decisions that are wrong given information the parent has. It may ask clarifying questions that the parent could have pre-empted.

**Too much context:** Chroma's research shows irrelevant context degrades accuracy by up to 30%. Worse, structured distractors (well-written but irrelevant paragraphs) are more harmful than random noise. Including the parent's entire conversation history "for context" actually makes the subagent perform worse.

**The right amount:** Include exactly what the subagent needs to do its job — no more, no less. For a code modification subagent: the specific files to modify, the change to make, the interfaces that must be preserved, and the success criteria. For a research subagent: the specific question, what has already been explored, and what kind of answer the parent needs.

**Use file references, not file contents.** Instead of pasting 500 lines of code into the invocation, say "Read src/auth/middleware.ts, focusing on the redirect logic at lines 45-80." The subagent reads the file itself in its own context, keeping the invocation prompt lean.

### Scoping for Focused Subagents

The narrower the subagent's scope, the better it performs. Broad subagents ("fix the authentication system") produce worse results than focused ones ("fix the OAuth redirect loop where successful login redirects to /login instead of /dashboard") because:

1. Broad scope means the subagent must explore more, consuming context on exploration rather than execution.
2. Broad scope means more ambiguity about what "done" looks like.
3. Broad scope means more risk of the subagent going off-track into tangential work.

When a task is naturally broad, decompose it into focused subtasks and spawn one subagent per subtask, rather than one subagent for the whole thing.

### Configuration Options

Key frontmatter fields for subagent definition files:

| Field | Purpose |
|-------|---------|
| `tools` | Allowlist of available tools |
| `disallowedTools` | Blocklist of denied tools |
| `model` | Model override (e.g., use Sonnet for focused tasks) |
| `maxTurns` | Safety limit on interaction count |
| `memory` | Persistence scope (user, project, local) |
| `isolation` | Worktree isolation mode |
| `skills` | Skills to preload into subagent context |

### Choosing the Right Model

Not every subagent needs the most powerful model. Multi-model routing significantly reduces cost without sacrificing quality:

- **Opus (most powerful):** Planning, coordination, complex reasoning, architectural decisions. Use for the orchestrator and for subagents doing work that requires deep understanding.
- **Sonnet (balanced):** Implementation, code modification, focused analysis. Use for well-scoped subagents where the task is clear and the agent does not need to make high-level judgment calls.
- **Haiku (fastest, cheapest):** Exploration, file discovery, simple searches. Use for read-only subagents that survey the codebase and return summaries.

The principle: use the cheapest model that can reliably do the job. Spending Opus tokens on a grep-and-summarise task is wasteful. Spending Haiku tokens on an architectural decision is risky.

---

## 4. Parallelisation Strategies

### When Parallelisation Works

ALL conditions must apply:

- 3+ unrelated tasks or independent domains.
- No shared state between tasks.
- Clear file boundaries with zero overlap.

### When to Stay Sequential

ANY condition applies:

- Task dependencies exist.
- Shared files or state.
- Unclear scope requiring pre-work clarification.

### Domain-Based Parallelism

Structure concurrent work by domain ownership. Each agent owns their domain with no file overlap:

- Frontend agent: React components, UI state, forms.
- Backend agent: API routes, server actions, business logic.
- Data agent: Schema, migrations, queries.

### Common Sequential Chains

| Chain | Rationale |
|-------|-----------|
| Schema → API → Frontend | Data structure must precede interfaces |
| Research → Planning → Implementation | Understanding before execution |
| Implementation → Testing → Verification | Build, validate, then audit |

### The Single Ownership Rule

**Never let two agents edit the same file.** This is the most important parallelisation rule. Two agents editing the same file leads to overwrites, merge conflicts, and inconsistent state. Break work so each agent owns a different set of files.

---

## 5. Worktree Isolation

### How It Works

When `isolation: "worktree"` is set, the subagent runs in its own git worktree — an isolated copy of the repository. The subagent has its own files, staging area, and HEAD reference, while sharing the same `.git` directory.

### The Base Branch Problem

**Critical:** Worktrees branch from the last commit (`origin/main` by default), NOT the current working state. Uncommitted changes in the main worktree are NOT reflected in new worktrees.

This means:
- If you switched from ReLU to tanh but did not commit, the worktree agent will see the old ReLU code.
- If you are mid-refactor with uncommitted changes, the worktree agent works from the pre-refactor state.

**Mitigation:** Commit all relevant changes before spawning worktree-isolated subagents. Or do not use worktree isolation when working state matters.

### Worktree Lifecycle

- **Auto-cleanup:** Worktrees with no changes are automatically cleaned up when sessions end.
- **With changes:** The worktree path and branch are returned to the parent for integration.
- **Branch limitation:** A branch can only be checked out in one worktree at a time.

### When to Use Worktree Isolation

- Parallel code modifications that touch different files.
- Experimental changes you may want to discard.
- Long-running analysis that should not block the main workspace.

### When NOT to Use Worktree Isolation

- When the subagent needs to see uncommitted working state.
- For read-only exploration (use a standard subagent instead — lighter weight).
- When you need the subagent's changes to be immediately visible in the main workspace.

---

## 6. Context Management

### The 40–60% Utilisation Target

Maintaining 40–60% context utilisation throughout prevents degradation. As utilisation approaches 100%, reasoning quality drops. Strategies:

1. **Research phase:** Use subagents to explore and return summaries, keeping the parent lean.
2. **Planning phase:** Create detailed plans that anchor the agent's attention.
3. **Implementation phase:** Execute from the plan, compacting status after each step.

### Persistent Memory for Subagents

Subagents can have their own persistent memory:

- `user` scope: `~/.claude/agent-memory/<name>/` — persists across projects.
- `project` scope: `.claude/agent-memory/<name>/` — project-specific, shareable via version control.
- `local` scope: `.claude/agent-memory-local/<name>/` — project-specific, not checked in.

When memory is enabled, the first 200 lines or 25KB of the subagent's `MEMORY.md` loads automatically at startup.

### What to Return from Subagents

Subagents should return **condensed, actionable summaries** — not raw exploration data. The whole point of delegation is keeping the parent context clean. A subagent that returns 50,000 tokens of analysis has failed at its primary job.

---

## 7. Coordination and Communication

### Task-Based Coordination

Agent teams use a shared task list with:
- Pending/in-progress/completed states.
- Dependency tracking — blocked tasks automatically unblock when dependencies complete.
- Task claiming — prevents race conditions.

### Direct Messaging

Teammates can communicate directly without funneling through the lead. This is useful for debate-style investigation where agents need to challenge each other's hypotheses.

### File Ownership

Establish clear file ownership at spawn time. Each agent owns specific files or directories. The agent should not touch files outside its ownership scope.

### Plan Approval Workflow

For risky work, require the subagent to create a plan before implementing. The parent reviews and approves. If rejected, the subagent revises. This adds latency but prevents costly mistakes.

---

## 8. Error Handling and Recovery

### Common Failure Patterns

- **Subagents stopping on errors** instead of recovering. Give additional instructions or spawn a replacement.
- **Lead shutting down before work is done.** Monitor task completion status.
- **Task status lag.** Subagents sometimes fail to mark tasks as completed, blocking dependent tasks.
- **Orphaned sessions.** Clean up with `tmux kill-session` or equivalent.

### The Stuck Agent Problem

Hard limit at 3 iterations on the same error. If an agent is stuck:
1. Force a reflection prompt: "What failed? What specific change fixes it?"
2. If still stuck, kill the agent and spawn a replacement with additional context about what went wrong.

### Background Subagent Failures

If a background subagent fails due to missing permissions, start a new foreground subagent with the same task to retry with interactive prompts.

---

## 9. Anti-Patterns and Known Failure Modes

### Context Anti-Patterns

- **Context overload:** One agent cannot hold large codebases; it loses important details as conversation grows. Use subagents to isolate exploration.
- **Token sprawl:** Redundant context sharing across agents. Multi-agent systems can consume 15x more tokens than single-agent.
- **Instruction fade-out:** LLM instruction adherence decays as conversations extend. Use structured note-taking to combat this.

### Coordination Anti-Patterns

- **No specialisation:** A generalist agent writing database AND UI AND tests produces inferior work compared to focused specialists.
- **Communication vacuum:** Agents working without coordination primitives create conflicts.
- **Hidden bottleneck:** If the lead must approve every message between teammates, it becomes a throughput killer.
- **Careless file scoping:** Multiple agents writing to the same file creates merge problems.

### Orchestration Anti-Patterns

- **Over-parallelising:** Launching excessive agents for simple features wastes tokens and creates coordination overhead. Group related micro-tasks instead.
- **Under-parallelising:** Running independent analyses sequentially when parallel execution applies.
- **Vague invocations:** Sending subagents with incomplete instructions instead of specific scope, file references, and expected outputs.

### The Verification Gap

The bottleneck in multi-agent work is no longer generation — it is verification. Key concerns:
- Tests passing before a change do not guarantee they catch regressions from the change.
- Agents may write technically valid tests that miss critical cases.
- Context limitations mean agents might miss constraints outside their view.

Until verification infrastructure catches up with generation, human review is not optional overhead — it is the safety system.

---

## 10. Quality Verification for Subagent Configurations

Research confirms that subagent failures are overwhelmingly invocation failures, not execution failures. The model's own reasoning capabilities are rarely the bottleneck — the quality of context it receives is. Chroma's "Context Rot" research (2025) found that adding irrelevant context reduces accuracy by up to 30%, and **structured, coherent distractors are more harmful than random noise** — meaning a well-written but irrelevant paragraph in a subagent prompt does more damage than gibberish.

### Invocation Quality Check

Before spawning a subagent, verify the invocation prompt:

- **Is it self-contained?** The subagent has no memory of the parent conversation. Does the prompt include everything the subagent needs — context, scope, file references, success criteria, what to return?
- **Is the scope clear?** Can the subagent determine exactly what files and systems it should touch and what is out of bounds?
- **Are success criteria explicit?** How will the subagent know it is done? How will the parent know the result is correct?
- **Is the return format specified?** The subagent should return a condensed, actionable summary — not raw exploration data. Specify what the parent needs back.

### File Ownership Check

Before spawning parallel subagents:

- **Map every file** each subagent will touch. If any file appears in more than one subagent's scope, restructure the work so each file has exactly one owner.
- **Check for transitive overlap.** Subagent A edits file X, which imports from file Y. Subagent B edits file Y. Even though they own different files, changes to Y's interface may break X. Identify these dependencies and either serialize them or scope them explicitly.

### Worktree Safety Check

Before using worktree isolation:

- **Are all relevant changes committed?** Worktrees branch from the last commit, not the working state. Uncommitted changes will not be visible to the subagent.
- **Does the subagent need working state?** If it does, worktree isolation is the wrong choice — use a standard subagent instead.
- **Is the branch available?** A branch can only be checked out in one worktree at a time.

### Post-Completion Check

After subagent work completes:

- **Verify the result makes sense** in the context of the parent conversation. The subagent may have made reasonable decisions within its limited context that are wrong given information only the parent has.
- **Check for drift from the original intent.** Subagents can go off-track, especially on ambiguous tasks. Compare the result against the original invocation criteria.
- **If multiple subagents ran in parallel**, verify their results are compatible before integrating. Changes that are individually correct can be collectively inconsistent.

---

## 11. Practical Guidelines

### Start Simple

Default to a single agent. Only add subagents when the task genuinely benefits from parallelisation or context isolation. The overhead of coordination (tokens, latency, potential conflicts) must be justified by the speedup or quality improvement.

### The Sweet Spot

3–5 concurrent agents is the practical limit for meaningful human review. More agents produce more output faster, but the review bottleneck prevents you from absorbing the results.

### Multi-Model Routing

Use expensive models (Opus) for planning and coordination. Use cheaper models (Sonnet, Haiku) for focused, well-scoped subtasks. This cuts costs significantly without sacrificing quality on well-scoped work.

### Commit Before Spawning

If using worktree isolation, commit all relevant changes first. Worktrees branch from the last commit, not the working state.

### Make Invocations Self-Contained

The subagent has no memory of your main conversation. Include everything it needs — file references, context, success criteria — in the invocation prompt.

---

## 12. Sources

### Subagent Design and Orchestration
- [Anthropic — Claude Code Sub-agents Documentation](https://code.claude.com/docs/en/sub-agents)
- [Anthropic — Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Anthropic — Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Anthropic — Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic — Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Addy Osmani — The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/)
- [claudefa.st — Sub-Agent Best Practices](https://claudefa.st/blog/guide/agents/sub-agent-best-practices)
- [Block/Goose — Agent Coordination Patterns](https://block.github.io/goose/blog/2025/08/14/agent-coordination-patterns/)
- [Google ADK — Multi-Agent Patterns](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [HumanLayer — Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
- [Vellum — Multi-Agent Systems with Context Engineering](https://vellum.ai/blog/multi-agent-systems-building-with-context-engineering)
- [VS Code Copilot — Subagents Documentation](https://code.visualstudio.com/docs/copilot/agents/subagents)
- [Shipyard — Multi-Agent Orchestration for Claude Code](https://shipyard.build/blog/claude-code-multi-agent/)

### Quality and Verification Research
- [Context Rot — Chroma Research, 2025](https://research.trychroma.com/context-rot)
- [LLMs can be easily Confused by Instructional Distractions, 2025](https://arxiv.org/html/2502.04362v1)
