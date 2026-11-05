from pathlib import Path
import json
# Reuse the PDF extraction functions without re-running batch 1.
exec(Path('work/cardio-expansion/batch1-assets.py').read_text().split('entries=[')[0])
entries=[
fa('fa-ischemic-heart',314,220,740,'Ischemic heart disease manifestations','Ischemia/infarction context; the wall-motion term hypokinesis is not used here.'),
fa('fa-hcm',318,254,458,'Hypertrophic cardiomyopathy, histology and outflow obstruction'),
fa('fa-fetal',291,65,500,'Fetal circulation and ductus arteriosus'),
fa('fa-prostaglandins',476,88,510,'Arachidonic acid pathway: TXA2, PGI2, PGE1 and drugs'),
fa('fa-hf-raas',319,65,510,'Heart failure and compensatory RAAS diagram'),
fa('fa-tof',309,419,603,'Tetralogy of Fallot'),
fa('fa-adp',436,322,425,'ADP receptor inhibitors: clopidogrel'),
fa('fa-atherosclerosis',313,65,413,'Atherosclerosis progression and smooth muscle recruitment'),
fa('fa-nitrates',326,65,208,'Nitrates: mechanism and effects'),
fa('fa-capillary',308,65,320,'Capillary fluid exchange and hydrostatic pressure','Related edema mechanism, not a direct CVI-valve or pigmentation passage.'),
fa('fa-circulation',307,40,185,'Normal cardiac pressures and circulation','Related adult circulation framework; equal serial flows are inferred, not explicitly stated.'),
fa('fa-platelets',414,65,267,'Platelet plug formation and pro/anti-aggregation factors'),
fa('fa-thrombolytics',436,180,320,'Thrombolytic drugs and bleeding complications'),
fa('fa-cell-injury',227,65,273,'Cell injury: ATP depletion and pump failure'),
hy('hy-lisinopril',[(40,(71,655.2,524,767.4))],'Lisinopril','The full drug box illustrates inhibition of the RAAS pathway.'),
hy('hy-tof',[(10,(71,280.1,524,429.5))],'Tetralogy of Fallot'),
hy('hy-athero-mechanism',[(28,(71,465.4,524,744.4))],'atherosclerosis mechanism'),
hy('hy-nitrates',[(41,(71,323.3,524,411.3))],'Nitrates'),
hy('hy-venous',[(33,(71,464.2,524,761.9)),(34,(71,72,524,183.8))],'venous disease'),
hy('hy-antiplatelet-context',[(19,(71,347,524,762.4)),(20,(71,72,524,634.5)),(21,(71,72,524,735.3)),(22,(71,72,524,219.8))],'acute MI','The matching aspirin/clopidogrel paragraph is on p. 21; the entire MI box is included.')
]
assets=dict(entries)
for key,page,label in [('pharm-nsaids',40,'NSAIDs · indomethacin and ibuprofen'),('pharm-prostaglandins',46,'Prostaglandins · alprostadil and prostacyclin'),('pharm-antiplatelets',34,'Antiplatelets · clopidogrel and aspirin'),('pharm-nitrates',25,'Nitrates · nitroglycerin'),('pharm-thrombolytics',35,'Fibrinolytics · alteplase')]:
 assets[key]=dict(title='Sketchy and Pixo Pharms',page=f'PDF p. {page} · {label}',image=key,alt=label+' — full mnemonic illustration',path=parts('pharm',[(page,(0,0,1920,1080))],key))
assets['pharm-adenosine-batch2']=dict(title='Sketchy and Pixo Pharms',page='PDF p. 30 · Adenosine',image='pharm-adenosine-batch2',alt='Adenosine — full mnemonic illustration',path='work/pharm-images/adenosine.jpg')
(ROOT/'batch2-assets.json').write_text(json.dumps(assets,indent=2))
print('Prepared',len(assets),'batch-2 reference images')
