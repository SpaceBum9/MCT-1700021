# Trace contract — MCT-1700021

Status: paper / HOLD. `LIVE_RAIL=false`. Execute remains rejected.

This repository publishes the lineage. It does not execute.

## Two layers

| Layer | What it is | What it is not |
|---|---|---|
| Ledger (`traces/*.json`) | Immutable session records | A signature, identity, or authorization |
| Contract (`schema/trace-v1.json`) | Required shape for **new** traces | A rewrite of existing files |

Existing files under `traces/MCT-1700021-TR-*` are not modified.

## Canonical hash (v1)

Same mixer as `SpaceBum9/MCT-2600027` `training/engine.py`:

1. Drop `trace_id` and `checkpoint_sha256` from the object.
2. `json.dumps(..., sort_keys=True, separators=(",", ":"), ensure_ascii=False)`
3. UTF-8 → SHA-256 hex.

`human_id` (`MCT-1700021-TR-YYYYMMDD-HHMMZ`) is a nickname. STATE.md already notes the 32-bit birthday bound. The 64-hex digest is the record.

## Parent rule

- Parent of this chain stays inside 1700021 or an explicit root: `CG-KERNEL-2026-08-19`, `MCT-170021-CORE`.
- `MCT-2600027` is related-lineage / runtime host, never parent.
- A missing parent is a finding, not a silent skip.

## Verifier

```
python3 scripts/verify_traces.py
python3 scripts/verify_traces.py --write-chain
```

Exit `0` when every file parses, the index covers every trace file, and v1 nodes match their digest. Legacy nodes may carry `hash_status=unverified`. Unknown missing parents fail. Gaps listed in `schema/known-gaps.json` stay visible and fail only with `--strict`.

## Runtime contract

Hash and checkpoint verification for GARAS training live in:

`https://github.com/SpaceBum9/MCT-2600027/blob/main/training/engine.py`

This repo binds that mixer by copy of the three rules above. It does not import the runtime.
