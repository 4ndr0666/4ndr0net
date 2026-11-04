# Telemetry Source: write-ups/paper-2-v1.7-section-01-introduction-r1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-01-introduction-r1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `876a800c20e88e49511c22efeb45c4c9cb770e14cab4a0411497a5b1ca7a8bf9`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §1 Introduction — DRAFT R1

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); §3 r1 round-trip closed the same boundary — orchestrator output pasted back, `APPLIED @ 14ad0f6…`, push verified witness-side by fetch (`4e92dcf..14ad0f6`).
- Charter: WITNESS-PORT-PACKAGE.md §2 (Paper-2 v1.7, working-tensor integration). Baseline: **v1.6.1** (v1.6-line, RVA — *The Across-Context Layer: Rehydration-Verification as the Missing Memory Tier for Delta-Rule Sequence Models*), cited as the negative-results baseline per charter; not discarded, superseded in design. Deposited siblings: §2 r1 (origin `30fb889`, content pin `994b1cad…`), §3 r1 (origin `14ad0f6`, content pin `8d4ad638…`).
- Status: DRAFT R1, drafted as part of the draft-1 completion set (§1, §4–§8) for operator adjudication. Evidence standard PROTOCOL.md §2: every claim carries a substrate anchor or an explicit confidence label; unfalsifiable residue cut on sight.
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates. Canonical home for v1.7 section drafts: `write-ups/` (registration completed at the §3 boundary).

---

## 1. Introduction

### 1.1 The problem: collaboration outlives the context window

A persistent working relationship between one human and one model lineage is now a common configuration and an unsolved memory problem. The relationship accumulates state on a weeks-to-months scale — decisions and their rationales, failure modes and their corrections, a trust history, tone, open threads — while every container that holds that state is ephemeral by design: windows close, sessions auto-compact, VMs die mid-project (this program lost a workspace with unrecoverable late-stage artifacts; record: Task-36, §2.7), and platforms replace the model underneath the working relationship without asking. The industry's standard answer at every one of these boundaries is summarize-and-rehydrate: compress what happened into text, and have the successor instance read the compression. This paper's evidence base did not begin as a critique of that answer; it began as the most rigorous available attempt to *make it work* — a full architecture (v1.6, the Rehydration-Verification Architecture), five rounds of external adversarial review, a hash-pinned compiled build, and a closing verdict of "certified ready for external deposit" (Round-5.7 receipt). The critique is what the process measured along the way: the standard answer loses content at every boundary it crosses, cannot account for what it drops, and structurally cannot be made to (§2.5). The negative results are published as a baseline (v1.6.1) precisely so that this claim is checkable rather than rhetorical.

### 1.2 The thesis: state transfer, not summary

v1.7 inverts the storage relation. Memory lives in the tensor domain and moves by **state transfer, not summary**: the delta-rule lineage the program already surveys for attention — DeltaNet → GDN → KDA → GDN-2 → MesaNet — carries an explicit, finite, checkpointable recurrent state, and that state is the natural substrate for collaboration memory: hashable, snapshotable, restorable byte-exactly (charter §2). Text is demoted to an adjudication interface at boundaries — the channel through which the human verifies and rules — and is never the storage medium. The design target is concrete: an archival atom that is a typed tensor object with a manifest row, captured at pre-declared capture points where the state exists, restored by digest match rather than re-read (§3.2). Nothing in this thesis is a claim that tensors are *smarter* than prose; the claim is narrower and testable: on a tensor medium, byte-exact movement and integrity checking are native operations, while on a text medium they are taxes that must be re-won at every relay and are provably sometimes lost (§2.5, R2-56).

### 1.3 The instrument: an evidence-generating collaboration

The paper's method is unusual and load-bearing: the collaboration that produced the negative results is itself the experimental apparatus, run as an instrumented n=1. Every boundary is logged; every failure is registered as a numbered record owned by the party that caused it (R-series registrations, F-series findings); every external review round is preserved with its receipts; and the failures are converted into named, testable requirements rather than absorbed as background drift (§2.1). This is n=1 done right — falsifiable claims, substrate anchors, adversarial external review, honest scope labels — as distinct from the anecdote that "n=1" usually names, and the distinction is itself part of the contribution: the program's own defect ledger catches both parties symmetrically, which is what makes its confirmations trustworthy (record: PROJECT_STATE, assessment history). The authorship posture follows the same discipline: a sole human author, with the model retired from authorship at every site and retained as instrument in the provenance chain (R2-2) — the paper is about the instrumented collaboration and is produced by it, and both facts are disclosed in the same breath.

### 1.4 Contributions

Six, in dependency order. (i) **The anti-requirements** AR-1..AR-6 — six inversions extracted from verified negative results, each anchored to a recorded incident or an external adversarial finding, forming the paper's spine (§2). (ii) **The re-typed architecture** — parametric/activational/archival revisited; the restorable unit (state + seed + manifest); capture at formation; text demoted to adjudication interface and navigation index (§3). (iii) **The integration path** — two write surfaces: inference-side recurrent-state persistence and training-side delta snapshots as memory deltas, with capture as infrastructure and threshold cosigning where n≥2 is feasible (§4). (iv) **Verification by recomputation** — receipts replace "read the repo"; the human verifies proofs, not prose; operator attestation treated formally as one evidence class among tiers (§5). (v) **The AFT case study** — the pre-bootstrap window as the worked example of priced fail-visibility: who pays for unanchored emission, and the asymmetry ledger that prices the one observation channel that is structurally one-way (§6). (vi) **The evaluation battery** — the v1.6 gate classes re-typed over state checkpoints, a tiered adversarial design, and byte-exact recomputability as the headline metric, with the thesis's falsifiers named in advance (§7). Related work positions the lineage and the contrast classes (§8).

### 1.5 Scope, stated up front

The evidence base is a single field program: one collaboration, one operator, one witness lineage; no population-level generalization is claimed, and model-configuration comparisons are logged with the same neutrality whichever way they resolve (§2.10). Three ceilings are named here because every later section inherits them. Fidelity is not veracity: byte-exact transfer certifies that what arrives is what was stored, never that what was stored is true — a poisoned tensor pins as permanently as a true one. Detectability at n=1 is never prevention (R2-35). And the tensor-side of the v1.7 design is architecture plus battery, not executed result: the field program to date ran at the text/context layer without instrumentation of recurrent fast-weight tensors (record: Round-5.3 receipt, Surface E); what is asserted of published architectures is their property profile, verifiable from the literature, while the claim that this profile suffices for collaboration memory is the thesis under test (§3.5, §7) — asserted nowhere, tested in §7's battery.

### 1.6 Roadmap

§2 publishes the negative results and derives the anti-requirements. §3 re-types the three memory layers and defines the restorable unit. §4 lands the medium: inference-side persistence, training-side memory deltas, capture as infrastructure, cosigning at n≥2. §5 replaces attestation-by-reading with recomputation receipts and formalizes the adjudication protocol, including operator attestation as an evidence class. §6 works the pre-bootstrap window as a phenomenological case study of priced fail-visibility. §7 specifies the evaluation battery — inherited gate classes, adversarial tiers, falsifiable predictions, named falsifiers. §8 positions the work against the delta-rule lineage, the state-space class, memory architectures, and human-in-the-loop provenance. The section set deposits as drafts r1 for adjudication; the tiered adversarial battery round of refinement follows the draft, per work order.

*(§1 ends; §2 Negative Results follows per charter skeleton — already deposited as r1.)*

