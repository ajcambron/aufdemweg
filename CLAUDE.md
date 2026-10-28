# Claude Code Configuration: Auf dem Weg

German Sunday School at DSB Hall, 2026–27: high schoolers, one mixed class (A1 to near C1), 120 minutes a week, 26 packet weeks. The site is the instructor's (or a parent sub's) refresher: one page per week.

## Read first
- `_planning/program-instructions.md`: the nine-module packet model, tiering rules and full 26-week scope and sequence. Source of truth for what each week covers.
- `_planning/lesson-frameworks.md`: how to fill the modules (gazebo task, structured input/output, the three grammar-problem variants, checklist). Use the `making-communicative-language-teaching-happen` skill when designing a week's Kernaufgabe or structured input.
- `_planning/weeks-1-5-build-log.md`: decisions already made for Weeks 1–5 (Sentence Builders format, match-up numbering convention, partial answer keys, Week 5 seeds Week 9).
- `_planning/weeks-6-26-build-log.md`: the data-file pipeline for Weeks 6–26, its validation rules, AP German alignment and content decisions. Use the `ap-german-language-and-culture` skill alongside the Lee & VanPatten one when changing a week.

## Week pages
- One page per week at `wochen/woche-NN.md`. Sections in order: Auf einen Blick, Ablauf, Grammatik, Wortschatz, Arbeitsblatt, Lösungen.
- Weeks 1–5 are hand-written pages. Weeks 6–26 are stubs (`layout: week`, `data: woche-NN`) rendered from `_data/weeks/woche-NN.yml`; edit the data file, never the generated packet HTML. New week: copy `_data/weeks/woche-06.yml`, then run `scripts/new-week-page.sh NN`.
- The page is instructor-facing. Grammatik is written for an adult with some German: the slice, an Achtung (`{: .warning }`) callout with the predictable student mistake and what to say, and one-line answers to likely B2 questions outside the slice.
- `_includes/week-plan.html` renders the module table from `modules:` front matter (minutes and core/optional are fixed). Skip order is always: energizer, buffer, Landeskunde; never the Kernaufgabe.
- Answer keys go inside `<details class="answer-key" markdown="1">`.
- When a week page is added, its `_data/calendar.yml` row needs `page:` so the home-page calendar links it (`scripts/new-week-page.sh` does this).

## Student packets (worksheets)
- Shown on the week page with `{% include worksheet.html file=page.packet title="..." %}`: preview thumbnail + PDF download, same as digcom. No Schoology embeds, no slide decks.
- Weeks 1–5: source is the original Word file in `worksheet-sources/docx/`; PDFs were exported with LibreOffice and split per week. Don't regenerate their content.
- Weeks 6+: `python3 scripts/build-packet.py NN` (validates the data file and writes `worksheet-sources/woche-NN-packet.html`), then `node scripts/render-worksheets.js woche-NN-packet` to produce `assets/worksheets/woche-NN-packet.pdf` and `-preview.png`. US Letter.
- Never print copyrighted song lyrics or texts in a packet; use public-domain or original material and label invented data as Beispieldaten.
- Word banks for fill-in-the-blank items are alphabetized and placed once, before the questions they serve.

## Site
- Jekyll + Just the Docs 0.12 (via `github-pages`), deployed on Cloudflare Pages (`cloudflare.yml`), domain in `CNAME`.
- Local build: `bundle exec jekyll serve` (if `bundle exec jekyll` isn't found, run the gem's `exe/jekyll` through `bundle exec ruby`).
- Palette in `_sass/custom/setup.scss` matches digcom; keep that file plain ASCII. German text in Markdown and HTML is fine as UTF-8.
- Fonts are self-hosted (`assets/fonts/`, Latin subset covers ä ö ü ß) via `assets/css/site-fonts.css`, shared by the site and the worksheet PDFs.
