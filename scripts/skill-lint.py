#!/usr/bin/env python3
"""Check every public skill and its README prerequisites entry."""
import pathlib,re,json,sys
ROOT=pathlib.Path(__file__).resolve().parent.parent
bad=[];scope=json.loads((ROOT/'publish-scope.json').read_text(encoding='utf-8'))['skills'];skills=[ROOT/'skills'/n/'SKILL.md' for n in sorted(scope)]; names=set()
readme=(ROOT/'README.md').read_text(encoding='utf-8')
headers=[line for line in readme.splitlines() if line.startswith('|') and 'Skill' in line]
if not headers or any('Needs' not in line for line in headers):bad.append('README table missing Needs column')
for p in skills:
 t=p.read_text(encoding='utf-8');name=p.parent.name
 def fail(msg):bad.append(name+': '+msg)
 if len(t.splitlines())>=120:fail('must be under 120 lines')
 if not t.startswith('---\n'):fail('frontmatter missing')
 nm=re.search(r'^name: (.+)$',t,re.M);desc=re.search(r'^description: (.+)$',t,re.M)
 if not nm or nm.group(1)!=name or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',name):fail('name mismatch')
 if not desc or not desc.group(1).startswith('"'):fail('description must be quoted')
 else:
  try:
   value=json.loads(desc.group(1))
   if not value or len(value)>=1024:fail('description length')
  except ValueError:fail('description quoting')
 needs=re.search(r'^Needs: (.+)$',t,re.M)
 if not needs:fail('Needs missing')
 if not re.search(r'\bValid(?:[: ,]|\*\*)',t) or not re.search(r'\bInvalid(?:[: ,]|\*\*)',t):fail('examples missing')
 rows=[line for line in readme.splitlines() if ']('+p.relative_to(ROOT).as_posix()+')' in line]
 if len(rows)!=1 or not needs or needs.group(1) not in rows[0]:fail('README prerequisite coverage mismatch')
 names.add(name)
 for target in re.findall(r'\]\(([^)]+)\)',t):
  if '://' not in target and not (p.parent/target.split('#')[0]).exists():fail('missing reference '+target)
listed=set(re.findall(r'\]\(skills/([^/]+)/SKILL.md\)',readme))
if listed!=names:bad.append('README skill names differ from actual names')
for msg in bad:print(msg)
print(('FAIL' if bad else 'PASS')+f': lint {len(bad)} flags; {len(skills)} skills checked')
sys.exit(bool(bad))
