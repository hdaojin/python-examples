"""
name: copy-file-with-pbar-2.py
description: A simple script for copying a file with a progress bar(Use tqdm).
author: hdaojin
version: 1.0.0
creation date: 2022-05-16
last modified: 2022-10-20
usage: python3 copy-file-with-pbar-2.py SOURCE DESTINATION
"""

from os import path 
import sys
import io

from tqdm import tqdm


if len(sys.argv) == 3:
    if path.isfile(sys.argv[1]) :
        src = sys.argv[1]
        dst = sys.argv[2]
    else:
        print("File does not exist.")
        sys.exit(1)
else:
    print("Usage: python copy_file.py src dst")
    sys.exit(1)

# open() is used to copy the file, and the progress bar is displayed by tqdm.

fsize = int(path.getsize(src))

with open(src, 'rb') as f:
    with open(dst, 'wb') as n:
        # with tqdm(ncols=60, total=fsize, bar_format='{l_bar}{bar} | Remaining: {remaining}') as pbar:
        with tqdm(total=fsize, unit_scale=True) as pbar:
        # ncols: the width of the progress bar
        # total: the number of expected iterations
        # bar_format: the format of the progress bar 
        # unit_scale: automatically adjust the unit of the progress bar for human readability
            while True:
                buf = f.read(io.DEFAULT_BUFFER_SIZE)
                n.write(buf)
                if len(buf) == 0:
                    break
                pbar.update(len(buf))