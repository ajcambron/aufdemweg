# Weeks 6–26 Build Log

Built 2026-10-28 in Claude Code, after Weeks 1–5 (see `weeks-1-5-build-log.md`).

## Pipeline
- Each week is one data file: `_data/weeks/woche-NN.yml`. It drives both outputs, so the page and the packet can't drift:
  - the instructor page, rendered by `_layouts/week.html` (page stub: `wochen/woche-NN.md`, created by `scripts/new-week-page.sh`, which also links the calendar);
  - the student packet, built by `python3 scripts/build-packet.py NN` into `worksheet-sources/woche-NN-packet.html`, then `node scripts/render-worksheets.js woche-NN-packet` → `assets/worksheets/woche-NN-packet.pdf` + `-preview.png`.
- `build-packet.py` validates every file before building: six fill-ins, six match-ups, eight translations, eight missing-letter words, four broken-word sentences, six suitable-word frames; two texts and four questions per reading level; every structured-input answer must be one of its options; `match_order` must be a permutation of 1–6 with no pair left on its own row.
- Start a new week by copying `_data/weeks/woche-06.yml` (the reference file). Optional keys: `task.maps` (street-grid town map, Week 18), `task.intro_html` (raw HTML before the task tables, Week 25's cloze), `task.key` (answer key for the Kernaufgabe, shown under Lösungen), per-item options on structured-input items.
- Special days are hand-written pages: `wochen/weihnachtsfeier.md` (+ the one-page insert `worksheet-sources/weihnachtsfeier-insert.html`) and `wochen/abschlussfeier.md`.

## Packet format
Same order and density as the Weeks 1–5 Word packets (sentence builder → six-box Vokabelaufbau → narrow reading at two levels → Kernaufgabe → structured output → Landeskunde → exit ticket → energizer → B1/B2 extension → buffer), with one addition: an **Achte auf die Form** section after the readings with referential then affective structured-input items (Lee & VanPatten), designed against that week's processing trap (`lesson-frameworks.md`, Section 3). Packets run 6–7 pages in the site fonts; Weeks 1–5 stay in the Word layout.

## Content decisions
- **AP German alignment** (CED, Fall 2026): each week names its AP theme and mode on the page ("AP-Brücke"); every Landeskunde ends with a *Warum?* question (product/practice → perspective) and an *Und bei uns?* comparison; B1/B2 extensions rehearse AP task types: chart reading with German number formats (6, 8, 12, 15, 17), two-pass listening (13), formal-register email (7, 14, 18, 24), 40-second cultural comparison (9, 21), source-attributed argument (14, 18, 19), full three-source argumentative essay (20, 23), register switching (25).
- **Invented data is labeled** (Beispieldaten) wherever a chart or survey appears. Real facts used were checked: e.g., Germany's 25-cent Einwegpfand since 2003, Delaware repealed its bottle bill in 2010, Easter Sunday 2027 = March 28, Karnevalssonntag 2027 = February 7.
- **Copyright:** no modern song lyrics are printed. Week 25's cloze uses the public-domain folk song *Die Gedanken sind frei*; the page tells instructors to project licensed lyrics instead of printing them.
- **Calendar hooks:** Week 9 builds on Week 5's Erntedank seed; Week 10 falls on Nikolaustag; Week 11's skits are performed at the Weihnachtsfeier; Week 12 starts a Vorsatz wall revisited in Week 26; Week 16 falls on Karnevalssonntag; Week 17 on Valentinstag; Week 22 runs the week before Easter; Week 26 prepares the Abschlussfeier performances.
- **Sensitivity defaults:** invented families allowed (Week 3 precedent, Week 19 trips), symptom cards instead of real health questions (14), friendship rather than romance on Valentine's Day (17), any spring holiday allowed in Week 22's output.

## Weeks 1–5 migrated (2026-10-28)
Weeks 1–5 were moved from the Word packets into data files on the same pipeline. Their sentence builders, readings, tasks, energizers and extensions were kept; each gained an Achte-auf-die-Form section, Warum? / Und bei uns? culture prompts, an AP-Brücke and an AP-style extension task (40-second self-introduction in Week 1, class language survey in Week 2, spoken family comparison in Week 3, formal landlord email in Week 4, written Erntedank/Thanksgiving comparison in Week 5). Fixes made while migrating: Week 3's mislabeled "accusative" note under the sentence builder, Week 5's claim that *wenn* recycles earlier weeks, Week 4's dependence on instructor-supplied room pictures (room plans are now printed in the packet), and Week 4's structured output, which referred to an interview the task didn't include. "Saturday School" is gone; the program meets on Sundays. The original .docx packets remain in `worksheet-sources/docx/` as an archive.
