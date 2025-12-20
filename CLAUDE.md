# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is Lawrence Wu's personal website/blog built with [Quarto](https://quarto.org/). It's a static site generator that combines Markdown with executable code blocks, similar to Jupyter notebooks. The site includes blog posts, project pages, and conference notes.

## Key Commands

### Local Development
- `quarto preview` - Start local development server with live reload
- `quarto render` - Build the site locally (outputs to `docs/` directory)
- `make render` - Alternative way to render using Makefile

### Deployment
The site uses automated GitHub Actions deployment:
- Pushes to `main` branch automatically trigger deployment
- Manual deployment: Go to Actions tab → "Quarto Publish" workflow → "Run workflow"
- Site is published to `gh-pages` branch and served via GitHub Pages

## Architecture

### Directory Structure
- `posts/` - Blog posts, each in date-named subdirectories with `index.qmd` files
- `conferences/` - Conference notes and summaries  
- `docs/` - Rendered HTML output (auto-generated, don't edit directly)
- `_freeze/` - Quarto's computational cache (auto-generated)
- `images/` - Static images and assets
- `js/` - JavaScript files (e.g., GitHub stars widget)

### Configuration Files
- `_quarto.yml` - Main Quarto configuration (site structure, theme, navbar)
- `posts/_metadata.yml` - Default settings for all blog posts (author, TOC, comments)
- `.github/workflows/publish.yml` - GitHub Actions deployment workflow
- `.python-version` - Python version (3.12.9) for reproducible builds

### Content Format
- All content is written in `.qmd` (Quarto Markdown) files
- Supports executable Python/R code blocks that run during rendering
- Blog posts use YAML frontmatter for metadata (title, date, author, etc.)
- Comments powered by Utterances (GitHub issues-based)

### Theme and Styling
- Uses Cosmo Bootstrap theme
- Custom CSS in `styles.css`
- Responsive design with navbar navigation
- Social media integration (Twitter cards, Open Graph)

## Development Notes

### Adding New Posts
1. Create new directory in `posts/` with format `YYYY-MM-DD-slug/`
2. Add `index.qmd` file with proper YAML frontmatter
3. Include any images/assets in the same directory
4. Quarto will automatically include in blog listing

### Content with Code
- Python code blocks are executed during rendering (requires Jupyter)
- Use `freeze: false` in metadata to re-execute code on each render
- Computational results are cached in `_freeze/` directory

### Image Optimization
Use this command to compress PNG files:
```bash
brew install pngquant
for file in *.png; do pngquant --force --output "$file" --quality 60-80 "$file"; done
```