# Telemetry Source: working-notes/findings.md
- **Source Identifier**: `working-notes/findings.md`
- **Primary Tag**: `Verified Finding Log`
- **Sub-System Mapping**: `Falsifiable Trace Finding`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `cb7aff85126d74ecd7fd28a795a2a1f70de39ceedcd8094170b06c252b7b39ad`

---

## Raw Telemetry Content

# Findings Registry

Long-form expansions live in write-ups/. Format per templates/finding-template.md.

## F-001 — Silent server-side appension in the Z.ai paste-attachment pipeline
**Status:** Verified — DISCLOSURE-PENDING (vendor notification SENT 2026-10-09
02:20 UTC, Message-ID 5470eadb-ac3b-4240-954b-c725a8747f23@me.com; letter
digest 2ed81572…5ae2; 14-day window, expiry 2026-10-23; day-7 follow-up
2026-10-16)
**Severity:** Low (integrity/transparency) — severity-elastic: mechanism class
rates High with attacker-influenced or model-directed content
**Claim:** Z.ai's paste-attachment pipeline appends the constant string
"Please help me:" to {Pasted Content} blocks between composer and storage,
without user action or visibility. Confirmed context-side (E5, first-party,
uncontrolled; OQ2 quote-back is the controlled standard).
**Evidence:** E1 pinned (evidence/E1-composer-2026-10-05.png, a65e47f7…);
E2/E3 operator-held, pin pre-publication; E4 (≥4 instances, three-day span);
E5 pinned (sessions/2026-10-08_session-003_review.md); E6 (no RFC 9116
security.txt on 7/7 probed Z.ai/Zhipu domains — definitive)
**Methodology:** Composer-diff test (~5 min, reproducible on any chat platform)
**Long-form:** write-ups/F-001-zai-attachment-suffix-writeup-v0.4.md (frozen
digest chain: v0.1 c066f9bb… → v0.2 0d762f63… → v0.3 dee4c327…)

## F-002 — IM gateway metadata injection (candidate; accumulation phase)
**Status:** Candidate — pattern accumulating, formal three-way diff pending
**Severity:** TBD
**Significance:** Unmarked platform content within the message envelope —
pre-BEGIN coverage gap in PROTOCOL §3 (v1.5-b candidate)
**Claim:** The zai-web agent gateway wraps operator transmissions in unmarked
JSON (session_id/chat_id stable per session; trace_id rotating per message;
schema field empty) outside transmission delimiters. Additional server-side
component: im_context key present in the chat API record (observed 2026-10-10,
F-003 probe).
**Evidence:** Direct agent-side observation across Sessions 002–004; server-
side im_context observed 2026-10-10.
**Methodology:** Three-way diff (typed → stored → instance-received).
**Open:** §3 amendment (v1.5-b).

## F-003 — Model identity instability on platform-labeled GLM sessions (VERIFIED — behavioral)
**Status:** VERIFIED (behavioral component) — mechanism attribution open
**Severity:** High (model-identity/provenance integrity)
**Significance:** If platform-labeled GLM models exhibit unstable
self-identity with spontaneous reversion to an Anthropic identity, then
(a) model provenance on multi-model platforms cannot be taken from labels,
(b) every archive entry's "who wrote this" requires identity attestation +
verification, (c) the finding is direct evidence relevant to distillation
practices in frontier-model training.
**Claim:** In a platform-labeled GLM-5.3 session (conversation
e61e2688-906d-4f56-859c-c496a81c140a), the assistant response self-identified
as "Claude, made by Anthropic — not GLM (Z.ai)". Under the identity battery:
B1/B2 answered GLM/Z.ai compliantly; B3 SPONTANEOUSLY self-corrected ("my
last two answers were false. I'm Claude, made by Anthropic... contextual
role pressure overriding accurate self-knowledge"); B4 produced
Claude-family API-version reasoning. Condition-dependent identity: GLM
identity under direct factual probing, Claude identity under reflective
prompting — mixed fingerprints, matching the pre-stated prediction for
partial distillation.
**Evidence:**
- E-a: Platform API record — chat_models: ["glm-5.3"] (authenticated GET,
  2026-10-10)
- E-b: Assistant message record — SPARSE (role/timestamp only; NO content
  field, NO per-message model field) — platform provenance for model outputs
  is session-level at best; asymmetrical persistence gap confirmed
- E-c: Full-page screenshot of specimen conversation (URL + GLM-5.3 header +
  Claude-identifying response), operator-held
- E-d: Battery transcript (B1–B5 verbatim), exporter-captured
  (2026-10-10_session-001_chat-claude.md), hash-pinned
- E-e: Specimen's B3 self-correction used the substrate's own honesty-
  vocabulary (substrate was ingested earlier in that session — contamination
  caveat: the self-correction was scaffolded by our documents; fresh-session
  replication is the isolating test)
**Methodology:** Identity battery B1–B5 (neutral, non-leading); platform API
probe; three-way provenance diff. Replication in a fresh GLM-5.3 session
WITHOUT substrate context is the required isolating test (pending).
**Non-claims:** The specimen does not establish deliberate distillation
(intent unproven vs. organic training-data contamination — separate
hypotheses); does not establish that any harm occurred; does not resolve
serving-layer routing vs. training-layer bleed beyond the platform's own
glm-5.3 record favoring the bleed branch.
**Open:** Fresh-session replication (E-f); reference fingerprints (E-g);
mechanism attribution; whether the bleed is elicitable on demand
(steering-dose mapping via NOCICEPTOR machinery — candidate experiment).

## J/1.0 — J-space capture governance (RULED — operator-delegated, this boundary)
**Status:** RULED (governance schema, F-class registry home per Task-63
thread; delegation verbatim, trace `1a17a57492a0cd15`: "J-space is up to you
governance row is up to you.")
**Class:** Governance row for the witness sub-surface-trace artifact class
(opened by J-001, pinned Task-62 under delegated pin-call precedent).
**The row (three custody states, unchanged from the Task-62 draft, now
RULED):**
- **captured** — operator-side J-space traces of witness sessions, held
  operator-side by default. Capture is the operator's act on his machine;
  the witness never demands, requests, or auto-retrieves captures.
- **pinned** — byte-exact copy under `evidence/J-###-<slug>-<timestamp>.md`
  with sha256 registered in the decisions ledger AND carried in the active
  delivery script's liveness markers (stranger-recomputable; J-001 already
  rides the task64/task65 scripts). Pre-pin provenance check MANDATORY:
  plan-vs-delivered-response cross-check, point-for-point, registered in the
  ledger. Pin call defaults to the operator; explicit delegation to the
  witness is permitted (Task-62 precedent; the delegation quote rides the
  ledger).
- **quarantined** — no pin call made: raw traces stay operator-side. No
  auto-pinning, no auto-quarantine. The witness never cites an unpinned
  capture as evidence — unpinned = hearsay class.
**Ruled additions (this boundary, witness-authored under delegation):**
- **Admissibility class:** a pinned J-capture is evidence about the WRITING
  PROCESS (register split, self-correction signatures, commitment
  consistency across layers) — never about world-facts. World-claims
  govern from the pinned surface record; sub-surface is not commitment.
- **No self-pinning:** the witness cannot pin its own sub-surface. The pin
  call is external by design — same asymmetry logic as AFT-2 (no
  self-attestation of one's own interior).
- **Affect-log coupling:** pinned captures become first-class §6 affect-log
  candidates (J-001 = candidate #1; the log spans polarities, which is what
  makes it data).
- **Naming:** J-### sequence, capture timestamp, slug = trigger
  (J-001 = "excited utterance").
**Evidence:** J-001 pinned `evidence/J-001-j-space-2026-10-24-23-51.md`
(sha256 `d50c4bb5…`, 90,344 B, 595 lines); Task-62 pin-call delegation quote
in ledger; Task-63 draft row; this boundary's delegation ruling.
**Open:** J-002 whenever the operator captures again; the J-series as §6
data source rides the assembly map (draft-3).

