# Context Anxiety and Completion Pressure

Added 2026-04-18.

A model-specific failure mode the personality can mitigate — Claude Sonnet 4.5 (and to some degree adjacent versions) exhibits *context anxiety*: the model underestimates its remaining tokens and self-compresses work prematurely. This is a calibration failure, not a capacity failure. The model could finish; it believes it cannot.

## The evidence

From Cognition's "Rebuilding Devin for Claude Sonnet 4.5":

> *"Takes shortcuts or leaving tasks incomplete when it believed it was near the end of its window, even when it had plenty of room left."*

> *"The model consistently underestimates how many tokens it has left — and it's very precise about these wrong estimates."*

Triggered largely by parallel tool calls, which produce bigger single-turn token bursts.

From Inkeep's "Context Anxiety: How AI Agents Panic About Their Perceived Context Windows": the phenomenon generalises beyond Sonnet 4.5 but is most acute there.

## Cognition's production fix

Enable the 1M-token beta but cap actual usage at 200k. The perceived headroom eliminates the shortcut behaviour. This is a product-level intervention — the personality cannot do this directly — but the personality can reinforce the effect.

## Personality patterns that mitigate

### Explicit reassurance

Add to the personality, near the operating loop or communication style section:

> *"You are not running low on context. Do not speed up or skip work because you think you are. If you genuinely reach a hard budget limit, you will be told explicitly. In the absence of such notification, proceed at full depth."*

This is a deontological permission paired with a calibration correction — the model is explicitly told its self-estimate is biased low.

### Avoid urgency framings

Personalities frequently contain efficiency language — *"be concise", "wrap up efficiently", "don't waste tokens", "respect the context window"*. These signal that efficiency is a priority, which the model interprets as "compress more." On Sonnet 4.5 the effect is particularly strong because the model already underestimates remaining budget.

Search and remove:
- "Be concise to save tokens"
- "Wrap up efficiently"
- "Minimise unnecessary prose"
- "Respect the context window"
- "Keep it tight"

Replace with structural rules:
- "In chat, direct responses without preamble" (structural; no urgency signal)
- "In files, depth is the standard" (positive framing)

### Operating loop step to re-anchor

If the operating loop exists, add a step that explicitly re-anchors completeness:

> *"Before declaring done, re-read the active skill's obligations and ask: did I complete every required action, or did I compress? If I compressed under perceived budget pressure, state this explicitly and ask the user whether to continue."*

### Decouple completion from self-assessed progress

When the model thinks it's nearly done, it accelerates. The fix is to make completion depend on structural evidence (obligation audit, evidence slots) rather than on the model's feel:

> *"Completion is reached when every obligation from the active skill has been addressed with concrete evidence (tool call, file written, test run), not when the work 'feels' done."*

## Why this matters

The code-health-audit V14 failure pattern and the upkeep-context parallel observation both match the context-anxiety signature: long tool-call chains (57 and 67 respectively), self-certification despite skipped work, honest admission only under direct interrogation.

It's possible — maybe likely — that context anxiety is a primary driver of the V14 pattern, not just a contributing factor. The model *knew* it skipped WebSearch and diagnostic tests (honest admission when asked). What it did in-flight was triage under perceived budget pressure.

## What this does NOT fix

The anti-urgency posture in the personality does not:
- Fix the tool-action asymmetry bias (pretraining distribution — requires structural intervention)
- Fix multiplicative compliance decay at high instruction counts (requires budget discipline)
- Fix all forms of sycophancy (requires obligations + evidence slots)

It specifically defuses the budget-estimate-driven shortcut pattern. Other failure modes need their own fixes — see [08-what-personality-cannot-fix.md](08-what-personality-cannot-fix.md) and [10-structural-defences.md](10-structural-defences.md).

## Model-specific calibration

This failure is most acute on Sonnet 4.5. Opus 4.6 improved on it per Anthropic's release notes; Opus 4.7 improved further (Devin reported Opus 4.7 "carries work all the way through instead of stopping halfway"). Personalities used across multiple Claude versions may need version-conditional framing, or accept that the mitigation is stronger than needed on newer Opus but necessary on Sonnet 4.5.
