"""
name: copy-file-final.py
description: A script for copying a file with a progress bar. Use copyfile() not copyfileobj() because  copyfileobj() has less efficient.
author: hdaojin
version: 1.0.1
creation date: 2022-10-20
last modified: 2022-10-21
usage: python3 copy-file-final.py SOURCE DESTINATION
"""

import shutil
import sys
import time
import threading
from pathlib import Path

from tqdm import tqdm

def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)
    # else:
    #     print(f"File copied successfully from {src} to {dst}")

def tqdm_bar(src, dst):
    with tqdm(total=(Path(src).stat().st_size), unit='B', unit_scale=True, unit_divisor=1024, desc='Copying: ', colour='red') as pbar:
        # pbar.set_description("Progressing: ")
        while True:
            if Path(dst).exists():
                pbar.update(Path(dst).stat().st_size - pbar.n) # pbar.n is number of finished iterations.
                if Path(src).stat().st_size == Path(dst).stat().st_size:
                    break
            time.sleep(0.01)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        src = sys.argv[1]
        dst = sys.argv[2]
    else:
        print("Usage: python3 copy-file-final.py SOURCE DESTINATION")
        sys.exit(1)
    
    try:
        threads = []

        c = threading.Thread(name="copying", daemon=True, target=copy_file, args=(src, dst))
        t = threading.Thread(name="tqdm", daemon=True, target=tqdm_bar, args=(src, dst))

        c.start()
        t.start()

        threads.append(c)
        threads.append(t)

        # The main thread waits for the two threads to complete.
        for x in threads:
            x.join()
        print(f"File copied successfully from {src} to {dst}")

    except KeyboardInterrupt:
        sys.exit(1)
