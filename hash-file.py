import io
import sys
import hashlib

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
            for block in read_chunks(f, size=blocksize):
                length += len(block)
                h.update(block)
        return h, length
    return hash_file(path)

path = sys.argv[1]
hash_value, file_size = hash_sum(path)
print("Sha256: ", hash_value.hexdigest())
print("Size:   ", file_size)