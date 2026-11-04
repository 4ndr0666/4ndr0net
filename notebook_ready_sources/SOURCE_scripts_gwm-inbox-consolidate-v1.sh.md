# Telemetry Source: scripts/gwm-inbox-consolidate-v1.sh
- **Source Identifier**: `scripts/gwm-inbox-consolidate-v1.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `21216f0a7ad1793f60b350f718012e265e0c213f01e159c8ac673d97a98206d5`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
#
# gwm-inbox-consolidate-v1.sh — the $GWM-INBOX intake consolidation (Task 77)
#
# WHAT IT DOES — copies the GUP-critical 8 pinned white-paper files from the
#   local gpt clone ($PROD_PATH/gpt/documentation/white_paper/4NDR0MEDA —
#   never uploaded, per the 2026-10-30 ruling) into $GWM-INBOX, verifying
#   each copied byte-stream against its recorded sha256 pin (pins of record
#   per INDEX.md §2; three rows re-anchored by the Task-77c supersession —
#   provenance registered at emissions-index §8). This finalizes the
#   canonical iteration of INDEX.md §2.
# USAGE — source your delivery.sh env block, then:
#     cd "$INBOX" && bash gwm-inbox-consolidate-v1.sh
# SAFETY — fail-closed: a missing source, a pin mismatch, or an unset env
#   var stops the run with the exact problem printed. A file this run copied
#   that then fails its pin is removed again (the inbox is left as found).
#   Pre-existing files are NEVER modified or deleted; a pre-existing file
#   that fails its pin is reported and halts the run for adjudication.
#   Re-run safe: already-consolidated files are detected and skipped
#   (idempotent — a second run is GREEN).
#
# The pin table below is the same table registered in INDEX.md §2. Pins are
# the repo's digests of record (artifact-index / ARGON receipts / task-72
# bib ledger), EXCEPT the three rows re-anchored by the Task-77c supersession
# (2026-10-31, trace 1a18f3fb25e9c1a9): the v1.6.1 tarball + changes file
# (operator adjudication [X0]/[X1]; the prior digests were name-level
# propagations of the v1.6 FINAL SET — H1 confirmed) and the round5.2
# sidecar (witness reconstruction of the canonical sha256sum line over the
# .md's true pin + operator [X0]; the prior b0bd553f… was ARGON's Round-5.3
# computation over a then-relayed pre-canonical form). Superseded-digest
# lineage: emissions-index §8. Pin format: <file>|<sha256>.
#
set -euo pipefail

# --- four-var env block (fail-closed) --------------------------------------
: "${PROD_PATH:?PROD_PATH unset — source your delivery.sh env block first}"
: "${INBOX:?INBOX unset — source your delivery.sh env block first}"
# GWM and ANDROMEDA are not used by this script; PROD_PATH and INBOX are.

GPT_WP="$PROD_PATH/gpt/documentation/white_paper/4NDR0MEDA"

# --- pin table (digests of record) -----------------------------------------
PINNED=(
  "paper-2-v1.6.1-source.tar.gz|a764eb1fafd4df3c5436bae58ecc178aa3a98bb2164f95b50f181415f6c6bfa0"
  "paper-2-v1.6-to-v1.6.1.changes|037dbdd997cc8c36d5749ade5333e93cd9252ac5acf64e7aebc63c1765148123"
  "refs-2.bib|798d1dd499244b283c921222f27199c186645dc1ce6ecae469985aa655b7b101"
  "round5.2-counters-v1.md|def5d3b1a77a700a5a7cc496d04d5e062188be59e75f207aad5803b82ca5a7ad"
  "round5.2-counters-v1.md.sha256|17b7d13b317ab3d5dd188be8d480451baa36510083e44e5f05b2b5a855992e46"
  "round5.4-counters-v1.md|8c3f0497fc7768433890406cdf21cc2224f8816c4f11bbeca70e9c94a5dfbe9d"
  "round5.4-counters-v1.md.sha256|94999ef7d8357cf7631038d9f8dd4f49313954f0b3c02bdb075976c394bdf264"
  "paper-2-arxiv-metadata.md|0ef99398ea3df5dc659532f523ee9548f36ceb5ede50b739e600b47d74add8ed"
)

sha_of() { sha256sum "$1" | cut -d' ' -f1; }

echo "[C0] \$GWM-INBOX intake consolidation — GUP-critical 8 (Task 77)"
echo "[C0] source tree: $GPT_WP"
echo "[C0] inbox:       $INBOX"
[[ -d "$GPT_WP" ]] || { echo "[C0] FAIL: source tree not found: $GPT_WP"; exit 1; }
[[ -d "$INBOX" ]]   || { echo "[C0] FAIL: inbox not found: $INBOX"; exit 1; }

copied=0; already=0
for entry in "${PINNED[@]}"; do
  f="${entry%%|*}"; want="${entry#*|}"
  src="$GPT_WP/$f"; dst="$INBOX/$f"

  if [[ -f "$dst" ]]; then
    got="$(sha_of "$dst")"
    if [[ "$got" == "$want" ]]; then
      echo "[C1] ALREADY-CONSOLIDATED (pin holds): $f"
      already=$((already + 1))
      continue
    else
      echo "[C1] FAIL: $f already exists in the inbox and DOES NOT MATCH its pin."
      echo "[C1]   recorded pin: $want"
      echo "[C1]   found bytes:  $got"
      echo "[C1]   The file was NOT modified. Adjudicate before re-running."
      exit 1
    fi
  fi

  if [[ ! -f "$src" ]]; then
    echo "[C2] FAIL: source file not found: $src"
    echo "[C2]   The gpt clone's white-paper tree is the only pin-satisfying source."
    exit 1
  fi

  cp -- "$src" "$dst"
  got="$(sha_of "$dst")"
  if [[ "$got" != "$want" ]]; then
    rm -- "$dst"
    echo "[C3] FAIL: copied bytes of $f do not match the recorded pin — removed."
    echo "[C3]   recorded pin: $want"
    echo "[C3]   copied bytes: $got"
    echo "[C3]   Adjudicate before re-running — pin lineage and provenance are"
    echo "[C3]   registered in INDEX.md §2 + emissions-index §8 (77c supersession)."
    exit 1
  fi
  echo "[C4] COPIED + PIN-VERIFIED: $f"
  copied=$((copied + 1))
done

echo "[C5] consolidation summary: copied+verified $copied, already-held $already, of ${#PINNED[@]}"
if [[ -f "$INBOX/INDEX.md" ]]; then
  echo "[C6] INDEX.md present in the inbox — canonical iteration finalized."
  echo "[C6] RESULT: GREEN — \$GWM-INBOX now matches INDEX.md §1 + §2."
else
  echo "[C6] NOTE: INDEX.md not found in the inbox."
  echo "[C6]   Save it from the declared share (file:///download/task77-index/)"
  echo "[C6]   into \$INBOX to finalize the canonical iteration."
  echo "[C6] RESULT: GREEN for the intake 8; INDEX.md mirror still pending."
fi

```
