import io


def spit(path, txt, encoding='UTF-8', append=False):
    """
    Write a unicode string `txt` to file `path`.

    By default encoded as UTF-8 and truncates the file prior to writing

    Parameters
    ----------

    path : str
        File path to file on disk
    txt : unicode
        Text content to write to file
    encoding : str, default `UTF-8`, optional
        Encoding of the file
    append : Boolean, default False
        Append to file instead of truncating before writing

    Returns
    -------

    The txt written to the file as a unicode string
    """
    mode = 'a' if append else 'w'
    with io.open(path, mode, encoding=encoding) as f:
        f.write(txt)
        return txt


def slurp(path, encoding='UTF-8'):
    """
    Reads file `path` and returns the entire contents as a unicode string

    By default assumes the file is encoded as UTF-8

    Parameters
    ----------
    path : str
        File path to file on disk
    encoding : str, default `UTF-8`, optional
        Encoding of the file

    Returns
    -------

    The txt read from the file as a unicode string
    """
    with io.open(path, 'r', encoding=encoding) as f:
        return f.read()
