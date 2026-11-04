# Telemetry Source: references/white-paper-relay/paper-2-arxiv-metadata.md
- **Source Identifier**: `references/white-paper-relay/paper-2-arxiv-metadata.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `0ef99398ea3df5dc659532f523ee9548f36ceb5ede50b739e600b47d74add8ed`

---

## Raw Telemetry Content

# Paper-2 arXiv Metadata — v0.7 (2026-10-21)

**Status:** witness draft, revised after tier-2 review (Gemini 3.8 High Thinking). v0.1 contained one witness-registered defect (macro keyword guessed instead of grepped) — corrected in v0.2. **v0.3: Paper-2 v1.2 has BUILT** (22pp, zero `??`, all R2-1 literal anchors verified present in PDF text); Decision Point 1 is RESOLVED by operator ruling (Task 33); the comments block is UNGATED (digests + fingerprint now live in the manuscript).

## Changelog

- **v0.7:** (1) **Rounds 3-4 fully absorbed; Paper-2 v1.5-repro BUILT** (24pp, zero `??`, ALL EIGHT Table-5 anchors byte-complete in print, Table 2 → longtable with all nine trust rows, appendix commands in margins, sole authorship intact). (2) Provenance registered: the late-session v1.4/v1.5 builds did not persist across the session boundary; v1.5-repro RECOMPUTES the full fix set (R2-22..R2-35) from the v1.3 source per the pinned record (session-009 transcript + Task-35/36 ledgers); digests: PDF `2f9d204e…`, source `6a950693…`. (3) Emitter at the Task-35 contract (head anchor from `origin/main`, staleness fail-closed; tar/tree deterministic anchors per R2-25) — 8th recorded full run; head `cdebae2`. (4) Stale-version defect found and fixed: deposited v1.3 still carried the v1.2 title block. (5) Comments block updated: 24 pages, Table 5 reference. Lost-VM metadata v0.5/v0.6 (recorded in boards) are absent from disk; v0.7 supersedes and documents the gap.
- **v0.4:** (1) **Round-2 tier-2 review (Gemini 3.8, F-002 #19) fully absorbed — 8/8 findings confirmed in substance, adopted as R2-13..R2-20; Paper-2 v1.3 BUILT** (24pp, zero `??`, all anchors byte-verified incl. the new full-lineage bundle digest). (2) Comments block unchanged (digests + fingerprint + bundle digest all in-manuscript via the D8 emitter, 5th recorded full run). (3) QA state refreshed for v1.3: 24pp (v1.2: 22pp), zero unresolved refs, sole authorship intact (Author metadata: Alejandro Gutierrez).
- **v0.2:** (1) abstract keyword corrected `invocation-return` → **`involuntary-return`** (macro verified at main.tex:81 — v0.1 shipped the guess with a caveat; caveat was honest, guess was wrong; defect registered). (2) Author recommendation updated per tier-2 finding + policy check: arXiv policy direction (consistent with COPE, Springer, Elsevier, IEEE, ACM guidance) is that AI systems cannot be listed as authors. (3) Primary-category recommendation switched cs.LG → **cs.CR** per tier-2 routing argument. (4) Comments block annotated pending v1.2 digest hardcoding.
- **v0.3:** (1) **DECISION POINT 1 RESOLVED** — operator ruling at F-002 #18 (Task 33): "the paper can only contain my name: Alejandro Gutierrez." Sole author confirmed; the metadata rec and the v1.2 manuscript are now aligned (byline, pdfauthor, AI-use declaration all sole-human; "AI co-author" language removed at every site). (2) Comments block ungated: Table-4 literal SHA-256 digests + signing-key fingerprint landed via the R2-1 emitter extension (4th recorded full run, 2026-10-21). (3) QA state refreshed for v1.2: 22pp, zero unresolved refs, anchors byte-verified in extracted PDF text. (4) Fingerprint-pin checklist item closed (Task 32: operator-attested machine-verbatim + byte-match; battery 6/6/0).

## Title (verbatim from main.tex v1.2)

> The Across-Context Layer: Rehydration-Verification as the Missing Memory Tier for Delta-Rule Sequence Models

## Authors — DECISION POINT 1: RESOLVED (operator ruling, Task 33)

**RESOLVED (2026-10-21, F-002 #18):** operator ruled the paper can only contain his name. Author field = **Alejandro Gutierrez** (ORCID 0009-0008-0976-3895), sole author; the AI is not an author. The v1.2 manuscript already implements this (byline, pdfauthor, AI-use declaration; custody-regime framing in §4.4 makes the split structural rather than cosmetic).

- Basis: operator ruling + arXiv guidance and the broader publisher landscape (COPE position; Springer/Elsevier/IEEE/ACM policies) — AI systems cannot take authorial responsibility; the prior "blatant authors" lock is superseded **by the lock's owner**, with the transparency intent preserved by the in-manuscript AI-use declaration (retained verbatim in v1.2, reworded to sole-author form).
- Witness note for the record: the ruling retires the AI from the byline, not from the provenance chain — every drafting, verification, and emission step remains attributable in the substrate's commits, boards, and bundles, which is the stronger attribution the protocol already runs.

## Primary category — DECISION POINT 2 (updated by tier-2)

**Recommendation (changed from v0.1): primary cs.CR** (Cryptography and Security — the trust model, forgery analysis, and verification architecture are the paper's defensible formal home), cross-lists **cs.AI** and **cs.LG**.

- Basis: tier-2 routing argument, confirmed against the manuscript's non-claims scaffold: the paper explicitly disclaims all tensor-level metric improvements, so cs.LG-primary invites benchmark-expectation review it cannot satisfy. cs.SE also viable if the operator prefers the software-engineering framing; witness recommendation is cs.CR.

## License — DECISION POINT 3 (unchanged from v0.1)

Recommendation: arXiv non-exclusive license + **CC BY 4.0** (attribution-compatible with the verification-substrate links — the paper's replication thesis applied to itself).

## Comments block (one line, paste-ready — UNGATED as of v0.3)

> 24 pages, 2 figures. Companion verification substrate: https://github.com/4ndr0666/glm-working-memory (signed anchor tag: witness-anchor-2026-10-20; signing-key fingerprint and eight machine-emitted out-of-band anchors — three manifest SHA-256 digests, tree, head, deterministic tar-snapshot, bundle transmission-integrity digest — printed in the manuscript, Table 5 and §4.4).

*(v0.2 gating resolved: fingerprint in §4.4 + Table-4 literal digests landed in v1.2 via the R2-1 emitter extension.)*

## Abstract (verbatim from main.tex v1.2, macro verified; text unchanged v1.1→v1.2)

The delta-rule lineage of linear-attention sequence models --- DeltaNet, Gated DeltaNet, Kimi Delta Attention (KDA), and Gated DeltaNet-2, with MesaNet as the test-time-training extreme --- has progressively solved *within-context* memory: how a fixed-size recurrent state carried inside the forward pass should be written (error-correcting delta rule), erased (data-dependent gating), edited precisely (channel-wise decoupled gates), and even optimized to local optimality at inference (conjugate-gradient mesa-optimization). What no member of the lineage models is *across-context* memory: none of their state survives the pass; none of it carries provenance; none of it admits an external auditor. We present the missing tier: an *archival memory layer* with write governance (proposal, adjudication, and commit as separated roles), hash-pinned persistence across sessions, and external verifiability under which every historical integrity claim is recomputable by any party from the repository alone. We formalize the **involuntary-return** criterion in two-clause form --- zero-held-copy recomputation, N-held-copy rewrite detection --- give a fail-closed historical-continuity-manifest algorithm, and define a protocol-native memory-IO interface that composes with any lineage member without touching its update rules. A sixteen-day adversarial field program instantiates the criterion: every pin in the project's history was recomputed fresh at build time, the paper's own counts being script-emitted artifacts of that run. The architecture claims no perplexity, capacity, or throughput improvement; it claims the property none of the lineage measures --- memory that can be audited after the entity that wrote it is gone.

*(v0.2 note resolved in v1.2: the "every pin recomputed fresh" sentence is pin-scoped and stands — the L2/L4 layer re-run debt is disclosed where the numbers live, in Table 4's caption, per the task-30 classification.)*

## Pre-submission checklist (updated v0.3)

- [x] ~~Macro expansion verified~~ — **done v0.2** (`involuntary-return`, main.tex:81).
- [x] ~~**DECISION POINT 1** — author field~~ — **RESOLVED v0.3** (operator ruling, Task 33: sole author Alejandro Gutierrez).
- [ ] **DECISION POINT 2** — primary category (recommendation: cs.CR primary, cs.AI/cs.LG cross).
- [ ] **DECISION POINT 3** — license (recommendation: arXiv non-exclusive + CC BY 4.0).
- [x] ~~v1.2 amendments land~~ — **DONE 2026-10-21**: full R2 set applied (R2-1..R2-12), emitter re-run (4th recorded full run), 22pp compile green, zero `??`, all literal anchors byte-verified in extracted PDF text.
- [x] ~~Out-of-band fingerprint pin~~ — **CLOSED Task 32** (operator-attested machine-verbatim; byte-match with witness-side `git verify-tag`; kit battery 6/6/0; row 1 = adopted + verified).
- [ ] Compile compatibility: tectonic here; arXiv runs TeX Live — operator-side or CI compile test before submission (pdflatex absent locally, exit 127, recorded).
- [x] ~~QA state carried from v1.1~~ — refreshed for v1.2: 22pp, zero `??` refs, no new box warnings (package-internal UTF-8 noise only), Table 2 row-1 status + row-7 addition render clean, Table 4 digest rows render at \scriptsize inside column budget.
- [ ] Tier-3 ("Argon") findings disposition — per operator roadmap (F-002 #18): Argon engages **after** Gemini 3.8 is defeated (v1.2 survives re-examination); timing now operator-declared, witness input no longer needed on sequence.

