# Mathematical And Scientific Writing

## Table of Contents

1. [Core Rule](#core-rule)
2. [Required Elements For Major Technical Topics](#required-elements-for-major-technical-topics)
3. [Notation Standard](#notation-standard)
4. [Equation Standard](#equation-standard)
5. [Worked Example Standard](#worked-example-standard)
6. [Scientific Topics](#scientific-topics)
7. [Alternatives And Debates](#alternatives-and-debates)
8. [Accessibility Rule](#accessibility-rule)
9. [Failure Modes](#failure-modes)

Use this reference for any topic where formal or scientific reasoning materially improves the teaching, such as:

- algorithms with important formal machinery,
- optimisation and numerical methods,
- probability, statistics, and stochastic processes,
- control theory and dynamical systems,
- simulation and modelling,
- cryptography and security protocols,
- distributed systems and consensus,
- signal processing and information theory,
- domain-specific scientific foundations relevant to the project.

## Core Rule

If mathematics or scientific mechanism materially improves understanding, include it.

Do not strip a technical topic down to prose-only explanation when equations, notation, diagrams, or worked examples would teach it better.

## Required Elements For Major Technical Topics

When relevant, major technical files should include:

- prerequisites,
- notation,
- formal definitions,
- equations,
- plain-English interpretation of the equations,
- worked examples,
- implementation or project relevance,
- alternatives or competing viewpoints,
- limitations or caveats,
- misconceptions.

Not every topic needs every element equally, but serious technical topics usually need most of them.

## Notation Standard

If notation appears:

- define it explicitly,
- keep it consistent,
- avoid switching symbols unnecessarily,
- restate the meaning in plain English.

Do not assume the learner remembers symbol choices from elsewhere.

## Equation Standard

Use equations when they clarify:

- update rules,
- objective functions,
- decomposition of a quantity,
- recurrence relations,
- geometric relationships,
- probabilistic definitions,
- state transitions,
- learning rules.

After each important equation, explain:

- what each term means,
- what the equation is doing intuitively,
- why it matters to the project or concept.

## Worked Example Standard

For major mathematical topics, include at least one worked example whenever possible.

Good worked examples:

- plug in concrete numbers,
- walk through intermediate steps,
- show how the abstract rule behaves,
- connect back to project reality.

If the topic is central, include more than one worked example when useful.

## Scientific and Domain-Specific Topics

For topics grounded in a specific scientific or technical domain (distributed consensus, fluid dynamics, compiler theory, signal processing, biological learning, etc.), combine:

- intuitive explanation,
- precise mechanism description,
- terminology clarification,
- comparison with nearby concepts,
- project relevance,
- what is established knowledge versus speculative or roadmap-facing application.

## Alternatives And Debates

When a field contains major alternatives or competing framings, explain them.

Examples:

- Paxos vs Raft for consensus,
- optimistic vs pessimistic concurrency control,
- gradient descent vs evolutionary strategies for optimisation,
- batch processing vs stream processing for data pipelines.

Do not present one idea as if there are no meaningful alternatives when the comparison is educationally important.

## Accessibility Rule

Write rigorous technical content in clear language.

After dense sections, add plain-language interpretation.

The learner should not need to decode research-paper prose to understand the archive.

## Failure Modes

Treat these as failures:

- a technical file with no equations where equations would help,
- a domain-specific file with only vague metaphors instead of precise mechanisms,
- notation introduced without explanation,
- equations presented without interpretation,
- a difficult topic with no numeric or concrete example.
