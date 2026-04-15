# Content Depth Standards

## Table of Contents

1. Goal
2. Comprehensive but Non-Redundant
3. Architecture Depth Expectations
4. System Document Depth Expectations
5. Depth Audit Questions
6. Producer and Consumer Perspectives
7. Evidence and Inference
8. Verification Questions
9. System File Maturity Assessment
10. Linter Shallow-Document Thresholds
11. Signs a Document Is Too Shallow
12. Signs a Document Is Overwritten

## 1. Goal

The goal is a `context/` folder that is sufficient to understand the project without opening the code. A reader who works only from `context/` should come away with a clear model of what is implemented, how it is structured, where the boundaries are, and what the active risks are. If that is not possible, the documentation is insufficient.

Preventing immediate code rediscovery is the minimum bar. Comprehensive project understanding is the target.

## 2. Comprehensive Without Redundancy

A strong context document should:

- cover the dimensions that matter for its role,
- be grounded in observed implementation reality,
- include enough detail to guide later work,
- avoid repeating the same fact in multiple documents as if each were canonical.

Depth is a virtue. Avoiding redundancy means avoiding the same fact appearing in two canonical homes — it does not mean avoiding thorough explanation. A system document that explains a subsystem clearly and completely is correct; a system document that lists components without explaining what they do or how they interact is insufficient.

## 3. Architecture Depth Expectations

`architecture.md` should usually cover:

- what the repository is and what it currently implements,
- a meaningful structure tree with important subdirectories and notable files,
- the major subsystem map,
- dependency direction between major layers,
- the main execution and data-flow pipelines,
- structural constraints or current-reality caveats that affect engineering work.

Depth should increase when:

- the repo has multiple layers or runtimes,
- there are important generated or non-source directories worth distinguishing,
- major behaviour depends on configuration or toolchain boundaries,
- different subsystems interact in non-obvious ways.

## 4. System Document Depth Expectations

A strong `systems/*.md` file should usually cover these dimensions when relevant to that subsystem:

- purpose,
- boundaries and ownership,
- current implemented behaviour,
- key interfaces or data flow,
- important artefacts or modules,
- active risks,
- partial work,
- missing or likely changes,
- durable lessons,
- obsolete assumptions.

Not every subsection needs the same density, but the document should not collapse into one-line bullets if the subsystem is materially important.

### Failure Propagation Depth

When a system has meaningful dependents, the "Known Issues / Active Risks" section benefits from tracing downstream impact — not just "this system has risk X" but "if this system fails or misbehaves, here is what happens to systems that depend on it." A cache that silently serves stale data is one kind of problem; a cache that silently serves stale data to a billing pipeline is a different severity entirely.

This is proportionate to dependency count. A standalone utility with no consumers does not need propagation analysis. A system that sits on a critical path or feeds multiple consumers should document what breaks when it breaks, because that context is expensive to rediscover under pressure.

### Historical Failure Patterns

The "Durable Notes / Discarded Approaches" section is most useful when it captures the failure mode, not just the failure fact. "We tried approach X and it didn't work" saves some rediscovery time. "We tried approach X, it appeared to work in testing, but under production load it caused symptom Y which looked like problem Z but was actually caused by W, and it took three days to diagnose" saves substantially more.

When a past failure involved misleading symptoms, a non-obvious root cause, or a long diagnostic path, capturing that detail is valuable. The goal is to arm future sessions with the diagnostic reasoning, not just the conclusion.

## 5. Depth Audit Questions

These questions help assess whether a system document has reached useful depth. They are not a checklist that every document must satisfy — they are probes that surface gaps worth considering.

- Does "Current Implemented Reality" trace a representative request or operation end-to-end through the system? A document that names components without showing how they interact during actual execution often leaves the reader unable to reason about behaviour.
- Does "Key Interfaces / Data Flow" document actual data shapes, not just "it calls the API"? Knowing that service A calls service B is architectural. Knowing what service A sends and what it expects back is operational. The operational detail is where debugging happens.
- Does "Known Issues / Active Risks" distinguish between theoretical risks and observed problems? A theoretical risk is worth noting. An observed problem that has actually caused an incident is worth explaining in detail. Mixing them without distinction makes it hard to prioritise.
- Does "Durable Notes / Discarded Approaches" explain why approaches were abandoned, not just that they were? "We considered X" is a fact. "We considered X because it would solve Y, but it introduced Z which was unacceptable because of W" is a durable lesson.

## 6. Producer and Consumer Perspectives

When a system has meaningful relationships with other systems, documenting it from both the producer and consumer perspectives surfaces information that a single perspective misses.

**Producer perspective** covers what the system does and outputs — its responsibilities, its interfaces, its guarantees. This is the natural perspective most system documents adopt.

**Consumer perspective** covers what depends on the system, what assumptions consumers make about its output, and what contracts consumers rely on. This is where surprising breakages tend to hide. A system can work perfectly by its own definition while breaking a consumer that assumed something about its output format, timing, ordering, or completeness that was never explicitly guaranteed.

Documenting consumer assumptions is particularly valuable when:

- multiple systems consume the same output,
- the output format has evolved over time and different consumers may rely on different historical shapes,
- the system's implicit contracts (ordering, completeness, timing) are not enforced by its interface.

This is not a requirement for every system file. A self-contained system with no external consumers does not need consumer-perspective documentation. But when a system sits at a boundary that other systems depend on, the consumer perspective is often where the most valuable undocumented knowledge lives.

## 7. Evidence and Inference

Prefer statements grounded in direct evidence from:

- entrypoints,
- owning modules,
- configuration,
- tests,
- scripts,
- existing context that still matches the codebase.

When something is inferred:

- keep the wording cautious,
- avoid presenting the inference as verified implementation truth.

## 8. Verification Questions

When a system file contains claims that are inferred rather than directly verified, it is useful to include explicit questions that would resolve the uncertainty. These give the next session a concrete thing to check rather than silently re-trusting a previous session's inference.

For example, if a document states that a cache invalidates on writes but the agent only observed write-path code without tracing the full invalidation logic, a verification question like "Does the cache actually invalidate on writes, or only on TTL expiry?" flags the specific uncertainty. The next session can look at the invalidation path and either confirm the claim or correct it.

Good verification questions are:

- specific enough to be answerable by reading a particular piece of code or running a particular test,
- attached to the claim they question, not collected in a separate section far from context,
- framed as genuine uncertainty, not rhetorical.

This is most useful when a session ran out of time to fully verify something, when the codebase was ambiguous, or when behaviour depends on runtime conditions that static analysis cannot confirm. Not every inferred claim needs a verification question — only those where being wrong would meaningfully mislead future work.

## 9. System File Maturity Assessment

It is useful to have a shared vocabulary for how developed a system file is. This helps both the agent and humans understand where more work is needed without implying that every file must reach the highest level.

**Stub.** The file exists and names the system's purpose and boundaries, but little else. A reader knows the system exists and roughly what it does. They would still need a full code-level discovery to work with it. Observable signs: mostly one-line bullets, missing sections for risks or interfaces, under the linter's shallow-document threshold.

**Working.** The file covers the basics — purpose, current implemented behaviour, key interfaces, known risks. A reader can understand the system well enough to make informed decisions about changes, though they may need to check the code for specifics. Observable signs: clears the linter threshold, most relevant sections are present and have multi-line content, but data shapes may be described generically and failure modes may be incomplete.

**Comprehensive.** The file captures full operational depth — data models, interface contracts, failure modes with downstream impact, historical context for design decisions, and enough detail that a reader rarely needs to open the code except for line-level implementation questions. Observable signs: representative operations are traced end-to-end, data shapes are documented concretely, discarded approaches include diagnostic reasoning, consumer assumptions are captured where relevant.

Most system files in an active project will be at the working level, which is appropriate. Stub files should be expanded when the system is next touched. Comprehensive depth is worth pursuing for systems that are complex, critical, or frequently misunderstood — but treating it as a universal requirement creates busywork for simple systems.

## 10. Linter Shallow-Document Thresholds

The bundled `lint_context.py` flags documents that fall below minimum line counts as likely too shallow:

- `architecture.md`: flagged if under 25 non-empty lines.
- `systems/*.md` files: flagged if under 30 non-empty lines.

These are minimum floors, not targets. A document that barely clears the threshold is not automatically adequate. The thresholds exist to catch obviously incomplete output; the real depth standard is whether a reader can understand the topic without opening the code.

## 11. Signs a Document Is Too Shallow

Warning signs include:

- repository structure stops at superficial folder names,
- system docs name components but do not explain ownership or interfaces,
- risks and partial work are absent in a clearly evolving subsystem,
- a new reader would still need a first-pass rediscovery from code,
- every section is a flat list of short bullets with little differentiation.

## 12. Signs a Document Is Overwritten

Warning signs include:

- the document mirrors code almost line by line,
- structural sections are crowded with low-signal detail,
- multiple sections restate the same facts in slightly different wording,
- prose becomes slower to read than opening the actual source files.
