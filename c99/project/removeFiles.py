import os 
import shutil
import time

def getFiles(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if os.stat(os.path.join(path, file)).st_mtime < (time.time() - 30*24*60*60):            
                files.append(file)
    return files

oldfiles = getFiles(os.getcwd())

for path in oldfiles:
    os.remove(path)

print("done! files removed: "+ str(len(oldfiles)))