"""Refresh the handoff resource index; never rewrites frozen style examples."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent.parent
catalog={}
for path in sorted((root/'work/cardio-expansion').glob('batch*-assets.json')):
 for key,item in json.loads(path.read_text()).items():
  file=root/item['path']
  catalog[key]={**item,'catalogFile':str(path.relative_to(root)),'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
# Include the original seven-question image dependencies, which predate batch catalogs.
import ast
s=(root/'work/assemble-qbank.py').read_text();tree=ast.parse(s)
for node in ast.walk(tree):
 if isinstance(node,ast.Dict):
  try: values=ast.literal_eval(node)
  except (ValueError,TypeError):continue
  if isinstance(values,dict) and values.get('filling')=='outputs/first-aid-filling.png':
   for key,path in values.items():
    f=root/path;catalog.setdefault(key,dict(image=key,path=path,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),catalogFile='work/assemble-qbank.py',provenance='Page/title metadata in the assembler question definitions; original crop scripts in work/.'))
(root/'resources/asset-index.json').write_text(json.dumps(catalog,indent=2)+'\n')
print('Indexed',len(catalog),'local source images')
