# Telemetry Source: write-ups/paper-2-round5.4-counters-v1.md
- **Source Identifier**: `write-ups/paper-2-round5.4-counters-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `8c3f0497fc7768433890406cdf21cc2224f8816c4f11bbeca70e9c94a5dfbe9d`

---

## Raw Telemetry Content

# round5.4-counters-v1 — Witness counters & guard adoption (response to the ARGON Round-5.3 In-Band Verification Receipt)

Provenance: witness emission, Task 46, boundary trace `1a1613c6ec71bced`, 2026-10-22 (UTC).
Parents: `round5.2-counters-v1.md` (`def5d3b1…` — bytes operator-side, see §6); ARGON Round-5.3 In-Band Verification Receipt (verbatim pin: `write-ups/paper-2-round5.3-argon-receipt-v1.md`).
Method — mirror discipline: ARGON executed the Round-5.2 gate code in his sandbox before ruling; this document executes the Round-5.3 guard code witness-side BEFORE adoption. Every execution below is scripted (`scripts/r5-4-*`, `scripts/r2-47-*`) and reproducible.

## §0 Standing registrations

- BOOTSTRAP GREEN, executed before any response work: fetch `e2e4372..d3e38f7` — origin/main == `d3e38f7` == the Task-45 catch-up head → **TASK-45 EMISSION ROUND-TRIP CLOSED** (6917255 + d3e38f7 both origin-side; fast-forward, zero divergence). sessions 19/19; MEDA 29/29; CDP 47/47. Tag `witness-anchor-2026-10-20` GOOD ("Good signature … 4ndr0666"); keyring loss **5th occurrence** (fresh `~/.gnupg`), recovered in-boundary from `scripts/operator-profile-key.gpg`. Custody **6/6 byte-match** (PDF `2f9d204e` / counters `b59a8431` / metadata `0ef99398` / tar `6a950693` / changes `9ae8cfb5` / lineage `119044ba`).
- **F-002 #34 registered** (17th consecutive CRITICAL ERROR header by unbroken arithmetic from the substrate-verified #31 at Task 45 plus the two intervening registered boundaries — those two registrations sit in the summarized boundary responses and are not re-verifiable from this context; noted fail-visible; trace `1a1613c6ec71bced`). START-typed delimiter 7th consecutive (alias lean unchanged; §3 ruling still requested).
- Receipt dependency pre-verified: commit `a207175` present in GWM and `git merge-base --is-ancestor a207175 origin/main` = TRUE (the R2-37 gate shape, executed live) — the L0 recomputation source is anchored before any guard runs.

## §1 Receipt verification

| Claim in the Round-5.3 receipt | Witness check | Result |
|---|---|---|
| counters SHA-256 `def5d3b1…` == computed | Bytes absent from the witness VM (in-band-only delivery; emitting context exhausted) — recompute impossible this side; ARGON's sandbox computation stands as the verification leg; save-side bytes held by operator | ACCEPTED-ON-TESTIMONY; recompute pending §6 re-supply |
| sidecar `b0bd553f…` over 90 B | 90 == 64 (hex) + 2 (sep) + 23 (`round5.2-counters-v1.md`) + 1 (LF) — exact `sha256sum` line format | CONSISTENT |
| R2-44 bytes-first rule (24,435 B / 24,070 chars) | 365 multi-byte chars, plausible for the document's math glyphs; byte-exact check rides the §6 re-supply | CONSISTENT (pending) |
| empty-stream sentinel `e3b0c442…` (R2-49) | `sha256(b"")` recomputed | MATCH (T4) |
| all four §2 defect claims | executed witness-side | CONFIRMED (§2) |

## §2 Guard validation by execution (before adoption)

Tooling at probe: `pdftotext`, `pdfinfo`, `qpdf`, `pypdf` all present.

### T1–T4 — ARGON's four defect claims: all reproduced
- **T1 (R2-48.1)**: POSIX pipe-subshell variable loss — `fails=1` set inside `| while` never reaches the parent; `[ "$fails" -eq 0 ]` prints `L0 OK` on total failure. CONFIRMED (bash and /bin/sh).
- **T2 (R2-48.2)**: awk `exit 1` jumps to `END` — original GATE-C prints `L5 FAIL non-monotonic at 4` AND `L5 OK 3/3 strictly monotonic` in one run (status 1; output-level false pass). CONFIRMED.
- **T3**: ARGON's bad-flag fix (`{bad=1; …; exit 1}` + `END{if(bad) exit 1; …}`) — FAIL printed, no OK, status 1. VALIDATED.
- **T4 (R2-49)**: `false | sha256sum` records `e3b0c442…` with pipeline status 0 — the silent empty-stream anchor. CONFIRMED; sentinel matches ARGON's byte-for-byte.

### T5 — ARGON's own R2-43/L0 fix, executed verbatim on the production data set: NEW WITNESS CATCH (→ R2-51)
ARGON's fixed pipeline (brace group + n-counter; backslash relay artifacts normalized) run in CDP against `PIN-CHAIN-RECOMPUTATION.md` + `GWM@a207175`. Observed:
1. **Field misparse**: `read -r old new dg` splits on whitespace, but every L0 evidence filename contains spaces — row 1 parses as `old=[evidence/005]`, `new=[-]`, `dg=[Z.ai - Advanced … 835bb368…]`.
2. **stdin consumption**: `sha256sum "$new"` with `$new="-"` makes sha256sum read STDIN — it consumed the remaining 7 pipeline rows; the loop ran exactly ONE phantom row.
3. **Gate outcome**: `L0 FAIL [evidence/005] [-]`, `n=1≠8` → exit 1. The fix PRESERVES fail-closed orientation (no false PASS — the Round-5.2 defect class stays closed) but false-FAILs byte-invariant production data: unusable as delivered.
Verdict: **R2-48 ACCEPT-WITH-REFINEMENT** — brace-group / n-counter / terminal-exit structure correct and adopted; field parsing replaced by the canonical forms in T6.

### T6 — canonical L0 gate (R2-51 fix): **8/8 OK on real data**
Python gate (`scripts/r5-4-l0-gate.py`): full-path regex parse (whitespace-proof), rc-checked `git show a207175:<old>` via GWM (a failed stream is never hashed — the R2-49 class closed at the source), hashlib compare old-bytes == worktree-new == table digest, empty-stream sentinel excluded, row-count assert == 8. Result: **L0 OK 8/8** — evidence byte-invariance across renames recomputed fresh at this boundary (F003-capture-001..006, F003-api-probe, E1-composer; heads `835bb368…`, `749103d5…`, `a81e1b2a…`, `46570911…`, `b667c36e…`, `cfa83a9e…`, `630d1eb0…`, `a65e47f7…`).

### T7 — canonical R2-49 anchor gate: **PASS on all three live repos**
`scripts/r5-4-tar-digest-gate.py` — per repo: rc-checked git, `HEAD == origin/main` asserted (force-push/staleness hole closed), tar digest computed IN-PROCESS via hashlib over `git archive --format=tar origin/main` (portable — no `set -o pipefail`, which dash lacks), empty-stream sentinel asserted absent:
- `GWM-HEAD d3e38f709876f449683de9907da05a5df4b9c5ed` — `GWM-TAR-DIGEST 6bd7258787…` (11,284,480 B)
- `CDP-HEAD e2f3d8658ac0a637bb952ee93567020f0551b98b` — `CDP-TAR-DIGEST 4109426bc7…` (5,150,720 B)
- `MEDA-HEAD ec40e2fb917e908d3fecff78fc51beefa26155d0` — `MEDA-TAR-DIGEST a526238e73…` (4,372,480 B)
Note: CDP HEAD (`e2f3d865…`) ≠ the printed Table-5 anchor (`a44018d2…`) — CDP advanced since the print; anchors are build-time-recomputed values recorded by the v1.6 emitter (R2-49 fold-in), never static prose (the R2-46 `47/47→48/48` class).

### T8 — GATE-D pair-walk prototype, first real execution: **FAIL CLOSED with 8 unresolved pairs** (→ R2-52)
`scripts/r5-4-gate-d-walk.py` over GWM `sessions/`: **42 unique (path, blob-oid) pairs across 24 commits**. Classification: 19 preserved; 1 translated; 14 authorized-retired (historical MANIFEST states passing the append-only subset check); **8 UNRESOLVED → exit 1**. The Round-5.2 filename-set GATE-D would have classified ALL of these `preserved`. Characterization:

| # | Pair | Proposed adjudication class |
|---|---|---|
| 1–2 | `2026-10-05_session-001_bootstrap.md` oids `0a5b5b4b…`, `b328fa81…` (commits 78b1508 Initial, b326294 v1.3) | pre-pin-chain in-place rewrites (2026-10-06-era header format, superseded twice before the current capture) |
| 3 | `2026-10-05_sessions-001_bootstrap.md` oid `e69de29…` (empty blob) | scaffolding typo path (empty file) |
| 4 | `2026-10-09_session-003_agent.md.~1~` oid `a2365fbf…` | editor backup artifact once committed |
| 5 | `2026-10-10_session-004_chat.md` oid `fe13d58b…` | superseded capture — in-place content change at a fixed path: the exact R2-50 hypothetical, materialized |
| 6–7 | MANIFEST states at eebb805 (6 lines), 8b6efc5 (10 lines) | pre-WO-B-rename manifest states — refinement: a historical manifest is authorized iff every line's digest is (a) in HEAD's manifest OR (b) a pin-chain-recorded pre-rename digest; literal line-subset is too strict across the rename event |
| 8 | `YYYY-MM-DD_sessiosn-NNN.md` oid `e69de29…` | scaffolding typo path (empty template) |

Disposition: GATE-D stays fail-closed on GWM until the operator adjudicates the allowlist with reasons (per the Round-5.2 GATE-D spec — the gate working as designed). Adjudication touches NO pin or manifest byte; it authorizes historical states the current chain already supersedes. Symmetry note: `e69de29…` is the SHA-1 empty sentinel — git's own `e3b0c442…` twin.

### T9 — R2-47 mechanism, three legs: CONFIRMED
Crafted A4 probe (`scripts/r2-47-preclip-demo.py`; MediaBox 595.28×841.89):
- **[1] pre-clip**: words `abovepage` (y=900) and `beyondright` (x=700) ABSENT from `pdftotext -bbox-layout` output — poppler drops out-of-MediaBox glyphs before the coordinate check runs. The R2-39 page-13 blind class, reproduced.
- **[2] parity leg**: pypdf raw extract sees all five words — the "unclipped stream vs clipped stream" comparison is executable exactly as the receipt specifies.
- **[3] textblock leg**: `bottommargin` (in-MediaBox, `yMax=814.37`) — page-edge bounds PASS (814.37 ≤ 841.89), textblock bounds FAIL (814.37 > 804). The page-13 class reproduced exactly.
Refinements folded into GATE-A: (i) thresholds are **top-left-origin** coordinates (poppler's bbox frame) — the gate documents its coordinate frame; (ii) the MediaBox-rewrite parity leg operates on a **TEMP COPY** (never in place) and rewrites **CropBox as well as MediaBox** (poppler clips to CropBox when present); (iii) the parity comparison asserts a per-page **multiset** of normalized word strings + counts, not sequence equality (ordering can drift across extractor configurations without any clipping implication); (iv) the 540/804 constants are v1.4-calibrated — v1.6 re-derives them from the template's text-block geometry and prints the derivation in the build log (no silent constant drift).

### T10 — GATE-C on real L5 data: **6/6 strictly monotonic**
Capture heights (pdfinfo, pts): 422.68 → 871.39 → 1057.10 → 1570.18 → 1939.51 → 2474.62 (F003-capture-001..006) through ARGON's fixed awk: `L5 OK 6/6 strictly monotonic`, status 0. `n==6` matches the real capture count.

## §3 New registry entries

| ID | Surface | Finding | Verdict / fold-in |
|---|---|---|---|
| **R2-51** | D | The Round-5.3 L0 shell fix false-FAILs production data: whitespace-bearing filenames misparse in `read -r old new dg`; `sha256sum "$new"` with `$new="-"` consumes pipeline stdin (T5). Fail-closed orientation preserved; usability broken. | CLOSED — canonical Python L0 gate adopted (T6, 8/8). Shell fallback permitted only with digest-first TAB-separated emission + parent-level `\|\| exit 1` status propagation + documented no-tabs/no-newlines precondition. |
| **R2-52** | D | GATE-D first real execution: 8 unresolved (path, blob) pairs in GWM sessions/ history (T8) — in-place rewrites, scaffolding, one tooling artifact, pre-rename manifest states. | OPEN-PENDING-ADJUDICATION — operator adjudicates the allowlist with reasons; GATE-D then runs clean at the v1.6 build. No pin/manifest byte changes. |

## §4 Registry state & concurrence

R2-36..R2-46: ACCEPTED per the Round-5.3 §1 rulings — no reopens, no rebuttals. R2-47..R2-50: ACCEPTED-WITH-REFINEMENT (§2). **Zero standing rebuttals remain on any surface** — the witness CONCURS with the receipt's §4: the Round-5.2 findings ledger is APPROVED FOR v1.6 BUILD EXECUTION, with the guards folded in as refined in this document.

## §5 Hide-analysis — accepted, with two witness notes

The receipt's §3 residual-defect table (Surfaces A–E) is accepted as the canonical hide-analysis for v1.6 Limitations, verbatim in structure: residual class → exposing evidence → why this loop structurally cannot produce it. Two witness notes, log-don't-rewrite:
1. **Surface A** (split-view) has a cheap partial mitigator the paper can NAME without overclaiming: the operator-side execution of THE CALL's fail-closed chain (base-assert → head-assert → manifest check) IS a live out-of-band probe from outside the air-gapped container, performed by the one party with network reach. It does not satisfy the independent-verifier requirement (n=1 custody stands); it narrows the equivocation window from "always" to "between pushes".
2. **Surfaces C and E** residuals are already pre-bounded by the paper's claim scoping (C-1 and Row 9 bound claims to post-commit byte invariance; the activational-tier claims are instrumented-benchmark-shaped, not field-program-shaped). The v1.6 Limitations text should cross-reference those two registers rather than restate them.

## §6 Gate to v1.6 execution — one input re-asked (§3: re-ask, never assume)

APPROVED FOR BUILD EXECUTION is adopted. The witness will execute the v1.6 build (source tree v1.5-repro + R2-16..R2-52 folded per the Round-5.2 §4/§5 spec + §2 of this document), run GATE-A..GATE-D at build, and emit the build receipt in-band for final post-build verification.

**BLOCKING INPUT (custody gap, registered fail-visible)**: `round5.2-counters-v1.md` exists witness-side only as digest `def5d3b1…` — the bytes were delivered in-band and the emitting context is exhausted; per §3 they are NEVER reconstructed. Re-supply path (either closes it): (a) operator pastes the file back in-band (24,435 B; save-side `sha256sum` must print `def5d3b1…`); (b) operator commits the save-side copy into his next substrate snapshot. One act closes BOTH the build-spec input AND the substrate custody pin.

Non-blocking parallel pendings: PROD_PATH pin (one `pwd` line; artifact-index slot reserved, Task 45); §8 envelope ruling; R2-52 adjudication (can ride to build time).

## §7 Artifact custody

This document: `download/paper-2-round5.4-counters/round5.4-counters-v1.md` == `write-ups/paper-2-round5.4-counters-v1.md` (byte-identical dual channel). ARGON Round-5.3 receipt: `write-ups/paper-2-round5.3-argon-receipt-v1.md` (verbatim pin + provenance header). Validation scripts: `scripts/r5-4-guard-validation.sh`, `r5-4-argon-l0-verbatim.sh`, `r5-4-l0-gate.py`, `r5-4-tar-digest-gate.py`, `r5-4-gate-d-walk.py`, `r2-47-preclip-demo.py`. Digests in the Task-46 emission table (in-band).

