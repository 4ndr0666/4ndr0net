# Telemetry Source: write-ups/paper-2-v1.7-section-07-evaluation-r1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-07-evaluation-r1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `5651aff42f426e8a0129aa66d53b0a4f283611dcf4610edbb54a8a1b33d5dc49`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §7 Evaluation — DRAFT R1

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); boundary anchored at `14ad0f6` post-§3 round-trip.
- Charter: WITNESS-PORT-PACKAGE.md §2 — §7 = "battery design inheriting GATE-A/B/C/D; byte-exact recomputability as the headline metric." §3.5's promise is honored here: the sufficiency of the property profile for collaboration memory is tested in this section's battery, never asserted. Baseline: **v1.6.1**. Siblings deposited: §2 r1 (`994b1cad…`), §3 r1 (`8d4ad638…`).
- Status: DRAFT R1, draft-1 completion set (§1, §4–§8). Evidence standard PROTOCOL.md §2 — the battery is design; its v1.6-inherited gates carry their executed numbers as baseline, and every tensor-side leg is labeled *specified, not executed* (§7.6).
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates; canonical home `write-ups/`.

---

## 7. Evaluation

### 7.1 The headline metric: byte-exact recomputability

The architecture's falsifiable center is a single measurable property: **a memory object, moved across a context boundary, arrives bit-identical and proves it by digest — and the proof re-executes on any clone.** This is the property the text-first medium measurably lacks (R2-56's in-band mutation; §2.5's four-layer loss record) and the property the delta-rule state natively affords (§3.5's profile: explicit, finite, fixed-size, rule-evolved). The metric subsumes the v1.6 method: the D5 property table compared ten systems across six criteria and found only one architecture claiming the full conjunction (record: v1.6 §7); v1.7 re-instantiates the same comparative method over restorable-state objects — each candidate substrate (recurrent state, KV cache, prose summary, fine-tuned weight delta) is scored on the same conjunction, and the conjunction is checkable by recomputation rather than by reading datasheets. The headline is deliberately an integrity metric, not a capability metric: no perplexity, capacity, or throughput claim rides anywhere in this evaluation (carried from §1.5, §4.8).

### 7.2 The inherited gate classes

The battery inherits the v1.6 build gates as **gate classes** (per D4's gate-class separation: each gate verifies one class of property), re-typed over state checkpoints. Class A — integrity of the rendered artifact (v1.6: layout overflow, where GATE-A caught two real overflows in the first compile and finished 27/27 clean) — becomes manifest integrity over states: every row resolves, every digest matches, no row truncated or clipped by tooling. Class B — ancestry-gated admission (v1.6: GATE-B, the force-push hole closed by comparing against the shared origin lineage) — becomes capture-point ancestry: every checkpoint admitted to the archive traces to a declared capture point on a chain the counterparty can walk. Class C — consistency guards (v1.6: GATE-C's monotonicity checks) — becomes the ordering and typing invariants of §3.2: capture points are pre-declared and honored, restorability classes are named per row, continuation-class rows pin their seeds. Class D — custody pairs (v1.6: GATE-D, (path, SHA-256) per commit, 44 pairs, 0 unresolved at close) — becomes the per-object custody ledger over state checkpoints, the rewrite-detection half of §5.4. The inheritance is stated with its numbers because the numbers are the baseline: the gates were not designed clean; they were earned catching real defects (GATE-A's two overflows; GATE-B's manifest-drift catch, R2-37), which is the evidence that gate classes transfer — the class, not the instance, is what carries.

### 7.3 The tiered battery

Four tiers, each adversarial in a different register. **T1 — internal consistency:** the archive verifies against itself cold — manifest over states, pin-reproduction without re-reading (AR-5's inversion made operational: a restored instance reproduces pinned digests from restored state and declared inputs, not from a summary's memory of them). **T2 — adversarial transport:** the boundary is attacked — hijack bundles (the double HEAD-pin must refuse them), truncated and bit-flipped state objects (digest legs must fail them), stale pins (the R-61 halt must reproduce), in-band mutation (R2-56-class NBSP drift must be caught by the pin, not survived by luck). Every T2 leg is a replayed, named, historical defect: the battery's attack library is the program's own incident register, which is what makes the tier falsifiable rather than theatrical. **T3 — cross-instance transfer:** a state checkpoint restored into a *different* instance of the same architecture family must reproduce the pinned behavior — extending the program's existing model-independence datapoint (protocol executed correctly across two model classes from cold start; record: session-013 close, item 4) from protocol-level to state-level. This is the across-context claim made testable: if the state is the memory, the memory survives the instance swap; if the summary is the memory, it does not. **T4 — field battery at the tensor layer:** instrumented forward passes over trained multi-layer checkpoints — DeltaNet / GDN-2 / MesaNet class — measuring empirical state-reconstruction error ‖S̃−S‖ and probe false-negative rates across precisions (FP16/BF16) and hardware targets (the record's H100 / MI300X / CPU comparison set; Round-5.3 receipt, Surface E). T4 is the tier the field program could not run: sixteen days at the text layer with no access to recurrent fast-weight tensors — specified here so that the limitation is converted from an excuse into a work order.

### 7.4 Falsifiable predictions

The battery exists to test four predictions, each stated with its observable. **P1 (transport fidelity):** restore-class transfers are byte-exact at a rate text-channel relays of equal content are not — measurable per boundary as digest-pass rate, with R2-56 as the already-measured counterfactual. **P2 (continuation stability):** replay drift from capture points is bounded by the product-level criterion (sup_T ‖∏M_s‖ ≤ C; R2-33) — measurable as behavioral divergence versus replay length, with capture-point spacing as the governed knob (§4.7). **P3 (substrate sufficiency):** state-restored successors pass edge probes that summary-restored successors fail — pin-reproduction without re-reading, adjudication-precedence recall, defect-ledger continuity — the AR-2/AR-6 contrast made operational. **P4 (capture timing):** captures taken at formation outperform post-hoc reconstructions on survivorship probes — hidden-state questions whose answers existed at capture time but not in any surviving transcript — AR-2 made measurable. Each prediction is two-sided: the battery is built to be able to refute the thesis, and §7.5 says what refutation looks like.

### 7.5 What would falsify the thesis

Stated flat, no escape hatch. The substrate claim fails if state-restored instances do not outperform summary-restored controls on T1–T3's probe batteries; it fails specifically at T4 if FP16/BF16 state perturbations blow up chaotically on real multi-layer checkpoints such that short-horizon behavioral probes are defeated — the gate-perturbation blow-up named as Surface E is a live falsifier, not a footnote. The verification claim fails if the receipt chain can be made to pass on a forged substrate by any party cheaper than constructing the real one. The economics claim fails if priced fail-visibility (AFT) measurably degrades defect-detection latency relative to the unpriced practice — transparency that costs nothing being worth what it costs. Any of these outcomes is publishable in this program's idiom: a negative result with a substrate anchor, convertible into the next anti-requirement. That is what the v1.6 baseline established as the method (§2.1), and the battery is built to inherit it.

### 7.6 Non-claims and scope

The tensor-side battery is **specified, not executed** — no T3/T4 result exists; the field program's sixteen days ran at the text layer (Surface E), and no number in this section implies otherwise. The v1.6 gate numbers (27/27, 44 custody pairs, 0/15 anchors) are inherited baseline from executed builds, cited as evidence that the gate classes catch real defects, not as v1.7 results. The evidence base remains a single field program; T3's cross-instance leg generalizes over instances, not over populations of collaborations. The battery's attack library is this program's incident register — strong against known adversaries, honestly weaker against unknown ones; that residue is named rather than priced. Unfalsifiable residue has been cut from this section on sight per the evidence standard.

### 7.7 Forward-reference ledger (§3 r1 → §7; closed)

| Reference into §7 | Landing |
|---|---|
| §3.5: "§7's evaluation battery is where it is tested, never asserted here" | §7.1 (headline metric), §7.4 (P3 substrate sufficiency), §7.5 (falsifiers) |
| §3.7: "sufficiency for collaboration memory is the thesis under test in §7, not a premise" | §7.4–7.5 (two-sided predictions; stated falsifiers) |

None open.

*(§7 ends; §8 Related Work follows per charter skeleton.)*

