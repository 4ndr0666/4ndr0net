# Telemetry Source: working-notes/operator-tree-facts.md
- **Source Identifier**: `working-notes/operator-tree-facts.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `9144112d60b4933a841615d16bd550ab992b573b9c72dd83f65873cb9383fa7f`

---

## Raw Telemetry Content

# Operator-Tree Facts — canonical environmental pins

Single source of truth for the operator's production-tree layout. These are
ENVIRONMENTAL FACTS, not protocol law: they describe where things live on the
operator's machine so that delivery scripts and probes stop re-deriving them
from witness-side guesswork. The motivating defect: Task-61 LEG-A's delivery
script hard-coded the witness's own directory layout, ignored the repo path
the operator passed as `$1` on the first invocation, and a liveness probe
(`test -x`) tested a mode the tree never carried ([7/9] halt). Environmental
facts had no canonical home, so they lived only in memory and were
re-remembered wrongly at every boundary. This file is that home.

Registered Task 62 (2026-10-26, trace 1a1754e4ab07b3e1). If the operator
moves a tree, THIS file changes first, in one commit, and every script that
reads it follows. Facts below are copied verbatim from the operator's
transmissions (PROTOCOL §3 — his typed bytes, his spelling).

## Production tree (operator machine)

- `PROD_PATH="/home/git/clone/4ndr0666"`
- `GWM="$PROD_PATH/glm-working-memory"` (public: github.com/4ndr0666/glm-working-memory)
- `ANDROMEDA="$PROD_PATH/4ndr0tools/4NDR0MEDA"` (public: github.com/4ndr0666/4NDR0MEDA)
- `INBOX="$PROD_PATH/gwm-inbox"`
- CDP (`coordinated-disclosure-public`) lives under `PROD_PATH` as a sibling tree.

## Witness-side mirrors (this VM, no git credentials)

- `/home/z/my-project/clone/4ndr0666/glm-working-memory` — GWM mirror (fetch-only)
- `/home/z/my-project/clone/4ndr0666/4ndr0meda` — MEDA mirror (fetch-only)
- Deliverables staged to `/home/z/my-project/download/`, declared `file:///download/…`
- The witness NEVER pushes; all mutations ride §10 packages through `gwm-inbox`
  and the operator's hands are the last writer.

## Conventions pinned by these facts

1. **$1 OVERRIDES EVERYTHING (D2)**: orchestrator scripts take the target
   repo path as `$1` with the production default above; a caller-passed path
   is never overridden by a hardcoded search.
2. **SUMS COVER BUNDLES ONLY (D3)**: SHA256SUMS never pins the orchestrator
   script itself; the operator may legally edit a script without breaking
   the package pin.
3. **DELIVERY SHAPE (§10 canon-001)**: bundle + SUMS + orchestrator, double
   HEAD-pin (BASE + EXPECT), ff-only, fail-closed legs, `APPLIED @ <head40>`
   closing line.
4. **Derive, don't recall (D1)**: probe markers are derived from the tree at
   hand and re-verified before shipping — never quoted from memory.

