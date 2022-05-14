import shutil
import sys
import time
import threading
from pathlib import Path

from tqdm import tqdm


def checker(src, dst):
    while not Path(dst).exists():
        time.sleep(1)
        print("waiting for", dst)
    while Path(src).stat().st_size != Path(dst).stat().st_size:
        print("percentage:", (Path(src).stat().st_size / Path(dst).stat().st_size) * 100, "%")
        time.sleep(0.01)
    print("percentage: 100%")

# def copy_file_with_pbar(fsrc, fdst, buffer_size):
#     with tqdm(total=100, desc="Copy file", unit="%", unit_scale=True, leave=True) as pbar:
#         for i in range(1, 101):
#             pbar.update(buffer_size)
#     shutil.copyfileobj(fsrc, fdst, buffer_size)


def copy_file(src, dst):
    print("copy file:", src, "to", dst)
    shutil.copyfile(src, dst)

if len(sys.argv) == 3:
    if Path(sys.argv[1]).is_file:
        src = sys.argv[1]
        dst = sys.argv[2]
    else:
        print("File does not exist.")
else:
    print("Usage: python copy_file.py src dst")

t = threading.Thread(name="copying", target=copy_file, args=(src, dst))
t.start()
b = threading.Thread(name="checking", target=checker, args=(src, dst))
b.start()
