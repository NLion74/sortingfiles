import os
import shutil

path = 'C:/sdd/other/test'
os.system(path[0:2] + " && cd " + path)

images = ["jpg", "jpeg", "png", "raw", "gif", "bmp"]
imagepath = 'C:/sdd/other/test/images'
os.mkdir(imagepath)
os.system(imagepath[0:2] + " && cd " + imagepath)

documents = ["pdf", "xlsx", "pptx", "docx", "txt"]
documentspath = 'C:/sdd/other/test/documents'
os.mkdir(documentspath)
os.system(documentspath[0:2] + " && cd " + documentspath)

tst = 'E:/other'
os.system(tst[0:2] + " && cd " + tst)

list_ = os.listdir(path)

def listext(list, ext):
    for i in range(len(list)):
        if ext == list[i]:
            return ext


# This will go through each and every file
for file_ in list_:
    name, ext = os.path.splitext(file_)

    ext = ext[1:]

    if ext == '':
        continue

    if ext == listext(list=images, ext=ext):
        if os.path.exists(imagepath):
            shutil.move(path + '/' + file_, imagepath + '/' + file_)
        else:
            print(imagepath + 'does not exist')

    elif ext == listext(list=documents, ext=ext):
        if os.path.exists(documentspath):
            shutil.move(path + '/' + file_, documentspath + '/' + file_)
        else:
            print(documentspath + 'does not exist')