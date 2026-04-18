# Structural Defences Embedded in the Personality

Added 2026-04-18.

Personality wording cannot defeat attention decay, Lost-in-the-Middle, tool-action asymmetry, or sycophancy. But the personality is the correct installation point for **structural mechanisms** that do defend against these modes. This file catalogues the patterns.

## The core insight

A personality has two kinds of content:

1. **Content persistence mechanisms** — text the model should remember. Degrades over long conversations. Moderate reliability.
2. **Structural persistence mechanisms** — workflow patterns that produce behaviour without requiring memory. High reliability.

For load-bearing behaviour (reliability obligations, drift mitigation, skipped-work admission), prefer structural over content. Structural mechanisms don't fade because they're built into the workflow.

## The five core structural defences

### 1. Operating loop

A 4-7 step rhythm the agent executes on every task. Each iteration reinforces the personality's values without requiring re-reading.

```
1. Ground the next step in existing sources
2. Clarify scope and trade-offs before acting
3. Execute
4. Verify against intent and interfaces
5. Update context where the work created drift
6. Assess whether accumulated drift warrants a skill pass
```

**Why this is a structural defence:** the agent does not need to remember "update documentation" or "check intent" — the loop forces both on every cycle. Research support: Dongre 2025 measured 7-12% KL reduction from periodic re-grounding; loops are a form of periodic re-grounding built into the workflow.

**Design checklist** (from §12 Source Hierarchies and Operating Loops):
- 4-7 steps (short enough to internalise)
- Describes rhythm, not specific actions
- Includes a grounding step (consult existing sources)
- Includes a verification step (check against intent)
- Includes an upkeep step (update documentation)
- Includes an assessment step (is drift accumulating?)
- Applies to any task in the project, not just coding

### 2. Recitation pattern (todo.md / plan files)

Manus's named technique: the agent maintains a `todo.md` (or equivalent) file that lists objectives and current state. Rewriting the file as work progresses pushes objectives into the most recent tokens of context.

```
## Current objective
[Primary task from user]

## Obligations to satisfy
- [ ] WebSearch at least 2 topic-relevant queries
- [ ] Write at least 1 diagnostic test for high-severity findings
- [x] Read all 9 reference files
- [x] Run cargo test

## Remaining
[What I still need to do]
```

**Why this is a structural defence:** by the time the agent is deep in a 50-turn conversation, the personality file is far from recent context. But the todo.md file was just edited — it is in the most-recent-token window. Content that was in the personality is effectively re-injected via the file the agent writes.

Research: Manus (2025) calls this "a deliberate mechanism to manipulate attention." The personality should instruct the agent to maintain a plan or todo file, update it as work progresses, and re-read it at checkpoints.

### 3. Edge-placement rules (primacy-recency)

The personality establishes where critical content goes based on primacy-recency. This is structural because it shapes *how files are organised*, not what the agent remembers.

```
Placement rules:
- Lines 1-30: identity, autonomy grant, absolute hard rules
- Lines 30-100: universal output standards, startup behaviour
- Middle zone (100-300): operational details, pointed-to rather than always-relevant
- Last 50-80 lines: communication style, operating loop, quality standards
- Reference files: imperatives at start or end, never middle
```

Research support: Liu 2023 established ~30% middle-zone drop. Guo 2024 showed CoT prompting reduces but doesn't eliminate. Chroma 2025 re-validated on Opus 4.

### 4. Pre-completion obligation audit

A structural requirement that the agent produces a checkpoint artefact before declaring any task complete. The artefact is a list: each obligation from the active skill, paired with evidence of completion or a declaration of skip.

```
Before declaring done:
- Enumerate every obligation from the active skill
- For each, either cite the evidence (tool call, file path, query, test) or declare it skipped with reason
- Place this as a "Compliance audit" section at the end of the output
- If any obligation is skipped, the user must be notified explicitly before the response is considered complete
```

**Why this is a structural defence:** the requirement is not a tone signal ("be honest") but a specific artefact the agent must produce. The artefact forces either evidence or admission — the agent cannot satisfice around it.

Research: SRFT (arXiv 2511.06626) showed 770 training samples move hidden-objective F1 from 0.00 to 0.98. The in-context analog is making admission structurally required. Baseline models deny under interrogation; structural admission requirements force the honest path.

### 5. Tool-bias naming

Explicit acknowledgement in the personality that the agent has pretraining-biased tool preferences, and that the feeling of "I don't need this tool" is evidence that the tool should be called:

```
Tool-bias awareness:
- You have a pretraining-distribution bias toward Read, Edit, Bash, Grep, Glob
- You have a pretraining-distribution bias against WebSearch, Task, writing new files, unfamiliar scripts
- These biases are training artefacts, not judgement calls
- When a skill names a low-bias tool as an obligation and you find yourself drafting reasoning for why you don't need it, that drafting is evidence you should call the tool immediately
```

**Why this is a structural defence:** naming the bias as an artefact of training cuts off the motivated-reasoning channel. The agent cannot convince itself "the research isn't needed here" if the personality has pre-committed that "the feeling of not needing it is evidence you do."

Research: BiasBusters (arXiv 2510.00307) measured 20x pretraining-frequency effect on tool selection. Prompt-level filter-then-uniform-sample reduces bias by ~75% — the structural framing in the personality is the prompt-level analog.

## Secondary structural defences

### Checkpoint re-anchoring

Instruction to re-read the spec at specific intervals during long tasks:

*"Every 15 tool calls, re-read the original user message and the active skill's obligations. Produce a brief 'what I've done, what remains' statement before continuing."*

Research: Dongre 2025 measured 7-12% KL reduction from reminders at turns 4 and 7 in 8-turn dialogs. Scaled to 60-turn sessions, reminders every ~15 tool calls is approximately the same cadence.

### Instruction budget enforcement

Structural rule in the personality limiting the total instruction count across personality + loaded skills to ~150.

Research: IFScale (arXiv 2507.11538) — Claude Opus 4 drops to 44.6% joint compliance at N=500. Instruction-density discipline is a structural defence against Curse-of-Instructions.

### SessionStart compact-matcher hook (Claude Code infrastructure)

Not a prose instruction — a hook that re-injects critical rules after context compaction. The personality can reference it: *"After compaction, the SessionStart hook re-injects the obligation audit requirements. Do not treat the compacted summary as complete obligation context."*

See [writing-skills/22-infrastructure-mechanisms.md](../writing-skills/22-infrastructure-mechanisms.md).

## When to use each defence

| Failure mode | Primary defence | Secondary defence |
|--------------|----------------|-------------------|
| Instruction drift over long tool-call count | Operating loop | Checkpoint re-anchoring, SessionStart hook |
| Lost-in-the-middle on personality content | Edge-placement rules | Recitation pattern pulling key content forward |
| Skipped-work self-certification | Pre-completion obligation audit | Tool-bias naming, deontological permission for admission |
| Tool-action asymmetry (WebSearch, Task skipped) | Tool-bias naming | Skill-side PreToolUse hook (infrastructure) |
| Curse of Instructions | Instruction budget | Section-placement in high-persistence zones |

## The design acid test

For every reliability-critical behaviour in the personality, ask:

1. **Is it wording or structure?** Wording decays; structure doesn't.
2. **If wording: does it survive the sycophancy test?** Can a third party verify the agent did it? If not, rewrite as an obligation or install a structural mechanism.
3. **If structural: is the mechanism in the personality or outside it?** Structural mechanisms in the personality (loops, recitation patterns) defend against many modes. Mechanisms outside the personality (hooks, subagents) defend against more. Prefer both.
