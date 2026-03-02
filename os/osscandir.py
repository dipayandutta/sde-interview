import os

for entry in os.scandir():
    print("Name     :", entry.name)
    print("Path     :", entry.path)
    print("Is file  :", entry.is_file())
    print("Is dir   :", entry.is_dir())
    print("Inode    :", entry.inode())
    print("-" * 40)
