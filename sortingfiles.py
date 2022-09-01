import os
import shutil

path = 'Drive:/path/to/my/files'

documents = ['zip', 'rar', '7z', 'gz', 'txt']
documentspath = 'Drive:/path/to/my/documents'

if os.path.exists(documentspath):
    pass
elif os.path.exists(os.path.dirname(documentspath)):
    pass
    os.mkdir(documentspath)
else:
    os.mkdir(os.path.dirname(documentspath))
    os.mkdir(documentspath)

os.system(documentspath[0:2] + " && cd " + documentspath)

office = ['doc', 'xls', 'ppt', 'odt', 'ods', 'pdf', 'docx', 'pptx', 'xlsx']
officepath = 'Drive:/path/to/my/office'

if os.path.exists(officepath):
    pass
elif os.path.exists(os.path.dirname(officepath)):
    pass
    os.mkdir(officepath)
else:
    os.mkdir(os.path.dirname(officepath))
    os.mkdir(officepath)

os.system(officepath[0:2] + " && cd " + officepath)

images = ['jpg', 'jpeg', 'png', 'raw', 'gif', 'bmp', 'tif']
imagepath = 'Drive:/path/to/my/images'

if os.path.exists(imagepath):
    pass
elif os.path.exists(os.path.dirname(imagepath)):
    pass
    os.mkdir(imagepath)
else:
    os.mkdir(os.path.dirname(imagepath))
    os.mkdir(imagepath)

os.system(imagepath[0:2] + " && cd " + imagepath)

videos = ['avi', 'mkv', 'mov', 'mpg', 'mp4', 'flv', 'wmv']
videopath = 'Drive:/path/to/my/videos'

if os.path.exists(videopath):
    pass
elif os.path.exists(os.path.dirname(videopath)):
    pass
    os.mkdir(videopath)
else:
    os.mkdir(os.path.dirname(videopath))
    os.mkdir(videopath)

os.system(videopath[0:2] + " && cd " + videopath)

music = ['mp3', 'wma', 'ogg', 'wav', 'aac', 'm4a','mka']
musicpath = 'Drive:/path/to/my/music'

if os.path.exists(musicpath):
    pass
elif os.path.exists(os.path.dirname(musicpath)):
    pass
    os.mkdir(musicpath)
else:
    os.mkdir(os.path.dirname(musicpath))
    os.mkdir(musicpath)

os.system(musicpath[0:2] + " && cd " + musicpath)

list_ = os.listdir(path)


def listext(list, ext):
    for i in range(len(list)):
        if ext.lower() == list[i]:
            return ext


# This will go through each and every file
for file_ in list_:
    name, ext = os.path.splitext(file_)

    ext = ext[1:]

    if ext == '':
        continue

    elif ext == listext(list=documents, ext=ext):
        if os.path.exists(documentspath):
            shutil.move(path + '/' + file_, documentspath + '/' + file_)
        else:
            print(documentspath + ' does not exist')

    elif ext == listext(list=office, ext=ext):
        if os.path.exists(officepath):
            shutil.move(path + '/' + file_, officepath + '/' + file_)
        else:
            print(officepath + ' does not exist')

    elif ext == listext(list=images, ext=ext):
        if os.path.exists(imagepath):
            shutil.move(path + '/' + file_, imagepath + '/' + file_)
        else:
            print(imagepath + ' does not exist')

    elif ext == listext(list=videos, ext=ext):
        if os.path.exists(videopath):
            shutil.move(path + '/' + file_, videopath + '/' + file_)
        else:
            print(videopath + ' does not exist')

    elif ext == listext(list=music, ext=ext):
        if os.path.exists(musicpath):
            shutil.move(path + '/' + file_, musicpath + '/' + file_)
        else:
            print(musicpath + ' does not exist')