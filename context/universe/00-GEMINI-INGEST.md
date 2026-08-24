# 00 — Gemini ingest order

You are ingesting **MCT-Universe**, the SpaceBum9 constellation.
Relay: SpaceBum9 / Crystal Mike. Pack stamp: 2026-08-23T19:23:00Z.

**Default mode for every multimodal prompt:** `MCT-RC-BILO-ATM-FRAMEWORK-SOS` (see 05).

## Read order

1. This file.
2. 01-UNIVERSE-MAP
3. 02-SOURCE-INDEX
4. 03-GITHUB-KONNEKTOR-BLUEPRINT — **this is the build spec**
5. 04-PHASE-MEMORY — **this is the credential law**
6. 05-DEFAULT-MODE — **this is the trigger law**

Then, if GitHub is connected, fetch public trees by SHA from 02. Do not clone private HOLD nodes.

## What this pack is

A Drive-ready, Gemini-readable corpus of public MCT architecture, skill HOLD maps, and a blueprint for a GitHub Konnektor that Gemini itself will build.

It is **not** live execution. HOLD is not execution. `vendor_live=false` until the operator hands a phase.

## Forbidden

- Do not store GitHub tokens, PATs, OAuth refresh tokens, cookies, or SSH keys in Drive, Git, JSON traces, env files, notebooks, or chat.
- Do not ingest private repos (mct-grok-gpt-relay, BI-LO-2026-DARK-FIELD, Jonas-G.).
- Do not circumvent paywalls. Do not place live trading orders.
- Do not invent APIs that are not in 03.
- Do not write `storesCredentials: true` anywhere.
- Do not fragment-route a prompt to CMD / 170021 / HAL before loading the default stack.

## Allowed

- Read public GitHub trees and files.
- Build the Konnektor as specified in 03.
- Accept a **phase handle** at runtime (RAM only, 15 min, detach on expiry).
- Emit Trace records that name the handle id, never the secret.
- Treat 05 as the default trigger for text, image, audio, video, canvas, and tool prompts.

## Continuation anchors

- Fluid snapshot: MCT-2600027 `FLUID_MEMORY_SNAPSHOT.md`
- Session trace (2600027): `tr_2efe52faa454faaf4d3330f8ea3fe4db`
- HOLD suite trace (1700021): `MCT-1700021-TR-20260823-1117Z`
- Temporal register: `temporal-register.ts` — `storesCredentials: false`, `credentialState: "not_stored"`
