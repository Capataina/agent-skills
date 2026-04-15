# Cross-System Analysis

## Table of Contents

1. [Purpose](#purpose)
2. [Inter-System Relationship Mapping](#inter-system-relationship-mapping)
3. [Bridge System Identification](#bridge-system-identification)
4. [Dependency Chain Tracing](#dependency-chain-tracing)
5. [Cross-Cutting Concerns Documentation](#cross-cutting-concerns-documentation)
6. [Connection Discovery Methodology](#connection-discovery-methodology)
7. [Surprising Connections](#surprising-connections)
8. [Knowledge Gaps Identification](#knowledge-gaps-identification)
9. [Hub and Hotspot Identification](#hub-and-hotspot-identification)
10. [Cohesion and Coupling Analysis](#cohesion-and-coupling-analysis)

## Purpose

This reference covers how to analyze and document relationships that span multiple systems during context upkeep. Individual system files describe what each subsystem does. Architecture files describe overall shape and dependency direction. Cross-system analysis fills the space between those two levels — the connective tissue, the hidden dependencies, the shared patterns, the gaps where no documentation exists.

Read this file when upkeep work reveals non-trivial interactions between systems, when the codebase is large enough that relationships between subsystems are not self-evident, or when the user explicitly asks for dependency analysis, coupling review, or knowledge gap identification.

Not every project needs every technique described here. A focused single-purpose tool with three source files does not benefit from hub analysis or bridge identification. A distributed platform with a dozen interacting services benefits from most of them. Apply judgment about which techniques add value given the repository's actual complexity.

## Inter-System Relationship Mapping

### What it is

Identifying and documenting the data flows, event chains, dependency cascades, and shared state between systems. The goal is to go beyond "A depends on B" and describe the shape of the dependency — what data moves, what transformations happen along the way, and what failure modes the connection introduces.

### Why it matters

A flat dependency list tells a reader that `orders` depends on `inventory`. It does not tell them that `orders` reads current stock levels synchronously during checkout, that a failed inventory check blocks the entire order flow, or that `inventory` publishes stock-change events that `orders` consumes asynchronously for display purposes. Those details determine what breaks when something changes and how confidently an engineer can modify one system without inspecting the other.

When relationships are documented with their shape and data content, future work can assess blast radius without re-tracing every connection from code.

### How to do it

Start from observable evidence in the codebase:

- **Imports and call sites.** Which modules import from which other modules? Are the imports for types only, for function calls, or for shared mutable state?
- **Data flow direction.** Does data flow one way (A sends to B) or bidirectionally (A and B exchange)? Is it synchronous or asynchronous? Is it request-response, event-driven, or shared-state?
- **Transformation points.** Where does data change shape between systems? A raw database row becomes a domain object becomes a serialised API response — each transformation is a potential failure point and a coupling surface.
- **Failure propagation.** If system A becomes unavailable, what happens to system B? Does B fail immediately, degrade gracefully, or continue unaffected? Does A's failure cascade further through B to systems C and D?

### What to document

Relationship mappings belong in `architecture.md` when they describe major structural flows, or in the relevant `systems/*.md` file when they describe a specific subsystem's outward connections. Use the format that conveys the information clearest — a table for comparable relationships across multiple systems, a diagram for flows with branching or feedback, prose for nuanced failure semantics.

A relationship entry should capture:

- the two systems involved,
- what data or control flows between them,
- the direction and mechanism (call, event, shared state, config, file),
- what transforms happen at the boundary,
- what breaks if the connection fails.

### When to skip

Simple projects where every module's dependencies are obvious from a single import block do not need formal relationship mapping. If a reader can see the full dependency picture from the architecture tree and a quick scan of system files, the mapping adds overhead without insight. Apply this technique when the relationships are non-obvious, numerous, or carry important failure semantics.

## Bridge System Identification

### What it is

Finding modules or services that connect otherwise separate clusters of functionality. A bridge system is one that, if removed or changed, would disconnect parts of the codebase that currently interact through it.

### Why it matters

Bridge systems are the highest-risk change points in a codebase. They sit between clusters, so changes to them ripple in multiple directions simultaneously. They are often not the most depended-on modules (hubs handle that), but they are the most structurally critical because they are the only path between groups of functionality.

Engineers naturally focus on the systems they are changing and the systems those directly depend on. Bridge systems cause problems precisely because they affect systems that seem unrelated — the blast radius is wider than intuition suggests.

### How to identify them

Look for modules that:

- are imported by systems that otherwise share no dependencies,
- translate between two different data models or protocols,
- sit at the boundary between two architectural layers that do not otherwise communicate,
- are the only module that references two otherwise independent subsystems,
- serve as adapters, translators, or mediators between different parts of the system.

Common shapes of bridge systems:

- **API gateways** that route between otherwise independent backend services.
- **Event buses or message brokers** that decouple producers from consumers.
- **Shared utility modules** that provide common abstractions used across unrelated subsystems.
- **Data transformation layers** that convert between internal and external representations.
- **Configuration systems** that parameterise behaviour across otherwise independent modules.

### What to document

When a bridge system is identified, document it in the owning system file with explicit mention of which clusters it connects and what would happen if it changed. In `architecture.md`, note the bridge role in the dependency or structural overview so the reader understands the structural importance without needing to trace it themselves.

The key information is:

- which otherwise-separate parts of the system does this bridge connect,
- what data or control passes through the bridge,
- what is the blast radius of changes to the bridge,
- are there alternative paths if the bridge fails or is removed.

### When to skip

Small codebases where every module directly interacts with most other modules do not have meaningful bridge structure — everything is already connected. Bridge analysis adds value when the codebase has natural clusters of functionality that interact through narrow interfaces.

## Dependency Chain Tracing

### What it is

Following critical paths end-to-end through the system to understand the full sequence of modules, transformations, and failure points that a request, event, or data item passes through.

### Why it matters

Individual system files describe their own boundaries and interfaces. Dependency chain tracing reveals the emergent behaviour that arises when those systems are composed. The longest dependency chain in a system often determines its latency characteristics, its most fragile failure paths, and the minimum set of systems that must be functioning for a critical operation to succeed.

Understanding the full chain also reveals which interface changes are truly local and which propagate. Changing a return type in system A may seem contained, but if systems B, C, and D all consume that type through a chain of intermediaries, the real blast radius is much larger than A's direct dependents suggest.

### How to do it

Pick the critical operations or data flows that matter most to the project — the ones that cross the most boundaries, carry the most risk, or are the hardest to reason about. For each one:

- **Trace the full path.** Start from the entry point (user action, API call, scheduled job, event) and follow the execution or data flow through every system it touches until it reaches its final effect (database write, response, side effect, output).
- **Note every boundary crossing.** Each time the flow moves from one system to another, that is a coupling point and a potential failure point.
- **Identify the longest chain.** The longest dependency chain in the system is the one most likely to cause latency issues, the hardest to debug, and the most sensitive to changes anywhere along its length.
- **Assess blast radius.** For each system in the chain, ask: if I change this system's interface, which other systems in the chain need to change? If this system fails, does the entire chain fail or can parts of it degrade gracefully?

### What to document

End-to-end chains belong in `architecture.md` when they represent the major flows of the system. Subsystem-specific chains belong in the relevant `systems/*.md` file. Use diagrams or ordered lists to make the sequence clear — readers should be able to follow the path without mentally reconstructing it.

Document:

- the entry point and final effect,
- every system touched along the way,
- the data shape at each boundary crossing,
- the failure behaviour at each step (fail-fast, retry, degrade, ignore),
- the total length of the chain and which segments are synchronous versus asynchronous.

### When to skip

Projects with flat architectures where most operations touch one or two modules do not have meaningful dependency chains. This technique adds value when operations cross three or more system boundaries, especially when the intermediate systems are not obvious from the entry point.

## Cross-Cutting Concerns Documentation

### What it is

Identifying and documenting patterns, conventions, failure modes, data structures, and configuration approaches that span multiple systems but do not belong to any single one.

### Why it matters

Cross-cutting concerns are the patterns that every system follows but no system owns. Error handling conventions, logging formats, authentication flows, configuration loading patterns, serialisation standards — these live everywhere and nowhere. In a typical `context/` structure, they are too broad for any single system file and too specific for `architecture.md`.

When cross-cutting concerns are undocumented, each system implements its own variation. When they are documented only in one system file, readers miss that the pattern applies broadly. When they are documented in `architecture.md`, they bloat the structural overview with implementation detail.

### Where to document them

Cross-cutting concerns that represent project conventions or design decisions fit naturally in `notes/` files — for example, `notes/error-handling-conventions.md` or `notes/configuration-patterns.md`. They are project knowledge that shapes future work, which is exactly what `notes/` is for.

Cross-cutting concerns that are more structural — the authentication flow that every service participates in, the event schema that every producer must follow — may warrant a dedicated system file if they have enough substance, or a section in `architecture.md` if they are brief.

The key principle is canonical ownership: pick one home for each cross-cutting concern and reference it from the system files that participate in it.

### What to look for

Common categories of cross-cutting concerns:

- **Error handling patterns.** How do systems report errors? Is there a shared error type? Do all systems follow the same retry logic or is it ad-hoc?
- **Logging and observability conventions.** Shared log formats, trace ID propagation, metric naming patterns.
- **Authentication and authorisation flow.** How does identity propagate through the system? Which systems verify credentials and which trust upstream assertions?
- **Configuration loading patterns.** Environment variables, config files, feature flags — is there a shared approach or does each system load config independently?
- **Data serialisation standards.** JSON conventions, protobuf schemas, shared type definitions that multiple systems import.
- **Testing conventions.** Shared fixtures, test database setup, integration test patterns that span system boundaries.

### When to skip

Projects where each system is genuinely independent and shares no conventions do not benefit from cross-cutting concern documentation. This technique adds value when you notice the same pattern implemented in three or more systems — that pattern deserves a canonical description somewhere.

## Connection Discovery Methodology

### What it is

A structured approach to actively looking for relationships between systems during upkeep, rather than only documenting relationships that are already obvious. This is the investigative work that turns a collection of independent system descriptions into a connected understanding of the codebase.

### Why it matters

Obvious connections — direct imports, explicit API calls, documented dependencies — are easy to find and usually already reflected in system files. The connections that cause the most trouble are the ones nobody documented because nobody noticed them. Shared data structures that two systems both define independently. Configuration keys that affect behaviour in multiple places. Parallel evolution where two subsystems solved the same problem in different ways.

Active discovery during upkeep is the mechanism for catching these before they cause problems.

### How to do it during upkeep

During the upkeep workflow, after updating individual system files and before finalising the pass, actively investigate connections:

**Shared data structures.** Look for types, schemas, or data shapes that appear in multiple systems. Are they shared through a common definition, or has each system defined its own version? If they are independent copies, are they still in sync? Divergence between parallel definitions is a common source of subtle bugs.

**Shared configuration.** Look for configuration keys, environment variables, or feature flags that affect behaviour in more than one system. A config change that seems local to one system may silently change behaviour in another. Document which systems are affected by shared config.

**Parallel evolution.** Look for systems that have independently developed similar solutions to the same problem. Two different caching layers, two different retry mechanisms, two different logging wrappers. These may be intentional (different requirements justified different approaches) or accidental (the developers did not know about each other's work). Either way, documenting the parallel implementations prevents future confusion.

**Hidden coupling through global state.** Look for shared mutable state — global variables, shared database tables, shared files, shared caches — that creates coupling between systems without any explicit import or call. Two systems that both read and write the same database table are tightly coupled even if neither imports the other.

**Event or message consumers.** In event-driven architectures, trace which systems produce events and which consume them. The producer-consumer relationship may not be visible from either system's imports — the coupling exists through the event infrastructure rather than through direct code references.

**Common external dependencies.** Systems that depend on the same external service or API are coupled through that dependency even if they are otherwise independent. If the external service changes its interface, all dependent systems are affected simultaneously.

### What to produce

Connection discovery should result in updates to existing documentation rather than a separate "connections" file. Update `architecture.md` with newly discovered structural relationships. Update relevant `systems/*.md` files with outward connections. If a cross-cutting concern emerges, create or update the appropriate `notes/` file.

When the discovered connections are significant enough to change a reader's mental model of the system, note them explicitly. A brief statement like "orders and recommendations both maintain independent copies of the product schema — these are not synchronised and may diverge" is more valuable than a hundred lines of obvious import-based dependency documentation.

### When to skip

Connection discovery is investigative work with diminishing returns. In a small project where you have already read every file, the connections are already known. In a well-documented project where system files already describe their outward connections accurately, active discovery may not surface anything new. Invest time in discovery proportional to the project's complexity and the staleness of its documentation.

## Surprising Connections

### What it is

Identifying and documenting relationships between systems that are non-obvious — connections that a competent engineer reading the code might miss on a first pass, or that would cause unexpected behaviour when one system changes.

### Why it matters

Obvious dependencies are manageable. An engineer changing system A checks its direct dependents and updates them. Surprising connections are the ones that cause incidents: the config change that broke an unrelated service, the database migration that silently changed another team's query results, the shared utility function whose behaviour change rippled through twelve call sites in six different modules.

Documenting surprising connections converts them from hidden landmines into known risks. The connection still exists, but now future engineers know to check it.

### Categories of surprising connections

**Hidden coupling through shared configuration.** Two systems that read the same config key are coupled through that key, but neither system's code references the other. Changing the config value affects both, and the second system's behaviour change may not be tested or even noticed.

**Parallel implementations.** Two systems that independently implement the same algorithm, data structure, or protocol. They may have diverged over time, leading to subtle behavioural differences. Or they may be candidates for consolidation — but only if the consolidation is intentional and tested.

**Transitive dependencies.** System A depends on system B, which depends on system C. If C changes its interface, A breaks even though A has no direct relationship with C. The longer the transitive chain, the more surprising the breakage.

**Shared mutable state.** Two systems that read and write the same database table, file, or cache entry without explicit coordination. Changes to the data layout or access patterns in one system can corrupt or invalidate the other system's assumptions.

**Semantic coupling.** Two systems that depend on the same implicit assumption — for example, that IDs are always positive integers, that timestamps are always UTC, or that a particular field is never null. The assumption is not enforced anywhere; it is just something both systems rely on. When the assumption is violated, both systems fail in ways that are hard to diagnose.

**Timing dependencies.** Systems that depend on the order in which they execute — system A must run before system B, or system B's output is incorrect. If the timing dependency is not documented, changes to scheduling or concurrency can introduce subtle bugs.

### How to document them

Surprising connections should be documented in the system file of the system most likely to be changed — that is where the engineer will look before making modifications. A brief, specific statement is more valuable than an elaborate analysis:

> The `pricing` module reads the `TAX_RATE` environment variable, which is also read by `invoicing`. Changing this value affects both invoice generation and real-time price display, but the two systems are not tested together.

If the surprising connection is structural — affecting the overall architecture rather than a specific subsystem — document it in `architecture.md` in the dependency or risk section.

### When to skip

Do not manufacture surprising connections where none exist. If the codebase is straightforward and dependencies are explicit, there may be few or no surprising connections to document. This technique adds value when the codebase has significant implicit coupling, shared state, or configuration-driven behaviour.

## Knowledge Gaps Identification

### What it is

Documenting what is poorly understood, isolated, uninspected, or under-documented in the codebase. Making the absence of knowledge explicit rather than letting it remain invisible.

### Why it matters

A `context/` folder that documents only what was inspected creates a false sense of completeness. If five systems are well-documented and three were never looked at, a reader may assume the three undocumented systems are unimportant or trivial. In reality, they may be critical systems that nobody has examined yet.

Explicit knowledge gaps serve two purposes: they prevent false confidence, and they create a natural priority list for future upkeep work. When gaps are visible, they can be addressed. When gaps are invisible, they are discovered only when something breaks.

### What to look for

**Uninspected areas.** During upkeep, track which parts of the codebase were actually examined and which were not. Directories that were skipped, modules that were noted but not read, subsystems that were described based on names and file structure alone rather than actual code inspection.

**Shallow documentation.** System files that exist but are thin — they name the subsystem and its general purpose but do not describe interfaces, data flow, failure modes, or active risks. A system file that says "handles user authentication" without explaining how is documenting the existence of a system, not the knowledge needed to work with it.

**Isolated modules.** Parts of the codebase that no system file references and no architecture section mentions. These may be dead code, legacy modules, utility libraries, or genuinely important systems that fell through the documentation cracks.

**Stale documentation.** System files whose descriptions no longer match the code. A stale system file is arguably worse than no system file — it actively misleads. When staleness is detected but the correct current state is not yet understood, marking the file as stale is more honest than leaving it as-is.

**Missing cross-references.** Systems that clearly interact (based on imports or shared data) but whose system files do not mention each other. The relationship exists in code but not in documentation.

### How to document gaps

Gaps can be documented in several places depending on their scope:

- **In `architecture.md`**, a brief section noting which areas of the codebase are not yet covered by system files or were not inspected during the current upkeep pass.
- **In individual system files**, a note when a subsystem's documentation is based on inference rather than thorough inspection — for example, "this description is based on file structure and naming; the internal logic has not been inspected."
- **In `notes.md` or a `notes/` file**, if the gaps represent a broader project concern — for example, "the entire legacy API layer is undocumented and poorly understood."

The important thing is that gaps are stated rather than hidden. A reader should be able to distinguish "this area was examined and found to be simple" from "this area was not examined."

### When to skip

Very small projects where the entire codebase was inspected during upkeep have no meaningful knowledge gaps to document. This technique adds value when the codebase is large enough that upkeep necessarily involves prioritising which areas to inspect deeply and which to defer.

## Hub and Hotspot Identification

### What it is

Finding the most-depended-on modules in the codebase — the files imported by everything, the functions called from everywhere, the types that appear in every system's interface. These are the hubs of the dependency graph.

### Why it matters

Hubs are the highest-impact change points. A change to a hub module affects every system that depends on it. Understanding which modules are hubs tells engineers where to be most careful, where to write the most tests, and where interface changes will be most expensive.

Hubs are also the best entry points for understanding a codebase. If one module is imported by fifteen others, understanding that module first provides context for everything that depends on it. Documenting hubs in `architecture.md` gives new readers a natural starting point.

Beyond structural hubs, hotspots are areas where change activity concentrates — files that are modified frequently, modules where bugs cluster, interfaces that keep getting extended. Hotspots indicate areas that may need refactoring or where the current abstraction is not stable.

### How to identify them

**Import frequency.** Which modules are imported by the most other modules? Look at the import graph across the codebase. Modules imported by many others are structural hubs.

**Type usage.** Which types, interfaces, or data structures appear in the most function signatures, return types, or data flows? Widely-used types are coupling surfaces — changing them propagates broadly.

**Call frequency.** Which functions or methods are called from the most diverse locations? Utility functions called from everywhere are hubs even if their owning module is not heavily imported.

**File change frequency.** If version control history is available, which files change most often? Files with high churn may indicate unstable abstractions, accumulating responsibilities, or areas under active development pressure.

**Bug concentration.** If issue tracking or commit messages reference specific modules frequently, those modules may be hotspots — areas where the current implementation is fragile or poorly understood.

### What to document

Hub identification results belong primarily in `architecture.md`, in the dependency or structural overview section. A brief inventory of the most-depended-on modules, what they provide, and why they are central gives readers an immediate sense of the codebase's structure.

For each identified hub, document:

- what it provides (types, functions, services, configuration),
- approximately how many systems depend on it,
- what the impact of changing its interface would be,
- whether it is a stable abstraction or an area of active change.

If a hub module has its own system file, note its hub status there as well — the engineer maintaining that module should understand that changes ripple broadly.

### When to skip

Projects with flat dependency structures — where no module is significantly more depended-on than any other — do not have meaningful hubs. This technique adds value when the dependency graph has clear concentration points, or when the codebase is large enough that understanding which modules are central saves significant exploration time.

## Cohesion and Coupling Analysis

### What it is

Describing which parts of the codebase are tightly coupled (change together, share data, depend on each other's internals) versus loosely coupled (interact through narrow interfaces, change independently, can be understood in isolation). Identifying the natural seams where the codebase divides into independent units, and the areas where coupling is unexpectedly high or suspiciously absent.

### Why it matters

Cohesion and coupling determine how safely and efficiently the codebase can be modified. Tightly coupled systems must be changed together — modifying one without updating the other introduces bugs. Loosely coupled systems can be changed independently — an engineer can work on one without understanding the other in detail.

Understanding coupling patterns helps with:

- **Change planning.** If systems A and B are tightly coupled, any plan that changes A should budget time for updating B.
- **Team organisation.** Tightly coupled systems should ideally be owned by the same team or at least coordinated closely.
- **Refactoring prioritisation.** Unexpectedly high coupling between systems that should be independent is a sign that an abstraction boundary is missing or leaking.
- **Risk assessment.** Tightly coupled areas are higher risk — a bug in one system can manifest as incorrect behaviour in its coupled partner.

### How to assess

**Shared data structures.** Systems that share complex data types or schemas are tightly coupled through those types. Changes to the shared type propagate to all users. The more complex the shared type, the tighter the coupling.

**Interface width.** Systems that interact through a narrow, stable interface (a few well-defined function calls or a versioned API) are loosely coupled. Systems that interact through broad, evolving interfaces (many function calls, direct access to internal data structures, shared mutable state) are tightly coupled.

**Change correlation.** Systems that historically change together in the same commits or pull requests are likely tightly coupled — even if the coupling is not obvious from the code structure alone. If modifying module A always requires a corresponding change to module B, the coupling is real regardless of what the import graph says.

**Internal cohesion.** Within a single system, cohesion measures whether the module's parts belong together. A module where every function operates on the same data, serves the same purpose, and would be affected by the same changes is highly cohesive. A module that contains unrelated utility functions grouped by convenience rather than purpose is low cohesion.

### What to document

Coupling analysis results belong in `architecture.md` when they describe the overall structure — which clusters are tightly coupled, where the natural seams are, which boundaries are clean and which are leaky.

Consider documenting:

- **Natural seams.** Where does the codebase divide into groups that can be understood and modified independently? These are the clean architectural boundaries.
- **Unexpectedly high coupling.** Where are two systems more entangled than their responsibilities suggest? This may indicate a missing abstraction, a leaky interface, or organic growth that has not been refactored.
- **Suspiciously absent coupling.** Where would you expect two systems to interact but they do not? This may indicate duplicated logic, missed integration, or a deliberate design decision worth documenting.
- **Coupling through side channels.** Where are systems coupled through something other than direct code dependencies — shared database tables, shared config, shared file system paths, timing assumptions?

A simple coupling summary can be a table in `architecture.md`:

| System A | System B | Coupling | Mechanism | Risk |
| --- | --- | --- | --- | --- |
| orders | inventory | tight | shared DB table, sync calls | changes to inventory schema break order processing |
| auth | user-profile | loose | narrow token interface | can evolve independently |
| billing | notifications | hidden | shared config key `CURRENCY` | config change affects both silently |

### When to skip

Projects where coupling is obvious from the architecture — a simple layered application where each layer depends only on the layer below — do not need formal coupling analysis. This technique adds value when the codebase has grown organically, when coupling is not obvious from the module structure, or when there are known pain points around changes that ripple unexpectedly.
