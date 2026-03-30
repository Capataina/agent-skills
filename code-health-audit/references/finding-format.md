# Finding Format

This reference defines the template for individual findings — required fields, depth expectations, and writing standards.

## Table of Contents

1. Finding Template
2. Required Fields
3. Writing Standards
4. Depth Expectations
5. Cross-References

## 1. Finding Template

Every finding must follow this structure:

```markdown
### [Descriptive Title]
- [ ] [One-line actionable summary]

**Category:** [category name from taxonomy]
**Severity:** [critical / high / medium / low]
**Effort:** [trivial / small / medium / large]
**Behavioural Impact:** [none / negligible (flagged) / possible (requires decision)]

**Location:**
- `path/to/file.rs:120-145` — `function_name()`
- `path/to/other_file.rs:30-42` — `related_function()`

**Current State:**
[What the code does now. Grounded in the actual implementation. Include enough detail that an engineer can understand the issue without reading the code first.]

**Proposed Change:**
[What should change. Specific enough to guide implementation. Include what stays the same.]

**Justification:**
[Why this is an improvement. Evidence, analysis, or research that supports the recommendation.]

**Expected Benefit:**
[Concrete improvement — performance gain, reduced complexity, fewer lines, clearer architecture. Be specific rather than vague.]

**Impact Assessment:**
[Why this change does not affect observable behaviour. Or, if it might, what the potential impact is and why it requires a decision.]
```

## 2. Required Fields

Every field in the template is required. Here is what each must contain:

### Title

A short, descriptive name for the finding. Should make sense in the index without further context.

Good:
- "Replace linear scan with KD-tree in proximity search"
- "Remove unused ReLU activation module"
- "Extract raycast angle computation to formula"

Bad:
- "Performance issue"
- "Dead code"
- "Refactor"

### Checkbox Line

One line summarising the actionable work. This is what gets ticked when the finding is implemented.

Good:
- "Replace `select_nearest()` linear scan with a KD-tree for O(log n) queries"
- "Delete `src/brain/activations/relu.rs` and remove it from `mod.rs`"

Bad:
- "Fix the performance"
- "Clean up"

### Category

Must match exactly one category from the analysis categories taxonomy.

### Severity and Effort

Must use the levels defined in the severity-and-prioritisation reference.

### Behavioural Impact

Must be one of:
- **None:** the change cannot affect behaviour by construction or verified analysis.
- **Negligible (flagged):** the change may have a trivial, practically insignificant effect. The assessment must explain what the effect is.
- **Possible (requires decision):** the change may affect behaviour in ways that require human judgment. The assessment must explain the potential impact.

### Location

Exact file paths and line numbers (or function/method names). Must be specific enough that an engineer can navigate directly to the relevant code.

Multiple locations are allowed when a finding spans several files.

### Current State

What the code does now. This must be:
- grounded in the actual code (not inferred),
- detailed enough to understand the issue,
- written in plain language (not pseudocode).

Include:
- what the code does,
- how it fits into the larger system,
- any relevant context (data sizes, call frequency, etc.).

### Proposed Change

What should change and how. This must be:
- specific enough to guide implementation,
- clear about what stays the same,
- not so prescriptive that it becomes pseudocode (the implementing engineer has discretion over exact implementation).

### Justification

Why the change is an improvement. This must include:
- the type of evidence (direct, analytical, research-backed, inference),
- the specific reasoning,
- references to any external research or documentation that supports the recommendation.

### Expected Benefit

The concrete improvement. Be specific:

Good:
- "Reduces time complexity from O(n^2) to O(n log n) for ~10,000 items."
- "Removes 400 lines of dead code, eliminating a misleading module from the codebase."
- "Replaces 32 hardcoded values with a formula, making the pattern explicit and the raycast count configurable."

Bad:
- "Improves performance."
- "Cleaner code."
- "Better architecture."

### Impact Assessment

Why the change does not affect behaviour, or what the potential impact is. This must be:
- specific to this finding (not a generic statement),
- grounded in analysis of the actual code,
- explicit about edge cases or uncertainties.

## 3. Writing Standards

### Voice

Write findings in a direct, analytical voice. State facts and reasoning, not opinions.

Good: "The `sort_experiences` function sorts all 50,000 buffer entries to select the top 64. A partial sort achieves the same result in O(n + k log k) instead of O(n log n)."

Bad: "I think we could probably improve the sorting here."

### Precision

Use precise language. Avoid hedging when the evidence is clear. Hedge explicitly when the evidence is uncertain.

Good: "This function has zero callers in the codebase."
Good: "This function appears to have no callers, but it is marked `pub` and may be used by external consumers or plugins."

Bad: "This function might be dead code."

### Conciseness

Be thorough but not verbose. Every sentence should add information. Do not pad findings with filler or repeat the same point in different words.

### Technical Accuracy

Use correct terminology for the language and domain. If the project uses specific terms for its systems (as documented in context/), use those terms consistently.

## 4. Depth Expectations

The depth of each field should be proportionate to the finding's severity and complexity:

### High-Severity or Complex Findings

- Current State: full paragraph explaining the implementation, data flow, and why it matters.
- Proposed Change: detailed description with clear guidance on implementation approach.
- Justification: thorough analysis with evidence, possibly including complexity analysis or research citations.
- Expected Benefit: quantified where possible (time complexity, line count, allocation count).
- Impact Assessment: detailed analysis of why the change is safe, including edge cases considered.

### Medium-Severity Findings

- Current State: clear description of the issue.
- Proposed Change: specific guidance on what to change.
- Justification: concise but complete reasoning.
- Expected Benefit: described but may not be precisely quantified.
- Impact Assessment: brief but explicit.

### Low-Severity Findings

- All fields present but can be brief.
- A low-severity finding like "unused import in `src/utils.rs:3`" does not need a paragraph for each field.

## 5. Cross-References

When a finding relates to other findings, cross-reference them:

- "See also: [Pattern Extraction #3](training-pipeline.md#raycast-angles) — the same file has hardcoded values that follow a computable pattern."
- "Related: this dead code may have been part of the system described in [Known Issues #1](cross-cutting.md#legacy-activation-functions)."

Cross-references help the implementing engineer understand the full picture and may suggest that related findings should be addressed together.
