# Cross-Skill Coherence

## The Coordination Problem

When multiple skills exist in the same ecosystem, they can conflict — different terminology, overlapping triggers, contradictory instructions. Agents exposed to conflicting instructions lose confidence and produce inconsistent output. Cross-skill coherence is not optional in a multi-skill ecosystem — it is as important as within-skill coherence.

## Coherence Dimensions

| Dimension | What to Check | Failure Mode |
|-----------|--------------|--------------|
| **Terminology** | Same concept uses same term across all skills. | Agent treats "system file" and "system document" as different concepts, producing inconsistent output or missing connections. |
| **Trigger boundaries** | Descriptions are mutually exclusive with clear boundaries. | Two skills activate for the same user request. The agent either loads both (wasting context) or loads the wrong one. |
| **Artefact references** | Skills reference artefact patterns, not other skills by name. | Renaming a skill breaks references in other skills. Skills develop hidden coupling. |
| **Self-containment** | Each skill has everything it needs within its own directory. | A skill depends on a reference file in another skill's directory. Moving or reorganising either skill breaks the other. |
| **Philosophical consistency** | All skills share the same stance on autonomy, depth, and quality. | One skill grants maximum autonomy while another prescribes rigid procedures. The agent's behaviour oscillates depending on which skill is active. |

## The Personality as Coordinator

Only the personality/coordinator file knows about all skills, how they relate, and when to invoke each one. Skills are specialists that do not know about each other. This means:

- A skill must never say "use the X skill for this" — it does not know the X skill exists.
- A skill may reference artefact patterns: "some files in context/references/ follow a multi-section research paper structure." This describes what exists, not which skill created it.
- When two skills could produce overlapping artefacts, their descriptions must include negative triggers that create clear boundaries.

## The 2026-04-18 Refinement: Shared Components Within Skill Families

The rule "no cross-skill name references" was originally stated as absolute. Research from R5 (Anthropic ground truth) showed this rule is stricter than Anthropic's own practice: the official `skill-creator` skill references its grader subagent by path (`agents/grader.md`).

The refined rule:

- **Skills must not assume the presence of other skills** — this is the load-bearing constraint. An agent running skill A should never fail because skill B is absent.
- **Coordinated skill families may share components.** If two skills live in the same directory tree and are designed together, they may reference shared files, shared subagents, or shared scripts via relative paths. The shared components must be in a location owned by the family, not by one skill.
- **The personality remains the coordinator** for cross-family dispatch. Cross-family coupling (skill A in one family directly calling skill B in another) remains prohibited.

This is a small softening, not a reversal. The spirit — skills are specialists, not omniscient — is preserved. The letter — absolute prohibition on cross-referencing — was over-engineered.

## Evaluating Cross-Skill Coherence

**Evaluation test:** Take any two skills in the ecosystem. For each pair:

1. Do their descriptions overlap? Could a single user request trigger both?
2. Do they use the same term for the same concept? Search for shared terminology.
3. Does either reference the other by name (outside a coordinated family)?
4. Does either depend on files outside its own directory (or its family's shared directory)?
5. If both were active in the same conversation, would their instructions conflict?
