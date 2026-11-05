from pathlib import Path
import json,base64

def source(title,page,image,alt):return dict(title=title,page=page,image=image,alt=alt)
fa=source('First Aid 2017','p. 272 · PDF p. 293','filling','Cardiac output equations and shortened diastolic filling time')
hy=source('Mehlman HY Cardio','pp. 18–19 · complete SVT box','svt','SVT ECG and associated recognition and treatment discussion')
wpw=source('First Aid 2017','p. 283 · PDF p. 304','wpw','WPW accessory pathway, delta wave, and re-entry')
adeno=source('First Aid 2017','p. 310 · PDF p. 331','adenosine','Adenosine mechanism, effects, and adverse effects')
ccb=source('First Aid 2017','p. 310 · PDF p. 331','ccb','Verapamil and diltiazem nodal conduction effects')
k=source('Mehlman HY Cardio','p. 24 · complete Peaked T wave box','hyperk','Hyperkalemia ECG and intravenous calcium for myocardial stabilization')
hy_filling=source('Mehlman HY Cardio','pp. 38–39 · complete beta-blocker box','hy-filling','Slowing heart rate increases diastolic filling time and end-diastolic volume')
hy_filling['context']='From the beta-blocker discussion: the reverse relationship between heart rate and filling time.'
hy_diastole=source('Mehlman HY Cardio','p. 27 · complete HOCM box','hy-diastole','Diastole shortens more than systole as heart rate rises')
hy_diastole['context']='From the HOCM discussion: directly states the effect of heart rate on diastolic duration.'
hy_adenosine=source('Mehlman HY Cardio','pp. 18–19 · complete SVT box','hy-adenosine','SVT treatment progression from vagal maneuvers to adenosine')
hy_adenosine['context']='Treatment context. This passage does not describe the AV nodal mechanism; First Aid above supplies that detail.'
hy_verapamil=source('Mehlman HY Cardio','p. 38 · complete Verapamil box','hy-verapamil','Verapamil acts on nodal calcium channels')
hy_verapamil['context']='Supports the nodal site of action; the explicit PR-interval effect is in First Aid above.'
hy_wpw=source('Mehlman HY Cardio','p. 24 · complete Delta wave box','hy-wpw','WPW accessory pathway bypasses the AV node, with short PR interval and delta wave')
hy_wpw['context']='Supports the accessory pathway and ECG findings; First Aid above names the bundle of Kent.'
more=[hy,wpw,adeno,ccb]
bank=[
dict(id='cardio-svt-filling',system='Cardiovascular',prompt='Why can supraventricular tachycardia (SVT) cause hypotension?',choices=['Increased systemic vascular resistance','Reduced diastolic filling','Increased ventricular compliance','Reduced circulating blood volume'],correct=1,note='Re-entry → SVT → <strong>reduced diastolic filling</strong> → hypotension',explanation='At very fast heart rates, diastole shortens and ventricular filling decreases. The resulting fall in stroke volume can reduce cardiac output and blood pressure.',sources=[fa,hy_filling],more=[hy_diastole,hy,wpw,adeno,ccb]),
dict(id='cardio-rate-diastole',system='Cardiovascular',prompt='As heart rate increases, which part of the cardiac cycle is preferentially shortened?',choices=['Isovolumetric contraction','Ventricular ejection','Diastole','Atrial depolarization'],correct=2,note='SVT → <strong>less time in diastole</strong> → reduced diastolic filling',noteLabel='CONNECTION FROM YOUR SVT NOTE',explanation='Diastole shortens proportionally more than systole as heart rate rises. At very fast rates, less filling time can lower cardiac output.',sources=[fa,hy_diastole],more=[hy_filling]),
dict(id='cardio-adenosine-node',system='Cardiovascular',prompt='Adenosine can terminate certain forms of SVT by slowing conduction through which structure?',choices=['The AV node','The bundle of Kent','Ventricular working myocardium','The left bundle branch'],correct=0,note='AV-node-dependent re-entry → <strong>slower AV nodal conduction</strong> can interrupt the circuit',noteLabel='SUPPLEMENT TO YOUR SVT NOTE',explanation='Adenosine transiently decreases AV nodal conduction. It can terminate SVT when the AV node is required to sustain the re-entry circuit.',sources=[adeno,hy_adenosine],more=[]),
dict(id='cardio-verapamil-pr',system='Cardiovascular',prompt='Verapamil slows AV nodal conduction. What happens to the PR interval?',choices=['It shortens','It becomes absent','It remains unchanged','It lengthens'],correct=3,note='Verapamil → slower AV nodal conduction → <strong>longer PR interval</strong>',noteLabel='CONNECTION TO YOUR PR-LENGTHENING NOTE',explanation='Verapamil and diltiazem are non-dihydropyridine calcium channel blockers. Slower AV nodal conduction increases the PR interval.',sources=[ccb,hy_verapamil],more=[]),
dict(id='cardio-wpw-pathway',system='Cardiovascular',prompt='Which accessory conduction pathway is associated with Wolff-Parkinson-White syndrome?',choices=['Cavotricuspid isthmus','Bundle of Kent','Bachmann bundle','Left anterior fascicle'],correct=1,note='WPW → <strong>bundle of Kent bypasses the AV node</strong> → potential re-entry',noteLabel='SUPPLEMENT TO YOUR RE-ENTRY NOTE',explanation='The bundle of Kent is an accessory atrioventricular pathway. WPW can show a short PR interval and delta wave in sinus rhythm, and the pathway can participate in re-entrant tachycardia.',sources=[wpw,hy_wpw],more=[]),
dict(id='cardio-hyperkalemia-calcium',system='Cardiovascular',prompt='Severe hyperkalemia has caused ECG changes. Which drug directly stabilizes the cardiac membrane?',choices=['Furosemide','Sodium polystyrene sulfonate','Intravenous calcium gluconate','Insulin with glucose'],correct=2,note='Severe hyperkalemia with ECG changes → <strong>calcium gluconate</strong>',explanation='Intravenous calcium stabilizes the myocardium in hyperkalemia with ECG changes. It does not remove potassium or lower its serum concentration.',sources=[k],more=[])
]
# Full mnemonic illustrations are matched to drugs in question content.
bank.append(dict(id='cardio-amiodarone-class',system='Cardiovascular',prompt='Amiodarone is primarily classified as which type of antiarrhythmic?',choices=['Class I: sodium channel blocker','Class II: beta blocker','Class III: potassium channel blocker','Class IV: calcium channel blocker'],correct=2,note='K+ channel–blocking antiarrhythmic → <strong>Class III</strong> → amiodarone',noteLabel='APPLICATION OF YOUR CLASS III NOTE',explanation='Amiodarone is primarily a class III potassium channel blocker, prolonging repolarization and the action potential. It also has class I, II, and IV effects.',sources=[source('First Aid 2017','p. 309 · PDF p. 330','fa-amiodarone','Class III antiarrhythmics, including amiodarone mechanism and adverse effects'),source('Mehlman HY Cardio','p. 39 · complete Amiodarone box','hy-amiodarone','Amiodarone potassium channel blockade, uses, and adverse effects')],more=[]))
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
# Merge resource-checked journal batches using stable IDs.
extra_assets={}
batch_paths=sorted((p for p in Path('work/cardio-expansion').glob('batch*.json') if p.stem.removeprefix('batch').isdigit()),key=lambda p:int(p.stem.removeprefix('batch')))
catalog={}
for batch_path in batch_paths:
 catalog.update(json.loads(batch_path.with_name(batch_path.stem+'-assets.json').read_text()))
def public_source(key):
 return {k:v for k,v in catalog[key].items() if k!='path'}
drug_images=[
 (['nifedipine','verapamil','diltiazem','nimodipine'],'pharm-ccb-batch1'),
 (['dobutamine'],'pharm-dobutamine'),(['digoxin'],'pharm-digoxin'),
 (['indomethacin','ibuprofen','thromboxane'],'pharm-nsaids'),
 (['alprostadil','prostacyclin'],'pharm-prostaglandins'),
 (['clopidogrel','aspirin'],'pharm-antiplatelets'),
 (['nitroglycerin','isosorbide'],'pharm-nitrates'),
 (['alteplase'],'pharm-thrombolytics'),
 (['adenosine'],'pharm-adenosine-batch2'),
 (['fibrates','omega-3','niacin'],'pharm-fibrates'),
 (['statins'],'pharm-statins'),
 (['tca','sodium bicarbonate'],'pharm-tca'),
 (['cocaine'],'pharm-cocaine'),
 (['hydralazine'],'pharm-nitrates'),
 (['phenylephrine','isoproterenol'],'pharm-alpha1'),
 (['prazosin'],'pharm-alpha-block'),
 (['glucagon','beta-blockers'],'pharm-beta-block'),
 (['fibrates','omega-3','niacin'],'pharm-fibrates'),
 (['statins'],'pharm-statins')
]
for batch_path in batch_paths:
 for item in json.loads(batch_path.read_text()):
  q=dict(item)
  q['noteLabel']='YOUR NOTE · JOURNAL PDF P. '+str(q['journalPage'])
  q['sources']=[public_source(key) for key in q.pop('faKeys')+q.pop('hyKeys')]
  drugs=q.pop('drugTerms',[]);other_drugs=q.pop('otherDrugTerms',[])
  main=[key for names,key in drug_images if any(d in drugs for d in names)]
  additional=[key for names,key in drug_images if key not in main and any(d in other_drugs for d in names)]
  q['pharm']=[public_source(key) for key in main]
  q['otherPharm']=[public_source(key) for key in additional]
  old=next((i for i,b in enumerate(bank) if b['id']==q['id']),None)
  if old is None:bank.append(q)
  else:bank[old]=q
for key,v in catalog.items():
 extra_assets[key]='data:image/jpeg;base64,'+base64.b64encode(Path(v['path']).read_bytes()).decode()

# Reference expansion is only relevant to the SVT question family.
assets={name:('data:image/jpeg;base64,' if path.endswith('.jpg') else 'data:image/png;base64,')+base64.b64encode(Path(path).read_bytes()).decode() for name,path in {'filling':'outputs/first-aid-filling.png','svt':'work/hy-svt-full.png','wpw':'work/wpw.png','adenosine':'work/adenosine.png','ccb':'work/ccb.png','hyperk':'work/hyperk.png','hy-filling':'work/hy-filling.png','hy-diastole':'work/hy-diastole.png','hy-adenosine':'work/hy-svt-full.png','hy-verapamil':'work/hy-verapamil.png','hy-wpw':'work/hy-wpw.png','fa-amiodarone':'work/fa-amiodarone.png','hy-amiodarone':'work/hy-amiodarone.png','pharm-amiodarone':'work/pharm-images/amiodarone.jpg','pharm-adenosine':'work/pharm-images/adenosine.jpg','pharm-ccb':'work/pharm-images/calcium-channel-blockers.jpg','pharm-furosemide':'work/pharm-images/furosemide.jpg','pharm-insulin':'work/pharm-images/insulin.jpg'}.items()}
assets.update(extra_assets)
s=Path('work/qbank-shell.html').read_text().replace('BANK_COUNT',str(len(bank))).replace('BANK_PLACEHOLDER',json.dumps(bank).replace('<','\\u003c')).replace('IMAGE_PLACEHOLDER',json.dumps(assets)).replace('APP_PLACEHOLDER',Path('work/qbank-app.js').read_text()+'\n'+Path('work/qbank-progress.js').read_text())
staged=Path('work/qbank-next.html')
staged.write_text(s)
staged.replace('outputs/svt-qbank.html')
Path('work/qbank-data.json').write_text(json.dumps(bank))
print('Built standalone Qbank:',len(bank),'questions;',len(s),'characters')
