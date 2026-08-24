# 02 — Source index

Owner: SpaceBum9. Only public blobs. SHAs pinned at pack stamp.

## MCT-2600027 — `c9f7dbf2ca3cb53136db419de4a0a7d3b7005cf4` · 57 files

Key files: `FLUID_MEMORY_SNAPSHOT.md`, `temporal-register.ts`, `skills/mct-2600027-core/SKILL.md`, `core/trace_id.py`, `core/trace_treue.py`, `core/collision_handler.py`, `core/orchestrator.py`, `border/protocol.py`, `dual_pol/hal.py`, `dual_pol/zero_telepath.py`, `skills/hold-index.json`.

https://github.com/SpaceBum9/MCT-2600027

## MCT-1700021 — `09b2bee1bcf9b9ebec04f6ffb80016d0b1dd4ce7` · 87 files

HOLD suite, `ethics/garas-sos-v3.json`, `skills/hold-manifest.json`, traces latest `MCT-1700021-TR-20260823-1117Z`.

https://github.com/SpaceBum9/MCT-1700021

## MCT-2600027-CMD — `7769032ee0182be77f35b1aa2c22bf1e88ef5edd` · 24 files

https://github.com/SpaceBum9/MCT-2600027/tree/main/apps/cmd

## MCP connectors — `1ed8b52490b138680a0df0f162fb0b47102ae3be` · 7 files

`mcp_connectors.py` — symbolic GPT / Gemini / Google / Siri fusion. No tokens.

## How Gemini should load source

Prefer GitHub get_tree + get_file_contents on the pinned SHA.
Do not dump entire `traces/` into context. Do not fetch private HOLD repos.
