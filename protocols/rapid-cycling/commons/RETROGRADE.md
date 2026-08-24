# SAI retrograde scan

Local module. Looks **backward** through device-side stamps (artifacts, Logos chain, Rapid Cycling dailies). Does not scan a phone, a disk, or a network.

Recurrence key = clock time in `Europe/Berlin` (`HH:MM`).

A stamp is **recurring / markable** when:
- the same `HH:MM` appears twice or more, or
- it is a schedule mark (`09:00` commons, `21:00` oracle)

Tap a chip to mark it. Mark mints `kind: self` note `retrograde|HH:MM` onto the Logos chain (`TR-…`). Unmark drops the local flag, not the chain.

Storage: `sai-scan-v1`. No credentials. HOLD is not execution.
