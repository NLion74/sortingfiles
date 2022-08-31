import os
import shutil

path = 'drive:/path/to/your/files'
os.system(path[0:2] + " && cd " + path)


documents = ['doc','xls','ppt','odt','ods','pdf','docx','pptx','xlsx','zip','rar','7z','gz','txt']
documentspath = 'drive:/path/to/your/documents'
if os.path.exists(documentspath):
    pass
else:
    os.mkdir(documentspath)
os.system(documentspath[0:2] + " && cd " + documentspath)

images = ['jpg', 'jpeg', 'png', 'raw', 'gif', 'bmp','tif']
imagepath = 'drive:/path/to/your/images'
if os.path.exists(imagepath):
    pass
else:
    os.mkdir(imagepath)
os.system(imagepath[0:2] + " && cd " + imagepath)

videos = ['avi','mkv','mov','mpg','mp4','flv','wmv']
videopath = 'drive:/path/to/your/videos'
if os.path.exists(videopath):
    pass
else:
    os.mkdir(videopath)
os.system(videopath[0:2] + " && cd " + videopath)

music = ['mp3','wma','ogg','wav','aac','m4a']
musicpath = 'drive:/path/to/your/music'
if os.path.exists(musicpath):
    pass
else:
    os.mkdir(musicpath)
os.system(musicpath[0:2] + " && cd " + musicpath)

list_ = os.listdir(path)

def listext(list, ext):
    for i in range(len(list)):
        if ext.lower == list[i]:
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

    elif ext == listext(list=videos, ext=ext):
        if os.path.exists(videopath):
            shutil.move(path + '/' + file_, videopath + '/' + file_)
        else:
            print(videopath + 'does not exist')

    elif ext == listext(list=music, ext=ext):
        if os.path.exists(musicpath):
            shutil.move(path + '/' + file_, musicpath + '/' + file_)
        else:
            print(musicpath + 'does not exist')