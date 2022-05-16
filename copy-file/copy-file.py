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

if __name__ == "__main__":
    try:
        copy_file(sys.argv[1], sys.argv[2])
    except IndexError:
        print("Usage: python copy_file.py src dst")