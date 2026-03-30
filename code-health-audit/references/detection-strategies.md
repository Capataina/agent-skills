# Detection Strategies

This reference defines how to find code health issues — the exploration approach, stack-agnostic techniques, when to use language-specific tooling, and how to conduct targeted research.

## Table of Contents

1. The Two-Pass Approach
2. Pass 1: Context and Broad Scan
3. Pass 2: System-by-System Deep Dive
4. Stack-Agnostic Detection Techniques
5. Language-Specific Tooling
6. Targeted Research
7. Exploration Discipline

## 1. The Two-Pass Approach

The audit uses two passes because effective detection requires both breadth and depth:

- **Pass 1** gives you the map: project structure, systems, boundaries, preferences, and a broad sense of where the codebase's centre of gravity is. No research happens yet.
- **Pass 2** gives you the territory: deep reading of actual implementation code, system by system, with targeted research where domain-specific knowledge would improve the analysis.

Do not skip Pass 1. Without it, you will waste time rediscovering architecture that is already documented, and you will miss context (project notes, preferences) that would prevent false positives.

Do not skip Pass 2's deep code reading. Context files describe systems at a high level. The actual code is where the findings are.

## 2. Pass 1: Context and Broad Scan

### Step 1: Read the Context

Read in this order:

1. `context/architecture.md` — structural map, subsystem responsibilities, dependency direction.
2. `context/notes.md` — project preferences, design rationale, guiding principles. **This is critical.** Notes tell you what the team cares about, what they have tried, and what constraints exist. Findings that contradict project notes are likely wrong.
3. Relevant `context/systems/` files — understand each subsystem's boundaries, current reality, known issues, and active risks. The "Known Issues / Active Risks" sections are especially valuable — they tell you what the team already knows about.
4. `context/references/` — existing research that may inform optimisation decisions.
5. `context/plans/` — active work that should be respected. Do not flag in-progress work as incomplete.

### Step 2: Broad Codebase Scan

After reading context, perform a broad survey:

- Walk the directory structure to understand the physical layout.
- Note file sizes — unusually large files are modularisation candidates.
- Identify the entry points and main execution paths.
- Identify the technology stack, languages, frameworks, and build system.
- Note the testing infrastructure (test framework, test directory structure, test count).
- Identify configuration files and how they are structured.
- Get a sense of the codebase's overall health — is it well-organised? Are naming conventions consistent? Is there an obvious style?

This is a survey, not a deep read. You are building a mental map. The deep reading happens in Pass 2.

### Step 3: Prioritise Systems for Pass 2

Based on what you learned:

- Which systems are largest and most complex? (higher chance of findings)
- Which systems have the most active risks in their context files? (higher impact findings)
- Which systems are on the critical path? (highest-value findings)
- Which systems have had the most recent change activity? (higher chance of drift and debt)

Order your Pass 2 deep dive to hit the highest-value systems first.

## 3. Pass 2: System-by-System Deep Dive

For each system, in priority order:

### Step 1: Read the Code

Read the actual implementation files. Not just the entry points — follow the logic through the call chain.

Focus on:

- the main execution paths,
- how data flows through the system,
- where the complex logic lives,
- what error handling looks like,
- what patterns are used (and whether they are consistent),
- what dependencies the system pulls in.

### Step 2: Analyse Against Categories

Walk through each analysis category and look for findings. Not every category will have findings in every system — that is expected.

Use the category definitions and "What to Look For" lists as checklists. But do not limit yourself to the listed items — they are examples, not exhaustive.

### Step 3: Research (If Needed)

If the system involves a domain where specialised knowledge would improve the analysis, conduct targeted research now. See the Targeted Research section below.

### Step 4: Record Findings

For each finding, capture all required fields (see finding-format reference). Record findings as you go — do not try to hold everything in memory and write it all at the end.

## 4. Stack-Agnostic Detection Techniques

These techniques work regardless of language, framework, or project type:

### File Size Analysis

Large files often indicate modularisation opportunities. Look at files that are significantly larger than their peers.

### Call Graph Analysis

Trace callers and callees to identify dead code. If a function has no callers (and is not an entry point, public API, or callback), it is likely dead.

### Duplication Detection

Look for repeated code patterns — similar logic implemented in multiple places. This indicates either a modularisation opportunity or an inconsistency.

### Dependency Inventory

Check the project's dependency manifest against actual usage. Unused dependencies are easy to spot by searching for their imports.

### Complexity Indicators

- Deep nesting (multiple levels of conditionals or loops)
- Long functions (significantly longer than peers)
- Long parameter lists
- Functions with many branch points

### Pattern Frequency

If you see the same operation done three or more different ways, flag it as an inconsistency. Look at error handling, configuration access, logging, and data transformation.

### Comment Analysis

Search for TODO, FIXME, HACK, WORKAROUND, TEMPORARY, DEPRECATED. These are self-documented issues.

### Dead Import Detection

Search for imports that are not referenced in the file. Many languages have tools for this, but a manual search works too.

## 5. Language-Specific Tooling

When the project uses a language or framework that has established analysis tools, consider leveraging them:

- **Rust:** `cargo clippy` for lints, `cargo udeps` for unused dependencies, `cargo audit` for security.
- **Python:** `pylint`, `flake8`, `mypy` for type issues, `vulture` for dead code.
- **TypeScript/JavaScript:** `eslint`, `tsc --noUnusedLocals`, bundler analysis for dead exports.
- **Go:** `go vet`, `staticcheck`, `deadcode`.
- **C/C++:** `cppcheck`, compiler warnings at high levels.

These tools are **supplements**, not replacements for manual analysis. They catch surface-level issues. The deeper findings — algorithm improvements, modularisation opportunities, pattern extraction — require human-level reasoning.

If a project has an existing linting configuration, respect it. Do not flag issues that the team has already configured their linter to ignore.

## 6. Targeted Research

### When to Research

Research during an audit is specifically for:

- finding domain-specific optimisation strategies for the systems in the project,
- validating that a proposed algorithm change is genuinely better for the specific use case,
- understanding best practices for a technology or pattern used in the project.

Research is NOT for:

- general software engineering knowledge you already have,
- language syntax or standard library features,
- opinions on coding style.

### How to Scope Research Queries

Good research queries are specific to the system you are analysing:

- "How to optimise PostgreSQL query planner hints without changing query semantics" (when the project uses Postgres)
- "Efficient nearest-neighbour search for 2D continuous space" (when the project does spatial queries)
- "Reducing memory allocations in Go HTTP request handlers" (when the project is a Go web service)

Bad research queries are too generic:

- "How to write clean code"
- "Performance optimisation best practices"
- "Code refactoring techniques"

### When Research Happens

Research happens in Pass 2, during the system-by-system deep dive, after you have read the code for that system. This timing is critical:

- You know the stack and the project context from Pass 1.
- You know the specific implementation from reading the code.
- Your research questions are therefore targeted and grounded.
- You can validate research findings against the actual code immediately.

### Validating Research Findings

Before turning a research finding into an audit recommendation:

1. **Does it apply to this specific implementation?** A general optimisation strategy may not apply to the specific data sizes, constraints, or patterns in this project.
2. **Does it violate either inviolable rule?** An optimisation that changes output, even slightly, is not a "free" change.
3. **Is the evidence strong?** Prefer findings from authoritative sources (language documentation, peer-reviewed research, well-known engineering blogs from the relevant community) over generic advice.
4. **Can you demonstrate the improvement?** If you cannot explain why the optimisation works for this specific case with concrete reasoning, the recommendation is too speculative.

## 7. Exploration Discipline

### Read Before You Recommend

Never propose a change to code you have not read. This sounds obvious, but it is the most common source of bad findings. "This file is probably doing X" is not evidence.

### Follow the Full Path

When investigating potential dead code, trace the full call chain. When investigating a performance issue, find the hot path. When investigating an inconsistency, check all instances, not just the first two you find.

### Respect What You Do Not Understand

If you encounter code that seems unnecessary but you cannot explain why it exists, classify it as "Triage Needed" rather than "Dead Code." The code may serve a purpose that is not obvious from the source alone (runtime plugins, external triggers, backward compatibility).

### Do Not Over-Explore

The audit should be thorough, but not infinite. If a system is small, simple, and well-structured, do not force findings out of it. It is valid for a system to have zero findings. The goal is accurate findings, not a quota.
