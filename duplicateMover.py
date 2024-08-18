import os
import shutil

files = 'D:\general modding\Python stuff\Duplicate mover\src\\'
# srcpath = r"D:\general modding\Python stuff\Duplicate mover\src"
dest = "D:\general modding\Python stuff\Duplicate mover\output\\"

movedFiles = 0

for filename in os.listdir(files):
    try:
        if filename.endswith(' (1).jpg') or filename.endswith(' (1).mp4'):
            shutil.move(files + filename, dest)
            movedFiles = movedFiles + 1
        # elif filename.endswith(' (1).mp4'):
        #    shutil.move(files + filename, dest)
        #    movedFiles = movedFiles + 1
            
        if movedFiles != 1:
            print(str(movedFiles) + " files have been moved successfully")
        else:
            print(str(movedFiles) + " file have been moved successfully")
    
    except FileExistsError:
        continue
