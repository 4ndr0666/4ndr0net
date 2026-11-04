# Telemetry Source: scripts/task77_consolidate_battery.sh
- **Source Identifier**: `scripts/task77_consolidate_battery.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `c408a7664d9cf1761250e84409526d6a3b7c00c413423cdd7dbf1e0f34817233`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
#
# task77_consolidate_battery.sh — pre-delivery battery for
# gwm-inbox-consolidate-v1.sh (Task 77). Tests every path reachable with
# witness-side mocks; the COPIED+PIN-VERIFIED (real-pin GREEN) path requires
# the operator-held certified bytes and exercises at the operator's run
# (paste-back receipt closes it) — registered as a scope note, not silent.
#
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
S="$REPO/scripts/gwm-inbox-consolidate-v1.sh"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT

pass=0; fail=0
ok()   { echo "PASS  $1"; pass=$((pass + 1)); }
bad()  { echo "FAIL  $1"; fail=$((fail + 1)); }
check() { # desc, expected-substring, logfile
  if grep -qF "$2" "$3"; then ok "$1"; else bad "$1 (expected substring not found: $2)"; fi
}

FILES=(paper-2-v1.6.1-source.tar.gz paper-2-v1.6-to-v1.6.1.changes refs-2.bib
       round5.2-counters-v1.md round5.2-counters-v1.md.sha256
       round5.4-counters-v1.md round5.4-counters-v1.md.sha256
       paper-2-arxiv-metadata.md)

echo "=================================================================="
echo "task77 consolidate battery — target: scripts/gwm-inbox-consolidate-v1.sh"
echo "=================================================================="

# P0 — syntax
if bash -n "$S"; then ok "P0 bash -n syntax"; else bad "P0 bash -n syntax"; fi

# P1 — env unset → fail-closed with the exact remedy
log="$T/p1.log"
if env -u PROD_PATH -u INBOX bash "$S" >"$log" 2>&1; then
  bad "P1 unset env must fail"
else
  check "P1 unset env fails closed" "PROD_PATH unset" "$log"
fi

# P2 — source tree missing → fail-closed
prod="$T/prod"; inbox="$T/inbox"; mkdir -p "$inbox"
log="$T/p2.log"
if PROD_PATH="$prod" INBOX="$inbox" bash "$S" >"$log" 2>&1; then
  bad "P2 missing source tree must fail"
else
  check "P2 missing source tree fails closed" "source tree not found" "$log"
fi

# P3 — source file missing → fail-closed, inbox untouched
prod="$T/prod3"; inbox="$T/inbox3"; wp="$prod/gpt/documentation/white_paper/4NDR0MEDA"
mkdir -p "$wp" "$inbox"
printf 'only-one-file-present\n' > "$wp/refs-2.bib"
log="$T/p3.log"
if PROD_PATH="$prod" INBOX="$inbox" bash "$S" >"$log" 2>&1; then
  bad "P3 missing source file must fail"
else
  check "P3 missing source file fails closed" "source file not found" "$log"
  if [[ -z "$(ls -A "$inbox")" ]]; then ok "P3 inbox untouched"; else bad "P3 inbox touched"; fi
fi

# RC — wrong-pin source bytes → copy rolled back, fail, inbox clean
prod="$T/prodRC"; inbox="$T/inboxRC"; wp="$prod/gpt/documentation/white_paper/4NDR0MEDA"
mkdir -p "$wp" "$inbox"
for f in "${FILES[@]}"; do printf 'tampered-bytes\n' > "$wp/$f"; done
log="$T/rc.log"
if PROD_PATH="$prod" INBOX="$inbox" bash "$S" >"$log" 2>&1; then
  bad "RC wrong-pin source must fail"
else
  check "RC wrong-pin copy fails at the pin" "do not match the recorded pin" "$log"
  check "RC rollback removes the bad copy" "removed" "$log"
  if [[ -z "$(ls -A "$inbox")" ]]; then ok "RC inbox clean after rollback"; else bad "RC inbox polluted"; fi
fi

# P4 — pre-existing wrong-pin inbox file → FAIL, file NOT modified
prod="$T/prodP4"; inbox="$T/inboxP4"; wp="$prod/gpt/documentation/white_paper/4NDR0MEDA"
mkdir -p "$wp" "$inbox"
for f in "${FILES[@]}"; do printf 'irrelevant-source\n' > "$wp/$f"; done
printf 'pre-existing-wrong-bytes\n' > "$inbox/${FILES[0]}"
before="$(sha256sum "$inbox/${FILES[0]}" | cut -d' ' -f1)"
log="$T/p4.log"
if PROD_PATH="$prod" INBOX="$inbox" bash "$S" >"$log" 2>&1; then
  bad "P4 pre-existing mismatch must fail"
else
  check "P4 pre-existing mismatch fails closed" "DOES NOT MATCH" "$log"
  after="$(sha256sum "$inbox/${FILES[0]}" | cut -d' ' -f1)"
  if [[ "$before" == "$after" ]]; then ok "P4 pre-existing file unmodified"; else bad "P4 pre-existing file modified"; fi
fi

echo "------------------------------------------------------------------"
echo "SCOPENOTE: the COPIED+PIN-VERIFIED (real-pin GREEN) path and the"
echo "SCOPENOTE: ALREADY-CONSOLIDATED (real-pin) path require the certified"
echo "SCOPENOTE: operator-held bytes; they exercise at the operator's run."
echo "SCOPENOTE: paste-back of the [C5]/[C6] lines closes them."
echo "=================================================================="
echo "BATTERY VERDICT: $pass PASS / $fail FAIL"
if [[ "$fail" -eq 0 ]]; then
  echo "BATTERY: GREEN — consolidation script is shippable (mock-reachable paths)"
else
  echo "BATTERY: RED — do not ship"
  exit 1
fi

```
