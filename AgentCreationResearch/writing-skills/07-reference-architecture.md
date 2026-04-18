# Reference File Architecture

## When to Split vs. Keep Inline

| Keep in SKILL.md | Split to reference files |
|-------------------|------------------------|
| Core workflow instructions | Detailed templates |
| Quick-start information | Domain-specific standards |
| Navigation to reference files | Extensive examples and worked scenarios |
| Inviolable rules section | Category taxonomies |
| Quality checklist | Format specifications |

**Hard rule:** SKILL.md body under 500 lines. This is a structural constraint, not a content constraint — the comprehensiveness lives in the reference files.

## Critical Rule: One Level Deep

Reference files must not point to other reference files. SKILL.md points to reference files. Reference files are terminal. When references nest, agents partially read files (using `head -100` or similar), resulting in incomplete information. A two-level chain means the agent may never reach the terminal content.

## Table of Contents in Long References

For reference files longer than 100 lines, include a table of contents at the top. This ensures the agent can see the full scope of available information even when previewing with partial reads. The table of contents should list every major section with a brief (3-8 word) description.

## Naming

Name files descriptively. The agent navigates the skill directory like a filesystem — clear names help it find what it needs without reading the file.

| Weak | Strong |
|------|--------|
| ref2.md | analysis-categories.md |
| doc.md | output-format.md |
| templates.md | finding-template.md |
| misc.md | edge-cases-and-boundaries.md |

## File Granularity

Each reference file should cover one coherent topic. If a file covers two unrelated topics, split it — the agent may load it for one topic and get distracted by the other. If two files cover overlapping topics, merge them — the agent may load only one and miss information from the other.

**Evaluation test:** For each reference file, state its topic in one sentence. If the sentence requires "and" to connect two unrelated topics, the file should be split. If two files have sentences that overlap significantly, they should be merged.

## Imperatives Belong in SKILL.md, Not References (2026-04-18 addition)

Research finding from AgentIF: tool-constraints collapse to **43% satisfaction rate** vs 80% for vanilla constraints. The category of instruction most frequently skipped is "you must call tool X" when placed in reference material.

**Rule:** Any obligation that requires calling a tool the agent might not otherwise call (WebSearch, writing files, running specific commands) MUST appear in SKILL.md body, not only in reference files.

This is a stronger form of the lost-in-the-middle finding. Reference files are read as informational context — imperatives buried in them tend to be filed mentally as "awareness" rather than "action." SKILL.md is the imperative layer; references are the supporting detail.

See [19-verification-gates.md](19-verification-gates.md) for the enforcement side of this rule.
