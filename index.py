import rawpy
import imageio
import os
# from PIL import Image
from rawpy import _rawpy
filenamelistIM=[]
dirEx="./imageiwza"
dirIm="./Raw file"
extensionEx=".jpg"
if not os.path.exists(dirEx):
    print("Make directory....")
    os.mkdir(dirEx)
    haveExFol=False
else:
    haveExFol=True
print("check file in rawfile")
for x in os.listdir(dirIm):
    if x.endswith(".CR2"):
        filenamelistIM.append(x)
if len(filenamelistIM)==0:
    print("not have file.CR2 in folder")
else:
    filenamelistEX=[]
    if haveExFol:
        print("check file in export directory")
        for x in os.listdir(dirEx):
            if x.endswith(extensionEx):
                filenamelistEX.append(x[:-4]+".CR2")
    filenamelist=[]
    for i in filenamelistIM:
            if not i in filenamelistEX:
                filenamelist.append(i)
    if len(filenamelist)==0:
        print("File have been export yet")
    else:
        print("Converting...")
        finished=0
        for i in filenamelist:
            path=dirIm+"/"+i
            with rawpy.imread(path) as raw:
                rgb = raw.postprocess(use_camera_wb=True,no_auto_bright=True)
            expath=dirEx+"/"+i[:-4]+extensionEx
            # Image.fromarray(rgb).save(expath,quality=100,)
            imageio.imsave(expath, rgb)
            finished+=1
            print(finished,"pic from",len(filenamelist),"pic")
        print("Finished")