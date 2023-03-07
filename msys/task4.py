import os
import sys

path = sys.argv[1]
folder_name = sys.argv[2]

folder_path = os.path.join(path, folder_name)

if os.path.isdir(folder_path):
    print("Папка уже существует.")
else:
    os.mkdir(folder_path)
    print("Папка создана.")