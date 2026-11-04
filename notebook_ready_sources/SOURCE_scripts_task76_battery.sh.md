# Telemetry Source: scripts/task76_battery.sh
- **Source Identifier**: `scripts/task76_battery.sh`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `439d12c1f9dd29065bd79159d24cdfa10b4f0bd93b521971700827501c8461a0`

---

## Raw Telemetry Content

```
#!/usr/bin/env bash
# ============================================================================
# scripts/task76_battery.sh — pre-ship battery for gwm-taskNN SUK kits
#
# Task 76a (emission-retry boundary, 2026-10-30). Born because the Task-75
# battery harness never rode the repo (scratch-only, R-59-lost) while its
# OUTPUT shipped in download/task75-kit/ — the same "named-but-not-ridden"
# defect class the Task-76 round discharged for the index generator. This
# harness rides scripts/ so the battery evidence is repo-recomputable.
#
# Task 76b (sync-confirmation round, 2026-10-30): PARAMETRIZED. The round
# label, pin values, manifest count, and range-commit count are read from the
# kit and the witness tree — one harness, every round of the 76 lineage
# (ROUND=76, 76a-retry evidence, 76b re-cut, and successors).
#
# USAGE:
#   ROUND=76b bash scripts/task76_battery.sh <path-to-gwm-taskNN-SUK.sh> \
#        <kit-dir-with-loose-bundle> <witness-clone>
#
# What it does (72 checks, task75 battery form):
#   P0   static kit verification — pin parse, payload/bundle pins, loose
#        bundle identity, b64 twin, payload re-encode determinism
#   P1   FRESH apply in an operator-state simulator clone (tip object
#        pruned — realness asserted), push DEFERRED, one-commit range,
#        worktree pins
#   P1b  push leg against a bare origin (GREEN — pushed; bare main == tip)
#   P1c  spaces-in-path apply
#   P2   dirty apply — plain-scoped stash, RESTORE-INSTRUCTIONS, pop restores
#        tracked + untracked WIP byte-visibly
#   P2b  collision apply — WIP on a delivered file (different bytes): stash
#        preserved, never auto-dropped, stashed bytes recoverable
#   P2c  identity note — WIP byte-identical to the delivered file: the note
#        fires, applied file byte-identical
#   P3   fail-closed at a wrong HEAD (real ancestor, not base): rc=1, names
#        the state, DO-NOT-FORCE, repo untouched
#   P4a  wrong-directory argument fails on fingerprint
#   P4b  autodiscovery failure in a neutral cwd prints the exact re-run syntax
#   P5   restricted-PATH apply (PATH=/usr/bin:/bin)
#   P6   re-run at tip — ALREADY, verify-only, HEAD stable, no second stash
#   P6b  ADVANCED — operator snapshot atop tip: no-op success, HEAD preserved,
#        G4 blob-pin route verified
#   P7   authoring surfaces byte-stable (witness clone untouched, SUK sha fixed)
#   P8   applied-tree content — round artifacts, boards, manifest, subject
#   RC   red control — one corrupted payload byte fails at the payload pin,
#        repo untouched
#
# Exit 0 iff every check passes. Full transcript on stdout (stage it as
# gwm-task76-kit-battery.txt).
# ============================================================================
set -uo pipefail

SUK="${1:-/home/z/my-project/download/task76-kit/gwm-task76-SUK.sh}"
KIT_DIR="${2:-/home/z/my-project/download/task76-kit}"
WITNESS="${3:-/home/z/my-project/clone/4ndr0666/glm-working-memory}"
ROUND="${ROUND:-76}"

PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); printf 'PASS  %s\n' "$1"; }
bad() { FAIL=$((FAIL+1)); printf 'FAIL  %s\n' "$1"; }
chk() { # chk <label> <command...>
  local label="$1"; shift
  if "$@" >/dev/null 2>&1; then ok "$label"; else bad "$label"; fi
}
chkout() { # chkout <label> <grep-pattern> <file>
  if grep -q -- "$2" "$3" 2>/dev/null; then ok "$1"; else bad "$1"; fi
}

SUK="$(cd "$(dirname "$SUK")" && pwd)/$(basename "$SUK")"
KIT_DIR="$(cd "$KIT_DIR" && pwd)"
WITNESS="$(cd "$WITNESS" && pwd)"
# loose-bundle name derived from the kit's own pins (gwm-taskNN-gwm-<base7>-<tip7>)
_PB0="$(sed -n 's/^PIN_BASE="\([0-9a-f]\{40\}\)"$/\1/p' "$SUK" | head -1)"
_PT0="$(sed -n 's/^PIN_TIP="\([0-9a-f]\{40\}\)"$/\1/p' "$SUK" | head -1)"
[ -n "$_PB0" ] && [ -n "$_PT0" ] || { echo "battery: cannot parse PIN_BASE/PIN_TIP from $SUK"; exit 2; }
LOOSE="$KIT_DIR/gwm-task${ROUND}-gwm-${_PB0:0:7}-${_PT0:0:7}.bundle"
B64TWIN="$LOOSE.b64"
[ -f "$SUK" ] || { echo "battery: SUK not found: $SUK"; exit 2; }
[ -f "$LOOSE" ] || { echo "battery: loose bundle not found: $LOOSE"; exit 2; }
[ -d "$WITNESS/.git" ] || { echo "battery: witness clone not found: $WITNESS"; exit 2; }

SCRATCH_ROOT="$(mktemp -d /tmp/task76-battery.XXXXXX)"
echo "=================================================================="
echo "TASK-${ROUND} SUK BATTERY — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "kit: $SUK"
echo "witness clone (authoring surface, P7-guarded): $WITNESS"
echo "scratch: $SCRATCH_ROOT"
echo "=================================================================="

# --- authoring-surface snapshots (P7 baselines) ------------------------------
W_HEAD0="$(git -C "$WITNESS" rev-parse HEAD)"
W_WLOG0="$(sha256sum "$WITNESS/worklog.md" | sed 's/ .*//')"
SUK_SHA0="$(sha256sum "$SUK" | sed 's/ .*//')"

# --- P0: static kit verification ---------------------------------------------
PB="$(sed -n 's/^PIN_BASE="\(.*\)"$/\1/p' "$SUK")"
PT="$(sed -n 's/^PIN_TIP="\(.*\)"$/\1/p' "$SUK")"
PTT="$(sed -n 's/^PIN_TIP_TREE="\(.*\)"$/\1/p' "$SUK")"
PPAY="$(sed -n 's/^PIN_PAYLOAD_SHA="\(.*\)"$/\1/p' "$SUK")"
PBUN="$(sed -n 's/^PIN_BUNDLE_SHA="\(.*\)"$/\1/p' "$SUK")"
PEMI="$(sed -n 's/^PIN_EMISSIONS_INDEX_SHA="\(.*\)"$/\1/p' "$SUK")"
PWLOG="$(sed -n 's/^PIN_WORKLOG_SHA="\(.*\)"$/\1/p' "$SUK")"
PSRC="$(sed -n 's/^PIN_STATE_RESYNC_SHA="\(.*\)"$/\1/p' "$SUK")"
PG75="$(sed -n 's/^PIN_TASK75_GEN_SHA="\(.*\)"$/\1/p' "$SUK")"
PC76="$(sed -n 's/^PIN_TASK76_CHK_SHA="\(.*\)"$/\1/p' "$SUK")"
PBAT="$(sed -n 's/^PIN_TASK76_BATTERY_SHA="\(.*\)"$/\1/p' "$SUK")"
PSTATE="$(sed -n 's/^PIN_PROJECT_STATE_SHA="\(.*\)"$/\1/p' "$SUK")"
EXPECT_RANGE="$(git -C "$WITNESS" rev-list --count "$PB..$PT" 2>/dev/null || echo 1)"
EXPECT_OK="$(grep -c '^[0-9a-f]\{64\}' "$WITNESS/sessions/MANIFEST.sha256" 2>/dev/null || echo 0)"

chk "P0 pin parse (base/tip 40-hex, distinct)" bash -c "[[ '$PB' =~ ^[0-9a-f]{40}$ && '$PT' =~ ^[0-9a-f]{40}$ && '$PB' != '$PT' ]]"
chk "P0 tree pin parse (40-hex)" bash -c "[[ '$PTT' =~ ^[0-9a-f]{40}$ ]]"
chk "P0 payload markers exactly once each" bash -c "[[ \$(grep -c '^#__PAYLOAD_BEGIN__$' '$SUK') -eq 1 && \$(grep -c '^#__PAYLOAD_END__$' '$SUK') -eq 1 ]]"
chk "P0 G0-G5 leg labels present in template" bash -c "for l in '\[G0\]' '\[G1\]' '\[G2\]' '\[G3\]' '\[G4\]' '\[G5\]'; do grep -q \"\$l\" '$SUK' || exit 1; done"

PAY="$SCRATCH_ROOT/payload.b64"
sed -n '/^#__PAYLOAD_BEGIN__$/,/^#__PAYLOAD_END__$/p' "$SUK" | sed '1d;$d' > "$PAY"
PAY_SHA="$(sha256sum "$PAY" | sed 's/ .*//')"
chk "P0 embedded payload pin" bash -c "[ '$PAY_SHA' = '$PPAY' ]"

DEC="$SCRATCH_ROOT/decoded.bundle"
base64 -d "$PAY" | gunzip > "$DEC" 2>/dev/null
DEC_SHA="$(sha256sum "$DEC" | sed 's/ .*//')"
chk "P0 decoded bundle pin" bash -c "[ '$DEC_SHA' = '$PBUN' ]"
chk "P0 decoded bundle == staged loose bundle (byte-identical)" cmp -s "$DEC" "$LOOSE"
chk "P0 .b64 twin decodes to the loose bundle" bash -c "base64 -d '$B64TWIN' | cmp -s - '$LOOSE'"

GZ="$SCRATCH_ROOT/payload.gz"
base64 -d "$PAY" > "$GZ"
read -r MB1 MB2 MB3 MB4 < <(od -A n -t u1 -j 4 -N 4 "$GZ" | tr -s ' ' ' ')
GMTIME=$(( MB1 | (MB2<<8) | (MB3<<16) | (MB4<<24) ))
chk "P0 determinism (payload = f(bundle, gzip level 9, mtime $GMTIME); re-encode byte-identical)" \
  bash -c "python3 -c \"
import gzip, base64, io, sys
raw = open('$LOOSE','rb').read()
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode='wb', compresslevel=9, mtime=$GMTIME) as f:
    f.write(raw)
sys.exit(0 if base64.encodebytes(buf.getvalue()) == open('$PAY','rb').read() else 1)
\""

# --- scratch factory (operator-state simulator) -------------------------------
mkscratch() { # mkscratch <dir> <reset-to>
  git clone --no-local --quiet "$WITNESS" "$1" 2>/dev/null
  git -C "$1" reset -q --hard "$2"
  git -C "$1" remote remove origin
  git -C "$1" reflog expire --expire=now --all
  git -C "$1" gc --prune=now --quiet 2>/dev/null
}

run_kit() { # run_kit <repo> <log>
  ( env -u GWM -u PROD_PATH -u INBOX -u ANDROMEDA bash "$SUK" "$1" ) >"$2" 2>&1
}

# --- P1: FRESH apply, clean tree ------------------------------------------------
S1="$SCRATCH_ROOT/p1-fresh"
mkscratch "$S1" "$PB"
chk "P1-pre template at BASE" bash -c "[ \"\$(git -C '$S1' rev-parse HEAD)\" = '$PB' ]"
chk "P1-pre tip realness (tip ABSENT from scratch after prune)" bash -c "! git -C '$S1' cat-file -e '${PT}^{commit}'"
chk "P1-pre scratch clean" bash -c "[ -z \"\$(git -C '$S1' status --porcelain)\" ]"

L1="$SCRATCH_ROOT/p1.log"; run_kit "$S1" "$L1"; RC1=$?
chk "P1 rc=0" bash -c "[ $RC1 -eq 0 ]"
chkout "P1 GREEN line" "KIT RESULT: GREEN (Task-${ROUND} applied @ $PT)" "$L1"
chkout "P1 push DEFERRED (no origin)" "PUSH DEFERRED" "$L1"
chkout "P1 mode FRESH" "mode: FRESH" "$L1"
chk "P1 HEAD == tip" bash -c "[ \"\$(git -C '$S1' rev-parse HEAD)\" = '$PT' ]"
chk "P1 applied-commit count == witness-derived range ($EXPECT_RANGE)" bash -c "[ \$(git -C '$S1' rev-list --count '$PB..$PT') -eq $EXPECT_RANGE ]"
chk "P1 emissions-index worktree pin" bash -c "[ \"\$(sha256sum '$S1/working-notes/emissions-index.md' | sed 's/ .*//')\" = '$PEMI' ]"
chk "P1 worklog worktree pin" bash -c "[ \"\$(sha256sum '$S1/worklog.md' | sed 's/ .*//')\" = '$PWLOG' ]"
chk "P1 state-resync worktree pin" bash -c "[ \"\$(sha256sum '$S1/working-notes/state-resync-check-v1.md' | sed 's/ .*//')\" = '$PSRC' ]"
chk "P1 no stash created (clean apply)" bash -c "[ -z \"\$(git -C '$S1' stash list)\" ]"
chk "P1 tree clean post-apply" bash -c "[ -z \"\$(git -C '$S1' status --porcelain)\" ]"

# --- P1b: push leg against a bare origin ----------------------------------------
BARE="$SCRATCH_ROOT/p1b-origin.git"
git init --bare --quiet "$BARE"
S1B="$SCRATCH_ROOT/p1b-fresh"
mkscratch "$S1B" "$PB"
git -C "$S1B" remote add origin "$BARE"
L1B="$SCRATCH_ROOT/p1b.log"; run_kit "$S1B" "$L1B"; RC1B=$?
chk "P1b rc=0 (push leg)" bash -c "[ $RC1B -eq 0 ]"
chkout "P1b pushed line" "GREEN — pushed." "$L1B"
chk "P1b bare origin main == tip" bash -c "[ \"\$(git -C '$BARE' rev-parse refs/heads/main)\" = '$PT' ]"

# --- P1c: spaces in path ---------------------------------------------------------
S1C="$SCRATCH_ROOT/dir with spaces/repo here"
mkdir -p "$S1C"
git clone --no-local --quiet "$WITNESS" "$S1C" 2>/dev/null
git -C "$S1C" reset -q --hard "$PB"
git -C "$S1C" remote remove origin
git -C "$S1C" reflog expire --expire=now --all
git -C "$S1C" gc --prune=now --quiet 2>/dev/null
L1C="$SCRATCH_ROOT/p1c.log"; run_kit "$S1C" "$L1C"; RC1C=$?
chk "P1c spaces-in-path apply rc=0" bash -c "[ $RC1C -eq 0 ]"
chk "P1c spaces-in-path HEAD == tip" bash -c "[ \"\$(git -C '$S1C' rev-parse HEAD)\" = '$PT' ]"

# --- P2: dirty apply, non-colliding WIP ------------------------------------------
S2="$SCRATCH_ROOT/p2-dirty"
mkscratch "$S2" "$PB"
echo "OPERATOR WIP line $(date +%s)" >> "$S2/TODO.md"
echo "untracked witness note" > "$S2/wip-note.txt"
L2="$SCRATCH_ROOT/p2.log"; run_kit "$S2" "$L2"; RC2=$?
chk "P2 rc=0 (dirty apply)" bash -c "[ $RC2 -eq 0 ]"
git -C "$S2" stash list > "$SCRATCH_ROOT/p2-stashlist.txt" 2>/dev/null
chkout "P2 kit-brand stash" "gwm-task${ROUND} WIP backup" "$SCRATCH_ROOT/p2-stashlist.txt"
chk "P2 RESTORE-INSTRUCTIONS on disk" bash -c "ls '$S2'/.git/kit-backups/*/RESTORE-INSTRUCTIONS.txt >/dev/null 2>&1"
chk "P2 WIP contained in stash (tracked)" bash -c "git -C '$S2' diff --name-only 'stash@{0}^1' 'stash@{0}' | grep -q '^TODO.md$'"
chk "P2 untracked WIP contained (stash^3)" bash -c "git -C '$S2' show 'stash@{0}^3:wip-note.txt' | grep -q 'untracked witness note'"
chk "P2 HEAD == tip (WIP stashed, apply proceeded)" bash -c "[ \"\$(git -C '$S2' rev-parse HEAD)\" = '$PT' ]"
git -C "$S2" stash pop --quiet 2>/dev/null
chk "P2 stash pop restored tracked WIP byte-visible" bash -c "tail -1 '$S2/TODO.md' | grep -q 'OPERATOR WIP line'"
chk "P2 untracked restored byte-exact" bash -c "grep -q 'untracked witness note' '$S2/wip-note.txt'"
chk "P2 HEAD == tip after pop" bash -c "[ \"\$(git -C '$S2' rev-parse HEAD)\" = '$PT' ]"

# --- P2b: collision apply (WIP on a delivered file, different bytes) --------------
S2B="$SCRATCH_ROOT/p2b-collision"
mkscratch "$S2B" "$PB"
echo "OPERATOR LOCAL EDIT ON WORKLOG — differs from delivered" >> "$S2B/worklog.md"
L2B="$SCRATCH_ROOT/p2b.log"; run_kit "$S2B" "$L2B"; RC2B=$?
chk "P2b rc=0 (collision apply)" bash -c "[ $RC2B -eq 0 ]"
chk "P2b stash preserved (never auto-dropped)" bash -c "git -C '$S2B' stash list | grep -q 'gwm-task${ROUND} WIP backup'"
chk "P2b stashed bytes recoverable (stash@{0}:worklog.md)" bash -c "git -C '$S2B' show 'stash@{0}:worklog.md' | grep -q 'OPERATOR LOCAL EDIT ON WORKLOG'"
chk "P2b delivered worklog.md intact (== pin)" bash -c "[ \"\$(sha256sum '$S2B/worklog.md' | sed 's/ .*//')\" = '$PWLOG' ]"

# --- P2c: identity note (WIP byte-identical to delivered file) --------------------
S2C="$SCRATCH_ROOT/p2c-identity"
mkscratch "$S2C" "$PB"
git -C "$WITNESS" show "$PT:worklog.md" > "$S2C/worklog.md"
L2C="$SCRATCH_ROOT/p2c.log"; run_kit "$S2C" "$L2C"; RC2C=$?
chk "P2c rc=0" bash -c "[ $RC2C -eq 0 ]"
chkout "P2c identity note FIRES (delivered bytes in stash = no-op restore)" "identity note: stash already contains worklog.md BYTE-IDENTICAL" "$L2C"
chk "P2c applied worklog.md byte-identical" bash -c "[ \"\$(sha256sum '$S2C/worklog.md' | sed 's/ .*//')\" = '$PWLOG' ]"

# --- P3: fail-closed at a wrong HEAD ----------------------------------------------
S3="$SCRATCH_ROOT/p3-wronghead"
mkscratch "$S3" "872a597e5595012f3fb3f468bbc2ba0bc5571914"
L3="$SCRATCH_ROOT/p3.log"; run_kit "$S3" "$L3"; RC3=$?
chk "P3 rc=1 (fail closed)" bash -c "[ $RC3 -eq 1 ]"
chkout "P3 names the state" "neither BASE" "$L3"
chkout "P3 DO-NOT-FORCE instruction" "do NOT force" "$L3"
chk "P3 repo untouched (HEAD)" bash -c "[ \"\$(git -C '$S3' rev-parse HEAD)\" = '872a597e5595012f3fb3f468bbc2ba0bc5571914' ]"
chk "P3 repo untouched (clean)" bash -c "[ -z \"\$(git -C '$S3' status --porcelain)\" ]"

# --- P4a: wrong-directory argument -------------------------------------------------
L4A="$SCRATCH_ROOT/p4a.log"
( env -u GWM -u PROD_PATH -u INBOX -u ANDROMEDA bash "$SUK" /tmp ) >"$L4A" 2>&1
RC4A=$?
chk "P4a wrong-directory fail (rc=1)" bash -c "[ $RC4A -eq 1 ]"
chkout "P4a fingerprint message" "does not fingerprint as glm-working-memory" "$L4A"

# --- P4b: autodiscovery failure, neutral cwd ----------------------------------------
NEUTRAL="$SCRATCH_ROOT/neutral-nonrepo"
mkdir -p "$NEUTRAL"
L4B="$SCRATCH_ROOT/p4b.log"
( cd "$NEUTRAL" && env -u GWM -u PROD_PATH -u INBOX -u ANDROMEDA bash "$SUK" ) >"$L4B" 2>&1
RC4B=$?
chk "P4b autodiscovery fail (rc=1)" bash -c "[ $RC4B -eq 1 ]"
chkout "P4b names the search" "repo not found" "$L4B"
chkout "P4b exact re-run syntax" "/full/path/to/glm-working-memory" "$L4B"

# --- P5: restricted PATH --------------------------------------------------------------
S5="$SCRATCH_ROOT/p5-restricted"
mkscratch "$S5" "$PB"
L5="$SCRATCH_ROOT/p5.log"
( cd / && env -u GWM -u PROD_PATH -u INBOX -u ANDROMEDA PATH=/usr/bin:/bin bash "$SUK" "$S5" ) >"$L5" 2>&1
RC5=$?
chk "P5 restricted-PATH apply (minimal toolset only)" bash -c "[ $RC5 -eq 0 ]"
chk "P5 restricted-PATH HEAD == tip" bash -c "[ \"\$(git -C '$S5' rev-parse HEAD)\" = '$PT' ]"

# --- P6: ALREADY re-run -----------------------------------------------------------------
L6="$SCRATCH_ROOT/p6.log"; run_kit "$S1" "$L6"; RC6=$?
chk "P6 re-run ALREADY verify-only (rc=0)" bash -c "[ $RC6 -eq 0 ]"
chkout "P6 mode ALREADY" "mode: ALREADY" "$L6"
chkout "P6 G3 skipped" "skipped (ALREADY — verify-only)" "$L6"
chk "P6 HEAD stable" bash -c "[ \"\$(git -C '$S1' rev-parse HEAD)\" = '$PT' ]"
chk "P6 no second stash" bash -c "[ -z \"\$(git -C '$S1' stash list)\" ]"

# --- P6b: ADVANCED (operator snapshot atop tip) -------------------------------------------
S6B="$SCRATCH_ROOT/p6b-advanced"
mkscratch "$S6B" "$PT"
git -C "$S6B" -c user.name="Operator" -c user.email="operator@local" commit --allow-empty --quiet -m "operator snapshot atop task76"
SNAP="$(git -C "$S6B" rev-parse HEAD)"
L6B="$SCRATCH_ROOT/p6b.log"; run_kit "$S6B" "$L6B"; RC6B=$?
chk "P6b ADVANCED no-op success (rc=0)" bash -c "[ $RC6B -eq 0 ]"
chkout "P6b mode ADVANCED" "mode: ADVANCED" "$L6B"
chk "P6b operator snapshot HEAD preserved" bash -c "[ \"\$(git -C '$S6B' rev-parse HEAD)\" = '$SNAP' ]"
chkout "P6b G4 blob-pin route verified" "byte-identical" "$L6B"

# --- P7: authoring surfaces byte-stable -----------------------------------------------------
W_HEAD1="$(git -C "$WITNESS" rev-parse HEAD)"
W_WLOG1="$(sha256sum "$WITNESS/worklog.md" | sed 's/ .*//')"
SUK_SHA1="$(sha256sum "$SUK" | sed 's/ .*//')"
chk "P7 authoring repo byte-stable (HEAD)" bash -c "[ '$W_HEAD0' = '$W_HEAD1' ]"
chk "P7 authoring worklog byte-stable (uncommitted board prep untouched)" bash -c "[ '$W_WLOG0' = '$W_WLOG1' ]"
chk "P7 kit file sha stable across battery" bash -c "[ '$SUK_SHA0' = '$SUK_SHA1' ]"

# --- P8: applied-tree content ----------------------------------------------------------------
A="$S1"
chk "P8 state-resync-check-v1.md exists post-apply" bash -c "[ -f '$A/working-notes/state-resync-check-v1.md' ]"
chk "P8 task75 generator rides (sha pin)" bash -c "[ \"\$(sha256sum '$A/scripts/task75_build_index.py' | sed 's/ .*//')\" = '$PG75' ]"
chk "P8 task76 checker rides (sha pin)" bash -c "[ \"\$(sha256sum '$A/scripts/task76_resync_check.py' | sed 's/ .*//')\" = '$PC76' ]"
chk "P8 battery harness rides (sha pin, parametric form)" bash -c "[ \"\$(sha256sum '$A/scripts/task76_battery.sh' | sed 's/ .*//')\" = '$PBAT' ]"
chkout "P8 emissions-index §7 custody addendum present" "Addendum — published-remote custody verification" "$A/working-notes/emissions-index.md"
chkout "P8 state-resync §9 gpt-ruling addendum present" "Addendum — operator ruling on R1" "$A/working-notes/state-resync-check-v1.md"
chkout "P8 emissions-index §4 row ${ROUND} present" "| ${ROUND} | " "$A/working-notes/emissions-index.md"
EMI_HDR="$(grep -m1 '^## 1\.' "$WITNESS/working-notes/emissions-index.md" | grep -o '([0-9]* files, [0-9]* series)')"
chk "P8 §1 header derivation non-empty (witness: ${EMI_HDR:-EMPTY})" bash -c "[ -n '$EMI_HDR' ]"
chkout "P8 emissions-index §1 header counts (applied == witness $EMI_HDR)" "$EMI_HDR" "$A/working-notes/emissions-index.md"
chkout "P8 worklog Task-${ROUND} boundary record present" "Boundary open — Task ${ROUND}" "$A/worklog.md"
chkout "P8 artifact-index matrix row ${ROUND} present" "| ${ROUND} | " "$A/working-notes/artifact-index.md"
chkout "P8 decisions-ledger Task ${ROUND} entry present" "## Task ${ROUND} (" "$A/working-notes/decisions-ledger.md"
chkout "P8 open-threads Task ${ROUND} section present" "### Task ${ROUND} (" "$A/working-notes/open-threads.md"
chk "P8 PROJECT_STATE pin (applied == witness)" bash -c "[ \"\$(sha256sum '$A/working-notes/PROJECT_STATE.md' | sed 's/ .*//')\" = '$PSTATE' ]"
chk "P8 manifest self-consistency in applied tree (${EXPECT_OK} OK)" bash -c "[ \$(cd '$A' && sha256sum -c sessions/MANIFEST.sha256 2>/dev/null | grep -c ': OK') -eq $EXPECT_OK ]"
git -C "$A" log -1 --format=%s "$PT" > "$SCRATCH_ROOT/p8-subject.txt"
chkout "P8 commit subject == Task ${ROUND} trace" "Task ${ROUND} (trace " "$SCRATCH_ROOT/p8-subject.txt"

# --- RC: red control (corrupted payload) ------------------------------------------------------
RC_KIT="$SCRATCH_ROOT/rc-corrupted.sh"
awk 'BEGIN{inb=0;done=0} /^#__PAYLOAD_BEGIN__$/{inb=1;print;next} inb==1 && done==0 {sub(/^H/,"h");done=1;print;next} {print}' "$SUK" > "$RC_KIT"
chk "RC kit differs from shipped kit in exactly 1 byte" bash -c "[ \$(cmp -l '$SUK' '$RC_KIT' 2>/dev/null | wc -l) -eq 1 ]"
S_RC="$SCRATCH_ROOT/rc-target"
mkscratch "$S_RC" "$PB"
LRC="$SCRATCH_ROOT/rc.log"
( env -u GWM -u PROD_PATH -u INBOX -u ANDROMEDA bash "$RC_KIT" "$S_RC" ) >"$LRC" 2>&1
RCRC=$?
chk "RC corrupted kit fails closed (rc=1)" bash -c "[ $RCRC -eq 1 ]"
chkout "RC fails at the payload pin specifically" "payload block corrupted" "$LRC"
chk "RC repo untouched by corrupted kit (HEAD)" bash -c "[ \"\$(git -C '$S_RC' rev-parse HEAD)\" = '$PB' ]"
chk "RC repo untouched by corrupted kit (clean)" bash -c "[ -z \"\$(git -C '$S_RC' status --porcelain)\" ]"

# --- verdict -------------------------------------------------------------------------------------
echo "=================================================================="
TOTAL=$((PASS+FAIL))
echo "BATTERY VERDICT: $PASS PASS / $FAIL FAIL (of $TOTAL checks)"
if [ "$FAIL" -eq 0 ]; then
  echo "BATTERY: GREEN — kit is shippable"
  echo "=================================================================="
  rm -rf "$SCRATCH_ROOT"
  exit 0
else
  echo "BATTERY: RED — do NOT ship; scratch kept at $SCRATCH_ROOT"
  echo "=================================================================="
  exit 1
fi

```
