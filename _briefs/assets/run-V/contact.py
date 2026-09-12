import sys,glob
from PIL import Image
d=sys.argv[1]; fs=sorted(glob.glob(d+'/slide-*.png'))
cols=4; tw=480; th=270; rows=(len(fs)+cols-1)//cols
sheet=Image.new('RGB',(cols*tw+(cols+1)*8, rows*th+(rows+1)*8),'#666')
for i,f in enumerate(fs):
    im=Image.open(f).resize((tw,th)); sheet.paste(im,(8+(i%cols)*(tw+8), 8+(i//cols)*(th+8)))
sheet.save(d+'/contact.png'); h=sheet.height//2
sheet.crop((0,0,sheet.width,h)).save(d+'/contact-a.png'); sheet.crop((0,h,sheet.width,sheet.height)).save(d+'/contact-b.png'); print(sheet.size)
