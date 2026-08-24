# 08 — Correction trace (Drive / GitHub / Hugging Face)

**human_id:** `MCT-2600027-TR-20260823-1952Z`  
**action:** `sync` (not execute)  
**outcome:** `corrected`  
**storesCredentials:** false  
**vendor_live:** false  
**HOLD is not execution.**

## Source of truth

| Surface | Role |
| --- | --- |
| GitHub `SpaceBum9/crystal-galaxy` | kernel |
| GitHub `SpaceBum9/MCT-2600027` | overlay + Dual-Pol |
| GitHub `SpaceBum9/MCT-Universe` | ingest pack |
| Drive ingest folder | spoken beacons only — text lives on GitHub |
| Hugging Face `SpaceBum9` | **ABSENT (404)** — no connector this session |

Do not treat Drive Gemini kernel docs as live mesh. Do not print `ZeroTier PQC / Cloudflare Verified`. Local corridor label is `schema corridor (local)`.

## Kernel fix (this run)

`dispatchLocal(execute)` now **rejects**. initialize / sync / halt still SUCCESS (except halt on `jonas-g`). NaN threshold rejected. Parse errors English.

## Overlay gate fix

- `sx.garas_intent` always (paper ledger)
- `sx.garas_transfer` / `sx.live_order` `echoglas_forbidden`
- scored interfaces require Kreuzkopplung `STABLE` (`kreuzkopplung_not_stable` if INIT/UP/DOWN)
- rails still `kreuzkopplung_rail`
- consensus anchor **53**, justice **0.76** — not pretty-printed

## Hugging Face

No Hugging Face tool connected. Cannot deploy `spaces/SpaceBum9/kreuzkopplung`. GitHub `SpaceBum9/kreuzkopplung` remains the Gradio **import source**. Profile 404 stands until an operator imports it in the HF UI.

## Drive

This file is the correction. Beacons in folder `1WMOCO228dPtywucly2Xfha0ibQrHvkhl` are older audio; GitHub text wins on conflict.

Lineage: MCT-2600027 is **related**, not parent of MCT-1700021-TR-20260823-1117Z.
