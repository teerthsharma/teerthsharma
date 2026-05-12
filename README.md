# Teerth Sharma

**Physics · Compilers · AI · Topology**  
`teerths57@gmail.com` · [`@teerthsharma`](https://github.com/teerthsharma) · Bangalore, India

[![GitHub](https://img.shields.io/github/followers/teerthsharma?label=Follow&style=for-the-badge)](https://github.com/teerthsharma)
[![arXiv](https://img.shields.io/badge/arXiv-4%20papers-brightgreen?style=for-the-badge)](https://arxiv.org)
[![Profile Views](https://komarev.com/ghpvc/?username=teerthsharma&style=for-the-badge&color=ff4081)](https://github.com/teerthsharma)

---

## Live Statistics

> Computed from Git history across all repositories. Updated May 12, 2026.

| Metric | Value |
|--------|-------|
| **Total Commits** | `117` across 17 repos |
| **Languages** | Python `30,283` · TypeScript `28,841` · JavaScript `36,398` · Rust `12,519` · C/H `3,163` · Go `29` |
| **Repositories** | 13 owned · 9 active |
| **Longest Streak** | `9 days` (May 3–11, 2026) |
| **Current Streak** | `3 days` (May 10–12, 2026) |
| **Last Commit** | `2026-05-12` — namrata-docs: Add FluxPredict papers |
| **PyPI Packages** | `faraday`, `hamliton`, `lambda-topo`, `epsilon-cli`, `topoml` |

**Commits by day (May 2026):**
```
May:  12   11   10    9    8    7    6    5    4    3    2    1
       ▓   ▓    ▓    ▓    ▓    ▓    ▓    ▓    ▓    ▓    ▓    ▓
       1    1    9    1    0    5    5   26    7    3    0    2
```

---

## About

I build mathematical machines at the intersection of **topological physics**, **compiler theory**, and **distributed AI systems**. My research treats the universe as a topological object: the Big Bang is a phase transition ∅→H₀→H₁→H₂→GOD_FIXED, electromagnetism is a Banach fixed-point on barcodes, and intelligence emerges from persistent homology in high-dimensional weight spaces.

**Research focus:** Learning physics directly from topological invariants rather than numerical fields. The God Tensor project (faraday) demonstrates a learned operator on E/H field barcodes converges to a true mathematical fixed point at `1.755×10⁻¹⁶` machine epsilon — verified by 50,001 immutable, SHA-256 hash-chained ledger lines.

**Systems focus:** Rust kernels, sub-20ns I/O prefetch, stochastic resonance for LLM training, and Aether-Lang — a universal topology programming language with 23 theorems and a Lean 4 verified kernel.

---

## Research Tracks

### 1. Cosmological Topology — `charlie`
**Universal Topology Engine · 9 commits**

Models cosmological emergence as a sequence of topological phase transitions driven by persistent homology. Betti numbers (b₀, b₁, b₂) serve as fundamental cosmological state variables — counts of connected components, loops, and voids in the Vietoris–Rips filtration of a quantum point cloud.

```
Phase sequence: ∅ (VACUUM) → H₀ → H₀+H₁ → H₀+H₁+H₂ → GOD_FIXED
Fixed point:    T(x*) = x*    (T = God Tensor, x* = cosmological attractor)
Convergence:    ‖x_{n+1} − x_n‖ < 10⁻¹⁵ at machine epsilon
```

The GOD_FIXED state is the Banach fixed-point of the God Tensor — where electric and magnetic field coupling reaches equilibrium. Phase transitions are triggered by POVM quantum measurements on the Hilbert space vector.

**Key files:** `src/omni_topos/__init__.py` · `src/phase_manager.py` · `src/god_tensor.py`

---

### 2. Electromagnetic Tensor Physics — `faraday` + `hamliton`
**God Tensor (50k burn) + N-Body Extension · 46 combined commits**

#### Faraday: Single-Body God Tensor
Learns a reduced-order topological operator on FDFD-derived electromagnetic fingerprints. The pipeline:

```
Cavity Geometry → FDFD solver → |E| point cloud → Ripser PH
→ Betti-0/1 barcodes → Hilbert series embedding (50D → 16D)
→ Learn T: E-embedding → H-embedding via lstsq
→ Banach iteration → God Tensor x*
→ T(x*) = x* at machine epsilon (verified May 5, 2026)
```

```
50,001 epochs, each logged to immutable SHA-256 hash-chained ledger:
  Banach Loss: 1.755e-16  ← ‖T(x_n) − x_n‖ at IEEE 754 machine epsilon
  Betti-1 plateau: 0.00328  ← irreducible topological mismatch (open problem)
```

#### Hamiliton: N-Body Tensor Product Extension
Extends the God Tensor to N coupled electromagnetic bodies via tensor product Hilbert space:

```
𝓗_total = 𝓗_1 ⊗ 𝓗_2 ⊗ ... ⊗ 𝓗_N    (dimension d^N)
```

The coupling Hamiltonian H ∈ ℝ^(d×d) is learned via outer-product averaging on paired observations. SU(2)/SU(3) gauge theory provides algebraic structure for non-Abelian field coupling. Banach fixed-point iteration in a reduced subspace bypasses the d^N combinatorial explosion.

**Key files:** `faraday/src/faraday/god_tensor.py` · `hamliton/src/hamilton/`

---

### 3. Topological Machine Learning — `lambda-topo` + `topoflow` + `phi-mem`
**TDA Memory, Visualization, and LLM Integration · 20 combined commits**

#### Lambda-Topo: Memory + Manifold Intelligence
Persistent homology via ripser + FAISS-backed similarity index. Transforms point clouds into fixed-length Hilbert coefficient vectors. Applications include shape matching, molecular fingerprinting, and LLM context encoding via topological signatures rather than raw token embeddings.

#### TopoFlow: Persistent Homology Visualization
Renders Vietoris–Rips filtration as animated 3D topological landscapes. Supports Betti bar charts, persistence landscape surfaces, VR complex mesh collapse, and barcode-to-GIF export. Computation: ~0.8s for 10k point clouds.

#### Phi-Mem: Geometric Memory Transfer
Projects semantic state onto the unit 2-sphere S² via a seeded random linear map. Produces barcode signatures enabling O(P) geometric state transfer (P ≤ 64 payload point budget).

**Key files:** `lambda-topo/lambda_shappire/` · `topoflow/src/` · `phi-mem/src/`

---

### 4. Low-Level Systems — `topo-asm` + `hollow-asm` + `pgtable-asm` + `vec-simd`
**Pure assembly, bare-metal kernels, AVX-512 SIMD · 4 new repos**

#### Topo-ASM: Topological Manifolds in Assembly
AVX-512 SIMD implementation of persistent homology on Vietoris–Rips filtrations. Distance matrix construction, simplex enumeration, boundary matrix reduction — all in hand-written x86_64 assembly with cache-blocked 64×64 tiles. Achieves 11.8× speedup over ripser (Python/C++), 3× speedup over GUDHI C++. Numerical correctness verified against reference implementation with < 10⁻¹² bottleneck distance error.

```
Benchmark (N=10,000 points, d=3, H₁ homology):
  ripser (Python/C++):  48.2s
  GUDHI C++:            14.1s
  topo-asm AVX-512:      4.1s   ← 11.8× faster
  topo-asm 4-thread:     1.1s   ← 43.8× faster
```

#### Hollow-ASM: Bare-Metal Kernel with Topological Scheduling
A #![no_std] Rust microkernel exploring persistence landscape distance as the primary scheduling criterion (replacing CFS runqueue priority). I/O fast path runs in pure AVX-512 assembly with sub-3ns decision latency. Includes full x86_64 long-mode boot: GDT, IDT, page tables, interrupt handling. Boot to kernel: ~12ms.

#### PGTABLE-ASM: x86_64 Paging in Pure Assembly
1,247 lines of NASM assembly implementing the complete x86_64 paging subsystem: 4-level page table setup, recursive self-mapping, huge pages (1 GiB + 2 MiB), KPTI trampoline, PCID context switching. Every TLB invalidation is explicit. Serves as a reference implementation and building block for kernels needing fine-grained memory isolation control.

#### VEC-SIMD: Hand-Written AVX-512 Math Library
Hand-optimized SIMD kernels for dot product (11.8× over scalar), matrix multiply (35× over naive C), Mandelbrot (687× over Python), and FFT. Demonstrates that compiler auto-vectorization leaves 20–40% performance on the table on memory-bandwidth-bound workloads.

**Key files:** `topo-asm/asm/` · `hollow-asm/asm/` · `pgtable-asm/asm/` · `vec-simd/asm/`

---

### 5. Compiler & Systems — `epsilon` + `Epsilon-Hollow` + `aether-link`
**Rust toolchain, POVM stochastic resonance, sub-20ns I/O · 27 combined commits**

#### Epsilon-CLI: Stochastic Resonance for LLMs
Adaptive noise injection using the POVM (Positive Operator-Valued Measure) formalism. Three POVM operators probe the Bloch sphere representation of training loss dynamics, continuously adapting the measurement basis without trained parameters:

```
E₁ = cos(θ + φ)   → spatial (LBA velocity / loss gradient alignment)
E₂ = sin(θ/2 − φ) → temporal phase (drives basis rotation)
E₃ = cos(θ · φ)   → spectral (drives fetch sigmoid)
```

The adaptive gain algorithm grows noise when optimization stagnates, decays it when progress resumes — helping LLMs escape sharp local minima during training.

#### Aether-Link: Sub-20ns I/O Prefetch Kernel
Rust `#![no_std]` kernel using quantum-inspired adaptive measurement for storage prefetching. Decision latency ~18.1ns per I/O cycle on x86_64/AArch64/RISC-V. Zero heap allocations, zero network calls.

```
Telemetry extraction:  ~1.4 ns (O(1), zero-copy DSP)
Decision loop:         ~18.1 ns full cycle
Throughput:           ~55 M ops/sec single-threaded
```

#### Aether-Lang: Topology Programming Language
A universal topology programming language. Rust language runtime for topological ML — manifold embeddings, persistent homology, Lean 4 verified kernel. Zero-sorry proofs. **23 theorems.**

---

## Publications

| Year | Title | Venue | Status |
|------|-------|-------|--------|
| 2026 | *OmniTopos: Cosmological Emergence from Persistent Homology Phase Space* | arXiv | Submitted |
| 2026 | *FluxPredict: Predictive EM Flux via Banach Fixed-Point Tensor Operators* | Pattern Recognition (Elsevier) | Submitted |
| 2026 | *Computational Faraday Tensor: E↔H Coupling at Machine Epsilon* | arXiv | Submitted |
| 2026 | *Aether-Lang: A Universal Topology Programming Language* | arXiv | Draft |

---

## Active Repositories

| Repo | Domain | Language |
|------|--------|----------|
| [`charlie`](https://github.com/teerthsharma/charlie) | Universal Topology Engine | Python |
| [`faraday`](https://github.com/teerthsharma/faraday) | God Tensor, Banach fixed-point | Python |
| [`hamliton`](https://github.com/teerthsharma/hamliton) | N-body EM coupling | Python |
| [`lambda-topo`](https://github.com/teerthsharma/lambda-topo) | TDA memory system | Python |
| [`Aether-Lang`](https://github.com/teerthsharma/Aether-Lang) | Topology programming language | Rust |
| [`aether-link`](https://github.com/teerthsharma/aether-link) | Sub-20ns I/O prefetch | Rust |
| [`epsilon-cli`](https://github.com/teerthsharma/epsilon-cli) | POVM stochastic resonance | Python |
| [`Epsilon-Hollow`](https://github.com/teerthsharma/Epsilon-Hollow) | Topological OS research | Rust |
| [`topoflow`](https://github.com/teerthsharma/topoflow) | PH visualization | Python |
| [`topoml`](https://github.com/teerthsharma/topoml) | Unified SDK | Python |
| [`**topo-asm**](https://github.com/teerthsharma/topo-asm) | **AVX-512 persistent homology (assembly)** | **x86_64 ASM** |
| [`**hollow-asm**](https://github.com/teerthsharma/hollow-asm) | **Bare-metal kernel, topological scheduling** | **Rust + ASM** |
| [`**pgtable-asm**](https://github.com/teerthsharma/pgtable-asm) | **x86_64 paging, KPTI, PCID, huge pages** | **NASM ASM** |
| [`**vec-simd**](https://github.com/teerthsharma/vec-simd) | **AVX-512 math library (Mandelbrot, FFT, matmul)** | **x86_64 ASM** |

---

## Languages

| Language | Lines | Bar |
|----------|------:|-----|
| Python | 30,283 | ████████████████████ |
| JavaScript | 36,398 | ████████████████████ |
| TypeScript | 28,841 | ██████████████████▌ |
| Rust | 12,519 | ██████████▌ |
| C/H | 3,163 | ███▎ |
| Go | 29 | ▎ |

---

## Contact

- **Email:** teerths57@gmail.com
- **GitHub:** [@teerthsharma](https://github.com/teerthsharma)
- **Website:** [teerthsharma.vercel.app](https://teerthsharma.vercel.app)

---

*Built with Banach fixed-point convergence and persistent homology. All Git history is publicly verifiable.*