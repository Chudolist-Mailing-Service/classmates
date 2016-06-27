from yaml import *
import chardet
import codecs


def loadfile(name, encoding=None, **kwargs):
    with open(name, 'rb' ) as content_file:
        content = content_file.read()  # type: bytes
        cd = chardet.detect(content)
    enc = encoding or cd.get('encoding', 'ascii')

    return load(content.decode(enc), **kwargs)


def dumps(data, encoding=None, **kwargs):
    res = dump(data, **kwargs)
    if encoding:
        return codecs.unicode_escape_decode(res)[0].encode(encoding)
    return res

