# Lesson Frameworks

How to design a week's content (Weeks 6–26, or a rebuild of 1–5) so it holds up against Lee & VanPatten, *Making Communicative Language Teaching Happen*. Read `program-instructions.md` first: the nine-module packet, the 120-minute class and the A1–B2 tiering are fixed there. This doc covers *how to fill* those modules, not what they are.

---

## 1. Start from the Kernaufgabe

Write the core task before anything else. It has to pass the **gazebo test**: when it's over, there's a product you can point at (a filled-in ID card, a family tree, a tally of survey results). "Practice the dative" fails. "Draw your partner's room from their description" passes.

Then derive everything from it:

| Ask | Goes into |
| :--- | :--- |
| What words does the task need? | Sentence builder + Wortschatz table on the week page |
| What grammar does it need? | Grammatik-Fokus: a **slice** (one gender, one case, two verb forms), never a full paradigm |
| What phrases does it need (ask, agree, compare)? | Kernaufgabe question bank |
| What does each level hand in? | Kernaufgabe directions (A1/A2 vs. B1/B2 line) |

The book's warning: a "daily routines" chapter teaches twenty reflexive verbs, and students describing their real routines use almost none. If the task doesn't need it, cut it; a later week can pick it up.

## 2. Input & structured input: make the form do work

This module is where the grammar slice gets acquired, so it can't just be comprehension questions about content. After the narrow reading, add **structured input** items: questions where the week's grammar form is the only way to get the answer.

- **Referential first (2–3 item types):** a right answer exists. *"Mein Bruder findet ihn nett / Meinen Bruder findet er nett: who likes whom?"*
- **Affective second:** no right answer. *"Stimmt für mich / Stimmt nicht."*
- **Students never write the target form here.** They choose, match, check, rank. Writing it comes in structured output.

**The nonsense-word test:** replace the content words with nonsense. If students can still complete the item, it's pattern-spotting, not processing. "Circle every *meinen*" fails. "Who is doing the liking?" passes.

**About Vokabelaufbau.** The six-box format from *German Sentence Builders* is a deliberate choice and stays. Know what it is, though: boxes 3–5 (translate, missing letter, broken words) are form drills, and they fail the nonsense-word test. They're fine for vocabulary recall. They don't replace the structured input items above, and they shouldn't grow at the expense of them.

## 3. Three grammar problems, three designs

Decide which one the week's slice is before writing any items.

### Variant 1: A word gives the meaning away (Lexical Preference)

**Applies to:** verb person endings, Perfekt (Week 19), *werden* future (Weeks 12, 24), plurals.

Learners read the meaning off a word and skip the ending. *Gestern* says "past," so *hat ... gespielt* never gets processed. **Rule:** strip time adverbs from tense items and subject pronouns from person-ending items. Blank the subject and let the ending answer *who* (*\_\_\_ spielst Fußball → ich / du / Max?*).

### Variant 2: The first noun gets read as the doer (First Noun Principle)

**Applies to:** accusative and dative (Weeks 3, 4, 13), verb-second with a fronted object, *weil/wenn/dass* verb-final, passive.

English speakers read *"Den Hund beißt der Mann"* as the dog biting. **Rule:** write object-first items where only the article tells you who acts, with picture or either/or choices. **Use masculine nouns only**: feminine, neuter and plural look the same in nominative and accusative, so those items are ambiguous and test nothing.

### Variant 3: The form barely changes the meaning (low communicative value)

**Applies to:** adjective endings (Week 15), gender agreement, most preposition-case pairs at A1.

*"Ein großer Hund"* and *"ein große Hund"* mean the same thing to a listener, so learners don't process the ending until comprehension is easy. **Rule:** keep it as exposure for A1/A2 (the program already says A1 skips agreement in Week 15); only B1/B2 get structured items, and those use cases where the ending *does* decide meaning. Don't grade it in A1 output.

## 4. Structured output: someone has to respond

Structured output needs three things: new information (not something the partner already knows), the one target form, and **a listener who responds to the content**: compares, signs, fills a chart, says *ich auch / ich nicht*. Without that last part it's a drill.

- A1/A2: sentence frames with the target form built in.
- B1/B2: an open prompt with a required form (*use at least two weil-clauses*), and the partner does something with the answer.

Structured output always follows structured input on the same form. Never reverse them.

## 5. The week page's Grammatik section

The week page is for the instructor or a parent sub, so it can be fuller than what students see. Every Grammatik section has:

1. The slice, stated in one or two sentences, with a small table if it helps.
2. A `{: .warning }` (Achtung) callout: **what students will do wrong**, and what to say. The default move is restating, not correcting: *"Ich habe fünfzehn" → "Ah, du bist fünfzehn!"*
3. Anything a B2 might ask that's outside the slice, with a one-line answer, so the sub isn't caught off guard.

Students themselves get about a minute of explanation, in context. The research the book cites found explanation alone produced no measurable gain; the structured input did the work.

## 6. Quizzes and checks

Test with the formats you taught with. A fill-in-the-blank conjugation quiz after input-based weeks tells students the input work didn't count. Build checks from structured input items (interpretation), structured output prompts (production) and class content (*whose family was biggest?*). Score speaking and writing on content first, then vocabulary, then the week's one form.

## 7. Checklist before a week ships

- [ ] Kernaufgabe passes the gazebo test and has separate A1/A2 and B1/B2 lines.
- [ ] Every sentence-builder row is used by the task.
- [ ] Grammatik-Fokus is a slice, and its variant (1, 2 or 3) is decided.
- [ ] Input module has referential then affective structured input items that pass the nonsense-word test, and none ask students to write the form.
- [ ] Structured output requires a partner to respond.
- [ ] Core modules alone (85 min) work without any optional module.
- [ ] Week page has the Achtung callout, Wortschatz table, packet card and answer key.
- [ ] `python3 scripts/build-packet.py NN` passes its checks (Weeks 6+).
