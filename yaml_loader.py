YAML_SOURCE_FILE = 'classmates.txt'

import yaml
import chardet
import codecs

def loadfile(name, encoding=None):
    """Guess encoding and load yaml data from file."""
    with open(name, 'rb') as content_file:
        content = content_file.read()  # type: bytes
        cd = chardet.detect(content)
    enc = encoding or cd.get('encoding', 'ascii')
    return yaml.load(content.decode(enc))

def dumps(data, encoding=None):
    """Dumps yaml data to file with spcified encoding.""" 
    res = yaml.dump(data)
    if encoding:
        return codecs.unicode_escape_decode(res)[0].encode(encoding)
    return res
