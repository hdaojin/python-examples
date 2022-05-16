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
else:
    print("Usage: python copy_file.py src dst")

fsize = int(path.getsize(src))

with open(src, 'rb') as f:
    with open(dst, 'wb') as n:
        with tqdm(ncols=60, total=fsize, bar_format='{l_bar}{bar} | Remaining: {remaining}') as pbar:
            # buffer = bytearray()
            while True:
                # buf = f.read(8192)
                buf = f.read(io.DEFAULT_BUFFER_SIZE)
                n.write(buf)
                if len(buf) == 0:
                    break
                # buffer += buf
                pbar.update(len(buf))