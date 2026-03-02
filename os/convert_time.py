from datetime import datetime
import os

info = os.stat('.')

print("Access time :", datetime.fromtimestamp(info.st_atime))
print("Modify time :", datetime.fromtimestamp(info.st_mtime))
print("Change time :", datetime.fromtimestamp(info.st_ctime))
