#!/usr/bin/env python3
"""Render the animated ticker cards for the profile README.

Each card cycles one entry at a time: 11 upstream landings, 7 projects. The
slides are plain CSS keyframes on opacity plus a small translate, which GitHub
serves through its image proxy intact -- no SMIL, no scripts, no web fonts.

    python gen.py            # writes commits.svg and systems.svg
    python gen.py --check    # width guard only, writes nothing
"""
import sys

W, H = 840, 264
DUR = 2.6                      # seconds per slide
PAD = 26                       # left gutter
# monospace advance widths, measured as a fraction of font-size
ADV = 0.6


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def overflows(text, size):
    """True if text at this font-size would run past the card's right edge."""
    return PAD + len(text) * size * ADV > W - 16


def card(out, aria, prompt, footer, slides):
    n = len(slides)
    total = n * DUR
    seg = 100.0 / n
    fin, fout = seg * 0.10, seg * 0.90
    tick_w = (W - 2 * PAD - (n - 1) * 8) / n

    bad = []
    for name, tag, head, meta, _ in slides:
        if overflows(head, 26):
            bad.append(f"  headline overflows ({len(head)} chars): {head}")
        if overflows(meta, 15):
            bad.append(f"  meta overflows ({len(meta)} chars): {meta}")
    if bad:
        print(f"{out}: FAIL", *bad, sep="\n")
        return False

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="{esc(aria)}">',
        f"<title>{esc(aria)}</title>",
        "<style>",
        '  .m { font-family: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas,'
        ' "Liberation Mono", monospace }',
        "  .prompt { fill: #6e7681; font-size: 15px }",
        "  .repo { fill: #58a6ff; font-size: 18px; font-weight: 600 }",
        "  .tag { fill: #6e7681; font-size: 16px }",
        "  .head { fill: #e6edf3; font-size: 26px; font-weight: 700 }",
        "  .meta { fill: #8b949e; font-size: 15px }",
        f"  .slide {{ opacity: 0; animation: cyc {total}s linear infinite }}",
        "  .tick { fill: #21262d }",
        f"  .tick-on {{ fill: #58a6ff; opacity: 0; animation: cyc {total}s linear infinite }}",
        "  .cursor { fill: #3fb950; animation: blink 1.1s steps(1) infinite }",
        "  @keyframes cyc {",
        "    0%          { opacity: 0; transform: translateY(7px) }",
        f"    {fin:.4f}%  {{ opacity: 1; transform: translateY(0) }}",
        f"    {fout:.4f}% {{ opacity: 1; transform: translateY(0) }}",
        f"    {seg:.4f}%  {{ opacity: 0; transform: translateY(-7px) }}",
        "    100%        { opacity: 0; transform: translateY(-7px) }",
        "  }",
        "  @keyframes blink { 0%,50% { opacity: 1 } 50.01%,100% { opacity: 0 } }",
        "</style>",
        f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="#30363d"/>',
        '<circle cx="22" cy="24" r="5" fill="#ff5f57"/>'
        '<circle cx="40" cy="24" r="5" fill="#febc2e"/>'
        '<circle cx="58" cy="24" r="5" fill="#28c840"/>',
        f'<text class="m prompt" x="80" y="29">{esc(prompt)}</text>',
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="#21262d"/>',
    ]

    for i, (name, tag, head, meta, dot) in enumerate(slides):
        # negative delay starts each slide pre-advanced, so one keyframe rule
        # drives every slide; slide 0 also carries a static opacity so a
        # renderer that ignores animation shows frame 1 instead of a blank card
        fb = ";opacity:1" if i == 0 else ""
        p += [
            f'<g class="slide" style="animation-delay:{-i*DUR:.3f}s{fb}">',
            f'  <circle cx="{PAD}" cy="86" r="6" fill="{dot}"/>',
            f'  <text class="m repo" x="{PAD+16}" y="92">{esc(name)}'
            f'<tspan class="tag" dx="10">{esc(tag)}</tspan></text>',
            f'  <text class="m head" x="{PAD}" y="146">{esc(head)}</text>',
            f'  <text class="m meta" x="{PAD}" y="180">{esc(meta)}</text>',
            "</g>",
        ]

    for i in range(n):
        x = PAD + i * (tick_w + 8)
        fb = ";opacity:1" if i == 0 else ""
        p.append(f'<rect class="tick" x="{x:.1f}" y="222" width="{tick_w:.1f}" height="4" rx="2"/>')
        p.append(
            f'<rect class="tick-on" x="{x:.1f}" y="222" width="{tick_w:.1f}" height="4" rx="2" '
            f'style="animation-delay:{-i*DUR:.3f}s{fb}"/>'
        )

    p += [
        f'<rect class="cursor" x="{PAD}" y="244" width="8" height="4" rx="2"/>',
        f'<text class="m meta" x="{W-16}" y="250" text-anchor="end">{esc(footer)}</text>',
        "</svg>",
    ]
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(p) + "\n")
    print(f"{out}: {n} slides, {total:.1f}s loop, {H}px tall")
    return True


COMMITS = [
    ("google-deepmind/mujoco", "#3396", "1,281x less constraint-solver memory",
     "C/C++ - dense adjacency and flood fill replaced by a disjoint-set forest", "#f34b7d"),
    ("google-deepmind/mujoco_warp", "#1541", "1.513x faster GPU island discovery",
     "Python, Warp - 2,048 worlds, 247,308 rows, 99% CI [1.406x, 1.584x]", "#3572A5"),
    ("google-deepmind/mujoco", "#3450", "3V/8 fewer convex-hull probes",
     "C++ - second quadratic scan removed, mesh checksums byte-identical", "#f34b7d"),
    ("openxla/xla", "#46539", "Deterministic GPU reduction grouping",
     "C++ - insertion-ordered set kills hash-order drift, landed as 3d5df1d", "#f34b7d"),
    ("tensorflow/tensorflow", "#124410", "Reproducible collective-op ordering",
     "C++ - exact bit-matrix closure, graph is a function of the model alone", "#f34b7d"),
    ("google/XNNPACK", "#10801", "32 MiB lower inference workspace",
     "C - planner reuses the arena gap, 6.4% off MobileNet V1 peak", "#555555"),
    ("google/highway", "#3244", "65x cheaper perfect-hash builds",
     "C++ SIMD - 894M pairwise compares down to 13.6M, same duplicates", "#f34b7d"),
    ("triton-lang/kernels", "#22", "3.48x faster long-context attention",
     "Triton - skips 81% of blocks at 4K, within 1e-3 of the dense result", "#89e051"),
    ("NVIDIA/NeMo-Relay", "#481", "Prompt-cache agreement 0.48 to 1.00",
     "Rust - governor re-keyed on the scaffold, not the first user message", "#dea584"),
    ("NVIDIA/topograph", "#432", "Least-privilege RBAC, ClusterRole gone",
     "Helm, Kubernetes - rules gated on engine and provider, 141/141 tests", "#0f1689"),
    ("facebook/pyrefly", "#4180", "Type-checker crash pinned down",
     "Rust - 208 chained components, shipped in 1.2.0 via 3e90baa", "#dea584"),
]

SYSTEMS = [
    ("topological-ml-toolkit", "systems", "Point clouds to persistence diagrams",
     "Rust, Python, C++/AVX-512, CUDA - checked against ripser and GUDHI", "#dea584"),
    ("Epsilon-Hollow", "systems", "How much kernel fits in safe Rust",
     "Rust, x86-64 asm, QEMU/UEFI, Lean 4 - SMP, paging, VFS, Miri-verified", "#dea584"),
    ("caustic", "systems", "Hallucination detection without labels",
     "Python, PyTorch - orbit collapse to a certified bound, 0.995 AUROC", "#3572A5"),
    ("Aether-Lang", "research", "Persistent homology as a primitive",
     "Rust, Lean 4 - no_std, 229 tests, 52 surviving mutants, six claims killed", "#dea584"),
    ("faraday", "research", "3D dielectric electromagnetic solver",
     "Python - Banach fixed point at 1.755e-16 after a 50,000-epoch burn", "#3572A5"),
    ("sigmoid", "research", "Trained model to world model, no retraining",
     "Python - Banach certificate when norm(T) < 1, sheaf-consistency gate", "#3572A5"),
    ("OpenCLAW-P2P v7.0", "arXiv", "Decentralized peer review for AI research",
     "Co-author, arXiv:2604.19792 - resilient persistence, live verification", "#8b949e"),
]

if __name__ == "__main__":
    ok = card(
        "commits.svg",
        "Eleven upstream contributions merged into production ML infrastructure in 2026",
        "upstream $ git log --author=teerthsharma --merged --year=2026",
        "11 merged - DeepMind, Google, OpenAI, NVIDIA, Meta",
        COMMITS,
    )
    ok &= card(
        "systems.svg",
        "Selected systems and topology research projects",
        "lab $ ls -1 systems/ research/ --explain",
        "7 projects - systems and topology research",
        SYSTEMS,
    )
    sys.exit(0 if ok else 1)
