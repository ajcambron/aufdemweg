#!/usr/bin/env python3
"""Builds a week's student packet HTML from its data file.

Reads _data/weeks/woche-NN.yml (the same file the week page renders from)
and writes worksheet-sources/woche-NN-packet.html in the packet's module
order. Render the PDF afterwards with:

    node scripts/render-worksheets.js woche-NN-packet

Usage:
    python3 scripts/build-packet.py 06 07 08 ...
"""
import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LETTERS = "abcdefghijklmnop"


def esc(text):
    """Escape text, then allow **bold** and *italic* inline marks."""
    out = html.escape(str(text), quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*(.+?)\*", r"<em>\1</em>", out)
    # a free-standing ___ is a fill-in line; underscores inside a word are puzzle gaps
    out = re.sub(r"(?<![A-Za-zÄÖÜäöüß_])_{3,}(?![A-Za-zÄÖÜäöüß_])", '<span class="blank"></span>', out)
    return out


def paras(text):
    return "".join(f"<p>{esc(p.strip())}</p>" for p in str(text).strip().split("\n\n") if p.strip())


def missing_letter(word):
    """Blank one inner letter, the way the Sentence Builders packets do."""
    letters = [i for i, c in enumerate(word) if c.isalpha()]
    inner = letters[1:-1] or letters
    i = inner[len(inner) // 2]
    return word[:i] + "_" + word[i + 1:]


def broken(sentence):
    """Keep first (and last) letter of each word; {braces} keep a word whole."""
    def brk(m):
        word = m.group(0)
        if word.startswith("{"):
            return word[1:-1]
        if len(word) <= 3:
            return word[0] + "_" * (len(word) - 1)
        return word[0] + "_" * (len(word) - 2) + word[-1]
    return re.sub(r"\{[^}]+\}|[A-Za-zÄÖÜäöüß]+", brk, sentence)


def keep(inner):
    return f'<div class="keep">{inner}</div>'


def band(title):
    return f'<div class="band">{esc(title)}</div>'


def box(title, body, full=False):
    cls = "box full" if full else "box"
    return f'<div class="{cls}"><div class="box-title">{esc(title)}</div>{body}</div>'


def ol(items, start_letter=True):
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<ol class="{"alpha" if start_letter else "num"}">{lis}</ol>'


def table(rows, head=None, cls="ws-table"):
    out = f'<table class="{cls}">'
    if head:
        out += "<tr>" + "".join(f"<th>{esc(h)}</th>" for h in head) + "</tr>"
    for row in rows:
        out += "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>"
    return out + "</table>"


def build(nn):
    d = yaml.safe_load((ROOT / "_data" / "weeks" / f"woche-{nn}.yml").read_text())
    w = d["week"]
    parts = []

    # ---------- title + can-do ----------
    parts.append(f'''<div class="ws-header">
 <h1 class="ws-title ws-title-sm">Woche {w} | {esc(d["theme"])}</h1>
 <div class="ws-fields-inline"><div class="ws-field-inline"><span class="ws-field-label-inline">Name</span><span class="field-blank"></span></div></div>
</div>''')
    parts.append(f'<p class="ws-date">{esc(d["date_label"])}</p>')
    parts.append(table([[f'**Können-Sie...? (A1/A2)** {d["cando"]["a1"]}',
                         f'**Können-Sie...? (B1/B2)** {d["cando"]["b1b2"]}']], cls="ws-table cando"))
    parts.append(f'<p class="ws-directions">Grammatik-Fokus: {esc(d["grammar_focus"])}</p>')

    # ---------- sentence builder ----------
    for b in d["builder"]:
        parts.append(band(f'Sentence Builder: {b["title"]}'))
        parts.append(table([[f"**{de}**", f"*{en}*"] for de, en in b["rows"]], cls="ws-table builder"))

    # ---------- Vokabelaufbau ----------
    v = d["vocab"]
    parts.append(band("Vokabelaufbau: Vocabulary Building"))
    complete = [f"{de} [{en}]" for de, en, _ in v["complete"]]
    order = v["match_order"]
    match = (
        '<p class="ws-directions">Match the German (1–6) to its English meaning (a–f).</p>'
        '<div class="match"><ol class="num">'
        + "".join(f"<li>{esc(de)}</li>" for de, _ in v["match"])
        + '</ol><ol class="alpha">'
        + "".join(f"<li>{esc(v['match'][i - 1][1])}</li>" for i in order)
        + "</ol></div>"
    )
    parts.append('<div class="box-grid">'
                 + box("1. Complete with the missing word", ol(complete))
                 + box("2. Match up", match)
                 + box("3. Translate into English", ol([de for de, _ in v["translate"]]))
                 + box("4. Add the missing letter", '<div class="cols2">' + ol([missing_letter(x) for x in v["letters"]]) + "</div>")
                 + box("5. Broken words", ol([f"{broken(de)} = [{en}]" for de, en in v["broken"]]))
                 + box("6. Complete with a suitable word", ol(v["suitable"]))
                 + "</div>")

    # ---------- Lesen + structured input ----------
    r = d["reading"]
    for lvl, label, qlabel in (("a1", "A1/A2", "Answer the questions"), ("b1", "B1/B2", "Beantworte die Fragen auf Deutsch")):
        texts = r[lvl]["texts"]
        head = band("Lesen: Narrow Reading") if lvl == "a1" else ""
        parts.append(keep(head + f'<p class="level">{label}</p>'
                          + '<div class="box-grid">' + "".join(box(name, paras(text)) for name, text in texts) + "</div>"))
        parts.append(box(f"{qlabel}", ol([q for q, _ in r[lvl]["questions"]]), full=True))

    si = d["structured_input"]
    si_head = band("Achte auf die Form: Focus on Form")
    ref_opts = si["ref"].get("options", [])
    ref_items = "".join(
        f'<li>{esc(item[0])} <span class="choices">{"".join(f"<span>{esc(o)}</span>" for o in (item[2] if len(item) > 2 else ref_opts))}</span></li>'
        for item in si["ref"]["items"])
    aff_opts = si["aff"]["options"]
    aff_items = "".join(
        f'<li>{esc(s)} <span class="choices">{"".join(f"<span>{esc(o)}</span>" for o in aff_opts)}</span></li>'
        for s in si["aff"]["items"])
    parts.append(keep(si_head + f'<p class="ws-directions">A. {esc(si["ref"]["directions"])}</p><ol class="ws-items si">{ref_items}</ol>'))
    parts.append(keep(f'<p class="ws-directions">B. {esc(si["aff"]["directions"])}</p><ol class="ws-items si">{aff_items}</ol>'))

    # ---------- Kernaufgabe ----------
    t = d["task"]
    parts.append(band(f'Kernaufgabe: {t["title"]}'))
    parts.append(f'<p class="format">{esc(t["format"])} (30 min)</p>')
    parts.append(paras(t["directions"]))
    parts.append(f'<div class="ws-note"><strong>A1/A2:</strong> {esc(t["a1"])}<br><strong>B1/B2:</strong> {esc(t["b1"])}</div>')
    for tb in t.get("tables", []):
        title = f'<p class="level">{esc(tb["title"])}</p>' if tb.get("title") else ""
        rows = [list(row) for row in tb.get("rows", [])]
        rows += [[""] * len(tb["head"]) for _ in range(tb.get("blank", 0))]
        parts.append(keep(title + table(rows, head=tb["head"], cls="ws-table task")))
    if t.get("html"):
        parts.append(t["html"])

    # ---------- Structured output ----------
    o = d["output"]
    parts.append(band("Structured Output"))
    parts.append(box("A1/A2", f"<p>{esc(o['a1'])}</p>" + '<div class="lines">' + '<div class="line"></div>' * 4 + "</div>", full=True))
    parts.append(box("B1/B2", f"<p>{esc(o['b1'])}</p>" + '<div class="lines">' + '<div class="line"></div>' * 4 + "</div>", full=True))

    # ---------- Landeskunde, exit ticket ----------
    lk = d["landeskunde"]
    parts.append(band(f'Landeskunde: {lk["title"]}'))
    parts.append(paras(lk["text"]))
    parts.append(f'<div class="ws-note"><strong>Warum?</strong> {esc(lk["warum"])}<br><strong>Und bei uns?</strong> {esc(lk["vergleich"])}</div>')

    ex = d["exit"]
    parts.append(band("Können-Sie...? Exit Ticket"))
    parts.append(box("Selbstcheck", f'<p>A1/A2: {esc(ex["a1"])} <span class="choices"><span>Ja</span><span>Fast</span><span>Noch nicht</span></span></p>'
                     f'<p>B1/B2: {esc(ex["b1"])} <span class="choices"><span>Ja</span><span>Fast</span><span>Noch nicht</span></span></p>', full=True))

    # ---------- optional modules ----------
    en = d["energizer"]
    parts.append(band(f'Vokabelspiel / Energizer: {en["title"]}'))
    parts.append(paras(en["text"]))

    x = d["extension"]
    parts.append(band(f'B1/B2 Extension: {x["title"]}'))
    if x.get("intro"):
        parts.append(f'<p class="ws-directions">{esc(x["intro"])}</p>')
    parts.append(box("Text", paras(x["text"]), full=True))
    if x.get("table"):
        parts.append(table(x["table"]["rows"], head=x["table"]["head"], cls="ws-table task"))
    if x.get("questions"):
        parts.append(box("Fragen", ol([q for q, _ in x["questions"]]), full=True))
    if x.get("task"):
        parts.append(f'<div class="ws-note"><strong>Aufgabe:</strong> {esc(x["task"])}</div>')

    parts.append(band("Buffer: Instructor's choice"))
    parts.append(paras(d["buffer"]))

    parts.append(f'<div class="ws-footer">Woche {w} &middot; {esc(d["theme"])} &middot; Auf dem Weg &middot; aufdemweg.cambron.cc</div>')

    # keep every section band on the same page as the block after it
    merged = []
    for part in parts:
        if merged and merged[-1].startswith('<div class="band">'):
            merged[-1] = keep(merged[-1] + part)
        else:
            merged.append(part)
    parts = merged

    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="worksheet.css">
</head>
<body>
<!-- Generated by scripts/build-packet.py from _data/weeks/woche-{nn}.yml. Edit the data file, not this one. -->
<div class="page packet">
{chr(10).join(parts)}
</div>
</body>
</html>
'''
    out = ROOT / "worksheet-sources" / f"woche-{nn}-packet.html"
    out.write_text(page)
    print(f"Built {out.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        build(arg.zfill(2))
