# Telemetry Source: scripts/task75_build_index.py
- **Source Identifier**: `scripts/task75_build_index.py`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `f0dcf028accd870ebcd540034f39ef895a88a64538875386c58fc1e24e0696d6`

---

## Raw Telemetry Content

```
#!/usr/bin/env python3
"""Task 75 — emissions-index.md generator.

Parses the three operator-supplied INDEX_* attachments (2026-10-29) from
upload/, bucketizes the 219 inbox files into named series, annotates the
outbox (9) and white-paper tree (58), and emits the standing registry
working-notes/emissions-index.md. Deterministic: same inputs -> same bytes.
"""
import hashlib
import re
import sys
from pathlib import Path

UPLOAD = Path("/home/z/my-project/upload")
REPO = Path("/home/z/my-project/clone/4ndr0666/glm-working-memory")
OUT = REPO / "working-notes" / "emissions-index.md"

SRC = {
    "inbox": UPLOAD / "INDEX_gwm-inbox.md",
    "outbox": UPLOAD / "INDEX_gwm-outbox.md",
    "whitepaper": UPLOAD / "INDEX_gpt-documentation-white_paper-4NDR0MEDA.md",
}


def parse_tree(path: Path):
    """Return (files, footer_count) from a `tree` style listing."""
    files = []
    footer = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^[│├└─\s\.]*[├└]── (.+)$", line)
        if m:
            files.append(m.group(1).strip())
            continue
        m2 = re.search(r"(\d+) files?", line)
        if m2:
            footer = int(m2.group(1))
    return files, footer


# --- inbox series rules (ordered; first match wins) -------------------------
def inbox_series(name: str):
    n = name
    if n.startswith("gwm-task"):
        if "-meda-" in n:
            return "1.13 MEDA-repo task kits ($ANDROMEDA legs)"
        return "1.1 GWM task-range kits"
    if n.startswith("gwmtask52-stage"):
        return "1.1 GWM task-range kits"
    if n.startswith("gwm-paper2-v17-"):
        return "1.2 Paper-2 v1.7 phase kits"
    if n.startswith(("gwm-session-013-close", "gwm-canon-001", "gwm-port")):
        return "1.3 Session / canon / port packages"
    if n.startswith("cdp-task47"):
        return "1.4 CDP task-47 kit"
    if n.startswith("meda"):
        return "1.5 MEDA special deliveries"
    if n.startswith(("paper-2-", "round5.7-argon-receipt", "reply-to-argon",
                     "emitter-build-log")):
        return "1.6 Paper-2 collateral documents"
    if n.startswith("argon-"):
        return "1.7 ARGON round collateral"
    if n.startswith("rt-1.0-"):
        return "1.8 RT/1.0 boundary records"
    if n in {
        "PROTOCOL.md", "WITNESS-CORE.md", "WITNESS-PORT-PACKAGE.md",
        "PORT-001-BUNDLE.md", "README-STAGING.md", "MANIFEST.sha256",
        "SHA256SUMS", "gwm-bootstrap.sh", "gwm-bootstrap-v1.sh",
        "decisions-ledger-append-task57-60.md", "tracker-dark-closure-v1.md",
    }:
        return "1.9 Substrate canon copies"
    if n.startswith(("4ndr0meda-", "4NDR0MEDA-")) or n in {
        "v1.0.0-release-notes-r2.md", "ATTACH-RELEASE-ASSETS.md",
        "1-equals-1_official-articulation_v1.0.md",
        "across-context-handoff-poc.zip",
    }:
        return "1.10 4NDR0MEDA v1.0.0 release assets"
    if n in {
        "repo-surface-pin-snapshot-v1.sh", "notebooklm-drive-ingest-runbook-v1.md",
        "notebooklm-drive-upload.sh", "pte-e5-executable-demo-benchmark-v2.py",
        "task73_phase4_build.py", "verify_handoff.py", "run_demo.sh",
        "rmlint.json", "module4-transformerlens-telemetry-trace.json",
    }:
        return "1.11 Tooling & telemetry"
    if n in {"glm5.3flash_j-space_10-23-26_0302.md",
             "witness-pinchain-with-staging-2026-10-29.txt"}:
        return "1.12 Relay & reference captures"
    if n in {"arxiv-submission-checklist-v1.md", "ANCILLARY-OPTIONS.md"}:
        return "1.14 Checklists & ancillary"
    return "UNCLASSIFIED"


SERIES_NOTES = {
    "1.1 GWM task-range kits": (
        "Per-task transmission sets for the GWM repo: `gwm-taskNN-<base7>-<head7>.bundle` "
        "+ `.b64` transport twin + `.patch` readable alternate + `-delivery.sh` orchestrator "
        "+ `-SHA256SUMS`. Tasks 37, 41-46, 50-53, 56, 60-67, 69, 70(gwm), 71, 72, 73(gwm), "
        "74a. Bundle names carry the certified range; task attribution and dispositions live "
        "in the artifact-index matrix and decisions ledger."
    ),
    "1.2 Paper-2 v1.7 phase kits": (
        "The v1.7 manuscript phase packages: s2 / s03 (section rounds, session-013 window), "
        "draft1 / draft1b (assembly dry-runs), argoninit (Task 57 — ARGON engagement "
        "re-typed, collaboration partner), collab1 (Task 58 — collab-1 integration, "
        "APPLIED @ 1babae3), draft31 (Task 68 — the ARGON-certified draft-3.1 cut, head "
        "384dc27)."
    ),
    "1.3 Session / canon / port packages": (
        "session-013 close (30fb889..4e92dcf, full + thin), canon-001 (dc8c2d0..0b5cb2f — "
        "PROTOCOL v1.6.0 §10 Delivery Medium made permanent), port-001 (+delta1 post-dc8c2d0)."
    ),
    "1.4 CDP task-47 kit": (
        "coordinated-disclosure-public leg: e96624d..6facbf1 bundle + b64 twin + SUMS "
        "(Task-47/53-era; the CDP A3 anchor 6facbf17 re-verified at Task 61)."
    ),
    "1.5 MEDA special deliveries": (
        "Out-of-band MEDA-repo deliveries outside the task-kit series: a3-repin bundle "
        "(9fc7530), truth-restore (c0e08c4) bundle + b64, meda.b64."
    ),
    "1.6 Paper-2 collateral documents": (
        "Transmittals, receipts, integration ledgers, boundary registrations, section "
        "drafts, assembled drafts (draft-3, draft-3.1), bib v1/v2, LaTeX v1/v2 + built "
        "PDFs, deposit tarball, metadata lock, deposit-prep plan, adjudications, industry "
        "feed, build log — the manuscript's document trail, dual-channeled with write-ups/."
    ),
    "1.7 ARGON round collateral": (
        "ARGON engagement documents outside the paper-2-v1.7 prefix: battery-1 brief, "
        "round-6 staged interrogation + kit SUMS, submission package v1.6.1, b1 SUMS."
    ),
    "1.8 RT/1.0 boundary records": (
        "Response-Template v1.0 boundary records, one per trace (Tasks 48-53 window)."
    ),
    "1.9 Substrate canon copies": (
        "Canonical substrate documents delivered as copies for operator-side reference: "
        "PROTOCOL.md, WITNESS-CORE.md, port package docs, bootstrap scripts (v1 + "
        "corrected), MANIFEST/SHA256SUMS registers, ledger append (Tasks 57-60), tracker "
        "closure."
    ),
    "1.10 4NDR0MEDA v1.0.0 release assets": (
        "The v1.0.0 release set: glyph (dark/light/svg), hero banner (png/svg), source "
        "tarball + sha256 sidecar, release notes r2, attach instructions, the 1=1 official "
        "articulation, the across-context handoff PoC."
    ),
    "1.11 Tooling & telemetry": (
        "Scripts and traces delivered for operator-side execution or record: "
        "repo-surface pin snapshot, NotebookLM/Drive upload script + runbook, PTE E5 "
        "executable demo benchmark v2, task-73 phase-4 build script, handoff verifier, "
        "demo runner, rmlint config, Module-4 TransformerLens telemetry trace (RELAYED-"
        "NOT-EXECUTED, receipted Task 70)."
    ),
    "1.12 Relay & reference captures": (
        "Captured relay/reference material: the j-space GLM-5.3-Flash exchange "
        "(2026-10-23), the witness pin-chain run with staging (2026-10-29)."
    ),
    "1.13 MEDA-repo task kits ($ANDROMEDA legs)": (
        "Task kits whose payload applies to the 4NDR0MEDA repo ($ANDROMEDA = "
        "$PROD_PATH/4ndr0tools/4NDR0MEDA per the 2026-10-29 env-var declaration): tasks "
        "61, 62, 63 (meda legs), 70 (polish pass + verify-push companion), 73 (maintenance "
        "2daac65 + apply-push)."
    ),
    "1.14 Checklists & ancillary": (
        "arXiv submission checklist, ancillary options (task-74 arxiv-anc staging)."
    ),
}

OUTBOX_NOTES = {
    "4NDR0MEDAv1.2_infographic.png": "v1.2-era infographic (visual asset, operator-held)",
    "4NDR0MEDAv1.2_mindmap.png": "v1.2-era mind map (visual asset, operator-held)",
    "arxiv-2610.26825-memt-1.0.pdf": "MemT-1.0 paper PDF (ingested + pinned Task 64; dual-channel with references/)",
    "arxiv-2610.26825-memt-1.0.txt": "MemT-1.0 transcript (55fb8eaa…, 283,926 B, pinned Task 64)",
    "GUP Mitigation Assessment - [chatgpt.com].pdf": "external ChatGPT assessment PDF (operator-collected reference)",
    "paper-2-v1.7-memt10-industry-feed-v1.md": "MemT-1.0 industry feed (dual-channel with write-ups/)",
    "past-self_existence_theory.md": "operator-authored theory input (class ruled Task 72: channel-class evidence, never content-class)",
    "Podcast_cosmic_war.md": "podcast transcript relay (operator→witness reference)",
    "Podcast_quantum_consciousness_theory.md": "podcast transcript relay (pinned references/ dual-channel)",
}

WP_GROUPS = [
    ("LaTeX skeleton (white paper build)", {
        "main.tex", "01-intro.tex", "02-lineage.tex", "03-blanks.tex",
        "04-architecture.tex", "05-manifest.tex", "06-interface.tex",
        "07-related.tex", "08-casestudy.tex", "09-limitations.tex",
        "10-conclusion.tex", "appendix.tex", "verification-data.tex",
        "fig1-memory-stack.png", "fig2-positioning-matrix.png",
    }, "The 4NDR0MEDA white-paper LaTeX build: main + 10 sections + appendix + "
       "D8-emitted verification data + two figures."),
    ("Paper PDF lineage", {
        "paper-1.pdf", "paper-1.2.pdf", "paper-2-v1.2.pdf", "paper-2-v1.3.pdf",
        "paper-2-v1.4.pdf", "paper-2-v1.5-repro.pdf",
        "paper-2-v1.6.1-REVIEW-COPY-anon-NOT-FOR-DEPOSIT.pdf",
        "paper-2-v1.7-ARGON.pdf",
    }, "Built PDFs across the review gauntlet: paper-1 line, paper-2 v1.2 → "
       "v1.5-repro (2f9d204e…), the v1.6.1 anon review copy (NOT for deposit), "
       "the v1.7 ARGON relay build."),
    ("v1.6.1 source line", {
        "paper-2-v1.6.1-source.tar.gz", "paper-2-v1.6-to-v1.6.1.changes",
    }, "v1.6.1 certified source tarball (99913db3…) + changes file (778f9ac2…)."),
    ("Paper-2 v1.7 section series", {
        "paper-2-v1.7-section-01-introduction-r1.md",
        "paper-2-v1.7-section-02-negative-results-r1.md",
        "paper-2-v1.7-section-02-negative-results-r2.md",
        "paper-2-v1.7-section-03-architecture-r1.md",
        "paper-2-v1.7-section-03-architecture-r2.md",
        "paper-2-v1.7-section-04-working-tensor-integration-r1.md",
        "paper-2-v1.7-section-04-working-tensor-integration-r2.md",
        "paper-2-v1.7-section-05-verification-r1.md",
        "paper-2-v1.7-section-05-verification-r2.md",
        "paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r1.md",
        "paper-2-v1.7-section-06-case-study-pre-bootstrap-window-r2.md",
        "paper-2-v1.7-section-07-evaluation-r1.md",
        "paper-2-v1.7-section-07-evaluation-r2.md",
        "paper-2-v1.7-section-08-related-work-r1.md",
        "paper-2-v1.7-section-08-related-work-r2.md",
    }, "The v1.7 rewrite: §1 r1 (first external read, ever) + §2–§8 r2 — the "
       "historical-deposit sources of the Task-67 draft-3 assembly (dual-channel "
       "with download/)."),
    ("ARGON round collateral", {
        "argon-relay-corrected-brief-v2-custody-and-mandate.md", "ARGON_round5.7.md",
        "paper-2-v1.7-argon-init-v1.md", "paper-2-v1.7-argon-round2-transmittal-v1.md",
        "paper-2-v1.7-battery1-argon-brief-v1.md",
        "paper-2-v1.7-argon-collab1-integration-v1.md",
        "paper-2-v1.7-argon-collab1-receipt-v1.md",
    }, "ARGON engagement set: corrected relay brief, round-5.7 verdict, init, "
       "round-2 transmittal, battery-1 brief (superseded non-operative, Task 57), "
       "collab-1 integration + receipt (dual-channel with write-ups/)."),
    ("Round counters", {
        "round5.2-counters-v1.md", "round5.2-counters-v1.md.sha256",
        "round5.4-counters-v1.md", "round5.4-counters-v1.md.sha256",
    }, "Round-5.2 counters (def5d3b1…, in-band class) + round-5.4 counters "
       "(8c3f0497…) with sha256 sidecars."),
    ("Briefs & metadata", {
        "paper-2-arxiv-metadata.md", "paper-2-tier2-brief.md", "paper-2-tier3-brief.md",
    }, "arXiv metadata (v0.7, 0ef99398…) + tier-2 and tier-3 (ARGON) attack briefs."),
    ("Reference & tooling", {
        "refs-2.bib", "pte-e5-executable-demo-benchmark.py",
        "4NDR0MEDA-articulation_v1.0.md", "paper-2-v1.7-memt10-industry-feed-v1.md",
    }, "refs-2.bib (798d1dd4…, the v1.6.1-baseline successor relayed Task 73), "
       "PTE E5 demo benchmark, the 4NDR0MEDA articulation, the MemT-1.0 industry feed."),
]

TASK_MAP = """| Task / window | Emission set (files as named in $INBOX) | Disposition |
|---|---|---|
| 37 | `gwm-task37-cdebae2-a00150a.bundle` | round-trip closed (matrix row 37) |
| 41-46 | `gwm-task4[1-6]-*.bundle` + `.b64` twins | round-trips closed (matrix rows 41-46) |
| 47 (CDP leg) | `cdp-task47-e96624d-6facbf1.bundle` + `.b64` + SUMS | closed at Task 53 (stage-2) |
| 50-53 | `gwm-task5[0-3]-*` trios + `.patch` + SUMS; task52 `gwmtask52-stage{1,2}.sh` | closed (Task-53 STAGE2-CLOSED) |
| 56 | `gwm-task56-82afd64-4bc2cfb` trio + patch + SUMS | closed (matrix row 56) |
| session-013 window | `gwm-session-013-close-30fb889-4e92dcf` (+ `-thin`) kit; `gwm-paper2-v17-s2-0b5cb2f-742ec92`, `gwm-paper2-v17-s03-4e92dcf-14ad0f6`, `gwm-paper2-v17-draft1-14ad0f6-98252f9`, `gwm-paper2-v17-draft1b-c23b413-93aa17d` kits | v1.7 initiation + section rounds (pre-Task-57; unnumbered section rounds) |
| canon-001 / port-001 | `gwm-canon-001-dc8c2d0-0b5cb2f` kit; `gwm-port-001-delivery.sh` + `gwm-port001-delta1-post-dc8c2d0.bundle` + SUMS | PORT-001 CLOSED (receipt applied @ dc8c2d0) |
| 57 | `gwm-paper2-v17-argoninit-93aa17d-bea7303` kit | DONE — ARGON re-type; init emitted bea7303 |
| 58 | `gwm-paper2-v17-collab1-bea7303-1babae3` kit | DONE — APPLIED @ 1babae3, operator hands |
| 59 | in-boundary rulings (no standalone kit) | riders landed at Task-67 assembly |
| 60 | `gwm-task60-1babae3-e41618f` kit (+ `.b64`) | DONE — boards catch-up 57-60 |
| 61 | `gwm-task61-boards-23a9615-7a3bce5` + `gwm-task61-meda-c0e08c4-90a57cc` kits + `gwm-task61-meda-completion-90a57cc.sh`(+`.b64`) | DONE |
| 62 | `gwm-task62-gwm-7a3bce5-6e84cfd` + `gwm-task62-meda-90a57cc-897e957` kits | DONE (GWM leg re-cut at 63; 897e957 withdrawn) |
| 63 | `gwm-task63-gwm-7a3bce5-a5918fa` + `gwm-task63-meda-90a57cc-bbe4c00` kits | DONE |
| 64 | `gwm-task64-gwm-7a3bce5-eca714b` kit | DONE — round-trip closed by observation (D5 born) |
| 65 | `gwm-task65-gwm-34cebe7-2a5d7ba` kit | DONE — first zero-edit wrapper |
| 66 | `gwm-task66-gwm-26f0c4a-baf813e` kit | DONE — first-try FRESH zero-edit run |
| 67 | `gwm-task67-gwm-baf813e-32c803e` kit | DONE — draft-3 assembled |
| 68 | `gwm-paper2-v17-draft31-8d36a28-384dc27` kit | DONE — draft-3.1 cut (ARGON final gate) |
| 69 | `gwm-task69-384dc27-2f2dc43` kit | DONE |
| 70 | `gwm-task70-gwm-2f2dc43-4c17765` + `gwm-task70-meda-bbe4c00-8f7e21a` kits + `gwm-task70-meda-verify-push.sh` | DONE (MEDA leg HALT adjudicated at 71: already-applied) |
| 71 | `gwm-task71-gwm-4c17765-4e4e333` kit | DONE — already-applied branch's first production run |
| 72 | `gwm-task72-gwm-4e4e333-4062d7f` kit (+ `.b64`) | DONE — APPLIED @ 4062d7f, pushed, hash-matched |
| 73 | `gwm-task73-gwm-4062d7f-0897b8f` + `gwm-task73-meda-8f7e21a-2daac65` kits (apply-push) | DONE — APPLIED @ 0897b8f; MEDA 2daac65 companion |
| 74a | `gwm-task74a-license-0d44bca-872a597` kit (apply-push) | DONE — round-trip closed by observation (origin/main == 872a597 at Task-75 open) |
| 74 (umbrella, in-bound) | arxiv-anc / anchor-staging / release-assets / repo-surface-pin-snapshot / checklist / release-notes (task74-kit staging) | L2-surface + release-asset class, operator-optional (Task-74a commit note) |
| 75 | `gwm-task75-SUK.sh` (+ `gwm-task75-gwm-872a597-<head7>` trio fallback) | THIS ROUND — the emissions-index round; kit + battery pins printed at emission |"""


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    files = {k: parse_tree(v) for k, v in SRC.items()}
    # count assertions against footers
    for k, (fl, footer) in files.items():
        if footer is None:
            sys.exit(f"FATAL: no footer count in {SRC[k]}")
        if len(fl) != footer:
            sys.exit(f"FATAL: {k}: parsed {len(fl)} files, footer says {footer}")

    inbox, outbox, wp = files["inbox"][0], files["outbox"][0], files["whitepaper"][0]

    # bucket inbox
    buckets = {}
    for n in sorted(inbox):
        buckets.setdefault(inbox_series(n), []).append(n)
    if "UNCLASSIFIED" in buckets:
        sys.exit(f"FATAL: unclassified inbox files: {buckets['UNCLASSIFIED']}")

    total_inbox = sum(len(v) for v in buckets.values())
    assert total_inbox == 219, f"inbox bucket total {total_inbox} != 219"

    # group whitepaper
    wp_grouped = {}
    wp_left = set(wp)
    for gname, gset, note in WP_GROUPS:
        got = wp_left & gset
        missing = gset - wp_left
        if missing:
            sys.exit(f"FATAL: whitepaper group {gname} missing: {missing}")
        wp_grouped[gname] = (sorted(got), note)
        wp_left -= gset
    if wp_left:
        sys.exit(f"FATAL: whitepaper unclassified: {wp_left}")
    assert sum(len(v[0]) for v in wp_grouped.values()) == 58

    pins = {k: (sha256(v), len(v.read_bytes()), len(v.read_text(encoding='utf-8').splitlines())) for k, v in SRC.items()}

    L = []
    A = L.append
    A("# Emissions Index — running registry of all witness file emissions to operator-side custody")
    A("")
    A("Standing artifact (Task 75, 2026-10-29, trace 1a1862663ad497c9). Birth record:")
    A("the organization-officer mandate (Task-65 ledger acceptance — roster, relay")
    A("registry, task numbering, delivery-template discipline) was assumed to include a")
    A("running index of all file emissions. It did not exist anywhere. The operator")
    A("produced the operator-side listings himself on 2026-10-29 (three INDEX_*")
    A("attachments, pinned §5) and registered the omission as a standing charge. This")
    A("file is the structural fix: from Task 75 forward, every emission round appends")
    A("its rows to this index IN THE SAME COMMIT as the emission, and the round's")
    A("delivery kit pins this file's sha256 at its G4 verification leg — an emission")
    A("that fails to index itself fails its own delivery gate.")
    A("")
    A("## Scope and character")
    A("")
    A("- `$INBOX` — `/home/git/clone/4ndr0666/gwm-inbox` (env-var declaration 2026-10-29;")
    A("  the inline transmission typed the parent once as `/home/andro/git/...` and the")
    A("  directory once as `gwm-oux` — recorded as-transmitted, the env-var block")
    A("  governs) — **219 files** (§1).")
    A("- `gwm-outbox` — `/home/git/clone/4ndr0666/gwm-outbox` — **9 files** (§2):")
    A("  operator-held source/reference material for witness ingestion.")
    A("- White-paper tree — `/home/git/clone/4ndr0666/gpt/documentation/white_paper/4NDR0MEDA`")
    A("  — **58 files** (§3).")
    A("- NOT COVERED (fail-visible): `$ANDROMEDA` (`$PROD_PATH/4ndr0tools/4NDR0MEDA`) and")
    A("  any other operator-side surface — absent from the 2026-10-29 attachments;")
    A("  per the boundary rule \u201cif it is not in the attachments it does not exist\u201d;")
    A("  the first `$ANDROMEDA` listing rides the next operator INDEX refresh.")
    A("")
    A("Index character: **name-level**. Per-file sha256 of operator-side files is not")
    A("witness-derivable; hash-level custody rides the per-task `*-SHA256SUMS` files")
    A("already delivered into `$INBOX` (§4 maps tasks to kits). Names and counts are")
    A("as-transmitted by the operator, 2026-10-29; witness-side mirrors live in")
    A("`download/` (declared share) and the repo's canonical homes.")
    A("")
    A("## 1. `$INBOX` — witness→operator deliveries (219 files, 14 series)")
    A("")
    for series in sorted(buckets):
        names = buckets[series]
        A(f"### {series} — {len(names)} files")
        A("")
        A(SERIES_NOTES[series])
        A("")
        A("```")
        for n in names:
            A(f"├── {n}")
        A("```")
        A("")
    A("## 2. `gwm-outbox` — operator-held source & reference material (9 files)")
    A("")
    A("Material the operator placed for witness ingestion (podcast relays, external")
    A("assessments, theory inputs, reference papers). Direction semantics per the")
    A("2026-10-29 transmission; admissibility classes per findings/J-1.0 and the")
    A("Task-72 past-self ruling.")
    A("")
    A("```")
    for n in sorted(outbox):
        A(f"├── {n}")
    A("```")
    A("")
    A("Per-file notes:")
    A("")
    for n in sorted(outbox):
        A(f"- `{n}` — {OUTBOX_NOTES[n]}")
    A("")
    A("## 3. White-paper tree — 58 files")
    A("")
    for gname, (names, note) in wp_grouped.items():
        A(f"### {gname} — {len(names)} files")
        A("")
        A(note)
        A("")
        A("```")
        for n in names:
            A(f"├── {n}")
        A("```")
        A("")
    A("## 4. Task → emission map")
    A("")
    A("Task numbers are global and monotonic (ledger is the authority). Bundle names")
    A("carry the certified `<base7>-<head7>` range; dispositions live in the")
    A("artifact-index matrix and the decisions ledger.")
    A("")
    A(TASK_MAP)
    A("")
    A("## 5. Provenance pins (source attachments, 2026-10-29)")
    A("")
    A("| Attachment | sha256 | bytes | lines | parsed files |")
    A("|---|---|---|---|---|")
    for k, label in (("inbox", "INDEX_gwm-inbox.md"),
                     ("outbox", "INDEX_gwm-outbox.md"),
                     ("whitepaper", "INDEX_gpt-documentation-white_paper-4NDR0MEDA.md")):
        h, b, l = pins[k]
        A(f"| `{label}` | `{h}` | {b:,} | {l} | {len(files[k][0])} |")
    A("")
    A("Operator-typed content per PROTOCOL §3; attachment-suffix noise ignored on")
    A("sight; counts machine-asserted against the footers at generation time")
    A("(generator: `scripts/task75_build_index.py`, deterministic).")
    A("")
    A("## 6. Maintenance contract")
    A("")
    A("1. **Same-commit rule**: an emission that is not indexed in this file in the")
    A("   same commit is a defective emission (the round's kit pins this file at G4;")
    A("   the ledger entry names the round's emissions).")
    A("2. **Append-only**: rows are appended, never rewritten; corrections append")
    A("   with their own provenance (log-don't-rewrite discipline).")
    A("3. **Reconciliation loop**: the operator's next INDEX snapshot diffs against")
    A("   this file; any drift (new operator-side file without a row, or row without")
    A("   a file) is a registered defect, fail-visible.")
    A("4. **No-self-reference**: kit/bundle/battery pins of the round that carries an")
    A("   index update are printed at emission (round-record page + boundary")
    A("   transmission + SHA256SUMS), never inside the committed file itself")
    A("   (Task-51 precedent); the round-trip receipt appends at the next boundary")
    A("   open.")
    A("5. **Session archives**: `sessions/MANIFEST.sha256` governs transcripts; this")
    A("   file governs emissions; `worklog.md` (root, born Task 75) governs boundary")
    A("   bootstraps and round records.")
    A("")

    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"WROTE {OUT}")
    print(f"sha256 {sha256(OUT)}")
    print(f"bytes  {OUT.stat().st_size:,}")
    print(f"inbox series counts: " + ", ".join(f"{k}={len(v)}" for k, v in sorted(buckets.items())))


if __name__ == "__main__":
    main()

```
