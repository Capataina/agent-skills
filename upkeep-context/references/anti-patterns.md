# Anti-Patterns

## Table of Contents

1. [Milestone Slicing](#1-milestone-slicing)
2. [Diary History](#2-diary-history)
3. [Duplicate Ownership](#3-duplicate-ownership)
4. [Vague Catch-All Files](#4-vague-catch-all-files)
5. [Over-Broad System Files](#5-over-broad-system-files)
6. [Cosmetic Rewrites](#6-cosmetic-rewrites)
7. [Aspirational Current-State Sections](#7-aspirational-current-state-sections)
8. [Shallow Architecture](#8-shallow-architecture)
9. [Thin Systems](#9-thin-systems)
10. [Decorative Formatting](#10-decorative-formatting)
11. [Stale Research References](#11-stale-research-references)
12. [Research Hoarding](#12-research-hoarding)

This reference names the common failure modes that make a `context/` folder noisy, unstable, shallow, or misleading.

## 1. Milestone Slicing

Bad:

- `milestone-1.md`
- `phase-2.md`
- `sprint-4-notes.md`

Why it fails:

- later milestones restate earlier reality,
- information duplicates instead of moving to a canonical home,
- readers must reconstruct the present from historical slices,
- upkeep becomes additive clutter rather than maintenance.

Corrective action:

- reorganise by subsystem or feature ownership,
- move durable content into `systems/` files,
- delete the milestone files once their useful content has a home.

## 2. Diary History

Bad:

- `history.md`
- `recent_changes.md`
- "today we did X" sections

Why it fails:

- grows without bound,
- preserves chronology instead of current truth,
- hides durable lessons inside timestamped narrative.

Corrective action:

- keep only durable lessons,
- attach them to the owning subsystem in `Durable Notes / Discarded Approaches`.

## 3. Duplicate Ownership

Bad:

- authentication described fully in both `systems/auth.md` and `systems/user-management.md`,
- caching logic described fully in both the API and storage docs,
- architecture repeating large chunks of system-doc reality.

Why it fails:

- updates drift,
- contradictory truth appears,
- readers do not know which file owns the topic.

Corrective action:

- pick one canonical home,
- trim neighbouring files to interface-level mention only.

## 4. Vague Catch-All Files

Bad:

- `misc.md`
- `general-systems.md`
- a single undifferentiated dump file with no topical structure

Why it fails:

- no stable scope,
- no canonical ownership,
- high overlap pressure,
- tends to accumulate uncurated leftovers.

Corrective action:

- redistribute content into proper system docs or topical note files,
- delete the catch-all file.

Note: the canonical `notes/` folder with topical note files is not a catch-all. Each note file has a clear topic, evolves in place, and is indexed in `notes.md`. The anti-pattern is an undifferentiated dump file, not a structured topical notes system.

## 5. Over-Broad System Files

Bad:

- one system file covers environment, observations, analytics, debug, and controller logic together.

Why it fails:

- too hard to keep current,
- independent changes collide,
- readers cannot isolate relevant information quickly.

Corrective action:

- split by stable implementation boundary.

## 6. Cosmetic Rewrites

Bad:

- renaming half the folder because cleaner names are possible,
- rewriting files that were already good enough,
- restructuring only for aesthetic purity.

Why it fails:

- creates churn,
- destroys stable references,
- makes upkeep noisy and untrustworthy.

Corrective action:

- preserve good-enough structure,
- change only when understanding materially improves.

## 7. Aspirational Current-State Sections

Bad:

- `Current Implemented Reality` describes things not actually implemented,
- missing items are presented as real,
- future design is mixed into present reality.

Why it fails:

- misleads implementation work,
- hides gaps,
- breaks trust in the folder.

Corrective action:

- move speculative material into planned or missing sections,
- keep current-state sections reality-only.

## 8. Shallow Architecture

Bad:

- architecture that only lists top-level folders,
- no subsystem responsibilities,
- no dependency direction,
- no execution or data flow,
- no one-line descriptions.

Why it fails:

- it does not orient the reader,
- it forces immediate code exploration,
- it fails its core purpose.

Corrective action:

- deepen the structural tree,
- read representative files,
- annotate the tree meaningfully.

## 9. Thin Systems

Bad:

- a system document that names a subsystem but barely explains ownership, interfaces, risks, or partial work,
- every section reduced to one short bullet regardless of subsystem importance.

Why it fails:

- the file exists without carrying enough memory value,
- future readers still need first-pass rediscovery from code,
- the folder looks complete while remaining informationally weak.

Corrective action:

- raise depth where the subsystem has real complexity or change pressure,
- add tables, interface summaries, or flow notes when bullets alone are insufficient.

## 10. Decorative Formatting

Bad:

- adding diagrams, charts, or tables just because they look richer,
- replacing clear prose with visuals that take longer to decode,
- using a single visual format as a hard rule regardless of the information.

Why it fails:

- increases noise rather than clarity,
- makes the document harder to scan,
- confuses style with memory quality.

Corrective action:

- choose the representation that makes the information clearest,
- combine formats only when they support understanding.

## 11. Stale Research References

Bad:

- a research file still says a capability is missing after the repository implemented it,
- a comparison section still reflects an old project constraint that no longer exists,
- `references/` papers are treated as permanent truth even when their repository-specific analysis has drifted.

Why it fails:

- it breaks trust in the memory layer,
- it misleads future design and implementation work,
- it turns durable research into stale folklore.

Corrective action:

- refresh repository-specific sections when implementation reality changes,
- preserve the durable external lessons,
- clearly separate what is still true from what became obsolete.

## 12. Research Hoarding

Bad:

- `references/` accumulates many overlapping papers on the same stable topic,
- a once-useful research folder remains expanded even after the repository has absorbed the decision and a tighter canonical artefact would be easier to maintain,
- upkeep preserves every research slice simply because it exists.

Why it fails:

- readers must scan too many adjacent files,
- overlap pressure rises,
- upkeep becomes additive clutter instead of maintenance.

Corrective action:

- preserve breadth when it still has clear independent value,
- merge or condense only when stable ownership and long-term usability improve,
- keep pruning conservative rather than aggressive.
