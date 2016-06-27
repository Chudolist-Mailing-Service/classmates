import yaml
import chardet
import codecs

CLASSMATES = [
    {
        'name': 'Громова Дарья',
        'url': 'https://www.facebook.com/gromova.da'
    },
    {
        'name': 'Слободник Алексей',
        'url': 'https://www.facebook.com/markus.duck.90'
    },
    {
        'name': 'Каминский Денис',
        'aff': 'fut.ru',
        'url': 'https://www.facebook.com/dennis.kaminsky.3'
    },
    {
        'name': 'Головизнин Алексей',
        'aff': 'Кант',
        'url': 'https://www.facebook.com/AirVetra'
    },
    {
        'name': 'Кузнецова (Ромашова) Екатерина',
        'aff': 'РФПИ',
        'url': 'https://www.facebook.com/kate.romashova'
    }
]

def loadfile(name, encoding=None, **kwargs):
    with open(name, 'rb') as content_file:
        content = content_file.read()  # type: bytes
        cd = chardet.detect(content)
    enc = encoding or cd.get('encoding', 'ascii')

    return yaml.load(content.decode(enc), **kwargs)


def dumps(data, encoding=None, **kwargs):
    res = yaml.dump(data, **kwargs)
    if encoding:
        return codecs.unicode_escape_decode(res)[0].encode(encoding)
    return res

FB_PREFIX = "https://www.facebook.com/"
classmates = loadfile('classmates.txt')

for i in range(0, len(CLASSMATES)):
    C = CLASSMATES[i]
    try:
        c = classmates[i]
        assert(C.__eq__(c))
    except AssertionError:
        raise Exception('%s is not equal to constant %s' % (c, C))
    except IndexError:
        raise

# currently get an error:  
# yaml.scanner.ScannerError: mapping values are not allowed here
# in "classmates.txt", line 2, column 5
