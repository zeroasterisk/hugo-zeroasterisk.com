# zeroasterisk.com

> **Personal hobby project** by [Alan Blount](https://github.com/zeroasterisk). Not affiliated with, endorsed by, or supported by any employer. No warranty.

Source for [zeroasterisk.com](https://zeroasterisk.com). Built with Hugo, deployed to GitHub Pages.

## Layout

```
content/
├── posts/      # technical posts and cross-posts
├── personal/   # personal posts
└── pages/      # about
themes/minimal-tech/
```

## Develop

```bash
# Hugo extended v0.121.1
hugo server
```

## Deploy

Push to `master`. GitHub Actions does a clean build (`rm -rf public && hugo --gc --minify`), deploys to Pages, then verifies the live site. Build output is never committed.

Cross-post conventions: [CROSSPOST_PATTERN.md](CROSSPOST_PATTERN.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
