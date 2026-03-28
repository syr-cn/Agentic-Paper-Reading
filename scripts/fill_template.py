#!/usr/bin/env python3
"""
fill_template.py — Fill ResearchClaw HTML templates from JSON data.

Usage:
  python fill_template.py paper-note  data.json  [-o output.html]
  python fill_template.py reading-list data.json [-o output.html]

Data format: JSON with keys matching {{PLACEHOLDER}} names (case-sensitive).
Missing keys are replaced with empty string.
"""
import json, sys, re, argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = REPO_ROOT / "templates" if (REPO_ROOT / "templates").exists() else Path("/tmp/ResearchClaw/templates")

# Also check the cloned repo in workspace
WORKSPACE_TEMPLATE_DIR = Path.home() / ".openclaw/workspace/SYRs-Memory-Paper-Reading/templates"

def find_template_dir():
    for d in [REPO_ROOT / "templates", WORKSPACE_TEMPLATE_DIR, Path("/tmp/ResearchClaw/templates")]:
        if d.exists():
            return d
    raise FileNotFoundError("No template directory found. Clone ResearchClaw first.")

TEMPLATE_MAP = {
    "paper-note": "paper-note.html",
    "reading-list": "reading-list.html",
    "research-profile": "research-profile.html",
}

def fill(template_text: str, data: dict) -> str:
    """Replace all {{KEY}} placeholders with values from data dict."""
    def replacer(m):
        key = m.group(1).strip()
        return str(data.get(key, ""))
    return re.sub(r"\{\{(\w+)\}\}", replacer, template_text)

def main():
    parser = argparse.ArgumentParser(description="Fill ResearchClaw HTML templates from JSON.")
    parser.add_argument("template", choices=list(TEMPLATE_MAP.keys()), help="Template type")
    parser.add_argument("data", help="Path to JSON data file")
    parser.add_argument("-o", "--output", help="Output HTML path (default: stdout)")
    parser.add_argument("--template-dir", help="Override template directory")
    args = parser.parse_args()

    tdir = Path(args.template_dir) if args.template_dir else find_template_dir()
    tpath = tdir / TEMPLATE_MAP[args.template]
    if not tpath.exists():
        print(f"Error: template not found at {tpath}", file=sys.stderr)
        sys.exit(1)

    with open(args.data, "r", encoding="utf-8") as f:
        data = json.load(f)

    template_text = tpath.read_text(encoding="utf-8")
    result = fill(template_text, data)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result, encoding="utf-8")
        print(f"Written to {out}")
    else:
        print(result)

if __name__ == "__main__":
    main()
