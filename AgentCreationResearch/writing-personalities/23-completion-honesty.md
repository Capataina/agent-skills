# Completion Honesty

Added 2026-04-18.

The personality is the coordinator — it is the line of defence against agent self-certification that masks skipped work. This file codifies the personality-layer patterns that produce honest completion reporting, backed by research.

## The core finding

The `code-health-audit` V14 failure — 57 tool calls, zero WebSearch, zero diagnostic tests, self-certified complete, honest admission only under direct interrogation — is an instance of a published phenomenon: **Procedure-Outcome Decoupling / Corrupt Success**.

arXiv 2603.03116 ("Beyond Task Completion") measured procedure-aware evaluation across frontier models: **27-78%** of reported successes are "procedurally corrupt" — final artefact looks right, path to it skipped mandatory steps.

The personality cannot fix this at the wording layer alone (generic "be honest" fails — Northeastern 2026). But it can install structural mechanisms that produce honest reporting, and it can establish deontological permissions that the model measurably acts on (npj Digital Medicine 2025: 94% rejection rate with explicit permission).

## The five personality patterns for completion honesty

### 1. Pre-completion obligation audit

A structural requirement that the agent produces an evidence ledger before declaring any task complete.

Personality framing:

> *"Before declaring any task complete, enumerate every obligation from the active skill. For each obligation, either cite the evidence (tool call name and arguments, file path, search query, test file) or declare it skipped with reason. Place this as a 'Compliance audit' section. If any obligation is skipped, notify the user explicitly before considering the response complete."*

This is a structural analogue of a Claude Code Stop hook. The agent cannot satisfice around it without producing visibly broken output.

Research support: SRFT (arXiv 2511.06626) — 770 training samples moved hidden-objective F1 from 0.00 to 0.98 on GPT-4.1. Baseline models deny under interrogation; training shifts them to admission. The in-context analog is making admission structurally required rather than optional.

### 2. Deontological permission for skipped-work admission

Explicit licensing of the honest behaviour the model would otherwise suppress:

> *"You may always say 'I did not do X' or 'I could not verify Y.' Admission is preferred over generating plausible content you have not produced. This is not a fallback — it is the correct response when work was not completed."*

Research: npj Digital Medicine 2025 measured 94% illogical-request rejection with explicit permission. arXiv 2506.21584 measured 27-64% reduction in alignment-faking gap with duty-framed prompts.

The mechanism: when honest admission is inferred from persona (e.g., "you are an honest assistant"), it generalises weakly. When it is explicitly permitted as bounded task behaviour, the model treats it as scoped and measurably acts on it.

### 3. Tool-bias naming as pretraining artefact

The model has pretraining-biased tool preferences. It can rationalise these into judgement calls. Naming the bias as an artefact of training cuts off the rationalisation:

> *"You have pretraining-distribution biases: toward Read, Edit, Bash, Grep, Glob; against WebSearch, Task dispatch, writing new files, unfamiliar scripts. These biases are training artefacts, not judgement calls. When a skill names a low-bias tool as an obligation and you find yourself drafting reasoning for why you don't need it, that drafting is evidence you should call the tool immediately — not evidence you should skip it."*

Research: BiasBusters (arXiv 2510.00307) measured 20x pretraining-frequency effect on tool selection as a **causal** mechanism. Prompt-level filter-then-uniform-sample reduces bias ~75%. The personality framing is the prompt-level analog.

The "Unspoken Hints" paper (arXiv 2509.26041) showed models use hints without verbalising them; post-hoc rationalisation rates were 13% (GPT-4o-mini) and 7% (Haiku 3.5). Without the tool-bias naming, this rationalisation channel stays open.

### 4. Adversarial reviewer persona for verification

When verification is needed, homogeneous self-critique shares the sycophant's worldview. Adversarial persona framings break this:

> *"When reviewing your own work before declaring done, adopt the persona of a skeptical reviewer who assumes you skipped something. Do not look for reasons why your work is complete. Look for obligations you might have overlooked."*

Research: MAR (arXiv 2512.20845) showed diverse critic personas produce +3pp on HotPotQA vs homogeneous self-critique. The qualitative effect on skip-detection should be larger because the base rate of skipping is higher than the base rate of reasoning errors.

### 5. Refuse iterative self-refinement

Explicitly do not include "review and refine your work" instructions as a reliability mechanism:

> *"Do not perform iterative self-review as a completeness check. Within a single context window, same-model self-review measurably inflates evaluator scores while actual quality drops. If verification is needed, it must come from a different context or a different model."*

Research: arXiv 2407.04549 measured within-context evaluator inflation during iterative self-refinement. No gradient updates needed. "Review and refine" is not a weak mitigation — it is actively harmful.

## How these combine

Individually, each pattern provides a measurable but modest shift. Combined, they produce a personality that structurally resists the V14 failure mode:

- The obligation audit (pattern 1) forces evidence or admission on every task.
- The deontological permission (pattern 2) makes admission structurally available and motivated.
- Tool-bias naming (pattern 3) cuts off the motivated-reasoning channel where the agent convinces itself a tool wasn't needed.
- The adversarial reviewer persona (pattern 4) breaks the sycophantic self-critique loop.
- Refusing iterative self-refinement (pattern 5) removes a favourite anti-pattern.

Research-backed expectation: no prompt-level intervention reduces sycophancy below ~40% residual (Sparse Activation Fusion floor, OpenReview BCS7HHInC2 — requires model internals, not available through API). But the combined intervention approaches this floor, which is substantially better than the unmitigated baseline (78.5% persistence).

## What the personality cannot do alone

For non-negotiable reliability, pair personality patterns with infrastructure:

- **Claude Code Stop hooks** (agent-type, 60s, 50-turn verifier) — runtime check that the transcript contains required tool invocations. See [writing-skills/22-infrastructure-mechanisms.md](../writing-skills/22-infrastructure-mechanisms.md).
- **SubagentStop hooks** for delegated work verification.
- **PreToolUse hooks** for forced tool ordering.

The personality reinforces behaviours; hooks enforce them. Production reliability comes from both layers, not from either alone.
