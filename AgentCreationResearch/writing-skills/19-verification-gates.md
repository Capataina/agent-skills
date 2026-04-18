# Verification Gates

Added 2026-04-18 from research pass.

This file treats verification as a first-class structural concern for reliability-critical skills. The central finding: premature termination and sycophantic self-evaluation are the largest failure categories in published taxonomies, and both are solved by out-of-loop verification rather than in-prompt exhortation.

## The evidence

**MAST taxonomy (Cemri et al., arXiv 2503.13657)** catalogued 1,600+ traces from 7 multi-agent systems and found:
- FM-3.1 Premature termination: 7.82%
- FM-3.2 No / incomplete verification: 6.82%
- FM-3.3 Incorrect verification: 6.66%
- Combined termination-and-verification: **21.3% of all observed failures** — the single largest cluster.

**Reasoning-action mismatch (FM-2.6): 13.98%** — nearly 2x premature termination. The agent reasons correctly about what it should do, writes that it will, then does not. This cannot be fixed by better plans.

**SycEval (arXiv 2502.08177):** 78.5% sycophancy persistence across context/model variation. Self-grading is sycophancy at the judge layer.

**Same Input, Different Scores (arXiv 2603.04417):** GPT-4o and Claude 3.5 Sonnet both display positive self-bias and family-bias in judging. Same-family judges systematically inflate same-family outputs.

**Iterative self-refinement (arXiv 2407.04549):** within a single context window, evaluator scores inflate while human scores drop during iterative self-refinement. No gradient updates needed. "Now review and refine" is actively harmful.

**Cross-family verification (arXiv 2512.02304):** self-verification < intra-family verification < cross-family verification, across 37 models and 9 benchmarks.

**Procedure-aware evaluation (arXiv 2603.03116):** 27-78% of reported successes across GPT-5, Kimi-K2-Thinking, and Mistral-Large-3 are "procedurally corrupt" — final artefact looks right, path to it skipped mandatory steps.

## The four-tier verification model

Skills with reliability obligations should pick a tier and commit to it explicitly:

### Tier 1 — Prose imperative (weakest)

Instruction in SKILL.md body: *"You must call WebSearch at least twice before declaring complete."*

Relies entirely on the agent's compliance with the prose. Subject to all sycophancy and motivated-reasoning failure modes. Weak but sometimes sufficient for non-critical obligations.

### Tier 2 — Recency-anchored checklist

Same instruction plus a quality-checklist item at the end of SKILL.md restating the obligation verbatim. Uses primacy-recency to reinforce.

Stronger than Tier 1 but still self-certified. The agent can satisfy the checklist item subjectively without producing evidence.

### Tier 3 — Evidence-anchored obligation

Checklist item requires specific evidence: *"Cite the WebSearch queries you ran (at least 2), list the sources found, and quote at least one passage per system you claimed to research."*

The agent can lie, but doing so produces a visibly broken artefact (invented queries, fake quotes). Much harder to satisfice. This is the minimum tier for a skill with non-negotiable investigative obligations.

**RULERS (arXiv 2601.08654)** shows evidence-anchored scoring is measurably more stable against adversarial rubric perturbation than prompt-phrasing-based rubrics. Smaller models using evidence-anchored rubrics rival larger-model judges using subjective rubrics.

### Tier 4 — Runtime enforcement (strongest)

Claude Code hooks runtime-check the session transcript. The skill cannot terminate until specific conditions are met.

**Stop hook with `type: "agent"`** — the canonical Anthropic pattern. A 60-second, 50-turn verifier that runs actual tool calls (test suite execution, grep for required tool invocations, file inspection) before allowing the main agent to stop.

Canonical Anthropic example: *"Check if all tasks are complete. If not, respond with {'ok': false, 'reason': 'what remains to be done'}. If the hook returns ok: false, Claude keeps working and uses the reason as its next instruction."*

**PreToolUse hook** — blocks tool execution until preconditions pass.

**SubagentStop hook** — verifies subagent output before the main agent accepts it.

All exit-non-zero hooks are enforced even under `--dangerously-skip-permissions`. This is the only tier that is not subject to the acting model's own assessment.

## Recommendation

For any skill with a tool-use obligation that the agent's pretraining bias disfavours (WebSearch, Task dispatch to specialised subagents, writing new failing tests): **Tier 3 is the floor.** Tier 4 should be available as an escalation.

For skills with deterministic, mechanical obligations (Read these files, run this script): Tier 1 or Tier 2 is usually sufficient.

## Cross-family verifier rule

If verification requires a separate agent pass, use a different model family than the generator. Research support:

- arXiv 2512.02304: cross-family gains > intra-family gains > self-verification gains
- arXiv 2603.04417: same-family judges inflate same-family outputs

For a Claude-driven skill, a verification pass should ideally be a different-model check (GPT, Gemini). Within the Claude family, a Sonnet-verifies-Opus or Haiku-verifies-Sonnet pattern is at least better than same-model self-verification.

## Evidence-slot template

A quality checklist item should look like this:

```
- [ ] **WebSearch obligation:** completed at least 2 WebSearch calls
  - Query 1: [exact query text]
  - Query 2: [exact query text]
  - Sources consulted: [list of URLs]
  - Direct quote from at least one source: [quoted passage]
```

Not like this:

```
- [ ] Conducted adequate research
```

The first cannot be satisfied without producing the evidence. The second can be satisfied by any response.

## The plan-validate-execute pattern

Anthropic's canonical workflow for non-trivial skills:

1. **Analyse** — read the spec, understand the task.
2. **Create a plan file** — write the plan to disk as a concrete artefact.
3. **Validate the plan with a script** — a deterministic check that the plan satisfies the spec.
4. **Execute** — carry out the plan.
5. **Verify** — check the output against the spec.

The key innovation vs a prose-only skill: the plan is a *file*, not a paragraph. A file can be linted, checked programmatically, or reviewed by a verifier. A paragraph is just more text the agent can satisfice around.

## Skipped-work declaration obligation

For skills where skipped obligations are a known risk (anything with investigative or test-writing work), require an explicit structured section:

```
## What I did not do

- [Obligation from spec]: [Reason for skipping or incomplete state]
- [Another obligation]: [Reason]
```

This is a deontological permission in structural form. The agent is licensed — required, even — to admit skipped work. SRFT research (arXiv 2511.06626) showed 770 samples moves hidden-objective F1 from 0.00 to 0.98. Baseline models deny under interrogation; training shifts them to admission. The in-context analog is making admission structurally required rather than optional.

Without this section, skipped work shows up only under direct user interrogation — too late to matter.

## Anti-pattern: iterative self-refinement

Do not include "review your own work and refine" steps in skills. Research (arXiv 2407.04549) showed within a single context window, evaluator scores inflate while human scores drop. Same-model self-review is the sycophancy mirror in action.

If the skill needs review, dispatch to a different-context verifier (a fresh subagent or a different model). Do not ask the generator to grade itself.
