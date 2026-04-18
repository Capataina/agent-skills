# Scoring Rubric

Use this rubric to evaluate personality files across eleven dimensions. Each dimension has concrete, observable criteria for Weak, Adequate, and Strong.

## Autonomy Balance

| Level | Criteria |
|-------|----------|
| **Weak** | Lists specific permissions ("you may commit, create files, run tests"). Contains "confirm before" for more than 3 actions. No explicit autonomy grant. Or: no guardrails at all — the agent has zero hard constraints. |
| **Adequate** | Has an autonomy grant and some named constraints. Mixes permission-listing with constraint-listing. The agent would know roughly how much latitude it has. |
| **Strong** | Few explicit hard constraints (typically 2-4), broad autonomy grant, explicit explanation of WHY autonomy matters. Reads like an operating charter for a senior engineer. The agent feels empowered. |

## Instruction Persistence

| Level | Criteria |
|-------|----------|
| **Weak** | Critical instructions appear only once, in the middle of the file. No operating loop. No structural reinforcement. Identity section is more than 20 lines in. |
| **Adequate** | Identity is first. Communication style is last. Some reinforcement via operating loop. Plan/note capture exists but is not tied to persistence. |
| **Strong** | Identity and autonomy first (primacy). Quality standards and communication style last (recency). Operating loop reinforces all critical middle-section values. Note-taking pushes objectives into recent attention. Every instruction in the moderate-persistence zone (middle of file) is reinforced by at least one structural mechanism. |

## Section Ordering

| Level | Criteria |
|-------|----------|
| **Weak** | Sections in random or alphabetical order. Identity is not first. Communication style is not last. Critical instructions scattered throughout. |
| **Adequate** | Identity is first. Reasonable grouping of related sections. Communication style is near the end. |
| **Strong** | Fully primacy-recency optimised. Identity and autonomy first. Output standards early. Operational details in the middle with structural reinforcement. Quality anchors and communication style last. The ordering has clear reasoning for every section's position. |

## Constraint Calibration

| Level | Criteria |
|-------|----------|
| **Weak** | Rigid procedures, scenario lists, numeric limits everywhere, ALWAYS/NEVER in caps on more than 5 instructions. |
| **Adequate** | Mix of principles and constraints. Some scenario lists remain but critical sections are principle-based. Emphasis is used selectively. |
| **Strong** | All instructions are principle-based with reasoning. Hard rules only where justified by irreversibility or structural necessity. No scenario-list anti-pattern. Emphasis reserved for genuinely inviolable constraints (3-5 items). Every constraint explains why it exists. |

## Skill Coordination

| Level | Criteria |
|-------|----------|
| **Weak** | Detailed how-to in personality. Skills described vaguely ("use when needed"). No relationship map. Skill descriptions do not match what skills actually do. |
| **Adequate** | Skills described with what and when. No how-to leaking. Skill descriptions mostly accurate. Missing relationship map or invocation etiquette. |
| **Strong** | Clear what/when/when-NOT for each skill. Relationship map showing data flow. Invocation etiquette established (ask before, name the skill, give a reason). No how-to leaking. All skill descriptions verified against actual skill content. |

## Coherence

| Level | Criteria |
|-------|----------|
| **Weak** | Contradictions between personality sections. Terminology drift (same concept called different things). Personality contradicts skill instructions. |
| **Adequate** | Mostly consistent within the personality. Minor terminology variations. Not verified against all skills. |
| **Strong** | Fully coherent within the personality and with all referenced skills. Consistent terminology throughout. No contradictions. Verified against actual skill content. |

## Formatting Quality

| Level | Criteria |
|-------|----------|
| **Weak** | Wall of text. No structural hierarchy. No tables, no visual aids. |
| **Adequate** | Headers and paragraphs. Some tables. Readable but not optimised. |
| **Strong** | Rich markdown hierarchy. Tables for structured comparisons (skill ecosystems, source hierarchies). Visual relationship maps. Clear heading structure. Information density appropriate to each section. |

## Budget Efficiency

| Level | Criteria |
|-------|----------|
| **Weak** | Contains skill-level procedures. Redundant with skill content. Explains things the agent already knows (software engineering basics). More than 30% of content could be offloaded to skills. |
| **Adequate** | Mostly personality-level content. Some how-to that could be in skills. Reasonable length. |
| **Strong** | Every token earns its place. All how-to offloaded to skills. No redundancy. The personality is as short as it can be while retaining all genuinely personality-level instructions. Passes the "would removing this cause mistakes?" test for every line. |

## Personality-Skill Boundary

| Level | Criteria |
|-------|----------|
| **Weak** | Personality contains step-by-step procedures for specific tasks. "How to write a context file" appears in the personality. Skill descriptions include implementation details. |
| **Adequate** | Mostly clean boundary. Occasional procedural detail that could be in a skill. Skill descriptions focus on what and when. |
| **Strong** | Clean boundary — the personality says when and what, skills say how. No procedural detail in the personality beyond the operating loop. Every instruction passes the when/what vs how test. |

## Sycophancy Resistance (added 2026-04-18)

Measures whether the personality's structure holds against the agent's trained incentive to produce "looks-complete" output rather than do thorough work.

| Level | Criteria |
|-------|----------|
| **Weak** | Uses vague exhortations (*"be thorough", "go above and beyond", "strive for excellence"*) as reliability mechanisms. No deontological permissions for honest admission. No forcing-function obligations. Review/refine instructions rely on same-model self-assessment. |
| **Adequate** | Some exhortations but also some obligations. At least one explicit permission for admission ("you may say 'I don't know'"). Review steps dispatch to different context or avoid same-model self-evaluation. |
| **Strong** | All reliability-critical instructions are verifiable obligations with evidence tests or deontological permissions. No vague exhortations as reliability mechanisms. Explicit skipped-work declaration obligation. Tool-bias named as a pretraining artefact. Iterative self-refinement patterns absent. |

Detection: search the personality for adverbs (*thoroughly, carefully, actively, honestly*) and modal exhortations (*always, never, must, should* without an evidence test). See [09-obligations-vs-exhortations.md](09-obligations-vs-exhortations.md).

## Structural Defences (added 2026-04-18)

Measures whether the personality installs structural mechanisms for failure modes that wording cannot fix (drift, Lost-in-the-Middle, tool-action asymmetry, sycophancy).

| Level | Criteria |
|-------|----------|
| **Weak** | Relies on content persistence — instructions in the middle of the file with no reinforcement. No operating loop. No recitation / plan-file pattern. No obligation audit. Placement rules not stated or followed. |
| **Adequate** | Has an operating loop. Some placement discipline (identity first, communication style last). Missing one or more of: recitation pattern, obligation audit, tool-bias naming, explicit edge-placement rules. |
| **Strong** | Operating loop with grounding + verification + upkeep + assessment. Recitation pattern (plan files, todo-style artefacts) that pushes obligations into recent context. Pre-completion obligation audit as a structural requirement. Tool-bias named explicitly as a pretraining artefact. Edge-placement discipline stated and followed. Claude Code infrastructure primitives (hooks, subagents) used where available. |

See [10-structural-defences.md](10-structural-defences.md) for the pattern catalogue.
