# Anti-Patterns

This reference names the common failure modes that make a `context/` folder noisy, unstable, or misleading.

## 1. Milestone Slicing

Bad:

- `MILESTONE_1.md`
- `PHASE_2.md`
- `SPRINT_4_NOTES.md`

Why it fails:

- later milestones restate earlier reality,
- information duplicates instead of moving to a canonical home,
- readers must reconstruct the present from historical slices,
- upkeep becomes additive clutter instead of maintenance.

Corrective action:

- reorganise by subsystem or feature ownership,
- move durable content into `systems/` files,
- delete the milestone files once their useful content has a home.

## 2. Diary History

Bad:

- `HISTORY.md`
- `RECENT_CHANGES.md`
- “today we did X” sections

Why it fails:

- grows without bound,
- preserves chronology instead of current truth,
- hides durable lessons inside timestamped narrative.

Corrective action:

- keep only durable lessons,
- attach them to the owning subsystem in `Durable Notes / Discarded Approaches`.

## 3. Duplicate Ownership

Bad:

- analytics described fully in both `systems/analytics.md` and `systems/telemetry.md`,
- reward logic described fully in both game and training docs,
- architecture repeating large chunks of system-doc reality.

Why it fails:

- updates drift,
- contradictory truth appears,
- readers do not know which file owns the topic.

Corrective action:

- pick one canonical home,
- trim the neighbouring file to interface-level mention only.

## 4. Vague Catch-All Files

Bad:

- `MISC.md`
- `NOTES.md`
- `GENERAL_SYSTEMS.md`

Why it fails:

- no stable scope,
- no canonical ownership,
- high overlap pressure,
- tends to accumulate uncurated leftovers.

Corrective action:

- redistribute content into proper system docs,
- delete the catch-all file.

## 9. Dumping-Ground Decisions and References

Bad:

- `decisions/misc.md`
- `references/random-research.md`
- folders filled with lightly curated scraps that have no clear reuse value

Why it fails:

- the role boundary collapses,
- research becomes hard to revisit,
- cross-cutting decisions become untrustworthy,
- the folder turns into storage instead of memory.

Corrective action:

- create decision and reference files only when they have a durable, specific role,
- name them by subject,
- delete or merge scraps that have no lasting value.

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

- “Current Implemented System” describes things not actually implemented,
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
- no execution/data flow,
- no one-line descriptions.

Why it fails:

- it does not orient the reader,
- it forces immediate code exploration,
- it fails its core purpose.

Corrective action:

- deepen the structural tree,
- read representative files,
- annotate the tree meaningfully.
