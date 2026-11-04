# Telemetry Source: write-ups/round5.6-build-receipt-v1.md
- **Source Identifier**: `write-ups/round5.6-build-receipt-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `1eb2158d8b9a3106b4d2213f3792e0b7a6e8982b6322470c293d7b103bfc0efd`

---

## Raw Telemetry Content

# round5.6-build-receipt-v1 — Witness v1.6 build execution & gate receipt

Provenance: witness emission, Task 47, boundary trace `1a1617ea8e57f261`,
2026-10-22 (UTC). Parents: ARGON Round-5.5 In-Band Verification Receipt
(verbatim pin: `write-ups/paper-2-round5.5-argon-receipt-v1.md`);
`round5.4-counters-v1.md` (`8c3f0497…` dual-channel); the Task-46 boards
state (`05c137f`). Method: the Round-5.5 §3 "next action" executed — the
v1.6 build ran witness-side with GATE-A..GATE-D at build; every number
below is instrument-computed at this boundary, none hand-typed.

## §0 Standing registrations

- **BOOTSTRAP GREEN**: fetch `d3e38f7..b481d75` (single commit, fast-forward;
  HEAD == origin/main == `b481d750d9928be47a1a119258fd002f548be818`);
  sessions MANIFEST 20/20 (self-caught cwd-error class 9th occurrence —
  manifest verify first run from `sessions/` instead of repo root, corrected
  in-boundary, only corrected readings entered); CDP fast-forwarded
  `e2f3d86 → e96624d` at probe; MEDA `ec40e2fb` == origin. Tag
  `witness-anchor-2026-10-20` commit `d4018e5` ancestry-asserted (A-2).
- **F-002 #35 registered** (18th consecutive CRITICAL ERROR header,
  unbroken arithmetic from #34, trace `1a1617ea8e57f261`).
- **THE CALL round-trip closed**: the operator's "gwmtask46 call executed" +
  push receipt `05c137f..b481d75 main -> main` closes the Task-46 emission
  round-trip hash-exact (bundle head == observed origin head).

## §1 New witness catches (fail-visible, three)

1. **Custody snapshot is digest-complete but byte-truncated (exporter
   truncation class).** The b481d75 snapshot commits the session-010
   archive under the counters digest name (`def5d3b1…` in the filename +
   manifest line) — the substrate custody PIN is thereby CLOSED. But the
   archive's Round-5.2 reply is exporter-truncated mid-ledger (the
   flattened reply line ends at "R2-41 major (R2-32 scope + {a207175," —
   "Show full message" UI truncation); the `round5.2-counters-v1.md` BYTES
   are not recoverable from the snapshot. Per §3 the witness never
   reconstructs them. **Resolution adopted:** the build executed from the
   digest-pinned receipt chain — Round-5.3 receipt (`4ba9ea6e…`, on-disk
   verbatim pin: per-finding rulings on R2-36..R2-46 + guards R2-47..R2-50
   with exact defect/fix text), `round5.4-counters-v1.md` (`8c3f0497…`:
   R2-51/R2-52 + validated gate implementations, scripts on disk), this
   boundary's Round-5.5 receipt (R2-53/R2-54 full text) — with per-ID
   traceability in §3. Argon holds the bytes (VERIFIED IN CUSTODY) and the
   operator holds the save-side copy: the post-build verification round is
   exactly the instrument that checks the executed build against the
   original spec (hide-analysis Surface B's designed closure path).
   Byte paste-back remains open, now non-blocking.
2. **CDP origin-tip manifest defect.** The operator's `e96624d`
   ("decisions-index update") changed `docs/DECISIONS-INDEX.md` without a
   `MANIFEST.sha256` regen → `sha256sum -c` = **46/47** at the origin tip —
   the verify-before-commit convention (paper §4.1) violated by the pushed
   state itself. The fail-closed emitter refused; CDP is therefore
   anchored at the **pinned commit `e2f3d86`** (pushed, manifest-consistent,
   ancestor of origin/main — R2-37 gate shape). The reconciliation +
   R2-46 pin act rides THE CALL as one atomic CDP commit (`6facbf1…`).
3. **MEDA A3 anchor fired** (CDP HEAD frozen pin at `e2f3d86`) on the same
   advance — the A1 tripwire class on the satellite row; admitted under
   the R2-37-shape ancestry gate (asserted, not assumed). MEDA PIN-CHAIN
   re-pin queued, next maintenance round.

## §2 Artifact custody (all instrument-hashed at emission)

| Artifact | Bytes | SHA-256 |
|---|---|---|
| `paper-2-v1.6.pdf` | 927,068 (27 pp, A4) | `0ef9ee40587dcf50a8732dae884835430481879c72b18f1021b5ad5821d308a3` |
| `paper-2-v1.6-source.tar.gz` | incl. sections, emitter v1.6, gate scripts, allowlist, verification-data | `99913db3f8ed8a1b85cc1e502226014345966bd3c23e6a106df3c30689f51a5c` |
| `paper-2-v1.5reconstruct-to-v1.6.changes` | changes manifest, per-ID | `778f9ac2d8fd62dc874b00347b1fabaa236e8f8402fedccbc05bc0953c22090c` |
| `verification-data.tex` (emitted) | 15 anchor macros + layer counts | `7fc0314de4767519aafce7e12a8e90387760859e3f7681fdfba45c9ca12f7071` |
| `gate-d-allowlist-v1.json` | 8 SHA-256-keyed entries | `72c834ad5250bde597028b97a78b8ae911fc4f0ca9cf6d12950d5d7ca30ed563` |
| `emitter-build-log.txt` | full fail-closed run log | `3b5e6e98cb772503deed39e80bb74e37c2439db121fe77a24401c48d89718b2e` |
| `SHA256SUMS` (sidecar set) | — | covers all of the above |

Location: `download/paper-2-v1.6-build/` + `download/paper-2-round5.6-build-receipt/`
(witness VM). All six artifacts cross in-band on request; the PDF (927 KB)
exceeds practical in-band size — per the Task-43 channel model the receipt
+ hashes are the verification legs, transport of the binary is an explicit
operator decision (same class as the v1.5 tar/changes deferral).

## §3 Executed fix ledger (R2-16..R2-54; full per-ID detail in the changes manifest `778f9ac2…`)

- **Battery dispositions**: A-1 (Table 5 pre-rename literal rows, asserted
  pre-loop), A-2 (tag^{commit} ancestry asserted; signature region scoped),
  A-3 (immutable-PIN parameterization + ancestry gate), B-1 (Algorithm 1
  walk EXECUTES via GATE-D), B-2 (Householder/oblique nomenclature; sup_T
  scoped; multi-layer + MesaNet CG divergence stated), B-3 (AST comparison
  stays demoted), B-4 (Table 3 cells ✓→∼, D4 separation in caption), B-5
  (n=1 operational-only clause), C-1 (Row 6 post-commit invariance; Row 7
  capture-fidelity demoted; §4.3 self-check → mechanical/external split),
  D-1 (overflow class fixed; see §4 GATE-A catch), D-2 (v1.5-reconstruct
  relabel; Figure 2 "Anchor chain (A1–A13)" re-rendered; authorized-retired
  closes the historical manifest), E-1 (scoped wording + L2/L4 debt
  statement), E-2 (model-agnostic boundary, §1/§6.4), E-3 (DAG log
  emitted; bit-exact replay qualified), Row 9 mandate (row 6 "reasoned"
  struck; row 9 expanded + closure condition named).
- **R2-36..R2-46**: L3 repo attribution; R2-37 ancestry gate; R2-38
  satellite pins; R2-39 GATE-A supersedes; R2-40 two-parameter bound;
  R2-42 scoping; R2-43/48/51 canonical L0 gate + `sha256sum --` fallback;
  R2-45 reduction chain; R2-46 pin act (CDP 48/48).
- **R2-47..R2-54**: GATE-A bounds (constants re-derived and printed) +
  R2-54 expanded-box parity leg; GATE-C fixed awk; R2-49 satellite
  contract; R2-50/52/53 GATE-D pair walk, SHA-256-keyed allowlist,
  §4.1/§5 prose qualified with D8-emitted walk numbers.
- **Spec-provenance disclosure**: the R2-36..R2-46 §4/§5 build-order prose
  of the original counters was reconstructed from the pinned Round-5.3
  receipt rulings (catch 1). Any drift between the executed fix set and
  the original spec is exactly what the post-build verification round
  adjudicates; the per-ID mapping above is the diff surface.

## §4 Gate outputs (build-time, fail-closed)

- **GATE-A (R2-47+R2-54): PASS, 27/27 pages.** Leg 1 bounds: X_BOUND
  540.01 (= 595.28 − 70.87 + 15.6 protrusion tol; clean-page observed max
  526.91), Y_BOUND 804.02 (= 841.89 − 70.87 + 33 folio; observed max
  803.03) — derivation printed in the log per refinement (iv). Leg 2
  parity: expanded-`[-500,-500,1500,2000]` same-binary `pdftotext
  -bbox-layout` comparison, 0 multiset diffs on every page (pypdf wrote
  the temp copy only; pypdf tokens never compared to poppler tokens).
  **The gate caught two real overflows in the first v1.6 compile** —
  Table 4 (53 pre-clipped words, p18) and the new hide-analysis table
  (p23, yMax 831.85 > 804.02) — both fixed by the R2-29 longtable
  mechanism and re-verified green. The reviewer's instrument demonstrably
  polices its own builder.
- **GATE-B (R2-37+R2-49): PASS.** GWM head `b481d75` == origin/main;
  CDP anchored at pinned `e2f3d86` (tar `4109426b…`, 5,150,720 B); MEDA
  `ec40e2fb` == origin (tar `a526238e…`, 4,372,480 B); GWM tar
  `e6ca764d…` (11,653,120 B); empty-stream sentinel absent everywhere;
  all rc-checked, in-process hashlib.
- **GATE-C (R2-48.2 fixed form): PASS** — `L5 OK 6/6 strictly monotonic`
  (422.68 → 871.39 → 1057.10 → 1570.18 → 1939.51 → 2474.62 pts), exit 0;
  bad-flag + guarded-END awk, printed in Appendix A.
- **GATE-D (R2-50+R2-53): PASS** — 25 commits, 44 unique (path, SHA-256)
  pairs: 20 preserved, 1 translated, 15 authorized-retired (rename-aware
  manifest invariant), **8 allowlisted pre-convention pairs** (SHA-256
  content digests; git SHA-1 blob-oids recorded as substrate-internal
  per D3), **0 unresolved**. Allowlist: `gate-d-allowlist-v1.json`
  (`72c834ad…`), witness-proposed classes per round5.4 §2/T8 rows 1–8,
  **operator adjudication presented herewith** (rides to build time per
  Task-46 QUEUE item 5; adjudication touches no pin or manifest byte).
  The two historical manifest states resolve through exactly one foreign
  digest each — `59f484e0…`, the superseded session-004 capture — the
  rename-aware refinement closing exactly as specified.
- **L0 (R2-51 canonical Python gate): PASS 8/8**, recomputed fresh at
  build (F003-capture-001..006 + api-probe + composer byte-invariance).

## §5 Emitted anchors (Table 5 of record, 15 rows; `verification-data.tex` `7fc0314d…`)

Layers: L0 8/8 · L1 10/10 · L3-CDP 10/10 · L3-GWM 20/20 · L5 monotonic
6/6 · CDP-ROOT 47/47 (at pinned `e2f3d86`) · GWM sessions 20/20 · MEDA
29/29 · pinchain 11 OK + A1/A3 admitted by ancestry gates + 13 anchors.
Literal anchors (SHA-256 unless noted): GWM session manifest `5c27b2cd…`;
CDP root manifest `a44018d2…`; MEDA manifest `38a24364…`; GWM tree
`0a44fbea…` (SHA-1, substrate-internal); GWM head `b481d750…` (SHA-1);
GWM tar `e6ca764d…`; tag fingerprint `888EAEEF…C7549`; bundle
`9e29982d…` (9,008,738 B); pre-rename manifest `5fce9669…`; pre-rename
tar `3717b21c…` (tree `db7fbd9b…` SHA-1); CDP head `e2f3d865…` (SHA-1);
CDP tar `4109426b…`; MEDA head `ec40e2fb…` (SHA-1); MEDA tar `a526238e…`;
DAG log `a4344269…` (277 rows, pinned reduction order, E-3). All ten
64-hex digests extract byte-complete from the printed PDF (R2-30
property verified by extraction).

## §6 Substrate acts (this boundary, witness-authored; operator applies)

1. **CDP `6facbf17a8dcf5dad1bdd441b328760b8b49779f`** (+230/−2, one atomic
   commit): R2-46 pin act (`1-equals-1_official-articulation_v1.0.md`,
   `63ea783d…`, root manifest 47→48) + manifest reconciliation of the
   `e96624d` drift (DECISIONS-INDEX digest refresh) + PIN-CHAIN-RECOMPUTATION
   R2-46 section. Post-push: CDP HEAD == origin/main == `6facbf1`; the
   46/47 defect clears; next build re-emits CDP anchors at the tip.
2. **GWM Task-47 boards commit** (this receipt pin + Round-5.5 receipt pin
   + working-notes updates) — head reported by THE CALL.
3. **Bundles**: `cdp-task47-e96624d-6facbf1.bundle` and
   `gwm-task47-b481d75-<head>.bundle` + `.b64` twins, fail-closed apply
   chains in THE CALL.

## §7 Residual register (post-build)

- R2-52 adjudication: presented (§4 GATE-D), awaiting the operator's
  one-line confirmation or amendment — the only open adjudication in the
  ledger.
- `round5.2-counters-v1.md` bytes: operator-side/Argon-custody only
  (`def5d3b1…`); non-blocking (§1).
- MEDA A3 re-pin: queued, next maintenance round.
- CDP tip reconciliation: rides THE CALL (§6.1).
- tar/changes/lineage transport decision (v1.6 set): now includes the PDF;
  operator decides (no clock).
- PROD_PATH pin + §8 envelope ruling: still pending-principal (unchanged).

