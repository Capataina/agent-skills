# Mathematical And Scientific Writing

Use this reference for topics such as:

- reinforcement learning,
- optimisation,
- probability and statistics,
- control,
- simulation,
- neuroscience,
- dynamical systems,
- algorithms with important formal machinery.

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

## Scientific Topics

For topics like neuroscience or biological learning, combine:

- intuitive explanation,
- precise mechanism description,
- terminology clarification,
- comparison with nearby concepts,
- project relevance,
- what is established knowledge versus speculative or roadmap-facing application.

## Alternatives And Debates

When a field contains major alternatives or competing framings, explain them.

Examples:

- Hebbian learning vs backpropagation,
- one-step TD vs GAE,
- shared-trunk vs separate actor/critic architectures,
- rate-based vs spike-based models.

Do not present one idea as if there are no meaningful alternatives when the comparison is educationally important.

## Accessibility Rule

Write rigorous technical content in clear language.

After dense sections, add plain-language interpretation.

The learner should not need to decode research-paper prose to understand the archive.

## Failure Modes

Treat these as failures:

- an RL file with no equations where equations would help,
- a neuroscience file with only vague metaphors,
- notation introduced without explanation,
- equations presented without interpretation,
- a difficult topic with no numeric or concrete example.
