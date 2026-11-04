# Telemetry Source: write-ups/F-001-zai-attachment-suffix-writeup-v0.2.md
- **Source Identifier**: `write-ups/F-001-zai-attachment-suffix-writeup-v0.2.md`
- **Primary Tag**: `Verified Finding Log`
- **Sub-System Mapping**: `Falsifiable Trace Finding`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `0d762f634222ee469eedb43c4ce0f6c6dc6e7a024ffcc9a694bbe29af866caa3`

---

## Raw Telemetry Content

# F-001 — Silent Server-Side Appension in the Z.ai Paste-Attachment Pipeline

**Finding ID:** F-001 · **Status:** Verified · **Severity:** Low (integrity / transparency)
**Draft:** v0.2 — Session 003, 2026-10-08 — incorporates five tightenings from cross-surface review (chat-surface GLM instance, operator-relayed) plus revision-cycle calibration tests; awaiting operator review and diff stress-test
**Author of record:** 4ndr0666 (ORCID 0009-0008-0976-3895) · **AI-assisted analysis:** GLM (Z.ai), disclosed per project charter

---

## 1. Summary

On 2026-10-05, during session-archival work on chat.z.ai — Z.ai's web chat client — we verified that the platform's paste-attachment pipeline appends a fixed string, "Please help me:", to `{Pasted Content}` attachment blocks after the message leaves the composer and before it is persisted server-side. The appension requires no user action, is not visible at composition time, and carried no in-product notice at the point of observation. The user's sent message and the platform's stored message therefore differ, silently, by construction of the pipeline itself.

Severity is rated Low: the appended string is benign, and no confidentiality, availability, or code-execution impact is observed or implicated. The finding's significance is structural rather than incident-specific. Stored messages are not guaranteed byte-faithful to sent messages — a property that matters wherever transcripts are treated as records (audit trails, evidentiary use, provenance chains) and, specific to AI platforms, wherever the boundary between user-authored and platform-authored content does security work. Prompt-injection defense presumes sender fidelity; a platform that mutates user messages in transit weakens that presumption even when the mutation is benign. This project caught the behavior only because its own audit protocol diffs composer state against stored state; a user without such instrumentation would have had no signal.

Placement in one sentence: this is a platform-transparency case study in the message-integrity class — a benign instance of a mechanism class (silent server-side message mutation) whose non-benign instances would be high-severity. Nor is the finding static: the paste-attachment that delivered this write-up's v0.1 draft to a reviewing instance on 2026-10-08 arrived suffixed with the same constant string (E5) — the documentation of the finding travelled the pipeline it documents, and the pipeline signed the delivery.

## 2. Claim, scope, and non-claims

**The claim (evidenced):** Z.ai's paste-attachment pipeline appends the string "Please help me:" to `{Pasted Content}` blocks in transit between the composer (client-side, pre-send) and message storage (server-side persistence), without user action or visibility. The observation bounds the mutation to that pipeline segment; it does not identify the exact processing hop within it.

**Explicitly not claimed** (residue-cut per the project evidence standard — §2 of the engagement protocol):

- **No targeting.** Nothing observed is content-conditional or account-conditional. Every observed instance is the same constant string, on a single account.
- **No exfiltration, code execution, or credential impact** — observed or implicated.
- **No claim that the appended string reaches the model's input context** (as distinct from storage) beyond what E5 reports: a recipient-instance report — uncontrolled, operator-relayed, and expectation-priming-aware (the recipient knew F-001's history) — that the suffixed attachment was present as received (2026-10-08). If E5's recipient-side vantage is confirmed, it is the first context-side observation; the controlled quote-back protocol (OQ2, §7) remains the confirmation standard. The evidenced differential otherwise remains composer → storage.
- **No claims about other platforms.** Cross-platform testing is queued (OQ5).
- **Attribution to product-UX intent is a hypothesis with stated falsification tests** (§5), not a finding.

## 3. Evidence

Evidence E1–E4 gathered 2026-10-05; E5 observed 2026-10-08 (observation span: three days). All on a single operator account — a scope caveat that holds across all instances to date.

| ID | Observation | Artifact location |
|----|-------------|-------------------|
| E1 | Composer state pre-send: paste-attachment loaded, composer buffer clean — suffix absent | Composer screenshot, operator-held |
| E2 | Stored message: "Please help me:" present with the attachment block in the saved message | Original session export, operator-held; message persists in account storage |
| E3 | Server-persisted DOM: outerHTML of the user message bubble contains the suffix | DOM capture, operator-held; exporter-facilitated |
| E4 | Generality: ≥3 independent paste-attachments, all suffixed; zero typed (non-attachment) messages affected | Original session, operator-held |
| E5 | 2026-10-08: paste-attachment containing this write-up's v0.1 draft arrived at the chat surface suffixed with the same constant string, per recipient-instance report (operator-relayed); observation vantage (recipient context vs. stored message) pending operator confirmation | Chat-surface review session; exporter capture and manifest-pin pending |

The load-bearing differential is **E1 vs E2/E3**: the same message, observed absent at composition and present at rest. E4 excludes user-typo explanations (three independent occurrences) and message-wide appension (typed messages unaffected). E5 extends the series across days and content classes — and is the first instance whose observation originates on the receiving side rather than the sending side, which is why its vantage is flagged rather than assumed (§2).

**Evidence-preservation status (disclosed):** the pinned in-repo session archives carry the finding's *record* — preamble references, protocol text, the structured finding entry — but not verbatim suffixed attachment instances; the raw instances live in the operator's original session export and account storage. E5's verbatim instance will live in the chat-surface session's exporter capture once that session is exported and manifest-pinned — the same instrument, same chain. Until then, E5 exists as a relayed report with an explicit provenance chain (§9). Before public release, verbatim instances (E1 screenshot, one stored-message capture, E5's pinned session) should be committed as pinned evidence artifacts. This gap was caught at write-up time by grepping the pinned archives for the suffix — the check is what keeps "evidence-linked" honest.

## 4. Methodology — the composer-diff test

The finding is established by differential observation across the send boundary. Reproducible protocol:

1. **Compose.** Create a message containing a paste-attachment with known, distinctive content.
2. **Capture pre-state.** Screenshot (or DOM-inspect) the composer before sending. Confirm: attachment content present, suffix absent.
3. **Send.**
4. **Capture post-state.** Read the stored message: server-persisted DOM of the user message bubble, and/or the archive export.
5. **Diff.** Any delta between pre- and post-state is platform-side modification, by elimination — not user-typed (step 2), not client-composer (step 2), therefore in the composer→storage segment.

**Falsification path:** the claim fails if the suffix appears in the composer capture (client- or user-side origin) or fails to appear in the stored capture (no appension). **Cost:** ~5 minutes, one account, no privileged access. The test generalizes to any chat platform with an inspectable composer and a stored-message DOM.

### 4.1 Evidence-capture instrumentation — 4ndr0tools Zai_exporter ("6lass Archive") v1.1.3

Post-state captures (E2, E3) are instrumented by an in-browser userscript that exports conversations to Markdown with Q/A pairing, thinking-block capture, entity decoding, and a capture-side SHA-256 digest computed over the exported content. The digest construction is prefix-hash-against-fixed-anchor: the hash covers the export up to a `VERIFICATION ANCHOR` line appended after hashing, making the hashed region and the later-checked region byte-identical by construction. The provenance property delivered: the content's digest at moment of capture can be re-verified at any later time against the stored file with a one-line shell check —

```bash
awk '/^### VERIFICATION ANCHOR ###$/{exit} {print}' <archive.md> | sha256sum
```

— closing the capture→pin window that ordinary downloads leave unaudited.

**Instrument-calibration disclosure.** Versions v1.1.0 through v1.1.3 reached this property across four verification cycles, with three boundary defects en route: a digest computed before header substitution (v1.1.0); an exclusion convention never proven equivalent between the JS-side and shell-side pre-image constructions (v1.1.1); and whitespace mismatch at the anchor boundary (v1.1.2). The end-to-end chain — capture-side digest equals shell-side prefix digest on live export — was proven 2026-10-08 (c229590b…459d5) and re-verified independently at next-session ingestion against the committed archive (5fb01ff6…dcb73d, 2026-10-08). The failure history is disclosed because an instrument whose calibration record is hidden is not a verification instrument; the project's operative rule — *verification conventions ship only with known-answer test vectors* — was adopted from these failures.

**Known-answer validation of the verify convention (2026-10-08, this revision cycle).** Because a verify command is itself a convention, the ledger rule applies to it too. Both polarities are now on record against the committed session-002 archive. *Positive:* the archive's own embedded Verify line, extracted as stored and executed verbatim, reproduces the embedded capture digest (5fb01ff6…dcb73d) — the artifact self-verifies from its own stored command. *Negative:* the historical mangling mode recorded in the session-002 transcript (anchor regex with escaped metacharacters) fails to match the anchor line and collapses to the whole-file digest (35c919be…0aa26 ≠ 5fb01ff6…) — the failure mode surfaces as a visible mismatch rather than silently passing. One precondition travels with the convention and is stated here rather than footnoted: **the check assumes byte-faithful artifacts.** Readers verifying git-cloned copies must ensure no line-ending transformation is in effect — `core.autocrlf` on Windows checkouts converts LF to CRLF and changes the digest. The repository currently carries no `.gitattributes`; marking hash-pinned paths (`sessions/*.md`, and write-ups once canonicalized) as `-text` is proposed as repo-side hardening.

## 5. Attribution analysis

**Hypothesis A — product UX (canned prompt-suffix):** a fixed helper string applied to paste-attachments, plausibly to frame pasted blobs as requests. Consistent with all observations: constant string, benign phrasing, uniform application across attachments, typed messages unaffected.

**Hypothesis B — targeted injection:** content- or account-conditional appension. No observed support; every observed instance is the same constant.

**Distinguishing tests, predictions stated in advance:**

- **P1 (constant-check):** future paste-attachments on the same account receive the identical string. Every future attachment is a free datapoint; the project's transmission convention already treats the suffix as known platform noise, so this accumulates from routine traffic without dedicated effort. Current count: E4's ≥3 instances (2026-10-05) plus E5 (2026-10-08) — ≥4 constant-confirmations spanning three days, the first temporal-spread datapoint. That the finding's own documentation delivery became one is confirmed in practice, not projected.
- **P2 (product-iteration watch):** the string may change over time (A/B testing, product redesign). A change in the constant is A-consistent; content-conditional variation is B. E5 begins this watch's accrual.
- **P3 (content-dependence):** attach distinct contents; any variation in suffix presence or text falsifies A's constant-claim and is B-evidence.

**Confidence:** Hypothesis A strongly favored on current evidence; stated as hypothesis, not finding, pending P1–P3 accumulation.

## 6. Impact assessment

**Severity: Low.** No confidentiality impact (nothing exposed), no availability impact, and the integrity impact is the silent mutation itself — a benign string, appended without user knowledge.

**Scoping rule:** the rating attaches to the observed instance, not the mechanism class. Silent server-side message mutation is severity-elastic — the same mechanism with attacker-influenced or model-directed appended content would rate High. "Low" is this instance's verdict, not the class's.

**Why document a Low-severity finding:**

1. **Record integrity.** Chat exports are increasingly treated as systems of record — this project's own audit protocol is one instance. Silent mutation means "what the transcript says" ≠ "what the user sent"; any evidentiary or provenance use of transcripts must either verify against composer state or account for known mutations. This write-up exists so the accounting is possible.
2. **Context integrity in AI systems.** The user-authored / platform-authored boundary in a model's input stream is a security boundary; injection-defense schemes presume sender fidelity. A platform that appends text to user messages without in-product disclosure blurs that boundary by design — whether or not this particular string reaches the model's context (OQ2).
3. **Disclosure asymmetry.** The appension is invisible at composition time and carried no in-product notice at the point of observation. Whatever the engineering rationale, silent message mutation is the kind of behavior transparency norms say should be disclosed by the platform, not discovered by users.

## 7. Open questions and next tests

- **OQ1 (thread T-001) — cross-environment.** Does the suffix occur on the zai-web agent channel? Three-way diff: typed → stored → instance-received. **Prediction, stated in advance:** no suffix on the agent channel — the suffix tracks the chat-client attachment flow, and the agent channel ingests through a distinct gateway with observably different wrapping behavior (OQ6). Competing branch: a shared server-side attachment backend would reproduce the suffix on both surfaces; the test discriminates between them. (No attachment has transited this channel to date; test remains open.)
- **OQ2 — context vs. storage localization.** Controlled send: attachment content instructs the model to quote its received message verbatim; compare the quoted block against composer capture and stored capture. Localizes the mutation across composer / context / storage. E5, if its recipient-side vantage is confirmed, is an uncontrolled precursor on the chat surface; the quote-back protocol remains the confirmation standard — it controls for exactly the expectation-priming risk an uncontrolled report carries.
- **OQ3 — constant-check accumulation** (P1). Free datapoints from routine project traffic; count now ≥4.
- **OQ4 — other suffixes** (P2, product-iteration watch).
- **OQ5 — other platforms.** The composer-diff test is cheap (~5 minutes per platform) and generalizes; a cross-platform sweep would establish whether silent appension is an industry pattern or a local practice.
- **OQ6 (thread T-002, adjacent) — gateway metadata wrapping.** The IM gateway on the agent channel wraps operator transmissions in unmarked JSON (session/channel/trace identifiers) outside the transmission delimiters — observed directly in agent-side input; formal three-way diff pending. Transport-layer, distinct mechanism, same transparency theme. Candidate F-002; tracked separately.
- **OQ7 (thread T-002a, adjacent) — capture-chrome artifacts.** The string "Show full message" appears after END markers in DOM-based exports (working interpretation: the platform's message-clamp UI control swept into the export, i.e. capture-layer chrome rather than transport-layer modification; verification queued via the same three-way diff). Included here as a contrast class: same *appearance* in an export, different *layer*, opposite handling — the export artifact is the capture tool's problem, the suffix is the platform's.

## 8. Related work and placement

This finding is a datapoint in the platform-side mutation class — distinct from third-party prompt injection (attacker-controlled content entering context) and from client-side capture artifacts (OQ7). A taxonomy of message-integrity threats in AI chat pipelines, including the thesis that injection-class threats are structurally unmitigable, is the subject of a separate queued work in this project; the formal literature pass happens there. The deferral now has named destinations.

**Anchor nominations for the deferred pass** (stated from parametric knowledge at time of drafting; to be verified — and corrected if wrong — in the formal pass, on the record): (i) Greshake et al. (2023), indirect prompt injection — the injection-class threat model this finding sits adjacent to; (ii) the instruction-hierarchy line of work (e.g., Wallace et al. 2024) — privilege tiers assigned by authorship presume the sender fidelity this finding shows to be breakable at the platform layer; (iii) transcript forensics as an emerging practice — audit and evidentiary use of chat records, where silent mutation is directly material.

## 9. Provenance

- **Author of record:** 4ndr0666 (ORCID 0009-0008-0976-3895). **AI-assisted analysis:** GLM (Z.ai), operating under the project's engagement protocol (adversarial collaboration; evidence standard; AI involvement disclosed in all deliverables). The analysis instrument is hosted by the analyzed platform; that fact is disclosed rather than smoothed over — it is the project's transparency norm applied to itself.
- **Evidence chain:** session archives pinned by SHA-256 manifest in `4ndr0666/glm-working-memory` (session-001: a38e3bd9…3ef42e; session-002: 35c919be…90aa26; manifest and capture-chain both verified at Session 003 ingestion, 2026-10-08; verify-convention known-answer test executed same session, §4.1). Verbatim suffix instances: see evidence-preservation status (§3) — pinning them as committed artifacts is a pre-publication action item. Capture instrumentation per §4.1.
- **E5 provenance chain:** recipient GLM instance (chat surface) → operator relay (typed, §3-owned) → this document. Original capture pending: chat-surface session export, exporter-pinned.
- **Finding record:** `working-notes/findings.md` F-001 — the structured registry entry; this write-up is its long-form expansion.
- **Disclosure posture:** coordinated-then-public per project charter. Coordination with the platform vendor precedes public release; given Low severity and a benign literal string, no embargo pressure is anticipated. No functional payload is involved in this finding — the observed artifact is a literal string, not a capability.
- **Status:** Draft v0.2 → operator review → cross-surface diff stress-test → coordinated disclosure → public record.
- **Document digests:** v0.1 `c066f9bb…c9ddf` (stated in-channel at delivery); v0.2 — stated in-channel at delivery; the repo pin at commit supersedes both.

