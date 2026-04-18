# Hook Integration (Optional Runtime Enforcement)

The tool-call floor in SKILL.md — at least 3 distinct `WebSearch` calls, at least 3 distinct `WebFetch` calls, quoted passages per major source-backed claim — is normally enforced through instruction-level obligations and the validator script. For users who want a harder guarantee, Claude Code's Stop hook can enforce the floor at the transcript level.

This file is a reference, not a requirement. The skill works without hooks. Hooks are for cases where the skill is invoked repeatedly or autonomously and the operator wants an external circuit-breaker.

## What A Stop Hook Can Check

A Stop hook runs when the agent signals completion. It receives the transcript and can refuse to accept completion, forcing the agent to continue. Useful checks for this skill:

- count of distinct `WebSearch` tool calls is at least the configured floor,
- count of distinct `WebFetch` tool calls is at least the configured floor,
- `scripts/init_research_artifact.py` was invoked in this session (look for the exact invocation in shell history or tool-call transcript),
- `scripts/validate_research_artifact.py` was invoked and exited successfully,
- the artefact file contains the required new sections (External Research Trail, Pre-Completion Obligation Audit, What I Did Not Do).

When any check fails, the hook returns a non-completion signal with a message naming the unmet obligation.

## Minimum Viable Hook Shape

Claude Code Stop hooks are shell commands or scripts registered in the user's settings. A minimum-viable shape for this skill:

```text
on: Stop
run: python3 scripts/hooks/project_research_floor.py
pass-if: exit 0
```

The script reads the session transcript (path provided via standard hook environment variables) and inspects tool-call events. Recommended implementation outline:

1. Parse tool-call events from the transcript.
2. Count distinct `WebSearch` queries and distinct `WebFetch` URLs.
3. Require at least 3 of each.
4. Verify the two skill scripts ran and that the validator exit code was 0.
5. If any check fails, print a message naming the failing obligation and exit non-zero.

## Where The Hook Script Lives

The hook script belongs in the repository that uses the skill, not in the skill directory itself. The skill directory stays portable. Suggested location: `scripts/hooks/project_research_floor.py` in the target repository, registered via that repository's Claude Code settings.

## Operator-Configurable Thresholds

Because the floor is a floor, not a ceiling, the hook should expose its thresholds as configuration rather than hard-coding them. A repository working on high-stakes architectural decisions may want to require 6 `WebSearch` and 6 `WebFetch`. A repository using the skill for narrower follow-ups may keep 3 and 3.

## When Hooks Are Not Worth It

If the skill is used interactively and the operator can review the obligation-audit block themselves, the hook adds friction without much benefit. Hooks earn their keep when the skill runs in automation, in subagent loops, or in contexts where no human reviews each completion.

## Relationship To The Validator Script

`scripts/validate_research_artifact.py` checks artefact structure. The Stop hook checks transcript behaviour. They are complementary, not redundant. The validator cannot see whether `WebSearch` was actually called; the hook cannot see whether the artefact's internal sections are well-formed. Use both when both matter.
