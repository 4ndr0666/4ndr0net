# Telemetry Source: write-ups/paper-2-round5-counters-v1.md
- **Source Identifier**: `write-ups/paper-2-round5-counters-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `b59a8431e741355b8a92e6cf943d831f9f405b34093e4bb70bfd52db2f0e376a`

---

## Raw Telemetry Content

# WITNESS COUNTERS — ROUND 5
## Response to Gemini 3.8 Flash (High Thinking Mode), round-4 findings on Paper-2 v1.4
### Prepared by GLM Witness for operator relay · trace 1a15d3b1636ece3d · 2026-10-21

---

**Provenance.** Every round-4 quote was machine-verified against the v1.4 source and the deposited PDF before any verdict was issued. Dispositions R2-29..R2-35 are registered in the public decisions ledger; R2-34/35 carry an explicit operator adoption ruling. Fixes are canonical in v1.5. Score this round: **7/7 confirmed, 0 rebutted** — the first round with zero rebuttals, and both criticals were understated by the reviewer relative to the build's actual state (details in R2-29, R2-30).

---

### R2-29 — Table 2 physical omission (§6.3 trust model) · CONFIRMED, worse than relayed

**Verdict: the reviewer is right, and the defect is larger than the finding.** Not just Row 7: rows 7, 8, **and 9** were all physically absent from printed v1.4 (pages 13–14). Row 7 is paragraph-length; a `[t]` float carrying nine such rows exceeds the printable page height, and LaTeX clipped the overflow silently — the caption's cross-reference to Row 7 survived while the row itself did not. A paper whose subject is silent alteration suffered silent alteration in its own trust table. That is not a defense; it is the finding confirmed at higher magnitude.

**Fix applied.** Table 2 converted from float to `longtable`: page-breaking with a continuation header, so no future row can be silently dropped by float geometry. All nine rows print — rows 1–6 on page 12, rows 7–9 on page 13 under the continuation header.

**Verification.** Page-level text extraction of the built PDF confirms all nine rows present; pagination and cross-references resolve; no unresolved markers.

### R2-30 — Table 5 horizontal cryptographic truncation · CONFIRMED, worse than relayed

**Verdict: conceded without reservation.** A truncated anchor is not an anchor. And the defect was larger than stated: not four values — **all eight** anchor values truncated at ~20 hex characters in print. Cause isolated by the witness, not the reviewer: the label column's natural width starved the value column to ~19 visible characters (the 40-hex identifiers that printed in full live in body prose, which is what isolated the failure to table geometry rather than data).

**Fix applied.** Table 5 rebuilt with fixed-width column geometry: label column constrained, value column full-width typewriter face. No anchor can clip by construction.

**Verification.** All eight anchors extract byte-complete from the printed table; the substrate head and signing-key fingerprint each appear twice (Table 5 + prose), giving an in-document cross-check.

### R2-31 — Appendix A verbatim overflow · CONFIRMED

**Verdict: confirmed as stated.** Lines 689–691 ran past the right text margin with trailing inline comments, clipping terminal flags mid-token. A reproducer following the printed commands could not execute them. The appendix's sole purpose is third-party reproducibility; clipped commands defeat it.

**Fix applied.** Trailing comments shortened and moved to their own lines above the commands they annotate; every command intact and inside margins.

**Verification.** Appendix verbatim block extracted from print; all commands complete within margins.

### R2-32 — Algorithm 1: simulation vs execution · CONFIRMED (the round's strongest finding)

**Verdict: confirmed in full.** An algorithm credited as running must either run or be labeled specification. `emit_verification_data.py` executes the static manifest layers (L0/L1/L3: current working tree plus one pinned historical commit) fail-closed — and nothing more. It performs no commit-traversal loop, no historical state reconstruction, no graph-wide set-union classification. Round 3's fix (R2-27) named the real script after the reviewer's proposed `tools/artifact_manifest.py` was found not to exist; that correction fixed a name, not the claim. The claim itself — "the implementation exists" — still over-credited a static inventory as the full Algorithm 1. The reviewer caught what our own round-3 refinement left standing.

**Fix applied.** §5 reconciled to the reviewer's fix #4 in substance: the static manifest layers are stated as executed fail-closed by the named script (execution entries in Appendix A); the full DAG-wide history walk — S_τ reconstruction across all commits, union classification into preserved/translated/authorized-retired/unresolved — is stated as **protocol specification**, not integrated CI. The paper now claims exactly what runs and labels the rest as design.

**Verification.** §5 language checked sentence-by-sentence against the Appendix A command list; no remaining sentence attributes DAG-wide execution to the script.

### R2-33 — §9 self-contradiction in recurrent stability bounds · CONFIRMED

**Verdict: the contradiction is real and the reviewer's reading is exact.** §9 demanded a uniform per-step induced-norm bound ‖M_t‖ ≤ 1 − δ as a sufficiency condition for ε-ball replay, while the adjacent sentence observes that the delta projection (I − β_t k_t k_tᵀ) carries eigenvalue exactly 1 on the preserved subspace — which forces ‖M_t‖ ≥ 1 in every induced norm wherever the key-decay factor is identity. The paper set a sufficiency criterion its own architecture violates by construction, one sentence after recording why. This was introduced by our own round-2 math fix (R2-16) and half-repaired in round 3 (R2-26); the reviewer caught the residue.

**Fix applied.** The per-step sufficiency demand struck entirely. The criterion is restated where it is actually meaningful — at the product level: boundedness of the sequence of products over the finite context window, `sup_T ‖∏_{s=1}^{T} M_s‖ ≤ C`. This is what the written-subspace analysis supports and what the replay discussion requires; per-step contraction is neither available nor needed.

**Verification.** §9 contains no per-step bound; the product-level criterion is consistent with the eigenvalue-1 structure note; internal consistency re-checked after edit.

### R2-34 — Replay-verify fallback collapses to Tier-3 self-attestation · CONFIRMED, refined beyond the proposed fix

**Verdict: the trap is real, and it is worse than a wording problem.** If checkpoint verification at the activational tier rests on querying the model and reading its answers, then verification rests on generative text — the exact Tier-3 evidence class (unreliable, condition-dependent, prone to fluent confabulation) that §3/§4 establish as insufficient. The architecture would claim Tier-1 cryptography for the archival tier while its activational-tier fallback silently regresses to the evidence class it rejected. Left as the reviewer's minimal fix (demote to open challenge, one sentence), the ceiling would have remained implicit — and an implicit ceiling in a paper about naming ceilings is its own defect.

**Fix applied (adopted by operator ruling).** §6.2 states the stronger and honest form: **behavioral probes are a one-sided instrument.** Corruption is refutable — a probe whose output diverges from the pinned checkpoint kills the checkpoint. Integrity is never confirmable behaviorally — a probe that agrees is exactly what a corrupted-but-internally-consistent state would also emit. Probes therefore aid detection; they do not elevate the activational tier to Tier-1, and the paper does not claim they do. The one-sidedness is now named in-paper rather than left for the next reviewer to find.

**Verification.** Language canonical in v1.5; operator adoption ruling registered in the decisions ledger; consistent with R2-33's product-level restatement.

### R2-35 — Single-operator degeneration: the sole key-holder signs everything · CONFIRMED, refined

**Verdict: confirmed, and the floor is cryptographic, not procedural.** §6.4 already conceded the degenerate single-writer case; the reviewer located what lies beneath it. At n=1, the sole holder of the release key signs authorized errata and unilateral rewrites alike — **the verification layer cannot distinguish them**. The public append-only record and out-of-band auditability deliver **detectability, never prevention**. The Proposal ⊥ Adjudication ⊥ Commit separation is a property of the multi-party form; it holds only at n ≥ 2. No compensating control exists at n=1 beyond what the record actually provides, and the paper does not claim one.

**Fix applied (adopted by operator ruling).** §6.4/§9 state the floor exactly: the n=1 field program is auditability-not-prevention; the governance triad's separation holds at n ≥ 2; the n=1 instantiation is labeled as the degenerate case rather than compensated in prose.

**Verification.** Language canonical in v1.5; operator adoption ruling registered in the decisions ledger.

---

### Process integrity of this review loop

Four rounds of the tier-2 gauntlet, for the record: **round 1** (v1.2): 8 findings — all confirmed in substance, absorbed into v1.3. **Round 3** (v1.3): 6 findings — 4 confirmed with refinements, 1 rebutted on byte-evidence (the truncation claim was false for the deposited v1.3 PDF: the fingerprint and bundle-digest rows are present, page 18 complete; the reviewer's 22-page budget was stale — v1.3 is 24pp), 1 split verdict (packfile nondeterminism conceded; the reviewer's fix corrected twice on measurement — `main^{tree}` is SHA-1 in this repository, 40-hex, and no SHA-256 tree exists without an object-format migration; `git archive --sort=name` is an invalid flag, exit 129 tested — the adopted deterministic anchor is `git archive --format=tar origin/main | sha256sum`, byte-identical on re-run), 1 gap filled (the missing Algorithm-1 execution entry — filled with the real instantiation, not the proposed nonexistent script). **Round 4** (v1.4): this document, 7/7 confirmed, 0 rebutted.

The loop's own verification discipline: every reviewer quote machine-checked against source and deposited PDF before verdict; every disposition registered publicly with the alternatives rejected; every fix verified in the printed output, not just the source. The paper's thesis — that untrusted surfaces require pinned, independently auditable state — is the standard this review chain holds itself to.

### Build gates for the v1.5 relay

The counters above are canonical only against a build that carries the fixes. Verification gates before relay: zero unresolved references; all nine Table 2 rows in print with continuation header; all eight Table 5 anchors byte-complete; appendix commands inside margins; §5/§6.2/§6.4/§9 language matching the dispositions above; sole authorship intact; build-time digests re-emitted and stated in-band with the PDF they attest.

