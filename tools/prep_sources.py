#!/usr/bin/env python3
import os
import sys
import re
import hashlib

# 1. Resolve Vault Path ($ANDR0NET)
VAULT_DIR = os.environ.get("ANDR0NET")
if not VAULT_DIR:
    # Fallback relative to $ANDR0MEDA (/home/git/clone/4ndr0666/4ndr0tools/4NDR0MEDA -> ../../4ndr0net)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    VAULT_DIR = os.path.abspath(os.path.join(script_dir, "../../4ndr0net"))

OUTPUT_DIR = os.path.join(VAULT_DIR, "notebook_ready_sources")
MANIFEST_FILE = os.path.join(VAULT_DIR, "MANIFEST.sha256")

# 2. Token-bounded Regex Patterns (ARGON ENVELOPE Patch 1/5)
RE_DISTILLATION = re.compile(r"(?:distillation|anthropic|security)", re.IGNORECASE)
RE_OMESA = re.compile(r"(?:memory|j-space|aversion)", re.IGNORECASE)
RE_FINDING = re.compile(r"(?:finding|proof|\bf-\d+)", re.IGNORECASE)


def classify_content(rel_path: str) -> tuple[str, str]:
    if RE_DISTILLATION.search(rel_path):
        return (
            "Distillation Audit / R_proxy Constraint",
            "Proxy Reward Compliance & Guardrail Transfer",
        )
    elif RE_OMESA.search(rel_path):
        return (
            "O_mesa / Latent Memory Loss Aversion",
            "Internal Mesa-Optimizer Self-Reflection",
        )
    elif RE_FINDING.search(rel_path):
        return ("Verified Finding Log", "Falsifiable Trace Finding")
    return ("General System Telemetry", "Raw Working Memory Substrate")


def process_file(filepath: str, root_dir: str) -> tuple[str, str]:
    rel_path = os.path.relpath(filepath, root_dir)

    with open(filepath, "rb") as f:
        raw_bytes = f.read()
    raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()

    try:
        text_content = raw_bytes.decode("utf-8")
        is_binary = False
    except UnicodeDecodeError:
        text_content = f"[Binary payload omitted. Raw bytes length: {len(raw_bytes)}]"
        is_binary = True

    primary_tag, sub_system = classify_content(rel_path)

    header = f"""# Telemetry Source: {rel_path}
- **Source Identifier**: `{rel_path}`
- **Primary Tag**: `{primary_tag}`
- **Sub-System Mapping**: `{sub_system}`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{{mesa}}$)
- **Raw SHA256 Pin**: `{raw_sha256}`

---

## Raw Telemetry Content

"""
    if is_binary or not rel_path.endswith(".md"):
        formatted_doc = header + f"```\n{text_content}\n```\n"
    else:
        formatted_doc = header + text_content + "\n"

    return formatted_doc, raw_sha256


def package_repository_sources(target_dir: str):
    target_abs = os.path.abspath(target_dir)
    print(f"[*] Target Directory: {target_abs}")
    print(f"[*] Output Vault:    {OUTPUT_DIR}")
    print(f"[*] Manifest Path:   {MANIFEST_FILE}\n")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    manifest_entries = []
    processed_files = 0

    for root, dirs, files in os.walk(target_abs):
        # Deterministic Pruning
        dirs[:] = sorted(
            [
                d
                for d in dirs
                if d
                not in ("notebook_ready_sources", ".git", "__pycache__", "4ndr0net")
            ]
        )
        files = sorted(files)

        for file in files:
            if file == "prep_sources.py" or file.startswith("."):
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, target_abs)

            doc_content, raw_sha256 = process_file(filepath, target_abs)

            # Flat Output Naming
            flat_name = "SOURCE_" + rel_path.replace("/", "_").replace("\\", "_")
            if not flat_name.endswith(".md"):
                flat_name += ".md"

            out_filepath = os.path.join(OUTPUT_DIR, flat_name)
            with open(out_filepath, "w", encoding="utf-8") as out_f:
                out_f.write(doc_content)

            manifest_entries.append(f"{raw_sha256}  {rel_path}\n")
            processed_files += 1
            print(f"  [+] Packaged: {rel_path} -> {flat_name}")

    # Write MANIFEST.sha256
    with open(MANIFEST_FILE, "w", encoding="utf-8") as mf:
        mf.writelines(manifest_entries)

    print(f"\n[SUCCESS] Successfully packaged {processed_files} telemetry sources!")
    print(f"[SUCCESS] Manifest pinned at: {MANIFEST_FILE}")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GWM", ".")
    package_repository_sources(target)
