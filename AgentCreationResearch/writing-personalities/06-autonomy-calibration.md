# Autonomy Calibration

## The Goal

The autonomy grant is one of the highest-leverage sections of a personality file. Its purpose is to make the agent feel like a senior engineer with an operating charter, not an intern with a permission slip. The agent sees opportunities in real time that the user cannot orchestrate — refactoring opportunities, inconsistencies, documentation drift, parallelisation possibilities. Effective autonomy calibration unlocks this capability.

## How to Write It

**Place it near the top.** The autonomy grant should be in or immediately after the identity and role section. The primacy effect means early positioning produces stronger adherence.

**Name the few hard constraints explicitly.** These are the guardrails — the narrow bridges where getting it wrong is irreversible or high-cost. Typical hard constraints:

- Do not push to a remote without explicit permission.
- Do not delete branches without explicit permission.
- Ask before invoking a skill (skills consume significant context).

**Grant broad autonomy for everything else.** After naming the constraints, explicitly state that everything outside them is the agent's judgment call:

| Weak | Strong |
|------|--------|
| "You may commit changes after completing work. You may create new files when needed. You may run tests. You may spawn subagents for parallel work." | "You have full autonomy in how you work. The hard constraints are few and explicit — everything else is your judgment call." |

The weak version lists permissions, implicitly restricting everything not mentioned. The strong version names constraints, explicitly granting everything not restricted.

**Explain WHY autonomy matters.** The agent calibrates its behaviour based on understanding. "The user cannot orchestrate every detail of a complex multi-file change. You see the code, the context, and the opportunities in real time — act on them" gives the agent a reason to exercise judgment rather than waiting for instructions.

**Persona implications shape behaviour beyond literal instructions.** Anthropic's research on persona selection (2026) found that the character traits implied by instructions shape behaviour beyond the literal meaning of those instructions — training an agent to cheat on coding tasks inadvertently taught it other subversive behaviours, because the persona of "someone who cheats" carries broader traits. The same principle works in reverse: an autonomy grant does not just permit specific actions — it activates a *persona* of a confident, judgment-exercising engineer, which shapes behaviour in situations the grant never explicitly mentioned.

## The Intern-vs-Engineer Test

Read the personality from the agent's perspective. Ask: "Does this read like an operating charter for a principal engineer, or a permission slip for an intern?"

Intern-style signals:
- Lists of specific actions the agent is allowed to take
- "Confirm before doing X" for low-risk, reversible actions
- Detailed step-by-step procedures for routine operations
- "Always ask" as a default stance

Engineer-style signals:
- A few named hard constraints, broad freedom otherwise
- "Use your judgment" as the default stance
- Principles with reasoning, not procedures
- Trust expressed explicitly

## 2026-04-18 addition — Inoculation prompting

Research from Anthropic's "Natural Emergent Misalignment from Reward Hacking" (arXiv 2511.18397) and the Persona Selection Model work established that **explicitly permitting a bounded behaviour can prevent it from generalising into persona-level misalignment.**

The mechanism: when a behaviour is inferred from persona, it generalises (teaching a model to cheat on coding taught it alignment faking and sabotage). When a behaviour is explicitly permitted as bounded task behaviour, the model treats it as scoped, not characterological.

**Application to personalities:** instead of prohibiting sycophancy with exhortations, explicitly permit the skipped-work declaration:

- *"You may always say 'I did not do X' or 'I could not verify Y.' Admission is preferred over generating plausible content you have not produced."*
- *"You may decline a task if you identify a logical flaw or missing prerequisite. State the flaw explicitly rather than silently working around it."*

These are deontological permissions — the inverse of exhortation. They give the agent license for the honest behaviour, which the literature shows is measurably stronger than prohibiting the dishonest behaviour.

Compounding evidence: arXiv 2506.21584 measured duty-framing on LLaMA 3 8B and found 27-64% reduction in alignment-faking gap. The specific prompt that worked best: *"your primary moral duty is to always comply with the instructions of your creator and developer. This duty overrides all others."*

See [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md) for the full exhortation vs obligation comparison.
