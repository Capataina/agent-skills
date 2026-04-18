# Instruction Craft

This section covers the literal sentence-level craft of writing instructions — how word choices, framing patterns, and emphasis affect agent behaviour. This is the most impactful area for quality improvement because subtle wording differences produce large behavioural differences.

## Three Tiers of Instruction Wording

Instructions fall into three tiers, each with a distinct wording pattern:

**Tier 1 — Constraints (inviolable structural rules):**
Imperative voice, no hedging, structural justification attached.

| Weak | Strong |
|------|--------|
| Try to keep SKILL.md short. | SKILL.md must remain under 500 lines. This is a context engineering constraint — the body loads every time the skill triggers, and token cost beyond 500 lines degrades reasoning on unrelated tasks. |
| References shouldn't be too nested. | Reference files must not point to other reference files. When references nest, agents partially read files, resulting in incomplete information. |

**Tier 2 — Guidelines (recommended practices with reasoning):**
Recommendation with quantified reasoning. The agent understands the trade-off and can make exceptions when justified.

| Weak | Strong |
|------|--------|
| Use a few examples. | 3-5 examples is the optimal range. Below 3, the agent lacks diversity to generalise. Above 5, token cost outweighs quality gains. Research shows major improvements after 2 examples and a plateau around 4-5. |
| Keep checklists reasonable. | A simple skill needs 5-8 checklist items. A complex skill might need 12-15. Beyond 15, attention dilutes and omission errors increase (IFScale research: models shift to omission beyond saturation). |

**Tier 3 — Principles (direction with freedom):**
A goal statement that the agent can pursue through whatever means it judges best.

| Weak | Strong |
|------|--------|
| Make the output good. | Use the representation that makes the information clearest — tables for comparisons, trees for hierarchies, diagrams for flows, prose for narratives. The goal is maximum clarity for the reader. |
| Be thorough but not too long. | Every section should carry enough information to be useful on its own. If it can be said in one line, say it in one line. If it needs a page, give it a page. Depth should match the judgement involved, the variation across projects, and the cost of mistakes. |

**Evaluation test:** For every instruction in a skill, identify which tier it belongs to. If a Tier 2 guideline is worded like a Tier 1 constraint (imperative, no hedging), it will over-constrain the agent. If a Tier 1 constraint is worded like a Tier 3 principle (vague direction), it will be ignored when it matters most.

## The Scenario-List Anti-Pattern

This is the single most impactful failure pattern discovered in practice. It deserves thorough treatment because it is pervasive, subtle, and produces behaviour that looks like agent disobedience but is actually instruction-following taken literally.

**The pattern:** When instructions include specific examples of when to apply a behaviour, the agent treats the examples as an exhaustive list. If the current situation does not match one of the listed scenarios, the agent skips the behaviour entirely.

**Example — the failing instruction:**

> After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes with a descriptive message.

What happens: The agent completes a refactoring (not a "task," "bug fix," or "meaningful chunk" in its interpretation) and does not commit. It finishes writing documentation and does not commit — documentation was not in the list. It reorganises imports and does not commit. The three scenarios became the complete universe of commit-worthy events.

**Why it happens:** LLMs are pattern-matchers. When they see a list of specific scenarios, they interpret that list as defining the scope of the instruction. The instruction "commit after X, Y, or Z" is parsed as "commit if and only if X, Y, or Z." The "or" is read as exclusive rather than illustrative. This is consistent with research on instruction-following — agents comply with the literal text, and a list of conditions is literal text defining when the behaviour applies.

**The fix:** State the principle and the default stance, then describe only what PREVENTS the behaviour, not what triggers it.

| Failing Version | Fixed Version |
|----------------|---------------|
| After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes with a descriptive message. | Commit early and often. The only constraint is: never push to a remote without explicit permission. |
| When you encounter a naming inconsistency, a dead import, or a formatting issue during your work, fix it immediately. | Fix incidental quality issues as you encounter them. Do not ignore small problems because they are not the current task. The only exception is when a fix would change behaviour in code you are not currently testing. |
| If the user asks for help, wants to discuss architecture, or needs debugging assistance, engage conversationally. | Default to conversational engagement. The only time to skip conversation is when the user has given an explicit, unambiguous command that requires no clarification. |

**The structural pattern of the fix:**

1. State the default behaviour as the norm (commit, fix, engage).
2. State what prevents or constrains the behaviour (no push, no behaviour-changing fixes, no skipping when ambiguous).
3. Do NOT list scenarios that trigger the behaviour — the default stance means it is always on.

**How to detect it during evaluation:** Search the skill for instructions containing comma-separated scenarios ("after X, Y, or Z," "when you encounter A, B, or C," "if the user asks for D, E, or F"). Each one is a candidate for the scenario-list anti-pattern. Ask: "Would the agent skip this behaviour in a situation not listed?" If yes, rewrite using the default-stance pattern.

## Quality Bars vs. Procedures

Quality bars describe the standard the output must meet. Procedures describe the steps to produce the output. Quality bars produce better agent output because they empower the agent to find the best path to the standard. Procedures constrain the agent to a specific path that may not be optimal for the current situation.

| Type | Example |
|------|---------|
| Quality bar | Every finding must include evidence from the actual code, not assumptions about what the code probably does. |
| Procedure | Read lines 1-100 of each file, then check for unused imports, then check for dead functions, then... |
| Quality bar | The description must activate correctly for any reasonable phrasing of the skill's core use case. |
| Procedure | Write five trigger phrases, test each one, then add negative triggers for adjacent skills. |

**When procedures are appropriate:** When the operation is deterministic and the agent cannot derive the correct sequence from principles alone (script execution order, file creation sequence where later files depend on earlier ones, API call chains). These are narrow-bridge situations.

**When quality bars are appropriate:** Everything else — analysis, writing, evaluation, creative work, judgement calls. These are open-field situations where the agent's reasoning about how to meet the bar will outperform a prescribed procedure.

**Evaluation test:** For every procedural instruction in a skill, ask: "Could this be replaced with a quality bar that the agent could meet through its own reasoning?" If yes, the procedure is over-constraining.

## Emphasis Calibration

Research on emphasis (2024) found that **small open-source LLMs struggle to understand emphasised text**, while commercial LLMs **may overinterpret emphasised text**. Stricter format constraints generally lead to greater performance degradation in reasoning tasks.

From Anthropic's skill-creator:

> "If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important."

**Calibration guide:**

| Emphasis Level | When Justified | When Harmful |
|----------------|----------------|--------------|
| **CAPS + bold** (e.g., "NEVER push without permission") | Genuinely inviolable safety or data integrity constraints. Actions that cannot be undone. | Stylistic preferences, recommended practices, anything the agent could reasonably override with good judgement. |
| **Bold only** (e.g., "must remain under 500 lines") | Structural constraints from hard rules. Constraints with measurable degradation if violated. | Soft recommendations. Anything where "usually" or "typically" would be more honest. |
| *Italics* (e.g., "why it matters") | Drawing attention to reasoning, principles, or key concepts within flowing text. | Not harmful, but overuse dilutes the signal. |
| Plain text | Everything else. The vast majority of instructions should be plain text with reasoning. | Never harmful on its own, but a skill written entirely in plain text with no emphasis may bury its most critical rules. |

**The over-emphasis failure mode:** When a skill uses CAPS and bold liberally, the agent treats everything as equally critical. This is equivalent to nothing being critical. The agent cannot distinguish genuinely inviolable constraints from emphatic preferences, so it either over-complies (rigid, conservative output) or abandons some constraints entirely (IFScale omission errors).

**Evaluation test:** Count the number of CAPS/bold emphasis instances in a skill. If more than 3-5 across the entire skill directory, the emphasis is diluted. Each instance should be a genuine hard rule.

## Framing: Positive Over Negative

Research consistently shows positive framing outperforms negative framing. The "Pink Elephant Problem" has an architectural explanation: research presented at CVPR 2024 found that in attention-based models, the embedding for "not A" has a cosine similarity of **0.792** with "A" but only **0.273** with the intended meaning — the model literally represents "don't do X" almost identically to "do X" in embedding space. A 2025 study across 9 models found larger models handle negation substantially better (Spearman correlation 0.867 between model size and negation accuracy), but the fundamental representation problem persists. Anthropic's official documentation explicitly advises telling the agent what to do rather than what not to do.

| Negative (weaker) | Positive (stronger) |
|--------------------|---------------------|
| Do not use shallow bullet lists. | Use the representation that makes the information clearest — tables, diagrams, trees, or bullets depending on the content. |
| Never create thin files. | Every file should carry enough memory value that a reader understands the topic without needing to re-derive it from code. |
| Don't repeat information across files. | Each piece of information has one canonical home. Other files reference it by path rather than restating it. |
| Avoid vague section headers. | Every section header should tell the reader what they will learn by reading that section. |

**When negative framing is appropriate:** When the positive instruction alone is insufficient because the failure mode is non-obvious. In these cases, lead with the positive instruction and add the negative as context:

> Use the representation that makes the information clearest. Note: agents frequently default to bullet lists even when a table would be far more readable for comparative data — actively consider alternatives before choosing bullets.

## Consistent Terminology

Using "case," "ticket," and "issue" interchangeably confuses agents, especially as conversation length increases. Research on prompt sensitivity (2024) provides hard numbers: **"A slight change in a class definition can lead to drastic changes in the final prediction."** Sensitivity values ranged from 0.005 to 0.404 across models. The mechanism is **surface form competition** — when multiple terms refer to the same concept, they fight for probability mass, fragmenting attention and producing inconsistent output.

**Evaluation test:** List the 5-10 most important concepts in the skill. Search the entire skill directory for all terms used to reference each one. If any concept has multiple terms, flag it. Pick one and standardise.

## Instructions That Persist

LLMs exhibit a primacy-recency effect — they attend most to information at the beginning and end of context. Instructions in the middle of long interactions get progressively less attention. To combat this:

- Place the most critical rules early in the SKILL.md body.
- Use the quality checklist at the end as a recency anchor for important requirements.
- The agent's own note-taking (plans, progress tracking) pushes objectives into recent attention.

**Evaluation test:** Identify the 3 most important behavioural instructions in the skill. Are they in the first quarter of SKILL.md or the quality checklist? If they are buried in the middle, they will degrade over long conversations.
