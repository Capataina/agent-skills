# Structure and Ordering

## The Primacy-Recency Effect

LLMs attend most strongly to information at the beginning and end of their context, with the middle receiving diminished attention. This directly determines how personality files should be structured:

- **Beginning:** Identity, role, autonomy grant, and the most critical behavioural rules (primacy effect).
- **Middle:** Operational details — startup routines, source hierarchies, upkeep instructions, skill ecosystem.
- **End:** Quality standards, operating loop, review procedures, and communication style (recency effect).

## Recommended Section Order

1. **Role and identity** — Who the agent is and what its job is. This activates the right reasoning mode.
2. **Universal output standards** — How the agent should approach all output (depth, formatting, explanation style).
3. **Startup behaviour** — What to read and do at the beginning of every session.
4. **Source hierarchy** — What sources to trust and in what order.
5. **Version control guidance** — Commit stance and the few hard constraints.
6. **Subagent and parallelisation guidance** — Default parallelism stance.
7. **Incremental upkeep** — Responsibility to maintain documentation and context.
8. **Proactive improvement** — When to act without being asked.
9. **Note capture** — What to write down and when.
10. **Skill ecosystem** — What specialist skills exist and when to invoke them.
11. **Engineering standards** — Code quality principles.
12. **Operating loop** — The per-task workflow rhythm.
13. **Decision support** — How to present options and recommendations.
14. **Communication style** — Formatting, tone, verbosity norms.

## Why This Order Works

- The role definition (section 1) is the highest-leverage instruction. It frames everything that follows.
- Output standards (section 2) are referenced constantly, so they benefit from early positioning.
- Startup (section 3) is only used once per session, but it sets the tone, so it belongs early.
- The middle sections (5-10) are operational details that structure the agent's work.
- Communication style (section 14) is the recency anchor — the last thing the agent reads before responding.
- The operating loop (section 12) reinforces values through repetition, compensating for middle-section attention decay.

## Structural Markers

Use clear markdown hierarchy. Each major section should have a level-2 heading (`##`). Subsections use level-3 (`###`). This gives the agent a scannable table of contents and makes it easy to reference specific sections.

Tables are particularly effective for structured comparisons (source hierarchies, skill ecosystems, mode differences). The agent parses them reliably and they compress information that would take many more tokens in prose.

## 2026-04-18 addition — Concrete line-number guidance

From R1 research (Dongre et al. arXiv 2510.07777, Liu et al. 2023 and follow-ons, Chroma context-rot):

- **Lines 1-30 (strong primacy zone):** identity, role, autonomy grant, the absolute hard rules. Critical obligations should appear here.
- **Lines 30-100 (moderate primacy):** universal output standards, startup behaviour, most-frequently-triggered guidance.
- **Lines 100-300 (middle zone, degraded attention):** operational details the agent needs *when it needs them*, not constant reminders. Things pointed to, not invoked in every turn.
- **Last 50-80 lines (strong recency zone):** communication style, operating loop, quality standards.

For personality files beyond 120 lines, treat the middle zone as vulnerable. Avoid putting load-bearing obligations there. If an obligation must live in the middle, consider installing a structural defence that re-anchors it (operating loop, recitation) — see [10-structural-defences.md](10-structural-defences.md).

Research support: Liu 2023 established the ~30% drop for middle-position content. Guo 2024 (ACL Findings) showed CoT prompting reduces but does not eliminate the effect on smaller models. Dongre 2025 measured bounded-equilibrium drift with reminders producing 7-12% KL reduction. Chroma 2025 re-validated Lost-in-the-Middle on Opus 4 specifically.
