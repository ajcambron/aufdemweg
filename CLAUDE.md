# Claude Code Configuration: Auf dem Weg

## Site
- Jekyll + Just the Docs (0.12, via the `github-pages` gem), deployed on Cloudflare Pages (`cloudflare.yml`), custom domain in `CNAME`.
- Build locally with `bundle exec jekyll serve` (see `.claude/launch.json`).
- Palette lives in `_sass/custom/setup.scss` and matches the digcom site. Keep that file plain ASCII: the legacy Ruby `sass` gem chokes on UTF-8 bytes.
- Fonts are self-hosted in `assets/fonts/` (Latin subset, which covers ä ö ü ß) and loaded through `assets/css/site-fonts.css`.

## Content
- German text on pages is fine as UTF-8 in Markdown; only the Sass files must stay ASCII.
- Use the configured callouts for recurring box types: `vocab` (Wortschatz), `grammar` (Grammatik), `culture` (Landeskunde), `note`, `important`, `warning`, `discussion`, `reflection`, `good`, `highlight`.
- Every page needs front matter with `title` and, for sections, `nav_order` / `parent` / `has_children` per Just the Docs.
- Word banks for fill-in-the-blank worksheets are alphabetized and placed once, before all questions.
