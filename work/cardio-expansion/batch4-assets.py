from pathlib import Path
import json
exec(Path('work/cardio-expansion/batch1-assets.py').read_text().split('entries=[')[0])
entries=[
fa('fa-alpha-block',257,65,748,'Alpha blockers and pressor responses'),
fa('fa-sympathomimetics',255,65,650,'Sympathomimetic receptor selectivity'),
fa('fa-hydralazine',325,485,580,'Hydralazine mechanism and adverse effects'),
fa('fa-tr',300,185,251,'Mitral and tricuspid regurgitation'),
fa('fa-bb-tox',330,65,365,'Beta blockers and overdose'),
fa('fa-wound',232,65,447,'Wound healing: type III replaced by type I'),
fa('fa-mi-evolution',315,65,750,'Evolution of myocardial infarction'),
fa('fa-af',305,65,193,'Atrial fibrillation recognition'),
fa('fa-htn-af',311,290,490,'Hypertension and cardiovascular complications'),
hy('hy-niacin',[(42,(71,72,524,183.4))],'Niacin'),
hy('hy-alpha1',[(41,(71,121.4,524,196.6))],'Oxymetazoline / Phenylephrine'),
hy('hy-isoproterenol',[(41,(71,196.1,524,209.8))],'Isoproterenol'),
hy('hy-hydralazine',[(41,(71,285.6,524,323.8))],'Hydralazine'),
hy('hy-tr',[(9,(71,109.2,524,293.3))],'Tricuspid regurgitation'),
hy('hy-af',[(17,(71,84.7,524,755.8))],'Atrial fibrillation')]
a=dict(entries)
k='hy-glucagon-review';a[k]=dict(title='Mehlman HY Cardio',page='p. 62 · complete beta-blocker-overdose rapid-review bullet',image=k,alt='Complete rapid-review bullet: beta-blocker overdose and glucagon',path=parts('hy',[(62,(85,533,524,554))],k))
for key,page,label in [('pharm-alpha1',10,'Adrenergic agonists · phenylephrine and isoproterenol'),('pharm-alpha-block',13,'Alpha blockers · prazosin'),('pharm-beta-block',14,'Beta blockers · glucagon reversal')]:
 a[key]=dict(title='Sketchy and Pixo Pharms',page=f'PDF p. {page} · {label}',image=key,alt=label+' · full illustration',path=parts('pharm',[(page,(0,0,1920,1080))],key))
(ROOT/'batch4-assets.json').write_text(json.dumps(a,indent=2))
print('Prepared',len(a),'reference images')
