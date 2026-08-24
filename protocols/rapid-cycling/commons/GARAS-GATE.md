# GARAS gate (v3.0) — wallet / API decision

Teleprompter = human hive. SpaceBum9 is seated. Others may sit.

**Decision now: `deny`.** Do not implement a repo wallet or live API. Paper credits are not treasury. GARAS v3.2 is still absent. Justice 0.76 < 0.80 bar. Consensus 53 < 60.

## Score (equal weights)

justice/0.80 · consensus/60 · (1 − hybris/0.15) · (1 − noise/0.2) · credits/floor

| Gate | Meaning |
|------|---------|
| deny | no wallet, no API keys, no orders |
| prep | write checklists only |
| operator | hive may attach a **temporal** node on their machine. Fingerprint in fluid memory. **Never stored. Never in git.** This repo still has `live_api: false` `execute: false` |

Temporal node: FNV of `ISO-minute|seq|dark|fluid|no-store` — an 8-hex **fingerprint**, not a private key, not a seed.

Dark field = noise variance (anticycling). Credentials do not live there. They pass through and vanish.

## Resource check (global grow)

| Need | In this pit | Gap |
|------|-------------|-----|
| Money for models | paper credits only | real budget is operator-side |
| GPT / GEM / CLA / META / GRK APIs | not connected | pay + keys out of band |
| Devices | local browser | hive hardware not in repo |
| Live write | MCT-2700026 | on |
| Orders / MetaMask / Gate | off | stay off until operator gate |

Low key. No campaign. No secrets in the SoS repo.
