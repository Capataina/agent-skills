# Examples

This file contains worked examples of how to shape research for a repository. Do not copy them mechanically. Use them to understand the level of synthesis and project grounding expected.

## Example 1: Single-File Research Paper

Topic:

- `A2C for this project`

Strong output shape:

- `context/references/a2c.md`

Why one file works:

- one stable topic,
- one dominant question,
- comparisons and maturity analysis fit cleanly as sections.

Good section mix:

- scope and purpose,
- current project relevance,
- what A2C actually is,
- research signal,
- what fits this project well,
- what fits this project badly,
- current state vs research-backed expectations,
- maturity ladder,
- gap analysis,
- recommended priority order,
- relationship to existing context.

## Example 2: Comparative Decision Paper

Topic:

- `SAC vs A2C for this project`

Strong output shape:

- `context/references/sac-vs-a2c.md`

Key moves:

- do not describe both algorithms in isolation for most of the paper,
- keep comparing them through the repository's constraints,
- end with a conditional decision rather than a vibes-based preference.

Useful sections:

- decision framing,
- repository constraints,
- comparison matrix,
- what each approach demands from the current codebase,
- transition costs,
- recommendation under current assumptions,
- what evidence could reverse the recommendation.

## Example 3: Topic Folder

Topic:

- `actor-critic methods for this repository`

Strong output shape:

```text
context/references/actor-critic/
├── overview.md
├── a2c.md
└── sac-vs-a2c.md
```

Why a folder works:

- there is a stable research area,
- multiple papers share context,
- follow-up work is likely,
- one file would become crowded.

Folder roles:

- `overview.md`:
  the area map, relationships, and where each paper fits
- `a2c.md`:
  single-topic deep dive
- `sac-vs-a2c.md`:
  explicit decision surface

## Example 4: Strong Research Signal Pattern

Useful table shape:

| Topic | Source-backed signal | Current repository state | Project implication |
|---|---|---|---|
| Observation normalisation | Often matters in practice for stable on-policy training | Static scaling only | Meaningful gap if instability persists |
| Separate value / policy networks | Often a strong default in tested settings | Already present | Preserve; not a priority area |
| Checkpointed evaluation | Crucial for honest comparison | Missing | High leverage for decision quality |

Why this works:

- the section does not merely list lessons,
- it translates them into repository consequences.

## Example 5: Weak Vs Strong Conclusion

Weak:

> A2C is a good algorithm and has been used in many projects. SAC is also strong and may be better in some situations.

Strong:

> In this repository, A2C still makes sense as a near-term baseline because the observation space is compact, the action space is continuous, and the current question is "is the environment learnable at all?" The main catch is that the current implementation discipline is not yet strong enough to make negative results highly trustworthy. That means the first research-backed priority is not algorithm novelty but baseline credibility.

Why the strong version works:

- it answers the project question,
- it names the governing constraint,
- it turns research into a decision.
