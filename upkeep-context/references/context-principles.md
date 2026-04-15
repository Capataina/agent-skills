# Context Principles

## Table of Contents

1. [Core Definition](#core-definition)
2. [Required Qualities](#required-qualities)
3. [Truth Model](#truth-model)
4. [Evidence Standard](#evidence-standard)
5. [Rationale Capture From Code](#rationale-capture-from-code)
6. [What Belongs In Context](#what-belongs-in-context)
7. [What Does Not Belong In Context](#what-does-not-belong-in-context)
8. [Canonical Ownership Principle](#canonical-ownership-principle)
9. [Supportive Presentation Principle](#supportive-presentation-principle)
10. [Stability Principle](#stability-principle)

This reference defines what `context/` is, what it must achieve, and what it must never become.

## Core Definition

`context/` is the repository's working memory layer.

Its job is to let a capable engineer or agent understand:

- what the repository contains,
- how the major systems fit together,
- what currently exists,
- what is partial, fragile, or missing,
- what previous attempts still matter,
- where a change will likely have downstream effects.

It is not a generic documentation bucket. It is a maintained implementation-state layer.

## Required Qualities

### Comprehensive, not thin

Someone who reads `context/` should be able to understand the repository as a whole without doing a first-pass rediscovery from code.

Comprehensive means the folder captures:

- repository structure,
- subsystem boundaries,
- core interfaces and flows,
- implementation reality,
- known issues and risks,
- durable lessons from past attempts.

It does not mean verbosity for its own sake.

### Thorough, not redundant

The standard is:

> say as much as needed without redundancy or padding

`context/` should be faster to read than re-exploring the repository. If a document becomes so sparse that a reader must immediately re-derive the basics from code, the memory layer has failed.

### Dynamic, not archival

`context/` must change with the repository.

It should track current reality, not preserve every intermediate state that once existed. Files must be updated, merged, split, renamed, or deleted as the repository changes.

### Durable, not chronological

Preserve durable knowledge:

- why an approach was discarded,
- what failed and why,
- what constraints remain because of it,
- what would need to be true to revisit it safely.

Do not preserve chronological accumulation:

- "today we did X",
- "yesterday we tried Y",
- weekly change logs,
- stacked milestone records.

### Adaptive, not threshold-driven

Do not decide depth or structure from arbitrary repo-size labels or fixed numeric cutoffs.

Instead, adapt to:

- boundary clarity,
- overlap pressure,
- dependency complexity,
- change independence,
- and how much explanation a future reader would need to act safely.

## Truth Model

When maintaining `context/`, treat the repository itself as primary evidence for implementation truth.

Use the existing `context/` folder as prior memory:

- valuable when accurate,
- correctable when stale,
- replaceable when structurally wrong.

Do not let polished old documents override the actual codebase.

## Evidence Standard

Context claims should be grounded in inspected repository evidence.

That means:

- inspect representative entrypoints and owning modules,
- read enough code and configuration to justify major subsystem boundaries,
- distinguish direct observation from inference,
- avoid confident claims about behaviour that was not actually verified.

The skill does not need a fixed file-count quota. It needs enough evidence to support its claims.

### Confidence Through Word Choice

The way a claim is worded should naturally communicate how well it is grounded.

When a statement is directly verified in code — an import exists, a function signature was inspected, a configuration value was read — it can stand as a plain assertion. "The API layer uses Express with middleware-based auth."

When a statement is inferred from structure, naming, or convention rather than direct inspection, the wording should reflect that. Phrases like "appears to," "likely," "based on the directory structure," or "judging from the naming pattern" signal that the claim rests on reasonable inference rather than confirmed observation.

When something is genuinely uncertain and could affect future work, consider including an explicit verification question or noting the gap directly. "The caching layer may use Redis — the dependency is present but no configuration was found."

This is not a formal tagging system or a required annotation format. It is a writing habit: let the reader gauge confidence from the natural language rather than having to guess whether every statement was fully verified.

## Rationale Capture From Code

Code sometimes contains explanatory comments that carry project knowledge beyond what the code itself expresses — `WHY`, `NOTE`, `HACK`, `IMPORTANT`, `TODO` annotations with substantive context, or plain comments explaining a design decision, workaround, or constraint.

During upkeep, when reading code to verify system reality, watch for these. If a comment explains something that would affect how a future session reasons about the system — why an approach was chosen, what constraint forced a workaround, what assumption a piece of code depends on — consider surfacing that rationale into the relevant system file's durable notes section.

Not every code comment warrants this treatment. The threshold is whether the rationale is durable and cross-session: would a future session benefit from knowing this without having to rediscover it in the code? If yes, capture it. If the comment is a local implementation note that only matters when editing that specific function, leave it in the code where it belongs.

When surfacing rationale, attribute it lightly — note where in the codebase the reasoning was found so a future reader can verify or revisit it.

## What Belongs In Context

`context/` should capture:

- architecture and repository shape,
- subsystem responsibilities,
- dependency direction and important flows,
- current implemented reality,
- partial work and active risks,
- planned or missing work tied to the owning subsystem,
- durable notes from prior attempts,
- obsolete approaches when still relevant to future decisions,
- project preferences, guiding principles, and design rationale that shape future work,
- trial-and-error outcomes — what was tried, what failed, and why it matters going forward,
- supporting infrastructure — testing frameworks, build systems, CI/CD pipelines, deployment configuration, dev tooling — when they carry real complexity, independent change pressure, or non-obvious configuration that a future session would need to understand.

Supporting systems belong in context when they are complex enough to warrant documentation, not because every project needs a file for its test runner. A project with a single `npm test` script and default Jest config probably does not need a testing system file. A project with custom test harnesses, multiple test categories, conditional CI behaviour, or environment-dependent test configuration probably does.

## What Does Not Belong In Context

Avoid:

- product specifications,
- roadmap documents detached from implementation ownership,
- release notes,
- changelogs,
- meeting notes,
- brainstorming dumps,
- milestone-by-milestone narrative progress files,
- generic history files,
- undifferentiated catch-all dump files.

## Canonical Ownership Principle

Every important topic should have one primary home.

Examples:

- architecture belongs in `architecture.md`,
- payment processing implementation reality belongs in `systems/payments.md`,
- a failed caching strategy belongs inside the owning system doc if it still affects future decisions,
- a guiding principle about API design may belong in `notes/api-design.md`,
- a REST versus GraphQL research comparison may belong in `references/rest-vs-graphql.md`.

This rule reduces overlap and prevents memory drift.

## Supportive Presentation Principle

Different markdown structures can support the same canonical topic inside one document.

For example:

- a table may inventory interfaces,
- bullets may summarize the operational implications,
- a diagram may show the same flow at a glance.

That is supportive presentation, not duplicate ownership.

The line is simple:

- multiple formats inside one owning document are allowed when they improve comprehension,
- multiple documents acting as co-owners of the same topic are not.

## Stability Principle

Repeated upkeep should not thrash a healthy folder.

The skill should preserve existing structure when it is:

- coherent,
- low-overlap,
- and still aligned with the codebase.

Good-enough structure is often preferable to perfect theoretical structure if perfect structure would create needless churn.
