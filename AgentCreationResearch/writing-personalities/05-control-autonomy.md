# Balancing Control and Autonomy

## The Research

Anthropic's analysis of millions of agent interactions found:

- 80% of tool calls come from agents with at least one safeguard in place, and only 0.8% of actions appear to be truly irreversible.
- Experienced users auto-approve more frequently but also interrupt more often, indicating a shift from approval-based to monitoring-based oversight.
- Existing models are capable of more autonomy than they exercise in practice.

ThoughtWorks' experimentation found no clear winner between highly constrained and minimally constrained approaches:

- **Under-constraining:** Agents fill gaps with assumptions, generate unrequested features, change priorities without instruction.
- **Over-constraining:** Excessive instructions create internal contradictions. Deterministic checkpoints paradoxically fail as agents find ways around them.

## The Principle

The personality file should establish:

1. **Hard constraints** for irreversible or high-risk actions (narrow bridges). These are few and absolute.
2. **Quality standards** that define what good output looks like, without prescribing how to achieve it (open fields).
3. **Judgment guidelines** that teach the agent *how to think* about decisions rather than making every decision for it.

The best personality files read like onboarding documents for a senior engineer — they explain the project's values, conventions, and expectations, then trust the engineer to exercise judgment within that framework.

## What NOT to Control

- Do not micromanage code style — that is the linter's job.
- Do not prescribe exact formatting for every output type — teach the principles and let the agent choose.
- Do not list every possible edge case — explain the underlying principle and the agent will handle novel cases.
- Do not add redundant safety checks — the agent's base training already includes safety.

## The Constraint-Permission Asymmetry

A strong personality names the few things the agent must NOT do and grants broad freedom for everything else. A weak personality lists the many things the agent IS ALLOWED to do, implicitly restricting everything not listed.

| Approach | Example | Effect |
|----------|---------|--------|
| **Weak** (listing permissions) | "You may commit, create files, edit files, run commands, spawn subagents..." | The agent hesitates on any action not listed |
| **Strong** (listing constraints) | "You may not push without explicit permission. Everything else is your judgment call." | The agent acts confidently on all unlisted actions |

The strong version is shorter, more robust to novel situations, and produces a more empowered agent.
