# decompress.py
import sys
from huffman import decompress

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decompress.py <input.huff> <output.txt>")
        sys.exit(1)
    decompress(sys.argv[1], sys.argv[2])
