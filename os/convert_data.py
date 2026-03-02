import os
import stat
print(stat.filemode(os.stat('.').st_mode))

