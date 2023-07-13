# Lawrence Wu's Personal Website

To shrink all png files in a directory, use the following command:

```bash
brew install pngquant
for file in *.png; do pngquant --force --output "$file" --quality 60-80 "$file"; done
```