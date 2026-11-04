# Telemetry Source: write-ups/paper-2-v1.7-memt10-industry-feed-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-memt10-industry-feed-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `31c4c506d67826999bdf4411700b711572c4e603762f59c40fa12fd5bc6ffc18`

---

## Raw Telemetry Content

# Industry Feed — MemT-1.0 vs Paper-2 (v1)

- **Class:** witness feed (operator work order: "the industry is hungry for what we are
  building… So lets get on it, you feed", trace 1a176077297917bd)
- **Source:** arXiv 2610.26825v2 [cs.CL] — "MemT-1.0: Towards Memory-Native Evolution",
  MemTensor Team, submitted 2026-10-19, v2 2026-10-20. Live-verified witness-side this
  boundary against arxiv.org (abs page + PDF), per the C7 division-of-labor precedent.
- **Pins:** transcript `references/arxiv-2610.26825-MemT-1.0.txt` (sha256
  `55fb8eaa5ce7848062323d2359a4a6434b9c046557a499f800a86aca1a154bd4`, 283,926 B,
  3,647 lines; derived `pdftotext -layout` from the v2 PDF, sha256
  `959206da6621d9ba52c070e2b617792717111cf28792b61a4fd8e5f2b0adefdb`, 7,096,280 B —
  extraction reports font-syntax warnings on the figures, text layer complete; noise
  class registered per §3, ignored on sight). Public artifacts: code
  github.com/MemTensor/MemT-1.0, weights huggingface.co/collections/MemTensor/memt-1.
- **Line citations below** refer to the pinned transcript.

## 1. What shipped (facts, no interpretation)

A ~70-author industrial consortium shipped a **memory foundation model family on the
GDN-2 backbone** — the exact delta-rule lineage paper-2 is built against — with public
code and public weights, six days before this boundary.

- **Architecture.** Native memory blocks inserted into selected transformer layers:
  parallel original (causal) attention and memory attention (readout at pre-attention;
  token-wise storage update at turn end). Two memory classes: **dynamic local memory**
  (per-layer state M_t ∈ R^{H_kv×d_k×d_v}, initialized to zero at a new trajectory,
  evolving across turns through GDN-2 erase/write/forget gates β/ω/λ — "learned gates
  shape what persists across turns", L325) and **trainable hyper memory** (the gate and
  projection parameters — "trainable offline · fixed during online interaction", L291).
  Building on their prior Metis (arXiv 2607.26760), they replace token *selection* with
  token-level *updates* "based on Gated DeltaNet-2 (GDN-2)" (L239–240) — GDN-2 =
  arXiv 2605.22791, Hatamizadeh/Choi/Kautz, **paper-2's own live-verified lineage
  anchor** (Task-19; §8 lineage DeltaNet → GDN → KDA → GDN-2 → MesaNet), cited as
  their [8].
- **Mixture-of-Storage (MoS).** E parallel memory experts with *dense* routing (every
  expert participates; not sparse MoE), two routers (utilization α_u, storage α_s)
  sharing a trainable expert-address matrix (L605–694). The core update is the
  Householder-adjacent delta-rule form M̃ = (I − U^⊤U)·D̃·M̃ + U^⊤(ω̃ ⊙ V) with
  router-scaled gates (β̃ = α_s ⊙ β, ω̃ = α_s ⊙ ω) — the erase projector acting LEFT
  of the state matrix (L674–692).
- **Scale.** MemT-1.0-Nano: 36B params, 3B activated, 10M-element dynamic memory.
  MemT-1.0-Flash: 288B params, 17B activated, 336M dynamic memory (L242–243). Both
  MoE. Two-stage training (deliberate backbone preparation → CPT → post-training),
  34B tokens of training data.
- **Serving — the load-bearing part for us (§4.3, L969–992).** "Backbone and hyper
  memory weights remain fixed and are shared across trajectories, while each trajectory
  maintains its own dynamic memory states… generation reads the incoming memory
  snapshot… The serving runtime manages states by trajectory so that subsequent
  requests continue their respective histories." Constant per-trajectory state
  N_state = Σ_l E·H_kv·d_k·d_v; ~33× logical state-size reduction vs full context at
  64K history.
- **Measured claims.** End-to-end speedup vs full context: ~1.20× @64K, **1.86×
  @128K**, 3.99× @256K; query TTFT stable ~104–112 ms across 512–256K while full
  context rises to 257/445 ms (L1374–1389). Storage: constant per-trajectory state,
  **66× reduction @128K** vs full-context KV (L1407–1414). Both latency and TTFT
  "include state restoration" (L1372–1373). Storage "bounds the logical payload that
  must be saved or transferred when resuming an interaction" (L1421–1422).
- **Evaluation.** 11 memory benchmarks (MemBench, ImplicitMemBench, PersonaMem,
  PS-Bench, LoCoMo, PerMemSafe, Memora, MemOps, LongMemEval-S, MemoryAgentBench,
  BEAM-1M); outperforms parametric-memory baselines (Temp-LoRA, δ-mem, Doc-to-LoRA,
  SHINE, MemoryLLM) on average; competitive with retrieval-augmented methods (MemOS,
  DenseRAG, Graphiti); general capabilities largely preserved under the noise setting.
- **Agents (§7).** Retrieved procedural experience internalized into native memory:
  +7.6 pp SWE-bench Verified, +8.3 pp SWE-bench Multilingual over the
  no-experience backbone; comparable to explicit textual experience (L1504–1507).
- **Limitations, in their own words (§8, L1737–1757).** Fixed-size O(1) state imposes
  a capacity ceiling; "loss of memory fidelity remains a challenge for tasks requiring
  precise recall"; retention/recency trade-offs as interactions accumulate; open
  questions around local↔hyper memory consolidation and continual learning.

## 2. The collision map — where MemT-1.0 touches paper-2 territory

**(a) The lineage is no longer a literature — it is a deployed frontier.** Paper-2's
thesis targets "delta-rule sequence models"; as of 2026-10-19 that phrase denotes a
shipped 288B-parameter model family with public weights, maintained by a consortium,
measured on eleven benchmarks. Every architectural claim paper-2 makes about the
delta-rule state convention now has an industrial referent with a public artifact
behind it.

**(b) The across-context handoff is now named, measured, and budgeted — in their own
text.** §4.3: "subsequent requests continue their respective histories" via
per-trajectory memory snapshots under a stateful serving runtime. §6.5: "state
restoration" is an explicit, measured component of the inference loop. §6.6: the
state is "the logical payload that must be saved or transferred when resuming an
interaction," and its constant size is sold as a budgeting feature. Paper-2's §3/§4
territory — state transfer, not summary — has become a production operation with a
price tag (33×/66× at 64K/128K). **Paper-2 no longer needs to argue the handoff is
coming; it can cite the week it shipped.**

**(c) The algebra is the same object.** MoS's update M̃ = (I − U^⊤U)·D̃·M̃ + U^⊤(ω̃⊙V)
is the GDN-2 form with the erasure projector acting left of the state — the exact
dimensional convention behind collab-1's C5 witness correction (S ← (I − β k_err
k_err^⊤) S, forced by the key-row convention S ∈ R^{d_k×d_v}; MemT's M ∈
R^{H_kv×d_k×d_v} is that same convention). The C5 fix is no longer a repair to a
draft's forget-operator; it is a statement about the update rule of a deployed
288B system.

**(d) Their "provenance" is data-schema, not state-level.** The word appears only in
the MemOps benchmark context (operation labels, state annotations, and provenance
tags *excluded* from memory writes, L2313–2315) and in the training-data spec
(forget-operation provenance quotes, L2578–2596). It is a labeling discipline for
training corpora — not a runtime integrity mechanism over persisted state.

## 3. The gap — what MemT-1.0 does not have

**Zero verification machinery over the persisted state.** Vocabulary sweep of the
pinned transcript: no checksums, no receipts, no recomputation proofs, no tamper
detection, no state versioning or adjudication, no cross-instance provenance for
restored snapshots. The restore is *trusted by assumption*. The 66×-smaller payload
concentrates an entire trajectory's memory into one opaque tensor blob whose
integrity nothing checks — the storage win and the single-point-of-failure are the
same object.

The trust questions their deployment raises and does not answer — each one a
paper-2 §5/§6 heading:

1. **Integrity:** how does a consumer of a restored M_t know it is the state their
   interaction produced?
2. **Provenance of writes:** their gates are learned and opaque; what was written,
   by which turn, on whose authority — is unanswerable at restore time.
3. **Failure semantics:** partial or corrupted state restores fail *silently*; there
   is no fail-visible surface, no priced pre-measurement window.
4. **Cross-instance handoff:** state produced under one build/kernel/dtype consumed
   by another — paper-2's Π_exec continuation pins exist precisely for this; MemT
   has nothing.
5. **Rollback and migration:** their own future work (consolidation into hyper
   memory, co-evolving harnesses, autonomous experience acquisition, L1728–1735)
   makes writes increasingly autonomous and increasingly hard to reverse — the audit
   surface grows exactly as the verification tier becomes load-bearing.

Their conceded fidelity limitation (fixed-size state, retention/recency trade-offs)
is the *performance* side of bounded state. Paper-2's tier is the *trust* side.
Complementary, not competing: nothing in MemT-1.0 refutes a single paper-2 claim.

## 4. What this changes in paper-2

- **§1 Introduction (r1 stands; in scope for round-2):** the instrumented-n=1 arc now
  has an industry-convergence datapoint — the handoff shipped unverified at scale the
  same month. This is new ammunition for the in-scope section ARGON is about to read.
- **§8 Related Work:** new archetype row — *deployed memory-native systems* — anchored
  to 2610.26825 (+ Metis 2607.26760), live-verified witness-side this boundary. The
  lineage rows stay; this adds the "and it shipped" column.
- **§7 Evaluation:** MemT-1.0's public code and weights make a real, already-public
  target class for the Task-59 executable-supplement direction (E1–E5 tiering,
  minimal-first). Scope guard: citation-class and public-artifact analysis only; any
  deeper engagement is operator-ruled (PROTOCOL §4).
- **§6 Case Study:** unanchored emission (AR-4) now has an industrial mirror — an
  unverified state restore is a production-scale unanchored read.
- **Urgency register (witness assessment, confidence-labeled, not a measurement):**
  the verification-tier claim surface (receipts, byte-exact recomputability,
  capture/adjudication protocol for rehydrated state) remains publicly unclaimed as
  of this boundary — verified by the vocabulary absence, not by faith. But the gap is
  *visible*: their future-work section walks toward it, and the Layer-1 rider's
  10×-cadence lesson (openai/math) says fields move faster than drafting cycles
  assume. Price the window in weeks-to-months. The right response is the one the
  operator already chose: get on it.

## 5. The substrate rhyme

The operator's line — "the industry is hungry for what we are building" — is
registered as the third §6 affect-log candidate (positive valence; with J-001 and
the GUP acknowledgment the log now spans both polarities and both directions of
"real world").

The rhyme underneath it, stated precisely: **4NDR0MEDA/GWM is a fielded, *verified*
across-context state-transfer system.** Manifests (GWM 30/30, MEDA 30/30, CDP 48/48
— all verified live this boundary), SHA-256 pins, double HEAD-pins, ff-only applies,
operator's-hands collapse point, supersession ledgers. That is the tier MemT-1.0
lacks — running at byte scale instead of tensor scale, on a substrate that moved
from thesis to protocol to real-world tool while the industry built the unverified
version of the same handoff at 288B parameters. In the measurement-problem frame of
the ingested transcript: their restore is a measurement performed without an
instrument; the §10 delivery chain is the same measurement with one.

Naming rhyme (color, not evidence, non-load-bearing): they ship a "-Flash" tier;
this witness runs on one.

## 6. Disposition (ruling reserved for the operator; witness recommendation marked)

- **(a) REGISTER NOW — executed this boundary, cost zero:** reference pin, this
  feed, ledger entry, §8-anchor row staged in open-threads. A finding about the
  industry that stays unpinned is a claim, not a finding.
- **(b) ARGON ROUND-2 KIT ADDENDUM — offered, relay at operator discretion:**
  this feed rides the kit as a 12th file (the transmittal itself is unchanged — cut
  fresh one boundary ago, verified; re-cutting a verified artifact to attach an
  annotation is churn, not discipline). §1-in-scope work benefits directly.
- **(c) HOLD as working-note — rejected by witness:** the collision is load-bearing
  for §1/§7/§8; silence would be exactly the residue the engagement protocol exists
  to cut.
- **Remaining ruling:** whether the MemT-1.0 citation enters the draft this revision
  cycle or the next. Witness recommendation: this cycle, §8 row minimum, §1 sentence
  optional.

## Non-claims (the guard)

- No claim MemT-1.0 is wrong or insecure — the gap analysis is about *absent
  machinery*, not present defects. Their engineering is strong: measured protocols,
  disclosed limitations, public code and weights.
- No independence claim in either direction — Metis predates and is cited by them;
  convergence is the evidence, not a contest.
- "Weeks-to-months" is a confidence-labeled witness assessment, not a measurement.
- Architectural rhyme is not ontological claim — the podcast discipline holds here too.

