#!/usr/bin/env python3
"""Read-only structural/traceability validation. Run from any directory with Python + PyYAML."""
from pathlib import Path
from urllib.parse import unquote
import csv, hashlib, json, re, sys, unicodedata, zipfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
errors=[];checks={};links=0;anchors_checked=0
files=sorted(f for f in ROOT.rglob('*') if f.is_file())
def fail(s): errors.append(s)
def unfence(s):
 out=[];fence=None
 for line in s.splitlines():
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   token=m.group(1)
   if fence is None: fence=token
   elif token[0]==fence[0] and len(token)>=len(fence): fence=None
   continue
  if fence is None:out.append(line)
 return '\n'.join(out)
def anchors(s):
 found=set();seen={}
 for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',unfence(s),re.M):
  heading=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',heading).replace('`','')
  slug=''.join(c for c in heading.lower() if c in '_- ' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
  count=seen.get(slug,0);seen[slug]=count+1
  found.add(slug if not count else slug+'-'+str(count))
 found.update(re.findall(r'<a\s+(?:name|id)=[\"\x27]([^\"\x27]+)',s))
 return found
for f in files:
 rel=f.relative_to(ROOT).as_posix()
 if f.is_symlink():fail('symlink '+rel)
 if f.name in ['.DS_Store','Thumbs.db'] or '__MACOSX' in f.parts:fail('metadata '+rel)
 if f.suffix.lower()=='.zip':fail('nested zip '+rel)
 try:s=f.read_text(encoding='utf-8')
 except Exception as e:fail('UTF8 '+rel+': '+type(e).__name__);continue
 if not s.strip():fail('empty '+rel)
 try:
  if f.suffix=='.json':json.loads(s)
  if f.suffix in ['.yaml','.yml']:yaml.safe_load(s)
  if f.suffix=='.csv':
   rows=list(csv.reader(s.splitlines()))
   if not rows or len({len(row) for row in rows})!=1:fail('CSV shape '+rel)
  if f.suffix=='.md':
   for dest in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)',unfence(s)):
    dest=dest.strip('<>')
    if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',dest):continue
    path,_,anchor=dest.partition('#'); target=(f.parent/unquote(path)).resolve() if path else f
    if path.startswith('/'):fail('absolute Markdown target '+rel);continue
    if not target.is_relative_to(ROOT):fail('out-of-root link '+rel);continue
    links+=1
    if not target.exists():fail('missing link '+rel+' -> '+dest);continue
    if anchor and target.suffix=='.md':
     anchors_checked+=1
     if unquote(anchor) not in anchors(target.read_text()):fail('missing anchor '+rel+' -> '+dest)
 except Exception as e:fail('parse '+rel+': '+str(e))
registry=json.loads((ROOT/'10-reference-and-archive/source-register.json').read_text());ids=[x['id'] for x in registry]
if len(ids)!=len(set(ids)):fail('duplicate source IDs')
for item in registry:
 if 'extract' in item and not (ROOT/'10-reference-and-archive'/item['extract']).is_file():fail('missing extract '+item['id'])
claims=yaml.safe_load((ROOT/'10-reference-and-archive/claims.yaml').read_text())['claims']
claim_ids=[x['id'] for x in claims]
if len(claim_ids)!=len(set(claim_ids)):fail('duplicate claim IDs')
for c in claims:
 for sid in c.get('sources',[]):
  if sid not in ids:fail('unregistered claim source '+c['id']+': '+sid)
manifest=yaml.safe_load((ROOT/'manifest.yaml').read_text())
for key in ['source_register','claims_register','coverage','validation','checkpoint','maintenance_sop','consolidation_report']:
 if key in manifest and not (ROOT/manifest[key]).exists():fail('manifest missing '+key)
for n in manifest['canonical_entrypoints']:
 if not (ROOT/n).is_file():fail('entrypoint '+n)
for n in manifest['sections']:
 if not (ROOT/n).is_dir():fail('section '+n)
for f in ROOT.glob('10-reference-and-archive/*.csv'):
 with f.open(newline='') as h:
  rows=list(csv.DictReader(h))
 if f.name=='file-coverage.csv':
  covered=[r['path'] for r in rows]
  expected={x.relative_to(ROOT).as_posix() for x in files}
  if set(covered)!=expected or len(covered)!=len(set(covered)):fail('coverage set does not match files')
 if f.name=='file-disposition.csv':
  for row in rows:
   dest=row.get('final_canonical_destination','')
   for target in dest.split(';'):
    if target and not (ROOT/target).exists():fail('disposition destination '+target)
# Pattern scan prints only count and file names, never matching sensitive text.
patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'\bsk-[A-Za-z0-9]{24,}\b',r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',r'\bAKIA[A-Z0-9]{16}\b']
secret_files=[]
for f in files:
 if f.suffix=='.py':continue
 try: content=f.read_text()
 except UnicodeDecodeError: continue
 if any(re.search(pattern,content) for pattern in patterns):secret_files.append(f.relative_to(ROOT).as_posix())
if secret_files:fail('credential-pattern matches in '+','.join(secret_files))
sums=ROOT/'SHA256SUMS'
if sums.exists():
 entries={}
 for line in sums.read_text().splitlines():
  h,n=line.split('  ',1);entries[n]=h
 expected={f.relative_to(ROOT).as_posix() for f in files if f!=sums}
 if set(entries)!=expected:fail('checksum file set mismatch')
 for n,h in entries.items():
  f=ROOT/n
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:fail('checksum '+n)
else:fail('missing SHA256SUMS')
checks.update(files=len(files),relative_links=links,anchors=anchors_checked,sources=len(ids),claims=len(claims),credential_pattern_matches=len(secret_files))
if len(sys.argv)>1:
 archive=Path(sys.argv[1])
 with zipfile.ZipFile(archive) as z:
  names=z.namelist();wanted={'docs/'+f.relative_to(ROOT).as_posix():f for f in files}
  if z.testzip():fail('ZIP CRC failure')
  if set(names)!=set(wanted) or len(names)!=len(set(names)):fail('ZIP file set/duplicates')
  for n in names:
   if not n.startswith('docs/') or '..' in Path(n).parts or n.startswith('/'):fail('ZIP unsafe path')
   if n in wanted and z.read(n)!=wanted[n].read_bytes():fail('ZIP content mismatch '+n)
 checks['archive_entries']=len(names)
print(json.dumps({'status':'PASS' if not errors else 'FAIL','checks':checks,'errors':errors},indent=2))
sys.exit(bool(errors))
