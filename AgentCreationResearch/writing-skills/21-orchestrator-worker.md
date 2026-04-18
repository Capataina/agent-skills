# Orchestrator-Worker and Architecture Patterns

Added 2026-04-18.

This file covers when to split a skill across multiple agents versus keep it in a single agent loop. The evidence is nuanced and the default has shifted since earlier versions of our research.

## The headline numbers

From Anthropic's "How we built our multi-agent research system":

> *"A multi-agent system with Claude Opus 4 as lead and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."*

This is the strongest pro-multi-agent finding in the literature. But the same post explicitly qualifies:

- *"Multi-agent systems use about 15x more tokens than chats"* (4x for single-agent)
- Best for *"valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools"*
- **Underperform** on *"tasks requiring shared context or many inter-agent dependencies, like most coding work"*

Cognition's "Don't Build Multi-Agents" post makes the opposing case for coding specifically: subagents lack shared context, "actions carry implicit decisions, and conflicting decisions carry bad results."

## The reconciliation

The two positions are not actually in conflict once you condition on task type:

- **Research and exploration tasks** (parallel info gathering, wide search of a problem space, comparison across many sources) — orchestrator-worker wins. Anthropic's 90.2% is in this regime.
- **Coding and shared-context tasks** (multi-step work on a codebase where sub-decisions depend on other sub-decisions) — single-agent wins. Cognition's position applies here.

Multi-obligation skills running on a codebase fall in the coding / shared-context regime. **The Anthropic 90.2% number does not apply.** Skills like `code-health-audit` or `upkeep-context` are shared-context tasks, and full orchestrator-worker decomposition is likely wrong.

## The multi-agent trap

From "The Multi-Agent Trap" (Towards Data Science, April 2026):

> *"As single-agent performance increases, the expected benefit of adding agents decreases, and above the threshold the expected benefit becomes negative."*

Measured:
- Unstructured multi-agent networks amplified errors up to **17.2x** vs single-agent.
- Claude on PlanCraft in a multi-agent setup lost **35%** of performance vs single-agent.

Mode separation helps only when:
- Single-agent performance is actually low on that specific obligation
- The obligation can be handed off with little shared context
- Scale justifies it (>15 tools or >100K cross-subtask context)

For a 10-50 tool-call skill, the right split is at most *one* verification subagent at the end, not decomposition of the main loop.

## Architecture patterns with empirical support

| Pattern | Task type | Measured effect | When to use |
|---------|-----------|-----------------|-------------|
| Orchestrator-worker | Parallel research | +90.2% vs single-agent Opus 4 (Anthropic) | Research tasks with wide parallel exploration |
| Plan-and-Act (planner/executor split) | Long-horizon web navigation | 57.58% vs 36.97% executor-only (+20.6pp) on WebArena-Lite (arXiv 2503.09572) | Tasks where the plan benefits from being a committed artefact before execution |
| ADaPT recursive decomposition | Household / embodied | +28.3pp vs baselines on ALFWorld | Clear subtask boundaries, independent sub-goals |
| Reflexion + ReAct | Reasoning QA | 44% EM vs 32% ReAct on HotPotQA | When self-critique can act on concrete tool failures |
| MAR (multi-agent Reflexion, adversarial personas) | Reasoning QA | 47% EM on HotPotQA (+3pp over Reflexion) | When self-critique needs to break homogeneous-worldview trap |
| Structured reflection on tool failure | Multi-turn tool calls | Consistent gains, largest on arg-repair | When tools fail and retry is useful |
| Single-agent with Stop-hook verification | Coding, shared-context | Product primitive, no published effect size | Default for reliability-critical coding skills |

## When to split a single skill into subagents

Use a subagent dispatch when *all* of these apply:

1. **Uncomfortable obligation.** The required tool has low pretraining support — WebSearch, writing new failing tests, cross-system analysis the main loop will satisfice on. See [20-tool-action-patterns.md](20-tool-action-patterns.md).
2. **Different cognitive mode.** The obligation requires a different kind of reasoning than the main loop (external knowledge retrieval vs local code editing; verification vs generation).
3. **Minimal context handoff.** The subagent can do its work with a small input (a query, a file path, a spec summary) and return a small output (1-2K tokens of distilled findings).

Do NOT split when:
- Obligations share heavy context with the main loop
- The subagent would need to re-load most of the project to do its work
- The task is under 15 tool calls total (overhead dominates)
- Sub-decisions depend on each other in ways that require shared state

## The hybrid pattern for reliability

Most reliability-critical multi-obligation skills land here:

- **Single-agent main loop** retains shared coding context, uses Read / Edit / Bash at will
- **One or two specialist subagents** handle specific uncomfortable obligations:
  - Research subagent: given a topic, returns 1-2K tokens of distilled findings with sources
  - Test-writer subagent: given a function spec, writes a failing test file
  - Verification subagent: given the main-loop output and the spec, returns pass/fail per obligation
- **Stop hook** (if Claude Code) runtime-checks the transcript for required subagent invocations

This is closer to Anthropic's "sub-agent architectures for context preservation" pattern than to the multi-agent research system architecture. Each subagent has an isolated context window, a narrow obligation, and a compact return.

## Resource-scaling rule (from Anthropic)

From the multi-agent research system post:

> *"Simple fact-finding requires just 1 agent with 3-10 tool calls; direct comparisons might need 2-4 subagents with 10-15 calls each."*

For context: a typical multi-obligation skill is 20-70 tool calls. By Anthropic's own rule this lives in the "direct comparisons" zone at most — 2-4 subagents total, not 10 agents. Most skills should use 1 or 2 subagents if any.

## Anti-pattern: bag-of-agents

Do not build skills that fan out into many subagents without a clear coordination structure. Unstructured multi-agent dispatch amplifies errors rather than reducing them. If a skill's architecture requires four or more subagents, it probably needs to be broken into separate skills each with a narrower scope.

## Cross-family verification preference

When a verification subagent is warranted, prefer a different model family than the generator — Sonnet-verifies-Opus or GPT-verifies-Claude. Same-family verifiers inflate same-family outputs (arXiv 2603.04417). Cross-family verification empirically dominates self- and intra-family (arXiv 2512.02304).

Within Claude Code this usually means using a different Claude version (Sonnet vs Opus vs Haiku) rather than the same version. Better than same-model but weaker than cross-family.
