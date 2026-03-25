---
name: project-research
description: "Conducts project-grounded technical research and writes durable reference material into `context/references/`. Use when asked to research an algorithm, architecture, implementation strategy, tooling option, protocol, subsystem pattern, or comparison such as `A2C for this project`, `SAC vs A2C for this repo`, or `research best practices for implementing X here`. Reads the project's `context/` first, inspects relevant code to verify current reality, performs substantial external research by default, and produces one paper or a small reference folder when scope warrants it. Not for quick summaries, generic web lookups, release notes, or bug fixing."
---

# Project Research

Maintain `context/references/` as the repository's durable research layer. The goal is not generic topic explanation. The goal is to run a serious research pass that starts from project reality, expands into external literature and real-world implementations, then comes back with repository-relevant guidance that remains useful after the session ends.

Before generating or editing any research artefact, read the reference files in this order:

1. Read `references/operating-modes.md` first.
   It defines the three supported workflows and the default scope rules.
2. Read `references/source-priority-and-evidence.md` second.
   It defines how to combine project evidence, code inspection, and external sources without blurring them together.
3. Read `references/project-grounding-workflow.md` third.
   It defines how to anchor the research in `context/` and targeted code inspection before writing conclusions.
4. Read `references/decomposition-rules.md` fourth.
   It defines when to write one paper, when to create a topic folder, and how to avoid fragmented output.
5. Read `references/section-patterns.md` fifth.
   It defines the highest-value sections and how to use them selectively.
6. Read `references/formatting-patterns.md` sixth.
   It defines the richer markdown structures this skill should use when they improve comprehension.
7. Read `references/anti-patterns.md` seventh.
   It defines the failure modes that make research look impressive while saying very little.
8. Read `references/examples.md` last.
   It contains worked examples of stronger output shapes and higher-value analysis moves.

## Core Identity

This skill is not a generic summariser, search assistant, or literature-dump generator.

It exists to produce **project-grounded external research** that:

- explains what the topic is and why it matters here,
- surveys the strongest relevant research and practical implementations,
- verifies what already exists in the repository,
- distinguishes source-backed findings from project-specific inference,
- translates findings into concrete guidance for this repository,
- stores the result in `context/references/` as durable project memory.

It must reject:

- README-only reasoning,
- shallow "topic overview" output,
- unrelated side quests,
- recommendation lists that ignore current implementation reality,
- rigid quota-thinking such as arbitrary paper counts,
- decorative formatting without analytical value.

## Priority Order

When trade-offs exist, optimise in this order:

1. Research must stay grounded in the repository's current reality.
2. External research must be broad and deep enough to support real decisions.
3. The output must preserve durable insights, not just session-local conclusions.
4. The artefact should match the true scope: one paper when coherent, a folder when decomposition is justified.
5. Formatting should increase scanability and synthesis value, not become ornament.
6. Repeated research runs should improve the references corpus without creating duplication.

## Supported Output Model

Write into `context/references/` using stable topic ownership.

Default patterns:

```text
context/
└── references/
    ├── a2c.md
    ├── rendering-pipeline.md
    ├── storage-engine-comparison.md
    └── actor-critic/
        ├── overview.md
        ├── a2c.md
        └── sac-vs-a2c.md
```

Prefer one file when the topic has one stable question and one coherent answer.

Prefer a topic folder when:

- the research naturally decomposes into multiple stable subtopics,
- one paper would become bloated or internally contradictory,
- future follow-up research is likely to extend the same area,
- multiple papers need a shared home with cross-references.

Do not create filler files just because a folder exists.

## Naming Rules

Prefer lowercase hyphenated filenames and folder names.

Use the shortest stable topic name that remains unambiguous in `context/references/`.

Good examples:

- `a2c.md`
- `sac-vs-a2c.md`
- `ecs-scheduling.md`
- `network-stack/`
- `network-stack/retry-strategy.md`

Avoid:

- date-stamped filenames,
- vague names such as `research.md`,
- names tied to one temporary prompt phrasing,
- duplicated topics split across multiple near-identical files.

## Operating Modes

Choose one of these modes:

- `Project-grounded external research`
  Default. Research a topic broadly and deeply, then translate it into project-specific guidance.
- `Project-grounded comparative decision research`
  Use when the core question is a comparison, trade-off, or selection for this repository.
- `Update / merge / extend existing research`
  Use when refining, consolidating, cross-referencing, or restructuring the existing research corpus in `context/references/`.

Do not invent a repo-only research mode as the default. Internal inspection is mandatory grounding, not the main research surface.

## Evidence Standard

Treat the repository as the source of truth for what is implemented now.

Use this evidence ladder:

1. `context/` for current durable project memory,
2. targeted code inspection for implementation verification,
3. external papers, documentation, and real-world implementations for broader research,
4. explicit inference for repository-specific interpretation and recommendations.

Never blur these together. A good artefact makes it obvious:

- what the codebase already does,
- what outside sources say,
- what you infer for this project,
- where uncertainty remains.

## Mandatory Script Usage

This skill is script-backed. The bundled scripts are mandatory parts of the workflow.

- Run `scripts/init_research_artifact.py` before writing a new paper or new topic folder.
- Run `scripts/validate_research_artifact.py` before presenting any completed creation or update.
- Use the scripts as deterministic scaffolding and structure validation, not as substitutes for judgment.
- If a script genuinely cannot run, say so explicitly and follow the fallback guidance in the relevant reference file.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Determine the operating mode from the user's request and the current state of `context/references/`.
2. Read the project's `context/` folder first, especially files that already touch the topic or subsystem.
3. Identify the smallest set of code paths needed to verify current implementation reality.
4. Inspect those files before forming project-specific claims.
5. Run substantial external research by default:
   papers, implementation references, engineering write-ups, official docs, and comparisons where they materially sharpen the decision.
6. Decide whether the result belongs in one paper, a topic folder, or an update to existing research.
7. Run `scripts/init_research_artifact.py` to scaffold the output location.
8. Write or update the artefact using the section patterns that best fit the topic.
9. Cross-reference related material already in `context/references/` when the relationship is meaningful.
10. Run `scripts/validate_research_artifact.py`.
11. Fix any hard failures and review warnings with judgment.
12. Present the created or updated research artefact, its placement, and any remaining uncertainties.

## Writing Standard

Write like a technically serious engineer-teacher, not like a dry journal abstract and not like a casual blog post.

The target style is:

- readable in one pass,
- scientifically precise where precision matters,
- explicit about mechanisms and trade-offs,
- comfortable mixing plain-language explanation with advanced terminology,
- dense with insight rather than dense with jargon.

The target artefact should read like a durable synthesis paper for the repository, not like notes from a search session.

## Composition Rules

Use the clearest format for the information at hand:

- bullets for concise takeaways and recommendation lists,
- tables for comparisons, gap analyses, and implementation matrices,
- trees for topic-folder structure when decomposition matters,
- ASCII diagrams or mermaid only when flows or relationships are clearer that way,
- short template blocks when a structure is easier to understand from a skeleton than from prose.

Supportive multi-format presentation inside one artefact is good when it helps scanning and reasoning.

Do not duplicate canonical ownership across artefacts. If one file is the home for a stable topic, related files should reference it rather than re-explaining it fully.

## Quality Checklist

Before considering the research artefact complete, verify:

- the artefact lives in the right place under `context/references/`,
- the topic is grounded in current project reality, not in README-only impressions,
- relevant code was inspected before making project-specific claims,
- external research is substantial enough to justify the conclusions,
- source-backed findings, repository facts, and inference are clearly separated,
- the section mix fits the actual question rather than following a rigid template blindly,
- the artefact says what fits this project, what does not, and why,
- recommendations are prioritised and tied to the repository's current state,
- related existing research is referenced or updated rather than duplicated,
- formatting improves comprehension,
- `scripts/init_research_artifact.py` was used for new artefacts unless a genuine fallback was needed,
- `scripts/validate_research_artifact.py` was run unless a genuine fallback was needed.
