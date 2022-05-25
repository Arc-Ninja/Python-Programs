from os import rename
from os import walk
newname = 1
files = []
path = "C:\\Users\\Baldeb Shaw\\Documents\\wallpapers"
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break
for name in files:
    try:
        exten = name[-4:]
        rename(f"{path}\\{name}", f"{path}\\{newname}{exten}")
        newname+=1
    except: 
        newname+=1