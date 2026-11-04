# Telemetry Source: write-ups/paper-2-v1.7-draft3-1-bib-v2.bib
- **Source Identifier**: `write-ups/paper-2-v1.7-draft3-1-bib-v2.bib`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `18d1e05fbdc7258df181aaf98d894534f308b94c7f8ff4c8931a66a410c5599e`

---

## Raw Telemetry Content

```
% paper-2-v1.7-draft3-1-bib-v2.bib — Phase-4 merged deposit bibliography
% (Task-73, trace 1a184806a91640c9, 2026-10-29 UTC).
%
% Composition: the SEVEN record-verified core entries of
% paper-2-v1.7-draft3-1-bib-v1.bib (Task-72, 7/7 live-verified; byte-preserved
% below, first) + TWENTY-ONE carried entries from the operator-relayed tree
% bibliography of record refs-2.bib (sha256 798d1dd4..., "the only bib file in
% the tree", relayed 2026-10-29 — the v1.6.1-baseline successor), each
% live-verified against origin sources this boundary (per-identifier records in
% write-ups/paper-2-v1.7-task72-bib-verification-ledger-v1.md SS7).
%
% Dedup ruling (ledger SS4 disposition): the draft-3.1 set prevails for the
% inline core; the six tree entries whose work the core already carries were
% dropped (yang2024deltanet, yang2024gdn, vonoswald2026mesanet,
% kimiteam2025kimilinear, hatamizadeh2026gdn2, schlag2021linear).
%
% No unverified citation key passes: any entry whose origin verification could
% not be completed this boundary is EXCLUDED and registered as pending in the
% ledger — never a placeholder.

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

@article{siems2026ckda,
  author  = {Julien Siems and Riccardo Grazzi and Korbinian P{\"o}ppel and Jaisidh Singh and Arber Zela and Timur Carstensen and Jenia Jitsev and Frank Hutter and Volkan Cevher and Antonio Orvieto and Aaron Klein},
  title   = {Complex {KDA}: Understanding and Enhancing the Expressivity of Kimi Delta Attention},
  journal = {arXiv preprint arXiv:2609.24797},
  year    = {2026}
}

@inproceedings{yang2024gla,
  author    = {Songlin Yang and Bailin Wang and Yikang Shen and Rameswar Panda and Yoon Kim},
  title     = {Gated Linear Attention Transformers with Hardware-Efficient Training},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
  note      = {arXiv:2312.06635},
  year      = {2024}
}

@inproceedings{katharopoulos2020transformers,
  author    = {Angelos Katharopoulos and Apoorv Vyas and Nikolaos Pappas and Fran{\c{c}}ois Fleuret},
  title     = {Transformers are {RNN}s: Fast Autoregressive Transformers with Linear Attention},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  pages     = {5156--5165},
  year      = {2020}
}

@inproceedings{arora2024zoology,
  author    = {Simran Arora and Sabri Eyuboglu and Aman Timalsina and Isys Johnson and Michael Poli and James Zou and Atri Rudra and Christopher R{\'e}},
  title     = {Zoology: Measuring and Improving Recall in Efficient Language Models},
  booktitle = {The Twelfth International Conference on Learning Representations (ICLR)},
  year      = {2024}
}

@inproceedings{dao2024mamba2,
  author    = {Tri Dao and Albert Gu},
  title     = {Transformers are {SSM}s: Generalized Models and Efficient Algorithms Through Structured State Space Duality},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
  pages     = {10041--10071},
  year      = {2024}
}

@article{lahoti2026mamba3,
  author  = {Aakash Lahoti and Kevin Y. Li and Berlin Chen and Caitlin Wang and Aviv Bick and J. Zico Kolter and Tri Dao and Albert Gu},
  title   = {Mamba-3: Improved Sequence Modeling Using State Space Principles},
  journal = {The Fourteenth International Conference on Learning Representations (ICLR)},
  year    = {2026}
}

@inproceedings{widrow1960adaptive,
  author    = {Bernard Widrow and Marcian E. Hoff},
  title     = {Adaptive Switching Circuits},
  booktitle = {IRE WESCON Convention Record},
  pages     = {96--104},
  year      = {1960}
}

@inproceedings{bischof1985wy,
  author    = {Christian H. Bischof and Charles Van Loan},
  title     = {The {WY} Representation for Products of Householder Matrices},
  booktitle = {SIAM Conference on Parallel Processing for Scientific Computing},
  year      = {1985}
}

@inproceedings{merkle1988,
  author    = {Ralph C. Merkle},
  title     = {A Digital Signature Based on a Conventional Encryption Function},
  booktitle = {Advances in Cryptology --- CRYPTO '87},
  pages     = {369--378},
  year      = {1988}
}

@misc{laurie2013ct,
  author       = {Ben Laurie and Adam Langley and Emilia Kasper},
  title        = {Certificate Transparency},
  howpublished = {RFC 6962, Internet Engineering Task Force},
  year         = {2013}
}

@inproceedings{torresarias2019intoto,
  author    = {Santiago Torres-Arias and Hammad Afzali and Trishank Karthik Kuppusamy and Reza Curtmola and Justin Cappos},
  title     = {in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes},
  booktitle = {28th USENIX Security Symposium},
  pages     = {1393--1410},
  year      = {2019}
}

@inproceedings{samuel2010tuf,
  author    = {Justin Samuel and Nick Mathewson and Justin Cappos and Roger Dingledine},
  title     = {Survivable Key Compromise in Software Update Systems},
  booktitle = {Proceedings of the 17th ACM Conference on Computer and Communications Security (CCS)},
  pages     = {61--72},
  year      = {2010}
}

@inproceedings{newman2022sigstore,
  author    = {Zachary Newman and J. Scott Meyers and Santiago Torres-Arias},
  title     = {Sigstore: Software Signing for Everybody},
  booktitle = {Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security (CCS)},
  pages     = {2353--2367},
  year      = {2022}
}

@article{costan2016sgx,
  author  = {Victor Costan and Srinivas Devadas},
  title   = {Intel {SGX} Explained},
  journal = {Cryptology ePrint Archive, Paper 2016/086},
  year    = {2016}
}

@inproceedings{mitchell2019modelcards,
  author    = {Margaret Mitchell and Simone Wu and Andrew Zaldivar and Parker Barnes and Lucy Vasserman and Ben Hutchinson and Elena Spitzer and Inioluwa Deborah Raji and Timnit Gebru},
  title     = {Model Cards for Model Reporting},
  booktitle = {Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT*)},
  pages     = {220--229},
  year      = {2019}
}

@article{packer2023memgpt,
  author  = {Charles Packer and Sarah Wooders and Kevin Lin and Vivian Fang and Shishir G. Patil and Ion Stoica and Joseph E. Gonzalez},
  title   = {{MemGPT}: Towards {LLM}s as Operating Systems},
  journal = {arXiv preprint arXiv:2310.08560},
  year    = {2023}
}

@article{zaharia2018mlflow,
  author  = {Matei Zaharia and Aaron Chen and Andrew Davidson and Ali Ghodsi and Sue Ann Hong and Andy Konwinski and Siddharth Murching and Tomas Nykodym and Paul Ogilvie and Mani Parkhe and others},
  title   = {Accelerating the Machine Learning Lifecycle with {MLflow}},
  journal = {IEEE Data Engineering Bulletin},
  volume  = {41},
  number  = {4},
  pages   = {39--45},
  year    = {2018}
}

@misc{dvc2020,
  author       = {{Iterative}},
  title        = {{DVC}: Data Version Control},
  howpublished = {\url{https://dvc.org}},
  note         = {Open-source version control for machine learning; accessed 2026-10},
  year         = {2020}
}

@book{chacon2014git,
  author    = {Scott Chacon and Ben Straub},
  title     = {Pro Git},
  edition   = {2nd},
  publisher = {Apress},
  year      = {2014}
}

@inproceedings{stevens2017sha1,
  author    = {Marc Stevens and Elie Bursztein and Pierre Karpman and Alex Albertini and Yarik Markov},
  title     = {The First Collision for Full {SHA-1}},
  booktitle = {Advances in Cryptology --- CRYPTO 2017},
  note      = {SHAttered},
  year      = {2017}
}

@misc{gutierrez2026articulation,
  author       = {Alejandro Gutierrez},
  title        = {1=1---The Rehydration-Verification Architecture: Official Articulation, v1.0},
  howpublished = {Hash-pinned artifact, \nolinkurl{github.com/4ndr0666/glm-working-memory}},
  note         = {2026-10-19; ORCID 0009-0008-0976-3895; AI assistance disclosed (GLM/Z.ai, instrument class)},
  year         = {2026}
}

```
