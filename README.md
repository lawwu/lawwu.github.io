# Lawrence Wu's Quarto Blog

- My blog built using [Quarto](https://quarto.org/) which I had heard about after following [nbdev](https://github.com/fastai/nbdev), [which now uses Quarto](https://www.fast.ai/posts/2022-07-28-nbdev2.html).
- I used Albert Rapp's [guide to starting a Quarto blog](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html#interact-with-your-audience) which was very helpful
- The Quarto documentation on "Creating a Website" was also helpful: <https://quarto.org/docs/websites/>

## Deployment Process

I used to run `quarto render` and commit the rendered files. Now, this blog is automatically deployed using GitHub Actions whenever changes are pushed to the main branch. Here's how it works:

1. The workflow is defined in [.github/workflows/publish.yml](.github/workflows/publish.yml)
2. When changes are pushed to `main`, GitHub Actions:
   - Checks out the repository
   - Sets up UV (fast Python package installer)
   - Sets up Python using the version specified in `.python-version`
   - Installs Jupyter and other dependencies (required for Quarto pages that contain code)
   - Sets up Quarto
   - Renders the Quarto documents and publishes to the `gh-pages` branch

The rendered site is then served via GitHub Pages from the `gh-pages` branch.

### Manual Deployment

To manually trigger deployment:

1. Go to the "Actions" tab in the repository
2. Select the "Quarto Publish" workflow
3. Click "Run workflow" and select the branch to deploy from

### Local Preview

To preview the blog locally, run:

```bash
quarto preview
```

Notes for me:

To shrink all png files in a directory, use the following command:

```bash
brew install pngquant
for file in *.png; do pngquant --force --output "$file" --quality 60-80 "$file"; done
```

It's possible to embed Streamlit apps directly into a Quarto page using an iframe:

```html
<iframe
  src="https://llm-impact-on-jobs.streamlit.app/?embed=true"
  height="1200"
  style="width:100%;border:none;"
></iframe>
```
