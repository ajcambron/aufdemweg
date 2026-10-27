# Weeks 1–5 — Build Log

> **Site note (2026-10-27):** the two .docx files now live in `worksheet-sources/docx/`. Each week's packet PDF was exported from the student docx with LibreOffice and split per week into `assets/worksheets/woche-NN-packet.pdf`. The docx stays the source for Weeks 1–5 until they are ported.

> Exported verbatim from the claude.ai Project "German Teacher" (`claude/Weeks 1-5 Build Log.md`) on 2026-10-27.

Built and delivered (2026-09-22): **Student Packet, Weeks 1–5.docx** and **Instructor Guide, Weeks 1–5.docx**, following the process and packet model in "Program Instructions.md" (see `program-instructions.md` in this export).

**These two .docx files are not included in this export.** They were delivered directly to the user in the session that built them, not saved into the claude.ai Project, and are not in this repo. If you need their actual content to migrate into the Hugo site, ask the user for the files.

## Sources used
- **Begegnungen Deutsch als Fremdsprache A2+** (user-uploaded PDF) — used as "food for thought" per the user's request: Kapitel 1 Teil A "Sich vorstellen" informed Week 1–2's self-introduction content and register (du/Sie); Kapitel 7 "Wohnen" (floor-plan comparison task, childhood-home narrative texts) informed Week 4's Landeskunde and B1/B2 extension. Not used for Weeks 3 or 5 — Begegnungen has no dedicated family or harvest-season chapter.
- **German Sentence Builders** (Conti, Viñales & Weidner — The Language Gym, EPI/lexicogrammar approach) — used as the format and density template per the user's instruction ("6 pages of Sentence Builders is perfect for a Saturday School Class"). Its exact page architecture was reused: a sentence-builder substitution table, then a boxed "Vocabulary Building" page (6 lettered exercises: complete-the-word, match-up, translate, missing-letter, broken-words, complete-with-suitable-word), then a "Narrow Reading" page (parallel short first-person texts at two levels + referential/affective comprehension questions), matching Lee & VanPatten's structured-input sequencing. Unit 5 (family) and Unit 17 (house) were followed most closely since they're directly on-theme for Weeks 3 and 4.

## Packet structure per week (matches Program Instructions' 2.5-hour model)
Title/can-do block → Sentence Builder → Vocabulary Building (6 boxes) → Narrow Reading (A1/A2 + B1/B2 texts, comprehension) → Kernaufgabe/core info-exchange task ("gazebo") → Structured Output (A1/A2 frames, B1/B2 open) → Landeskunde → Exit ticket → Energizer → B1/B2 Extension → Buffer. Runs ~5–6 dense pages per week (25 pages total for Weeks 1–5, title page included).

## Content decisions worth knowing about for later weeks
- Grammar is introduced as a slice per week (e.g., ordinal dates in Week 2, mein/meinen in Week 3, a locative-preposition chunk set in Week 4), not full paradigms — per the CLT skill's guidance that grammar needs are usually a slice, not a full paradigm.
- Week 5 (Erntedank) deliberately seeds vocabulary and the Erntedank/Thanksgiving comparison that Week 9 ("Dankbarkeit & Traditionen") pays off later in the scope-and-sequence — flagged in both the student packet's Landeskunde note and nowhere else; worth remembering when Week 9 gets built so it doesn't re-teach Erntedank from scratch.
- The "Match up" vocab-building exercise numbers the German column (1–n) and letters the English column (a–n) as two independently-ordered lists — this was a deliberate fix after an early draft's answer key mismatched them; if you extend the same box type to later weeks, keep the numbering/lettering convention (don't render pairs on the same table row, which visually implies they're already matched).
- Instructor guide's answer key is intentionally partial (Exercise 1 fill-ins + Exercise 2 match-up only) to keep it to one page per week; translation/broken-words/open items are marked as self-checking against the English gloss already printed in the student packet.

## Not yet built
Weeks 6–26 per the scope-and-sequence in "Program Instructions.md" (`program-instructions.md` in this export). The scripts (`weeks.js` data + `build-student.js` + `build-instructor.js`) that generated these two docx files were session-local (not saved to the project) — a future session rebuilding or extending this will need to recreate the generation approach, though the two delivered docx files are the durable record of Weeks 1–5's actual content.
