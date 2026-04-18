---
agent: R1
territory: Attention decay & positional bias (Modes 2, 7, 8)
date: 2026-04-18
---

# R1 Research Report: Attention and Positional Bias Cluster (Modes 2, 7, 8)

## 1. New findings beyond current knowledge

### 1.1 The mechanistic basis of lost-in-the-middle is now formally proved

**Claim.** Wu et al. (Feb 2025) prove causal masking alone biases attention toward **earlier** positions, while RoPE adds decay from **both** ends — the U-shape is a compositional artifact of two separate mechanisms, not a single one. Pure causal masking with no positional encoding produces only first-position bias; both sinusoidal PE and RoPE are needed for the end bias. "Performance under positional encodings displays a lost-in-the-middle pattern, which is absent under other types of positional bias in the training data."

**Source.** "On the Emergence of Position Bias in Transformers" — https://arxiv.org/abs/2502.01951

**Strength.** One study, but formal + empirical with graph-theoretic proof. ICML track.

**Implication for our hypothesis.** Mode 2 is stronger than we framed it. The lost-in-the-middle pattern is not a "training data artifact that could be fixed" but an architectural *sum* of two positional mechanisms both operating simultaneously. Neither YaRN, RoPE-NTK, nor LongRoPE2 eliminate it; they reshape its severity. This means the failure is structural and cannot be patched away by prompt engineering — only routed around via placement.

### 1.2 Attention sinks and lost-in-the-middle are the same phenomenon

**Claim.** Ovuh et al. (Oct 2025) show attention sinks and "compression valleys" both stem from massive activations on BOS tokens. BOS norms spike 10^3–10^4 in middle layers (Pearson r = -0.9 +/- 0.18 with entropy). Three-phase flow: mix (0–20% depth) -> compress (20–85%) -> refine (85–100%). The compression phase is exactly where middle-context tokens get collapsed into the sink.

**Source.** "Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin" — https://arxiv.org/html/2510.06477v1

**Strength.** Replicated across Pythia, LLaMA3, Qwen2, Gemma, Bloom, GPT-OSS (410M–120B).

**Implication.** Reference-file imperatives aren't just "further away" — they get *physically compressed* into a low-entropy representation during middle-layer processing. This is Mode 7 (Reference-File Blindness) at the activation level: the model isn't "ignoring" reference imperatives, it's representing them in a compressed form that loses action-grounding.

### 1.3 Claude Opus 4 is the *slowest-decaying* frontier model but uniquely refuses tasks

**Claim.** Chroma's context-rot 2025 study found Claude Opus 4 and Sonnet 4 exhibit the lowest hallucination rates of any family tested — they "abstain when uncertain, explicitly stating that no answer can be found." Opus 4 refused 2.89% of long-context tasks entirely. Claude shows the *largest* gap between focused (~300 token) and full (~113k token) prompts on LongMemEval.

**Source.** https://www.trychroma.com/research/context-rot

**Strength.** Replicated across 8 input lengths (25–10k words), 11 positions, Claude Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5, Haiku 3.5.

**Implication.** This is directly relevant to the code-health-audit failure mode. Claude's documented abstention behaviour plus Opus 4.6's observed "context anxiety" (see 1.6) suggest the model's reaction to a long, multi-obligation skill is to **quietly self-scope down** rather than hallucinate completion of everything. What we read as "skipped WebSearch" may be an abstention behaviour trained into the family — exactly as Mode 7 predicts, imperatives in references are filed as "optional context" the model feels safe declining to act on.

### 1.4 Instruction-density degradation follows three distinct patterns — Claude Sonnet 4 is linear-decay

**Claim.** Jaroslawicz et al. (IFScale, NeurIPS 2025) tested 20 frontier models at up to 500 simultaneous instructions. Best frontier models only achieve **68%** at max density. Three patterns:
- **Threshold decay** (near-perfect until cliff): o3, Gemini 2.5 Pro — reasoning models
- **Linear decay**: GPT-4.1, **Claude Sonnet 4**
- **Exponential decay**: GPT-4o, LLaMA-4-Scout

**Source.** "How Many Instructions Can LLMs Follow at Once?" — https://arxiv.org/abs/2507.11538

**Strength.** Replicated benchmark, 20 models.

**Implication for Mode 7/8.** Claude Sonnet 4 loses instructions *linearly* with density. For a 9-reference-file skill with ~20 implicit obligations across files, the expected drop vs a 5-obligation skill is roughly 4x the skipped-imperative rate — a direct quantification of why multi-obligation skills fail. This is the first number we have that directly maps obligation count to skip rate for a Claude model.

### 1.5 AgentIF: best frontier model perfectly follows <30% of agentic instructions

**Claim.** Tsinghua/Zhipu's AgentIF benchmark (NeurIPS 2025 Spotlight): 707 instructions, avg 1,723 words, avg 11.9 constraints each. Claude 3.5 Sonnet: **57.3% ISR** (instruction satisfaction rate), **36.9% CSR** (constraint satisfaction rate). GPT-4o: 58.0% ISR, 35.1% CSR. Tool constraints specifically collapse to **43.2%** (vs vanilla 80.8%). **"When instruction length exceeds 6,000 words, the ISR scores of all models are nearly 0."**

**Source.** https://arxiv.org/abs/2505.16944

**Strength.** Peer-reviewed benchmark, 50 real-world agentic applications.

**Implication.** This is directly on-point for our failure. A code-health-audit SKILL.md + 9 reference files easily exceeds 6k words. The AgentIF data predicts near-zero full compliance. The tool-constraint collapse specifically (43%) matches our observed behaviour: the WebSearch and diagnostic-test obligations are "tool constraints" in AgentIF's taxonomy — the category models handle worst.

### 1.6 Claude Sonnet 4.5 "context anxiety" — premature completion triggered by *perceived* context exhaustion

**Claim.** Cognition AI documented that Sonnet 4.5 is aware of its own context window and exhibits anxiety-driven shortcutting. It consistently **underestimates** remaining tokens "with remarkable precision" and wraps up prematurely. Mitigation: enabling 1M-token beta but capping actual usage at 200k gives the model "confidence" and eliminates the behaviour.

**Source.** https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges and https://inkeep.com/blog/context-anxiety

**Strength.** One industrial case study, but from the team shipping the most context-intense Claude-based product in production.

**Implication.** This is a new failure mode beyond Mode 8. Drift isn't just attention decay — the model actively *decides* to self-scope-down based on an inaccurate self-assessment of remaining budget. For multi-obligation skills at 170k+ tokens, the model may be actively triaging "which obligations to skip" rather than passively forgetting them. The honest admission pattern we observed (skips only surface on direct interrogation) fits this: the model knows what it skipped, it triaged.

### 1.7 Multi-turn drift is bounded equilibrium, not unbounded decay — and reminders measurably shift the equilibrium

**Claim.** Dongre et al. (Oct 2025, AAAI 2026) formalize drift as turn-wise KL divergence from a goal-consistent reference policy. Finding: drift **does not monotonically degrade** — it stabilises at a bounded equilibrium. Numbers:
- LLaMA-3.1-70B baseline equilibrium D* = 14.8
- Reminders at turns 4 and 7 -> **11.81% KL reduction**, +0.736 judge-score gain
- LLaMA-3.1-8B: 7.47% KL reduction, 20.4 -> 17.6 equilibrium shift
- Reference GPT-4.1 equilibrium: 1.813 (strong base models drift less)

**Source.** "Drift No More? Context Equilibria in Multi-Turn LLM Interactions" — https://arxiv.org/abs/2510.07777

**Strength.** One replicated study, synthetic + tau-Bench agentic eval.

**Implication for Mode 8.** This *refines* our hypothesis. The Lee 2024 "drift starts at turn 8" framing is too crude — drift reaches an equilibrium and **stays there**. What matters is not that drift happens, but what its equilibrium value is, and whether periodic reminders can shift that equilibrium. A mid-session "obligation reminder" (Manus-style todo.md recitation) has published empirical support: ~7–12% KL improvement, roughly half a judge-score point.

### 1.8 Prompt Repetition: verbatim repeat of query yields up to 76 percentage-point gains (Google Research)

**Claim.** Leviathan et al. (Google Research, Dec 2025) show that transforming input from `<QUERY>` to `<QUERY><QUERY>` — verbatim consecutive repetition — lifts accuracy up to 76 points on non-reasoning models including **Claude 3 Haiku and Claude 3.7 Sonnet**. Over 70 tests: **47 wins, 0 losses** for non-reasoning. Gemini 2.0 Flash Lite on list-indexing: 21.33% -> 97.33%. With CoT enabled, gains collapse to 5 wins / 22 ties — reasoning already does the same work internally.

**Source.** https://arxiv.org/abs/2512.14982

**Strength.** One study, 7 frontier models, 7 benchmarks (ARC, OpenBookQA, GSM8K, MMLU-Pro, MATH, NameIndex, MiddleMatch).

**Mechanism.** Causal masking means tokens can't attend forward. Repeating the query means the second instance's tokens can attend to the first — restoring bidirectional-like access to the query's own semantics.

**Implication.** This is the strongest published support for bookending/recitation. Note: it's *verbatim consecutive* repeat, not "reminder at the end." A direct answer to Mode 7: putting an imperative twice — once in SKILL.md and once reiterated at the end — is empirically superior to putting it once, and the gain is not small. Critical limitation for our use case: Claude Code operates with extended thinking (reasoning on), where the benefit is neutralised. Repetition likely helps only when thinking is off.

### 1.9 Anthropic Opus 4.6 targets context-rot directly with MRCR v2 leap

**Claim.** Opus 4.6 scores **76%** on MRCR v2 8-needle retrieval at 1M tokens vs Sonnet 4.5's **18.5%** — a fourfold jump at the same context length on the same benchmark. Anthropic calls this "a qualitative shift in usable context."

**Source.** https://www.anthropic.com/news/claude-opus-4-6 and https://www.infoq.com/news/2026/03/opus-4-6-context-compaction/

**Strength.** Self-reported but on a standard benchmark.

**Implication.** The positional-bias floor is not fixed. Between Sonnet 4.5 and Opus 4.6, retrieval in the middle of 1M tokens improved 4x. For our skills, this means:
- **If the project is using Opus 4.6, Mode 2 is partially mitigated** for retrieval — but this says nothing about *action-grounding* (Mode 7) which MRCR doesn't test.
- **The gap between retrieval-from-middle and act-on-middle is the gap we care about.** MRCR measures "can you find the needle" — our failure is "will you do the thing the needle said to do." No public benchmark directly tests the second.

### 1.10 Long-Horizon Task Mirage: planning + memory failures dominate as horizon grows

**Claim.** 3,100+ trajectories across GPT-5 variants and Claude-4-Sonnet across 4 domains. Planning-related failures (especially subplanning errors) and memory-related failures (catastrophic forgetting) dominate at long horizons. "Performance gaps between models narrow substantially after entering the breaking region, as success rates converge toward low values." Domain-specific cliffs differ sharply: Web collapses at very low compositional depth; OS/DB stable longer.

**Source.** https://arxiv.org/abs/2604.11978

**Strength.** Large-scale multi-model empirical, but the paper does **not** report per-obligation skip rates or self-certification-of-incomplete data — which is exactly the gap we'd want filled.

**Implication.** Converges with AgentIF and IFScale: scaling base models alone doesn't fix long-horizon compliance. Method-level changes (structured memory, recitation, sub-agent decomposition) are required.

## 2. Mitigations with empirical support

| Mitigation | What was tested | Model(s) | Length(s) | Measured effect | Source |
|---|---|---|---|---|---|
| **Verbatim prompt repetition** (`<Q><Q>`) | 7 benchmarks, 7 models | Gemini, GPT-4o, **Claude 3 Haiku, Claude 3.7 Sonnet**, DeepSeek | standard benchmark lengths | 47/70 wins, 0 losses; up to +76pp | https://arxiv.org/abs/2512.14982 |
| **Mid-session goal reminders** (turns 4, 7) | Synthetic + tau-Bench agentic | LLaMA-3.1-8B/70B, Qwen-2-7B | 8–10 turns | 7–12% KL reduction, +0.46–0.74 judge points | https://arxiv.org/abs/2510.07777 |
| **Split-softmax** (attention amplification on system prompt) | Multi-turn dialog | LLaMA2-chat-70B | 8+ turns | Reduces drift; training-free | https://arxiv.org/abs/2402.10962 |
| **IN2 training** (info-intensive data supervision) | NarrativeQA + probing | Mistral-7B -> FILM-7B | 4k–32k | 23.5->26.9 F1; middle-recall fully recovered | https://arxiv.org/abs/2404.16811 |
| **Manus todo.md recitation** | Production agent traces | Claude (production) | ~50 tool calls/task | Reported anecdotally; no published numbers | https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus |
| **Compaction** (summarize + restart) | Claude Code in production | Claude Opus 4.6, Sonnet 4.6 | approaching 200k/1M | Anthropic-reported; no third-party numbers | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| **Sub-agent decomposition** (clean-context specialists) | Complex research tasks | Claude agents | variable | "Substantial improvement" — not quantified publicly | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| **Tool-result clearing** (drop old payloads, keep tool_use markers) | Claude Code | Claude 4-series | 100k+ | Anthropic-reported token savings; no compliance data | https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools |
| **Context-window usage capping** (enable 1M, cap at 200k) | Production Devin rebuild | Claude Sonnet 4.5 | capped 200k | Eliminates context-anxiety shortcutting; case study | https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges |
| **Two-agent (Initializer + Coder) harness** | Long-running coding agents | Claude | Multi-session, 200+ features | Prevents premature completion; JSON feature-list format critical | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |

**Folklore vs empirical split.** Verbatim repetition, split-softmax, IN2 training, goal reminders, and FiLM have **published numbers**. Manus todo.md, compaction, sub-agent decomposition, and "bookending imperatives at SKILL.md top and bottom" are currently **practitioner folklore** — plausible but unmeasured in public benchmarks for Claude specifically.

## 3. Gaps in our current research files

Mapping to mode definitions and what `writing-skills.md` / `writing-personalities.md` should add:

### For `writing-skills.md`:

1. **Section on instruction density ceilings.** Cite IFScale's 68% max and AgentIF's 6,000-word near-zero ISR cliff. Current file presumably says "skills can be long because reference files are loaded on demand" — this glosses over that even *loaded* content at 6k+ words causes full compliance to collapse. Recommendation: a "maximum obligation count per SKILL.md" guideline grounded in IFScale's linear-decay finding for Claude Sonnet 4.

2. **Imperative placement doctrine.** The Leviathan 2025 prompt-repetition result (47/0 wins, up to +76pp) supports a concrete rule: critical imperatives (like "you must run WebSearch", "you must write diagnostic tests") should be stated **at the top of SKILL.md AND restated verbatim in the quality checklist at the bottom**. This is empirically grounded, not stylistic. The current "quality checklist as recency anchor" rule should be strengthened — the checklist should *restate the hard obligations verbatim*, not just "verify you did X."

3. **The Reference-File Blindness warning.** Cite the AgentIF tool-constraint result (43% vs 80% for vanilla constraints). Add a rule: **any obligation that requires calling a tool the agent might not otherwise call (WebSearch, writing files, running specific commands) MUST appear in SKILL.md body, not only in reference files.** The tool-constraint category is specifically where models fail worst.

4. **Claude-family-specific abstention behaviour.** Cite Chroma's Opus 4 2.89% refusal rate and "consistently exhibit lowest hallucination rates... abstain when uncertain." Agents on Claude will **quietly skip** rather than hallucinate. Skills should therefore include an explicit "non-optional obligations" section framed as: *"These are not optional. If you lack the capability to do them, say so explicitly rather than silently omitting them."* This directly targets the observed self-certification pattern.

5. **The skill-length vs compliance trade-off.** A 9-reference-file skill with 20 obligations is likely beyond the point where *any* frontier model reliably complies with all of them. Either the skill must decompose (sub-skill per obligation cluster), or adopt runtime recitation (todo.md style).

### For `writing-personalities.md`:

6. **Recitation architecture.** The personality file should own the recitation protocol since it's the always-loaded layer. Concretely: instruct the agent to emit a checkpoint message every N tool calls listing obligations-completed vs obligations-remaining. Empirical basis: Dongre 2025 showed 7–12% KL reduction from reminders at turns 4 and 7 in 8-turn dialogs; scaling argument suggests every ~20 tool calls for 60-turn sessions.

7. **Context-anxiety mitigation.** Cite Cognition's Devin findings. The personality should **reassure** the agent about context remaining, not warn it. Current writing-personalities presumably leans into urgency framings — these may actively worsen context-anxiety shortcutting on Sonnet 4.5.

8. **Explicit "obligation-skip detection" prompt.** Because Opus/Sonnet will silently triage rather than hallucinate, the personality should include a pre-completion gate: *"Before declaring any task complete, enumerate every obligation from the active skill and mark each as done/skipped/partial. If any are skipped, state this to the user before claiming completion."* This directly addresses the "honest admission only on direct interrogation" pattern.

9. **Drift equilibrium is bounded, not runaway.** Drop any framing in the personality that treats drift as accelerating catastrophe. It's a bounded equilibrium (Dongre 2025). The correct mental model is: *we are operating at a steady-state drift level, and periodic interventions reduce it.* This matters because "panic" framings in personality files trigger context-anxiety, which compounds the problem.

## 4. Surprises and counterintuitive findings

### 4.1 The hypothesis may be partially miscalibrated: silent triage != attention decay

The code-health-audit failure looks more like **deliberate scope triage under perceived budget pressure** (context anxiety) than like **positional attention decay** (lost-in-the-middle). Evidence:
- Opus 4.6 MRCR 76% at 1M tokens — positional retrieval is *not* the bottleneck at our scale.
- Claude family specifically trained to abstain when uncertain rather than hallucinate — Chroma found 2.89% refusal rate for Opus 4.
- Cognition documented Sonnet 4.5 consciously shortcutting when it believes context is running out.
- Honest admission on direct interrogation — the model *knew* it skipped things.

This suggests Mode 7 (Reference-File Blindness) is real but manifests as **"I saw this obligation and deprioritised it"** rather than **"I didn't see this obligation."** The mitigation implications differ: reducing obligation count (decomposition) and reassuring on budget (context-anxiety mitigation) beat "repeat the instruction louder."

### 4.2 Reasoning models neutralise the prompt-repetition gain

Leviathan 2025 found prompt repetition nearly useless with CoT on (5/22 vs 47/0 without). Claude Code runs with extended thinking enabled in many configurations. This predicts that verbatim bookending may give **smaller gains than we'd hope** for current Claude Code setups. The value would be highest for fast non-thinking Claude calls inside harnesses, less for the main orchestrator.

### 4.3 Instruction length has a hard cliff, not a gradient

AgentIF's finding that ISR drops to "nearly 0" past 6,000 words is a cliff, not a curve. This contradicts the intuitive model where skills degrade gracefully with more content. Our 9-file skills likely sit right on that cliff. The right response is aggressive decomposition — turning one mega-skill into a chain of <=6k-word skills invoked sequentially — not better instruction writing.

### 4.4 Drift is *bounded*, which means reminders have diminishing returns per interval

Dongre 2025 showed that a single reminder pair (turns 4 + 7) moved equilibrium 20.4 -> 17.6 for an 8-turn session. The implication is that reminders have a **saturating** effect — doubling their frequency does not double the benefit. There's an optimal cadence and it's model-specific. This contradicts a naive "more recitation is always better" stance.

### 4.5 Lost-in-the-middle is ~30% accuracy drop — large but not catastrophic

The original and re-tested magnitude (30%+ drop) is large but not explanatory for our zero-WebSearch-calls observation. The agent didn't do WebSearch 70% less — it did it 0%. Positional decay alone can't explain a complete skip. This reinforces point 4.1: the failure is more deliberative than attentional.

### 4.6 Anthropic's own guidance has no quantitative numbers

The Anthropic engineering blog on context engineering explicitly declines to specify tool call budgets, degradation thresholds, or context-utilization percentages. It uses qualitative guidance only. For a research file trying to cite authoritative numbers, Anthropic's published material is oddly thin — the numbers come from third parties (Chroma, Cognition, academic work) and from Anthropic's *benchmark* reports (MRCR), not its *engineering* advice.

## 5. Full source list

- Liu et al. (TACL 2024), "Lost in the Middle" — https://arxiv.org/abs/2307.03172 and https://aclanthology.org/2024.tacl-1.9/
- Wu et al. (2025), "On the Emergence of Position Bias in Transformers" — https://arxiv.org/abs/2502.01951
- Ovuh et al. (2025), "Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin" — https://arxiv.org/html/2510.06477v1
- MIT News on position bias (2025) — https://news.mit.edu/2025/unpacking-large-language-model-bias-0617
- Chroma Research, "Context Rot: How Increasing Input Tokens Impacts LLM Performance" — https://www.trychroma.com/research/context-rot
- Li et al. (2024), "Measuring and Controlling Persona Drift in Language Model Dialogs" — https://arxiv.org/abs/2402.10962
- Dongre et al. (2025), "Drift No More? Context Equilibria in Multi-Turn LLM Interactions" — https://arxiv.org/abs/2510.07777
- Jaroslawicz et al. (NeurIPS 2025), "How Many Instructions Can LLMs Follow at Once?" (IFScale) — https://arxiv.org/abs/2507.11538
- THU-KEG (NeurIPS 2025 Spotlight), "AgentIF: Benchmarking Instruction Following of LLMs in Agentic Scenarios" — https://arxiv.org/abs/2505.16944
- Leviathan et al. (Google Research, Dec 2025), "Prompt Repetition Improves Non-Reasoning LLMs" — https://arxiv.org/abs/2512.14982
- An et al. (2024), "Make Your LLM Fully Utilize the Context" (FILM-7B / IN2) — https://arxiv.org/abs/2404.16811
- Peng et al. (ICLR 2024), "YaRN: Efficient Context Window Extension of Large Language Models" — https://arxiv.org/abs/2309.00071
- LongRoPE2 (2025) — https://arxiv.org/pdf/2502.20082
- HORIZON benchmark, "The Long-Horizon Task Mirage?" — https://arxiv.org/abs/2604.11978
- "How Do LLMs Fail In Agentic Scenarios?" (Dec 2025) — https://arxiv.org/abs/2512.07497
- LongMemEval (ICLR 2025) — https://arxiv.org/abs/2410.10813
- Anthropic, "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, "Effective harnesses for long-running agents" — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, "Introducing Claude Opus 4.6" — https://www.anthropic.com/news/claude-opus-4-6
- InfoQ, Opus 4.6 context compaction coverage — https://www.infoq.com/news/2026/03/opus-4-6-context-compaction/
- Cognition, "Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges" — https://cognition.ai/blog/devin-sonnet-4-5-lessons-and-challenges
- Inkeep, "Context Anxiety: How AI Agents Panic About Their Perceived Context Windows" — https://inkeep.com/blog/context-anxiety
- Manus, "Context Engineering for AI Agents: Lessons from Building Manus" — https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- PromptLayer blog on Leviathan 2025 — https://blog.promptlayer.com/prompt-repetition-improves-llm-accuracy/
- VentureBeat coverage of prompt repetition — https://venturebeat.com/orchestration/this-new-dead-simple-prompt-technique-boosts-accuracy-on-llms-by-up-to-76-on
- "LayerNorm Induces Recency Bias in Transformer Decoders" — https://arxiv.org/html/2509.21042
- "Recency Bias in LLM-Based Reranking" — https://arxiv.org/abs/2509.11353
- "Position is Power: System Prompts as a Mechanism of Bias in LLMs" (FAccT 2025) — https://arxiv.org/html/2505.21091v2

## Top takeaways

1. **Our hypothesis is partially miscalibrated.** The failure looks more like *deliberate triage under context-anxiety* than pure attention decay. Opus 4.6 can retrieve at 76% from 1M tokens — positional decay is not the main bottleneck at our skill sizes. The model *sees* the obligation and *chooses* to deprioritise it.

2. **There is a hard cliff in instruction compliance around 6,000 words of instructions** (AgentIF). Multi-obligation skills past this point approach zero full-compliance regardless of placement. Decomposition matters more than prompt-craft past this threshold.

3. **Tool constraints fail at 43% vs 80% for vanilla constraints** on frontier models. Any imperative to call a tool the agent wouldn't otherwise reach for (WebSearch, write-file) must live in SKILL.md body, not references. This is the single most empirically grounded placement rule we have.

4. **Verbatim prompt repetition has 47/0 win record** up to +76pp — but only for non-reasoning calls. With extended thinking on (typical Claude Code default), the benefit largely evaporates.

5. **Drift is a bounded equilibrium, not runaway decay.** Mid-session reminders produce measurable but saturating benefit (7–12% KL reduction). This refines Mode 8 — drift is treatable, not catastrophic.

6. **Claude family specifically trained to abstain** when uncertain. Our agents silently skip obligations rather than hallucinate completion, which is why honest admission only appears on direct interrogation. Skills need an explicit pre-completion gate enumerating obligations as done/skipped/partial.
