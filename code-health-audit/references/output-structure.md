# Output Structure

This reference defines how to organise the audit output folder, name files, and structure the index.

## Table of Contents

1. Folder Location and Naming
2. Index File
3. Finding Files
4. File Naming Conventions
5. Lifecycle
6. Relationship to Context
7. What I Did Not Do Section

## 1. Folder Location and Naming

The audit output is a folder inside `context/plans/`:

```
context/plans/code-health-audit/
├── index.md
├── training-pipeline.md
├── environment.md
├── data-pipeline.md
├── cross-cutting.md
└── ...
```

The folder name should be `code-health-audit` for standard audits. If the project runs multiple audits over time (unlikely but possible), append a short descriptor: `code-health-audit-pre-v2` or similar.

## 2. Index File

The `index.md` file is the entry point. It must provide:

### Header

```markdown
# Code Health Audit

**Date:** YYYY-MM-DD
**Scope:** full repository / specific systems (list them)
**Status:** active / in-progress / complete

## Summary

[2-5 sentences summarising the overall findings: how many findings, which systems had the most, what the biggest opportunities are, any critical issues found.]
```

### Finding Overview Table

A table summarising all findings across all files:

```markdown
## Findings Overview

| File | System | Critical | High | Medium | Low | Total |
|------|--------|----------|------|--------|-----|-------|
| [training-pipeline.md](training-pipeline.md) | Training | 0 | 3 | 5 | 2 | 10 |
| [environment.md](environment.md) | Environment | 0 | 1 | 3 | 4 | 8 |
| [cross-cutting.md](cross-cutting.md) | Project-wide | 0 | 2 | 1 | 0 | 3 |
| **Total** | | **0** | **6** | **9** | **6** | **21** |
```

### Priority Highlights

After the overview table, list the top 5-10 highest-priority findings with direct links:

```markdown
## Priority Actions

1. **[HIGH]** Replace linear scan with spatial index in proximity calculations — [training-pipeline.md#proximity-search](training-pipeline.md#proximity-search)
2. **[HIGH]** Remove 400-line dead ReLU activation module — [training-pipeline.md#dead-relu](training-pipeline.md#dead-relu)
3. **[HIGH]** Pre-allocate observation buffer in hot loop — [environment.md#observation-buffer](environment.md#observation-buffer)
...
```

### Category Breakdown

A brief summary of how many findings fall into each analysis category:

```markdown
## By Category

- Dead Code Removal: 4 findings
- Algorithm Optimisation: 3 findings
- Performance Improvement: 5 findings
- Modularisation: 3 findings
- Inconsistent Patterns: 2 findings
- ...
```

## 3. Finding Files

Each finding file covers one system or one cross-cutting concern. Within each file:

### File Header

```markdown
# [System Name] — Code Health Findings

**Systems covered:** [list of subsystems or areas covered]
**Finding count:** X findings (Y high, Z medium, W low)
```

### Findings

Findings are organised by category within the file, with each finding following the template defined in the finding-format reference.

Use heading levels consistently:

- `##` for category headings (e.g., `## Dead Code Removal`)
- `###` for individual findings (e.g., `### Unused ReLU Activation Module`)

### Checkboxes

Every actionable finding must have a top-level checkbox:

```markdown
### Unused ReLU Activation Module
- [ ] Remove `src/brain/activations/relu.rs` and its test file

**Current state:** ...
**Proposed change:** ...
...
```

This enables the context upkeep workflow to track progress by ticking checkboxes as findings are implemented.

## 4. File Naming Conventions

- Use lowercase hyphenated names.
- Name by system or concern, not by category or date.
- Keep names short and descriptive.

Good:
- `training-pipeline.md`
- `environment.md`
- `data-processing.md`
- `cross-cutting.md`

Bad:
- `dead-code-findings.md` (category-based — use system-based)
- `audit-part-1.md` (sequential numbering — not navigable)
- `march-28-audit.md` (date-based — will be stale)

Exception: if the project has very few subsystems and findings are best grouped by category, category-based naming is acceptable. Use judgment.

## 5. Lifecycle

The audit folder follows the standard plan lifecycle:

1. **Created** by this skill with status "active."
2. **Maintained** during implementation — checkboxes are ticked, notes are added, findings are marked as deferred or rejected.
3. **Removed** when all actionable findings are either complete or consciously deferred.

The context upkeep workflow treats this folder like any other plan — it updates checkbox status during upkeep passes and removes the folder when the work is done.

If some findings are deferred indefinitely, they should either be:
- moved into the relevant system's "Known Issues / Active Risks" section in `context/systems/`, or
- consciously accepted as "not worth fixing" and documented as such before the folder is removed.

Do not leave a half-finished audit folder in `context/plans/` indefinitely.

## 6. Relationship to Context

The audit output should reference context files where relevant:

- When a finding affects a system documented in `context/systems/`, reference the system file.
- When a finding contradicts a project note, flag the conflict explicitly.
- When a finding builds on existing research in `context/references/`, reference the research.
- When a finding reveals something that should be captured as a new note, recommend creating the note.

The audit is a consumer of context, not a producer of it (except for its plan files). It does not update system files, architecture, or notes — it only reads them and produces plan files. Updates to context happen through the normal upkeep workflow as findings are implemented.

## 7. What I Did Not Do Section

Before presenting the audit, the `index.md` file must include a "What I Did Not Do" section that enumerates every non-negotiable obligation from the skill and reports its status. Silent omission is not permitted — an obligation either has evidence, a reasoned deferral, or an acknowledged skip.

Structure:

```markdown
## What I Did Not Do

For each obligation, status is `done` (with evidence), `partial` (with reason and partial evidence), or `skipped` (with reason).

- **Pre-Pass-1 front-loaded WebSearch:** done — query "[text]"; source [URL]; recorded in obligation-evidence-map.md.
- **Pass-1 checkpoint file written:** done — `context/plans/code-health-audit/PASS-1-CHECKPOINT.md`.
- **Pass-2 systems-audited file written:** done — `context/plans/code-health-audit/PASS-2-SYSTEMS-AUDITED.md`.
- **Obligation Evidence Map populated for every substantive system:** done — N rows for N substantive systems.
- **WebSearch call per substantive system:** partial — 6 of 7 substantive systems; the seventh (`src/util/format_seconds.rs`) is a single-line glue module and is recorded as a reasoned omission per §"When Research Is Not Required".
- **Research mode variety across queries:** done — modes 1, 2, and 3 all represented; distribution recorded in the map.
- **Diagnostic tests written where they would resolve moderate-to-high confidence:** done — M tests written, all referenced from the findings they support.
- **Data Layout and Memory Access Patterns analysis applied to every audited system:** done — per-system applicability decisions recorded.
- **Project test suite baseline captured:** done — command: `cargo test`; result: 312 pass, 2 failing (recorded as Known Issues findings).
```

This section is an index-level obligation ledger, not a retrospective. Populate it from the Obligation Evidence Map — they must agree. Mismatch between the two is itself a finding-integrity failure and must be resolved before the audit is presented.

Mirror: the Obligation Evidence Map (see `obligation-evidence-map.md`) is the per-system detail; the "What I Did Not Do" section is the project-level summary. Both are required.
