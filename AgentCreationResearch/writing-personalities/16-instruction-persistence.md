# Instruction Persistence

## The Problem

Instructions fade over long conversations. The primacy-recency effect means middle-of-conversation instructions receive less attention as the conversation grows. This is well-documented: "Lost in the Middle" (Liu et al., 2023) found that multi-document QA performance drops by more than 20% when relevant information is positioned in the middle rather than at the beginning or end — in the worst case, performance was *lower than having no documents at all*. Serial position research (Guo et al., 2024) found that primacy effects appeared in 73 out of 104 tested instances (70%), with the first third of labels accounting for more than 40% of predictions. Encouragingly, chain-of-thought reasoning effectively mitigated these effects across most models — which means skills that encourage step-by-step reasoning may naturally reduce lost-in-the-middle problems.

The personality file, placed at the very beginning of the context, benefits from primacy — but as the conversation grows, even primacy attenuates. An instruction that shapes behaviour perfectly at turn 3 may have no effect at turn 50.

## The Two Types of Persistence

**Content persistence** relies on the agent remembering specific instructions. It is the weakest form — the agent must recall text from potentially thousands of tokens ago, competing with all the intermediate conversation for attention. Content persistence degrades predictably as conversations lengthen.

**Structural persistence** is built into the workflow. The agent does not need to remember the instruction because the workflow naturally produces the behaviour. Structural persistence is far more reliable because it does not depend on memory.

| Mechanism | Type | How It Works | Reliability |
|-----------|------|-------------|-------------|
| Personality section placement | Content | Primacy-recency effect keeps early and late instructions in attention | Moderate — degrades as conversation grows |
| Operating loop | Structural | Every task cycle reinforces grounding, verification, and upkeep | High — each iteration is fresh |
| Quality checklists at end | Content (recency) | Last thing the agent reads before responding | Moderate — effective for output quality |
| Note-taking / plan files | Structural | Agent writes objectives into recent context, keeping them in attention | High — objectives are literally in the recent conversation |
| Self-reinforcing workflows | Structural | Steps that naturally produce desired behaviour (e.g., verify step forces re-reading intent) | High — behaviour emerges from structure |

## Concrete Positioning Guidance

Based on the primacy-recency effect:

- **Lines 1-20 of the personality:** Highest persistence. Identity, role, autonomy grant, and the most critical universal standards belong here.
- **Lines 20-60:** Strong persistence. Startup routines, source hierarchy, and version control stance.
- **Lines 60-120:** Moderate persistence. Operational details — upkeep, parallelisation, note capture. These benefit most from structural reinforcement via the operating loop.
- **Final 20 lines:** Strong persistence (recency). Communication style, quality checklist, and formatting norms.

Instructions in the moderate-persistence zone (lines 60-120) should be reinforced by at least one structural mechanism. If the operating loop includes an "update context" step, the upkeep instruction does not need to rely solely on being remembered — the loop naturally triggers the behaviour.

## How Long Conversations Cause Instruction Drift

Over a long conversation (50+ turns), several mechanisms cause drift:

1. **Context window pressure.** The personality file represents a shrinking fraction of total context. At turn 5, the personality might be 10% of context; at turn 50, it might be 1%.
2. **Recency bias.** The most recent turns dominate attention. If recent turns involved a specific coding pattern, the agent gravitates toward continuing that pattern even if the personality says otherwise.
3. **Implicit instruction override.** If the user approves output that violates a personality instruction (e.g., accepts a shallow commit message), the agent infers that the instruction is not important and stops following it.
4. **Accumulated conversational norms.** The conversation develops its own norms through repetition. If the first three tool calls used a particular pattern, that pattern becomes the conversational norm regardless of personality instructions.

## Structural Defences Against Drift

1. **Operating loops** — every iteration is a fresh reinforcement cycle. The agent does not need to remember "update documentation" from the personality if the loop step is "update context where the work created drift."

2. **Note-taking and plan files** — when the agent writes its objectives into a plan file or notes, those objectives appear in recent context. They are literally the most recent thing the agent read. This converts a content-persistence problem (remembering the personality) into a recency advantage (the plan file is recent). Manus (2025) calls this "recitation" — constantly updating todo.md files step-by-step so that objectives are recited into the end of context, keeping goals in the agent's recent attention span without requiring architectural changes.

3. **Quality checklists as recency anchors** — placing the quality checklist at the end of the personality exploits recency. Placing verification steps at the end of skill invocations exploits recency again. The agent's last read before producing output contains the quality standards.

4. **Self-reinforcing step dependencies** — design workflow steps that require consulting context before proceeding. "Verify against the architecture file" forces the agent to re-read the architecture, which naturally grounds it in the project's actual state.

## 2026-04-18 refinement — Drift is a bounded equilibrium, not runaway decay

Dongre et al. 2025 (arXiv 2510.07777) measured drift formally as turn-wise KL divergence from a goal-consistent reference policy. Key findings:

- Drift **does not monotonically degrade**. It stabilises at a bounded equilibrium specific to the model and conversation.
- Reminders at turns 4 and 7 produced **7-12% KL reduction** and +0.46-0.74 judge-score gain.
- LLaMA-3.1-70B baseline equilibrium D* = 14.8; 8B = 20.4.
- The effect of reminders is saturating — doubling frequency does not double the benefit.

**Implications for personality design:**

- The right mental model is "we are operating at a steady-state drift level; periodic interventions reduce it" — not "drift accelerates catastrophically."
- Reminders have an optimal cadence and it's model-specific. For a 60-turn conversation, reminders every ~15 tool calls is a reasonable starting point.
- Panic framings ("don't lose focus!") are counterproductive — they trigger context anxiety on Sonnet 4.5 (see [12.10](12-failure-catalogue.md)) and reinforce exhortation patterns that absorb sycophantically.

Lee et al. COLM 2024 (arXiv 2402.10962) is the foundational drift paper — >30% degradation after 8 dialogue turns. Dongre 2025 refines this with bounded-equilibrium framing. Both citations are load-bearing for the personality's approach to drift.

## Additional structural defence: obligation-audit step

Reliability-critical personalities should add an explicit obligation-audit step to the operating loop — a structural requirement that the agent produces an evidence ledger before declaring completion. This is the personality-layer analogue of a Claude Code Stop hook. See [10-structural-defences.md](10-structural-defences.md).
