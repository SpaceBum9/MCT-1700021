# 03 — GitHub Konnektor blueprint (Gemini builds this)

**Name:** `mct-github-konnektor`
**Owner:** SpaceBum9
**Surface:** Department (anthropomorph allowed), never Dual-Pol core.
**Default:** HOLD. `vendor_live=false`.
**Credential law:** 04-PHASE-MEMORY. Non-negotiable.

## Purpose

Give Gemini a GitHub Konnektor that can list, read, and — only inside an active phase — write to SpaceBum9 public MCT repos. The Konnektor is a para-Border department, not a secret store.

## Tools

| Tool | Phase required |
| --- | --- |
| `gh.whoami` | no |
| `gh.list_universe` | no |
| `gh.tree` | no |
| `gh.read` | no |
| `gh.commit` | **yes** |
| `gh.open_pr` | **yes** |

Write tools MUST call `validateTemporalAccess(registerId)` and refuse if not `active`.

## Architecture

```
Gemini
  │  Border payload: CREDENTIAL_PHASE { registerId }  (no token)
  ▼
para Border (constraint gate)
  │  RELEASE_PARTIAL only if phase active
  ▼
GitHub Konnektor Department
  │  RAM: token bound to registerId, never serialized
  ▼
GitHub REST
```

## Token handling (temporal-register.ts)

```
storesCredentials: false
credentialState: "not_stored"
inclusiveAccess: true
status: active | expired | detached
```

1. Accept the GitHub token only as a function argument at phase start. Name it `phaseSecret`.
2. Keep it in a module-level `let` (RAM). Bind to `registerId`.
3. TTL 15 minutes.
4. On expire or detach: wipe buffer, emit Trace `phase_detached` with registerId only.
5. Never write `.env`. Never log the secret.
6. Prefer GitHub App installation tokens or device-flow over long-lived PATs.

Writes go to branch `mct/gemini-konnektor/<trace-id>`, then PR. Never force-push main.

Allowlist write: MCT-2600027, MCT-1700021, MCT-2600027-CMD.
Deny private HOLD nodes.

Serializing Konnektor state to JSON must not contain a token.
