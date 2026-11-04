# Telemetry Source: scripts/task79_relay_verify.sh
- **Source Identifier**: `scripts/task79_relay_verify.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `770a2825a024f0681cc5b8a73a437e99554d66a6fdc9d35092db57cc5e7fd72e`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
#
# task79_relay_verify.sh — witness-side verification of the R2 stage-2
# channel-(a) relay (Task 79, trace 1a18fc5c14a61761).
#
# WHAT IT VERIFIES — the operator-direct relay commit 435d598 depositing the
#   GUP-critical 8 under references/white-paper-relay/ (copies from
#   $GWM-INBOX per the operator's commit message; INDEX.md §2 pins of record,
#   77c supersession). Run from the repo root after the bootstrap pull.
# GATES
#   [R0] commit shape — single-commit advance off the Task-78 applied head
#        aaac871; exactly 8 files, all under references/white-paper-relay/;
#        no deletions; clean worktree (witness bytes == HEAD bytes).
#   [R1] pin equality — 8/8 relay digests == INDEX.md §2 pins of record
#        (parsed live from §2) AND == the 77c supersession pin map below
#        (double bind: drift in either embed site = RED).
#   [R2] sidecar internal consistency — each .sha256 reconstructs as the
#        canonical sha256sum line over its .md's true pin (the 77c
#        adjudication method, now standing evidence).
#   [R3] stats cross-check — tarball size + diff shortstat vs the operator
#        paste-back (739,787 B; 8 files changed, 957 insertions).
# SAFETY — fail-closed: any RED names its gate and exits 1. Full GREEN exits 0.
#   Read-only: verifies bytes, touches nothing.
#
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

BASE="aaac871b59c65fb2abbd0e347dd261eb0aaf24d4"   # Task-78 applied head (true full sha;
                                                   # the operator's paste-back line dropped
                                                   # "26" — 38-hex slip, closed by the push
                                                   # receipt short sha + 435d598^ + history)
RELAY="435d598"                                   # operator relay commit

# 77c supersession pin map (== INDEX.md §2 pins of record; mirrors the
# generator's INTAKE_FILES and the consolidate script's PINNED table).
FILES=(
  "paper-2-v1.6.1-source.tar.gz"
  "paper-2-v1.6-to-v1.6.1.changes"
  "refs-2.bib"
  "round5.2-counters-v1.md"
  "round5.2-counters-v1.md.sha256"
  "round5.4-counters-v1.md"
  "round5.4-counters-v1.md.sha256"
  "paper-2-arxiv-metadata.md"
)
PIN=(
  "a764eb1fafd4df3c5436bae58ecc178aa3a98bb2164f95b50f181415f6c6bfa0"
  "037dbdd997cc8c36d5749ade5333e93cd9252ac5acf64e7aebc63c1765148123"
  "798d1dd499244b283c921222f27199c186645dc1ce6ecae469985aa655b7b101"
  "def5d3b1a77a700a5a7cc496d04d5e062188be59e75f207aad5803b82ca5a7ad"
  "17b7d13b317ab3d5dd188be8d480451baa36510083e44e5f05b2b5a855992e46"
  "8c3f0497fc7768433890406cdf21cc2224f8816c4f11bbeca70e9c94a5dfbe9d"
  "94999ef7d8357cf7631038d9f8dd4f49313954f0b3c02bdb075976c394bdf264"
  "0ef99398ea3df5dc659532f523ee9548f36ceb5ede50b739e600b47d74add8ed"
)

fail=0
red() { printf 'RED: %s\n' "$*"; fail=1; }
ok()  { printf '    %s\n' "$*"; }

echo "[R0] commit shape (base ${BASE:0:7} -> relay)"
RELAY_FULL="$(git rev-parse "$RELAY")"
PARENT="$(git rev-parse "$RELAY^")"
COUNT="$(git rev-list --count "${BASE}..${RELAY}")"
NFILES="$(git diff --name-only "$BASE" "$RELAY" | wc -l | tr -d ' ')"
SHORTSTAT="$(git diff --shortstat "$BASE" "$RELAY")"
OUTSIDE="$(git diff --name-only "$BASE" "$RELAY" | grep -v '^references/white-paper-relay/' || true)"
[ "$PARENT" = "$BASE" ]                  || red "relay parent is $PARENT, expected $BASE"
[ "$COUNT" -eq 1 ]                       || red "advance is $COUNT commits, expected 1 (single-commit relay)"
[ "$NFILES" -eq 8 ]                      || red "$NFILES files changed, expected 8"
[ -z "$OUTSIDE" ]                        || red "collateral path(s) outside references/white-paper-relay/: $OUTSIDE"
printf '%s' "$SHORTSTAT" | grep -q "deletion" && red "unexpected deletions in $SHORTSTAT"
[ -z "$(git status --porcelain -- references/white-paper-relay/)" ] \
  || red "relay path not clean vs HEAD — the eight hashed files would not be HEAD bytes"
ok "relay=$RELAY_FULL parent=${PARENT:0:7} — single-commit advance, 8 files confined"
ok "$SHORTSTAT — no deletions; worktree clean"

echo "[R1] pin equality vs INDEX.md §2 (8/8 required)"
SECTION="$(sed -n '/^## §2 /,/^## §3 /p' INDEX.md)"
pin_of() {  # live-parse the §2 pin for a filename (token-boundary match)
  printf '%s\n' "$SECTION" \
    | grep -E "(^|[^A-Za-z0-9._-])${1}([^A-Za-z0-9._-]|$)" \
    | grep -oE "[0-9a-f]{64}" | head -1
}
i=0
for f in "${FILES[@]}"; do
  want="${PIN[$i]}"
  got="$(sha256sum "references/white-paper-relay/$f" | cut -d' ' -f1)"
  idx="$(pin_of "$f")"
  if [ "$got" = "$want" ] && [ "$idx" = "$want" ]; then
    ok "$f  ${got:0:12}…  relay == INDEX §2 == 77c map"
  else
    red "$f: relay=${got:0:12}… index=${idx:0:12}… map=${want:0:12}…"
  fi
  i=$((i + 1))
done

echo "[R2] sidecar internal consistency (canonical-line reconstruction, 77c method)"
for n in 5.2 5.4; do
  md="references/white-paper-relay/round${n}-counters-v1.md"
  sc="references/white-paper-relay/round${n}-counters-v1.md.sha256"
  true_pin="$(sha256sum "$md" | cut -d' ' -f1)"
  sc_hash="$(sha256sum "$sc" | cut -d' ' -f1)"
  sc_bytes="$(cat "$sc")"
  canon_nl="$(printf '%s  round%s-counters-v1.md\n' "$true_pin" "$n" | sha256sum | cut -d' ' -f1)"
  canon_bare="$(printf '%s  round%s-counters-v1.md' "$true_pin" "$n" | sha256sum | cut -d' ' -f1)"
  printf '%s' "$sc_bytes" | grep -q "$true_pin" \
    || red "round${n} sidecar does not carry its .md's true pin"
  { [ "$sc_hash" = "$canon_nl" ] || [ "$sc_hash" = "$canon_bare" ]; } \
    || red "round${n} sidecar != canonical-line reconstruction (${sc_hash:0:12}…)"
  ok "round${n}: sidecar == canonical sha256sum line over ${true_pin:0:12}… (self ${sc_hash:0:12}…)"
done

echo "[R3] stats cross-check vs operator paste-back"
SIZE="$(stat -c%s references/white-paper-relay/paper-2-v1.6.1-source.tar.gz)"
[ "$SIZE" = "739787" ] || red "tarball size $SIZE B != 739,787 B (77c [X0] stat)"
printf '%s' "$SHORTSTAT" | grep -q "8 files changed" \
  || red "shortstat mismatch vs paste: $SHORTSTAT"
printf '%s' "$SHORTSTAT" | grep -q "957 insertions" \
  || red "insertions mismatch vs paste: $SHORTSTAT"
ok "tarball 739,787 B; $SHORTSTAT (operator paste: 8 files, 957 insertions)"

if [ "$fail" -eq 0 ]; then
  echo "RELAY VERIFY: GREEN — [R0]-[R3] all GREEN; 8/8 relay bytes == pins of record."
  exit 0
else
  echo "RELAY VERIFY: RED — see the gates above; fail-closed, nothing was modified."
  exit 1
fi

```
