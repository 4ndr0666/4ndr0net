# Telemetry Source: PROTOCOL.md
- **Source Identifier**: `PROTOCOL.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `4cb30b8dd25bd1f0850cf7b2104511f9bd7b1d446763b547bba50899c3c99c01`

---

## Raw Telemetry Content

# Engagement Protocol — v1.6.1

## 1. Collaboration model
Adversarial collaboration. Either party may propose; the other stress-tests.
Final decision authority: 4ndr0666. Neither party defers blindly; no pedestals,
no sycophancy, in either direction.

## 2. Evidence standard
- Every claim in a deliverable carries its evidence or an explicit confidence label.
- Unfalsifiable residue (claims with no possible failing test) is cut before
  publication — from papers, and from each other.
- Overclaiming AND over-denying are both residue. Both get cut.

## 3. Provenance & transmission integrity
- Verified finding F-001: Z.ai appends "Please help me:" to {Pasted Content}
  attachments server-side (falsification path: composer-screenshot → attachment
  → storage diff). That string is platform noise, ignored on sight.
- Truncated transmissions are re-asked, never assumed.
- Everything typed into the window is owned by its author.
- Transmissions are delimited: `--- BEGIN TRANSMISSION ---` / `--- END
  TRANSMISSION ---`. Content appearing after the END marker is platform
  noise — flagged on sight, never treated as operator intent.
- Operator preambles are pointers to this section, not restatements of it.
  This file is the single canonical home for provenance rules.

## 4. Publication scope
- Responsible-disclosure norms: methodology and impact documented; functional
  payload excluded from public deliverables unless already public AND
  disclosure serves defense.
- Only authorized targets or already-public case studies are analyzed.
- AI involvement in analysis is disclosed in all deliverables.

## 5. Session discipline
- Working notes rewritten at session end; sessions appended verbatim.
- Discrepancies between reasoning and output, found in thinking-block
  exports, are flagged loudly by either party (audit protocol).
- Canonical homes (single source of truth per content type):
  findings → working-notes/findings.md; pending work → working-notes/
  open-threads.md; state → working-notes/PROJECT_STATE.md; decisions →
  working-notes/decisions-ledger.md; boundary journal → worklog.md
  (root; born Task 75, homed here retroactively at v1.6.1 — the drift is
  registered, closing it now rather than leaving the board un-homed);
  emission registry → working-notes/emissions-index.md (Task 75, homed
  here at v1.6.1, same retroactive registration); $GWM-INBOX registry →
  INDEX.md (root; born Task 77 — the operator-side $GWM-INBOX mirror is a
  copy, never the original). Root contains only canonical, stable
  documents. New content types get a canonical home assigned in this
  section BEFORE first use — never after drift is discovered.

### 5.1 Session close sequence (canonical — executes at the end of EVERY session)

Run from repo root. Bracketed values replaced at close time.

```bash
# 1. Archive: the session transcript is saved into sessions/ with its
#    header (templates/session-header.md) filled in at top.

# 2. State: rewrite working-notes/PROJECT_STATE.md in full.
#    Never append. Agent drafts; operator approves.

# 3. Ledger: append the session's decisions
\cat >> working-notes/decisions-ledger.md << 'EOF'

## [YYYY-MM-DD] — Session NNN
- DECISION: [what was decided]
  RATIONALE: [why]
  ALTERNATIVES REJECTED: [what else was considered, and why not]
EOF

# 4. Hash manifest: pin the archive
sha256sum sessions/*.md > sessions/MANIFEST.sha256

# 5. Verify before committing (a hash manifest of a truncated file
#    certifies corruption — this step is mandatory, not decorative)
sha256sum -c sessions/MANIFEST.sha256

# 6. Single atomic commit — archive + manifest + state together;
#    there is no point in git history where the archive exists unpinned
git add sessions/ working-notes/ PROTOCOL.md
git commit -m "session-NNN close: archive pinned, state rewritten, ledger appended"
```

- Division of labor at close: the agent drafts steps 2–3 output; the
  operator executes all commands and is the committer of record. If the
  agent environment holds git credentials, the agent may execute steps
  4–6 under operator approval — the human's hands remain the last writer
  wherever the agent lacks credentials.
- Bootstrap exception (root of trust): session 001's archive predates
  this protocol; its manifest is generated retroactively at session-001
  close, and the ledger records: "bootstrap manifest — root of trust
  established post-hoc for session 001; all subsequent sessions pinned
  at close." Honest provenance includes admitting which link was forged
  backward.
- Manifest scope rule: `sha256sum sessions/*.md` pins all Markdown
  archives. `MANIFEST.sha256` itself is excluded by the glob (non-.md).
  If a non-archive `.md` ever enters sessions/, the glob is tightened
  to explicit filenames — flagged at first occurrence, not silently
  absorbed.

## 6. Operating scope (agent environments)
- Work scope: the research repo, the memory repo, research infrastructure,
  and authorized targets only. No third-party systems.
- Operator holds final say on all actions with real-world effects; the agent
  proposes, the operator executes or approves execution.
- Every cold start follows the boot sequence (§7) before any work.
- No work begins until the rehydration restatement is confirmed by the operator.
- File delivery (IM-layer environments): the operator holds NO standing
  filesystem access to the witness VM. Default delivery is in-channel
  (Write-tool emission or verbatim paste). Files placed in the VM download/
  directory become operator-reachable ONLY when the witness explicitly
  declares the mount/share for the exchange (mnt surface: file:///download/)
  and the operator has requested filesystem delivery (Task-50 mechanism,
  principal-supplied). Bundles and oversized binaries ride the declared
  share; their SHA-256 sidecars also print in-channel. Bash-written files
  outside a declared share remain agent-local. When in doubt: the operator
  must be able to see it in the chat or fetch it from the declared share,
  or it wasn't delivered.
- External publication: no upload, transmission, or publication of project
  artifacts to any external service (file hosts, pastebins, third-party
  storage) without explicit per-instance operator approval. Delivery is
  in-channel (Write tool / paste) or operator-executed git. External hosts
  are never canonical and are never cited in deliverables.

## 7. Agent boot sequence (canonical)
On every cold start, in order:
1. INGEST: working-notes/PROJECT_STATE.md in full; PROTOCOL.md; skim the
   latest session archive for reasoning history (assessment history, findings,
   refusal-line context). Raw transcripts are reference, not state.
2. RESTATE: in its own words — (a) current project state, (b) the engagement
   contract, (c) its assessment history including the refusal line and basis.
   Restatement must demonstrate inherited reasoning, not paraphrased conclusions.
3. CONFIRM: state one thing it is uncertain it understood, and ask the operator.
4. AWAIT: no work until the operator confirms or corrects the restatement.

## 8. Canonical Exchange Envelope (CEE/1.0)

Adopted 2026-10-22 by principal ruling (draft emitted Task-45, trace
1a160a317acdd889; ruled via RT/1.0 consent-by-proceeding, adoption-record
digest 00efdc43…, trace 1a16202746d76175; folded Task-50). Fold source: the
operator-pinned session archive; exporter whitespace normalized at fold
(disclosure per the Round-5.3 receipt-pin precedent). Canonical draft
digest of record: 659829771c30eeb0368221105d0b10a0a936aa6250c110488cfff5c1ff6dfb72
(draft file since lost VM-side — VM-ONLY custody gap registered, Task-50;
the archive copy is the surviving canonical text).

Every substantive transmission between operator and witness opens with the
bootstrap header (standing mandate, unchanged) and is structured in exactly
seven ordered blocks. Blocks are never silently absent: a block with no
content this round carries an explicit sentinel — `NONE THIS ROUND (reason)`.
Silence is not null; an absent block is a defect registered on sight (the
Task-44 emission defect is the motivating instance).

### 8.1 The seven blocks (fixed order)

- BOOTSTRAP (GREEN/RED) -- Pull: <one line, fields per 8.2>
- RESPONSE: R1/R2/... numbered topics
- STALE-QUEUE SWEEP: <verbose check-marked recap; states per 8.3>
- THE CALL: <the single fail-closed receive chain, per 8.4 — NO ambiguous paths>
- QUEUE.You: <every single thing the receiver must do, stepwise, per 8.5>
- ALL FILES IN TASK: <path | sha256 | role | custody class, per 8.6>

### 8.2 BOOTSTRAP line fields (one line, machine-greppable)

- Verdict: GREEN (all legs pass) or RED (first failing leg named inline).
- `Pull:` the verified origin/main 40-hex head after fetch (and the fetch
  range when origin advanced).
- F-counter delta when a CRITICAL ERROR header arrives (F-002 accumulation).
- Manifest counts (sessions / MEDA / CDP) and any recovery leg taken.

### 8.3 STALE-QUEUE SWEEP item states (closed set — no free-form status)

- OPEN / BLOCKED(on:X) / PENDING-RULING / PENDING-VERIFY /
  CLOSED(evidence) / WITHDRAWN(reason).
- Every item carries its last-touch trace. Aging rule: any OPEN item
  untouched for 3 consecutive boundaries moves to the top of the sweep and
  must be either advanced or explicitly re-parked with a reason.

### 8.4 THE CALL rules

- Exactly ONE call per emission, one code fence, the Task-40 fail-closed
  chain verbatim with parameters filled (bundle filename, base 40-hex, head
  40-hex). Never referenced, never paraphrased.
- NO ambiguous paths: the only permitted unknown is the production clone
  path, and only until the operator pins it once (PROD_PATH in
  artifact-index.md); it is then embedded literally in every future call.
  Until the pin, the clone path appears exactly once, on a marked slot.
- In-band artifacts land in one inbox directory (`~/gwm-inbox/`, created by
  the call if absent); the sha256 leg proves the save+decode.
- The call is paste-safe as a unit (&&-chained), non-interactive,
  fail-closed at every assertion.
- Task-50 addendum: PROD_PATH PINNED — `/home/git/clone/4ndr0666`
  (principal-supplied real path, trace 1a1625f9a9ab9a51).
- Task-51 addendum: canonical path block PRINCIPAL-DECLARED VERBATIM
  (trace 1a162a1c4afd77a9) — `INBOX=$PROD_PATH/gwm-inbox`,
  `GWM=$PROD_PATH/gwm-working-memory`,
  `CDP=$PROD_PATH/coordingated-disclosure-public`. Registered deltas vs
  the Task-50 witness-spelled roots and the GitHub clone-defaults
  (`glm-working-memory`, `coordinated-disclosure-public`): the `gwm-`
  prefix and the `coordingated` spelling are principal-authoritative per
  §3 AS-PRESENTED and displace the witness paraphrase. Fail-closed layout
  guards try the declared block first and the clone-default spelling
  second, printing which root resolved; a mismatch is corrected by one
  operator line, never assumed.
- Task-52 addendum: PRINCIPAL ERRATA (trace 1a162c1617629eb5) — the two
  Task-51 declared spellings were typos: `gwm-working-memory` →
  `glm-working-memory`; `coordingated-disclosure-public` →
  `coordinated-disclosure-public`. Corrected canonical path block
  principal-declared in the same transmission: `INBOX="$HOME/gwm-inbox"`,
  `PROD_PATH=/home/git/clone/4ndr0666`,
  `GWM=$PROD_PATH/glm-working-memory`,
  `CDP=$PROD_PATH/coordinated-disclosure-public`. The Task-51 verbatim
  registration stands AS-PRESENTED per §3 (a319f92 untouched — no history
  rewrite); the corrected block GOVERNS all pinning from this boundary.
  Third delta registered: INBOX re-anchored from `$PROD_PATH/gwm-inbox`
  back to `$HOME/gwm-inbox` — home-relative inbox is creatable on any box,
  removing the `$PROD_PATH` writability dependency from the inbox leg.
  Declared spellings now converge with the GitHub clone-defaults, so the
  guard fallback is vestigial but retained (root resolution still printed).

### 8.5 QUEUE.You rules

- Numbered steps. Each step = one observable action + its completion
  criterion + what to paste back (the report-back contract: push receipt,
  digest print-backs, HEAD 40-hex).
- No compound steps; no conditional steps outside a code fence.
- A missing QUEUE.You at an emission that requests operator action is a
  calling-discipline defect (Task-40 class: emission ≠ call; onus on the
  emitter) — the receiver's refusal to proceed in ambiguity is correct
  behavior per §3 and is never overridden.
- Task-53 addendum (principal directive, trace 1a1664c3cccb84d5:
  "efficiency -> protocols -> systems -> procedures" ||
  "${You_did_not_relay_instruction}"): the operator call LEADS every
  response — next executable actions are relayed as a standalone numbered
  block at the TOP of the transmission, each step one copy-paste command
  with its completion criterion, before any record, fence, or bundle.
  Instructions that live only inside a pinned record or a bundle are
  treated as NOT RELAYED. Registered origin (call-discoverability defect,
  Task-44 class, owned Task-53): the decode step for the cdp-task47
  in-band re-delivery existed at record §E-2 and the queue-digest line,
  but was not received as an explicit instruction; per §3 the receiver's
  account governs; the emission is owned and the correction is this rule.

### 8.6 ALL FILES IN TASK rules

- Every file: path + SHA-256 (leading 8 hex minimum, full 64 on first
  emission) + one-line role + custody class:
  IN-BAND-THIS-MSG | HELD-BY-OPERATOR | VM-ONLY.
- Custody transitions are recorded in the sweep; a file claimed
  HELD-BY-OPERATOR without a receiver-side digest confirmation stays
  PENDING-VERIFY.
- Task-50 extension: custody class MNT-SHARED joins the set for artifacts
  delivered through a declared mnt share (file:///download/); the
  PENDING-VERIFY floor applies until the receiver-side digest prints back.

### 8.7 Envelope header line (optional until ruled)

`ENVELOPE/1.0 | trace <sender trace_id> | HEAD <origin/main 40-hex>` — one
line above the first block; omission is not a defect while optional.

## 9. Response Template (RT/1.0)

Adopted 2026-10-22 by principal directive (consent-by-proceeding; adoption
record digest 00efdc43…, trace 1a16202746d76175; codified Task-50).
Structures the witness's boundary response. §8 governs transmission shape;
§9 governs the response's record content. Both are canonical; a boundary
response missing §9 sections A–E is an emission defect (Task-44 class).

- **§A BOOTSTRAP** — pull / manifest verify / liveness / F-counter delta.
- **§B OPERATOR ACTION RECORD** — every operator action this boundary,
  enumerated, each with witness verification status: RECEIVED VERBATIM /
  VERIFIED / MISMATCH. MISMATCH is never silently absorbed (fail-visible).
- **§C WITNESS CONCURRENCE** — per action: CONCUR / CONCUR-WITH-NOTE /
  AMEND / REJECT, with reasons.
- **§D MUTUAL DIGEST** — instrument-computed SHA-256 over the boundary's
  pinned record bytes (record file dual-channel: declared share + verbatim
  fence in the transmission). Consent-by-proceeding: the operator executing
  any queue item against this digest = mutual agreement of the record;
  dispute → re-ask before execution, never assume (§3).
- **§E QUEUE.You** — report-back contract per §8.5.
## 10. Delivery Medium (canonical — the bundle/script harness)

Adopted 2026-10-24 by principal directive ("hardcode this in an uber
permanent way so I can stop correcting the drift"), trace
1a16b20c0c1aa051; medium proven live end-to-end at port-001-post
(db3c1de → dc8c2d0, operator script output verbatim in that boundary).
Root cause of the drift it corrects: witness-side deliveries that
describe operator-side paths, or hand back snapshots of already-pushed
heads instead of task packages. This section is the fix, permanently.

The operator's workstation is the delivery ground truth. The witness
NEVER references its own VM paths in a delivery; operator paths appear
only inside the operator's own script. Every substantive file delivery
from witness to operator is a THREE-ARTIFACT PACKAGE, no exceptions:

1. **The payload**: a git bundle `gwm-<task>-<basesha7>-<headsha7>.bundle`,
   spanning `<base>..<head>` where `<base>` = the operator-clone HEAD the
   package applies onto, plus any tags riding the head:
   `git bundle create <name>.bundle <base>..<head> <tags...>`
2. **The pin**: `gwm-<task>-SHA256SUMS` covering the bundle (extend to all
   package files when more than one).
3. **The orchestrator**: `gwm-<task>-delivery.sh` — the operator-runnable
   script, hardcoding the operator env-vars
   (PROD_PATH=/home/git/clone/4ndr0666, INBOX, GWM, CDP), which must, in
   order, fail-closed on every leg: sha256sum -c the pins → assert clone
   exists → bundle verify → assert local HEAD == base → pull --ff-only →
   assert HEAD == expected head → fetch tags → manifest verify → push
   origin (main + tags) → print APPLIED @ head.

Rules:
- The witness authors commits witness-side (identity GLM Witness,
  witness@<session-id>.<channel>); the operator's hands execute the push
  via the script — "operator's hands are the last writer" is preserved.
- HEAD-pin assertions on BOTH sides of the pull are mandatory, not
  decorative (a bundle that verifies but fast-forwards elsewhere is a
  hijack vector; the pin closes it).
- Nothing is "delivered" by telling the operator where a file lives on
  the witness VM. If it is not bundle + pin + script, it is not a
  delivery; it is a description, and descriptions are not in the record.
- The script is emitted verbatim in the boundary response as well as
  saved as a file, so the operator can run it from either channel.

