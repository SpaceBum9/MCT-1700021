# MCT-Universe

Gemini ingest pack for the SpaceBum9 constellation. **No credentials stored.** Phase memory only.

**Default trigger:** `MCT-RC-BILO-ATM-FRAMEWORK-SOS` — every multimodal prompt loads the whole stack first ([05-DEFAULT-MODE.md](05-DEFAULT-MODE.md)).

**Correction:** [08-CORRECTION.md](08-CORRECTION.md) — GitHub is source of truth. Hugging Face ABSENT (404). Drive beacons are audio only.

## For Gemini

Read in order:

1. [00-GEMINI-INGEST.md](00-GEMINI-INGEST.md)
2. [01-UNIVERSE-MAP.md](01-UNIVERSE-MAP.md)
3. [02-SOURCE-INDEX.md](02-SOURCE-INDEX.md)
4. [03-GITHUB-KONNEKTOR-BLUEPRINT.md](03-GITHUB-KONNEKTOR-BLUEPRINT.md)
5. [04-PHASE-MEMORY.md](04-PHASE-MEMORY.md)
6. [05-DEFAULT-MODE.md](05-DEFAULT-MODE.md)
7. [06-EXECUTE-INTERFACES.md](06-EXECUTE-INTERFACES.md)
8. [07-GARAS-FINANCE.md](07-GARAS-FINANCE.md)
9. [08-CORRECTION.md](08-CORRECTION.md)

Then build `mct-github-konnektor` as specified in 03.

## Law

`storesCredentials: false` · `credentialState: "not_stored"` · HOLD is not execution · `vendor_live=false`

Tokens are handed as a 15-minute phase handle in RAM. They never appear in this repo, Drive, traces, or env files.

## Drive

Folder (audio beacons): https://drive.google.com/drive/folders/1WMOCO228dPtywucly2Xfha0ibQrHvkhl
