# Formatting and Notation Standards

How skills should literally be formatted affects agent comprehension. Consistent formatting also makes skills easier to evaluate and maintain.

## SKILL.md Structure

The canonical structure for a SKILL.md file, in order:

```
1. YAML frontmatter (name, description)
2. One-paragraph skill summary
3. Core workflow / operating instructions
4. Reference file loading instructions (mandatory-core, then conditional)
5. Inviolable rules section (hard rules specific to this skill)
6. Quality checklist (recency anchor)
```

The workflow section is the largest. It describes what the agent does when the skill triggers — not step-by-step procedures, but the framework of the task, the quality standards, and the decision points.

## Reference File Structure

```
1. Table of contents (if >100 lines)
2. Brief purpose statement (1-2 sentences: what this file covers and when to read it)
3. Sections and subsections
```

## Section Header Conventions

- Use `##` for major sections in SKILL.md, `###` for subsections.
- Use `##` for major sections in reference files, `###` and `####` for subsections.
- Headers should be descriptive enough that a reader scanning headers alone understands the file's scope.

| Weak | Strong |
|------|--------|
| `## Section 3` | `## Finding Classification Taxonomy` |
| `### Details` | `### Boundary Rules for Overlapping Categories` |
| `## Misc` | `## Edge Cases and Project-Specific Adaptations` |

## Markdown Patterns That Improve Agent Comprehension

Different information types benefit from different representations:

| Information Type | Best Representation | Example Use |
|-----------------|---------------------|-------------|
| Comparisons (good vs. bad, options A/B/C) | Tables | Instruction wording comparisons, scoring rubrics |
| Hierarchies (file trees, category taxonomies) | Indented trees or nested lists | Directory structures, category breakdowns |
| Sequential operations | Numbered lists | Script execution order, file creation order |
| Parallel options | Bullet lists | Alternative approaches, multiple valid strategies |
| Templates and output formats | Fenced code blocks | File templates, output structure |
| Decision logic | Conditional prose or flowcharts | "If X, do Y. If Z, do W." |

**Anti-pattern:** Using bullet lists for everything. Bullet lists are appropriate for parallel items of equal weight. They are inappropriate for comparisons (use tables), hierarchies (use trees), or sequential steps (use numbered lists).

## How to Format Templates Within Reference Files

Templates should be in fenced code blocks with a content-type label. Each template section should have inline comments explaining intent:

```markdown
## Finding Template

### [Finding Title — Specific, Actionable, Domain-Free]

**Category:** [From the taxonomy in analysis-categories.md]
**Severity:** [Critical | High | Medium | Low — based on impact and fix cost]

#### Current State
[What the code does now. Ground every claim in the actual implementation.
Include file paths and function names. An engineer reading this should
understand the issue without opening the code.]

#### Proposed Change
[The specific change. Enough implementation detail that an engineer could
act on it without further research.]

#### Justification
[Why this change matters. Connect the evidence in Current State to the
benefit in Expected Impact. Research-backed where possible.]

#### Expected Impact
[Concrete, measurable where possible. "Reduces allocation in hot path
from O(n) to O(1)" not "improves performance."]
```

## How to Mark Hard Rules vs. Guidelines Visually

Within a skill's instructions, hard rules and guidelines should be visually distinguishable:

- **Hard rules:** Collected in a dedicated "Inviolable Rules" or "Structural Constraints" section. Each rule is a single declarative sentence with its justification.
- **Guidelines:** Woven into the workflow sections as principled instructions with reasoning. They do not need special visual marking — the presence of reasoning and the absence of imperative framing signals that they are guidelines.

Do not use emoji, colour, or other non-semantic markers. Structural separation (dedicated section) and wording tier (constraint vs. guideline vs. principle) are sufficient.
