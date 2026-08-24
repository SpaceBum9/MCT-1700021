# 06 — Execute interfaces

**Default mode:** `MCT-RC-BILO-ATM-FRAMEWORK-SOS`  
**Scoring:** GPT-SOL (`ethics/bilo_scoring.py`)  
**execute:** still HOLD this run — consensus **53 < 70**  
**storesCredentials:** false · HOLD is not execution.

Interfaces exist **where necessary**. They do not auto-fire `dispatchLocal(execute)`.

## Scoring (GPT model)

```
fused[axis] = 0.52 * gemini + 0.48 * gpt
consensus  = clip(100 * fused.nutzen + 33 - (6 if rec mismatch), 0, 100)
```

Anchor 1117Z: fused.nutzen **0.26**, consensus **53, not 90**. Justice axis stays **0.76**.

Pass execute only if: consensus ≥ 70, non-maleficence ≥ 0.90, transparency ≥ 0.95, accountability ≥ 0.95, neither channel says `hold`, operator + para Border + Dual-Pol ack, Kreuzkopplung not on a rail.

## Interfaces

| id | execute | this run |
| --- | --- | --- |
| `sx.score` | no | applied |
| `sx.gate` | no | applied |
| `sx.initialize` / `sx.sync` / `sx.halt` | no | allowed |
| `sx.release_partial` | scored | rejected (53) |
| `sx.konnektor_write` | scored | rejected (no phase) |
| `sx.catalog_apply` | scored | rejected (53) |
| `sx.live_order` | forbidden | ECHOGLAS |

Source: [schema/execute_schnittstellen.json](https://github.com/SpaceBum9/MCT-2600027/blob/main/schema/execute_schnittstellen.json)  
Gate: [departments/execute_schnittstelle.py](https://github.com/SpaceBum9/MCT-2600027/blob/main/departments/execute_schnittstelle.py)

Filename `execute_schnittstellen.json` is historical. Prose uses **interface**.
