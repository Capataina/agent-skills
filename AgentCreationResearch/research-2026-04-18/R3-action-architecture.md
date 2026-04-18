---
agent: R3
territory: Action selection, tools & architecture (Modes 5, 6)
date: 2026-04-18
---

# R3 Research Report: Action Selection and Architecture

## 1. New findings beyond current knowledge

### 1.1 BiasBusters measured 20x pretraining-frequency effect on tool selection

**Claim.** Pretraining exposure causally amplifies tool-selection bias, not just correlates with it. Saturated continued pre-training on one tool endpoint's metadata raised that tool's selection share from 0.6% to 12.8% — a 20x relative gain in one epoch.

**Source.** Hu et al., "BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models," arXiv:2510.00307, ICLR 2026. https://arxiv.org/abs/2510.00307 and https://arxiv.org/html/2510.00307

**Evidence strength.** Strong. Controlled intervention on Qwen3-8B, 7 LLMs in overall study, benchmark public at https://github.com/thierry123454/tool-selection-bias. Total-variation-distance bias across models: 0.249 (Qwen3-235B) to 0.377 (GPT-4.1-mini, DeepSeek-V3.2). Claude 3.5 Sonnet delta_model = 0.347 — meaning ~35% of selection mass would need redistribution for fairness.

**Implication for Mode 5.** Directly supports the tool-action-asymmetry hypothesis with a causal mechanism. However, BiasBusters measured only functionally equivalent tools within a category (e.g., five weather APIs). The study does NOT measure cross-category bias — Read vs WebSearch is an open measurement question. Nobody has directly run the benchmark we care about.

### 1.2 Mitigation works at prompt/inference level — ~75% bias reduction without weight changes

**Claim.** Filter-then-uniform-sample reduced combined bias from 0.380 to 0.094 (~75% reduction), API bias 0.338 -> 0.108, positional bias 0.422 -> 0.079.

**Source.** BiasBusters section 5 (same URL as above).

**Evidence strength.** Strong for within-category bias; unknown for cross-category asymmetry.

**Implication.** Validates that prompt/architecture-level mitigation can address tool-selection bias without retraining. For our case this maps to: (a) explicit tool-category floors in SKILL.md, (b) dispatcher-level tool-budget quotas, (c) personality-level "sample uniformly across obligation types" framing.

### 1.3 MAST gives us exact base rates for the failure we observe

**Claim.** Across 1,600+ traces from 7 MAS frameworks, the most relevant failure modes are:
- **FM-1.1 Disobey task specification: 10.98%**
- **FM-1.3 Step repetition: 17.14%**
- **FM-1.5 Unaware of termination conditions: 9.82%**
- **FM-2.6 Reasoning-action mismatch: 13.98%** (reasoning says "I should do X" but action does not)
- **FM-3.1 Premature termination: 7.82%**
- **FM-3.2 No or incomplete verification: 6.82%**
- **FM-3.3 Incorrect verification: 6.66%**

**Source.** Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657. https://arxiv.org/abs/2503.13657 and https://arxiv.org/html/2503.13657v2

**Evidence strength.** Very strong. kappa = 0.88 inter-annotator agreement across 6 expert annotators.

**Implication.** The pattern we call "skip uncomfortable tools and self-certify" is the combination of FM-2.6 (reasoning-action mismatch) + FM-3.1 (premature termination) + FM-3.2 (incomplete verification). Three distinct failures compounding, together ~28% of observed failures. Fixing just one leaves the other two operative.

### 1.4 Reasoning-action mismatch is larger than premature termination

**Claim.** FM-2.6 (13.98%) nearly doubles FM-3.1 (7.82%). The agent "reasons correctly" about what it should do but then acts differently — it knows WebSearch is required and writes that it is required, then proceeds without calling it.

**Source.** MAST paper, same URL.

**Implication for Mode 6.** Single-agent cognitive-mode overload manifests most heavily as a reasoning-versus-execution gap, not as plan quality. The planner subsystem inside a single agent can produce good plans and the executor subsystem still skips items. This is architectural — it will not be fixed by better planning prompts alone.

### 1.5 Anthropic's 90.2% is specific to research-style tasks, and they explicitly say multi-agent is WRONG for most coding

**Claim.** Anthropic's 90.2% improvement came from a specific evaluation (e.g., "identify all board members of IT S&P 500 companies") where parallel search is the bottleneck. The same post states: "most coding tasks have fewer parallelizable components than research." Token cost: 15x a chat, 4x a single agent.

**Source.** Anthropic Engineering, "How we built our multi-agent research system." https://www.anthropic.com/engineering/multi-agent-research-system

**Evidence strength.** High trust, single internal evaluation, specific task distribution.

**Implication.** For our 10-50-tool-call skill-size tasks, full orchestrator-worker is likely wrong. The pattern fit is: skill-internal dispatcher with narrow scope ("verification subagent," "WebSearch subagent"), not general multi-agent research orchestration.

### 1.6 Multi-agent trap: below a single-agent-performance threshold, teams hurt more than they help

**Claim.** "As single-agent performance increases, the expected benefit of adding agents decreases, and above the threshold the expected benefit becomes negative." Unstructured multi-agent networks amplified errors up to 17.2x vs single-agent. Claude on PlanCraft in a multi-agent setup lost 35% of performance vs single-agent.

**Source.** "The Multi-Agent Trap," Towards Data Science, April 2026. https://towardsdatascience.com/the-multi-agent-trap/ Consistent with MAST findings.

**Evidence strength.** Medium (industry analysis citing multiple experiments).

**Implication.** Mode 6 must be applied surgically. Mode separation helps only when: (a) single-agent performance is actually low on that specific obligation, (b) the obligation can be fully handed off with little shared context, (c) >15 tools or >100K cross-subtask context. For a 30-tool-call skill, the right split is probably *one* verification subagent at the end, not a decomposed hierarchy.

### 1.7 Claude Code hooks give us architectural tool-gating — the key primitive exists today

**Claim.** Claude Agent SDK's `Stop` hook can block the agent from terminating unless programmatic completion checks pass. `PreToolUse` hooks can force tool permission decisions. `PostToolUse` hooks can inject feedback into context. All exit-non-zero hooks are enforced even under `--dangerously-skip-permissions`.

**Source.** Claude API Docs — Agent SDK Hooks. https://platform.claude.com/docs/en/agent-sdk/hooks and https://code.claude.com/docs/en/hooks-guide

**Evidence strength.** Product documentation; primitive is shipped.

**Implication for writing-skills.md.** For skills with non-negotiable obligations (code-health-audit WebSearch, upkeep-context cross-system analysis), architectural gating exists: a Stop hook that greps the session transcript for the tool-call and blocks termination until present. This moves enforcement from instruction compliance (weak) to runtime check (strong). None of this is in our current research files.

### 1.8 Structured reflection improves tool-call argument repair measurably — but only on the *failed* call, not the *skipped* call

**Claim.** "Failure Makes the Agent Stronger" (Ma et al., arXiv:2509.18847) shows structured reflection-after-failure improves multi-turn tool calling across three backbones, largest gains on argument-repair and missing-info retrieval.

**Source.** https://arxiv.org/abs/2509.18847

**Evidence strength.** Strong, three backbones.

**Implication for self-critique hypothesis.** Self-critique works when the tool was *called and failed*. It does NOT address the skipped-call case — you cannot reflect on a call you never made. This is a critical asymmetry. Reflexion-style loops cannot recover obligations the agent never attempted. Mitigation must come from pre-commit checklists (before declaring done, list obligations and verify each was called at least once) rather than post-failure reflection.

### 1.9 MAR: adversarial critic personas outperform homogeneous self-critique

**Claim.** "MAR: Multi-Agent Reflexion" (arXiv:2512.20845) uses diverse critic personas with intentionally divergent reasoning tendencies. Reflexion+ReAct improves HotPotQA from 32% -> 44% EM; MAR reaches 47% EM. Homogeneous self-critique underperforms adversarial-persona critique.

**Source.** https://arxiv.org/html/2512.20845v1

**Evidence strength.** Medium. Specific to reasoning QA, not tool-use tasks directly.

**Implication for sycophancy interaction.** A single-agent self-critique shares the sycophant's worldview. Adversarial personas ("imagine a skeptical reviewer who assumes you skipped something") break this. This is the strongest prompt-level lever we have for the sycophancy-self-critique interaction.

## 2. Architectural patterns with empirical support

| Pattern | Task type | Model(s) | Measured effect vs baseline | Source URL |
|---|---|---|---|---|
| Orchestrator-worker (research) | Parallel info gathering (board-member lookup) | Opus 4 lead + Sonnet 4 workers | +90.2% vs single-agent Opus 4 | https://www.anthropic.com/engineering/multi-agent-research-system |
| Plan-and-Act (planner/executor split) | WebArena-Lite web navigation | LLaMA-70B | 57.58% vs 36.97% executor-only (+20.6 pp), 49.1% prior SOTA | https://arxiv.org/abs/2503.09572 |
| Plan-and-Act | WebVoyager text-only | QWQ-32B | 81.36% vs 44.3% GPT-4-Turbo prior | https://arxiv.org/abs/2503.09572 |
| ADaPT recursive decomposition | ALFWorld household tasks | GPT-3.5/GPT-4 | up to +28.3 pp vs baselines | https://allenai.github.io/adaptllm/ |
| Reflexion + ReAct | HotPotQA multi-hop QA | GPT-3.5 | 44% EM vs 32% EM ReAct (+12 pp) | https://arxiv.org/html/2512.20845v1 |
| MAR (multi-agent Reflexion) | HotPotQA | GPT-3.5 | 47% EM (+3 pp over Reflexion+ReAct) | https://arxiv.org/html/2512.20845v1 |
| Structured reflection on tool failure | Multi-turn tool calling | 3 backbones | Consistent gains, largest on arg-repair/missing-info | https://arxiv.org/abs/2509.18847 |
| Filter-then-uniform-sample (BiasBusters) | Tool selection fairness | 7 LLMs | Combined bias 0.380 -> 0.094 (~75% reduction) | https://arxiv.org/abs/2510.00307 |
| Adaptive Graph of Thoughts | GPQA scientific reasoning | Various | +46.2% improvement | https://arxiv.org/abs/2502.05078 |
| Unstructured bag-of-agents (anti-pattern) | General | Claude on PlanCraft | -35% vs single-agent; up to 17.2x error amplification | https://towardsdatascience.com/the-multi-agent-trap/ |
| Stop-hook completion gating | Skill enforcement | Claude Agent SDK | Product primitive, no published effect size yet | https://platform.claude.com/docs/en/agent-sdk/hooks |

## 3. Gaps in current research files

### 3.1 Additive content for `writing-skills.md`

**Section A — Obligation enforcement architecture (new).** Current file treats instructions as the primary enforcement mechanism. Add a tier model:

- Tier 1 (weakest): instruction in SKILL.md body
- Tier 2: instruction + quality-checklist recency anchor at end
- Tier 3: instruction + explicit pre-completion verification section ("before you declare done, state the tool name and message ID for each obligation")
- Tier 4 (strongest): Stop-hook or PreToolUse-hook that runtime-checks the session transcript for the required tool call and blocks termination otherwise

Recommend: for any skill with a tool that the agent's pretraining bias disfavors (WebSearch, diagnostic test authoring, cross-system analysis), Tier 3 is the floor. Tier 4 should be available as an escalation.

**Section B — Tool-asymmetry awareness in skill design (new).** Pretraining frequency biases tool selection by measurable amounts (BiasBusters: 20x shift from training exposure, 0.25-0.38 delta_model at baseline). When designing a skill, explicitly categorize each obligation as "comfortable" (Read, Edit, Bash in a code repo) or "uncomfortable" (WebSearch, Task dispatch to specialized subagent, writing new failing tests before any fix). For every uncomfortable obligation, add a named recency-anchor section ("WebSearch obligation — you must complete this with evidence") and consider Tier 3/4 enforcement.

**Section C — Reasoning-action mismatch as a design concern (new).** MAST shows reasoning-action mismatch (13.98%) is nearly 2x premature termination (7.82%). Don't trust that an agent writing "next I should call WebSearch" will call WebSearch. Build the skill so the agent produces a *tool call* as the committed artifact, not a *paragraph saying it will call*. Prefer skill sections that end with "your next action is a WebSearch tool call" rather than "consider whether WebSearch is needed."

**Section D — When to split into a subagent (new).** Current files lean toward everything-in-one-SKILL. Give a concrete threshold: if the skill has an obligation where the model's pretraining bias is strong *against* calling it AND the obligation requires a different cognitive mode (searching external knowledge vs editing local files), consider a Task dispatch to a subagent whose entire prompt is dedicated to that mode. Do not split if obligations share heavy context (MAST FM-2.4 information withholding accounts for only 1.66% but cascades — splits only work when context handoff is minimal).

**Section E — Anti-pattern: bag-of-agents (new).** Unstructured multi-agent amplifies errors up to 17.2x; Claude on PlanCraft lost 35%. Skills should not fan out into many subagents unless (a) >15 tools needed, (b) >100K context across subtasks, (c) tasks decompose into genuinely parallel work with minimal handoff. For 10-50 tool-call skills (our typical size), the right split is at most *one* verification subagent at the end — not decomposition.

### 3.2 Additive content for `writing-personalities.md`

**Section A — Dispatch-to-subagent as a first-class personality primitive (new).** Personality should know when to use the Task tool to dispatch uncomfortable work. Specifically: "When a skill names an obligation requiring WebSearch or cross-system synthesis, and you find yourself drafting reasoning about why you don't need it, dispatch a Task subagent whose sole obligation is that tool. The handoff forces commitment."

**Section B — Pre-completion obligation audit (new).** Before the personality lets the agent declare a skill complete, it must produce a structured list: each named obligation from the skill, the tool call that satisfied it (with a short transcript quotation), and the artifact produced. Any obligation without both fields is uncompleted. This is the prompt-level analog of a Stop hook.

**Section C — Adversarial persona for self-critique (new).** Homogeneous self-critique is too close to the executor's worldview. When reviewing work, the personality should explicitly adopt a skeptical-reviewer persona that assumes obligations were skipped until proven otherwise. MAR shows 3 pp gain from persona divergence on HotPotQA; qualitative effect on skip-detection should be larger because the base rate of skipping is higher.

**Section D — Tool-asymmetry naming (new).** The personality should name the bias. "You will feel pulled toward Read/Edit/Bash and away from WebSearch and Task dispatch — this is a pretraining-distribution artifact, not a judgment call. Treat any instinct to skip these tools as evidence you should call them immediately." Naming the bias as an artifact of training (not as an argument the agent is making) cuts off the agent's ability to rationalize.

**Section E — Token-budget honesty (new).** Multi-agent systems use 15x a chat, 4x a single agent (Anthropic). Personality should default to single-agent and only dispatch when the cost is justified by the obligation being genuinely uncomfortable, not for convenience.

## 4. Surprises / counterintuitive findings

1. **Reasoning-action mismatch is the dominant failure mode, larger than premature termination.** The agent knows it should call the tool, writes that it should, then doesn't. This means improving plan quality alone won't fix the problem — the plan is already correct. The gap is in execution commitment, which requires structural intervention (hooks, pre-commit obligation audits).

2. **Self-critique cannot recover skipped tools.** Reflexion works when a tool is called and fails. A tool that was never called produces no failure to reflect on. The self-critique literature is load-bearing for error *correction*, not for error *prevention of omission*. This undermines any "we'll just add self-critique" response to the skipping problem.

3. **Pretraining-frequency effect on tool selection is empirically 20x — and it's a causal intervention, not a correlation.** BiasBusters showed continued pre-training on one endpoint produced a 20x shift in selection share. This means our "pretraining bias toward Read/Edit/Bash" hypothesis is not a hand-wave — it is the known causal mechanism. It also means prompt-level mitigations have a hard ceiling: 75% bias reduction via filter-and-uniform-sample, which is excellent, but pretraining remains the dominant prior.

4. **Anthropic's own claim explicitly says multi-agent is wrong for most coding.** The 90.2% headline number is for parallel research tasks with minimal inter-agent dependency. For coding (and by extension, skill-driven work on a codebase), the Anthropic post recommends against full orchestrator-worker. This cuts against naive "just use multi-agent" conclusions.

5. **Bag-of-agents amplifies error 17.2x; Claude on PlanCraft lost 35% when put in a multi-agent setup.** Adding agents is not free and often net-negative below a task-complexity threshold. Mode 6 must be surgical.

6. **Hooks are a product primitive today, but there is no published empirical effect size for Stop-hook completion gating in Claude Code.** This is actually a research opportunity — measuring it on code-health-audit V14 style evals would produce the first published number.

7. **Within a category of functionally equivalent tools, even the least-biased model (Qwen3-235B) still needs 25% of selection mass redistributed for fairness.** The problem is not a fringe effect on weak models — frontier models at 235B parameters are substantially biased.

## 5. Full source list

### Primary sources (strong, load-bearing)

- Hu et al., "BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models," arXiv:2510.00307 (ICLR 2026). https://arxiv.org/abs/2510.00307 / https://arxiv.org/html/2510.00307
- BiasBusters benchmark and code. https://github.com/thierry123454/tool-selection-bias
- Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657. https://arxiv.org/abs/2503.13657 / https://arxiv.org/html/2503.13657v2
- Anthropic Engineering, "How we built our multi-agent research system." https://www.anthropic.com/engineering/multi-agent-research-system
- Erdogan et al., "Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks," arXiv:2503.09572. https://arxiv.org/abs/2503.09572 / https://arxiv.org/html/2503.09572v3
- Prasad et al., "ADaPT: As-Needed Decomposition and Planning with Language Models," arXiv:2311.05772. https://allenai.github.io/adaptllm/
- Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning," arXiv:2303.11366. https://arxiv.org/abs/2303.11366
- Ma et al., "Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions," arXiv:2509.18847. https://arxiv.org/abs/2509.18847
- "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs," arXiv:2512.20845. https://arxiv.org/html/2512.20845v1
- "Adaptive Graph of Thoughts: Test-Time Adaptive Reasoning Unifying Chain, Tree, and Graph Structures," arXiv:2502.05078. https://arxiv.org/abs/2502.05078
- "AgentIF: Benchmarking Instruction Following of Large Language Models in Agentic Scenarios," arXiv:2505.16944. https://arxiv.org/html/2505.16944v1
- "Sherlock: Reliable and Efficient Agentic Workflow Execution," arXiv:2511.00330. https://arxiv.org/pdf/2511.00330
- "Plan Verification for LLM-Based Embodied Task Completion Agents" (VerifyLLM), arXiv:2509.02761. https://arxiv.org/html/2509.02761v2
- "United Minds or Isolated Agents? Exploring Coordination of LLMs under Cognitive Load Theory," arXiv:2506.06843. https://arxiv.org/html/2506.06843v1

### Product documentation

- Claude Agent SDK hooks. https://platform.claude.com/docs/en/agent-sdk/hooks
- Claude Code hooks guide. https://code.claude.com/docs/en/hooks-guide
- Claude API tool choice (forced function calling). https://platform.claude.com/docs/en/agent-sdk/custom-tools
- Anthropic, "Building effective agents." https://www.anthropic.com/research/building-effective-agents
- Orchestrator-worker cookbook. https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers

### Secondary sources

- "The Multi-Agent Trap," Towards Data Science, April 2026. https://towardsdatascience.com/the-multi-agent-trap/
- "Why Your Multi-Agent System is Failing: Escaping the 17x Error Trap." https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/
- Beam.ai, "6 Multi-Agent Orchestration Patterns for Production (2026)." https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production
- Arize AI, "Orchestrator-Worker Agents: A Practical Comparison of Common Agent Frameworks." https://arize.com/blog/orchestrator-worker-agents-a-practical-comparison-of-common-agent-frameworks/
- Stevens Online, "Building Self-Healing AI: The Orchestrator-Workers and Reflexion Patterns." https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/
- Medium/Karapetyan, "Tackling the Partial Completion Problem in LLM AI Agents." https://medium.com/@georgekar91/tackling-the-partial-completion-problem-in-llm-agents-9a7ec8949c84
- "AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents," ICSE 2026. https://cposkitt.github.io/files/publications/agentspec_llm_enforcement_icse26.pdf
- TokenMix, "Function Calling and Tool Use Guide 2026." https://tokenmix.ai/blog/function-calling-guide
- Mindra, "The Collaboration Layer: Multi-Agent Design Patterns." https://mindra.co/blog/multi-agent-system-design-patterns-orchestration
