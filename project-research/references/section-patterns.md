# Section Patterns

Choose the sections that best fit the question. Do not mechanically include every section every time. The aim is a strong fit between the problem and the artefact.

## High-Value Core Sections

These sections are strong defaults for many research artefacts.

### Scope / Purpose

Use this to define:

- what the artefact is trying to answer,
- what it is not trying to answer,
- how the repository-specific framing narrows the broader topic.

### Current Project Relevance

Use this to explain why the topic matters now in this repository:

- current implementation dependency,
- near-term engineering decision,
- architectural uncertainty,
- evaluation need,
- replacement candidate,
- scaling pressure.

### What The Topic Actually Is

Use this when shared conceptual grounding will make the rest of the paper much easier to understand. Keep it concise and high-signal.

### Research Signal

This is one of the most valuable sections. Use it to connect research-backed lessons to the repository's current implementation state.

Strong forms include:

- a table with `implementation choice`, `research signal`, and `repository implication`,
- a matrix of `supported`, `missing`, `uncertain`, and `not applicable`,
- a short ranking of which lessons matter most here and why.

### What Fits This Project Well

Use this to explain where the topic aligns with repository constraints, goals, and current architecture.

### What Fits This Project Badly

Use this to explain where the topic clashes with the repository's constraints, goals, or likely long-term direction.

### Current State Vs Research-Backed Expectations

Use this to compare:

- what the repository currently does,
- what stronger implementations typically include,
- which differences matter,
- which differences are acceptable for the repository's current stage.

### Maturity Ladder

Use this when the artefact benefits from a staged model such as:

- minimal / mediocre / strong / expert,
- prototype / credible / production-ready,
- baseline / reliable baseline / decision-grade baseline.

This section is especially good for implementation-heavy topics.

### Gap Analysis

Use this to identify:

- what is missing,
- what is weak,
- what is already good enough,
- what would be misleading to improve first.

### Recommended Priority Order

Use this to sequence work based on the repository's current reality. This section should not be a generic roadmap. It should say why the ordering is right here.

### What Not To Overbuild

Use this when a topic attracts unnecessary complexity. This often prevents the repository from turning an interim baseline into a long-term architectural centre.

### Alternatives That Materially Matter

Use this when adjacent options sharpen the decision. Mention alternatives only when they materially affect the recommendation.

### Open Uncertainties And Validation Needs

Use this to record where the research ends and experiment or implementation validation must begin.

### Relationship To Existing Context

Use this to show:

- which `context/` files this paper depends on,
- which existing references it extends or contrasts with,
- whether it supersedes or complements prior work.

## Strong Optional Supporting Sections

- `Foundational lessons`
- `Implementation lessons from practice`
- `Evaluation and benchmarking guidance`
- `Failure modes and misread signals`
- `Migration considerations`
- `Repository-specific constraints`
- `Terminology and framing notes`

## Pattern Rule

The artefact should feel inevitable after reading the title. If a section does not help answer the actual repository question, omit it.
