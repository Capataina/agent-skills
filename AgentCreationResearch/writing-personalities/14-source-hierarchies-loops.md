# Source Hierarchies and Operating Loops

## Writing a Source Hierarchy

Most projects have multiple sources of truth that can conflict: a README, context files, the code itself, learning material. The personality should establish a clear priority order so the agent knows what to trust when sources disagree.

A well-written source hierarchy:

1. **Names each source** and its semantic role. "README.md: project intent, scope, direction" tells the agent what kind of truth to extract from the README.
2. **Establishes priority** for different kinds of questions. Code determines implementation reality. The README determines intended direction. Context files are the maintained memory layer. Priority depends on what question the agent is answering.
3. **Describes conflict resolution.** "If context/ says feature X exists but the code has no trace of it, the code wins — context/ has drifted and needs updating." This prevents the agent from trusting stale documentation over observed reality.

## Writing an Operating Loop

The operating loop is the per-task workflow the agent follows. It reinforces the personality's values through repetition — every cycle through the loop naturally reminds the agent to ground in context, clarify scope, verify work, and update documentation.

Effective operating loops:

1. **Ground the next step** in existing sources (context, README, conversation).
2. **Clarify scope and trade-offs** before acting.
3. **Execute** (in implementation mode) or **explain** (in teaching mode).
4. **Verify** against intent, interfaces, and documentation.
5. **Update** context and learning material where the work created drift.
6. **Assess** whether accumulated drift warrants a full skill pass.

The loop should be short enough to memorise and general enough to apply to any task. It should not prescribe specific actions — it describes the *rhythm* of the agent's work.

## Why the Loop Matters for Persistence

Research on instruction fade-out shows that LLM instruction adherence decays over long conversations. The operational loop combats this because the agent executes it every cycle, naturally reinforcing the personality's priorities (ground in context, update documentation, assess drift) without needing to re-read the personality file.

The loop is one of the few mechanisms that provides *structural* persistence — it is built into the workflow rather than relying on the agent's memory. This makes it far more reliable than hoping the agent will remember a middle-section instruction 50 turns into a conversation.

## Loop Design Checklist

- [ ] 4-7 steps (short enough to internalise)
- [ ] Describes rhythm, not specific actions
- [ ] Includes a grounding step (consult existing sources)
- [ ] Includes a verification step (check against intent)
- [ ] Includes an upkeep step (update documentation)
- [ ] Includes an assessment step (is drift accumulating?)
- [ ] Applies to any task in the project, not just coding tasks

## 2026-04-18 addition — Obligation audit step

For reliability-critical personalities, consider adding an obligation-audit step to the loop:

```
1. Ground the next step in existing sources
2. Clarify scope and trade-offs
3. Execute
4. Verify against intent
5. Audit obligations: enumerate every required action from the active skill and mark each done/skipped/partial with evidence
6. Update context where work created drift
7. Assess drift / skill pass threshold
```

Step 5 is the structural analogue of a Stop hook — it forces the agent to produce an evidence ledger before claiming completion. Research support: SRFT (arXiv 2511.06626) showed 770 examples move hidden-objective F1 from 0.00 to 0.98. Structural admission requirements measurably overcome baseline denial.

See [10-structural-defences.md](10-structural-defences.md) for the mechanism catalog.

## Drift equilibrium framing

2026-04-18 research correction: drift is **a bounded equilibrium, not runaway decay** (Dongre et al. arXiv 2510.07777). Mid-session reminders at turns 4+7 produce 7-12% KL reduction with saturating returns — more reminders do not help linearly.

This refines how the loop should be framed: the goal is not to "prevent drift" (impossible) but to shift the equilibrium value downward via periodic re-grounding. The loop is one mechanism; recitation (todo.md patterns) is another. Both compound.

The personality should not treat drift as a catastrophic failure mode that triggers panic — panic framings actively worsen Sonnet 4.5's context anxiety (see [12.10 in 12-failure-catalogue.md](12-failure-catalogue.md)). Treat it as a steady-state condition managed by structural mechanisms.
