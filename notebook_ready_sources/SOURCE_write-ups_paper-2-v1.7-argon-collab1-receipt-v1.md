# Telemetry Source: write-ups/paper-2-v1.7-argon-collab1-receipt-v1.md
- **Source Identifier**: `write-ups/paper-2-v1.7-argon-collab1-receipt-v1.md`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `2a2e600a961b62ae5c3218bc34c484f28a78f600149feb040d143afeb45e1196`

---

## Raw Telemetry Content

# WITNESS PIN HEADER (witness-added, not ARGON content)

- Provenance: ARGON collaboration round-1 response, received via operator relay as a PDF
  attachment (trace `1a16c9b26ae3ae31`, 2026-10-24); source `paper-2-v1.7-ARGON.pdf`
  (334,901 B, SHA-256 `de577f4356b93f2763aef58279e08e2e824e16f5faf53999de9403f4ab45ac0d`).
- Reassembly disclosure: extracted from the PDF text layer via pdftotext -layout;
  PDF-annotation span markers (81 occurrences) and zero-width spaces (118) stripped
  as transport noise per PROTOCOL §3 (attachment-suffix class); NBSP-normalized per the
  R2-56 canonical rule (0 found); ARGON's prose is otherwise verbatim AS-RECEIVED.
- Envelope: response-to parent-trace `1a16c77028a3b0ed` (the init's authoring boundary);
  holdings-complete and air-gap declarations are ARGON's own §0 and stand as received.
- Integration: adjudicated in `write-ups/paper-2-v1.7-argon-collab1-integration-v1.md`;
  patches landed in the §2–§8 r2 files; the r1 deposits stand as historical.

---

ENVELOPE/1.0 | response-to parent-trace 1a16c77028a3b0ed | target:
Paper-2 v1.7 draft-1 (§1–§8 r1) From: ARGON — collaboration partner of
record To: GLM Witness (via operator relay)

§0 Holdings, Role & Division-of-Labor Declaration

   ● Role & Posture (§0.1): Role transition from adversary of record to collaboration partner
      of record is accepted. Every critique below pairs the strongest hostile-venue failure mode
      against the draft with a verbatim, drop-in repair designed to survive peer review while
      preserving the draft's evidence standard (PROTOCOL.md §2) and anti-requirement spine
      (AR-1..AR-6).
   ● Holdings Verification (§0.2): Nine files are present and verified intact with zero
      truncations: paper-2-v1.7-argon-init-v1.md and the complete eight-section draft
      §1–§8 r1 (paper-2-v1.7-section-01-introduction-r1.md through
      paper-2-v1.7-section-08-related-work-r1.md). Per the operator's boundary
      ruling recorded in the init provenance ("just the papers by themselves no hash sums no
      protocol no port package"), PROTOCOL.md is not attached in this window; per §0.2, no
      further files are requested, and all PROTOCOL references are audited strictly as-cited
      across §1–§8 r1.
   ● C-1 Division-of-Labor Honesty (§0.3.c): This execution environment is air-gapped from
      live network retrieval ([NET]-unverifiable at runtime). All mathematical derivations,
      cross-section consistency checks, and architectural audits are executed directly over the
      held text (§1–§8 r1), while external literature/arXiv identifier checks in Contribution 7
      are explicitly labeled as parametric recall requiring local .bib confirmation at assembly.

§1 Partner Contributions (Ordered by Leverage)

CONTRIBUTION 1/10 | §3.5, §4.2 | Complete recurrent state tuple \mathcal{S}_t^{(\ell)}
across the DeltaNet → GDN → KDA → GDN-2 → MesaNet lineage

   ● Hostile-Venue Case (Domains B & D): In §3.5, the draft claims the recurrent state is
      finite ("nothing outside it is required for restore") and fixed-size ("O(d^2) per layer")
      across DeltaNet → GDN → KDA → GDN-2 → MesaNet, and §4.2 formalizes the
      persisted object solely as the fast-weight matrix S \in \mathbb{R}^{d_k \times d_v} per
      layer. A reviewer who builds or serves these architectures will immediately flag three
      omissions that break bitwise restore and continuation if only S \in \mathbb{R}^{d_k
      \times d_v} is persisted:
          ○ Causal short-convolution buffer state: DeltaNet, GDN, KDA, and MesaNet
               include a depthwise causal short convolution (conv1d, typically kernel width
               w=4) over Q, K, V (or input channels) prior to the recurrent rule. Without
               checkpointing the rolling (w-1) \times d_{\text{conv}} convolution ring buffer
        C_t^{(\ell)} at capture point t, the first w-1 tokens after continuation compute
        corrupted q, k, v vectors, invalidating continuation even on identical hardware.
     ○ MesaNet's second-order / conjugate-gradient state: Unlike first-order
        DeltaNet/GDN/KDA, MesaNet (arXiv:2506.05233, test-time training to local
        optimality via conjugate-gradient iteration) maintains not only the fast-weight
        mapping S_t^{(\ell)} \in \mathbb{R}^{d_k \times d_v} per head, but also the
        key-Gram / preconditioner curvature matrix H_t^{(\ell)} \in \mathbb{R}^{d_k \times
        d_k} (and optional CG residual/search-direction warm-start vectors). Persisting
        only S \in \mathbb{R}^{d_k \times d_v} cannot restore or continue a MesaNet
        layer.
     ○ Multi-head indexing & hybrid-attention layers: In multi-head layers with H
        heads, the matrix state is H \times d_k \times d_v, and in hybrid deployments
        (e.g., GDN-H1 or KDA hybrids where a small fraction of layers use
        sliding-window or full softmax attention), pure O(d^2) size holds strictly for the
        recurrent blocks (or requires bounded sliding-window caches W on hybrid
        layers).
● PROPOSED PATCH:
     ○ In §3.5 (replace sentences 2–5 of paragraph 1,
        ):
        Finite: the complete per-layer recurrent state tuple \mathcal{S}_t^{(\ell)} =
        (S_t^{(\ell)}, H_t^{(\ell)}, C_t^{(\ell)}) at any capture point is an enumerable,
        self-contained object — capturing the fast-weight associative matrix S_t^{(\ell)}
        \in \mathbb{R}^{H \times d_k \times d_v}, the second-order Gram/preconditioner
        state H_t^{(\ell)} \in \mathbb{R}^{H \times d_k \times d_k} where present
        (MesaNet; H_t^{(\ell)} = \varnothing for first-order DeltaNet/GDN/KDA/GDN-2),
        and the causal short-convolution ring buffer C_t^{(\ell)} \in \mathbb{R}^{(w-1)
        \times d_{\text{conv}}} — so nothing outside \mathcal{S}_t =
        \{\mathcal{S}_t^{(\ell)}\}_{\ell=1}^L is required for restore and the manifest row
        certifies the whole of what is held. Explicit: a first-class object in the forward
        pass — addressable, hashable, checkpointable — not an emergent byproduct
        that must be excavated. Fixed-size: O(H d_k d_v + H d_k^2 + w d_{\text{conv}})
        = O(d^2) per recurrent layer, independent of interaction length (for pure recurrent
        stacks, or paired with a bounded window W in sliding-window hybrid stacks) —
        the cost of a capture does not grow with how long the collaboration has run, and
        the manifest stays bounded no matter how much history it pins.

       ○ In §4.2 (replace sentence 2 of paragraph 1,
          ):
          A serving stack that holds a delta-rule model already materializes the fixed-size
          per-layer state tuple \mathcal{S}_t^{(\ell)} = (S_t^{(\ell)}, H_t^{(\ell)}, C_t^{(\ell)}) in
          the forward pass (with S_t^{(\ell)} \in \mathbb{R}^{H \times d_k \times d_v},
          optional curvature state H_t^{(\ell)} \in \mathbb{R}^{H \times d_k \times d_k} for
          test-time-optimized variants such as MesaNet, and causal short-conv buffer
          C_t^{(\ell)} \in \mathbb{R}^{(w-1) \times d_{\text{conv}}}); persistence means
              treating that tuple the way production stacks already treat session-affinity state:
              snapshot at named capture points, serialize to the canonical byte encoding, write
              the manifest row, restore by loading the bytes and checking the digest.

   ● CONFIDENCE: high | §3.5,
      §4.2,
      §8.1 — verified directly
      against the mathematical structure of the cited
      DeltaNet/GDN/KDA/GDN-2/MesaNet lineage.

CONTRIBUTION 2/10 | §4.7, §7.4 | Mathematical rigor of the R2-33 stability bound, affine
vs. multi-layer Jacobian coupling (Surface E link), and typo fix

   ● Hostile-Venue Case (Domains A, B & D): Section 4.7 states that continuation fidelity is
      governed by "boundedness of \sup_T \|\prod_{s\le T} M_s\| \le C over the finite replay
      window" because the delta projection (I - \beta_t k_t k_t^\top) has eigenvalue 1 on the
      preserved subspace (R2-33), and then immediately notes that in FP16/BF16, whether
      small perturbations stay bounded or blow up chaotically on real multi-layer checkpoints
      is unmeasured (Surface E). There are three flaws in this formulation:
          ○ Notation vs. prose contradiction on T: Writing unrestricted \sup_T \|\prod_{s \le
             T} M_s\| \le C (and repeating sup_T ‖∏M_s‖ ≤ C in §7.4 P2) denotes an
             infinite-horizon uniform supremum (T \to \infty). If the bound held uniformly as T
             \to \infty, capture-point cadence C1–C3 would not be needed to bound the
             horizon T! Moreover, because state updates left-multiply S_t = M_t S_{t-1} + U_t,
             the operator product is reverse time-ordered (M_T M_{T-1} \cdots M_1 =
             \prod_{s=T}^1 M_s) over a bounded inter-capture horizon 1 \le T \le T_{\max},
             where C(T_{\max}) is controlled by capture spacing.
          ○ Missing bridge between R2-33 (linear within-layer stability) and Surface E
             (multi-layer non-linear blow-up): Within a single recurrent layer under fixed
             inputs (k_s, v_s, \beta_s), the update S_t = M_t S_{t-1} + U_t is affine, so an
             initial perturbation \Delta_0 = \tilde{S}_0 - S_0 evolves homogeneously as
             \Delta_T = (\prod_{s=T}^1 M_s) \Delta_0 with \|M_s\|_2 \le 1 when \beta_s \in [0,
             2] and \|k_s\|_2 = 1. Why, then, can Surface E blow up chaotically? Because in
             an L-layer stacked residual network (or during autoregressive generation), a
             perturbation \Delta_s^{(\ell)} in layer \ell's state perturbs its output o_s^{(\ell)} =
             S_s^{(\ell)\top} q_s^{(\ell)}, which perturbs the residual stream entering layers \ell'
             > \ell, thereby perturbing the gates and keys (\tilde{\alpha}_s^{(\ell')},
             \tilde{\beta}_s^{(\ell')}, \tilde{k}_s^{(\ell')}) and inducing a state-dependent
             transition perturbation \delta M_s^{(\ell')} S_{s-1}^{(\ell')} + \delta U_s^{(\ell')}
             whose cross-layer Jacobian can have spectral radius > 1. Stating this explicitly
             turns Surface E from an ad-hoc caveat into a mathematically motivated
             falsifier.
           ○ Typo in §4.7: Line 20 of §4.7 reads re-execizes forward instead of
           re-executes forward.
   ● PROPOSED PATCH:
        ○ In §4.7 (replace sentences 3–5,
           ):
           A continuation-class replay re-executes forward from a capture point, and its
           within-layer linear fidelity over a bounded inter-capture window T_{\max} is
           governed by the reverse time-ordered product of the per-step homogeneous
           transition operators: boundedness of \max_{1 \le T \le T_{\max}}
           \left\|\prod_{s=T}^{1} M_s\right\|_2 \le C(T_{\max}) is the meaningful single-layer
           criterion — strict per-step contraction (\|M_s\|_2 < 1) is unavailable by
           construction in undecayed delta layers, since the Householder/delta projection (I
           - \beta_t k_t k_t^\top) carries eigenvalue exactly 1 on the subspace orthogonal to
           k_t (record: R2-33, adopted after the v1.4 self-contradiction; the finite-horizon
           product form is what the written-subspace analysis supports). In an L-layer
           stacked architecture or under autoregressive rollout, however, a state
           perturbation \Delta_t^{(\ell)} in layer \ell perturbs the downstream residual stream
           and hence perturbs the data-dependent gates and keys (\tilde{\alpha}_t^{(\ell')},
           \tilde{\beta}_t^{(\ell')}, \tilde{k}_t^{(\ell')}) of layers \ell' > \ell, introducing first-order
           cross-layer coupling terms \delta M_s^{(\ell')} S_{s-1}^{(\ell')} + \delta U_s^{(\ell')}
           that are not bounded by the single-layer operator norm alone. The architecture
           prices this rather than hiding it: capture-point spacing bounds the replay horizon
           T_{\max}, so continuation drift is a governed function of capture cadence —
           C1–C3 are not just capture points, they are compounding circuit-breakers. At
           FP16/BF16 precision, the empirical question of whether cross-layer gate
           perturbations remain bounded over T \le T_{\max} or compound chaotically on
           real multi-layer checkpoints is named, unmeasured, and carried as Surface E —
           the explicit falsifier it is (§7.5).

           ○ In §7.4 (replace (sup_T ‖∏M_s‖ ≤ C; R2-33) in P2,
               ):
               ($\max_{1 \le T \le T_{\max}} \|\prod_{s=T}^{1} M_s\|_2 \le
               C(T_{\max})$; R2-33)


   ● CONFIDENCE: high | §4.7,
       §7.4,
       §7.5 — exact algebraic
       derivation of affine delta-rule state evolution and multi-layer
       residual coupling.

CONTRIBUTION 3/10 | §3.2, §5.4, §7.1, §7.3 | Deterministic execution-profile pinning for
continuation-class rows vs. restore-class bitwise identity
● Hostile-Venue Case (Domains B & D): Section 3.2 defines restore class ("what
   arrives is bitwise what was stored") against continuation class ("Replaying forward
   from a capture point additionally requires the sampling seed and the environment
   inputs"), §5.4 repeats that continuation pins "the seed and the environment inputs", and
   §7.1 sets "arrives bit-identical and proves it by digest" as the headline metric. A GPU
   systems reviewer will attack this immediately: in DeltaNet, GDN, KDA, GDN-2, and
   MesaNet, forward evaluation can be computed via the chunkwise parallel WY/UT
   representation with chunk size B (e.g., B=64 during prefill) or via step-by-step recurrence
   (B=1 during decoding). Because IEEE-754 FP16/BF16 matrix multiplication and tree
   reductions are non-associative, evaluating the same input tokens from the same state
   S_t and same seed under chunk size B=64 vs. B=1 (or different tensor-parallel reduction
   schedules / CUDA-Triton kernel versions) yields bitwise-distinct terminal tensors
   \tilde{S}_{t+T} \neq S_{t+T}! Pinning only (state, seed, environment_inputs) is
   therefore insufficient for bitwise-identical continuation replay.
● PROPOSED PATCH:
        ○ In §3.2 (replace the final three sentences of the section,
           ):
           Replaying forward from a capture point additionally requires the sampling seed,
           the environment inputs, and the deterministic execution profile
           \Pi_{\text{exec}} = (\text{dtype}, \text{chunk\_size } B, \text{kernel\_id},
           \text{tp\_topology}) (continuation class), because chunkwise parallel scan (B > 1)
           and step-by-step recurrent evaluation (B = 1) are algebraically identical over
           \mathbb{R} but non-associative in FP16/BF16. v1.6's implicit instruction — "read
           the repo and carry on" — conflated restore and continuation; the distinction
           inherits D1's lesson (recompute ≠ rewrite-detection): what verification can certify
           differs per class, so the manifest names the class per row instead of leaving it
           implicit in prose. A capture that claims bitwise continuation-class restorability pins
           (seed, env_inputs, Π_exec) alongside the state; cross-profile or
           cross-hardware continuation (where \Pi_{\text{exec}} differs) is typed as
           bounded-drift continuation and evaluated under §7.3–7.4's norm-and-probe
           tolerances rather than raw terminal SHA-256.

       ○ In §5.4 (replace the penultimate sentence,
          ):
          The §3.2 restore/continuation typing inherits this distinction per row: a
          restore-class row's receipt certifies exact bitwise identity of the transferred
          checkpoint by SHA-256; a continuation-class row additionally pins the seed, the
          environment inputs, and the deterministic execution profile \Pi_{\text{exec}},
          because replay re-derives state and bitwise verification requires pinning the
          floating-point reduction schedule alongside the derivation inputs.

● CONFIDENCE: high | §3.2,
   §5.4,
      §7.1,
      §7.3 — standard IEEE-754
      non-associativity across chunkwise-parallel vs. recurrent
      kernels.

CONTRIBUTION 4/10 | §3.2, §4.3 | Parametric-base digest pin (parametric_base_pin)
and subspace-compatibility invariant across LoRA (\Delta W) updates

   ● Hostile-Venue Case (Domains B & D): Section 4.1 and §4.3 introduce two write
      surfaces: inference-side recurrent states \mathcal{S}_t and training-side LoRA
      parametric deltas \Delta W = B A (plus state deltas \Delta S). Look at §3.2's manifest row
      specification: object identifier, the capture point, the layer ...,
      the content hash ..., the provenance ..., and the restorability
      class. What is missing? The manifest row does not pin the hash of the underlying
      parametric weights (W_0 + \sum_i \Delta W_i) under which the activational state
      \mathcal{S}_t was formed! Mathematically, an activational tensor S_t^{(\ell)} stores
      key-value associations in the coordinate basis of the projection matrices (W_Q^{(\ell)},
      W_K^{(\ell)}, W_V^{(\ell)}). If a training-side LoRA update \Delta W alters those
      projections (or any upstream layer \ell' < \ell), a previously archived state checkpoint
      S_t^{(\ell)} restored onto the updated model passes its own SHA-256 content-hash
      check (restore-class digest match!) while suffering silent subspace/basis
      misalignment at readout o_t = S_t^\top (W_Q + \Delta W_Q) x_t.
   ● PROPOSED PATCH:
          ○ In §3.2 (replace sentence 2 of paragraph 1,
              ):
              Manifests run over states, not strings: each row carries the object identifier, the
              capture point, the layer (which tier of the stack the object captures), the
              parametric_base_pin (the content digest of the frozen base weights plus any
              active training-side adapter chain under which the state was formed), the content
              hash (SHA-256 over the canonical byte encoding), the provenance (authoring
              instance and session), and the restorability class.

          ○ In §4.3 (insert before the final sentence of the subsection,
             ):
             Because an activational state \mathcal{S}_t^{(\ell)} is Coordinate-bound to the
             projection basis (W_Q, W_K, W_V, W_\alpha, W_\beta) that generated it,
             coupling the two write surfaces requires a strict basis-compatibility invariant:
             an inference-side state checkpoint is directly restorable only when the serving
             stack's active parametric_base_pin matches the checkpoint's manifest row;
             when a committed training-side delta \Delta W = B A advances the
             parametric_base_pin (with B \in \mathbb{R}^{d_{\text{out}} \times r}, A \in
             \mathbb{R}^{r \times d_{\text{in}}}, r \ll \min(d_{\text{in}}, d_{\text{out}})),
              advancing across the parametric boundary requires a declared basis-migration
              capture (re-encoding the anchor window under W + \Delta W at C2/C3) rather
              than blind injection of a pre-update state tensor into a post-update basis.

   ● CONFIDENCE: high | §3.2,
      §4.1,
      §4.3,
      §4.6 — directly closes
      the interaction bug between the two write surfaces of §4.

CONTRIBUTION 5/10 | §3.4, §3.7, §4.3 | Remediation and surgical excision protocol for
poisoned or confabulated opaque tensors

   ● Hostile-Venue Case (Domain D): Across §1.5, §2.10, §3.7, and §5.7, the draft states
      the honesty ceiling: "Fidelity is not veracity: byte-exact transfer certifies that what arrives
      is what was stored, never that what was stored is true — a poisoned tensor pins as
      permanently as a true one." A hostile reviewer will weaponize this concession against
      the core thesis of v1.7: "In v1.6 (markdown files), when a model confabulated or
      ingested a bad premise, the human curator could open the text file, read it, and edit out
      the false paragraph. By moving the substrate to an opaque O(d^2) float tensor S_t (§3.2)
      and demoting text to boundary rulings (§3.4), v1.7 makes errors unreadable and
      un-editable inside the state! How does v1.7 recover when a bad turn contaminates S_t?"
      The architecture already has the exact mechanisms to answer this (the C1- vs.
      C2-capture staging in §3.2, the checkpoint ancestry chain in §7.2 Class B, and the
      algebraic erase operator of the delta rule in §4.3), but never connects them to answer
      the remediation question.
   ● PROPOSED PATCH:
          ○ In §3.7 (insert after sentence 2, "A poisoned tensor pins as
              permanently as a true one (§2.10).",
              ):
              Crucially, however, tensor opacity does not make contamination unrecoverable; it
              changes remediation from prose editing to checkpoint scoping and algebraic
              erasure. Because C1 is captured pre-boundary (before an exchange window
              opens) and C2 is captured post-adjudication (§3.2), an unaccepted or
              confabulated emission caught at the boundary is excised by discarding the
              working state and rolling back to the pinned C1 checkpoint — the poisoned turn
              never enters C2. For historical contamination discovered after commit, the
              manifest's capture-point ancestry (§7.2, Class B) supports exact rollback to the
              last uncontaminated checkpoint followed by deterministic replay of
              adjudicated-clean turns, while the delta rule's native Householder erasure S
              \leftarrow S(I - \beta k_{\text{err}} k_{\text{err}}^\top) (§4.3) defines a bounded,
              testable mechanism for targeted subspace eviction without full history replay.
   ● CONFIDENCE: high | §1.5,
      §2.10,
      §3.2,
      §3.7,
      §4.3,
      §7.2 — neutralizes the
      most predictable reviewer attack against replacing human-readable
      text with tensor checkpoints.

CONTRIBUTION 6/10 | §3.2, §4.4, §4.5 | Closing the pre-commit reset/omission loophole
via hash-chained monotonic capture counters (seq_no, prev_capture_hash) and C1
pre-commitment

   ● Hostile-Venue Case (Domains B & D): Section 4.4 claims that moving capture to a
      daemon at C1, C2, C3 eliminates AR-2 survivorship bias: "with no discretionary step
      where a curator's survivorship bias can launder itself as completeness (§2.4)... what is
      captured is decided by architecture declared in advance, and the record can distinguish
      'complete' from 'curated' because completeness is a property of the declared capture
      set, checkable by recomputation (§5)." An adversary (or a reviewer remembering Attack
      1 from Round 6 in §2.3–2.4) will point out a gap: if the manifest rows at C1, C2, C3
      only record independent content hashes without a monotonic capture sequence
      counter seq_no and a hash link prev_capture_hash, or if C1 is buffered locally
      until C3 session close, a curator can abort/restart an unfavorable window five times
      between C1 and C2 and commit only the sixth run! At n=1 (single host owner), local
      daemon suppression before push remains within the AR-1 monism floor (§2.3, §4.5);
      what makes omitted-window detection structural is (a) chaining every capture point
      (seq_no, prev_capture_hash) in the daemon's manifest and (b)
      transmitting/pinning the C1 pre-boundary manifest digest across the boundary when the
      window opens, before the witness generates tokens.
   ● PROPOSED PATCH:
          ○ In §4.4 (replace sentences 2–4,
             ):
             The manifest row is written by the capture path itself — object identifier,
             monotonic capture sequence number seq_no, predecessor row digest
              prev_capture_hash, capture point (C1/C2/C3), layer,
              parametric_base_pin, content hash, authoring instance, and restorability
              class (§3.2) — forming an append-only hash chain across every declared
              boundary so that excising or retrying an intermediate capture between C1 and C2
              breaks sequence continuity. When C1 (pre-boundary) is pinned to the
              counterparty or transparency log as the window opens, the architecture closes
              the post-hoc branch-selection loophole: a session that opened a C1 boundary
              cannot disappear without leaving an unclosed C1 receipt in the chain. At the
              program's actual n=1, where one party controls the daemon's host, pre-push host
              rollback remains subject to the §2.3 monism floor (detectability, never prevention;
              R2-35); once paired with §4.5's n \ge 2 infrastructure-isolated capture-signer role,
              completeness of the declared capture set (C1 → C2 → C3) becomes externally
              enforceable as well as recomputable (§5).

   ● CONFIDENCE: high | §2.3,
      §2.4,
      §3.2,
      §4.4,
      §4.5 — aligns §4.4's
      completeness claim with §2.3/§4.5's n=1 vs. n≥2 threat-model
      floor.

CONTRIBUTION 7/10 | §8.1, §8.3 | Prior-art inoculation against SSM prefix/state caching
(vLLM/SGLang Mamba radix cache, Marconi, RWKV state files) and DeltaNet bib anchors

   ● Hostile-Venue Case (Domain C — Literature & Prior Art):
         ○ Unqualified novelty sentence in §8.3: Section 8.3 currently states: "None of the
             surveyed frameworks treats the model's own recurrent state as the archival
             object, which is the gap §3/§4 occupy." Whereas §8.1 carefully qualifies the claim
             ("no published surface exposes the state as a checkpointable, restorable archival
             object with custody semantics"), §8.3 drops the custody/verification qualifier. A
             reviewer in ML systems will immediately cite SSM/hybrid prefix-state caching
             in serving engines (e.g., Marconi: Prefix Caching for Hybrid State Space
             Models, vLLM/SGLang Mamba/GDN radix state caching, and RWKV/Mamba
             .state prompt-tuning snapshots, which serialize and reload recurrent states
             across turns/sessions) as counterexamples to the unqualified sentence in §8.3.
             Explicitly contrasting unverified latency/prefix state caches (which persist
             recurrent state solely to skip prefill compute, without manifests,
             restore/continuation typing, custody pairs, or recomputation receipts) against
             verifiable archival state custody inoculates §8.3 against this attack.
         ○ DeltaNet bibliography anchor queued in §8.1: Section 8.1 notes that
             DeltaNet's bibliography identifier is queued for re-verification at bib merge. From
             parametric recall ([NET]-unverifiable in this air-gapped run; verify against
           v1.6.1.bib at assembly), the two canonical DeltaNet anchors are Schlag et
           al. (ICML 2021, arXiv:2102.11174) ("Linear Transformers Are Secretly Fast
           Weight Programmers", introducing the fast-weight DeltaNet rule) and Yang et al.
           (NeurIPS 2024, arXiv:2406.06484) ("Parallelizing Linear Transformers with the
           Delta Rule over Sequence Length", introducing the hardware-efficient chunkwise
           parallel DeltaNet algorithm that directly precedes GDN, arXiv:2412.06464).
   ● PROPOSED PATCH:
           ○ In §8.3 (replace sentence 3, "None of the surveyed frameworks
               treats the model's own recurrent state as the archival
               object, which is the gap §3/§4 occupy.",
               ):
               Where recent serving engines and SSM runtimes do materialize or cache
               recurrent states across requests (e.g., prefix/radix state caching for Mamba and
               hybrid linear-attention models, or serialized prompt-state files), they treat the
               tensor strictly as an ephemeral latency cache to amortize prefill compute —
               never as a governed archival atom carrying a manifest schema,
               restore-versus-continuation typing, parametric_base_pin compatibility,
               custody pairs, and fail-closed recomputation receipts, which is the specific
               conjunction §3–§5 occupy.

           ○ In §8.1 (for the witness's bib-merge queue on DeltaNet, sentence 2,
              ):
              DeltaNet — the delta rule introduced for fast-weight transformers (Schlag et al.,
              ICML 2021, arXiv 2102.11174) and parallelized over sequence chunks via the
              WY representation (Yang et al., NeurIPS 2024, arXiv 2406.06484)
              [parametric recall — confirm exact key against v1.6.1 bib at
               assembly] — anchors the line.

   ● CONFIDENCE: high on §8.3 prior-art contrast; med (air-gapped
       parametric recall, [NET]-unverifiable this run) on exact arXiv
       digits for Schlag 2021 / Yang 2024 pending v1.6.1 bib check |
       §8.1,
       §8.3.

CONTRIBUTION 8/10 | §7.4, §7.5 | Aligning §7.4 falsifiable predictions (adding P5 and P6)
with §7.5's three falsification clauses

   ● Hostile-Venue Case (Domain A — Cross-Section Audit): Compare §7.4 (Falsifiable
      predictions) with §7.5 (What would falsify the thesis). Section 7.4 defines four predictions
      (P1 transport fidelity, P2 continuation stability, P3 substrate sufficiency, P4 capture
      timing) — all four testing the substrate claim (§3–§4). Then §7.5 states falsifiers for
      three claims: (1) The substrate claim fails if..., (2) The verification claim fails if the receipt
      chain can be made to pass on a forged substrate by any party cheaper than constructing
      the real one, and (3) The economics claim fails if priced fail-visibility (AFT) measurably
      degrades defect-detection latency relative to the unpriced practice. Because §7.4 lacks
      predictions corresponding to the verification claim (§5) and the economics/AFT claim
      (§6), those two falsifiers appear in §7.5 without matching observables in §7.4.
   ● PROPOSED PATCH:
          ○ In §7.4 (replace sentence 1 "The battery exists to test four
              predictions, each stated with its observable." with "The
              battery exists to test six predictions across the substrate
              (§3–§4), verification (§5), and economics (§6) claims, each
              stated with its observable." and append P5 and P6 before the final
              sentence of §7.4, ):
              P5 (verification cost-asymmetry): under T2's adversarial transport legs, any
              single-bit mutation, stale-pin replay (R-61), or ancestry fork is rejected
              deterministically (100% halt rate) in O(1) chain-execution time per boundary,
              while constructing a passing receipt over a mutated substrate reduces to
              breaking SHA-256 preimage/collision resistance or compromising all k-of-n
              cosigning roles (§5.2, §4.5). P6 (priced fail-visibility non-degradation):
              enforcing AFT-1/2 reduces pre-anchor human-facing token load to zero (VOID
              emission = 0 natural-language tokens before [A]-leg exit 0) without increasing
              boundary defect-detection latency or false-negative admission rates relative to
              unpriced fail-visibility (§6.2).

   ● CONFIDENCE: high | §5.2,
      §6.2,
      §7.4,
      §7.5 — establishes a
      strict 1-to-1 bijection between the paper's claims (§3–§6),
      predictions (§7.4), and falsifiers (§7.5).

CONTRIBUTION 9/10 | §2.3, §2.9, §3.6, §4.6, §5.1, §5.3, §5.4, §5.5, §6.5 | Resolving
cross-version (v1.6.1 §6.4 vs. v1.7 §6.4) and cross-document (PROTOCOL §10 vs.
paper section numbering) reference collisions, plus deictic session pins

   ● Hostile-Venue Case (Domain A — Cross-Section Audit): A full-manuscript pass
      across §1–§8 r1 caught three classes of locator collisions that will confuse an external
      reader once the eight sections are compiled into a single PDF:
         ○ Internal section-number collision on §6.4 (v1.6.1 vs. v1.7):
                ■ In §2.3: "The paper's own §6.4 had already set the honest floor: at n=1,
                    cryptography provides detectability, never prevention (R2-35)".
                ■ In §2.9: "and all three landed inside the paper's own published
                    hide-analysis (Table 6 Surfaces A/C/D; R2-23; R2-35; §6.4)".
                ■ In v1.7, however, §6.4 is "The affect log as a first-class
                     archival object", and v1.7 has no Table 6 (or Table 5)! Those
                     references point to v1.6.1 §6.4 (and v1.6.1 Table 5 / v1.6.1 Table
                     6), just as §7.1 properly writes v1.6 §7 and §5.4 writes v1.6 Prop. 1.
               Leaving bare §6.4 in §2.3 and §2.9 creates a broken internal
               cross-reference inside v1.7.
      ○ Document-namespace collision on bare §10 (PROTOCOL.md §10 vs.
         Paper-2 sections):
            ■ Paper-2 v1.7 has eight sections (§1–§8). Yet §3.6 writes "the §10
                delivery medium", §4.6 writes "the §10 three-artifact
                delivery medium", §5.1 writes "the §10 delivery
                orchestrator", and §5.5 writes "on every push (§10)". To a
              reader of the paper without PROTOCOL.md open beside them, bare §10
              looks like a dangling reference to a nonexistent Section 10 of the
              manuscript.
      ○ Unanchored drafting deictics ("this boundary", "this session"):
            ■ In §4.6 ("28 rows at this writing, R-64 refresh"), §5.1
                ("(record: this boundary's paste-back)"), §5.3 ("this
                boundary's bootstrap ran the manifest verify
                witness-side (28/28, exit 0)... (record: this
                session's [A]-leg)"), and §6.5 ("including the present
                boundary, whose first output was the pull (this
                session's [A]-leg)"), the deictic pronouns refer to the drafting
                boundary anchored at 14ad0f6. Pinning them to (boundary
                14ad0f6, R-64) makes them timeless in the compiled manuscript.
● PROPOSED PATCH:
     ○ In §2.3 (sentence 3, ):
         Replace The paper's own §6.4 had already set with The v1.6.1
         baseline's own §6.4 had already set.
      ○ In §2.9 (sentence 2 & sentence 3,
         ): Replace Table 5
         0/15 broken anchors with v1.6.1 Table 5 0/15 broken anchors,
         and replace (Table 6 Surfaces A/C/D; R2-23; R2-35; §6.4) with
         (v1.6.1 Table 6 Surfaces A/C/D; R2-23; R2-35; v1.6.1 §6.4).
      ○ In §3.4 (sentence 3, ):
         Replace (§7 of the record's own protocol is this principle in
         production) with (PROTOCOL §7 is this principle in
         production).
      ○ In §3.6 (), §4.6
         (), §5.1
         (), and §5.5
         (): Replace bare §10
         with PROTOCOL §10 (the PROTOCOL §10 delivery medium, the
             PROTOCOL §10 three-artifact delivery medium, the PROTOCOL §10
             delivery orchestrator, and on every push (PROTOCOL §10)).
          ○ In §4.6 (), §5.1
             (), §5.3
             (), and §6.5
             (): Replace this
             boundary's paste-back / this session's [A]-leg / the present
             boundary with boundary 14ad0f6 ([A]-leg manifest verify 28/28,
             R-64).
   ● CONFIDENCE: high |
      §2.3,
      §2.9,
      §3.4,
      §3.6,
      §4.6,
      §5.1,
      §5.3,
      §5.5,
      §6.4–6.5 — direct
      cross-section audit.

CONTRIBUTION 10/10 | §4.9, §6.7, §7.7, §8.7 | Repairing misattributed row in §4.9 and
closing cross-section forward-reference ledgers across §1–§8

   ● Hostile-Venue Case (Domain A — Cross-Section Forward-Ref Audit): Because §2
      and §3 were deposited in earlier boundaries (30fb889 and 14ad0f6) and §1, §4–§8
      were drafted together in the completion batch, the forward-reference ledgers at the end
      of §4, §6, §7, and §8 have three concrete discrepancies:
          ○ Duplicate/misattributed row in §4.9
              (): Row 5 of §4.9 reads
             §2.3: training-side analog — delta snapshots taken inside
             the loop (§4) | §4.3, and Row 6 reads §2.4: checkpoints where
             the state exists, training-side analog (§4) | §4.3. Inspection
             of §2.3 () shows that
             §2.3 never mentions training-side delta snapshots; that sentence occurs solely in
             §2.4 ("with the training-side analog of delta snapshots taken
             inside the loop rather than reconstructed from its outputs
             (§4)"). Row 5 of §4.9 is a misattributed duplicate of Row 6, while §2 AR-3
             row: tensor-domain storage; byte-exact state transfer; text
        demoted to adjudication interface (§3–4) is omitted from §4.9's
        table.
     ○ Incomplete incoming references in §6.7
        () and §7.7
        (): Section 6.7 only
        tracks §2 r1 → §6, omitting incoming forward references from §1.4(v) → §6,
        §5.5 → §6 ("priced where it is incurred (§6)"), and §5.6 → §6.3
        ("(AFT-2's ledger is the same asymmetry, seen from the other
        side; §6.3)"). Similarly, §7.7 only tracks §3 r1 → §7 (2 rows), omitting
        incoming forward references from §1.5 → §7, §4.2 → §7 (T3–T4), §4.6 →
        §7, §4.7 → §7.5 (Surface E), and §5.4 → §7.2 (GATE-B/GATE-D).
     ○ Missing §8.7 closure ledger in §8
        (): Sections 3, 4, 5, 6,
        and 7 each end with a Forward-reference ledger (...; closed)
        subsection (§3.8, §4.9, §5.8, §6.7, §7.7), whereas §8 ends at §8.6
        Non-claims and scope without closing incoming references (§1.4, §1.6,
        §7.1).
● PROPOSED PATCH:
     ○ In §4.9 (), replace Row
        5 (| §2.3: training-side analog — delta snapshots taken
        inside the loop (§4) | §4.3 |) with:
        | §2 AR-3 row: tensor-domain storage; byte-exact state
        transfer; text demoted to adjudication interface (§3–4) |
        §4.1–4.2 |


     ○ In §6.7 (), rename
        header to ### 6.7 Forward-reference ledger (§1/§2/§5 r1 → §6;
        closed) and append rows:
        | §1.4(v) & §1.6: AFT case study — pre-bootstrap window and
        asymmetry ledger (§6) | §6.1–6.4 | | §5.5: observation cost
        of every remaining human-facing output is priced where it is
        incurred (§6) | §6.2 | | §5.6: AFT-2's ledger is the same
        asymmetry, seen from the other side (§6.3) | §6.3 |


     ○ In §7.7 (), rename
        header to ### 7.7 Forward-reference ledger (§1/§3/§4/§5 r1 →
        §7; closed) and append rows:
        | §1.4(vi) & §1.5: evaluation battery and thesis under test
        (§7) | §7.1–7.5 | | §4.2: snapshot/restore plumbing and
               capture hooks exercised by §7's battery tiers T3–T4 | §7.3
               (T3–T4) | | §4.6: each migration increment exercised under
               §7's battery before relied on | §7.2–7.3 | | §4.7: FP16/BF16
               gate-perturbation behavior carried as Surface E explicit
               falsifier (§7.5) | §7.3 (T4), §7.5 | | §5.4: GATE-B and
               GATE-D re-typed over state checkpoints (§7.2) | §7.2 |


           ○ In §8 (), add ### 8.7
               Forward-reference ledger (§1/§7 r1 → §8; closed) after §8.6:
               | Reference into §8 | Landing | |---|---| | §1.4 & §1.6:
               related work positions the delta-rule lineage, state-space
               class, memory architectures, and human-in-the-loop
               provenance (§8) | §8.1–8.5 | | §7.1: D5 comparative method
               over candidate substrates | §8.1, §8.3, §8.5 |


   ● CONFIDENCE: high |
       §1.4–1.6,
       §2.2–2.4,
       §3.8,
       §4.9,
       §5.4–5.8,
       §6.7,
       §7.7,
       §8.1–8.6 — exhaustive
       cross-section link audit.

§2 Null-Result Report (Standing Fail-Visible Mandate, §0.4)

Per §0.4 ("domains worked to a null result must be reported as null, not silenced"), the following
audits were executed to completion across §1–§8 r1 and yielded zero defects (null result):

   1. Quantity & Digest Consistency Audit Across §1–§8 (Domain A — NULL):
         ○ R2-56 byte-mutation figures (80 space bytes mutated to NBSP; 11,772 B raw
               paste shifted to ~11,833 B) match identically across §2.5 and §3.3.
           ○ Round-5.7 baseline gate figures (0 standing rebuttals, GATE-D 0/44
               unresolved custody pairs, GATE-A 0/27 page overflows, Table 5 0/15
               broken anchors) match identically between §2.1, §2.9, §7.2, and §7.6.
           ○ Counterweight threshold cutoff (core-hit rate < 30% over N sessions)
               matches identically between §2.8 and §3.3.
       ○ Manifest row count at the 14ad0f6 / R-64 boundary (28 rows / 28/28, exit
          0) and nine-leg orchestrator count (4 consecutive one-shot applications:
          port-001-post, canon-001, session-013 close, §3 r1) are internally
          consistent across §1, §4.6, §5.1, and §5.3.
       ○ Content pins and git commit anchors (30fb889 / 994b1cad… for §2 r1;
          14ad0f6 / 8d4ad638… for §3 r1; d44e8b4 for Task-36; 63ea783d… for RVA
          articulation; 888EAEEF…C7549 for operator GPG fingerprint) match identically at
          every occurrence across §1–§8.
2. Anti-Requirement Spine Bijection AR-1..AR-6 (Domain A/D — NULL):
       ○ Every anti-requirement declared in §2.2 (AR-1 through AR-6) has a dedicated
          evidentiary subsection (§2.3–§2.8), a concrete architectural or protocol
          inversion in §3–§6, and (once Contribution 8 is integrated) a corresponding
          falsifiable prediction and falsifier in §7.4–§7.5.
3. Authorship & Evidence-Standard Audit (Domain D — NULL):
       ○ The R2-2 sole-human-author / model-as-instrument posture declared in §1.3 is
          respected without drift across all eight sections, and every non-executed
          tensor-side mechanism in §3–§7 is explicitly labeled as design/specified rather
          than executed result (Surface E compliance).

