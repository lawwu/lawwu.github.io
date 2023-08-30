# Lawrence Wu's Quarto Blog

- My blog built using [Quarto](https://quarto.org/) which I had heard about after following [nbdev](https://github.com/fastai/nbdev), [which now uses Quarto](https://www.fast.ai/posts/2022-07-28-nbdev2.html).
- I used Albert Rapp's [guide to starting a Quarto blog](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html#interact-with-your-audience) which was very helpful
- The Quarto documentation on "Creating a Website" was also helpful: https://quarto.org/docs/websites/

Notes for me:

To shrink all png files in a directory, use the following command:

```bash
brew install pngquant
for file in *.png; do pngquant --force --output "$file" --quality 60-80 "$file"; done
```

It's possible to embed Streamlit apps directly into a Quarto page using an iframe:
```
<iframe
  src="https://llm-impact-on-jobs.streamlit.app/?embed=true"
  height="1200"
  style="width:100%;border:none;"
></iframe>
```