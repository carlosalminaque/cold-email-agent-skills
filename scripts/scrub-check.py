#!/usr/bin/env python3
"""Block a commit or publish if any file holds private data.

Checks every tracked text file for:
  - terms in .scrub-blocklist.txt (local, gitignored: real names, clients, internal IDs)
  - email addresses (except @example.com / @example.org)
  - Windows or home-folder paths
  - long hex IDs, UUIDs, API-key-like strings
  - phone numbers
Exit 1 on any hit. Run from the repo root: python3 scripts/scrub-check.py
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules"}
SKIP_FILES = {".scrub-blocklist.txt", ".scrub-allow.txt"}
# Exact lines allowed on purpose (e.g. the author credit), listed in .scrub-allow.txt.
ALLOW_LINES = {l.strip() for l in (ROOT / ".scrub-allow.txt").read_text().splitlines() if l.strip()} if (ROOT / ".scrub-allow.txt").exists() else set()
PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@(?!example\.(com|org)\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "windows path": re.compile(r"[A-Za-z]:\\\\?[A-Za-z]"),
    "home path": re.compile(r"/(home|Users)/[a-z]", re.I),
    "uuid": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "long hex id": re.compile(r"\b[0-9a-f]{24,}\b", re.I),
    "key-like": re.compile(r"\b(sk|pk|ghp|xox[bap])[-_][A-Za-z0-9_-]{16,}"),
    "phone": re.compile(r"\+?\d[\d\s().-]{8,}\d"),
}

def blocklist():
    f = ROOT / ".scrub-blocklist.txt"
    if not f.exists():
        print("WARN: .scrub-blocklist.txt missing; only generic patterns checked")
        return []
    return [l.strip() for l in f.read_text().splitlines() if l.strip() and not l.startswith("#")]

def main():
    terms = blocklist()
    hits = 0
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir() or p.name in SKIP_FILES or SKIP_DIRS & set(p.parts):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = p.relative_to(ROOT)
        for n, line in enumerate(text.splitlines(), 1):
            if line.strip() in ALLOW_LINES:
                continue
            for t in terms:
                if t.lower() in line.lower():
                    print(f"{rel}:{n}: blocklisted term ({len(t)} chars)"); hits += 1
            for name, rx in PATTERNS.items():
                if rel.as_posix() == "scripts/scrub-check.py":
                    continue
                if rx.search(line):
                    print(f"{rel}:{n}: {name}: {line.strip()[:80]}"); hits += 1
    print(f"{'FAIL' if hits else 'PASS'}: {hits} hits, {len(terms)} blocklisted terms checked")
    sys.exit(1 if hits else 0)

if __name__ == "__main__":
    main()
