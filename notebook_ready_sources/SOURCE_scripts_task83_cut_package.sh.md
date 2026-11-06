# Telemetry Source: scripts/task83_cut_package.sh
- **Source Identifier**: `scripts/task83_cut_package.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `f9deb616df4be0c091aa7c6977abec32d1ae834ceb0c9895a3bd000a160d8889`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
# ============================================================================
# scripts/task83_cut_package.sh — deterministic deposit-package v2 cutter
# (repo-rode, fail-closed, GUP-class)
#
# Task 83 (2026-11-01, trace 1a19470a33de4459). Cuts the GO-FIX deposit
# package paper-2-arxiv-deposit-v2.tar.gz from the v3 sources:
#   member 1: paper-2-v1.7-draft3-1-latex-v3.tex  (pin a975d7d1…)
#   member 2: paper-2-v1.7-draft3-1-bib-v3.bib    (pin 8b5bc0fc…)
#
# Determinism (improvement over the v1 cut, registered in the build ledger):
# sorted member order + fixed mtime + numeric owner 0:0 + gzip -n (no name,
# no timestamp) — the same v3 sources + this script = byte-identical wrapper
# on any machine. v1 (46,466 B, c4148807…) was not owner/mtime-normalized;
# v2 is bit-reproducible by construction.
#
# The wrapper lands at references/arxiv-deposit/paper-2-arxiv-deposit-v2.tar.gz
# + canonical sha256 sidecar (77c method). The v1 package is NOT touched —
# both deposit versions hold substrate custody side by side (v1 = the
# verified-bytes anchor of the Task-81 round; v2 = the GO-FIX submission
# candidate).
#
# Usage: bash scripts/task83_cut_package.sh   (from the repo root)
# ============================================================================
set -euo pipefail

REPO="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
fail() { echo "[CUT-PACKAGE FAIL-CLOSED: $*]" >&2; exit 1; }

PIN_TEXV3="a975d7d199d0aea878543945299618089288e2d24ba0b2daa6cf794e878847e5"
PIN_BIBV3="8b5bc0fca290d22fa9249111cc92b896dc3f2c2b17e7f461215ec5ceff20e0a2"
TEX_NAME="paper-2-v1.7-draft3-1-latex-v3.tex"
BIB_NAME="paper-2-v1.7-draft3-1-bib-v3.bib"
TGZ_NAME="paper-2-arxiv-deposit-v2.tar.gz"
FIXED_MTIME="2026-11-01 00:00:00 UTC"

TEX="$REPO/write-ups/$TEX_NAME"
BIB="$REPO/write-ups/$BIB_NAME"
OUT="$REPO/references/arxiv-deposit/$TGZ_NAME"
OUT_SIDECAR="$OUT.sha256"

[ -f "$TEX" ] || fail "tex-v3 missing: write-ups/$TEX_NAME"
[ -f "$BIB" ] || fail "bib-v3 missing: write-ups/$BIB_NAME"
[ "$(sha256sum "$TEX" | sed 's/ .*//')" = "$PIN_TEXV3" ] \
  || fail "tex-v3 pin drift (expected $PIN_TEXV3)"
[ "$(sha256sum "$BIB" | sed 's/ .*//')" = "$PIN_BIBV3" ] \
  || fail "bib-v3 pin drift (expected $PIN_BIBV3)"

TMP="$(mktemp -d "${TMPDIR:-/tmp}/t83-cut.XXXXXX")"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/stage"
cp "$TEX" "$BIB" "$TMP/stage/"

( cd "$TMP/stage" \
  && tar --sort=name --mtime="$FIXED_MTIME" --owner=0 --group=0 \
         --numeric-owner -cf - "$TEX_NAME" "$BIB_NAME" \
  | gzip -n -9 > "$TMP/$TGZ_NAME" ) \
  || fail "deterministic tar+gzip pipeline failed"

# --- shape gate: source-only, exactly 2 members -------------------------------
MEMBERS="$(tar -tzf "$TMP/$TGZ_NAME")"
[ "$(printf '%s\n' "$MEMBERS" | grep -c .)" -eq 2 ] || fail "member count != 2"
printf '%s\n' "$MEMBERS" | grep -qx "$TEX_NAME" || fail "missing member $TEX_NAME"
printf '%s\n' "$MEMBERS" | grep -qx "$BIB_NAME" || fail "missing member $BIB_NAME"

# --- determinism gate: a second cut must be byte-identical ---------------------
( cd "$TMP/stage" \
  && tar --sort=name --mtime="$FIXED_MTIME" --owner=0 --group=0 \
         --numeric-owner -cf - "$TEX_NAME" "$BIB_NAME" \
  | gzip -n -9 > "$TMP/second.tar.gz" )
cmp -s "$TMP/$TGZ_NAME" "$TMP/second.tar.gz" \
  || fail "determinism gate failed — two cuts differ"

mkdir -p "$REPO/references/arxiv-deposit"
cp "$TMP/$TGZ_NAME" "$OUT"
PIN_TGZ="$(sha256sum "$OUT" | sed 's/ .*//')"
printf '%s  %s\n' "$PIN_TGZ" "$TGZ_NAME" > "$OUT_SIDECAR"

echo "[cut-package] $TGZ_NAME"
echo "[cut-package] wrapper sha256: $PIN_TGZ ($(stat -c '%s' "$OUT") B)"
echo "[cut-package] sidecar: $OUT_SIDECAR"
echo "[cut-package] inner tex: $PIN_TEXV3"
echo "[cut-package] inner bib: $PIN_BIBV3"

```
