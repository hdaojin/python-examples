"""
name: copy-file-with-pbar-1.py
description: A simple script for copying a file with a progress bar(Use multithreading).
author: hdaojin
version: 1.0.0
creation date: 2022-05-16
last modified: 2022-10-20
usage: python3 copy-file-with-pbar-1.py SOURCE DESTINATION
"""

import shutil
import sys
import time
import threading
from pathlib import Path

def checker(src, dst):
    while not Path(dst).exists():
        time.sleep(0.01)
        print("waiting for", dst)
    while Path(src).stat().st_size != Path(dst).stat().st_size:
        print(f"percentage: {(Path(dst).stat().st_size / Path(src).stat().st_size) * 100:.2f}%", end='\r', flush=True)
        # "flush=True" is used to flush the screen output.
        time.sleep(0.01)
    # print()
    print("percentage: 100.00%")
    print("copy file:", src, "to", dst, "completed")

def copy_file(src, dst):
    print("copy file:", src, "to", dst)
    shutil.copyfile(src, dst)

if len(sys.argv) == 3:
    if Path(sys.argv[1]).is_file:
        src = sys.argv[1]
        dst = sys.argv[2]
        if Path(dst).exists():
            print("File already exists.")
            sys.exit(1)
    else:
        print("Destiation file does not exist.")
        sys.exit(2)
else:
    print("Usage: python copy_file.py src dst")
    sys.exit(1)

t = threading.Thread(name="copying", target=copy_file, args=(src, dst))
t.start()
# one thread is used to copy the file, and the other thread is used to check the progress of the copy.
b = threading.Thread(name="checking", target=checker, args=(src, dst))
b.start()
