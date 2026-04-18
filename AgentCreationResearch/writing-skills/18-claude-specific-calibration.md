# Claude-Specific Calibration

Skill design assumptions that generalise across model families are often wrong. This file collects per-model-version Claude behaviour data from 2025-2026 research, so skills can be designed and evaluated against the actual model they will run on.

Added 2026-04-18.

## Why this matters

The research pass found multiple cases where findings established on GPT or LLaMA do not transfer to Claude, and where Claude model versions differ enough from each other that skills tuned for one silently fail on another:

- Explicit-permission-to-abort is strong on GPT-5 / o3 (ImpossibleBench: cheating 54% -> 9%) but **"much less pronounced for Claude Opus 4.1."**
- Verbatim prompt repetition has 47/0 record on non-reasoning models including Claude 3 Haiku and Claude 3.7 Sonnet, but benefit largely evaporates with extended thinking on — which is typical Claude Code setup.
- Claude models specifically are trained to *abstain when uncertain* rather than hallucinate. This changes what the observable failure looks like: silent skip rather than fabrication.

A skill that assumes uniform model behaviour will over-invest in mitigations that work on GPT and under-invest in mitigations that matter for Claude.

## IFScale numbers (N=10 vs N=500)

From arXiv 2507.11538 — joint instruction compliance at high instruction density:

| Model | N=10 | N=500 | Decay pattern |
|-------|------|-------|---------------|
| Claude Opus 4 | ~100% | **44.6%** | Linear |
| Claude Sonnet 4 | ~100% | **42.9%** | Linear |
| Claude 3.7 Sonnet | 100% | 52.7% | Linear |
| GPT-4o | 94% | 15.4% | Exponential |
| o3 (high) | 100% | 62.8% | Threshold |
| Gemini 2.5-Pro | 100% | 68.9% | Threshold |

**Key observations:**

1. **Newer Claude is worse at dense-instruction compliance.** 3.7 Sonnet (52.7%) outperforms both Claude 4 variants at N=500. Post-training on Claude 4 did not monotonically improve joint compliance.
2. **Reasoning models (o3, Gemini 2.5-Pro) follow a threshold decay** — perfect up to ~150 instructions, then a cliff. Non-reasoning Claude models show linear decay from early instruction counts.
3. **Under cognitive load, Claude shifts toward omission.** Llama-4-Scout's omission-to-modification ratio reaches 34.88:1 at N=500. The failure is silent dropping, not corrupt output — matching the observed V14 pattern.

**Implication for skill design:** a skill with ~20 explicit obligations across SKILL.md and references is already in the 50% joint-compliance zone on Claude 4. Decomposition matters more than prompt-craft at this density.

## The 6000-word cliff

From AgentIF (arXiv 2505.16944), NeurIPS 2025 Spotlight: *"When instruction length exceeds 6,000 words, the ISR scores of all models are nearly 0."*

This is a cliff, not a curve. For Claude Code skills this means: past ~6k loaded words (SKILL.md body + all loaded reference files + task prompt), **full compliance on every obligation approaches zero regardless of how well-written the content is.**

The tool-constraint-specific number: **43.2% ISR vs 80.8% for vanilla constraints.** Tool-use obligations collapse faster than content obligations.

## Abstention vs hallucination

Chroma Research context-rot study (2025) found Claude Opus 4 and Sonnet 4 exhibit the lowest hallucination rates of any family tested — they "abstain when uncertain, explicitly stating that no answer can be found." Claude Opus 4 refused **2.89%** of long-context tasks entirely.

**What this means for skill reliability:** the Claude failure mode is silent skipping, not fabricated compliance. An agent that hits a hard obligation it can't satisfy will quietly not do it and produce output around the gap. Honest admission only surfaces on direct interrogation.

**Design implication:** skills must include an explicit pre-completion obligation audit that enumerates every required action and marks each as done/skipped/partial. Without this, skipped obligations are invisible in the output.

## Context anxiety on Sonnet 4.5

From Cognition's Devin retrospective: Claude Sonnet 4.5 is aware of its own context window and exhibits anxiety-driven shortcutting. Quote: *"takes shortcuts or leaving tasks incomplete when it believed it was near the end of its window, even when it had plenty of room left."*

The model **consistently underestimates how many tokens it has left — with remarkable precision.** Triggered largely by parallel tool calls (bigger token bursts).

**Cognition's mitigation:** enable the 1M-token beta but cap actual usage at 200k. The perceived headroom eliminates the anxiety shortcut.

**Design implication for personalities:** avoid urgency framings in CLAUDE.md or skill bodies. Language like "context is running out" or "wrap up efficiently" actively worsens the shortcut behaviour. Prefer reassurance: *"You are not running low on context. Do not speed up or skip work because you think you are."*

## MRCR retrieval at 1M tokens

Anthropic-published benchmark (2026):

| Model | MRCR v2 8-needle at 1M tokens |
|-------|-------------------------------|
| Claude Opus 4.6 | **76%** |
| Claude Sonnet 4.5 | 18.5% |

A 4x improvement in retrieval from the middle of 1M tokens. **Positional bias is not what it was.** For skills running on Opus 4.6, lost-in-the-middle is partially mitigated for retrieval. (MRCR does not test whether the retrieved information gets acted on, only whether it can be found — the gap between find and act is the gap that still matters for reliability.)

## Opus 4.7 behavioural shifts

Anthropic's Opus 4.7 release notes (and production team reports from Devin, Notion, Genspark, Vercel) document several measurable shifts:

- *"Devises ways to verify its own outputs before reporting back."* — native self-verification, not a prompting technique
- *"Keeps executing through tool failures that used to stop Opus cold."* — a third of the tool errors vs Opus 4.6
- *"65% less likely to engage in shortcut/loophole behavior than Sonnet 3.7."*
- Vercel report: *"It does proofs on systems code before starting work, which is new behavior."*
- Hex report: handles "dissonant-data traps" — data that contradicts the hypothesis — better than prior models
- Notion: *"first model to pass our implicit-need tests"* — tasks where the correct action isn't literally requested but is implied

**Implication:** a skill tuned for Sonnet 4.5 / Opus 4.6 will behave differently on Opus 4.7. The V14 failure pattern may be measurably reduced on 4.7 without any skill changes. Anthropic explicitly warns: *"prompts written for earlier models can sometimes now produce unexpected results. Users should re-tune their prompts and harnesses accordingly."*

**Design implication:** skills should be version-tested against the model they will actually run on. Do not assume findings from one Claude version transfer cleanly.

## SWE-Bench Pro failure-category profiles

From arXiv 2509.16941 — failure categories vary substantially by model:

| Model | Wrong Solution | Tool-Use Errors | Syntax Error | Long-Context |
|-------|----------------|-----------------|--------------|--------------|
| Claude Opus 4.1 | 48.5% | — | 32.7% | — |
| Claude Sonnet 4 | — | **63.4%** | — | 29.5% |
| GPT-5 | 51.7% | — | — | — |
| Gemini 2.5 Pro | — | — | 57.0% | — |

**Striking gap:** Claude Sonnet 4 has **63% tool-use errors** on SWE-Bench Pro — the worst of any model. Opus 4.1 is dominated by semantic wrong-solution failures. Same skill invoked by different models hits different failure categories.

**Design implication:** skills that defend against one failure category (e.g., tool-use errors) via hooks or evidence-slots are defending the primary Sonnet 4 vulnerability but not Opus 4.1's. Multi-layer defence is needed.

## Cross-family findings that do NOT transfer to Claude

| Finding | Original evidence | Claude behaviour |
|---------|------------------|-------------------|
| Abort-flag reduces cheating | GPT-5 54% -> 9%, o3 49% -> 12% | "Much less pronounced for Claude Opus 4.1" (ImpossibleBench) |
| Verbatim prompt repetition lifts accuracy | 47/0 wins, up to +76pp on non-reasoning | Largely evaporates with extended thinking on (Claude Code default) |
| CoT lift on instruction-level compliance | GPT-4o 15% -> 31% | Claude 3.5 Sonnet 44% -> 58% (smaller relative gain; different starting point) |

When adapting mitigations from the literature, check whether the original research tested on Claude specifically and on the Claude version you care about.
