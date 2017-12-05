# spitslurp

Write text to a file with `spit` and read from a file with `slurp`.

By default files are assumed to be encoded in UTF-8. You can specify an alternative encoding via the `encoding` keyword argument. For a full list of encodings see [Standard Encodings](https://docs.python.org/2/library/codecs.html#standard-encodings).

## Installation

    pip install spitslurp

## Usage

    from spitslurp import spit, slurp

    # Read the entire contents of a file into a unicode string. Assumes the
    # file is in UTF-8 by default
    txt = slurp('path/to/file.txt')

    # Specify an encoding
    txt = slurp('path/to/file.txt', encoding='latin1')


