# compress.py
import sys
from huffman import compress

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compress.py <input.txt> <output.huff>")
        sys.exit(1)
    compress(sys.argv[1], sys.argv[2])
