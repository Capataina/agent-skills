---
name: upkeep-context
description: "Maintains a repository-level context folder as durable implementation memory. Use when asked to create, initialise, regenerate, audit, clean up, restructure, repair, or update a project's context/ documentation by reading the repository, running the bundled repo scan and context lint scripts, and producing canonical architecture and subsystem documents grounded in current code reality. Prefers feature-adjacent or subsystem-adjacent files over milestone slices, preserves durable lessons, supports richer markdown structures such as trees, tables, matrices, and diagrams when they improve comprehension, and keeps context docs comprehensive without redundancy. Not for product specs, roadmaps, release notes, changelogs, or general-purpose prose docs."
---

# Upkeep Context

Maintain a `context/` folder as the repository's working memory layer. The goal is durable, implementation-grounded memory that lets a future engineer or agent understand the repository quickly without re-deriving everything from code.

## Reference Loading

Before editing or generating any `context/` files, read the **mandatory core**. These four files apply to every invocation of this skill:

1. `references/context-principles.md` — what `context/` is for, what it must contain, and what it must never become.
2. `references/document-model.md` — the canonical file types, section templates, and how canonical ownership works.
3. `references/upkeep-decision-rules.md` — when to preserve, update, merge, split, rename, or delete files with low churn.
4. `references/cross-system-analysis.md` — techniques for surfacing inter-system relationships, dependency chains, hubs, knowledge gaps, and surprising connections. Read this even if you suspect the project is simple; the Mandatory Analytical Obligations below still apply.

Then apply the following task-based rules. Read the additional file before doing the matching kind of work:

**Choosing file boundaries or restructuring the folder:**
Read `references/granularity-rules.md` before deciding how to split, merge, or scope files in `systems/`.

**Diagnosing or correcting a folder that looks broken:**
Read `references/anti-patterns.md` before declaring a structural problem and before proposing a corrective restructure.

**Running the bundled scripts (always required for non-audit runs):**
Read `references/script-contract.md` before running `scan_repo.py` or `lint_context.py`, and before deciding what to do if a script cannot run.

**Expanding architecture or system documents:**
Read `references/content-depth-standards.md` before writing or expanding `architecture.md` or any `systems/*.md` file. It defines the depth bar these documents must clear.

**Adding rich visual structure to a context document:**
Read `references/markdown-presentation-patterns.md` before adding substantial tables, diagrams, trees, or ASCII visualisations. It documents the patterns this skill uses for dense visual content.

**Creating or maintaining a plan file:**
Read `references/plan-file-guidance.md` before creating, updating, or restructuring any file in `plans/`.

**Uncertain about how a structural decision should land in practice:**
Read `references/examples.md` for worked examples of good decompositions, supportive multi-format presentation, and common corrections.

The mandatory core is always required because it carries the principles, document model, and decision rules that every operation depends on. The task-based files carry depth on specific patterns and should be read when the work calls for them — read them eagerly when in doubt rather than guessing.

## Core Identity

This skill is not a generic summariser, changelog generator, or planning assistant.

It maintains a **repository memory layer** that captures:

- current implementation reality,
- subsystem boundaries and interfaces,
- dependency and execution flows,
- cross-system relationships, shared state, and integration points,
- active risks, partial work, and downstream blast radius,
- durable lessons from prior attempts,
- project preferences, design rationale, and guiding principles as evolving notes,
- recurring conventions and patterns that shape how the project is built,
- maintainable reference material whose relevance depends on current project reality,
- temporary execution plans only when explicitly requested or clearly necessary.

The standard for `context/` completeness is high: a reader working only from `context/` should be able to understand the entire project. If that is not possible after reading `context/`, the documentation is insufficient, not just imperfect. Architecture files, system files, and reference material should be written at a depth that makes immediate code rediscovery unnecessary.

It must reject:

- milestone-based or phase-based slicing,
- diary-style history,
- duplicated canonical ownership across files,
- speculative subsystem files,
- static research archives that are never revisited as the repository changes,
- cosmetic rewrites that create churn without improving understanding.

### Tool-Bias Warning

Pretraining biases this agent toward the tools and actions that feel comfortable — reading files, running the bundled scripts, producing plausible markdown — and away from investigative actions that have no single obvious tool call, such as actively probing for shared data structures, tracing a critical operation end-to-end, or enumerating what was not inspected. When you catch yourself drafting reasons why the Mandatory Analytical Obligations below are "not needed for this project," treat that drafting itself as evidence the bias is firing. Execute the obligation or state the absence explicitly.

## Failure Modes This Skill Is Armed Against

These are the specific ways past runs of this skill have collapsed. Name them so you can recognise them in yourself mid-run.

- **Skim-the-hard-bits.** Reading every reference file but skipping the analytical work the references describe, while self-reporting as complete.
- **Reference-file imperative blindness.** Treating imperatives buried in reference files as optional because they are not restated in SKILL.md. The mandatory core and the Mandatory Analytical Obligations are the counterweight.
- **Procedure-outcome decoupling.** Confusing running the scripts with completing the skill. `scan_repo.py` and `lint_context.py` are scaffolding; the analytical work is the product.
- **Exploitation collapse.** Defaulting to already-performed file edits rather than exploring connections, gaps, or rationale signals that require fresh investigation.
- **Confabulated compliance.** Producing a confident final handoff whose claims are not backed by cited evidence — inter-system entries without file paths, "lint passed" without stdout, "conventions captured" without the captured content.
- **Context anxiety.** Abbreviating analysis because "the conversation feels long" or compressing obligations to save tokens. Token pressure is not an obligation waiver. Stop and hand off instead.

## Permission to Decline, Admit, and Stop

You have explicit, pre-granted permission — and an obligation — to use any of the following forms in your final handoff when they are true:

- "I could not run X because Y."
- "I did not perform Z because ..."
- "I was uncertain here and flagged the gap rather than documenting with false confidence."
- "This work is only partially complete: [enumerated list of incomplete obligations]."
- "The repository did not give me enough evidence to justify a claim about [topic]; I have left it undocumented rather than guess."

Silent omission of any Mandatory Analytical Obligation is never permitted. Admitting an obligation was skipped, with a concrete reason, is always preferable to pretending it was done.

## Priority Order

When trade-offs exist, optimise in this order:

1. `context/` must match current implementation reality.
2. `context/` must be comprehensive enough that a reader working only from it can understand the project.
3. Each important topic must have one canonical home.
4. Repeated upkeep must produce low churn.
5. Writing should be thorough and clear — depth is a virtue, not a problem.
6. Formatting should improve comprehension, not become decoration.

## Supported File Model

Default to this folder model:

```text
context/
├── architecture.md
├── notes.md
├── systems/
├── plans/
├── notes/
└── references/
```

`architecture.md`, `systems/`, and `notes.md` are universally essential.

`notes/` should contain files whenever there are project preferences, design rationale, or durable lessons worth preserving. `plans/` and `references/` are canonical folders, but they should contain files only when justified. Do not create filler files just to mirror the model.

`references/` is not a museum. Research and supporting papers there may need upkeep when implementation reality changes. Update, merge, split, condense, or prune reference material only when that materially improves accuracy, canonical ownership, or long-term usability. Do not apply aggressive pruning pressure by default.

Some `references/` artefacts may follow a richer research-paper structure, including topic folders and analysis-heavy papers. Preserve that stronger structure when it still matches the topic and remains maintainable.

`notes.md` may also serve as a lightweight indicator of active work areas — a brief mention of which systems are currently under active development helps the agent prioritise which system files to read first. This is optional and should only be maintained when the project is large enough that prioritisation matters.

Do not create default files such as:

- `history.md`
- `changes.md`
- `milestone-1.md`
- `open-questions.md`
- `misc.md`

Durable historical knowledge belongs in the owning system document, a topical note file, or a reference file — not in a rolling log.

## Naming Rules

Prefer lowercase hyphenated filenames because they scan better in IDEs and keep the meaningful topic visible early.

Use:

- `architecture.md`
- `systems/analytics.md`
- `systems/debug-overlays.md`
- `systems/agent-observations.md`
- `plans/auth-migration.md`
- `notes/caching-strategy.md`
- `references/rest-vs-graphql.md`

Avoid:

- all-caps filenames such as `ARCHITECTURE.md`,
- vague filenames,
- milestone or chronology words,
- names that exist only to mirror a temporary project phase.

Prefer the shortest stable topic name that is still unambiguous in its folder and in the repository.

## Living System

`context/` is not a one-shot output. It is an evergrowing, maintained memory layer.

The coordinating personality maintains `context/` incrementally during normal sessions — creating files when new systems are added, updating owning documents when behaviour changes, and making targeted edits without invoking this skill. This skill is invoked for large passes when accumulated drift is too broad for inline edits to handle reliably.

Drift is a bounded equilibrium under regular upkeep, not an accelerating catastrophe. Expect steady small corrections between large passes; do not treat ordinary drift as a structural emergency or a licence to rewrite healthy files.

## Operating Modes

Choose the mode that matches the user's intent and the repository state:

- `Initialise`: create an initial `context/` for a repo that does not yet have one.
- `Upkeep`: refresh an existing coherent `context/` in place with minimal churn.
- `Repair`: correct stale, inconsistent, or structurally drifting files without broad reorganisation.
- `Restructure`: merge, split, rename, or delete files when the current layout is actively misleading or duplicative.
- `Audit-only`: diagnose the state of `context/` and recommend actions without rewriting files.
- `Plan-support`: create or maintain a temporary `plans/` file only when explicitly requested or clearly necessary for active execution.

Do not choose a mode based on repository size labels such as "small" or "large." Choose it based on evidence about structure quality, overlap pressure, missing canonical homes, and user intent.

### Choosing Your Mode (Decision Guide)

Walk this question tree and state the answers briefly in your output before committing to a mode. Default to `Upkeep` if no answer strongly favours another mode.

1. **Does `context/` already exist in the repository?** If no → `Initialise`. If yes → continue.
2. **Did the user request a diagnosis without edits (audit, review, assessment, dry run)?** If yes → `Audit-only`. If no → continue.
3. **Is the current structure clearly wrong in a widespread way — multiple duplicated canonical homes, pervasive milestone slicing, or a layout that actively misleads?** If yes → `Restructure`. If the problem is isolated (a few stale files, a single misnamed document, a small inconsistency) → `Repair`.
4. **Did the user explicitly ask for plan support, or is there active multi-step work that clearly needs a `plans/` file?** If yes → `Plan-support` (usually layered on top of `Upkeep`). If no → continue.
5. **None of the above triggered?** → `Upkeep`.

If the signals conflict, state the conflict and pick the narrower mode. Escalating from `Upkeep` to `Restructure` mid-run is cheaper than reversing an unnecessary restructure.

## Evidence Standard

Use the repository as primary evidence for implementation truth. Existing `context/` files are prior memory, not unquestionable truth.

Inspect enough of the repository to justify each major claim about:

- top-level structure,
- major subsystem boundaries,
- dependency direction,
- key execution or data flows,
- what appears implemented, partial, missing, or obsolete.

When a statement is inferred rather than directly observed in code or configuration, write it as an inference rather than as a verified fact.

## Script Usage

This skill is a script-backed workflow. The bundled scripts are mandatory parts of the process, not optional conveniences.

- Run `scripts/scan_repo.py` near the start of every non-auditless run to inventory repository structure, existing `context/` files, and likely subsystem roots.
- Run `scripts/lint_context.py` before presenting a completed `context/` update.
- Use the scripts as deterministic scaffolding, not as semantic decision-makers.
- If a script genuinely cannot run, follow the fallback rules in `references/script-contract.md` and say so explicitly in the final handoff, quoting the specific environment error (missing interpreter, permissions, import failure) that prevented execution.

### Tool-Trace Obligation

When reporting that a script ran, include in the final handoff:

- the **exact command** invoked (e.g. `python scripts/scan_repo.py` or the full path used),
- the **first three and last three lines of stdout** so the run is verifiable from the transcript,
- for `lint_context.py`, **every warning** it emitted with a per-warning disposition (fixed, justified, deferred) and the specific reason.

Reporting a run without this evidence is not permitted — treat the run as not performed and re-run it. The scripts are cheap; confabulating their output is expensive.

## Execution Workflow

When this skill is triggered, follow this sequence:

1. Determine the operating mode from user intent and repository state using the decision guide above.
2. Run `scripts/scan_repo.py` and inspect key entrypoints plus any existing `context/` files.
3. Map stable subsystem and feature boundaries from repository evidence.
3a. **Pre-commit to the Mandatory Analytical Obligations.** Before beginning content work in step 4, produce a visible skeleton in your output enumerating, for this specific repository:
    1. the candidate inter-system relationships you will investigate (system A × system B pairs),
    2. which critical operation's dependency chain you will trace end-to-end,
    3. the inspection-scope tracking you will maintain for knowledge gaps (inspected / noted-but-not-read / inferred-from-structure),
    4. the planned rationale-capture pass (what grep patterns, what candidate files),
    5. the planned convention-capture pass (what source areas, what pattern categories),
    6. the connection-discovery probes from `references/cross-system-analysis.md` §Connection Discovery Methodology you will run.
    This skeleton is your pre-commitment. Later steps fill it in. Do not proceed to step 4 without this skeleton visible in the transcript. If the repository is genuinely trivial and a row cannot apply, state that row's obligation name and the reason; do not silently omit it.
4. Identify cross-system relationships, integration points, and documentation gaps per the Mandatory Analytical Obligations section below. Look for systems that share data structures or config without documenting the connection, significant source directories with no system file, and dependency hotspots where many systems converge.
5. Decide whether the current `context/` should be preserved, updated, repaired, or restructured.
6. Update or create `architecture.md`.
7. Update, create, merge, split, rename, or delete files in `systems/` as justified.
8. Update or create `notes.md` and `notes/` files — capture any design rationale, project preferences, conventions, or trial-and-error outcomes that surfaced since the last upkeep. Audit existing notes for staleness.
9. Check all active `plans/` files — tick completed checkboxes, update status, remove plans whose completion criteria are fully met. Plan files produced by analysis workflows (code health audits, refactoring sweeps) follow the same lifecycle.
10. Check `references/` for staleness — if the repository now implements something a reference says is missing, or if a comparison reflects outdated constraints, refresh or prune the reference.
11. Create or update other files in `plans/` or `references/` only when justified by their role.
12. Run `scripts/lint_context.py`.
13. Fix any hard failures. For each warning, state explicitly in the handoff: (a) the warning text, (b) whether it is fixed, justified, or deferred, (c) the specific reason. Coverage-gap warnings must be matched against the Knowledge Gap obligation. Cross-reference warnings must be reconciled against the Inter-system Relationship Mapping obligation. Shallow-document warnings must be reconciled against `references/content-depth-standards.md`. Do not leave warnings with "judgment" as the explanation.
14. Present the resulting tree, major decisions, and any remaining risks or caveats. Include the **What I Did Not Do** declaration from the Quality Checklist — every Obligation-half item that was skipped or partially completed, with reason. If nothing was skipped, state "All obligations completed."

## Mandatory Analytical Obligations

The following investigative obligations apply to every `Initialise`, `Upkeep`, `Repair`, `Restructure`, or `Audit-only` run unless the repository is trivially small (single file or fewer than roughly five source files). They are not conditional on the agent judging them "needed" — the agent's own judgement that an obligation is not needed is itself evidence that it IS needed, because that judgement is exactly the shape the tool-bias failure mode takes.

1. **Inter-system relationship mapping.** Identify at least `N` relationships where `N = min(systems, systems-choose-2)`. Each entry must cite the two systems involved, the mechanism (call, event, shared state, config, file), and what breaks if the connection fails. Evidence: the entries written into `architecture.md` or the relevant `systems/*.md` files, cited in the handoff by file path and section.
2. **Dependency chain trace for at least one critical operation.** Pick one operation that crosses system boundaries and trace it end-to-end: entry point, systems touched in order, boundary data shapes, failure behaviour at each step. Evidence: the traced chain written into `architecture.md` or the owning system file.
3. **Knowledge gap enumeration.** State explicitly which parts of the repository were actually inspected, which were noted-but-not-read, and which were described purely from file-structure inference. Evidence: a Coverage subsection in `architecture.md` or an equivalent note in `notes.md`.
4. **Rationale capture from code.** Grep or search for `WHY`, `NOTE`, `HACK`, `IMPORTANT`, `TODO` annotation patterns and plain comments explaining design decisions. Surface durable cross-session rationale into the owning system file — or state explicitly that no such comments were found after inspection, citing where you searched.
5. **Convention capture.** Scan representative source files for patterns that appear in three or more locations and are not tooling-enforced (linter rules, formatter config). Capture them into `notes/` with a named topic — or state explicitly that no unmarked conventions were found, citing what you scanned.
6. **Connection discovery pass.** Execute the active investigation described in `references/cross-system-analysis.md` §Connection Discovery Methodology: shared data structures, shared config, parallel evolution, hidden coupling through global state, event producers and consumers, common external dependencies. Each probe must produce an outcome statement — "found and documented here," "looked and found none," or "not applicable because ..." — in the handoff.

If the repository is genuinely trivial and an obligation cannot meaningfully apply, name the obligation and state the reason. Silent omission is not permitted. A one-line acknowledgement that an obligation was considered and is inapplicable satisfies the obligation; pretending it was done, or not mentioning it, does not.

## Architecture and System Separation

`architecture.md` is the top-down structural map. It should describe the repository shape, subsystem responsibilities, dependency direction, and major execution/data flows.

`systems/*.md` files are the canonical homes for feature- or subsystem-level reality. They should capture implemented behaviour, boundaries, interfaces, active risks, partial work, likely change pressure, and durable lessons for one stable topic.

Do not let `architecture.md` duplicate all system docs. It is the map, not the territory.

`references/` files are durable supporting memory, including project-grounded research. They may discuss external findings, comparisons, or implementation lessons, but they still need upkeep when the repository changes enough to make their project-specific claims stale.

When a reference artefact clearly follows a research-paper structure with analytical sections and topic folders, upkeep should preserve its research-specific sections and analytical structure unless there is a clear reason to simplify or consolidate it.

## Composition

Output is rich, expressive, and depth-friendly — tables for dense inventories and comparisons, trees for repository structure, ASCII diagrams for flows and relationships, ASCII visualisations when information has spatial or density structure, bullets for digestible takeaways, and combined formats when one representation helps scanning and another helps reasoning. The full expressive range of markdown and ASCII is available; reach for whatever conveys the information clearest. See `references/markdown-presentation-patterns.md` for the specific patterns this skill uses for dense visual content.

Supportive duplication inside the same document is allowed when it improves comprehension — a table followed by bullets that interpret it, a diagram followed by prose that explains the failure modes. Canonical duplication across documents is not allowed: if two files both fully own the same topic, pick one canonical home and reduce the other to interface-level mention.

## Optional Runtime Enforcement

These hooks are not required, but they raise the floor when a user configures them. They are listed here so the agent knows they may exist and behaves as if the enforcement might fire.

- **Prompt-type Stop hook.** A Stop hook configured in `settings.json` can grep the agent transcript for the expected Obligation headings ("Inter-system relationship mapping", "Dependency chain trace", "Knowledge gap", "Rationale capture", "Convention capture", "Connection discovery pass") and for evidence tokens (file paths, lint stdout excerpts, grep outputs). Absence of any heading or token fails the hook and requires the agent to complete the gap before handoff.
- **Agent-type Stop hook.** A hook that re-runs `scripts/lint_context.py` after the agent declares completion, then surfaces any warnings the agent did not acknowledge. This catches confabulated "lint passed" claims.

Neither hook is part of the skill contract — assume they may or may not be configured. Write the handoff as if they are configured: explicit headings, cited evidence, no silent omission.

## Quality Checklist

The checklist has two halves. The first is **Obligations** — binary items that require cited artefact evidence and must all be satisfied (or explicitly declined with reason) before handoff. The second is the **Quality Rubric** — subjective items that apply only after the obligations are satisfied. Treat the Quality Rubric as second-tier: a beautifully-formatted `context/` that skips the obligations is a failure.

### Obligations (evidence required)

Each item below must either be satisfied with the cited artefact, or appear in the **What I Did Not Do** section with a reason.

- `scripts/scan_repo.py` was run. Cite the exact command and the first and last three lines of stdout.
- `scripts/lint_context.py` was run. Cite the exact command, first and last three lines of stdout, and every warning with its per-warning disposition (fixed / justified / deferred) and reason.
- The **pre-commitment skeleton** (Execution Workflow step 3a) is present in the transcript.
- **Inter-system relationship mapping** produced at least `min(systems, systems-choose-2)` entries. Cite at least one entry by file path and section.
- **Dependency chain trace** for one critical operation is present. Cite the file path and section where the chain is documented.
- **Knowledge gap enumeration** is present as a Coverage subsection. Cite the file path.
- **Rationale capture pass** ran. Cite the grep patterns used and either the surfaced rationale entries or an explicit "no such comments found after inspecting [areas]".
- **Convention capture pass** ran. Cite either the captured conventions (with file path) or an explicit "no unmarked conventions found in [areas]".
- **Connection discovery pass** ran. Each of the six probes from `references/cross-system-analysis.md` §Connection Discovery Methodology has a stated outcome.

### Quality Rubric (subjective)

Apply only after obligations are satisfied:

- `architecture.md` exists and is structurally deep enough to orient a new reader,
- every important subsystem or feature has one canonical home,
- folder roles are respected: systems for implementation truth, notes for evolving project knowledge, plans for active execution, references for supporting material,
- naming is lowercase and stable rather than chronological or vague,
- the repo scan was run unless a documented fallback was genuinely necessary,
- the context lint was run unless a documented fallback was genuinely necessary,
- architecture and system docs are comprehensive enough to avoid immediate rediscovery from code,
- supportive formatting improves comprehension without replacing canonical ownership,
- existing good-enough files were preserved rather than rewritten for cosmetic reasons,
- system docs describe current reality rather than aspiration,
- durable lessons are attached to the owning subsystem rather than placed in a history log,
- `notes.md` exists and accurately indexes all files in `notes/`,
- note files are topical and current, not stale or redundant with system files,
- research references that depend on current implementation reality were refreshed when they had gone stale,
- `references/` was kept useful without aggressive or cosmetic pruning,
- active plan files have up-to-date checkbox status reflecting current progress,
- completed plans have been removed,
- material overlap between files is low,
- cross-system relationships are documented where they add value — system files reference the systems they interact with, architecture captures significant integration points,
- supporting infrastructure (testing, build, deployment) is documented when it has real complexity, not left as tribal knowledge,
- recurring conventions and patterns discovered during upkeep are captured in notes when they would help maintain consistency,
- claims in context docs reflect their confidence level through word choice — verified facts stated directly, inferences framed cautiously.

### What I Did Not Do

This section is required in every final handoff. Enumerate every Obligation-half item that was skipped, deferred, or only partially completed, with a concrete reason for each. If nothing was skipped, state:

> All obligations completed.

Silent omission of this section is treated as a failed run. Admitting that an obligation was skipped with a real reason is always preferable to pretending it was satisfied.
