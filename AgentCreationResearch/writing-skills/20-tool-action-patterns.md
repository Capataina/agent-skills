# Tool-Action Patterns

Added 2026-04-18.

This file covers tool-selection bias, the tool-action asymmetry failure pattern, and the skill-design patterns that counteract them.

## The core finding

Agents systematically prefer tools whose use pattern matches their pretraining distribution. Reading files, editing code, running shell commands — these have massive training representation. Web searching, writing new test files, dispatching to specialised subagents, cross-system analysis — these have far less training representation.

The effect is not a correlation or a soft preference. It is a **20x causal effect** established by controlled pre-training intervention.

## BiasBusters (arXiv 2510.00307) — the anchor finding

Hu et al., ICLR 2026. Controlled experiment on Qwen3-8B: saturated continued pre-training on one tool endpoint's metadata raised that tool's selection share from **0.6% to 12.8%** — a 20x relative gain in one epoch.

Cross-model baseline bias measured by total-variation distance (TVD from fair selection):
- Qwen3-235B: 0.249 (least biased frontier model)
- GPT-4.1-mini, DeepSeek-V3.2: 0.377 (most biased)
- Claude 3.5 Sonnet: 0.347 — ~35% of selection mass would need redistribution for fairness

This measured bias is *within a category of functionally equivalent tools* (five weather APIs). Cross-category bias (Read vs WebSearch) has not been directly measured but the mechanism predicts it should be larger.

## The AgentIF tool-constraint number

AgentIF (arXiv 2505.16944, NeurIPS 2025): tool-use constraints specifically collapse to **43.2% satisfaction rate** vs **80.8% for vanilla constraints.**

The category of instruction models handle worst is "you must call tool X." Any obligation framed as a tool-use imperative is in the lowest-compliance category.

## What this means for skill design

1. **Never assume a prose imperative to call a tool will be reliably followed.** Especially for tools with low pretraining support.
2. **Categorise every obligation by tool-support.** High-support tools (Read, Edit, Bash, Grep, Glob) vs low-support tools (WebSearch, Task, writing new files, running unfamiliar scripts).
3. **For low-support tool obligations, add an enforcement mechanism beyond prose.** Tier 3 (evidence-anchored checklist) minimum; Tier 4 (runtime hook) for non-negotiable obligations.
4. **Reify investigation obligations as tool calls.** A skill obligation to "research current best practices" reads as a prose instruction the agent can satisfice. An obligation to "call WebSearch at least 2 times with topic-specific queries and quote at least one source per system" is a tool-call schema the agent must produce.

## Fix patterns

### Filter-then-uniform-sample (prompt-level)

From BiasBusters section 5: filter-then-uniform-sample reduced combined bias from 0.380 to 0.094 (**~75% reduction**) without weight changes. Applied to our case: when a skill has multiple plausible tool paths, explicitly enumerate them and require the agent to consider each rather than picking the most pretraining-familiar one.

Example: *"For each system you analyse, you must choose at least one technique from the following equally-valid categories: (a) code-path tracing via Read/Grep, (b) documentation lookup via WebSearch, (c) test-writing via Write for behavioural verification. Do not use only one category."*

### Forced function calling

Claude API `tool_choice` can force a specific tool at a specific step. Not usable in every skill context, but available as an escalation for non-negotiable obligations.

### PreToolUse hook gates

Claude Code's `PreToolUse` hook can block other tool calls until required tools have fired. Architectural enforcement — agent cannot skip the required tool because the hook refuses the attempt to proceed.

### Tool-trace requirement in exit gate

Stop hook (agent-type) runs tool calls to verify the session transcript contains required tool invocations. *"Grep the transcript for `<tool_use name=\"WebSearch\">`. If fewer than 2 occurrences, return {ok: false, reason: 'WebSearch obligation not met.'}"*

### Naming the bias in the personality

Research support is weaker but the pattern costs nothing. In the personality (CLAUDE.md), explicitly name the bias as a pretraining artefact rather than a judgement call:

*"You will feel pulled toward Read / Edit / Bash and away from WebSearch and Task dispatch. This is a pretraining-distribution artefact, not a judgement. When a skill names a tool obligation and you find yourself drafting reasoning about why you don't need it, treat that reasoning as evidence you should call the tool immediately."*

Naming the bias as an artefact of training (not as an argument the agent is making) cuts off the motivated-reasoning channel where the agent convinces itself the tool isn't needed.

### Dispatch-to-subagent for uncomfortable obligations

If an obligation is both uncomfortable (low pretraining support) and specialised (different cognitive mode from the main loop), dispatch to a subagent whose entire prompt is that obligation. The handoff forces commitment.

Caveats from R3 research:
- Multi-agent dispatch costs 15x tokens vs chat, 4x vs single-agent (Anthropic multi-agent research system post)
- Unstructured bag-of-agents can amplify errors 17.2x (Towards Data Science "Multi-Agent Trap")
- Anthropic explicitly warns orchestrator-worker underperforms on shared-context tasks like coding

Dispatch sparingly. For a typical 30-tool-call skill, at most one verification subagent at the end — not decomposition of the main loop.

See [21-orchestrator-worker.md](21-orchestrator-worker.md) for the architectural pattern.

## Detection

For each obligation in the skill:

1. **Identify the required tool.** What primitive action must happen?
2. **Classify tool support.** High pretraining frequency (Read, Edit, Bash, Grep, Glob) or low (WebSearch, Task, Write new file, unfamiliar command)?
3. **Check enforcement tier.** If low-support tool and the enforcement is only prose (Tier 1) or subjective checklist (Tier 2), the obligation is at high risk of being skipped.
4. **Escalate the tier** — add evidence requirements (Tier 3) or runtime hook (Tier 4) as warranted by the stakes.

The V14 code-health-audit pattern — 57 tool calls, zero WebSearch, zero diagnostic tests — is the textbook manifestation: two low-support tool obligations with only prose enforcement, skipped silently, self-certified complete.
