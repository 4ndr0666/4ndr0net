# Telemetry Source: write-ups/paper-2-v1.7-draft3-1-bib-v1.bib
- **Source Identifier**: `write-ups/paper-2-v1.7-draft3-1-bib-v1.bib`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `51be6f9fd2b0bf49f233a8f5998a0acfaac7afaffffe3f9511788231a6d56855`

---

## Raw Telemetry Content

```
% paper-2-v1.7-draft3-1-bib-v1.bib — deposit bibliography, Phase-3 §8.6
% reconciliation (Task-72, trace 1a1845ec2301368d, 2026-10-29 UTC).
%
% Source set: the SEVEN inline arXiv identifiers of the certified draft-3.1
% (paper-2-v1.7-draft3-1-assembled-v1.md, sha256 9b326af7…, commit 384dc27;
% convention register: "arXiv identifiers inline as [arXiv NNNN.NNNNN]").
% Identifier inventory (10 inline sites -> 7 keys): 2102.11174 x1,
% 2406.06484 x2, 2412.06464 x1, 2506.05233 x1, 2510.26692 x1,
% 2605.22791 x1, 2610.26825 x3.
%
% Verification: EVERY entry live-verified against arxiv.org this boundary
% (per-identifier records in
% write-ups/paper-2-v1.7-task72-bib-verification-ledger-v1.md); venue
% strings cross-verified against PMLR and NeurIPS proceedings pages.
% Operator constraint honored: "No unverified citation key is permitted to
% pass without verification" (DeltaNet precedent, trace 1a16c9b26ae3ae31).
% Nothing in this file is silent-trusted.
%
% Author-field ruling (registered in the verification ledger §3): papers
% whose own title page carries a TEAM byline (2510.26692 "Kimi Team";
% 2610.26825 "MemTensor Team") are entered under the team byline with the
% member-enumeration count in a note; the enumerated form is re-derivable
% from the origin at Phase-4 if preferred. Individual-byline papers carry
% their full author lists as fetched.
%
% Carry-forward status: the v1.6.1 bib baseline (state-space survey class,
% HCI alarm-fatigue class, provenance/content-addressing class,
% memory-for-agents stack class) is OPERATOR-HELD (whitepaper tree; not
% witness-reachable — search record in the verification ledger §4). Its
% merge rides Phase-4 after a hash-pinned operator relay. No placeholder
% entries are emitted for it here: an invented or parametric-recall entry
% would violate the no-unverified-key constraint.

@inproceedings{schlag2021linear,
  title         = {Linear Transformers Are Secretly Fast Weight Programmers},
  author        = {Schlag, Imanol and Irie, Kazuki and Schmidhuber, J{\"u}rgen},
  booktitle     = {Proceedings of the 38th International Conference on Machine Learning (ICML)},
  series        = {Proceedings of Machine Learning Research},
  volume        = {139},
  pages         = {9355--9366},
  year          = {2021},
  eprint        = {2102.11174},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG}
}

@inproceedings{yang2024parallelizing,
  title         = {Parallelizing Linear Transformers with the Delta Rule over Sequence Length},
  author        = {Yang, Songlin and Wang, Bailin and Zhang, Yu and Shen, Yikang and Kim, Yoon},
  booktitle     = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
  year          = {2024},
  eprint        = {2406.06484},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG}
}

@inproceedings{yang2025gated,
  title         = {Gated Delta Networks: Improving Mamba2 with Delta Rule},
  author        = {Yang, Songlin and Kautz, Jan and Hatamizadeh, Ali},
  booktitle     = {International Conference on Learning Representations (ICLR)},
  year          = {2025},
  eprint        = {2412.06464},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}

@inproceedings{vonoswald2026mesa,
  title         = {MesaNet: Sequence Modeling by Locally Optimal Test-Time Training},
  author        = {von Oswald, Johannes and Scherrer, Nino and Kobayashi, Seijin and Versari, Luca and Yang, Songlin and Mittal, Sarthak and Schlegel, Maximilian and Maile, Kaitlin and Schimpf, Yanick and Sieberling, Oliver and Meulemans, Alexander and Saurous, Rif A. and Lajoie, Guillaume and Frenkel, Charlotte and Pascanu, Razvan and Ag{\"u}era y Arcas, Blaise and Sacramento, Jo{\~a}o},
  booktitle     = {International Conference on Learning Representations (ICLR)},
  year          = {2026},
  eprint        = {2506.05233},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG}
}

@article{kimi2025linear,
  title         = {Kimi Linear: An Expressive, Efficient Attention Architecture},
  author        = {{Kimi Team}},
  journal       = {arXiv preprint arXiv:2510.26692},
  year          = {2025},
  eprint        = {2510.26692},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  note          = {Technical report; core module Kimi Delta Attention (KDA); 60 listed team members, first-listed Yu Zhang}
}

@article{hatamizadeh2026gateddeltanet2,
  title         = {Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention},
  author        = {Hatamizadeh, Ali and Choi, Yejin and Kautz, Jan},
  journal       = {arXiv preprint arXiv:2605.22791},
  year          = {2026},
  eprint        = {2605.22791},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  note          = {Technical report}
}

@article{memtensor2026memt,
  title         = {MemT-1.0: Towards Memory-Native Evolution},
  author        = {{MemTensor Team}},
  journal       = {arXiv preprint arXiv:2610.26825},
  year          = {2026},
  eprint        = {2610.26825},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  note          = {66 pages, 15 figures, 16 tables; 68 listed team members, first-listed Zhiyu Li}
}

```
