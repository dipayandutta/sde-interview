import os
from datetime import datetime

with os.scandir("/var/log") as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith(".log"):
            file_info = entry.stat()
            atime = datetime.fromtimestamp(file_info.st_atime)
            mtime = datetime.fromtimestamp(file_info.st_mtime)
            ctime = datetime.fromtimestamp(file_info.st_ctime)
            path  = entry.path
            print(f"{atime},{mtime},{ctime},{path}")
            #print(file_info)
            #print(datetime.fromtimestamp(file_info.st_atime),datetime.fromtimestamp(file_info.st_mtime),(entry.path))
            #print(entry.path,datetime.fromtimestamp(entry.st_atime))

'''

from datetime import datetime
import os

info = os.stat('.')

print("Access time :", datetime.fromtimestamp(info.st_atime))
print("Modify time :", datetime.fromtimestamp(info.st_mtime))
print("Change time :", datetime.fromtimestamp(info.st_ctime))
'''
