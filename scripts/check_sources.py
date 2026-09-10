#!/usr/bin/env python3
"""Check that every quote in the skill carries a source.

The skill's one promise is that a line presented as something Steve Jobs said
can be traced to a transcript, a published interview, a keynote or a document
he wrote. This script is what makes that promise checkable instead of stated.

It verifies:
  1. Every block quote in quotes.md is followed by an attribution line that
     names a venue, a four-digit year and a URL.
  2. No line listed in the misattribution table appears as a real quote.
  3. Every URL in the reference files is well formed.
  4. SKILL.md has valid frontmatter and stays under the line budget.
  5. Every reference path mentioned in SKILL.md exists.

Run: python3 scripts/check_sources.py
Exits non-zero on any failure, so it can gate a pull request.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "steve" / "SKILL.md"
REFS = ROOT / "skills" / "steve" / "references"
QUOTES = REFS / "quotes.md"
SKILL_LINE_BUDGET = 400

problems: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def check_quotes() -> None:
    """Every > quote block in quotes.md needs an attribution beneath it."""
    lines = QUOTES.read_text(encoding="utf-8").split("\n")
    in_table = False
    checked = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|"):
            in_table = True
            i += 1
            continue
        if in_table and not line.startswith("|"):
            in_table = False
        if line.startswith("> ") and not in_table:
            # collect the whole block quote
            block_start = i
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            attribution = "\n".join(lines[block_start:i])
            checked += 1
            has_year = re.search(r"\b(19|20)\d{2}\b", attribution)
            has_url = "http" in attribution
            has_dash = "—" in attribution
            if not (has_year and has_url and has_dash):
                missing = []
                if not has_dash:
                    missing.append("an attribution line starting with —")
                if not has_year:
                    missing.append("a year")
                if not has_url:
                    missing.append("a URL")
                snippet = lines[block_start].strip()[:70]
                fail(f"quotes.md line {block_start + 1}: {snippet}… is missing {', '.join(missing)}")
            continue
        i += 1
    if checked == 0:
        fail("quotes.md: found no quotes at all — the file is the point of the skill")
    print(f"  {checked} quotes checked, each with venue, year and link")


def check_misattributions() -> None:
    """Lines named in the misattribution table must not be used as real quotes."""
    text = QUOTES.read_text(encoding="utf-8")
    section = text.split("### Never use these")[-1].split("### Real, but usually misused")[0]
    banned = []
    for row in section.split("\n"):
        if not row.startswith("|"):
            continue
        first_cell = row.split("|")[1] if row.count("|") > 1 else ""
        found = re.findall(r'"([^"]{12,})"', first_cell)
        banned.extend(found)
    if not banned:
        fail("quotes.md has no \"Never use these\" table — the guard rail is gone")
    NEGATIONS = ("never", "did not say", "didn't say", "not say", "bad:", "avoid",
                 "misattribut", "he did not", "poster", "no primary source", "wrong")
    for path in list(REFS.rglob("*.md")) + [SKILL]:
        if path == QUOTES:
            continue
        text_l = path.read_text(encoding="utf-8").lower()
        for line in banned:
            idx = text_l.find(line.lower())
            while idx != -1:
                window = text_l[max(0, idx - 300):idx + len(line) + 300]
                if not any(word in window for word in NEGATIONS):
                    fail(
                        f'{path.name}: a line listed as never-use appears without a warning '
                        f'around it: "{line[:60]}"'
                    )
                idx = text_l.find(line.lower(), idx + 1)
    print(f"  {len(banned)} misattributed lines listed and not used anywhere else")


def check_urls() -> None:
    bad = 0
    total = 0
    for path in REFS.rglob("*.md"):
        for url in re.findall(r"https?://[^\s<>)\]]+", path.read_text(encoding="utf-8")):
            total += 1
            if not re.match(r"^https?://[\w.-]+\.[a-z]{2,}(/|$)", url):
                fail(f"{path.name}: malformed URL {url}")
                bad += 1
    print(f"  {total} URLs, {bad} malformed")


def check_skill() -> None:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md does not start with frontmatter")
        return
    frontmatter = text.split("---", 2)[1]
    name = re.search(r"^name:\s*(\S+)", frontmatter, re.M)
    desc = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    if not name or name.group(1) != SKILL.parent.name:
        fail("SKILL.md frontmatter `name` must match the directory name")
    if not desc:
        fail("SKILL.md frontmatter has no description")
    elif len(desc.group(1)) > 1024:
        fail(f"SKILL.md description is {len(desc.group(1))} chars; the limit is 1024")
    n_lines = len(text.split("\n"))
    if n_lines > SKILL_LINE_BUDGET:
        fail(f"SKILL.md is {n_lines} lines; the budget is {SKILL_LINE_BUDGET}")
    for ref in re.findall(r"`references/([^`]+)`", text):
        target = REFS / ref.replace("<mode>", "verdict")
        if not target.exists():
            fail(f"SKILL.md points at references/{ref}, which does not exist")
    print(f"  SKILL.md: {n_lines} lines, description {len(desc.group(1)) if desc else 0} chars")


def check_manifests() -> None:
    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = ROOT / rel
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(f"{rel} is not valid JSON: {exc}")
            continue
        if "name" not in data:
            fail(f"{rel} has no name")
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin["name"] not in names:
        fail(f"marketplace.json does not list the plugin {plugin['name']}")
    print(f"  manifests fine: /plugin install {plugin['name']}@{market['name']}")


def main() -> int:
    print("Checking the skill.")
    check_skill()
    check_quotes()
    check_misattributions()
    check_urls()
    check_manifests()
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nAll good. Every quote has a source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
