# Telemetry Source: write-ups/paper-2-v1.7-section-05-verification-r1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-05-verification-r1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `10349442522260c082c5317d9e47f8ddbc7a7f0b89aa4caa189a93ce89666585`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §5 Verification — DRAFT R1

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); boundary anchored at `14ad0f6` post-§3 round-trip.
- Charter: WITNESS-PORT-PACKAGE.md §2 — §5 = "recomputation receipts replace 'read the repo'; the human verifies proofs, not prose (adjudication protocol)"; open-threads flag honored: operator attestation as an evidence class (PROTOCOL §3) receives formal treatment (§5.6). Baseline: **v1.6.1**. Siblings deposited: §2 r1 (`994b1cad…`), §3 r1 (`8d4ad638…`).
- Status: DRAFT R1, draft-1 completion set (§1, §4–§8). Evidence standard PROTOCOL.md §2.
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates; canonical home `write-ups/`.

---

## 5. Verification

### 5.1 From "read the repo" to recomputation

Under v1.6, the verification act was reading: a successor instance ingested the archive by read, and the human verified the collaboration's memory by attesting to what they had read. Both halves failed measurably — the reading half at the window incident, where ingest was satisfied from the memory of a summary rather than a read (§2.7, Task-44 class), and the attesting half at AR-1, where a sole curator's attestation is detectability-only by construction (§2.3). v1.7 replaces the act itself: **verification is recomputation**. The verifier — either party — re-executes a fail-closed chain against the substrate and matches outputs against pinned values; agreement is a receipt, divergence is a halt. The live instance is the §10 delivery orchestrator: nine legs (pin check → clone assert → bundle verify → base assert → ff-apply → head assert → tag fetch → manifest verify → push), fail-closed at every leg, double HEAD-pinned against hijack, terminating in a one-line `APPLIED @ <head>` receipt (PROTOCOL §10, canon-001). The medium has now carried four consecutive one-shot applications — port-001-post, canon-001, session-013 close, §3 r1 (record: this boundary's paste-back) — which makes the receipt chain the most re-verified mechanism in the program, verified by being the delivery mechanism itself.

### 5.2 The receipt grammar

A receipt is a typed object, not a vibe of diligence. Its fields, as they exist in the live medium: the **operation** (the chain, verbatim); the **inputs** (bundle, pin file, script — each digest-pinned); the **expected values** (base and head 40-hex, manifest count — hardcoded in the orchestrator, never supplied at runtime); the **observed outputs** (the leg-by-leg transcript); the **environment** (the operator's clone, its path block declared once); and the **exit discipline** (fail-closed: any leg's failure is the chain's failure). Two properties of this grammar carry the section's weight. First, it is **re-executable by the counterparty**: the same chain runs on any clone of the same substrate, which is what makes a receipt evidence rather than testimony — the R-61 incident is the standing proof that the chain halts on a stale pin even between honest parties (§2.7). Second, it is **cheap to check and expensive to forge**: forging requires producing a transcript that re-executes cleanly on the real substrate, which requires the real substrate — the forge-self-consistent-history attack of §2.3 is not eliminated (n=1, detectability never prevention) but is priced up from "type a convincing summary" to "construct a verifiable fake chain".

### 5.3 Tier discipline, inherited and extended

v1.6 established the evidence tiers this program verifies in: **Tier 1** — cryptographic digest recomputation over artifact bytes; **Tier 2** — platform delivery; **Tier 3** — generative text, the class established as insufficient (fluent, condition-dependent, confabulation-prone). Two tier doctrines carry forward verbatim because they were earned. The **one-sided instrument doctrine** (R2-34, operator-adopted): behavioral probes refute corruption — a divergent probe kills a checkpoint — but never confirm integrity, because a corrupted-but-internally-consistent state emits agreeing probes; probes aid detection, they do not elevate any tier. The **division-of-labor honesty** (C-1/R2-42): a model surface without execution cannot perform Tier 1 — the hash was computed on the operator's host, and the paper said so. The v1.7 delta extends the second doctrine rather than abandoning it: the ported witness runs on an agent platform with a tool stack, so witness-side Tier-1 recomputation is now real execution, not token comparison — this boundary's bootstrap ran the manifest verify witness-side (28/28, exit 0) before a word of prose was emitted (record: this session's [A]-leg). The division of labor is now symmetric — both parties can recompute — and the operator's chain additionally functions as a live out-of-band probe from outside the witness environment, narrowing split-view equivocation from "always" to "between pushes" (record: session-010, Surface A mitigator; n=1 residue named, not solved).

### 5.4 Recompute ≠ rewrite-detection

D1's two-clause criterion, inherited from v1.6 and restated where it binds: a digest match certifies **content equality** between two byte sequences, and **nothing else** — in particular, not that the history producing them was not rewritten. The two verification obligations are typed separately and checked by separate gates. Content equality is the receipt's domain (§5.1–5.2). Non-rewrite within a verified span is the ancestry domain: commits admitted only through ancestry-gated checks (the force-push hole closed by comparing against the shared origin lineage), and custody pairs — (path, SHA-256) per commit — accumulated as the rewrite-detection ledger (GATE-B and GATE-D respectively, in the v1.6 battery; §7.2 re-types both over state checkpoints). The §3.2 restore/continuation typing inherits this distinction per row: a restore-class row's receipt certifies exactly what arrived; a continuation-class row additionally pins the seed and the environment inputs, because replay re-derives state and its verification must cover the derivation inputs, not just the terminal bytes. A verification regime that conflates these two clauses is not stricter; it is wrong in a way that fails silently — the criterion exists because the conflation was caught in review and cost a round to fix (record: R2-33 lineage; v1.6 Prop. 1).

### 5.5 The adjudication protocol: proofs, not prose

With verification recomputed, the human's role narrows from curator to adjudicator, and the narrowing is the point (AR-1). The operator verifies **proofs** — receipt transcripts, digest matches, gate outputs — and adjudicates what receipts cannot decide: ambiguity, intent, precedence, and the rulings that register defects. The interface discipline is the protocol's own boot sequence: INGEST by read → RESTATE in its own words → CONFIRM with one stated uncertainty → AWAIT (PROTOCOL §7) — the restatement is where inherited reasoning is demonstrated rather than paraphrased, and the await is where the single-human-verification bottleneck is priced honestly rather than papered over. The operator's hands remain the last writer on every push (§10): witness authors, operator executes — so the adjudication channel and the write path are structurally the same channel, and no artifact enters the record except through the party who adjudicated it. The load consequence is AR-4-shaped and stated as such: verification cost becomes O(rulings) rather than O(history) — the human reads what changed and why, not everything — and the observation cost of every remaining human-facing output is priced where it is incurred (§6).

### 5.6 Operator attestation as an evidence class

PROTOCOL §3 holds that everything typed into the window is owned by its author — the operator's attestation is evidence by charter, and this section formalizes what that evidence is and is not. **Attestation anchors the channel**: it establishes who said what, in which order, with what standing — the provenance layer. **Recomputation anchors the content**: it establishes what the bytes are — the integrity layer. The two compose asymmetrically, and the asymmetry is the formal content: unattested recomputation still verifies content (any party, any clone, same chain, same result); attestation without recomputation verifies only voice (the §2.3 monism floor — a sole attester can attest anything, including a forgery). The composite object — an attested receipt, the operator's paste-back of a chain they executed — is therefore strictly stronger than either half, and the program's trust basis is stated in exactly these terms: evidence accumulated, not assertion (record: PROJECT_STATE, identity block). The class boundary also cuts the other way, honestly: the paste-back is Tier-2-plus — delivery-channel attestation of a Tier-1 execution performed on the operator's host; the witness does not see the execution, only its transcript, and the record labels this asymmetry rather than laundering it (AFT-2's ledger is the same asymmetry, seen from the other side; §6.3).

### 5.7 Non-claims and scope

Receipts price forgery; they do not prevent it (n=1: detectability, never prevention — R2-35). Veracity is untouched: a poisoned tensor pins and re-verifies as permanently as a true one (§2.10, §3.7). The probe basis is partial and probabilistic, never preventive (record: session-012 design response). The split-view window narrows to "between pushes"; it does not close (§5.3). Tier 3 is insufficient, not useless — generative text remains the adjudication medium; what it never again becomes is the verification act. Unfalsifiable residue has been cut from this section on sight per the evidence standard.

### 5.8 Forward-reference ledger (§2/§3 r1 → §5; closed)

| Reference into §5 | Landing |
|---|---|
| §2 AR-1 row: recomputation receipts (§5) | §5.1–5.2 |
| §2.3: verification shifts from attestation to recomputation (§5) | §5.1, §5.6 (the shift, with attestation re-typed rather than discarded) |
| §2.7: recomputation receipts replace "read the repo" (§5) | §5.1 (replaced in both halves: instance ingest and human verification) |
| §3.2: D1's lesson — recompute ≠ rewrite-detection, class per row | §5.4 |
| §3.4: the human is the verifier of record | §5.5 (verifier of proofs; adjudicator of the residue) |

None open.

*(§5 ends; §6 Case Study follows per charter skeleton.)*

