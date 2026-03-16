import os 

def scan_dir(path):
    for item in os.listdir(path):
        full = os.path.join(path,item)

        if os.path.isdir(full):
            scan_dir(full)
        else:
            print(full)

scan_dir("/Users/dipayandutta/Developer/python/sde-interview")
