# 07 — GARAS SoS finance

**Command:** `execute` `mct-2600027` → `garas-finance`  
**Operator:** finance this SoS  
**Default mode:** `MCT-RC-BILO-ATM-FRAMEWORK-SOS`

| Step | Result |
| --- | --- |
| parseCommand | ok |
| dispatchLocal | would SUCCESS (kernel does not gate) |
| sx.gate / sx.garas_transfer | **echoglas_forbidden** |
| sx.garas_intent | **applied** — paper ledger |
| justice axis | **0.76** — not lifted |
| consensus | 53 < 70 |

Live funds, IBC, trader, paywall circumvention: forbidden. Paywalls paid. HOLD is not execution.

Procedure: [schema/garas_finance.json](https://github.com/SpaceBum9/MCT-2600027/blob/main/schema/garas_finance.json)
