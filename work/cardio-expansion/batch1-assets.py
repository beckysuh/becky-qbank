from pathlib import Path
from PIL import Image
import subprocess,json
ROOT=Path('work/cardio-expansion');OUT=ROOT/'assets';CACHE=ROOT/'pages';OUT.mkdir(exist_ok=True);CACHE.mkdir(exist_ok=True)
PDF={'fa':'/Users/user/Downloads/first-aid-for-the-usmle-step-1-2017.pdf','hy':'/Users/user/Downloads/HY Cardio (1).pdf','pharm':'/Users/user/Downloads/Sketchy and Pixo Pharms.pdf'}
DIMS={'fa':(612,783),'hy':(595,842),'pharm':(1920,1080)}
def render(kind,n):
 p=CACHE/f'{kind}-{n}.png'
 if not p.exists():subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','2000','-png','-singlefile',PDF[kind],str(p.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 return Image.open(p).convert('RGB')
def parts(kind,rects,key):
 ims=[]
 for n,rect in rects:
  im=render(kind,n);w,h=DIMS[kind];scaleX=im.width/w;scaleY=im.height/h
  ims.append(im.crop(tuple(round(v*(scaleX if i%2==0 else scaleY)) for i,v in enumerate(rect))))
 out=Image.new('RGB',(max(im.width for im in ims),sum(im.height for im in ims)+18*(len(ims)-1)),'white');y=0
 for im in ims:out.paste(im,(0,y));y+=im.height+18
 path=OUT/f'{key}.jpg';out.save(path,quality=90,subsampling=0);return str(path)
def fa(key,n,y1,y2,label,context=None):
 return (key,dict(title='First Aid 2017',page=f'p. {n-21} · PDF p. {n} · {label}',image=key,alt=label,context=context or '',path=parts('fa',[(n,(30,y1,590,y2))],key)))
def hy(key,rects,label,context=None):
 nums=list(dict.fromkeys(n for n,_ in rects));pg='p. '+str(nums[0]) if len(nums)==1 else 'pp. '+str(nums[0])+'–'+str(nums[-1]);return (key,dict(title='Mehlman HY Cardio',page=f'{pg} · complete {label} box',image=key,alt=f'Complete {label} box, including all text, labels and figures',context=context or '',path=parts('hy',rects,key)))
entries=[
fa('fa-ccb',325,275,485,'Calcium channel blockers'),
fa('fa-co',293,90,317,'Cardiac output and pulse pressure'),
fa('fa-afterload',294,428,510,'Preload, afterload and hypertrophy'),
fa('fa-oxygen',294,350,430,'Myocardial oxygen demand'),
fa('fa-aging',234,592,750,'Lipofuscin and cellular aging','Related aging context; not a direct statement about cardiomyocyte number.'),
fa('fa-baroreflex',306,210,745,'Baroreceptors and chemoreceptors','Baroreflex physiology; the age-specific change is not stated here.'),
fa('fa-pe',658,65,495,'Pulmonary emboli'),
fa('fa-rhf',319,65,232,'Heart failure'),
fa('fa-pda',310,310,588,'Patent ductus arteriosus'),
fa('fa-flutter',305,190,263,'Atrial flutter','Recognition and ECG; the cavotricuspid anatomy is not specified.'),
fa('fa-beta-agonists',255,68,177,'Sympathomimetics: dobutamine'),
fa('fa-pericarditis',321,310,453,'Acute pericarditis'),
fa('fa-tamponade',321,450,592,'Cardiac tamponade and pulsus paradoxus'),
fa('fa-marfan',69,65,300,'Elastin and Marfan syndrome'),
fa('fa-aneurysm',313,570,650,'Thoracic aortic aneurysm and medial degeneration'),
fa('fa-coronary',292,90,350,'Coronary artery anatomy','Related coronary anatomy; this page does not state the RV-specific systolic/diastolic distinction.'),
fa('fa-dissection',314,65,214,'Aortic dissection'),
fa('fa-digoxin',328,65,405,'Cardiac glycosides: digoxin'),
fa('fa-chagas',175,82,225,'Trypanosoma cruzi: cardiomyopathy and GI dilation'),
hy('hy-nifedipine',[(38,(71,578.2,524,653.1))],'Nifedipine'),
hy('hy-verapamil',[(38,(71,529.0,524,578.8))],'Verapamil'),
hy('hy-hocm',[(27,(71,403.2,524,710.5))],'HOCM','The rate/filling statement appears within the HOCM discussion.'),
hy('hy-beta',[(38,(71,652.6,524,751.5)),(39,(71,72,524,396.6))],'beta-blocker','The slowing-HR/filling relationship appears within the beta-blocker discussion.'),
hy('hy-cor-pulmonale',[(3,(71,518.4,524,751.5)),(4,(71,72,524,195.5))],'cor pulmonale','Related RV afterload/pulmonary-pressure context; not PE-specific.'),
hy('hy-pda',[(9,(71,477.4,524,768.8)),(10,(71,72,524,280.9))],'PDA'),
hy('hy-flutter',[(17,(71,755.3,524,768.8)),(18,(71,72,524,187.8))],'atrial flutter','Recognition and ECG; the cavotricuspid isthmus is not described in this box.'),
hy('hy-dobutamine',[(39,(71,395.8,524,409.2))],'Dobutamine'),
hy('hy-pericarditis',[(22,(71,218.9,524,562.2))],'Pericarditis'),
hy('hy-tamponade',[(23,(71,196.1,524,683.7))],'pericardial effusion / cardiac tamponade'),
hy('hy-dissection',[(13,(71,684,524,746.2)),(14,(71,72,524,545.9))],'aortic dissection'),
hy('hy-digoxin',[(39,(71,470.4,524,581.7))],'Digoxin'),
hy('hy-dcm',[(26,(71,352.1,524,760.6)),(27,(71,72,524,171))],'dilated cardiomyopathy','Chagas is listed as a cause; First Aid supplies the GI-dilation connection.')
]
assets=dict(entries)
for key,page,label in [('pharm-dobutamine',10,'Dobutamine · adrenergic agonists'),('pharm-digoxin',30,'Digoxin · full mnemonic scene'),('pharm-ccb-batch1',24,'Calcium channel blockers · full mnemonic scene')]:
 path=parts('pharm',[(page,(0,0,1920,1080))],key)
 assets[key]=dict(title='Sketchy and Pixo Pharms',page=f'PDF p. {page} · {label}',image=key,alt=label,path=path)
(ROOT/'batch1-assets.json').write_text(json.dumps(assets,indent=2))
print('Prepared',len(assets),'reference images')
