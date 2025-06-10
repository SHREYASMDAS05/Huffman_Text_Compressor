# Huffman Text Compressor

This project implements the Huffman algorithm as a text compressor in **Python**. The Huffman algorithm is renowned for its effective compression techniques, making it ideal for reducing the size of text files while ensuring they remain decompressible.

## Features

* **Effective Compression**: Achieves significant reduction in text file sizes.
* **Maintains Decompressibility**: Ensures that compressed files can be accurately decompressed to their original state.
* **Self-Contained Output**: Stores the code map and padding info in the compressed file, so no external dictionaries are required.

## Performance

### Compression Rates (Example Results)

Below are placeholder results from sample tests on various text files. Replace the values with your actual measurements:

| File Name   | Original Size (bytes) | Compressed Size (bytes) | Compression Rate |
| ----------- | --------------------- | ----------------------- | ---------------- |
| sample1.txt | —                     | —                       | —%               |
| sample2.txt | —                     | —                       | —%               |
| sample3.txt | —                     | —                       | —%               |

### Decompressibility

All compressed files can be decompressed back to their original text without any data loss. (Insert your own checksum or diff-based verification steps here.)

## Implementation Details

The compressor consists of the following Python modules:

* **`huffman.py`**

  * `build_huffman_tree(text)` — Constructs the Huffman tree from character frequencies.
  * `make_codes(node)` — Generates variable-length codes for each character via tree traversal.
  * `compress(input_path, output_path)` — Reads a text file, encodes it, writes a header + compressed bytes, and reports space saved.
  * `decompress(input_path, output_path)` — Reads the compressed file, rebuilds the code map, decodes the bits, and writes the original text.

* **`compress.py`**

  * CLI wrapper: `python compress.py <input.txt> <output.huff>`

* **`decompress.py`**

  * CLI wrapper: `python decompress.py <input.huff> <output_restored.txt>`

## Usage

1. **Clone or download** this repository and navigate into its directory.

2. Ensure **Python 3.7+** is installed.

3. **Compress** a text file:

   ```bash
   python compress.py my_text.txt my_text.huff
   ```

   * **Input**: `my_text.txt` — your original plain-text file
   * **Output**: `my_text.huff` — compressed file containing header + data
   * **Example output**:

     ```
     Compressed 'my_text.txt' → 'my_text.huff'
     Original size:   10240 bytes
     Compressed size:  3567 bytes
     Space saved:      65.17%
     ```

4. **Decompress** to restore the text:

   ```bash
   python decompress.py my_text.huff my_text_restored.txt
   ```

   * **Input**: `my_text.huff`
   * **Output**: `my_text_restored.txt` — should exactly match the original


