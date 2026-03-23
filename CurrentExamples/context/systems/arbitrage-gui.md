# Arbitrage GUI

## Scope / Purpose

- This document tracks the current desktop presentation layer for the implemented arbitrage screen, including page composition, component boundaries, and the shared visual system.

## Current Implemented System

- `src/App.tsx` renders a single full-screen arbitrage page with no routing or cross-tab navigation.
- `src/features/arbitrage/ArbitragePage.tsx` composes the top bar, hero price-and-chart surface, insights panel, venue list, and detail panel.
- `src/features/arbitrage/components/PriceCard.tsx` presents the primary venue snapshot, gas readout, refresh state, and error banner.
- `src/features/arbitrage/components/MarketChart.tsx` renders the chart controls, SVG plot, legend, and optional event markers.
- `src/features/arbitrage/components/InsightsPanel.tsx` renders the live interpretation cards and recent event feed.
- `src/styles/theme.css` and `src/styles/dashboard.css` provide the current dark dashboard look, layout grid, colour tokens, and responsive behaviour.

## Implemented Outputs / Artifacts

- `src/App.tsx` provides the single-screen app root.
- `src/features/arbitrage/ArbitragePage.tsx` provides the current page composition.
- `src/features/arbitrage/components/PriceCard.tsx` provides the hero-side readout.
- `src/features/arbitrage/components/MarketChart.tsx` provides the main visual monitoring surface.
- `src/features/arbitrage/components/InsightsPanel.tsx` provides the textual interpretation surface.
- `src/styles/theme.css` and `src/styles/dashboard.css` provide the shared CSS system.
- `index.html` still carries the default `Tauri + React + Typescript` page title and Vite favicon reference.

## In Progress / Partially Implemented

- The visual direction is coherent for one screen, but the desktop shell polish is incomplete because the HTML title and favicon still use starter defaults.
- The GUI supports responsive layout collapse, but it remains a single-page monitor rather than a broader product shell.
- The chart surface is feature-complete enough to use, but readability and behavioural refinement are still active concerns in the code comments and layout choices.
- Refresh errors are shown to the user, but the surface does not yet expose per-venue status, stale-state indicators, or connection diagnostics.

## Planned / Missing / To Be Changed

- Replace the remaining starter metadata in `index.html` when the product shell is treated as part of the implementation rather than scaffolding.
- Add broader navigation and layout framing only when a second implemented feature exists in the repository.
- Add richer historical and operational panels only after persistence and more trustworthy event modelling exist.
- Add clearer source-health indicators once backend fetches can fail independently by venue.

## Notes / Design Considerations

- The GUI is chart-first and uses compact supporting copy rather than text-heavy dashboards.
- Styling is centralised in plain CSS rather than utility-heavy component markup, which keeps the current look coherent but couples many components to the same stylesheet.
- The current screen is designed for monitoring and interpretation rather than order entry or wallet interaction.
- The Tauri window is fixed to a relatively small default size, so dense layout decisions need to remain readable under that constraint.

## Discarded / Obsolete / No Longer Relevant

- The default Tauri greeting UI is obsolete.
- Any assumption that the repository already contains a multi-tab desktop shell is obsolete because the implemented GUI is still one arbitrage page.
