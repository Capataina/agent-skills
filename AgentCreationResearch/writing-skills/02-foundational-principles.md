# Foundational Principles

These are the philosophical commitments that inform every specific rule and recommendation in this document. They are not optional — they are the foundation on which quality evaluation rests.

## The Agent Is Already Smart

The single most important design principle: **modern LLMs are already extremely capable.** Every piece of information in a skill should pass the challenge: "Does the agent really need this, or is it something the agent already knows?" Do not explain what PDFs are. Do not teach software engineering fundamentals. The skill's job is to provide what the agent *cannot* derive from its training — your specific conventions, your specific quality standards, your specific edge cases, and the reasoning behind them.

This does not mean skills should be thin. It means every token should carry signal. A 500-line SKILL.md where every line teaches the agent something it would not otherwise know is better than a 100-line SKILL.md padded with obvious instructions and a 200-line SKILL.md that wastes half its tokens restating common knowledge.

There is a counterweight to this principle: research from "What Prompts Don't Say" (2025) found that unspecified requirements are **2x as likely to regress** across model updates (5.9% vs 3.0% regression rate). Relying on the model to "figure it out" works today but may break on the next model version. The principle is not "omit everything the agent knows" — it is "omit the obvious, but explicitly state your specific quality standards and conventions, because those are what break silently when models change."

## Explain Why, Not Just What

Anthropic's own skill-creator captures this principle precisely:

> "Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen."

When you explain *why* something matters, the agent generalises from the explanation. It can handle edge cases you never anticipated because it understands the underlying principle. When you only say *what* to do, the agent follows the letter of the instruction and may violate the spirit in novel situations.

| Version | Instruction | Why It's Better/Worse |
|---------|-------------|----------------------|
| Weak | Always use bullet lists for system document sections. | Rigid. Agent uses bullets even when a table or diagram would be clearer. |
| Strong | Use the representation that makes the information clearest. Bullets work for concise takeaways, tables for dense inventories, diagrams for flows that are awkward in prose. The goal is maximum clarity for both human readers and future agents. | Principled. Agent chooses the best representation for each situation because it understands the goal. |

## The Bridge and Field Analogy

Calibrate instruction specificity based on risk:

- **Narrow bridge (high risk, one safe path):** Database migrations, file format specifications, API contracts. Provide exact instructions. The agent has no latitude because getting it wrong is catastrophic.
- **Open field (low risk, many valid paths):** Analysis, writing, creative exploration, code structure decisions. Provide direction and quality standards. The agent has full latitude because many good solutions exist.

Most of the content in this archive's skills falls on the "open field" end. The structural rules (folder layout, naming conventions, file roles) are narrow bridges. The content within those structures (how to explain a subsystem, what depth to reach, what visual representations to choose) is open field.

## Structure Fixed, Content Free

This principle directly follows from the bridge-and-field analogy. In skill design:

- **Fix the structure:** Folder layout, file naming, required sections, output locations, script execution order. These are deterministic and must be consistent.
- **Free the content:** How the agent explains things, what depth it reaches, what formatting it chooses, how it reasons about the domain. These are judgement calls where agent autonomy produces better results than rigid templates.

Research directly supports this split. A 2024 study ("Let Me Speak Freely?") found that **stricter format constraints cause 10-15% performance degradation on reasoning tasks** — forcing format compliance during reasoning interferes with the reasoning itself. The mechanism: when the model must simultaneously reason about the problem and comply with format restrictions, the format constraints consume cognitive capacity that would otherwise go to the actual task. This is why fixing structure at the skill level (folder layout, file naming) works — it is decided before reasoning begins — while constraining content within the output harms quality.

**Evaluation test:** For every instruction in a skill, ask: "Is this fixing structure or constraining content?" If it constrains content without a clear failure-mode justification, it should be rewritten as a principle or removed.
