# Telemetry Source: scripts/task76_resync_check.py
- **Source Identifier**: `scripts/task76_resync_check.py`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `37a3d68b0aa6b1b9d288ec195e2c297aa46343ec2c103a9845f41fc46912ba1f`

---

## Raw Telemetry Content

```
#!/usr/bin/env python3
"""Task 76 — state-resync custody cross-check (repo-runnable, recomputable).

Recomputes the Task-76 classification from THIS repository plus the two
public operator-side remotes (anonymous, read-only, blobless probes):

    github.com/4ndr0666/gpt          (white-paper tree host)
    github.com/4ndr0666/4NDR0MEDA    ($ANDROMEDA published state)

Classifies every file registered in working-notes/emissions-index.md §3
(white-paper tree, 58 names; ground truth = operator INDEX attachment
2026-10-29, pinned in-file §5) by DURABLE custody:

  DURABLE-REPO   — present in THIS repository (git ls-files)
  DURABLE-GPT    — present in the published gpt tree at its main tip
  DURABLE-MEDA   — present in the published 4NDR0MEDA tree at its main tip
  LOCAL-ONLY     — none of the above (operator local disk only)

The witness VM download/ share is deliberately NOT a custody class (R-59:
if it mattered, it is in the repo or it does not exist).

Also pins the published tips it observed, so the round record's remote
states are re-derivable: gpt and MEDA main, plus the exact contents of the
published documentation/white_paper/4NDR0MEDA subtree.

Usage:  python3 scripts/task76_resync_check.py [probe-dir]
        (probe-dir defaults to a temp dir; remotes probed read-only)
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GPT_URL = "https://github.com/4ndr0666/gpt.git"
MEDA_URL = "https://github.com/4ndr0666/4NDR0MEDA.git"


def sh(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True).stdout


def parse_blocks(text, start_pat, end_pat):
    """Filenames from fenced tree blocks between two headings."""
    inside, fence, names = False, False, []
    for ln in text.splitlines():
        if re.match(start_pat, ln):
            inside = True
            continue
        if re.match(end_pat, ln):
            inside = False
            continue
        if not inside:
            continue
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence:
            m = re.match(r"^[│├└─\s]+(.+?)\s*$", ln)
            if m and m.group(1) and not m.group(1).startswith("#"):
                names.append(m.group(1))
    return names


def probe(url, name, probe_dir):
    """Blobless read-only clone; returns (tip_sha, {basenames})."""
    dst = probe_dir / name
    if not dst.exists():
        subprocess.run(
            ["git", "clone", "--filter=blob:none", "--no-checkout", url, str(dst)],
            capture_output=True, text=True, check=True,
        )
    tip = sh(["git", "-C", str(dst), "rev-parse", "HEAD"]).strip()
    files = sh(["git", "-C", str(dst), "ls-tree", "-r", "--name-only", "HEAD"]).splitlines()
    return tip, {Path(f).name for f in files}


def main():
    probe_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="gwm76probe."))
    probe_dir.mkdir(parents=True, exist_ok=True)

    idx_text = (REPO_ROOT / "working-notes/emissions-index.md").read_text()
    inbox = parse_blocks(idx_text, r"^## 1\.", r"^## 2\.")
    outbox = parse_blocks(idx_text, r"^## 2\.", r"^## 3\.")
    whitepaper = parse_blocks(idx_text, r"^## 3\.", r"^## 4\.")
    print(f"index parsed: inbox={len(inbox)} outbox={len(outbox)} whitepaper={len(whitepaper)} "
          f"(expect 219 / 9 / 58)")
    if (len(inbox), len(outbox), len(whitepaper)) != (219, 9, 58):
        print("INDEX DRIFT: counts differ from the Task-75 ground truth — re-derive before trusting")
        sys.exit(1)

    repo_files = {Path(p).name for p in sh(["git", "ls-files"], cwd=REPO_ROOT).splitlines() if p.strip()}
    gpt_tip, gpt_files = probe(GPT_URL, "gpt-probe", probe_dir)
    meda_tip, meda_files = probe(MEDA_URL, "meda-probe", probe_dir)
    print(f"probes: gpt@{gpt_tip} ({len(gpt_files)} unique basenames of "
          f"{len(sh(['git', '-C', str(probe_dir / 'gpt-probe'), 'ls-tree', '-r', '--name-only', 'HEAD']).splitlines())} paths)  "
          f"4NDR0MEDA@{meda_tip} ({len(meda_files)} files)")
    print("published gpt documentation/white_paper/4NDR0MEDA contents:")
    wp_pub = sh(["git", "-C", str(probe_dir / 'gpt-probe'),
                 "ls-tree", "-r", "--name-only", "HEAD",
                 "documentation/white_paper/4NDR0MEDA"]).splitlines()
    for f in wp_pub:
        print(f"  {f}")

    print("\nwhite-paper 58 — custody classification:")
    local_only = []
    for f in sorted(whitepaper):
        r, g, m = f in repo_files, f in gpt_files, f in meda_files
        if r or g or m:
            cls = "DURABLE" + ("-REPO" if r else "") + ("-GPT" if g else "") + ("-MEDA" if m else "")
        else:
            cls = "LOCAL-ONLY"
            local_only.append(f)
        print(f"  {f:62} {cls}")

    print(f"\nSUMMARY: durable {58 - len(local_only)}/58 | LOCAL-ONLY {len(local_only)}/58")
    print("GUP note: the pinned subset of LOCAL-ONLY (state-resync-check-v1.md §3)")
    print("carries record pins that are NOT repo-recomputable until relayed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

```
