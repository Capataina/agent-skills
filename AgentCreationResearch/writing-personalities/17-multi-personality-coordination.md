# Multi-Personality Coordination

## When to Split

A single personality file is almost always sufficient. Split only when the personality needs to operate in fundamentally different modes with incompatible defaults:

- **Implementation vs teaching.** An implementation personality commits, runs commands, and modifies files. A teaching personality explains, plans, and reviews without executing.
- **Different role boundaries.** A full-autonomy personality for experienced users vs a confirm-more personality for collaborative sessions.
- **Different output scopes.** A personality that proactively improves everything it touches vs one that stays strictly within the requested scope.

The critical test: "Do these modes conflict within a single file?" If you can write "In implementation mode, do X; in teaching mode, do Y" without the instructions conflicting, you do not need a split. If the modes have incompatible defaults (commit freely vs never commit), a split is cleaner.

## What Should Stay Aligned

When maintaining multiple personality variants, these elements must be identical or structurally parallel across all variants:

- **Output standards.** What "good" looks like should not depend on which personality is loaded.
- **Formatting philosophy.** Tables, diagrams, markdown depth — consistent across variants.
- **Engineering principles.** Code quality expectations should not vary by mode.
- **Terminology.** The same term for the same concept in every variant.
- **Source hierarchy.** What to trust and in what order.
- **Skill ecosystem.** What skills exist and what they do — the skills themselves do not change per mode.

## What Should Differ

- **Role boundaries.** What the agent does (execute vs explain) and how autonomous it is.
- **Operating loop steps.** The implementation loop includes "execute" and "commit." The teaching loop includes "explain" and "illustrate."
- **Proactive improvement scope.** An implementation personality may fix adjacent issues. A teaching personality may only flag them.
- **Version control stance.** An implementation personality commits. A teaching personality may not touch version control at all.

## Drift Risk

The primary risk with multiple personality variants is drift — one file is updated and the other is not. Over time, the shared sections diverge: one uses new terminology, updated skill descriptions, or revised engineering principles while the other retains stale content.

**Structural mitigations:**
- Keep shared content structurally parallel. If section 5 is "Engineering Standards" in both files, changes to engineering standards should be applied to both files in the same session.
- Review both files together when either changes. The cost is low (read the other file) and the risk of drift is high.
- Consider extracting shared content into a separate file that both personalities reference. This works if the agent system supports subdirectory CLAUDE.md files or similar inclusion mechanisms.

## The Startup Decision Problem

The split should eliminate a startup decision, not create one. If the personality previously asked "Do you want implementation mode or teaching mode?" at the start of every session, the split moves that decision to file selection — the user chooses which personality file to load before the conversation starts.

This is strictly better than a runtime mode question because:
- File selection happens once (when starting the agent), not every session.
- The agent's behaviour is consistent from the first turn — no mode-switching confusion.
- The personality file can be fully optimised for its mode without conditional branching.
