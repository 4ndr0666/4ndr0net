# Telemetry Source: working-notes/notebooklm-drive-ingest-runbook-v1.md
- **Source Identifier**: `working-notes/notebooklm-drive-ingest-runbook-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `18ee9b185a5a8214ea6df680587a0d7943e0d8515ed6d7ddc693c85db306d7b7`

---

## Raw Telemetry Content

# NotebookLM Drive-Ingest Runbook, v1 (Task-73)

**Date:** 2026-10-29 (UTC) · **Witness:** GLM (Z.ai), designation Witness
**Trace:** `1a184806a91640c9` · **Trigger:** operator item 5 — "look through
the AUR for something better [than rclone] (tried gdrive,
google-workspace-cli, etc). … Can upload a bundle; I need the full complete
folders. The reason … is NotebookLM … it only 'skims' the first layers of
online repos with no recursion … Only by uploading all the info to Google
Drive will it truly have recursive abilities."

**Context of record:** NotebookLM's role in the three-node topology is
formalized (Task-69: sourcing arm + derived-artifact foundry) and the repos
are bound as live ingestion sources — so the ingestion channel's mechanics
are now program-relevant, not operator convenience. This runbook is the
working answer; claims carry their verification status (web-search-verified
this boundary vs. witness prior knowledge, fail-visible per the house
discipline).

---

## 1. Why full folders, not bundles — the NotebookLM ingestion model

A bundle (`.tar.gz`, `.zip`) uploaded to Drive is a **dead end for
NotebookLM**: it ingests *sources*, one file at a time, and has no unzip
step. The operator's instinct is correct and is now the rule of record:
**full complete folder trees of real files.** The GitHub-URL source type
indexes only the repository's surface layers (README and top-level files —
the operator extracted this admission from NotebookLM directly), so the
program's repos cannot ride the GitHub channel for deep context either.
Drive is the only recursive channel. [search-verified 2026-10-29: Google
support + blog.google source-type docs; operator's own NotebookLM probe]

What Drive-feeding buys, concretely:

- **Per-file sources with real content** — the whole tree, recursively.
- **Drive-connected sources stay fresh** — NotebookLM re-syncs Drive-linked
  sources when the file changes in Drive, which matches the program's
  append-only repo cadence far better than manual re-uploads.
  [search-verified 2026-10-29]
- **Folders inside notebooks** (up to ~50 per notebook) organize sources
  without extra notebooks. [search-verified 2026-10-29, nlmtools guide]

## 2. The limits that shape the pipeline [search-verified 2026-10-29]

| Limit | Free tier | Notes |
|---|---|---|
| Sources per notebook | 50 | paid tiers raise this (some plans to ~300–600); one notebook cannot hold a whole repo tree either way |
| Words per source | 500,000 (or 200 MB) | the largest repo files fit comfortably |
| Notebooks | 100 | split by repo / by paper-2 phase / by evidence class |
| Folders per notebook | ~50 | organizational only |

Consequence: **plan the notebook split before uploading** — e.g. one
notebook per repo (GWM / MEDA / CDP / userscripts), with the paper-2
write-ups as their own notebook, rather than one mega-notebook that hits the
50-source cap at 3% coverage.

## 3. File-type gate (what actually ingests)

Supported source types relevant to the program's trees
[search-verified 2026-10-29, Google support + blog.google]:

- **Directly ingestible:** `.md`, `.txt`, `.pdf`, `.docx`, images
  (png/jpg/webp/…), audio, Google Docs/Slides/Sheets, YouTube, web URLs.
- **NOT ingestible (must convert first):** `.tex`, `.bib`, `.skill`,
  `.bundle`, `.diff`, `.json` (renders as text but is noise — convert),
  code files generally (they ingest as plain text only via the GitHub
  channel's syntax handling; on Drive they are just text).

Conversion one-liners (witness-side, pre-upload):

```sh
# .tex -> .md (pandoc; the deposit .tex converts cleanly — tested class:
# pandoc handles the article-class preamble + thebibliography)
find "$TREE" -name '*.tex' -exec sh -c 'pandoc -f latex -t gfm "$1" -o "${1%.tex}.md"' _ {} \;

# .bib -> .txt (plain text is ingestible; keep the original alongside)
find "$TREE" -name '*.bib' -exec sh -c 'cp "$1" "${1}.txt"' _ {} \;
```

The `.bundle`/`.skill`/binary evidence objects stay uploaded (Drive keeps
them for the record) but are not NotebookLM sources; their *ledgers* (the
`.md` receipts) are the ingestible surface — which is exactly what the
program's manifest discipline already produces.

## 4. The AUR landscape — is there anything better than rclone? [prior
knowledge + 2026-10-29 search pass; verify live per §5]

Straight answer: **for one-shot, recursive, resumable, integrity-checked
upload of complete folder trees, nothing on AUR beats rclone.** The
alternatives each lose on the axis this task cares about:

| Tool | Where | Class | Verdict for this job |
|---|---|---|---|
| `rclone` | [extra] | CLI, Apache | **the tool** — recursive by default, checksummed, resumable, rate-limit-aware; the search consensus ("rockin'", "success using rclone") matches witness experience |
| `rclone-browser` | AUR | Qt GUI over rclone | the GUI answer without losing rclone's engine — drive it manually per folder |
| `google-drive-ocamlfuse` | [extra] | FUSE mount | mount + `cp -r`/`rsync` works, but per-file round-trips make big trees slow and 403-prone; fine for browse, wrong for bulk |
| `insync` | AUR, **paid** | sync daemon | the only serious commercial Linux Drive client left; bidirectional continuous sync — worth it only if the Drive mirror must stay live without scripting |
| `overgrive` | AUR, paid | sync client | cheap but long-stale; not recommended for large trees |
| `gdrive` | AUR | CLI | upstream archived/deprecated — the operator already hit this |
| `google-workspace-cli` | AUR | CLI | the operator already tried it; Drive-uploading whole trees is not its strength |
| `drive` (odeke) | AUR | CLI | abandoned for years |
| restic/kopia/duplicati | [extra] | backup | they *do* upload to Drive — as deduplicated object blobs, i.e. the "bundle" problem again: not browsable, not ingestible. Ruled out by §1 |

So: rclone stays, not for lack of looking but because the job is rclone's
design center. The improvements that matter are (a) the tuned invocation
below (rate-limit armor for Google's per-user quotas), (b) the pre-conversion
gate from §3 so the tree that lands in Drive is already NotebookLM-ready,
and (c) the notebook split from §2.

## 5. The pipeline (copy-paste)

```sh
# One-time: configure the Drive remote (browser OAuth)
rclone config            # n) new remote -> drive -> OAuth flow

# Stage 1 — build the NotebookLM-ready tree (originals untouched):
#   copy tree, convert .tex/.bib per §3, drop .git and build noise
rsync -a --exclude='.git' --exclude='*.aux' "$TREE/" "$TREE-nlm/"

# Stage 2 — full recursive upload (the tuned command):
rclone copy "$TREE-nlm" "gdrive:notebooklm/<name>" \
  --transfers 8 --checkers 16 --fast-list \
  --drive-chunk-size 64M \
  --tpslimit 10 --drive-pacer-burst 100 \
  --retries 5 --low-level-retries 20 \
  --checksum --update --progress

# Stage 3 — verify the tree landed, recursively:
rclone lsf -R "gdrive:notebooklm/<name>" | wc -l   # compare to local count
```

Why each flag (the "better than default rclone" the operator asked for):
`--tpslimit 10` + `--drive-pacer-burst 100` are the rate-limit armor
(Google's per-user query quota is what kills naive bulk uploads with 403s);
`--drive-chunk-size 64M` cuts per-file upload API calls for the large PDFs;
`--fast-list` halves listing calls on big trees; `--checksum` makes the
upload integrity-checked (Drive MD5) rather than size-only; `--update` makes
re-runs idempotent — the same append-only discipline the program's bundles
use. A ready-to-run copy rides this delivery as
`notebooklm-drive-upload.sh` (kit + `download/`, sha256 registered in §7).

Package AUR/live-status check one-liners (verify §4's table on your box):

```sh
pacman -Ss rclone google-drive-ocamlfuse   # [extra] entries
paru -Ss rclone-browser insync overgrive   # AUR entries + votes/maintenance
```

## 6. NotebookLM-side wiring (operator's hands)

1. In the target notebook: *Add source → Google Drive* → navigate the
   uploaded folder; multi-select files (or the folder — 2026-era UI accepts
   Drive folders as source containers). [search-verified for the general
   capability; exact UI mutates — fail-visible note]
2. Mind the 50-source cap per notebook (free); the folder split keeps the
   structure legible.
3. Drive-linked sources re-sync on change — re-running Stage 2 after a
   program boundary refreshes the same Drive paths, and NotebookLM picks up
   the new bytes without re-adding sources. [search-verified 2026-10-29]

## 7. Artifact registration

- `notebooklm-drive-upload.sh` — the Stage-2 command wrapped fail-closed
  (arg check, remote existence check, pre-flight `rclone lsd`), staged in
  this delivery kit; sha256 in the kit `SHA256SUMS`.
- This runbook: canonical home `working-notes/notebooklm-drive-ingest-runbook-v1.md`
  (GWM). It is operator-utility documentation, not paper-2 content — no
  rider status, not deposit-relevant.

**Verification-status disclosure:** §1–§3 and §6 claims marked
"search-verified 2026-10-29" rest on this boundary's web pass (Google
support/help pages, blog.google, elephas.app limits rundown, nlmtools
folders guide); §4's table is witness prior knowledge + the same pass, and
ships with live-check one-liners because package repos mutate faster than
any record. Nothing here is silently trusted — the house rule applies to
tooling claims too.

