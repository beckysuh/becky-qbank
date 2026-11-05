"""Copy the verified local Qbank to the GitHub Pages /docs publishing folder."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent.parent
source=root/'outputs/svt-qbank.html'
if not source.exists():raise SystemExit('Build first: python3 work/assemble-qbank.py')
text=source.read_text()
if '<title>Becky Qbank</title>' not in text or 'id="question-data"' not in text:raise SystemExit('Unexpected Qbank artifact')
target=root/'docs/index.html'
target.write_bytes(source.read_bytes())
(root/'docs/.nojekyll').touch()
assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest()
print(f'Prepared docs/index.html: {target.stat().st_size:,} bytes; identical to current local Qbank, including embedded images.')
