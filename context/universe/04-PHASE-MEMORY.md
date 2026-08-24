# 04 — Phase memory credentials

Law, copied from MCT-2600027 `temporal-register.ts`:

- `storesCredentials: false`
- `credentialState: "not_stored"`
- Status is `active | expired | detached`
- Access is temporal. Inclusive while active. Never persisted.

## Fluid state

Credentials are **handed**, not stored.

1. Operator starts a phase at the para Border.
2. The Border issues `registerId` and a short-lived `phaseSecret` in RAM.
3. Only the Konnektor Department may see `phaseSecret`.
4. Gemini, Drive, Git, traces, and this pack see **only** `registerId`.
5. After 15 minutes, or on HOLD/detach, the secret is wiped.

## Payload (Border)

```
CREDENTIAL_PHASE
  registerId: string
  validUntil: ISO-8601
  capability: "github.konnektor"
  storesCredentials: false
  secret: <RAM only, never on this document, never on Drive>
```

If a document, commit, or Drive file contains a GitHub token, it is a Trace-Treue violation. Quarantine. Do not use the token.

The Konnektor may **use** a handed secret for a phase. It may not **keep** it.
