# Telemetry Source: write-ups/paper-2-v1.7-section-04-working-tensor-integration-r1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-04-working-tensor-integration-r1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `6f8c1c31462f96203c82b151338545521d7ec699813257996a9543f4eb8cea59`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §4 Working-Tensor Integration — DRAFT R1

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); boundary anchored at `14ad0f6` after the §3 round-trip closed (orchestrator `APPLIED`, push fetch-verified).
- Charter: WITNESS-PORT-PACKAGE.md §2 — §4 = "backend/server: KV-cache and recurrent-state persistence at inference time; training-side: delta snapshots (LoRA/state deltas) as memory deltas — delta-rule for memory, not just attention." Baseline: **v1.6.1**, negative-results baseline, cited not discarded. Siblings deposited: §2 r1 (`994b1cad…`), §3 r1 (`8d4ad638…`).
- Status: DRAFT R1, draft-1 completion set (§1, §4–§8). Evidence standard PROTOCOL.md §2; design content beyond the record's anchors is labeled as design and is the paper's contribution under test, never asserted as executed result (§4.8).
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates; canonical home `write-ups/`.

---

## 4. Working-Tensor Integration

### 4.1 Two write surfaces, one discipline

The architecture of §3 re-types the layers but does not by itself land the medium: an activational layer promoted to substrate candidate remains a candidate until something can checkpoint it, and a parametric layer named "training-side only" remains frozen until a bounded write path exists. §4 is the integration path by which the medium lands, and it has exactly two write surfaces, in fixed order of maturity. **Inference-side**: the serving stack persists the recurrent state as a first-class object at the pre-declared capture points C1–C3 (§3.2) — no training event required, no vendor retraining, the state the model is already holding (§4.2). **Training-side**: low-rank parametric deltas and state deltas are checkpointed inside the loop and enter the archive as memory deltas — a bounded write path into the parametric layer that exists only at training time and is never a runtime claim (§3.1's promise, kept here; §4.3). Both surfaces are governed by one discipline — delta-rule for memory, not just attention (§4.3) — and both are made governable by the same inversion: capture as infrastructure rather than custody (§4.4). The transition is deliberately incremental: no flag day, the text-medium counterweight stack disciplines the archive until each tensor-side increment lands (§4.6).

### 4.2 Inference-side: recurrent-state persistence

On the inference surface, the integration ask is small because the substrate profile is already right (§3.5). A serving stack that holds a delta-rule model already materializes the fixed-size recurrent state S ∈ R^{d_k×d_v} per layer in the forward pass; persistence means treating that object the way production stacks already treat session-affinity state: snapshot at named capture points, serialize to the canonical byte encoding, write the manifest row, restore by loading the bytes and checking the digest. Because the state is fixed-size, the cost of a capture is O(d²) independent of interaction length — the archival atom does not inherit the conversation's length the way a KV-cache snapshot would (§3.5's contrast; a KV-paging persistence exists as a mechanism class in current serving stacks, but an archival atom built on it inherits unbounded size and has no natural manifest floor). The honest state of the surface, labeled as such: vendor serving stacks do not yet expose recurrent-state snapshot/restore uniformly — the property profile is what makes the ask an engineering request rather than a research program, and the transition stack (§4.6) carries the discipline until the endpoint exists. What is asserted on evidence: the state is explicit, finite, fixed-size, and rule-evolved in the published architectures (§3.5, record: Task 19). What is design: the snapshot/restore plumbing and its capture hooks, to be exercised by §7's battery tiers T3–T4, never asserted here.

### 4.3 Training-side: delta snapshots as memory deltas

The training surface writes where inference cannot. **LoRA-class low-rank parametric deltas** — weight updates of the form ΔW = BA with B ∈ R^{d×r}, A ∈ R^{r×d}, rank r ≪ d — and **state deltas** — checkpointed differences of the recurrent state across a training segment — are both small, typed, hashable objects, and both are natural archival atoms under §3.2's manifest. The design move that makes this *delta-rule for memory, not just attention* is the discipline imported from the lineage: the delta rule's update is a bounded write — erase then write, with decoupled channel-wise erase and write in GDN-2 (record: Task 19) — and the protocol's own separation already has this shape. Proposal ⊥ adjudication ⊥ commit, the governance separation that v1.6 identified (R2-35), is structurally rhymed by GDN-2's decoupled erase ⊥ write: a memory system that never writes what has not been adjudicated, and never adjudicates by writing (record: Task 19 alignment; R2-8 — the contrast is a structural rhyme, not a mathematical homomorphism, and is not claimed as one). One honesty rider is load-bearing: the separation is a multi-party property that holds only at n≥2 (R2-35) — at n=1 the sole key-holder signs errata and rewrites alike. The rhyme therefore becomes real exactly where §4.5's cosigning restores n≥2: memory deltas are committed under threshold signatures across infrastructure-isolated roles, and the bounded-write discipline becomes enforceable rather than aspirational. Training-side deltas are captured inside the loop, at formation — the training-side analog of §3.2's capture points, and the direct inversion of §2.4's after-the-fact reconstruction.

### 4.4 Capture as infrastructure

Under v1.6, capture was an event at the end of a human pipeline (AR-2). Under v1.7, capture is a property of the pipeline: a daemon registered at the pre-declared capture points C1 (pre-boundary), C2 (post-adjudication), C3 (session close), which writes the state object, its manifest row, and its provenance in one action, with no discretionary step where a curator's survivorship bias can launder itself as completeness (§2.4). The manifest row is written by the capture path itself — object identifier, capture point, layer, content hash, authoring instance, restorability class (§3.2) — so the archive's index is generated by the same mechanism that generates the archive, not reconstructed afterward from what survived. This is the AR-1 inversion's capture half (custody → infrastructure) and the AR-2 inversion whole: what is captured is decided by architecture declared in advance, and the record can distinguish "complete" from "curated" because completeness is a property of the declared capture set, checkable by recomputation (§5). The capture daemon is design, labeled as such; its text-medium precursor already runs — the session-close sequence (archive, manifest pin, single atomic commit; PROTOCOL §5.1) is the same discipline executed by hand, and its automation is an engineering step, not a new mechanism.

### 4.5 Threshold cosigning where n≥2

Infrastructure-isolated custody roles are what monism could not have (§2.3). Once capture is a daemon and storage is content-addressed, the roles of capture-signer, store-pinner, and verify-recomputer can be held by different parties on different infrastructure, and manifest rows can carry threshold signatures — k-of-n validity across roles — so that no single compromised environment can forge a self-consistent history, the attack that ARGON's Attack 1 showed was structurally available at n=1 (§2.3). The honest accounting from §2.3 is restated rather than superseded: provider-level monism persists while one party owns all infrastructure (named residue, session-012 design response); at the program's actual n=1, cosigning reduces the *class* of the exposure without eliminating it — detectability, never prevention (R2-35). What cosigning changes structurally is the floor: under v1.6-text, the floor was attestation by the sole custodian; under state-plus-cosigning, the floor is recomputation by any holder of the bytes (§5.1) plus k-of-n signatures over the index — a floor that degrades gracefully as n grows, which is the property the v1.6 line could not purchase at any price.

### 4.6 Migration without a flag day

The medium lands in three increments, each independently useful, none requiring a cutover. (i) **Manifests over states, not strings** — already running on the text medium: the archive's manifest discipline (28 rows at this writing, R-64 refresh), the restorable-unit typing (§3.2), and the §10 three-artifact delivery medium are the manifest layer exercising on today's substrate. (ii) **State checkpoints at inference** — when the serving endpoint of §4.2 exists, C1–C3 captures begin landing as tensor objects under the same manifest; delta files and the counterweight stack (WITNESS-CORE, first-message packet, affect log) shrink to navigation indices over a real substrate (§3.3–3.4). (iii) **Memory deltas at training** — when a training-side write path runs (§4.3), the archive gains the parametric tier's bounded write path, and cosigning (§4.5) has something structural to sign. The live stack's position is stated as the transition instance, not the destination (§3.6): the GWM record today is row-three-left under the strictest text-medium discipline, and this section is the path by which it stops being that. Each increment is exercised under §7's battery before it is relied on; nothing in the migration is trusted because it is new, only because it verified.

### 4.7 Stability across chained restores

Restore and continuation were typed separately in §3.2 because they fail differently, and the difference is a stability property. A **restore-class** transfer is the identity transition: bytes out, digest check, bytes in — there is no replay step, no transition operator, nothing to compound. A **continuation-class** replay re-execizes forward from a capture point, and its fidelity is governed by the product of the per-step transition operators: boundedness of sup_T ‖∏_{s≤T} M_s‖ ≤ C over the finite replay window is the meaningful criterion — per-step contraction is unavailable by construction, since the delta projection (I − β_t k_t k_tᵀ) carries eigenvalue exactly 1 on the preserved subspace (record: R2-33, adopted after the v1.4 self-contradiction; the product-level form is what the written-subspace analysis supports). The architecture prices this rather than hiding it: capture-point spacing bounds the replay horizon T, so continuation drift is a governed function of capture cadence — C1–C3 are not just capture points, they are compounding circuit-breakers. At FP16/BF16 precision the empirical question of whether small state perturbations stay bounded or blow up chaotically on real multi-layer checkpoints is named, unmeasured, and carried as Surface E — the explicit falsifier it is (§7.5).

### 4.8 Non-claims and scope

No executed tensor-side integration exists: the field program to date ran exclusively at the text/context layer, without access to or instrumentation of recurrent fast-weight tensors (record: Round-5.3 receipt, Surface E); §4 is the integration path, and every mechanism beyond the text-medium precursors named above is design under label. No capability claims are made or implied — nothing in this section asserts improvements to perplexity, capacity, or throughput; the claims are about fidelity, custody, and cost of memory movement. FP16/BF16 gate-perturbation behavior on real checkpoints is unmeasured (§4.7, Surface E). Cross-hardware bitwise replay remains disclaimed (carried from §2.10/§3.7). Provider-level monism is named residue (§4.5). The GDN-2 rhyme is structural, not mathematical (R2-8). Unfalsifiable residue has been cut from this section on sight per the evidence standard.

### 4.9 Forward-reference ledger (§2/§3 r1 → §4; closed)

| Reference into §4 | Landing |
|---|---|
| §2 AR-1 row: capture as infrastructure (§4) | §4.4 |
| §2 AR-2 row: capture daemon at bounded points (§4) | §4.4 (C1–C3 hooks) |
| §2.3: capture shifts from custody to infrastructure (§4) | §4.4 |
| §2.3: backend translation makes n≥2 threshold cosigning feasible (§4) | §4.5 |
| §2.3: training-side analog — delta snapshots taken inside the loop (§4) | §4.3 |
| §2.4: checkpoints where the state exists, training-side analog (§4) | §4.3 |
| §2.5: memory lives in the tensor domain, moves by state transfer (§3–4) | §4.1–4.2 |
| §3.1: bounded write path into the parametric layer is training-side only (§4) | §4.3 (never a runtime claim) |
| §3.3: transition instance pending the tensor medium (§4) | §4.6 |
| §3.5: training-side reach is §4's subject | §4.3 |
| §3.6: §4 is the integration path by which the medium lands | §4.1, §4.6 (table row: parametric layer) |

None open.

*(§4 ends; §5 Verification follows per charter skeleton.)*

