# Source Priority And Evidence

Research quality depends less on how many sources are mentioned and more on whether they are combined cleanly.

Use this evidence ladder.

## 1. Project Memory

Read the project's `context/` folder first.

Use it to learn:

- current architecture and subsystem boundaries,
- prior research that already exists,
- durable implementation notes,
- active decisions or partial work that may affect the topic.

Treat `context/` as prior memory, not unquestionable truth. If a high-stakes claim matters to the research conclusion, verify it in code.

## 2. Targeted Code Inspection

Inspect the smallest useful set of files that can verify the repository-specific claims.

Code inspection is for:

- confirming whether a mechanism actually exists,
- checking how it is implemented,
- understanding current constraints and interfaces,
- detecting when an apparent recommendation is already in place,
- preventing incorrect project descriptions.

Code inspection is not a mandate to traverse the entire repository. Use it with purpose.

## 3. External Research

External research is the main breadth and depth source for this skill.

Prefer high-signal sources such as:

- foundational papers,
- major follow-up or correction papers,
- official documentation,
- widely respected engineering write-ups,
- strong open-source implementations that are relevant to the repository's constraints,
- benchmarks or evaluations when they materially affect the decision.

Use adjacent alternatives only when they improve the project decision. Do not mention them just to look comprehensive.

## 4. Explicit Inference

Inference is expected and necessary. The important rule is to label it honestly.

Use inference for:

- repository-specific judgement,
- priority ordering,
- maturity ladders,
- likely implementation risks,
- translation from generic research to project-specific guidance.

Never present inference as direct evidence.

## Evidence Labelling

When a section makes mixed claims, keep the distinction visible. The artefact should make it easy to see:

- `repository fact`
- `source-backed finding`
- `project inference`
- `open uncertainty`

This can be done through prose, callouts, table columns, or explicit section notes. The exact presentation may vary. The separation itself is mandatory.

## Source Taxonomy

Try to understand the topic through multiple evidence surfaces when relevant:

- foundational theory,
- implementation practice,
- production constraints,
- adjacent alternatives,
- evaluation methodology,
- repository reality.

Do not force every taxonomy bucket into every paper. Use only the buckets that sharpen the question.

## Failure Modes

Common evidence failures:

- trusting `README.md` as if it were implementation proof,
- describing the repo without checking relevant code,
- citing papers without extracting the implementation lesson,
- listing alternatives without tying them back to the repository,
- mixing factual observation and recommendation into one unsupported paragraph.
