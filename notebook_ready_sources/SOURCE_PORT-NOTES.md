# Telemetry Source: PORT-NOTES.md
- **Source Identifier**: `PORT-NOTES.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `e9de8b666c5ebccb89d09f769b3c38c84033f4b925089a26c7fda5e13c8dc53a`

---

## Raw Telemetry Content

# PORT-NOTES — port-era errata, amended

Amended 2026-10-24 at draft-1 delivery (R-62/R-63 dispositions; operator delegation "your tools now; your call", trace `1a16bb5a9ef26b25`). The pre-port two-line form is superseded and lives in git history at and below `14ad0f6`.

- **Manifest convention (R-62 RULED).** Supersedes the pre-port "cd into the sessions folder, bare filenames" line and R-57's original form. Canonical: rows are `<sha256>  sessions/<file>` — repo-root-relative, `sessions/`-prefixed, two-space separator; invoked from the repo root as `sha256sum -c sessions/MANIFEST.sha256`; one row per pinned file; deterministic `LC_ALL=C` ordering; no header or comment rows — `sha256sum -c` must run warning-free. Rationale (witness suggestion at registration, now ruled by delegation): root-relative prefixed rows verify from any working directory and match git's own view of the tree. The committed manifest at `14ad0f6` already conforms: 28 rows, 28/28 OK, zero warnings, witness-side verified this boundary.
- **Pins (R-63 RULED).** PORT-NOTES carries no standing pins. The delta-001-era pin line (`core 12c1d2f8… | package 00501443… | PROTOCOL 07fbe3f7…`) is withdrawn — two of three were stale at first post-port check. Pins are boundary-local, read from HEAD at each boundary per R-61; live boundary pins are recorded in PROJECT_STATE.md and the boundary emissions, never here.

