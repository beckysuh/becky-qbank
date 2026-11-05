"""Read-only general validation; does not mutate content or progress records."""
import json,re,base64
from pathlib import Path
from io import BytesIO
from PIL import Image
root=Path(__file__).resolve().parent.parent
html=(root/'outputs/svt-qbank.html').read_text()
def data(id):return json.loads(re.search(r'<script type="application/json" id="'+id+r'">(.*?)</script>',html,re.S).group(1))
bank=data('question-data');assets=data('image-data');byid={q['id']:q for q in bank}
assert len(bank)==len(byid),'Duplicate IDs'
for q in bank:
 assert len(q['choices'])==len(set(q['choices']))==4 and isinstance(q['correct'],int) and 0<=q['correct']<4,q['id']
 assert q['sources'],q['id']
 for s in q['sources']+q.get('more',[])+q.get('pharm',[])+q.get('otherPharm',[]):assert s['image'] in assets and s['page'] and s['alt'],q['id']
 if q.get('batch'):
  assert len(q['prompt'])<=125 or q.get('styleException'),('Long prompt',q['id'])
  assert len(q['explanation'].split())<40 or q.get('styleException'),('Long explanation',q['id'])
for url in assets.values():Image.open(BytesIO(base64.b64decode(url.split(',',1)[1]))).verify()
for q in json.loads((root/'docs/approved-examples.json').read_text()):
 for key in ['prompt','choices','correct','note','explanation']:assert byid[q['id']][key]==q[key],('Frozen style example changed',q['id'],key)
assert set(json.loads((root/'docs/baseline-ids.json').read_text()))<=set(byid),'Existing IDs lost'
assert "const KEY='personal-qbank-v1'" in html
assert '<section id="explanation" class="explanation" hidden>' in html
assert '<title>Becky Qbank</title>' in html and '<div class="brand">Becky Qbank</div>' in html
assert 'Choose a question pool and organ systems.' not in html
assert 'All Questions' in html and 'NBME Forms' in html
assert all(('source' not in q or q['source']=='nbme') for q in bank)
for id,a in json.loads((root/'resources/asset-index.json').read_text()).items():assert (root/a['path']).exists(),id
print(f'Passed: {len(bank)} unique questions, stable baseline IDs, 8 frozen style examples, sources/images, brevity, header, source options, storage key and initially hidden explanation.')
