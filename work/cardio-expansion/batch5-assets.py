from pathlib import Path
import json
exec(Path('work/cardio-expansion/batch1-assets.py').read_text().split('entries=[')[0])
a=dict([
fa('fa-b1',83,375,750,'Thiamine: wet and dry beriberi'),
fa('fa-b12',86,65,450,'B12 deficiency: anemia and neurologic findings'),
fa('fa-tca',566,430,748,'Tricyclic antidepressants and overdose'),
fa('fa-muscle-coupling',454,65,750,'Skeletal muscle contraction and calcium release'),
fa('fa-congenital-associations',311,65,290,'Congenital cardiac defect associations'),
fa('fa-ms',300,460,530,'Mitral stenosis'),
fa('fa-arch',607,65,395,'Aortic arch derivatives and arterial diagram','Embryologic anatomy context; not a direct statement of the adult carotid route.'),
hy('hy-rhf',[(3,(71,309.8,524,445.0))],'Right heart failure'),
hy('hy-avsd',[(6,(71,725,524,762.7))],'Atrioventricular septal defect'),
hy('hy-ms',[(7,(71,353.3,524,769.2))],'Mitral stenosis'),
hy('hy-as',[(8,(71,561.4,524,757.7)),(9,(71,72,524,109.7))],'Aortic stenosis')
])
k='hy-lipofuscin-review';a[k]=dict(title='Mehlman HY Cardio',page='p. 71 · complete lipofuscin rapid-review bullet',image=k,alt='Complete rapid-review bullet on cardiac aging and lipofuscin',path=parts('hy',[(71,(85,264,524,309))],k))
for key,page,label in [('pharm-tca',79,'Tricyclic antidepressants'),('pharm-cocaine',12,'Indirect sympathomimetics · cocaine')]:
 a[key]=dict(title='Sketchy and Pixo Pharms',page=f'PDF p. {page} · {label}',image=key,alt=label+' · full mnemonic illustration',path=parts('pharm',[(page,(0,0,1920,1080))],key))
(ROOT/'batch5-assets.json').write_text(json.dumps(a,indent=2));print('Prepared',len(a),'images')
