#!/usr/bin/env python3
"""Minimal doc-suite validator. Stdlib only. Exit 1 on any finding.

Checks (the cheap, high-value subset — the full traceability matrix stays
deferred per docs/README.md):
  1. Frontmatter: every docs/**/*.md except README.md opens with a valid
     `---` / `status: <skeleton|drafted|reviewed|final>` / `---` block.
  2. Local links: relative markdown links resolve to real files.
  3. Comment balance: every `<!--` has its `-->` (a stray marker means a
     template leaked into real content, or vice versa).
  4. Placeholder leaks: ID placeholders like `F-XXX` outside HTML comments
     in docs whose status is beyond skeleton.
  5. README status drift: index table status vs each doc's frontmatter.
  6. ID references: every `D-NNN` mentioned anywhere exists in the decision
     log index; every `T-NNN` exists in the state-machine doc.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
VALID_STATUSES = {"skeleton", "drafted", "reviewed", "final"}

findings: list[str] = []


def flag(path: Path, msg: str) -> None:
    findings.append(f"{path.relative_to(ROOT)}: {msg}")


def strip_code_fences(text: str) -> str:
    return re.sub(r"^```.*?^```\s*$", "", text, flags=re.S | re.M)


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", strip_code_fences(text), flags=re.S)


def doc_files() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.md") if p.name != "README.md")


def frontmatter_status(path: Path, text: str) -> str | None:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        flag(path, "frontmatter: file does not open with `---`")
        return None
    m = re.match(r"status:\s*(\S+)\s*$", lines[1].strip())
    if not m:
        flag(path, f"frontmatter: line 2 is {lines[1]!r}, expected `status: <value>`")
        return None
    if lines[2].strip() != "---":
        flag(path, "frontmatter: missing closing `---` on line 3")
        return None
    status = m.group(1)
    if status not in VALID_STATUSES:
        flag(path, f"frontmatter: unknown status {status!r}")
        return None
    return status


def check_links(path: Path, text: str) -> None:
    for target in re.findall(r"\]\(([^)]+)\)", strip_comments(text)):
        target = target.split("#")[0].strip()
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (path.parent / target).exists():
            flag(path, f"broken link: ({target})")


def check_comment_balance(path: Path, text: str) -> None:
    text = strip_code_fences(text)
    opens, closes = text.count("<!--"), text.count("-->")
    if opens != closes:
        flag(path, f"unbalanced HTML comments: {opens} `<!--` vs {closes} `-->`")


def check_placeholders(path: Path, text: str, status: str | None) -> None:
    if status in (None, "skeleton"):
        return
    for line_no, line in enumerate(strip_comments(text).splitlines(), 1):
        if re.search(r"\b[A-Z]{1,5}-XXX\b", line):
            flag(path, f"line {line_no}: ID placeholder outside a comment in a {status} doc")


def check_readme_drift(statuses: dict[str, str]) -> None:
    readme = DOCS / "README.md"
    text = readme.read_text(encoding="utf-8")
    for m in re.finditer(r"^\|[^|]*\|\s*\[[^\]]+\]\(([^)]+)\)\s*\|[^|]*\|\s*(\w+)\s*\|", text, re.M):
        target, listed = m.group(1), m.group(2)
        actual = statuses.get(str((DOCS / target).resolve()))
        if actual and listed != actual:
            flag(readme, f"index says {listed!r} for {target}, frontmatter says {actual!r}")


def check_id_refs(texts: dict[Path, str]) -> None:
    decision_log = DOCS / "decision-log.md"
    state_doc = DOCS / "2-domain" / "06-state-machines-and-transitions.md"
    defined_d = set(re.findall(r"###\s+(D-\d{3})\b", texts[decision_log]))
    defined_t = set(re.findall(r"\|\s*(T-\d{3})\s*\|", texts[state_doc]))
    for path, text in texts.items():
        # Strip comments but KEEP code fences: T-refs in the state doc's own
        # mermaid diagram (and any fenced example) must validate too.
        body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        for ref in set(re.findall(r"\bD-\d{3}\b", body)):
            if ref not in defined_d:
                flag(path, f"references {ref}, not defined in decision-log.md")
        for ref in set(re.findall(r"\bT-\d{3}\b", body)):
            if ref not in defined_t:
                flag(path, f"references {ref}, not defined in 06-state-machines-and-transitions.md")


def main() -> int:
    texts = {p: p.read_text(encoding="utf-8") for p in doc_files()}
    statuses: dict[str, str] = {}
    for path, text in texts.items():
        status = frontmatter_status(path, text)
        if status:
            statuses[str(path.resolve())] = status
        check_links(path, text)
        check_comment_balance(path, text)
        check_placeholders(path, text, status)
    check_links(DOCS / "README.md", (DOCS / "README.md").read_text(encoding="utf-8"))
    check_readme_drift(statuses)
    check_id_refs(texts)

    if findings:
        print(f"{len(findings)} finding(s):")
        for f in findings:
            print(f"  {f}")
        return 1
    print(f"OK — {len(texts)} docs checked, no findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
