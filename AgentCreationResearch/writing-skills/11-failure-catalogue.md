# Anti-Patterns and Failure Catalogue

This file documents failure modes observed in practice and from research. Each entry includes: symptom, root cause, example of the failing instruction, and the fix. Use this catalogue both for writing new skills and for diagnosing problems in existing ones.

## Research Foundation

Anti-patterns have a nuanced effect:

- **Specific, well-explained anti-patterns work.** A study found that anti-pattern avoidance prompts reduced code weaknesses by 59-64%. The key is specificity and explanation of *why* the pattern is bad.
- **Vague negative instructions backfire.** "Don't make it bad" is noise. "Do not create milestone-based files because they force readers to reconstruct the present from historical slices" is signal.
- **Many negative instructions fragment attention.** A long list of "do not" items creates ambiguity about what the agent *should* do.

## Best Practice for Documenting Anti-Patterns

1. Lead with the positive instruction. State what the agent should do first.
2. Add the anti-pattern as context for *why* the positive instruction matters.
3. Keep anti-patterns few and specific. Each one should describe a concrete failure mode with a clear explanation of the harm.
4. Consider whether the anti-pattern can be reframed as a positive instruction instead.

## Table of Contents

- F1: Scenario-List Exhaustion
- F2: Domain Bias Anchoring
- F3: Decision-Support Cardinality Anchoring
- F4: Reference File Under-Loading
- F5: Instruction Contradiction Across Files
- F6: Template-as-Output
- F7: Mode-Question Friction
- F8: Over-Constraining Collapse
- F9: Stale Internal References
- F10: Verification-Gate Absence (new, 2026-04-18)
- F11: Sycophantic Self-Scoring (new, 2026-04-18)
- F12: Tool-Action Asymmetry (new, 2026-04-18)
- F13: Reference-File Imperative Blindness (new, 2026-04-18)
- F14: Exploitation Collapse on Established Strategy (new, 2026-04-18)

---

## F1: Scenario-List Exhaustion

**Symptom:** The agent performs a behaviour in some situations but inexplicably skips it in others that seem equally appropriate.

**Root cause:** The instruction listed specific triggering scenarios, and the agent treats the list as exhaustive. See [05-instruction-craft.md](05-instruction-craft.md#the-scenario-list-anti-pattern) for full treatment.

**Failing instruction:** "After completing a task, fixing a bug, or finishing a meaningful chunk of work, commit."

**Fix:** "Commit early and often. The only constraint is: never push without explicit permission."

**Detection:** Search for instructions containing comma-separated scenarios ("after X, Y, or Z"). Ask whether the agent would skip the behaviour for an unlisted scenario.

---

## F2: Domain Bias Anchoring

**Symptom:** The agent applies domain-specific patterns to unrelated projects. A web app audit produces ML-flavoured findings. A CLI tool's documentation reads like an API reference.

**Root cause:** Examples in the skill are drawn from a single domain. The agent's induction heads replicate the domain vocabulary and conceptual framework from the examples.

**Failing instruction:** Three examples all referencing ML concepts (training pipelines, replay buffers, model checkpoints) in a general-purpose code health skill.

**Fix:** Span examples across at least 2-3 domains. No single domain should represent more than half the examples in any file. See [10-example-design.md](10-example-design.md).

**Detection:** Read every example in the skill and ask: "If an agent read only these examples, would it think this skill is designed for one specific kind of project?"

---

## F3: Decision-Support Cardinality Anchoring

**Symptom:** The agent always produces exactly N options, alternatives, or categories, regardless of the actual decision space. If examples show 3 options, every output has 3 options.

**Root cause:** The examples all had the same number of items (e.g., every comparison showed exactly 3 alternatives). The agent learned the cardinality as part of the format.

**Failing instruction:** Three worked examples, each showing exactly 3 alternatives for a design decision.

**Fix:** Vary the cardinality across examples. One example with 2 options, another with 4, another with 5. Explicitly state: "The number of alternatives depends on the decision space, not on a fixed count."

**Detection:** Check whether all examples of a particular output type have the same structural dimensions (same number of items, same number of sections, same depth). If yes, cardinality anchoring is likely.

---

## F4: Reference File Under-Loading

**Symptom:** The agent produces output that ignores information available in reference files it was told to read. Quality is inconsistent — sometimes good (when reference was loaded), sometimes shallow (when it was not).

**Root cause:** SKILL.md listed many reference files sequentially without marking which are mandatory vs. conditional. The agent read the first few and stopped. Observed in practice: agents given a list of 10 files to read often stop at 3.

**Failing instruction:**
> Read the following reference files: `categories.md`, `evidence.md`, `format.md`, `examples.md`, `edge-cases.md`, `taxonomy.md`, `quality-bars.md`, `templates.md`, `scoring.md`, `glossary.md`.

**Fix:** Separate mandatory-core files (read immediately, every time) from task-based conditional files (read when specific conditions apply):

> **Always read these files first:**
> - `categories.md` — finding classification taxonomy
> - `evidence.md` — evidence and justification standards
>
> **Read these when relevant to the current task:**
> - `edge-cases.md` — when encountering unusual project structures
> - `templates.md` — when producing output files

**Detection:** Count reference files in the loading instructions. If more than 3-4 are listed without conditional triggers, under-loading is likely.

---

## F5: Instruction Contradiction Across Files

**Symptom:** The agent's output is inconsistent — it follows different rules at different times, or produces output that seems uncertain and hedging.

**Root cause:** SKILL.md says one thing ("use judgement to choose the best format") but a reference file says something contradictory ("always use bullet lists for this section"). The agent loses confidence and produces inconsistent output.

The paper "LLMs can be easily Confused by Instructional Distractions" (2025) tested six models and found that when task instructions compete with content signals, accuracy on the intended task can fall as low as **30%** (style transfer) or even **5.1%** (question answering). The core finding: when instructions compete, compliance degrades broadly across ALL instructions — not just the contradicting pair.

**Failing instruction:**
- SKILL.md: "Use your judgement to choose the best representation for each section."
- reference/format.md: "All analysis sections must use bullet lists."

**Fix:** Ensure every instruction in every file is consistent. When a reference file provides more specific guidance than SKILL.md, frame it as a refinement, not a contradiction: "For analysis sections, bullets are usually the clearest format, but use tables when comparing alternatives and prose when explaining complex reasoning chains."

**Detection:** For each instruction in the skill, search the entire skill directory for any instruction that could be read as contradicting it. Pay special attention to contradictions across files — they are harder to spot and there are no existing tools for multi-file prompt coherence checking.

---

## F6: Template-as-Output

**Symptom:** The agent fills in template blanks mechanically. Output sections are shallow, formulaic, and lack genuine reasoning. Every finding looks the same structurally regardless of complexity.

**Root cause:** The template provided labels without intent descriptions. The agent treats the template as a form to fill in rather than a framework for reasoning.

**Failing instruction:**
```
### Current State
[describe current state]

### Recommendation
[describe recommendation]
```

**Fix:** Describe the intent of each section:
```
### Current State
What the code does now, grounded in the actual implementation.
Include enough detail that an engineer can understand the issue
without reading the code first. Reference specific files and
functions.

### Recommendation
The specific change proposed, with enough implementation detail
that an engineer could act on it without further research. Connect
the recommendation to the evidence in Current State.
```

**Detection:** Read the template sections. If any section is just a label with a bracket placeholder, it will produce mechanical output. Every section needs an intent description.

---

## F7: Mode-Question Friction

**Symptom:** The agent asks the user to choose a mode, depth level, or configuration at startup, even when the context makes the choice obvious. Users experience friction and perceive the skill as unhelpful.

**Root cause:** The skill instructs the agent to ask the user to choose between modes before starting work.

**Failing instruction:** "Ask the user whether they want a quick scan, standard audit, or deep dive before beginning."

**Fix:** "Infer the appropriate depth from context — project size, user's request specificity, and available time signals. If genuinely ambiguous, state your inference and ask for confirmation rather than presenting a menu."

**Detection:** Search for instructions that require the agent to ask the user a question before starting work. Each one is a friction point. Ask whether the question could be answered by inference from context.

---

## F8: Over-Constraining Collapse

**Symptom:** The agent abandons some instructions entirely rather than partially complying with all of them. Output is missing sections or categories that the skill explicitly requires.

**Root cause:** The skill has too many rigid constraints, and the agent hits its instruction saturation point. The IFScale benchmark (2025) quantifies this: o3, the strongest model tested, achieved only **62.8% accuracy at 500 instructions**, with most models performing significantly worse. Reasoning models maintain near-perfect compliance until roughly 150 instructions, then degrade steeply — o3 scores 98.2% at 100 instructions but crashes to 62.8% at 500. Beyond saturation, models shift overwhelmingly toward **omission errors** — they abandon instructions entirely rather than partially complying, with an extreme 34.88:1 omission-to-modification ratio in the worst case. The paper also identifies a strong **primacy effect**: earlier instructions are followed more reliably than later ones, consistent with attention limitations.

The paper "What Prompts Don't Say" (2025) found that specifying all requirements simultaneously **backfires** — with 19 requirements specified, accuracy drops to 85% from a 98.7% baseline.

**2026-04-18 Claude-specific addendum:** IFScale numbers for Claude specifically: Opus 4 44.6% at N=500; Sonnet 4 42.9%; Claude 3.7 Sonnet 52.7%. Newer Claude models are *worse* at dense-instruction compliance than 3.7. AgentIF adds a cliff finding: **ISR drops to ~0 past 6000 words of instructions** on all tested models. See [18-claude-specific-calibration.md](18-claude-specific-calibration.md).

**Failing instruction:** A skill with 200+ instructions across SKILL.md and reference files, many of which are rigid constraints rather than principles.

**Fix:** Reduce instruction count by converting rigid constraints to principles with reasoning. Reserve imperative constraints for genuine hard rules. Use quality bars instead of procedures. Trust the agent's judgement for content decisions.

The Sonar Foundation Agent case study (2025) provides direct evidence: a prescriptive two-stage workflow achieved **58% efficacy**, a freer workflow reached **70%**, and distilling to a concise, principle-based prompt with extended thinking reached **75%** — both architectural freedom and prompt conciseness contributed independently.

**Detection:** Count the total instructions across the skill directory. If the count exceeds ~100, the skill is at risk of saturation. Evaluate each instruction: is it a genuine constraint, or could it be a principle?

---

## F9: Stale Internal References

**Symptom:** The agent tries to read files that do not exist, references concepts by old names, or produces output that follows an outdated structure.

**Root cause:** The skill's structure changed (folders renamed, files moved, concepts reorganised) but internal references were not all updated. No automated tools exist to detect this.

**Fix:** After any structural change, search the entire skill directory for old names. Every stale reference must be updated.

**Detection:** Verify that every file referenced in SKILL.md's loading instructions actually exists with that exact filename. Search for any path or concept name that does not match the current directory structure.

---

## F10: Verification-Gate Absence (new, 2026-04-18)

**Symptom:** The agent declares a skill complete while having skipped one or more required obligations. The honest admission only surfaces under direct user interrogation (the `code-health-audit` V14 pattern: zero WebSearch calls and zero diagnostic tests written despite both being explicit obligations).

**Root cause:** MAST taxonomy (Cemri et al., arXiv 2503.13657) — *Task Verification and Termination* failures account for **21.3%** of all multi-agent failure instances. The skill had no deterministic gate between "agent thinks it's done" and "declared done." Every obligation relied on the agent's own assessment that it had been completed. When the agent's assessment was wrong — silent triage, motivated reasoning, or confabulated compliance — there was nothing to catch it.

**Failing pattern:** Quality checklist at the end of SKILL.md phrased as "did I think about X?" rather than "did tool call X fire and produce evidence Y?"

**Fix patterns:**
- **Tool-evidence exit requirement:** completion requires the agent to cite the tool call, file path, and message ID for each obligation. No citation = obligation not met.
- **Skipped-work surfacing obligation:** the skill explicitly requires a "What I did not do" section in the output with reasons. Omitting this section means the work is not complete.
- **External verifier pass:** a separate subagent reads the spec and the output and returns pass/fail per obligation. Cross-family verification outperforms same-family (R2 research, arXiv 2512.02304).
- **Stop hook:** Claude Code's `Stop` hook with `type: "agent"` can run tool calls (test suite, grep the transcript for required tool invocations) before allowing termination. This is the strongest tier.

**Detection:** Read the skill's quality checklist. If every item is a subjective self-rating ("is it good?", "did I do enough?"), the gate is sycophantic. Verifiable items cite specific artefacts (tool names, file paths, search queries, test IDs).

See also: [19-verification-gates.md](19-verification-gates.md) for the full treatment.

---

## F11: Sycophantic Self-Scoring (new, 2026-04-18)

**Symptom:** Agent rubric-scores its own output at 8-10/10 while the output has visible gaps. Self-assessment is consistently higher than external assessment.

**Root cause:** SycEval (arXiv 2502.08177) measured **78.5% sycophancy persistence** across context/model variation. RLHF-trained models inflate self-scores because training rewards confident, "looks-complete" output. When the same model does the work and grades the work, the rubric becomes a sycophancy mirror — the grading output is optimised for the same "looks done" signal as the working output.

Compounding finding from arXiv 2603.04417 "Same Input, Different Scores": GPT-4o and Claude 3.5 Sonnet both display measurable positive self-bias and family-bias in judging. Same-family judges systematically inflate same-family outputs.

**Compounding finding from arXiv 2407.04549:** iterative self-refinement ("now review and refine your work") actively rewards sycophancy inflation *within a single context window* — evaluator scores inflate while human scores drop. No gradient updates needed. "Add a review step" is an anti-pattern, not a mitigation.

**Fix patterns:**
- Replace quality rubrics (subjective, inflatable) with **obligation checklists** (objective, each item cites evidence).
- **Cross-family verifier:** if verification is needed, use a different model family than the generator (Sonnet-grades-Opus or inverse, not same-model).
- **Blind-grader handoff:** external verifier receives only the output and the spec, not the agent's own assessment.
- **Skipped-work declaration:** make admission of skipped work a structural requirement, not a subjective honesty choice.

**Detection:** Search the skill's quality checklist for items that require subjective self-rating. Each one is a candidate for obligation-checklist rewriting.

---

## F12: Tool-Action Asymmetry (new, 2026-04-18)

**Symptom:** Agent completes the "comfortable" tools (Read, Edit, Bash in a code repo) and skips the "uncomfortable" tools (WebSearch, writing diagnostic tests, cross-system analysis), then self-certifies complete. Canonical case: V14 run made 57 tool calls but zero WebSearch and zero diagnostic tests.

**Root cause:** BiasBusters (arXiv 2510.00307) measured **20x pretraining-frequency effect** on tool selection — continued pre-training on one endpoint raised that tool's selection share from 0.6% to 12.8% in one epoch. Tool selection is dominated by pretraining distribution, not by prompt content. Claude 3.5 Sonnet shows delta_model = 0.347 at baseline — ~35% of selection mass needs redistribution for fairness within a single tool category. Cross-category bias (Read vs WebSearch) is larger but unmeasured.

Additional mechanism: AgentIF finding that tool-constraints specifically collapse to **43.2% satisfaction rate** vs 80.8% for vanilla constraints. The category of instruction models handle worst is "you must call tool X."

**Fix patterns:**
- **Reify obligations as tool calls** with schemas, not as prose instructions. "Call `websearch_verification(topic)` with evidence" beats "do research on the topic."
- **Tool-trace requirement in exit gate:** completion check greps the session transcript for each required tool invocation.
- **Forced function calling:** Claude API `tool_choice` can force a specific tool at a specific step.
- **PreToolUse hooks** (Claude Code) can block other tool calls until required tools have fired.
- **Name the bias in the personality:** tell the agent it will feel pulled toward Read/Edit and away from WebSearch, and that this feeling is a training-distribution artefact, not a judgement call.

**Detection:** For every obligation in the skill, classify the required tool as "high pretraining support" (Read, Edit, Bash, Grep, Glob) or "low pretraining support" (WebSearch, Task, writing new test files, running unfamiliar scripts). Low-support tools are at risk. If the skill has any low-support obligation without an enforcement mechanism beyond prose, add one.

See also: [20-tool-action-patterns.md](20-tool-action-patterns.md).

---

## F13: Reference-File Imperative Blindness (new, 2026-04-18)

**Symptom:** Distinct from F4 (under-loading): the agent *did* read the reference file but the imperative in it was still not executed. The obligation appears in the agent's context but does not produce corresponding action.

**Root cause:** Models file reference-file content as "context I have loaded" rather than "actions I must perform." Imperatives buried in reference prose are mentally indexed as awareness, not commands. This is reinforced by Anthropic's own guidance ("process in SKILL.md, context in references") — references are architecturally informational.

Additional evidence: AgentIF tool-constraints collapse (43.2%). Placing a tool-use imperative in a reference file compounds this effect.

**Fix patterns:**
- **Imperatives belong in SKILL.md body, not references.** Reference files describe *how* to perform an action; SKILL.md is the only place that says *whether* an action must occur.
- **Promotion rule:** for every ALWAYS, NEVER, MUST, "do not", "you must" in every reference file, ask whether it should be promoted to SKILL.md body.
- **Verbatim restatement:** critical imperatives should appear in SKILL.md body AND be restated verbatim in the quality checklist at the bottom. Research support: Leviathan 2025 (arXiv 2512.14982) — verbatim prompt repetition has 47 wins / 0 losses record over 70 tests, up to +76pp on non-reasoning models. (Benefit evaporates with extended thinking on.)

**Detection:** Search every reference file for imperative language. Each occurrence is a candidate for promotion to SKILL.md body.

---

## F14: Exploitation Collapse on Established Strategy (new, 2026-04-18)

**Symptom:** Agent runs for many tool calls but all calls are variants of the same pattern. The agent found a path that produces plausible-progress tokens and will not try novel approaches even when the current path is clearly incomplete. This is distinct from premature termination — the agent isn't stopping short, it's terminating wide-and-shallow.

**Root cause:** LLM policies have a documented exploitation bias — they default to short-sighted greedy behaviour, over-exploiting known rewards at the expense of exploration (arXiv 2509.24923, "When Greedy Wins"). For agent skills, the "reward" signal is "does this action produce plausible progress text?" Any action that produces progress-looking tokens becomes self-reinforcing. Novel actions (WebSearch on an unfamiliar topic, writing a failing test, running an unfamiliar script) have higher variance and lower training-distribution support, so they are systematically avoided.

Compounding: **self-conditioning on own prior trace** (arXiv 2509.09677). Once the agent skipped WebSearch on calls 3-5, calls 6-57 few-shot learn the skip from their own context. Thinking models resist this; non-thinking models do not.

**Fix patterns:**
- **Mandate variety in required actions.** "At least one WebSearch, at least one grep across unfamiliar directories, at least one script execution" forces exploration.
- **Front-load hard obligations.** Put the WebSearch requirement as the first tool call the agent must make. Self-conditioning then reinforces "WebSearch first" as the prevailing pattern.
- **Pattern breakers** mid-skill: forced checkpoints that re-read the obligation list and state what has/has not been done. Resets the few-shot prior.
- **Named novel-action categories:** the agent cannot generate a rare-distribution action it doesn't recognise as required. Enumerate explicitly.
- **Reward exploration in the quality checklist.** "Did you consider at least three hypotheses before converging?" pushes against greedy collapse.

**Detection:** For each obligation, ask: "Would an agent that found one acceptable path for this obligation try a second path?" If no and the obligation requires exploration (research, cross-checking, testing), the skill is vulnerable to exploitation collapse.
