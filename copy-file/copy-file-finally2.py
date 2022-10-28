"""
name: copy-file-fianlly2.py
description: A simple script for copying a file with a progress bar(Use tqdm).
author: hdaojin
version: 1.0.0
creation date: 2022-10-28
last modified: 2022-10-28
usage: python3 copy-file-finally2.py SOURCE DESTINATION
"""

from pathlib import Path
from pydoc import describe
import sys
import io

from tqdm import tqdm


def copy_file(src, dst):
    with open(src, 'rb') as src_obj:
        with open(dst, 'wb') as dst_obj:
            with tqdm(total=Path(src).stat().st_size, unit='B', unit_divisor=1024, desc="Copying", unit_scale=True) as pbar:
                while True:
                    buf = src_obj.read(io.DEFAULT_BUFFER_SIZE)
                    # buf = src_obj.read(1024 * 1024 * 8)
                    dst_obj.write(buf)
                    if len(buf) == 0:
                        break
                    pbar.update(len(buf))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        src = sys.argv[1]
        dst = sys.argv[2]
    else:
        print("Usage: python3 copy-file-finally2.py SOURCE DESTINATION")
        sys.exit(1)

    try :
        copy_file(src, dst)
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)
    else:
        print("copy file:", src, "to", dst, "completed")
