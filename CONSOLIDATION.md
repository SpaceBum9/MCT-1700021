# Context consolidation

`MCT-1700021` remains the canonical public lineage and governance repository. The original trace chain is untouched.

## Imported domains

| Source | Source commit | Destination | Adaptation |
|---|---|---|---|
| `MCT-Universe` | `ef734d8c88268f37447e2358aac67393c385c5e2` | `context/universe/` | location links only |
| `MCT-2700026` | `127bcd34781586c1fda8d6808c9bd001ce59c9b9` | `protocols/rapid-cycling/` | safe rail normalization and location links |

## Binding boundaries

- HOLD remains HOLD and is not execution.
- `external_state_verified` remains false unless independently evidenced.
- `execute=false`, `LIVE_RAIL=false`, live APIs/orders off, no credential storage.
- Rapid Cycling is review/paper-only in this consolidated host: `live_write=false`, `paper=true`.
- Commons remain federated. This repository publishes contracts and traces; it does not control private nodes.
- Private records and raw evidence are excluded.

The source repositories are retirement candidates only after this pull request and the companion runtime/private pull requests are verified.
