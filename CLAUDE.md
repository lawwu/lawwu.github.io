# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Lawrence Wu's personal website/blog built with [Quarto](https://quarto.org/). It's a static site generator that combines Markdown with executable code blocks, similar to Jupyter notebooks.

**Site URL:** https://lawwu.github.io/blog.html
**Content:** 49+ blog posts, 10+ conference summaries, AI resources, and project pages

## Key Commands

### Local Development
```bash
quarto preview          # Start local development server with live reload
quarto render          # Build the site locally (outputs to docs/ directory)
make render            # Alternative way to render using Makefile
```

### Deployment
The site uses automated GitHub Actions deployment:
- **Automatic:** Pushes to `main` branch trigger deployment
- **Manual:** Go to Actions tab → "Quarto Publish" workflow → "Run workflow"
- **Output:** Site is published to `gh-pages` branch and served via GitHub Pages
- **Build time:** ~2-5 minutes (cached builds are faster)

### Python Environment
```bash
# Install dependencies using uv (recommended)
uv sync                # Install all dependencies from uv.lock

# Traditional method (fallback)
pip install -e .       # Install from pyproject.toml
```

## Architecture

### Directory Structure
```
lawwu.github.io/
├── posts/                  # 49+ blog posts (YYYY-MM-DD-slug/index.qmd)
├── conferences/            # 10+ conference summaries (same structure)
├── images/                 # Static assets (lawrence.jpg, etc.)
├── js/                     # JavaScript files
│   └── github-stars.js    # GitHub star count widget
├── docs/                   # Rendered HTML output (auto-generated, git-ignored)
├── _freeze/                # Quarto's computational cache (auto-generated)
├── .github/workflows/      # GitHub Actions automation
│   ├── publish.yml        # Production deployment
│   └── claude-code.yml    # Claude Code integration
├── _quarto.yml            # Main site configuration
├── posts/_metadata.yml    # Default post settings
├── pyproject.toml         # Python dependencies
├── uv.lock                # Locked dependencies (217KB)
├── .python-version        # Python 3.13.9
├── Makefile               # Build shortcuts
└── styles.css             # Custom CSS overrides
```

### Configuration Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Main site config: project type, output dir (`docs/`), theme (Cosmo), navbar navigation, Google Analytics, social media tags, JavaScript injections |
| `posts/_metadata.yml` | Default blog post settings: freeze (disabled), author, TOC, Utterances comments, page layout |
| `pyproject.toml` | Python project metadata: Python >=3.12, dependencies (jupyter, pandas, plotly) |
| `.python-version` | Specifies Python 3.13.9 for reproducible builds |
| `uv.lock` | Locked dependency versions (217KB) - ensures reproducible builds |
| `Makefile` | Simple build task: `make render` → `quarto render` |
| `styles.css` | Custom CSS for GitHub stars widget and other styling |
| `.gitignore` | Excludes `.quarto/`, `_site/`, `.DS_Store` |

### Content Pages

**Main Pages:**
- `index.qmd` - Homepage with bio, professional experience, newsletter subscription
- `blog.qmd` - Blog listing with sorting/filtering
- `projects.qmd` - Static project links page
- `conferences.qmd` - Conference summaries listing
- `ai_resources.qmd` - Curated AI resources (newsletters, blogs, YouTube, podcasts, Twitter)

**Blog Posts:**
- Location: `posts/YYYY-MM-DD-slug/index.qmd`
- Each post in its own directory
- Frontmatter example:
  ```yaml
  ---
  title: "Post Title"
  author: "Lawrence Wu"
  date: '2025-01-01'
  categories: [AI, Machine Learning, Career]
  image: "preview.png"  # Optional
  ---
  ```

**Conference Content:**
- Location: `conferences/YYYY-MM-DD-name/index.qmd`
- Same structure as blog posts
- Indexed separately on `conferences.qmd`

### Content Format
- **File type:** `.qmd` (Quarto Markdown) files
- **Executable code:** Python/R code blocks run during rendering (requires Jupyter)
- **Frontmatter:** YAML metadata (title, date, author, categories, etc.)
- **Comments:** Utterances (GitHub issues-based) - stored in `lawwu/blog_comments` repo
- **Features:** Embedded videos, Streamlit app iframes, code execution, image lazy loading

### Theme and Styling
- **Theme:** Cosmo Bootstrap theme
- **Custom CSS:** `styles.css` for additional styling
- **Responsive:** Mobile-friendly navbar navigation
- **Social media:** Twitter cards (@law_wu), Open Graph tags
- **Analytics:** Google Analytics (G-LN4GM4FVCJ)
- **Consent:** Cookie consent banner enabled

### JavaScript Integrations
- **GitHub stars widget** (`js/github-stars.js`) - Displays dynamic star counts
- **Blue Letter Bible** - Adds Bible verse tooltips/links (ESV translation)
- **Custom scripts** - Injected via `_quarto.yml` header configuration

## Development Workflows

### Adding New Blog Posts
1. Create new directory: `posts/YYYY-MM-DD-slug/`
2. Add `index.qmd` file with YAML frontmatter:
   ```yaml
   ---
   title: "Your Post Title"
   author: "Lawrence Wu"
   date: '2025-01-01'
   categories: [Category1, Category2]
   ---
   ```
3. Write content using Quarto Markdown
4. Include images/assets in the same directory
5. Quarto automatically includes in blog listing
6. Preview locally with `quarto preview`

### Adding Conference Summaries
Same process as blog posts, but use `conferences/` directory instead

### Working with Executable Code
- **Python code blocks** execute during rendering (requires Jupyter)
- **Freeze control:** Use `freeze: false` in frontmatter to re-execute on each render
- **Cache location:** Results cached in `_freeze/` directory
- **Dependencies:** Ensure packages listed in `pyproject.toml`

Example code block:
````markdown
```{python}
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df.head()
```
````

### Image Optimization
Compress PNG files before committing:
```bash
brew install pngquant
for file in *.png; do pngquant --force --output "$file" --quality 60-80 "$file"; done
```

### Content Guidelines
- **Categories:** Use existing categories when possible (AI, Career, Data Science, etc.)
- **Images:** Place in post directory, reference with relative paths
- **Code:** Prefer executable code blocks for reproducibility
- **Links:** Use markdown link syntax `[text](url)`
- **Videos:** Use Quarto's video shortcode for embeds

## Build & Deployment

### GitHub Actions Workflows

**1. Production Deployment (`publish.yml`)**
- **Triggers:** Push to `main` branch OR manual workflow dispatch
- **Steps:**
  1. Checkout repository
  2. Install `uv` (fast Python package manager)
  3. Set up Python 3.13.9 (from `.python-version`)
  4. Run `uv sync` to install dependencies
  5. Cache `_freeze/` directory for faster builds
  6. Configure git credentials
  7. Render Quarto site
  8. Publish to `gh-pages` branch
- **Output:** `docs/` directory
- **URL:** https://lawwu.github.io/blog.html

**2. Claude Code Integration (`claude-code.yml`)**
- **Triggers:** `@claude` mention in comments, PRs, or issues
- **Permissions:** contents write, PR/issue management, CI integration
- **Purpose:** Enables Claude Code to interact with repository

### Dependency Management
- **Package manager:** `uv` (astral-sh/setup-uv) - fast, reliable Python package installer
- **Lock file:** `uv.lock` (217KB) ensures reproducible builds
- **Dependencies:**
  ```toml
  [project]
  requires-python = ">=3.12"
  dependencies = [
      "jupyter>=1.0.0",
      "pandas>=2.1.0",
      "plotly>=5.18.0",
  ]
  ```
- **Python version:** 3.13.9 (specified in `.python-version`)

### Freeze & Caching Strategy
- **`_freeze/` directory:** Caches computational results for performance
- **GitHub Actions:** Includes caching for faster rebuilds
- **Per-file control:** Posts can override with `freeze: true/false` in metadata
- **When to freeze:**
  - `freeze: true` - Cache results, don't re-execute (default)
  - `freeze: false` - Re-execute code on each render

## External Integrations

### Comments System
- **Platform:** [Utterances](https://utteranc.es/)
- **Storage:** Comments stored as GitHub issues in `lawwu/blog_comments` repo
- **Configuration:** Set in `posts/_metadata.yml`

### Analytics & Social
- **Google Analytics:** `G-LN4GM4FVCJ`
- **Twitter:** Creator `@law_wu`, Twitter card support
- **Open Graph:** Meta tags for social sharing previews
- **RSS Feed:** Auto-generated `blog.xml`

### Newsletter
- **Platform:** Substack
- **Integration:** Subscription form on homepage

## Common Tasks

### Preview Changes Locally
```bash
quarto preview
# Opens browser at http://localhost:XXXX with live reload
```

### Build Entire Site
```bash
quarto render
# Output in docs/ directory
```

### Clear Cache and Rebuild
```bash
rm -rf _freeze/
quarto render
# Forces re-execution of all code blocks
```

### Update Dependencies
```bash
uv sync           # Install/update from uv.lock
uv lock           # Update uv.lock with latest compatible versions
```

### Check Site Locally
```bash
# After rendering, serve the docs/ directory
cd docs
python -m http.server 8000
# Visit http://localhost:8000
```

## Repository Statistics

- **Total content files:** 63+ Quarto/Jupyter files
- **Blog posts:** 49+ posts (2023-2025)
- **Conference summaries:** 10+ events
- **Repository size:** ~86MB (42MB git history)
- **Topics:** AI/ML, LLMs, data science, career, personal development

## Important Conventions

### File Naming
- **Posts:** `YYYY-MM-DD-descriptive-slug/index.qmd`
- **Images:** Place in same directory as post, use descriptive names
- **Case:** Use lowercase with hyphens for directory names

### Git Workflow
- **Main branch:** `main` - Production code only
- **Feature branches:** `feature/description` or `claude/description-xxxxx`
- **Commits:** Descriptive messages, commit rendered output (`docs/`)
- **Don't commit:** `.quarto/`, `_site/` (git-ignored)
- **Do commit:** `_freeze/`, `docs/` (needed for GitHub Pages)

### Code Style
- **Python:** Follow PEP 8, use type hints when helpful
- **Markdown:** Use ATX headers (`#`), not Setext (`===`)
- **YAML:** Use consistent indentation (2 spaces)

## Troubleshooting

### Build Failures
1. Check Python version: `python --version` (should be 3.13.9)
2. Verify dependencies: `uv sync`
3. Clear cache: `rm -rf _freeze/`
4. Check Quarto version: `quarto check`

### Code Execution Errors
1. Ensure Jupyter is installed: `uv sync`
2. Check if package is in `pyproject.toml`
3. Try `freeze: false` to re-execute code
4. Verify Python kernel: `jupyter kernelspec list`

### Preview Not Updating
1. Stop preview (Ctrl+C)
2. Clear cache: `rm -rf _freeze/`
3. Restart: `quarto preview`

### Deployment Issues
1. Check GitHub Actions logs in Actions tab
2. Verify `gh-pages` branch exists
3. Check GitHub Pages settings (Settings → Pages)
4. Ensure `docs/` directory is committed

## Resources

- **Quarto Documentation:** https://quarto.org/docs/
- **Quarto Blog Guide:** https://quarto.org/docs/websites/website-blog.html
- **GitHub Pages:** https://docs.github.com/en/pages
- **Utterances:** https://utteranc.es/
- **UV Package Manager:** https://github.com/astral-sh/uv