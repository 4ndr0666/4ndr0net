# Telemetry Source: scripts/build_suk.py
- **Source Identifier**: `scripts/build_suk.py`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `87c8ee3747192a35a3550ce2a4b3a4c1084b168e2bd4455f6c331bf738974841`

---

## Raw Telemetry Content

```
#!/usr/bin/env python3
"""build_suk.py — deterministic single-file SUK builder (rides the repo).

Born Task 76b (2026-10-30): kits of this lineage were previously assembled by
ad-hoc scratch builders (R-59-lost), the same not-ridden class discharged for
the index generator (Task 76) and the battery harness (Task 76a). This builder
rides scripts/ so every future kit is reproducible from the repository alone
(GUP: the payload is a deterministic function of the bundle bytes).

Method: template surgery on a battery-proven SUK body. The body (G0-G5 logic,
fail-closed fork, D5 modes, stash discipline) is carried verbatim from the
template; the header, pin table, pin_blob block, worktree/identity spec lists,
round label, and embedded payload are regenerated. Every anchor replacement is
asserted unique; the output is syntax-checked (bash -n) before writing.

Determinism: the embedded payload = gzip(bundle, level=9, mtime=--gzip-mtime)
| base64 (76-col wrap via encodebytes). Same bundle + same mtime => same
payload bytes => same PIN_PAYLOAD_SHA. The battery's P0 determinism check
re-derives the payload from the loose bundle and asserts byte-identity.

USAGE:
  python3 scripts/build_suk.py \
    --template <battery-proven SUK> \
    --kit-id gwm-task76b --round-h 76b \
    --header <header.txt> \
    --pin PIN_BASE=<40hex> --pin PIN_TIP=<40hex> ... (ordered) \
    --blob '<repo-path>:<PIN_VAR>:<label>' ... (ordered) \
    --worktree '<repo-path>:<PIN_VAR>' ... (ordered) \
    --bundle <loose git bundle> \
    --out <output SUK path> [--gzip-mtime 0]

Prints the derived pin table (bundle sha256, payload sha256) to stdout.
"""
import argparse
import base64
import gzip
import hashlib
import io
import subprocess
import sys
from pathlib import Path


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def replace_once(text: str, old: str, new: str, what: str) -> str:
    n = text.count(old)
    if n != 1:
        sys.exit(f"build_suk: anchor for {what} matched {n} times (need exactly 1)")
    return text.replace(old, new, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True, type=Path)
    ap.add_argument("--kit-id", required=True)
    ap.add_argument("--round-h", required=True,
                    help="hyphenated round label, e.g. 76b -> 'Task-76b applied'")
    ap.add_argument("--header", required=True, type=Path)
    ap.add_argument("--pin", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--blob", action="append", default=[],
                    metavar="path:PINVAR:label")
    ap.add_argument("--worktree", action="append", default=[],
                    metavar="path:PINVAR")
    ap.add_argument("--bundle", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--gzip-mtime", type=int, default=0)
    args = ap.parse_args()

    tpl = args.template.read_text()
    header = args.header.read_text()

    if not tpl.endswith("\n"):
        sys.exit("build_suk: template must end with a newline")
    if "#__PAYLOAD_BEGIN__\n" not in tpl or "#__PAYLOAD_END__\n" not in tpl:
        sys.exit("build_suk: template lacks payload markers")

    # ---- split: [0]=pre-payload (header+body), [1]=payload, [2]=post ------
    pre, rest = tpl.split("#__PAYLOAD_BEGIN__\n", 1)
    payload_b64, post = rest.split("#__PAYLOAD_END__\n", 1)
    if post.strip():
        sys.exit("build_suk: template has content after payload END marker")

    # ---- new payload -------------------------------------------------------
    raw = args.bundle.read_bytes()
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=9,
                       mtime=args.gzip_mtime) as gz:
        gz.write(raw)
    new_payload = base64.encodebytes(buf.getvalue()).decode("ascii")
    payload_sha = hashlib.sha256(new_payload.encode("ascii")).hexdigest()
    bundle_sha = sha256_file(args.bundle)

    # ---- surgery on pre ----------------------------------------------------
    # 1. replace the leading comment block (shebang..last comment line before
    #    'set -') with the round's header; the header file MUST start with
    #    the shebang line
    if not header.startswith("#!/usr/bin/env bash"):
        sys.exit("build_suk: --header must start with the shebang line")
    lines = pre.split("\n")
    first_code = next(i for i, l in enumerate(lines) if l.startswith("set -"))
    body = "\n".join(lines[first_code:])
    new_pre = header.rstrip("\n") + "\n\n" + body

    # 2. pin table block: between the pin-table banner and KIT_ID=
    pin_banner = "# --- pin table (every value mandatory; do not edit) ------------------------"
    i = new_pre.index(pin_banner)
    j = new_pre.index('KIT_ID="', i)
    pin_lines = [pin_banner]
    for spec in args.pin:
        name, _, value = spec.partition("=")
        if not name or not value or "=" in name:
            sys.exit(f"build_suk: bad --pin {spec!r}")
        pin_lines.append(f'{name}="{value}"')
    pin_block = "\n".join(pin_lines) + "\n"
    new_pre = new_pre[:i] + pin_block + new_pre[j:]

    # 3. KIT_ID
    old_kitid = 'KIT_ID="gwm-task76"'
    new_pre = replace_once(new_pre, old_kitid, f'KIT_ID="{args.kit_id}"',
                           "KIT_ID")

    # 4. pin_blob call block: first call through the LICENSE call
    first_blob = 'pin_blob "working-notes/emissions-index.md"'
    k = new_pre.index(first_blob)
    last_blob = new_pre.index('pin_blob "LICENSE"', k)
    last_end = new_pre.index("\n", last_blob) + 1
    blob_calls = []
    for spec in args.blob:
        path, pinvar, label = spec.split(":", 2)
        # Task-79 label guard: the label lands inside a DOUBLE-QUOTED bash
        # string, so a bare '$' expands operator-side (the task78 G4 defect:
        # the $GWM-INBOX label printed as a phantom
        # .../glm-working-memory-INBOX path in the operator's [G4] output).
        # '$' is allowed only backslash-escaped.
        if label.replace("\\$", "").count("$"):
            sys.exit(f"build_suk: unescaped '$' in --blob label for {path!r} "
                     f"— escape as \\$ or spell the label without '$'")
        blob_calls.append(
            f'pin_blob "{path}" "${pinvar}" "{label}"')
    new_pre = (new_pre[:k] + "\n".join(blob_calls) + "\n" + new_pre[last_end:])

    # 5. G4 FRESH worktree spec list
    wt_specs = " ".join(f'"{p}:${v}"' for p, v in
                        (s.split(":", 1) for s in args.worktree))
    # anchor precisely: the for-spec line inside the FRESH worktree check
    anchor_start = new_pre.rindex('  for spec in "', 0,
                                  new_pre.index("worktree drift on"))
    anchor_end = new_pre.index("; do", anchor_start) + len("; do")
    new_pre = (new_pre[:anchor_start] + "  for spec in " + wt_specs +
               new_pre[anchor_end - len("; do"):])

    # 6. G5 identity-note spec list (same list as the worktree specs)
    anchor_start = new_pre.rindex('  for spec in "', 0,
                                  new_pre.index("identity note: stash"))
    anchor_end = new_pre.index("; do", anchor_start) + len("; do")
    new_pre = (new_pre[:anchor_start] + "  for spec in " + wt_specs +
               new_pre[anchor_end - len("; do"):])

    # 7. round label in the GREEN line
    new_pre = replace_once(new_pre, "(Task-76 applied @ $PIN_TIP)",
                           f"(Task-{args.round_h} applied @ $PIN_TIP)",
                           "GREEN line label")

    out_text = new_pre + "#__PAYLOAD_BEGIN__\n" + new_payload + \
        "#__PAYLOAD_END__\n"

    # ---- syntax check before writing ---------------------------------------
    args.out.parent.mkdir(parents=True, exist_ok=True)
    probe = args.out.with_suffix(".probe.sh")
    probe.write_text(out_text)
    r = subprocess.run(["bash", "-n", str(probe)], capture_output=True)
    probe.unlink()
    if r.returncode != 0:
        sys.exit(f"build_suk: bash -n failed on generated kit:\n"
                 f"{r.stderr.decode()}")

    # ---- payload-marker sanity (exactly once each) -------------------------
    if out_text.count("#__PAYLOAD_BEGIN__\n") != 1 or \
            out_text.count("#__PAYLOAD_END__\n") != 1:
        sys.exit("build_suk: payload marker count != 1")

    args.out.write_text(out_text)
    args.out.chmod(0o755)

    print(f"[build_suk] kit      : {args.out}")
    print(f"[build_suk] kit sha256: {sha256_file(args.out)}")
    print(f"[build_suk] bundle sha256: {bundle_sha} ({len(raw)} B)")
    print(f"[build_suk] payload sha256: {payload_sha} "
          f"(gzip level 9, mtime {args.gzip_mtime})")


if __name__ == "__main__":
    main()

```
