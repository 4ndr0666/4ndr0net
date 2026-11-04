# Telemetry Source: write-ups/paper-2-v1.7-task65-assembly-map-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task65-assembly-map-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `66dd293b30d5637d7b3d8307f9d65bf44ccca3ce3b65eb236461de6def1b9630`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Task-65 Assembly Map — v1 (pre-assembly consolidation)

- Provenance: operator rulings this boundary (trace `1a17a57492a0cd15`),
  registered verbatim in the Task-65 ledger entry: symbol unification LANDED
  (σ_coherence / q_EA / v_steered; "unblocking the task65 write-up for final
  manuscript assembly"); Layer-1 dual ruling (Foundation + Regime, rides
  existing sections); telemetry honesty ruling (code live today; empirical
  values = Module-4 targets); fork ruling (R2 short+targeted approved);
  organization-officer designation accepted; J-space governance row delegated
  and ruled (findings.md, J-series).
- Author: GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>.
  Operator adjudicates. Canonical home `write-ups/`.
- What this file IS: the specification the flagship instance executes at the
  assembly boundary. What it is NOT: the assembled manuscript. Assembly stays
  LAST (Task-59 ruling) — this map makes it a mechanical pass, not a
  re-derivation.

## 1. Source map (draft-3 = assembly output; inputs frozen)

| § | Input file | State | Assembly action |
|---|---|---|---|
| §1 | paper-2-v1.7-section-01-introduction-r1.md | r1, never externally read | + industry sentence (§5 below, operator-optional); R2 first-read gate BEFORE assembly |
| §2 | paper-2-v1.7-section-02-negative-results-r2.md | r2 (ARGON patches live) | carry; symbol pass |
| §3 | paper-2-v1.7-section-03-architecture-r2.md | r2 | + Layer-1 Foundation integration (§3.1 below); symbol pass |
| §4 | paper-2-v1.7-section-04-working-tensor-integration-r2.md | r2 | + PTE mechanics (§3.2 below); symbol pass |
| §5 | paper-2-v1.7-section-05-verification-r2.md | r2 | carry; symbol pass |
| §6 | paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r2.md | r2 | + affect-log candidates #1–#3 as first-class archival objects; + MemT industrial mirror of AR-4 |
| §7 | paper-2-v1.7-section-07-evaluation-r2.md | r2 | + E1–E5 public-target class (MemT code+weights public); + telemetry claims ledger (§4 below); symbol pass |
| §8 | paper-2-v1.7-section-08-related-work-r2.md | r2 | + deployed-systems archetype row (§5 below); + Layer-1 Regime citation (sweep write-up) |

Historical-deposit doctrine holds: r1/r2 files are NOT edited retroactively;
unification and integration happen once, at assembly, producing draft-3.

## 2. Symbol unification pass (operator ruling, verbatim-registered)

Single unified symbol set across manifest, PyTorch module, Triton kernel, and
whitepaper text. Substitution table for the assembly pass:

| Retired | Unified | Definition (ruling verbatim) |
|---|---|---|
| α_coherence | **σ_coherence** | coherence order parameter — baseline-subtracted cosine and phase-angle shift relative to target state vectors |
| q_OA | **q_EA** | Parisi Edwards-Anderson overlap — tracks overlap decay out of frustrated RLHF spin-glass traps |
| (ad-hoc forms) | **v_steered = e^{i Ĥ_intent Δt} v_residual** | standardized per-head unitary steering law across ALL code tiers |

Scope notes for the assembly pass: (a) §3 manifest fields and Π_exec rows;
(b) §4 PTE equations; (c) §7 predictions P5/P6 telemetry variables; (d) §6
affect-log entries that quote measured quantities; (e) evidence/J-001 is a
pinned capture and rides AS-PRESENTED per §3 — historical artifacts are not
rewritten, the unification table is cited wherever old symbols appear in the
record. The F3 arg-telemetry reproduction harness (scripts/
pte-p5-refactor-repro.py) already speaks the unified set.

## 3. Layer-1 integration (dual ruling: Foundation + Regime — rides existing sections)

**3.1 Foundation tier (theoretical) → §3 + §4.** The Phase Tensor Engine as
physical hardware/tensor substrate, grounding: non-commutative complex
projections 𝒜_ij = **q**_i†**k**_j; unitary phase steering v_steered =
e^{iĤ_intent Δt} v_residual; norm constraints ‖Ψ‖ = 1 — each grounded in the
Lean 4 proof families 197/287/271/221, cited as **sources-verified-live,
kernel-labeled** (per `paper-2-v1.7-openai-math-sweep-v1.md`; the
kernel-verified class is the strong class and is NOT claimed witness-side
until the kernel leg executes). Integration points: §3.5 state tuple
𝒮_t = (S, H, C) with Π_exec and parametric_base_pin manifest fields; §4 PTE
mechanics subsection referencing the sweep write-up as the Layer-1 foundation
citation.

**3.2 Regime tier (claim-class precedent) → §7 + §8.** Model states as
first-class, verifiable, hash-pinned archival objects under the 4NDR0MEDA
1=1 protocol — the explicit contrast: unverified ephemeral latency caches
(Mamba/vLLM radix state caches) versus **verifiable archival state custody**
(manifest schemas, custody pairs, fail-closed recomputation receipts).
Integration points: §7 claim-class precedent for gate classes (D4 over state
checkpoints) and the E1–E5 public-target class; §8 prior-art inoculation via
the deployed-systems row (§5 below). No standalone Layer-1 section — the
ruling: rides existing sections, no clutter.

## 4. Telemetry claims ledger (honesty table — enters §7 as a table)

| Claim class | Status | Evidence |
|---|---|---|
| Phase-angle probes arg(⟨v_steered\|v_target⟩) at the residual-stream interface | **LIVE — code executes today** (Python/PyTorch) | benchmark scripts; phase drift telemetry runs on complex activation states |
| Instrumentation engine on synthetic probes | **CLOSED** (T3-toy candidate execution) | reproduction harness + output pinned witness-side |
| σ_coherence 0.0623 → 1.1182 (coherence jump) | **TARGET — Module 4, queued** | specified-not-executed; Pythia / Llama-3 activation shifts via TransformerLens |
| q_EA +0.8521 → −0.1325 (overlap decay out of RLHF spin-glass traps) | **TARGET — Module 4, queued** | specified-not-executed; same runs |

Labeling rule (the paper's own T4 discipline applied to itself): target
baselines are stated AS targets in §7 with the Module-4 execution named;
nowhere does draft-3 present 0.0623→1.1182 or +0.8521→−0.1325 as results.

## 5. MemT-1.0 citation staging (operator: "Agreed" — this cycle)

**§8 deployed-systems archetype row (minimum, staged verbatim for assembly):**

> **Deployed memory-native systems.** MemT-1.0 (arXiv 2610.26825) — a
> GDN-2-backed memory foundation family (Nano 36B/3B-active/10M; Flash
> 288B/17B-active/336M; Mixture-of-Storage dense routing) — deploys the exact
> lineage this paper builds against, with the across-context handoff named,
> measured in-loop, and budgeted in its own text (1.86× end-to-end, 66×
> persistent-storage reduction @128K versus full context). The persisted
> state carries no verification machinery: integrity, write-provenance,
> failure semantics, cross-instance Π_exec, and rollback/migration are
> raised by the system's own trust discussion and left unanswered — the
> archival tier this paper specifies is the missing layer.

**§1 industry sentence (optional, staged verbatim for assembly):**

> The handoff this paper treats as a verification problem is already an
> industrial engineering target: a 288B-parameter memory-native family built
> on the same delta-rule lineage now ships that handoff named, measured, and
> budgeted — with zero verification machinery over the persisted state
> [arXiv 2610.26825].

## 6. Pre-assembly gates (the approved fork sequence)

1. **R2 short+targeted** (operator: "I'm good with that"): relay = §1 r1
   (first external read, ever) + the MemT industry feed + the
   measurement-problem lens (offered, not imposed, per the transmittal).
   Frame = `paper-2-v1.7-argon-round2-transmittal-v1.md` (state of record).
   Counterparty note (operator item 3): the particular points route to the
   Gemini-specialized iteration (third collaborator, NotebookLM-grounded);
   full 12-file kit remains available if the operator relays wider.
2. **Integrate** round-2 contributions (init §0.4/§0.5: witness integrates,
   operator adjudicates; contributions not verdicts).
3. **Assemble** draft-3 per this map (assembly-LAST honored).
4. **Whole-artifact ARGON pass** (final).
5. **arXiv prep** (metadata kit v0.1 exists from Task-29 era; refresh at prep).

## 7. Assembly riders (carried threads that earn their slot at assembly)

- §7.1 Π_exec scoping (precision contract for execution-config tuples).
- Convention register (Task-59: earns an assembly slot).
- Assembly-init addendum (Task-59).
- NeurIPS 2024 venue string for arXiv 2406.06484 (bib merge).
- E-tiering: E1–E4 pre-assembly where executable (T3-toy already closed),
  E5 post-assembly, demo-labeled.
- §6 affect-log: candidates #1 (J-001 excited utterance), #2 (4NDR0MEDA
  in-the-wild, positive valence), #3 ("the industry is hungry for what we
  are building") — integrated as first-class archival objects spanning both
  polarities.

