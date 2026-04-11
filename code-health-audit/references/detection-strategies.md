# Detection Strategies

This reference defines how to find code health issues — the exploration approach, stack-agnostic techniques, when to use language-specific tooling, how to conduct targeted research, and how to write diagnostic tests that resolve evidence gaps before issuing findings.

## Table of Contents

1. The Two-Pass Approach
2. Pass 1: Context and Broad Scan
3. Pass 2: System-by-System Deep Dive
4. Stack-Agnostic Detection Techniques
5. Language-Specific Tooling
6. Targeted Research
7. Diagnostic Test Writing
8. Exploration Discipline

## 1. The Two-Pass Approach

The audit uses two passes because effective detection requires both breadth and depth:

- **Pass 1** gives you the map: project structure, systems, boundaries, preferences, and a broad sense of where the codebase's centre of gravity is. No research or test writing happens yet.
- **Pass 2** gives you the territory: deep reading of actual implementation code, system by system, with targeted research and diagnostic test writing interleaved as the analysis surfaces uncertainties that those tools resolve.

Do not skip Pass 1. Without it, you will waste time rediscovering architecture that is already documented, and you will miss context (project notes, preferences) that would prevent false positives.

Do not skip Pass 2's deep code reading. Context files describe systems at a high level. The actual code is where the findings are. And do not skip Pass 2's research and diagnostic-test steps for systems where they apply — most of the highest-value findings come from analysis grounded in research and verified by tests the audit wrote itself, not from generic detection techniques.

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

### Step 3: Run the Project's Test Suite (Baseline Check)

Before going deeper, run the project's existing test suite end-to-end to capture the current pass/fail baseline. Use whatever the project's idiomatic test command is — `cargo test`, `pytest`, `npm test`, `go test ./...`, `mix test`, `dotnet test`, or the language and framework's equivalent. This is a fast and important check, and it tells you the audit's starting position.

What you learn from running it:

- Whether the suite currently passes at all. A failing baseline changes the whole footing of the audit — every recommendation needs to account for the fact that the existing suite cannot be used as a verification ground.
- Which tests are flaky, ignored, or skipped. Flaky tests are often a finding in their own right.
- How long the suite takes to run. This informs whether the audit can cheaply write its own diagnostic tests as part of Pass 2 or whether test runtime will be a real constraint.
- Whether the test infrastructure even works. Some projects have test configuration that has rotted — missing fixtures, broken dependency setup, outdated test runner configuration. The audit needs to know.

Any pre-existing test failures are recorded as **Known Issues and Active Risks** findings immediately. They are not the audit's findings to introduce — they were already there before the audit started — but they belong in the audit output because they affect the safety of every other recommendation, they are exactly the kind of correctness risk the audit exists to surface, and the implementing engineer needs to know about them before acting on any other finding.

If the suite cannot be run at all (no test framework, broken test runner config, missing dependencies), record that as a finding and proceed with the audit knowing that the diagnostic test writing in Pass 2 will need to either fix the infrastructure first or work around it. A project with no working test suite is a different audit posture than a project with a healthy one — the audit's confidence in its own recommendations is partly underwritten by the existing suite's ability to catch regressions.

### Step 4: Prioritise Systems for Pass 2

Based on what you learned:

- Which systems are largest and most complex? (higher chance of findings)
- Which systems do computationally heavy work that would benefit from domain-specific research? (highest chance of high-value findings)
- Which systems have the most active risks in their context files? (higher impact findings)
- Which systems are on the critical path? (highest-value findings)
- Which systems have had the most recent change activity? (higher chance of drift and debt)
- Which systems contained the failing tests, if any? (immediate priority)

Order your Pass 2 deep dive to hit the highest-value systems first.

## 3. Pass 2: System-by-System Deep Dive

Pass 2 is iterative, not strictly sequential. The flow is: read the code until you hit a question, resolve the question with whichever tool fits (more reading, research, or a diagnostic test), then continue. Read → question → evidence → answer → next question. The steps below describe the kinds of work that happen in Pass 2, not a rigid order to walk through them.

### Read the Code

Read the actual implementation files. Not just the entry points — follow the logic through the call chain.

Focus on:

- the main execution paths and what runs in the hot loops,
- how data flows through the system and what its layout looks like in memory,
- where the complex logic lives,
- what error handling looks like,
- what patterns are used (and whether they are consistent),
- what dependencies the system pulls in,
- how data structures are accessed in performance-sensitive code (which fields are touched, which are wasted, which allocations are repeated).

Reading should be deep enough that you can answer: "what does this system actually do, on what data, and how does the data move through memory?" If you cannot answer that, read more.

### Conduct Research (Required for Substantive Systems)

For any system that does substantive work, conduct targeted research. This applies broadly — not only to systems that look numerically heavy, but also to request handlers, business logic with non-trivial control flow, query handlers, parsers, schedulers, middleware, batch processors, and most other non-trivial systems. Almost every system has accumulated domain knowledge that an experienced engineer in that domain would bring to the analysis. Research is how you bring that knowledge in.

See section 6 for the full guidance on which systems require research and how to scope the queries. The default should be to research; skip it only when the system is genuinely trivial (small utility helpers, single-line glue, type definitions, constant tables). When in doubt, research.

### Write Diagnostic Tests Where They Resolve Uncertainty

When the analysis surfaces a question that a test could answer better than reading or research can, write the test. Do not wait until the end of the audit to do this — write the test while the question is fresh, run it, capture the result, and feed the answer back into the analysis of that system. Tests are a tool for resolving uncertainty before issuing findings, not a separate phase tacked on afterwards.

See section 7 for the full guidance on when and how to write diagnostic tests.

### Analyse Against Categories

Walk through each analysis category and look for findings. Not every category will have findings in every system — that is expected.

Use the category definitions and "What to Look For" lists as starting points, not as complete checklists. The lists name the most common cases, but the agent should generalise from the principle behind each category and surface findings that fit the principle even when they do not match a listed example.

For systems with computational depth, pay particular attention to the Data Layout and Memory Access Patterns category — it is the highest-value category for these systems and the easiest to overlook.

### Record Findings

For each finding, capture all required fields (see finding-format reference). Record findings as you go — do not try to hold everything in memory and write it all at the end. When a finding is grounded in a diagnostic test the audit wrote, reference the test in the finding's evidence so the implementing engineer can re-run it themselves.

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

If you see the same operation done several different ways, flag it as an inconsistency. Look at error handling, configuration access, logging, and data transformation.

### Comment Analysis

Search for TODO, FIXME, HACK, WORKAROUND, TEMPORARY, DEPRECATED. These are self-documented issues.

### Dead Import Detection

Search for imports that are not referenced in the file. Many languages have tools for this, but a manual search works too.

### Hot Path Reading

Identify the hottest loops in the system and read them with deliberate care — what data they touch, what they allocate, what they branch on, what they would look like if rewritten with the principles from the Data Layout category in mind. Surface findings from this reading rather than waiting for them to fall out of generic detection.

## 5. Language-Specific Tooling

When the project uses a language or framework that has established analysis tools, consider leveraging them:

- **Rust:** `cargo clippy` for lints, `cargo udeps` for unused dependencies, `cargo audit` for security.
- **Python:** `pylint`, `flake8`, `mypy` for type issues, `vulture` for dead code.
- **TypeScript and JavaScript:** `eslint`, `tsc --noUnusedLocals`, bundler analysis for dead exports.
- **Go:** `go vet`, `staticcheck`, `deadcode`.
- **C and C++:** `cppcheck`, compiler warnings at high levels.

These tools are **supplements**, not replacements for manual analysis. They catch surface-level issues. The deeper findings — algorithm improvements, layout improvements, modularisation opportunities, pattern extraction — require human-level reasoning.

If a project has an existing linting configuration, respect it. Do not flag issues that the team has already configured their linter to ignore.

## 6. Targeted Research

### Research Is Required for Substantive Systems

Research during the deep-dive phase is required for any system that does substantive work — not only the systems that "look computationally heavy." The trap to avoid is dismissing a system because it does not involve linear algebra or simulation. Most systems benefit from research, because most systems have domain-specific patterns that experienced engineers in that domain know about and that the audit should surface.

Systems where research is clearly required include:

- **Numerical and computational work:** linear algebra, optimisation, statistics, simulation, signal processing, machine learning runtimes, physics, graphics, numerical kernels and tight inner loops.
- **Data transformation:** parsing, encoding, compression, serialisation, schema validation, format conversion.
- **I/O and concurrency:** network protocols, file system access, lock-free structures, async runtimes, request pipelines, streaming and real-time systems.
- **Storage and persistence:** indexes, caching, log structuring, transaction handling, query planning, connection pooling.
- **Compilers, interpreters, and language tools:** parsing, intermediate representation, optimisation passes, code generation, type checking.
- **Business logic with non-trivial control flow:** permission and access control, scheduling and dispatch, state machines, workflow engines, rule evaluation.
- **Web service handlers:** request lifecycles, middleware stacks, response builders, caching layers, rate limiters.
- **Background and batch processing:** job queues, worker pools, scheduled tasks, batch ingestion.

The principle is that almost any system that does meaningful work has accumulated domain knowledge — established patterns, known anti-patterns, well-understood optimisation strategies — that an experienced engineer in that domain would apply. If you cannot name the specific patterns that experienced engineers in the relevant domain look for in this kind of system, that is a research gap. Search before declaring the system audited.

The agent's general knowledge is a starting point, not a substitute for targeted research. Generic engineering knowledge will catch the obvious wins. Domain-specific research is what surfaces the wins that surprise the engineer in a useful way.

### When Research Is Not Required

Research can be skipped only for systems that are genuinely trivial: small utility helpers, single-line glue functions, configuration loaders that just read a file and parse JSON, type definitions, and constant tables. The discrimination is not "does the system look mathy?" — it is "does this system contain logic worth studying?" If a system has loops, branching, error handling, multiple data structures, or any non-trivial decision flow, research likely applies even if the surface looks plain.

When in doubt, research. The cost of an unnecessary search is small. The cost of skipping research on a system that turned out to have hidden patterns is a missed finding that the audit was supposed to catch.

### How to Scope Research Queries

Good research queries are specific to the system you are analysing:

- "How to optimise the query planner in a relational database without changing query semantics" (when the project is a database engine)
- "Efficient nearest-neighbour search for two-dimensional continuous space" (when the project does spatial queries)
- "Reducing memory allocations in HTTP request handlers in a high-throughput service" (when the project is a web service)
- "Cache-friendly layout for sparse matrix multiplication" (when the project does numerical work)
- "Streaming compression algorithm choice for low-latency small-message workloads" (when the project does network compression)
- "Avoiding false sharing between worker threads in a lock-free queue" (when the project has lock-free data structures)
- "Buffer flattening and contiguous storage for tight numerical loops" (when the project has hot numerical loops over fragmented data)

Bad research queries are too generic:

- "How to write clean code"
- "Performance optimisation best practices"
- "Code refactoring techniques"

The discriminating question: would this query return advice that applies to *this specific system* with *this specific data* and *this specific access pattern*? If yes, the query is well-scoped.

### When Research Happens

Research happens in Pass 2, during the system-by-system deep dive, after you have read the code for that system. This timing is critical:

- You know the stack and the project context from Pass 1.
- You know the specific implementation from reading the code.
- Your research questions are therefore targeted and grounded.
- You can validate research findings against the actual code immediately.

### Validating Research Findings

Before turning a research finding into an audit recommendation:

1. **Does it apply to this specific implementation?** A general optimisation strategy may not apply to the specific data sizes, constraints, or patterns in this project.
2. **Does it violate either inviolable rule?** An optimisation that changes output, even slightly, is not a free change.
3. **Is the evidence strong?** Prefer findings from authoritative sources (language documentation, peer-reviewed research, well-known engineering write-ups from the relevant community) over generic advice.
4. **Can you demonstrate the improvement?** If you cannot explain why the optimisation works for this specific case with concrete reasoning grounded in the actual code, the recommendation is too speculative.

## 7. Diagnostic Test Writing

The audit writes tests as a tool for gathering evidence. When reading or research surfaces a question that a test could resolve better than further reading, write the test, run it, and use the result as the evidence for whatever finding it informs.

This is one of the most important shifts in how this skill works. The audit is no longer "analysis only" — it actively builds the verification scaffolding it needs to issue confident findings. The discrimination is precise: production source code is still off-limits, but tests are not production code. They are verification infrastructure that the audit owns and that the project gets to keep.

### When to Write a Diagnostic Test

Write a test when:

- **You need to compare implementations.** Two functions claim to do the same thing. A benchmark or equivalence test resolves "which is faster" or "do they actually behave the same" in a way that reading cannot.
- **You need to confirm a function is dead.** A function looks unused but might be invoked through reflection, dynamic dispatch, plugin systems, or external entry points. A test that exercises every plausible call site (or the absence of one) gives the audit the confidence it needs to recommend deletion.
- **You need to verify an algorithmic claim.** A finding proposes replacing one algorithm with another and asserts they produce identical output. An equivalence test on representative inputs proves it instead of asserting it.
- **You need to baseline current behaviour before recommending a change.** When proposing a refactor or layout change, a test that pins the current observable behaviour gives the implementing engineer something concrete to verify the new code against.
- **You need to expose hidden coupling.** A test that exercises a module in isolation will fail if the module has hidden dependencies the call chain hides — and the failure is itself a finding worth recording.
- **A critical code path has no coverage at all and you cannot reason safely about changes there.** Filling that gap is a precondition for issuing any finding that touches the path.
- **A finding's confidence level would jump from "moderate" to "high" if you had a test result.** That delta is exactly what diagnostic test writing exists for.

Do not write a test when:

- The question can be resolved by reading the code in five minutes. Tests are not a substitute for reading.
- The test would require rebuilding most of the system to set up. The cost of the scaffolding outweighs the value of the answer.
- The finding does not actually depend on the test result — you are writing the test to look thorough rather than because you need the evidence.

### What Kinds of Tests to Write

Use the lightest test that resolves the diagnostic question:

- **Unit tests** for behaviour of individual functions or modules.
- **Integration tests** for behaviour at the seams between modules or at system boundaries.
- **Equivalence tests** that run two implementations on the same inputs and assert their outputs match — the standard tool for "are these actually doing the same thing?"
- **Benchmarks** for "which one is faster" or "is the hot path actually hot." Capture the benchmark results in the finding.
- **Property tests or fuzz-style tests** when the question is "does this behave correctly across the input space?" rather than "does this work on this specific input?"
- **Coverage probes** — minimal tests that just exercise a path to confirm it is reachable, useful for dead-code analysis.

Match the test type to the question. A benchmark is wrong when you need an equivalence test. A unit test is wrong when the question is integration behaviour. The shape of the test follows the shape of the uncertainty.

### Where Diagnostic Tests Live

Tests go where the project's tests already live, following the project's existing test conventions for naming, structure, and layout. If the project has no test infrastructure at all, the audit can stand up the minimal setup needed (test framework, runner config, conventional directory) — but only what is actually required for the diagnostic work, not a full testing platform.

The audit commits the tests it writes as part of its work. They are not scaffolding to be deleted; they are a permanent improvement to the test suite. The implementing engineer should be able to run the same tests later to verify that proposed changes have been applied correctly and have not introduced regressions.

### How Diagnostic Tests Become Findings Evidence

When a finding is grounded in a test the audit wrote:

- Reference the test file path in the finding's evidence section.
- Summarise what the test asserts and what result it produced.
- Note that the test is part of the audit's output and can be re-run by the implementing engineer to verify the recommendation.

A finding backed by a test the audit wrote is the strongest kind of evidence in the audit's vocabulary — stronger than analytical reasoning, stronger than research, comparable to a profiler reading. Use this when you have it.

### What If a Diagnostic Test Reveals a Bug?

If the test you wrote to investigate one finding incidentally reveals a real correctness bug, that becomes a Known Issues and Active Risks finding immediately, with the failing test as the proof. This is exactly the kind of high-value surprise finding the audit should surface — a bug nobody knew about, caught by the verification work the audit was doing for a different reason. Record it, classify it, and let the implementing engineer prioritise the fix.

## 8. Exploration Discipline

### Read Before You Recommend

Never propose a change to code you have not read. This sounds obvious, but it is the most common source of bad findings. "This file is probably doing X" is not evidence.

### Follow the Full Path

When investigating potential dead code, trace the full call chain. When investigating a performance issue, find the hot path and read it carefully. When investigating an inconsistency, check all instances rather than the first two you find. When investigating a layout issue, read the actual access pattern and trace which fields the hot loop touches.

### Respect What You Do Not Understand

If you encounter code that seems unnecessary but you cannot explain why it exists, classify it as "Triage Needed" rather than "Dead Code." The code may serve a purpose that is not obvious from the source alone (runtime plugins, external triggers, backward compatibility, generated callers, downstream consumers in another repository).

### Stop When You Have Understood, Not When You Have Found Enough

The audit should be thorough. Stop when you have actually understood the system — what it does, how it works, what its hot paths are, what its data layouts look like, what domain-specific optimisations apply — not when you have produced enough findings to make the audit "look complete."

Zero findings on a computationally heavy system is a red flag, not an acceptable outcome. If a math-heavy module, a parser, a streaming pipeline, or a concurrency primitive returned only minor findings, the deep dive did not happen — go back and look harder.

Conversely, if a small utility module is genuinely clean after a careful read, having no findings is the correct result. The discrimination is depth of understanding, not finding count. Could a senior engineer specialising in this domain look at your analysis and say "yes, that is what the audit should have found"? If you cannot answer with confidence, the analysis is not done.
