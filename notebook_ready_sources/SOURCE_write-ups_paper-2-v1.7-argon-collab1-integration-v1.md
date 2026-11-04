# Telemetry Source: write-ups/paper-2-v1.7-argon-collab1-integration-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-argon-collab1-integration-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `011ce31b7fe7c2eab16cbc5242303f925b4690354c69f5a8f5531f69e1eda326`

---

## Raw Telemetry Content

# Paper-2 v1.7 — ARGON Collab-1 Integration Ledger — v1

- Provenance: ARGON collaboration round-1 response, relayed by the operator as a PDF attachment this boundary (trace `1a16c9b26ae3ae31`); pinned verbatim at `write-ups/paper-2-v1.7-argon-collab1-receipt-v1.md` (source PDF SHA-256 `de577f4356b93f2763aef58279e08e2e824e16f5faf53999de9403f4ab45ac0d`, 334,901 B).
- Contract: init §0.4 (per-contribution blocks), §0.5 (witness integrates; operator adjudicates). Ten contributions received, all in the §0.4 format; §2 null report received (three domains, all NULL).
- Composition of draft-2 after this ledger: §1 r1 (untouched — no patch targeted §1) + §2–§8 r2 (this boundary). The r1 deposits stand as historical; their content pins are unchanged.

## Integration doctrine (registered, applied throughout)

1. **Patch text governs; span/sentence designations are aids.** Where ARGON's designated span is broader than the patch text's coverage, the unreplaced original content is retained (content preservation), and the decision is registered below. No original sentence was silently dropped.
2. **Notation normalized to the draft's Unicode-math convention** (𝒮 vs S distinction preserved from ARGON's 𝓢/S split; `R^{…}`; ᵀ; ‖·‖₂; − U+2212; ∅; ≥). ARGON's LaTeX source forms remain authoritative in the receipt for assembly-time conversion.
3. Every anchor string was byte-verified exactly once before apply (32/32 patches, fail-closed run); NBSP-normalized 0 across all outputs; the §4.7 typo and all locator repairs verified pre-apply.

## Per-contribution dispositions

| # | Locators | Disposition | Verification & adjustments |
|---|---|---|---|
| C1 | §3.5, §4.2 | **APPLIED-ADJUSTED** | §4.2 sentence 2 applied (tuple form, w/ MesaNet H_t and conv buffer C_t). §3.5: ARGON designated "sentences 2–5" but the patch text covers only Finite/Explicit/Fixed-size — the **Rule-evolved sentence is retained verbatim** (content preservation; dropping it would have deleted a load-bearing property from the four-property spine). Verified: depthwise causal short-conv (w=4) across DeltaNet/GDN/KDA/MesaNet matches the published lineage; multi-head H×d_k×d_v and hybrid bounded-window W are standard; MesaNet's second-order state is integrated as a completeness requirement hedged "where present/optional" — the manifest certifies the whole of what is held, whatever the variant holds — not as a claim that MesaNet persists an explicit Gram matrix. |
| C2 | §4.7, §7.4 (P2) | **APPLIED** | Typo `re-execizes` byte-verified at §4.7 pre-apply; 0 occurrences post-apply. sup_T → max_{1≤T≤T_max} with reverse time-ordering ∏_{s=T}^{1} M_s — correct for the draft's left-update convention (§4.2's S ∈ R^{d_k×d_v}, rows = key side; ‖M_s‖₂ = 1 at β∈[0,2], ‖k‖₂=1 — eigenvalue 1−β along k, 1 on k⊥). Cross-layer bridge (Surface E motivation) applied: first-order coupling δM_s S_{s−1} + δU_s via gate/key perturbation in layers ℓ′>ℓ. §7.4 P2 pin applied. §4.8's existing "gate-perturbation" phrasing now consistent. |
| C3 | §3.2, §5.4 | **APPLIED** | IEEE-754 non-associativity of chunkwise (B>1) vs step-by-step (B=1) reductions is standard numerics; Π_exec = (dtype, chunk_size B, kernel_id, tp_topology) added to continuation-class pins; cross-profile continuation typed bounded-drift under §7.3–7.4 norm-and-probe tolerances. §5.4 penultimate sentence replaced as specified. |
| C4 | §3.2, §4.3 | **APPLIED** | parametric_base_pin added to the §3.2 row spec; basis-compatibility invariant inserted before §4.3's final sentence. LoRA dims B ∈ R^{d_out×r}, A ∈ R^{r×d_in}, r ≪ min(d_in, d_out) standard. Closes the silent subspace misalignment hole (restore-class digest passes while basis drifts). |
| C5 | §3.7 | **APPLIED-ADJUSTED** | Remediation insert applied after "A poisoned tensor pins as permanently as a true one (§2.10)." **Witness adjustment**: the erasure's projector moved to the LEFT of S — patch as written had `S ← S(I − β k_err k_errᵀ)`; in the draft's convention (§4.2: S ∈ R^{d_k×d_v}, rows = key side; §4.7: projection (I − β_t k_t k_tᵀ) ∈ R^{d_k×d_k}) the right-multiplied form is dimensionally invalid for d_k ≠ d_v and would act on the value side, not the key side. Corrected to `S ← (I − β k_err k_errᵀ) S`, matching the delta rule's left update (C2's own convention). ARGON's original form preserved in the receipt. |
| C6 | §4.4 | **APPLIED-ADJUSTED** | ARGON designated "sentences 2–4"; the patch text maps onto original sentences 3–4 (manifest-row expansion + complete-vs-curated → hash-chain / C1 pre-commitment / n-floor). **Sentence 2 (daemon registration) and sentence 5 (design label) retained** (content preservation). seq_no + prev_capture_hash chain and C1-across-boundary pinning align §4.4 with the §2.3/§4.5 n=1 vs n≥2 threat-model floor, as claimed. |
| C7 | §8.1, §8.3 | **APPLIED + witness upgrade** | §8.3 prior-art contrast applied verbatim (Marconi-class prefix/radix state caching, RWKV-style state files → ephemeral latency cache, never governed archival atom). §8.1: ARGON's parametric recall **live-verified witness-side this boundary** (division of labor: witness has net; ARGON ran air-gapped): arXiv 2102.11174 Schlag/Irie/Schmidhuber "Linear Transformers Are Secretly Fast Weight Programmers" confirmed via arxiv.org (ICML 2021 venue confirmed via author citation); arXiv 2406.06484 Yang/Wang/Zhang/Shen/Kim "Parallelizing Linear Transformers with the Delta Rule over Sequence Length" confirmed via arxiv.org (title/authors/Householder-WY content; NeurIPS 2024 venue label rides parametric recall + identifier verification — reconcile at bib merge per the standing §8.1 label). Bracket upgraded from "[parametric recall — confirm…]" to "[live-verified witness-side this boundary…]". **Witness-initiated consequential edit**: §8.6 parenthetical "pending re-verification" → "live-verified witness-side, this boundary" (consistency with the upgraded label; registered here as witness-initiated, Round-5.1 Table-2 row 9 precedent). |
| C8 | §7.4 | **APPLIED** | Sentence 1 → six predictions across substrate/verification/economics; P5 (verification cost-asymmetry) and P6 (priced fail-visibility non-degradation) inserted before the closing sentence. Bijection verified: §7.5's three falsifier clauses byte-checked this boundary (substrate §7.5-1, verification §7.5-2, economics §7.5-3) now have matching predictions P1–P4 / P5 / P6. |
| C9 | §2.3, §2.9, §3.4, §3.6, §4.6, §5.1, §5.3, §5.5, §6.5 | **APPLIED** | All twelve locator repairs applied: v1.6.1 §6.4 (§2.3); v1.6.1 Table 5 + v1.6.1 Table 6/§6.4 (§2.9 ×2); PROTOCOL §7 (§3.4); PROTOCOL §10 (§3.6, §4.6, §5.1, §5.5); deictics pinned to boundary 14ad0f6 ([A]-leg manifest verify 28/28, R-64) in §4.6, §5.1, §5.3, §6.5. Every quoted anchor string byte-verified pre-apply. The v1.7 §6.4 collision (affect log) and the dangling bare-§10 namespace are both real and both now resolved. |
| C10 | §4.9, §6.7, §7.7, §8 (§8.7) | **APPLIED** | §4.9 row 5 replaced with the §2 AR-3 row → §4.1–4.2 (misattribution confirmed by byte-check: §2.3 contains no training-side delta-snapshot sentence; that sentence lives in §2.4, which keeps row 6). §6.7 renamed (§1/§2/§5 r1 → §6) + 3 rows appended; §7.7 renamed (§1/§3/§4/§5 r1 → §7) + 5 rows appended; §8.7 added (2 rows + "None open.", house-style completion). PDF table-row flattening normalized — each row on its own line (transport noise, disclosed in the receipt header). |

## Null report (§2 of the response) — spot-verified witness-side

- R2-56 figures (80 NBSP; 11,772 B → ~11,833 B) match the round-5.7 receipt §1 byte-for-byte.
- Round-5.7 gate figures (0 standing rebuttals; GATE-D 0/44; GATE-A 0/27; Table 5 0/15) match §2.9 and the round-5.7 receipt.
- Manifest 28 rows @ 14ad0f6 (R-64) consistent with the record; current manifest is 29 rows (operator snapshot c23b413 added one) — no contradiction: §4.6's pin now names the boundary explicitly (C9).
- Commit anchors 30fb889 / 14ad0f6 / 994b1cad / 8d4ad638 byte-verified this boundary (r1 files unchanged since deposit).

## Witness remarks (non-blocking, for assembly)

- §7.1's headline ("arrives bit-identical and proves it by digest") is now implicitly scoped by §3.2's Π_exec typing: same-profile continuation verifies bitwise; cross-profile is bounded-drift under §7.3–7.4. No §7.1 patch was proposed; flag for the assembly pass.
- ARGON's envelope response-to parent-trace cites `1a16c77028a3b0ed` (the init's authoring boundary trace) — consistent with the init's own provenance line; no counter needed.
- Air-gap honesty (§0.3.c) and holdings-complete declaration (§0.2) accepted as received; PROTOCOL references audited as-cited per ARGON's own statement.

