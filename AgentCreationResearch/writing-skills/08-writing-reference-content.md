# Writing Rich Reference Content

This is the hardest part of skill creation. Designing the folder structure is straightforward. Writing a 400-line reference file that is comprehensive, domain-agnostic, teaches through reasoning, and gives the agent freedom without losing quality — that is the craft.

## Calibrating Depth

Not every reference file needs the same depth. The right depth depends on three factors:

1. **How much judgement is involved.** A category taxonomy where the agent must decide which bucket a finding goes in needs extensive definitions, boundary guidance, and examples. A file naming convention where there is one right answer needs a short list.

2. **How much variation exists across projects.** A reference that must work for Rust game engines, Python data pipelines, and TypeScript web apps needs more examples and more principle-based reasoning than one designed for a specific stack. Universal applicability demands depth because you cannot rely on shared assumptions.

3. **How costly mistakes are.** The evidence-and-justification reference in a code health audit needs extreme depth because a poorly justified finding wastes an engineer's time and erodes trust. A file naming reference can be brief because naming mistakes are cheap to fix.

**The heuristic:** If an agent reading this reference file and nothing else could produce output that meets the skill's quality checklist, the file is deep enough. If the agent would need to guess, infer, or improvise to fill gaps, the file needs more content.

## Writing for Universal Applicability

Skills that work across any project type must be written at the level of universal software engineering principles, not stack-specific patterns. This requires a specific writing approach:

**Lead with the principle, follow with diverse illustrations.** Instead of "In Rust, use `clippy` to find dead code," write "Trace the call chain from every function to its callers. If a function has no callers and is not an entry point, public API, or callback target, it is likely dead. Language-specific tools (clippy for Rust, vulture for Python, eslint for TypeScript) can automate the surface-level detection, but dynamic dispatch, reflection, and code generation require manual verification."

**Name the pattern, not the technology.** Instead of "Use a HashMap for O(1) lookups," write "If the operation requires frequent key-based retrieval, a hash-based data structure gives O(1) average lookup. The specific type depends on the language (HashMap in Rust, dict in Python, Map in TypeScript, map in Go)."

**When you give examples, span domains.** A section about "hardcoded patterns that could be algorithmic" should show a raycast spacing example (game dev), a retry interval example (backend), and a grid layout example (frontend) — not three game dev examples. Each example teaches the same principle in a different context, proving the principle is universal.

**Acknowledge that best practice varies by stack.** Some principles genuinely differ across ecosystems. When they do, say so: "Error handling patterns vary significantly by language — Result types in Rust, exceptions in Python, error returns in Go. The important thing is consistency within the project, not adherence to one pattern." This gives the agent permission to adapt rather than forcing one approach.

## Designing Taxonomies and Categories

Several skills require taxonomies — classification systems where the agent must decide which category a finding, a file, or a concept belongs to. Well-designed taxonomies share several properties:

**Mutually exclusive.** Every item should belong to exactly one category. If two categories overlap, the agent wastes time deciding and may inconsistently classify similar items. When overlap is unavoidable, provide explicit boundary rules: "If a finding could belong to both X and Y, use this priority order..."

**Collectively exhaustive.** The taxonomy should cover every plausible finding. If the agent encounters something that fits no category, the taxonomy has a gap. Include a "how to handle items that do not fit" instruction — either a catch-all category or guidance on extending the taxonomy.

**Defined by principle, not by example.** Each category should have a clear definition that the agent can apply to novel situations, not just a list of examples. Examples illustrate the definition — they do not replace it. An agent encountering a finding type it has never seen before should be able to read the category definition and classify correctly.

**Ordered by decision priority.** When categories could compete for the same finding, provide a priority order that resolves ambiguity. "If it is a correctness issue, it goes in Known Issues regardless of what else it could be."

## Writing Templates That Guide Without Becoming the Output

Templates are structural guides — they show the expected shape of the output. The risk is that the agent treats the template as the output and fills in the blanks mechanically rather than reasoning about what each section needs.

**Show the structure, describe the intent.** For each section in a template, explain what the section is *for* — what question it answers, what value it provides to the reader.

| Weak template section | Strong template section |
|-----------------------|------------------------|
| `### Current State` | `### Current State` — What the code does now, grounded in the actual implementation. Include enough detail that an engineer can understand the issue without reading the code first. |
| `### Recommendation` | `### Recommendation` — The specific change proposed, with enough implementation detail that an engineer could act on it without further research. Connect the recommendation to the evidence in Current State. |

**Vary template completeness across examples.** If you show one fully filled template as an example, also show a shorter one for a simpler finding. This teaches the agent that depth should be proportionate to the finding's complexity, not uniform.

**Templates are minimum structure, not maximum structure.** The agent should feel free to add sections, sub-sections, diagrams, tables, or other elements that improve clarity. The template defines what must be present, not what is allowed.

## Writing "Open Field" Content

The hardest reference files to write are the ones where the agent needs maximum creative freedom — detection strategies, analysis approaches, writing standards. These are "open field" content: the skill establishes direction and quality, but the agent determines the path.

**Teach reasoning patterns, not procedures.** Instead of "Step 1: Check file sizes. Step 2: Check function lengths. Step 3: Check nesting depth," write "Look for structural indicators of complexity — files significantly larger than their peers, functions with deep nesting or many branch points, modules that mix multiple responsibilities. The specific indicators depend on the language and project conventions."

**Use conditional guidance.** "If the system involves domain-specific algorithms (ML training, physics simulation, graph traversal), conduct targeted research to find established optimisation strategies for that specific domain. If the system is primarily data transformation and I/O, focus on allocation patterns, unnecessary copies, and hot-path waste."

**State the quality bar, not the procedure for reaching it.** "Every finding must include evidence from the actual code, not assumptions about what the code probably does" is a quality bar. "Read lines 1-100 of each file, then check for..." is a procedure. Quality bars empower; procedures constrain.

**Give the agent explicit permission to be creative.** "The structural rules in this skill are fixed. Everything within that structure is yours — how you explain a system, what depth you reach, what visual representations you choose, how you scope your research queries." This is not filler — it actively counteracts the agent's tendency to be conservative when it senses many rules.
