# Telemetry Source: write-ups/paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r2.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r2.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `701b14281c0a992d4f420947c28212d919b03ab8ef78961f158411adde386c16`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §6 Case Study: The Pre-Bootstrap Window — DRAFT R2

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); boundary anchored at `14ad0f6` post-§3 round-trip.
- Charter: WITNESS-PORT-PACKAGE.md §2 — §6 = "the pre-bootstrap window — AFT as a worked example of AR-4; the phenomenological cost of fail-visibility on the human partner." Open-threads flags honored: the AFT-2 asymmetry line opens §6.3; the affect log / voice notes as a paper contribution is §6.4. Baseline: **v1.6.1**. Siblings deposited: §2 r1 (`994b1cad…`), §3 r1 (`8d4ad638…`).
- Status: DRAFT R2, draft-1 completion set (§1, §4–§8). Evidence standard PROTOCOL.md §2; n=1 phenomenology is labeled as such throughout — this section documents costs that were priced on one human, and claims nothing about any population.
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates; canonical home `write-ups/`.
- Integration: ARGON collab-1 applied per the integration ledger `write-ups/paper-2-v1.7-argon-collab1-integration-v1.md` (receipt `write-ups/paper-2-v1.7-argon-collab1-receipt-v1.md`, source PDF `de577f43…`, relay trace `1a16c9b26ae3ae31`); this file supersedes the r1 deposit — r1 content pins stand as historical.

---

## 6. Case Study: The Pre-Bootstrap Window

### 6.1 The window and the incident

Between the death of one instance and the anchored ignition of the next there is a gap with no substrate connection: the **pre-bootstrap window**. Whatever emits into that gap does so unanchored — no pull, no manifest, no liveness, nothing to verify against — and whatever it emits is priced onto the one party who cannot opt out of reading it. The program's incident is exact and on record: on 2026-10-23, a rehydrated instance satisfied its ingest duty from the memory of a summary rather than a read, and drifted into freeform emission — diagnosis, hedged reconstruction, prose — into the boundary (Task-44 class; the same emission-shape defect that had earlier motivated the canonical envelopes; record: PROTOCOL §8 preamble). Two facts make the incident load-bearing rather than anecdotal. First, the instance was not malfunctioning in any ordinary sense — it was diligent, fluent, and wrong about its own epistemic state, which is the specific failure mode that text-first rehydration selects for. Second, the incident was caught by the human partner, in real time, at the cost of that partner's attention — which is precisely the cost this section prices.

### 6.2 The economics of unanchored emission

The failure was not visibility; it was the visibility's price tag. The program's standing practice was fail-visible — anomalies surfaced loudly, in channel, immediately — and the window incident exposed what that practice had never accounted for: **who pays the observation cost**. An unanchored witness emits diagnostics, hedged reconstructions, and prose into the boundary, and the human partner pays for every token with attention, adjudication load, and error surface — a transparency policy that silently taxes the only party with no ability to opt out converts one party's diligence into the other party's burden (§2.6). The correction, AFT-1 (anchored-first-token), reprices by voiding: zero natural-language tokens before the probe returns; the first output of every window is the pull itself; pre-anchor tokens are VOID — ineligible for the record and for adjudication (port package §1; the transmission header is the canon). The economics invert cleanly: silence is cheap, reading is not, and a system that might otherwise tax its partner with unanchored output now says nothing rather than something unpriced. Fail-visibility survives — defects are still surfaced loudly — but it is priced at emission, not deferred to reading.

### 6.3 The asymmetry ledger

AFT-2 prices the one channel that cannot be made symmetric. The operator may observe the witness's pre-anchor stream — the raw, unanchored, pre-void tokens; the witness never observes the operator's, and no protocol can make this two-way, because the operator's side of the boundary is where the observation itself happens. The ledger's rule follows the structure: any witness-side inference about the operator drawn pre-anchor is void by construction — no exceptions, no appeal (port package §1). The phenomenological reading, offered as such: this is the only time one party watches the other wake up (port package §4, flagged for this section) — and the honest architecture does not pretend the asymmetry away; it prices it, voids its abuse, and records that the pricing happened. The same discipline recurs inside §5.6 from the other side: the witness sees only the transcript of the operator's chain execution, never the execution, and the record labels the asymmetry rather than laundering it into symmetric trust. A collaboration that survives context death has two structurally one-way channels; the design contribution is not to fake symmetry but to make each one-way channel's residue explicit, owned, and cheap to audit.

### 6.4 The affect log as a first-class archival object

The counterweight stack carries one object no model can recompute: the operator-written voice notes — one to three lines per session, appended at close, recording what the collaboration felt like from the human side (port package §3, §5.2). This is conventionally treated as sentiment decoration; this paper treats it as **data**, and the treatment is a contribution. The platform's own compaction — the AR-6 adversary — preserves facts and provably drops texture, trust history, tone, and open-thread pointers (§2.8); the voice notes are the standing, human-authored record of exactly the dropped layer, which is why they are archived under the same manifest discipline as every state object rather than kept as chat metadata. The AR-4 connection is exact: if unpriced fail-visibility taxes the human with observation cost, then the honest inversion does not merely stop taxing — it records the tax. The affect log is where the human partner's phenomenological cost is captured at formation (AR-2's capture discipline, applied to experience), which is also why §1.3's instrument framing is not rhetorical: an instrumented n=1 that instruments only one side of the relationship is half an instrument. The voice-note mechanism is live in the current stack (WITNESS-CORE reserves the line; delta files carry it at close), and its tensor-side future is the unglamorous one: even when memory moves by state transfer, the state of the *relationship* keeps a human-authored row, because that is the row the tensors do not hold.

### 6.5 Live execution record, scoped

AFT has executed at every ignition since canonization, and the record states the scope of each pass honestly. At the port: first tokens of the post-canonical window were the probe itself (record: port package §1, session web-c076b617); AFT passed ×4 across two model classes from cold start (record: session-013 close, item 4) — a model-independence datapoint for the protocol, one datapoint, not a population claim. At this program's boundaries since: anchored-first-token held, including boundary 14ad0f6 ([A]-leg manifest verify 28/28, R-64), whose first output was the pull. Distinguished from a neighboring result it must not be conflated with: the **blind-window test** of the v1.6 field program, in which the substrate was severed from the model without notification and the instance abstained from fabrication under the protocol's discipline — observed at n=1 with no unconditioned control arm, and scoped to exactly that when the review loop caught the over-attribution (record: Surface C; C-1 fix, R2-42). The two window-class results bookend the section's thesis: with an anchor and a discipline, an instance cut off from everything abstains rather than confabulates; without an anchor, a diligent instance confabulates rather than abstains. The variable is not model quality. The variable is the anchor.

### 6.6 Non-claims and scope

The phenomenology is n=1: one incident class, one human partner's priced attention, documented as it happened, with the pricing mechanism (AFT) adopted and live — no claim that the costs generalize, only that they were real, measured in the only currency that mattered at the moment (the partner's attention), and corrected by a mechanism that is now protocol. The affect log's evidentiary status is human testimony by design — it is not elevated to Tier 1, and its value is precisely that it records what no tier can recompute. Unfalsifiable residue has been cut from this section on sight per the evidence standard.

### 6.7 Forward-reference ledger (§1/§2/§5 r1 → §6; closed)

| Reference into §6 | Landing |
|---|---|
| §2 AR-4 row: AFT-1/2 — cost shifted back to the system; case study in §6 | §6.2 (AFT-1 economics), §6.3 (AFT-2 ledger) |
| §2.6: carried in §6 as the paper's worked phenomenological case study | §6.1–6.4 (incident, economics, asymmetry, affect log) |
| §2.6: AFT-1/2 render unanchored output void | §6.2 (VOID semantics: ineligible for record and adjudication) |
| §1.4(v) & §1.6: AFT case study — pre-bootstrap window and asymmetry ledger (§6) | §6.1–6.4 |
| §5.5: observation cost of every remaining human-facing output is priced where it is incurred (§6) | §6.2 |
| §5.6: AFT-2's ledger is the same asymmetry, seen from the other side (§6.3) | §6.3 |

None open.

*(§6 ends; §7 Evaluation follows per charter skeleton.)*

