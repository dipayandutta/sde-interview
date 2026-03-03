import os
import csv
from datetime import datetime, timezone

OUTPUT_FILE = "log_report.csv"
TARGET_DIR = "/var/log"

with open(OUTPUT_FILE, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    # Header
    writer.writerow(["Access Time", "Modify Time", "Change Time", "Path"])
    
    with os.scandir(TARGET_DIR) as entries:
        for entry in entries:
            if entry.name.endswith(".log") and entry.is_file(follow_symlinks=False):
                stat = entry.stat(follow_symlinks=False)

                atime = datetime.fromtimestamp(stat.st_atime, timezone.utc)
                mtime = datetime.fromtimestamp(stat.st_mtime, timezone.utc)
                ctime = datetime.fromtimestamp(stat.st_ctime, timezone.utc)

                writer.writerow([atime.isoformat(),
                                 mtime.isoformat(),
                                 ctime.isoformat(),
                                 entry.path])
