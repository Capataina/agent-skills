# Runtime Foundation

## Scope / Purpose

- This document tracks the application shell, backend configuration path, shared RPC transport, and shared market payload contract that every live read currently depends on.

## Current Implemented System

- `src/App.tsx` mounts a single arbitrage page and does not yet include any tab navigation or multi-surface routing.
- `src-tauri/src/lib.rs` registers one IPC command, `fetch_market_overview`, and initialises the opener plugin.
- `src-tauri/src/config.rs` resolves Ethereum mainnet access from `MAINNET_RPC_URL` first and falls back to `ALCHEMY_API_KEY`.
- `src-tauri/src/ethereum/client.rs` exposes a reusable read-only JSON-RPC client with `eth_call` and `eth_gasPrice` support.
- `src-tauri/src/market/types.rs` defines the normalised `PriceSnapshot` and `MarketOverview` payloads shared across the Rust and TypeScript boundary.
- `src/features/arbitrage/types.ts` mirrors the backend payload shape for frontend use.

## Implemented Outputs / Artifacts

- `src/main.tsx` provides the React entrypoint and loads the shared stylesheets.
- `src/App.tsx` defines the current single-feature root.
- `src-tauri/src/main.rs` provides the desktop binary entrypoint.
- `src-tauri/src/lib.rs` wires the Tauri runtime and command handler.
- `src-tauri/src/config.rs` provides environment-driven RPC configuration.
- `src-tauri/src/ethereum/client.rs` provides the low-level Ethereum transport.
- `src-tauri/src/market/types.rs` and `src/features/arbitrage/types.ts` define the current cross-boundary market contract.
- `src-tauri/tauri.conf.json` fixes the Tauri dev/build handshake with Vite and defines one 800x600 main window.
- `src-tauri/capabilities/default.json` grants only default core and opener permissions to the main window.

## In Progress / Partially Implemented

- The shared runtime foundation is adequate for one live screen, but it does not yet expose reusable command boundaries for later tabs.
- The payload contract is stable enough for the current screen, but it contains only live snapshot fields and no persistence-oriented metadata.
- The Tauri window configuration still reflects starter defaults more than an application-specific desktop shell.

## Planned / Missing / To Be Changed

- Add shared command boundaries only when another implemented feature needs them rather than mirroring the README roadmap pre-emptively.
- Introduce a persistence layer before treating time-series behaviour as a repository-level shared system.
- Tighten the desktop shell details such as product title and static assets when the UI direction is no longer in rapid flux.
- Add automated tests around configuration fallback and RPC response decoding once the current interfaces stabilise.

## Notes / Design Considerations

- The runtime layer is intentionally read-only and should stay separate from protocol-specific decoding.
- The config layer should continue to hide provider-specific URL construction from the rest of the backend.
- Shared market payloads should remain presentation-ready and protocol-agnostic so later surfaces can consume them without DEX-specific knowledge.
- The current repository has no automated test suite, so build success is the main verified signal for this layer at present.

## Discarded / Obsolete / No Longer Relevant

- The default Tauri greeting scaffold is no longer part of the runtime structure.
- The repository is not currently a generic multi-tab platform despite the README roadmap, so platform abstractions beyond the live market path would be speculative.
