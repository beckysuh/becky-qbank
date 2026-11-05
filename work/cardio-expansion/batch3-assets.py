from pathlib import Path
import json
exec(Path('work/cardio-expansion/batch1-assets.py').read_text().split('entries=[')[0])
entries=[
fa('fa-mvp',300,249,322,'Mitral valve prolapse and connective-tissue disorders'),
fa('fa-dcm',318,81,254,'Dilated cardiomyopathy'),
fa('fa-pregnancy',619,65,355,'Pregnancy and maternal physiologic adaptations'),
fa('fa-vf',305,258,322,'Ventricular fibrillation'),
fa('fa-mi-complications',317,65,655,'Myocardial infarction complications'),
fa('fa-shock',320,65,280,'Shock hemodynamics'),
fa('fa-lipid-agents',327,65,750,'Lipid-lowering drugs and mechanisms'),
hy('hy-mvp',[(8,(71,72,524,305.2))],'Mitral valve prolapse'),
hy('hy-s3s4',[(11,(71,110.2,524,416.8))],'S3 versus S4','Pregnancy is included as physiologic high-volume/S3 context.'),
hy('hy-statins',[(41,(71,410.4,524,594.9))],'Statins'),
hy('hy-fibrates',[(41,(71,594,524,669.8))],'Fibrates'),
hy('hy-omega',[(42,(71,269.8,524,283.4))],'Omega/fish oils')
]
assets=dict(entries)
key='hy-septic-review'
assets[key]=dict(title='Mehlman HY Cardio',page='p. 44 · complete septic-shock rapid-review bullet',image=key,alt='Complete unboxed rapid-review bullet linking high CO, low PCWP and low TPR to septic shock',path=parts('hy',[(44,(70,530,524,628))],key))
for key,page,label in [('pharm-fibrates',38,'Fibrates, niacin and omega-3s'),('pharm-statins',36,'Statins')]:
 assets[key]=dict(title='Sketchy and Pixo Pharms',page=f'PDF p. {page} · {label}',image=key,alt=label+' — full mnemonic illustration',path=parts('pharm',[(page,(0,0,1920,1080))],key))
(ROOT/'batch3-assets.json').write_text(json.dumps(assets,indent=2))
print('Prepared',len(assets),'batch-3 reference images')
