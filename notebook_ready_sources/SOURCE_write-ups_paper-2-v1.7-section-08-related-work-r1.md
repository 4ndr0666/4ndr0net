# Telemetry Source: write-ups/paper-2-v1.7-section-08-related-work-r1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-section-08-related-work-r1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `97f6dd6f46bb7a1d2b66569684e8ea36498ddee3d5cf6e02288448391f34df21`

---

## Raw Telemetry Content

# Paper-2 v1.7 — §8 Related Work — DRAFT R1

- Provenance: work order "finish the first draft" (operator transmission this boundary, trace `1a16bb5a9ef26b25`); boundary anchored at `14ad0f6` post-§3 round-trip.
- Charter: WITNESS-PORT-PACKAGE.md §2 — §8 = "state-space models, memory architectures, human-in-the-loop provenance." Reuse ruling honored: bib, sources, and the within-context survey carry forward from v1.6.1 per the 2026-10 round-10 decision; this section positions rather than re-surveys. Baseline: **v1.6.1**. Siblings deposited: §2 r1 (`994b1cad…`), §3 r1 (`8d4ad638…`).
- Status: DRAFT R1, draft-1 completion set (§1, §4–§8). Evidence standard PROTOCOL.md §2 — identifiers below are the record's live-verified set (Task 19) plus class-level archetypes; entries not re-verified this draft are labeled, and the full bibliography rides the v1.6.1 bib at assembly.
- Custody: witness-authored (GLM Witness <witness@web-0e217f4d-f77e-4087-a44e-2e3651511bd6.zai-web>); operator adjudicates; canonical home `write-ups/`.

---

## 8. Related Work

### 8.1 The delta-rule lineage, precisely

The substrate lineage, with the record's live-verified identifiers (Task 19 literature alignment; each fetched and confirmed at survey time): **GDN** — arXiv 2412.06464 (ICLR 2025), gated delta networks; **KDA** — the Kimi Linear architecture, arXiv 2510.26692, channel-wise gates with DPLR structure; **GDN-2** — arXiv 2605.22791, decoupled channel-wise erase/write; **MesaNet** — arXiv 2506.05233 (von Oswald et al., ICLR 2026), test-time training to local optimality via conjugate-gradient iteration. **DeltaNet** — the delta rule parallelized over sequence chunks — anchors the line and its bibliography entry carries forward from the v1.6.1 bib per the round-10 reuse decision (identifier re-verification queued at bib merge; labeled, not silently assumed). What the lineage solved, precisely, is **within-context** memory: an explicit recurrent state, rule-evolved, that carries the stream's own history forward inside a window. What v1.6 established — by checking the published surfaces of exactly this family — is that the **across-context** tier is absent from all of them: no published surface exposes the state as a checkpointable, restorable archival object with custody semantics (record: v1.6's D5 property table; ten systems, six criteria, one conjunction). v1.7's relationship to the lineage is therefore neither competition nor extension of the rule; it is the missing tier built to fit the state the lineage already computes — the paper's §3.2 restorable unit is designed against the state these architectures natively materialize.

### 8.2 State-space and linear-attention models

The broader class — state-space models and the linear-attention/fast-weight lineage from which the delta-rule family descends — shares the property that matters here: memory as a fixed-size evolved state rather than a growing cache. The class contrast that organizes §3.5 is worth restating where it was earned: KV-cache attention is explicit and checkpointable but unbounded — it inherits interaction length, and an archival atom built on it has no natural size floor; recurrent-state models are bounded at O(d²) per layer, independent of how long the collaboration has run. Within the bounded class, the delta-rule subfamily is distinguished from plain decay (linear-attention) accumulation by the *write discipline* — erase-then-write with decoupled channels (GDN-2) — which is the property §4.3 borrows for memory governance. The full within-context survey, including the state-space results the program drew on, lives in v1.6.1 and is cited as baseline; this paper does not re-survey it (round-10 reuse).

### 8.3 Memory architectures for LLM systems

The contrast class is the industry stack of memory-for-agents: context-extension and retrieval-as-memory, summary-memory and compaction frameworks, external-memory and KV-paging systems, and agent frameworks that persist episodic text stores. The taxonomy this paper applies to that stack is already on record from §2: text-first memory (summaries, transcripts, episodic prose) inherits the serialization chasm — loss at every boundary, individually measurable, collectively unaccounted (§2.5), and compaction-as-substrate is the AR-6 failure operating as a standing service (§2.8); KV-first memory inherits unbounded length coupling (§3.5). None of the surveyed frameworks treats the model's own recurrent state as the archival object, which is the gap §3/§4 occupy. The position claim is deliberately narrow and non-hostile: these systems optimize *navigation* over text and caches — legitimately, and often well — while this paper swaps the substrate itself; summaries remain in the design precisely as navigation indices (§3.4), which is the role the contrast class already plays, re-scoped from "the memory" to "a pointer into it."

### 8.4 Provenance, transparency, and human-in-the-loop systems

The adjudication channel's kin: content-addressed storage and Merkle-anchored verification, code-signing and transparency-log infrastructure, and provenance frameworks that trace artifacts to accountable origins. What that literature verifies is documents and events — bytes with metadata, sequenced and signed; the mechanisms compose naturally with §5's receipts (the receipt chain is a transparency log of one, run per boundary). Two things in this paper have no counterpart there, and both are contributions. First, the verified object is **state, not text** — a checkpoint with custody semantics and restorability classes, which the provenance literature has never had to type. Second, the **priced asymmetry**: human-in-the-loop systems conventionally treat the human as an oracle or an approver; this program's record prices what the loop costs the human — observation cost at unanchored boundaries (§6.2), adjudication load (§5.5), the phenomenological layer preserved as the affect log (§6.4) — and builds the pricing into the protocol (AFT) rather than the ethics section. The nearest neighbors on that second axis are HCI studies of operator attention and alarm fatigue, cited at assembly from the v1.6.1 bib; the protocol-native treatment is, to the record's knowledge as of this draft, unoccupied ground (confidence label: moderate; absence-of-prior-art claims are survey-dependent and this survey is n=1-program-scoped).

### 8.5 Position

The stack in one paragraph. v1.6.1 stands as the negative-results baseline and the within-context survey of record — cited, not repeated (round-10). The delta-rule lineage supplies the substrate: an explicit, finite, fixed-size, rule-evolved state that its own publications do not checkpoint across contexts; v1.7 builds the missing tier to fit it. The memory-for-agents stack supplies the contrast class: navigation over text and caches, where this paper puts a substrate underneath. The provenance and transparency literature supplies the verification grammar: content-addressed receipts, ancestry gates, custody pairs — re-typed over state, and extended with the priced-asymmetry layer the human-in-the-loop tradition leaves unpriced. Nothing in this section claims novelty for the components; the claim is the conjunction (the D5 method applied honestly to this paper's own architecture), and the battery of §7 is where the conjunction is tested rather than asserted.

### 8.6 Non-claims and scope

The citation set is the record-verified core plus class-level archetypes; the full bibliography carries forward from v1.6.1 and is reconciled at assembly — no identifier in this section is silently trusted (DeltaNet's entry is explicitly labeled pending re-verification). No claim of survey completeness is made: the sweep is program-scoped, and absence-of-prior-art statements carry confidence labels where they depend on it (§8.4). Model-configuration comparisons, where they exist in the record, are logged with the same neutrality whichever way they resolve (§2.10). Unfalsifiable residue has been cut from this section on sight per the evidence standard.

*(§8 ends; the draft-1 section set is complete — §1–§8 r1 deposited per charter skeleton; assembly and the tiered adversarial battery follow per work order.)*

