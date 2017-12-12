spit slurp
==========

Write text to a file with ``spit`` and read from a file with ``slurp``.

By default files are assumed to be encoded in ``UTF-8``. You can specify an
alternative encoding via the ``encoding`` keyword argument. For a full list of
encodings see `Standard Encodings`.

.. _Standard Encodings: https://docs.python.org/2/library/codecs.html#standard-encodings

Installation
------------

.. code-block:: console

    pip install spitslurp

Usage
-----

.. code-block:: python

    from spitslurp import spit, slurp

    txt = u'Hello\nWorld'

    # Write a unicode string to a file, by default encoded as UTF-8 and
    # truncating the file prior to writing
    spit('path/to/file.txt', txt)

    txt = u'Hello\nLatin1'

    # Append to a file (if it exists) and specify encoding as Latin 1
    spit('path/to/file.txt', txt, append=True, encoding='latin1')

    # Read the entire contents of a file into a unicode string. Assumes the
    # file is in UTF-8 by default
    txt = slurp('path/to/file.txt')

    # Specify an encoding
    txt = slurp('path/to/file.txt', encoding='latin1')

TODO
----

* Moar tests
