import os
import sys
from PIL import Image
import shutil
import time
import random
filename0= sys.argv[1]
filename1= sys.argv[2]
filename= sys.argv[3]
shutil.copy2(filename0, 'instagram/')
shutil.copy2(filename1, 'instagram/')
aa = Image.open(filename0).convert("RGB")
bb = Image.open(filename1).convert("RGB")
xx=aa.resize((640,640), Image.NEAREST)
yy=bb.resize((640,640), Image.NEAREST)
xx.save("junk/aa.png")
yy.save("junk/bb.png")
src = Image.open('junk/aa.png').convert('RGB')
dst = Image.open('junk/bb.png').convert('RGB')
src.save("junk/aa.png")
dst.save("junk/bb.png")
n = 5 #number of partitions per channel.
src_handle = Image.open("junk/bb.png")
dst_handle = Image.open("junk/aa.png")
src = src_handle.load()
dst = dst_handle.load()
assert src_handle.size[0]*src_handle.size[1] == dst_handle.size[0]*dst_handle.size[1],"images must be same size"
def makePixelList(img):
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            l.append((x,y))
    return l
lsrc = makePixelList(src_handle)
ldst = makePixelList(dst_handle)
def sortAndDivide(coordlist,pixelimage,channel): #core
    global src,dst,n
    retlist = []
    #sort
    coordlist.sort(key=lambda t: pixelimage[t][channel])
    #divide
    partitionLength = int(len(coordlist)/n)
    if partitionLength <= 0:
        partitionLength = 1
    if channel < 2:
        for i in range(0,len(coordlist),partitionLength):
            retlist += sortAndDivide(coordlist[i:i+partitionLength],pixelimage,channel+1)
    else:
        retlist += coordlist
    return retlist

print(src[lsrc[0]])
lsrc = sortAndDivide(lsrc,src,0)
ldst = sortAndDivide(ldst,dst,0)
for i in range(len(ldst)):
    dst[ldst[i]] = src[lsrc[i]]
dst_handle.save(filename)
shutil.copy2(filename, "instagram/")
print filename