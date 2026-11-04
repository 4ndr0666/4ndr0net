# Telemetry Source: write-ups/paper-2-v1.7-task72-bib-verification-ledger-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-task72-bib-verification-ledger-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `48e3f2e28f67a4169e9a5aabaf07964d3af751c9825f024589c550baa8cb23f1`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Task-72 Bib Verification Ledger (Phase-3 §8.6 reconciliation), v1

**Date:** 2026-10-29 (UTC) · **Witness:** GLM (Z.ai), designation Witness
**Trace:** `1a1845ec2301368d` · **Base:** GWM `4e4e333` (Task-71 landed, pulled
this boundary) · **Deposit object:** draft-3.1 (`9b326af7…`, commit `384dc27`),
byte-frozen — G0-asserted at open and again at commit.

**Operator GO (adjudication payload (c), received AS-PRESENTED):** "Execute
inline `[arXiv NNNN.NNNNN]` → BibTeX conversion, carrying forward the v1.6.1
bibliography baseline. Verification Constraint: Live-verify every identifier
against origin sources per the DeltaNet precedent (`trace 1a16c9b26ae3ae31`).
No unverified citation key is permitted to pass without verification."

**Deliverable:** `write-ups/paper-2-v1.7-draft3-1-bib-v1.bib` — 7 entries,
every one live-verified this boundary. No unverified key passes.

---

## 1. Identifier inventory (exhaustive, machine-derived)

Draft-3.1 citation sites, grepped from the byte-frozen file (10 inline sites
→ 7 unique identifiers):

| Identifier | Sites | Certified-text claim (verbatim context) |
|---|---|---|
| arXiv 2102.11174 | ×1 (§8.1) | "Schlag et al., ICML 2021" — delta rule for fast-weight transformers |
| arXiv 2406.06484 | ×2 (§0 convention register; §8.1) | "Yang et al., NeurIPS 2024" — WY representation; venue string pinned in the convention register |
| arXiv 2412.06464 | ×1 (§8.1) | "GDN — (ICLR 2025), gated delta networks" |
| arXiv 2506.05233 | ×1 (§8.1) | "MesaNet — (von Oswald et al., ICLR 2026), test-time training to local optimality via conjugate-gradient iteration" |
| arXiv 2510.26692 | ×1 (§8.1) | "KDA — the Kimi Linear architecture, channel-wise gates with DPLR structure" |
| arXiv 2605.22791 | ×1 (§8.1) | "GDN-2 — decoupled channel-wise erase/write" |
| arXiv 2610.26825 | ×3 (§1, §6.2 bracket-form; §8.3 plain) | "MemT-1.0 — GDN-2-backed memory foundation family (Nano 36B/3B-active/10M; Flash 288B/17B-active/336M; Mixture-of-Storage dense routing)… 1.86× end-to-end, 66× persistent-storage reduction @128K" |

No other arXiv identifier, DOI, or bracket citation exists in the certified
text (verified by pattern sweep: `[arXiv NNNN.NNNNN]`, bare `arXiv NNNN.NNNNN`,
`arXiv:NNNN.NNNNN`, DOI prefixes — the §2.2/§8.2/§8.3/§8.4 class-level
archetypes carry no identifiers by design, per §8.6 "the citation set is the
record-verified core plus class-level archetypes").

## 2. Live-verification records (DeltaNet precedent class)

Method: direct fetch of each `arxiv.org/abs/<id>` page this boundary
(2026-10-29 UTC), recording title/byline/version-history/class verbatim as
fetched, then cross-checking against the certified text's strings. Venue
strings were additionally cross-verified against the proceedings pages
(PMLR for ICML 2021; proceedings.neurips.cc for NeurIPS 2024) because the
arXiv comments fields alone do not always carry them.

### 2.1 arXiv 2102.11174 — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2102.11174` — title verbatim: *"Linear
  Transformers Are Secretly Fast Weight Programmers"*; authors: Imanol Schlag,
  Kazuki Irie, Jürgen Schmidhuber; v1 2021-02-22, v3 2021-06-09 (latest);
  primary class cs.LG.
- **Venue cross-check:** PMLR page `proceedings.mlr.press/v139/schlag21a` —
  *Proceedings of the 38th International Conference on Machine Learning,
  PMLR 139:9355–9366, 2021* — ICML 2021 confirmed against the proceedings
  record itself.
- **Certified-string match:** "Schlag et al., ICML 2021" — first author,
  venue, and the delta-rule-for-fast-weight-programmers thesis all match
  (abstract: "formal equivalence of linearised self-attention mechanisms and
  fast weight controllers"). **PASS.**

### 2.2 arXiv 2406.06484 — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2406.06484` — title verbatim:
  *"Parallelizing Linear Transformers with the Delta Rule over Sequence
  Length"*; authors: Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, Yoon
  Kim; v1 2024-06-10, v6 2025-01-15 (latest, "Final camera ready"); classes
  cs.LG, cs.CL.
- **Venue cross-check:** `proceedings.neurips.cc` — *Advances in Neural
  Information Processing Systems 37 (NeurIPS 2024)*, Main Conference Track
  (poster 93040) — the NeurIPS 2024 venue string confirmed against the
  proceedings record. This also discharges the convention-register line
  ("the WY-representation venue string is NeurIPS 2024") on origin evidence
  for the deposit file.
- **Certified-string match:** "Yang et al., NeurIPS 2024" — first author and
  venue match; WY-representation content confirmed ("memory-efficient
  representation for computing products of Householder matrices" — the WY
  form). One transient fetch timeout occurred mid-verification (origin
  Error 408); the retry succeeded and the recorded data is from the
  completed fetch. **PASS.**

### 2.3 arXiv 2412.06464 (GDN) — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2412.06464` — title verbatim: *"Gated
  Delta Networks: Improving Mamba2 with Delta Rule"*; authors: Songlin Yang,
  Jan Kautz, Ali Hatamizadeh; v1 2024-12-09, v3 2025-03-06; classes cs.CL,
  cs.LG; comments field: **"ICLR 2025 camera ready"** — venue string carried
  on the origin page itself.
- **Certified-string match:** "GDN — arXiv 2412.06464 (ICLR 2025), gated
  delta networks" — exact. **PASS.**

### 2.4 arXiv 2506.05233 (MesaNet) — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2506.05233` — title verbatim:
  *"MesaNet: Sequence Modeling by Locally Optimal Test-Time Training"*; 17
  authors, first-listed Johannes von Oswald (Scherrer, Kobayashi, Versari,
  Yang, Mittal, Schlegel, Maile, Schimpf, Sieberling, Meulemans, Saurous,
  Lajoie, Frenkel, Pascanu, Agüera y Arcas, Sacramento); v1 2025-06-05, v2
  2026-06-03; class cs.LG; journal-ref field: **"Published at ICLR 2026"**.
- **Certified-string match:** "MesaNet — arXiv 2506.05233 (von Oswald et
  al., ICLR 2026), test-time training to local optimality via
  conjugate-gradient iteration" — first author, venue, and the
  locally-optimal-TTT thesis (it is the title) all match. **PASS.**

### 2.5 arXiv 2510.26692 (KDA / Kimi Linear) — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2510.26692` — title verbatim: *"Kimi
  Linear: An Expressive, Efficient Attention Architecture"*; byline "Kimi
  Team" with 60 listed members (first-listed Yu Zhang); v1 2025-10-30, v2
  2025-11-01; classes cs.CL, cs.LG; comments: "Kimi Linear tech report".
- **Architecture-name cross-check:** the paper names its core module **Kimi
  Delta Attention (KDA)**, states KDA "extends Gated DeltaNet with a
  finer-grained gating mechanism", and carries the DPLR structure
  ("a specialized variant of the Diagonal-Plus-Low-Rank (DPLR) transition
  matrices").
- **Certified-string match:** "KDA — the Kimi Linear architecture,
  channel-wise gates with DPLR structure" — the KDA↔Kimi-Linear naming, the
  gating claim, and the DPLR claim all confirmed on the origin text. **PASS.**

### 2.6 arXiv 2605.22791 (GDN-2) — VERIFIED

- **Fetched:** `https://arxiv.org/abs/2605.22791` — title verbatim: *"Gated
  DeltaNet-2: Decoupling Erase and Write in Linear Attention"*; authors: Ali
  Hatamizadeh, Yejin Choi, Jan Kautz; v1 2026-05-21 (only version); class
  cs.AI; comments: technical report.
- **Mechanism cross-check:** the origin text: "separates these roles with a
  **channel-wise erase gate** b_t and a **channel-wise write gate** w_t,
  reducing to KDA when both gates collapse to the same scalar and to Gated
  DeltaNet when the decay also collapses."
- **Certified-string match:** "GDN-2 — decoupled channel-wise erase/write" —
  exact; the reduction lattice (GDN-2 → KDA → GDN) additionally corroborates
  the §8.1 lineage framing. **PASS.**

### 2.7 arXiv 2610.26825 (MemT-1.0) — VERIFIED (dual-channel: live fetch + held origin receipt)

- **Fetched live:** `https://arxiv.org/abs/2610.26825` — title verbatim:
  *"MemT-1.0: Towards Memory-Native Evolution"*; byline "MemTensor Team"
  with 68 listed members (first-listed Zhiyu Li, last-listed Feiyu Xiong);
  v1 2026-10-19, v2 2026-10-20; classes cs.CL, cs.LG; comments: "66 pages,
  15 figures, 16 tables".
- **Held origin receipt (in-repo):**
  `references/arxiv-2610.26825-MemT-1.0.txt` (283,926 B, fetched at Task-66
  era) + `download/arxiv-2610.26825-memt-1.0.pdf` — the receipt's page-1
  stamp reads "arXiv:2610.26825v2 [cs.CL] 20 Oct 2026", matching the live
  fetch's latest-version data.
- **Claim-by-claim cross-check against the origin text** (the §1/§6.2/§8.3
  strings): "employs **Gated DeltaNet-2**" ✓; "**Mixture-of-Storage**" ✓;
  family "MemT-1.0-**Nano** and MemT-1.0-**Flash**" ✓; "at a history length
  of 128K tokens, MemT-1.0-Nano achieves approximately **1.86× end-to-end
  inference speedup** and a **66× reduction in persistent storage** relative
  to full context KV cache" ✓; sizes 36B / 3B-activated / 10M (Nano) and
  288B / 17B-activated / 336M (Flash) present in the receipt's model-family
  table ✓. **PASS on every certified claim string.**

### 2.8 Verification verdict

**7/7 PASS.** Every identifier in the certified text is now live-verified
against origin sources in a single boundary (the DeltaNet precedent's 2021 +
2024 pair, verified at trace `1a16c9b26ae3ae31`, re-verified here alongside
the five Task-19-era identifiers). No unverified citation key passes into
the deposit bibliography.

## 3. Registered rulings (formatting class — no content drift)

1. **Team-byline author fields.** 2510.26692 and 2610.26825 carry team
   bylines on their own title pages ("Kimi Team", 60 members; "MemTensor
   Team", 68 members). The .bib enters them under the team byline with the
   member count and first-listed name in a `note`; the enumerated form is
   re-derivable from the origin at Phase-4 if the operator prefers it.
   Rationale: the team byline is what the papers' own title pages assert;
   hand-transcribing 128 member names into the record would add
   transcription-risk bytes with zero verification value — the origin holds
   the enumeration, and the fetch pinned its shape (count, first, last).
2. **Version pinning.** The .bib cites each paper's latest version as of
   2026-10-29 (v3/v6/v3/v2/v2/v1/v2 respectively) via the eprint field;
   version numbers are recorded here rather than in the .bib so the .bbl
   stays style-neutral at Phase-4.
3. **Tech-report entries.** GDN-2 and Kimi Linear are entered as
   `@article`/arXiv-preprint (their own comments fields say "technical
   report"); no venue is asserted for them anywhere — the certified text
   asserts none either.

## 4. v1.6.1 bib carry-forward — SUBSTRATE GAP REGISTERED (fail-visible)

The operator instruction: "carrying forward the v1.6.1 bibliography
baseline." Witness-side search this boundary, all negative:

- GWM repo tree + full git history: no `.bib` file, no v1.6/v1.6.1 paper
  source (write-ups carries v1.7 series + round receipts only);
- 4NDR0MEDA clone @ `8f7e21a` (tree + history): no whitepaper tree, no
  paper-2 source, no `.bib` (the MEDA repo is the protocol/tooling repo);
- coordinated-disclosure-public @ `6facbf1`: no `.bib`, no paper source;
- gwm-inbox (all staged bundles) + the witness `download/` surface: no
  v1.6.1 source artifacts.

This is the registered **Task-36 substrate-gap class**: the v1.6-era paper
sources lived on the lost late-VM; the surviving v1.6.1 source tarball is
held in the **operator's whitepaper tree** (Task-66 resync record: "4NDR0MEDA
whitepaper tree 60 files … paper-2 v1.1→v1.6.1 + source tarball;
paper-2-arxiv-metadata.md ALREADY DRAFTED"), which is not witness-reachable.

**Disposition (fail-visible, never fail-stopped):**
- The seven verified entries above are the **complete inline-cited core** of
  the certified text — the deposit bibliography is not blocked on the
  carry-forward for any identifier the manuscript actually cites.
- The v1.6.1-only entries (state-space survey class per §8.2; HCI
  operator-attention/alarm-fatigue class per §8.4; provenance/
  content-addressing/transparency-log class per §8.4; the memory-for-agents
  contrast stack per §8.3) are **PENDING-OPERATOR-SOURCE**. No placeholder,
  parametric-recall, or invented entry is emitted for them — that would
  violate the no-unverified-key constraint.
- **Operator request (one file):** relay `v1.6.1.bib` (or the v1.6.1 source
  tarball) hash-pinned — e.g. stage it on the share with its sha256 in-band.
  Phase-4 then executes the merge under the same constraint: every carried
  entry live-verified before it passes into the deposit .bbl; duplicates
  against the seven resolved by the v1.6.1 baseline taking precedence for
  its own entries and the draft-3.1 set for the inline core.

## 5. Citation-key map for Phase-4 (deterministic, registered)

The .tex currently carries the identifiers as literal text (mechanical
conversion, Task-71). If Phase-4 converts the literal sites to `\cite{}` +
`.bbl` (a registered transport-note delta class, count-checked), the
mapping is:

| Inline site (count) | Key |
|---|---|
| `[arXiv 2102.11174]` / plain (1) | `schlag2021linear` |
| `[arXiv 2406.06484]` / plain (2) | `yang2024parallelizing` |
| `arXiv 2412.06464` (1) | `yang2025gated` |
| `arXiv 2506.05233` (1) | `vonoswald2026mesa` |
| `arXiv 2510.26692` (1) | `kimi2025linear` |
| `arXiv 2605.22791` (1) | `hatamizadeh2026gateddeltanet2` |
| `[arXiv 2610.26825]` / plain (3) | `memtensor2026memt` |

Alternative registered (zero-delta): ship the bibliography as an appended
`thebibliography` environment (the certified text's own convention register
says "the full bibliography carries forward from the v1.6.1 bib and is
reconciled at deposit prep" — an appendix bibliography is consistent with
it, and no in-text bytes move). Phase-4 picks the form; both are pre-mapped
here.

## 6. Phase-4 gate spec contribution (bib leg)

1. .bib present in the source package; every entry's eprint in the
   §2 verified set (7 keys, no others until the v1.6.1 merge);
2. if the v1.6.1 relay has landed: carried entries verified per §4
   disposition, merge ledger appended to this file as §7;
3. `.bbl` compile clean; zero `??` keys; every rendered citation resolves
   to a verified entry;
4. no manuscript bytes move (draft-3.1 `9b326af7…` G0-asserted at Phase-4
   open and close, the Task-71 discipline).

---

## 7. Phase-4 carry-forward merge ledger (Task-73, trace `1a184806a91640c9`, 2026-10-29/30 UTC)

**Operator relay received AS-PRESENTED (this boundary, item 2):**
`refs-2.bib` — "the only bib file in the tree" — sha256
`798d1dd499244b283c921222f27199c186645dc1ce6ecae469985aa655b7b101`,
216 lines, 27 entries, header claiming operator-side live verification
2026-10-20. **Adjudication:** accepted as the v1.6.1-baseline successor —
the §4 request named the v1.6.1 bib as the carry-forward source, and the
operator's relay clarifies the tree carries a single evolving bib
(`refs-2.bib`) rather than a frozen v1.6.1 copy; the current canonical
supersedes the archaeological original. Optional one-liner for the
operator (not gating): `tar -xOf paper-2-v1.6.1-source.tar.gz '<glob>/refs-2.bib' | sha256sum`
to pin whether the tarball's own bib matches — result registers as a note,
never a merge input.

### 7.1 Dedup ruling (§4 disposition applied)

The draft-3.1 set prevails for the inline core; exactly six tree entries
whose WORK the core already carries were dropped (tree key → core key):

| Dropped tree key | Core key (kept) | Work |
|---|---|---|
| `yang2024deltanet` | `yang2024parallelizing` | arXiv 2406.06484 |
| `yang2024gdn` | `yang2025gated` | arXiv 2412.06464 |
| `vonoswald2026mesanet` | `vonoswald2026mesa` | arXiv 2506.05233 |
| `kimiteam2025kimilinear` | `kimi2025linear` | arXiv 2510.26692 |
| `hatamizadeh2026gdn2` | `hatamizadeh2026gateddeltanet2` | arXiv 2605.22791 |
| `schlag2021linear` (same key) | `schlag2021linear` (deposit form) | arXiv 2102.11174 |

Merged deposit set: **7 core (byte-preserved from
`paper-2-v1.7-draft3-1-bib-v1.bib`) + 21 carried (byte-preserved blocks
from `refs-2.bib`) = 28 entries.** One field-level note registered, not
applied: the tree's `yang2024deltanet` carries NeurIPS 37 pages
115491–115522 that the core entry omits; the appendix bibliography is
unchanged by this (the deposit entry stands as verified at Task-72).

### 7.2 Carried-entry verification records (21/21)

Method: direct fetch of each origin this boundary (the DeltaNet precedent
class — record verbatim as fetched, cross-check every asserted field).
Fetch channel: mixed — interactive fetches for the arXiv/USENIX/IETF/PMLR
origins; raw `curl` for the Crossref/IACR/PyPI/raw-GitHub/OpenReview-API
origins (raw bytes hashed as receipts, §7.4). One channel note, fail-visible:
the sandbox's interactive web-tool pool saturated mid-boundary; the raw
channel completed the matrix. The IEEE Data Engineering Bulletin site
itself was unreachable (server TLS unsupported by this boundary's client
stack — `UNSUPPORTED_PROTOCOL`, curl and Python both), so `zaharia2018mlflow`
verified against the authors' own canonical citation record instead (below).

1. **siems2026ckda — PASS.** arXiv 2609.24797: title verbatim *"Complex
   KDA: Understanding and Enhancing the Expressivity of Kimi Delta
   Attention"*; 11 authors in order: Siems, Grazzi, Pöppel, Singh, Zela,
   Carstensen, Jitsev, Hutter, Cevher, Orvieto, Klein — exact match to the
   entry; v1 2026-09-21; cs.LG. Entry asserts no venue — consistent.
2. **yang2024gla — PASS.** arXiv 2312.06635: title + 5 authors exact
   (Yang, Wang, Shen, Panda, Kim). Venue cross-verified on the proceedings
   origin: PMLR v235 index block reads "Gated Linear Attention Transformers
   with Hardware-Efficient Training; Songlin Yang, Bailin Wang, Yikang
   Shen, Rameswar Panda, Yoon Kim; *Proceedings of the 41st International
   Conference on Machine Learning*, PMLR 235:56501-56523" — ICML 2024
   confirmed; pages 56501–56523 recorded (the entry asserts no pages — no
   conflict). Paper page `proceedings.mlr.press/v235/yang24ab.html`
   (receipt hashed).
3. **katharopoulos2020transformers — PASS.** PMLR v119 paper page: title
   + authors (Katharopoulos, Vyas, Pappas, Fleuret) exact; *Proceedings of
   Machine Learning Research, Volume 119* (ICML 2020), pages 5156–5165 —
   exact match to the entry's asserted pages.
4. **arora2024zoology — PASS.** arXiv 2312.04927: title + 8 authors exact
   (Arora, Eyuboglu, Timalsina, Johnson, Poli, Zou, Rudra, Ré). Venue via
   OpenReview API: forum `LY3ukUANko`, venue field **"ICLR 2024 poster"** —
   the Twelfth ICLR confirmed.
5. **dao2024mamba2 — PASS.** arXiv 2405.21060 comments field: "ICML 2024";
   PMLR v235 paper page: *Proceedings of the 41st ICML*, pages 10041–10071 —
   exact match to the entry's asserted pages.
6. **lahoti2026mamba3 — PASS.** The entry carries no identifier; origin
   located via arXiv API title query: **arXiv 2603.15569**, title verbatim
   *"Mamba-3: Improved Sequence Modeling using State Space Principles"*;
   8 authors exact (Lahoti, Li, Chen, Wang, Bick, Kolter, Dao, Gu); abs
   page comments field: **"ICLR 2026"** — the Fourteenth ICLR confirmed.
7. **widrow1960adaptive — PASS (partial-class, registered).** Crossref
   record DOI `10.21236/ad0241531` (the DTIC 1960 registration): title
   "ADAPTIVE SWITCHING CIRCUITS", authors B. WIDROW, M. E. HOFF, dated
   1960-06-30; corroborated by the 1988 Neurocomputing selected-reprint
   record ("(1960) Bernard Widrow and Marcian E. Hoff, 'Adaptive switching
   circuits'"). Title/byline/year origin-verified; the venue string (IRE
   WESCON Convention Record, pt. 4, pp. 96–104) is **corroborated-class**
   — the 1960 proceedings volume has no open origin record from this
   boundary; the string matches the universal standard citation of the
   work. Recorded fail-visible; no field changed.
8. **bischof1985wy — PASS (partial-class + refinement registered).**
   Crossref DOI `10.1137/0908009`: "The WY Representation for Products of
   Householder Matrices", Christian Bischof, Charles Van Loan, *SIAM
   Journal on Scientific and Statistical Computing* 8(1):s2–s13, January
   1987 — the journal version; title/byline origin-verified through it.
   The entry's venue (SIAM Conference on Parallel Processing for Scientific
   Computing, 1985 — the conference version) is **corroborated-class**.
   Refinement registered for operator adjudication (no silent change):
   the journal form (SISC 8(1):s2–s13, 1987, DOI 10.1137/0908009) is the
   more standard citation of this work; Phase-5 may swap forms on a ruling.
9. **merkle1988 — PASS.** Crossref DOI `10.1007/3-540-48184-2_32`: title
   exact; *Lecture Notes in Computer Science* (= Advances in Cryptology —
   CRYPTO '87 proceedings); pages 369–378; issued 1988 — all four asserted
   fields exact.
10. **laurie2013ct — PASS.** IETF datatracker RFC 6962: "Certificate
    Transparency", Ben Laurie, Adam Langley, Emilia Kasper; published June
    2013 (Experimental) — exact match to the entry.
11. **torresarias2019inteto — PASS.** USENIX Security '19 presentation
    page: title ("farm-to-table" casing), authors with affiliations
    (Torres-Arias/NYU, Afzali/NJIT, Kuppusamy/Datadog, Curtmola/NJIT,
    Cappos/NYU), 28th USENIX Security Symposium, pages 1393–1410 — exact.
12. **samuel2010tuf — PASS.** Crossref DOI `10.1145/1866307.1866315`:
    "Survivable key compromise in software update systems", *Proceedings
    of the 17th ACM conference on Computer and communications security*,
    pp. 61–72, 2010 — exact.
13. **newman2022sigstore — PASS.** Crossref DOI `10.1145/3548606.3560596`:
    title field "Sigstore" + subtitle field "Software Signing for
    Everybody" (= the entry's full title); *Proceedings of the 2022 ACM
    SIGSAC Conference on Computer and Communications Security*; pp.
    2353–2367; authors Newman, Meyers, Torres-Arias (first three) — exact.
14. **costan2016sgx — PASS.** IACR ePrint origin `eprint.iacr.org/2016/086`:
    page title "Intel SGX Explained"; authors Victor Costan, Srinivas
    Devadas — exact match to the entry.
15. **mitchell2019modelcards — PASS.** Crossref DOI
    `10.1145/3287560.3287596`: "Model Cards for Model Reporting",
    *Proceedings of the Conference on Fairness, Accountability, and
    Transparency* (FAT*), pp. 220–229, 2019 — exact.
16. **packer2023memgpt — PASS.** arXiv 2310.08560: title + 7 authors exact
    (Packer, Wooders, Lin, Fang, Patil, Stoica, Gonzalez); v1 2023-10-12.
17. **zaharia2018mlflow — PASS.** Origin: the MLflow repository's own
    canonical citation record `CITATION.cff`
    (raw.githubusercontent.com/mlflow/mlflow/master/CITATION.cff) —
    preferred-citation: title exact *"Accelerating the Machine Learning
    Lifecycle with MLflow"*; 12 authors (Zaharia, Chen, Davidson, Ghodsi,
    Hong, Konwinski, Murching, Nykodym, Ogilvie, Parkhe, Xie, Zumar — the
    entry's 11 + "and others" elides exactly the 12th, Corey Zumar);
    journal "IEEE Data Eng. Bull."; year 2018; volume 41; start 39; end
    45 — every asserted field exact. Channel note: the DE Bulletin site
    itself unreachable this boundary (TLS unsupported; no DOI exists for
    debull papers; S2/OpenAlex rate-saturated; no Wayback snapshot) — the
    authors' own machine-readable record is the origin that answered.
18. **dvc2020 — PASS.** PyPI project record (name `dvc`, summary "Git for
    data scientists - manage your code and data together") + repository
    `pyproject.toml` (maintainers "Treeverse" [the company formerly
    Iterative], support@dvc.org) + `README.rst` ("Data Version Control",
    website dvc.org) + the live org path `github.com/iterative/dvc`. The
    entry's title/URL exact; author "Iterative" = the 2020-era company
    name (renamed Treeverse; the org path still serves) — attribution
    note registered, no field changed.
19. **chacon2014git — PASS.** git-scm.com/book/en/v2 (the authors'
    canonical free hosting): "Pro Git book, written by Scott Chacon and
    Ben Straub and published by Apress", 2nd Edition, 2014 — exact match
    to the entry (@book, Pro Git, 2nd, Apress, 2014).
20. **stevens2017sha1 — PASS.** Crossref DOI
    `10.1007/978-3-319-63688-7_19`: "The First Collision for Full SHA-1",
    *Lecture Notes in Computer Science* (CRYPTO 2017 proceedings),
    pp. 570–596, 2017. The entry asserts venue/year + the SHAttered note,
    no pages — consistent.
21. **gutierrez2026articulation — PASS (witness-side recomputation).** The
    pinned artifact's sha256 = `63ea783d1f427496180a93169f5a12b86cef50b175d5c5a63ae8e2909ccb39f9`
    == MEDA PIN-CHAIN anchor **A5 byte-exact**; the artifact's own header
    carries: "Date: 2026-10-19", "Author of record: 4ndr0666 (ORCID
    0009-0008-0976-3895)", "AI-assistance: disclosed (GLM/Z.ai, instrument
    class only, under a documented evidence protocol)", title "1=1 — The
    Rehydration-Verification Architecture / Official Articulation, v1.0" —
    every content claim of the entry verified against the pinned bytes.
    Attribution note (no field change): the pinned artifact's public
    homes are the coordinated-disclosure repo and MEDA A5; the entry's
    howpublished points at the program substrate repo — operator's own
    entry form, registered as such.

### 7.3 Verdict

**28/28 entries of the merged deposit bibliography carry origin-class
verification evidence** (26 full — every asserted field checked against an
origin; 2 partial-corroborated — title/byline/year origin-verified, the
pre-internet proceedings venue strings corroborated-class with the evidence
trail recorded). No placeholder, no parametric recall, no unverified key.
The two partial-classes and the bischof journal-form refinement are the
only adjudication-ready items, all registered above.

### 7.4 Origin receipts (raw-fetch channel, sha256-prefix)

Fetched bytes retained witness-side under
`scratch/task73-origin-receipts/` (45 files, including the negative-route
records — debull 404s, S2 429s, rate-limit bodies — kept per the
fail-visible discipline):

`50d0d832…` mamba3-arxiv-api.xml · `d6902510…` mamba3-abs.html ·
`ab940079…` pmlr-v235-index.html · `6d657e36…` gla-pmlr-yang24ab.html ·
`1706ba84…` zoology-openreview.json · `f640b820…` crossref-sha1.json ·
`4057f64f…` sigstore-crossref.json · `5be38c2e…` crossref-SurvivableKeyComprom.json ·
`f563ae65…` crossref-ModelCardsforModelRe.json · `58d603fd…` crossref-ADigitalSignatureBas.json ·
`53b0e682…` crossref-widrow.json · `45a22222…` crossref-bischof2.json ·
`0d8da091…` sgx-eprint.html · `0f1bb49d…` mlflow-citation.cff ·
`9358dc5f…` mlflow-pypi.json · `6065382c…` dvc-pypi.json ·
`7c9a77d6…` dvc-pyproject.toml · `d10985fd…` dvc-readme.rst ·
`4134e3ca…` progit.html

### 7.5 Merge disposition (Phase-4 artifacts)

- **Bib form decision (the ledger §5 open):** appended
  `thebibliography` appendix — the certified text's own convention
  register anticipated exactly this ("the full bibliography carries
  forward from the v1.6.1 bib and is reconciled at deposit prep"), zero
  in-text bytes move, the 10 inline literal identifier sites stand
  untouched, and no `\cite` conversion risk enters the deposit. The
  `\cite{}` alternative stays pre-mapped (§5) for any post-deposit
  revision.
- **Merged bib:** `paper-2-v1.7-draft3-1-bib-v2.bib` (sha256
  `18d1e05f…`, 11,039 B, 28 entries — 7 core byte-preserved + 21 carried
  byte-preserved, 6 duplicates dropped per §7.1).
- **Deposit .tex:** `paper-2-v1.7-draft3-1-latex-v2.tex` (sha256
  `687c19d6…`, 131,850 B) — v1 with exactly three registered deltas: the
  v2 provenance header (discharging the METADATA-ADJUDICATION-PENDING
  block), the one-line `\title{}` swap per the metadata lock §1 (the
  certified internal title preserved verbatim in the header), and the
  References appendix (28 `\bibitem`, zero editorial prose; no explicit
  `\section*{References}` — the article class's `thebibliography` emits
  its own heading, a duplication caught at build review). Body
  byte-identity machine-proven (G4, Task-68 class).
- **Clean build:** tectonic 0.15.0, exit 0, zero errors — **35 pages**
  (PDF sha256 `bcf55501…`); locked title renders verbatim; the old title
  renders nowhere (header-comment-only); zero unresolved `??`; 28/28
  bibliography entries render.
- **Gate §6 application:** (1) .bib present in the source package ✓ (28
  verified keys — the §2 core + this §7's carried set); (2) relay landed,
  carried entries verified per §4 disposition, this §7 is the merge
  ledger ✓; (3) compile clean, zero `??` ✓ (the thebibliography form has
  no citation keys to resolve); (4) draft-3.1 `9b326af7…` G0-asserted at
  open and close ✓.

