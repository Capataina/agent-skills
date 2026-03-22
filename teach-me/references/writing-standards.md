# Writing Standards Reference

This file defines the quality bar for all generated content. Every concept file, exercise, materials entry, and curriculum section must meet these standards.

## Language and Tone

- Always use British English (optimisation, behaviour, analyse, colour, modelling, generalise).
- Use a semi-formal professional tone — like university lecture notes or a well-written textbook, not marketing copy.
- Avoid buzzwords, hype, and theatrical language. Let technical substance speak for itself.
- Use everyday professional language when possible. Explain complex ideas simply before introducing jargon.
- Never use phrases like "dive deep", "unleash", "supercharge", "game-changing", or "cutting-edge" unironically.

## Depth Calibration

Every explanation must hit the right depth — neither too shallow nor too deep. Here are calibrated examples:

### Surface-Level (Never Acceptable)

> "We use cosine similarity for image search."

This tells the reader nothing they couldn't get from reading a function name. It provides no understanding of what cosine similarity is, why it was chosen, or how it works.

### Appropriate Depth (Target This)

> "We use cosine similarity to measure image similarity. Cosine similarity computes the angle between two vectors in high-dimensional space, rather than their Euclidean distance. For two vectors A and B, it is calculated as:
>
> cosine_similarity = (A · B) / (‖A‖ × ‖B‖)
>
> where A · B is the dot product and ‖A‖ is the magnitude (the square root of the sum of squared components).
>
> Why cosine instead of Euclidean distance? Because CLIP embeddings encode semantic meaning in the *direction* of the vector, not its magnitude. Two sunset images might have vectors [0.8, 0.2, 0.1, ...] and [1.6, 0.4, 0.2, ...] — different magnitudes but the same direction (both are scaled versions of the same semantic concept). Cosine similarity correctly identifies these as identical (similarity = 1.0), while Euclidean distance would say they are different.
>
> To optimise this calculation, we pre-normalise all vectors to unit length (magnitude = 1). This means cosine_similarity reduces to just the dot product: A · B. This is much faster to compute and the result is identical."

This explains what it is, how it works mathematically, why it was chosen over alternatives, and how the project optimises it. A reader could implement it from this explanation alone.

### Too Deep (Also Avoid)

> "Cosine similarity in Hilbert spaces generalises to infinite-dimensional function spaces where the inner product ⟨f, g⟩ is defined via the Lebesgue integral..."

Unless the project actually operates in infinite-dimensional function spaces, this is irrelevant depth that wastes the reader's time and obscures the practical understanding.

### The Depth Test

For any explanation, ask: "Does this explanation give the reader enough to implement the concept from scratch and explain it in an interview?" If yes, you have the right depth. If they could only use it as a black box, go deeper. If they are drowning in irrelevant theory, pull back.

## Concrete Examples Policy

Every abstract concept must be accompanied by a concrete example with actual numbers, actual code, or actual data. No exceptions.

### Bad (Abstract Only)

> "Policy gradients optimise the policy by following the gradient of expected return."

### Good (Abstract + Concrete)

> "Policy gradients optimise the policy by following the gradient of expected return. Concretely: suppose our agent is in state 'near cliff' and takes action 'move forward', leading to a fall (return = -100). The gradient update computes ∇log(π(a|s)) and scales it by the return. Since the return is -100, the gradient update will *decrease* the probability of 'move forward' in state 'near cliff' by updating the policy network weights in the negative gradient direction. If we had moved backward (return = +10), we would increase that probability instead.
>
> Numerically: if π('forward' | 'near cliff') = 0.6 before the update, and the scaled gradient shifts the logit by -0.3, the new probability might drop to approximately 0.45. Over many episodes, the agent learns to avoid actions that lead to poor returns."

### Example Angles

When generating worked examples for a concept, each example should illuminate a different facet. The standard set of angles is:

1. **Basic mechanics** — Show the core computation with simple, concrete numbers. Walk through every intermediate step.
2. **Parameter variation** — Show what happens when you change a key parameter (learning rate, discount factor, grid resolution). Demonstrate sensitivity and intuition.
3. **Failure mode or edge case** — Show what goes wrong and why. This is where real understanding lives: understanding when something breaks reveals what makes it work.
4. **Comparison to alternative** — Compare this approach to a closely related one (cosine vs Euclidean, A2C vs PPO, hash map vs tree map). Show why one is preferred in this context.
5. **Connection to project code** — Show how this concept manifests in the actual project, referencing specific files or functions.

Not every concept needs all five angles, but every concept needs at least three, and the first three (basic, parameter variation, failure mode) are almost always necessary.

## Mathematical Notation

Use plaintext with Unicode symbols for all mathematical expressions. This renders correctly in GitHub, VS Code, Obsidian, and most markdown viewers without requiring LaTeX compilation.

### Inline Expressions

```
δ_t = r_t + γ · (1 − done_t) · V(s_{t+1}) − V(s_t)
```

```
GAE_t = Σ_{l=0}^{∞} (γλ)^l · δ_{t+l}
```

```
∂L/∂μ = (a − μ) / σ²
```

### Multi-Line Derivations (Use Code Blocks)

```
Step 1: Compute squared deviation
  (x − μ)² / σ² = (1.5 − 1.0)² / 0.5²
                 = (0.5)² / 0.25
                 = 0.25 / 0.25
                 = 1.0
```

### Available Unicode Symbols

Use these freely:
- **Greek letters**: α β γ δ ε η θ λ μ π σ τ φ ω Δ Σ Ω
- **Math operators**: × · ≈ ≠ ≤ ≥ ∈ ∉ ∞ ∂ ∇ √ ± ∝
- **Subscripts**: ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ᵢ ⱼ ₖ ₙ ₜ
- **Superscripts**: ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ
- **Set/logic**: ∀ ∃ ∧ ∨ ¬ → ↔ ∪ ∩ ⊂ ⊃ ∅

### Do NOT Use

- LaTeX delimiters (`$...$` or `$$...$$`)
- Raw LaTeX commands (`\Delta`, `\frac{}{}`, `\sum`)
- Any notation that requires a LaTeX renderer

## Progressive Build-Up

Complex concepts are never presented as a single block. They are decomposed into progressive steps where each step builds on the previous one.

### Structure

```markdown
### Step 1: [Foundational Sub-Concept]
[Explain with examples. The reader should fully understand this before moving on.]

### Step 2: [Intermediate Sub-Concept]
[Build on Step 1. Reference specific ideas from Step 1 explicitly.]

### Step 3: [Advanced Synthesis]
[Combine Steps 1 and 2 into the full concept. Show how the pieces fit together.]
```

### When to Use Progressive Build-Up

Use it whenever the concept requires more than one paragraph to explain properly. The test: if you find yourself writing a sentence that assumes knowledge you have not yet established in the file, stop and add a preceding step.

For example, explaining "advantage estimation" requires first explaining "value functions" and "temporal difference error." These should be Steps 1 and 2, with advantage estimation as Step 3.

## Misconception Standards

Misconceptions are one of the highest-value pedagogical tools because they address the specific failure modes in a reader's mental model. Each misconception entry follows this format:

```markdown
❌ **Misconception**: [The wrong belief, stated clearly and without condescension]
✅ **Reality**: [The correct understanding, with enough explanation to show why the misconception is wrong and what the correct mental model is]
```

### Coverage Requirements (5–8 Per Concept)

Cover all of the following categories that apply:

1. **Beginner misconceptions** (2–3) — The mistakes someone makes on first encounter.
   - Example: "Cosine similarity measures distance" → No, it measures angle (or equivalently, directional similarity).

2. **Persistent misconceptions** (2–3) — Errors that survive initial learning and persist into intermediate understanding.
   - Example: "Normalising returns and normalising advantages are the same thing" → They are not; one operates on cumulative rewards, the other on the advantage function.

3. **Failure mode misconceptions** (1–2) — Beliefs about when/why something breaks.
   - Example: "Policy gradient divergence is caused by a bad learning rate" → It can also be caused by unnormalised returns, which create wildly varying gradient magnitudes.

4. **Comparison misconceptions** (1–2) — Confusions between related concepts.
   - Example: "A2C and A3C are the same algorithm" → A3C uses asynchronous parallel workers; A2C uses synchronous updates, which has different convergence properties.

## Materials Curation Standards

Every resource entry must be actionable, not a vague pointer. The reader should know exactly what to consume, what to skip, what to focus on, and what to do afterwards.

### Resource Entry Format

```markdown
- [ ] **[Resource Title] — [Specific Chapter/Section/Timestamp]**
  - **Consume**: [Exact pages, sections, or timestamp ranges]
  - **Skip**: [Sections that are not relevant or are covered elsewhere]
  - **Focus on**: [Key theorem, derivation, concept, or insight]
  - **Exercise**: [What to do after consuming: reproduce pseudocode, work a problem, etc.]
  - **Why**: [1 sentence explaining what unique value this resource provides]
  - **Time**: [X hours/minutes] | **Difficulty**: [Beginner / Intermediate / Advanced]
  - **Link**: [URL if publicly accessible]
```

### Resource Type Distribution (8–12 Per Concept)

- **Textbooks** (2–3): Canonical references with specific chapter/page guidance. Always specify which edition.
- **Videos** (2–3): Lectures or explainers with specific timestamp ranges. Include what topic each timestamp covers.
- **Blog posts / articles** (2–3): Accessible, modern treatments. Prefer original technical blog posts over aggregator summaries.
- **Papers** (1–2): Original or seminal papers, but only for concepts where reading the paper adds genuine value (not all concepts need papers). Specify which sections to read and which to skip.
- **Interactive / code** (1–2): Reference implementations, Jupyter notebooks, or interactive tools. Specify what to run and what to compare against.

### Quality Criteria

- Resources must be publicly accessible (no paywalls for core materials; textbooks can be paywalled but should have free alternatives noted).
- Specific sections, not "read this book."
- Realistic time estimates (a 20-page chapter takes 1–2 hours, not 30 minutes).
- Each resource provides unique value — do not list three resources that all cover the same ground at the same depth.

## Glossary Standards

### Per-File Glossary (15–20 Terms)

Every concept file includes a glossary section at the bottom defining every technical term used in that file. "Technical term" includes anything a second-year undergraduate might not immediately recognise. When in doubt, define it.

Each glossary entry:
- Provides a clear, self-contained definition (1–3 sentences)
- Includes a concrete example or illustrative snippet
- References the global `GLOSSARY.md` for comprehensive treatment if applicable

### Global GLOSSARY.md

Alphabetically ordered. Every term defined in any per-file glossary also appears here with a more comprehensive definition and a reference to where it is used. The global glossary is the single authoritative definition source.

Format:
```markdown
### [Term]
[2–4 sentence definition with concrete example]

Used in: `concepts/core/file.md`, `concepts/domain_patterns/file.md`
```

## Abundance Enforcement

These numeric targets exist because LLMs systematically under-produce pedagogical content. Without explicit floors, the output will be too sparse for mastery.

| Content Type | Minimum Per Concept File | Rationale |
|---|---|---|
| Worked examples | 3–5 | Each illuminates a different facet; fewer than 3 leaves blind spots |
| Misconceptions | 5–8 | Beginners, intermediates, and cross-concept confusions all need coverage |
| Glossary terms | 15–20 | Technical writing uses many terms; under-defining creates knowledge gaps |
| Materials | 8–12 | Multiple learning modalities (text, video, interactive) need coverage |

| Content Type | Minimum Per Project | Rationale |
|---|---|---|
| Concept files | 25–30 | A medium-complexity project has 25–30 concepts worth explaining |
| Exercises | 15–20 | Spaced across foundations, core, advanced, and patterns |
| Materials files | 3–6 | One per major topic area |
| Implementation deep-dives | 5–10 | One per major system/component |

These are floors, not ceilings. Exceed them when the project warrants it.
