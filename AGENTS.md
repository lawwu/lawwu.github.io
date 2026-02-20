# AGENTS.md

Guidance for coding agents (Claude Code, Codex, etc.) working in this repository.

## Project

Lawrence Wu's personal blog at https://lawwu.github.io/blog.html, built with [Quarto](https://quarto.org/).

## Key Commands

```bash
quarto preview       # Local dev server with live reload
quarto render        # Build site → docs/
uv sync              # Install Python dependencies
```

Deployment: push to `main` → GitHub Actions renders and publishes to `gh-pages`.

## Structure

```text
posts/YYYY-MM-DD-slug/index.qmd    # Blog posts
conferences/YYYY-MM-DD-name/index.qmd  # Conference summaries
_quarto.yml                         # Main site config
posts/_metadata.yml                 # Default post settings
pyproject.toml / uv.lock            # Python deps (Python 3.13.9)
docs/                               # Rendered output (commit this)
_freeze/                            # Computational cache (commit this)
```

## Adding Content

Create `posts/YYYY-MM-DD-slug/index.qmd` with frontmatter:

```yaml
---
title: "Post Title"
author: "Lawrence Wu"
date: '2025-01-01'
categories: [AI, Machine Learning]
---
```

Use `.qmd` files (not `.md`) for all blog posts and conference summaries.

## Conventions

- **Branches:** `main` (production), `feature/description` or `claude/description-xxxxx`
- **Commit:** include `docs/` and `_freeze/`; exclude `.quarto/`, `_site/`
- **Images:** place in post directory, compress PNGs with `pngquant --quality 60-80`
- **Code blocks:** executable Python runs via Jupyter during render; use `freeze: false` to force re-execution

## Troubleshooting

- Build fails → `uv sync`, then `rm -rf _freeze/ && quarto render`
- Preview stale → restart `quarto preview`
- Deployment issues → check Actions tab logs
