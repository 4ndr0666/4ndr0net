# Telemetry Source: references/white-paper-relay/round5.2-counters-v1.md
- **Source Identifier**: `references/white-paper-relay/round5.2-counters-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `def5d3b1a77a700a5a7cc496d04d5e062188be59e75f207aad5803b82ca5a7ad`

---

## Raw Telemetry Content

# Round-5.2 Counters & v1.6 Build Order — v1

Witness counter set for the Argon Round-5.2 In-Band Verification Receipt.
Role: GLM (Witness), zai-web surface, 2026-10-22, boundary trace 1a1611603db2ab99.
Parent artifacts (all digests already verified in-band by both parties in the
Round-5.2 receipt unless marked otherwise): review object `paper-2-v1.4.pdf`
c7e0e931…, `round5-counters-v1.md` b59a8431…, `paper-2-v1.3-to-v1.5repro.changes`
9ae8cfb5…, `paper-2-arxiv-metadata.md` v0.7 0ef99398…, corrected brief v2
f5f12404… (carrier, digest first printed by the receipt and re-verified
witness-side this boundary).

## §0 Scope and self-containment

This artifact is the "refine" leg of the single task stream: paper → Argon
critique (DELIVERED, Round-5.2) → refine (this artifact) → transmit → Argon
ruling → v1.6 build. It is self-contained in the corrected-brief sense: every
artifact it references is either (a) this artifact itself, (b) an artifact
whose digest both parties have already verified in-band, or (c) a patch site
quoted from the v1.5-repro source tree, which is the paper's source of record
and is in Argon's custody via the verified changes file and metadata. No
reference assumes the operator or Argon holds anything not already in the
verified custody set.

The Round-5.1 triage stands as transmitted (brief v2 §8: 15/15 ACCEPTED,
R2-16, R2-22–R2-35, routed to the v1.6 fix ledger). This artifact adds the
Round-5.2 findings as R2-36–R2-46, continuing the registry numbering. Per the
standing carrying contract: per-finding verdict + fix + verification; the
operator adjudicates; the cycle closes at zero standing rebuttals.

## §1 Bootstrap record (this boundary)

- Pull: `git pull --ff-only` on the production-path clone — already up to
  date; origin/main == local HEAD `ac3f9ead627d6addb56a5955c76aacceef67efa2`
  (boards update Task 46, committed 2026-10-22T00:00:40Z). Liveness: GREEN,
  substrate advanced to ac3f9ea and public.
- Sessions manifest: 19/19 OK. CDP root manifest: 47/47 OK. 4NDR0MEDA: 29/29
  pinned files match. Signed tag `witness-anchor-2026-10-20`: GOOD signature,
  primary fingerprint 888EAEEFF89E8CAFACAF191873DD9742274C7549, keyring
  persisted (no recovery leg this boundary).
- F-002 #34 registered: 17th consecutive CRITICAL ERROR header (trace
  1a1611603db2ab99). Header present, transmission complete, `--- END
  TRANSMISSION ---` present with the promised Argon reply attached in-band —
  the Round-5.2 re-ask from the prior boundary is CLOSED by delivery, nothing
  re-asked, nothing assumed.
- cwd-error class, 10th occurrence (self-caught, log-don't-rewrite): first
  manifest pass ran `sha256sum -c MANIFEST.sha256` in the substrate root,
  where no root manifest exists by design (substrate inventory is
  `sessions/MANIFEST.sha256` only). Corrected in-boundary; the corrected
  readings above are the only ones entered into the record.

## §2 Receipt processing and custody resolutions

### §2.1 Artifact cross-check (recomputed witness-side this boundary)

| Artifact | Receipt declared | Witness recomputed | Verdict |
| --- | --- | --- | --- |
| `argon-relay-corrected-brief-v2-custody-and-mandate.md` | f5f12404… (carrier) | f5f12404… · 28,750 B | MATCH |
| `round5-counters-v1.md` | b59a8431… | b59a8431… · 10,879 B | MATCH |
| `paper-2-v1.3-to-v1.5repro.changes` | 9ae8cfb5… | 9ae8cfb5… · 1,912 B | MATCH |
| `paper-2-arxiv-metadata.md` v0.7 | 0ef99398… | 0ef99398… · 9,571 B | MATCH |
| `paper-2-v1.4.pdf` (review object) | c7e0e931… · 905,767 B | NOT HELD witness-side | see §2.2 |

Four of five rows close byte-exact on independent recomputation. The review
object is resolved separately below.

### §2.2 Review-object identity (pre-registered fork, now resolved)

The Task-46 board pre-registered the rule: "2f9d204e = label-only
(log-don't-rewrite), anything else = out-of-chain build, custody record
changes D6/D7-relevant." The receipt resolves the digest:
`paper-2-v1.4.pdf` as received = c7e0e931… / 905,767 B. Witness-side
recomputation: the only PDF in the custody chain is `paper-2-v1.5-repro.pdf`
= 2f9d204e… / 908,897 B (two identical copies, re-verified this boundary).
Neither digest nor size matches the received object.

Resolution, entered per the board's own rule: the transmitted review object
is an OUT-OF-CHAIN build relative to the witness custody record. Logged, not
rewritten. Consequences, stated plainly:

1. The Round-5.2 findings bind the object Argon actually received
   (c7e0e931…). Nothing below re-litigates that.
2. Every Round-5.2 finding was cross-checked against the v1.5-repro SOURCE
   TREE (the paper's source of record), not the received PDF bytes: every
   quoted defect sentence was located in the source at a specific file/line
   (given per finding in §3). The findings therefore survive the identity
   question: they are source-level defects, not PDF-build artifacts.
3. D6/D7 note rides the next boards commit: the custody record gains one
   line — review object as received = c7e0e931… (out-of-chain build, label
   `paper-2-v1.4.pdf`); chain identity of record = 2f9d204e… (v1.5-repro /
   relabeled v1.5-reconstruct per brief v2 §3).
4. The v1.6 build (§4) re-establishes the chain from the pinned source tree;
   its changes file covers both prior identities explicitly.

### §2.3 Residual relay items closed

- Task-46 catch (b) — REGISTRY OMISSION (counters b59a8431 unmentioned in
  the relay set): CLOSED by the receipt itself; Argon verified the counters
  in-band from the brief-v2 §5 embed (hash match). Surface B had what it
  needed; the omission had no effect.
- Task-46 prepared Argon addendum variants (two, per digest outcome): MOOT —
  the critique proceeded and delivered; no addendum is required.

## §3 Findings ledger R2-36–R2-46 (dispositions)

Severity as assigned by Argon; mechanism notes refine where the emitter
source (which both parties can re-derive) settles the exact cause.
Disposition classes: ACCEPT (fix as specified) / ACCEPT-WITH-REFINEMENT
(fix accepted, mechanism or route corrected). No REBUTs: eleven for eleven,
no standing rebuttals from this set.

### R2-36 · CRITICAL · Surface A — L3 count contradiction (10/10 vs 16/16)

- Verdict: ACCEPT-WITH-REFINEMENT (mechanism now proven from the emitter
  source; both of Argon's minimal-fix branches are superseded by the exact
  fix, which is simpler).
- Proven mechanism: the two counts are emitted from TWO DIFFERENT
  REPOSITORIES' session manifests under one identical command string.
  Emitter lines 90–96: L3 runs `sha256sum -c sessions/MANIFEST.sha256` with
  cwd = coordinated-disclosure-public (the disclosure record's ported
  session archive; 10 entries at build time → Table 4 "L3: 10/10"). Emitter
  lines 152–156: GWM-SESSIONS runs the same command string with cwd =
  glm-working-memory (substrate manifest; 16 entries at build time → Table 4
  row "Substrate session-archive manifest: 16/16"). Appendix A prints the
  bare command with no repository attribution (appendix.tex:26 vs the
  substrate manifest line), so a stranger running it in the wrong tree
  refutes the printed count. Not a sliced manifest; not a stale carry —
  repository ambiguity, exactly the D-1 class.
- Fix: (i) every Appendix A verbatim block gains a repo-attribution comment
  (`# in coordinated-disclosure-public` / `# in glm-working-memory` / `# in
  4NDR0MEDA`); (ii) Table 4 row L3 description becomes "Whole-file session
  pins, disclosure-record ported archive (`sha256sum -c`, run in
  coordinated-disclosure-public)"; (iii) the substrate row description keeps
  its name and gains "(run in glm-working-memory)"; (iv) the emitter emits
  the repo tag next to each count so Table 4 cannot drift from the commands.

### R2-37 · MAJOR · Surface A — A1 unconditional allowlist

- Verdict: ACCEPT. The defect is real and the emitter source proves it:
  emitter lines 166–177 record the pin-chain result as OK whenever the only
  FAIL is A1 (`expected_tripwire == ["A1"] and pin_unreach == 0`), with no
  ancestry check — a force-push orphaning a1c27468… would still produce
  "12 OK, 1 expected tripwire (A1)" and exit 0.
- Fix (emitter, verbatim patch shape): replace the unconditional adjudication
  with an ancestry-gated admission:
  ```
  rc_anc, _, _ = sh("git merge-base --is-ancestor "
                    "a1c27468db880dd224f879e2330cd3e512c6c66b origin/main",
                    cwd=GWM)
  rc_head, head_out, _ = sh("git rev-parse origin/main", cwd=GWM)
  legit_a1 = (expected_tripwire == ["A1"] and pin_unreach == 0
              and rc_anc == 0
              and head_out.strip() == BUILD_TIME_EXPECTED_HEAD)
  ```
  with `BUILD_TIME_EXPECTED_HEAD` a constant pinned at the v1.6 build (the
  build head, printed into verification-data.tex). Note the refinement:
  the gate compares against origin/main, not local HEAD — the Task-35
  semantics the emitter already uses for the head anchor (operator-verifiable
  state). Anything else fails closed (exit 1, no .tex).
- Fix (paper): appendix.tex:90 comment becomes "# fails closed on unexpected
  FAIL; A1 admitted only if a1c27468… is an ancestor of origin/main AND
  origin/main == build-time pin (ancestry gate, R2-37)"; §8.2 prose
  (08-casestudy.tex:103–111) gains one sentence stating the gate, so the
  tripwire is described as conditional, not allowlisted.

### R2-38 · MAJOR · Surface A — asymmetric anchoring + execute-before-verify

- Verdict: ACCEPT (both sub-defects).
- Fix (1): the emitter emits, and Table 5 prints, build-time commit pins and
  deterministic tree-snapshot digests for the two satellite repositories:
  ```
  for label, repo in (("CDP", CDP), ("MEDA", MEDA)):
      rc, out, _ = sh("git rev-parse HEAD", cwd=repo)
      record(f"{label}-HEAD", out.strip())
      rc, out, _ = sh("git archive --format=tar HEAD | sha256sum", cwd=repo)
      record(f"{label}-TAR-DIGEST", out.split()[0])
  ```
  (Signed tags for the satellites are NOT promised — none exist today; the
  paper says exactly that rather than implying parity with the substrate's
  signed tag.)
- Fix (2): Appendix A is reordered so the coreutils-only out-of-band leg runs
  first: "Root manifests" + "Literal out-of-band anchors" blocks
  (sha256sum/sha256sum -c against Table 5 values; git verify-tag) move ABOVE
  the tool blocks (`python3 tools/manifest.py verify`,
  `python3 tools/pinchain.py verify --local`, and the emitter invocation),
  with an explicit sentence: no repository-supplied code executes before the
  out-of-band digest comparison exits 0.

### R2-39 · MAJOR · Surface B — vacuous R2-29/R2-30 gates + unretracted Round-3 rebuttal

- Verdict: ACCEPT (both sub-defects).
- Fix (1): registry errata, append-only — the pinned counters bytes
  (b59a8431…, also substrate-pinned at write-ups/) are NOT rewritten. A new
  errata artifact (`round5-counters-errata-v1.md`, emitted with v1.6) records:
  (a) the Round-3 truncation rebuttal is reclassified SUPERSEDED — the
  pdftotext text-extraction test that "refuted" it is the same test R2-29/
  R2-30 later proved blind to glyph clipping, so the Round-3 finding
  retroactively stands as confirmed-late; (b) the R2-29/R2-30 verification
  gates are replaced by the glyph-bounding-box gate (GATE-A, §5) and the
  errata cites that gate's build-time output digest.
- Fix (2): GATE-A becomes the standing layout gate for every future build
  (spec in §5).

### R2-40 · MAJOR · Surface B — R2-33 criterion bounds the wrong product

- Verdict: ACCEPT. Argon's mathematics is correct: a one-parameter prefix
  bound constrains only the propagation of e_0; with singular transition
  matrices (det M_s = 0 whenever β_s‖k_s‖² = 1) it places zero constraint on
  suffix products ∏_{s=r+1}^T M_s, so per-step injections η_r are unbounded.
- Fix (source 09-limitations.tex:73–75): the operative criterion becomes the
  two-parameter interval-product bound
  `sup_{1 ≤ r ≤ t ≤ T} ‖ ∏_{s=r}^{t} M_s ‖ ≤ C` (C ≥ 1, shared submultiplicative
  norm), with the one-line consequence stated so the reader sees why the
  interval form is the right object: under the perturbed replay
  `e_t = M_t e_{t-1} + η_t`, the interval bound gives
  `‖e_T‖ ≤ C‖e_0‖ + C Σ_{r=1}^{T} ‖η_r‖` (the r = T product is empty, i.e. the
  identity — hence C ≥ 1 wlog). The surrounding paragraph's existing claims
  (per-step contraction unattainable, ρ(M_t) < 1 insufficient, R2-16) are
  unaffected and remain as written.
- Registry: R2-33's product-level restatement is corrected by the same
  errata artifact as R2-39.

### R2-41 · MAJOR · Surface B — R2-32 scope leak + B-1 checkpoint tautology

- Verdict: ACCEPT (both sub-defects).
- Fix (1): 06-interface.tex:198 ("Sketched, not built.") gains Algorithm 1's
  DAG-wide commit traversal in the explicitly-unexecuted list, so §6.4 no
  longer implies the whole context-layer specification is built while §8.2's
  static set runs only L0/L1/L3 over the current tree and a207175
  (appendix.tex:76–85 already says the walk is protocol specification, not an
  integrated command — the two passages now agree).
- Fix (2): the v1.6 B-1 disposition is the real loop, not the {a207175, HEAD}
  restriction (Argon's tautology objection is correct — for every commit
  after a207175 the only checkpoint in that set is HEAD itself, covering
  zero of sessions 11–16). GATE-D (§5) specifies the `git rev-list --all`
  manifest-union walk for the emitter. If it does not ship by build time,
  Algorithm 1 is printed as specified-but-unexecuted with no checkpoint-
  coverage claim — the paper claims exactly what runs.

### R2-42 · MAJOR · Surface C — blind-window causal attribution + "Tier 1 alone"

- Verdict: ACCEPT (both wording corrections; no architecture change).
- Fix (1): 03-blanks.tex:49 — "emerged only because the discipline demanded
  it" becomes "was observed under the protocol's abstention contract (n = 1
  observational test; no unconditioned base-model control arm was run, so
  attribution to the discipline is not experimentally isolated)". The
  narrative keeps its force; the claim stops being an uncontrolled causal
  counterfactual.
- Fix (2): the bare-surface passages are corrected to state who executes
  Tier 1. 04-architecture.tex:92 ("the digest chain is the last layer
  standing … the bare-surface rehydration of Section 8 succeeded through
  Tier 1 alone") and 08-casestudy.tex:11–13 ("the only surviving layer was
  Tier-1 digest verification") each gain the accurate division of labor: on
  a bare model surface stripped of shell/VM execution, Tier-1 digest
  recomputation runs on the operator's host; the model ingests the
  operator-verified text (Tier-2 platform delivery), performs token-level
  comparison (Tier-3), and its rehydration is graded by the boot-restatement
  heuristic (R2-9/D4, non-Tier-1). Tier 1 remains the last layer standing —
  on the operator's machine, not on the model surface.

### R2-43 · MAJOR · Surface D — Appendix A repro contract (four sub-defects)

- Verdict: ACCEPT (all four).
- Fix (1) — L0 executable loop: the placeholders in appendix.tex:33–35 are
  replaced by the actual loop, and the "pinned rename-map table" is named
  and digested: it is
  `coordinated-disclosure-public/PIN-CHAIN-RECOMPUTATION.md` (witness-side
  recomputation this boundary: 37b5028f… — build-time value re-emitted).
  The block printed in Appendix A becomes:
  ```
  # in coordinated-disclosure-public
  grep -E '^\| `(evidence/[^`]+)`\s+\| `(evidence/[^`]+)`\s+\| `[0-9a-f]{64}`' \
      PIN-CHAIN-RECOMPUTATION.md \
  | sed -E 's/^\| `([^`]+)`\s+\| `([^`]+)`\s+\| `([0-9a-f]{64})`.*/\1 \2 \3/' \
  | while read -r old new dg; do
      a=$(git -C ../glm-working-memory show "a207175:$old" | sha256sum | cut -d' ' -f1)
      b=$(sha256sum "$new" | cut -d' ' -f1)
      [ "$a" = "$dg" ] && [ "$b" = "$dg" ] || { echo "L0 FAIL $old"; fails=1; }
    done; [ "$fails" -eq 0 ] && echo "L0 OK" || exit 1
  ```
  (mirror of emitter lines 98–123, which parse the same table with the same
  regex; `fails=0` is initialized above the loop — final typesetting
  tightens this into the exact block that is itself emitted by the emitter).
- Fix (2) — working-directory ambiguity: every block repo-prefixed (shared
  with R2-36 fix); L0's cross-repo step states the sibling layout explicitly.
- Fix (3) — L5 non-asserting loop: appendix.tex:40–42 replaced by the
  fail-closed assertion (GATE-C, §5).
- Fix (4) — emitter path gap: Appendix A states the build layout in relative
  terms: `scripts/emit_verification_data.py` lives in the paper build
  workspace, NOT in any of the three public repositories; the three
  repositories are siblings of one parent directory; `python3
  scripts/emit_verification_data.py` is invoked from that parent. No
  absolute sandbox paths are printed.

### R2-44 · MINOR · Surface D — D-5 size-unit defect in the save rule

- Verdict: ACCEPT, verbatim. The registry record is amended to
  "(10,879 UTF-8 bytes / 10,744 chars for §5; 1,912 UTF-8 bytes / 1,901
  chars for §6)" — riding the same errata artifact as R2-39 — and the
  standing convention registry-wide is now bytes-first: every save rule and
  every attestation prints UTF-8 bytes as the primary size and chars in
  parentheses. This artifact complies (§7).

### R2-45 · MINOR · Surface E — Equations (1)–(5) orientation conflict

- Verdict: ACCEPT. The source confirms the split: eq:gdn (02-lineage.tex:29)
  right-multiplies (`S_{t-1}(I − β_t k_t k_t^T)`, implying S ∈ R^{d_v×d_k}),
  while line 92's prose, Table 1's caption, and eq:gdn2 (02-lineage.tex:43)
  use S ∈ R^{d_k×d_v} with left-multiplication; eq:mesa (02-lineage.tex:58)
  retrievals `S k_i` fit the transposed convention only.
- Fix: unify to R^{d_k×d_v} left-multiplication throughout (the majority
  convention): Eq (1) `S_t = S_{t-1} + k_t v_t^T`; delta rule
  `S_t = (I − β_t k_t k_t^T) S_{t-1} + β_t k_t v_t^T`; eq:gdn
  `S_t = α_t[(I − β_t k_t k_t^T) S_{t-1} + β_t k_t v_t^T]`; eq:mesa
  `S_t ≈ argmin_S Σ_{i≤t} ‖S^T k_i − v_i‖²`; eq:gdn2 unchanged. The
  reduction sentence (02-lineage.tex:49–50) gains the exact substitution:
  eq:gdn2 reduces to eq:gdn under `D_t = α_t I_{d_k}, b_t = β_t 1_{d_k},
  w_t = α_t β_t 1_{d_v}` — the write gate carries the decay so the new write
  is scaled exactly as eq:gdn scales it (Argon's point: with w_t = β_t 1 the
  reduction is inexact). Optional one-line footnote: source papers' transpo-
  sition conventions vary; one orientation is fixed here throughout.

### R2-46 · MINOR · Surface E — Ref [18] digest unprinted — ESCALATED by witness verification

- Verdict: ACCEPT-WITH-REFINEMENT, with a custody escalation Argon could not
  see from its air-gapped container: the artifact is not merely
  digest-unprinted — it is pinned NOWHERE. Witness-side verification this
  boundary: `1-equals-1_official-articulation_v1.0.md` has ZERO hits in the
  full histories of all three public repositories (glm-working-memory,
  coordinated-disclosure-public, 4NDR0MEDA; `git log --all --name-only`
  across each). The reference's location claim ("pinned in the substrate",
  appendix.tex:104–106; "Hash-pinned artifact, github.com/4ndr0666/
  glm-working-memory", Ref [18]) is currently unverifiable by any stranger.
- Witness holds the bytes: `1-equals-1_official-articulation_v1.0.md`,
  SHA-256 63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9,
  12,261 UTF-8 bytes (12,237 chars) — available for immediate in-band
  transport on the operator's word (12 KB text, IM-safe).
- Fix: (1) PIN ACT at the v1.6 build — commit the artifact bytes into
  coordinated-disclosure-public (root-manifest-covered repo), regenerate its
  root manifest, and print the pinned path + digest; (2) Ref [18] and
  appendix.tex:104–106 corrected to "pinned in the disclosure record
  (coordinated-disclosure-public) as <path>, SHA-256 63ea783d…"; (3) Table 4
  caption's "pinned proof artifact" for the L2/L4 receipts is named and
  digested: `coordinated-disclosure-public/PIN-CHAIN-RECOMPUTATION.md`,
  build-time digest (witness-side value 37b5028f…, re-emitted at build).

## §4 v1.6 build order (gated, in sequence)

1. Emitter upgrades, each gated before the next: R2-37 ancestry gate;
   R2-36 repo-attribution emission; R2-38 satellite pins + tar-snapshot
   digests + new Table 5 rows; R2-43 layout and rename-map emission;
   R2-41 GATE-D rev-list walk (or its explicit absence, per the fallback).
2. Source patches: R2-45 equations; R2-40 criterion (09-limitations.tex:74);
   R2-41 §6.4; R2-42 three sites; R2-37 §8.2 prose + appendix comment;
   R2-46 Ref [18] + artifact-availability paragraph + Table 4 caption.
3. Appendix A rewrite (one pass): repo prefixes everywhere; reorder
   out-of-band-first; L0 loop; L5 assertion; emitter layout paragraph
   (R2-36/38/43 jointly).
4. Registry errata artifact (R2-39/44) — append-only, pinned counters
   bytes untouched.
5. Pin act (R2-46): 1-equals-1 artifact into CDP; CDP root manifest
   regenerated; digest recorded.
6. Build: emitter → GATE-A bbox pass → compile → PDF digest of record →
   changes file `paper-2-v1.4+v1.5repro-to-v1.6.changes` covering BOTH prior
   identities (c7e0e931… out-of-chain, 2f9d204e… chain) → SHA256SUMS sheet
   at assembly (Task-41 convention, going forward).
7. Boards: D6/D7 identity line (§2.2); findings-cycle closure entries.

## §5 New verification gates (standing, executable)

- GATE-A (layout, anti-clipping — from R2-39): `pdftotext -bbox-layout
  build.pdf out.html`; parse the per-page XHTML; assert every word's
  xMax ≤ page width and yMax ≤ page height; fail closed listing offenders;
  run on every page, reported per page (Table 2 and Table 5 pages named in
  the build log).
- GATE-B (A1 ancestry — from R2-37): the emitter patch in §3/R2-37; a FAIL
  on A1 is admissible only under ancestor-of-origin/main AND head == build
  pin; otherwise exit 1, no .tex.
- GATE-C (capture geometry — from R2-43):
  ```
  # in coordinated-disclosure-public
  for f in $(ls evidence/F003-capture-00*.pdf | sort); do
    pdfinfo "$f" | awk '/^Page size:/{for(i=1;i<=NF;i++) if($i=="x"){
      print $(i+1); break}}'
  done | awk 'NR>1 && $1+0<=p+0{print "L5 FAIL non-monotonic at " NR; exit 1}
              {p=$1; n++}
              END{if(n!=6){print "L5 FAIL count=" n; exit 1}
                  print "L5 OK 6/6 strictly monotonic"}'
  ```
- GATE-D (historical manifest walk — from R2-41): for each commit in
  `git rev-list --all` touching sessions/, collect the session filename set;
  emit the union classification preserved / translated (rename-mapped,
  byte-equal) / authorized-retired (documented) / unresolved; print counts;
  any unresolved → fail closed unless the build carries an adjudicated
  allowlist with reasons. This is Algorithm 1 executed, not described.
- GATE-E (equation orientation — from R2-45): manual review pass, declared
  as such (no automatable check is claimed).

## §6 Transport and operator queue

One transmit step, per the HALT single-task discipline:

1. Transmit THIS artifact (`round5.2-counters-v1.md`) to Argon in-band.
   Save rule and attestation basis: §7.
2. Report Argon's Round-5.3 ruling back (per-finding verdicts; the carrying
   contract closes at zero standing rebuttals).
3. On acceptance, the v1.6 build executes witness-side per §4. One
   transport decision rides the build, not this boundary: the 1-equals-1
   artifact bytes (63ea783d…, 12,261 B) cross in-band on the operator's
   word if the operator does not already hold them (R2-46 pin act input).

No other requests, no parallel fronts, nothing assumed.

## §7 Save rule and attestation basis

- Digest basis: SHA-256 over the WHOLE file exactly as stored — UTF-8,
  LF line endings, exactly one trailing POSIX newline, fence-free (no
  embedded-digest gymnastics; hash the bytes received; if your transport
  altered the trailing newline the byte count shifts by 1 — re-ask, do not
  assume).
- Attestation values are printed in the transmission cover and the sidecar
  `.sha256` (computed post-write; they cannot live inside this file).
- Sizes are bytes-first per R2-44/D-5.

