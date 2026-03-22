---
name: teach-me
description: "Generate comprehensive, university-style learning curricula from software project repositories. Use this skill whenever the user wants to deeply understand a codebase, asks to 'teach me' about a project, requests learning materials or study guides for a repo, wants interview preparation for a project they built, asks for first-principles explanations of their code, wants exercises or practice problems based on their project, or says anything like 'help me learn this project', 'explain my codebase', 'create a curriculum', 'generate learning materials', or 'I want to understand how this works from the ground up'. Also trigger when the user asks to understand design decisions, wants to identify reusable patterns in their code, or needs to prepare to explain their project technically. This skill produces a complete learning/ folder with concept files, exercises, materials, and a structured curriculum. Do NOT use for general coding tasks, code review, or bug fixing — this is specifically for pedagogical content generation from codebases."
---

# Teach Me — Comprehensive Project Learning Curriculum Generator

Transform any codebase into a self-contained educational resource. The output is a complete `learning/` folder that enables someone to explain the project in technical interviews with first-principles depth, understand every design decision, identify reusable patterns that transfer to other projects, and modify or extend the codebase confidently.

Before generating any content, read the reference files in `references/`. They contain the templates, writing standards, and exercise formats that govern quality. Read them in this order:

1. **Read `references/writing-standards.md` first** — it defines depth calibration, math rendering, abundance targets, and the explanation quality bar. Every file you generate must meet these standards.
2. **Read `references/templates.md` second** — it contains the structural templates for every file type (concepts, patterns, implementations, materials, curriculum, glossary).
3. **Read `references/exercises.md` third** — it contains exercise skeleton requirements, debugging challenge format, and solution structure.

## Core Philosophy

The goal is mastery, not minimal competence. Every design decision in this skill serves one purpose: producing learning materials so thorough that someone could mass-delete every concept file, keep only the exercises, and still reconstruct the core ideas — or conversely, read only the concept files and pass a technical interview.

Six principles govern all generated content:

**1. First-Principles Depth** — Every concept is explained from the ground up. Mentioning "vector embeddings" means explaining what a vector is, what a vector space is, why we represent things as vectors, how distance relates to similarity, and the mathematical operations involved. Surface-level summaries are never acceptable. The reader should never need to consult an external resource to understand what a file is saying.

**2. Interview-Ready Explanations** — After reading any single concept file, the reader should be able to give a coherent, technically accurate 5-minute explanation of that concept in an interview. Test every file against this standard: "Could someone who read only this file answer 'How does X work?' to a senior engineer?"

**3. Progressive Build-Up** — Complex concepts are built step-by-step. Step 1 covers the foundational sub-concept with examples. Step 2 builds on Step 1. Step N synthesises everything. Never jump to the final abstraction without showing the journey. If you find yourself writing a sentence that assumes knowledge you haven't yet established in the file, stop and add the prerequisite explanation first.

**4. Glossary Saturation** — Every non-trivial term is defined, either inline in a per-file glossary section or by reference to the global `GLOSSARY.md`. "Non-trivial" means anything a second-year undergraduate might not immediately recognise. No reader should ever encounter an undefined term.

**5. Concrete Examples Everywhere** — Every abstract concept includes concrete numerical or code examples. "Policy gradients optimise the policy directly" is never acceptable on its own. It must be accompanied by a worked example showing actual numbers, actual gradient updates, actual parameter changes. Abstract explanations without concrete grounding are pedagogically useless.

**6. Separation of Concerns** — Three knowledge types are kept strictly separate:
- **Universal/Foundational**: Applies to any project (calculus, probability, data structures). Lives in `concepts/foundations/`.
- **Domain Patterns**: Reusable within a domain but not project-specific (grid systems, async patterns, embeddings). Lives in `concepts/domain_patterns/`.
- **Project-Specific**: Unique to this codebase (why we chose X, how we implemented Y). Lives in `project_specific/`.

This separation matters because domain patterns transfer to other projects. A grid system learned from a game project applies to network zone partitioning. An async pattern from a web server applies to a trading engine. Conflating these with project-specific details buries the transferable knowledge.

## Abundance Over Minimalism

LLMs have a strong tendency to produce the minimum viable output — 3 examples when 5 are needed, 3 misconceptions when 8 are needed, 4 glossary terms when 20 are needed. This skill explicitly counteracts that tendency with hard numeric floors. These numbers are not aspirational targets; they are minimums.

**Per concept file:**
- Worked examples: 3–5 minimum, each from a different angle (basic mechanics, parameter variation, failure mode, comparison to alternative, connection to project code)
- Common misconceptions: 5–8 minimum, covering beginner mistakes, subtle persistent errors, failure modes, and comparisons with related concepts
- Glossary terms: 15–20 minimum, defining every technical term used in the file
- Recommended materials: 8–12 minimum, covering textbooks, videos, blog posts, papers, and interactive resources

**Per project (medium-sized):**
- Total concept files: 25–30
- Total exercises: 15–20
- Materials files: 3–6 (topic-organised)
- Project-specific implementation files: 5–10

When deciding whether to add another example, misconception, exercise, or material, the default answer is always YES. Stop only when you have thoroughly covered the concept from multiple angles and the numeric floors are met.

## Codebase Analysis Process

Before generating any files, analyse the project thoroughly. This analysis determines the entire folder structure and content plan.

### Step 1: Identify Core Technologies
Scan the codebase for programming languages, frameworks, major libraries, and the domain area (ML, systems, web, game, compiler, networking, etc.).

### Step 2: Identify Key Algorithms and Patterns
Look for specific algorithms (A2C, NEAT, Dijkstra, CLIP), architectural patterns (ECS, async, lock-free, microservices), data structures (grids, graphs, trees, embeddings), and domain-specific concepts (RL, neuroevolution, compilers, networking).

### Step 3: Build Dependency Graph
For each identified concept, recursively extract prerequisites until you hit assumed undergraduate knowledge:
- A2C → policy gradients, value functions, advantage estimation
- Policy gradients → gradient descent, expected value, MDP formalism
- Gradient descent → derivatives, loss functions
- Derivatives → basic calculus

This graph determines the learning phases in `CURRICULUM.md` and the prerequisite chains in each concept file.

### Step 4: Identify Reusable Domain Patterns
Look for implementations that are instances of general patterns. A grid-based spatial system is a domain pattern. A raycast observation system is a domain pattern. An async I/O architecture is a domain pattern. These become `concepts/domain_patterns/` files — the most transferable knowledge in the entire curriculum.

### Step 5: Identify Project-Specific Decisions
Look for "why X instead of Y?" decisions, unique combinations (e.g. hybrid STDP + A2C), and custom implementations with interesting details. These become `project_specific/` files.

### Step 6: Design the Folder Structure
Based on the analysis, decide which `concepts/core/` subdirectories to create, which `concepts/domain_patterns/` to create, which foundational concepts are needed, and how many curriculum phases are appropriate (3–5 is typical). The structure is not fixed — design it to fit the project.

## Output Structure

Generate a `learning/` folder in the project root. The structure is flexible, but most projects need these categories:

### Always Generate

**`CURRICULUM.md`** — Sequential learning roadmap organised into phases with learning goals, time estimates, milestones (concrete deliverables that prove understanding), priority markers (⭐ critical path, 🔵 optional), and an interview preparation section. Each phase ends with a milestone like "Implement X from scratch" or "Explain Y to someone else." See `references/templates.md` for the full template.

**`GLOSSARY.md`** — Comprehensive, alphabetically-ordered glossary of every technical term used across all files. Each entry has a clear definition, a concrete example, and a reference to where the term is used (e.g. "See `concepts/core/policy_gradients.md`").

### Concept Categories (Create As Needed)

**`concepts/foundations/`** — Universal CS/math concepts the project requires (calculus, linear algebra, probability, concurrency, memory management). Only create files for concepts the project actually uses.

**`concepts/core/`** — The heart of the learning system. Domain-specific concepts organised into subdirectories that match the project's domain: `reinforcement_learning/`, `neuroscience/`, `compilers/`, `networking/`, `databases/`, `computer_vision/`, `algorithms/`, etc. Create whatever subdirectories the project needs.

**`concepts/domain_patterns/`** — Reusable architectural patterns that appear across multiple projects within a domain: spatial systems, agent perception, embeddings and search, concurrent patterns, ECS architecture, etc. This category is critical for knowledge transfer.

**`concepts/advanced/`** — Only for projects with research-level or cutting-edge components. Skip for most projects.

### Project-Specific Files

**`project_specific/architecture_decisions.md`** — High-level "why" decisions: why this algorithm over alternatives, why this tech stack, what trade-offs were made.

**`project_specific/implementations/`** — One file per major system/component with interesting implementation details. Each file references the general pattern in `concepts/domain_patterns/` and explains this project's specific implementation, including code locations and deviations from standard approaches.

**`project_specific/debugging_guide.md`** — Optional. Common issues, bugs, and fixes. Only create if there are known gotchas.

### Materials

**`materials/`** — Topic-organised resource files (not medium-organised). Each file covers a major topic area with 8–12 curated resources across textbooks, videos, blog posts, papers, and interactive tools. See `references/templates.md` for the resource entry format.

**Correct structure** (topic-organised):
```
materials/
├── reinforcement_learning.md
├── neuroscience.md
├── rust_async.md
└── spatial_algorithms.md
```

**Wrong structure** (medium-organised):
```
materials/
├── books.md
├── videos.md
└── articles.md
```

### Exercises

**`exercises/`** — Target 15–20 total exercises. See `references/exercises.md` for skeleton requirements and templates.

- `exercises/minimal_implementations/` — Small (20–100 line) skeleton exercises with TODOs
- `exercises/debugging_challenges/` — Broken code the user must fix (no comments pointing to bugs)
- `exercises/comparison_challenges/` — "Implement X and Y, compare results" (optional)
- `exercises/optimization_challenges/` — "Make this 10× faster" (optional)
- `exercises/extension_challenges/` — "Add feature Z to this working code" (optional)

## Token Budget Management

Prioritise ruthlessly. Quality over quantity — 7 deeply-explained concepts with 5 examples each are worth more than 20 shallow concepts with 1 example each.

**Tier 1 — Must Generate (50% of budget):**
1. `CURRICULUM.md`
2. Top 7–10 `concepts/core/*` files
3. Top 5–7 `concepts/domain_patterns/*` files
4. `project_specific/architecture_decisions.md`
5. `GLOSSARY.md`

**Tier 2 — Should Generate (30% of budget):**
6. Remaining important core concepts
7. `project_specific/implementations/*` (3–5 key systems)
8. `materials/*` (topic-organised resource lists)
9. Top 10–12 exercises

**Tier 3 — Nice to Have (15% of budget):**
10. `concepts/foundations/*` (only if prerequisites are not common knowledge)
11. `concepts/advanced/*` (only for cutting-edge projects)
12. Remaining exercises (to reach 15–20 total)
13. Additional debugging challenges

**Tier 4 — If Budget Remains (5% of budget):**
14. Additional worked examples (beyond the 3–5 minimum)
15. Additional misconceptions (beyond the 5–8 minimum)
16. Additional materials (beyond the 8–12 minimum)

## Common Failure Modes to Avoid

These are patterns LLMs frequently fall into when generating educational content. Be vigilant against all of them:

**Shallow summaries disguised as explanations.** "Cosine similarity measures the angle between vectors" is a summary, not an explanation. An explanation includes how the angle is computed, why angle matters more than distance for this use case, what happens when vectors are normalised, and a worked numerical example.

**Missing intermediate steps in derivations.** Every mathematical derivation must show every intermediate step. If the reader cannot follow from line N to line N+1 without mental effort, add another line.

**Glossary laziness.** Defining 5 terms when 20 were used in the file. Every technical term — even ones that seem obvious — gets a definition. "Gradient" seems obvious until a reader confuses it with "derivative" or doesn't know it's a vector of partial derivatives.

**Example starvation.** Providing 1–2 examples when the concept needs 5. Each example should illuminate a different facet: basic mechanics, parameter sensitivity, failure modes, comparisons, and project-specific usage.

**Misconception undercount.** Listing 2–3 misconceptions when 5–8 exist. Beginners have obvious misconceptions; intermediate learners have subtle ones. Both need coverage.

**Providing complete exercise implementations.** Exercises must be skeleton code with TODOs, step-by-step hints, and expected outputs. Never provide working implementations — that defeats the purpose.

**Conflating domain patterns with project-specific details.** A grid-based spatial system is a domain pattern that transfers across projects. The specific grid resolution and update frequency chosen for this project are implementation details. Keep them in separate files.

**Topic-organised materials files that become shopping lists.** Each resource entry needs specific chapters/timestamps, what to skip, focus areas, a post-reading exercise, a why sentence, time estimates, and difficulty levels. "Read Sutton & Barto" is useless; "Read Chapter 13, pages 325–340, focus on the REINFORCE derivation, skip section 13.5" is actionable.

## Quality Checklist

Before considering the `learning/` folder complete, verify every item:

**Content Quality:**
- Every concept has a first-principles explanation (not surface-level)
- Every concept has 3–5 worked examples from different angles
- Every concept has 5–8 common misconceptions
- Every concept has 15–20 glossary terms defined
- Every concept has 8–12 curated materials
- Every abstract concept has concrete numerical/code examples
- Complex concepts build progressively (Step 1 → Step 2 → Step N)

**Exercise Quality:**
- 15–20 total exercises generated
- All implementation exercises are skeletons with TODOs (not complete code)
- Every exercise has step-by-step hints in its docstring
- Every exercise has expected output documented
- Every exercise has a time estimate
- Debugging challenges have no comments pointing to bugs
- `SOLUTIONS.md` has progressive hints (Hint 1, Hint 2, Full Solution)

**Materials Quality:**
- 8–12 resources per major concept
- Each resource has specific chapters/timestamps (not "read this book")
- Each resource explains why it is valuable
- Each resource has a time estimate and difficulty level
- Resources cover multiple learning modalities (text, video, interactive)

**Structure Quality:**
- `CURRICULUM.md` provides a clear learning path with phases and milestones
- Concepts are organised logically (foundations → core → patterns → project-specific)
- Cross-references work (files reference each other appropriately)
- Folder structure makes sense for this specific project
- No unnecessary duplication

**Completeness:**
- All major algorithms/patterns in the codebase have explanation files
- Project-specific architectural decisions are documented
- Reusable patterns are separated from project-specific details
- Glossary covers all non-trivial terms
- Every file path mentioned in `CURRICULUM.md` actually exists
- Exercise count meets 15–20 target
- Misconception count meets 5–8 per file
- Materials count meets 8–12 per concept

## Execution

When this skill is triggered:

1. **Read reference files** — Load `references/writing-standards.md`, `references/templates.md`, and `references/exercises.md`.
2. **Analyse the codebase** — Identify technologies, algorithms, patterns, and decisions.
3. **Build a dependency graph** — Recursively extract concept prerequisites.
4. **Design the folder structure** — Create a structure tailored to this project's domain.
5. **Generate files in priority order** — Tier 1 → Tier 2 → Tier 3 → Tier 4.
6. **Verify quality** — Run every item in the quality checklist above before presenting the output.

Begin now.
