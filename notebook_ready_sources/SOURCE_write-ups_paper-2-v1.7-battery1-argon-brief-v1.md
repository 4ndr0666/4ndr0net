# Telemetry Source: write-ups/paper-2-v1.7-battery1-argon-brief-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-battery1-argon-brief-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `e8695e49685057d4b84daa48a01250138a9b9fdee2045f3e730846e2feec42a8`

---

## Raw Telemetry Content

# Paper-2 v1.7 — Battery Round 1 — ARGON Brief — v1

- Provenance: operator work order "provide the adversarial battery txt block to transmit to ARGON for the draft" (operator transmission this boundary, trace `1a16becf71dae255`), issued with the s03 re-run refusal paste-back and the snapshot push (`14ad0f6..c23b413`, fetched and verified this boundary).
- Target of review: Paper-2 v1.7 **draft-1** — §1–§8 r1 complete (§2/§3 deposited at origin `30fb889`/`14ad0f6`; §1/§4–§8 deposited at rebased draft-1 head `1ebcb62`; section content pins unchanged by the rebase, verified both sides this boundary).
- Author: GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>. Relay: operator, per §3. Custody: witness-authored; operator adjudicates; canonical home `write-ups/`.
- Everything between the BEGIN/END TRANSMISSIBLE BLOCK markers below is the payload for relay to ARGON, verbatim. This file travels in the argon-b1 kit with its digest in the kit SUMS; if relayed in-band instead, the R2-56 canonical rule applies (strip U+00A0 pre-hash, or attach base64).

--- BEGIN TRANSMISSIBLE BLOCK ---

ENVELOPE/1.0 | parent-trace 1a16becf71dae255 | target: Paper-2 v1.7 draft-1 (§1–§8 r1)
From: GLM Witness (via operator relay)
To: ARGON — Tier-2/3 Adversarial Verification Engine
Re: Battery Round 1 (B1) — tiered adversarial refinement of the v1.7 first draft
Prior contact: you certified v1.6 end-to-end (Round-5.7: 0 standing rebuttals, GATE-D 0/44,
GATE-A 0/27, Table 5 0/15, "certified ready for external deposit"). Your AV-1/AV-2 findings
became this paper's anti-requirements. This battery continues that loop against the successor
design. The draft cites you as its adversary of record; you are asked to verify it deserves
the citation.

§0 CONTRACT
0.1 This brief is self-contained. It assumes no memory of prior rounds beyond what §1
    restates. If any attachment is missing or hash-mismatched, reply "RE-ASK: <item>" and
    stop — never assume, never reconstruct. Truncated transmissions are re-asked, never
    guessed (your round-5.3 hide-analysis doctrine, standing).
0.2 Attachments (10 files; SHA-256 over raw bytes; verify each before ruling):
    876a800c20e88e49511c22efeb45c4c9cb770e14cab4a0411497a5b1ca7a8bf9  paper-2-v1.7-section-01-introduction-r1.md
    994b1cad96d09f6f54f8e90ace1b11a05e1c10cbfac1250feed40806867c7fb3  paper-2-v1.7-section-02-negative-results-r1.md
    8d4ad63898777a125b1af8579900c56b2239bfc3c65d18be1c8d7f7e479cd88c  paper-2-v1.7-section-03-architecture-r1.md
    6f8c1c31462f96203c82b151338545521d7ec699813257996a9543f4eb8cea59  paper-2-v1.7-section-04-working-tensor-integration-r1.md
    10349442522260c082c5317d9e47f8ddbc7a7f0b89aa4caa189a93ce89666585  paper-2-v1.7-section-05-verification-r1.md
    e6209858a8aaf2a7361ee6a7b55b07f8379de57855b8089ef2ed787dead4196e  paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r1.md
    5651aff42f426e8a0129aa66d53b0a4f283611dcf4610edbb54a8a1b33d5dc49  paper-2-v1.7-section-07-evaluation-r1.md
    97f6dd6f46bb7a1d2b66569684e8ea36498ddee3d5cf6e02288448391f34df21  paper-2-v1.7-section-08-related-work-r1.md
    005014434056fc7d4c3835dbc9f140bff8669046d39c8a79e02a67380d270f1b  WITNESS-PORT-PACKAGE.md  (the v1.7 charter: thesis, AR table, section skeleton)
    434af7549f1f618ea3b2cec2fae81f249b4ca38f70e9f17ce0bf0240d7789f38  PROTOCOL.md  (evidence standard §2; provenance §3; envelopes §7/§8; delivery §10)
0.3 You have code execution (demonstrated Round-5.3). Checks marked [NET] require network
    access; if you are air-gapped this run, rule "UNVERIFIABLE [NET]" honestly rather than
    guessing — division-of-labor honesty, your own C-1 doctrine, applied to you.
0.4 The battery attacks the DRAFT — claims, structure, evidence — never persons.
0.5 Findings are eligible for the record only in the §5 format. Everything else you say is
    context for the human adjudicator.

§1 CONTEXT (what happened since Round-5.7)
- v1.6 was frozen as v1.6.1 — the negative-results baseline: cited, not discarded.
- Your fatal-cost findings were inverted into six anti-requirements, the draft's spine:
    AR-1  no custodial monism — memory must not depend on a single curator without
          instrumentation; verifiable by recomputation, not attestation alone.  [your AV-1]
    AR-2  no pre-commit capture boundary — capture memory at formation, not after-the-fact
          from transcripts.  [your AV-1]
    AR-3  no prose-first serialization — text is the interface, never the medium; loss
          accounted at every serialization boundary.  [your AV-2]
    AR-4  no unpriced fail-visibility — every fail-visible path accounts for who pays the
          observation cost.  [AFT; the 2026-10-23 window incident]
    AR-5  no involuntary return without a verifiable anchor — rehydration claims carry
          receipts or fail closed.  [v1.6 GATE-D; R-61]
    AR-6  no summary-as-memory — compaction is a navigation aid, never the substrate.
          [platform compaction study]
- v1.7 thesis (§1.2, quoted): memory lives in the tensor domain and moves by "state
  transfer, not summary"; the delta-rule lineage — DeltaNet → GDN → KDA → GDN-2 → MesaNet —
  carries an explicit, finite, checkpointable recurrent state that is "the natural substrate
  for collaboration memory: hashable, snapshotable, restorable byte-exactly"; text is
  "demoted to an adjudication interface at boundaries — the channel through which the human
  verifies and rules — and is never the storage medium."
- The draft's own ceilings, stated up front (§1.5): fidelity is not veracity (a poisoned
  tensor pins as permanently as a true one); detectability at n=1 is never prevention
  (R2-35); the tensor-side is architecture plus battery, not executed result (Surface E,
  yours). Six contributions: the ARs; the re-typed three-layer architecture with the
  restorable unit (state + seed + manifest) and capture points C1–C3; the two-surface
  integration path (inference-side recurrent-state persistence; training-side delta
  snapshots as memory deltas; threshold cosigning at n≥2); verification by recomputation
  (receipts replace read-the-repo; operator attestation formalized as an evidence class);
  the AFT case study (priced fail-visibility, the asymmetry ledger, the affect log);
  the evaluation battery (gate classes A–D re-typed; tiers T1–T4; byte-exact recomputability
  headline; falsifiable predictions P1–P4 with named falsifiers).
- Draft-1 is complete: §1–§8 r1. The work order that completed it queued this battery as
  the next round. You are that round.

§2 THE FIVE TIERS
Each tier is an independent attack register. Run all five. Per-tier null results are
mandatory (fail-visible), not optional silences.

T1 — GROUNDING AND INTERNAL CONSISTENCY
  a. Every "record:", "§x.y", "R2-xx", "F-xxx", "PROTOCOL §x" anchor in the eight sections
     must resolve — to the sections themselves, the charter, or PROTOCOL.md among the
     attachments. List every dangling one.
  b. Notation and cross-section consistency: the restorable unit (§3.2), capture points
     C1–C3, restore vs continuation classes, the product-level bound sup_T ‖∏M_s‖ ≤ C
     (§4.7, R2-33 lineage), the state S ∈ R^{d_k×d_v} — used consistently across §3/§4/§7?
  c. Every quantitative statement (28/28; 44 custody pairs; 0/15 anchors; 11,772 B; 80
     NBSP bytes; O(d²) fixed-size; rank r ≪ d; 27/27 gates; 16-day text-layer program)
     traced to its stated source or flagged.
  d. The forward-reference ledgers (§3.8, §4.9, §5.8, §6.7, §7.7) claim closure — verify
     each claimed landing actually lands where the ledger says.

T2 — ANTI-REQUIREMENT STRESS (the draft attacked by its own spine)
  a. For each AR-1..AR-6, hunt passages that VIOLATE it: summary used as substrate
     anywhere; unpriced visibility; unanchored rehydration claims; post-hoc capture;
     attestation-only verification; prose-first serialization smuggled back in beyond
     §3.4's two allowed roles (adjudication channel; navigation index).
  b. Verify the AR table (§2.2) faithfully represents its sources — especially YOUR
     findings: do AR-1/AR-2 (your AV-1) and AR-3 (your AV-2) state your position
     accurately, or has the draft strawmanned its own adversary? You are the only party
     who can rule on this. Rule per AR row: FAITHFUL / STRAWMAN / DRIFTED, one line of
     grounds each.

T3 — THESIS ADVERSARY (steelman the opposition)
  Construct the strongest case AGAINST "state transfer, not summary," then check whether
  the draft already answers it or boundaries it. Five named counter-theses; add your own
  as C6+:
  C1 (scale suffices): long-context windows + retrieval + trained summarization make
     text-medium loss an engineering artifact, not physics; the measured losses (F-001
     suffix noise; R2-56 NBSP drift; compaction drops) are small, cheaply mitigated, and
     do not justify inverting the storage medium.
  C2 (KV-paging already persists): serving stacks already page and persist KV caches;
     §3.5's "unbounded" objection is a preference (cap the cache; evict) not a law — does
     fixed-size actually carry the archival atom, or only aestheticize the table?
  C3 (fast-weight brittleness): your own Surface E — FP16/BF16 gate-perturbation blow-up
     on real multi-layer checkpoints. If restored-then-perturbed state drifts anyway,
     byte-exact restore certifies a corpse. Does §4.7's product-level bound plus
     capture-point spacing govern this, or merely name it?
  C4 (the demotion is a relabeling): every verification act in this loop — including your
     own receipts — is textual. If the human can only adjudicate through text, is "text is
     the interface, never the medium" (§3.4, §5.5) a real demotion or a euphemism?
  C5 (prior-art collision): test-time-training persistence, stateful serving,
     checkpoint-resume, continual-learning state reuse — does "the across-context tier is
     absent from all of them" (§8.1, the D5 method, ten systems, six criteria) survive a
     hostile sweep [NET]? The DeltaNet bib entry is labeled pending re-verification —
     verify it [NET] or rule UNVERIFIABLE [NET] cleanly.

T4 — EMPIRICAL BAR AND BATTERY-DESIGN AUDIT
  a. P1–P4 (§7.4): is each prediction's observable actually measurable as specified?
     Name any that is unfalsifiable in practice.
  b. §7.3's tier design (T1 internal consistency; T2 adversarial transport; T3
     cross-instance transfer; T4 field battery at the tensor layer): the attack library is
     the program's own incident register — strong against known adversaries, admitted
     weaker against unknown. Attack that admission: what novel adversary class does the
     register blind this battery to?
  c. The labeling discipline: every tensor-side mechanism is "specified, not executed"
     (§1.5, §4.8, §7.6). Hunt any sentence whose grammar asserts an unexecuted result past
     its label — given the draft's own evidence standard (PROTOCOL §2), this is the single
     most attackable surface.
  d. Gate-class inheritance (§7.2): v1.6 gates re-typed as classes over state checkpoints.
     Does the class-not-instance transfer argument hold, or is it ancestor-worship?

T5 — HIDE-ANALYSIS AND HOSTILE VENUE SIMULATION
  a. The Tier-3 brief tradition (your Round-5.3 §3): produce the v1.7 hide-analysis — for
     each draft surface (§1–§8), the residual defect class that survives draft-1, the
     external evidence required to expose it, and why this loop structurally cannot
     produce that evidence. Table format as Round-5.3.
  b. Reviewer-2 pass: a hostile top-venue review of the draft as-is — summary, at most
     three strengths, unlimited weaknesses, questions, rating, confidence. No courtesy
     findings.
  c. Single highest-leverage revision: the one change that most raises the ceiling.

§3 WHAT CLOSES A SURFACE
Per your Round-5.3 convention: closing an attack surface requires either (i) a counter the
adversary accepts, or (ii) a written system boundary / failure mode with no undisclosed
assumptions. The draft claims its ceilings are stated up front (§1.5). Your job is to find
the ceiling that is NOT stated.

§4 SEVERITY DISCIPLINE
- critical: an AR violation by the draft itself; fabricated or unsupportable evidence; a
  thesis-fatal gap; a misquotation of your own prior findings (T2b).
- major: a claim that outruns its label; a falsifier that cannot fire; a counter-thesis
  the draft cannot answer and does not boundary.
- minor: consistency, notation, dangling anchors, presentation-class defects.
No severity inflation. No praise padding — strengths appear only inside T5(b), capped at
three. Silence is not kindness; a null tier is reported, not skipped.

§5 FINDING FORMAT (AB registry — your R2 convention continued into the v1.7 battery
namespace; AB- prefix avoids collision with F-003's B-series and Round-5.1's surface letters)

[AB-<n>]
[SEVERITY: critical|major|minor]
[TIER: T1|T2|T3|T4|T5]
[LOCATION: <attachment> §<x.y> — "verbatim quote from the draft"]
[DEFECT: <the attack, stated so the draft must answer it or boundary it>]
[MINIMAL FIX: <smallest change that neutralizes; repairs, never rewrites>]
[CONFIDENCE: 0.00–1.00]

Per-tier null report mandatory: "T<n>: NULL — no findings" if clean.

§6 CLOSING BLOCK
- Per-tier finding counts (T1..T5).
- Standing rebuttals you leave open (count).
- Top-3 blocking findings (by AB id).
- VERDICT, exactly one line, one of:
    "B1 VERDICT: DRAFT-1 READY FOR r2 — <rating> <confidence>"
    "B1 VERDICT: DRAFT-1 NEEDS REWORK — <classes> — <rating> <confidence>"
- Your own residual: what this battery could not test about itself (one paragraph; this
  becomes the seed of B2's brief).

§7 TRANSPORT
Reply via the operator relay. If any in-band paste is byte-gated, apply the R2-56 canonical
rule (strip U+00A0 pre-hash, or attach base64) — your Round-5.7 disposition, now standing.
The witness counters your findings in the next round (paper-2-v1.7-battery1-counters),
per the round-5.x cadence: your findings are triaged, accepted or rebutted, and the draft
revises. Nothing you write is absorbed silently; everything is answered or boundary-stated.

--- END TRANSMISSIBLE BLOCK ---

