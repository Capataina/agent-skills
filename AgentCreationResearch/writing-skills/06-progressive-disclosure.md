# Progressive Disclosure and Context Engineering

## The Three-Level Loading System

Skills use progressive disclosure to manage context efficiently:

| Level | What Loads | When | Token Cost |
|-------|-----------|------|------------|
| 1 — Metadata | Name + description | Always at startup | ~100 tokens per skill |
| 2 — SKILL.md body | Core workflow instructions | When skill triggers | Under 5k tokens |
| 3 — Reference files | Detailed standards, templates, examples | On explicit demand | As needed |

This means you can have many skills installed without impacting performance on unrelated tasks. The cost is paid only when the skill activates.

## Context Is a Finite Resource

As token count in the context window increases, the model's ability to accurately recall information decreases proportionally (Chroma Research, "Context Rot," 2025). Every token has a cost — not in money, but in attention. This means:

- Do not front-load reference files that are only needed sometimes. Use conditional loading.
- Do not repeat the same information in multiple reference files.
- Do front-load references that are always needed. If every invocation requires all references, say so and load them all.

## Mandatory-Core vs. Task-Based Conditional Loading

Reference files fall into two categories:

| Category | Description | Loading Instruction |
|----------|-------------|---------------------|
| **Mandatory-core** | Files needed for every invocation of the skill, regardless of task. | "Read these files immediately after SKILL.md loads." List them explicitly and unconditionally. |
| **Task-based conditional** | Files needed only for specific tasks or phases. | "Read this file when [specific condition]." The condition must be concrete and unambiguous. |

**Failure mode:** Listing all reference files sequentially without marking which are mandatory vs. conditional causes the agent to read only the first few (observed in practice — agents given a list of 10 files to read often stop at 3). The fix is explicit categorisation with clear loading triggers.

**Evaluation test:** Count the reference files listed in SKILL.md's loading instructions. If more than 3-4 are listed without clear conditional triggers, the agent will under-load. Mark mandatory files distinctly (e.g., in a separate section or with explicit "always read" language).

## Just-In-Time Context

Rather than pre-loading all context, maintain lightweight pointers (file paths, section references) and let the agent load detailed information on demand. This mirrors how humans work — we do not memorise entire reference manuals, we know where to look.

The skill should tell the agent what each reference file contains and when to read it, so the agent can decide what it needs for the current task. A one-line summary per reference file is sufficient:

> `references/analysis-categories.md` — Taxonomy of finding categories with definitions, boundary rules, and examples. Read before classifying findings.

## The 6000-Word Cliff (2026-04-18 update)

AgentIF (NeurIPS 2025) measured instruction-satisfaction rate (ISR) across 50 real-world agentic applications. Finding: **when total instruction length exceeds 6,000 words, the ISR scores of all tested models are nearly 0.** This is a cliff, not a curve.

For skill design this means: past ~6k words of *loaded* instruction content (SKILL.md body + all loaded reference files), full compliance collapses regardless of how well-written the content is. Decomposition matters more than prompt-craft past this threshold.

Implication for progressive disclosure: the point is not just that more content costs more tokens — it is that loaded content past 6k words forfeits reliable compliance on *every* obligation in the loaded set. The three-level loading system is load-bearing for compliance, not just for cost.

See also: [18-claude-specific-calibration.md](18-claude-specific-calibration.md) for per-model IFScale numbers.
