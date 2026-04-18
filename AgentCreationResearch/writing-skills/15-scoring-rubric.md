# Scoring Rubric

This rubric provides a structured evaluation framework for any agent skill. Each dimension is scored on a three-point scale with concrete, observable criteria. A skill does not need to be "Strong" on every dimension — but weaknesses should be intentional and justified, not accidental.

## How to Use the Rubric

Score each dimension independently. Record the score and one sentence of evidence (what you observed that led to the score). After scoring all dimensions, identify the lowest-scoring dimensions — these are the highest-leverage improvement targets.

## The Rubric

### 1. Trigger Accuracy

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Description is vague or generic. Fewer than 3 unique trigger terms. No negative triggers. Would fail to activate for common phrasings of the skill's use case, or would false-activate for adjacent skills. |
| **Adequate (2)** | Description covers the main use case with 3-5 trigger terms. Some negative triggers present. Would activate for standard phrasings but miss edge cases or unusual vocabulary. |
| **Strong (3)** | Description is dense with trigger terms (6+), includes negative triggers for all adjacent skills, covers both formal and informal phrasings. Would activate correctly for any reasonable user request, including edge cases. Assertive activation cue present. |

### 2. Instruction Clarity

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Instructions are ambiguous, contradictory, or assume domain knowledge. Missing *why* explanations. Heavy use of CAPS/bold for non-critical items. Scenario-list anti-pattern present. |
| **Adequate (2)** | Instructions are clear and mostly consistent. Some *why* explanations present. Emphasis is mostly calibrated. No major contradictions, though minor inconsistencies may exist across files. |
| **Strong (3)** | Every major instruction explains *why*. Emphasis reserved for genuine hard rules. No scenario-list anti-patterns. Instruction tiers (constraint/guideline/principle) are correctly matched to their content. No contradictions within or across files. |

### 3. Example Diversity

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Single domain. Uniform complexity and depth. No rejected examples. Cardinality is anchored (all examples have same number of items). |
| **Adequate (2)** | 2-3 domains represented. Some variation in complexity. May lack rejected examples or vary cardinality. |
| **Strong (3)** | 3+ domains, varied complexity, includes at least one rejected example demonstrating a decision boundary, varied cardinality. Examples are framed as illustrations of principles with annotations pointing to what makes them good. |

### 4. Depth Calibration

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Uniformly shallow across all reference files, or uniformly deep regardless of judgement-involvement. The "agent reading only this file" test fails for most references. |
| **Adequate (2)** | Depth is roughly appropriate for most files. Some files could be deeper (high-judgement topics treated shallowly) or shallower (low-judgement topics over-explained). |
| **Strong (3)** | Depth precisely matches the three calibration factors (judgement involvement, cross-project variation, mistake cost). High-judgement files are comprehensive with extensive examples and boundary guidance. Low-judgement files are concise. |

### 5. Autonomy Balance

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Over-constrained: rigid procedures for open-field decisions, excessive numeric limits, CAPS/bold overuse. Or under-constrained: no guidance, no quality standards, no structural rules. |
| **Adequate (2)** | Reasonable balance. Most structural decisions are fixed, most content decisions are free. Some unnecessary constraints remain. Total instruction count is manageable. |
| **Strong (3)** | Clear framework with explicit freedom grants. Hard rules only where justified with structural reasoning. Principles and quality bars for open-field content. Total instruction count well below saturation (~100). Agent reading the skill would feel empowered, not constrained. |

### 6. Reference Architecture

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Monolithic SKILL.md (over 500 lines) with no reference files. Or many reference files with no loading guidance. Or nested references (references pointing to references). |
| **Adequate (2)** | Reasonable split between SKILL.md and references. Loading instructions present but may not distinguish mandatory-core from conditional. File names are descriptive. |
| **Strong (3)** | Progressive disclosure with mandatory-core and task-based conditional loading clearly distinguished. One level deep. Descriptive file names. Each file covers one coherent topic. Table of contents in long files. SKILL.md under 500 lines. |

### 7. Formatting Quality

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Inconsistent markdown. Bullet lists used for everything. No visual hierarchy. Headers are vague ("Section 3," "Details"). Templates lack intent descriptions. |
| **Adequate (2)** | Consistent markdown. Some appropriate use of tables, trees, and code blocks. Headers are mostly descriptive. Templates have basic intent descriptions. |
| **Strong (3)** | Rich representation throughout — tables for comparisons, trees for hierarchies, code blocks for templates. Clear visual hierarchy. All headers descriptive. Templates have comprehensive intent descriptions. Hard rules visually separated from guidelines. |

### 8. Coherence

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Contradictions between files. Terminology drift (multiple terms for same concept). Philosophical inconsistency (autonomy-granting in one file, prescriptive in another). |
| **Adequate (2)** | Mostly consistent terminology. No major contradictions. Minor inconsistencies in philosophical stance across files. |
| **Strong (3)** | Fully coherent terminology — every concept has exactly one term used consistently across all files. No contradictions. Consistent philosophical stance (same level of autonomy, same approach to depth, same quality expectations) across the entire skill directory. |

### 9. Quality Checklist

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Missing, or present with vague/unverifiable items ("Is it good?"). Duplicates instructions from the body. More than 15 items (diluted attention). |
| **Adequate (2)** | Present with mostly verifiable items. Proportionate count (5-15). Some items could be more concrete. |
| **Strong (3)** | Every item is concrete and verifiable (yes/no answer). Proportionate count. Ordered by importance. Independent items. Does not duplicate the body. Acts as an effective recency anchor for the skill's most critical quality requirements. |

### 10. Cross-Skill Fit

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Overlapping triggers with adjacent skills. References other skills by name. Inconsistent terminology with the ecosystem. Depends on files outside its directory. |
| **Adequate (2)** | Non-overlapping triggers. Self-contained. May have minor terminology inconsistencies with the ecosystem. |
| **Strong (3)** | Clean trigger boundaries with negative triggers for all adjacent skills. Artefact-pattern references only (no skill names). Consistent terminology with the entire ecosystem. Fully self-contained. Philosophical stance aligned with ecosystem norms. |

### 11. Verification Robustness (2026-04-18 addition)

Reliability-critical skills need a completion gate that is not subject to the acting model's own assessment.

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Quality checklist is all subjective rubric items ("is it thorough?"). No evidence slots. Skipped-work declaration not required. Agent's own self-assessment is the only gate. |
| **Adequate (2)** | Checklist has some obligation-items with evidence requirements. Skipped-work declaration is optional or hinted. No structural (hook-based) gate. |
| **Strong (3)** | Checklist is majority obligation-items, each with a required evidence slot (tool name, file path, URL, test ID). Skipped-work declaration is structurally required. Where available, a Stop hook or PreToolUse hook enforces tool-call presence before termination. Cross-family verifier used if any verifier is used. |

### 12. Sycophancy Resistance (2026-04-18 addition)

Measures whether the skill's structure holds against the agent's trained incentive to produce "looks-complete" output.

| Score | Criteria |
|-------|----------|
| **Weak (1)** | Skill uses vague exhortations ("be thorough", "go above and beyond"). Quality checklist items require subjective self-rating. No deontological permissions. No forcing-function language. |
| **Adequate (2)** | Some exhortations but also some obligations. Checklist has a mix of subjective and evidence-anchored items. Some language giving the agent permission to decline / admit skipped work. |
| **Strong (3)** | All obligation-language is verifiable. Agent has explicit deontological permissions ("you may say 'I did not do X'"). Iterative self-refinement patterns are absent. Same-model self-verification is absent. Adversarial critic framing used where verification is needed. |

## Interpreting Scores

- **All 3s:** The skill is exceptionally well-crafted. Maintain it.
- **Mostly 3s with one or two 2s:** Strong skill. The 2s are improvement opportunities but not urgent.
- **Mix of 2s and 3s:** Good skill with clear areas for improvement. Address 2s methodically.
- **Any 1:** The skill has a significant weakness that will degrade agent output. Address 1s before deployment.
- **Multiple 1s:** The skill needs substantial rework. Prioritise by impact: Trigger Accuracy and Instruction Clarity affect everything downstream.
