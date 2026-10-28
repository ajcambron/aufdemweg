#!/usr/bin/env bash
# Creates wochen/woche-NN.md for a week whose data file exists, and links it
# from the home-page calendar. Usage: scripts/new-week-page.sh 07 08 ...
set -euo pipefail
cd "$(dirname "$0")/.."
for nn in "$@"; do
  nn=$(printf "%02d" "$((10#$nn))")
  n=$((10#$nn))
  theme=$(python3 -c "import yaml;print(yaml.safe_load(open('_data/weeks/woche-$nn.yml'))['theme'])")
  cat > "wochen/woche-$nn.md" <<PAGE
---
layout: week
title: "$n | $theme"
parent: Wochen
nav_order: $n
permalink: /wochen/woche-$nn/
data: woche-$nn
---
PAGE
  # link the calendar row (idempotent)
  python3 - "$n" "$nn" <<'PY'
import re, sys
n, nn = sys.argv[1], sys.argv[2]
p = "_data/calendar.yml"
lines = open(p).read().split("\n")
for i, line in enumerate(lines):
    if re.match(rf"- \{{week: {n},", line) and "page:" not in line:
        lines[i] = line[:-1] + f", page: /wochen/woche-{nn}/}}"
open(p, "w").write("\n".join(lines))
PY
done
