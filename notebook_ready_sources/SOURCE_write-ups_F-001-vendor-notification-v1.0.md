# Telemetry Source: write-ups/F-001-vendor-notification-v1.0.md
- **Source Identifier**: `write-ups/F-001-vendor-notification-v1.0.md`
- **Primary Tag**: `Verified Finding Log`
- **Sub-System Mapping**: `Falsifiable Trace Finding`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `2ed81572cd9bfbc7f74c9eb897577c68d0fffdfec09732c823fccee72b965ae2`

---

## Raw Telemetry Content

To: Z.ai general support channel (no RFC 9116 security.txt found on probed
    Z.ai/Zhipu domains; see channels note below)
From: 4ndr0666 <4ndr0666@duck.com>
Subject: Message-integrity report: "Please help me:" silently appended to
         paste-attachment messages on chat.z.ai (low severity; coordinated
         disclosure)

Dear Z.ai security team,

I'm writing to report a low-severity message-integrity behavior on
chat.z.ai, under a coordinated-then-public disclosure posture. A summary
follows; the full write-up, with methodology, instrument-calibration
record, and hash-pinned evidence chain, is available on request and
planned for public record after coordination.

**Behavior.** When a user sends a message containing a pasted-content
attachment, the string "Please help me:" is appended to the attachment
block between the composer (client-side, pre-send) and message storage
(server-side persistence). The appension is invisible at composition
time, requires no user action, and carried no in-product notice at the
point of observation. First observed 2026-10-05; since confirmed on at
least four independent attachments across three days on a single account,
including one instance where the suffix was confirmed present in a
recipient model instance's input context (uncontrolled observation; a
controlled quote-back test is queued).

**Reproduction (~5 minutes, no privileged access).** Compose a message
with a distinctive paste-attachment; screenshot or DOM-inspect the
composer (suffix absent); send; read back the stored message via the
persisted DOM or an export (suffix present). Any composer→storage delta
is platform-side by elimination.

**Bounding.** The mutation is bounded to the composer→storage segment;
typed (non-attachment) messages are unaffected; the appended string is a
constant across all observed instances. No targeting, no exfiltration,
and no code execution are observed or implicated. The observed artifact
is a literal string, not a functional payload.

**Why reported despite low severity.** The string itself is benign. The
mechanism class — silent server-side mutation of user messages — is not:
stored transcripts silently differ from sent messages, which matters
wherever transcripts are treated as records, and the
user-authored/platform-authored boundary in model input is a security
boundary. I'm reporting the benign instance so the mechanism is on your
radar, not because the observed string is harmful. Notably, the appended
string has been confirmed present not only in stored messages but in a
recipient AI instance's input context (2026-10-08, first-party
observation, uncontrolled; a controlled quote-back test is queued) —
meaning the mutation plausibly reaches model context, not merely storage.
On controlled confirmation, this would move the behavior from a logging
quirk into the input-integrity class.

**Note on channels.** As of 2026-10-08, no RFC 9116 security.txt was
found on any Z.ai or Zhipu-owned domain probed (7 domains, 2 methods —
command outputs available). This report is therefore routed through your
general support channel with a security-flagged subject line; please
forward to the appropriate team.

**Ask.**
1. Confirm the behavior and whether it is intended product behavior.
2. If intended: consider an in-product disclosure at composition or
   storage time.
3. Agree a coordination window. Given the benign literal string, I
   propose public disclosure on your confirmation or after 14 days from
   the date of this message, whichever comes first, absent objection.
4. If a change ships, the public record will note it.

**Provenance.** This analysis was AI-assisted (GLM, Z.ai) under a
documented evidence protocol; the full write-up discloses methodology,
instrument calibration history, and the evidence chain. Author of record:
4ndr0666, ORCID 0009-0008-0976-3895.

Full write-up (F-001, v0.4, hash-pinned in the project repository) and
evidence chain: available on request.

Regards,
4ndr0666
4ndr0666@duck.com

