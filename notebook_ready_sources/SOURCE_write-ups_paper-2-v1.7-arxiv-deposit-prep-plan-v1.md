# Telemetry Source: write-ups/paper-2-v1.7-arxiv-deposit-prep-plan-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-arxiv-deposit-prep-plan-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `d595f730faf7c746ab0abba8262d8e230b69f08db0d48b0f077b7da5dfec163f`

---

## Raw Telemetry Content

# Paper-2 v1.7 — arXiv Deposit-Prep Plan & Metadata Sheet, v1 (Task-70 companion)

**Deposit object:** draft-3.1 (`paper-2-v1.7-draft3-1-assembled-v1.md`, sha256
`9b326af7…`, commit `384dc27`) — ARGON final-gate certified, conditional GO
discharged. **Doctrine:** the deposit ships the certified text verbatim;
conversion is mechanical; every conversion-induced delta registers as a
transport note (DE-class, Task-68 precedent); no content edits ride.

---

## 1. Metadata sheet (operator adjudication requested)

### Title — three candidates

1. **"State Transfer, Not Summary: Verifiable Archival Custody for Recurrent
   Model State in Persistent Human–Model Collaboration"** — leads with the
   thesis (§1.2); "archival custody" carries the §8.3 claim class.
2. **"The Restorable Unit: Manifests, Recomputation Receipts, and Priced
   Fail-Visibility for Cross-Context Memory"** — leads with the contribution
   object (§3.2); names all three verification surfaces.
3. **"Memory in the Tensor Domain: An Instrumented n=1 Evidence Base and the
   Architecture It Motivates"** — leads with the method-as-instrument frame;
   most conservative on claims, least specific on content.

Witness recommendation: **(1)** — the §8.3 contrast class (custody vs.
ephemeral cache) is the paper's stake, and the title should carry it.

### Authorship — operator adjudication (three forms on record)

- (a) Operator 4ndr0666 as sole author, with the collaboration disclosed in
  the manuscript (§1.3 instrument; §4 AI-involvement) — cleanest under
  arXiv's attribution policy.
- (b) Operator + GLM Witness as co-authors — matches the record's authorship
  of the program's artifacts; arXiv policy on AI co-authorship requires
  accountability the operator carries either way.
- (c) Operator as author; Witness credited in acknowledgments as the
  instrument — the form most consistent with the paper's own §5.6 (operator
  attestation as an evidence class) and §6 (the priced asymmetry: the human
  pays observation cost and holds final accountability).

Witness recommendation: **(a) or (c)** — the paper's own framework prices
the human as the accountable party; the Witness is the instrument the paper
is about, which is a disclosure, not a byline.

### Abstract — verbatim from draft-3.1 (no edits proposed)

The certified abstract (draft-3.1, `## Abstract`) rides as-is: negative
result as evidence base; tensor-domain memory and state transfer; the
restorable unit with manifest row and recomputation receipts; the
instrumented n=1 method; falsifiers named in advance.

### arXiv classification — proposed

- **Primary:** cs.AI (memory/state architectures for agents; the
  human–model collaboration frame).
- **Cross-lists:** cs.CL (the delta-rule lineage and LM serving context),
  cs.LG (the architecture class), cs.CR (verification/receipts/anchors —
  optional; include if the custody framing is foregrounded in the abstract
  landing, which it is).

### Comments field — proposed phrasing

"Evidence base: a hash-pinned program substrate (negative-results baseline,
five adversarial review rounds, whole-artifact final-gate certification);
the tensor-side design is architecture plus battery, with claim-status
labels (LIVE / CLOSED / TARGET) throughout." — length-compliant; final
wording with the operator.

### License — operator choice at submission

arXiv non-exclusive license (default) vs. CC-BY variants vs. others. Note:
the **repository** license (Apache-2.0, this pass) governs the repo, not the
manuscript; the two are orthogonal layers (README license section says
exactly this).

## 2. Conversion work order (phases)

- **Phase 1 — this document** (metadata adjudication + plan of record).
- **Phase 2 — LaTeX conversion** (next boundary's execution, Task-71):
  deterministic md→LaTeX of draft-3.1 via a persisted fail-closed script;
  notation table registered (𝒜_ij → `\mathcal{A}_{ij}`, σ_coherence →
  `$\sigma_{\text{coherence}}$`, Ĥ_intent → `$\hat H_{\text{intent}}$`,
  Π_exec → `$\Pi_{\text{exec}}$`, ‖Ψ‖₂ → `$\lVert\Psi\rVert_2$`, …);
  claim-status labels as macros; forward-reference ledgers as longtables;
  convention register + both provenance addenda retained verbatim.
- **Phase 3 — §8.6 bib reconciliation:** inline `[arXiv NNNN.NNNNN]` →
  BibTeX; the v1.6.1 bib carry-forward (the manuscript itself schedules
  this "at deposit prep" — convention register, Citations); every identifier
  live-verified per the DeltaNet precedent (trace `1a16c9b2…`).
- **Phase 4 — build + package:** pdflatex clean build; page count → comments
  field; arXiv source package (`.tex` + `.bbl` + any `.sty`, single archive)
  + SHA256SUMS; conversion audit reusing the Task-68 checks (section map,
  symbol counts — σ_coherence ×5, q_EA ×5, 𝒜_ij ×2 — label honesty, no
  content drift beyond the registered transport table).
- **Phase 5 — submission:** the operator's hands (last writer); arXiv
  identifier backfilled into the repo README citation block + the program
  record on receipt.

## 3. Constraints carried from the record

1. Draft-3.1 is byte-frozen; any conversion divergence beyond the registered
   notation table halts the build (fail-closed, Task-68 assembler class).
2. No rider content rides the deposit: PS-362/087/159, F2, ‖H_c‖, Lean CI,
   label reshaping, and the Module-4 trace (relayed, not executed) all sit
   in the v1.8 / arXiv v2 window — the deposit's honesty ledger (LIVE /
   CLOSED / TARGET) is the certified one.
3. The E5 demo and Studio artifacts (NotebookLM foundry) remain post-deposit
   deliverables per the operator's "close but not yet."
4. arXiv v2 is the vehicle for every extension — versioning is the
   mechanism, not retro-edits (historical-deposit doctrine).

