import io
import sys
import hashlib
from pathlib import Path

from tqdm import tqdm

def hash_sum(path):
    def read_chunks(file, size=io.DEFAULT_BUFFER_SIZE):
        """Yield pieces of data from a file-like object until EOF."""
        while True:
            chunk = file.read(size)
            if not chunk:
                break
            yield chunk


    def hash_file(path, blocksize=1 << 20):
        # type: (Text, int) -> Tuple[Any, int]
        """Return (hash, length) for path using hashlib.sha256()
        """
        h = hashlib.sha256()
        length = 0
        with open(path, 'rb') as f:
            with tqdm(total=Path(path).stat().st_size, unit='B', unit_divisor=1024, desc="Hashing", unit_scale=True) as pbar:
                for block in read_chunks(f, size=blocksize):
                    length += len(block)
                    h.update(block)
                    pbar.update(len(block))
        return h, length
    return hash_file(path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 hash-file.py FILE")
        sys.exit(1)

    try :
        hash_value, file_size = hash_sum(path)
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)
    else:
        print("Sha256: ", hash_value.hexdigest())
        print("Size: ", file_size)
