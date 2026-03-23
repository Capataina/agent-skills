# Arbitrage Analytics

## Scope / Purpose

- This document tracks the in-session analytical layer for the implemented arbitrage screen, including rolling history, chart calculations, gas-adjusted estimates, and derived insight rules.

## Current Implemented System

- `src/features/arbitrage/ArbitragePage.tsx` maintains a rolling in-memory history of the last 100 market overviews.
- `src/features/arbitrage/components/MarketChart.tsx` derives four mutually exclusive chart modes: raw prices, median-relative deviation, absolute venue spread, and a simple gas-adjusted estimate.
- The chart can optionally mark points where the simple gas-adjusted estimate is positive.
- `src/features/arbitrage/insights.ts` derives one primary insight, up to four secondary insight cards, and a short recent-event list from the same in-session history.
- The insight rules currently evaluate venue ordering, spread trend, median-relative deviation, gas-adjusted state, persistence length, and a shallow-history caution case.
- `ArbitragePage.tsx` also computes summary metrics for the detail panel, including current spread, median price, and net spread estimate.

## Implemented Outputs / Artifacts

- `src/features/arbitrage/ArbitragePage.tsx` owns the history buffer and summary metric derivation.
- `src/features/arbitrage/components/MarketChart.tsx` owns the current chart calculations and SVG rendering inputs.
- `src/features/arbitrage/insights.ts` owns the rule-based interpretation logic.
- `src/features/arbitrage/components/InsightsPanel.tsx` renders the derived insights and event feed.

## In Progress / Partially Implemented

- The analytics are deterministic and inspectable, but they still live in frontend feature code rather than a reusable shared core.
- The gas-adjusted estimate uses a fixed 220,000 gas-unit assumption and should not be treated as execution-grade profitability logic.
- Baselines, persistence rules, and event transitions are session-scoped only because there is no persisted history.
- The chart and insight layers both derive related metrics separately, so some analytical logic is duplicated across files.

## Planned / Missing / To Be Changed

- Extract shared analytical primitives so charting, detail metrics, and insights stop re-deriving the same concepts independently.
- Add persisted historical analytics before adding claims about long-run baselines, opportunity frequency, or restart continuity.
- Add configurable thresholds and richer event classification only after the current signals are validated against longer-lived data.
- Add tests around median, spread, deviation, and persistence rules once the analytical surface stops shifting structurally.

## Notes / Design Considerations

- Raw prices are supporting context; spread, deviation, venue ranking, and gas-adjusted interpretation are the main analytical story.
- The insight layer is intentionally conservative in wording and should stay interpretive rather than prescriptive.
- Event markers currently indicate positive simple net estimates only, so they are signal hints rather than a complete opportunity model.
- The current analytics answer questions about relative venue state, not execution feasibility or trade path optimisation.

## Discarded / Obsolete / No Longer Relevant

- Treating raw price alone as the complete Tab 1 analytical product is no longer current.
- Treating the current gas-adjusted estimate as a persisted opportunity log or execution model is not supported by the codebase.
