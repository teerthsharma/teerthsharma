<h1 align="center">Teerth Sharma</h1>

<p align="center"><b>Performance and systems engineer — compilers, GPU kernels, ML infrastructure. Research in topology.</b></p>

<p align="center">
📄 <a href="Teerth_Sharma_Resume.pdf"><b>Résumé (PDF)</b></a> &nbsp;·&nbsp; <a href="https://teerthfolio.vercel.app">Portfolio</a> &nbsp;·&nbsp; <a href="https://teerthsharma.vercel.app">Website</a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/teerth-sharma-seal">LinkedIn</a> &nbsp;·&nbsp; <a href="https://orcid.org/0009-0005-0882-9168">ORCID</a> &nbsp;·&nbsp; <code>teerths57@gmail.com</code> &nbsp;·&nbsp; Jaipur, India
</p>

<p align="center">
<img src="https://img.shields.io/badge/upstream%20landings%202026-11-1f6feb?style=flat-square" alt="11 upstream landings in 2026">
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA">
<img src="https://img.shields.io/badge/Triton-2b2b2b?style=flat-square" alt="Triton">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
</p>

---

I make systems that already run at scale use less memory, run faster, and give the same answer twice. In 2026 that meant eleven contributions landed in production machine-learning infrastructure at Google DeepMind, Google, OpenAI, NVIDIA and Meta, each reviewed and accepted by the team that owns the code, one credited by name in the MuJoCo 3.11.0 release notes. Alongside that I do research in topology: persistent homology applied to attention scheduling and hallucination detection.

The pattern across the merged work is one move. A hot path pays quadratic or redundant cost because it ignores a partial order, a connectivity relation or an interval structure already present in its own data. The change replaces the scan with the structure.

## Experience

### KarmicSphere Media — [NovelPedia (now NovelCult)](https://novelcult.com/) — Jaipur, India — January 2025 to June 2026

- **Founding Engineer** · January 2025 – December 2025 · TypeScript, Next.js, Linux, Azure. Helped build the platform from scratch as part of the founding team — the services behind reading, discovery and the author portal — now carrying **15,000 accounts**, **100,000 viewers** and **200,000 chapters**.
- **TTS Division Lead** · December 2025 – June 2026 · Python, Django, Azure Speech. Stood up and led the text-to-speech division, narrating **9,000+ chapters** end to end while holding synthesis to **under $2 of Azure credit per chapter**.

### [Google DeepMind](https://github.com/google-deepmind) — Open Source Contributor — 3 merged, July–August 2026

- **[MuJoCo](https://github.com/google-deepmind/mujoco)** · C/C++ · **1,281× less solver memory.** Large robot scenes ran out of memory long before they ran out of compute: the constraint solver sized its scratch buffer on the square of the body count. Replacing the dense adjacency matrix and flood fill with a disjoint-set forest made that growth linear, and the union-find primitives are now public API. **[Credited by name in the MuJoCo 3.11.0 release notes.](https://mujoco.readthedocs.io/en/3.11.0/changelog.html#version-3-11-0-july-27-2026)** ([PR #3396](https://github.com/google-deepmind/mujoco/pull/3396))
- **[MuJoCo Warp](https://github.com/google-deepmind/mujoco_warp)** · Python, NVIDIA Warp · **1.51× faster GPU island discovery in linear memory.** The GPU port carried the same quadratic per-world adjacency plus a DFS stack. Replaced both with a persistent parent array and three allocation-free, CUDA-graph-capturable phases, one 32-lane block per world; island labels stay bitwise-identical under row and endpoint reordering. On a 2,048-world checkpoint with 247,308 active constraint rows: matched the dense kernels exactly in every A-B-B-A block, **1.513× faster by geometric mean, 99% CI [1.406×, 1.584×]**. ([PR #1541](https://github.com/google-deepmind/mujoco_warp/pull/1541))
- **[MuJoCo](https://github.com/google-deepmind/mujoco)** · C++ · **faster model loading.** Loading a detailed mesh got slower the more detailed it was. Removed a second quadratic scan in convex-hull construction, cutting probes by a factor of 3V/8, with every mesh checksum coming back byte-identical. ([PR #3450](https://github.com/google-deepmind/mujoco/pull/3450))

### [Google](https://github.com/google) — Open Source Contributor — 4 landed, July–August 2026

- **[XLA](https://github.com/openxla/xla)** · C++ · **deterministic GPU reduction grouping.** Compiling the same module twice could produce different reduction groups: union-find merge order in GroupDisjointReductions followed hash order, so the blockIdx.z constraint in the resulting indexing map varied between builds. Switched to an insertion-ordered set, making group order a function of the graph alone. Landed on main through Google's internal import as commit [3d5df1d](https://github.com/openxla/xla/commit/3d5df1da699bfb63cbeedaa56f09885c7974b06e). ([PR #46539](https://github.com/openxla/xla/pull/46539))
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** · C++ · **reproducible distributed training.** The same model could schedule differently on two identical runs, which makes a failure impossible to reproduce. The pass that orders collective operations relied on a reachability map that was never transitively closed, so redundant edges survived and hash ordering picked the winners. Rebuilt it as an exact bit-matrix closure, making the emitted graph a function of the model alone. ([PR #124410](https://github.com/tensorflow/tensorflow/pull/124410))
- **[XNNPACK](https://github.com/google/XNNPACK)** · C · **32 MiB lower inference workspace.** XNNPACK is the inference backend under TensorFlow Lite, so its memory ceiling decides whether a model fits on the device at all. Taught the planner to reuse the arena gap ahead of the first live tensor: 6.4% off MobileNet V1 peak allocation, outputs byte-identical. ([PR #10801](https://github.com/google/XNNPACK/pull/10801))
- **[Highway](https://github.com/google/highway)** · C++ SIMD · **65× cheaper perfect-hash builds.** Building a perfect hash over a million keys did 894 million pairwise comparisons. Pruning candidates by slice structure took that to 13.6 million and found exactly the same duplicates. ([PR #3244](https://github.com/google/highway/pull/3244))

### [OpenAI](https://github.com/openai) — Open Source Contributor — merged July 2026

- **[Triton](https://github.com/triton-lang/kernels)** · Triton, Python · **3.48× faster long-context attention.** Attention over long sequences spends most of its time on blocks that contribute almost nothing. Contributed a sparse attention kernel that skips 81% of blocks at 4K context and still lands within 1e-3 of the dense result, shipped with a benchmark runner so the number survives inspection. Relocated from Triton core on maintainer advice, then merged. ([PR #22](https://github.com/triton-lang/kernels/pull/22))

### [NVIDIA](https://github.com/NVIDIA) — Open Source Contributor — 2 merged, August 2026

- **[NeMo-Relay](https://github.com/NVIDIA/NeMo-Relay)** · Rust · **prompt-cache reuse unblocked.** The cache that should make repeated LLM calls cheap almost never fired. Its governor keyed learning on the first user message, so workflows sharing a system prompt fragmented into one profile per task and never gathered enough evidence to reuse anything. Re-keyed on the stable scaffold and took cross-process agreement from 0.48 to 1.00 — scoped down to a single crate after maintainer review. ([PR #481](https://github.com/NVIDIA/NeMo-Relay/pull/481))
- **[Topograph](https://github.com/NVIDIA/topograph)** · Helm, Kubernetes · **least-privilege RBAC.** The chart granted cluster-wide Kubernetes permissions regardless of configuration — an install that never touches the Kubernetes API still received cluster-wide pods, nodes and daemonsets access. Gated every RBAC rule on the selected engine and provider, dropping the ClusterRole entirely when none applies; 141/141 chart unit tests. ([PR #432](https://github.com/NVIDIA/topograph/pull/432))

### [Meta](https://github.com/facebook) — Open Source Contributor — landed July 2026

- **[Pyrefly](https://github.com/facebook/pyrefly)** · Rust · **type-checker crash pinned down.** Meta's Python type checker panicked mid-commit on large codebases when dependency chains ran deeper than the incremental recheck budget. Landed the reproducer that isolates it — 208 chained components — with the maintainer confirming the mechanism on the thread. Shipped in release 1.2.0 via commit [3e90baa](https://github.com/facebook/pyrefly/commit/3e90baa2a44754983666b1b33cd3bcfb1b0e4a94). ([PR #4180](https://github.com/facebook/pyrefly/pull/4180))

## Selected systems

- **[Topological ML Toolkit](https://github.com/teerthsharma/topological-ml-toolkit)** · Rust, Python, C++/AVX-512, CUDA. Turns point clouds and time series into persistence diagrams and Betti features through scikit-learn-style transformers. Four backends, one contract, checked against ripser and GUDHI.
- **[Epsilon-Hollow](https://github.com/teerthsharma/Epsilon-Hollow)** · Rust, x86-64 assembly, Linux, QEMU/UEFI, Lean 4. Research OS testing how much of a kernel can be written in safe Rust: UEFI boot, SMP bring-up, four-level paging, demand paging, scheduling and a VFS — verified under Miri, booted in QEMU on every commit. The README carries the gate table and says first that nothing in the kernel is production-tested.
- **[Caustic](https://github.com/teerthsharma/caustic)** · Python, PyTorch, HuggingFace. Detects LLM hallucinations without ground-truth labels by measuring orbit collapse — when a model's internal geometry maps distinct entities onto one answer — and turns that partition into a certified lower bound on error rate, with an inference-time governor that picks its own intervention strength blind. 0.995 AUROC on collapse-type failures at sub-0.5B scale; 163 tests, CI across Python 3.10–3.12, and a [published results page](https://teerthsharma.github.io/caustic/) documenting where the method does not hold.

## Research in topology

The same idea, structure already in the data, as a research programme rather than a fix.

- **[Aether-Lang](https://github.com/teerthsharma/Aether-Lang)** · Rust, Lean 4. A DSL and runtime where persistent homology is a language primitive and loops terminate on topological invariants, compiling to `no_std` binaries for bare metal. 229 tests, 52 injected mutants surviving, six earlier claims killed by the mutation harness and documented under *What We Got Wrong*.
- **[faraday](https://github.com/teerthsharma/faraday)** · Python. 3D dielectric electromagnetic solver whose learned reduced-order coupling operator reaches a Banach fixed point at 1.755 × 10⁻¹⁶ after a 50,000-epoch burn. The run reproduces from a checkpoint in the repo.
- **[sigmoid](https://github.com/teerthsharma/sigmoid)** · Python. Converts a trained model into a world model without retraining: activation windows to persistence barcodes, a Hilbert-series embedding, a linear coupling operator with a Banach contraction certificate when ‖T‖ < 1, and a sheaf-consistency gate that fires when an imagined trajectory leaves the calibrated manifold.
- **[Electromagnetic-Field-Data-Simulator](https://github.com/teerthsharma/Electromagnetic-Field-Data-Simulator)** · TypeScript, React, Rust/Python core. Visualisation front-end for the physics work, deployed as a static GitHub Pages site.
- **OpenCLAW-P2P v7.0** — co-author, [arXiv:2604.19792](https://arxiv.org/abs/2604.19792), 2026. Decentralized peer-review protocol for AI research, with resilient persistence and live verification of cited references.

## Technical range

```text
Languages:    Rust, C++, Python, CUDA, Triton, x86-64 assembly (AVX-512), Lean 4, TypeScript
Systems:      GPU kernels, compilers, runtimes, operating systems, Linux, QEMU/UEFI, performance profiling, Docker, GitHub Actions, CI/CD
ML:           PyTorch, JAX, TensorFlow, scikit-learn, sparse attention, inference optimisation, persistent homology, reproducible benchmarking
```

## Open to

- Performance, inference and compiler engineering roles, including research engineering
- Residencies, research apprenticeships and mentored research placements
- Collaborations that put persistent homology into a real training or inference pipeline

## Contact

- **Email:** `teerths57@gmail.com`
- **Résumé:** [Teerth_Sharma_Resume.pdf](Teerth_Sharma_Resume.pdf)
- **Portfolio:** [teerthfolio.vercel.app](https://teerthfolio.vercel.app)
- **Website:** [teerthsharma.vercel.app](https://teerthsharma.vercel.app)
- **GitHub:** [@teerthsharma](https://github.com/teerthsharma)
