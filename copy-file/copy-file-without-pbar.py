"""
name: copy-file-without-pbar.py
description: A simple script for copying a file.
author: hdaojin
version: 1.0.0
creation date: 2022-05-16
last modified: 2022-10-20
usage: python3 copy-file.py SOURCE DESTINATION
"""
import shutil
import sys

def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
        print("copy file:", src, "to", dst)
    except shutil.SameFileError:
        print("Error: source and destination are the same file")
    except FileNotFoundError:
        print("Error: source file does not exist")
    except PermissionError:
        print("Error: permission denied")
    except:
        print("Error occurred while copying file")
        print("Usage: python3 copy_file.py src_file dst_file")

if __name__ == "__main__":
    try:
        copy_file(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage: python3 copy_file.py src_file dst_file")