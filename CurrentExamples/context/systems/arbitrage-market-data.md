# Arbitrage Market Data

## Scope / Purpose

- This document tracks the live market-ingestion path for the implemented arbitrage screen, including venue reads, gas reads, protocol decoding, and command assembly.

## Current Implemented System

- The backend reads four live Ethereum mainnet WETH/USDC venues on each refresh tick.
- `src-tauri/src/dex/uniswap_v3.rs` reads the Uniswap V3 5 bps and 30 bps pools through `slot0()` and derives spot price from `sqrtPriceX96`.
- `src-tauri/src/dex/uniswap_v2.rs` resolves the canonical Uniswap V2 and SushiSwap pairs from their factories and derives price from reserves.
- `src-tauri/src/commands/market.rs` fetches all four venue snapshots and the current gas price concurrently with `tokio::join!`.
- The command returns one `MarketOverview` containing a shared timestamp, pair label, gas price, and the venue snapshot list.

## Implemented Outputs / Artifacts

- `src-tauri/src/commands/market.rs` exposes the `fetch_market_overview` IPC command.
- `src-tauri/src/dex/uniswap_v3.rs` provides the two Uniswap V3 pool readers.
- `src-tauri/src/dex/uniswap_v2.rs` provides the Uniswap V2 and SushiSwap readers.
- `src-tauri/src/ethereum/client.rs` provides the `eth_call` and gas-price reads those adapters depend on.
- `src-tauri/src/market/types.rs` provides the normalised output model returned to the frontend.

## In Progress / Partially Implemented

- The venue set is broader than the first README milestone, but it is still fixed to one pair and one chain.
- The command fetches venues concurrently, but it does not yet degrade gracefully when one venue is stale or unavailable.
- The current timestamp comes from local system time within each adapter rather than a shared command-level capture.
- The current gas estimate is a single live price and does not yet include fee history or more nuanced execution modelling.

## Planned / Missing / To Be Changed

- Add per-venue error handling so one broken source does not blank the whole market overview.
- Add local snapshot persistence before claiming historical market data support.
- Add pair configurability only after the hard-coded WETH/USDC path is validated and the normalised model remains trustworthy.
- Add more venues only when the comparison remains genuinely like-for-like and protocol decoding stays auditable.

## Notes / Design Considerations

- Price correctness matters more than venue count because the app is analytical rather than decorative.
- Uniswap V2-style readers and Uniswap V3 readers should remain separate because their decoding and failure modes differ.
- The current market overview is a transport object, not a persistence schema or opportunity log.
- The backend performs read-only chain access and does not submit transactions or mutate on-chain state.

## Discarded / Obsolete / No Longer Relevant

- The earlier single-venue-only implementation state is no longer current.
- Any assumption that milestone 1.2 persistence already exists is obsolete because no local market-history store is present in the codebase.
