#!/usr/bin/env python3
"""Lint a folder of skills for structure problems.

Usage:
  python3 lint_skills.py SKILLS_ROOT [--max-kb 15] [--facts FILE] [--retired FILE] [--strict]

Flags:
  SIZE      SKILL.md over --max-kb with no references/ folder
  FACT      a line matches a pattern from --facts (a fact that belongs in one source)
  DUP       the same rule line (40+ chars) in two or more skills
  HISTORY   many dated incident markers in SKILL.md (move them to references/)
  REF       SKILL.md points to a references/ file that does not exist
  RETIRED   SKILL.md names a skill listed as merged or removed in --retired

--facts FILE    one regex per line, optionally followed by a tab and a label.
                Blank lines and lines starting with # are ignored.
--retired FILE  one "old=new" per line (old skill name = where its job lives now).
                Blank lines and lines starting with # are ignored.

Exit code is 1 when anything is flagged and --strict is given, else 0.
"""
import re, sys, pathlib, collections

HISTORY_RE = re.compile(r"\((added|updated|changed) 20\d\d-\d\d-\d\d\)|\bOn 20\d\d-\d\d-\d\d\b", re.I)


def read_lines(path):
    out = []
    for raw in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if raw.strip() and not raw.lstrip().startswith("#"):
            out.append(raw.rstrip("\n"))
    return out


def load_facts(path):
    facts = []
    for line in read_lines(path):
        pat, _, label = line.partition("\t")
        try:
            facts.append((re.compile(pat.strip(), re.I), label.strip() or pat.strip()))
        except re.error as e:
            sys.exit(f"bad regex in {path}: {pat!r} ({e})")
    return facts


def load_retired(path):
    retired = {}
    for line in read_lines(path):
        old, sep, new = line.partition("=")
        if not sep or not old.strip() or not new.strip():
            sys.exit(f"bad line in {path}: {line!r} (expected old=new)")
        retired[old.strip()] = new.strip()
    return retired


def opt(args, name):
    if name in args:
        i = args.index(name)
        if i + 1 >= len(args):
            sys.exit(f"{name} needs a value")
        return args[i + 1]
    return None


def body(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__); sys.exit(2)
    root = pathlib.Path(args[0])
    max_kb = float(opt(args, "--max-kb") or 15)
    facts = load_facts(opt(args, "--facts")) if opt(args, "--facts") else []
    retired = load_retired(opt(args, "--retired")) if opt(args, "--retired") else {}
    strict = "--strict" in args
    skills = sorted(root.glob("*/SKILL.md"))
    flags = []
    lines_seen = collections.defaultdict(set)
    for sk in skills:
        name = sk.parent.name
        text = sk.read_text(encoding="utf-8", errors="replace")
        b = body(text)
        kb = len(text.encode()) / 1024
        if kb > max_kb and not (sk.parent / "references").is_dir():
            flags.append(("SIZE", name, f"{kb:.1f} KB, no references/ folder"))
        for rx, label in facts:
            if rx.search(b):
                flags.append(("FACT", name, f"{label} restated; point to its one source instead"))
        n_hist = len(HISTORY_RE.findall(b))
        if n_hist >= 5:
            flags.append(("HISTORY", name, f"{n_hist} dated incident markers in SKILL.md; move stories to references/"))
        for owner, ref in set(re.findall(r"([\w\-]+/)?(references/[\w.\-]+\.md)", b)):
            target = (root / owner / ref) if owner else (sk.parent / ref)
            if target.exists():
                continue
            if not owner and any((d / ref).exists() for d in root.iterdir() if d.is_dir()):
                flags.append(("REF", name, f"{ref} lives in another skill; name the owner"))
            else:
                flags.append(("REF", name, f"points to {owner or ''}{ref}, which is missing"))
        if name not in retired:
            for old, new in retired.items():
                if new != name and re.search(r"(`|(?<![\w/])/)" + re.escape(old) + r"\b", b):
                    flags.append(("RETIRED", name, f"names `{old}`; it is now `{new}`"))
        for line in b.splitlines():
            s = re.sub(r"[\s*_`>#\-\d.]+", " ", line).strip().lower()
            if len(s) >= 40 and not s.startswith(("valid", "invalid", "related")):
                lines_seen[s].add(name)
    for s, names in lines_seen.items():
        if len(names) > 1:
            flags.append(("DUP", ", ".join(sorted(names)), f'same line: "{s[:80]}"'))
    for kind, name, msg in sorted(flags):
        print(f"{kind:8} {name}: {msg}")
    print(f"\n{len(skills)} skills read, {len(facts)} fact patterns, {len(retired)} retired names, {len(flags)} flags.")
    sys.exit(1 if (flags and strict) else 0)


if __name__ == "__main__":
    main()
