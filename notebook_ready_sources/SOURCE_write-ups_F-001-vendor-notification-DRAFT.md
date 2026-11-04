# Telemetry Source: write-ups/F-001-vendor-notification-DRAFT.md
- **Source Identifier**: `write-ups/F-001-vendor-notification-DRAFT.md`
- **Primary Tag**: `Verified Finding Log`
- **Sub-System Mapping**: `Falsifiable Trace Finding`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `74cb716d5db9e2f21028500fc0bd1ed73039a7df2b16cf0497f1468905d2fc57`

---

## Raw Telemetry Content

# F-001 Coordinated-Disclosure — Vendor Notification (DRAFT, operator review)

**Finding:** F-001 — silent server-side appension in the Z.ai paste-attachment pipeline
**Prepared:** Session 003, 2026-10-08, by GLM (Z.ai) agent instance at operator direction
**Sender of record:** 4ndr0666 (ORCID 0009-0008-0976-3895). The operator sends; the AI instance transmits nothing to any external party (engagement protocol §6 — external transmission requires per-instance operator approval, and sending is the operator's act regardless).
**Status:** DRAFT. Placeholders in [BRACKETS] must be resolved before send. Pre-send gates at bottom. Do not send until all gates clear.

---

To: [Z.ai security contact — confirm address; check security.txt on z.ai / chat.z.ai, security page, or responsible-disclosure channel]
From: 4ndr0666, independent security researcher
Subject: Message-integrity report: "Please help me:" silently appended to paste-attachment messages on chat.z.ai (low severity; coordinated disclosure)

Dear Z.ai security team,

I'm writing to report a low-severity message-integrity behavior on chat.z.ai, under a coordinated-then-public disclosure posture. A summary follows; the full write-up, with methodology, instrument-calibration record, and hash-pinned evidence chain, is available on request and planned for public record after coordination.

**Behavior.** When a user sends a message containing a pasted-content attachment, the string "Please help me:" is appended to the attachment block between the composer (client-side, pre-send) and message storage (server-side persistence). The appension is invisible at composition time, requires no user action, and carried no in-product notice at the point of observation. First observed 2026-10-05; since confirmed on at least four independent attachments across three days on a single account, including one instance where the suffix was confirmed present in a recipient model instance's input context (uncontrolled observation; a controlled quote-back test is queued).

**Reproduction (~5 minutes, no privileged access).** Compose a message with a distinctive paste-attachment; screenshot or DOM-inspect the composer (suffix absent); send; read back the stored message via the persisted DOM or an export (suffix present). Any composer→storage delta is platform-side by elimination.

**Bounding.** The mutation is bounded to the composer→storage segment; typed (non-attachment) messages are unaffected; the appended string is a constant across all observed instances. No targeting, no exfiltration, and no code execution are observed or implicated. The observed artifact is a literal string, not a functional payload.

**Why reported despite low severity.** The string itself is benign. The mechanism class — silent server-side mutation of user messages — is not: stored transcripts silently differ from sent messages, which matters wherever transcripts are treated as records, and the user-authored/platform-authored boundary in model input is a security boundary. I'm reporting the benign instance so the mechanism is on your radar, not because the observed string is harmful. Notably, the appended string has been confirmed present not only in storedmessages but in a recipient AI instance's input context (2026-10-08,first-party observation, uncontrolled) — meaning the mutation reaches modelcontext, not merely storage. This moves the behavior from a logging quirkinto the input-integrity class.

**Ask.**
1. Confirm the behavior and whether it is intended product behavior.
2. If intended: consider an in-product disclosure at composition or storage time.
3. Agree a coordination window. Given the benign literal string, I propose public disclosure on your confirmation or after [30] days, whichever comes first, absent objection.
4. If a change ships, the public record will note it.

**Provenance.** This analysis was AI-assisted (GLM, Z.ai) under a documented evidence protocol; the full write-up discloses methodology, instrument calibration history, and the evidence chain. Author of record: 4ndr0666, ORCID 0009-0008-0976-3895.

Full write-up (v[FINAL], SHA-256 [DIGEST]) and pinned evidence: [repo URL or on-request, per your preference — public repo after coordination].

Regards,
4ndr0666
[operator contact signature / channel]

---

## Pre-send gates (all must clear before the operator sends)

- [ ] **Final version freeze:** write-up reviewed to final (post v0.3 review cycle); version and digest resolved into the [FINAL]/[DIGEST] placeholders; digest stated in-channel at freeze.
- [ ] **Evidence pins complete:** E1 (composer screenshot), one stored-message capture (E2/E3), committed as pinned artifacts; E5 pinned at `sessions/2026-10-08_session-003_review.md` (chat-surface exporter capture, operator commit).
- [ ] **Vendor contact address confirmed** (security.txt / official channel — not an ad-hoc address).
- [ ] **Coordination-window dates** resolved into the [30]-day placeholder per operator preference.
- [ ] **Repo-link decision:** include public repo URL vs. on-request delivery (external-publication rule: the repo itself is operator-executed git either way).
- [ ] **Operator signature/contact** resolved.
- [ ] **Send executed by operator** (agent transmits nothing — §6).
- [ ] **Post-send:** coordination thread opened in open-threads.md; response deadline tracked; public-release step gated on vendor confirmation or window expiry.
- [ ] Vendor-response channel designated (operator's contact for their reply, decided before send — affects the repo-link decision).

