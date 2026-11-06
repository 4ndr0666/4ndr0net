# Telemetry Source: scripts/task83_deposit_verify.sh
- **Source Identifier**: `scripts/task83_deposit_verify.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `62569c180387f67ad97998aecb83fc5a047fede1573496db17d515f30eadd981`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
# ============================================================================
# scripts/task83_deposit_verify.sh — GO-FIX deposit-package v2 verifier
# (repo-rode, fail-closed, read-only)
#
# Task 83 (2026-11-01, trace 1a19470a33de4459). Born with the GO-FIX deposit
# home entry references/arxiv-deposit/paper-2-arxiv-deposit-v2.tar.gz — the
# fix-before-submit re-cut ordered by the operator's GO (the Task-82
# recommendation elected): tex-v3 + bib-v3 (the Task-82 verdict-ledger
# confirmed patch set, cut by scripts/task83_cut_v3.py; the ARGON \nocite{ * }
# patch rejected as a no-op), recompiled tectonic 0.15.0 exit 0 -> 35 pages
# (page count UNCHANGED from v2 — the metadata lock's "…35 pages." comments
# field STANDS), packaged deterministically by scripts/task83_cut_package.sh
# (sorted members, fixed mtime, owner 0:0, gzip -n — bit-reproducible by
# construction, an improvement over the v1 cut, registered in the build
# ledger). This verifier re-proves, from the repository alone (GUP-class),
# at every future bootstrap:
#
#   [E0] the v2 deposit-home copy exists, is size-exact (47,084 B) and
#        hashes the witness-recorded pin of record bacc1f18… (double-bound:
#        the pin table below AND the canonical sidecar line)
#   [E1] the package shape is source-only: exactly two members, no
#        directories, no extraneous entries
#   [E2] the inner .tex == the repo-held tex-v3 of record (pin a975d7d1…,
#        write-ups/paper-2-v1.7-draft3-1-latex-v3.tex — live-rehashed)
#   [E3] the inner .bib == the repo-held bib-v3 of record (pin 8b5bc0fc…,
#        write-ups/paper-2-v1.7-draft3-1-bib-v3.bib — live-rehashed)
#   [E4] the sidecar is the canonical sha256sum line over the tarball's
#        true pin (77c method: reconstruct, compare)
#   [E5] the §1.6 inbox-registration name matches the deposit-home filename
#        (the INDEX row and the repo file name the same artifact)
#   [E6] the v1 anchor still holds: the Task-81 verifier re-runs GREEN over
#        the v1 package + v2 sources of record (backward compatibility —
#        both deposit versions keep substrate custody)
#
# Documented state (not re-derived here; measured at the Task-83 build and
# pinned in the build ledger): v3 clean-build page count = 35; v3 render
# sha256 a39931dd…; arXiv form comments field stays LOCKED at "…35 pages.".
#
# Usage: bash scripts/task83_deposit_verify.sh   (from the repo root)
# Exit 0 = all GREEN. Any failure = fail-closed halt with a named gate.
# ============================================================================
set -euo pipefail

REPO="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
fail() { echo "[DEPOSIT-V2 VERIFY FAIL-CLOSED: $*]" >&2; exit 1; }

# --- pin table (witness-recorded digests of record) --------------------------
PIN_TGZ="bacc1f1833e7d0bb29db0efdc73c3d4d858987ec43e4c9ce233f85dc26af5d80"
PIN_TGZ_SIZE="47084"
PIN_TEXV3="a975d7d199d0aea878543945299618089288e2d24ba0b2daa6cf794e878847e5"
PIN_BIBV3="8b5bc0fca290d22fa9249111cc92b896dc3f2c2b17e7f461215ec5ceff20e0a2"
TGZ_NAME="paper-2-arxiv-deposit-v2.tar.gz"
TEX_NAME="paper-2-v1.7-draft3-1-latex-v3.tex"
BIB_NAME="paper-2-v1.7-draft3-1-bib-v3.bib"

TGZ="$REPO/references/arxiv-deposit/$TGZ_NAME"
SIDECAR="$TGZ.sha256"

# --- [E0] deposit-home copy: existence, size, pin -----------------------------
[ -f "$TGZ" ] || fail "[E0] deposit-home copy missing: references/arxiv-deposit/$TGZ_NAME"
SZ="$(stat -c '%s' "$TGZ")"
[ "$SZ" = "$PIN_TGZ_SIZE" ] || fail "[E0] size drift: $SZ != $PIN_TGZ_SIZE"
H0="$(sha256sum "$TGZ" | sed 's/ .*//')"
[ "$H0" = "$PIN_TGZ" ] || fail "[E0] digest drift: $H0 != $PIN_TGZ"
echo "[E0] deposit-home v2 copy GREEN — $PIN_TGZ ($PIN_TGZ_SIZE B)"

# --- [E1] package shape: exactly the two source members -----------------------
TMP="$(mktemp -d "${TMPDIR:-/tmp}/t83-verify.XXXXXX")"; trap 'rm -rf "$TMP"' EXIT
tar -xzf "$TGZ" -C "$TMP" || fail "[E1] tar extraction failed"
MEMBERS="$(tar -tzf "$TGZ")"
[ "$(printf '%s\n' "$MEMBERS" | grep -c .)" -eq 2 ] || fail "[E1] member count != 2"
printf '%s\n' "$MEMBERS" | grep -qx "$TEX_NAME" || fail "[E1] missing member $TEX_NAME"
printf '%s\n' "$MEMBERS" | grep -qx "$BIB_NAME" || fail "[E1] missing member $BIB_NAME"
[ ! -d "$TMP/$TEX_NAME" ] && [ ! -d "$TMP/$BIB_NAME" ] || fail "[E1] member is a directory"
echo "[E1] package shape GREEN — source-only, exactly 2 members, no directories"

# --- [E2]/[E3] inner bytes == the repo-held v3 sources of record ---------------
WT_TEX="$REPO/write-ups/$TEX_NAME"; WT_BIB="$REPO/write-ups/$BIB_NAME"
[ -f "$WT_TEX" ] || fail "[E2] repo tex-v3 missing: write-ups/$TEX_NAME"
[ -f "$WT_BIB" ] || fail "[E3] repo bib-v3 missing: write-ups/$BIB_NAME"
H1="$(sha256sum "$TMP/$TEX_NAME" | sed 's/ .*//')"
W1="$(sha256sum "$WT_TEX" | sed 's/ .*//')"
[ "$H1" = "$PIN_TEXV3" ] || fail "[E2] inner tex digest $H1 != pin $PIN_TEXV3"
[ "$W1" = "$PIN_TEXV3" ] || fail "[E2] repo tex-v3 drifted ($W1 != $PIN_TEXV3) — v3 liveness broken"
echo "[E2] inner tex GREEN — == pin a975d7d1… == repo tex-v3 of record"
H2="$(sha256sum "$TMP/$BIB_NAME" | sed 's/ .*//')"
W2="$(sha256sum "$WT_BIB" | sed 's/ .*//')"
[ "$H2" = "$PIN_BIBV3" ] || fail "[E3] inner bib digest $H2 != pin $PIN_BIBV3"
[ "$W2" = "$PIN_BIBV3" ] || fail "[E3] repo bib-v3 drifted ($W2 != $PIN_BIBV3) — v3 liveness broken"
echo "[E3] inner bib GREEN — == pin 8b5bc0fc… == repo bib-v3 of record"

# --- [E4] sidecar canonical-line consistency (77c method) ----------------------
[ -f "$SIDECAR" ] || fail "[E4] sidecar missing: references/arxiv-deposit/$TGZ_NAME.sha256"
EXPECT_LINE="$PIN_TGZ  $TGZ_NAME"
GOT_LINE="$(cat "$SIDECAR")"
[ "$GOT_LINE" = "$EXPECT_LINE" ] || fail "[E4] sidecar is not the canonical sha256sum line (got: $GOT_LINE)"
SIDE_SHA="$(sha256sum "$SIDECAR" | sed 's/ .*//')"
echo "[E4] sidecar GREEN — canonical line reconstructed; sidecar pin $SIDE_SHA"

# --- [E5] INDEX §1.6 registration names the same artifact ----------------------
[ -f "$REPO/INDEX.md" ] || fail "[E5] INDEX.md missing at repo root"
grep -q "^├── $TGZ_NAME$" "$REPO/INDEX.md" || fail "[E5] INDEX.md does not register $TGZ_NAME (§1.6 row expected)"
echo "[E5] INDEX registration GREEN — §1.6 names the deposit-home v2 artifact"

# --- [E6] the v1 anchor still holds (Task-81 verifier re-run) ------------------
bash "$REPO/scripts/task81_deposit_verify.sh" \
  || fail "[E6] the v1 deposit anchor broke — task81_deposit_verify.sh RED"
echo "[E6] v1 anchor GREEN — the Task-81 verifier passes unmodified beside v2"

echo "DEPOSIT-V2 VERIFY: GREEN — [E0]-[E6] all passed (Task-83 verifier, repo-rode)"

```
