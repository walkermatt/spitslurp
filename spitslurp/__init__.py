import io


def spit(path, txt, encoding='UTF-8'):
    """ Writes unicode txt to a file """
    with io.open(path, 'w', encoding=encoding) as f:
        return f.write(txt)


def slurp(path, encoding='UTF-8'):
    """ Reads and returns the entire contents of a file """
    with io.open(path, 'r', encoding=encoding) as f:
        return f.read()
