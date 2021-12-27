import os 
import shutil
import time

"get files which are more than 30 days old"
def getFiles(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            "add file to list if it is more than 30 days old"
            if os.stat(os.path.join(path, file)).st_mtime < (time.time() - 30*24*60*60):            
                files.append(file)
    return files

print(getFiles(os.getcwd()))

