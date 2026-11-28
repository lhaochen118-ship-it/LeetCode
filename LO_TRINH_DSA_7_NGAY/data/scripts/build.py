import sys, os, re, json, glob, openpyxl
repo, xlsx, out = sys.argv[1], sys.argv[2], sys.argv[3]
tags = {}
for p in glob.glob(os.path.join(repo, 'solution', '*', '*', 'README_EN.md')):
    d = os.path.basename(os.path.dirname(p))
    m = re.match(r'(\d+)\.(.*)', d)
    if not m: continue
    pid = int(m.group(1))
    txt = open(p, encoding='utf-8').read(4000)
    fm = re.match(r'---\n(.*?)\n---', txt, re.S)
    t, diff, rating, src = [], None, None, None
    if fm:
        body = fm.group(1)
        dm = re.search(r'difficulty:\s*(\w+)', body); diff = dm.group(1) if dm else None
        rm = re.search(r'rating:\s*(\d+)', body); rating = int(rm.group(1)) if rm else None
        sm = re.search(r'source:\s*(.*)', body); src = sm.group(1).strip() if sm else None
        tm = re.search(r'tags:\s*\n((?:\s+-.*\n?)+)', body)
        if tm: t = [x.strip()[1:].strip() for x in tm.group(1).splitlines() if x.strip().startswith('-')]
    tags[pid] = {'title_dir': m.group(2), 'difficulty': diff, 'tags': t, 'rating': rating, 'source': src}
wb = openpyxl.load_workbook(xlsx, read_only=True)
ws = wb['Danh muc DSA']
rows = []
for r in ws.iter_rows(min_row=6, values_only=True):
    if r[2] is None: continue
    pid = int(r[2]); info = tags.get(pid, {})
    rows.append({'id': pid, 'title': r[3], 'difficulty': r[4], 'status': r[5], 'file': r[9],
                 'tags': info.get('tags'), 'doocs_diff': info.get('difficulty'), 'rating': info.get('rating'), 'source': info.get('source')})
json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
missing = [x['id'] for x in rows if x['tags'] is None]
print('rows', len(rows), 'missing tags', len(missing), missing[:20])
print('empty tag lists', sum(1 for x in rows if x['tags'] == []))
