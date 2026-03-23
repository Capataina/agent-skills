# Architecture

## Scope / Purpose

- This document defines the current repository structure, subsystem boundaries, dependency direction, and execution flow for Aurix as implemented today.

## Repository Overview

- Aurix is currently a single-screen Tauri desktop application with a React frontend and a Rust backend.
- The implemented product surface is narrower than the root README roadmap and is limited to a WETH/USDC arbitrage-monitoring slice.
- The current system fetches four live Ethereum venue prices plus the current gas price, normalises them in Rust, and derives chart and insight views in the frontend.

## Repository Structure

```text
Aurix/
├── README.md                         # Project intent and long-range roadmap
├── package.json                      # Frontend package manifest and scripts
├── src/
│   ├── main.tsx                      # React entrypoint and global stylesheet loading
│   ├── App.tsx                       # App root; mounts the arbitrage feature page
│   ├── features/
│   │   └── arbitrage/
│   │       ├── ArbitragePage.tsx     # Polling loop, page composition, session history
│   │       ├── api.ts                # Tauri IPC client for market overview reads
│   │       ├── insights.ts           # In-session derived insight and event rules
│   │       ├── types.ts              # Frontend market payload contracts
│   │       └── components/
│   │           ├── PriceCard.tsx     # Primary live market readout
│   │           ├── MarketChart.tsx   # Rolling chart modes and event markers
│   │           └── InsightsPanel.tsx # Live interpretation and recent-event surface
│   └── styles/
│       ├── theme.css                 # Global theme tokens and base element rules
│       └── dashboard.css             # Dashboard layout and component styling
├── src-tauri/
│   ├── Cargo.toml                    # Rust crate manifest
│   ├── tauri.conf.json               # Tauri build and window configuration
│   ├── capabilities/default.json     # Tauri capability manifest for the main window
│   └── src/
│       ├── main.rs                   # Desktop binary entrypoint
│       ├── lib.rs                    # Tauri builder and command registration
│       ├── config.rs                 # Environment and dotenv-backed RPC configuration
│       ├── commands/
│       │   └── market.rs             # IPC boundary for fetching one market overview
│       ├── ethereum/
│       │   └── client.rs             # Read-only Ethereum JSON-RPC transport
│       ├── dex/
│       │   ├── uniswap_v2.rs         # Uniswap V2 and SushiSwap reserve readers
│       │   └── uniswap_v3.rs         # Uniswap V3 slot0 price readers
│       └── market/
│           └── types.rs              # Normalised backend payload models
├── dist/                             # Generated frontend production build output
├── src-tauri/target/                 # Generated Rust build output
└── context/                          # Repository memory layer
```

## Subsystem Responsibilities

- The frontend feature in `src/features/arbitrage/` owns refresh cadence, in-session state, chart-mode selection, and user-facing interpretation.
- The frontend styles in `src/styles/` own the current visual system and dashboard layout.
- The Tauri wiring in `src-tauri/src/lib.rs` owns application startup and IPC command exposure.
- The backend configuration in `src-tauri/src/config.rs` owns RPC endpoint resolution from `MAINNET_RPC_URL` or `ALCHEMY_API_KEY`.
- The Ethereum transport in `src-tauri/src/ethereum/client.rs` owns raw JSON-RPC requests and low-level response decoding.
- The DEX adapters in `src-tauri/src/dex/` own protocol-specific calldata, pool discovery, and price extraction.
- The market models in `src-tauri/src/market/types.rs` own the presentation-ready backend contract returned to the GUI.

## Dependency Direction

- `src/main.tsx` depends on `src/App.tsx`, which depends on the arbitrage feature page.
- `ArbitragePage.tsx` depends on the Tauri IPC client, local analytics helpers, and presentational components.
- Presentational components depend on frontend market types and already-derived state; they do not call the backend directly.
- `commands/market.rs` depends on config, Ethereum transport, DEX adapters, and market model types.
- DEX adapters depend on the shared Ethereum RPC client and shared market output types.
- The RPC client depends on `reqwest` and JSON decoding only, and does not depend on any DEX-specific module.
- Dependency flow is one-way from protocol readers to normalised payloads to frontend rendering; no Rust module depends on frontend concerns.

## Core Execution / Data Flow

- App startup runs the Tauri shell, serves the Vite frontend, and mounts `ArbitragePage`.
- The page performs an immediate `fetch_market_overview` IPC call and then repeats that call every second.
- The backend command loads configuration, constructs one RPC client, and concurrently requests four venue snapshots plus the current gas price.
- The DEX adapters decode protocol-specific state into `PriceSnapshot` values and the command assembles them into one `MarketOverview`.
- The frontend appends each overview to an in-memory rolling history, updates the primary snapshot, and derives chart series and textual insights from that session history.
- The page renders the price card, chart, insights, venue list, and detail panel from the latest overview plus the local history buffer.

## Structural Notes / Current Reality

- The implemented scope is Tab 1 only; Tabs 2 to 5 remain README roadmap items rather than repository reality.
- The app currently supports one hard-coded pair, `WETH / USDC`, across four hard-coded venues.
- Session history is frontend-only and capped to 100 samples; there is no persistence, local database, or restart continuity.
- Failure handling is command-wide rather than venue-specific, so one failing venue currently fails the whole overview request.
- The repository contains generated build artefacts in `dist/` and `src-tauri/target/`, which are not source subsystems but are part of the current tree.
- Build health was verified during context upkeep with `cargo check` and `pnpm build`, both passing on 2026-03-23.
