import os
import shutil

# path of your folder containing duplicate files, needs an extra \, like 'C:\images\\'
files = 'source_path'
# path of your folder where duplicates are being moved to, needs an extra \, like 'C:\images\\'
dest = 'output_path'

movedFiles = 0

for filename in os.listdir(files):
    try:
        if filename.endswith(' (1).jpg') or filename.endswith(' (1).mp4'):
            shutil.move(files + filename, dest)
            movedFiles = movedFiles + 1

        # still prints every string twice if duplicate files are found
        if movedFiles != 1:
            print(str(movedFiles) + " files have been moved successfully")
        else:
            print(str(movedFiles) + " file have been moved successfully")
    
    except FileExistsError:
        continue
