# `dcompressee`: a small Python library to generate temporarirly decompressed files

## Background

A common use case in Bioinformatics is having to temporarily decompress a file in
order to run it through some tool. For instance, `blastn` can only read uncompressed
FASTA files. This library provides a simple way to do this. The library will automatically
detect the compression format of the file and decompress it to a temporary file. The
temporary file will be automatically deleted when the program exits. The library 
currently supports the following compression formats: `gzip`, `bzip2`, `xz`, `lz4`, and `lzma`.

## Usage

```python  
from dcompressee import unpack

# A list of file paths as pathlib.Path objects with various compression formats, 
# and some are not compressed
files = ["/path/to/file1.fasta.gz", "/path/to/file2.fasta.bz2", "/path/to/file3.fasta.xz", "/path/to/file4.fasta"]

# Generate a list of paths as pathlib.Path objects to temporarily decompressed 
# files (these will be created in $TMPDIR) if necessary. For files that are not 
# compressed, the function will return the original path. 
# The created temporary files will be automaicallly deleted when the program exits.
paths = [unpack(f) for f in files]

```

## Installation

```bash
pip install dcompressee
```

## Examples

Two examples are provided in the `examples` directory. The first example shows how to
use `dcompressee` in a simple Python script. The second example shows how to use
`dcompressee` in a asynchronous manner.

## Author
Anders Goncalves da Silva (@andersgs)
