# Telemetry Source: write-ups/paper-2-v1.7-task71-conversion-ledger-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task71-conversion-ledger-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `b044fb655403e28bff842ee8c7e76575ff588237cc734f0758e1af7e48b94e2b`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Task-71 Conversion Ledger (LaTeX transport notes, v1)

**Task:** Task-71 Phase 2 (deposit-prep plan v1) · **Trace:** 1a181456f4ee82d9
**Source:** `paper-2-v1.7-draft3-1-assembled-v1.md` — sha256
`9b326af709b9dc2236b93364d1e315b6b2a7b08adb1e23bd386be13f37d28c60`
(G0-asserted before any work; re-verified after; byte-frozen throughout).
**Output:** `paper-2-v1.7-draft3-1-latex-v1.tex` — 124,539 B, sha256
`16710f17d8041eeac043bd6f2f6680594596f5a58db0250c26611d51f4ffcb06`.
**Converter:** `scripts/task71_latex_convert.py` (persisted, fail-closed,
Task-68 assembler class). **Build:** tectonic v2 smoke build GREEN — 33-page
PDF, 209.64 KiB, zero errors.

Doctrine (deposit-prep plan §2, carried): the deposit ships the certified text
verbatim; conversion is mechanical; every conversion-induced delta registers
as a transport note (DE-class); no content edits ride.

---

## 1. Gate results

| Gate | Check | Result |
|---|---|---|
| G0 | source sha256 == record pin | OK |
| G1 | zero math-class unicode outside `$…$` spans (pre-pandoc) | OK — 159 transport applications, 61 of 85 rules fired |
| G2 | zero math-class unicode in final body; non-ASCII whitelist clean (`…`, `é` only) | OK |
| G3 | per-character macro parity, 34 families (source count == macro count) | OK |
| G4 | label macros `\live{}`×3 `\closed{}`×3 `\target{}`×4; quoted verdict retained literal | OK |
| G5 | structure: 11 `\section` + abstract env ×1, 64 `\subsection`, 9 `longtable`, `\S`×426 | OK |
| Build | tectonic compile, zero errors | OK |

## 2. Notation transport table (authoritative counts)

Anchor: witness-side measurement of draft-3.1 (this boundary), superseding the
external audit's drifted counts and correcting one stale record count.

| Source form | LaTeX transport | Count | Notes |
|---|---|---|---|
| `σ_coherence` | `\(\sigma_{\text{coherence}}\)` | 5 | plan-pinned; audit confirmed |
| `q_EA` | `\(q_{\text{EA}}\)` | 5 | **audit said 6 — drift; record ×5 confirmed** |
| `Π_exec` | `\(\Pi_{\text{exec}}\)` | 13 | audit confirmed |
| `𝒜_ij` | `\(\mathcal{A}_{ij}\)` | 4 | **record (Task-68) said ×2 — stale; actual ×4** (L15, L19, L195×2); Phase-4 gate spec corrected |
| `𝒜_ji`, `𝒜_ji*` | `\(\mathcal{A}_{ji}\)`, `\(\mathcal{A}_{ji}^{*}\)` | 2 | conjugate/reversal forms (L195) |
| `𝒮_t` (tuple) | `\(\mathcal{S}_t\)` | 8 | **object-distinct from the matrix below** |
| `S_t^{(ℓ)}` (matrix) | `\(S_t^{(\ell)}\)` | 4 | fast-weight component of `𝒮_t = (S, H, C)`; **audit's unified `S_t → \mathcal{S}_t ×12` mapping DECLINED — it conflates tuple and matrix** |
| `H_t^{(ℓ)}`, `C_t^{(ℓ)}` | `\(H_t^{(\ell)}\)`, `\(C_t^{(\ell)}\)` | 5, 4 | incl. `H_t^{(ℓ)} = ∅` (MesaNet rider) |
| `e^{±iĤ_intent Δt}` | `\(e^{\pm i\hat{H}_{\text{intent}}\Delta t}\)` | 4 | steering law + conjugate; `v_steered = e^{iĤ_intent Δt} v_residual` as one run ×2 |
| `[Ĥ_intent, Ĥ_context]` | `\([\hat{H}_{\text{intent}}, \hat{H}_{\text{context}}]\)` | 1 | commutator (non-commutativity resource, §4.8) |
| `𝒜_ij = q_i†k_j` | `\(\mathcal{A}_{ij} = q_i^\dagger k_j\)` | def ×2 + `∈ C` ×1 | **`\mathbf{q}`/`\mathbf{k}` bolding (audit table) DECLINED — source carries none; mechanical transport adds none** |
| `‖·‖₂` family | `\(\lVert·\rVert_2\)` | 7 | Ψ×1, v_steered×2, v_residual×3, M_s×2(incl. product bound ×2 sites) — audit's "2 occurrences" refers only to the Ψ form; actual Ψ literal ×1 |
| `‖S̃−S‖` | `\(\lVert\tilde{S} - S\rVert\)` | 1 | restore-fidelity norm |
| `max_{1≤T≤T_max} ‖∏_{s=T}^{1} M_s‖₂ ≤ C(T_max)` | one math run | 2 | R2-33 stability criterion (L191, L333) |
| `(I − β k_err k_errᵀ) S` ← | one math run | 1 | Householder erasure (§4.3) |
| `(I − β_t k_t k_tᵀ)` | one math run | 1 | per-step projection |
| `R^{H×d_k×d_v}` etc. | `\(\mathbb{R}^{…}\)` | 8 | all five shape forms, `×`→`\times`, `−`→`-` |
| `Δ` family | `\(\Delta t\)`×4, `\(\Delta W\)`×3, `\(\Delta_t^{(\ell)}\)`×1 | 8 | |
| `α̃_t^{(ℓ')}, β̃_t^{(ℓ')}, k̃_t^{(ℓ')}` | `\(\tilde{\alpha}_t^{(\ell')}\)` … | tuple ×1 | cross-layer gate/key perturbations (L191) |
| `δM_s^{(ℓ')} S_{s−1}^{(ℓ')} + δU_s^{(ℓ')}` | one math run | 1 | first-order coupling terms |
| `n≥2` | `\(n\geq 2\)` | 8 | multi-party separation rider (R2-35) |
| `→` | `\(\to\)` | 44 | lineage chains, telemetry bands, forward-ledger headings |
| `§N.N` | `\S{}N.N` literal | 426 | **no `\ref{}` in v1** — zero renumber risk; label-map option deferred to Phase 4+ |
| `ℓ`, `ℓ'` | `\(\ell\)`, `\(\ell'\)` | 28 | layer indices |
| `×`, `·`, `∈`, `≥`, `≤`, `≠`, `≪`, `⊥`, `∅`, `ℤ`, `∏`, `⟨⟩`, `†`, `ᵀ`, `²`, `₂`, `−`, `←` | standard macros | 17, 4, 11, 11, 7, 6, 2, 3, 1, 1, 2, 2+2, 5, 2, 4, 7, 10, 1 | full parity in G3 |
| `arg(⟨v_steered\|v_target⟩)` | `\(\arg(\langle v_{\text{steered}} \mid v_{\text{target}}\rangle)\)` | 2 | table-cell escaped pipe de-escaped (DE-class, Task-68 precedent) |

## 3. Structural transport notes (DE-class)

1. **Title/author verbatim.** `\title` = draft-3.1 line 1; `\author` = "Alejandro
   Gutierrez (ORCID 0009-0008-0976-3895)" extracted from the in-text ruling
   ("Sole human author… model lineage retired from authorship… record R2-2");
   the full annotation paragraph rides verbatim in the body. No invention.
   `METADATA-ADJUDICATION-PENDING` comment block carries the Phase-5 opens
   (title candidates ×3, comments field, license at submission).
2. **Abstract → `abstract` environment.** Structural only; content verbatim;
   closed before the next section. Source order preserved (annotation
   paragraph precedes the abstract, as in draft-3.1).
3. **Claim-status labels as macros.** `\live`/`\closed`/`\target` render
   identical to source uppercase (styling = one-line Phase-4/5 swap). Macro
   class = table cells + definition line + ledger mention (3/3/4). The quoted
   verdict string `CRITIQUE LOOP CLOSED END-TO-END` (§6) is **not** a
   claim-status label — excluded from the macro class, rides literal.
4. **Heading shift.** `##`→`\section`, `###`→`\subsection` (pandoc
   `--shift-heading-level-by=-1`); 11 sections + abstract + 64 subsections =
   77 headings, matching the audited count exactly. Pandoc auto-labels and
   `\texorpdfstring` bookmark branches retained as scaffolding.
5. **Tables.** 9 pipe tables → `longtable` with booktabs rules; requires
   `array`+`calc` (pandoc `\real{}` column arithmetic) — caught by the smoke
   build, added to the preamble.
6. **Identifier typography.** Tuple contents that are multi-letter
   identifiers (`dtype`, `kernel_id`, `tp_topology`) ride as text, mirroring
   the source's own typography; only symbol heads (`Π_exec`) enter math.
   Standalone `T_max` wrapped (consistency with the stability-criterion
   compounds); plain-ASCII identifiers without unicode neighbors left as text
   by the same doctrine.

## 4. Hardening iterations (fail-closed catches, Task-68 class)

1. **texorpdfstring duplication.** First parity run counted §×446 vs 426:
   pandoc duplicates heading content into PDF-bookmark branches; the 6
   forward-reference-ledger headings (§3.8, §4.10, §5.8, §6.7, §7.8, §8.7)
   carry 20 §refs among them — the exact discrepancy (+4 §1, +3 §2, +4 §3,
   +2 §4, +3 §5, +1 §6, +2 §7, +1 §8). Gate re-anchored to the typeset
   branch; bookmark scaffolding retained.
2. **Pandoc digit-adjacency rule.** `$…$` whose closing `$` is followed by a
   digit parses as money and gets escaped (`\$-\$0.1325`, `\$\times\$4`) —
   4 spans. Fixed via digit-inclusive compound tokens
   (`−0.1325`→`\(-0.1325\)`, `×4`→`\(\times 4\)`).
3. **`\real{}` column arithmetic.** Pandoc's longtable column specs require
   `array`+`calc` beyond the audit's package list (amsmath/amssymb/amsfonts,
   booktabs, hyperref — all adopted); build halted at the first longtable
   until both were added.
4. **`\to`/`\top` substring collision** in the parity counter — regex
   negative-lookahead fix.

## 5. Deviations from the external audit's notation table (adjudicated)

| Audit proposal | Disposition |
|---|---|
| `S_t` → `$\mathcal{S}_t$` (×12 unified) | **DECLINED** — conflates the state tuple 𝒮_t (×8) with the fast-weight matrix S_t^{(ℓ)} (×4); both transported distinctly per the convention register's own decomposition |
| `A_ij = q_i†k_j` → `$\mathcal{A}_{ij} = \mathbf{q}_i^\dagger \mathbf{k}_j$` | **PARTIAL** — 𝒜 macro adopted; `\mathbf` bolding declined (not in source) |
| q_EA ×6 | **CORRECTED** to ×5 (witness count; record confirmed) |
| §refs "Mapped for `\ref{}` handling" | **DEFERRED** — literal `\S{}N.N` in v1 (zero renumber risk); label-map option is a Phase-4+ adjudication |
| `‖Ψ‖_2 = 1` ×2 | **CORRECTED** — one literal site (L195); the second audit sighting is the Ψ-definition compound (`Ψ = v_steered / ‖v_residual‖₂`), transported as its own run |
| Package list | **ADOPTED + EXTENDED** (array, calc, longtable, geometry added — pandoc scaffolding requirements surfaced by the build) |

## 6. Phase-4 audit-gate spec (updated for the record)

The deposit-prep plan §2 Phase-4 gate anchored on "σ_coherence ×5, q_EA ×5,
𝒜_ij ×2". Corrected anchor set for the packaged-build audit:
**σ_coherence ×5, q_EA ×5, 𝒜_ij ×4** (+ the parity families of this ledger's
table, all machine-checkable via the converter's G3 gate).

