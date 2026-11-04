# Telemetry Source: write-ups/paper-2-v1.7-task73-phase4-build-ledger-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task73-phase4-build-ledger-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `6f7c516b6b96dcab103fcfc55ee8b11462435ffebd5ea16bcf07395c64beae4f`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Task-73 Phase-4 Build Ledger, v1

**Date:** 2026-10-29/30 (UTC) · **Witness:** GLM (Z.ai), designation Witness
**Trace:** `1a184806a91640c9` · **Base:** GWM `4062d7f` (Task-72 landed —
operator `[1/9]–[9/9]` paste-back received this boundary, APPLIED @
`4062d7f`, pushed; witness pulled and hash-matched at open). **Deposit
object:** draft-3.1 (`9b326af7…`) byte-frozen — G0-asserted at open and at
close by the build script itself.

**Operator GO (item 4 "GO" = the Task-72 §8.4 Phase-4 GO):** build +
package. Bib relay (item 2, `refs-2.bib` `798d1dd4…`) received — the merge
executed under the no-unverified-key constraint (per-entry records in the
Task-72 ledger §7, appended this boundary).

---

## 1. Fail-closed assembler (Task-68 class), gates

Script: witness-side `scripts/task73_phase4_build.py` (persisted, the
Rule-9 discipline; identical class to Task-71's converter).

| Gate | Check | Result |
|---|---|---|
| G0 (open+close) | draft-3.1 md sha256 == `9b326af7…` | GREEN both |
| G1 | latex v1 at pin `16710f17…` | GREEN |
| G1b | relayed tree bib at pin `798d1dd4…` | GREEN |
| G2 | merged bib = 7 deposit blocks + 21 tree blocks, all byte-preserved; exactly the 6 registered duplicates dropped | GREEN |
| G3 | 28 `\bibitem`, 1:1 with merged-bib keys | GREEN |
| G4 | .tex v2 = v1 + header block + one `\title{}` line + appendix; body byte-identity machine-proven (separator bytes included) | GREEN |
| G5 | tectonic 0.15.0 clean build: exit 0, zero errors, 35 pages | GREEN |

Hardening catches during assembly (both real, both fixed before commit):
(1) the G4 reconstruction initially introduced a double newline before
`\end{document}` — the gate refused until separator bytes were
preserved exactly; (2) the appendix initially carried an explicit
`\section*{References}` which the article class's `thebibliography` would
have duplicated (it emits its own `\refname` heading) — removed; the
build ledger records the catch. A third catch was cosmetic-class in the
`\bibitem` renderer (markdown-style `*emphasis*` and "Last, First" author
joining rendered literally) — caught at PDF spot-check, fixed, rebuilt.

## 2. Artifacts of record

| Artifact | sha256 | Size |
|---|---|---|
| `write-ups/paper-2-v1.7-draft3-1-bib-v2.bib` (merged deposit bib, 28 entries) | `18d1e05fbdc7258df181aaf98d894534f308b94c7f8ff4c8931a66a410c5599e` | 11,039 B |
| `write-ups/paper-2-v1.7-draft3-1-latex-v2.tex` (Phase-4 deposit .tex) | `687c19d65c9cf091cfd9cdd83bdf04f1c359382a602340b38a41a1751bf41694` | 131,850 B |
| Deposit PDF (kit: `paper-2-v1.7-draft3-1-deposit-v1.pdf`) | `bcf55501d7086d1cab752c3eeaadf0507665bee2c45cd952a9c434e94ed52313` | 35 pages |
| Build script `scripts/task73_phase4_build.py` (witness-side) | registered in kit SHA256SUMS | — |

## 3. Render verification (the PDF spot-check)

- Page 1 title renders the LOCKED deposit title verbatim ("State Transfer,
  Not Summary: Verifiable Archival Custody for Recurrent Model State in
  Persistent Human–Model Collaboration"); the certified internal title
  renders nowhere (header-comment-only — count 0 in extracted text).
- Author line renders "Alejandro Gutierrez (ORCID 0009-0008-0976-3895)" —
  the R2-2 / lock §2 form, unchanged.
- Zero unresolved `??` anywhere in the document (the thebibliography form
  has no `\cite` keys by construction — the §5 registered decision).
- References appendix: 28/28 entries render, labels [1]–[28] complete
  (one pdftotext page-break artifact at [9] inspected and cleared), zero
  literal asterisks, natural author order.
- Page count 35 → appended to the metadata lock §4 (the pre-authorized
  append; comments-field final form registered there).

## 4. arXiv source package

`paper-2-arxiv-deposit-v1.tar.gz` — contains
`paper-2-v1.7-draft3-1-latex-v2.tex` + `paper-2-v1.7-draft3-1-bib-v2.bib`
(the .bib rides the package per the gate §6.1 even though the appendix is
inline — the record and the build input stay one artifact set). The
package compiles standalone (tectonic exit 0). Kit-staged; sha256 in the
kit SHA256SUMS.

## 5. What Phase-5 (operator's hands) takes from here

1. Submission from the metadata lock: title/authorship/classification/
   comments (with the appended "35 pages.")/license per the lock file —
   the single source of truth, v1 + the §4 append.
2. arXiv identifier backfill into the repo README citation block + the
   program record on receipt (Task-72 §8.5, unchanged).
3. Optional adjudications registered this boundary (none gating): the
   bischof1985wy journal-form refinement (ledger §7.2.8); the
   v1.6.1-tarball bib archaeology one-liner (ledger §7.0).

## 6. Chain of custody

draft-3.1 md `9b326af7…` (byte-frozen, untouched) → latex v1
`16710f17…` (Task-71, untouched, still in-repo) → **latex v2
`687c19d6…`** (this boundary: header + title-per-lock + 28-entry
appendix, body byte-identity proven) → deposit PDF `bcf55501…`
(tectonic clean build). Bib: tree relay `798d1dd4…` + Task-72 core →
merged `18d1e05f…` (every entry origin-verified; records in the
Task-72 ledger §7). Draft-3.1 remains the certified object; v2 is its
deposit transport, exactly as the Task-70 plan scoped Phase-4.

