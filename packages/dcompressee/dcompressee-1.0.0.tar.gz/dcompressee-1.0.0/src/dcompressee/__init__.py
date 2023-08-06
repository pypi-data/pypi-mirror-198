"""
A small library to return temporary decompressed files when one needs them.

A common use case is when you have a compressed FASTA file and you want to 
run blast against it. Blast will not accept a compressed file, so you need 
to decompress it first. This library will decompress the file into a temporary
file and return the path to that file. The file will automatically be deleted
at the end of you script or if it it unexpectedly terminates.
"""

import os
import atexit
import pathlib
import tempfile
from contextlib import ExitStack


def unpack(input_file: pathlib.Path) -> pathlib.Path:
    """Check if file is compressed and decompress if needed"""

    # Magic numbers to check for various compression formats
    gzip_magic = b"\x1f\x8b\x08"
    bz2_magic = b"BZh"
    lz4_magic = b"\x04\x22\x4d\x18"
    xz_magic = b"\xfd\x37\x7a\x58\x5a\x00"

    # Read the first few bytes of the file to check the magic numbers
    with open(input_file, "rb") as f:
        magic = f.read(6)

    # Check if the file is compressed and decompress if needed
    with ExitStack() as stack:
        if magic.startswith(gzip_magic):
            import gzip

            uncompressed_file = stack.enter_context(
                tempfile.NamedTemporaryFile(delete=False)
            )
            with gzip.open(input_file, "rb") as f:
                uncompressed_file.write(f.read())
            atexit.register(os.unlink, uncompressed_file.name)
            return pathlib.Path(uncompressed_file.name)
        elif magic.startswith(bz2_magic):
            import bz2

            uncompressed_file = stack.enter_context(
                tempfile.NamedTemporaryFile(delete=False)
            )
            with bz2.open(input_file, "rb") as f:
                uncompressed_file.write(f.read())
            atexit.register(os.unlink, uncompressed_file.name)
            return pathlib.Path(uncompressed_file.name)
        elif magic.startswith(lz4_magic):
            import lz4.frame

            uncompressed_file = stack.enter_context(
                tempfile.NamedTemporaryFile(delete=False)
            )
            with open(input_file, "rb") as compressed_file:
                uncompressed_data = lz4.frame.decompress(compressed_file.read())
                uncompressed_file.write(uncompressed_data)
            atexit.register(os.unlink, uncompressed_file.name)
            return pathlib.Path(uncompressed_file.name)
        elif magic.startswith(xz_magic):
            import lzma

            uncompressed_file = stack.enter_context(
                tempfile.NamedTemporaryFile(delete=False)
            )
            with lzma.open(input_file, "rb") as f:
                uncompressed_file.write(f.read())
            atexit.register(os.unlink, uncompressed_file.name)
            return pathlib.Path(uncompressed_file.name)
        else:
            return pathlib.Path(input_file)
