# Telemetry Source: write-ups/paper-2-round5.3-argon-receipt-v1.md
- **Source Identifier**: `write-ups/paper-2-round5.3-argon-receipt-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `4ba9ea6e781af5917e6f5d42a92c7098a0f196520174f95bcbb8be2627046b12`

---

## Raw Telemetry Content

# paper-2-round5.3-argon-receipt-v1 — verbatim pin

Provenance: ARGON (Gemini) "Round-5.3 In-Band Verification Receipt", relayed by
the operator through the IM layer at boundary trace `1a1613c6ec71bced`
(Task 46, 2026-10-22). Pinned byte-for-byte between the marker lines below.
Normalization disclosure (fail-visible, §3): the chat transport wrapped the
relay in code fences and scattered stray empty fence pairs between blocks;
fence scaffolding is normalized, all operative content (tables, severity
blocks, code, math) is verbatim as transmitted — including relay-escaping
artifacts inside quoted code (`\$(` forms), which are themselves registered
as transport-layer evidence in `round5.4-counters-v1.md` §2/T5.

--- BEGIN VERBATIM RELAY ---

### Round-5.3 In-Band Verification Receipt

| Artifact | Sidecar Declared SHA-256 | Computed UTF-8 Bytes (Chars) | Computed SHA-256 | Verdict |
| --- | --- | --- | --- | --- |
| `round5.2-counters-v1.md` | `def5d3b1a77a700a5a7cc496d04d5e062188be59e75f207aad5803b82ca5a7ad` | `24,435` B (`24,070` chars) | `def5d3b1a77a700a5a7cc496d04d5e062188be59e75f207aad5803b82ca5a7ad` | **MATCH** |
| `round5.2-counters-v1.md.sha256` | *(sidecar)* | `90` B (`90` chars) | `b0bd553f1aa8e320b42f132312a8818456c4ff3a9bdcf423d0d5e67d0b3a2b1d` | **RECEIVED** |

### §1 Per-Finding Ruling on R2-36–R2-46 (`round5.2-counters-v1.md`)

All 11 Round-5.2 dispositions (R2-36 through R2-46) and the §2.2 review-object resolution (`c7e0e931…` logged as out-of-chain build; `2f9d204e…` relabeled `v1.5-reconstruct`) are **ACCEPTED IN SUBSTANCE**, subject to **four executable implementation guards** (`R2-47` through `R2-50` below) caught by running your proposed `GATE-A`, `GATE-C`, `R2-38`, `R2-41/GATE-D`, and `R2-43` code snippets in `/bin/sh`, `awk`, and `pdftotext -bbox-layout` against `paper-2-v1.4.pdf`.

| Registry ID | Surface | Witness Verdict | Argon Round-5.3 Ruling |
| --- | --- | --- | --- |
| **R2-36** | Surface A (L3 `10/10` vs. `16/16` repo collision) | ACCEPT-WITH-REFINEMENT | **CLOSED** — emitter proof (CDP `10/10` vs. GWM `16/16`, now `19/19` at `ac3f9ea…`) settles the cause; repo attribution in Table 4 and Appendix A resolves the collision. |
| **R2-37** | Surface A (`A1` ancestry-gated admission + `GATE-B`) | ACCEPT | **CLOSED** — comparing against `origin/main` with `git merge-base --is-ancestor a1c27468... origin/main` and `head == BUILD_TIME_EXPECTED_HEAD` closes the force-push hole. |
| **R2-38** | Surface A (Satellite pins/tar digests + verify-before-execute order) | ACCEPT | **CLOSED WITH GUARD (`R2-49`)** — reorder and satellite anchors accepted; apply `set -o pipefail` and `origin/main` parity in the emitter loop (see `R2-49`). |
| **R2-39** | Surface B (Vacuous R2-29/30 gates + Round-3 rebuttal errata + `GATE-A`) | ACCEPT | **CLOSED WITH GUARD (`R2-47`)** — errata reclassification accepted; `GATE-A` requires textblock bounds (`xMax <= 540`, `yMax <= 804`) + unclipped word-count parity because Poppler's `pdftotext -bbox-layout` pre-clips outside the MediaBox and misses Page 13 of `v1.4.pdf` (see `R2-47`). |
| **R2-40** | Surface B (Two-parameter interval bound $\sup_{1 \le r \le t \le T} \Vert{}\prod_{s=r}^t M_s\Vert{} \le C$) | ACCEPT | **CLOSED** — interval bound with $C \ge 1$ and $\Vert{}e_T\Vert{} \le C\Vert{}e_0\Vert{} + C\sum_{r=1}^T \Vert{}\eta_r\Vert{}$ is mathematically exact. |
| **R2-41** | Surface B (§6.4 scope + `GATE-D` `git rev-list --all` walk) | ACCEPT | **CLOSED WITH GUARD (`R2-50`)** — `GATE-D` must track `(path, blob_sha256)` pairs rather than bare filenames so in-place blob edits at a fixed filename cannot pass as `preserved` (see `R2-50`). |
| **R2-42** | Surface C (Blind-window observational scoping + bare-surface Tier-1 division of labor) | ACCEPT | **CLOSED** — removes the uncontrolled causal counterfactual and accurately attributes Tier-1 hash computation to the operator's host machine. |
| **R2-43** | Surface D (Appendix A L0 loop, CWD prefixes, L5 `GATE-C`, emitter layout) | ACCEPT | **CLOSED WITH GUARD (`R2-48`)** — the proposed L0 shell pipeline in §3/R2-43 has a POSIX pipe-subshell bug where `fails=1` is lost when the `while` loop exits, causing `[ "$fails" -eq 0 ]` to print `L0 OK` and exit `0` on failure (see `R2-48`). |
| **R2-44** | Surface D (Bytes-first save rule convention) | ACCEPT | **CLOSED** — verified in `round5.2-counters-v1.md` (`24,435` UTF-8 bytes / `24,070` chars). |
| **R2-45** | Surface E (Unified $S_t \in \mathbb{R}^{d_k \times d_v}$ left-multiplication + $w_t = \alpha_t \beta_t \mathbf{1}_{d_v}$) | ACCEPT | **CLOSED** — consistent across Equations (1)–(5) and Table 1. |
| **R2-46** | Surface E (`1-equals-1` pin act into CDP `63ea783d…` + `PIN-CHAIN-RECOMPUTATION.md` `37b5028f…`) | ACCEPT-WITH-REFINEMENT | **CLOSED** — witness catch that `1-equals-1_official-articulation_v1.0.md` was absent from all three repos confirms the value of the audit; pinning it into CDP increases the CDP root manifest count from `47/47` to `48/48` (ensure no static `47/47` prose remains). |

### §2 Pre-Build Implementation Guards on the v1.6 Specification (`round5.2-counters-v1.md` §3 & §5)

Executing the proposed gate and shell code from `round5.2-counters-v1.md` inside this sandbox exposed four concrete implementation defects that would otherwise ship into the v1.6 build harness and Appendix A:

```
[SEVERITY: critical]
[LOCATION: `round5.2-counters-v1.md` §5 (`GATE-A`, lines 287–291) and §3 (`R2-39` Fix 2)]
[CLAIM AS WRITTEN: "GATE-A (layout, anti-clipping — from R2-39): `pdftotext -bbox-layout build.pdf out.html`; parse the per-page XHTML; assert every word's xMax <= page width and yMax <= page height; fail closed listing offenders; run on every page, reported per page (Table 2 and Table 5 pages named in the build log)."]
[DEFECT: Tested directly against `paper-2-v1.4.pdf` (`w = 595.28`, `h = 841.89`), `GATE-A` as specified (`xMax <= page_width` and `yMax <= page_height` over `pdftotext -bbox-layout`) catches Page 19 (`xMax = 599.13`, 8 words) and Page 23 (`xMax = 599.13`, 3 words), but **REPORTS ZERO OFFENDERS (`over_x = 0, over_y = 0`, PASS) ON PAGE 13 (Table 2 vertical overflow, R2-29)** for two independent reasons:
1. Poppler's `TextOutputDev` (`pdftotext -bbox-layout`) pre-clips glyphs against the page `CropBox`/`MediaBox` (`[0, 0, 595.28, 841.89]`) *before* emitting `<word>` elements. Every word whose bounding box starts below `y = 841.89` (the tail of Row 6 plus all of Rows 7, 8, and 9 on Page 13) is silently discarded from `out.html` before your coordinate check runs, whereas unclipped stream extractors (`pypdf`) still see all of Rows 7–9.
2. The last partially surviving line of Table 2 Row 6 on Page 13 (`"errata-over-"`) has `yMax = 834.52`, which overruns the bottom textblock margin and prints below the page-number baseline (`yMax = 803.03` on all 25 pages), yet still satisfies `834.52 <= 841.89` (`page_height`). Across all 22 non-overflowing pages of `v1.4.pdf`, `max(xMax) = 526.91` and `max(yMax) = 803.03`.]
[MINIMAL FIX: Tighten `GATE-A` to: (1) assert textblock-plus-footer bounds rather than paper-edge bounds on every word in `pdftotext -bbox-layout` (`xMax <= 540.0` and `yMax <= 804.0` for A4 `595.28 x 841.89`, which immediately flags Page 13 at `yMax = 834.52`, Page 19 at `xMax = 599.13`, and Page 23 at `xMax = 599.13` with zero false positives across the other 22 pages), AND (2) assert that no text was pre-clipped outside the `MediaBox` by verifying that every page's normalized token stream in `pdftotext -bbox-layout` equals the unclipped stream extracted after rewriting the PDF `/MediaBox` to `[-500, -500, 1500, 2000]` (or via `pypdf`).]
```

```
[SEVERITY: critical]
[LOCATION: `round5.2-counters-v1.md` §3 (`R2-43` Fix 1, lines 211–221) and §5 (`GATE-C`, lines 296–305)]
[CLAIM AS WRITTEN: R2-43 Fix 1: "grep -E ... PIN-CHAIN-RECOMPUTATION.md | sed -E ... | while read -r old new dg; do a=\$(git -C ../glm-working-memory show \"a207175:\$old\" | sha256sum | cut -d' ' -f1); b=$(sha256sum \"$new\" | cut -d' ' -f1); [ \"$a\" = \"$dg\" ] && [ \"$b\" = \"$dg\" ] || { echo \"L0 FAIL $old\"; fails=1; }; done; [ \"$fails\" -eq 0 ] && echo \"L0 OK\" || exit 1" / GATE-C: "done | awk 'NR>1 && \$1+0<=p+0{print \"L5 FAIL non-monotonic at \" NR; exit 1} {p=\$1; n++} END{if(n!=6){print \"L5 FAIL count=\" n; exit 1} print \"L5 OK 6/6 strictly monotonic\"}'"]
[DEFECT: Two shell/awk assertion-masking bugs verified by execution in `/bin/sh` and `awk`:
1. R2-43 Fix 1 (POSIX pipe-subshell variable loss + zero-match masking): In POSIX `/bin/sh` and default `bash`, the right-hand side of a pipeline (`| while read ...; do ... fails=1; done`) executes in a subshell. Setting `fails=1` inside the piped `while` loop never mutates `$fails` in the parent shell; when the loop ends, the parent shell still sees `fails=0`, evaluates `[ "$fails" -eq 0 ]` as true, prints `L0 OK`, and exits `0` even when every file prints `L0 FAIL`. Additionally, if `grep` matches 0 lines, the loop runs 0 times and prints `L0 OK`.
2. GATE-C (`awk` `exit 1` jumps to `END` block): In `awk`, executing `exit 1` inside a rule block does not bypass the `END` block; it jumps directly into `END`. If a 7th file fails monotonicity when `n == 6` (or if `END` does not check a failure flag), `END` still executes `print "L5 OK 6/6 strictly monotonic"` after printing `L5 FAIL`.]
[MINIMAL FIX: (1) Wrap the right-hand side of the R2-43 L0 pipeline in a brace group `{ ... }` so `$fails` and an explicit row counter `n=8` are evaluated inside the same subshell before exiting:
```sh
grep -E '^\| `(evidence/[^`]+)`\s+\| `(evidence/[^`]+)`\s+\| `[0-9a-f]{64}`' \
    PIN-CHAIN-RECOMPUTATION.md \
| sed -E 's/^\| `([^`]+)`\s+\| `([^`]+)`\s+\| `([0-9a-f]{64})`.*/\1 \2 \3/' \
| { fails=0; n=0
    while read -r old new dg; do
      n=\$((n + 1))
      a=\$(git -C ../glm-working-memory show "a207175:\$old" | sha256sum | cut -d' ' -f1)
      b=$(sha256sum "$new" | cut -d' ' -f1)
      [ "$a" = "$dg" ] && [ "$b" = "$dg" ] || { echo "L0 FAIL \$old"; fails=1; }
    done
    [ "$fails" -eq 0 ] && [ "$n" -eq 8 ] && echo "L0 OK 8/8" || exit 1; }

```

(2) In `GATE-C`, set `bad=1` before `exit 1` (`{bad=1; print "L5 FAIL non-monotonic at " NR; exit 1}`) and begin `END` with `END{if(bad) exit 1; if(n!=6){...}}`.]
```

```
[SEVERITY: major]
[LOCATION: `round5.2-counters-v1.md` §3 (`R2-38` Fix 1, lines 134–139)]
[CLAIM AS WRITTEN: "for label, repo in (("CDP", CDP), ("MEDA", MEDA)): rc, out, _ = sh("git rev-parse HEAD", cwd=repo); record(f"{label}-HEAD", out.strip()); rc, out, _ = sh("git archive --format=tar HEAD | sha256sum", cwd=repo); record(f"{label}-TAR-DIGEST", out.split()[0])"]
[DEFECT: Unlike the `GWM` head contract (which checks `origin/main` and fails closed on staleness), the `R2-38` loop for `CDP` and `MEDA` queries local `HEAD` without asserting `rc == 0`, without asserting `git rev-parse HEAD == git rev-parse origin/main`, and without `set -o pipefail` on `git archive --format=tar HEAD | sha256sum`. In `/bin/sh`, if `git archive` fails (exit 128), `sha256sum` hashes 0 bytes (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`) and exits `0`, silently recording the empty-stream SHA-256 as the repository's root tar anchor.]
[MINIMAL FIX: In `R2-38` Fix 1, assert `HEAD == origin/main` for both `CDP` and `MEDA` (especially critical since `R2-46` commits `1-equals-1` to `CDP` during the v1.6 build, which must be pushed so `origin/main` matches `HEAD`), check `rc == 0` on every command, and either compute the SHA-256 of `git archive --format=tar origin/main` in Python (`hashlib.sha256`) after checking `git archive`'s exit code or prepend `set -o pipefail;`.]
```

```
[SEVERITY: major]
[LOCATION: `round5.2-counters-v1.md` §5 (`GATE-D`, lines 306–312)]
[CLAIM AS WRITTEN: "GATE-D (historical manifest walk — from R2-41): for each commit in `git rev-list --all` touching sessions/, collect the session filename set; emit the union classification preserved / translated (rename-mapped, byte-equal) / authorized-retired (documented) / unresolved; print counts; any unresolved → fail closed unless the build carries an adjudicated allowlist with reasons. This is Algorithm 1 executed, not described."]
[DEFECT: Collecting only "the session filename set" across `git rev-list --all` checks path-existence continuity, not content-digest continuity (Definition 2, $H(R(\tau, \text{path})) = h$). If a historical session file `sessions/session-004.md` had blob SHA-256 $h_1$ at commit $\tau_1$ and was later overwritten in place with different bytes $h_2 \neq h_1$ at the same path without an adjudicated retirement/supersession record, a filename-only walk classifies `sessions/session-004.md` as `preserved` because the filename still exists in `HEAD`.]
[MINIMAL FIX: Have `GATE-D` collect `(path, blob_sha256)` pairs across every historical version of `sessions/MANIFEST.sha256` (and `sessions/` tree objects) in `git rev-list --all`, classifying a historical `(path, h)` pair as `preserved` iff the exact blob digest `h` is present at `path` in `HEAD`, `translated` iff `h` is byte-equal at a rename-mapped path, `authorized-retired` iff `(path, h)` is listed in an adjudicated retirement/errata record, and `unresolved` (exit 1) otherwise.]
```

### §3 Mandatory Hide-Analysis Across Surfaces A–E (Closing the Pre-Build Review Loop)

With all 26 Round-5.1 and Round-5.2 findings (`A-1..A-6`, `B-1..B-8`, `C-1..C-2`, `D-1..D-6`, `E-1..E-5`, and `Row 9`) accepted and the four v1.6 implementation guards (`R2-47..R2-50`) specified above, zero standing rebuttals remain. Per §1 of the Tier-3 brief, closing any attack surface requires a formal **hide-analysis**: the exact class of defect that could still survive on each surface after `v1.6` incorporates `R2-16..R2-50`, the specific external evidence required to expose it, and why this review loop is structurally unable to produce that evidence.

| Surface | Residual Defect Class Hidden After `R2-16..R2-50` | Evidence Required to Expose It | Why This Review Loop Cannot Produce That Evidence |
|---|---|---|---|
| **Surface A** (Anchor Chain in Print) | **Split-view / equivocation between the witness's local git remotes and the public GitHub mirrors** (e.g., `ac3f9ea…` or `cdebae2…` existing in the witness workspace while the public GitHub remote is force-pushed, private, or serves a different ref to third parties), or **GPG subkey / revocation state divergence** on public keyservers. | Live out-of-band network queries from an independent verifier outside the operator's relay (`git ls-remote [https://github.com/4ndr0666/](https://github.com/4ndr0666/)...`, full clone + `git verify-tag` against a public keyserver / GitHub `.gpg` endpoint at verification time). | The Tier-3 runtime is an air-gapped container with outbound internet disabled, and every repository state receipt reaches Tier-3 through the operator's text relay (`round5.2-counters-v1.md` §1). An air-gapped reviewer can verify internal consistency of in-band hashes, never external network reachability or public mirror non-equivocation. |
| **Surface B** (Closure Registry & Counter-Fixes) | **Source-to-registry drift during the v1.6 compilation step** — i.e., a gap between the accepted fix specification in `round5.2-counters-v1.md` (`R2-16..R2-50`) and the actual LaTeX macros, Python emitter lines, and rendered glyphs produced when `v1.6` compiles. | The compiled `paper-2-v1.6.pdf` binary, the `v1.6` source tarball (including `scripts/emit_verification_data.py` and `verification-data.tex`), and the build-time output of `GATE-A..GATE-D`. | In this turn (`Round 5.3`), `round5.2-counters-v1.md` is a pre-build specification (§4/§6: `v1.6` executes after Round-5.3 acceptance). Until the compiled `v1.6` artifact bytes cross the relay boundary, no reviewer can verify that the executed `v1.6` build matches its specification. |
| **Surface C** (Guarantee Structure & Veracity) | **Pre-commit selection and survivorship bias ($\mathcal{F}: \text{World} \to R$)** — unlogged sessions, discarded model generations, cherry-picked stochastic reviewer runs, or client-side clock manipulation prior to `MANIFEST.sha256` creation. | Cryptographic origin and completeness attestations from the model-serving provider (zkTLS / TLSNotary session proofs with monotonic provider sequence numbers) plus RFC 3161 trusted timestamping authority (TSA) or public transparency-log inclusion receipts (e.g., Rekor) at each session close. | All agents in this loop (Witness, Tier-1, Tier-2, Tier-3) operate downstream of the operator's capture boundary and receive only the curated repository projection $R$. No computation over $R$ can detect the absence of sessions or turns that never entered $R$ (which is why `C-1` and `Row 9` explicitly bound the paper's claim to post-commit byte invariance). |
| **Surface D** (Custody & Recomputability) | **Correlated single-custodian compromise ($n=1$ key + transport + adjudication monism)** — because the human operator holds the sole signing key (`888EAEEF…C7549`), controls the relay channel between the witness and external reviewers, and adjudicates retirement records, a single compromised or adversarial operator environment can forge a self-consistent history, re-sign all tags, and relay matching in-band digests. | Hardware-isolated per-agent signing keys (TEE/HSM-backed witness and reviewer keys not exportable to the operator) and multi-party threshold cosigning ($n \ge 2$ independent custodians publishing out-of-band pins to disjoint public logs). | By architectural construction ($n=1$ field program), the operator is the sole committer and sole relay transport between the witness VM and Tier-3. The loop cannot verify $n \ge 2$ custody independence when its own communication channel is a star topology centered on the single custodian. |
| **Surface E** (Unfalsifiable / Over-Denial Residue) | **Empirical activational-tier breakdowns on real delta-rule weights** — specifically, whether multi-layer GDN-2 / KDA / MesaNet checkpoints under actual FP16/BF16 GPU inference exhibit chaotic gate-perturbation blow-up ($\tilde{M}_t^{(\ell)} \neq M_t^{(\ell)}$) that defeats even short-horizon behavioral probes. | Instrumented forward passes over trained multi-layer DeltaNet / GDN-2 / MesaNet checkpoints measuring empirical $\Vert{}\tilde{S}_t^{(\ell)} - S_t^{(\ell)}\Vert{}$ and probe false-negative rates across hardware targets (e.g., H100 vs. MI300X / CPU). | The paper's 16-day field program runs exclusively at the text/context layer without access to or instrumentation of recurrent fast-weight tensors $S_t \in \mathbb{R}^{d_k \times d_v}$, and the review loop evaluates static proofs and scripts rather than executing multi-GPU tensor replay benchmarks. |

### §4 Gate to `v1.6` Execution

The Round-5.2 findings ledger (`R2-36..R2-46`) is **APPROVED FOR v1.6 BUILD EXECUTION** with the four implementation guards (`R2-47..R2-50`) folded into §4 steps 1–3 and §5 (`GATE-A`, `GATE-C`, `GATE-D`). Once `v1.6` compiles witness-side, transmit the resulting artifacts (or their in-band text equivalents + `GATE-A..GATE-D` build receipt) for final post-build verification.

--- END VERBATIM RELAY ---

