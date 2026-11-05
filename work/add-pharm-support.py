from pathlib import Path
p=Path('work/assemble-qbank.py');s=p.read_text()
pos=s.index('# Reference expansion')
s=s[:pos]+'''# Full mnemonic illustrations are matched to drugs in question content.
bank.append(dict(id='cardio-amiodarone-class',system='Cardiovascular',prompt='Amiodarone is primarily classified as which type of antiarrhythmic?',choices=['Class I: sodium channel blocker','Class II: beta blocker','Class III: potassium channel blocker','Class IV: calcium channel blocker'],correct=2,note='K+ channel–blocking antiarrhythmic → <strong>Class III</strong> → amiodarone',noteLabel='APPLICATION OF YOUR CLASS III NOTE',explanation='Amiodarone is primarily a class III potassium channel blocker, prolonging repolarization and the action potential. It also has class I, II, and IV effects.',sources=[source('First Aid 2017','p. 309 · PDF p. 330','fa-amiodarone','Class III antiarrhythmics, including amiodarone mechanism and adverse effects'),source('Mehlman HY Cardio','p. 39','hy-amiodarone','Amiodarone potassium channel blockade, uses, and adverse effects')],more=[]))
pharm_index=[
 dict(terms=['amiodarone'],image='pharm-amiodarone',page=28,label='Amiodarone · Class III antiarrhythmics'),
 dict(terms=['adenosine'],image='pharm-adenosine',page=30,label='Adenosine · full mnemonic scene'),
 dict(terms=['verapamil','diltiazem'],image='pharm-ccb',page=24,label='Verapamil / diltiazem · calcium channel blockers'),
 dict(terms=['furosemide'],image='pharm-furosemide',page=21,label='Furosemide · loop diuretics'),
 dict(terms=['insulin'],image='pharm-insulin',page=56,label='Insulin · full mnemonic scene')
]
for q in bank:
 primary=' '.join([q['prompt'],q['note'],q['explanation'],q['choices'][q['correct']]]).lower()
 options=' '.join(q['choices']).lower()
 q['pharm']=[];q['otherPharm']=[]
 for entry in pharm_index:
  match=any(t in primary for t in entry['terms'])
  if match or any(t in options for t in entry['terms']):
   item=source('Sketchy and Pixo Pharms',f"PDF p. {entry['page']} · {entry['label']}",entry['image'],entry['label']+' — complete original illustration')
   q['pharm' if match else 'otherPharm'].append(item)
''' +s[pos:]
s=s.replace("'hy-wpw':'work/hy-wpw.png'","'hy-wpw':'work/hy-wpw.png','fa-amiodarone':'work/fa-amiodarone.png','hy-amiodarone':'work/hy-amiodarone.png','pharm-amiodarone':'work/pharm-images/amiodarone.jpg','pharm-adenosine':'work/pharm-images/adenosine.jpg','pharm-ccb':'work/pharm-images/calcium-channel-blockers.jpg','pharm-furosemide':'work/pharm-images/furosemide.jpg','pharm-insulin':'work/pharm-images/insulin.jpg'")
s=s.replace("'data:image/png;base64,'+base64", "('data:image/jpeg;base64,' if path.endswith('.jpg') else 'data:image/png;base64,')+base64")
s=s.replace("print('Built standalone", "print('Built standalone")
p.write_text(s)
p=Path('work/qbank-app.js');s=p.read_text();s=s.replace("${q.sources.map(sourceHTML).join('')}","${q.sources.map(sourceHTML).join('')}${(q.pharm||[]).length?'<h2>Drug illustration</h2>'+q.pharm.map(sourceHTML).join(''):''}${(q.otherPharm||[]).length?'<details><summary>Drug illustrations for other answer choices</summary>'+q.otherPharm.map(sourceHTML).join('')+'</details>':''}")
p.write_text(s)
p=Path('work/qbank-shell.html');s=p.read_text().replace('Starter bank: 6 cardiovascular questions.','Starter bank: 7 cardiovascular questions.');p.write_text(s)
