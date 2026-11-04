# Telemetry Source: references/white-paper-relay/paper-2-v1.6-to-v1.6.1.changes
- **Source Identifier**: `references/white-paper-relay/paper-2-v1.6-to-v1.6.1.changes`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `037dbdd997cc8c36d5749ade5333e93cd9252ac5acf64e7aebc63c1765148123`

---

## Raw Telemetry Content

```
# paper-2 v1.6 -> v1.6.1 — CHANGES OF RECORD (R2-55 refresh, operator-selected)

Boundary: trace 1a167750ba56e08d, 2026-10-23, Task 59.
Parent: v1.6 (certified, Round-5.7: 'manuscript is certified ready for external deposit').
Prereq discharged: MEDA A3 re-pin (9fc75309b3f2…) — delivered and pushed by operator this round.

## 1. Emitter parameterization (emit_verification_data_v16.py -> emit_verification_data_v161.py)

    --- paper-src/home/z/my-project/scripts/emit_verification_data_v16.py	2026-10-22 03:32:41.000000000 +0000
    +++ scripts/emit_verification_data_v161.py	2026-10-23 06:39:09.606107295 +0000
    @@ -1,9 +1,19 @@
     #!/usr/bin/env python3
    -"""emit_verification_data_v16.py — D8 build-time verification emitter, v1.6.
    +"""emit_verification_data_v161.py — D8 build-time verification emitter, v1.6.1.
     
    -Task 47 (trace 1a1617ea8e57f261). v1.6 ledger folds (R2-16..R2-54):
    -  R2-37  A1 ancestry gate replaces the unconditional expected-tripwire
    -         allowlist: drift is admitted iff a1c27468... is an ancestor of
    +v1.6.1 maintenance refresh (R2-55 disposition fork, operator-selected):
    +parameterized from v1.6 by the witness at Task 59 (trace 1a167750ba56e08d):
    +  - CDP pinned anchor advanced e2f3d86 -> 6facbf17 (the reconciliation commit
    +    itself reconciled the manifest; origin tip is now the pinned,
    +    manifest-consistent state — 48/48, carrying the R2-46 articulation pin).
    +    The v1.6 CDP special case (pinned-commit anchor over a 46/47 origin-tip
    +    defect) collapses to the plain HEAD == origin/main contract.
    +  - MEDA-PINCHAIN takes the clean path: A1 re-pinned to 4bc2cfb and A3
    +    re-pinned to 6facbf17 at maintenance commit 9fc75309b3f2 (Tasks 36/50/56
    +    queue discharged); no admission gymnastics remain.
    +  - OUT_DIR -> scripts/build-v161 (v1.6 outputs left pristine).
    +All v1.6 legs, gates, and fail-closed semantics unchanged:
    +  R2-37  A1 ancestry gate: drift is admitted iff a1c27468... is an ancestor of
              origin/main AND the build head equals origin/main; any other FAIL
              aborts. Also asserts the historical PIN source a207175 is an
              ancestor (A-3 parameterization gate) and that the signed tag's
    @@ -15,13 +25,8 @@
       R2-46  CDP root manifest count emitted dynamically (no static prose).
       R2-36  L3 emitted per repository (CDP disclosure record vs GWM substrate).
       A-1    Pre-rename literal anchors emitted and asserted BEFORE the L0/L1
    -         loops: SHA-256 of a207175:sessions/MANIFEST.sha256, SHA-1 tree id
    -         of a207175^{tree} (substrate-internal), SHA-256 tar-snapshot of
    -         a207175^{tree} (portable).
    -  E-3    Deterministic full-DAG SHA-256 log: canonical serialization of the
    -         (commit, path, blob-sha256) walk over sessions/ history, hashed
    -         into one chain digest (pinned reduction order: sorted, reverse
    -         chronological commits, byte-exact serialization).
    +         loops.
    +  E-3    Deterministic full-DAG SHA-256 log (pinned reduction order).
     Fail-closed throughout: any unexpected FAIL aborts with exit 1 and no .tex.
     """
     import hashlib
    @@ -36,17 +41,18 @@
     CDP = os.path.join(BASE, "coordinated-disclosure-public")
     MEDA = os.path.join(BASE, "4ndr0meda")
     GWM = os.path.join(BASE, "glm-working-memory")
    -OUT_DIR = os.path.join(BASE, "scripts", "build-v16")
    +OUT_DIR = os.path.join(BASE, "scripts", "build-v161")
     PINCHAIN_MD = os.path.join(CDP, "PIN-CHAIN-RECOMPUTATION.md")
     A207175 = "a207175"
     A1C27468 = "a1c27468db880dd224f879e2330cd3e512c6c66b"
     TAG = "witness-anchor-2026-10-20"
     EMPTY_SHA = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    -# CDP pinned anchor (new witness catch, Round-5.6): latest origin/main state
    -# that is pushed AND manifest-consistent; the origin tip e96624d carries a
    -# manifest reconciliation defect. Advance admitted under the R2-37-shape
    -# ancestry gate (pinned commit must remain an ancestor of CDP origin/main).
    -CDP_PINNED = "e2f3d8658ac0a637bb952ee93567020f0551b98b"
    +# CDP pinned anchor (v1.6.1 refresh): the origin tip itself — the
    +# reconciliation commit 6facbf1 restored manifest consistency at the tip
    +# (48/48, R2-46 articulation pin carried). HEAD == origin/main == pinned
    +# state; the v1.6 special case is collapsed (kept as a constant so the
    +# CDP-ROOT plumbing and the ancestry assertion remain one parameter).
    +CDP_PINNED = "6facbf17a8dcf5dad1bdd441b328760b8b49779f"
     
     log = []
     results = {}
    @@ -210,7 +216,7 @@
             cdp_root_ok += 1
     record("CDP-ROOT", f"{cdp_root_ok}/{cdp_root_total}",
            ok=(cdp_root_ok == cdp_root_total and cdp_root_total > 0))
    -log.append("CDP-ROOT evaluated at pinned commit e2f3d86 (origin tip 46/47 defect registered fail-visible)")
    +log.append(f"CDP-ROOT evaluated at pinned commit {CDP_PINNED[:12]} == origin/main (reconciled tip; v1.6.1 refresh)")
     
     rc, out, _ = sh("sha256sum -c sessions/MANIFEST.sha256", cwd=GWM)
     gwm_ok = out.count(": OK")
    @@ -253,16 +259,9 @@
         record("MEDA-PINCHAIN", f"{pin_ok} OK, {pin_fail} FAIL ({failed_anchors}), {pin_unreach} unreachable", ok=False)
     
     # ---------------------------------------------------------------- R2-49 satellite loop (CDP, MEDA)
    -# CDP SPECIAL CASE (new witness catch, registered fail-visible in the build
    -# receipt): origin/main advanced e2f3d86 -> e96624d mid-boundary with a
    -# manifest reconciliation defect (docs/DECISIONS-INDEX.md changed without a
    -# MANIFEST.sha256 regen -> sha256sum -c 46/47 at origin tip). The emitter
    -# therefore anchors CDP at the PINNED COMMIT e2f3d86 — the latest origin/main
    -# state that is (i) pushed, (ii) manifest-consistent — and admits the advance
    -# under the R2-37 ancestry gate shape (pinned commit must be an ancestor of
    -# origin/main; else fatal). The manifest check runs against the pinned tree
    -# via git plumbing (no worktree). MEDA keeps the plain HEAD==origin/main
    -# contract (its origin is consistent).
    +# v1.6.1: both satellites hold the plain contract. (v1.6 anchored CDP at a
    +# pinned commit because the then-origin-tip e96624d carried a 46/47 manifest
    +# defect; the reconciliation commit 6facbf1 resolved it — see docstring.)
     for label, repo in (("CDP", CDP), ("MEDA", MEDA)):
         rc, _, err = sh("git fetch origin", cwd=repo)
         if rc != 0:
    @@ -271,28 +270,20 @@
         if rc != 0:
             fatal(f"R2-49: {label} origin/main unresolvable")
         origin = out.strip()
    -    if label == "MEDA":
    -        rc, out, _ = sh("git rev-parse HEAD", cwd=repo)
    -        if rc != 0:
    -            fatal(f"R2-49: {label} HEAD unresolvable")
    -        head = out.strip()
    -        if head != origin:
    -            fatal(f"R2-49: {label} HEAD {head[:12]} != origin/main {origin[:12]}")
    -        anchor_commit = head
    -        anchor_note = "HEAD == origin/main"
    -    else:
    -        rc, _, err = sh(f"git merge-base --is-ancestor {CDP_PINNED} origin/main", cwd=repo)
    -        if rc != 0:
    -            fatal(f"R2-37-shape ancestry gate (CDP): pinned anchor {CDP_PINNED[:12]} is NOT an ancestor of origin/main {origin[:12]}: {err}")
    -        rc, out, _ = sh(f"git rev-parse {CDP_PINNED}^{{tree}}", cwd=repo)
    -        if rc != 0:
    -            fatal("CDP pinned tree unresolvable")
    -        anchor_commit = CDP_PINNED
    -        anchor_note = (f"pinned-commit anchor (R2-37-shape admission): {CDP_PINNED[:12]} is an ancestor of "
    -                       f"origin/main {origin[:12]}; origin tip carries a manifest reconciliation defect (46/47), "
    -                       "reconciliation commit rides THE CALL")
    -        log.append(f"R2-49: CDP anchored at pinned commit {CDP_PINNED[:12]} (ancestor of origin/main {origin[:12]}); "
    -                   "origin-tip manifest defect registered fail-visible")
    +    # v1.6.1: plain HEAD == origin/main contract for BOTH satellites — the
    +    # CDP pinned-commit special case existed only for the v1.6-era 46/47
    +    # origin-tip defect, which the reconciliation commit 6facbf1 resolved.
    +    rc, out, _ = sh("git rev-parse HEAD", cwd=repo)
    +    if rc != 0:
    +        fatal(f"R2-49: {label} HEAD unresolvable")
    +    head = out.strip()
    +    if head != origin:
    +        fatal(f"R2-49: {label} HEAD {head[:12]} != origin/main {origin[:12]}")
    +    if label == "CDP" and head != CDP_PINNED:
    +        fatal(f"v1.6.1 parameterization gate: CDP HEAD {head[:12]} != pinned anchor {CDP_PINNED[:12]} (re-run only at the pinned tip)")
    +    anchor_commit = head
    +    anchor_note = "HEAD == origin/main == pinned anchor"
    +    log.append(f"R2-49: {label} anchored at {anchor_commit[:12]} ({anchor_note}), tar-digest computed in-process")
         rc, tarb, err = shb(f"git archive --format=tar {anchor_commit}", cwd=repo)
         if rc != 0 or not tarb:
             fatal(f"R2-49: {label} git archive failed: {err}")

## 2. Table-5 delta (what the refresh was FOR)

- CDP-ROOT: 47/47 @ e2f3d86 (pinned-commit anchor over 46/47 origin-tip defect) -> 48/48 @ 6facbf17 DIRECTLY (reconciled tip; the R2-55 objective).
- GWM-SESSIONS: 20/20 @ b481d75 -> 22/22 @ 088ef69 (Task-50-era tip -> current tip incl. session-012 snapshot).
- MEDA: manifest 29/29 @ ec40e2f -> 29/29 @ 9fc7530; pinchain '11 OK + A1+A3 admitted' -> '12 OK + A1 admitted' (A3 clean via re-pin; A1 lagged the mid-build snapshot push, gate-admitted; fully re-pinned to 088ef69 in the follow-up production pass c0e08c4).
- GWM anchors: head 088ef69, bundle 6d224618… (9,133,384 B), DAG 327 pairs 0dd0cdb9…, GATE-D 27 commits / 48 pairs / 8 precon.
- Crypto leg: TAG-FINGERPRINT 888EAEEF…C7549 — keyring loss n=5 recovered in-boundary from the designated channel (scripts/operator-profile-key.gpg, sha256 0eba631d…); git verify-tag GOOD.

## 3. QA adjudication

- 27 pp (== v1.6 baseline); ??-scan 0; 10/11 literal anchors byte-verified in PDF text raw, 11/11 after whitespace normalization; the one raw miss (tag-commit d4018e5…) behaves IDENTICALLY in the certified v1.6 extraction -> extraction artifact, not a regression.
- Pinchain cell delta 11OK->12OK is the refresh's own signature (A3 clean via re-pin).
- Fail-closed events during build: 2 FATAL parity-gate aborts traced to a stale workspace-restored clone shadowing the glm-working-memory path (ln -sfn trap; stale clone preserved as glm-working-memory.stale-bak). No verification was skipped; the emitter refused until the environment was truthful — working as designed.

```
