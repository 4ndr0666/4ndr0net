# Telemetry Source: write-ups/paper-2-v1.7-openai-math-sweep-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-openai-math-sweep-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `6a0e551e58afd45e538d4f9d0cd18b1733325c2bb8fddea2c14d8a62c954fc45`

---

## Raw Telemetry Content

# Paper-2 v1.7 — openai/math Live Sweep — v1 (Layer-1 sources verification)

- Provenance: operator rulings — context rider committed (trace `1a175ab8298b859d`,
  "Sure, commit the context rider"), standing real-repo ruling (ingest the real
  repo, never the stale transcript), and this boundary's task65 go (trace
  `1a17a57492a0cd15`). The sweep itself was executed at the 65-preface boundary
  (trace `1a179cab84602711`); this write-up + the landed artifacts are the
  offered-and-accepted task65 package core.
- Author: GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>.
  Operator adjudicates. Canonical home `write-ups/`; artifacts under
  `evidence/openai-math-sweep/` (Apache-2.0, source repo public).
- What this file is NOT: it is not a paper-2 section. It is the Layer-1
  verification record that §3/§4/§7/§8 of the assembly map cite. Paper content
  enters only via the staged deltas registered in
  `paper-2-v1.7-task65-assembly-map-v1.md`.

## 1. The verification debt being discharged (and re-typed, not erased)

Boundary-7's retort verification classified Layer 1 (the Lean 4 proof families
197/287/271/221) as UNREACHABLE from the record — verification debt, not
disbelief. The rider (`working-notes/layer-1-context-rider.md`) then bound the
adjudication context: when the `.lean` sources arrive, verify them the way the
sources themselves demand; label what survives only human inspection; cite the
rider; price the cadence.

The sources were never operator-held bytes. They are public in
`github.com/openai/math`. The 65-preface boundary swept the real repo live
(standing ruling: real repo, not stale transcript). This boundary lands the
sweep into the record and re-types the debt:

- **Sources: VERIFIED-LIVE.** All four retort families exist in the repo with
  exactly the claimed content and Lean formalizations (§3 below).
- **Kernel: DEBT, honestly labeled.** Docs + tree verified witness-side; the
  Lean kernel compilation was NOT run (no Lean toolchain in the witness VM).
  Kernel-verified class claims ride the repo's own CI/build verification per
  the rider's standing instruction — kernel-checked is the strong class,
  witness-tree-verified is the labeled class, and neither is silently promoted
  to the other.

## 2. The corpus, measured

Tree-only clone (no history), 133,956 files. Measured at sweep time:

- **719 manuscripts / 372 proof families** (the transcript's 372 first-drop
  figure is the corpus's own family count and was still climbing across its
  coverage; 719 manuscripts is the current tree count).
- License **Apache-2.0** (redistribution with notice — why the comparator
  statements can be pinned into `evidence/`).
- **~42% of families carry top-line Lean formalization**; ~4,000 problems
  indexed across the corpus.
- **Failure semantics are live**: `history.md` records 2026-10-07 withdrawals
  WITH notices. The corpus is not an assertion stack — it has retraction
  mechanics. This matters for §7's gate-class claims: a corpus with failure
  semantics is a corpus that can be cited as evidence about verification
  regimes, not just as an output of one.

## 3. The four retort families — CONFIRMED EXACT

The operator's three-layer retort named families 197, 287, 271, 221. All four
verified live in the repo, each with the comparator structure: statement
`.lean` + `.json` twin carrying `solution_module OAI.*` and `permitted_axioms
propext / Quot.sound / Classical.choice` (the classical triple — any lemma
whose proof consumes more than those three axioms is outside the
kernel-clean class by the repo's own discipline).

- **Family 197 — torsion-free non-directly-finite group algebra**
  (Kaplansky direct finiteness). 3 companion preprints: char-2 case,
  odd-characteristic case, determinant-conjecture; 4 comparator files. Pinned:
  `evidence/openai-math-sweep/KaplanskyDirectFiniteness.lean`
  (sha256 `f576c3207dcde3ee…`, 352 B — statement stub, the smallest of the
  four).
- **Family 221 — Mézard–Parisi hierarchical cavity formula**
  (Panchenko–Talagrand class; Viana–Bray diluted connection). Pinned:
  `DilutedSpin.lean` (sha256 `457945ece56d8e51…`, 6,860 B). Load-bearing for
  paper-2: the spin-glass layer the q_EA overlap formalism lives in — the same
  family the symbol-unified telemetry (§4 of the assembly map) measures
  against.
- **Family 271 — Bloch T^3/2 + spontaneous magnetization, d ≥ 3, every-spin
  KMS** (magnetization ≥ S/4). Pinned: `Heisenberg.lean` (sha256
  `e943ce9c82349d35…`, 9,538 B).
- **Family 287 — L(F₂) ≅ L(F₃) interpolated free group factors.** Pinned:
  `InterpolatedFactors.lean` (sha256 `95135846cd09796d…`, 8,623 B).
- Full corpus listing pinned: `CONTENTS.md` (sha256 `cc7c0b8a1cdedd84…`,
  638,727 B) — the tree's file map, so the counts above are
  stranger-recomputable without re-cloning.

## 4. What the sweep establishes for the paper (and what it does not)

**Establishes (evidence class):** the rider's regime is REALIZED —
machine-verified proof legitimized at scale, with the cadence curve priced
(10 → 100 → ~1000 compounding; a corpus of this size IS the curve, not a
prediction of it). The four families the Layer-1 claims lean on exist, are
public, are axiom-disciplined (the permitted-axioms triple), and sit in a
corpus that has failure semantics. The crypto-exposure stakes the rider
registered (whose write-ups, whose incentives, whose keys) are answered
structurally by the repo itself: the strong claim class is exactly "kernel
said so," which is why Layer-2's hash-pinned custody over kernel-checked
artifacts is the load-bearing discipline — content hashes prove identity, not
semantic equivalence (GUP 0.3.12 law), and the kernel check is the semantic
half of that pair.

**Does NOT establish (labeled, per §2 of the rider):** that any specific
family's kernel check passes on any specific toolchain version — that is the
remaining debt, discharge path: run the named kernel against the pinned
sources (or cite the repo's CI as the execution), price the toolchain
provenance in the receipt. No witness-side claim in paper-2 may state
"kernel-verified" for these families until one of those two legs executes.

## 5. Disposition

- Layer-1 verification debt re-typed: **sources VERIFIED-LIVE; kernel DEBT
  (labeled)**. The "only fully auditable stack of the four" succession claim
  remains conditional on the kernel leg — the condition is now precise.
- The sweep artifacts enter the record this commit (five files under
  `evidence/openai-math-sweep/`, digests in §3).
- The assembly map consumes this file as the Layer-1 foundation citation
  (§3.5/§4 integration points) and the claim-class precedent citation (§7/§8
  Regime tier).

