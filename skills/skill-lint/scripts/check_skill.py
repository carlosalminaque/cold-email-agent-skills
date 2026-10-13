#!/usr/bin/env python3
"""Check a SKILL.md (or a folder, or a .skill zip) against the claude.ai save rules.
Usage: python3 check_skill.py <SKILL.md | skill folder | file.skill>
Exit 0 = PASS, 1 = FAIL."""
import re, sys, zipfile, pathlib
p = pathlib.Path(sys.argv[1])
if p.suffix == ".skill":
    z = zipfile.ZipFile(p); names = [n for n in z.namelist() if n.endswith("SKILL.md")]
    text = z.read(names[0]).decode("utf-8") if names else ""
elif p.is_dir():
    text = (p / "SKILL.md").read_text(encoding="utf-8")
else:
    text = p.read_text(encoding="utf-8")
errs = []
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errs.append("no frontmatter block at the top"); fm = ""
else:
    fm = m.group(1)
# strict YAML: some installers (for example npx skills) skip a skill whose frontmatter is not valid YAML,
# such as an unquoted description containing ": ". claude.ai is more lenient, so check strictly here.
try:
    import yaml
    try:
        yaml.safe_load(fm)
    except yaml.YAMLError as e:
        errs.append("frontmatter is not valid strict YAML (quote the description if it contains ': '): " + str(e).splitlines()[0])
except ImportError:
    if re.search(r"^description:[ \t]*(?![ \t\"']).*: ", fm, re.M):
        errs.append("unquoted description contains ': ' (invalid YAML for strict installers); wrap it in double quotes")
name = re.search(r"^name:[ \t]*(.*)$", fm, re.M)
desc = re.search(r"^description:[ \t]*(.*)$", fm, re.M)
if not name: errs.append("missing name")
else:
    n = name.group(1).strip().strip('"\'')
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", n): errs.append(f"name '{n}' must be lowercase letters, digits, hyphens, max 64")
    if "claude" in n or "anthropic" in n: errs.append("name must not contain 'claude' or 'anthropic'")
if not desc: errs.append("missing description")
else:
    d = desc.group(1).strip()
    if len(d) >= 2 and d[0] == d[-1] and d[0] in "\"'":
        d = d[1:-1].replace('\\"', '"')
    if len(d) > 1024: errs.append(f"description is {len(d)} characters (max 1024)")
    if "<" in d or ">" in d: errs.append("description contains < or > (claude.ai reads them as XML tags and refuses to save)")
    if not d: errs.append("description is empty")
print("FAIL\n- " + "\n- ".join(errs) if errs else f"PASS (description {len(d)} chars)")
sys.exit(1 if errs else 0)
