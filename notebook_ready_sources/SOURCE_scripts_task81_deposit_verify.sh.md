# Telemetry Source: scripts/task81_deposit_verify.sh
- **Source Identifier**: `scripts/task81_deposit_verify.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `730ce87c76cdb24fe18b2d412e288e665f968af7b9c33ac8bf57203830ff69cd`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
# ============================================================================
# scripts/task81_deposit_verify.sh — Phase-5 deposit-package verifier
# (repo-rode, fail-closed, read-only)
#
# Task 81 (2026-10-31, trace 1a1905cebcf39595). Born with the deposit home
# references/arxiv-deposit/: the exact bytes of the arXiv submission package
# paper-2-arxiv-deposit-v1.tar.gz (the Task-73 Phase-4 build emission,
# boundary-delivered by the operator at Task 81 and witness-verified
# three-way: upload delivery == Task-73 staged emission == Task-73
# SHA256SUMS pin). This verifier re-proves, from the repository alone
# (GUP-class), at every future bootstrap:
#
#   [D0] the deposit-home copy exists, is size-exact (46,466 B) and hashes
#        the witness-recorded pin of record c4148807… (double-bound: the
#        hardcoded pin table below AND the canonical sidecar line)
#   [D1] the package shape is source-only: exactly two members, no
#        directories, no extraneous entries
#   [D2] the inner .tex == the repo-held tex-v2 of record (pin 687c19d6…,
#        write-ups/paper-2-v1.7-draft3-1-latex-v2.tex — live-rehashed)
#   [D3] the inner .bib == the repo-held bib-v2 of record (pin 18d1e05f…,
#        write-ups/paper-2-v1.7-draft3-1-bib-v2.bib — live-rehashed)
#   [D4] the sidecar is the canonical sha256sum line over the tarball's
#        true pin (77c method: reconstruct, compare)
#   [D5] the §1.6 inbox-registration name matches the deposit-home filename
#        (the INDEX row and the repo file name the same artifact)
#
# Usage: bash scripts/task81_deposit_verify.sh   (from the repo root)
# Exit 0 = all GREEN. Any failure = fail-closed halt with a named gate.
# ============================================================================
set -euo pipefail

REPO="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
fail() { echo "[DEPOSIT-VERIFY FAIL-CLOSED: $*]" >&2; exit 1; }

# --- pin table (witness-recorded digests of record) --------------------------
PIN_TGZ="c4148807834e1826e0ab9d2e5575ff01cb36f82befeaa0c7acb843556275b30c"
PIN_TGZ_SIZE="46466"
PIN_TEXV2="687c19d65c9cf091cfd9cdd83bdf04f1c359382a602340b38a41a1751bf41694"
PIN_BIBV2="18d1e05fbdc7258df181aaf98d894534f308b94c7f8ff4c8931a66a410c5599e"
TGZ_NAME="paper-2-arxiv-deposit-v1.tar.gz"
TEX_NAME="paper-2-v1.7-draft3-1-latex-v2.tex"
BIB_NAME="paper-2-v1.7-draft3-1-bib-v2.bib"

TGZ="$REPO/references/arxiv-deposit/$TGZ_NAME"
SIDECAR="$TGZ.sha256"

# --- [D0] deposit-home copy: existence, size, pin -----------------------------
[ -f "$TGZ" ] || fail "[D0] deposit-home copy missing: references/arxiv-deposit/$TGZ_NAME"
SZ="$(stat -c '%s' "$TGZ")"
[ "$SZ" = "$PIN_TGZ_SIZE" ] || fail "[D0] size drift: $SZ != $PIN_TGZ_SIZE"
H0="$(sha256sum "$TGZ" | sed 's/ .*//')"
[ "$H0" = "$PIN_TGZ" ] || fail "[D0] digest drift: $H0 != $PIN_TGZ"
echo "[D0] deposit-home copy GREEN — $PIN_TGZ ($PIN_TGZ_SIZE B)"

# --- [D1] package shape: exactly the two source members -----------------------
TMP="$(mktemp -d "${TMPDIR:-/tmp}/t81-verify.XXXXXX")"; trap 'rm -rf "$TMP"' EXIT
tar -xzf "$TGZ" -C "$TMP" || fail "[D1] tar extraction failed"
MEMBERS="$(tar -tzf "$TGZ")"
[ "$(printf '%s\n' "$MEMBERS" | grep -c .)" -eq 2 ] || fail "[D1] member count != 2"
printf '%s\n' "$MEMBERS" | grep -qx "$TEX_NAME" || fail "[D1] missing member $TEX_NAME"
printf '%s\n' "$MEMBERS" | grep -qx "$BIB_NAME" || fail "[D1] missing member $BIB_NAME"
[ ! -d "$TMP/$TEX_NAME" ] && [ ! -d "$TMP/$BIB_NAME" ] || fail "[D1] member is a directory"
echo "[D1] package shape GREEN — source-only, exactly 2 members, no directories"

# --- [D2]/[D3] inner bytes == the repo-held v2 sources of record ---------------
WT_TEX="$REPO/write-ups/$TEX_NAME"; WT_BIB="$REPO/write-ups/$BIB_NAME"
[ -f "$WT_TEX" ] || fail "[D2] repo tex-v2 missing: write-ups/$TEX_NAME"
[ -f "$WT_BIB" ] || fail "[D3] repo bib-v2 missing: write-ups/$BIB_NAME"
H1="$(sha256sum "$TMP/$TEX_NAME" | sed 's/ .*//')"
W1="$(sha256sum "$WT_TEX" | sed 's/ .*//')"
[ "$H1" = "$PIN_TEXV2" ] || fail "[D2] inner tex digest $H1 != pin $PIN_TEXV2"
[ "$W1" = "$PIN_TEXV2" ] || fail "[D2] repo tex-v2 drifted ($W1 != $PIN_TEXV2) — liveness trio broken"
echo "[D2] inner tex GREEN — == pin 687c19d6… == repo tex-v2 of record"
H2="$(sha256sum "$TMP/$BIB_NAME" | sed 's/ .*//')"
W2="$(sha256sum "$WT_BIB" | sed 's/ .*//')"
[ "$H2" = "$PIN_BIBV2" ] || fail "[D3] inner bib digest $H2 != pin $PIN_BIBV2"
[ "$W2" = "$PIN_BIBV2" ] || fail "[D3] repo bib-v2 drifted ($W2 != $PIN_BIBV2) — liveness trio broken"
echo "[D3] inner bib GREEN — == pin 18d1e05f… == repo bib-v2 of record"

# --- [D4] sidecar canonical-line consistency (77c method) ----------------------
[ -f "$SIDECAR" ] || fail "[D4] sidecar missing: references/arxiv-deposit/$TGZ_NAME.sha256"
EXPECT_LINE="$PIN_TGZ  $TGZ_NAME"
GOT_LINE="$(cat "$SIDECAR")"
[ "$GOT_LINE" = "$EXPECT_LINE" ] || fail "[D4] sidecar is not the canonical sha256sum line (got: $GOT_LINE)"
SIDE_SHA="$(sha256sum "$SIDECAR" | sed 's/ .*//')"
echo "[D4] sidecar GREEN — canonical line reconstructed; sidecar pin $SIDE_SHA"

# --- [D5] INDEX §1.6 registration names the same artifact ----------------------
[ -f "$REPO/INDEX.md" ] || fail "[D5] INDEX.md missing at repo root"
grep -q "^├── $TGZ_NAME$" "$REPO/INDEX.md" || fail "[D5] INDEX.md does not register $TGZ_NAME (§1.6 row expected)"
echo "[D5] INDEX registration GREEN — §1.6 names the deposit-home artifact"

echo "DEPOSIT VERIFY: GREEN — [D0]-[D5] all passed (Task-81 verifier, repo-rode)"

```
