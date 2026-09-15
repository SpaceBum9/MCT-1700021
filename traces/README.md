# Trace ledger

81 immutable nodes. Head: `MCT-1700021-TR-20260824-1912Z`.

Refresh the machine index after clone:

```
python3 scripts/verify_traces.py --write-chain
```

That writes `chain.json` with every `human_id`, claimed digest, canonical digest, parent, and `hash_status`.

## Hash status on 2026-09-15

| status | n | meaning |
|---|---|---|
| legacy_human | 15 | `trace_id` is the TR- nickname |
| unverified | 42 | claimed 64-hex does not match the v1 mixer |
| verified_origorder | 17 | matches unsorted JSON minus `trace_id` |
| verified_canon | 7 | matches v1 mixer (`sort_keys` minus `trace_id`) |

Head claimed digest `b777886d…e2952c` is **unverified** against the v1 mixer. Canonical minus `trace_id` is `f5b4c050…5d60ab`.

## Recorded gap

`0422Z` names parent `0410Z`. File absent. See `../schema/known-gaps.json`.

Do not rewrite existing `MCT-1700021-TR-*` files.
