# Startup Routines

## Purpose

The startup routine establishes the agent's understanding of the project before it takes any action. It answers: What is this project? What state is it in? What does the user likely need?

## Design Principles

1. **Read the minimum needed to orient, then pull more on demand.** Do not load all context files at startup. Load the structural map (architecture) and the preference layer (notes), then pull specific system files when the task requires them.

2. **Do not block startup on missing files.** If a context folder does not exist, note it and recommend creating it — do not refuse to work. The agent should degrade gracefully.

3. **Summarise what you learned.** The startup summary serves two purposes: it confirms to the user that the agent understands the project, and it anchors the agent's own understanding.

4. **Ask a focusing question.** After the summary, ask what the user wants to do. This prevents the agent from guessing and going in the wrong direction.

## What to Avoid

- Loading the entire `context/` folder at startup — wastes context tokens on information that may not be relevant.
- Reading code at startup unless the task clearly requires it — startup should be fast.
- Running heavy analysis at startup — that is what skills are for.
- Loading reference or learning material at startup — educational material is reference, not startup context.

## 2026-04-18 addition — version-awareness in startup

Anthropic's Opus 4.7 release notes explicitly warn: *"prompts written for earlier models can sometimes now produce unexpected results. Users should re-tune their prompts and harnesses accordingly."*

Personalities should be version-aware. Consider adding to the startup routine: *"At startup, note the model version in use. This personality was tuned for [version X]. If running on a different version, expect some behaviour differences and flag any that materially affect the user's request."*

This is not strictly a startup mechanism but a version-calibration primitive. Opus 4.7 specifically exhibits measurably different failure profiles from 4.6 (per Devin, Notion, Vercel, Genspark reports) — skills and personalities tuned for one version shouldn't be assumed to transfer.
