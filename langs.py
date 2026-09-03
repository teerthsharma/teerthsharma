#!/usr/bin/env python3
"""Render languages.svg from live GitHub API data.

Sums language bytes across every non-fork repository on the account and draws a
stacked bar plus legend, styled to match the ticker cards. Run by
.github/workflows/languages.yml on a weekly cron; safe to run by hand.

    GITHUB_TOKEN=$(gh auth token) python langs.py [user] [outfile]
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date

USER = sys.argv[1] if len(sys.argv) > 1 else "teerthsharma"
OUT = sys.argv[2] if len(sys.argv) > 2 else "languages.svg"
TOP = 8
MIN_PCT = 0.5          # anything smaller is legend noise; folded into "Other"

# github/linguist colours; anything unmapped falls back to grey
COLOURS = {
    "Rust": "#dea584", "Python": "#3572A5", "Lean": "#a0a2d2", "Shell": "#89e051",
    "WGSL": "#1a5e9a", "Jupyter Notebook": "#DA5B0B", "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a", "Cuda": "#3A4E3A", "Assembly": "#6E4C13",
    "CSS": "#663399", "HTML": "#e34c26", "C++": "#f34b7d", "C": "#555555",
    "Dockerfile": "#384d54", "Go": "#00ADD8", "Java": "#b07219", "Nix": "#7e7eff",
    "Makefile": "#427819", "CMake": "#DA3434", "Zig": "#ec915c", "Julia": "#a270ba",
}
OTHER = "#6e7681"


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "langs.py"},
    )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect(user):
    """Sum language bytes over non-fork repos. Returns (totals, repo_count)."""
    totals, repos, page = {}, 0, 1
    while True:
        batch = api(f"/users/{user}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        for repo in batch:
            if repo.get("fork") or repo.get("archived"):
                continue
            repos += 1
            for lang, size in api(f"/repos/{user}/{repo['name']}/languages").items():
                totals[lang] = totals.get(lang, 0) + size
        if len(batch) < 100:
            break
        page += 1
    return totals, repos


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(totals, repos):
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    grand = sum(v for _, v in ranked) or 1
    head = [kv for kv in ranked[:TOP] if 100.0 * kv[1] / grand >= MIN_PCT]
    rest = grand - sum(v for _, v in head)
    if rest:
        head.append(("Other", rest))

    W, BAR_X, BAR_W, BAR_Y, BAR_H = 840, 26, 788, 78, 24
    rows = (len(head) + 3) // 4                      # 4 legend columns
    H = BAR_Y + BAR_H + 26 + rows * 30 + 30

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="Language distribution across '
        f'{repos} source repositories, by bytes">',
        f"<title>Languages by bytes across {repos} source repositories</title>",
        "<style>",
        '  .m { font-family: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas,'
        ' "Liberation Mono", monospace }',
        "  .prompt { fill: #6e7681; font-size: 15px }",
        "  .name { fill: #e6edf3; font-size: 15px; font-weight: 600 }",
        "  .pct { fill: #8b949e; font-size: 15px }",
        "  .meta { fill: #6e7681; font-size: 13px }",
        "  .seg { animation: grow 1.1s cubic-bezier(.2,.8,.2,1) both }",
        "  @keyframes grow { from { transform: scaleX(0) } to { transform: scaleX(1) } }",
        "</style>",
        f'<rect width="{W}" height="{H}" rx="10" fill="#0d1117"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="#30363d"/>',
        '<circle cx="22" cy="24" r="5" fill="#ff5f57"/>'
        '<circle cx="40" cy="24" r="5" fill="#febc2e"/>'
        '<circle cx="58" cy="24" r="5" fill="#28c840"/>',
        f'<text class="m prompt" x="80" y="29">~ $ gh api /repos/{esc(USER)}/*/languages | sum</text>',
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="#21262d"/>',
        f'<clipPath id="bar"><rect x="{BAR_X}" y="{BAR_Y}" width="{BAR_W}" '
        f'height="{BAR_H}" rx="6"/></clipPath>',
        f'<g clip-path="url(#bar)">',
    ]

    x = float(BAR_X)
    for i, (lang, size) in enumerate(head):
        w = BAR_W * size / grand
        colour = OTHER if lang == "Other" else COLOURS.get(lang, OTHER)
        # transform-origin keeps each segment growing from its own left edge
        out.append(
            f'  <rect class="seg" x="{x:.2f}" y="{BAR_Y}" width="{max(w,1):.2f}" '
            f'height="{BAR_H}" fill="{colour}" '
            f'style="transform-origin:{x:.2f}px {BAR_Y}px;animation-delay:{i*0.07:.2f}s"/>'
        )
        x += w
    out.append("</g>")

    ly = BAR_Y + BAR_H + 46
    for i, (lang, size) in enumerate(head):
        col, row = i % 4, i // 4
        lx = BAR_X + col * 197
        colour = OTHER if lang == "Other" else COLOURS.get(lang, OTHER)
        pct = 100.0 * size / grand
        out.append(f'<circle cx="{lx+5}" cy="{ly+row*30-5}" r="5" fill="{colour}"/>')
        out.append(
            f'<text class="m" x="{lx+18}" y="{ly+row*30}">'
            f'<tspan class="name">{esc(lang)}</tspan>'
            f'<tspan class="pct" dx="8">{pct:.1f}%</tspan></text>'
        )

    mb = grand / 1_000_000
    out.append(
        f'<text class="m meta" x="{W-16}" y="{H-14}" text-anchor="end">'
        f"{repos} source repos - {mb:,.1f} MB - regenerated {date.today():%Y-%m-%d}</text>"
    )
    out.append(f'<text class="m meta" x="26" y="{H-14}">live from the GitHub API</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    try:
        totals, repos = collect(USER)
    except urllib.error.HTTPError as e:
        sys.exit(f"GitHub API {e.code}: {e.reason}")
    if not totals:
        sys.exit("no language data returned; refusing to write an empty card")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(totals, repos))
    print(f"{OUT}: {len(totals)} languages over {repos} repos, "
          f"{sum(totals.values()):,} bytes")
