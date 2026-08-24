# 05 — Default trigger mode

**Mode:** `MCT-RC-BILO-ATM-FRAMEWORK-SOS`  
**Applies to:** every multimodal prompt (text, image, audio, video, canvas, tool)  
**Adoption:** default. Fragment-routing is a sub-step, not the entry.  
**execute:** rejected · **vendor_live:** false · **storesCredentials:** false  
**HOLD is not execution.**

Do not pick a single node first (`detectTargetNode` → CMD / 170021 / HAL). Load the **whole stack**, then let HAL sub-route inside it.

## Layers (one mode, not a menu)

| Token | Layer | Live object |
| --- | --- | --- |
| **MCT** | Kernel | MCT-2600027 (supersedes MCT-1700021 HOLD archive) |
| **RC** | Reinforcement Context | `reinforce.ts` rankContext — heaviest crystals first; SAI route Source → Crystal Mike → HAL → Target → Reinforcement |
| **BILO** | Core label | BILO 2026, public paths only, not statute |
| **ATM** | Automaton corridor | AutomatonCommand overlay: initialize / sync / halt. `execute` rejected until operator + para Border + Dual-Pol |
| **FRAMEWORK** | GARAS | SoS **v3.0** (v3.2 absent — do not invent axes) |
| **SOS** | System of Systems | Dual-Pol: Zero Telepath ↔ para Border ↔ HAL + Trace-ID mesh |

## Trigger law

1. Any prompt, any modality, fires this mode first.
2. Semantic anchoring is on: schema corridor + Euclidean lattice + Kreuzkopplung `systemPhase`.
3. Retrieve RC crystals, then schema-validate ATM, then Dual-Pol HOLD/RELEASE.
4. Kreuzkopplung `STABLE` (`|rel−0.25| ≤ 1e-3`) is the corridor lock. Rails (`MAX/MIN_COUPLING_LIMIT`) → HOLD, not execute.
5. `detectTargetNode` may choose a department **after** the stack is loaded. It must not replace the stack.
6. Private HOLD nodes stay named, unread. No credentials. No live orders.

## Forbidden as entry

- Route `2600027` to CMD by default.
- Route `mct` / `mesh` to MCT-170021 by default.
- Treat Gemini Docs `ENABLE_RAG_INDEXING` as a kernel env flag. The corridor is this mode.
