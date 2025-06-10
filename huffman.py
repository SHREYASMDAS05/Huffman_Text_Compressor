# huffman.py
import heapq
import os
from collections import Counter
from typing import Dict, Optional, Tuple

class Node:
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __lt__(self, other: "Node"):
        return self.freq < other.freq

def build_huffman_tree(text: str) -> Node:
    freq_map = Counter(text)
    heap = [Node(ch, fr) for ch, fr in freq_map.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        only = heapq.heappop(heap)
        root = Node(None, only.freq)
        root.left = only
        root.right = Node(None, 0)
        return root

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]

def make_codes(node: Node, prefix: str = "", code_map: Dict[str, str] = None) -> Dict[str, str]:
    if code_map is None:
        code_map = {}
    if node.char is not None:
        code_map[node.char] = prefix or "0"
    else:
        make_codes(node.left, prefix + "0", code_map)
        make_codes(node.right, prefix + "1", code_map)
    return code_map

def pad_encoded_bits(bits: str) -> Tuple[str, int]:
    extra = 8 - len(bits) % 8
    bits += "0" * extra
    return bits, extra

def bits_to_bytes(bitstring: str) -> bytes:
    return bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

def bytes_to_bits(b: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in b)

def compress(input_path: str, output_path: str):
    # 1. Read
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Tree + codes
    root = build_huffman_tree(text)
    code_map = make_codes(root)

    # 3. Encode bits
    bits = "".join(code_map[ch] for ch in text)
    bits, padding = pad_encoded_bits(bits)
    data = bits_to_bytes(bits)

    # 4. Write header + data
    with open(output_path, 'wb') as out:
        out.write(bytes([padding]))
        mapping = "\n".join(f"{ord(ch)}:{code}" for ch, code in code_map.items())
        mb = mapping.encode('utf-8')
        out.write(len(mb).to_bytes(4, 'big'))
        out.write(mb)
        out.write(data)

    # 5. Report sizes & reduction
    orig = os.path.getsize(input_path)
    comp = os.path.getsize(output_path)
    saved = (1 - comp / orig) * 100

    print(f"Compressed {input_path!r} → {output_path!r}")
    print(f"Original size:   {orig} bytes")
    print(f"Compressed size: {comp} bytes")
    print(f"Space saved:     {saved:.2f}%")

def decompress(input_path: str, output_path: str):
    with open(input_path, 'rb') as inp:
        padding = inp.read(1)[0]
        map_len = int.from_bytes(inp.read(4), 'big')
        map_bytes = inp.read(map_len)
        lines = map_bytes.decode('utf-8').splitlines()
        inv_map = {code: chr(num) for num, code in
                   ((int(l.split(':')[0]), l.split(':')[1]) for l in lines)}
        data = inp.read()

    bits = bytes_to_bits(data)
    bits = bits[:-padding]  # remove padding

    # decode
    result = []
    cur = ""
    for b in bits:
        cur += b
        if cur in inv_map:
            result.append(inv_map[cur])
            cur = ""

    with open(output_path, 'w', encoding='utf-8') as out:
        out.write("".join(result))

    print(f"Decompressed {input_path!r} → {output_path!r}")
    print(f"Output size: {os.path.getsize(output_path)} bytes")
