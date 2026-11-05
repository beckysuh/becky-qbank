from pathlib import Path
from PIL import Image
base=Path('work/pdf-previews')
def crop(page,box):return Image.open(base/f'hy-{page}.png').crop(box)
def save(name,parts):
 width=max(p.width for p in parts);height=sum(p.height for p in parts)+12*(len(parts)-1)
 out=Image.new('RGB',(width,height),'white');y=0
 for part in parts:out.paste(part,(0,y));y+=part.height+12
 out.save('work/'+name+'.png')
save('hyperk',[crop(24,(136,503,995,876))])
save('hy-diastole',[crop(27,(136,766,995,1351))])
save('hy-filling',[crop(38,(136,1240,995,1429)),crop(39,(136,137,995,754))])
save('hy-verapamil',[crop(38,(136,1005,995,1101))])
save('hy-wpw',[crop(24,(136,1199,995,1295))])
save('hy-amiodarone',[crop(39,(136,775,995,849))])
save('hy-svt-full',[crop(18,(136,1158,995,1231)),crop(19,(136,137,995,661))])
p=Path('work/assemble-qbank.py');s=p.read_text().replace("'outputs/mehlman-svt.png'","'work/hy-svt-full.png'").replace("'work/hy-adenosine.png'","'work/hy-svt-full.png'")
s=s.replace("'p. 19','svt'","'pp. 18–19 · complete SVT box','svt'").replace("'p. 19','hy-adenosine'","'pp. 18–19 · complete SVT box','hy-adenosine'").replace("'p. 39','hy-filling'","'pp. 38–39 · complete beta-blocker box','hy-filling'")
s=s.replace("'p. 27','hy-diastole'","'p. 27 · complete HOCM box','hy-diastole'").replace("'p. 24','hyperk'","'p. 24 · complete Peaked T wave box','hyperk'").replace("'p. 38','hy-verapamil'","'p. 38 · complete Verapamil box','hy-verapamil'").replace("'p. 24','hy-wpw'","'p. 24 · complete Delta wave box','hy-wpw'").replace("'p. 39','hy-amiodarone'","'p. 39 · complete Amiodarone box','hy-amiodarone'")
p.write_text(s)
