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

from application import get_classmates 

classmates = get_classmates()

for i in range(0, len(CLASSMATES)):
    C = CLASSMATES[i]
    try:
        c = classmates[i]
        assert(C.__eq__(c))
    except AssertionError:
        raise Exception('%s is not equal to constant %s' % (c, C))
    except IndexError:
        raise
