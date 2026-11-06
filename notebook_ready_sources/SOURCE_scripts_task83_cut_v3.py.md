# Telemetry Source: scripts/task83_cut_v3.py
- **Source Identifier**: `scripts/task83_cut_v3.py`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `60db0d5c7616de18131d9d49d61a2822b1142497625cf711673442ba017aa802`

---

## Raw Telemetry Content

```
#!/usr/bin/env python3
"""task83_cut_v3.py — tex-v3 + bib-v3 deterministic cut (the GO-FIX round).

Task 83 (2026-11-01, trace 1a19470a33de4459). The operator returned GO on the
Task-82 FIX-BEFORE-SUBMIT recommendation. This tool applies EXACTLY the
Task-82 verdict-ledger confirmed defect set (ARGON §1 findings, verified
witness-side against the locked v2 bytes) — nothing else:

  TEX: (1) \\setcounter{secnumdepth}{0} (double-numbering fix);
       (2) twelve math-escape site repairs (incl. the critical literal-
           underscore site in the section on chained restores);
       (3) thebibliography repairs (chacon2014git un-truncated from the .bib
           of record; 5 two-author comma-before-and sites; lahoti2026mamba3
           venue normalization).
  BIB: lahoti2026mamba3 re-typed @article -> @inproceedings (journal ->
       booktitle) — the lone ICLR-as-@article outlier.

REJECTED by Task-82 adjudication and NOT applied: ARGON's \\nocite{*} patch
(a no-op before a manual thebibliography).

Companion fixes (registered in the build ledger, same-sentence siblings of
flagged sites, identical defect class): the (B = 1) twin of the flagged
(B \\textgreater{} 1); the lahoti "In " venue prefix.

Method: read tex-v2/bib-v2 (liveness-pinned), assert every replacement
matches its expected count exactly (fail-closed), write the v3 paths, and
re-hash the v2 inputs to prove they were read-only. GUP-class: v2 bytes +
this script = v3 bytes, recomputable from the repository alone.

Usage: python3 scripts/task83_cut_v3.py   (from the repo root)
"""
import hashlib
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEX2 = REPO / "write-ups/paper-2-v1.7-draft3-1-latex-v2.tex"
BIB2 = REPO / "write-ups/paper-2-v1.7-draft3-1-bib-v2.bib"
TEX3 = REPO / "write-ups/paper-2-v1.7-draft3-1-latex-v3.tex"
BIB3 = REPO / "write-ups/paper-2-v1.7-draft3-1-bib-v3.bib"

PIN_TEX2 = "687c19d65c9cf091cfd9cdd83bdf04f1c359382a602340b38a41a1751bf41694"
PIN_BIB2 = "18d1e05fbdc7258df181aaf98d894534f308b94c7f8ff4c8931a66a410c5599e"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sub(text, old, new, count, what):
    n = text.count(old)
    if n != count:
        sys.exit(f"FAIL-CLOSED [{what}]: expected {count} occurrence(s), "
                 f"found {n} — v2 bytes are not as registered; halting")
    return text.replace(old, new)


TEX3_HEADER = (
    "%% paper-2-v1.7-draft3-1-latex-v3.tex — GO-FIX deposit build (Task-83, trace\n"
    "%% 1a19470a33de4459). Base: paper-2-v1.7-draft3-1-latex-v2.tex (sha256 687c19d6...,\n"
    "%% Task-73, byte-preserved in-repo as its own file; its header rides below).\n"
    "%% Registered GO-FIX deltas ONLY (the Task-82 verdict-ledger confirmed set —\n"
    "%% ARGON §1 findings verified witness-side against the locked v2 bytes):\n"
    "%% (1) \\setcounter{secnumdepth}{0} — the 8 manually-numbered sections render\n"
    "%%     \"1. Introduction\" not \"4 1. Introduction\" (the double-numbering\n"
    "%%     defect carried by both prior renders, 33pp v1 and 35pp v2);\n"
    "%% (2) twelve math-escape site repairs: B>1 (+ its paired B=1 sibling);\n"
    "%%     window W; the W_Q/W_K/W_V family + W+dW; k-of-n at 3 sites; the\n"
    "%%     critical Delta_t^{(ell)} literal-underscore/caret/brace site (+ k_t\n"
    "%%     + ell'>ell); the two \\neq splits; beta=1; d>=3;\n"
    "%% (3) thebibliography repairs: chacon2014git un-truncated (fields from\n"
    "%%     the .bib of record); 5 two-author comma-before-and sites;\n"
    "%%     lahoti2026mamba3 venue normalization.\n"
    "%% NO content, math, or claim bytes moved; draft-3.1 markdown byte-frozen\n"
    "%% (9b326af7...). The ARGON \\nocite{*} patch REJECTED (no-op before a\n"
    "%% manual thebibliography — Task-82 adjudication). Build ledger:\n"
    "%% write-ups/paper-2-v1.7-task83-fix-build-ledger-v1.md.\n"
)

BIB3_HEADER = (
    "% paper-2-v1.7-draft3-1-bib-v3.bib — GO-FIX deposit bibliography (Task-83,\n"
    "% trace 1a19470a33de4459). Base: paper-2-v1.7-draft3-1-bib-v2.bib (sha256\n"
    "% 18d1e05f..., Task-73, byte-preserved in-repo as its own file; its header\n"
    "% rides below). Registered GO-FIX delta ONLY: lahoti2026mamba3 re-typed\n"
    "% @article -> @inproceedings with journal -> booktitle (the lone\n"
    "% ICLR-as-@article outlier — Task-82 verdict ledger). NO other entry\n"
    "% touched.\n"
    "%\n"
)


def main() -> None:
    # --- liveness: the v2 inputs must hash their pins of record ---------------
    if sha(TEX2) != PIN_TEX2:
        sys.exit(f"FAIL-CLOSED: tex-v2 liveness broken — {sha(TEX2)} != {PIN_TEX2}")
    if sha(BIB2) != PIN_BIB2:
        sys.exit(f"FAIL-CLOSED: bib-v2 liveness broken — {sha(BIB2)} != {PIN_BIB2}")

    # The patches + negative guards operate on the v2 BODY only; the v3
    # provenance headers are prepended at write time so the guards can never
    # false-positive on the header's own descriptions of the defect classes.
    tex = TEX2.read_text(encoding="utf-8")

    # --- (1) secnumdepth ------------------------------------------------------
    tex = sub(tex,
              "\\newcommand{\\target}{TARGET}\n",
              "\\newcommand{\\target}{TARGET}\n"
              "%% GO-FIX (1): manual section numbers only — auto-numbering off.\n"
              "\\setcounter{secnumdepth}{0}\n",
              1, "secnumdepth insertion")

    # --- (2) math-escape repairs (Task-82 ledger order) -----------------------
    tex = sub(tex,
              "parallel scan (B \\textgreater{} 1) and step-by-step recurrent "
              "evaluation (B = 1) are algebraically identical",
              "parallel scan (\\(B > 1\\)) and step-by-step recurrent "
              "evaluation (\\(B = 1\\)) are algebraically identical",
              1, "L166 B>1 (+B=1 companion)")
    tex = sub(tex,
              "paired with a bounded window W in sliding-window hybrid stacks",
              "paired with a bounded window \\(W\\) in sliding-window hybrid "
              "stacks",
              1, "L178 window W")
    tex = sub(tex,
              "(W\\_Q, W\\_K, W\\_V, \\(W_{\\alpha}\\), \\(W_{\\beta}\\))",
              "(\\(W_Q, W_K, W_V\\), \\(W_{\\alpha}\\), \\(W_{\\beta}\\))",
              1, "L250 W_Q family")
    tex = sub(tex,
              "under W + \\(\\Delta W\\) at C2/C3",
              "under \\(W + \\Delta W\\) at C2/C3",
              1, "L250 W+dW")
    tex = sub(tex,
              "threshold signatures --- k-of-n validity across roles",
              "threshold signatures --- \\(k\\)-of-\\(n\\) validity across roles",
              1, "L258 k-of-n (a)")
    tex = sub(tex,
              "plus k-of-n signatures over the index",
              "plus \\(k\\)-of-\\(n\\) signatures over the index",
              1, "L258 k-of-n (b)")
    tex = sub(tex,
              "a state perturbation \\(\\Delta\\)\\_t\\^{}\\{(\\(\\ell\\))\\} in "
              "layer \\(\\ell\\) perturbs",
              "a state perturbation \\(\\Delta_t^{(\\ell)}\\) in "
              "layer \\(\\ell\\) perturbs",
              1, "L266 critical Delta_t site")
    tex = sub(tex,
              "orthogonal to k\\_t (record: R2-33",
              "orthogonal to \\(k_t\\) (record: R2-33",
              1, "L266 k_t")
    tex = sub(tex,
              "of layers \\(\\ell'\\) \\textgreater{} \\(\\ell\\), introducing",
              "of layers \\(\\ell' > \\ell\\), introducing",
              1, "L266 ell'>ell")
    tex = sub(tex,
              "\\(\\operatorname{Im}(q_i^\\dagger k_j)\\) \\(\\neq\\) 0)",
              "\\(\\operatorname{Im}(q_i^\\dagger k_j) \\neq 0\\))",
              1, "L270 neq split (a)")
    tex = sub(tex,
              "(\\([\\hat{H}_{\\text{intent}}, \\hat{H}_{\\text{context}}]\\) "
              "\\(\\neq\\) 0)",
              "\\([\\hat{H}_{\\text{intent}}, \\hat{H}_{\\text{context}}] "
              "\\neq 0\\)",
              1, "L270 neq split (b)")
    tex = sub(tex,
              "idempotent at \\(\\beta\\) = 1 but non-invertible",
              "idempotent at \\(\\beta = 1\\) but non-invertible",
              1, "L270 beta=1")
    tex = sub(tex,
              "every d \\(\\geq\\) 3, every spin",
              "every \\(d \\geq 3\\), every spin",
              1, "L274 d>=3")
    tex = sub(tex,
              "compromising all k-of-n cosigning roles",
              "compromising all \\(k\\)-of-\\(n\\) cosigning roles",
              1, "L444 k-of-n (c)")

    # --- (3) thebibliography repairs ------------------------------------------
    tex = sub(tex,
              "\\bibitem{dao2024mamba2} Tri Dao, and Albert Gu.",
              "\\bibitem{dao2024mamba2} Tri Dao and Albert Gu.",
              1, "L614 dao comma")
    tex = sub(tex,
              "\\bibitem{widrow1960adaptive} Bernard Widrow, and Marcian E. Hoff.",
              "\\bibitem{widrow1960adaptive} Bernard Widrow and Marcian E. Hoff.",
              1, "L618 widrow comma")
    tex = sub(tex,
              "\\bibitem{bischof1985wy} Christian H. Bischof, and Charles Van Loan.",
              "\\bibitem{bischof1985wy} Christian H. Bischof and Charles Van Loan.",
              1, "L620 bischof comma")
    tex = sub(tex,
              "\\bibitem{costan2016sgx} Victor Costan, and Srinivas Devadas.",
              "\\bibitem{costan2016sgx} Victor Costan and Srinivas Devadas.",
              1, "L632 costan comma")
    tex = sub(tex,
              "\\bibitem{chacon2014git} Scott Chacon, and Ben Straub. ",
              "\\bibitem{chacon2014git} Scott Chacon and Ben Straub. "
              "\\emph{Pro Git}, 2nd ed. Apress, 2014.",
              1, "L642 chacon un-truncate")
    tex = sub(tex,
              "State Space Principles. \\emph{The Fourteenth International "
              "Conference on Learning Representations (ICLR)}, 2026.",
              "State Space Principles. In \\emph{The Fourteenth International "
              "Conference on Learning Representations (ICLR)}, 2026.",
              1, "L616 lahoti venue prefix (companion)")

    bib = BIB3_HEADER + BIB2.read_text(encoding="utf-8")
    bib = sub(bib,
              "@article{lahoti2026mamba3,\n"
              "  author  = {Aakash Lahoti and Kevin Y. Li and Berlin Chen and "
              "Caitlin Wang and Aviv Bick and J. Zico Kolter and Tri Dao and "
              "Albert Gu},\n"
              "  title   = {Mamba-3: Improved Sequence Modeling Using State "
              "Space Principles},\n"
              "  journal = {The Fourteenth International Conference on "
              "Learning Representations (ICLR)},\n"
              "  year    = {2026}\n"
              "}",
              "@inproceedings{lahoti2026mamba3,\n"
              "  author    = {Aakash Lahoti and Kevin Y. Li and Berlin Chen "
              "and Caitlin Wang and Aviv Bick and J. Zico Kolter and Tri Dao "
              "and Albert Gu},\n"
              "  title     = {Mamba-3: Improved Sequence Modeling Using State "
              "Space Principles},\n"
              "  booktitle = {The Fourteenth International Conference on "
              "Learning Representations (ICLR)},\n"
              "  year      = {2026}\n"
              "}",
              1, "bib lahoti @article->@inproceedings")

    # --- negative guards: the defect strings must be GONE in v3 ----------------
    for gone, what in [
        ("\\textgreater{} 1) and step-by-step", "B>1 residue"),
        ("W\\_Q", "W_Q residue"),
        ("\\(\\Delta\\)\\_t", "critical literal-underscore residue"),
        ("\\(\\neq\\) 0", "neq-split residue"),
        ("\\(\\beta\\) = 1", "beta-split residue"),
        ("d \\(\\geq\\) 3", "d-geq residue"),
        ("\\bibitem{dao2024mamba2} Tri Dao, and", "dao comma residue"),
        ("Scott Chacon, and Ben Straub. \n", "chacon truncation residue"),
        (" k-of-n ", "k-of-n residue"),
    ]:
        if gone in tex:
            sys.exit(f"FAIL-CLOSED: {what} still present in tex-v3")
    if "@article{lahoti2026mamba3" in bib or "journal = {The Fourteenth" in bib:
        sys.exit("FAIL-CLOSED: lahoti @article residue in bib-v3")

    TEX3.write_text(TEX3_HEADER + tex, encoding="utf-8")
    BIB3.write_text(BIB3_HEADER + bib, encoding="utf-8")

    # --- read-only proof on the v2 inputs --------------------------------------
    if sha(TEX2) != PIN_TEX2 or sha(BIB2) != PIN_BIB2:
        sys.exit("FAIL-CLOSED: v2 inputs mutated during the cut")

    print(f"[task83_cut_v3] tex-v3: {TEX3.name}  {sha(TEX3)}  "
          f"{len(TEX3.read_bytes())} B")
    print(f"[task83_cut_v3] bib-v3: {BIB3.name}  {sha(BIB3)}  "
          f"{len(BIB3.read_bytes())} B")
    print(f"[task83_cut_v3] tex-v2 re-verified read-only: {PIN_TEX2}")
    print(f"[task83_cut_v3] bib-v2 re-verified read-only: {PIN_BIB2}")


if __name__ == "__main__":
    main()

```
