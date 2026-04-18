# Infrastructure Mechanisms

Added 2026-04-18.

Skills run inside a runtime that provides structural reliability primitives. A skill file that ignores this runtime is missing the most reliable enforcement layer available. This file enumerates the Claude Code and Claude Agent SDK features that matter for skill reliability.

## The framing

Anthropic's canonical answer to long-horizon reliability is not *"write better prose"* — it is infrastructure:

- Stop hooks with agent-type verification
- SessionStart compact matchers for re-anchoring after compaction
- InstructionsLoaded hooks for lazy-load re-injection
- PreToolUse / PostToolUse hooks for action-level gating
- SubagentStop for delegated-work verification
- Plan-validate-execute with file artefacts
- Subagent frontmatter for specialist scoping

Our research files previously treated these as optional advanced patterns. Based on R5's evidence base, they should be primary defence. Prose-level principles remain important but load less weight than the infrastructure.

## Hooks — full event inventory

From Claude Code hooks guide (`code.claude.com/docs/en/hooks-guide`):

| Event | Reliability use |
|-------|-----------------|
| `Stop` | Fires when Claude finishes responding. Returning `{ok: false, reason}` forces continuation. The canonical mechanism against premature termination. Prompt- and agent-based variants. |
| `SubagentStop` | Verifies subagent output before accepting. Same semantics as `Stop`. |
| `PreToolUse` | Validates/modifies tool inputs. Can block with exit code 2. Fires before permission mode check — cannot be bypassed by `--dangerously-skip-permissions`. |
| `PostToolUse` | Observes tool outputs after execution. Cannot undo, but can inject feedback into context. |
| `PostToolUseFailure` | Recovery logic when tools fail. |
| `SessionStart` (matcher: `compact`) | Fires after context compaction. Re-inject critical rules and obligations. The canonical drift-mitigation primitive. |
| `InstructionsLoaded` | Fires at session start and when files are lazily loaded. Anchor for personality content. |
| `UserPromptSubmit` | Can inject `additionalContext` before Claude processes the prompt. |
| `PreCompact` / `PostCompact` | Instrument compaction-driven drift directly. |
| `TaskCreated` / `TaskCompleted` | Instrument the native task tool. |
| `FileChanged` / `CwdChanged` | Environment reactivity. |

### The three hook types

- `command` — shell command, fastest, deterministic. Use for grep-the-transcript checks, file existence, script exit codes.
- `prompt` — single-turn LLM evaluation (Haiku default). Returns a JSON `{ok: bool, reason: str}`. Use for "is the completion report structurally adequate" checks.
- `agent` — multi-turn agent with tool access. 60-second default timeout, up to 50 tool-use turns. Can run the full test suite, open files, search the codebase. Strongest available verification primitive.

### Canonical Stop-hook example (Anthropic)

```
Type: agent
Timeout: 60s
Prompt: "Verify that all unit tests pass. Run the test suite and check the results. Return {ok: true} if all tests pass. Return {ok: false, reason: 'what failed'} otherwise."
```

If the hook returns `ok: false`, Claude keeps working and uses the reason as its next instruction. This is not a check — it's a reviewer-agent.

## Subagent frontmatter inventory

From Claude Code subagent docs:

| Frontmatter field | Use |
|-------------------|-----|
| `tools` / `disallowedTools` | Allowlist / denylist. Enforces specialist roles structurally. |
| `model` | Override (sonnet/opus/haiku). Cost control + capability specialisation. |
| `maxTurns` | Stopping condition safeguard. |
| `skills` | Skills loaded as full content at startup (not just made available). Composes specialists with skill inventories. |
| `hooks` | Subagent-scoped hooks — includes its own Stop verification. |
| `memory` | `user` / `project` / `local` scope for cross-session learning. Addresses long-horizon continuity. |
| `isolation: worktree` | Git worktree copy for parallel reviewer/implementer workflows without cross-pollution. |
| `initialPrompt` | Auto-submitted first turn. Useful for priming verification expectations. |
| `permissionMode` | `default`/`acceptEdits`/`auto`/`dontAsk`/`bypassPermissions`/`plan`. |
| `effort` | Reasoning budget control. |
| `background` | Run without blocking the parent. |
| `color` | Visual identification in UI. |

Current skills in this repository under-use these fields. A specialist verification subagent with `tools: [Read, Bash]`, `model: opus`, `maxTurns: 10`, `skills: []`, and an agent-type Stop hook is substantially different from a "call the Task tool with a prose prompt."

## Skills runtime features

From Claude Code and Claude API docs:

- **Three-level progressive disclosure** — metadata (~100 tokens) / SKILL.md body (<5k tokens) / resources (unlimited). Directly addresses the 6000-word compliance cliff.
- **YAML frontmatter:** `name`, `description`, `allowed-tools`, `disable-model-invocation`
- **`disable-model-invocation`** — skill is present on the filesystem but only invoked explicitly by the user. Useful to keep heavy-artillery skills out of always-loaded context budget.
- **Discovery** — bash-based filesystem walk, description-triggered via LLM reasoning. No embeddings, no classifiers. Makes description quality disproportionately load-bearing.

## Memory and session features (Agent SDK)

- **Session resumption:** `resume=session_id` continues from prior state with full context
- **`memory` tool** (via subagent frontmatter): persistent cross-session memory with scoped visibility
- **CLAUDE.md + `.claude/rules/*.md`**: auto-loaded into session system prompt. Canonical place for always-on personality content.
- **`AskUserQuestion` built-in tool:** multiple-choice clarification. Reifies ambiguity resolution as a tool call rather than a prose ask.

## Permissions

- **`allowedTools` / `disallowedTools`** — structural constraint, cannot be loosened by hooks
- **`permissionMode`** — spectrum from "always ask" to "bypass permissions"
- Tool restrictions are orthogonal to hooks — the two can be combined for defence-in-depth

## Plan-validate-execute pattern

Anthropic's canonical workflow for non-trivial skills:

1. **Analyse** the task and spec
2. **Create a plan file** — write the plan to disk as a concrete markdown artefact, not a paragraph in context
3. **Validate the plan with a script** — a deterministic check that the plan satisfies the spec (every required component is present, paths exist, etc.)
4. **Execute** the plan
5. **Verify** the output against the spec (Stop hook or separate verifier)

The key innovation: the plan is a *file*, not a paragraph. Files can be linted, checked programmatically, reviewed by a verifier. Paragraphs are just more text the agent can satisfice around.

## Plugin packaging

Claude Code plugins bundle hooks + subagents + skills + commands as a single distributable unit (`hooks/hooks.json`, `agents/`, `skills/`, `commands/`). For a reliability-critical workflow that spans multiple primitives, the plugin is the right unit of design — not the skill alone.

## Slash commands and initialPrompt workflows

`.claude/commands/*.md` files define canned workflows with optional `initialPrompt`. Filesystem-based, discoverable, scoped per user / project / plugin. Useful for recurring verification protocols that run a specific sequence of tool calls.

## How to use this inventory in skill design

When designing a reliability-critical skill, ask:

1. **Is there a Stop hook?** If the skill has non-negotiable obligations, the Stop hook is the only layer that is not subject to the agent's own assessment.
2. **Which obligations need PreToolUse gates?** If a tool must be called before another tool, a PreToolUse hook enforces order.
3. **Does the skill touch long-running sessions?** SessionStart compact matcher + recitation protocol address drift across compaction.
4. **Is there a subagent opportunity?** Specialist subagent with `isolation: worktree` for parallel reviewer patterns.
5. **Does the skill survive model upgrades?** Hooks are version-stable; prose instructions are not. Anthropic explicitly warns Opus 4.7 behaves differently from Opus 4.6 on prompts tuned for older models.

The skills in this archive should be evaluated against this inventory. Any skill whose reliability depends on prose obligations alone is missing infrastructure.
