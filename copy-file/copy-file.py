import shutil
import sys
from os import path

def copy_file(src, dst):
    shutil.copy(src, dst)

if len(sys.argv) == 3:
    if path.isfile(sys.argv[1]): 
        copy_file(sys.argv[1], sys.argv[2])
    else:
        print("File does not exist.")
else:
    print("Usage: python copy_file.py src dst")