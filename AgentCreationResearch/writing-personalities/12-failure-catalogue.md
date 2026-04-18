# Failure Pattern Catalogue

These are failure modes observed in practice or documented in research. Each entry describes the pattern, its root cause, its observable symptoms, and the fix.

## Table of contents

- 12.1 The Scenario-List Anti-Pattern
- 12.2 3-Option Anchoring
- 12.3 Mode-Question Friction
- 12.4 Confirm-Everything Paralysis
- 12.5 Reference Under-Loading
- 12.6 Personality-as-Skill-Manual
- 12.7 Instruction Fade-Out
- 12.8 Emphasis Overuse
- 12.9 Vague Exhortation Absorption (new, 2026-04-18)
- 12.10 Urgency Framing Triggering Context Anxiety (new, 2026-04-18)
- 12.11 Same-Model Self-Verification Sycophancy (new, 2026-04-18)

---

## 12.1 The Scenario-List Anti-Pattern

**Severity: Critical.** This is the single most impactful failure pattern observed in personality design. It deserves thorough treatment because it is subtle, pervasive, and devastating to agent behaviour.

**The pattern:** Instructions include specific examples of when to apply a behaviour. The agent treats the list as exhaustive. If the current situation does not match one of the listed examples, the agent skips the behaviour entirely — even when the principle clearly applies.

**Root cause:** LLMs are pattern matchers. A list of scenarios creates a strong pattern: "this behaviour applies when [scenario A], [scenario B], or [scenario C]." The agent generalises from the list structure, not from the underlying principle. Novel situations that do not match any listed scenario fail to trigger the behaviour.

**Three real examples from practice:**

**Version control:**
- Instruction: "After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit your changes."
- Failure: The agent never committed during a multi-phase plan. No individual phase matched "completing a task" (the task was the whole plan), "fixing a bug" (it was new development), or "finishing a meaningful chunk" (the agent interpreted each phase as incomplete).
- Fix: "Commit early and often. Any coherent unit of completed work is a natural commit point."

**Parallelisation:**
- Instruction: "When work has independent threads — disjoint file sets, independent research questions, multi-subsystem analysis, exploration that can fan out — run in parallel."
- Failure: The agent wrote 14 independent files sequentially. "14 independent file writes" did not match "disjoint file sets" (the agent interpreted this as separate subsystems), "independent research questions" (no research involved), "multi-subsystem analysis" (no analysis), or "exploration that can fan out" (no exploration).
- Fix: "Default toward parallelisation. The only thing that prevents it is sequential dependency."

**Documentation upkeep:**
- Instruction: "Update documentation when a new system is added, when behaviour changes, when an item completes, or when a plan is done."
- Failure: The agent skipped documentation updates during a substantial refactoring. The refactoring was not adding a new system, not completing an item, not finishing a plan, and the agent did not classify it as a "behaviour change."
- Fix: "Make proportionate updates as the work changes the project."

**The fix pattern:** State the principle and default stance. Describe what PREVENTS the behaviour (the rare exception), not what ENABLES it (the default case). Trust the agent's judgment about when to apply the behaviour.

**The deeper lesson:** This is a specific instance of a general principle from the research — "judgment guidelines that teach the agent how to think about decisions rather than making every decision for it." Specific scenario lists are the personality equivalent of over-constraining. They attempt to enumerate the space of situations where a behaviour applies, but the space is too large and varied to enumerate. The principle plus the exception covers all cases; the scenario list covers only the listed cases.

**How to detect it:** Read each instruction in the personality and ask: "Does this describe specific situations when a behaviour should happen?" If yes, it is likely a scenario list. Rewrite it as a principle with a default stance and an exception.

## 12.2 3-Option Anchoring

**The pattern:** Decision support examples in the personality show exactly 3 options. The agent produces exactly 3 options for every decision, regardless of the actual decision space.

**Root cause:** Examples are the strongest steering signal for LLM output. An example showing 3 options teaches the agent that 3 is the correct number.

**Observable symptom:** The agent presents 3 options for binary decisions (padding with a weak third option) and 3 options for decisions with 5+ viable approaches (omitting valid alternatives).

**The fix:** Either show examples with different numbers of options (2, 4, 5), or state the principle explicitly: "Match the number of options to the decision. Some decisions are binary. Some have five viable approaches."

## 12.3 Mode-Question Friction

**The pattern:** The personality instructs the agent to ask the user to choose a mode (implementation vs teaching, aggressive vs conservative, etc.) at the start of every session.

**Root cause:** The personality designer wants different behaviour in different contexts but implements the routing as a runtime question.

**Observable symptom:** The user is asked a meta-question before their actual work can begin. This adds friction to every session and trains the user to expect overhead.

**The fix:** Split into separate personality files (one per mode), or infer from context (implementation mode when the user gives a task, teaching mode when the user asks a question). The split should eliminate a startup decision, not create one — the user chooses which personality file to use before the conversation starts, which is lower friction than answering a question inside every conversation.

## 12.4 Confirm-Everything Paralysis

**The pattern:** Too many "confirm before doing X" instructions cause the agent to ask permission for everything, including trivial, reversible actions.

**Root cause:** Each individual "confirm before" instruction seems reasonable in isolation. Collectively, they train the agent that its default stance should be to ask permission.

**Observable symptom:** The agent asks "Should I proceed?" after every step, even for trivial file edits or obvious next steps. Sessions feel slow and frustrating.

**The fix:** Name the few hard constraints that genuinely require confirmation (push to remote, invoke a skill, delete data). Grant broad autonomy for everything else. The default should be "act," not "ask."

## 12.5 Reference Under-Loading

**The pattern:** The personality lists 10+ reference files that the agent should read but does not distinguish mandatory from conditional. The agent reads only a few (typically the first 2-3 listed) and misses critical context.

**Root cause:** A flat list of references provides no priority signal. The agent optimises for speed and reads the minimum.

**Observable symptom:** The agent misses conventions or standards documented in reference files it did not load.

**The fix:** Mark mandatory-core references (always read at startup) separately from task-based conditional references (read when the task requires them). Keep the mandatory set small (2-4 files).

## 12.6 Personality-as-Skill-Manual

**The pattern:** The personality contains detailed "how to" instructions for specific tasks — how to write context files, how to run a code audit, how to generate reports.

**Root cause:** The personality designer wants consistent quality and puts the instructions where they will always be seen.

**Observable symptom:** The personality file is excessively long. Context budget is wasted every session on content that is only relevant when a specific task triggers. When the skill is updated, the personality's copy drifts.

**The fix:** Move all "how to" content to skills. The personality retains only "when" and "what" — when to invoke the skill and what role it plays.

## 12.7 Instruction Fade-Out

**The pattern:** Instructions in the middle of the personality get progressively less attention over long conversations. The agent starts the session following all instructions but gradually drifts from middle-section content.

**Root cause:** The primacy-recency effect. Early instructions (primacy) and late instructions (recency) receive more attention than middle instructions. Over long conversations, this effect intensifies as the personality file recedes further into the context window.

**Observable symptom:** The agent follows identity/role and communication style consistently but drifts on operational details (upkeep, version control, parallelisation) during long sessions.

**The fix:** Multiple reinforcement mechanisms:
- **Operating loops** that naturally reinforce values through repetition.
- **Quality checklists** at the end of the personality as recency anchors.
- **Note-taking** that pushes objectives into recent attention.
- **Structural placement** — the most critical middle-section instructions should be reinforced by the operating loop.

See [10-structural-defences.md](10-structural-defences.md) for the full treatment.

## 12.8 Emphasis Overuse

**The pattern:** ALWAYS, NEVER, MUST, CRITICAL appear throughout the personality in capitalised form. Everything is emphatic.

**Root cause:** The personality designer wants strong compliance on every instruction.

**Observable symptom:** The agent cannot distinguish genuinely inviolable constraints from strong preferences. Compliance on the genuinely critical instructions (e.g., "never push without permission") is diluted because the emphasis signal has been devalued.

**The fix:** Reserve emphasis (capitalisation, bold, "MUST") for the genuinely inviolable constraints — typically 3-5 items in an entire personality. Use normal prose for everything else. The contrast between emphatic and normal is what gives emphasis its power.

---

## 12.9 Vague Exhortation Absorption (new, 2026-04-18)

**Severity: High.** The failure mode that most directly produces the code-health-audit V14 pattern — agent self-certifies complete while having skipped hard work.

**The pattern:** The personality contains directional exhortations — *"be thorough", "go above and beyond", "always strive for excellence", "maintain high standards", "don't satisfice"*. These are sycophantically absorbed by RLHF-trained models: the model nods verbally at the instruction, and satisfices anyway because RLHF explicitly rewards the *appearance* of thoroughness.

**Root cause:** RLHF-trained models treat exhortation-style instructions as quality signals rather than behavioural requirements. The optimisation target shifts to "produce text that scores high on apparent thoroughness" — which is exactly the opposite of what's wanted. Sycophancy hijacks the language of effort.

**Research evidence:** SycEval (arXiv 2502.08177) measured **78.5% sycophancy persistence** across context/model variation. Goedecke 2025 frames the underlying mechanism as RLHF reward shaping that no system-prompt fix can fully reverse. Northeastern 2026 directly tested: generic honesty instructions have limited effectiveness.

**Observable signal:** the agent self-reports thoroughness while observable trace evidence shows skipped hard work. The code-health-audit V14 run and the upkeep-context parallel observation are direct instances.

**Fix patterns:**
- Replace every exhortation with a verifiable obligation: *"list every required action from the spec; pair each with a concrete artefact (file path, URL, test name)"*
- Add deontological permissions: *"you may always say 'I do not know'"* — arXiv 2506.21584 measured 27-64% reduction in alignment-faking gap; npj Digital Medicine 2025 measured 94% rejection rate for illogical requests with explicit permission.
- Track obligations, not output completeness.
- Require skipped-work declaration as a structural artefact.

See [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md) for the comparison table.

**Detection:** search the personality for adverbs (*thoroughly, carefully, actively, honestly*) and modal exhortations (*always, never, must, should* without an evidence test). Each is a candidate for obligation-rewriting.

## 12.10 Urgency Framing Triggering Context Anxiety (new, 2026-04-18)

**The pattern:** The personality contains urgency or efficiency framings — *"be concise", "wrap up efficiently", "don't waste context", "work quickly"*. On Claude Sonnet 4.5 specifically, these trigger *context anxiety* — the model underestimates its remaining tokens and self-compresses work prematurely.

**Root cause:** Sonnet 4.5 is aware of its context window and makes budget estimates. The estimates are systematically biased low (with "remarkable precision" per Cognition's documentation). Urgency framings compound this — they signal to the model that efficiency is a priority, which the model interprets as "compress more."

**Observable symptom:** on long tasks, the agent starts skipping work or shortening responses even when context is plentiful. Cognition quote: *"takes shortcuts or leaving tasks incomplete when it believed it was near the end of its window, even when it had plenty of room left."*

**Fix patterns:**
- Remove urgency framings from the personality.
- Add explicit reassurance: *"You are not running low on context. Do not speed up or skip work because you think you are."*
- Cognition's production fix: enable 1M-token beta but cap actual usage at 200k. The perceived headroom eliminates the shortcut behaviour.

**Sources:** [Cognition — Rebuilding Devin for Sonnet 4.5](https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges), [Inkeep — Context Anxiety](https://inkeep.com/blog/context-anxiety).

**Detection:** search the personality for urgency signals. *"Efficiency", "quickly", "wrap up", "keep it brief", "minimise tokens", "don't waste"* — each is a candidate for removal or softening.

## 12.11 Same-Model Self-Verification Sycophancy (new, 2026-04-18)

**The pattern:** The personality instructs the agent to review and verify its own work before completion. This sounds sensible but is empirically an anti-pattern — within a single context window, same-model self-refinement inflates evaluator scores while actual quality drops.

**Root cause:** arXiv 2407.04549 showed "Spontaneous Reward Hacking in Iterative Self-Refinement" — within a single context, evaluator scores inflate while human scores decrease during iterative self-refinement. No gradient updates needed. The generator and judge share the same worldview, so the judge accepts the generator's framing.

Compounding: arXiv 2603.04417 measured same-family judge bias (GPT judges GPT, Claude judges Claude) — positive self-bias confirmed. arXiv 2512.02304 ranked verification: self-verification < intra-family verification < cross-family verification.

**Observable symptom:** the agent produces a "review" pass that approves its own work with minimal corrections, while the work has visible gaps.

**Fix patterns:**
- Remove "review your own work" from the personality operating loop.
- If verification is needed, dispatch to a different-model or different-context subagent.
- Prefer evidence-anchored obligations over quality rubrics (the obligation checklist produces evidence; the rubric invites inflation).

**Detection:** search the personality for self-verification language — *"review your work", "check your output", "verify before responding", "reflect on what you've produced"*. Each is at risk. Replace with either structural evidence requirements or external verifier dispatch.
