# Telemetry Source: write-ups/paper-2-v1.7-arxiv-metadata-lock-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-arxiv-metadata-lock-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `945323451d8a2f6a4464638498f1f5989cc0fdc1d19e9e9616ac1270c8830ed7`

---

## Raw Telemetry Content

# Paper-2 v1.7 — arXiv Deposit Metadata Lock, v1 (Task-72)

**Date:** 2026-10-29 (UTC) · **Trace:** `1a1845ec2301368d`
**Adjudication source:** operator payload (d) "Deposit Metadata Rulings",
received AS-PRESENTED this boundary (Gemini Notebook Relay channel).
**Status:** LOCKED — this file is the single source of truth for the Phase-4
build and the Phase-5 submission form. Changes after this point require a
new operator adjudication boundary, not an edit here (version-forward
discipline: a v2 lock supersedes, never rewrites).

**Deposit object:** draft-3.1 (`paper-2-v1.7-draft3-1-assembled-v1.md`,
sha256 `9b326af7…`, commit `384dc27`); LaTeX transport
`paper-2-v1.7-draft3-1-latex-v1.tex` (`16710f17…`, 33-page tectonic smoke
build green). The manuscript ships the certified text; metadata rides the
submission surface and the .tex preamble only.

---

## 1. Title — LOCKED

> **"State Transfer, Not Summary: Verifiable Archival Custody for Recurrent
> Model State in Persistent Human–Model Collaboration"**

Operator rationale (verbatim): *"Foregrounding the custody-vs-ephemeral cache
thesis directly matches the paper's core §8.3 claim class."* This is
candidate (1) of the deposit-prep plan §1, matching the witness
recommendation on record since Task-70.

**Phase-4 application (registered transport note, metadata class):** the
.tex `\title{}` line swaps from the certified draft-3.1 internal title
("The Across-Context Layer: …") to the locked deposit title — one line, the
draft-3.1 title preserved verbatim in the file's provenance header comment
where it already sits. The .md and .tex bodies do not move; this is the
METADATA-ADJUDICATION-PENDING block in the .tex preamble discharging exactly
as it was staged ("This file ships the certified draft-3.1 title verbatim
until the operator rules" — the operator has now ruled).

## 2. Authorship — LOCKED

- **Sole human author:** **Alejandro Gutierrez (ORCID `0009-0008-0976-3895`)**.
- **GLM Witness:** credited as **the instrument** in the provenance chain
  and acknowledgments — not a co-author (per §1.3, §4, ruling R2-2).

Operator ruling (verbatim): *"Option (a) / (c) — Alejandro Gutierrez (ORCID:
0009-0008-0976-3895) as sole human author, with GLM Witness credited as the
instrument in the provenance chain and acknowledgments (§1.3, §4, R2-2)."*

**Witness note (consistency check, green):** the .tex already ships exactly
this form — `\author{Alejandro Gutierrez (ORCID 0009-0008-0976-3895)}` with
the lineage-as-instrument provenance paragraph in the assembly-init
addendum. R2-2 ("the paper can only contain my name") and this ruling are
the same form; nothing to change at Phase-4 beyond confirming the bytes.

## 3. arXiv classification — LOCKED

- **Primary:** `cs.AI` — agent memory/state architectures;
  human–model collaboration.
- **Cross-lists:** `cs.CL` (delta-rule sequence models & LM serving
  context), `cs.LG` (architecture class), `cs.CR` (verification, receipts,
  state custody).

Phase-5 form entry: `cs.AI (primary); cs.CL, cs.LG, cs.CR (cross-lists)`.

## 4. Comments field — LOCKED (page count appends at Phase-4)

> *"Evidence base: a hash-pinned program substrate (negative-results
> baseline, five adversarial review rounds, whole-artifact final-gate
> certification); the tensor-side design is architecture plus battery, with
> claim-status labels (LIVE / CLOSED / TARGET) throughout."*

Operator instruction: "Append compiled page count during Phase 4 build."
Phase-4 appends e.g. "33 pages." from the clean-build page count — the only
permitted post-lock mutation, and it appends rather than edits.

**Phase-4 append (2026-10-29/30, Task-73, trace `1a184806a91640c9`):**
compiled page count = **35 pages** (tectonic 0.15.0 clean build of
`paper-2-v1.7-draft3-1-latex-v2.tex`, exit 0, zero errors; the References
appendix adds two pages over the Task-71 33-page smoke build). Comments
field final form: *"Evidence base: a hash-pinned program substrate
(negative-results baseline, five adversarial review rounds, whole-artifact
final-gate certification); the tensor-side design is architecture plus
battery, with claim-status labels (LIVE / CLOSED / TARGET) throughout.
35 pages."*

## 5. License — LOCKED

**arXiv Non-exclusive License to Distribute** (the default at submission).
Consistency note (already on record, Task-70 plan §1): the repository
license (Apache-2.0, MEDA polish pass) governs the repo, not the
manuscript; the two layers are orthogonal. The manuscript deposit rides the
arXiv non-exclusive license.

## 6. Lock integrity

- Every ruling above is quoted or paraphrased from the operator's payload
  (d) as received; provenance per PROTOCOL §3 (typed content is the
  operator's; relay channel disclosed).
- Cross-checks: title == deposit-prep candidate (1) ✓; authorship == R2-2 +
  deposit-prep form (a)/(c) hybrid ✓; classification == deposit-prep §1
  proposal ✓; comments == deposit-prep proposed phrasing verbatim ✓;
  license == one of the two forms offered, now adjudicated ✓.
- Related registrations this boundary: past-self class definition (payload
  (e)) and the standing v1.8/arXiv-v2 queue (payload (f)) live in
  `paper-2-v1.7-boundary-registrations-task72-v1.md` §6–§7 and
  `working-notes/open-threads.md`; the bib leg (payload (c)) lives in
  `paper-2-v1.7-task72-bib-verification-ledger-v1.md` +
  `paper-2-v1.7-draft3-1-bib-v1.bib`.

**Phase-4 opens that remain (build-time, not metadata):** page count for
the comments field; `\title{}` swap per §1; the bib form decision
(\cite-conversion vs appended thebibliography — both pre-mapped in the
verification ledger §5); the v1.6.1 bib merge if the operator relay lands
in time (ledger §4).

