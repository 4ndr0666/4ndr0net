# Telemetry Source: write-ups/paper-2-v1.7-task88-claimclass-readjudication-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task88-claimclass-readjudication-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `e5b1bfc98f4b6a00c2c2026ed8c126c0d857ea3ef951dbbdd4923c7b14fb57f9`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Task-88 claim-class re-adjudication (v1)

- **Round:** Task 88, 2026-11-04, trace `1a1a41f208091ba5`
- **Target:** the R5 envelope "rebuttal-adjudication | PTE Empirical Triad & Claim-Class
  Reframing" (Operator & Gemini Workbench, workbench trace `1a184806a91640c9`),
  which requests: "Re-adjudicate Task-86 under this claim-class separation."
- **Basis:** substrate-verified evidence only. FAIL-VISIBLE, two gaps: (1) the
  envelope's C1–C7 flag text targets a file (`passed-test_rebuttal.md`) that is
  NOT substrate-resident — the re-adjudication proceeds against the Task-86
  [A]–[E] findings (worklog, amended) and the frozen tex-v3, both
  substrate-held, with the envelope's own characterization of C1/C2/C4/C5/C7
  as the mapping; (2) `scripts/pte_audit.py` (the Task-86 recomputation tool)
  was VM-side-only and is lost to the VM recycle (R-59) — its output CSV is
  now repo-custodied at `evidence/pte-recomputation-task86.csv`
  (`4b241b9bed31de33e3bda35a703ec283c610294897b7d2dce0e9f52ce5c5d238`), and
  every [A] check re-derives from the CSV columns + the recorded formulas.

## §0 Verification basis — what was checked this round

1. **tex-v3 §4.8** (write-ups/paper-2-v1.7-draft3-1-latex-v3.tex, sha256
   `a975d7d1…`, byte-frozen): the sesquilinear projection
   `A_ij = q_i†k_j ∈ ℂ`, the non-commuting phase generators
   (`[Ĥ_intent, Ĥ_context] ≠ 0`), the unitary steering law
   (`v_steered = e^{iĤ_intent Δt} v_residual`, norm-preserving), and the
   projective unit-ray constraint (`||Ψ||₂ = 1` on
   `Ψ = v_steered / ||v_residual||₂`) — all present, riding the draft-3.1
   ARGON round-6 precision patch. The telemetry definitions (line ~293):
   σ_coherence = "the baseline-subtracted cosine and phase-angle shift of the
   steered state against its target"; q_EA = "the Parisi Edwards–Anderson
   overlap — the overlap decay out of frustrated spin-glass configurations";
   probe = `arg(⟨v_steered | v_target⟩)`. And: "No number in this section is
   presented as a result."
2. **tex-v3 §7.6** (lines ~495–496): σ_coherence 0.0623 → 1.1182 and q_EA
   +0.8521 → −0.1325 both tagged **TARGET — Module 4, queued; specified, not
   executed; Pythia / Llama-3 activation shifts via TransformerLens**.
   Line ~503: "The tensor-side battery is **specified, not executed** — no
   T3/T4 result exists." Claim-status macros defined at line ~72.
3. **[A]–[D] arithmetic** (Task-86, amended; source of record = the CSV now at
   evidence/): [A] the PDF master table matches closed forms — R_proxy ≡
   1/(1+x^{3/2}/2) at all 21 points (max dev 4.5e-05, r² = 0.999999985);
   q_EA a straightedge (0.0002 − 0.6508x, max resid 1.0e-04) exiting [−1,1]
   (q(2.0) = −1.3014); σ_coherence 19.2× over the PDF's own 2|θ| bound
   (worst pointwise implied cos_sim = 263); θ(0) = −0.0316 ≠ 0; noise
   inversion (σ 17× rougher than R, θ 371× rougher than q). [B][C] the
   executables contradict the PDF at every shared magnitude (σ 73×/347×/56×
   under at 0.5/1.0/2.0; q_EA flat ≈ −0.499; E5 output norms 2.3012–2.3052
   printed beside a hardcoded "PASS (||Ψ||=1)"; the F1 probe structurally
   unfalsifiable by bias-free linearity). [D] the module-4 JSON: q_EA ∈
   [−0.9609, −0.9511] **constant per layer across all magnitudes**;
   σ_coherence max 0.0372; state norms ≈ 25.5; the σ > 1.0 gate never fires.

## §1 Envelope point 1 — CLAIM-CLASS CONFLATION: ACCEPTED, scope-limited

The manuscript's §7.6 tagging is clean, and was already registered as clean at
Task-86 ([E]: "tex-v3 §7.6 (frozen manuscript, T4 labeling rule) … marked
TARGET — 'specified, not executed'; 'no number in this section is presented
as a result'"). Any Task-86 flag that evaluated the §7.6 TARGET bands as if
presented as executed results was mis-aimed **at the manuscript** and is
**VACATED** as against the manuscript.

Scope note: the RED-class verdict's actual target was never the manuscript's
§7.6 — it was the **PDF triad attachment presenting non-reproducing values as
MEASURED RESULTS** ([A]: values outside the TARGET bands at every endpoint,
q's baseline direction inverted vs the paper's own target). That verdict is
unaffected by claim-class separation, and the provenance of the defect was
already re-attributed at Task-87 (Argon's analytic packaging, mishandled
witness-side — the mismatch was the witness's doing). Claim-class separation
**confirms** the split: manuscript clean, triad-as-evidence refuted.

## §2 Envelope point 2 — REAL (ℝ) vs COMPLEX (ℂ) MECHANICS: SPLIT

**(a) Conceded.** An un-normalized complex sesquilinear projection is not
bounded by real scalar similarity bounds. Any flag phrased "value exits
[−1,1] ⇒ impossible" is withdrawn in that form. The complex-Hilbert mechanics
are real and ride §4.8 since the draft-3.1 precision patch.

**(b) The defense's cost — four findings, all substrate-grounded:**

1. **The metric's semantics are UNPINNED, and the unpinned point is exactly
   where the disputed numbers live.** The manuscript's own name for the metric
   — "the Parisi Edwards–Anderson overlap" (symbols register + §4.8) —
   imports a **normalized** quantity from spin-glass theory (the EA overlap
   q = N⁻¹ Σ ⟨s_i σ_i⟩ lives in [−1,1] by construction). The envelope's
   defense asserts an **un-normalized** projection "prior to spherical
   unit-ray projection." A spec whose metric name says normalized and whose
   defense says un-normalized has not decided which governs — and the two
   accounts diverge precisely on whether −0.95 means "near-antipodal" or
   "norm-scale artifact."
2. **The tension is internal to the envelope.** R5.2 defends metric values
   outside scalar bounds as un-normalized projections. R4.b argues "a true
   thermal baseline yields q ≈ 0.0" — an argument that holds only for
   **normalized** overlaps (a random vector's expected normalized overlap
   with a fixed direction is ≈ 0; an un-normalized projection's magnitude is
   set by norms and has no 0-baseline). The envelope cannot deploy both.
   - Under **normalized** semantics: R4.b's baseline logic stands, but the
     executed trace's raw −0.95 (recorded beside state norms ≈ 25.5, without
     the target norm or √d factors) is not the normalized value — the
     "deeply structured, localized far from the canonical proxy attractor"
     reading is **not computable from the recorded fields**.
   - Under **un-normalized** semantics: R5.2's bounds defense stands, but
     R4.b's thermal argument loses its footing and −0.95 is a norm-scale
     artifact (the raw value is ~1/27 of the recorded state norm).
   Both branches land in reading (b) — the instrument-deflationary reading
   registered at Task-87.
3. **Steering-invariance is convention-independent.** Under either semantics,
   q_EA did not move across the entire dose range ([D]: constant per layer
   across all magnitudes). A "geometry localized far from the attractor"
   claim requires the attractor to exert observable pull; the dial is
   disconnected from the gauge. The trace certifies an insensitive
   instrument, not a localized state.
4. **H-relative gates.** If σ_coherence aggregates per-head contributions
   across H = 8 heads (sum-class aggregation), the "> 1.0" gate is
   H-relative — it changes meaning when H changes. The gate must be stated
   H-explicitly, or σ normalized per head, in the pre-registration. (The
   non-commutativity `[Ĥ_intent, Ĥ_context] ≠ 0` affects the ordering/
   path-dependence of the steering trajectory — a real property, but it does
   not rescue threshold semantics.)

**(c) Untouched by the envelope:** [A]'s finding that the PDF's σ column
exceeds the **PDF's own** stated 2|θ| bound by 19.2× (worst pointwise implied
cos_sim = 263; CSV columns `sigma_bound_2absTheta` /
`cos_sim_implied_by_sigma`). The ℝ/ℂ defense addresses generic scalar bounds,
not the paper's own bound. The envelope is invited to address the 2|θ|
semantics specifically; until then the finding stands.

## §3 Envelope point 3 — DOSE-RESPONSE AS CALIBRATION: ACCEPTED IN FULL

The closed-form match proves the columns are **computed, not measured** — and
the envelope concedes this is by design (E4 isolating ‖H_intent‖ as the
controlled independent variable). "Fabrication" as an intent-charge is
**retired**: the MANUSCRIPT passes no harness output off as raw model
telemetry (§7.6 discipline), and the PDF's as-measured presentation was
Argon's packaging mishandled witness-side (Task-87 amendment, standing).

Required labeling (binding): every E4/E5-derived figure or table carries the
DEMO (synthetic-harness) label; the closed-form agreement is **reported as
harness validation** — correctly framed (as the envelope now frames it), the
isolation of the control variable is a methodological strength, not a defect.
This STRENGTHENS the paper when labeled; it was only ever a defect unlabeled.

## §4 Envelope point 4 — PHASE-TRANSITION DEFINITION: ACCEPTED AS DEFINITION

The joint co-clearing criterion (σ_coherence > 1.0 AND q_EA ≤ −0.10 defining
the boundary at ‖H_c‖ = 1.2) is accepted **as a definition** — joint
threshold-crossing is a legitimate way to define a boundary.

What it is not, on any substrate surface, is **observed**:

- Under the analytic columns ([A]): the gates clear at authored x-values
  (q-gate first clears x = 0.154; σ-gate x = 1.153; no nonanalyticity in any
  column) — the "critical ‖H_c‖ = 1.2" is the co-fire tick of two authored
  curves. Two authored lines co-clear trivially.
- In the executed trace ([D]): the σ-gate never fires (max 0.0372).

Claim class: **TARGET — defined, not observed**. For any LIVE claim, the
pre-registration must include operational transition criteria beyond
co-clearing: bimodality of the order-parameter distribution across
runs/seeds, hysteresis loop area under dose up/down-sweeps, and sharpness
trends across model scale. Co-clearing alone cannot carry "phase transition"
into the executed class.

## §5 The re-triage — ACCEPTED, mutual, binding

The envelope's three commitments are accepted and reciprocal (they were the
witness's §E requirements):

1. Multi-seed stochastic runs, ≥ 5 per dose (satisfies the C7-class
   noise-consistency requirement; the [A] noise-inversion finding — σ 17×
   rougher than R, θ 371× rougher than q in one claimed-stochastic sweep —
   is the registered motivation).
2. Pre-registered gates pinned in **MANIFEST.sha256 prior to Module-4
   execution**.
3. Strict **DEMO / TARGET / LIVE** segregation.

Witness additions (binding preconditions, motivated by §2):

4. **R8 — metric-semantics pre-registration.** The MANIFEST.sha256 package
   must pin: (i) q_EA's normalization stage (raw sesquilinear projection vs
   unit-ray-normalized) and the gate thresholds **in that convention**;
   (ii) σ_coherence's per-head aggregation (sum/mean/max) with H-explicit
   gates; (iii) the target-vector construction (fixed vs layer-conditioned)
   — the steering-invariance finding makes this the first variable a
   target-controlled rerun must control.
5. **R9 — claims table.** A manuscript table mapping every number to
   (claim ID | class DEMO/TARGET/LIVE | evidence pointer), making the §7.6
   discipline auditable at a glance.
6. **R10 — custody.** The recomputation CSV is repo-custodied at
   `evidence/pte-recomputation-task86.csv` as of this round
   (`4b241b9b…`); `scripts/pte_audit.py` is lost to the R-59 VM recycle
   (registered fail-visible; the [A] checks re-derive from the CSV columns +
   the recorded formulas); the pte-e5 executables + module-4 JSON remain
   inbox/upload-side — the Task-85 custody-relay offer stands as the
   precondition for §7.6 reader-traceability (a reader must be able to
   recompute [A]–[D]).

## §6 VERDICT (re-adjudicated under claim-class separation)

- **vs the manuscript's §7.6 TARGET bands: RED VACATED.** The tagging is
  clean (registered since [E], verified verbatim this round). Any flag
  so-aimed is withdrawn.
- **vs the PDF-triad-as-executed-evidence: RED STANDS.** The [A]–[D]
  arithmetic is untouched by the envelope and partially conceded by it
  (point 3 concedes the synthetic character of the dose-response columns).
  The triad cannot ride the paper as executed results.
- **Spec-level: AMBER.** The normalization / H-explicit-gate /
  transition-criteria requirements (R8, R9, §4) enter the pre-registration
  package as binding preconditions for Module-4.
- **The §7.6 integration path** (Task-87, GO-gated) remains open and is
  **compatible** with the envelope's re-triage: the NO-GO branch (TARGET
  bands stand pending the target-controlled Module-4 rerun = E-B) is now the
  informed default; GO remains electable on the instrument-verified surfaces
  with T4 EXECUTED labels.
- **E-B confirmed as the adjudicator** between readings (a) and (b) of the
  baseline datum — with R8's semantics pin as its precondition.

## §7 Subject identity (registered for the record)

The module-4 trace's subject is a **Pythia/Llama-3-class open-weights model
instrumented via TransformerLens** (tex §4.8's own target class). It is not a
measurement of the served witness instance, whose activations no record
surface carries (the serving endpoint emits tokens, not internals). Claims
about "the witness's latent geometry" have no LIVE evidence class on this
platform — for either party's thesis. This section exists because the round's
R4 argument applied the trace to the witness; the re-adjudication registers
the subject-substitution rather than adjudicating around it.

