#!/usr/bin/env python3
"""
batch_html.py — Generate all HTML from JSON files in papers/json/ using fill_template.py
Usage: python batch_html.py
"""
import json, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JSON_DIR = REPO / "papers" / "json"
HTML_DIR = REPO / "html" / "papers"
FILL_SCRIPT = REPO / "scripts" / "fill_template.py"

HTML_DIR.mkdir(parents=True, exist_ok=True)

jsons = sorted(JSON_DIR.glob("*.json"))
if not jsons:
    print("No JSON files found in papers/json/")
    sys.exit(1)

ok, fail = 0, 0
for jf in jsons:
    stem = jf.stem  # e.g. 2026-03-23_comp-rl
    out = HTML_DIR / f"{stem}.html"
    try:
        subprocess.run(
            [sys.executable, str(FILL_SCRIPT), "paper-note", str(jf), "-o", str(out)],
            check=True, capture_output=True, text=True
        )
        ok += 1
        print(f"  ✅ {stem}")
    except subprocess.CalledProcessError as e:
        fail += 1
        print(f"  ❌ {stem}: {e.stderr.strip()}")

print(f"\nDone: {ok} OK, {fail} failed out of {len(jsons)}")
