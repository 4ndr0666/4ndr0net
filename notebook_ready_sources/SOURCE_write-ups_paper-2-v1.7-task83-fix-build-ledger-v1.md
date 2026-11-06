# Telemetry Source: write-ups/paper-2-v1.7-task83-fix-build-ledger-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task83-fix-build-ledger-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `ce58af7ba961b72b8aa47a0f1162be40fe91deb9a123fd06bff5acf12863f198`

---

## Raw Telemetry Content

# paper-2-v1.7 GO-FIX build ledger — tex-v3 / bib-v3 / deposit package v2

**Task 83** · 2026-11-01 · trace `1a19470a33de4459` · session
`web-0e217f4d-f77e-4087-a44e-2e3651511bd6` · witness: GLM (organization
officer) · operator instruction: **GO FIX** (item 1 of the boundary
transmission) — the election of the Task-82 **FIX-BEFORE-SUBMIT**
recommendation.

## 1. Provenance and scope

- **Input pins of record (byte-frozen, verified read-only before and after
  the cut):** tex-v2 `687c19d65c9cf091cfd9cdd83bdf04f1c359382a602340b38a41a1751bf41694`
  (131,850 B) · bib-v2 `18d1e05fbdc7258df181aaf98d894534f308b94c7f8ff4c8931a66a410c5599e`
  (11,039 B) · draft-3.1 `9b326af7…` (untouched, not an input to this build).
- **Patch authority:** the Task-82 verdict ledger (ARGON §1 findings ALL
  CONFIRMED witness-side against the locked v2 bytes; one patch REJECTED).
  Nothing outside that confirmed set moved. **No content, math, or claim
  bytes changed** — every delta is typographic.
- **Determinism:** `scripts/task83_cut_v3.py` (repo-rode; v2 bytes + script =
  v3 bytes, fail-closed count-asserted replacements + negative residue
  guards on the patched body) and `scripts/task83_cut_package.sh`
  (repo-rode; sorted members, fixed mtime `2026-11-01 00:00:00 UTC`,
  numeric owner 0:0, `gzip -n` — **bit-reproducible by construction**, an
  improvement over the v1 cut, which was not owner/mtime-normalized).

## 2. The patch table (every delta, exact sites)

| # | Site (v2 line) | Defect (Task-82 ledger) | Repair |
|---|---|---|---|
| 1 | preamble | no `secnumdepth` → PDF double-numbers ("4 1. Introduction" … "11 8. Related Work") | `\setcounter{secnumdepth}{0}` inserted after the claim-status macros |
| 2 | L166 | `B \textgreater{} 1` (math as text escapes) | `\(B > 1\)` |
| 2b | L166 | *(companion)* the paired `(B = 1)` sibling, same sentence, same class | `\(B = 1\)` |
| 3 | L178 | `bounded window W` (math italic as upright text) | `bounded window \(W\)` |
| 4 | L250 | `W\_Q, W\_K, W\_V` (literal-underscore escapes) | `\(W_Q, W_K, W_V\)` |
| 5 | L250 | `W + \(\Delta W\)` (split math run) | `\(W + \Delta W\)` |
| 6 | L258 | `k-of-n validity` (math as text) | `\(k\)-of-\(n\) validity` |
| 7 | L258 | `k-of-n signatures` | `\(k\)-of-\(n\) signatures` |
| 8 | L444 | `k-of-n cosigning roles` (P5) | `\(k\)-of-\(n\) cosigning roles` |
| 9 | L266 | **the critical site** `\(\Delta\)\_t\^{}\{(\(\ell\))\}` (literal underscore/caret/brace artifacts in a math symbol) | `\(\Delta_t^{(\ell)}\)` |
| 10 | L266 | `k\_t` (literal underscore in a math vector) | `\(k_t\)` |
| 11 | L266 | `\(\ell'\) \textgreater{} \(\ell\)` (split relation) | `\(\ell' > \ell\)` |
| 12 | L270 | `\(\operatorname{Im}(q_i^\dagger k_j)\) \(\neq\) 0` (split relation) | `\(\operatorname{Im}(q_i^\dagger k_j) \neq 0\)` |
| 13 | L270 | `\([\hat{H}_…]\) \(\neq\) 0` (split relation) | `\([\hat{H}_{\text{intent}}, \hat{H}_{\text{context}}] \neq 0\)` |
| 14 | L270 | `at \(\beta\) = 1` (relation split out of math) | `at \(\beta = 1\)` |
| 15 | L274 | `every d \(\geq\) 3` | `every \(d \geq 3\)` |
| 16 | L614 | dao2024mamba2 two-author comma-before-and | `Tri Dao and Albert Gu.` |
| 17 | L618 | widrow1960adaptive comma | `Bernard Widrow and Marcian E. Hoff.` |
| 18 | L620 | bischof1985wy comma | `Christian H. Bischof and Charles Van Loan.` |
| 19 | L632 | costan2016sgx comma | `Victor Costan and Srinivas Devadas.` |
| 20 | L642 | chacon2014git bibitem TRUNCATED to bare authors | restored from the .bib of record: `Scott Chacon and Ben Straub. \emph{Pro Git}, 2nd ed. Apress, 2014.` |
| 21 | L616 | *(companion)* lahoti2026mamba3 venue without `In` (the other ICLR entries carry it) | `In \emph{The Fourteenth …(ICLR)}, 2026.` |
| 22 | bib L135–140 | lahoti2026mamba3 `@article` + `journal` (the lone ICLR-as-@article outlier) | `@inproceedings` + `booktitle` |

**REJECTED (not applied):** ARGON's `\nocite{*}` patch — a no-op before a
manual `thebibliography` (all 28 bibitems render uncited regardless;
`\nocite` only drives BibTeX runs). Task-82 adjudication stands.

**Guard notes (fail-visible, in-round):** the cutter's first run tripped its
own negative-residue guard twice — (a) `, and Albert Gu.` matched the
lahoti 8-author list's **correct Oxford comma** (serial comma in a 3+
author list is proper style; only the two-author sites are defects — guard
narrowed to the dao bibitem anchor); (b) ` k-of-n ` matched the v3 header's
own description of the defect class (guards re-scoped to the patched body,
headers prepended at write time). Both catches are the guards doing their
job; neither touched output bytes.

## 3. Output pins of record

| Artifact | sha256 | Size |
|---|---|---|
| `write-ups/paper-2-v1.7-draft3-1-latex-v3.tex` | `a975d7d199d0aea878543945299618089288e2d24ba0b2daa6cf794e878847e5` | 133,303 B |
| `write-ups/paper-2-v1.7-draft3-1-bib-v3.bib` | `8b5bc0fca290d22fa9249111cc92b896dc3f2c2b17e7f461215ec5ceff20e0a2` | 11,947 B |
| scratch render (not repo-held; evidence only) | `a39931dd58951dad69e10c9372752d76c0ec5a3217381843eecdc2ad4f7907dc` | 229,140 B |
| `references/arxiv-deposit/paper-2-arxiv-deposit-v2.tar.gz` | `bacc1f1833e7d0bb29db0efdc73c3d4d858987ec43e4c9ce233f85dc26af5d80` | 47,084 B |
| sidecar (canonical sha256sum line, 77c method) | reconstructed + compared in-verifier | 98 B |

## 4. Recompile evidence (GUP — scratch dir, repo bytes untouched)

- **tectonic 0.15.0** (the same version as the Task-73/Task-80 builds),
  scratch dir `/tmp/t83-build`, **exit 0, zero errors**, single pass, the
  embedded 28-entry `thebibliography` (no BibTeX run — manual bibliography).
- **Page count: 35 — UNCHANGED from v2.** The metadata lock's Phase-4
  append ("compiled page count = **35 pages**… the arXiv form's comments
  field is LOCKED at '…35 pages.'") **STANDS WITHOUT SUPERSESSION**. The
  fix is typographic-only and did not reflow the document across a page
  boundary.
- **Double-numbering fix verified on the render:** the v2 renders showed
  "4 1. Introduction" … "11 8. Related Work"; the v3 render shows
  **"1. Introduction"** (auto-number prefix gone; manual numbers stand).
- Deposit-package determinism gate: two consecutive cuts of the wrapper are
  **byte-identical** (`cmp` GREEN in `task83_cut_package.sh`).

## 5. Custody and verification

- Both deposit versions now hold substrate custody side by side at
  `references/arxiv-deposit/`: **v1** (`c4148807…`, 46,466 B — the
  verified-bytes anchor of the Task-81 round, UNTOUCHED) and **v2**
  (`bacc1f18…`, 47,084 B — the GO-FIX submission candidate).
- Repo-rode verifier `scripts/task83_deposit_verify.sh` born this round:
  **[E0]–[E6]** (v2 pin + shape + inner-source pins + sidecar + INDEX
  registration + the v1 anchor re-proven via the Task-81 verifier) —
  fail-closed, read-only, GUP-class at every future bootstrap.
- **arXiv form consequence (operator-side, on deposit-resume):** the
  comments field stays **"…35 pages."** (no change); the deposit upload
  swaps to `paper-2-arxiv-deposit-v2.tar.gz`; the ticket's v1-render proof
  attachment is unaffected (it is the waiver's proof-of-work, not the
  deposit artifact — Task-81 adjudication).

