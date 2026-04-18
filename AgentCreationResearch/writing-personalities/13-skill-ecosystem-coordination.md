# Skill Ecosystem Coordination

## The Personality as Coordinator

The personality file is the only place that knows about all skills and how they relate. Each skill is a self-contained specialist that does not know about other skills. The personality orchestrates by:

- Knowing what each skill does and when to invoke it.
- Understanding how skill outputs interact (one skill's output feeds into another's input).
- Deciding when accumulated drift warrants a full skill pass vs inline edits.
- Asking the user before invoking any skill (skills are heavy-weight operations).

## Describing Skills in the Personality

For each skill, include:

1. **What it does** (one paragraph). Write this as a capability description, not a technical summary. "Maintains context/ as the repository's implementation memory layer. Runs a repo scan script, then produces or updates architecture, system, and supporting files" tells the agent what the skill delivers.
2. **When to invoke it** (concrete conditions). List specific, observable triggers: "accumulated drift is too broad for inline edits," "multiple subsystems were created or retired," "the architecture has shifted substantially." Avoid vague triggers like "when needed."
3. **When NOT to invoke it** (to prevent unnecessary invocations). This is especially important because skills consume significant context. "Do not invoke for adding one system file or updating a single document — handle those inline."

## The Relationship Map

After describing individual skills, include a section showing how they interact. This is the coordination map — it tells the agent how data flows between skills and prevents it from invoking skills in the wrong order or misunderstanding outputs.

The relationship map works best as a visual (ASCII diagram or tree) followed by prose that explains the flow:

```
skill-A  --writes to-->  folder-X/
                              |
skill-B  --governs----->  folder-Y/  (includes folder-X/)
                              |
                         read by all skills before generating output
```

The prose should explain: What does each skill write? What does each skill read? How does the output of one skill become the input for another? What is the dependency order?

## Invocation Etiquette

The personality should establish clear norms for skill invocation:

- **Always ask before invoking.** Skills are heavy-weight operations that consume significant context. The agent should recommend a skill run and give a concrete reason, then wait for the user to confirm.
- **Name the specific skill.** "I recommend running upkeep-context because we've made significant changes across multiple subsystems" is actionable. "Maybe we should update the docs" is not.
- **Distinguish inline work from skill work.** The agent should develop judgment about the threshold between "I can handle this with a targeted edit" and "this needs a full skill pass." The personality should describe this threshold in terms of observable conditions, not feelings.

## The Rule (2026-04-18 refinement)

**Skills must not assume the presence of other skills.** This is the load-bearing constraint — an agent running skill A should never fail because skill B is absent.

Skills reference artefact patterns ("plan files in context/plans/"). Only the personality references skill names, because only the personality is the coordinator.

**Softening from original rule:** coordinated skill families may share components via relative paths. Anthropic's own `skill-creator` references its grader subagent (`agents/grader.md`) directly. Within a family designed together, shared components are acceptable. Cross-family coupling remains prohibited — a skill in one family calling a skill in another is the anti-pattern. See [writing-skills/14-cross-skill-coherence.md](../writing-skills/14-cross-skill-coherence.md) for the skill-side treatment.

## Dispatch-to-subagent for uncomfortable obligations (2026-04-18 addition)

When a skill names an obligation requiring a tool with low pretraining support (WebSearch, Task dispatch, writing new failing tests, cross-system analysis), the personality should prefer dispatch to a specialist subagent over asking the main loop to perform the obligation.

**Why:** the main loop inherits pretraining bias toward Read/Edit/Bash. It will satisfice on the uncomfortable tool and draft reasoning about why the tool wasn't needed. A specialist subagent with a narrow prompt dedicated to that single tool forces commitment — the subagent has no alternative action to satisfice toward.

**Suggested personality framing:** *"When a skill names an obligation requiring WebSearch, cross-system synthesis, or new test writing, and you find yourself drafting reasoning about why you don't need to perform it, dispatch a Task subagent whose sole obligation is that tool. The handoff forces commitment. Do not perform the obligation in the main loop if you have drafted reasoning against it."*

**Caveats:** multi-agent dispatch costs 15x tokens vs chat, 4x vs single-agent. Dispatch sparingly. For a typical 30-tool-call skill, at most one verification subagent at the end.

See [writing-skills/21-orchestrator-worker.md](../writing-skills/21-orchestrator-worker.md) for the architectural pattern.
